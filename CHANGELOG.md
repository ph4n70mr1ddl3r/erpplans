# Changelog

> Track major changes to the BuildRight Depot ERP Plans repository.

---

## 2026-06-14 — Repo Review: Retire VS-49/50/51/52 Placeholder Content, Harden Validator

A second full-repository review identified four value streams whose workflow files had
been committed with only auto-generated placeholder content (broken H1 headers, generic
"Process trigger" steps, copy-paste 3-step bodies, and no criticality/dependency/matrix
references). All other cross-document counts reconciled cleanly.

### Removed
- **Retired VS-49, VS-50, VS-51, VS-52** (96 placeholder workflows, W2022–W2117) — the four
  directories under `01-model-company/workflows/` were deleted:
  - `VS-49-dark-store-micro-fulfillment/` (3 PA files, 24 workflows)
  - `VS-50-damage-claims-management/` (3 PA files, 24 workflows)
  - `VS-51-assembly-kitting-bundling/` (3 PA files, 24 workflows)
  - `VS-52-cooperative-community-procurement/` (3 PA files, 24 workflows)
  
  Each PA file had a broken H1 (e.g. `# PA-50.1](PA-50.1-...md — 8`), workflow titles of
  the form "Workflow 2046 — 8 Process 0", and copy-paste body content. The four VS numbers
  are intentionally **retired** and will not be reused — the value streams will be reintroduced
  with fully detailed workflows in a future revision. Existing references to these VS numbers
  elsewhere have been removed or rewritten.

### Updated counts (repository-wide reconciliation)
All documents that referenced the old totals were reconciled to the new figures:

| Metric | Old | New |
|---|---|---|
| Value streams | 88 | **84** |
| Process areas | 268 | **256** |
| Total workflows | 2,940 | **2,844** |
| Unclassified workflows | 1,773 | **1,677** |
| Plan & Source subtotal | 308 | 284 |
| Make & Move subtotal | 283 | 235 |
| Sell & Serve subtotal | 1,098 | 1,074 |

Files updated (summary table, family tables, footer notes, or grand totals):
- `README.md` — folder tree, Key Metrics table, Document Relationships diagram, and a new
  **Coverage & Known Gaps** section disclosing the retired VS numbers and the 1,677
  workflows still pending criticality classification.
- `01-model-company/executive-summary.md` — totals line.
- `01-model-company/workflows/README.md` — Quick Stats, family tables, and reconciliation line.
- `01-model-company/workflows/value-stream-index.md` — header banner, summary table rows,
  family subtotals, grand total, detailed VS-49–VS-52 sections removed, and a coverage note.
- `01-model-company/workflows/workflow-criticality-classification.md` — disclaimer, Summary
  table, and footer version (bumped to v7.2).
- `01-model-company/workflows/workflow-dependency-map.md` — header note and footer (v2.3).
- `01-model-company/workflows/workflow-system-touchpoint-map.md` — footer (v54.0).
- `01-model-company/workflows/VS-56-third-party-delivery-partner/PA-56.2-delivery-performance-sla.md`
  — one inline reference to "VS-50" (damage-record routing) rewritten to VS-agnostic wording.

### Hardened
- **`07-methodology/validate-repo.sh`** — tightened and extended to prevent regressions:
  - **Check 1** (unclassified workflows) now counts actual classification **table rows**
    (`^| W...|`) rather than any `\bW\d+\b` token in the file's prose. The old extraction
    undercounted by ~22 IDs and produced a misleading "1,794 unclassified" figure. The new
    count reconciles exactly with the file's stated 1,167 classified rows.
  - **Check 8** (new) — placeholder/skeleton content detector. Flags any PA file containing
    the known generator-script failure markers: broken H1 (`# PA-X.Y](...`), generic
    "Workflow NNNN — N Process N" titles, "Process trigger", "Execute standard process step",
    or "Standard operational risks mitigated by procedural controls". This would have caught
    VS-49–VS-52 at commit time.
  - **Check 9** (new) — grand-total reconciler. Asserts that the `Grand Total` row in
    `value-stream-index.md` equals the actual count of `## W...` headers in PA files. This
    would have caught the VS-49–VS-52 inflation immediately.

---

## 2026-06-14 — Repo Review: Fix Dangling W5G Reference & Harden Validator

A full-repository review identified a small number of defects. Investigation narrowed the
scope: most flagged items were validator artifacts, not content defects. The genuinely
required fixes are below.

### Fixed
- **W5G (Offline POS Recovery & Reconciliation)** — the only genuinely dangling workflow
  reference in the repository. It was referenced 15+ times across `PA-07.1`, `PA-08.1`,
  `workflow-dependency-map.md`, `workflow-system-touchpoint-map.md`, and
  `requirement-workflow-matrix.md`, but had no definition at any heading level. Added the
  full `### W5G.` sub-workflow definition inside `## W5. Daily Store Operations`
  (`PA-07.1-store-daily-management.md`), covering offline-event replay, inventory/void/
  loyalty reconciliation (NR-3/4/5), settlement matching, and escalation to W48/W37.
  Existing inline references to `W5G.5` (cross-channel loyalty conflict) are now honored.
- **`workflow-dependency-map.md` section numbering** — duplicate `## 5.` heading;
  "Circular Data Loop Risks" and "Dependency Matrix" were both misnumbered. Renumbered
  to sequential 5 (Critical Path) → 6 (Circular Data Loop Risks) → 7 (Dependency Matrix).
- **`workflow-system-touchpoint-map.md` duplicate entries** — `W439` was listed twice
  (Inventory Management) and `W440`/`W442` were each listed twice (Services / Rental).
  Deduplicated to one entry each.
- **`README.md` requirement-category count** — stated "32+ categories"; there are actually
  **38** distinct requirement prefixes. Corrected in both the folder-structure comment and
  the Key Metrics table (consistent with `erp-requirements.md` which already stated 38).

### Updated
- **`07-methodology/validate-repo.sh`** — the validator's `\bW\d{1,4}\b` regex silently
  ignored letter-suffixed sub-workflow IDs (`W<number><letter>`, defined in the
  `WORKFLOW-FORMAT-GUIDE.md` as sub-workflow/variant notation), and Check 1 only inspected
  `## ` (h2) headers, missing `### ` (h3) sub-workflow definitions. This is what had
  masked W5G and produced misleading "unclassified" counts. Hardened as follows:
  - **Check 1** now extracts headers at both `## ` and `### ` levels, so h3 sub-workflows
    (W5A–W5G, W12A–C, W2A–C, etc.) are counted.
  - **Check 6** regex widened to `\bW\d{1,4}[A-Z]?\b` so letter-suffixed references in the
    requirement-workflow matrix are validated.
  - **Check 7 (new)** scans all four cross-reference documents (dependency map, touchpoint
    map, requirement-workflow matrix, internal-controls matrix) for workflow IDs that are
    referenced but never defined as a `## `/`### ` header in any PA file. Dangling
    references are reported as **errors** (this check would have caught W5G pre-fix).

