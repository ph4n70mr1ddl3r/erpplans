# ERP Plans — Model Company & System Architecture

## Purpose

This repository contains the operational specifications, active workflows, and system architecture for **BuildRight Depot Corp.** (the **"Model Company"**), operating with all its capabilities and systems fully enabled under a modern, unified cloud ERP platform. Each subfolder contains the configuration, design, and architecture for running the model company on specific ERP platforms.

## Out of Scope

The following are **not** covered in this repository and would be addressed during ERP platform selection and implementation:

- **Specific ERP vendor evaluation or comparison** — platform-agnostic requirements only
- **Warehouse robotics or automation hardware** — conveyor systems, AS/RS, autonomous mobile robots
- **Blockchain or cryptocurrency** — not applicable to current retail operations
- **IoT sensor networks** — beyond temperature monitoring and GPS telematics already specified
- **Custom mobile app development details** — strategy defined; UX/UI design and code are out of scope
- **Organizational change management plan** — training strategy is referenced but not detailed
- **Implementation project plan** — phase prioritization (Tier 1/2/3) is defined; Gantt charts and resourcing are not
- **Hardware procurement and vendor selection** — reference specifications provided; purchasing is out of scope
- **Network infrastructure detailed design** — bandwidth targets specified; network architecture diagrams are not

See [CHANGELOG.md](CHANGELOG.md) for revision history.

## Folder Structure

```
erpplans/
├── README.md                    ← You are here
├── 01-model-company/            ← Complete model company profile, requirements & workflows
│   ├── model-company-profile.md       Company profile, operations, financials
│   ├── erp-requirements.md            730 requirements across 32+ categories
│   ├── data-volumes-and-integrations.md  Transaction volumes, integration map (canonical integration diagram)
│   ├── workflows/                      1,385 workflows organized by value stream
│   │   ├── value-stream-index.md              Master index (8 families · 30 value streams)
│   │   ├── WORKFLOW-FORMAT-GUIDE.md            Workflow format, RACI key & conventions
│   │   ├── workflow-criticality-classification.md  Phase 1/2/3 implementation priorities
│   │   ├── workflow-dependency-map.md           Prerequisite relationships, critical path
│   │   ├── workflow-system-touchpoint-map.md    ERP module-to-workflow cross-reference
│   │   ├── VS-01-merchandise-strategy/         32 workflows (3 process areas)
│   │   ├── VS-02-supply-planning/               27 workflows (3 process areas)
│   │   ├── VS-03-vendor-management/             74 workflows (4 process areas)
│   │   ├── VS-04-dc-warehouse/                  26 workflows (3 process areas)
│   │   ├── VS-05-inventory-lifecycle/           20 workflows (3 process areas)
│   │   ├── VS-06-logistics-fleet/               15 workflows (3 process areas)
│   │   ├── VS-07-store-operations/              124 workflows (4 process areas)
│   │   ├── VS-08-pos-checkout/                  47 workflows (3 process areas)
│   │   ├── VS-09-in-store-services/             142 workflows (3 process areas)
│   │   ├── VS-10-ecommerce-digital/             39 workflows (3 process areas)
│   │   ├── VS-11-trade-project-wholesale/       37 workflows (3 process areas)
│   │   ├── VS-12-installation-services/         19 workflows (3 process areas)
│   │   ├── VS-13-customer-experience/           51 workflows (3 process areas)
│   │   ├── VS-14-marketing/                     24 workflows (3 process areas)
│   │   ├── VS-15-procure-to-pay/                39 workflows (2 process areas)
│   │   ├── VS-16-order-to-cash/                 23 workflows (3 process areas)
│   │   ├── VS-17-record-to-report/              54 workflows (4 process areas)
│   │   ├── VS-18-treasury-cash/                 22 workflows (3 process areas)
│   │   ├── VS-19-hire-to-retire/                61 workflows (5 process areas)
│   │   ├── VS-20-real-estate-construction/      24 workflows (3 process areas)
│   │   ├── VS-21-internal-audit-risk/           42 workflows (3 process areas)
│   │   ├── VS-22-compliance-regulatory/         49 workflows (3 process areas)
│   │   ├── VS-23-loss-prevention/               12 workflows (3 process areas)
│   │   ├── VS-24-health-safety-environment/     20 workflows (3 process areas)
│   │   ├── VS-25-esg-sustainability/            12 workflows (3 process areas)
│   │   ├── VS-26-business-continuity-insurance/ 18 workflows (3 process areas)
│   │   ├── VS-27-it-operations-security/        57 workflows (3 process areas)
│   │   ├── VS-28-data-analytics-bi/             9 workflows (3 process areas)
│   │   ├── VS-29-master-data/                   41 workflows (3 process areas)
│   │   ├── VS-30-innovation-digital/            13 workflows (3 process areas)

│   ├── executive-summary.md            1-page C-suite overview
│   ├── assumptions-and-design-decisions.md  Consolidated assumptions & rationale
│   ├── requirement-workflow-matrix.md  Cross-reference: requirements ↔ workflows
│   ├── internal-controls-matrix.md     67 internal controls by objective
│   ├── mobile-app-strategy.md          Customer & employee mobile app strategy
│   └── data-migration-mapping.md       Data migration field mapping templates
├── CHANGELOG.md                 ← Revision history
└── 07-methodology/              ← Technical system architecture and guidelines
    ├── README.md                     Methodology index & future document plan
    └── technical-guidelines.md       POS hardware, infrastructure, integration, security
```

