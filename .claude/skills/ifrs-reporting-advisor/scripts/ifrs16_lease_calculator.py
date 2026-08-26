#!/usr/bin/env python3
"""
IFRS 16 Lease Calculator

Computes the initial lease liability and right-of-use (ROU) asset for a
lessee under IFRS 16, then builds the full period-by-period amortization
schedule (effective-interest liability roll-forward + straight-line ROU
depreciation).

Uses standard library only (math, json, argparse) - NO numpy/pandas.

Usage:
    python ifrs16_lease_calculator.py lease_data.json
    python ifrs16_lease_calculator.py lease_data.json --format json

Input JSON shape (see SKILL.md / references/ifrs16-leases.md for the
underlying accounting):

{
  "lease": {
    "description": "HQ office lease",
    "payment_amount": 10000,
    "num_payments": 60,
    "periods_per_year": 12,
    "payment_timing": "arrears",       // "arrears" or "advance"
    "annual_discount_rate": 0.06,
    "payment_escalation_rate": 0.02,   // optional, default 0
    "escalation_every_periods": 12     // optional, default = periods_per_year
  },
  "initial_direct_costs": 5000,
  "prepayments": 0,
  "lease_incentives": 20000,
  "restoration_costs": 15000,
  "depreciation_periods": null        // optional override; default = num_payments
}
"""

import argparse
import json
import sys
from typing import Any, Dict, List


def periodic_rate_from_annual(annual_rate: float, periods_per_year: int) -> float:
    """Convert a nominal annual discount rate to an equivalent periodic rate."""
    if periods_per_year <= 0:
        raise ValueError("periods_per_year must be positive")
    return (1.0 + annual_rate) ** (1.0 / periods_per_year) - 1.0


def build_payment_schedule(
    payment_amount: float,
    num_payments: int,
    escalation_rate: float = 0.0,
    escalation_every_periods: int = 12,
) -> List[float]:
    """Build the list of lease payments, applying periodic escalation."""
    payments: List[float] = []
    current = payment_amount
    for i in range(num_payments):
        if i > 0 and escalation_rate and escalation_every_periods > 0 and i % escalation_every_periods == 0:
            current *= 1.0 + escalation_rate
        payments.append(current)
    return payments


def present_value(payments: List[float], rate: float, timing: str = "arrears") -> float:
    """PV of a payment stream, either as an ordinary annuity (arrears) or annuity-due (advance)."""
    pv = 0.0
    for i, payment in enumerate(payments):
        period = i if timing == "advance" else i + 1
        pv += payment / ((1.0 + rate) ** period)
    return pv


def build_liability_schedule(
    initial_liability: float, payments: List[float], rate: float, timing: str = "arrears"
) -> List[Dict[str, float]]:
    """Effective-interest amortization schedule for the lease liability."""
    schedule: List[Dict[str, float]] = []
    opening = initial_liability

    for i, payment in enumerate(payments):
        if timing == "advance":
            balance_after_payment = opening - payment
            interest = balance_after_payment * rate
            closing = balance_after_payment + interest
        else:
            interest = opening * rate
            closing = opening + interest - payment

        schedule.append(
            {
                "period": i + 1,
                "opening_liability": round(opening, 2),
                "interest_expense": round(interest, 2),
                "payment": round(payment, 2),
                "closing_liability": round(closing, 2),
            }
        )
        opening = closing

    return schedule


def build_rou_schedule(rou_initial: float, depreciation_periods: int) -> List[Dict[str, float]]:
    """Straight-line ROU asset depreciation schedule."""
    if depreciation_periods <= 0:
        raise ValueError("depreciation_periods must be positive")

    per_period = rou_initial / depreciation_periods
    schedule: List[Dict[str, float]] = []
    opening = rou_initial

    for i in range(depreciation_periods):
        # Final period absorbs any rounding residual so the closing balance is exactly zero.
        depreciation = per_period if i < depreciation_periods - 1 else opening
        closing = opening - depreciation
        schedule.append(
            {
                "period": i + 1,
                "opening_rou": round(opening, 2),
                "depreciation": round(depreciation, 2),
                "closing_rou": round(closing, 2),
            }
        )
        opening = closing

    return schedule


