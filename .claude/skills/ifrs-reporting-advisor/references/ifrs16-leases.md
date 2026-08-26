# IFRS 16 — Leases

General guidance for lessee accounting (the case that shows up in financial
models most often). Lessor accounting is covered briefly at the end.

## The Core Model

IFRS 16 uses a **single on-balance-sheet model for lessees**: with narrow
exceptions, every lease results in a right-of-use (ROU) asset and a lease
liability on the balance sheet. There is no separate "operating lease"
category for lessees the way there was under the old IAS 17 model — the only
big-picture exceptions are:

- **Short-term leases**: lease term of 12 months or less at commencement,
  with no purchase option — can be expensed straight-line instead of
  capitalized (elected by class of underlying asset).
- **Low-value assets**: leases of assets that are low value when new (the
  standard doesn't fix a number, but low-value is generally understood as
  roughly the price range of items like laptops, small office furniture, or
  phones — assessed on an absolute basis, not relative to the lessee's
  size) — can also be expensed straight-line, elected lease-by-lease.

## Identifying a Lease

A contract is (or contains) a lease if it conveys the right to control the
use of an identified asset for a period of time in exchange for
consideration. "Control" here means the customer has both the right to
obtain substantially all the economic benefits from use of the asset **and**
the right to direct how and for what purpose the asset is used during the
period. If the supplier has substantive substitution rights over the asset,
or the contract is really just a service where the supplier operates the
asset and decides how it's used, it's not a lease.

## Determining the Lease Term

Lease term = the non-cancellable period, plus:
- Periods covered by an option to extend, if the lessee is **reasonably
  certain** to exercise it, and
- Periods covered by an option to terminate, if the lessee is **reasonably
  certain not** to exercise it.

"Reasonably certain" is a high threshold — consider contractual, economic,
and business-specific factors (e.g., significant leasehold improvements,
importance of the location to the business, cost of relocating).

## Initial Measurement

**Lease liability** = present value of lease payments not yet paid at
commencement, discounted using:
- The interest rate implicit in the lease, if readily determinable; otherwise
- The lessee's **incremental borrowing rate (IBR)** — the rate the lessee
  would have to pay to borrow, over a similar term and with similar
  security, the funds needed to obtain an asset of similar value in a
  similar economic environment.

Lease payments included: fixed payments (less any lease incentives
receivable), variable payments that depend on an index or rate (initially
measured using the index/rate at commencement), amounts expected under
residual value guarantees, exercise price of a purchase option the lessee is
reasonably certain to exercise, and termination penalties if the lease term
reflects exercising a termination option. Purely usage-based variable
payments (e.g., a percentage of sales) are **excluded** from the liability
and expensed as incurred.

**Right-of-use asset**, at cost, comprising:
```
ROU asset = Initial lease liability
          + lease payments made at or before commencement
          + initial direct costs incurred by the lessee
          - lease incentives received
          + estimate of costs to dismantle/remove/restore
            (if the lessee has that obligation, per IAS 37 principles)
```

## Subsequent Measurement

**Lease liability** — effective interest method:
```
Interest expense (period) = Opening liability balance x periodic discount rate
Closing liability balance = Opening balance + interest - cash payment made
```
This front-loads the interest expense (higher early, declining as the
balance amortizes), which is a key reason total lease expense recognized
under IFRS 16 is *not* straight-line even when cash payments are level.

**ROU asset** — depreciated on a systematic basis (usually straight-line)
from the commencement date to the earlier of the end of its useful life or
the end of the lease term. If ownership transfers at the end of the lease,
or a purchase option is reasonably certain to be exercised, depreciate over
the asset's useful life instead. Also test for impairment under IAS 36
rather than a leases-specific impairment model.

**P&L pattern**: expense = depreciation (straight-line) + interest
(declining) — combined, this produces a total expense that is higher in
early periods and lower in later periods, even though cash rent is flat.
This differs from a straight-line "single lease cost" pattern.

## Reassessment and Modifications

Remeasure the lease liability (with an offsetting adjustment to the ROU
asset) when:
- The lease term changes (reassessed exercise of extension/termination
  options),
- A residual value guarantee amount changes,
- An index- or rate-based payment resets (remeasure using the new
  rate/index, discount rate generally unchanged unless the liability itself
  changes due to a rate-dependent variable lease payment structure),
- The scope of the lease changes without a separate contract being created
  (a **modification**) — if the modification decreases scope, recognize a
  gain/loss for the decrease; if it increases scope at a price not
  commensurate with standalone price, remeasure using a revised discount
  rate.

A modification that both adds a right of use for one or more underlying
assets **and** increases consideration by an amount commensurate with the
standalone price for the increase is accounted for as a **separate new
lease**, not a remeasurement.

## Sale-and-Leaseback

Assess first whether the "sale" leg qualifies as a sale under IFRS 15
(control transfer). If yes, the seller-lessee recognizes a ROU asset for the
portion of the asset it retains use of (not the full previous carrying
amount) and only recognizes gain/loss on the rights transferred to the
buyer. If the transfer doesn't qualify as a sale, both parties account for
it as a financing arrangement instead (no sale, no leaseback lease — the
"seller" keeps the asset and recognizes a financial liability).

## Lessor Accounting (Brief)

Unlike lessees, lessors still classify each lease as **finance** or
**operating**, using criteria carried over from the old IAS 17 model
(substantially all risks/rewards of ownership transferred = finance lease).
Finance leases: derecognize the asset, recognize a net investment in the
lease receivable, recognize finance income over the lease term. Operating
leases: keep the underlying asset on the lessor's balance sheet, recognize
lease income (typically straight-line) over the lease term.

## Modeling Checklist

- [ ] Confirm discount rate basis (implicit rate vs. IBR) and document it —
      this is usually the single biggest driver of the initial liability
- [ ] Build the full period-by-period liability roll-forward (opening +
      interest − payment = closing), not just an amortization shortcut
- [ ] Depreciate the ROU asset separately from the liability schedule —
      they diverge over time even though they start equal (net of any
      initial direct costs/incentives)
- [ ] Exclude short-term/low-value leases from the balance-sheet schedule
      but keep their straight-line expense in the model
- [ ] Flag any options (renewal, termination, purchase) where the
      "reasonably certain" judgment materially changes the lease term
- [ ] Use `scripts/ifrs16_lease_calculator.py` for the actual schedule
      instead of computing period-by-period by hand