## The Model Company at a Glance

| Parameter | Value |
|---|---|
| Company Name | **BuildRight Depot Corp.** |
| Format | Hardware / DIY / Home Improvement Big Box |
| Stores | 200 |
| Distribution Centers | 4 |
| Corporate HQ | Davao City, Philippines |
| POS Machines per Store | 3 |
| Monthly POS Transactions per Store | 14,000 |
| Avg Lines per Transaction | 4 |
| Staff per Store | 29 |
| Active SKUs | 35,000 |
| Monthly Trade Purchase Orders | ~1,200 merchandise; ~1,400–1,600 total |
| Legal Entities | 5 |
| Total Headcount | 6,715 (200 stores × 29 + 600 DC + 315 HQ) |
| Ecommerce | Yes (with BOPIS) |
| Country | Philippines |

## Key Metrics

> **Single source of truth**: Counts below are derived from actual document content. All documents in this repository reference these figures.

| Metric | Value | Source |
|---|---|---|
| Requirements | **730** across 32+ categories | `01-model-company/erp-requirements.md` |
| Workflows (total) | **1,340** across 30 value streams, 91 process areas | `01-model-company/workflows/value-stream-index.md` |
| Workflows (classified by tier) | 1,187 classified (Tier 1: 439, Tier 2: 499, Tier 3: 229) — includes 14 parent/sub-variant grouping references; 1,173 have dedicated `## W` section headers in PA files | `workflows/workflow-criticality-classification.md` |
| Internal Controls | 67 (31 preventive, 36 detective) | `01-model-company/internal-controls-matrix.md` |
| Must Have Requirements | 431 | `01-model-company/erp-requirements.md` |
| Should Have Requirements | 296 | `01-model-company/erp-requirements.md` |
| Nice to Have Requirements | 6 | `01-model-company/erp-requirements.md` |

## Document Relationships

```
                              ┌──────────────────────┐
                              │     README.md        │
                              │  (this file — index) │
                              └──────────┬───────────┘
                                         │
              ┌──────────────────────────┼──────────────────────────┐
              │                          │                          │
   ┌──────────▼──────────┐  ┌───────────▼───────────┐  ┌──────────▼──────────┐
   │  01-model-company/  │  │  07-methodology/      │  │  (future: 02-06/)   │
   │  Business context   │  │  Technical reference  │  │  Platform-specific  │
   └──────────┬──────────┘  └───────────┬───────────┘  └─────────────────────┘
              │                          │
   ┌──────────▼──────────────────────────▼───────────┐
   │              CROSS-REFERENCE LAYER               │
   │                                                   │
   │  erp-requirements.md ←→ workflows/ (1,340 WF)    │
   │       ↕                    ↕                      │
   │  internal-controls-   workflow-criticality-      │
   │  matrix.md (67 CTL)   classification.md          │
   │       ↕                    ↕                      │
   │  requirement-workflow- workflow-dependency-       │
   │  matrix.md              map.md                   │
   │       ↕                    ↕                      │
   │  assumptions-and-      workflow-system-           │
   │  design-decisions.md   touchpoint-map.md          │
   │                          ↕                        │
   │                value-stream-index.md              │
   │              (30 VS · 91 process areas)           │
   └───────────────────────────────────────────────────┘
```


