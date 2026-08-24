# Workflow Format Guide

> Describes the standard format, conventions, and role key used across all operational
> workflow domain files in this repository. Enforced (informationally) by
> [`07-methodology/validate-repo.sh`](../../07-methodology/validate-repo.sh).

---

## Purpose of Workflows

The operational workflows serve three purposes:

1. **Validate headcount** — by mapping work volume to roles, we can verify staffing assumptions
2. **Inform ERP design** — each workflow reveals system touchpoints, automation opportunities, and integration needs
3. **Optimize organization** — by exposing handoffs, bottlenecks, and spans of control

For these purposes to hold, the analysis fields (**Pain Points / Risks**, **System Touchpoints**,
**Time Estimate**, and **Automation / Controls** where used) must contain *workflow-specific*
content. Verbatim boilerplate (identical text copied across many workflows) defeats all three
purposes and is flagged by the validator (Check 10).

---

## Standard Workflow Format

Each workflow is a `## W<number>. <Name>` block inside a Process Area (PA) file, with the
following fields.

### Required fields (every workflow)

| Field | Meaning |
|---|---|
| **Trigger** | What initiates the workflow |
| **Frequency** | How often it occurs |
| **Volume** | How many instances per occurrence, with the ×-math that scales it to the enterprise |
| **Owner** | Role accountable for the outcome (the single throat-to-choke) |
| **Participants** | All other roles involved |
| **Steps** | Sequential activities in a table with Responsible (R) and Accountable (A) columns and a per-step Duration |
| **System Touchpoints** | Where ERP/system support is needed — name the *specific* module/object/integration (e.g. "Goods receipt exception; damage quarantine bin"), not a generic pointer |
| **Time Estimate** | Estimated effort per occurrence, rolled up to an annual or per-store figure where it drives headcount |
| **Pain Points / Risks** | What can go wrong, named specifically (e.g. "**Evidence risk**: damage not documented at receipt forfeits claim rights"), with the mitigating control |

> **Completeness note (2026-06-27).** All 5,349 workflows now carry all 9 required fields (validator Check 22 green). The last 645 missing instances were closed as follows: the 224 missing **Participants** rows (VS-53–VS-63 plus VS-86/87/99/189) were mechanically derived from each workflow's own Steps-table roles via [`07-methodology/backfill-participants.py`](../../07-methodology/backfill-participants.py) (honest-draft: values come from authored steps; no invented roles); the 175 missing **System Touchpoints** and 246 missing **Pain Points / Risks** sections (VS-15–18, VS-27, VS-31–40, VS-48) were authored per-workflow, grounded in each workflow's own steps and cross-references. Treat these like any authored field: refine freely during per-workflow review.

### Standard analysis fields (add to every fully-detailed workflow)

These two fields were previously listed as "recommended"; a 2026-06-15 review found **Automation Opportunity absent from all 376 PA files** and **Controls present in only 5**. They are now standard for any fully-detailed workflow (see VS-73 for the reference implementation). As of 2026-06-20 the field **headers** are present on all **5,349 workflows (100% presence)** across all blocks (Core, Expansion, Statutory, and Gap analysis).

> **Content-quality caveat (2026-06-21).** Presence ≠ quality. The repo-wide insertion was performed by a first-pass generator (`add-automation-controls.py`), and a 2026-06-21 review found the bulk of the generated content is **draft** quality: Automation bullets were emitted as mid-phrase fragments (e.g. `- auto-review (account manager reviews application: (a) verify)`) and most Controls sections cited no CTL-XX from the controls register. Two corrections shipped in that review: (1) `backfill-controls.py` retroactively injected real CTL-XX references wherever `internal-controls-matrix.md` provides a workflow→control mapping, and normalized the missing blank line before the next `###` header; (2) validator **Check 21** now reports the live quality metrics (fragment-bullet count, CTL-XX coverage %, pure-boilerplate count) so the backlog is tracked rather than silently claimed as complete. Because the 67-control register was originally authored against the Core workflows (W1–W942), only ~60 workflows had a CTL mapping; the 2026-06-27 register extension (CTL-68–CTL-171, one anchor control per gap-analysis value stream VS-89–VS-192) raised mapped coverage via `backfill-controls.py`, and the 2026-06-28 process-area operating controls (CTL-240–CTL-808, `add-pa-controls.py`) closed CTL-XX citation to 100% of workflows — every Controls section now cites at least one register control (PA controls are honest-draft derived mappings pending per-workflow review). Treat any generated Automation/Controls bullet not matching the quality bar below as a draft pending per-workflow human refinement.