### Reviewed — no action needed (corrected from initial review)
- **Letter-suffixed workflow IDs were NOT dangling.** 23 of 24 such IDs in the criticality
  file are legitimately defined as `### ` (h3) sub-workflows (e.g. `W5A`, `W12A`, `W2A`,
  `W7C`), and 2 (`W2C`, `W19B`) as `## ` (h2) workflows — exactly per the format guide's
  `W<number><letter>` sub-workflow convention. The initial review's "24 dangling IDs"
  claim was a validator-regex artifact, now resolved by the validator hardening above.
- **Criticality sub-section counts reconcile.** All 42 domain sections and 3 "Tier N
  Additions" sections sum to exactly 1,167 classified rows (486 domain + 681 tier
  additions), matching the stated grand total. The initial review's "sums to ~490" finding
  was an off-by-one in the ad-hoc awk used during review.

### Verified ✓
- `07-methodology/validate-repo.sh` passes with **0 errors** (1 informational warning on
  the acknowledged ~1,793 unclassified workflows pending criticality review).
- New **Check 7** reports 0 dangling references across all 4 cross-reference documents.
- All 268 PA file footers still match their `## ` header counts (0 mismatches).
- Total defined workflow IDs: **2,963** (2,940 h2 primary + 23 h3 sub-workflows),
  0 duplicates.

---

## 2026-06-14 — Add 10 New Value Streams (240 Workflows, W2753–W2992)

### Added
Identified 10 business capabilities relevant to the model company that were not yet
organized as value streams, and authored each as a full 3-process-area / 24-workflow value
stream (10 × 24 = 240 new workflows, W2753–W2992):

- **VS-79: Tax Management & BIR Statutory Reporting** (Finance) — Indirect tax (VAT/percentage tax) & BIR EIS e-Invoicing; Withholding tax (EWT/CWT) & Form 2307; Corporate income tax, local business tax, DST & BIR audit defense. Consolidates/extends scattered tax touchpoints (W90, W260, W473, W293, W478) into a coherent tax-compliance program.
- **VS-80: Payment Operations, Acquirer & Settlement Management** (Finance) — Acquirer/PSP/e-wallet/BNPL partner lifecycle; settlement reconciliation & chargeback representment; PCI-DSS, 3DS, tokenization & payment fraud governance across ~2.8M POS transactions/month.
- **VS-81: Cash-in-Transit, Vault & Armored Car Operations** (Make & Move) — Smart-safe and pickup planning for ~1.2M monthly cash transactions; armored car/vault execution; CIT insurance, risk & cash analytics.
- **VS-82: Sari-Sari Store & MSME Micro-Wholesale Program** (Sell & Serve) — Acquisition & micro-distribution for the Philippines' ~1.3M sari-sari stores; last-mile micro-wholesale ordering & delivery; MSME credit, digital enablement & growth.
- **VS-83: Occupational Health, Safety Clinic & Employee Wellness** (People) — Clinic operations & medical case management; pre-employment/APE/DOLE hazard exams & disease surveillance; mental health (RA 11036), EAP & wellness for 6,715 employees.
- **VS-84: Labor Relations & Collective Bargaining Management** (People) — Union recognition & CBA negotiation/administration; grievance handling, 2-notice rule & DOLE conciliation/NLRC; employee voice & partnership governance.
- **VS-85: Mandatory Discount, Eligibility & Tax Credit Recovery** (Governance & Assurance) — SC/PWD/Solo Parent discount program (RA 9994/10754/11861); VAT-exempt & zero-rated customer certification; tax credit recovery via BIR Form 2552 & TCC. Program layer over W170/W217/W432.
- **VS-86: Anti-Financial Crime, AML/KYC & Anti-Corruption** (Governance & Assurance) — First-line KYC/CDD/PEP/sanctions screening; AML transaction monitoring, CTR/STR filing with AMLC; anti-bribery, gifts & conflict-of-interest (AMLA RA 9160/10365, RA 3019, ISO 37001). Operational counterpart to audit workflows W159/W354.
- **VS-87: Customs Trade Compliance & Tariff Optimization** (Governance & Assurance) — HS tariff classification, valuation & rules of origin; FTA preference (AFTA/RCEP), duty drawback & bonded warehouse; BOC audit defense, broker governance & ADC/CVD for ~40% of COGS imported.
- **VS-88: Document Control, Records Management & Retention** (Governance & Assurance) — Taxonomy, versioning & access control; retention scheduling (BIR 10-yr, SEC, DOLE, NPC), legal hold & secure disposition; e-Discovery & BIR/SEC/NPC/DOLE records audit.

### Updated
- Total workflows: **2,700 → 2,940** (+240 new)
- Total value streams: **78 → 88** (+10 new)
- Total process areas: **238 → 268** (+30 new)
- `value-stream-index.md` — added 10 VS rows, 10 detailed map blocks, updated all family subtotals (Make & Move 259→283; Sell & Serve 1074→1098; Finance 339→387; People 74→122; Governance & Assurance 384→480), grand total, and decision tree.
- `README.md` (workflows) — full rewrite of family tables to complete and accurate 88-VS view (also corrected a pre-existing omission of VS-70/71/72/73/75/76/77/78 from the family tables).
- `README.md` (repository) — folder structure extended with VS-79–VS-88; counts updated to 2,940 / 88 VS / 268 PA in structure, key metrics, and integration diagram.
- `executive-summary.md` — workflow count updated to 2,940 across 88 value streams.
- `workflow-criticality-classification.md` — grand total 2,700→2,940; unclassified 1,533→1,773 (the 240 new workflows are unclassified pending criticality review; flagged many as Tier 1 candidates).
- `workflow-dependency-map.md` — total 2,700→2,940; VS count 78→88.
- `workflow-system-touchpoint-map.md` — total 2,700→2,940 (1,167 classified + 1,773 unclassified).

### Verified ✓
- 10 new VS folders, each with README + 3 PA files = 40 new files.
- 240 new `## W<number>.` workflow headers (W2753–W2992); 0 duplicate workflow IDs.
- Family subtotal reconciliation: 308 + 283 + 1,098 + 387 + 122 + 104 + 480 + 158 = 2,940.
- `07-methodology/validate-repo.sh` passes with 0 errors.

---

## 2026-06-14 — Consistency Review: Requirement-ID Dedup & Criticality Summary Fix

