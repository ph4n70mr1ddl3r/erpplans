# 07 — Technical Methodology & Guidelines

> This folder contains technical implementation guidelines and reference specifications
> for the BuildRight Depot Corp. ERP system. It is intentionally minimal at this stage;
> detailed methodology documents (implementation approach, testing strategy, change management)
> will be added during platform selection and implementation planning.

## Contents

| Document | Description |
|---|---|
| [technical-guidelines.md](technical-guidelines.md) | POS hardware specs, infrastructure & deployment reference, integration architecture (reference copy; canonical diagram lives in `01-model-company/data-volumes-and-integrations.md`), security requirements |
| [validate-repo.sh](validate-repo.sh) | Cross-reference validation script — 25 checks covering workflow counts, requirement/control IDs, classification register, dangling workflow references, markdown table structure, analysis-field-header canonicalization, PA-footer format, orphan-workflow-body (ghost) detection, criticality-classification prose-count vs heading consistency, boilerplate/tier-1 chain consistency, value-stream-index PA/VS link resolution, PA-file relative-link resolution, Automation/Controls draft-field content quality, required-field (9-field) completeness, intra-file TOC anchor resolution, workflows/README.md family reconciliation + stale canonical-figure guard, criticality proposed-register mirror reconciliation + stale unclassified-figure guard, and touchpoint-map self-declared reconciliation guard |
| [classify-workflows.py](classify-workflows.py) | Keyword-driven criticality classifier — regenerates `01-model-company/workflows/workflow-criticality-proposed.md` (Tier 1/2/3 proposal for every workflow not in the hand-confirmed register) |
| [backfill-controls.py](backfill-controls.py) | `### Controls` blank-line normalizer + CTL-XX backfiller — reverses `internal-controls-matrix.md` into a workflow→control map and injects real CTL-XX references into Controls sections that lack them; also restores the missing blank line before the next `###` header |
| [add-automation-controls.py](add-automation-controls.py) | Automation/Controls field generator — inserts workflow-specific Automation Opportunity and Controls sections derived from steps/touchpoints. Now CTL-map-aware and emits complete sentences (draft quality, refined per-workflow); companion to `backfill-controls.py` for retroactive CTL backfill |
| [defragment-automation.py](defragment-automation.py) | One-time repair of legacy mid-phrase fragment Automation bullets — regenerates any section containing a generator-fragment bullet into complete `- System {action} of "{step}" (replaces manual Step N).` sentences. Idempotent; verified to destroy no hand-written content |
| [backfill-time-estimate.py](backfill-time-estimate.py) | Mechanically derives the `### Time Estimate` section where absent — parses each workflow's per-step Durations into a draft roll-up, explicitly labelled as pending human annualization. Honest-draft principle (values come from authored steps; no fabricated throughput math) |
| [fix-headcount-6757.py](fix-headcount-6757.py) | Stale total-headcount figure repairer — propagates the 2026-06-25 headcount change (`6,757 → 6,762`) into the workflow catalog body, skipping legitimate historical `X → Y` change-notes and `workflow-gap-analysis.md`; companion to validator Check 24 (Part B) |
| [fix-toc-anchors.py](fix-toc-anchors.py) | Intra-file TOC anchor repairer — regenerates each PA file's `## Workflows in This Process Area` navigation anchors from the (correct) display text using GitHub's slug rules, fixing the 1,926 malformed anchors (dropped hyphens, stale W-numbers) the gap-analysis generator left across 271 PA files. Idempotent; companion to validator Check 23 |

## Future Additions (Post-Platform Selection)

The following documents are out of scope for the current planning phase and will be developed
during implementation:

- **Implementation approach & phasing** — Wave/go-live strategy aligned with Tier 1/2/3 criticality
- **Testing strategy** — SIT, UAT, integration testing, parallel run approach
- **Change management plan** — Training curriculum, organizational readiness, adoption metrics
- **Data migration runbook** — Detailed cutover plan building on `01-model-company/data-migration-mapping.md`
- **Integration specification** — API contracts, message schemas, error handling per touchpoint
- **Security hardening guide** — Role matrix, SOD rules, penetration testing scope
- **Performance testing plan** — Load targets, batch window validation, peak simulation

---

*Date: 2026-06-19*
