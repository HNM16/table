# IFRS vs. US GAAP — Key Differences for Modeling & Reconciliation

High-level divergence points that most often matter when reconciling an
IFRS-basis entity to US GAAP (or vice versa) or building a model that needs
to flex between the two bases. This is not exhaustive — always confirm
against the current standards for a specific fact pattern, since both
frameworks are amended periodically and some gaps (leases, revenue) have
narrowed significantly over time through convergence projects.

| Area | IFRS | US GAAP | Modeling implication |
|---|---|---|---|
| Inventory costing | LIFO **prohibited** (IAS 2) | LIFO **permitted** (ASC 330) | An entity switching from US GAAP LIFO to IFRS must restate to FIFO/weighted-average, which can be a material one-time COGS/inventory adjustment in inflationary periods |
| Inventory write-down reversal | Reversal of a prior write-down is **required** if circumstances that caused it no longer exist, up to the original cost basis | Reversal of a prior write-down is **prohibited** — the written-down amount becomes the new cost basis | IFRS inventory carrying values can bounce back up in a recovery; US GAAP values are a one-way ratchet down |
| Development costs | IAS 38 **requires capitalization** once defined technical/commercial feasibility criteria are met | ASC 730 generally **expenses R&D as incurred**; internal-use/certain software development costs are capitalized under separate, narrower guidance (ASC 350-40/985-20) | IFRS entities often show a development cost intangible and related amortization that a comparable US GAAP entity wouldn't |
| PP&E measurement | IAS 16 allows a **revaluation model** (carry at fair value, with revaluation surplus in OCI) as an accounting policy choice, by class of asset | **Historical cost only** — no revaluation model | If an IFRS entity has elected revaluation, PP&E carrying values and depreciation (based on revalued amounts) won't tie to a historical-cost US GAAP build without adjustment |
| Component depreciation | Required for significant components with materially different useful lives (IAS 16) | Permitted but far less commonly applied as a hard requirement in practice | Can cause different depreciation patterns for the same physical asset even before considering the revaluation difference above |
| Impairment testing (long-lived assets other than goodwill) | IAS 36: **one-step** test — impairment if carrying amount exceeds recoverable amount (higher of fair value less costs of disposal and value in use); **reversal permitted** (except goodwill) if the recoverable amount recovers | ASC 360: historically a **two-step** test for held-and-used long-lived assets (undiscounted cash flow recoverability test, then measure loss); **reversal prohibited** | IFRS impairments can trigger earlier (no undiscounted-cash-flow screen) and can be written back up later; US GAAP impairments, once taken, are permanent |
| Goodwill impairment | IAS 36: single quantitative test comparing a cash-generating unit's (CGU) carrying amount to recoverable amount | ASC 350: qualitative screen optional, then a quantitative test comparing a reporting unit's fair value to carrying amount | Different unit of account (CGU, which can be smaller than a US GAAP reporting unit) means goodwill impairment can be triggered at a more granular level under IFRS |
| Leases | IFRS 16: **single lessee model**, all leases (except short-term/low-value) capitalized; expense = depreciation + interest, front-loaded | ASC 842: dual lessee model retained — **finance leases** look like IFRS 16; **operating leases** are capitalized too, but total expense is recognized **straight-line** | Even for the identical lease, the P&L expense pattern for an operating-type lease differs: front-loaded under IFRS 16 vs. straight-line under ASC 842 |
| Provisions / contingent liabilities | IAS 37: recognize a provision when an outflow is **probable** (commonly applied as "more likely than not," i.e., >50%) and reliably estimable | ASC 450: recognize when a loss is **probable**, a term applied in US practice as a notably higher bar than a bare 50% threshold, and reasonably estimable | IFRS entities can end up provisioning for contingencies somewhat earlier/more readily than a US GAAP entity would for a similar fact pattern — treat this as a directional, practice-based tendency rather than a precisely defined numeric rule under either framework |
| Extraordinary items | Presenting items as "extraordinary" is **prohibited** (IAS 1) | Also eliminated from US GAAP (ASU 2015-01) — historically a difference, now converged | No longer a live difference for current-period reporting, but relevant when comparing to pre-2015 US GAAP filings |
| Financial statement titles | Commonly "statement of financial position," "statement of profit or loss and other comprehensive income" | "Balance sheet," "income statement" (titles are not prescribed terms under either framework, but these are the conventional usages) | Cosmetic, but relevant when mapping line items between a GAAP-labeled model and IFRS-labeled statutory accounts |
| Classified balance sheet & debt covenant breaches | IAS 1: a covenant breach without a **waiver obtained by the reporting date** forces current classification of the related debt | ASC 470: similar current-classification consequence for a breach, though the specific relief conditions (e.g., grace periods before the reporting date) differ in detail | Check both the breach date and the exact waiver-timing rule under the applicable framework before classifying debt as long-term |
| NCI / business combinations | IFRS 3 allows an **election** (full goodwill vs. proportionate share) for measuring NCI, made per acquisition | ASC 805 generally requires NCI at **fair value** (full goodwill approach) with no proportionate-share option | An IFRS acquirer electing proportionate-share NCI will show lower goodwill and lower NCI than the same deal modeled under US GAAP |
| Interest and dividends in the cash flow statement | IAS 7 allows **classification flexibility** — interest/dividends paid or received can be operating, investing, or financing, as long as applied consistently | ASC 230 is more prescriptive — interest paid/received and dividends received are operating; dividends paid are financing | Cash flow statement subtotals (operating cash flow especially) may not be directly comparable without reclassifying to a common basis |

## Practical Reconciliation Approach

1. Start from the IFRS (or US GAAP) profit/loss and equity as reported.
2. Walk each row of the table above that's relevant to the entity's actual
   transactions (most entities won't hit all of them) and quantify the
   adjustment.
3. Keep a bridge schedule (starting balance → each named adjustment →
   ending balance) rather than a single net plug, so each adjustment can be
   reviewed and updated independently as facts change.
4. Tax-effect each adjustment where it would create or eliminate a
   temporary difference under the target framework's tax accounting
   (IAS 12 vs. ASC 740) — the tax effect is often as significant as the
   pre-tax adjustment itself.
