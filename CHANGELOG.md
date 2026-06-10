# Changelog

> Track major changes to the BuildRight Depot ERP Plans repository.

---

## 2026-06-10 — Add 10 New Workflows Across 10 Process Areas (Batch 3)

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

## 2026-06-09 — Add 20 New Workflows Across 16 Process Areas
## 2026-06-10 — Add 20 New Workflows Across 19 Process Areas

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