### Fixed
- **Removed 19 mislabeled duplicate requirement-ID rows** from `requirement-workflow-matrix.md`: each row carried a low requirement ID (e.g. `POS-071`, `GOV-045`, `FIN-045`) but the description and workflow mapping of a higher-numbered "Additional" requirement (e.g. `POS-106` Store-Level Daily Closing Procedure → `W574`). In `erp-requirements.md` those low IDs already map to *different* requirements (e.g. `POS-071` = POS Credit Card Installment Selling → `W747`), so the duplicate rows were both wrong and misleading. Verified that every canonical requirement retains its correct primary-workflow mapping (0 unmapped requirements; 0 orphan references).
- **Corrected the `requirement-workflow-matrix.md` Coverage Validation block** — previous counts (730 / 429 / 295 / 6) did not match `erp-requirements.md`. Now reads **733 / 431 / 296 / 6** and references the full 2,700-workflow / 78-value-stream scope.
- **Reconciled the tier totals in `workflow-criticality-classification.md`** — the `## Summary` table now reflects the "Additions" sections (Tier 1: 155+284=**439** · Tier 2: 206+293=**499** · Tier 3: 125+104=**229** = 1,167 classified; 1,533 unclassified; grand total **2,700**) and the per-subsection headings were updated to match (e.g. Core POS 21→23, Core HR 8→6, Extended Ecommerce 4→2, Extended Finance 22→21, Internal Audit 15→42, Advanced Master Data 3→7).
- **Removed a stale, contradictory `## Updated Summary` + `### Operational Tier Guidance` block** at the end of `workflow-criticality-classification.md`. It reported a Tier 3 total of **226** (correct: 229), **0 unclassified** (correct: 1,533), and a grand total of **1,167** (correct: 2,700), directly contradicting the canonical `## Summary`. The authoritative summary above is unchanged.
- **Replaced the per-domain breakdown table** in `workflow-criticality-classification.md` with a note pointing at the per-tier subsection headings and `value-stream-index.md`, since the table's partial counts could not be reconciled with the tier totals.

### Verified ✓
- `07-methodology/validate-repo.sh` passes with 0 errors (1 informational warning).
- Grand total: **2,700** workflows; 1,167 classified (439/499/229) + 1,533 unclassified.
- Requirements: **733** (431 Must / 296 Should / 6 Nice); all mapped to workflows; 0 duplicate IDs.
- 0 genuinely broken intra-repo markdown links.

---

## 2026-06-13 — Consistency Review: Deduplicate Workflow IDs & Reconcile Counts

### Fixed
- **Eliminated all 15 duplicate workflow IDs** (workflow IDs must be unique per `WORKFLOW-FORMAT-GUIDE.md`):
  - **Removed 4 duplicate authorings in VS-16** — `W812`, `W889`, `W890` were authored twice (once misplaced in PA-16.1 Credit, once correctly in PA-16.2 AR & Collections); `W892` was duplicated in PA-16.3. Kept the correctly-placed PA-16.2 versions; removed the misplaced copies. VS-16: 35 → 31 workflows.
  - **Renumbered 11 ID collisions** (two different workflows sharing one number) to the next free IDs `W2742`–`W2752`. Canonical (externally-referenced) owner retained in each case: VS-09 PA-09.3 (`W1380–1382`), VS-16 PA-16.2 (`W813–814`), VS-22 PA-22.1 (`W331`), VS-40 PA-40.3 (`W1830–1834`) were the displaced copies; VS-15/VS-21/VS-41 versions kept their numbers.
  - Updated the 2 cross-references that pointed at a displaced copy: `workflow-dependency-map.md` (`W331 (DTI Application)` → `W2747`) and VS-40 PA-40.1 (`per W1830` → `per W2748`).
- **Rebuilt all 238 PA-file "Workflows in This Process Area" tables of contents** from actual headers, which also:
  - Fixed **295 broken in-page anchor links** (TOC anchors missing the `W<number>-` prefix, concentrated in generated VS-49–VS-78).
  - Added **~42 workflows** that had bodies but were missing from their PA's TOC.
  - Dropped **2 stub TOC entries** (`W1194`, `W1318`) that have no workflow body (flagged as content gaps).
  - Recomputed every PA footer `Workflow Count`.
- **Reconciled over-counted workflow totals** (grand total 2,705 → **2,700**; unclassified 1,538 → **1,533**): VS-08 (POS & Checkout) 59 → 58 — PA-08.1 claimed 37 but contained 36; VS-16 35 → 31 (duplicate removal above). Updated `value-stream-index.md`, `README.md`, `executive-summary.md`, `workflow-criticality-classification.md`, `workflow-dependency-map.md`, `workflow-system-touchpoint-map.md`, and the 2 affected VS READMEs.
- **Fixed broken link** in `value-stream-index.md` — VS-61 PA-61.3 pointed at `VS-61-fleet-cost-management/` (non-existent) → corrected to `VS-61-fuel-fleet-cost-management/`.

### Verified ✓
- Grand total: **2,700 workflows** across 78 value streams, 238 process areas, 8 families
- 0 duplicate workflow IDs; 2700 distinct IDs = 2700 headers
- 0 broken in-page TOC anchors; 0 missing intra-repo links in the index
- All 78 VS README totals and all 238 PA footers match actual `## W` header counts
- All 8 family subtotals reconcile (308 + 259 + 1074 + 339 + 74 + 104 + 384 + 158 = 2700)
- Requirements: 733 (431 Must / 296 Should / 6 Nice); Internal Controls: 67 (31 Preventive / 36 Detective)
- `07-methodology/validate-repo.sh` passes with 0 errors

> Note: the prior total of 2,705 was an over-count — it included 4 duplicate workflows in VS-16, 1 phantom workflow over-counted in VS-08, and missed that VS-03/VS-10 were already correct (their letter-suffix workflows `W2C` and `W19B` had not been tallied). Corrected here.

---

## 2026-06-13 — Consistency Review: Standardize PA File Footers

### Fixed
- **Standardized all 238 PA file footers** to consistent format: `*Workflow Count: N · Back to **[VS-XX: Name](./README.md)** · [Value Stream Index](../value-stream-index.md)*`
- **Corrected 4 wrong workflow counts in PA footers**:
  - PA-07.2 (Store Facility & Safety): 44 → 46
  - PA-11.1 (Trade Account Management): 8 → 10
  - PA-12.2 (Tool Rental & Equipment): 10 → 9
  - PA-25.1 (Environmental Monitoring): 12 → 14
- **Added missing `Workflow Count` footer** to 48 PA files that only had a back-link without a count (PA files across VS-01 through VS-40)
- **Standardized VS link text** in all PA footers to use readable names (e.g., `VS-50: Damage & Claims Management`) instead of folder slugs (e.g., `VS-50-damage-claims-management`)
- **Updated WORKFLOW-FORMAT-GUIDE date** to 2026-06-13

### Verified (no changes needed)
- Grand total: 2,705 workflows across 78 value streams, 238 process areas ✓
- All 78 VS README totals match actual `## W` header counts ✓
- All 238 PA-level counts in value-stream-index.md match actual counts ✓
- Requirements: 733 (431 Must Have + 296 Should Have + 6 Nice to Have) ✓
- Internal Controls: 67 (31 Preventive + 36 Detective) ✓
- POS terminal count: 3 per store (600 total) — no stale "5 terminal" references ✓
- validate-repo.sh passes with 0 errors ✓

---

## 2026-06-13 — Consistency Review: Reconcile All Cross-Document Counts