| Field | Meaning |
|---|---|
| **Automation Opportunity** | Steps that are manual today but are candidates for system automation — directly informs ERP design (purpose 2) |
| **Controls** | Internal-control IDs (from [`internal-controls-matrix.md`](../internal-controls-matrix.md)) exercised by this workflow — closes the loop with the 808-control register |

### Cross-reference field

| Field | Meaning |
|---|---|
| **Cross-references** | Links to related workflows in other value streams (e.g. "links to VS-04", "per W533") using the `VS-NN` and `W<number>` identifiers |

### Quality bar for the analysis fields

The fields that deliver the workflow's value are **System Touchpoints**, **Time Estimate**, and
**Pain Points / Risks**. Each must be specific to the workflow:

- ❌ `System Touchpoints: ERP integration point (W2599)` — generic, adds no information
- ✅ `System Touchpoints: Damage-case module with evidence attachments; image repository (links to VS-88)`
- ❌ `Pain Points: **Execution risk**: Operational variability mitigated by standard procedures and system controls` — generic boilerplate
- ✅ `Pain Points: **Evidence risk**: damage not documented at receipt forfeits claim rights; mitigated by mandatory photo + discrepancy capture at goods receipt`
- ❌ `Time Estimate: 30–120 min per occurrence` — generic range with no scaling math
- ✅ `Time Estimate: 5–15 min per discrepancy; ~72,000 receipts/yr → ~6,000 discrepancies/yr`
- ❌ `Automation Opportunity: Automate manual steps` — vacuous
- ✅ `Automation Opportunity: Weigh-scale → ERP auto-posting (eliminates hand-keyed volumes); mobile damage-flag → disposition-suggestion`
- ❌ `Controls: Standard controls apply` — vacuous
- ✅ `Controls: CTL-06 (DENR-certified vendor onboarding); CTL-44 (duplicate-invoice guard); operational: manifest-vs-invoice match before payment`

---

## Role Key (Responsible / Accountable)

The per-step **Steps** table uses two columns:

| Column | Meaning |
|---|---|
| **Role (R)** — Responsible | Does the work |
| **Role (A)** — Accountable | Owns the outcome (exactly one per step) |

Full **RACI** (adding **C**onsulted and **I**nformed) is **not** enumerated as per-step columns —
in practice it crowds the table and almost every step ends up R/A only. Instead:

- **Consulted** and **Informed** parties are captured in the workflow-level **Participants** field and in the narrative, and are called out explicitly only on the specific step where a consultation or notification handoff is material.
- Where a step genuinely needs a separate authorizer (e.g. a manager swipe for an override), that role is named in the step's **Role (A)** column or in the step prose.

This keeps the table readable while preserving accountability on every step.

---

## Naming Conventions

| Pattern | Example | Meaning |
|---|---|---|
| `W<number>` | W7, W2598, W3017 | Primary workflow. New value streams use sequential IDs allocated in blocks (see [`workflow-gap-analysis.md`](workflow-gap-analysis.md)); legacy streams use small numbers (W1–W999) |
| `W<number><letter>` | W5A, W5B, W9A | Sub-workflow or variant of a parent (e.g. W5A Store Opening / W5B In-Store Selling under W5). Mostly used in the original (VS-01–VS-31) streams |
| `W<number>.<step>` | W7.2, W5B.4 | Reference to a specific step within a workflow (used in cross-references and the requirement-workflow matrix) |
| `PA-<VS>.<n>` | PA-07.1, PA-90.2 | Process Area file within a value stream folder |
| `VS-<number>` | VS-07, VS-124 | Value stream. Numbers 49–52 are intentionally retired (see [Value Stream Index](value-stream-index.md)) |

