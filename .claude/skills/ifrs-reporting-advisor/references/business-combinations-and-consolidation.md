# IFRS 3 / IFRS 10 / IFRS 11 — Business Combinations, Consolidation & Joint Arrangements

Guidance for M&A modeling (purchase price allocation) and group reporting.

## IFRS 3 — Business Combinations

### Is it a business combination?

First confirm the acquired set of activities/assets meets the definition of
a **business** (an integrated set of activities and assets capable of being
conducted and managed to provide a return, e.g., dividends or lower costs,
directly to investors/owners) rather than just an **asset acquisition**. If
it's an asset acquisition, there's no goodwill — the purchase price is
allocated to the individual assets/liabilities based on relative fair value,
and transaction costs are capitalized (vs. expensed for a business
combination).

### The Acquisition Method

1. **Identify the acquirer** — the entity that obtains control (per IFRS 10
   principles). In a "reverse acquisition," the legal acquirer may be the
   accounting acquiree.
2. **Determine the acquisition date** — the date control transfers, not
   necessarily the closing/signing date.
3. **Recognize and measure identifiable assets acquired, liabilities
   assumed, and any non-controlling interest (NCI)** — generally at
   **acquisition-date fair value**, including intangible assets that the
   target may not have recognized on its own books (customer relationships,
   trade names, developed technology, backlog, etc., if they meet the
   separability or contractual-legal recognition criteria).
4. **Recognize goodwill or a bargain purchase gain**:
   ```
   Goodwill = Consideration transferred
            + NCI (measured per the elected method below)
            + Fair value of any previously held equity interest (step acquisitions)
            − Net identifiable assets acquired at fair value
   ```
   If the result is negative, it's a **bargain purchase** — reassess the
   valuation first (this is unusual and often signals a measurement error),
   and if confirmed, recognize the gain immediately in P&L.

### NCI Measurement Election

For each business combination, elect (instrument-by-instrument at the
acquisition level, not entity-wide) to measure NCI at:
- **Proportionate share of the acquiree's identifiable net assets**
  (no goodwill allocated to NCI), or
- **Fair value** (the "full goodwill" method — goodwill is grossed up to
  include the portion attributable to NCI, not just the parent's share).

This election changes the goodwill figure and the NCI equity balance, but
not the parent's own share of goodwill.

### Measurement Period

Provisional amounts recognized at the acquisition date can be adjusted
retrospectively (with a corresponding goodwill adjustment) during the
**measurement period** — up to one year from the acquisition date — as new
information about facts and circumstances existing at the acquisition date
comes to light. Changes due to events *after* the acquisition date are not
measurement-period adjustments; they go through P&L instead.

### Contingent Consideration

Measured at acquisition-date fair value and included in consideration
transferred. Classified as a liability (or asset) generally remeasured
through P&L each period, or as equity (not remeasured), based on its terms.

## IFRS 10 — Consolidated Financial Statements

### The Control Model

An investor controls an investee when it has **all three**:
1. **Power** over the investee (existing rights that give the current
   ability to direct the relevant activities — the activities that
   significantly affect the investee's returns),
2. **Exposure, or rights, to variable returns** from its involvement with
   the investee, and
3. **The ability to use its power** to affect the amount of the investor's
   returns (the link between power and returns).

Ownership of a majority of voting rights is a strong indicator but not the
only path to control — control can also arise from contractual arrangements
(e.g., structured entities), potential voting rights that are currently
exercisable, or de facto control (a large minority stake where the rest is
widely dispersed, historically sufficient to direct outcomes).

### Consolidation Mechanics

- Combine the parent's and each subsidiary's financial statements line by
  line, eliminate intercompany balances/transactions/unrealized profits,
  and present NCI separately within equity (not as a liability or
  mezzanine item).
- A subsidiary is included in consolidation from the date control is
  obtained until the date control is lost — partial periods are common in
  the year of acquisition/disposal.
- Uniform accounting policies are applied across the group; a subsidiary's
  financial statements are adjusted to the group's policies before
  consolidation if they differ.

## IFRS 11 — Joint Arrangements

Classify a joint arrangement (jointly controlled by two or more parties
under a contractual arrangement) as either:
- **Joint operation** — the parties have rights to the assets and
  obligations for the liabilities of the arrangement. Each party recognizes
  its **own share of assets, liabilities, revenue, and expenses** directly
  (not equity-accounted).
- **Joint venture** — the parties have rights to the **net assets** of the
  arrangement. Accounted for using the **equity method** (per IAS 28), not
  proportionate consolidation (proportionate consolidation for joint
  ventures was eliminated).

Classification depends on the legal structure, contractual terms, and (for
arrangements structured through a separate vehicle) other facts and
circumstances — a separate legal vehicle is a strong but not automatic
indicator of joint venture classification.

## IFRS 12 — Disclosure of Interests in Other Entities

Requires disclosure sufficient for users to evaluate the nature of, and
risks associated with, interests in subsidiaries, joint arrangements,
associates, and unconsolidated structured entities — including significant
judgments made in determining control/joint control/significant influence,
and the nature/extent of any significant restrictions on accessing group
assets or settling group liabilities.

## PPA (Purchase Price Allocation) Modeling Checklist

- [ ] Confirm business vs. asset acquisition first — it changes goodwill,
      deferred tax, and transaction-cost treatment entirely
- [ ] Build a fair value schedule for every identifiable intangible
      (customer relationships, trade names, technology, non-competes,
      backlog) with its own useful life and amortization method, not a
      single blended intangible line
- [ ] Recognize deferred tax on the fair value step-ups (the tax base
      usually doesn't change even though the accounting carrying amount
      does), which itself affects goodwill
- [ ] State the NCI measurement election used and its effect on goodwill
- [ ] Track the measurement-period window separately from post-acquisition
      P&L items so true-ups don't get mis-recorded
- [ ] For consolidation, schedule intercompany eliminations (balances,
      unrealized profit in inventory/PP&E) as their own roll-forward, not a
      single plug