### Fixed
- **Deduplicated CHANGELOG.md** — removed 13 identical copies of the "Add 20 New Workflows (W1533–W1552)" entry (kept one); removed the merged duplicate header in the W1167–W1206 section
- **Fixed value-stream-index.md subtotals** — Governance & Assurance: 376 → 384; Grand Total: 2,481 → 2,705
- **Updated README.md** — Key Metrics: 68 VS → 78, 208 PA → 238, 2,465 workflows → 2,705; folder structure updated with VS-69 through VS-78; document relationship diagram updated
- **Updated workflow-criticality-classification.md** — total 2,465 → 2,705; unclassified 1,298 → 1,538
- **Updated workflow-dependency-map.md** — total 2,465 → 2,705; unclassified 1,298 → 1,538
- **Updated workflow-system-touchpoint-map.md** — footer total 2,465 → 2,705
- **Updated executive-summary.md** — workflow count 2,465 → 2,705

---

## 2026-06-12 — Add 4 New Value Streams with 96 Workflows (W1830–W1925)

### Added
- **VS-41: Private Label & Exclusive Brand Management** — 3 process areas, 24 workflows
  - PA-41.1: Private Label Product Development & Sourcing (W1830–W1837)
  - PA-41.2: Private Label Quality Assurance & Compliance (W1838–W1845)
  - PA-41.3: Private Label Brand, Packaging & Marketing (W1846–W1853)
- **VS-42: Property & Lease Administration** — 3 process areas, 24 workflows
  - PA-42.1: Lease Negotiation & Administration (W1854–W1861)
  - PA-42.2: Rent Payment, Escalation & CAM Reconciliation (W1862–W1869)
  - PA-42.3: Property Tax, LGU Compliance & Lease Accounting (W1870–W1877)
- **VS-43: Trade Professional Program & Contractor Services** — 3 process areas, 24 workflows
  - PA-43.1: Trade Account Lifecycle & Relationship Management (W1878–W1885)
  - PA-43.2: Contractor Loyalty, Incentive & Volume Program (W1886–W1893)
  - PA-43.3: Trade Training, Certification & Community Engagement (W1894–W1901)
- **VS-44: Consumer Insights & Market Research** — 3 process areas, 24 workflows
  - PA-44.1: Customer Satisfaction & Experience Research (W1902–W1909)
  - PA-44.2: Market & Competitive Intelligence (W1910–W1917)
  - PA-44.3: Product Category & Shopper Research (W1918–W1925)

### Updated
- Total workflows: **1,834 → 1,930** (+96 new)
- Total value streams: **40 → 44** (+4 new)
- Total process areas: **124 → 136** (+12 new)
- Updated value-stream-index.md with new value stream entries and revised totals

---

## 2026-06-12 — Add 20 New Workflows Across 20 Process Areas (W1533–W1552)

### Added
- **W1533**: S&OP Monthly Consensus Demand Review, Cross-Functional Alignment & Supply Plan Ratification (PA-02.1)
- **W1534**: DC Night Shift Operations, Security Protocol & Shift Handover Management (PA-04.3)
- **W1535**: Emergency Inter-DC Stock Transfer for Critical Out-of-Stock Prevention (PA-05.2)
- **W1536**: Fleet Vehicle Registration Renewal, LTO Compliance & LTFRB Cargo Freight License Management (PA-06.2)
- **W1537**: Store-Level Parking Lot & Exterior Area Daily Operations, Customer Vehicle Flow & Security Management (PA-07.1)
- **W1538**: POS Multi-Tender Partial Refund Processing, Change Allocation & Tender Reversal Management (PA-08.1)
- **W1539**: Installation Service Post-Completion Quality Inspection, Customer Sign-Off & Punch List Resolution (PA-12.1)
- **W1540**: Trade Account Monthly Statement Generation, Aging Analysis & Collection Priority Scoring (PA-16.2)
- **W1541**: Key Risk Indicator (KRI) Monthly Monitoring, Threshold Alert & Risk Appetite Dashboard Operations (PA-21.2)
- **W1542**: Organized Retail Crime (ORC) Pattern Detection, Multi-Store Correlation & Law Enforcement Coordination (PA-23.1)
- **W1543**: Store-Level Energy Consumption Benchmarking, Carbon Footprint Estimation & Reduction Target Tracking (PA-25.1)
- **W1544**: POS Terminal Lifecycle Management, Hardware Refresh Cycle & Peripheral Standardization (PA-27.2)
- **W1545**: Cost Center & Profit Center Hierarchy Governance, Allocation Rule Review & Reporting Validation (PA-29.2)
- **W1546**: Vendor Factory Social Compliance Audit Scheduling, Scoring & Corrective Action Tracking (PA-03.1)
- **W1547**: Product Regulatory Compliance Certification Management (DTI-BPS, FPA, DENR) & Renewal Tracking (PA-01.1)
- **W1548**: Ecommerce Customer Product Bundle Builder & Custom Project Kit Assembly Order Processing (PA-10.1)
- **W1549**: Contractor Annual Spend Tier Review, Loyalty Tier Recalculation & Benefit Adjustment (PA-11.2)
- **W1550**: Customer Voice-of-Customer (VOC) Monthly Analysis, Trend Dashboard & Strategic Insight Reporting (PA-13.1)
- **W1551**: Local Store Marketing Campaign Execution, Barangay-Level Outreach & Community Event Partnership (PA-14.1)
- **W1552**: Typhoon Post-Event Rapid Store Damage Assessment, Safety Clearance & Phased Reopening Protocol (PA-26.2)

### Updated
- Total workflows: **1,522 → 1,542** (+20 new)
- Updated all affected VS README files, PA file footers, and value-stream-index.md with revised workflow counts
- Updated root README.md folder structure counts

---

## 2026-06-12 — Add 20 New Workflows Across 19 Process Areas (W1485–W1504)

