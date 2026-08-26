# IFRS 9 — Financial Instruments

Covers classification & measurement, impairment (expected credit losses),
and a brief overview of hedge accounting.

## Classification & Measurement of Financial Assets

A debt-type financial asset is classified based on two tests:

1. **Business model test** — is the asset held to collect contractual cash
   flows, held both to collect and to sell, or held for another purpose
   (e.g., trading)?
2. **SPPI test** — do the contractual cash flows represent **S**olely
   **P**ayments of **P**rincipal and **I**nterest on the principal amount
   outstanding (i.e., basic lending-type cash flows, where "interest"
   compensates for time value of money, credit risk, and basic lending
   costs/margin — not equity-like or leveraged returns)?

Resulting categories:

| Business model | Passes SPPI? | Classification |
|---|---|---|
| Hold to collect | Yes | **Amortized cost** |
| Hold to collect and sell | Yes | **FVOCI** (fair value through OCI) with recycling to P&L on derecognition |
| Anything else (trading, etc.) | — | **FVTPL** (fair value through profit or loss) |
| Any model | No (fails SPPI) | **FVTPL** regardless of business model |

Equity investments are measured at **FVTPL** by default, unless the entity
makes an irrevocable election at initial recognition to present fair value
changes in OCI (FVOCI for equities) — in which case gains/losses are
**never recycled** to P&L, even on sale (only dividend income hits P&L
normally). This is a one-time, instrument-by-instrument election.

Financial liabilities are mostly measured at **amortized cost**, with FVTPL
reserved for held-for-trading liabilities, derivatives, and liabilities
designated at FVTPL under the fair value option (subject to conditions).
For liabilities designated at FVTPL, changes in fair value attributable to
the entity's own credit risk generally go to OCI (not P&L), to avoid the
counter-intuitive result of recognizing a gain when the entity's own
creditworthiness deteriorates.

## Expected Credit Loss (ECL) Model

IFRS 9 replaced the old "incurred loss" impairment model with a
**forward-looking expected credit loss** model — losses are recognized
before an actual default event occurs, based on reasonable and supportable
information about future conditions.

### General (three-stage) approach

| Stage | Trigger | Measurement basis |
|---|---|---|
| Stage 1 | No significant increase in credit risk since initial recognition | 12-month ECL (losses from default events possible within 12 months) |
| Stage 2 | Significant increase in credit risk since initial recognition, but not yet credit-impaired | Lifetime ECL |
| Stage 3 | Credit-impaired (objective evidence of default/impairment) | Lifetime ECL, and interest revenue calculated on the net (impaired) carrying amount |

"Significant increase in credit risk" is assessed relative to risk at
initial recognition (not an absolute risk level) — commonly operationalized
with a mix of quantitative triggers (e.g., days past due, often with a
rebuttable presumption around 30 days past due as a backstop indicator) and
qualitative triggers (watchlist status, covenant breach, rating downgrade).

### Simplified approach

For **trade receivables, contract assets (IFRS 15), and lease receivables**
without a significant financing component, entities apply (or, for those
with a significant financing component, may elect to apply) the simplified
approach: always measure the loss allowance at an amount equal to
**lifetime ECL**, no staging required. In practice this is commonly
implemented as a **provision matrix** — historical loss rates by aging
bucket, adjusted for current conditions and forward-looking factors (macro
outlook, industry trends).

### ECL Calculation Building Blocks

```
ECL = Probability of Default (PD)
    x Loss Given Default (LGD)
    x Exposure at Default (EAD)
```

Discounted back to the reporting date at the instrument's effective interest
rate (or an approximation of it) when the timing of expected shortfalls
extends beyond a short period.

## Reclassification

Financial assets are reclassified only when the entity **changes its
business model** for managing those assets — this is expected to be rare
and applies prospectively from the reclassification date (no restatement of
prior gains/losses/interest already recognized).

## Hedge Accounting (Overview)

Three hedge types:
- **Fair value hedge** — hedges exposure to changes in fair value of a
  recognized asset/liability or firm commitment. Gain/loss on the hedging
  instrument and the hedged item's fair value change (attributable to the
  hedged risk) both go to P&L, largely offsetting.
- **Cash flow hedge** — hedges exposure to variability in cash flows from a
  recognized item or highly probable forecast transaction. The effective
  portion of the hedging instrument's gain/loss goes to OCI (a hedging
  reserve) and is reclassified to P&L when the hedged item affects P&L;
  ineffective portion goes to P&L immediately.
- **Net investment hedge** — hedges currency exposure on a net investment in
  a foreign operation; accounted for similarly to a cash flow hedge.

To qualify for hedge accounting, there must be: an economic relationship
between the hedged item and hedging instrument, credit risk not dominating
the value changes from that economic relationship, and a hedge ratio
consistent with actual risk management (not artificially inflated to
minimize ineffectiveness). IFRS 9's hedge accounting model is more
principles-based and easier to qualify for than the old IAS 39 bright-line
80-125% effectiveness test, though entities may still elect to keep applying
IAS 39's hedge accounting requirements instead of IFRS 9's.

## Modeling Checklist

- [ ] Classify each material financial asset (amortized cost / FVOCI /
      FVTPL) — this determines whether fair value moves hit P&L, OCI, or
      neither
- [ ] For receivables, build a provision matrix by aging bucket rather than
      a single flat bad-debt %, and revisit it each period for
      forward-looking adjustments
- [ ] For loans/debt instruments held to collect, model the effective
      interest rate amortization of any premium/discount/fees, not just the
      coupon rate
- [ ] If hedge accounting is applied, keep the OCI hedging reserve as its
      own roll-forward line, separate from other OCI items