def run_lease_calculation(data: Dict[str, Any]) -> Dict[str, Any]:
    lease = data.get("lease", {})

    payment_amount = lease.get("payment_amount")
    num_payments = lease.get("num_payments")
    annual_rate = lease.get("annual_discount_rate")

    if payment_amount is None or num_payments is None or annual_rate is None:
        raise ValueError(
            "lease.payment_amount, lease.num_payments, and lease.annual_discount_rate are required"
        )

    periods_per_year = lease.get("periods_per_year", 12)
    timing = lease.get("payment_timing", "arrears")
    if timing not in ("arrears", "advance"):
        raise ValueError('lease.payment_timing must be "arrears" or "advance"')

    escalation_rate = lease.get("payment_escalation_rate", 0.0)
    escalation_every = lease.get("escalation_every_periods", periods_per_year)

    rate = periodic_rate_from_annual(annual_rate, periods_per_year)
    payments = build_payment_schedule(payment_amount, num_payments, escalation_rate, escalation_every)

    initial_liability = present_value(payments, rate, timing)

    initial_direct_costs = data.get("initial_direct_costs", 0.0)
    prepayments = data.get("prepayments", 0.0)
    lease_incentives = data.get("lease_incentives", 0.0)
    restoration_costs = data.get("restoration_costs", 0.0)

    rou_initial = (
        initial_liability
        + initial_direct_costs
        + prepayments
        - lease_incentives
        + restoration_costs
    )

    depreciation_periods = data.get("depreciation_periods") or num_payments

    liability_schedule = build_liability_schedule(initial_liability, payments, rate, timing)
    rou_schedule = build_rou_schedule(rou_initial, depreciation_periods)

    total_interest = sum(row["interest_expense"] for row in liability_schedule)
    total_depreciation = sum(row["depreciation"] for row in rou_schedule)
    total_payments = sum(payments)
    final_liability = liability_schedule[-1]["closing_liability"] if liability_schedule else 0.0

    return {
        "description": lease.get("description", ""),
        "periodic_discount_rate": round(rate, 6),
        "initial_lease_liability": round(initial_liability, 2),
        "initial_rou_asset": round(rou_initial, 2),
        "total_cash_payments": round(total_payments, 2),
        "total_interest_expense": round(total_interest, 2),
        "total_depreciation_expense": round(total_depreciation, 2),
        "final_liability_balance": final_liability,
        "liability_schedule": liability_schedule,
        "rou_schedule": rou_schedule,
    }


def format_text(results: Dict[str, Any]) -> str:
    lines: List[str] = []
    lines.append("=" * 70)
    title = results.get("description") or "IFRS 16 Lease Calculation"
    lines.append(title)
    lines.append("=" * 70)
    lines.append(f"Periodic discount rate:      {results['periodic_discount_rate'] * 100:.4f}%")
    lines.append(f"Initial lease liability:     {results['initial_lease_liability']:,.2f}")
    lines.append(f"Initial ROU asset:           {results['initial_rou_asset']:,.2f}")
    lines.append(f"Total cash payments:         {results['total_cash_payments']:,.2f}")
    lines.append(f"Total interest expense:      {results['total_interest_expense']:,.2f}")
    lines.append(f"Total depreciation expense:  {results['total_depreciation_expense']:,.2f}")
    lines.append(f"Final liability balance:     {results['final_liability_balance']:,.2f}  (should be ~0)")
    lines.append("")
    lines.append(f"{'Per.':>4}  {'Open Liab':>12}  {'Interest':>10}  {'Payment':>10}  {'Close Liab':>12}  {'Depr.':>10}  {'Close ROU':>12}")

    rou_by_period = {row["period"]: row for row in results["rou_schedule"]}
    for row in results["liability_schedule"]:
        rou = rou_by_period.get(row["period"], {"depreciation": 0.0, "closing_rou": 0.0})
        lines.append(
            f"{row['period']:>4}  {row['opening_liability']:>12,.2f}  {row['interest_expense']:>10,.2f}  "
            f"{row['payment']:>10,.2f}  {row['closing_liability']:>12,.2f}  {rou['depreciation']:>10,.2f}  "
            f"{rou['closing_rou']:>12,.2f}"
        )

    lines.append("=" * 70)
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="IFRS 16 Lease Calculator - lease liability and ROU asset amortization schedule"
    )
    parser.add_argument("input_file", help="Path to JSON file with lease data")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )

    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{args.input_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{args.input_file}': {e}", file=sys.stderr)
        sys.exit(1)

    try:
        results = run_lease_calculation(data)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.format == "json":
        print(json.dumps(results, indent=2))
    else:
        print(format_text(results))


if __name__ == "__main__":
    main()