### Added
- **W1485**: Store Paint Mixing Station Daily Calibration, Color Formula Database Update & Tint Inventory Replenishment (PA-07.1)
- **W1486**: Lumber Yard Inventory Measurement, Board Foot Calculation & Dimensional Grading Verification (PA-05.1)
- **W1487**: Store Garden Center & Plant Nursery Seasonal Assortment Rotation, Vendor-Managed Inventory & Markdown Optimization (PA-01.1)
- **W1488**: Customer Bulk Sand, Gravel & Cement Delivery Scheduling, Weight Ticket Verification & Site Unloading Coordination (PA-06.3)
- **W1489**: BIR Electronic Invoicing (E-Invoice) Compliance, System Registration & Monthly Transmission (PA-22.1)
- **W1490**: Store-Level Plumbing & Electrical Fixture Display Model Rotation, Demo Unit Tracking & Write-Off (PA-07.1)
- **W1491**: Customer Kitchen & Bathroom Design Consultation, 3D Rendering & Material Take-Off Generation (PA-09.2)
- **W1492**: Typhoon Season Pre-Positioning of Emergency Construction Materials (Tarpaulins, Plywood, CGI Sheets) & Demand Allocation Across Store Network (PA-02.3)
- **W1493**: Store-Level Contractor Lounge & Trade Amenities Management, Satisfaction Survey & Retention (PA-09.3)
- **W1494**: POS Customer Project Receipt, Multi-Store Purchase Aggregation & Tax Credit Certificate Processing (PA-08.1)
- **W1495**: Vendor-Managed Inventory (VMI) Replenishment, Min/Max Review & Automated PO Generation (PA-03.4)
- **W1496**: Intercompany Warehouse Service Fee Dispute Resolution, Rate Review & Quarterly Settlement Agreement (PA-17.2)
- **W1497**: Store-Level Anti-Theft Cable & Sensor Tag Deployment, Deactivation Compliance & Equipment Maintenance (PA-23.3)
- **W1498**: DC Temperature-Sensitive Material (Adhesives, Sealants, Paint) Storage Monitoring, Expiry Alert & FIFO Enforcement (PA-04.3)
- **W1499**: Customer Loyalty Program Tier Qualification Period Reset, Points Expiration Management & Downgrade Communication (PA-13.2)
- **W1500**: Store New Employee Shadow Training Program, Buddy Assignment & 90-Day Competency Checklist (PA-19.4)
- **W1501**: Store Rooftop Solar Panel Installation ROI Assessment, Net Metering Application & Monthly Energy Offset Tracking (PA-20.3)
- **W1502**: Customer E-Commerce Product Comparison Tool, Alternate/Substitute Product Recommendation & Cross-Sell Engine (PA-10.1)
- **W1503**: BIR Percentage Tax vs. VAT Threshold Monitoring, Quarterly Tax Regime Evaluation & Registration Adjustment (PA-17.3)
- **W1504**: Supplier Invoice Price Discrepancy Investigation, Debit Note Issuance & Resolution Tracking (PA-15.1)

### Fixed
- **Corrected PA-12.2 workflow count** in VS-12 README: 6 → 7 (actual file count); VS-12 total: 31 → 32
- **Corrected VS-10 detailed section** in value-stream-index.md: 53 → 58 (summary table was already correct)
- **Corrected VS-28 detailed section** in value-stream-index.md: 20 → 22 (summary table was already correct)

### Updated
- Total workflows: **1,470 → 1,490** (+20 new + 1 existing uncounted fix)
- Updated all affected VS README files and value-stream-index.md with revised workflow counts
- Updated workflow counts in PA file footers
- Updated root README.md folder structure counts

---

## 2026-06-11 — Consistency Review: Reconcile All Workflow Counts

### Fixed
- **Reconciled workflow counts across entire repository** — all 30 VS READMEs, value-stream-index.md, and root README.md now reflect actual workflow header counts from PA files
- **Corrected header in value-stream-index.md** — family count (9 → 8), process area count (95 → 94), grand total remains 1,400
- **Fixed VS-28 README** — removed duplicate PA-28.3 row
- **Fixed table formatting** in VS-07, VS-13, VS-20, VS-24 READMEs — removed extraneous pipe characters
- **Corrected VS-level totals** for 14 value streams where arithmetic or batch updates caused drift:

| VS | Before | After | PA-level Changes |
|---|---|---|---|
| VS-05 | 28 | 29 | PA-05.3: 12→13 |
| VS-07 | 134 | 136 | PA-07.2: 43→45 |
| VS-08 | 52 | 53 | PA-08.3: 10→11 |
| VS-11 | 42 | 45 | PA-11.2: 27→28 |
| VS-12 | 32 | 31 | PA-12.2: 7→6 |
| VS-13 | 59 | 60 | PA-13.2: 16→17 |
| VS-15 | 40 | 41 | PA-15.2: 23→24 |
| VS-16 | 29 | 32 | arithmetic fix (15+8+9=32) |
| VS-17 | 60 | 61 | PA-17.2: 7→8 |
| VS-19 | 67 | 70 | arithmetic fix (34+8+10+10+8=70) |
| VS-20 | 25 | 26 | PA-20.1: 8→9 |
| VS-22 | 55 | 55 | PA-22.1: 29→30 (total unchanged) |
| VS-24 | 23 | 26 | PA-24.3: 7→8, total recalculated |
| VS-28 | 14 | 18 | removed duplicate row, PA-28.3: 7 |

- **Updated root README** — folder structure counts, Key Metrics (94 process areas), document relationship diagram
- **Updated workflow-criticality-classification.md** — noted 233 unclassified workflows (1,400 − 1,167 classified)
- **Updated workflow-dependency-map.md** — corrected total workflow count reference
- **Updated all dates** to 2026-06-11 where stale

---

## 2026-06-10 — Add 15 New Workflows Across 12 Process Areas (W1400–W1414)

### Added
- **W1400**: Driver License Expiration Monitoring, LTO Compliance & Renewal Tracking (PA-06.2)
- **W1401**: Fleet Vehicle Annual LTO Registration Renewal & Motor Vehicle Inspection Compliance (PA-06.2)
- **W1402**: DC Seasonal Merchandise Pre-Staging, Forward-Pick Slot Reallocation & Promotional Lane Setup (PA-04.3)
- **W1403**: Store-Level Material Handling Equipment Inspection, Preventive Maintenance & Operator Safety Certification (PA-20.3)
- **W1404**: DENR Environmental Compliance Inspection Response, Documentation Package & Corrective Action Management (PA-22.2)
- **W1405**: Store-Level P&L Auto-Generation, Contribution Margin Analysis & Monthly Financial Performance Review (PA-17.4)
- **W1406**: Weekly Flash Sales Report, Chain-Wide KPI Dashboard & Executive Performance Summary (PA-17.4)
- **W1407**: Store Seasonal Department Reset, Category Space Reallocation & New Product Introduction Floor Execution (PA-07.1)
- **W1408**: ERP User Access Quarterly Review, Segregation of Duties (SoD) Audit & Excessive Access Remediation (PA-27.1)
- **W1409**: IT Change Advisory Board (CAB) Weekly Review, Risk Assessment & Deployment Approval (PA-27.1)
- **W1410**: Store Employee Inter-Location Transfer Processing, Labor Cost Reallocation & Benefit Continuity (PA-19.3)
- **W1411**: Import PO Customs Documentation Package Preparation, Broker Coordination & Compliance Checklist (PA-03.2)
- **W1412**: Store-Level Receiving Dock Safety Inspection, Material Handling Compliance & Incident Reporting (PA-07.3)
- **W1413**: DC-Level Cycle Count Discrepancy Root Cause Analysis, Corrective Action & Recount Protocol (PA-05.1)
- **W1414**: Customer Trade Account Credit Insurance Premium Review, Claims Filing & Recovery Management (PA-16.2)

### Updated
- Total workflows: **1,385 → 1,400** (+15)
- Updated all affected VS README files and value-stream-index.md with revised workflow counts
- Updated workflow counts in PA file footers

---

## 2026-06-10 — Add 20 New Workflows Across 9 Process Areas (W1380–W1399)

