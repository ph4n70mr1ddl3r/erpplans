# Workflow Format Guide

> Describes the standard format, conventions, and RACI key used across all operational
> workflow domain files in this repository.

---

## Purpose of Workflows

The operational workflows serve three purposes:

1. **Validate headcount** — by mapping work volume to roles, we can verify staffing assumptions
2. **Inform ERP design** — each workflow reveals system touchpoints, automation opportunities, and integration needs
3. **Optimize organization** — by exposing handoffs, bottlenecks, and spans of control

---

## Standard Workflow Format

Each workflow follows this format:

| Field | Meaning |
|---|---|
| **Workflow ID** | Unique identifier (W-XX) |
| **Name** | Process name |
| **Trigger** | What initiates the workflow |
| **Frequency** | How often it occurs |
| **Volume** | How many instances per occurrence |
| **Owner** | Role accountable for the outcome |
| **Participants** | All roles involved |
| **Steps** | Sequential activities with responsible role |
| **System Touchpoints** | Where ERP/system support is needed |
| **Time Estimate** | Estimated effort per occurrence |
| **Pain Points / Risks** | What can go wrong |

---

## RACI Key

| Letter | Role | Meaning |
|---|---|---|
| **R** | Responsible | Does the work |
| **A** | Accountable | Owns the outcome |
| **C** | Consulted | Provides input before/during |
| **I** | Informed | Notified of outcome |

---

## Naming Conventions

| Pattern | Example | Meaning |
|---|---|---|
| `W<number>` | W7 | Primary workflow |
| `W<number><letter>` | W5B, W2A, W9A | Sub-workflow or variant of parent |
| `W<number><letter><letter>` | W12A, W12B | Further variant |
| `W<number>.<step>` | W7.2, W5B.4 | Specific step within a workflow |

---

## Related Documents

| Document | Purpose |
|---|---|
| [README.md](README.md) | Domain file index and complete workflow table |
| [workflow-criticality-classification.md](workflow-criticality-classification.md) | Tier 1/2/3 priority classification |
| [workflow-dependency-map.md](workflow-dependency-map.md) | Prerequisite relationships and critical path |
| [workflow-system-touchpoint-map.md](workflow-system-touchpoint-map.md) | ERP module-to-workflow cross-reference |
| [../requirement-workflow-matrix.md](../requirement-workflow-matrix.md) | Requirement-to-workflow traceability |

---

*Date: 2026-06-09*
