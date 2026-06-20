# 07 — Technical Methodology & Guidelines

> This folder contains technical implementation guidelines and reference specifications
> for the BuildRight Depot Corp. ERP system. It is intentionally minimal at this stage;
> detailed methodology documents (implementation approach, testing strategy, change management)
> will be added during platform selection and implementation planning.

## Contents

| Document | Description |
|---|---|
| [technical-guidelines.md](technical-guidelines.md) | POS hardware specs, infrastructure & deployment reference, integration architecture (reference copy; canonical diagram lives in `01-model-company/data-volumes-and-integrations.md`), security requirements |
| [validate-repo.sh](validate-repo.sh) | Cross-reference validation script — 15 checks covering workflow counts, requirement/control IDs, classification register, dangling workflow references, markdown table structure, analysis-field-header canonicalization, and boilerplate/tier-1 chain consistency |
| [classify-workflows.py](classify-workflows.py) | Keyword-driven criticality classifier — regenerates `01-model-company/workflows/workflow-criticality-proposed.md` (Tier 1/2/3 proposal for every workflow not in the hand-confirmed register) |

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