### Added
- **W1380**: Customer Post-Dated Check (PDC) Receipt, Register Management & Bank Deposit Processing (PA-16.3)
- **W1381**: Customer Bounced Check (DAIF) Resolution, Legal Action & BIR Reporting (PA-16.3)
- **W1382**: Customer Electronic Payment (PESONet/InstaPay) Reconciliation & Auto-Application (PA-16.3)
- **W1383**: Employee Resignation Processing, Clearance & Final Pay Computation — Philippine Labor Code (PA-19.5)
- **W1384**: Employee 13th Month Pay Computation, Proration & BIR Taxable Benefit Reporting (PA-19.5)
- **W1385**: Employee Separation Pay Computation, DOLE Clearance & Retirement Benefit Settlement (PA-19.5)
- **W1386**: Typhoon Early Warning Response, Store Pre-Closure Preparation & Post-Disaster Assessment (PA-24.2)
- **W1387**: Store-Level Flood Response, Inventory Elevation Protocol & Water Damage Recovery (PA-24.2)
- **W1388**: Store CCTV System Daily Health Check, Footage Retention & Incident Retrieval Processing (PA-23.2)
- **W1389**: Store After-Hours Burglary Alarm Response, Police Coordination & Incident Documentation (PA-23.2)
- **W1390**: Store POS Transaction Data Quality Validation, Anomaly Detection & Correction Processing (PA-28.2)
- **W1391**: Master Data Duplicate Detection, Merge Processing & Golden Record Management (PA-28.2)
- **W1392**: DC-Level Business Continuity Plan, Annual Tabletop Exercise & Recovery Time Objective Validation (PA-26.1)
- **W1393**: Store-Level IT Disaster Recovery, POS System Failover & Manual Operations Procedure (PA-26.1)
- **W1394**: Customer Trade Account Annual Credit Review, Tier Reclassification & Terms Adjustment (PA-11.1)
- **W1395**: Customer Trade Account Suspension, Reactivation & Delinquent Account Rehabilitation (PA-11.1)
- **W1396**: Store-Level Energy Consumption Benchmarking, Carbon Footprint Estimation & Reduction Target Tracking (PA-25.3)
- **W1397**: Philippine SEC Sustainability Reporting (Memo Circular No. 4) Annual Data Collection & Report Preparation (PA-25.3)
- **W1398**: Customer Churn Prediction Model, At-Risk Account Identification & Proactive Retention Campaign (PA-28.3)
- **W1399**: Store-Level Sales Forecasting Accuracy Monitoring, Model Drift Detection & Retraining Trigger (PA-28.3)

### Updated
- Total workflows: **1,365 → 1,385** (+20)
- Updated all affected VS README files and value-stream-index.md with revised workflow counts
- Updated workflow counts in PA file footers

---

## 2026-06-10 — Add 20 New Workflows Relevant to BuildRight Depot Model Company (W1348–W1367)

### Added
- **W1348**: Fleet Vehicle Preventive Maintenance Scheduling, Work Order & Parts Management (PA-06.2)
- **W1349**: Fleet Tire Lifecycle Management, Tread Monitoring & Replacement Scheduling (PA-06.2)
- **W1350**: Email Marketing Campaign Operations, Segmentation & Engagement Analytics (PA-14.2)
- **W1351**: Customer Referral Program Operations, Reward Fulfillment & Fraud Prevention (PA-14.2)
- **W1352**: DC Outbound Pick Accuracy Verification, Short-Ship Prevention & Error Reporting (PA-04.2)
- **W1353**: DC Outbound Staging, Loading Bay Scheduling & Dock Door Assignment Management (PA-04.2)
- **W1354**: Store Daily Cash Deposit Preparation, Armored Car Pickup & Bank Credit Reconciliation (PA-08.2)
- **W1355**: Typhoon & Natural Disaster Demand Surge Forecasting & Pre-Positioning (PA-02.1)
- **W1356**: Store-Level Demand Sensing & Local Event-Driven Forecast Adjustment (PA-02.1)
- **W1357**: Store Shift Optimization Based on Foot Traffic Analytics & Sales Pattern Analysis (PA-19.3)
- **W1358**: Seasonal Workforce Scaling, Temporary Hiring Ramp & Post-Season Right-Sizing (PA-19.3)
- **W1359**: Ecommerce Promotional Price Sync, Markdown Conflict Resolution & POS Price Parity Verification (PA-10.1)
- **W1360**: Omnichannel Inventory Reservation, Oversell Prevention & Multi-Channel Stock Allocation Governance (PA-10.1)
- **W1361**: Multi-Bank Cash Position Daily Aggregation & Automated Zero-Balance Sweep (PA-18.2)
- **W1362**: Vendor Payment Run Execution, File Generation & Multi-Bank Disbursement Processing (PA-18.2)
- **W1363**: Trade Professional VIP Priority Support Hotline & Dedicated Account Manager Escalation (PA-13.1)
- **W1364**: Customer Product Knowledge Base & DIY Self-Service Help Center Content Management (PA-13.1)
- **W1365**: DC Inbound Vendor ASN Pre-Receipt Verification & PO Matching Exception Management (PA-04.1)
- **W1366**: DC Inbound Damage Claim Processing, Vendor Chargeback & Freight Recovery Management (PA-04.1)
- **W1367**: BIR CAS Registration Renewal, System Change Notification & Annual Compliance Attestation (PA-22.2)

### Updated
- VS-02, VS-04, VS-06, VS-08, VS-10, VS-13, VS-14, VS-18, VS-19, VS-22 README.md — workflow counts
- value-stream-index.md — total: 1,312 → 1,340 workflows (reconciled all VS counts to match actual README.md totals)
- Root README.md — workflow total

---

## 2026-06-10 — Add 10 New Workflows Relevant to BuildRight Depot Model Company (W1318–W1327)

### Added
- **W1318**: Tool Rental Reservation, Waitlist Management & Demand-Based Fleet Scheduling (PA-12.2)
- **W1319**: Tool Rental Customer Safety Briefing, Liability Waiver & Equipment Operation Acknowledgment (PA-12.2)
- **W1320**: Supplier ESG Due Diligence Assessment & Sustainable Procurement Qualification (PA-25.3)
- **W1321**: ESG Target Setting, Quarterly Progress Tracking & Board Dashboard Reporting (PA-25.3)
- **W1322**: IT Disaster Recovery (DR) Failover Test Execution, Validation & Recovery Time Assessment (PA-26.1)
- **W1323**: Supply Chain Disruption Simulation & Alternate Sourcing Activation Drill (PA-26.1)
- **W1324**: Employee Retrenchment & Redundancy Processing (DOLE DO 174 Compliance) (PA-19.5)
- **W1325**: Employee Death-in-Service Benefits Processing & Beneficiary Claim Management (PA-19.5)
- **W1326**: Customer B2B Project Payment Plan Negotiation, Arrears Management & Restructuring (PA-16.3)
- **W1327**: Customer Trade Account Spend Analysis, Category Insights & Quarterly Business Review (PA-16.3)

### Updated
- VS-12, VS-16, VS-19, VS-25, VS-26 README.md — workflow counts
- value-stream-index.md — total: 1,282 → 1,292 workflows
- Root README.md — workflow total and folder description
- Reconciled PA-12.1, PA-16.1, PA-19.2, PA-19.3, PA-26.2 counts to match actual ## W entries

