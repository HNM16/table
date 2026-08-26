---
name: ifrs-reporting-advisor
description: >
  Guidance on IFRS (International Financial Reporting Standards) financial
  reporting and how it feeds into financial modeling: revenue recognition
  (IFRS 15), leases (IFRS 16), financial instruments and expected credit
  losses (IFRS 9), business combinations and consolidation (IFRS 3/10/11),
  and statement presentation (IAS 1). Use when preparing IFRS-basis
  financial statements, adjusting a financial model for IFRS treatment,
  reconciling IFRS results to US GAAP, or classifying/measuring a lease,
  revenue contract, financial instrument, or acquisition under IFRS.
metadata:
  version: 1.0.0
  category: finance
  domain: financial-reporting
  tags: [ifrs, financial-reporting, accounting-standards, revenue-recognition, leases, financial-instruments, gaap-comparison, consolidation]
---

# IFRS Reporting Advisor

Helps apply IFRS recognition, measurement, and presentation requirements to a
real transaction or financial model, and translates the accounting treatment
into concrete model mechanics (schedules, roll-forwards, journal-level logic).

**Important scope note:** This skill gives practitioner-level, general
guidance distilled from how the standards are commonly applied. It is not a
reproduction of the authoritative IFRS Standards text, is not a substitute
for reading the current standard/interpretation in full, and is not audit or
legal advice. Standards are amended periodically (new/amended IFRSs, IFRIC
interpretations) — for a transaction with real financial statement impact,
confirm the current text with the entity's auditors or the IFRS Foundation's
official material before finalizing a position.

## Clarify First

Before giving a conclusion or building a schedule, confirm what's actually
being asked. If unknown, ASK — do not assume:

- [ ] **Which standard/transaction** — revenue contract, lease, financial
      instrument, business combination, or general presentation question
      (routes to the right reference file and checklist)
- [ ] **Reporting context** — first-time IFRS adopter (IFRS 1 territory) vs.
      ongoing IFRS reporter vs. GAAP reporter wanting an IFRS comparison
- [ ] **Purpose** — statutory financial statements, a financial model that
      needs to reflect IFRS mechanics, a GAAP-to-IFRS reconciliation, or a
      policy-election decision
- [ ] **Materiality/precision needed** — a ballpark treatment for modeling
      vs. a position that will go into audited statements (the latter needs
      professional sign-off, not just this skill)

Stop rule: ask only the 1-2 questions that change the answer. If the user
says "just apply the standard treatment," proceed with the most common
policy choice and state the assumption explicitly.

## Workflow

1. **Classify the transaction** — identify which standard governs (see the
   table below) and confirm it isn't scoped out by a more specific standard
   (e.g., a lease of intangible IP may fall under IAS 38, not IFRS 16).
2. **Apply recognition & measurement** — walk the relevant reference file's
   steps/tests, using the entity's actual facts (discount rate, contract
   terms, payment schedule, etc.), not generic placeholders.
3. **Flag judgment areas** — standards embed estimates and policy choices
   (discount rate selection, useful life, ECL staging, NCI measurement
   method). List each one explicitly so it can be reviewed/approved rather
   than silently assumed.
4. **Translate into model mechanics** — if the output feeds a financial
   model, build the actual schedule (lease liability roll-forward, ECL
   provision matrix, contract asset/liability schedule, PPA allocation)
   rather than a single number, so the model updates correctly period to
   period. `ifrs16_lease_calculator.py` does this for leases.
5. **Reconcile to GAAP if asked** — use `references/ifrs-vs-us-gaap.md` to
   identify where IFRS and US GAAP diverge for this transaction type, and
   quantify the adjustment (this is a common ask when a US-based investor
   or parent needs an IFRS subsidiary's numbers translated, or vice versa).
6. **Document the policy** — summarize the accounting policy applied and key
   estimates in a short note, in the form an auditor or reviewer would
   expect to see in the financial statement disclosures.

## Standards Covered

| Standard | Topic | Most relevant when... | Reference |
|---|---|---|---|
| IFRS 15 | Revenue from Contracts with Customers | Building a revenue build, SaaS/subscription contracts, multi-element arrangements, licensing | `references/ifrs15-revenue-recognition.md` |
| IFRS 16 | Leases | Any lessee with office/equipment/vehicle leases; almost always on-balance-sheet now | `references/ifrs16-leases.md`, `scripts/ifrs16_lease_calculator.py` |
| IFRS 9 | Financial Instruments | Loans, receivables, investments, derivatives, bad-debt/ECL provisioning | `references/ifrs9-financial-instruments.md` |
| IAS 1 | Presentation of Financial Statements | Structuring the statement set, OCI classification, current/non-current split | `references/ias1-presentation.md` |
| IFRS 3 / IFRS 10 / IFRS 11 | Business Combinations, Consolidation, Joint Arrangements | M&A modeling, purchase price allocation, group consolidation, JV accounting | `references/business-combinations-and-consolidation.md` |
| (cross-cutting) | IFRS vs. US GAAP differences | Dual reporting, GAAP-to-IFRS conversion, US parent with IFRS subsidiaries | `references/ifrs-vs-us-gaap.md` |

## Quick Reference: Lease Accounting Mechanics (IFRS 16)

The most common financial-modeling touchpoint. At commencement:

```
Lease liability = PV of remaining lease payments, discounted at the rate
                   implicit in the lease (if determinable) or the lessee's
                   incremental borrowing rate

Right-of-use asset = Lease liability
                    + initial direct costs
                    + payments made at/before commencement
                    - lease incentives received
                    + estimated cost of restoration/dismantling obligations
```

Each period: the liability accretes interest (effective interest method) and
is reduced by cash payments; the ROU asset is depreciated on a systematic
basis (usually straight-line) over the shorter of the lease term or the
asset's useful life. Use `scripts/ifrs16_lease_calculator.py` to generate the
full period-by-period schedule instead of doing this by hand:

```bash
python3 scripts/ifrs16_lease_calculator.py examples/sample_lease.json
python3 scripts/ifrs16_lease_calculator.py examples/sample_lease.json --format json
```

## Out of Scope

- Country-specific tax law, transfer pricing, or local statutory GAAP other
  than the US GAAP comparison in `references/ifrs-vs-us-gaap.md`
- Audit opinions, assurance procedures, or anything requiring an auditor's
  professional judgment sign-off
- Highly specialized standards only summarized in passing, not covered in
  depth: IFRS 17 (Insurance Contracts), IFRS 6 (Exploration for and
  Evaluation of Mineral Resources), IAS 41 (Agriculture), IAS 26 (Retirement
  Benefit Plans)
- Legal interpretation of ambiguous contract wording — flag as a legal
  question rather than guessing at intent
- XBRL tagging / regulatory filing mechanics
