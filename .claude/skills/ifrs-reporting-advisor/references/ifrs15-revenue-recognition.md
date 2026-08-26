# IFRS 15 — Revenue from Contracts with Customers

General guidance on applying the five-step revenue model. This is a summary
for practical application, not a replacement for the full standard.

## The Five-Step Model

### Step 1: Identify the contract

A contract exists (for IFRS 15 purposes) once it has commercial substance,
the parties have approved it, each party's rights and payment terms can be
identified, and collection is probable. Verbal or implied contracts count if
they create enforceable rights and obligations under the applicable legal
framework. Combine multiple contracts entered into at/near the same time
with the same customer if they were negotiated as a package, consideration
in one depends on the other, or the goods/services are a single performance
obligation across contracts.

### Step 2: Identify the performance obligations

A performance obligation is a promise to transfer a distinct good or
service. "Distinct" requires both:
- The customer can benefit from the good/service on its own or with readily
  available resources, **and**
- The promise is separately identifiable from other promises in the
  contract (i.e., not so interrelated that it's really one combined output).

Common modeling-relevant cases:
- **SaaS with implementation/onboarding**: onboarding is often *not*
  distinct if it's a setup activity that doesn't transfer a good/service on
  its own — it typically gets bundled into the subscription performance
  obligation and recognized over the subscription term, not upfront.
- **Software + post-contract support (PCS)/updates**: if updates are
  "when-and-if-available" and part of the ongoing service, they're commonly
  combined with the license into a single obligation recognized over time.
- **Free trials, discounts on future purchases, loyalty points**: a
  material right to a future discount is a separate performance obligation
  if it gives the customer a discount they wouldn't get otherwise.

### Step 3: Determine the transaction price

Transaction price is the consideration the entity expects to be entitled to,
adjusted for:
- **Variable consideration** (discounts, rebates, refunds, performance
  bonuses, penalties) — estimated using either the expected value method
  (probability-weighted) or most-likely-amount method, whichever better
  predicts the outcome, and then constrained: only include variable
  consideration to the extent it's *highly probable* a significant
  reversal won't occur once the uncertainty resolves.
- **Significant financing component** — if payment timing and the timing of
  transfer of goods/services diverge enough to provide either party a
  significant financing benefit, adjust the transaction price to the cash
  selling price and recognize interest income/expense separately. A
  practical expedient exists when the gap between payment and transfer is
  one year or less.
- **Non-cash consideration** — measured at fair value.
- **Consideration payable to the customer** — generally reduces the
  transaction price unless it's payment for a distinct good/service the
  customer provides.

### Step 4: Allocate the transaction price

Allocate to each performance obligation based on **relative standalone
selling price (SSP)**. If SSP isn't directly observable, estimate it using
an adjusted market assessment approach, expected cost plus margin, or (in
limited circumstances) a residual approach. Any overall contract discount is
generally spread proportionally across all obligations unless there's
observable evidence the discount relates to only some of them.

### Step 5: Recognize revenue

Recognize revenue when (point in time) or as (over time) the performance
obligation is satisfied — i.e., when control of the good/service transfers
to the customer. A performance obligation is satisfied **over time** if any
one of these is met:
1. The customer simultaneously receives and consumes the benefits as the
   entity performs (e.g., many recurring services).
2. The entity's performance creates or enhances an asset the customer
   controls as it's created (e.g., work-in-progress on customer-owned land).
3. The entity's performance doesn't create an asset with alternative use to
   the entity, **and** the entity has an enforceable right to payment for
   performance completed to date (common for customized/bespoke builds).

If none of these apply, revenue is recognized at the **point in time**
control transfers — using indicators like present right to payment, legal
title, physical possession, risks/rewards of ownership, and customer
acceptance.

## Contract Assets, Contract Liabilities, and Receivables

- **Contract liability (deferred revenue)**: cash received (or due) ahead of
  performance.
- **Contract asset**: performance has occurred but the right to
  consideration is conditional on something other than the passage of time
  (e.g., completing a further milestone) — not yet an unconditional
  receivable.
- **Receivable**: an unconditional right to consideration (only the passage
  of time is required before payment is due).

For a subscription/model build, this maps directly to the standard deferred
revenue roll-forward: opening deferred revenue + billings − revenue
recognized = closing deferred revenue.

## Contract Costs

- **Incremental costs of obtaining a contract** (e.g., sales commissions
  directly tied to signing a specific contract) are capitalized and
  amortized over the period of benefit — often the customer's expected
  life, not just the initial contract term, if renewals are expected and
  the commission on renewal isn't commensurate with the value of the
  incremental service. A practical expedient allows expensing these
  immediately if the amortization period would be one year or less.
- **Costs to fulfill a contract** are capitalized only if they relate
  directly to an identified contract, generate/enhance resources used to
  satisfy future obligations, and are expected to be recovered — otherwise
  expense as incurred.

## Licensing

- **Right to access** IP (the IP's value changes with the licensor's ongoing
  activity, e.g., a brand or technology the licensor keeps updating) →
  revenue recognized **over time**.
- **Right to use** IP as it exists at a point in time (static IP) → revenue
  recognized **at the point in time** the license transfers.

## Principal vs. Agent

If the entity controls the good/service before transferring it to the end
customer, it's the **principal** and recognizes revenue gross. If it's
arranging for another party to provide the good/service, it's an **agent**
and recognizes revenue net (the commission/fee only). Key indicators:
who's primarily responsible for fulfillment, who bears inventory risk, who
has discretion in setting price.

## Modeling Checklist

- [ ] Map each revenue stream to a performance obligation and its
      recognition pattern (point in time vs. over time, and the measure of
      progress if over time — output method or input method)
- [ ] Build the deferred revenue / contract asset roll-forward explicitly,
      don't just plug a revenue number
- [ ] Separately schedule capitalized contract costs (commissions) and their
      amortization if material
- [ ] Flag any variable consideration constraint judgment and its
      sensitivity to the model's revenue line
- [ ] Note any significant financing component adjustment for long-dated or
      prepaid contracts