---

## 2026-06-10 — Add 20 New Workflows Relevant to BuildRight Depot Model Company (W1298–W1317)

### Added
- **W1298**: Consignment Inventory Reconciliation, Settlement & Ownership Transfer Processing (PA-05.3)
- **W1299**: Intercompany Transfer Pricing Review, Adjustment & Arm's-Length Compliance Documentation (PA-17.2)
- **W1300**: Trade Account Credit Limit Annual Review, Adjustment & Exposure Monitoring (PA-16.1)
- **W1301**: E-Wallet (GCash/Maya) Settlement Reconciliation & Discrepancy Resolution (PA-08.2)
- **W1302**: Typhoon Season Store Protection, Rapid Reopening & Post-Disaster Assessment Protocol (PA-07.2)
- **W1303**: Vendor Rebate, Co-Op Advertising Fund & Promotional Incentive Management (PA-03.3)
- **W1304**: BIR Computerized Accounting System (CAS) Registration, Compliance & Audit Readiness (PA-22.1)
- **W1305**: Catch-Weight & Variable-Quantity Item POS Pricing Verification & Scale Calibration Compliance (PA-08.3)
- **W1306**: Multi-Entity Statutory Benefits Consolidation, Remittance Reconciliation & Government Portal Compliance (PA-19.2)
- **W1307**: DC Cross-Dock Fast-Mover Expedited Receiving, Sortation & Same-Day Dispatch Processing (PA-04.1)
- **W1308**: B2B Project Bid, Tender Response & Government Procurement Compliance Management (PA-11.2)
- **W1310**: Import Letter of Credit (LC) Lifecycle Management, Amendment & Settlement Processing (PA-15.2)
- **W1311**: E-Commerce Product Review & Rating Management, Seller Response & Negative Review Escalation (PA-10.1)
- **W1312**: Store-Level Hazardous Material (Paint/Chemical/Solvent) Spill Response, Cleanup & Environmental Reporting (PA-24.3)
- **W1313**: Vendor-Supplied Merchandising Fixture, Display & Point-of-Purchase (POP) Material Lifecycle Management (PA-01.3)
- **W1314**: Customer Project Material List (Bill of Materials) Creation, Management & Reorder Tracking (PA-09.2)
- **W1315**: Delivery Vehicle Loading Optimization, Weight Compliance & LTFRB Regulation Adherence (PA-06.1)
- **W1316**: Loyalty Points Liability Accounting, Redemption Forecasting & Program Financial Management (PA-13.2)
- **W1317**: Store-Level Generator Backup Power Operations, Fuel Management & Load Shedding Protocol (PA-07.2)

### Updated
- Value Stream Index: 1,262 → 1,282 workflows (20 new across 16 process areas, 14 value streams)

---

## 2026-06-10 — Add 10 New Workflows Across 10 Process Areas (Batch 3) (W1268–W1277)

### Added
- **W1268**: E-Wallet (GCash/Maya) Daily Settlement & Reconciliation (PA-08.2)
- **W1269**: Customer Trade Account Application, Credit Assessment & Onboarding (PA-11.1)
- **W1270**: Seasonal Promotional Catalog Production, Printing & Store Distribution (PA-14.1)
- **W1271**: DC Inbound Import Container Devanning, Staging & Quality Sampling (PA-04.1)
- **W1272**: Store-Level Emergency Local Cash Purchase Authorization & Reimbursement (PA-07.3)
- **W1273**: Customer E-Commerce In-Store Return Drop-Off Processing & Cross-Channel Refund (PA-10.2)
- **W1274**: Customer Loyalty Points Financial Liability Monthly Valuation & Accounting Reserve (PA-13.2)
- **W1275**: Store-Level Daily Consignment Inventory Sales Reconciliation & Vendor Reporting (PA-05.1)
- **W1276**: POS Multi-Tender Split Payment Processing & Reconciliation (PA-08.1)
- **W1277**: Intercompany Warehouse Service Fee Monthly Calculation, Billing & Reconciliation (PA-17.2)

### Updated
- VS-04, VS-05, VS-07, VS-08, VS-10, VS-11, VS-13, VS-14, VS-17 README.md — workflow counts
- value-stream-index.md — total: 1,262 workflows (was 1,252)
- All affected PA files — TOC entries and footer counts

---

## 2026-06-09 — Add 20 New Workflows Across 16 Process Areas (W1167–W1186)

### Added
- **W1167**: Reverse Logistics & Vendor Return Shipment Management (PA-06.1)
- **W1168**: Direct Store Delivery (DSD) Receiving, Verification & Vendor Compliance (PA-06.1)
- **W1169**: Import Container Inbound Logistics, Port Drayage & DC Delivery (PA-06.1)
- **W1170**: Subcontractor Installation Daily Dispatch, Work Order & Capacity Management (PA-12.1)
- **W1171**: Installation Defect Punch List, Customer Walk-Through & Quality Sign-Off (PA-12.1)
- **W1172**: Tool Rental Fleet Procurement, Lifecycle Planning & Retirement Management (PA-12.2)
- **W1173**: High-Risk SKU Protection Plan & Product Security Fixture Deployment (PA-23.3)
- **W1174**: Loss Prevention Store Compliance Audit Program & Scoring (PA-23.3)
- **W1175**: Sustainable Packaging Reduction & Single-Use Plastic Elimination Program (PA-25.1)
- **W1176**: Green Procurement & Sustainable Vendor Certification Program (PA-25.2)
- **W1177**: Enterprise Data Governance Council, Standards & Stewardship Program (PA-28.2)
- **W1178**: Predictive Analytics Model Development, Deployment & Monitoring (PA-28.3)
- **W1179**: Store-Level Gift Card Sales, Redemption & Balance Management (PA-09.3)
- **W1180**: Government Procurement (PhilGEPS) Bidding, Accreditation & Public Sector Account Management (PA-11.2)
- **W1181**: BIR Point-of-Sale (POS) System Registration & CAS Compliance Maintenance (PA-17.3)
- **W1182**: Multi-Entity Cross-Company Workforce Scheduling & Labor Cost Allocation (PA-19.3)
- **W1183**: Store Lease CAM Reconciliation, Rent Escalation & Landlord Relationship Management (PA-20.1)
- **W1184**: Influencer & Home Improvement Content Creator Partnership Management (PA-14.2)
- **W1185**: Ecommerce Product Review, Rating & User-Generated Content Moderation (PA-10.1)
- **W1186**: Loyalty Program Partner Cross-Promotion & Third-Party Reward Integration (PA-13.2)

### Updated
- Total workflows: **1,153 → 1,173** (+20)
- Updated all affected VS README files, value-stream-index.md, and root README.md

---

## 2026-06-09 — Add 20 New Workflows Across 19 Process Areas (W1187–W1206)