Workflow IDs are unique across the whole repository (not just within a value stream), so a `W`
number never needs a VS prefix.

---

## Repository Layout

```
workflows/
├── README.md                         Navigation hub & quick stats
├── value-stream-index.md              Master index (8 families · 188 VS · 569 PAs)
├── WORKFLOW-FORMAT-GUIDE.md           This file
├── workflow-gap-analysis.md           Gap-analysis methodology & workflow-ID allocation log
├── workflow-criticality-classification.md  Tier 1/2/3 priorities (5,372 confirmed rows = full coverage; workflow-criticality-proposed.md now empty)
├── workflow-criticality-proposed.md      Keyword-driven tier proposal register (currently empty — 0 rows; repopulates if new workflows ship unclassified)
├── workflow-dependency-map.md         Prerequisite relationships, critical path
├── workflow-system-touchpoint-map.md  ERP module-to-workflow cross-reference
└── VS-<NN>-<slug>/
    ├── README.md                      Value-stream summary + PA list
    └── PA-<VS>.<n>-<slug>.md          Process area file containing the workflow blocks
```

---

## Related Documents

| Document | Purpose |
|---|---|
| [value-stream-index.md](value-stream-index.md) | Master index of all value streams and process areas |
| [workflow-criticality-classification.md](workflow-criticality-classification.md) | Tier 1/2/3 priority classification (confirmed) |
| [workflow-criticality-proposed.md](workflow-criticality-proposed.md) | Keyword-driven tier proposal register for unclassified workflows (companion; currently empty — 0 rows — since full coverage on 2026-06-28) |
| [workflow-dependency-map.md](workflow-dependency-map.md) | Prerequisite relationships and critical path |
| [workflow-system-touchpoint-map.md](workflow-system-touchpoint-map.md) | ERP module-to-workflow cross-reference |
| [workflow-gap-analysis.md](workflow-gap-analysis.md) | Gap-analysis methodology and workflow-ID allocation log |
| [../requirement-workflow-matrix.md](../requirement-workflow-matrix.md) | Requirement-to-workflow traceability |
| [../internal-controls-matrix.md](../internal-controls-matrix.md) | 808 internal controls mapped to workflows and requirements |
| [../../07-methodology/validate-repo.sh](../../07-methodology/validate-repo.sh) | Consistency & boilerplate validator |

---

*Date: 2026-06-28 (workflow-criticality-proposed.md descriptions aligned to the register's current state — the Repository Layout diagram row and the Related Documents row now carry the 'currently empty (0 rows)' marker with the repopulation note; same repair in workflows/README.md and the root README tree; validator Check 28 Part B now guards the descriptions. Prior 2026-06-27: required-field completeness achieved — Participants backfilled from Steps roles via `backfill-participants.py`; System Touchpoints + Pain Points authored for VS-15–18/27/31–40/48; Check 22 green across all 5,349 workflows. Prior 2026-06-26: stale proposed-count figure `2,564` → `2,596` corrected in the Repository Layout diagram — drift from the 2026-06-25 PA-127.4 regeneration of `workflow-criticality-proposed.md`. 2026-06-25: VS-127 PA-127.4 added — 8 workflows, W5489–W5496 — specializing the S&OP/IBP consensus cycle for BuildRight's PH-retail context; totals now 5,349 workflows / 188 value streams / 569 process areas. Prior 2026-06-21: Pass 30 added VS-192 Green Fleet Transition — 24 workflows — bringing totals to 5,341 workflows / 188 value streams / 568 process areas; the family-subtotal, grand-total, and criticality-proposed coverage line are reconciled. Prior 2026-06-20: adoption sentence in “Standard analysis fields” corrected to 100% of all 5,317 workflows after reformatting W641–W647. Repository Layout counts reconciled to 188 value streams / 568 process areas / 2,588 proposed; `README.md` (navigation hub) added to the layout diagram so it lists all 8 support files; classified-register reconciliation note aligned with workflow-criticality-classification.md)*
