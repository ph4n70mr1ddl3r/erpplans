# Changelog

> Track major changes to the BuildRight Depot ERP Plans repository.

---

## 2026-06-09 — Post-Review Cleanup

### Fixed
- **Added WHL-001, WHL-002, WHL-003** to `erp-requirements.md` — these DC/warehouse management requirements were referenced in the requirement-workflow matrix but had no formal requirement definition. Now formalized under R4 (Warehouse Management) with Must Have / Should Have priorities.
- **Removed dead link** to `_archive-domains/` in `value-stream-index.md` — the archive directory was deleted in a prior commit but the reference remained.
- **Reconciled workflow counts** — removed 4 duplicate classification entries (W1163, W1164, W1165, W1166 appeared in two tier sections) from `workflow-criticality-classification.md`. Corrected title from 1,147 → 1,167. Updated summary totals (Tier 1: 439, Tier 2: 499, Tier 3: 226 = 1,167 classified).
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