### Added
- **W1187**: Post-Disaster Construction Material Demand Surge Fulfillment & Emergency Replenishment (PA-02.3)
- **W1188**: Consignment Inventory Monthly Reconciliation & Vendor Settlement Processing (PA-05.1)
- **W1189**: Cement & Bagged Material Shelf Life Expiry Monitoring & Proactive Markdown (PA-05.3)
- **W1190**: Inter-Island DC-to-Store RoRo & Ferry Consolidated Shipment Planning (PA-06.1)
- **W1191**: Construction Site Delivery Coordination, Access Assessment & Crane/Boom Truck Scheduling (PA-06.3)
- **W1192**: Post-Typhoon Store Damage Assessment, Insurance Claim & Rapid Reopening Protocol (PA-07.2)
- **W1193**: Heavy & Bulky Material Customer Pickup Scheduling & Loading Bay Priority Management (PA-07.3)
- **W1194**: Customer Whole-House Bill of Materials (BOM) Builder & Multi-Trade Package Assembly (PA-09.2)
- **W1195**: Mixed-Basket Multi-Origin Order Orchestration & Split Shipment Coordination (PA-10.2)
- **W1196**: Ship-from-Store Fulfillment Operations & Store-Level Inventory Reservation (PA-10.2)
- **W1197**: Government Agency & LGU Annual Procurement Catalog Listing & Price Registration (PA-11.2)
- **W1198**: Installation Material Kit Pre-Stage, Quality Check & Site-Ready Packing (PA-12.1)
- **W1199**: Import Letter of Credit (LC) Lifecycle, Amendment & Bank Release Management (PA-15.2)
- **W1200**: Trade Account Monthly Statement Review, Credit Limit Recalibration & Churn Prevention (PA-16.2)
- **W1201**: Intercompany Monthly Settlement Batch Processing & Netting Execution (PA-17.2)
- **W1202**: Store Daily Cash Collection, Armored Car Pickup & Bank Deposit Reconciliation (PA-18.1)
- **W1203**: Philippine Data Privacy Act (RA 10173) Compliance Audit, DPO Reporting & NPC Registration (PA-22.1)
- **W1204**: Store-Level Business Continuity Plan (BCP) Annual Update, Tabletop Exercise & Certification (PA-26.1)
- **W1205**: PCI-DSS Compliance for POS Payment Card Data & Annual QSA Audit Management (PA-27.3)
- **W1206**: AI-Powered Demand Forecasting Model Training, Accuracy Monitoring & Retraining Cycle (PA-30.2)

### Changed
- Updated all VS README files with revised workflow counts
- Updated value-stream-index.md: 1,173 → 1,193 workflows
- Updated root README.md workflow total

---

## 2026-06-09 — Review: Fix Count & Cross-Reference Issues

### Fixed
- **Fixed VS-16 workflow count** in `README.md` — changed from "17 workflows" to "23 workflows" to match actual PA file content (PA-16.1: 13 + PA-16.2: 6 + PA-16.3: 4)
- **Removed duplicate sentence** in `value-stream-index.md` — second occurrence of the WORKFLOW-FORMAT-GUIDE cross-reference was removed
- **Fixed broken link** in `requirement-workflow-matrix.md` — changed `workflows/README.md` (non-existent) to `workflows/value-stream-index.md`
- **Deduplicated classification entries** — removed 9 cross-tier duplicates (W59, W131, W132, W158, W257, W265, W266, W267, W271 appeared in two tiers) and 2 within-Tier-1 duplicates (W74, W76) from `workflow-criticality-classification.md`
- **Reconciled classification tier totals** — updated section headers and footer: Tier 1: 439, Tier 2: 499, Tier 3: 229 = 1,167 total
- **Added count clarification** — documented that 1,167 classified references include 14 parent/sub-variant grouping entries (e.g., W2, W5B, W9A) that appear as `###` sub-headings in PA files; 1,153 have dedicated `## W` section headers
- **Updated README Key Metrics** — simplified tier classification row with deduplicated totals and count explanation

---

## 2026-06-09 — Post-Review Cleanup

### Fixed
- **Added WHL-001, WHL-002, WHL-003** to `erp-requirements.md` — these DC/warehouse management requirements were referenced in the requirement-workflow matrix but had no formal requirement definition. Now formalized under R4 (Warehouse Management) with Must Have / Should Have priorities.
- **Removed dead link** to `_archive-domains/` in `value-stream-index.md` — the archive directory was deleted in a prior commit but the reference remained.
- **Reconciled workflow counts** — removed 4 duplicate classification entries (W1163, W1164, W1165, W1166 appeared in two tier sections) from `workflow-criticality-classification.md`. Corrected title from 1,147 → 1,167. Deduplicated 9 cross-tier and 2 within-tier entries. Updated summary totals (Tier 1: 439, Tier 2: 499, Tier 3: 229 = 1,167 classified).
- **Fixed "5 terminals" → "3 terminals"** across `PA-07.1-store-daily-management.md`, `PA-22.1-regulatory-permits-and-licenses.md`, and `PA-27.1-service-management.md` — the model company profile specifies 3 POS terminals per store but multiple workflow sections referenced 5 terminals from an earlier design iteration. Corrected all related staffing calculations, time estimates, and skim event volumes.
- **Fixed MER-028 reference** in GOV-053 — changed undefined `MER-028 (sample/demo inventory)` to `MDM-025 (digital asset & product content master — demo inventory)`.
- **Fixed XXX-000-000 TIN format** in COM-011 — changed to standard Philippine TIN format `XXX-XXX-XXX-T00`.

### Updated counts
| Metric | Before | After |
|---|---|---|
| Requirements | 730 | 733 (+WHL-001/002/003) |
| Must Have | 429 | 431 (+WHL-002, WHL-003) |
| Should Have | 295 | 296 (+WHL-001) |
| Classified workflows | 1,168 (with duplicates) | 1,167 (deduplicated) |
| Tier 2 | 501 | 499 (−2 duplicates) |
| Tier 3 | 228 | 226 (−2 duplicates) |

---

## 2026-06-09 — Comprehensive Review & Restructuring

### Changed
- Reorganized 1,143 workflows from 48 domain files to 30 value streams (91 process areas).
- Removed archived domain files — fully superseded by value stream structure.
- Reconciled counts, added out-of-scope section, added document relationship diagram.
- Fixed structural issues, split large README, fixed tier guidance.
- Added Batches 8–12 (W983–W1162) — 100 new Philippine-context operational workflows.
- Multiple review rounds fixing inconsistencies across documents.

---

## 2026-06-08 — Initial Repository

### Added
- Complete model company profile for BuildRight Depot Corp. (200 stores, 4 DCs, Philippines).
- 730 ERP requirements across 37 categories (R1–R32 + operational gap closures).
- 1,153 operational workflows across 30 value streams.
- 67 internal controls (31 preventive, 36 detective).
- Cross-reference documents: requirement-workflow matrix, dependency map, system touchpoint map.
- Technical guidelines: POS hardware specs, infrastructure, integration architecture, security.
- Data migration mapping templates, mobile app strategy, assumptions & design decisions.
- Validation script (`validate-repo.sh`).
