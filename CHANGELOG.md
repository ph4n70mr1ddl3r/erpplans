# Changelog

> Track major changes to the BuildRight Depot ERP Plans repository.

---

## 2026-06-19 — Workflow gap analysis (Pass 20): add VS-165–VS-167 (72 workflows W4817–W4888)

A twentieth gap-analysis pass, re-running the established methodology (defining terms appearing in
**zero** PA files as dedicated workflow headers, no dedicated owner, conflated with adjacent covered
coverage or reduced to a single-domain slice), surfaced three further genuinely-unowned operational
disciplines relevant to BuildRight's operations after nineteen prior passes had been judged complete.
One is a genuinely-uncovered statutory licensing regime and two are scattered-slice consolidations
following the proven VS-161 TPRM pattern:

- **[VS-165 — PCAB Contractor Licensing & RA 4566 Construction Contractor Compliance](01-model-company/workflows/VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/README.md)** (Governance & Assurance, W4817–W4840, 24 workflows) — BuildRight as a *licensed construction contractor* under RA 4566 (Contractors' License Law): obtaining/maintaining/renewing its own PCAB license for the installation (VS-12), design-build (VS-66), government delivery-and-install bids (VS-46/VS-11.2), bulky install (VS-143), and own-construction (VS-20) work where it is the contractor of record — a go-to-market precondition with criminal liability (Sec. 6/8) for unlicensed contracting. 'PCAB license' / 'RA 4566' / 'PCAB project registration' appeared in zero PA files for BuildRight's *own* license; every existing PCAB reference verifies *someone else's* license (customer trade-pro W590 in VS-09.1/VS-43.1; vendor/contractor eligibility W162 in VS-11.2/VS-46.1; employee PCAB tracking VS-19.4). Covers licensing strategy/entity-eligibility, application & registration, category/upgrade, annual renewal & calendar, CIAP board engagement, multi-entity coverage, **project registration per contract**, performance/surety bonding linkage (VS-116), construction safety & health (DOLE D.O. 13), bid-support license proof, subcontractor license cascading, warranty/acceptance/retention, **mechanic's-lien rights & lien waivers**, inspection response, license-condition monitoring, PRC engineer-of-record credentialing, **unlicensed-contracting risk control**, JV/consortium & foreign-contractor licensing, penalty/reinstatement, and analytics.
- **[VS-166 — Regulatory License, Permit & Accreditation Portfolio Management](01-model-company/workflows/VS-166-regulatory-license-permit-and-accreditation-portfolio-management/README.md)** (Governance & Assurance, W4841–W4864, 24 workflows) — the unified cross-domain discipline owning a single register of **every statutory license/permit/certification/accreditation** held by the 5 entities across ~205 sites (LGU business/mayor's permit, barangay clearance, BFP FSIC, DENR ECC/hazwaste-generator, BIR + CAS permit + ATP, DTI-BPS, PCAB, PhilGEPS, FDA-adjacent/FPA/BPI, PEZA/BOI, SSS/PhilHealth/Pag-IBIG, DOLE OSH, LTO/LTFRB, BSP agency, NPC) numbering in the thousands — with the renewal calendar, expiry-risk engine, evidence repository, regulator-change monitor, multi-site renewal campaigns, inspection-response hub, third-party permit-service (fixer/consultant) management, lapsed-permit remediation, and executive compliance dashboard. 'license portfolio' / 'permit portfolio' / 'regulatory inventory' / 'centralized compliance calendar' appeared in zero PA files; each compliance domain owned its execution slice (VS-22/76/79/114/117/138/165/46/06) but none owned the unified register (the VS-161 TPRM consolidation pattern).
- **[VS-167 — Workforce Background Screening, Credentialing & Personnel Vetting](01-model-company/workflows/VS-167-workforce-background-screening-credentialing-and-personnel-vetting/README.md)** (People, W4865–W4888, 24 workflows) — the unified cross-category screening discipline covering employees (~6,715 + ~1,200–1,600 hires/yr), contingent/outsourced labor (~10–20%), vendor/3PL site-access personnel (drivers/delivery/service), and executives — through a centralized screening program, role-based packages, screening-vendor governance, consent/RA 10173 compliance, adverse-action/fair-chance due process, and ongoing re-screening, to control negligent-hiring and insider-risk exposure. 'background screening program' / 'pre-employment screening' / 'credentialing' / 'workforce vetting' appeared in zero PA files for a cross-category program; the only existing screen was the single **contingent-worker** workflow W3223 in VS-98.2 (a slice), plus an onboarding step in VS-121 and license-only driver checks W1400 — unified here following the VS-161 pattern.

**Counts:** 160 → **163 value streams** · 484 → **493 process areas** · 4,668 → **4,740 workflows**
(W4817–W4888, 3 value streams × 3 process areas × 8 workflows). All 72 new workflows are
**unclassified** and carry a keyword-driven proposed tier in the regenerated
[`workflow-criticality-proposed.md`](01-model-company/workflows/workflow-criticality-proposed.md)
(3,523 → 3,595 unclassified); the family impact is Governance & Assurance +48 (VS-165 + VS-166)
and People +24 (VS-167).

**Candidates considered but rejected as adequately covered / out of charter** (documented in
[`workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md)): timber & forest-
products legality / FSC-PEFC chain-of-custody (owned by VS-25.2 sustainable sourcing + VS-131 human-
rights DD, explicitly cross-referenced); customer/vendor bankruptcy & insolvency claims (covered by
VS-16 AR/collections W287/W16.3); trade promotion management / trade spend / vendor deductions
(covered by VS-39/VS-14/VS-58); BIR e-invoicing / CAS permit-to-use / ATP (6 dedicated workflows in
VS-79/VS-08.3); energy-supply procurement / RCOA / WESM (owned by VS-120.1); centralized SEC
reportorial / corporate-secretary (covered by VS-36 + VS-100.3); in-store specialty services (key
cutting/locksmith/engraving/LPG — covered by VS-09/VS-114); mechanic's-lien management (folded into
VS-165 PA-165.2 W4831); conflict minerals / 3TG (covered by VS-131 + VS-25.2); guest WiFi /
captive-portal (out of charter, VS-27/VS-14); and employee pension / gift-card escheat beyond gift
cards / lone-worker safety (covered or too narrow).

`07-methodology/validate-repo.sh` still reports **0 errors / 3 informational warnings** after the
additions (Check 9 grand total 4,740 = actual PA header count 4,740; Check 1 all 3,595 proposed IDs
resolve to headers). All cross-document totals (README, executive-summary, value-stream-index,
workflows/README, criticality classification, dependency map, touchpoint map,
requirement-workflow-matrix) were reconciled to the new counts.

---

## 2026-06-19 — Workflow gap analysis (Pass 19): add VS-162–VS-164 (72 workflows W4745–W4816)

A nineteenth gap-analysis pass, re-running the established methodology (defining terms appearing in
**zero** PA files as dedicated workflow headers, no dedicated owner, conflated with adjacent covered
coverage), surfaced three further genuinely-unowned operational disciplines relevant to BuildRight's
operations. Each is a distinct big-box-retail operational capability that the surrounding coverage
made appear owned:

- **[VS-162 — Customer Pickup Truck & Cargo Van Rental (Self-Haul) Operations](01-model-company/workflows/VS-162-customer-pickup-truck-and-cargo-van-rental/README.md)** (Sell & Serve, W4745–W4768, 24 workflows) — the "Load N Go" big-box self-haul rental (2–3 trucks + 1 van per store ≈ 600–800 vehicles group-wide) that converts the "I can't get it home" bulky-merchandise basket-abandonment (lumber/tile/appliance/furniture — ~36% of SKUs) into a same-day completed sale plus rental/fuel/LDW income. 'pickup truck rental' / 'cargo van rental' / 'self-haul rental' appeared in zero PA files; distinct from VS-06 (goods delivery fleet), VS-12.2 (item/tool rental), VS-74/VS-56 (delivery services), VS-141 (employee transport) — this rents a titled registered motor vehicle to a customer to self-drive under motor-vehicle-liability law (LTO registration, CTPL/RA 10006, driver-license verification, LDW/deductible, telematics, theft/non-return recovery).
- **[VS-163 — Electric Vehicle (EV) Charging Station Host Network Operations](01-model-company/workflows/VS-163-electric-vehicle-ev-charging-station-host-network-operations/README.md)** (Asset & Infrastructure, W4769–W4792, 24 workflows) — BuildRight as the property host & network operator deploying EV charging across ~205 large parking-rich sites, converging its EV-charger merchandise (Electrical category), rooftop solar/prosumer program (VS-108), energy-efficiency/RA 11285 program (VS-120), and sustainability brand (VS-25) under the RA 11697 (EVIDA, 2022) electrification tailwind — capturing the dwell-time basket, own-solar energy sales, decarbonization, and property future-proofing. 'EV charging station host' / 'EVSE host network' / 'OCPI roaming' appeared in zero PA files; distinct from VS-108 (own-consumption generation — this *sells* energy/services to EV drivers), VS-120 (own energy efficiency), VS-06/VS-61 (own diesel fleet fueling — this also owns the forward green-fleet charging path), VS-138 (general facilities). Covers strategy/CPO-partnering, siting, ERB/Meralco utility interconnection, solar/storage peak-shaving, OCPP/OCPI CSMS & roaming, billing/payment/loyalty, EVSE maintenance, accessibility (RA 7277), safety, compliance, and network/decarbonization analytics.
- **[VS-164 — Smart Locker & Automated Parcel Collection Network](01-model-company/workflows/VS-164-smart-locker-and-automated-parcel-collection-network/README.md)** (Sell & Serve, W4793–W4816, 24 workflows) — a network of automated self-service collection lockers (in-store, parking-lot drive-up, and off-site transit/condo/mall) extending BOPIS beyond the counter and beyond store hours, unlocking returns drop-off and a 3P-parcel-pickup revenue stream (the Amazon-Hub / Lazada-locker model) for ~42,900 ecommerce orders/month and ~2.8M monthly footfall. 'smart locker network' / 'automated parcel collection' / 'returns locker' appeared in zero PA files; distinct from VS-10 (the BOPIS fulfillment *transaction* at the counter — this owns the *locker network infrastructure & channel*), VS-149 (in-store unattended *selling* tech — this owns outdoor/transit/off-site *parcel lockers*), VS-93/VS-60 (fulfillment), VS-32 (returns — this owns the *locker returns-drop-off channel*). Covers network strategy/vendor, siting/capacity, BOPIS-to-locker staging & access-control, returns drop-off, overflow/abandonment, 3P carrier integration, ERP/OMS/loyalty integration, security/anti-theft, accessibility (RA 7277/BP 344), privacy (RA 10173), uptime/SLA, and analytics.

**Counts:** 157 → **160 value streams** · 475 → **484 process areas** · 4,596 → **4,668 workflows**
(W4745–W4816, 3 value streams × 3 process areas × 8 workflows). All 72 new workflows are
**unclassified** and carry a keyword-driven proposed tier in the regenerated
[`workflow-criticality-proposed.md`](01-model-company/workflows/workflow-criticality-proposed.md);
the family impact is Sell & Serve +48 and Asset & Infrastructure +24.

**Candidates considered but rejected as adequately covered / out of charter** (documented in
[`workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md)): heavy/pro
construction equipment rental (covered by W1094 partner-coordination model in VS-09.1 + W1062
scaffolding); self-storage/mobile-storage containers, in-store cafe/F&B, notary/blueprint/photo/
coin-machine, and pet/aquarium/pharmacy/dry-cleaning (out of the home-improvement retail charter).

`07-methodology/validate-repo.sh` still reports **0 errors / 3 informational warnings** after the
additions (Check 9 grand total 4,668 = actual PA header count 4,668; Check 1 all 3,523 proposed IDs
resolve to headers). All cross-document totals (README, executive-summary, value-stream-index,
workflows/README, criticality classification, dependency map, touchpoint map,
requirement-workflow-matrix) were reconciled to the new counts.

---

## 2026-06-19 — Whole-repo consistency review: broken anchors, scope ambiguities, vendor/TIN reconciliation & en-dash normalization

A full-repository read-through surfaced and resolved six classes of inconsistency. The
validator (`07-methodology/validate-repo.sh`) continues to report **0 errors / 3 informational
warnings** (unchanged — the warnings track known in-progress content gaps: boilerplate
analysis fields, Automation/Controls field adoption, and unclassified workflows).

**1. Broken cross-document anchor links (factual defects).** Two documents linked to a
profile heading using the wrong slug: `model-company-profile.md#143-integration-touchpoints`.
The actual heading is `### 14.3 Active Integration Touchpoints`, whose anchor is
`#143-active-integration-touchpoints`. Fixed in:

- `07-methodology/technical-guidelines.md` §3.1 (intro to the Integration Methods table)
- `01-model-company/erp-requirements.md` NFR-012 (Integration Capability)

**2. Goods Receipts scope ambiguity (`model-company-profile.md` §15.1).** The
`Goods Receipts (Inbound) ~6,000 / ~72,000` row was DC-only, but §7.1 also documents
~500–600 DSD receipts/month and `data-volumes-and-integrations.md` §1.1 reports the two
streams separately. This was the same merchandise-vs-total scope ambiguity previously
resolved for AP invoices. Added a **Goods Receipts scope** note (mirroring the existing
AP scope note) clarifying that total inbound incl. DSD is ~6,500–6,600/month
(~79,000–79,200/year). (Profile v2.18 → v2.19.)

**3. Vendor master inconsistencies (`data-migration-mapping.md` §2.2).** Two reconciliations:

- **Target record count** `~1,000 active vendors` → `~800–1,000 active vendors (per
  model-company-profile.md §6.5)` — the migration template previously stated only the upper
  bound of the canonical range.
- **Vendor TIN cleansing rule** `Validate format (XXX-XXX-XXX-XXX)` → `Validate format
  (XXX-XXX-XXX or XXX-XXX-XXX-XXX)` — accepts both Philippine TIN formats per COM-011 and
  the §3 Data Cleansing Rules table, which already listed both.

(v2.2 → v2.3.)

**4. TOC round-range label (`erp-requirements.md`).** The TOC row `R19–R24 | Operational
Gap Closure (Rounds 11–21)` was misleading: R19–R24 actually covers Rounds 11, 13, 14, 16,
17, 19, and R32 separately covers Round 21. Reworded to `Rounds 11–19` so it no longer
contradicts the R32 row (`Round 21`). (No requirement count or ID changed — 733 across 38
categories, all priorities unchanged.)

**5. Repository Layout completeness (`WORKFLOW-FORMAT-GUIDE.md`).** The `workflows/` layout
diagram listed 7 support files but omitted `README.md` (the navigation hub & quick-stats
entry point documented elsewhere as the start-here file). Added `README.md` as the first
entry so the diagram lists all 8 support files actually present.

**6. En-dash normalization for numeric ranges (repo-wide typography).** Approximate numeric
ranges written with a hyphen (`~800-1,000`, `~30-60`, `~5,000-8,000`) were normalized to the
en-dash form (`~800–1,000`, `~30–60`, `~5,000–8,000`) used by the dominant convention across
the workflow PA files and support docs. 584 substitutions across 63 files; the pattern is
narrow (`~<digits/commas>-<digits/commas>` only) so it does not touch requirement IDs
(`POS-013`), value-stream IDs (`VS-07`), day-offsets (`T-7`/`T-14`), compound modifiers
(`30-day`, `5-year`), or unsuffixed numeric ranges. Non-tilde ranges (e.g. `80-95%`, `20-30
SKUs`) are deliberately left for a future pass — they require a richer pattern to avoid
colliding with ID/version tokens.

**Version stamps bumped** on the four substantively-edited files (`model-company-profile.md`,
`data-migration-mapping.md`, `technical-guidelines.md`, `WORKFLOW-FORMAT-GUIDE.md`);
`erp-requirements.md` uses per-section stamps and its changes are cross-reference hygiene
only.

---

## 2026-06-19 — BIR record retention canonicalized to 10 years (TRAIN/NIRC) across all documents

Resolves the retention-period inconsistency flagged in the prior pass (7 years in the
foundational summary docs vs 10 years in the newer detailed workflow docs). Under the
**National Internal Revenue Code (NIRC) Sec. 235 as amended by the TRAIN Act (RA 10963)**,
books of accounts and the supporting accounting/invoice records (including CAS/e-invoice
records under RR 11-2024) must be **preserved for 10 years** (5 + 5). 10 years is now the
single canonical retention period for BIR/tax/accounting records, applied to ~85 references
across ~45 files. `validate-repo.sh` still reports **0 errors / 3 informational warnings**
(unchanged). **No workflow, requirement, control, value stream, or grand-total count changed.**

**Canonical sources updated** (these are the figures every other doc references):

- **`erp-requirements.md`** — `NFR-006` Data Retention `7 years (BIR)` → **`10 years (BIR per
  TRAIN/NIRC — Sec. 235, as amended by RA 10963)`**; `DOC-005` → 10-year; `DOC-008` `BIR 7-year`
  → `BIR 10-year`; `FIN-062` (Form 2307 vendor certificates) `5-year retention per BIR` →
  **10-year** (2307 retention aligns with the books-of-accounts period).
- **`assumptions-and-design-decisions.md` A6.5** — `7-year data retention` → **10-year**;
  storage sizing recomputed **~700 GB over 7 years → ~1,000 GB over 10 years** (~100 GB/year).
- **`model-company-profile.md` §15.3** — `Data retention | 7 years` → **10 years** (v2.18).
- **`data-volumes-and-integrations.md` §1.2** — storage row relabelled **`10-Year Retention |
  ~1,000 GB (uncompressed); ~700 GB with compression`** (was 7-Year / ~700 GB / ~500 GB)
  (v4.4).
- **`technical-guidelines.md` §2.3** — `Data retention | 7 years` and `Data backup | … +
  7-year archive` → **10 years** (v2.3).
- **`requirement-workflow-matrix.md`** — `NFR-006`, `DOC-005`, `POS-052` rows and the
  NFR column-convention example updated 7 → 10.

**Detailed workflow documents** (VS-NN/PA-NN.N files) updated from 7 → 10 where they state a
BIR/tax/accounting-records retention: VS-01.1, VS-03.2, VS-03.4, VS-07.1, VS-07.2, VS-07.4,
VS-08.1, VS-08.3, VS-09.1, VS-10.1, VS-10.2, VS-13.1, VS-15.1, VS-16.3, VS-17.1, VS-17.3,
VS-17.4, VS-19.5, VS-22.1, VS-22.2, VS-24.2, VS-26.3, VS-27.1, VS-27.2, VS-27.3, VS-28.2,
VS-29.2, VS-30.3, VS-35.2, VS-35.3, VS-40.3, VS-43.1, VS-59.1, VS-59.2, VS-71.1, VS-74.2,
VS-76.2, VS-76.3, VS-157.3, VS-158.3. VS-17.3 / VS-22.1 NIRC references corrected from the
outdated "minimum 5 years per NIRC" to **"10 years per NIRC (TRAIN RA 10963)"**.

**Storage-sizing downstream updates:** the data-warehouse / backup-capacity figure that was
sized to the 7-year horizon is recomputed to the 10-year horizon in `VS-28/PA-28.2` (`700 GB
over 7-year` → `1,000 GB over 10-year`; DW volume `~700 GB` → `~1,000 GB`; backup capacity
check `700 GB` → `1,000 GB`).

**Deliberately left as 7 years (not BIR accounting records — different regulatory/operational
context):**

- **CCTV footage prosecution tier** (`LP-002`, `VS-23/PA-23.2`) — governed by criminal-procedure
  prescriptive periods, not BIR; the VS-23.2 parenthetical was reworded from "(aligned with
  BIR/legal requirements)" to explicitly note CCTV is separate from the 10-year BIR
  accounting-records retention, removing the misleading BIR tie.
- **Fixed-asset depreciation useful lives** (`VS-35.1` forklifts 7 years; `VS-40.3` generator
  7 years, signage 7–10 years) — PFRS useful-life estimates, not retention.
- **IT hardware useful life** (`VS-27.1` POS terminals 5–7 years) — hardware refresh cycle.
- **Vehicle resale cycle** (`VS-06.2` 6–7 years) — fleet economics.
- **CREATE Act Income Tax Holiday** (`VS-17.3` 4–7 years) — tax-incentive duration.
- **Store-remodel / refurbishment cycle** (`VS-109`, `workflow-gap-analysis.md` 5–7 years) and
  **coastal-paint maintenance cycle** (`VS-09.2` 5–7 years inland) — operational cycles.
- **Metrology legal-for-trade retention** (`VS-115.1` 3–7 years) — weights-&-measures rule.
- **Corporate legal correspondence** (`VS-36.1` 7 years) — corporate-governance retention, not a
  BIR accounting record.
- **DENR environmental/timber-sourcing documentation** (`VS-25.1` 7-year DENR audit archive) and
  **rainwater-harvesting ROI payback** (`VS-25.1` 3–7 years) — DENR-governed / financial
  payback, not BIR.

---


## 2026-06-19 — Whole-repo consistency review pass: TOC count drift, stale POS/documented-workflow figures, AP-volume scope ambiguity

A top-to-bottom read of every summary/cross-reference document and a sample of high-traffic
workflow PA files, looking for inconsistencies, ambiguities, and stale figures that
`validate-repo.sh` does not already catch (it checks counts, IDs, cross-references, and table
structure — not whether a free-text figure matches its canonical value, nor whether a TOC
category count matches its actual row count). `validate-repo.sh` still reports **0 errors / 3
informational warnings** (unchanged). **No workflow, requirement, control, value stream, or
numeric grand total changed.**

- **`01-model-company/erp-requirements.md` (Table of Contents)** — the per-category counts had
  drifted out of sync with the actual row counts as letter-suffixed requirements were added in
  later rounds, so the TOC over-summed (to ~754 vs the stated 733 total). Corrected five rows so
  the TOC now sums to exactly 733 and every count matches the actual prefix-row count:
  - **R3 Procurement** `PUR … 43` → **45** (PUR-025a/b added: 43 base + 2 suffixed).
  - **R4 Warehouse Management** `WMS-001 – WMS-023 | 23` → **`WMS-001 – WMS-023, WHL-001 – WHL-003 | 26`** — the 3 WHL rows live in the R4 section but were previously uncounted in the TOC (WHL was a "ghost" prefix not mapped to any TOC row).
  - **R5 POS & Retail** `117` → **118** (POS-014a, POS-022a added).
  - **R14 Non-Functional** `41` → **42** (NFR-022a added).
  - **Additional (Various)** `87` → **59** — the 13 listed prefixes (COM, ENG, ESG, HAZ, HSE, LOG, MER, MKT, MNT, PRJ, PROP, REG, AUD) actually total 59; the old 87 was stale and contributed the bulk of the TOC over-sum. (WHL moved into the R4 row above.) The `> Total: 733 …` line and the Must/Should/Nice split (431/296/6) were already correct and unchanged.
- **`VS-22/PA-22.1` (Regulatory Permits & Licenses)** — the BIR EIS e-invoicing narrative said
  *"~5–10M POS transactions monthly across 200 stores"*. The canonical POS volume (per
  `data-volumes-and-integrations.md` §1.1, `model-company-profile.md` §5, and `VS-08/PA-08.2`)
  is **~2.8M POS transactions/month (~93,000/day)**. The 5–10M figure was ~2–4× too high
  (likely a stale draft figure); corrected to *~2.8M POS transactions monthly (~93,000/day)*.
- **`VS-133/README.md` + `workflows/workflow-gap-analysis.md` §3 (gap #47, VS-133)** — both
  narrative justifications for VS-133 (Operational Excellence) cited a stale *documented
  workflows* count in present tense: README said *"BuildRight runs ~3,900 documented workflows"*
  and the gap-analysis said *"running ~3,996 documented workflows"* (snapshots from Pass 9 and
  Pass 10 respectively). Every other figure in the same paragraphs (6,715 employees, PHP 62.3B,
  200 stores, 4 DCs, 2.8M transactions) is current, so the workflow count is the lone stale
  figure; both corrected to **~4,596** (current grand total) so the two narratives agree with
  each other and with the rest of the repository.
- **`model-company-profile.md` §15.1 (ambiguity resolution)** — the Transactional Volumes table
  row `AP Invoices | ~6,715 | ~80,500` is the merchandise-only AP figure (3-way match per W7,
  per the 2026-06-19 AP-annual-total reconciliation), but the unqualified label read as **total**
  AP and contradicted the ~8,500–9,500/month total-AP figure in §10.2 and
  `data-volumes-and-integrations.md` §1.1. Relabelled to **`AP Invoices (merchandise, 3-way
  match per W7)`** and added a scope note pointing to the total-AP basis in §10.2 and
  `data-volumes-and-integrations.md` §1.1. The numeric figure (~6,715 / ~80,500) is unchanged
  (deliberately canonicalized earlier). Document version bumped 2.16 → 2.17.
- **`requirement-workflow-matrix.md` (ambiguity resolution)** — added a *Column convention*
  note under How-to-Read clarifying that the 3rd column is **Priority** (M/S/N) for every
  section except **R14 NFR**, which uses the **Target** spec value (99.9%, < 3 sec, 7 years,
  etc.) since the target is the operative spec for an NFR; NFR priorities remain in
  `erp-requirements.md` R14. Previously a reader scanning the priority column encountered 17
  NFR rows whose 3rd cell held a target value rather than M/S/N — locally clear from the R14
  header but inconsistent with the top-level legend.

> **Known inconsistency deliberately left for a domain decision — BIR record retention: 7 vs 10
> years.** The foundational summary documents use **7 years (BIR)** as the canonical retention
> period — `NFR-006`, `DOC-005`, `model-company-profile.md` §15.3, `assumptions-and-design-
> decisions.md` A6.5 (which drives the ~700 GB / 7-year storage sizing), `technical-guidelines.md`
> §2.3, and ~6 internal-control references — while the newer detailed workflow documents use **10
> years (BIR)** for the same tax/accounting records: `VS-22/PA-22.1` (e-invoicing), `VS-88`
> (Document Control, incl. README and PA-88.2/88.3), and `PRJ-002` (project close-out). Under
> TRAIN (RA 10963) the BIR retention for books of accounts and accounting/e-invoice records is
> **10 years** (5 + 5); the 7-year figure in the foundational docs is the older/conservative
> number. Reconciling this is a **substantive tax-compliance and storage-sizing decision** (it
> changes NFR-006, A6.5 storage math, and multiple control references) and is deferred to a
> domain review rather than made unilaterally in a documentation-consistency pass. Flagged here
> so the next reviewer can decide which figure to canonicalize.

---


## 2026-06-19 — Cross-document figure consistency review (bank list, bank-account count, headcount, AP annual total) & ambiguity resolution

A whole-repo cross-reference review of the overview and high-traffic workflow documents found
a family of **stale figures that contradicted the canonical bank list / headcount / AP volume**
established in earlier passes, plus one ambiguity. None were caught by `validate-repo.sh`
(which checks counts, IDs, cross-references, and table structure — not whether a free-text
figure matches the canonical value). `validate-repo.sh` still reports **0 errors / 3
informational warnings** (unchanged). No workflow, requirement, control, value stream, or
grand total changed.

- **`VS-18/PA-18.1` (Cash Positioning & Forecasting)** — W233 (Cash Flow Forecasting &
Liquidity Management) carried a stale, pre-bank-reconciliation footprint: the Volume field
and three surrounding prose lines said "~50 bank accounts" and listed **Security Bank** as
the fourth bank. The canonical footprint (used 9× elsewhere in the same file and across
`VS-18/PA-18.2`, `model-company-profile.md` §10.4, `data-volumes-and-integrations.md`,
`erp-requirements.md` FIN-009, and `technical-guidelines.md`) is **~210 bank accounts across
4 banks (BDO, BPI, Metrobank, Chinabank)**. All four references in W233 were corrected to
~210 accounts and Chinabank. (Security Bank legitimately remains where it is a *customer*
financing partner rather than BuildRight's own bank — e.g. `VS-14/PA-14.3` co-branded card,
`VS-09/PA-09.1` home-improvement loan referrals — and was left untouched.)
- **`VS-15/PA-15.2` (Vendor Payment & Reconciliation)** — the LC-management pain point said
"maintaining LC facilities across **3 banks**"; corrected to **4 banks** to match the
canonical banking footprint (`VS-18/PA-18.2`: "4 banking relationships (BDO, BPI,
Metrobank, Chinabank)").
- **`VS-19/PA-19.2` (Payroll & Compensation)** — W1527 (SSS/PhilHealth/Pag-IBIG Contribution
Filing) Volume field said "~5,800–6,500 employees"; corrected to **~6,715 employees**, the
canonical total headcount (`model-company-profile.md` §4; `README.md`).
- **`model-company-profile.md` §15.1 + `VS-22/PA-22.3`** — the annual AP-invoice figure was
**~78,000**, which implies ~6,500/month and is inconsistent with the canonical monthly
merchandise-AP figure of ~6,715 (§10.2). Corrected to **~80,500** (= ~6,715 × 12) in both
the §15.1 Transactional Volumes table and the downstream EIS-onboarding Volume field in
`VS-22/PA-22.3`.
- **`model-company-profile.md` §9.1 (ambiguity resolution)** — the Customer Segments table
listed "Ecommerce | 5%" of revenue, which reads as a direct contradiction of §9.4 / §8.5 /
assumptions A1.4, where ecommerce is ~2.9% of revenue (Year-1 actual, ramping to ~5% in Year 2).
Rather than alter the pervasive "55% B2C / 30% Trade / 10% Corporate / 5% Ecommerce" split
(cited in 9+ workflow/analytics docs), the table is now annotated as the **strategic target
segment mix** (steady-state, ~95% in-store / ~5% ecommerce = Year-2 target), explicitly
distinguished from the **Year-1 actual** revenue split in §9.4 (~97.1% in-store / ~2.9%
ecommerce). The apparent 5%-vs-2.9% conflict is thereby resolved without churning the
many downstream "55% B2C" references.
- **`workflows/workflow-gap-analysis.md`** — header readability: "Pass 15 and Pass 16
(2026-06-17), Pass 17 (2026-06-17)" collapsed to "Pass 15, Pass 16, and Pass 17 (all
2026-06-17)" since all three share the same date.

> **Deliberately not changed:** the monthly total-AP figure "~8,500–9,500" (§10.2 + ~12
> downstream references across 8 files). 6,715 + 2,000–3,000 sums to ~8,700–9,700, so the
> stated total is ~2% soft at each bound — but it is an explicitly approximate ("~") figure
> that was deliberately canonicalized in the v4.3 data-volumes reconciliation and is used
> consistently repo-wide, so it was preserved rather than rippling a new range through 12+
> locations.

---

## 2026-06-19 — Volume-unit consistency review (monthly figures mislabeled as daily) & wording fixes

A prose-level review of the overview and high-traffic workflow documents found a small
family of **volume figures stated with the wrong time unit** — the canonical monthly POS
total (~2.8M transactions/month, i.e. ~93,000/day per `data-volumes-and-integrations.md` §1.1)
was written as a *daily* figure in four places, and one per-store card figure carried the
same monthly-as-daily error. None were caught by `validate-repo.sh` (which checks counts,
IDs, cross-references, and table structure — not the unit attached to a free-text figure).
Two further wording fixes resolved an overclaim and an ambiguity. `validate-repo.sh` still
reports **0 errors / 3 informational warnings** (unchanged). No workflow, requirement,
control, value stream, or grand total changed.

- **`01-model-company/erp-requirements.md`** — NFR-031 (Data Warehouse & ETL Daily
Operations, W614): `~2.8M POS events/day` → `~93,000 POS transactions/day (~2.8M/month)`,
aligning with the canonical daily volume and with the correct phrasing already used in
`VS-08/PA-08.2` (W1425: “~2.8M POS transactions/month = ~93,000/day”) and `VS-08/PA-08.1`
(W533: “~93,333 events/day”).
- **`VS-27/PA-27.2` (Infrastructure & Platform)** — two spots in the data-warehouse ETL
monitoring workflow: the Volume field `~2.8M POS events/day` → `~93,000 POS
transactions/day (~2.8M/month)`, and the Storage-growth pain point `at ~2.8M POS
transactions/day, data warehouse storage grows ~100–200 GB/month` → `at ~2.8M POS
transactions/month (~93,000/day)`. (The sibling figures on the same row — ~1,400 ecommerce
orders/day, ~18,000 PO lines/month, ~9,500 AP invoices/month — were already correct.)
- **`VS-08/PA-08.2` (Payment & Cash Management)** — W537 (POS Card Terminal & Acquirer
Settlement) Volume field: `~5,000 card transactions/day/store` → `~5,000 card
transactions/store/month (~167/day/store)`. 5,000 is the correct *per-store monthly* figure
(1.0M card txns ÷ 200 stores); the daily per-store figure is ~167 (5,000 ÷ 30).
- **`01-model-company/workflows/workflow-dependency-map.md`** — intro overclaim fix: the
old phrasing “3,451 remain unclassified, all carrying a keyword-driven proposed tier, **and
default to Tier 2** pending review” read as if all 3,451 unclassified workflows are Tier 2,
contradicting the actual proposed distribution (688 Tier 1 / 2,608 Tier 2 / 155 Tier 3 in
`workflow-criticality-proposed.md`). Reworded to state that each carries a keyword-driven
proposed tier and that Tier 2 is the *conservative catch-all default* — accurately
describing the classifier rule without implying all are Tier 2.
- **`01-model-company/model-company-profile.md`** — §18 Glossary scope clarified: the old
header claimed to be the single source of truth for “**all** terms used across the
repository”, but the glossary holds ~25 business terms while many industry/IT acronyms
(VAT, GL, KPI, SLA, etc.) are used inline without an entry. Reworded to scope the claim to
model-company / Philippine-retail / ERP-domain terms (industry acronyms used inline).
Document version bumped 2.15 → 2.16.

*Spot-checked but left unchanged (verified correct, not drift):* the **4 acquiring banks**
named in `VS-15/PA-15.2` (BDO, BPI, Metrobank, EastWest) and `FIN-075` are intentionally a
*different* commercial relationship from the **4 operational banks** (BDO, BPI, Metrobank,
Chinabank per `FIN-009`) — already documented in the 2026-06-19 bank-list entry above; and
all other `/day` and `per day` figures spot-checked across the requirements and workflow
files (e.g. ~50–200 SKUs/store/day, ~60–100 routes/day, 80–120 calls/day) are legitimately
small daily values.

## 2026-06-19 — Operational bank-list reconciliation (3 → 4 banks) & minor figure drift

The 2026-06-18 bank-list reconciliation that standardised the operational bank list to
**4 banks (BDO, BPI, Metrobank, Chinabank)** in the canonical sources — `model-company-profile.md`
§10, `erp-requirements.md` FIN-009 (lines 59 & 72), and both integration-architecture diagrams —
was not propagated to the **operational-banking** prose in one methodology doc and six workflow
PA files, which still named only three banks. The drift was invisible to `validate-repo.sh`
(which checks counts/IDs/structure, not named-bank lists in prose). This commit aligns every
*operational-banking* reference (AP disbursement, payroll, treasury, bank-statement import, bank
master/payment-file-format configuration, IT bank-endpoint health-checks, FX counterparties, escrow
receipt, AAB tax remittance) with the 4-bank canonical list. `validate-repo.sh` still reports
**0 errors / 3 informational warnings** (unchanged). No workflow, requirement, control, value
stream, or grand total changed.

- **`07-methodology/technical-guidelines.md`** — §3.1 Integration Methods table, *Bank ↔ ERP* row:
`Bank-specific formats (BDO, BPI, Metrobank)` → `(BDO, BPI, Metrobank, Chinabank)`. This row
literally describes the bank integration depicted by the adjacent §3.2 diagram, which already
shows four banks `(BDO, BPI, MB, CB)` — the row was the lone 3-bank hold-out in the file (its
own v2.2 footer already claimed "reconciled to 4 banks"). Also renamed the §3.2 duplicate
diagram's banner `INTEGRATION TOUCHPOINTS` → `INTEGRATION ARCHITECTURE` so the "duplicate for
convenience" is faithful to the canonical diagram in `data-volumes-and-integrations.md` (the
title text is not referenced anywhere else; box alignment unchanged — both words are 12 chars).
- **`VS-17 PA-17.3` (Tax & Statutory)** — bank list cited as `AAB (BDO, BPI, Metrobank per
FIN-009)` but FIN-009 lists four banks; added Chinabank so the citation matches its source.
- **`VS-29 PA-29.1` (Foundational Masters)** — two spots in the bank-master/payment-file-format
workflow: `~15–20 active bank accounts across 5 entities and 3 banking partners (BDO, BPI,
Metrobank)` → `4 banking partners (… Chinabank)` (the count 15–20 across 5 entities × 4 banks
≈ 1/entity/bank still holds), and the AP payment-file-format step `(BDO, BPI, Metrobank — each
uses different file layouts)` → `(…, Chinabank …)` so all four operational file layouts are
configured.
- **`VS-27 PA-27.2` (Infrastructure & Platform)** — three spots in the daily ERP health-check
workflow (W380 bank-endpoint monitoring): the Volume row `bank integrations (BDO, BPI,
Metrobank)`, the Background `banking systems (BDO, BPI, Metrobank for payroll, AP, treasury)`,
and step 7 `(a) BDO, BPI, Metrobank file transmission` — all now include Chinabank so the
monitoring covers every operational bank endpoint.
- **`VS-18 PA-18.3` (FX & Investments)** — two spots: `Counterparty banks: BDO, BPI, Metrobank
(same banks used for operational accounts per FIN-009)` → adds Chinabank (the parenthetical
already ties the counterparty set to the FIN-009 operational list), and the concentration-risk
note `forward contracts are placed with 3 banks` → `4 banks`.
- **`VS-11 PA-11.2` (Project Sales & B2B)** — escrow step 2 `customer deposits funds via bank
transfer (BDO, BPI, Metrobank)` → adds Chinabank (BuildRight's receiving operational accounts).
- **`erp-requirements.md` VPP-006** — vendor-count figure `~800 vendors` → `~800–1,000 vendors`
to match the range used by the sibling vendor-portal/compliance requirements (PUR-027, FIN-062,
PUR-040) and `model-company-profile.md` §6.5 / `assumptions-and-design-decisions.md` A4.3.

Deliberately **left as-is** (not defects): the distinct *card-acquiring* bank set
`BDO, BPI, Metrobank, EastWest Bank` in VS-15.2 (acquiring is a separate commercial
relationship from operational banking); the *financing-partner* bank sets in VS-08.1, VS-09.1,
VS-11.2 §financing-narrative, and VS-14.3 (`+ Security Bank` / `+ PSBank` / `+ Home Credit` —
consumer/project financing partners, a legitimately varying subset); and VS-18.3 / VS-14.1
references to "major Philippine banks / credit-card issuers (BDO, BPI, Metrobank)" as general
market context (the top-3 PH banks by size, not a claim about BuildRight's bank list).

## 2026-06-19 — Whole-repo consistency review: documentation hygiene & number-format drift

A top-to-bottom review of every summary/cross-reference document plus the two methodology
scripts and a sample of workflow PA files, looking for inconsistencies, redundancies, and
ambiguities the validator does not already catch. `validate-repo.sh` still reports **0 errors /
3 informational warnings** (the three tracked, pre-existing Expansion-block boilerplate and
Automation/Controls-adoption items). **No workflow, requirement, control, value stream, or
numeric grand total changed.**

- **`README.md` (folder-structure tree)** — the `workflows/` subtree omitted three files that
  exist and are referenced elsewhere in the README: `workflows/README.md` (navigation hub & quick
  stats), `workflow-criticality-proposed.md`, and `workflow-gap-analysis.md`. Added all three so the
  tree is a complete map of the directory. Also aligned the `workflow-criticality-classification.md`
  leaf label from "Phase 1/2/3 implementation priorities" to "Tier 1/2/3 confirmed priorities
  (1,168 rows)" to match the wording used in `workflows/README.md` and the classification doc itself
  (Phase↔Tier mapping is documented in the classification Summary table).
- **`07-methodology/README.md`** — Contents table omitted `classify-workflows.py` (referenced from
  `workflow-criticality-classification.md`, `workflow-criticality-proposed.md`, `workflow-gap-analysis.md`,
  and CHANGELOG). Added it; refreshed the `validate-repo.sh` description to reflect the current 14
  checks; clarified that the integration diagram in `technical-guidelines.md` is a reference copy
  (canonical lives in `data-volumes-and-integrations.md`); updated the stale footer date 2026-06-09
  → 2026-06-19.
- **Number-format consistency** — grand totals were written without thousands separators in four
  spots (`4596`, `1168`, `1145`, `3451`) versus the dominant comma form (`4,596` 21×, `1,168` 15×,
  `1,145` 13×, `3,451` 14×). Standardised on the comma form in `value-stream-index.md` (architecture
  banner, Grand-Total table cell, footer) and in the auto-generated `workflow-criticality-proposed.md`.
- **`07-methodology/classify-workflows.py`** — emit comma-formatted counts (`{n:,}`) in both the
  stdout summary and the generated header line, so regeneration no longer reintroduces the
  non-comma form. Regenerated `workflow-criticality-proposed.md`; only the header summary line
  changed (`3451` → `3,451`, `2608` → `2,608`; counts unchanged: 688 / 2,608 / 155).
- **`07-methodology/validate-repo.sh`** — made the grand-total extraction robust to comma-formatted
  cells. Checks 1, 3, and 9 extracted the total via `grep -oP '\d+' | tail -1`, which silently
  grabbed `596` from `4,596` once the Grand-Total cell was comma-formatted (Check 9 then reported
  a false `Grand total (596) != actual (4596)`). Switched all three to `grep -oP '\d[\d,]*' | tail -1 |
  tr -d ','` so the validator tracks the documented number style instead of fighting it.

Findings reviewed and deliberately **left as-is** (not defects): the deliberate canonical/reference
  duplication of the integration architecture diagram between `data-volumes-and-integrations.md`
  and `technical-guidelines.md` (cross-referenced); the Phase↔Tier terminology mapping; per-doc
  footer dates that reflect each file's last substantive edit; VS-49–VS-52 historical references in
  CHANGELOG/gap-analysis (all clearly marked retired).

## 2026-06-19 — Content-quality & cross-reference drift review (pass 2)

A second whole-repo review, this one focused on content-level defects the validator did not
previously catch: templated doubled-word pain-point labels, one-off typos/redundancies, a
percentage-rounding error, and drift in the dependency map's §8.1 anchor reference counts.
**No workflow, requirement, control, value stream, or numeric grand total changed.**
`validate-repo.sh` still reports 0 errors / 3 informational warnings, now joined by a new
Check 14 that prevents the main defect class from recurring.

- **12 PA files (VS-99/107/114/116/121/123/130/135)** — templated Pain Points bullets of the form
  `**<Word>-risk risk**:` (the generator appended the noun "risk" after a descriptor that already
  ended in `-risk`): Untransferred, Welfare, Rehire, Vendor, Migration, Separation, Operational,
  Hidden, Retire, Pilot, Unmanaged, Systemic. Collapsed to the sibling-correct `**<Word> risk**:`
  form used by every surrounding bullet (e.g. "Strategy-misalignment risk"). No collisions after
  the fix. Same sweep corrected `**Finencing risk**` → `**Financing risk**` (VS-130.1).
- **4 further one-off typos / redundancies in PA and cross-reference files:**
  - `workflow-system-touchpoint-map.md` — W421 glossed `batch/shade shade reconciliation`; removed
    the duplicate `shade` (W421's canonical name in VS-11.2 is "Batch/Shade Reconciliation").
  - VS-154.1 — `Project Design design the construction draw-schedule` → `designs` (subject-verb).
  - VS-19.4 — `target department Department Supervisor` → `target department's Department Supervisor`.
  - VS-04.1 — `cross-dock dock assignments` / `cross-dock dock doors` → `cross-dock assignments` /
    `cross-dock doors` (the cross-dock *is* a dock; "dock" appeared twice).
  - (`Build Build Build`, the Philippine infrastructure program, was reviewed and left as-is — it is
    a correct proper noun, not a duplication.)
- **`workflow-criticality-classification.md` (Summary table)** — the `% of Classified` column had two
  rounding errors: Phase 1 read 37.6% (440/1,168 = 37.67% → 37.7%) and Phase 2 read 42.8%
  (499/1,168 = 42.72% → 42.7%); Phase 3 19.6% was already correct. Corrected; the three still sum to
  100.0%. (v7.16)
- **`workflow-dependency-map.md` §8.1** — the ten anchor "references from VS-79–VS-161" counts were
  stated as mined from `VS-79–VS-161 PA files`, but were actually mined from PA **and** README files
  in those directories; three had also drifted since v3.6 as content was edited. Recomputed all ten
  against the current files and corrected the §8 prose to say "PA and README files". Changes:
  VS-21 1181→1184, VS-27 877→878, VS-03 484→486; the other seven (VS-17/100/28/19/36/01/33) were
  already exact. (v3.7)
- **`07-methodology/validate-repo.sh`** — added **Check 14 (templated doubled-word pain-point
  labels)**: flags any PA file containing `**<word>[-| ]risk risk**`, the exact artifact fixed above.
  Zero false positives (proper nouns like "Build Build Build" are excluded by the required "risk risk"
  suffix).

---

## 2026-06-19 — Cross-reference consistency & structural cleanup

A whole-repo review for inconsistencies, redundancies, and ambiguities surfaced seven issues across the
cross-reference layer. **No workflow, requirement, control, value stream, or numeric grand total changed.**
`validate-repo.sh` still reports 0 errors / 3 informational warnings.

- **`workflows/workflow-gap-analysis.md` §4 (family-subtotal table)** — the cumulative *Process areas* row
  drifted at Pass 9 and Pass 10: it read `… 352 | 356 | 368 | 388 …` but Pass 9 and Pass 10 each added
  4 value streams × 3 process areas = 12 PAs, so the correct progression is `… 352 | 364 | 376 | 388 …`.
  The error cancelled by Pass 11 (which is why the final 475 total and every other row reconciled),
  and the workflows / value-streams / per-family rows were always correct. Now verified: every per-step
  delta matches the per-pass PA additions stated in the §4 headers (12, 12, 12, 12, 12, 12, 12, 12, 12,
  12, 6, 12, 12, 18, 15).
- **`workflows/workflow-criticality-classification.md` (Tier 1)** — the `### Core Compliance & IT (29
  workflows)` heading understated its section: a second 16-row sub-table of foundational master-data
  governance workflows (W252 item, W253 customer, W254 location, W287 vendor, W288 financial, W289
  pricing, … W405 data-privacy-consent masters) had been appended under the same heading, giving the
  section 45 rows and leaving those 16 masters unplaced under the wrong domain. Split into two
  subsections: `### Core Compliance & IT (29 workflows)` and a new `### Core Master Data Governance
  (16 workflows)`. Tier totals are unchanged (Tier 1 main = 156 = 30+14+13+7+23+2+7+6+5+29+16+4; +284
  Additions = 440).
- **`workflows/workflow-gap-analysis.md` §3 / §6 structure** — four *Candidate gaps considered but
  rejected* subsections (Pass 7, Pass 9, Pass 8, Pass 12) were orphaned at the end of §6 *Remaining
  (deferred) gaps* — a section about gaps deferred then filled, not about candidates rejected as
  already-covered. Moved all four into §3 *Gaps Identified* alongside the existing Pass-5-elevations,
  Pass-6, and generic *rejected* subsections, and reordered them to numeric pass order (7, 8, 9, 12).
- **`workflows/workflow-dependency-map.md` §8.4** — single-digit value-stream references used mixed
  forms: most rows wrote `VS-1`, `VS-2`, `VS-3`, `VS-4`, `VS-6`, `VS-7`, `VS-8` (no leading zero), while
  the VS-131 and VS-136 rows wrote `VS-01`, `VS-02`, `VS-03` (leading zero). Normalised all 11 affected
  rows to the leading-zero form (`VS-01`–`VS-09`) used by directory names, `value-stream-index.md`,
  `workflow-gap-analysis.md`, and the §8.3 prose.
- **`README.md` (Document Relationships diagram)** — three rows of the CROSS-REFERENCE LAYER ASCII box
  (`erp-requirements.md ←→ workflows/`, `value-stream-index.md`, `157 VS · 475 process areas`) carried a
  4-space leading indent that pushed their left `│` border one column right of every other row, breaking
  the box outline. Restored column-3 alignment.
- **`workflows/value-stream-index.md` (detailed map)** — collapsed 8 stray double-blank-line gaps: one
  before VS-143 (within Make & Move), three within-family (before VS-144/145/146), three before family
  section headings (### Make & Move, ### People, ### Governance & Assurance — the other five family
  headings used a single blank), and one before the closing separator. All VS/PA separators now use a
  single blank line uniformly.
- **`workflows/workflow-dependency-map.md`** — removed a duplicate `---` horizontal rule between §7
  and §8 (rendered as two stacked `<hr>`s).
---

## 2026-06-18 — Markdown table structural-integrity review

A repo-wide sweep for table-rendering inconsistencies surfaced a class of bug that `validate-repo.sh`
did not previously catch: markdown table rows whose rendered columns silently diverge from their
header, even though every plain-text count (workflows, requirements, controls, cross-references)
stayed correct. **No workflow, requirement, control, or numeric total changed.** `validate-repo.sh`
still reports 0 errors / 3 informational warnings, now joined by a new Check 13 that prevents this
whole class from recurring.

- **`workflows/value-stream-index.md` (architecture table)** — 27 gap-analysis rows (VS-133–VS-161,
added across passes 13–18) were missing their leading `|` and wrote `  | [VS-NN](…) | …` instead of
  `|  | [VS-NN](…) | …`. Under GFM this lands the VS link in the **Family** column and shifts every
  subsequent column (Name→VS, Block→Name, …), garbling 27 of 157 rows in the canonical navigation
  table. Restored the leading `|` on all 27; the per-family VS counts now reconcile with
  `workflows/README.md` (8 families · 157 value streams · 475 process areas · 4,596 workflows).
- **`erp-requirements.md` COM-011** — the BIR TIN format example read `XXX-XXX-XXX-T00`, a corrupted
  string that matches neither the 3- nor 4-segment Philippine TIN format documented in
  `data-migration-mapping.md` (§§ vendor/employee lists: `XXX-XXX-XXX` / `XXX-XXX-XXX-XXX`).
  Corrected to `XXX-XXX-XXX or XXX-XXX-XXX-XXX` to match the canonical migration field validation.
- **`assumptions-and-design-decisions.md` (Design Decisions table)** — one row carried a stray
  `A8.1 |` assumption-ID prefix left over from the 5-column A1–A6 assumption tables, giving the
  4-column Design Decisions table a 5-column row ("POS terminals per store" landed in the Choice
  column). There is no A7/A8 section and `A8.1` is referenced nowhere else, so the prefix was removed.
- **PA-file table structure (13 PA files across VS-01/03/05/10/11/22/23/28/34/38/39/40/48)** —
  mechanical fixes to step/RACI tables that rendered with shifted or empty trailing columns:
  - 15 rows wrote the step number merged into the description cell (`| 3. text | owner | approver |
    time |`, 4 cells under a 5-column header) — split into a proper `| 3 | text | … |` step cell.
    Concentrated in VS-48 (Retail Media Network) and VS-40 (Capex), with single rows in VS-03/34.
  - 16 further rows used `| 3. | text` (correct 5-cell count, cosmetic trailing dot) — normalised to
    `| 3 | text` for a uniform step-number style across VS-11/34/38/39/40.
  - Missing/duplicate trailing pipes and a missing leading pipe in VS-10 `PA-10.2` rows 12a/12b,
    VS-05 `PA-05.2` row 7, VS-10 `PA-10.1` "Volume" row, VS-01 `PA-01.1` sub-step 7a, and the
    VS-22/VS-23 README total rows (which used `| | **Total** | **N** | |` vs the `| | **Total** |
    **N** |` form used by the other 150+ value-stream READMEs).
  - VS-28 `PA-28.3` row 1 used literal `|actual − forecast|` math delimiters inside a table cell,
    which GFM reads as column separators; escaped to `\|actual − forecast\|`.
- **`07-methodology/validate-repo.sh`** — added **Check 13 (Markdown table structural integrity)**
  with two guards: (a) flags any summary-doc table row whose opening `|` is preceded by whitespace
  (the value-stream-index column-shift bug), and (b) verifies every summary-doc table row's
  unescaped-pipe count matches its header (missing/extra pipes, merged cells, unescaped in-cell
  `|`). Both pass on the current tree.

## 2026-06-18 — Data-volumes AP figure reconciliation

Resolved the one outstanding cross-reference ambiguity flagged in the prior consistency review
(the data-volumes AP figures did not reconcile with the canonical `model-company-profile.md`
§10.2/§10.3). **No workflow, requirement, or control content changed.** `validate-repo.sh` still
reports 0 errors / 3 informational warnings.

- **`data-volumes-and-integrations.md` §1.1 (Daily Volumes)**: the "AP Invoices Processed" row
  stated 217/day (×2.0 peak = 433), which only matched the *merchandise-only* invoice stream by
  rounding (6,715 ÷ 30 ≈ 224) and silently dropped the ~2,000–3,000 non-PO/recurring invoices.
  Since the row is unlabeled and sits alongside other *total* rows (e.g. Ecommerce Orders),
  reconciled it to **total AP** per profile §10.2: ~8,500–9,500/month → midpoint **~300/day**,
  peak **~600/day** (month-end). Added an "AP volume note" tying the figure to profile §10.2
  and the W7/W7C split.
- **`data-volumes-and-integrations.md` §1.2 (Data Storage)**: the "AP/AR Documents" row carried
  ~1,440,000 annual records — roughly 9–10× the ~150K annual invoice-document count (108K AP +
  42K AR), i.e. it is line-level records, not documents. Relabelled to **"AP/AR Documents &
  Lines"** so the count is self-consistent with the corrected daily total (~150K docs × ~9.6
  lines/doc ≈ 1.44M) and with the neighbouring "Purchase Orders + Lines" / "Ecommerce Orders +
  Lines" rows. The record count (~1,440,000), size (~4 GB), annual total (~100 GB), and 7-year
  retention (~700 GB) are all unchanged.

## 2026-06-18 — Gap-analysis structural consistency: restore missing Pass 12 table, fix family counts and stale figures

A documentation-consistency pass focused on `workflow-gap-analysis.md` plus two small cross-reference
fixes surfaced by reviewing the cross-reference layer end-to-end. **No workflow, requirement, or
control content changed** — every correction reconciles the gap-analysis narrative to the
authoritative per-pass data already established elsewhere (the other §4 tables, the family-subtotal
table, and §3). `validate-repo.sh` still reports 0 errors / 3 informational warnings.

- **Restored the missing Pass 12 entry in §4 "New Value Streams Added".** The section jumped
  Pass 11 → Pass 13, omitting the per-value-stream table for Pass 12 (VS-133–VS-136, W4049–W4144)
  even though Pass 12 was referenced everywhere else (intro, gap rows #47–#50, the family-subtotal
  table, and the post-subtotal narrative). Added the table — VS-133 Operational Excellence
  (Governance & Assurance), VS-134 OCM (People), VS-135 TBM/FinOps (Technology & Data), VS-136
  Network Design/MEIO (Make & Move) — with the verified W-range allocation and a matching
  unclassified-status note, so all eighteen passes now have a §4 table.
- **Fixed two family-count mismatches in the §4 pass intros.** Pass 10 said "distributed across
  four families" but listed three (Finance, Technology & Data, Plan & Source) — the family-subtotal
  table confirms only three families moved. Pass 18 said "strengthens four families" but listed
  three (Finance +48, Governance & Assurance +48, People +24). Both corrected to "three families".
- **Removed stale per-pass unclassified totals.** The Pass 8/9/10 status notes each carried a
  present-tense "currently unclassified (counted in the N-workflow unclassified total)" with a
  stale running figure (2,445 / 2,541 / 2,637) that no longer matches the current 3,451 unclassified
  total and was inconsistent with every other pass's "counted in the unclassified total" wording.
  Normalized all three to the sibling-pass wording.
- **Reconciled two stale "rejected as adequately covered" entries.** §6 listed Lease
  accounting/IFRS 16 and Supplier risk/supply-chain resilience as rejected in Pass 12, but both
  were subsequently re-evaluated and **filled** (VS-148 in Pass 16; VS-161 TPRM in Pass 18). Added
  "re-evaluated and filled in Pass N as VS-NNN" notes so the entries no longer contradict §3/§4.
  Also reworded that subsection header, which had labelled four *elevated* Pass 12 capabilities as
  "rejected".
- **`workflow-dependency-map.md` §2.8**: the "Warehouse Operations Chain" heading was indented by
  two spaces, which breaks GitHub Markdown heading rendering (it would not render as an `###`
  heading nor appear in the document outline). De-indented to column 0.
- **`VS-15-procure-to-pay/PA-15.1`**: the W7C note referenced "the ~6,000–6,000 figure in the
  model-company-profile §10.2" — a garbled figure (the profile states ~6,715 merchandise invoices).
  Corrected to "~6,715".

## 2026-06-18 — Content consistency pass: payroll dates, bank list, stale ranges, W40 category, stale date stamps

A content-level consistency pass following the cross-reference housekeeping earlier today. **No
workflow, requirement, or control content changed**; every correction reconciles existing prose to
a canonical figure already established elsewhere in the repo. `validate-repo.sh` still reports
0 errors / 3 informational warnings.

- **Payroll cut-off dates standardized** to the canonical semi-monthly **15th & 30th**
  (per `model-company-profile.md` §11.2 and `assumptions-and-design-decisions.md`; the dominant
  figure already used in VS-10, VS-15, VS-19.3). Previously `data-volumes-and-integrations.md`
  (Batch Windows + Peak Load Calendar), `erp-requirements.md` FIN-076, and four workflow PA files
  (VS-18.1 ×3, VS-19.2 ×1) stated "14th & 28th" — two different cut-off pairs for the same
  5-entity payroll.
- **Bank list reconciled to 4 banks** (BDO, BPI, Metrobank, Chinabank) — the canonical model per
  `model-company-profile.md` §10.4, FIN-043, and VS-18.2. `erp-requirements.md` FIN-009 and both
  copies of the integration architecture diagram (`data-volumes-and-integrations.md` §2 canonical
  and `technical-guidelines.md` §3.2 convenience copy) previously listed only three.
- **`workflow-system-touchpoint-map.md`**: the "Gap-Analysis Value Streams" section heading and
  prose were still at the Pass-14 snapshot (VS-79–VS-142 / "fourteen passes" / 64 VS / 1,536
  workflows) while the footer had already moved to Pass-18. Reconciled heading + prose to
  VS-79–VS-161 / eighteen passes / 83 VS / 1,992 workflows, added the missing VS-143–VS-161
  primary-module rows, and fixed a phantom "Treasury / Cash Management" module label on the
  VS-142 row (not a defined module in the table above).
- **`workflow-dependency-map.md` §8**: heading, prose, and the §8.1 anchor table were stale
  (claimed VS-79–VS-142 / VS-79–136 / "twelve passes" / 58 VS / 1,392 workflows with
  under-counted reference figures). Re-ran the `grep`-based reference count over the full
  VS-79–VS-161 PA-file range and republished all ten anchor counts (e.g. VS-17 817 → 1449,
  VS-21 657 → 1181); reconciled all range labels and pass/VS/workflow totals. Added a note
  clarifying that the curated §8.3/§8.4 program tables (built incrementally through VS-142/VS-136)
  will be extended to VS-143–VS-161 in a follow-up; §8.1 counts already cover the full range.
- **`workflow-criticality-classification.md`**: W40 (Regular Price Change Execution) moved from
  "Core Finance" to "Core Merchandising & Pricing" — a pricing workflow previously misfiled under
  Finance while its sibling W13 sat in Merchandising. Subsection counts updated (Core Finance
  31→30; Core Merchandising & Pricing 1→2); tier totals unchanged.
- **`technical-guidelines.md`**: POS offline-storage figure clarified from the ambiguous "~1,000
  txns/store/day at peak" to the documented 467 avg/day × 2.0 peak factor = ~933 peak-day, with
  the 1,500-buffer framed as an extended-outage safety margin; HQ bandwidth rationale reconciled
  from "300 users" to "~315 HQ staff (≈300 concurrent users)" per profile §3.3.
- **`workflows/README.md`**: Quick Stats tier rows reconciled with the "1,145 unique + 23
  parent/summary sub-workflow rows = 1,168" register reconciliation used elsewhere; the
  ~2,000-word duplicated gap-analysis Note (stale-dated 2026-06-14) replaced with a concise
  pointer to `workflow-gap-analysis.md`.
- **Stale document date/version stamps** reconciled to 2026-06-18 on files whose content already
  reflected the 06-18 state but whose footers still read 06-09/06-15: `model-company-profile.md`
  (2.14→2.15), `assumptions-and-design-decisions.md`, `technical-guidelines.md` (2.1→2.2),
  `mobile-app-strategy.md` (v3→v3.1), `WORKFLOW-FORMAT-GUIDE.md`, `data-volumes-and-integrations.md`
  (4.1→4.2), `workflow-criticality-classification.md` (v7.14→v7.15),
  `workflow-system-touchpoint-map.md` (70.0→70.1), `workflow-dependency-map.md` (v3.5→v3.6).

## 2026-06-18 — Cross-reference consistency & stale-figure cleanup

A housekeeping pass correcting stale figures and broken references that had accumulated in the
cross-reference layer behind the gap-analysis passes. **No workflow, requirement, or control
content changed** — all counts were re-verified against `07-methodology/validate-repo.sh`, which
still reports 0 errors / 3 informational warnings.

- **workflow-criticality-classification.md** (v7.13 → v7.14): the footer and the `## Summary`
  "Proposed classification" block still cited the Pass-14 totals (4,236 workflows / 3,091
  unclassified / 2,995–3,331 proposed); updated to the current 4,596 / 3,451 unclassified, all
  3,451 proposed (688 Tier 1 / 2,608 Tier 2 / 155 Tier 3) through Pass 18 (VS-89–VS-161,
  W2993–W4744). Added a layout note clarifying that each tier's count spans the original
  `## Tier N` register plus the later `### Tier N Additions` batch.
- **workflow-criticality-proposed.md**: regenerated via the fixed `classify-workflows.py`. The
  title no longer carries a stale "Pass 14" label, and all 3,451 value-stream links now resolve —
  previously every one of the 157 distinct links was malformed (unpadded number, human title,
  raw spaces/ampersands) and pointed at non-existent paths.
- **classify-workflows.py**: the VS-folder slug is now looked up from the real folders and used in
  the generated link (`[VS-01](VS-01-merchandise-strategy/README.md)`); the hardcoded "Pass 14"
  title string was removed.
- **value-stream-index.md**: the 8 family subtotal rows and the grand-total row had their workflow
  counts landing in the wrong table column (Process Areas) due to a missing cell; subtotals now
  sit in the Workflows column, per-family process-area subtotals are shown (summing to 475), and
  the grand total reads 475 PAs / 4,596 workflows. The Expansion-block note is corrected from
  "23 pending rework" to 22 (VS-73 is now also detailed).
- **WORKFLOW-FORMAT-GUIDE.md**: the Repository Layout block stated 142 VS / 430 PAs / 3,331
  proposed; updated to 157 VS / 475 PAs / 3,451 proposed.
- **requirement-workflow-matrix.md** (v59 → v60): footer totals updated from 4,236 workflows /
  142 value streams to 4,596 / 157 through Pass 18, with the incremental-mapping caveat clarified.
- **mobile-app-strategy.md**: the W615 cross-reference pointed at PA-27.2 but W615 lives in
  PA-27.1; corrected.
- **data-volumes-and-integrations.md**: the daily ecommerce-order figure (~1,400/day → ~4,200
  peak) was inconsistent with the 42,900/month and ~515,000/year figures in the same document;
  corrected to ~1,430/day (~4,290 peak).
- **model-company-profile.md**: added an "ERP Platform" glossary entry; this is now the
  canonical term — **"unified cloud ERP"** — replacing the previously-listed "monolithic ERP" /
  "model ERP" variants.
- **ERP platform term standardized**: the same single cloud-deployed, single-vendor platform was
  described inconsistently as "monolithic ERP" (executive-summary, technical-guidelines,
  assumptions, NFR-030, VS-22.2, VS-27.2) and "unified cloud ERP" (README, model-company-profile,
  gap-analysis, VS-113/VS-130/VS-134/VS-135). "Monolithic" is an architecture anti-pattern term
  that mischaracterizes a modern cloud suite, so all 13 occurrences across 6 files were
  standardized to the canonical "unified cloud ERP" (system/platform as context dictates). The
  VS-27.2 "single point of failure" observation is preserved verbatim (a single-instance
  unified platform still has one blast radius, hence the HA-clustering/DR mitigation).
- **validate-repo.sh**: Checks 1 / 3 / 9 read the Grand Total line's first number; they now read
  the last number (the Workflows column) so the two-total grand-total row validates correctly.
  The computed grand total is unchanged (4,596).

## 2026-06-18 — Workflow gap analysis (Pass 18): add VS-157–VS-161 (120 workflows W4625–W4744)

A focused gap-analysis pass (5 value streams, 15 process areas, 120 workflows) closing five
further genuinely-unowned disciplines re-surfaced by running the established gap methodology
(defining terms in zero PA files as dedicated workflow headers, no dedicated owner, conflated with
adjacent covered coverage) after seventeen prior passes had been judged complete. Two are
**single-workflow elevations** (VS-157 elevates the over-stuffed W487 in VS-15.1; VS-158 elevates
the heavily-referenced W85 in VS-17.4), one is a **scattered-slice consolidation** (VS-161 unifies
the TPRM slices spread across VS-21/VS-86/VS-91/VS-119/VS-125), and two are **genuinely uncovered**
(VS-159 corporate security/executive protection; VS-160 immigration/global mobility). Strengthens
Finance (603 → 651), Governance & Assurance (816 → 864), and People (338 → 362).

- **VS-157 — Revenue Recognition (PFRS 15) & Complex Contract Accounting** (Finance, W4625–W4648):
  the enterprise PFRS 15 five-step recognition discipline across the full multi-element-arrangement
  portfolio (loyalty points, gift-card breakage, bundles, product+installation, consignment/VMI
  sell-through, subscription, extended warranty, retail media, marketplace commissions, COD, VAS,
  trade-in, construction-finance referral). The discipline existed only as the single over-stuffed
  workflow W487 in VS-15.1 (referenced across 12 PA files, explicitly covering eleven revenue
  streams with no dedicated PFRS 15 accounting owner). Distinct from VS-118 (revenue-leakage
  protection) and VS-17.4 (FP&A reporting).
- **VS-158 — Product Costing, Landed-Cost & Cost Accounting** (Finance, W4649–W4672): the per-unit
  cost-accounting operating system beneath ~PHP 42–45B COGS — standard-cost setup, import
  landed-cost build-up, catch-weight/cut-to-length unit cost, kit/BOM roll, private-label
  fully-burdened cost, PPV/landed-cost/conversion variance, margin analytics, project/service/
  intercompany costing, cost-master governance. The discipline existed only as the single workflow
  W85 in VS-17.4 (referenced across 25 PA files as the catch-all cost reference). Distinct from
  VS-05 (inventory transactions) and VS-17.4 (FP&A).
- **VS-159 — Corporate Security, Executive Protection & Travel Risk Management** (Governance &
  Assurance, W4673–W4696): the corporate-security & executive-protection program — protective
  intelligence, the GSOC, executive protection, principal travel, event security, K&R/extortion
  response, employee travel-risk/duty-of-care, corporate investigations, insider threat, workplace
  violence, and coordinated crisis response. 'executive protection', 'protective intelligence',
  'corporate security', 'travel security', 'kidnap & ransom' each appeared in zero PA files.
  Distinct from retail-shrink LP (VS-23), customer premises safety (VS-147), cyber (VS-27.3), BCP
  (VS-26), and the physical-security audit (VS-21.3 W358).
- **VS-160 — Global Mobility, Immigration & Foreign Worker Compliance** (People, W4697–W4720): the
  cross-border/provincial mobility and DOLE Alien Employment Permit / Bureau of Immigration 9G
  Pre-Arranged Employee Visa & ACR I-Card foreign-worker program, plus assignment payroll/tax/
  statutory benefits, relocation, and repatriation. 'immigration', '9G visa', 'alien employment',
  'expatriate', 'international assignment', 'employee mobility' each appeared in zero PA files.
  Distinct from VS-19 (PH employees), VS-122 (vendor-side sourcing), VS-98 (contingent workforce),
  VS-103 (domestic HR shared services), and VS-144 (staff housing).
- **VS-161 — Third-Party & Supplier Risk Management (TPRM)** (Governance & Assurance, W4721–W4744):
  the unified cross-domain enterprise third-party-risk backbone across ~800–1,000 vendors + 3PL/
  SaaS/payment/BPO/CIT/sourcing-agent/marketplace/EPC third parties and all risk domains (financial,
  cyber, operational, compliance, privacy, ESG/human-rights, concentration, fourth-party), with the
  single inventory, tiering, due diligence, continuous monitoring, resilience/exit, and
  regulator-facing evidence program. Each risk domain owned only its slice (W1328 supply, W334
  audit, W2942 ABC, W3052 privacy, W3863 fraud, W3733 integrity); no owner held the whole.
  Distinct from VS-03/VS-67 (commercial vendor management) and each domain slice.

Counts reconciled across all documents: **4,596 workflows across 157 value streams / 475 process
areas** (was 4,476 / 152 / 460). The 120 new workflows are unclassified and carry a keyword-driven
proposed tier in `workflow-criticality-proposed.md` (regenerated via `classify-workflows.py`),
exactly as prior batches. `validate-repo.sh` passes with 0 errors.

---

## 2026-06-17 — Workflow gap analysis (Pass 17): add VS-151–VS-156 (144 workflows W4481–W4624)

The largest single gap-analysis pass (6 value streams, 18 process areas, 144 workflows),
combining three genuinely-uncovered operational disciplines with the three capabilities explicitly
flagged as *future business-model extensions* in §6 of prior passes. Each gap's defining terms
appeared in zero or near-zero PA files as dedicated workflow headers with no dedicated owner; the
three future-flagged capabilities are activated here **within BuildRight's current retail charter**
(captive = own risk-financing vehicle, not a third-party insurer; construction finance =
broker/referral, not lending; resale = certified pre-owned, not an open C2C marketplace). VS
numbering was shifted to VS-151–VS-156 / W4481–W4624 to avoid colliding with VS-143–VS-150 /
W4289–W4480 allocated by Passes 15–16 (which independently added bulky-goods delivery, staff
housing, garden center, mystery shopping, customer-safety/premises-liability, lease accounting,
self-checkout, and drug-free-workplace value streams).

- **VS-151 — Auto-ID, Barcode, RFID, Price-Tag Labeling & EAS Operations** (Technology & Data,
  W4481–W4504): physical item-identification & labeling infrastructure for 35K SKUs / 600 POS /
  200 stores / 134.4M annual POS line items. 'auto-ID', 'barcode governance', 'RFID operations',
  'price-tag labeling', 'EAS operations' appeared in zero PA files as headers / zero VS names;
  scattered across VS-29 (W1345 barcode/GS1), VS-71, VS-08, VS-23, VS-04/VS-05, VS-115, VS-111.
  None owned GS1 governance, label spec/production, in-store application, EAS/RFID operations,
  RA 7394 price-tag compliance, read-rate/label-conformance, or auto-ID fraud-vector control.
  Strengthens Technology & Data (326 → 350).
- **VS-152 — Corporate Social Responsibility, Foundation & Community Investment** (Governance &
  Assurance, W4505–W4528): social-impact & community-investment discipline. 'CSR' appeared in ~58
  PA files, 'foundation' ~24, but as incidental references; 'CSR'/'social responsibility'/'
  foundation'/'community investment' appeared in zero PA files as headers. None owned the
  Foundation (SEC/BIR-donee/PCNC), community-investment portfolio, disaster relief, volunteerism,
  impact measurement (SROI), or GRI/IRIS+ reporting — distinct from VS-25 (ESG reporting), VS-94
  (cooperative sourcing), VS-104 (govt affairs), VS-69 (corporate disaster ops), VS-14.3 (CSR
  comms). Strengthens Governance & Assurance (792 → 816).
- **VS-153 — Captive Insurance, Reinsurance & Enterprise Risk Financing** (Finance, W4529–W4552):
  enterprise risk-financing / self-insurance discipline. Previously flagged as a future
  business-model extension; 'captive insurance', 'reinsurance', 'self-insur' appeared in only 1–4
  PA files. None owned captive feasibility/formation/domicile, underwriting scope, reinsurance
  program, claims, captive finance/statutory/RBC compliance, or portfolio analytics — distinct
  from VS-26 (buys/claims commercial policies), VS-21.2 (measures risk), VS-18 (group cash).
  Strengthens Finance (555 → 579).
- **VS-154 — Home Construction Finance, Loan Brokerage & Mortgage Referral Services** (Finance,
  W4553–W4576): customer construction-finance enablement discipline. Previously flagged as a
  future capability; 'construction loan', 'home loan', 'mortgage' appeared in 1–6 PA files. None
  owned the brokerage/referral model (lender network, BSP accreditation, origination handoff,
  draw-schedule linkage to VS-66/VS-12, referral economics, anti-predatory-lending compliance) —
  distinct from VS-38 (in-house credit), VS-16 (trade AR), VS-66 (project design). Scoped as
  broker/referral (not lending). Strengthens Finance (579 → 603).
- **VS-155 — Trade-In, Buy-Back & Certified Pre-Owned / Refurbished Product Resale** (Make & Move,
  W4577–W4600): circular trade-in & certified-resale discipline. Previously flagged as a future
  capability; 'trade-in', 'buy-back', 'pre-owned', 'second-hand' appeared in 0–10 PA files. None
  owned trade-in valuation/grading, take-back, inspection/refurbishment/certification, resale
  listing/fulfillment/warranty, or circular-economy analytics — distinct from VS-32 (defective
  returns), VS-73 (end-of-life disposal), VS-12.1 (repair for owner — this refurbishes for resale),
  VS-05.3 (BuildRight's own stock disposition). Scoped as certified resale (not open C2C).
  Strengthens Make & Move (403 → 427).
- **VS-156 — In-Store Value-Added Services & Financial Agency Operations** (Sell & Serve,
  W4601–W4624): financial-agency/VAS counter discipline (bills payment, domestic remittance,
  e-money cash-in/out, mobile load). 'bills payment', 'e-money', 'cash-in', 'value-added service'
  appeared in 0–2 PA files as headers. None owned the agency product/partner portfolio, BSP agent
  accreditation, counter operations/KYC, settlement/reconciliation/commission, AML/BSP compliance,
  or analytics — distinct from VS-80 (BuildRight's own payment rail), VS-08.2 (in-store retail
  cash), VS-86 (AML program — this executes it as agent), VS-142 (COD), VS-154 (project
  financing). Scoped as agent-of-principal (not principal). Strengthens Sell & Serve (1,242 →
  1,266).

All six are fully detailed to the WORKFLOW-FORMAT-GUIDE quality bar (specific system touchpoints,
pain points with mitigations, time estimates with scaling math, Automation Opportunity, Controls,
and cross-references). The 144 new workflows are **unclassified** and carry a keyword-driven
proposed tier in `workflow-criticality-proposed.md` (regenerated via
`07-methodology/classify-workflows.py`), exactly as prior batches.

**Cross-reference reconciliation:** updated value-stream-index (152 VS / 460 PA / 4,476 workflows,
family subtotals + grand total, value-stream-blocks, coverage note, detailed map, footer),
workflow-gap-analysis (Pass 17 §3 rows #65–#70, §4 table, family-subtotal-impact table with new
After-Pass-17 column, §5 validation, §6 deferred-gaps + future-flag update, header),
workflow-criticality-classification (1,145/4,476 classified; 3,331 unclassified all proposed;
phase table 673/2,504/154), workflow-criticality-proposed (regenerated, 3,331),
workflow-system-touchpoint-map footer (v69.0, 4,476 / 152 VS / VS-79–VS-156 scope),
workflow-dependency-map header + footer (v3.4, 152 VS / 4,476 workflows / VS-151–VS-156 noted),
README (tree, key metrics, classification line, coverage note, ASCII diagrams), executive-summary
counts, requirement-workflow-matrix total, workflows/README master-index count + family
reconciliation, WORKFLOW-FORMAT-GUIDE index line, and VS-133 PA-file volume lines. Validator:
0 errors.

---

## 2026-06-17 — Workflow gap analysis (Pass 16): add VS-147–VS-150 (96 workflows W4385–W4480)

A sixteenth gap-analysis pass added **four value streams / twelve process areas / ninety-six
workflows**, each filling a genuinely-uncovered operational discipline whose defining terms
appeared in **zero** PA files as dedicated workflow headers (verified via repo-wide grep) and
which had been conflated with adjacent covered capabilities. The pass was deliberately balanced
(+24 to each of four operating families: Governance & Assurance, Finance, Sell & Serve, People).
New totals: **146 value streams · 442 process areas · 4,332 workflows**.

| VS | Value Stream | Family | Workflows | W-range |
|---|---|---|---|---|
| [VS-147](01-model-company/workflows/VS-147-customer-safety-premises-liability-and-in-store-risk-management/README.md) | Customer Safety, Premises Liability & In-Store Risk Management | Governance & Assurance | 24 | W4385–W4408 |
| [VS-148](01-model-company/workflows/VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/README.md) | Lease Accounting (PFRS 16/IFRS 16) & Right-of-Use Asset Management | Finance | 24 | W4409–W4432 |
| [VS-149](01-model-company/workflows/VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/README.md) | Self-Checkout, Scan-&-Go & Unattended Retail Technology Operations | Sell & Serve | 24 | W4433–W4456 |
| [VS-150](01-model-company/workflows/VS-150-drug-free-workplace-and-substance-abuse-program/README.md) | Drug-Free Workplace & Substance Abuse Program | People | 24 | W4457–W4480 |

Each gap is profile-grounded and distinct from adjacent covered value streams (see the per-VS
README for the distinctness rationale):

- **VS-147 Customer Safety, Premises Liability & In-Store Risk Management** — owns the
  *customer-facing* premises-liability & in-store safety program across ~205 high-traffic public
  sites where customers/trade-pros share the floor with forklifts, overhead racking, and a
  lumber/tile/chemical yard; distinct from VS-24 (employee/occupational HSE), VS-23 (shrink LP),
  VS-07 (self-reported housekeeping), and VS-138 (building IFM). Defining terms 'premises
  liability', 'customer safety', 'falling merchandise', 'aisle safety' appeared in zero PA-file
  headers.
- **VS-148 Lease Accounting (PFRS 16/IFRS 16) & Right-of-Use Asset Management** — owns the PFRS 16
  recognition/measurement/disclosure program (right-of-use assets & lease liabilities) across the
  5-entity group's ~205 leased sites plus leased equipment/fleet/IT; distinct from VS-42 (lessee
  commercial lease admin), VS-17.3 (tax deduction), VS-35 (owned assets), and VS-97 (lessor view).
  Defining terms 'right-of-use', 'lease liability', 'ROU asset' appeared in zero PA-file headers.
- **VS-149 Self-Checkout, Scan-&-Go & Unattended Retail Technology Operations** — owns the
  self-service/unattended checkout operating program (SCO lanes, mobile scan-&-go, computer-vision,
  unattended formats); distinct from VS-08 (staffed POS), VS-23 (broad shrink LP), VS-80
  (payment-acquirer rails), and VS-109 (project deployment). Defining terms 'scan-and-go',
  'unattended', 'self-checkout' appeared in zero PA-file headers.
- **VS-150 Drug-Free Workplace & Substance Abuse Program** — owns the end-to-end DOLE D.O. 53-04 /
  RA 9165 Art. V drug-free workplace program (policy, testing matrix, collection/lab/MRO, case &
  due-process, rehabilitation, return-to-duty, confidentiality); distinct from VS-83 (clinic/exam),
  VS-19.1 (pre-employment onboarding), VS-24 (post-incident HSE), and VS-06.2 (driver fleet).
  Defining terms 'drug test', 'drug-free workplace', 'reasonable suspicion' appeared in zero PA-file
  headers.

All 96 new workflows are fully detailed (Trigger / Frequency / Volume-with-×-math / Owner /
Participants / Steps RACI / System Touchpoints / Time Estimate / Pain Points-Risks / Automation
Opportunity / Controls / Cross-references) and carry **no boilerplate**. They are currently
**unclassified** (unclassified total: 3,091 → 3,187, of which the 96 Pass-16 workflows are pending
their first keyword-driven proposal) and will be tier-assigned in a follow-up criticality review,
exactly as the Pass 1–Pass 15 batches were handled.

Consistency updates applied across count-bearing current-state docs (historical CHANGELOG /
gap-analysis table entries preserved as-is): `value-stream-index.md` (architecture line, blocks
table, coverage note, 4 family subtotals + family-table VS rows, 4 VS + 12 PA detailed rows,
grand total, footer), `workflows/README.md` (Quick Stats, master-index count, family-subtotal
reconciliation, Pass-16 narrative), root `README.md` (counts, retired-VS pass note,
classification/unclassified line, diagrams), `executive-summary.md` (counts), and
`workflow-gap-analysis.md` (header, §3 gap rows 61–64, §4 Pass-16 section + family-subtotal-impact
column, §5 grand-total). The criticality-classification/dependency-map/touchpoint-map/
requirement-workflow-matrix were **not** altered (the new workflows are unclassified and carry no
new requirement mappings; `validate-repo.sh` confirms zero dangling references and grand-total /
header-count match).

`07-methodology/validate-repo.sh` passes with **0 errors** (3 informational warnings) after the
additions: grand total 4,332 matches actual PA workflow header count 4,332; all classified IDs
resolve; no dangling references; no placeholder/boilerplate content; Automation Opportunity &
Controls field adoption rose from 360 → 456 workflows.

---

## 2026-06-17 — Workflow gap analysis (Pass 15): add VS-143–VS-146 (96 workflows W4289–W4384)

A fifteenth gap-analysis pass added **four value streams / twelve process areas / ninety-six
workflows**, each filling a genuinely-uncovered operational discipline whose defining terms
appeared in **zero** PA files as dedicated workflow headers (verified via repo-wide grep) and
which had been conflated with adjacent covered capabilities. The pass was deliberately balanced
(+24 to each of four operating families). New totals: **142 value streams · 430 process areas ·
4,236 workflows**.

| VS | Value Stream | Family | Workflows | W-range |
|---|---|---|---|---|
| [VS-143](01-model-company/workflows/VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/README.md) | Bulky & White-Goods Delivery, Installation, Haul-Away & Recycling Operations | Make & Move | 24 | W4289–W4312 |
| [VS-144](01-model-company/workflows/VS-144-employee-accommodation-dormitory-and-staff-housing/README.md) | Employee Accommodation, Dormitory & Staff Housing Operations | People | 24 | W4313–W4336 |
| [VS-145](01-model-company/workflows/VS-145-garden-center-live-goods-and-plant-nursery/README.md) | Garden Center, Live Goods & Plant Nursery Operations | Sell & Serve | 24 | W4337–W4360 |
| [VS-146](01-model-company/workflows/VS-146-customer-mystery-shopping-and-service-quality-assurance/README.md) | Customer Mystery Shopping & Service Quality Assurance Program | Governance & Assurance | 24 | W4361–W4384 |

Each gap is profile-grounded and distinct from adjacent covered value streams (see the per-VS
README for the distinctness rationale). All 96 new workflows are fully detailed (Trigger /
Frequency / Volume-with-×-math / Owner / Participants / Steps RACI / System Touchpoints / Time
Estimate / Pain Points-Risks / Automation Opportunity / Controls / Cross-references) and carry
**no boilerplate**. They are currently **unclassified** (counted in the unclassified total:
2,995 → 3,091, of which 96 are pending their first keyword-driven proposal) and will be
tier-assigned in a follow-up criticality review, exactly as the Pass 1–Pass 14 batches were
handled.

Consistency updates applied across all count-bearing current-state docs (historical CHANGELOG /
gap-analysis table entries preserved as-is): `value-stream-index.md` (architecture line, blocks
table, 4 family subtotals, decision-tree family lists, 4 VS + 12 PA detailed rows, footer,
coverage note), `workflows/README.md` (Quick Stats + full per-family navigation reconstruction —
also corrected pre-existing stale Pass-11/12 family subtotals and misplaced VS-129/130/132/133
rows), root `README.md`, `executive-summary.md`, `workflow-criticality-classification.md`
(v7.12 → v7.13), `workflow-criticality-proposed.md`, `workflow-dependency-map.md` (v3.2 → v3.3),
`workflow-system-touchpoint-map.md` (v67.0 → v68.0), `requirement-workflow-matrix.md` (v58 → v59),
`WORKFLOW-FORMAT-GUIDE.md`, and VS-133 narrative counts. `workflow-gap-analysis.md` §3/§4/§5/§6
updated with the Pass 15 record, candidate-gap rows #57–60, and the family-subtotal table's
After-Pass-15 column.

---

## 2026-06-17 — Consistency review: correct unclassified-workflow count (2,972 → 2,995) and collapse provenance footers

A full-repo review found the **unclassified-workflow count reported as 2,972 in five places but
2,995 elsewhere**, while `WORKFLOW-FORMAT-GUIDE.md` still cited a stale **2,659** proposed count
(pre-Pass-13/14). Root cause: the confirmed criticality register holds **1,168 rows**, of which
**23 are `###` parent/summary sub-workflows** (e.g. W2, W5B, W9A) double-counted against a `##`
parent. Unique `##` workflows classified = **1,145**, so true unclassified = 4,140 − 1,145 =
**2,995** (not 4,140 − 1,168 = 2,972). The validator's Check 1 echo was also printing the
row-arithmetic "Documented unclassified: 2,972" figure, contradicting the correct unique-workflow
count it printed in the same section.

Fixes:

- **`workflow-criticality-classification.md`** — header reframed to "1,145 unique workflows
  classified (1,168 register rows, incl. 23 `###` parent/summary sub-workflows)"; the Summary
  Coverage table now reads "1,168 rows (1,145 unique)" so **1,145 + 2,995 = 4,140** reconciles
  explicitly; the provenance footer (which enumerated all fourteen gap-analysis passes inline in
  one ~2,300-char line) was collapsed to a concise pointer — the full per-pass history remains in
  `workflow-gap-analysis.md` and this CHANGELOG. Version bumped v7.11 → v7.12.
- **`README.md`**, **`workflow-dependency-map.md`**, **`workflow-system-touchpoint-map.md`** —
  every current-state "2,972 unclassified" corrected to **2,995**, with the row-vs-unique
  distinction noted wherever subtraction is shown (4,140 − 1,145).
- **`WORKFLOW-FORMAT-GUIDE.md`** — layout diagram corrected 2,659 → **2,995** proposed.
- **`executive-summary.md`** — collapsed the giant per-pass date footer to a pointer; corrected
  the `07-methodology/` label from "COMPLETE" to "partial" (its README lists 7 methodology docs
  still pending platform selection).
- **`07-methodology/validate-repo.sh`** — Check 1 echo no longer prints the misleading
  "Documented unclassified" row-arithmetic figure; it now states register-rows vs unique
  classified, and the real unclassified count (2,995) is printed by the existing WARN.

Validator result: **0 errors, 3 warnings** (the three warnings are the tracked, pre-existing
Expansion-block boilerplate and Automation/Controls-adoption items — unchanged by this commit).
A separate scan for broken markdown links surfaced one apparent hit in `CHANGELOG.md` that was
verified to be a **false positive**: the `](../value-stream-index.md)` text sits inside an inline
code span illustrating the standardized PA-footer template, so it is literal code, not a live link.

---

## 2026-06-17 — Consistency review: correct stale requirement total in `erp-requirements.md` (730 → 733)

The `erp-requirements.md` v21.0 footer (line 845) stated **"total unique requirements: 730"**, but
the document header, `requirement-workflow-matrix.md`, `executive-summary.md`, `README.md`, and
the validator all count **733**. The figure was correct when written (commit `254f1e8`, 2026-06-09
07:10), but a later review the same day (commit `f34a520`, "implement all 6 recommendations",
2026-06-09 22:26) added the new **WHL-001–003** DC-operations requirements to R4 (Warehouse
Management) without updating the footer, taking the total 730 → 733. (The companion
`requirement-workflow-matrix.md` Coverage-Validation block was corrected to 733 in an earlier
commit; this footer was the lone holdout.)

Verified the count three ways before editing:
- 733 total requirement table rows and **733 unique IDs** under the precise regex
  `^\| [A-Z]+-\d+[a-z]? ` — i.e. **zero real duplicates**.
- The three apparent duplicates surfaced by a coarser `[A-Z]+-\d+` extraction (NFR-022,
  POS-014, PUR-025) are false positives: they are distinct letter-suffixed requirements
  (NFR-022a BIR CAS Registration, POS-014a SC/PWD Discount, PUR-025a Commodity Index,
  PUR-025b Supplier Innovation) that the truncating regex collapsed.
- `requirement-workflow-matrix.md` independently holds 733 unique requirement IDs.

Fix: updated the footer total to **733** with a concise note recording the WHL-001–003
addition and the reconciliation. The requirement count (733) is now consistent across
`erp-requirements.md` (header + footer), `requirement-workflow-matrix.md`, `executive-summary.md`,
and `README.md`. Validator Check 4 (requirement-IDs-in-matrix vs defined) already passed at 733/733
and is unaffected.

---

## 2026-06-17 — Consistency review: reconcile Pass 13/14 (VS-137–VS-142) across cross-reference docs

Pass 13 (VS-137–VS-140) and Pass 14 (VS-141–VS-142) added the value-stream directories,
PA files, and most cross-reference updates, but several orientation/index docs and the
criticality proposal still described the repository as if gap analysis had stopped at
Pass 12 (VS-136) or Pass 13. The validator passed (these are summary/prose sections and
the proposed-tier file it does not fully cross-check), but the prose was stale, the
proposed-tier register was missing VS-141/VS-142, and the Pass-14 entry's claim that the
new workflows "carry a keyword-driven proposed tier in `workflow-criticality-proposed.md`"
was not yet true. This commit finishes the reconciliation so every doc agrees on the
current **138 value streams / 418 process areas / 4,140 workflows** state.

Fixes:

- **`workflow-criticality-proposed.md`** — regenerated via `classify-workflows.py` (title
  bumped Pass 13 → Pass 14) so it now includes VS-141/VS-142; 2,947 → **2,995** proposed
  workflows (Tier 1 615→622 · Tier 2 2,188→2,227 · Tier 3 144→146). The classification
  file's "0 workflows without a proposal" claim is now true (was false: the 48 Pass-14
  workflows previously had none).
- **`workflow-criticality-classification.md`** — header total 4,092→4,140 and unclassified
  2,924→2,972; proposed-summary table refreshed to match the regenerated proposal
  (613/2,096/142/2,947 → 622/2,227/146/2,995) and the stale prose "2,851 workflows not
  yet confirmed" → 2,995; Grand-Total coverage 4,092→4,140; domain-breakdown prose
  4,092→4,140; footer bumped v7.10→v7.11 and corrected the stale opening summary
  (1,167 classified / Tier 1 439 / 22 parent-summary → 1,168 / 440 / 23 — matching the
  authoritative `## Summary` table and the validator) and appended Pass 13 & Pass 14 to
  the per-pass narrative.
- **`workflow-dependency-map.md`** — header 4,092→4,140 total and 2,924→2,972 unclassified
  (the previous state was internally inconsistent with the file's own 2,972 footer);
  §8 scope VS-79–VS-140 → VS-79–VS-142; VS-133 row "~3,996 workflows" → "~4,140 workflows".
- **`requirement-workflow-matrix.md`** — "4,092 workflows across 136 value streams" →
  4,140 / 138; footer bumped v57→v58, totals 3,996/132 → 4,140/138, mapping scope
  VS-113–VS-136 → VS-113–VS-142.
- **`workflows/README.md`** — stats block (136/412/4,092/439 → 138/418/4,140/440), nav
  "all 136 value streams" → 138, family-subtotal reconciliation
  (…+507+266…=4,092 → …+531+290…=4,140), and a Pass 13/14 addendum to the retirement
  note (previously stopped at Pass 12).
- **`value-stream-index.md`** — block table "VS-89 – VS-140 | 52 | thirteen passes" →
  "VS-89 – VS-142 | 54 | fourteen passes".
- **VS-133 `PA-133.1` & `PA-133.3`** — enterprise-scale Volume rows "~3,900 workflows
  across 132 value streams" → "~4,140 / 138".

Validator: **0 errors**, 3 informational warnings (unchanged). Narrative figures
(138 value streams, 418 process areas, 4,140 workflows, 1,168 classified / 2,972
unclassified, fourteen passes) are now consistent across README, executive-summary,
value-stream-index, dependency-map, touchpoint-map, classification, proposed register,
and requirement-workflow-matrix.

---

## 2026-06-16 — Workflow gap analysis (Pass 14): add VS-141–VS-142 (48 workflows W4241–W4288)

A fourteenth gap-analysis pass — deliberately smaller (2 value streams, 48 workflows) — closed
the two remaining genuinely-clean gaps after the thirteen prior passes had covered the
operational, statutory, strategic, cross-cutting-management, technology, shared-service, and
B2B-growth surface. Each gap's defining terms appeared in **zero** PA files as dedicated workflow
headers, and each had been conflated with an adjacent covered capability:

- **VS-141 — Employee Transport, Shuttle & Daily Commute Management** (People, W4241–W4264):
  the daily people-movement discipline for ~6,715 staff across 205 sites on 2–3 shifts (incl.
  night). 'employee shuttle', 'company bus', 'transport allowance', and 'daily commute' appeared
  in zero PA files as headers; only adjacent coverage existed — VS-19.1 *business travel*,
  VS-18.2 *errand* petty-cash transport, VS-138 *building* services, VS-06 *goods* fleet. None
  owned commute-need assessment, transport policy/allowance, shuttle fleet/routes/manifest,
  driver/vendor/safety (LTFRB franchise, women-safe/after-dark), cost allocation, or
  commute-EX/analytics. Strengthens the thinnest family by workflow count (People 266 → 290).
- **VS-142 — Cash-on-Delivery (COD) Operations, Driver Cash Handling & Reconciliation**
  (Finance, W4265–W4288): the enterprise COD cash chain for a COD-dominant Philippine ecommerce
  market (~13,000–21,000 COD orders/month at a 30–50% share). 'COD operations', 'driver cash
  handling', and 'COD reconciliation' appeared in zero PA files as headers; only W2837
  (MSME-segment COD in VS-82) and W1202 (store daily cash) existed, with COD scattered as single
  steps across VS-06.3/VS-08.2/VS-10.2/VS-16.3/VS-80/VS-56. None owned COD policy/limits,
  doorstep collection/custody, driver/3PL remittance & reconciliation, settlement/float, fraud,
  or analytics — distinct from acquirer settlement (VS-80), last-mile delivery (VS-06.3), and
  in-store cash (VS-08.2). Strengthens Finance (507 → 531).

Both are fully detailed to the WORKFLOW-FORMAT-GUIDE quality bar (specific system touchpoints,
pain points with mitigations, time estimates with scaling math, Automation Opportunity, Controls,
and cross-references). The 48 new workflows are **unclassified** and carry a keyword-driven
proposed tier in `workflow-criticality-proposed.md`, exactly as prior batches.

**Cross-reference reconciliation:** updated value-stream-index (138 VS / 418 PA / 4,140 workflows,
family subtotals, decision tree, detailed map), workflow-gap-analysis (Pass 14 §3 rows, §4
table, family-subtotal-impact table, §5/§6), workflow-system-touchpoint-map (VS-141/VS-142
primary-module rows + VS-137–VS-140 rows that were also missing), workflow-dependency-map §8
(VS-141/VS-142 + missing VS-137–VS-140 rows; VS-79–VS-142 scope), README (tree, key metrics,
coverage note — also brought current with Pass 13's VS-137–VS-140 which the prior commit had not
propagated), executive-summary counts, and WORKFLOW-FORMAT-GUIDE index line. Validator: 0 errors.

---

## 2026-06-16 — Workflow gap analysis (Pass 13): add VS-137–VS-140 (96 workflows W4145–W4240)

A thirteenth gap-analysis pass added four more value streams (3 process areas, 24 workflows each),
each filling a genuinely-unowned **shared-service or B2B-growth discipline** whose defining terms
appeared in **zero or near-zero** PA files as dedicated workflow headers (only incidental
references to the broader capability existed, scattered across multiple adjacent value streams).
The four were chosen to be **distinct from the Pass 12 set (VS-133–VS-136: OpEx/CI, OCM, TBM/
FinOps, network design/MEIO)** — they cover product-content management (PIM/DAM), integrated
facilities management/workplace/building automation, B2B trade-show/field-event marketing, and the
field-sales/outside-sales force. The pass deliberately strengthened the two thinnest-by-workflow
families (Asset & Infrastructure and Technology & Data) and added two genuine, B2B-relevant gaps
to the largest family (Sell & Serve).

- **VS-137 — Product Information Management (PIM) & Digital Asset Management (DAM)**
  (Technology & Data, W4145–W4168): owns the product-content discipline — the canonical product
  information model & attribute taxonomy, new-product content onboarding, DAM repository & media
  production lifecycle, Safety Data Sheet (SDS) & regulatory-certificate management for the ~8–10%
  DG assortment, how-to/rich-content authoring, multilingual/UoM localization, product-relationship
  modeling, vendor-supplied content intake, channel content syndication & publication rules, price/
  promo/availability sync, and PIM/DAM analytics. Genuinely uncovered ('product information
  management'/'PIM'/'digital asset management'/'DAM' appeared scattered across ~30 PA files with
  zero dedicated headers; each channel kept its own copy). Distinct from transactional master data
  (VS-29), the ecommerce storefront (VS-10), retail-media monetization (VS-48), assortment/range
  (VS-01.1), and marketing (VS-14).
- **VS-138 — Integrated Facilities Management, Workplace Services & Building Automation**
  (Asset & Infrastructure, W4169–W4192): owns the facilities/physical-environment discipline — IFM
  strategy & provider governance, the facilities service catalog & SLA framework, facilities asset
  register & building-condition management, preventive/reactive maintenance, hard FM trades (HVAC,
  electrical, plumbing, fire systems), soft services (cleaning, pest, guarding, grounds, waste,
  cafeteria, mailroom), building automation/BMS & IoT, energy/environmental control, space &
  occupancy, green-building operations, compliance/permits/fire-life-safety coordination, and
  facilities analytics. Genuinely uncovered (facility/building-service terms sprinkled across ~30 PA
  files with zero dedicated headers for the integrated operating model). Distinct from equipment
  maintenance (VS-20.3), energy management (VS-120), physical security (VS-23.2), and outsourced-
  workforce governance (VS-98).
- **VS-139 — Trade Show, Exhibition & Field Event Marketing**
  (Sell & Serve, W4193–W4216): owns the B2B event/field-marketing channel — event strategy &
  portfolio/calendar, budget & business case, audience targeting & trade-pro invitation, vendor
  co-funding/MDF, compliance/permits/promo-prize governance, booth/stand design & logistics, show
  registration & sponsorship, product display/demo/sample coordination, on-site sales & lead
  capture, hospitality/VIP/account meetings, travel & per-diem, teardown/asset recovery, event
  HSE, hosted trade days, product launches, store grand-opening/in-store events, partner/sponsored
  events, digital/hybrid events, lead routing/nurture, and event-ROI analytics. Genuinely uncovered
  ('trade show'/'exhibition'/'field event' appeared scattered across ~9 PA files with zero dedicated
  headers; each event run ad-hoc). Distinct from broad marketing (VS-14), trade-pro membership
  (VS-43), key-account management (VS-107), and store commissioning (VS-37).
- **VS-140 — Field Sales, Outside Sales & Route-to-Market Force Management**
  (Sell & Serve, W4217–W4240): owns the outside-sales-force discipline covering the ~40% B2B revenue
  base — field-sales strategy & go-to-coverage model, force sizing/structure, territory design &
  balancing, account segmentation/tiering & coverage plan, quota/target setting, route-to-market &
  channel assignment, onboarding/enablement/certification, CRM/mobility tooling, daily route & call
  planning, customer visits/relationship management, project estimating/quoting, pipeline/forecast,
  field order capture/pricing/fulfillment, project bid/tender/spec pursuit, field samples/demos,
  field ABC/data-quality, performance/attainment, compensation/incentive administration,
  conversion win/loss analytics, route efficiency/productivity, retention/churn, coaching/PIP, force
  cost/ROI & workforce planning, and continuous improvement. Genuinely uncovered ('field sales'/
  'outside sales'/'route-to-market' appeared in only ~1–3 PA files with zero dedicated headers).
  Distinct from key-account management (VS-107), trade-pro membership (VS-43), B2B/project
  transaction processing (VS-11), and general sales enablement (VS-124).

### Repository totals after Pass 13

| Metric | Before (Pass 12) | After (Pass 13) |
|---|---|---|
| Value streams | 132 | **136** |
| Process areas | 400 | **412** |
| Workflows | 3,996 | **4,092** (+96) |
| Unclassified (keyword-proposed pending review) | 2,851 | **2,947** |
| Confirmed-classified (Tier 1/2/3) | 1,168 | 1,168 (unchanged) |

Family workflow subtotals: Sell & Serve 1,146 → **1,194** (+48 via VS-139 + VS-140); Asset &
Infrastructure 224 → **248** (+24 via VS-138); Technology & Data 302 → **326** (+24 via VS-137);
all other families unchanged.

The 96 new workflows carry a keyword-driven proposed tier in `workflow-criticality-proposed.md`
(regenerated by `07-methodology/classify-workflows.py`, relabelled Pass 13): 2 proposed Tier 1
(facilities business-continuity/critical-systems resilience in VS-138, and event HSE/incident
management in VS-139), 2 proposed Tier 3 (BMS/IoT integration and HVAC/environmental-control
optimization in VS-138), and 92 Tier 2 (the four are shared-service/B2B-growth disciplines, so
most land at the safe Tier-2 default). They will be rolled into the dependency graph, touchpoint
map, and requirement-to-workflow matrix during the next confirmed-classification pass, matching
the Pass 1–Pass 12 pattern.

`07-methodology/validate-repo.sh` passes with **0 errors** after the additions (grand total 4,092
matches actual PA workflow header count 4,092; all 1,168 classified IDs resolve; all 2,947 proposed
IDs resolve and do not duplicate the confirmed register; no dangling references; no placeholder
content; no empty process areas).

---

## 2026-06-15 — Workflow gap analysis (Pass 12): add VS-133–VS-136 (96 workflows W4049–W4144)

A twelfth gap-analysis pass added four more value streams (3 process areas, 24 workflows each),
each filling a genuinely-unowned **enterprise-management discipline** whose defining terms
appeared in **zero** PA files as dedicated workflow headers (only incidental single-step
references to the broader capability existed, scattered across multiple adjacent value streams).
The four were chosen to be **distinct from the Pass 11 set (VS-129–VS-132: competition law, M&A,
human rights, political engagement)** — they cover operational excellence/continuous improvement,
organizational change management, technology financial management/FinOps, and supply-chain
network/inventory engineering. The pass deliberately strengthened three of the four thinnest-
by-workflow families (People, Technology & Data, Make & Move) plus the cross-cutting Governance &
Assurance family.

- **VS-133 — Operational Excellence, Process Mining & Continuous Improvement Program**
  (Governance & Assurance, W4049–W4072): owns the continuous-improvement operating system —
  process architecture/ownership, Lean/Six Sigma methodology, an improvement-opportunity
  pipeline, process/task mining from ERP/POS/WMS event logs, bottleneck & root-cause analysis,
  standard-work/SOP authoring, pilot execution, benefit-case modeling & realization,
  productivity/cost-out programs, and a kaizen culture. Genuinely uncovered ('operational
  excellence', 'process mining', 'continuous improvement', 'lean', 'six sigma', 'kaizen' each
  appeared in zero PA files; the only matches were literal 'cleaning/cleanup' workflows).
  Distinct from emerging-tech scouting/PoCs (VS-30), audit assurance (VS-21), and project
  delivery (VS-112).
- **VS-134 — Organizational Change Management, Digital Adoption & Transformation Enablement**
  (People, W4073–W4096): owns the people-side-of-change discipline — change portfolio & capacity
  planning, stakeholder mapping, change-impact & readiness assessment, sponsor activation, the
  equip-the-manager cascade, the super-user/champion network, resistance & change-saturation
  management, change communications, go-live readiness/hypercare, digital-adoption-platform
  operations, adoption measurement & sustainment, and benefit realization. Genuinely uncovered
  ('change management', 'OCM', 'change enablement', 'adoption management' each appeared in zero
  PA files; only ~45 incidental mentions). Distinct from the digital-transformation portfolio
  (VS-30.1), project delivery (VS-112), training content (VS-19.4/VS-124), HR operations
  (VS-103), and the IT service desk (VS-27.1).
- **VS-135 — Technology Business Management, IT Financial Management & Cloud FinOps**
  (Technology & Data, W4097–W4120): owns the financial-management-of-technology discipline —
  the TBM cost taxonomy, zero-based & capacity-based IT budgeting, technology investment
  portfolio & TCO/business-case modeling, demand management, showback/chargeback, application
  run-cost/rationalization, cloud FinOps (inform/optimize/operate: spend visibility, rightsizing,
  reservations/commitments, waste elimination, anomaly detection), SaaS license utilization &
  renewal optimization, shadow-IT discovery, value realization, and unit economics.
  Genuinely uncovered ('finops', 'cloud cost', 'technology business management', 'IT financial
  management', 'TBM' each appeared in zero PA files). Distinct from IT asset lifecycle (VS-99),
  application-landscape design (VS-113), platform operations (VS-27), and enterprise FP&A
  (VS-17.4/VS-33).
- **VS-136 — Supply Chain Network Design, Multi-Echelon Inventory Optimization & Flow
  Engineering** (Make & Move, W4121–W4144): owns the network/inventory-engineering discipline —
  network strategy & modeling/scenario simulation, DC footprint/location/capacity optimization,
  store coverage/territory, inbound sourcing-lane & outbound distribution-flow architecture,
  network resilience/redundancy, inventory strategy (postponement/pooling), multi-echelon
  inventory optimization (MEIO), safety-stock & service-level optimization, ABC/XYZ-differentiated
  policy, slow-mover/obsolescence optimization, simulation/digital-twin stress-testing, and a
  continuous re-optimization cycle. Genuinely uncovered ('multi-echelon', 'inventory
  optimization', 'network design', 'safety stock optimization' each appeared in zero PA files;
  only the single periodic W183 network-review workflow in VS-02.3). Distinct from operational
  replenishment (VS-02), the S&OP consensus cycle (VS-127), inventory transactions/lifecycle
  (VS-05), and logistics execution (VS-06).

### Repository totals after Pass 12

| Metric | Before (Pass 11) | After (Pass 12) |
|---|---|---|
| Value streams | 128 | **132** |
| Process areas | 388 | **400** |
| Workflows | 3,900 | **3,996** (+96) |
| Unclassified (keyword-proposed pending review) | 2,755 | **2,851** |
| Confirmed-classified (Tier 1/2/3) | 1,168 | 1,168 (unchanged) |

Family workflow subtotals: Make & Move 355 → **379** (+24 via VS-136); People 242 → **266**
(+24 via VS-134); Technology & Data 278 → **302** (+24 via VS-135); Governance & Assurance
720 → **744** (+24 via VS-133); all other families unchanged.

The 96 new workflows carry a keyword-driven proposed tier in `workflow-criticality-proposed.md`
(regenerated by `07-methodology/classify-workflows.py`, relabelled Pass 12): 3 proposed Tier 1
and 93 Tier 2 (the four are enterprise-management disciplines, not statutory/gating controls, so
most land at the safe Tier-2 default). They will be rolled into the dependency graph, touchpoint
map, and requirement-to-workflow matrix during the next confirmed-classification pass, matching
the Pass 1–Pass 11 pattern.

`07-methodology/validate-repo.sh` passes with **0 errors** after the additions (grand total
3,996 matches actual PA workflow header count 3,996; all 1168 classified IDs resolve; all 2851
proposed IDs resolve and do not duplicate the confirmed register; no dangling references; no
placeholder content; no empty process areas).

---

## 2026-06-15 — Workflow gap analysis (Pass 11): add VS-129–VS-132 (96 workflows W3953–W4048)

An eleventh gap-analysis pass added four more value streams (3 process areas, 24 workflows each),
each filling a capability previously reduced to a single workflow within another value stream or
genuinely uncovered with no dedicated owner. The four were chosen to be **distinct from the
Pass 10 set (VS-125–VS-128: fraud, CDP, S&OP, AI governance)** — they cover competition law,
corporate development/M&A, supply-chain human rights, and political engagement, all of which
remained genuinely uncovered after Pass 10.

- **VS-129 — Competition & Antitrust Compliance (RA 10667 / PCC)** (Governance & Assurance,
  W3953–W3976): elevates the single competition-law workflow W2683 in VS-76.2 into a full
  market-power/pricing-conduct/RPM-and-vertical-restraint/association-protocol/merger-notification/
  PCC-engagement-and-investigation/leniency/penalty/remediation program. Distinct from competitive
  price intelligence (VS-57), revenue assurance (VS-118), government affairs (VS-104), ABC (VS-86),
  fraud management (VS-125), and M&A execution (VS-130).
- **VS-130 — Corporate Development, Mergers, Acquisitions, Divestiture & Strategic Transactions**
  (Governance & Assurance, W3977–W4000): owns the end-to-end inorganic-growth/M&A/divestiture
  lifecycle (strategy, target sourcing, valuation, deal structuring, due diligence, SPA, regulatory
  clearance incl. PCC via VS-129, Day-1 cutover, post-merger integration/synergy, carve-out/TSA,
  divestiture, value realization). Genuinely uncovered. Distinct from strategic planning (VS-33),
  store opening (VS-37), capex accounting (VS-40), PMO (VS-112), legal (VS-100), and competition
  clearance (VS-129).
- **VS-131 — Human Rights, Modern Slavery & Responsible Supply Chain Due Diligence** (Plan &
  Source, W4001–W4024): owns the enterprise human-rights due-diligence program per the UNGPs across
  own operations and the ~40%-import global supply chain (policy/saliency/HRDD, supply-chain mapping,
  code/contract safeguards, modern-slavery/forced-labor risk modeling, responsible recruitment,
  social-compliance audit, worker voice/grievance, remediation/responsible disengagement, conflict
  minerals, living-wage, KPIs and UK MSA/German LkSG/EU CSDDD/US UFLPA reporting). Genuinely
  uncovered. Distinct from ESG reporting (VS-25), vendor operations (VS-03), global sourcing (VS-122),
  product quality (VS-31), internal ethics (VS-119), and S&OP (VS-127).
- **VS-132 — Corporate Political Engagement, Election Compliance & Public Affairs Governance**
  (Governance & Assurance, W4025–W4048): owns the lawful-and-accountable-political-activity program
  under the Omnibus Election Code, RA 9006/COMELEC, RA 3019 anti-graft, and RA 6713 (policy/risk,
  contribution controls/disclosure, lobbying governance, association review, election-period
  compliance, campaign-finance controls, anti-graft official-interaction controls, grassroots/
  employee political-activity governance, board oversight). Genuinely uncovered. Distinct from
  government-affairs relationships (VS-104), ABC (VS-86), ethics (VS-119), B2G sales (VS-46), and
  corporate communications (VS-14.3).

### Repository totals after Pass 11

| Metric | Before (Pass 10) | After (Pass 11) |
|---|---|---|
| Value streams | 124 | **128** |
| Process areas | 376 | **388** |
| Workflows | 3,804 | **3,900** (+96) |
| Unclassified (keyword-proposed pending review) | 2,659 | **2,755** |
| Confirmed-classified (Tier 1/2/3) | 1,168 | 1,168 (unchanged) |

Family workflow subtotals: Plan & Source 404 → **428** (+24 via VS-131); Governance & Assurance
648 → **720** (+72 via VS-129/VS-130/VS-132); all other families unchanged.

The 96 new workflows carry a keyword-driven proposed tier in `workflow-criticality-proposed.md`
(regenerated by `07-methodology/classify-workflows.py`): 4 proposed Tier 1 (statutory/gating
controls) and 92 Tier 2. They will be rolled into the dependency graph, touchpoint map, and
requirement-to-workflow matrix during the next confirmed-classification pass, matching the
Pass 1–Pass 10 pattern.

`07-methodology/validate-repo.sh` passes with **0 errors** after the additions (grand total
3,900 matches actual PA workflow header count 3,900; all PA counts match the index; no dangling
references; no placeholder content).

---

## 2026-06-15 — Workflow review implementation (2/5): keyword-driven classification pass (P2)

Second commit of the review-implementation program. **2,659 workflows (70% of the estate) had no
criticality tier**, so the go-live sequencing (Tier 1/2/3) could not be applied to most of the
repository. Rather than bury ~2,600 auto-classified rows inside the authoritative hand-reviewed
register, the proposal is kept in a **separate, clearly-marked, reversible** companion file:

- **New [`07-methodology/classify-workflows.py`](07-methodology/classify-workflows.py)** — a reusable, documented classifier. It assigns a Tier 1/2/3 proposal to every workflow not in the confirmed register, using conservative keyword rules over the workflow *name* plus whole-family overrides for wholly-statutory value streams (VS-79 tax, VS-85 mandatory discount, VS-89 recall, VS-91 privacy, VS-114 DG/hazmat, VS-117 DTI-BPS, VS-118 revenue assurance, VS-125 fraud). VS-128 (AI *governance*) is handled specially so the regulator/risk framework lands Tier 1 while platform engineering lands Tier 2 — the AI *use-cases* elsewhere remain the Tier 3 candidates.
- **New [`workflows/workflow-criticality-proposed.md`](01-model-company/workflows/workflow-criticality-proposed.md)** — the proposed assignment for all 2,659 workflows (Tier 1: 606 · Tier 2: 1,925 · Tier 3: 128), grouped by tier then by value stream for review. On review, rows are promoted/demoted by moving them into the confirmed register.
- **Rules are deliberately conservative**: Tier 1 only on high-confidence statutory / core-transactional keywords; Tier 3 only on high-confidence advanced-tech keywords; everything else defaults to Tier 2 (the documented safe default). A first draft incorrectly matched against PA *filenames* (leaking broad category words like "settlement" into every workflow in a settlement PA); fixed to match the workflow name only.
- **`workflow-criticality-classification.md` summary** rewritten to separate *confirmed* (1,168) from *proposed* (2,659) and to show **0 workflows without even a proposal**.
- **`validate-repo.sh` Check 1** enhanced: recognises the proposed file, reports `N unclassified in confirmed; M have a proposed tier; K have no proposal yet`, and verifies every proposed ID resolves to a real header and does not duplicate the confirmed register.

Validator: 0 errors / 2 warnings. The two remaining warnings (boilerplate fields, unclassified-in-confirmed) are addressed in subsequent commits.

---

## 2026-06-15 — Workflow review implementation (1/5): structural-integrity fixes (P4) + validator reverse-check

First commit of a five-commit program implementing the recommendations from a value-stream/workflow
review. This commit delivers the bounded, structural fixes plus a new validator check that prevents
regression of the defects it corrects:

- **W54A (BIR Computerized Accounting System (CAS) Registration) classified as Tier 1** in `workflow-criticality-classification.md` (Core Compliance & IT) — it was referenced as a Tier-1 hard prerequisite in the dependency map's deepest chain but was never in the classification table. Section/subtotal/summary counts updated (Tier 1: 439 → 440; classified total: 1,167 → 1,168).
- **Deepest dependency-chain count corrected** in `workflow-dependency-map.md` ("48 workflows" → "46 workflows") — the block actually lists 46 unique workflow IDs.
- **Block/origin legend + per-row `Block` column** added to `value-stream-index.md` summary table, so a reader can gauge content maturity at a glance (Core VS-01–48, Expansion VS-53–78, Statutory VS-79–88, Gap analysis VS-89–128; retired VS-49–52).
- **New `validate-repo.sh` Check 11** — verifies the dependency map's "deepest dependency chain (all Tier 1)" block is internally consistent: the stated total equals the unique workflow count, and every workflow in the chain is classified Tier 1 (scanning both the main Tier 1 section and the "Tier 1 Additions" tail subsection). This is a *reverse* check (dependency-claim → classified) that the existing checks could not catch. Uses here-strings to avoid a `grep -q` / `pipefail` SIGPIPE false-negative.

Validator now passes with 0 errors / 2 warnings (the 2 warnings are the known unclassified + boilerplate counts, addressed in subsequent commits).

---

## 2026-06-15 — Workflow gap analysis (Pass 10): add VS-125–VS-128 (96 workflows W3857–W3952)

A tenth gap-analysis pass added four new value streams, each filling a genuinely-unowned program
whose defining terms appeared in zero or near-zero PA files:

- **[VS-125 (Cross-Channel Fraud Management & Payment Fraud Protection — Finance)](01-model-company/workflows/VS-125-cross-channel-fraud-management-payment-fraud-protection/README.md)** — the enterprise fraud program across POS/ecommerce/returns/promo/loyalty/gift-card/payment/account-takeover/trade channels ('fraud orchestration' appeared in zero PA files), distinct from physical shrink (VS-23), revenue leakage (VS-118), payment operations (VS-80), AML (VS-86), and data privacy (VS-91).
- **[VS-126 (Customer Data Platform, Single Customer View & Identity Resolution — Technology & Data)](01-model-company/workflows/VS-126-customer-data-platform-single-customer-view-identity-resolution/README.md)** — the CDP platform and single-customer-view discipline ('customer golden record' in zero PA files), distinct from foundational master data (VS-29), loyalty ops (VS-13), privacy (VS-91), key-account (VS-107), and enterprise BI (VS-28).
- **[VS-127 (Sales & Operations Planning (S&OP) & Integrated Business Planning — Plan & Source)](01-model-company/workflows/VS-127-sales-operations-planning-integrated-business-planning/README.md)** — the monthly cross-functional consensus demand-supply planning cycle ('integrated business planning'/'IBP' in zero PA files), distinct from operational supply (VS-02), merchandise financial planning (VS-101), corporate strategy (VS-33), assortment (VS-01), and commodity risk (VS-106).
- **[VS-128 (AI/ML Governance & Responsible AI — Technology & Data)](01-model-company/workflows/VS-128-ai-ml-governance-responsible-ai/README.md)** — the enterprise AI-governance and responsible-AI discipline ('model risk management' and 'algorithmic fairness' in zero PA files), distinct from AI engineering (VS-30.2), cybersecurity (VS-27.3), privacy (VS-91), architecture (VS-113), and enterprise audit (VS-21).

Each new value stream has 3 process areas × 8 workflows = 24 workflows, following the standard
format (Trigger / Frequency / Volume / Owner / Participants / Steps table with R+A columns /
System Touchpoints / Time Estimate / Pain Points & Risks), with workflow-specific (non-boilerplate)
analysis fields and cross-references throughout. Totals updated: **120 → 124 value streams**, **356
→ 368 process areas**, **3,708 → 3,804 workflows**. The 96 new workflows are unclassified pending
the next criticality review. `07-methodology/validate-repo.sh` passes with 0 errors. See
[`workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md) for the
full Pass 10 methodology, candidate gaps considered and rejected, and family-subtotal impact.

---

## 2026-06-15 — Workflow documentation review: format guide, index, validator

A review of the value-stream and workflow documentation identified two issues: (1) the
[`WORKFLOW-FORMAT-GUIDE.md`](01-model-company/workflows/WORKFLOW-FORMAT-GUIDE.md) documented a
full RACI (R/A/C/I) key that the actual per-step tables never implemented (only R and A columns
are used), described a `W<number>` / `W<number><letter>` ID scheme that no longer reflected the
sequential 4-digit IDs used by newer value streams, and omitted two fields (Automation
Opportunity, Controls) that directly serve the workflows' stated purposes; and (2) **552
workflows across 23 value streams (VS-53–VS-78) — 15% of the 3,708 total — carry verbatim
boilerplate** in their three analysis fields (Pain Points / System Touchpoints / Time Estimate),
defeating the headcount-validation and ERP-design purposes those fields exist to serve.

This commit addresses the **documentation layer only** (no workflow content was rewritten):

- **[`WORKFLOW-FORMAT-GUIDE.md`](01-model-company/workflows/WORKFLOW-FORMAT-GUIDE.md)** — rewritten
  to match actual conventions: R/A-only per-step tables (C/I captured at workflow level), the
  real ID scheme (sequential 4-digit `W` numbers + legacy letter-suffixed variants), an explicit
  quality bar for the three analysis fields (with ❌/✅ examples), and two recommended fields
  (Automation Opportunity, Controls) closing the loop with
  [`internal-controls-matrix.md`](01-model-company/internal-controls-matrix.md).
- **[`value-stream-index.md`](01-model-company/workflows/value-stream-index.md)** and
  **[`README.md`](README.md)** — the ~2,500-word nine-pass gap-analysis narrative (duplicated in
  both files and already covered by the per-pass CHANGELOG entries below) was replaced with a
  concise one-paragraph summary pointing to CHANGELOG and
  [`workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md) for detail.
- **[`07-methodology/validate-repo.sh`](07-methodology/validate-repo.sh)** — added Check 10, which
  detects the verbatim boilerplate marker in analysis fields and reports the affected value
  streams as **warnings** (surfaces the defect list without failing the build, since the templated
  content has not yet been reworked).

**Deferred (judgment calls, not done here):** whether to rework or relabel-as-stub the 552
templated workflows; whether to consolidate the 46 value streams that were "elevated from a
single workflow" or fit the uniform 8×3=24 pattern; and whether to add a machine-readable
`workflows.csv` sidecar. The validator's Check 10 output quantifies the first of these.

---

## 2026-06-14 — Workflow Gap Analysis (Pass 9): Add VS-121–VS-124 (96 workflows W3761–W3856)

A ninth workflow **gap-analysis** pass was performed against the model company's operations
(BuildRight Depot Corp. — Philippine hardware/DIY/home-improvement big-box retailer: 200 stores,
4 DCs, 35,000 active SKUs, ~PHP 62.3B annual revenue, 5 legal entities, ~6,715 employees). After
Passes 1–8 had filled the genuinely-uncovered *operational* and *statutory* capabilities across
Make & Move, Asset & Infrastructure, Technology & Data, Finance, and Governance & Assurance,
Pass 9 targeted the remaining genuinely-uncovered **strategic people-attraction and selling-
effectiveness** disciplines, which cluster in **People** (the thinnest family by workflow count at
194). Each candidate gap was validated by keyword search across all PA files and confirmed to be
**genuinely uncovered** — the defining terms ('candidate experience'/'career site'/'talent
community', 'global sourcing'/'sourcing agent'/'overseas buying office', 'apprenticeship program',
and 'clienteling') each appeared in **zero** PA files, with only incidental single-workflow
references to the broader capability. The four new value streams add two to **People** (VS-121,
VS-123), one to **Plan & Source** (VS-122), and one to **Sell & Serve** (VS-124). Methodology and
results (including the full list of rejected-as-covered candidates) are documented in
[`01-model-company/workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md).

- **VS-121 Talent Acquisition, Employer Brand & Candidate Experience** (People) — owns the
  strategic attraction and candidate-side of hiring for ~1,200–1,600 hires/yr at 15–20% turnover
  across a 5-entity, 205-location group: employer brand/EVP, career-site product, talent-marketing
  & sourcing-channel strategy, candidate experience & candidate-NPS, talent community/CRM, and
  TA operations/analytics; distinct from recruitment *transaction* processing (VS-19.1), total-
  rewards design (VS-102), employee experience (VS-103.2), and trade-capability building (VS-123).
- **VS-122 Global Sourcing, Import Buying & Sourcing Agent Management** (Plan & Source) — owns
  the strategic source-side of imported merchandise for the ~40%-import assortment (~PHP 17–18B/yr,
  ~400 international vendors, ~400–600 TEUs/month): source-market/country strategy, sourcing-model
  decision (direct vs agent vs overseas office), sourcing-agent & overseas-buying-office governance,
  import vendor development, consolidated container buying, and total-landed-cost sourcing
  analytics; distinct from operational import/customs (VS-02.2), transactional vendor/PO (VS-03),
  customs compliance (VS-87), quality (VS-31), and commodity hedging (VS-106).
- **VS-123 Skilled-Trade Apprenticeship, Vocational Education & Capability Pipeline** (People) —
  owns BuildRight's own structured, TESDA-registered (RA 7796) apprenticeship and vocational
  capability pipeline for trade-knowledgeable staff: program design & registration, cohort
  operations, mentor/master-tradesperson network, competency assessment & certification,
  vocational-school feeder, instructor pipeline, and trade-capability analytics; distinct from
  general L&D (VS-19.4), customer-facing workshops/TESDA participation (VS-12.3 W1556), trade-
  customer training (VS-43.3), and general talent attraction (VS-121).
- **VS-124 Sales Enablement, Product Knowledge Mastery & Clienteling** (Sell & Serve) — owns the
  associate selling-effectiveness discipline across ~5,800 store staff serving 2.8M monthly
  transactions: selling-skills curriculum & coaching, product-knowledge mastery & certification,
  department/category attach playbooks, clienteling tool & customer-360 at POS, trade-pro/B2B
  consultative selling enablement, selling-quality assurance, and selling-effectiveness analytics;
  distinct from general L&D (VS-19.4), loyalty/CRM (VS-13), store operations (VS-07), in-store
  services (VS-09), and trade-capability building (VS-123).

**Counts**: 3,612 → **3,708** workflows; 116 → **120** value streams; 352 → **356** process
areas. Family impact: People 194 → **242** (+48), Plan & Source 356 → **380** (+24), Sell & Serve
1,122 → **1,146** (+24). The 96 new workflows are unclassified pending a follow-up criticality
review (exactly as Passes 1–8 were handled). `07-methodology/validate-repo.sh` passes with **0
errors**.

---

## 2026-06-14 — Workflow Gap Analysis (Pass 8): Add VS-117–VS-120 (96 workflows W3665–W3760)

An eighth workflow **gap-analysis** pass was performed against the model company's operations
(BuildRight Depot Corp. — Philippine hardware/DIY/home-improvement big-box retailer: 200 stores,
4 DCs, 35,000 active SKUs, ~PHP 62.3B annual revenue, 5 legal entities). After Passes 1–7, the
thinner operating families (People, Technology & Data, Make & Move) were substantially
strengthened; Pass 8 targeted the remaining genuinely-uncovered capabilities, which cluster in
**Governance & Assurance** and **Finance**. Each candidate gap was validated by keyword search
across all PA files: three were confirmed to be a **single workflow within another value stream**
ripe for elevation to a dedicated end-to-end program (the same pattern used in Pass 1/5/7), and
the fourth was genuinely uncovered with only incidental references and no dedicated owner. The
four new value streams add one each to **Finance** (VS-118), **Asset & Infrastructure** (VS-120),
and two to **Governance & Assurance** (VS-117, VS-119). Methodology and results (including the
full list of rejected-as-covered candidates) are documented in
[`01-model-company/workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md).

- **VS-117 DTI-BPS Product Standards Certification & PS Mark/ICC Compliance** (Governance &
  Assurance) — elevates the single import-clearance workflow W447 (VS-22.1) to a full PS-Mark-
  license / vendor-certification / import-ICC-SOC / accredited-testing / ICC-sticker /
  market-surveillance / vendor-recovery program for the ~44%-regulated assortment (steel, cement,
  PVC, electrical, tiles, paint) and ~40% imports; distinct from customs (VS-87), internal quality
  (VS-31), recall (VS-89), DG (VS-114), and vendor management (VS-03).
- **VS-118 Revenue Assurance, Pricing Integrity & Leakage Management** (Finance) — elevates the
  single monthly-audit workflow W348 (VS-21.3) to a continuous, all-channel revenue-protection /
  leakage-detection / recovery program spanning pricing, promo, loyalty, gift-card, mandatory-
  discount, catch-weight/weighing, payment/MDR, ecommerce/marketplace settlement, and refund/
  reversal integrity (PHP 0.6B–1.9B/yr leakage exposure at PHP 62.3B revenue); distinct from the
  periodic audit (VS-21.3), inventory shrink (VS-23), POS execution (VS-08), and FP&A (VS-17.4).
- **VS-119 Whistleblower, Ethics & Corporate Integrity (Speak-Up) Program** (Governance &
  Assurance) — extends the ABC-specific W2943 (VS-86.3) to an enterprise multi-channel-intake /
  triage / independent-investigation / retaliation-protection / culture / analytics program across
  all violation types; distinct from the ABC regime (VS-86), internal audit (VS-21), legal
  (VS-100), loss prevention (VS-23), labor relations (VS-84), and HR case management (VS-103).
- **VS-120 Energy Efficiency, Conservation & RA 11285 Compliance Program** (Asset &
  Infrastructure) — fills the genuinely-uncovered statutory energy-management program for ~205
  RA 11285 designated-establishment sites (EEO designation, mandatory energy audit, conservation
  plan, DOE reporting, ISO 50001 EnMS, ECM pipeline, M&V, retail-competition energy procurement);
  distinct from facility maintenance (VS-20.3), ESG reporting (VS-25), own-generation (VS-108),
  expense procurement (VS-34), and store remodel (VS-109).

**Candidate gaps considered but rejected as adequately covered** (documented in the gap-analysis
file): PIM/DAM/product-content (PA-01.3), vendor routing-guide/ASN (VS-110.2), fleet/telematics
(VS-06/VS-61), ORC/refund/loyalty/gift-card fraud (VS-23), product-liability claims (W185/W863/
W1566/VS-100), B2B job-costing/progress-billing (VS-11), DEIB (W719/W3343), carbon/GHG/net-zero
(W192/W3466), pricing/markdown (VS-01.2/VS-57/VS-101), tool repair (VS-12), and AI/model-risk
governance (VS-30.2/VS-113, emerging).

### Updated counts

| Metric | Before | After |
|---|---|---|
| Value streams | 112 | **116** (+4) |
| Process areas | 340 | **352** (+12) |
| Workflows | 3,516 | **3,612** (+96) |
| Unclassified workflows | 2,349 | **2,445** (+96; pending criticality review) |

Family subtotals after Pass 8: Governance & Assurance 600→**648** (+48 via VS-117 + VS-119);
Finance 459→**483** (+24 via VS-118); Asset & Infrastructure 200→**224** (+24 via VS-120);
Plan & Source 356, Make & Move 355, Sell & Serve 1,122, People 194, Technology & Data 230
unchanged.

### Changed

- Created 4 new value-stream directories (`VS-117`…`VS-120`) with README + 3 PA files each (16 new
  files, 96 workflows W3665–W3760).
- Updated cross-reference docs: value-stream-index (summary table, detailed map, decision tree,
  grand total), README, executive-summary, workflows/README (stats, family sections, subtotals,
  note), workflow-gap-analysis (Pass 8 gaps #31–34, Pass 8 value-stream table, family-impact table,
  deferred-gaps, rejected candidates), workflow-criticality-classification (unclassified/grand-total
  counts, version v7.9, Pass 8 footer note), workflow-dependency-map (totals, version v2.10),
  workflow-system-touchpoint-map (totals, version 61.0), CHANGELOG.
- Validator (`07-methodology/validate-repo.sh`) passes with **0 errors** (1 informational warning
  for the 2,445 unclassified workflows pending criticality review, consistent with prior passes).

---

## 2026-06-14 — Workflow Gap Analysis (Pass 7): Add VS-113–VS-116 (96 workflows W3569–W3664)

A seventh workflow **gap-analysis** pass was performed against the model company's operations
(BuildRight Depot Corp. — Philippine hardware/DIY/home-improvement big-box retailer: 200 stores,
4 DCs, 35,000 active SKUs, ~PHP 62.3B annual revenue, 5 legal entities). Pass 7 targeted
capabilities that were **genuinely uncovered by every value stream, referenced across many PA
files with no dedicated owner, conflated with a fixed-site HSE capability, or reduced to single
steps within B2G/B2B/treasury value streams**. Each candidate gap was validated by keyword search
across all PA files to confirm it had no dedicated value stream and to scope it distinct from
adjacent ones. The four new value streams deliberately strengthen the thinnest family by workflow
count — **Technology & Data** (+48 via VS-113 and VS-115) — and add one each to **Governance &
Assurance** (VS-114) and **Finance** (VS-116). Methodology and results are documented in
[`01-model-company/workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md).

### Added — 4 new value streams, 12 process areas, 96 workflows

| VS | Value Stream | Family | W-range |
|---|---|---|---|
| **VS-113** | Enterprise Architecture, Application Portfolio & Technology Strategy | Technology & Data | W3569–W3592 |
| **VS-114** | Dangerous Goods (DG) & Hazmat Transport, Ecommerce & Regulatory Compliance | Governance & Assurance | W3593–W3616 |
| **VS-115** | Calibration, Metrology & Measurement Traceability Management | Technology & Data | W3617–W3640 |
| **VS-116** | Performance Bond, Surety & Bank Guarantee Management | Finance | W3641–W3664 |

Each value stream comprises a README plus three process-area files (8 workflows each), all fully
specified (trigger, frequency, volume, owner, participants, steps with RACI, system touchpoints,
pain points, time estimates) and cross-referenced to adjacent value streams.

### Rationale (gaps filled)

- **VS-113 Enterprise Architecture, Application Portfolio & Technology Strategy** — a 5-entity,
  200-store, PHP 62.3B-revenue retailer on a unified cloud ERP with ~10+ active integration
  touchpoints and an expanding digital perimeter (ecommerce, marketplace, retail media, mobile app,
  BIR e-invoicing, AI/ML) requires a continuous enterprise-architecture discipline, yet 'enterprise
  architecture' appeared in **0** PA files. VS-27 operates/secures platforms, VS-28 consumes data,
  VS-30 evaluates emerging tech/POCs, VS-99 manages hardware/software asset lifecycle — none designs
  and governs the application landscape, integration architecture, technology standards, solution
  architecture, or technology strategy. Distinct from all four.
- **VS-114 Dangerous Goods (DG) & Hazmat Transport, Ecommerce & Regulatory Compliance** — an 8–10%+
  DG-intensive assortment (paint/solvents ~2,800 SKUs, adhesives/thinners, aerosols, garden/agro
  chemicals, lithium batteries) moves by ocean, inter-island, road, and ecommerce last-mile under
  DENR-EMB RA 6969, BFP Fire Code, DOLE OSH, MARINA/Coast Guard, CAB, LTFRB/DOTC, and IMDG/IATA/ADR.
  VS-24.3 (HSE) covers only **fixed-site** storage safety; VS-87 import customs; VS-89 recall; VS-111
  product/transport packaging generally — no value stream owned the DG transport, ecommerce
  ship-eligibility, documentation/carrier-qualification, hazardous-waste transport manifest, or
  incident/claim lifecycle. Distinct from all four and from VS-06/VS-110 logistics execution.
- **VS-115 Calibration, Metrology & Measurement Traceability Management** — catch-weight/cut-to-length
  selling at 600 POS across 2.8M monthly transactions, custom fabrication (pipe/lumber/sheet/wire
  cutting) and paint mixing/tinting at every store, DC weighbridges/truck scales at 4 DCs, fuel &
  logistics meters, environmental/process instruments, and test & measurement tools. Calibration/
  metrology was referenced incidentally across **53** PA files with **no dedicated owner** and **zero**
  PA with 'calibration'/'metrology' in its title. No value stream owned the program, standards/
  traceability (ISO 17025), scheduling, records, or DTI weights & measures compliance. Distinct from
  POS operations, in-store services, DC operations, quality testing, master data, and facility
  maintenance.
- **VS-116 Performance Bond, Surety & Bank Guarantee Management** — ~10% B2G + ~30% B2B/project
  revenue under RA 9184 and large enterprise contracts require bid/performance/payment/warranty
  bonds, bank guarantees, LCs, and cash retention that encumber on the order of **PHP 5M–50M+** of
  credit facility simultaneously. VS-46 (B2G) references the bond as one bid step, VS-11 (B2B/project)
  references tender/performance bonds in bidding, VS-18 (Treasury) manages the bank/facility — no
  value stream owned the surety facility strategy, bond application/issuance/tracking/encumbrance
  lifecycle, counter-indemnity/collateral, release/closeout, claim/default response, or surety
  analytics. Distinct from B2G/B2B sales, treasury, trade credit, cross-entity billing, and legal
  operations.

### Updated counts

| Metric | Before | After |
|---|---|---|
| Value streams | 108 | **112** (+4) |
| Process areas | 328 | **340** (+12) |
| Workflows | 3,420 | **3,516** (+96) |
| Unclassified workflows | 2,253 | **2,349** (+96; pending criticality review) |

Family subtotals after Pass 7: Technology & Data 182→**230** (thinnest family, +48); Finance
435→**459**; Governance & Assurance 576→**600**; Plan & Source 356, Make & Move 355, Sell & Serve
1,122, People 194, Asset & Infrastructure 200 unchanged.

### Changed

- Created 4 new value-stream directories (`VS-113`…`VS-116`) with README + 3 PA files each (16 new
  files, 96 workflows W3569–W3664).
- Updated `value-stream-index.md` (architecture line, coverage note, summary table + subtotals,
  detailed map, decision tree, footer).
- Updated `README.md`, `executive-summary.md`, `workflows/README.md` (counts, folder structure,
  coverage note, reconciliation, diagram).
- Extended `workflow-gap-analysis.md` (Pass 7 gaps, candidate table, new-VS table, family-subtotal
  impact, validation, deferred-gaps, and Pass-7 rejected candidates).

---

## 2026-06-14 — Workflow Gap Analysis (Pass 6): Add VS-109–VS-112 (96 workflows W3473–W3568)

A sixth workflow **gap-analysis** pass was performed against the model company's operations
(BuildRight Depot Corp. — Philippine hardware/DIY/home-improvement big-box retailer: 200 stores,
4 DCs, 35,000 active SKUs, ~PHP 62.3B annual revenue, 5 legal entities). Pass 6 targeted
capabilities that were **genuinely uncovered by any value stream, sprinkled across multiple value
streams without a single owner, or conflated with the financial-accounting view of an asset**.
Each candidate gap was validated by keyword search across all PA files to confirm it had no
dedicated value stream and to scope it distinct from adjacent ones. The four new value streams are
concentrated in the two thinnest families by *workflow count* — **Make & Move** (+48) and **Asset &
Infrastructure** (+48). Methodology and results are documented in
[`01-model-company/workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md).

### Added — 4 new value streams, 12 process areas, 96 workflows

| VS | Value Stream | Family | W-range |
|---|---|---|---|
| **VS-109** | Store Remodel, Renovation & Lifecycle Refurbishment Program | Asset & Infrastructure | W3473–W3496 |
| **VS-110** | Freight Procurement, Carrier Management & Freight Audit | Make & Move | W3497–W3520 |
| **VS-111** | Packaging, Pallet & Returnable Transport Item (RTI) Management | Make & Move | W3521–W3544 |
| **VS-112** | Corporate Project & Program Management Office (PMO) | Asset & Infrastructure | W3545–W3568 |

Each value stream comprises a README plus three process-area files (8 workflows each), all fully
specified (trigger, frequency, volume, owner, participants, steps with RACI, system touchpoints,
pain points, time estimates) and cross-referenced to adjacent value streams.

### Rationale (gaps filled)

- **VS-109 Store Remodel, Renovation & Lifecycle Refurbishment Program** — a 200-store chain
  remodels on a ~5–7-year cycle (~30–40 events/year at PHP 8–25M each; ~PHP 300–700M/yr program),
  yet no value stream owned the *operational* remodel program. VS-37 covers only new-store
  opening, VS-59 only closure, VS-20 only new-build construction, VS-97 the landlord view, and
  VS-40 only the capex *accounting*. Distinct from all five.
- **VS-110 Freight Procurement, Carrier Management & Freight Audit** — freight is a major cost
  line (inbound/import/line-haul/last-mile) that was sprinkled across VS-02.2 (import freight,
  W66, W249), VS-04 (DC), VS-06.1 (outbound), and VS-06.3 (last-mile, incl. the single
  carrier-rate/freight-audit workflow W1166). No value stream owned the end-to-end
  carrier-contracting/routing-guide/freight-audit/landed-cost discipline. Distinct from VS-06
  (execution), VS-56 (3PL last-mile partner), VS-87 (customs), and VS-15 (AP).
- **VS-111 Packaging, Pallet & Returnable Transport Item (RTI) Management** — at BuildRight's
  volume, packaging/pallets/RTI are a PHP 200–500M/yr cost line, a damage/shrink source, a
  freight-cube driver, and a sustainability/EPR (RA 11898) exposure, referenced incidentally across
  VS-04/VS-05/VS-06/VS-32/VS-73/VS-41/VS-87/VS-24.3 with no dedicated owner. Distinct from DC
  operations, merchandise inventory, logistics, returns, waste, and private-label development.
- **VS-112 Corporate Project & Program Management Office (PMO)** — PHP 800M–1.2B annual capex
  plus major transformation programs require portfolio governance/stage-gate/program-management/
  benefits-realization, but VS-40 performs only the *financial accounting* of capital projects
  (W1811–W2752) and VS-33 sets the budget envelope; no value stream owned the operational PMO
  discipline. Distinct from capex accounting, strategic planning, and the delivery-domain VSs.

### Updated counts

| Metric | Before | After |
|---|---|---|
| Value streams | 104 | **108** (+4) |
| Process areas | 316 | **328** (+12) |
| Workflows | 3,324 | **3,420** (+96) |
| Unclassified workflows | 2,157 | **2,253** (+96; pending criticality review) |

Family subtotals after Pass 6: Make & Move 307→**355**, Asset & Infrastructure 152→**200**;
Plan & Source 356, Sell & Serve 1,122, Finance 435, People 194, Governance & Assurance 576,
Technology & Data 182 unchanged.

### Changed

- Created 4 new value-stream directories (`VS-109`…`VS-112`) with README + 3 PA files each (16 new
  files, 96 workflows W3473–W3568).
- Updated `value-stream-index.md` (architecture line, coverage note, summary table + subtotals,
  detailed map, decision tree, footer).
- Updated `README.md`, `executive-summary.md`, `workflows/README.md` (counts, folder structure,
  coverage note, reconciliation).
- Extended `workflow-gap-analysis.md` (Pass 6 gaps, candidate table, new-VS table, family-subtotal
  impact, validation, deferred-gaps, and Pass-6 rejected candidates).

---

## 2026-06-14 — Workflow Gap Analysis (Pass 5): Add VS-105–VS-108 (96 workflows W3377–W3472)

A fifth workflow **gap-analysis** pass was performed against the model company's operations
(BuildRight Depot Corp. — Philippine hardware/DIY/home-improvement big-box retailer: 200 stores,
4 DCs, 35,000 active SKUs, ~PHP 62.3B annual revenue, 5 legal entities). Pass 5 targeted
capabilities that had been **overlooked because each existed only as a single workflow within
another value stream** (or was conflated with an adjacent covered capability) — the same pattern
used in Pass 1, where VS-89 Product Recall was elevated from the single customer-notification
workflow W776 in VS-09. Each of the four candidate gaps was validated by keyword search across
all PA files to confirm it had no dedicated value stream. The four new value streams are
distributed one each across Plan & Source, Sell & Serve, Finance, and Asset & Infrastructure
(the last being the thinnest family by value-stream count). Methodology and results are documented
in
[`01-model-company/workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md).

### Added — 4 new value streams, 12 process areas, 96 workflows

| VS | Value Stream | Family | W-range |
|---|---|---|---|
| **VS-105** | Supply Chain Finance & Working Capital Management | Finance | W3377–W3400 |
| **VS-106** | Commodity & Input-Cost Risk Management | Plan & Source | W3401–W3424 |
| **VS-107** | Strategic Key Account & Enterprise Customer Management | Sell & Serve | W3425–W3448 |
| **VS-108** | On-Site Renewable Energy & Prosumer Asset Operations | Asset & Infrastructure | W3449–W3472 |

Each value stream comprises a README plus three process-area files (8 workflows each), all fully
specified (trigger, frequency, volume, owner, participants, steps with RACI, system touchpoints,
pain points, time estimates) and cross-referenced to adjacent value streams.

### Rationale (gaps filled — each previously a single workflow or conflated with a covered capability)

- **VS-105 Supply Chain Finance & Working Capital Management** — the supplier-finance /
  reverse-factoring / dynamic-discounting / cash-conversion-cycle discipline existed only as the
  single program-summary workflow W324 in VS-18 (Treasury). No value stream owned the
  comprehensive SCF program (multi-funder facility, vendor enrollment, dynamic-discounting
  platform, CCC governance) that monetizes BuildRight's payer position across ~PHP 37B annual
  procurement spend and 30–60-day payment terms. Distinct from VS-18 (cash positioning), VS-15
  (P2P processing), and VS-39 (rebates).
- **VS-106 Commodity & Input-Cost Risk Management** — BuildRight's heavy commodity exposure
  (steel/cement/lumber 14%+14% of SKUs, copper 10%+12%, oil-derived paint/plastics 8%, ~40%
  import) had no dedicated owner; "commodity hedging" appeared in only 1 PA file. A 10% commodity
  swing can move COGS by ~PHP 0.5–1.5B and threatens the 28–32% gross-margin target. Distinct
  from VS-02 (supply operations), VS-18.3 (FX hedging only), and VS-101 (merchandise margin).
- **VS-107 Strategic Key Account & Enterprise Customer Management** — ~40% of revenue is
  concentrated in ~5,200 B2B accounts; the top ~700 strategic accounts warrant dedicated
  relationship/growth management, but "key account" was only sprinkled across VS-11/VS-43/VS-46/
  VS-13 (transactional trade, trade loyalty, government bidding, mass support). Distinct from all
  four and from VS-16/VS-68 (credit/billing).
- **VS-108 On-Site Renewable Energy & Prosumer Asset Operations** — BuildRight's own rooftop
  solar/storage generation across ~205 large rooftops (1.6–3.0M sqm) in a high-tariff market had
  no dedicated owner; only single monitoring workflows existed (W111 energy, W173 solar in
  VS-07/VS-20.3). Distinct from VS-70 (selling solar products to customers), VS-35 (fixed-asset
  accounting), and VS-25 (ESG reporting).

### Updated counts

| Metric | Before | After |
|---|---|---|
| Value streams | 100 | **104** (+4) |
| Process areas | 304 | **316** (+12) |
| Workflows | 3,228 | **3,324** (+96) |
| Unclassified workflows | 2,061 | **2,157** (+96; pending criticality review) |

Family subtotals after Pass 5: Plan & Source 332→**356**, Sell & Serve 1,098→**1,122**, Finance
411→**435**, Asset & Infrastructure 128→**152**; Make & Move 307, People 194, Governance &
Assurance 576, Technology & Data 182 unchanged.

### Changed

- Created 4 new value-stream directories (`VS-105`…`VS-108`) with README + 3 PA files each (16 new
  files, 96 workflows W3377–W3472).
- Updated `value-stream-index.md` (architecture line, coverage note, summary table + subtotals,
  detailed map, decision tree, footer).
- Updated `README.md`, `executive-summary.md`, `workflows/README.md` (counts, folder structure,
  coverage note, reconciliation).
- Updated `workflow-gap-analysis.md` (Pass 5 section, gaps #19–22, family impact table,
  validation, deferred-gaps section).
- Updated count references in `workflow-criticality-classification.md`, `workflow-dependency-map.md`,
  `workflow-system-touchpoint-map.md`, and `requirement-workflow-matrix.md` (new VS are unclassified
  and will be tier-assigned in a follow-up criticality review, consistent with prior passes).
- `07-methodology/validate-repo.sh` passes with 0 errors.

---

## 2026-06-14 — Workflow Gap Analysis (Pass 4): Add VS-101–VS-104 (96 workflows W3281–W3376)

A fourth workflow **gap-analysis** pass was performed against the model company's operations
(BuildRight Depot Corp. — Philippine hardware/DIY/home-improvement big-box retailer). As with
Pass 3, Pass 4 targeted capabilities that had been **overlooked because each was conflated with an
adjacent, already-covered value stream**. Each of the four candidate gaps was validated to have
**zero** dedicated workflow headers in the existing PA files before being added. The four new value
streams deliberately strengthen the three thinnest operating families (People +2; Plan & Source +1;
Governance & Assurance +1). Methodology and results are documented in
[`01-model-company/workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md).

### Added — 4 new value streams, 12 process areas, 96 workflows

| VS | Value Stream | Family | W-range |
|---|---|---|---|
| **VS-101** | Merchandise Financial Planning, OTB & Margin Management | Plan & Source | W3281–W3304 |
| **VS-102** | Compensation, Benefits & Total Rewards Strategy | People | W3305–W3328 |
| **VS-103** | HR Shared Services, Employee Experience & People Analytics | People | W3329–W3352 |
| **VS-104** | Government Affairs, Public Policy & Industry Relations | Governance & Assurance | W3353–W3376 |

Each value stream comprises a README plus three process-area files (8 workflows each), all fully
specified (trigger, frequency, volume, owner, participants, steps with RACI, system touchpoints,
pain points, time estimates) and cross-referenced to adjacent value streams.

### Rationale (gaps filled — each previously conflated with a covered capability)

- **VS-101 Merchandise Financial Planning, OTB & Margin Management** — the merchandise-finance
  discipline (seasonal merchandise plan, open-to-buy, markdown budget, IMU/maintained-margin
  modeling, turn/GMROI/WOS planning, in-season reforecast, merchandise P&A) was conflated with
  assortment (VS-01), supply operations (VS-02), corporate budgeting (VS-33.1), and finance FP&A
  (VS-17.4) — none of which own the open-to-buy and margin-governance layer that protects a
  ~PHP 42–45B COGS / 28–32% gross-margin business.
- **VS-102 Compensation, Benefits & Total Rewards Strategy** — pay/benefits design was conflated
  with payroll processing (VS-19.2, which only executes pay runs, statutory remittance, 13th-month,
  and final pay). Job architecture, salary structure, market benchmarking, pay equity, benefits/HMO
  design, retirement, and STI/LTI plan design had no owner.
- **VS-103 HR Shared Services, Employee Experience & People Analytics** — the HR service-delivery
  layer was conflated with the employee lifecycle (VS-19) and labor relations (VS-84). The employee
  service center, ESS/MSS, multi-entity shared services, EX/engagement, DEI, workforce planning,
  people analytics, and HRIS administration had no dedicated owner.
- **VS-104 Government Affairs, Public Policy & Industry Relations** — proactive national corporate
  external affairs was conflated with local/LGU permitting (VS-76), regulatory permit execution
  (VS-22), labor-specific advocacy (VS-84.3), PR/crisis comms (VS-14.3), and litigation (VS-100).
  National stakeholder relations, legislative/regulatory monitoring, advocacy, coalition building,
  association leadership, public affairs, and political/regulatory risk had no owner.

### Repository impact

- Grand total: **3,132 → 3,228** workflows (+96)
- Value streams: **96 → 100** (+4); Process areas: **292 → 304** (+12)
- The 96 new workflows are **unclassified** (unclassified count: 1,965 → 2,061) and will be
  tier-assigned in a follow-up criticality review, exactly as the Pass 1–3 batches were.
- All cross-reference documents reconciled (root README, executive summary, value-stream-index,
  workflows/README, criticality classification, dependency map, touchpoint map).
- `07-methodology/validate-repo.sh` passes with 0 errors.

---

## 2026-06-14 — Workflow Gap Analysis (Pass 3): Add VS-97–VS-100 (96 workflows W3185–W3280)

A third workflow **gap-analysis** pass was performed against the model company's operations
(BuildRight Depot Corp. — Philippine hardware/DIY/home-improvement big-box retailer). Whereas
Passes 1 and 2 (VS-89–VS-96) filled retired-number gaps and added ecommerce/marketplace/leasing
capabilities, Pass 3 deliberately targeted capabilities that had been **overlooked because each
was conflated with an adjacent, already-covered value stream**. The four new value streams were
distributed across the four previously-thinnest operating families. Methodology and results are
documented in
[`01-model-company/workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md).

### Added — 4 new value streams, 12 process areas, 96 workflows

| VS | Value Stream | Family | W-range |
|---|---|---|---|
| **VS-97** | Corporate Real Estate & Property Portfolio Management | Asset & Infrastructure | W3185–W3208 |
| **VS-98** | Contingent, Contract & Outsourced Workforce Management | People | W3209–W3232 |
| **VS-99** | IT Asset & Technology Lifecycle Management | Technology & Data | W3233–W3256 |
| **VS-100** | Legal Operations, Litigation & IP Management | Governance & Assurance | W3257–W3280 |

Each value stream comprises a README plus three process-area files (8 workflows each), all fully
specified (trigger, frequency, volume, owner, participants, steps with RACI, system touchpoints,
pain points, time estimates) and cross-referenced to adjacent value streams.

### Rationale (gaps filled — each previously conflated with a covered capability)

- **VS-97 Corporate Real Estate & Property Portfolio Management** — BuildRight Property
  Management, Inc. (one of the 5 named legal entities, profile §2) is a real-estate
  owner/lessor/developer. VS-20 (site selection) and VS-42 (lease administration) cover
  BuildRight **as tenant**; VS-35 covers fixed-asset accounting. The **lessor / property-owner /
  investor** operating model — acquisition underwriting, PFRS 40 investment-property fair-value,
  landlord leasing & CAM recovery, real property tax as owner, portfolio NOI/yield — was entirely
  uncovered.
- **VS-98 Contingent, Contract & Outsourced Workforce Management** — ~10–20% of store/DC labor
  is non-employee (outsourced security, janitorial, promodizers, construction/agency labor). VS-19
  covers BuildRight's own employees (incl. directly-hired seasonal W555); VS-34 covers commercial
  service contracts at the PO/invoice level. The **contingent-workforce program** — DOLE D.O. 174
  labor-only-contracting compliance, four-fold-test worker classification, contractor onboarding /
  access / permit-to-work, time-vs-invoice reconciliation, co-employment risk — had no dedicated
  owner.
- **VS-99 IT Asset & Technology Lifecycle Management** — 600 POS terminals + RF guns + mobile +
  network + servers + the full software/SaaS estate across 205+ locations. VS-35 is fixed-asset
  **accounting**; VS-27 is IT **operations / service desk**. The **ITAM discipline** — hardware /
  software discovery & CMDB, software asset management & license optimization, SaaS portfolio &
  FinOps, technology refresh, secure retirement with data sanitization (RA 10173 / DENR e-waste) —
  was uncovered.
- **VS-100 Legal Operations, Litigation & IP Management** — active legal matters and outside
  counsel across the 5-entity group; commercial, labor (NLRC), consumer/DTI, property, tax (BIR),
  customs, and IP exposure; the board receives periodic litigation updates (per VS-36.1). VS-36
  (governance), VS-22 (compliance), and VS-88 (records / legal-hold execution) covered adjacent
  areas but not the **litigator work** — matter/case management, litigation lifecycle, outside
  counsel, IP portfolio prosecution & enforcement, settlement/loss-contingency.

### Counts reconciled

| Metric | Before | After |
|---|---|---|
| Value streams | 92 | **96** |
| Process areas | 280 | **292** |
| Workflows | 3,036 | **3,132** |
| Unclassified | 1,869 | **1,965** (+96, pending criticality review) |

All cross-document counts (README, executive-summary, value-stream-index, workflows/README,
criticality classification, dependency map, touchpoint map) reconciled; `07-methodology/validate-repo.sh`
passes with **0 errors**. The 96 new workflows remain unclassified (consistent with how Pass 1 and
Pass 2 batches were handled) and will be tier-assigned in a follow-up criticality review.

---

## 2026-06-14 — Workflow Gap Analysis (Pass 2): Add VS-93–VS-96 (96 workflows W3089–W3184)

A second workflow **gap-analysis** pass was performed against the model company's operations
(BuildRight Depot Corp. — Philippine hardware/DIY/home-improvement big-box retailer). The pass
filled the two remaining retired-number gaps (former VS-49 and VS-52) and added two further new
value streams identified by the analysis. Methodology and results are documented in
[`01-model-company/workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md)
(Pass 1 = VS-89–VS-92; Pass 2 = VS-93–VS-96).

### Added — 4 new value streams, 12 process areas, 96 workflows

| VS | Value Stream | Family | W-range |
|---|---|---|---|
| **VS-93** | Dark Store & Micro-Fulfillment Operations | Make & Move | W3089–W3112 |
| **VS-94** | Cooperative & Community Enterprise Procurement | Plan & Source | W3113–W3136 |
| **VS-95** | Marketplace Operator & Third-Party Seller Management | Sell & Serve | W3137–W3160 |
| **VS-96** | Equipment Leasing & Capital Equipment Finance | Finance | W3161–W3184 |

Each value stream comprises a README plus three process-area files (8 workflows each), all fully
specified (trigger, frequency, volume, owner, participants, steps with RACI, system touchpoints,
pain points, time estimates) and cross-referenced to adjacent value streams.

### Rationale (gaps filled)

- **VS-93 Dark Store & Micro-Fulfillment** — fills the retired-VS-49 gap. Ecommerce is growing
  from ~3% to ~7% of revenue (~42,900 orders/month scaling toward ~100K); dense Metro
  Manila/Cebu/Davao markets need dedicated pick/pack/dispatch nodes distinct from full DCs
  (VS-04) and ship-from-store (VS-10 PA-10.2).
- **VS-94 Cooperative & Community Enterprise Procurement** — fills the retired-VS-52 gap. Buy-
  side counterpart to VS-82 (Sari-Sari/MSME sell-side). Covers CDA-registered cooperatives,
  social enterprises, livelihood programs (DSWD-SLP, DOLE, DTI-BMED), and indigenous-community
  sourcing under IPRA — distinct from mainstream vendor onboarding (VS-03) by virtue of
  fair-trade pricing, capacity-building, advance-financing, and impact-reporting duty.
- **VS-95 Marketplace Operator & Third-Party Seller Management** — **new gap**. BuildRight as
  **operator** of its own 3P marketplace (buildright.com.ph / app), where vetted sellers list
  specialty SKUs alongside BuildRight's 1P catalog. Distinct from VS-48 retail media
  (advertising), VS-65 (BuildRight selling on Lazada/Shopee), and VS-10 (1P fulfillment).
- **VS-96 Equipment Leasing & Capital Equipment Finance** — **new gap**. B2B lease / lease-to-
  own / capital-equipment finance for trade, project, corporate, and government customers
  acquiring expensive equipment (generators, scaffolding, solar/storage — links to VS-70, HVAC,
  MHE) over multi-year terms. Distinct from VS-12 short-term tool rental and VS-38 consumer
  credit.

### Candidate gaps considered but rejected (adequate coverage)

- Energy/Utilities Management — covered (VS-25 W692/W1543, VS-20 W701/W1563).
- B2B PunchOut/cXML — covered (VS-10 W1242, VS-11 W283).
- Customer Trade-In/Refurbishment — covered (VS-09 W916, VS-05 disposition).
- Ocean Freight/Demurrage — covered (VS-02 W144/W249, VS-87).
- Lumber Yard Operations — covered (VS-07 PA-07.1 incl. W1276).
- Typhoon Emergency Merchandise/Price-Freeze Compliance — covered (VS-02 W927/W1187.7, VS-07,
  VS-69).
- Concessionaire/Sublease Management — covered (VS-07 W177).
- Workers' Compensation/ECC — covered (VS-24 W805, VS-83 W2853).
- Self-Checkout/Scan-and-Go — covered (VS-08 W281/W516/W538).
- Pallet/RTI Pool Management — covered (VS-04 W270 + RTP reconciliation).
- Treasury FX Hedging — covered (VS-18 PA-18.3 incl. W1473).

### Reconciled counts (repository-wide)

| Metric | Before (after Pass 1) | After (Pass 2) |
|---|---|---|
| Value streams | 88 | **92** |
| Process areas | 268 | **280** |
| Workflows | 2,940 | **3,036** |
| Plan & Source subtotal | 284 | 308 |
| Make & Move subtotal | 283 | 307 |
| Sell & Serve subtotal | 1,074 | 1,098 |
| Finance subtotal | 387 | 411 |
| Unclassified workflows | 1,773 | 1,869 |
| Classified workflows | 1,167 | 1,167 (unchanged) |

Files updated (summary table, family tables, footer notes, or grand totals):
- `README.md` — folder tree (4 new VS dirs), Key Metrics, Coverage & Known Gaps, totals.
- `01-model-company/executive-summary.md` — totals line.
- `01-model-company/workflows/README.md` — Quick Stats, family tables, subtotal reconciliation,
  retired-VS note.
- `01-model-company/workflows/value-stream-index.md` — header banner, summary table, family
  tables/subtotals, grand total, detailed VS sections, decision tree, totals footer.
- `01-model-company/workflows/workflow-criticality-classification.md` — disclaimer, footer (v7.4).
- `01-model-company/workflows/workflow-dependency-map.md` — header note and footer (v2.5).
- `01-model-company/workflows/workflow-system-touchpoint-map.md` — footer (v56.0).
- `01-model-company/requirement-workflow-matrix.md` — Coverage Validation and footer (v51).
- `01-model-company/workflows/workflow-gap-analysis.md` — methodology, gaps-identified table,
  Pass 1/Pass 2 value-stream table, family subtotal impact, validation, remaining-gaps section.

### Validation result
`validate-repo.sh` passes with **0 errors**. Grand total (3,036) matches actual PA workflow
header count (3,036); all 1,167 classified IDs resolve; no dangling references; no placeholder
content. The 96 new workflows are unclassified (counted in the 1,869 unclassified total) pending
a follow-up criticality pass. All four retired VS numbers (49, 50, 51, 52) now have
fully-detailed successor value streams (VS-90/VS-92 from Pass 1; VS-93/VS-94 from Pass 2); no
retired-number gaps remain.

---

## 2026-06-14 — Workflow Gap Analysis: Add VS-89–VS-92 (96 workflows W2993–W3088)

A workflow **gap analysis** was performed against the model company's operations
(BuildRight Depot Corp. — Philippine hardware/DIY/home-improvement big-box retailer) to confirm
the operational workflow inventory comprehensively covers its business, and to fill capability
gaps. Methodology and results are documented in the new
[`01-model-company/workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md).

### Added — 4 new value streams, 12 process areas, 96 workflows

| VS | Value Stream | Family | W-range |
|---|---|---|---|
| **VS-89** | Product Recall & Safety Corrective Action Management | Governance & Assurance | W2993–W3016 |
| **VS-90** | Damage, Claims & Freight Recovery Management | Make & Move | W3017–W3040 |
| **VS-91** | Consumer Data Privacy & Data Protection Program | Governance & Assurance | W3041–W3064 |
| **VS-92** | Kitting, Bundling & Build-to-Order Assembly Operations | Make & Move | W3065–W3088 |

Each value stream comprises a README plus three process-area files (8 workflows each), all fully
specified (trigger, frequency, volume, owner, participants, steps with RACI, system touchpoints,
pain points, time estimates) and cross-referenced to adjacent value streams.

### Rationale (gaps filled)

- **VS-89 Product Recall** — only the store-level customer-notification execution step (W776)
  existed; the end-to-end recall program (hazard intake, risk assessment, DTI-BPS/FDA notification,
  retrieval, vendor reimbursement, destruction, CAPA, post-recall surveillance) was missing.
  Consumer Act (RA 7394) + DTI-BPS mandate recall procedures.
- **VS-90 Damage & Claims** — fills the retired-VS-50 gap. Systematic damage identification/
  disposition, vendor/carrier/freight claim filing & settlement, customer damage-claim handling,
  subrogation/insurance recovery, and enterprise damage cost analytics.
- **VS-91 Consumer Data Privacy** — employee data privacy existed (W647); the consumer program
  (consent/preference, DSAR fulfillment, PIA/DPIA, vendor privacy due diligence, DPA 72-hour
  breach NPC notification) was missing. ~600K loyalty members + ~515K ecommerce orders/yr.
- **VS-92 Kitting & Bundling** — fills the retired-VS-51 gap (distinct from VS-09 custom
  fabrication). Kit/Bundle is an explicit item type (profile §6.4); covers BOM, centralized &
  store-level build, tear-down/component recovery, bundle pricing/promotion analytics.

### Considered but not added

- Workforce Management — already covered (PA-19.3 in VS-19, 10 workflows).
- Facilities/Equipment Maintenance — substantially covered (VS-20 PA-20.3 + VS-07 PA-07.2).
- Dark Store & Micro-Fulfillment (former VS-49) and Cooperative/Community Procurement (former
  VS-52) — **deferred** (lower near-term priority); VS-49–VS-52 numbers remain retired.

### Reconciled counts (repository-wide)

| Metric | Before | After |
|---|---|---|
| Value streams | 84 | **88** |
| Process areas | 256 | **268** |
| Workflows | 2,844 | **2,940** |
| Make & Move subtotal | 235 | 283 |
| Governance & Assurance subtotal | 480 | 528 |
| Unclassified workflows | 1,677 | 1,773 |
| Classified workflows | 1,167 | 1,167 (unchanged) |

Files updated (summary table, family tables, footer notes, or grand totals):
- `README.md` — folder tree (4 new VS dirs), Key Metrics, Coverage & Known Gaps, Document
  Relationships diagram, totals.
- `01-model-company/executive-summary.md` — totals line.
- `01-model-company/workflows/README.md` — Quick Stats, family tables, subtotal reconciliation,
  retired-VS note, navigation.
- `01-model-company/workflows/value-stream-index.md` — header banner, summary table, family
  tables/subtotals, grand total, detailed VS sections, decision tree, totals footer.
- `01-model-company/workflows/workflow-criticality-classification.md` — disclaimer, summary
  table, addition note, footer (v7.3).
- `01-model-company/workflows/workflow-dependency-map.md` — header note and footer (v2.4).
- `01-model-company/workflows/workflow-system-touchpoint-map.md` — footer (v55.0).
- `01-model-company/requirement-workflow-matrix.md` — Coverage Validation and footer (v50).
- `01-model-company/workflows/workflow-gap-analysis.md` — **new** methodology & results document.

### Validation result
`validate-repo.sh` passes with **0 errors**. Grand total (2,940) matches actual PA workflow
header count (2,940); all classified IDs resolve; no dangling references; no placeholder content.
The 96 new workflows are unclassified (counted in the 1,773 unclassified total) pending a
follow-up criticality pass.

---

## 2026-06-14 — Consistency Review: Decision Tree, Matrix Counts & Validator Accuracy

A full-repository consistency review (all 84 value streams, 256 process areas, 2,844
workflows) reconciled every cross-document count. The grand totals (2,844 workflows /
84 value streams / 256 process areas / 733 requirements / 67 controls / 1,167 classified)
were already correct and consistent across `README.md`, `executive-summary.md`, both
workflow indexes, the dependency/touchpoint maps, and the criticality classification.
Four residual defects were found and fixed:

### Fixed
- **`01-model-company/workflows/value-stream-index.md`** — the "Decision Tree: Where
  Does a New Workflow Go?" block still listed the **retired** VS-49 (Sell & Serve),
  VS-49–VS-50 (Make & Move), and VS-52 (Plan & Source) alongside the live value streams.
  These references contradicted the 2026-06-14 retirement of VS-49/50/51/52 and the
  coverage note at the top of the same file. Removed; the surviving VS lists now match
  the authoritative family tables exactly.
- **`01-model-company/requirement-workflow-matrix.md`** — the Coverage Validation section
  and footer still reported the pre-retirement figures **"2,700 workflows across 78 value
  streams"** (should be 2,844 / 84). Updated both; footer bumped to v49.
- **`01-model-company/workflows/WORKFLOW-FORMAT-GUIDE.md`** — the Workflow ID format was
  documented as `(W-XX)`, but no workflow ID in the repository uses a dash (actual IDs
  are `W7`, `W5B`, `W9A`, …). Corrected to `(W-number, e.g. W7, W5B)`.
- **`01-model-company/workflows/workflow-criticality-classification.md`** — the footer
  stated **"14 classified references are parent/summary workflows"** that appear as `###`
  sub-headings; the actual count is **22**. Corrected.

### Hardened — `07-methodology/validate-repo.sh`
- **Check 1** (unclassified workflows) rewritten to report the **documented** unclassified
  total (`grand_total − classified` = 1,677) used by every repo document, instead of the
  `##`-header-minus-classified figure (1,699) that double-counted the 22 `###` parent/
  summary workflows. It now also verifies that **every classified workflow ID resolves to
  a real `##`/`###` header** in a PA file, catching stale classification references, and
  prints the count of `###` parent/summary workflows for transparency.
- **Check 4** (requirement ↔ matrix consistency) now extracts requirement IDs from
  **table rows only** (`^| REQ-XX |`) instead of any `[A-Z]+-\d+` token. This eliminates
  false positives such as day-offset tokens (`T-7`, `T-14`) and the `VS-49` token inside
  the retirement footnote, so the check now reports the accurate **733** (matrix) = **733**
  (defined) instead of 740.

### Validation result
`validate-repo.sh` passes with **0 errors** and a single informational warning
("1,677 workflows remain unclassified") that reflects the documented pending-review total.

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

---

## 2026-06-15 — Workflow review implementation (3/5): roll up VS-79–VS-128 into the cross-reference maps (P3)

Third commit. Both rollup maps ended with "will be incorporated during the next classification
pass", so the strategically-central, cross-cutting programs added in gap-analysis passes 2–10
were not wired into the dependency graph or the ERP-module matrix. The raw cross-reference data
already existed inline in each PA file; this commit rolls it up:

- **`workflow-dependency-map.md` → new §8 "Cross-Cutting Program Dependencies (VS-79–VS-128)"**, mined by `grep` over every `links to VS-NN` / `VS-NN` reference in VS-79–VS-128 PA files. §8.1 lists the anchor foundational value streams the gap-analysis programs hook into (VS-17 R2R, VS-21 Audit, VS-27 IT, VS-28 Analytics, VS-19 HR …); §8.2 captures the cross-cutting **Tier-1 statutory** programs (VS-79/85/89/91/114/117/118/125) and where they sit relative to the core compliance chain; §8.3 captures the **Tier-2/3 platform/governance overlays** (CDP, S&OP/IBP, AI Governance, Calibration, EA, SCF, Freight, PMO) and their consumers; §8.4 lists the strongest declared per-program anchor edges. Confirms the key sequencing insight: the gap-analysis programs are largely Tier-2/3 overlays *on top of* the Tier-1 core, with the statutory exceptions in §8.2.
- **`workflow-system-touchpoint-map.md` → new "Gap-Analysis Value Streams (VS-79–VS-128) — Primary ERP Module Coverage"** section: a curated VS → primary-module mapping for all 50 gap-analysis value streams (per-workflow module/object detail remains in each PA file). Deliberately a summary table rather than appending ~1,200 more IDs to the already-dense per-module rows (which would be unreadable).
- Both version footers rewritten to drop the stale "will be incorporated … next pass" caveat.

Validator: 0 errors / 2 warnings; no dangling references in either map.

---


---

## 2026-06-15 — Workflow review implementation (4/5): boilerplate rework reference (P1) + Automation/Controls standardization (P6/P7) + README refresh (P5)

Fourth commit. The largest recommendation (P1: rework 552 boilerplate workflows across 23 Expansion-block value streams) is multi-session work; this commit establishes the **gold-standard reference** and formalizes the two missing fields, so the remaining 22 VSs follow a concrete template:

- **VS-73 (Store-Level Waste Management & Circular Economy) fully reworked** — all 24 workflows (W2598–W2621) rewritten: generic boilerplate `System Touchpoints` / `Pain Points / Risks` / `Time Estimate` replaced with workflow-specific content (named ERP modules/objects, named risks with named mitigations, scaled time math), and **Automation Opportunity** + **Controls** fields added to every workflow (24 of each). Selected because it was cited as the bad-example in the review and carries the highest regulatory exposure (DENR DAO 2013-22, RA 6969, BFP Fire Code). `validate-repo.sh` Check 10 drops 552→528 workflows / 23→22 VSs.
- **`WORKFLOW-FORMAT-GUIDE.md`** — Automation Opportunity + Controls promoted from "recommended" to **Standard analysis fields** for any fully-detailed workflow (P6: Controls was in only 5/376 files; P7: Automation Opportunity in 0/376). Quality-bar good/bad examples added for both. Cross-references split into its own subsection.
- **New `validate-repo.sh` Check 12** — tracks Automation Opportunity + Controls field adoption across all PA files (now 24/3,804 = 1% baseline from VS-73), measuring rework progress toward 100% on fully-detailed workflows. Backs the format-guide "Check 12" reference.
- **VS-73 README** rewritten to the richer standard (purpose, why-it-matters, owner/participants, dependencies, controls, rework status) — the reference for the other 47 original Core-block README refreshes (P5).

**Remaining work (tracked, not blocking):** rework the other 22 Expansion-block VSs to the VS-73 standard (528 workflows); add Automation/Controls to the 101 fully-detailed Core/Statutory/Gap-analysis VSs; refresh the 47 remaining Core-block READMEs. Validator: 0 errors / 3 warnings.

---


---

## 2026-06-15 — Workflow review implementation (5/5): Core-block README refresh (P5)

Fifth/final commit of the review-implementation program. The original Core-block value streams
(VS-01–VS-20) had 16–18-line stub READMEs (overview sentence + PA table only). Refreshed all 20
to the richer standard demonstrated by VS-73 and the gap-analysis VSs — each now carries
**Overview · Why it matters · Owner & participants · Process Areas · Key dependencies · Key
controls**, so the most-visited value streams orient a reader without requiring a dive into PA
files. PA tables and workflow counts preserved exactly (validator Check 2 confirms).

**Remaining P5 work (tracked, not blocking):** refresh the remaining 27 original Core-block
READMEs (VS-21–VS-48) to the same standard.

---

## Summary of the five-commit review-implementation program

| # | Recommendation | Status |
|---|---|---|
| P4 | Structural fixes (W54A classified, deepest-chain count, Block column, reverse validator check) | ✅ Done |
| P2 | Classification pass for the 2,659 unclassified workflows | ✅ Done (keyword-driven proposal file; 0 workflows now without a proposed tier) |
| P3 | Roll VS-79–VS-128 into the dependency & touchpoint maps | ✅ Done (dependency-map §8; touchpoint-map module summary) |
| P1 | Rework the 552 boilerplate workflows | ◑ Reference done (VS-73, 24 wf); 22 VSs / 528 wf follow the pattern |
| P6 | Wire internal-controls (CTL-IDs) into workflows | ◑ Standardized + demonstrated (VS-73); rollout pending |
| P7 | Add the missing Automation Opportunity field | ◑ Standardized + demonstrated (VS-73); rollout pending |
| P5 | Refresh the stub VS READMEs | ◑ VS-73 + VS-01–VS-20 done; VS-21–VS-48 follow |

Validator: **0 errors / 3 warnings** (boilerplate-remaining, unclassified-in-confirmed,
field-adoption — all three now explicitly tracked and decreasing toward zero).

---

