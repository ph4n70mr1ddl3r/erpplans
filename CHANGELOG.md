# Changelog

> Track major changes to the BuildRight Depot ERP Plans repository.
>
> **Note (2026-06-21):** This file was condensed from ~4,100 lines to improve navigation.
> Every dated entry and factual change is preserved below; verbose rationale that already
> lives in code comments, commit messages, or [`workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md)
> was trimmed. The 29 repetitive gap-analysis passes are unified into a single summary table.

---

## 2026-06-21 — Quality review: Automation/Controls draft fields, backfill CTL-XX, repo hygiene, validator Check 21

A whole-repo **quality** review (distinct from the prior consistency reviews, which validated cross-reference *integrity*). The Automation/Controls fields were added repo-wide by a first-pass generator whose output was overwhelmingly draft quality, yet docs/validator reported it as "100% complete" — overstating maturity. All corrected below. `validate-repo.sh` now reports **0 errors / 2 informational warnings** across all **21** checks.

**Canonical totals (unchanged):** 187 value streams · 565 process areas · 5,317 workflows · 733 requirements · 67 controls · W1–W5464.

1. **Validator Check 21 (new)** — reports Automation/Controls *content quality* (fragment-bullet count, CTL-XX coverage %, pure-boilerplate count) as a WARN, making the quality bar measurable rather than aspirational.
2. **Honest-ized "100%" → "100% presence, draft content"** in `WORKFLOW-FORMAT-GUIDE.md`, Check 12's OK message, and both READMEs.
3. **`backfill-controls.py` (new)** — reverses `internal-controls-matrix.md` into a workflow→control map; injected real CTL-XX refs into **60 Core workflows** (555→615), and normalized **3,235** Controls sections missing the blank line before the next `###` (0 remain).
4. **Hardened `add-automation-controls.py`** — fixed duplicate `'approve'` dict key; `generate_automation()` now emits complete period-terminated sentences; `generate_controls()` is CTL-map-aware.
5. **`defragment-automation.py` (new)** — one-time repair regenerating **3,319** Automation sections (9,071 fragment bullets) into complete `- System {action} of "{step}" (replaces manual Step N).` sentences. Verified zero hand-written content destroyed (all co-existing bullets were also fragments).
6. **Repo hygiene** — added `.gitignore`; un-tracked committed `__pycache__/*.pyc` + `.antigravitycli/*.json`; cleared `+x` on 14 docs.

---

## 2026-06-21 — Consistency review #9: fix 1 stale PA-file nav link (VS-56) + add validator Check 20

Fixed 1 broken PA-file navigation link in `VS-56 PA-56.1` (`../value-stream.md` → `../value-stream-index.md`); a whole-repo scan of all 7,134 links confirmed it was the only genuinely-broken navigational link. Added **Check 20** (PA-file relative-link resolution — resolves all 2,262 relative links across 565 PA files).

## 2026-06-21 — Consistency review #8: fix 12 stale PA links in the value-stream index + add validator Check 19

Fixed 12 broken PA-file links in `value-stream-index.md` for **VS-178/179/180/181** (Pass 26 — hrefs used slugs with an extra `and` conjunction). Fixed stale pending-mapping range in `requirement-workflow-matrix.md` (VS-53–VS-177 → VS-53–VS-191). Added **Check 19** (PA/VS link resolution in the index — resolves all 752 links).

## 2026-06-20 — Consistency review #7: close Pass 26–29 criticality confirmation + dependency-map §8 extension

1. **Pass 26–29 criticality confirmation** (`workflow-criticality-classification.md` v7.26): 336 workflows (VS-178–VS-191; W5129–W5464) promoted from the keyword proposal after tier review — **117 → Tier 1** (statutory/regulatory execution), **24 → Tier 3** (analytics), **195 → Tier 2**. Confirmed **2,440 → 2,776 rows (2,417 → 2,753 unique)**; unclassified **2,900 → 2,564** (51.8%). **All 103 gap-analysis VSs (VS-89–VS-191) now confirmed.**
2. Dependency-map §8.2 (Tier-1 statutory programs) extended with VS-178/179/180/187/188/189/190/191.

## 2026-06-20 — Consistency review #6: stale aggregate-count reconciliation + gap-analysis Pass 27 completeness

Reconciled stale summary-prose counts across `workflow-criticality-classification.md`, `workflow-dependency-map.md`, `workflow-system-touchpoint-map.md`, and `workflow-gap-analysis.md`. Added the missing §3 rows for **VS-182–VS-185 (Pass 27, W5225–W5320)** and a Pass 26–29 family-subtotal progression table in `workflow-gap-analysis.md` §4 (now carrying totals through Pass 29 = 5,317).

## 2026-06-20 — Consistency review #5: W641–W647 standard formatting, 100% field adoption, validator Check 18

1. Re-formatted **W641–W647** (VS-19) to standard tables/subheadings, bringing Automation/Controls field **adoption to 100%** of all workflows.
2. Added **Check 18** (criticality-classification prose counts vs headings — catches the v7.19→v7.25 regression where tier-body sentences froze while headings advanced).

## 2026-06-20 — Consistency review #4: cash-float conflict, stale adoption claim, stale counts, validator Check 17

1. Corrected a factual POS opening cash-float conflict (PHP 3,000 vs PHP 2,500) in `VS-07 PA-07.1`.
2. Removed stale "Automation/Controls adoption pending" claims (the fields were already at 100%).
3. Added **Check 17** (orphan-workflow-body / ghost detection — found and flagged the VS-12 PA-12.2 W1318 ghost).

## 2026-06-20 — Consistency review #3: stale prose counts in criticality-classification, validator Check 16

Corrected 5 stale prose counts in `workflow-criticality-classification.md` and 2 stale grand-total citations in VS-133 PA files. Added **Check 16** (PA-file footer format — every PA must end with the standardized `*Workflow Count: N · Back to...*` footer; caught 30 deviating files in VS-168–VS-177 and 50 duplicate-footers in Core).

## 2026-06-20 — Consistency review #2: PA-subtotal correction, README folder-tree completeness

Corrected `value-stream-index.md` family PA subtotals (drifted during gap-analysis additions); added the missing `07-methodology/` scripts to the root README folder tree.

## 2026-06-20 — Consistency review #1: stale Expansion-block status, validator overlap-note, dept count

Corrected stale "Expansion-block pending rework" claims (the 2026-06-20 rework had completed); removed a validator Check 12 note that contradicted Check 10; corrected HQ department count drift.

## 2026-06-20 — Restore VS-12 ghost workflow W1318

Restored the missing `## W1318. Tool Rental Reservation, Waitlist & Scheduling` header in `VS-12 PA-12.2` (the workflow body existed but its `## W` header was lost in generation, making it invisible to every count/index/classification — Check 17). Count cascade **4,980 → 4,981** across current-state citations.

## 2026-06-20 — Defect-class exhaustion audit + validator Check 15

Added **Check 15** (analysis-field header canonicalization). Found and fixed VS-161's 8 `### Automation Option` typos and VS-10's 2 `### Risks & Exceptions` synonyms to the canonical forms.

## 2026-06-20 — Cross-reference consistency review: stale Pass-19 snapshots, touchpoint-map VS-162 gap

Updated `workflow-system-touchpoint-map.md` (gap-analysis module table was 16 value streams behind); corrected stale enterprise-process-volume figures in VS-133 PA files and a stale Pass-19 snapshot.

## 2026-06-20 — Profile consistency: org-chart ownership, Merchandising role mix, headcount

Mapped all 18 HQ departments to a C-suite owner (`model-company-profile.md` §11.1); fixed Merchandising team breakdown to sum to 40 (§13.1).

## 2026-06-20 — HQ headcount rebalance (minimum workflow-coverage): HQ 315 → 357; total 6,715 → 6,757

Cross-referenced stated HQ department headcounts against the actual roles implied by workflow coverage; rebalanced to the minimum defensible HQ staffing. See [`headcount-reality-check.md`](01-model-company/headcount-reality-check.md).

## 2026-06-20 — Whole-repo consistency review: stale counts (3,595/172/675), missing VS-170–VS-177 links

Corrected stale unclassified-workflow count **3,595 → 3,835** and stale value-stream count **172 → 173**; added missing VS-170–VS-177 links across the cross-reference layer.

## 2026-06-20 — Criticality hand-confirmation batch 3: 8 operational-support VSs (192 workflows)

**VS-40/43/55/63/64/65/83/84.** 21 → Tier 1 (PFRS capex capitalization, DOLE occupational-health/labor-relations mandatory steps); 30 → Tier 3 (analytics); 141 → Tier 2. Confirmed 1,552 → 1,744 rows.

## 2026-06-20 — Criticality hand-confirmation batch 2: 8 support & governance VSs (192 workflows)

**VS-100/104/112/113/126/129/133/139.** 14 → Tier 1 (statutory execution the keyword rules missed); 29 → Tier 3 (analytics/optimization); 149 → Tier 2. Confirmed 1,360 → 1,552 rows.

## 2026-06-20 — Criticality hand-confirmation batch 1: 8 wholly-statutory VSs (192 workflows)

**VS-79/85/89/91/114/117/118/125.** 154 → Tier 1 (statutory execution); 32 → Tier 2 (program support); 6 → Tier 3 (analytics). Confirmed 1,168 → 1,360 rows. Prompted by "can the 2 validator warnings be fixed mechanically?" — they cannot (the unclassified majority need genuine tier review).

## 2026-06-20 — Pass 29: Two new value streams (VS-190–VS-191; W5417–W5464; +48 workflows)

VS-190 Operational Technology (OT)/ICS Cybersecurity; VS-191 Customer Construction Debris & Site Cleanup. (See Gap Analysis table below.)

## 2026-06-20 — Pass 28: Four new value streams (VS-186–VS-189; W5321–W5416; +96 workflows)

VS-186 Compact/Heavy Equipment Rental; VS-187 Household Hazardous Waste Take-Back; VS-188 Trade Reseller Floor-Plan Financing; VS-189 Trade Receivables Factoring. (See Gap Analysis table below.)

---

## Workflow Gap Analysis (2026-06-14 → 2026-06-20)

Twenty-nine passes identified genuinely-unowned operational capabilities (defining terms appearing in **zero** PA files) and authored full value-stream directories, PA files, and cross-reference updates for each. **Totals: 103 value streams (VS-89–VS-191) · 2,472 workflows (W2993–W5464)** added, growing the active inventory from 84 to 187 value streams. The retired placeholder VS-49–VS-52 (see 2026-06-14 entry below) left gaps partly filled by these passes. Per-pass candidate/ID-allocation detail lives in [`workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md) §3–§4.

| Pass | Date | Value Streams | Workflows | W-range |
|---|---|---|---|---|
| 1 | 2026-06-14 | VS-89–VS-92 | 96 | W2993–W3088 |
| 2 | 2026-06-14 | VS-93–VS-96 | 96 | W3089–W3184 |
| 3 | 2026-06-14 | VS-97–VS-100 | 96 | W3185–W3280 |
| 4 | 2026-06-14 | VS-101–VS-104 | 96 | W3281–W3376 |
| 5 | 2026-06-14 | VS-105–VS-108 | 96 | W3377–W3472 |
| 6 | 2026-06-14 | VS-109–VS-112 | 96 | W3473–W3568 |
| 7 | 2026-06-14 | VS-113–VS-116 | 96 | W3569–W3664 |
| 8 | 2026-06-14 | VS-117–VS-120 | 96 | W3665–W3760 |
| 9 | 2026-06-14 | VS-121–VS-124 | 96 | W3761–W3856 |
| 10 | 2026-06-15 | VS-125–VS-128 | 96 | W3857–W3952 |
| 11 | 2026-06-15 | VS-129–VS-132 | 96 | W3953–W4048 |
| 12 | 2026-06-15 | VS-133–VS-136 | 96 | W4049–W4144 |
| 13 | 2026-06-16 | VS-137–VS-140 | 96 | W4145–W4240 |
| 14 | 2026-06-16 | VS-141–VS-142 | 48 | W4241–W4288 |
| 15 | 2026-06-17 | VS-143–VS-146 | 96 | W4289–W4384 |
| 16 | 2026-06-17 | VS-147–VS-150 | 96 | W4385–W4480 |
| 17 | 2026-06-17 | VS-151–VS-156 | 144 | W4481–W4624 |
| 18 | 2026-06-18 | VS-157–VS-161 | 120 | W4625–W4744 |
| 19 | 2026-06-19 | VS-162–VS-164 | 72 | W4745–W4816 |
| 20 | 2026-06-19 | VS-165–VS-167 | 72 | W4817–W4888 |
| 21 | 2026-06-19 | VS-168–VS-169 | 48 | W4889–W4936 |
| 22 | 2026-06-19 | VS-170–VS-172 | 72 | W4937–W5008 |
| 23 | 2026-06-20 | VS-173 | 24 | W5009–W5032 |
| 24 | 2026-06-20 | VS-174–VS-176 | 72 | W5033–W5104 |
| 25 | 2026-06-20 | VS-177 | 24 | W5105–W5128 |
| 26 | 2026-06-20 | VS-178–VS-181 | 96 | W5129–W5224 |
| 27 | 2026-06-20 | VS-182–VS-185 | 96 | W5225–W5320 |
| 28 | 2026-06-20 | VS-186–VS-189 | 96 | W5321–W5416 |
| 29 | 2026-06-20 | VS-190–VS-191 | 48 | W5417–W5464 |
| **Total** | | **VS-89–VS-191** | **2,472** | **W2993–W5464** |

---

## 2026-06-19 — Whole-repo consistency reviews (5 passes)

A series of top-to-bottom reads of every summary/cross-reference document and high-traffic PA files. Findings and fixes:

- **Broken anchor links** (factual defects) and **Goods Receipts scope ambiguity** (`model-company-profile.md` §15.1).
- **BIR record retention canonicalized to 10 years** (TRAIN/NIRC) across all documents (was inconsistent 7 vs 10 years).
- **Volume-unit consistency** — monthly figures mislabeled as daily; corrected.
- **Operational bank list reconciled to 4** (BDO, BPI, Metrobank, China Bank) and minor figure drift fixed.
- **Documentation hygiene** — number-format drift, TOC count drift, stale POS/documented-workflow counts.

## 2026-06-19 — Cross-document figure consistency review (bank list, headcount, POS figures)

Reconciled stale figures (bank-account count, headcount totals, POS transaction volumes) across overview and high-traffic workflow documents.

## 2026-06-18 — Data-volumes AP figure reconciliation & cross-reference housekeeping

Resolved the outstanding AP-figures cross-reference ambiguity; corrected stale figures and broken references accumulated behind the gap-analysis block. Content pass on payroll dates, bank list, stale ranges, and the W40 category.

## 2026-06-18 — Gap-analysis structural consistency: restore missing Pass 12 table

Restored the missing Pass 12 table in `workflow-gap-analysis.md` §3; fixed family counts and two small cross-reference issues.

## 2026-06-17 — Consistency reviews (3 passes)

- Corrected **unclassified-workflow count 2,972 → 2,995** (reported inconsistently in five places) and collapsed the related prose.
- Corrected stale **requirement total 730 → 733** in `erp-requirements.md` v21.0 footer.
- Reconciled Pass 13/14 (VS-137–VS-142) across cross-reference docs.

## 2026-06-15 — Workflow review implementation (5-commit program)

1. **(1/5) Structural-integrity fixes** — bounded set of PA-file format/structural fixes + validator hardening.
2. **(2/5) Keyword-driven classification pass** — addressed 2,659 workflows (70%) with no criticality tier; generated `workflow-criticality-proposed.md` via `classify-workflows.py`.

## 2026-06-15 — Workflow documentation review: format guide, index, validator

Reviewed value-stream/workflow documentation; updated `WORKFLOW-FORMAT-GUIDE.md`, the value-stream index, and the validator.

## 2026-06-14 — Consistency review: decision tree, matrix counts & validator accuracy

Full-repository review (then 84 VS / 256 PA / 2,844 workflows) reconciling every cross-document count.

## 2026-06-14 — Repo review: retire VS-49/50/51/52 placeholder content, harden validator

Identified 4 value streams (VS-49–VS-52) whose workflow files contained only auto-generated placeholder content; retired them (96 placeholder workflows removed; numbers remain unused). The resulting capability gaps were filled across the gap-analysis passes above.

## 2026-06-14 — Repo review: fix dangling W5G reference & harden validator

Full-repository review; investigated flagged items, narrowed to real defects, fixed the dangling W5G reference and hardened the validator.

## 2026-06-14 — Add 10 new value streams (240 workflows, W2753–W2992)

Identified 10 business capabilities not yet organized as value streams; authored each with 3 process areas / 24 workflows.

## 2026-06-14 — Consistency review: requirement-ID dedup & criticality summary fix

Removed 19 mislabeled duplicate requirement-ID rows from `requirement-workflow-matrix.md`; fixed the criticality summary.

## 2026-06-13 — Consistency reviews (3 passes)

- **Eliminated all 15 duplicate workflow IDs** (IDs must be unique per `WORKFLOW-FORMAT-GUIDE.md`).
- **Standardized all 238 PA file footers** to the `*Workflow Count: N · Back to...*` convention.
- **Reconciled all cross-document counts**; deduplicated CHANGELOG (removed 13 identical copies of one entry).

## 2026-06-12 — Add 4 new value streams with 96 workflows (W1830–W1925)

VS-41 Private Label; VS-42 Property & Lease Admin; VS-43 Trade Professional Program; VS-44 Consumer Insights.

## 2026-06-12 — Add 40 new workflows across 39 process areas (W1485–W1552)

Two batches (W1485–W1504, W1533–W1552) of model-company-relevant workflows across store, DC, supply, and finance process areas.

## 2026-06-11 — Consistency review: reconcile all workflow counts

Reconciled workflow counts across all 30 VS READMEs, `value-stream-index.md`, and the root README.

## 2026-06-10 — Add 65 new workflows (W1298–W1414)

Four batches of model-company-relevant workflows: fleet/vehicle management (W1348–W1414), customer PDC/trade-account processing (W1380–W1399), consignment/intercompany (W1298–W1317), tool rental (W1318–W1327).

## 2026-06-09 — Add workflows & post-review cleanup

- Added **WHL-001/002/003** to `erp-requirements.md` (DC/warehouse management requirements referenced in workflows).
- Added 77 new workflows across multiple batches (W1167–W1277) including reverse logistics, DSD receiving, e-wallet settlement, and post-disaster demand fulfillment.
- Fixed VS-16 workflow count (17 → 23) and related cross-reference issues.
