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
│   ├── erp-requirements.md            733 requirements across 38 categories
│   ├── data-volumes-and-integrations.md  Transaction volumes, integration map (canonical integration diagram)
│   ├── workflows/                      3,708 workflows organized by value stream
│   │   ├── value-stream-index.md              Master index (8 families · 120 value streams · 364 process areas)
│   │   ├── WORKFLOW-FORMAT-GUIDE.md            Workflow format, RACI key & conventions
│   │   ├── workflow-criticality-classification.md  Phase 1/2/3 implementation priorities
│   │   ├── workflow-dependency-map.md           Prerequisite relationships, critical path
│   │   ├── workflow-system-touchpoint-map.md    ERP module-to-workflow cross-reference
│   │   ├── VS-01-merchandise-strategy/         46 workflows (3 process areas)
│   │   ├── VS-02-supply-planning/               37 workflows (3 process areas)
│   │   ├── VS-03-vendor-management/             81 workflows (4 process areas)
│   │   ├── VS-04-dc-warehouse/                  45 workflows (3 process areas)
│   │   ├── VS-05-inventory-lifecycle/           35 workflows (3 process areas)
│   │   ├── VS-06-logistics-fleet/               36 workflows (3 process areas)
│   │   ├── VS-07-store-operations/              144 workflows (4 process areas)
│   │   ├── VS-08-pos-checkout/                  58 workflows (3 process areas)
│   │   ├── VS-09-in-store-services/             158 workflows (3 process areas)
│   │   ├── VS-10-ecommerce-digital/             61 workflows (3 process areas)
│   │   ├── VS-11-trade-project-wholesale/       52 workflows (3 process areas)
│   │   ├── VS-12-installation-services/         39 workflows (3 process areas)
│   │   ├── VS-13-customer-experience/           64 workflows (3 process areas)
│   │   ├── VS-14-marketing/                     40 workflows (3 process areas)
│   │   ├── VS-15-procure-to-pay/                42 workflows (2 process areas)
│   │   ├── VS-16-order-to-cash/                 31 workflows (3 process areas)
│   │   ├── VS-17-record-to-report/              67 workflows (4 process areas)
│   │   ├── VS-18-treasury-cash/                 33 workflows (3 process areas)
│   │   ├── VS-19-hire-to-retire/                74 workflows (5 process areas)
│   │   ├── VS-20-real-estate-construction/      32 workflows (3 process areas)
│   │   ├── VS-21-internal-audit-risk/           48 workflows (3 process areas)
│   │   ├── VS-22-compliance-regulatory/         57 workflows (3 process areas)
│   │   ├── VS-23-loss-prevention/               28 workflows (3 process areas)
│   │   ├── VS-24-health-safety-environment/     26 workflows (3 process areas)
│   │   ├── VS-25-esg-sustainability/            31 workflows (3 process areas)
│   │   ├── VS-26-business-continuity-insurance/ 30 workflows (3 process areas)
│   │   ├── VS-27-it-operations-security/        62 workflows (3 process areas)
│   │   ├── VS-28-data-analytics-bi/             24 workflows (3 process areas)
│   │   ├── VS-29-master-data/                   43 workflows (3 process areas)
│   │   ├── VS-30-innovation-digital/            29 workflows (3 process areas)
│   │   ├── VS-31-quality-management/            22 workflows (3 process areas)
│   │   ├── VS-32-returns-reverse-logistics/     23 workflows (3 process areas)
│   │   ├── VS-33-strategic-planning/            23 workflows (3 process areas)
│   │   ├── VS-34-expense-procurement/           22 workflows (3 process areas)
│   │   ├── VS-35-fixed-asset-management/        24 workflows (3 process areas)
│   │   ├── VS-36-corporate-governance/          23 workflows (3 process areas)
│   │   ├── VS-37-store-opening-commissioning/   26 workflows (3 process areas)
│   │   ├── VS-38-consumer-credit-financing/     24 workflows (3 process areas)
│   │   ├── VS-39-vendor-rebate-incentive/       24 workflows (3 process areas)
│   │   ├── VS-40-capex-project-accounting/      24 workflows (3 process areas)
│   │   ├── VS-41-private-label-brand/           24 workflows (3 process areas)
│   │   ├── VS-42-property-lease-admin/          24 workflows (3 process areas)
│   │   ├── VS-43-trade-professional-program/    24 workflows (3 process areas)
│   │   ├── VS-44-consumer-insights-market-research/ 24 workflows (3 process areas)
│   │   ├── VS-45-consignment-vmi-operations/    24 workflows (3 process areas)
│   │   ├── VS-46-government-institutional-sales/ 24 workflows (3 process areas)
│   │   ├── VS-47-subscription-recurring-services/ 24 workflows (3 process areas)
│   │   ├── VS-48-retail-media-network/          24 workflows (3 process areas)
│   │   ├── VS-53-warranty-guarantee-management/ 24 workflows (3 process areas)
│   │   ├── VS-54-gift-card-stored-value/        24 workflows (3 process areas)
│   │   ├── VS-55-store-planogram-space-optimization/ 24 workflows (3 process areas)
│   │   ├── VS-56-third-party-delivery-partner/  24 workflows (3 process areas)
│   │   ├── VS-57-competitive-price-intelligence/ 24 workflows (3 process areas)
│   │   ├── VS-58-coupon-digital-promotions/     24 workflows (3 process areas)
│   │   ├── VS-59-store-closure-decommissioning/ 24 workflows (3 process areas)
│   │   ├── VS-60-omnichannel-order-routing/     24 workflows (3 process areas)
│   │   ├── VS-61-fuel-fleet-cost-management/    24 workflows (3 process areas)
│   │   ├── VS-62-product-sample-display-management/ 24 workflows (3 process areas)
│   │   ├── VS-63-store-communication-task-management/ 24 workflows (3 process areas)
│   │   ├── VS-64-seasonal-merchandise-clearance/ 24 workflows (3 process areas)
│   │   ├── VS-65-ecommerce-marketplace-integration/ 24 workflows (3 process areas)
│   │   ├── VS-66-customer-project-design-services/ 24 workflows (3 process areas)
│   │   ├── VS-67-vendor-scorecard-analytics/    24 workflows (3 process areas)
│   │   ├── VS-68-trade-credit-risk-management/  24 workflows (3 process areas)
│   │   ├── VS-69-typhoon-disaster-response/      24 workflows (3 process areas)
│   │   ├── VS-70-solar-renewable-energy/          24 workflows (3 process areas)
│   │   ├── VS-71-anti-counterfeit-authentication/  24 workflows (3 process areas)
│   │   ├── VS-72-cross-entity-shared-services/    24 workflows (3 process areas)
│   │   ├── VS-73-store-waste-circular-economy/    24 workflows (3 process areas)
│   │   ├── VS-74-contractor-jobsite-delivery/     24 workflows (3 process areas)
│   │   ├── VS-75-digital-engagement-app/          24 workflows (3 process areas)
│   │   ├── VS-76-multi-region-lgu-compliance/     24 workflows (3 process areas)
│   │   ├── VS-77-construction-material-staging/   24 workflows (3 process areas)
│   │   ├── VS-78-green-building-advisory/          24 workflows (3 process areas)
│   │   ├── VS-79-tax-management-bir-reporting/     24 workflows (3 process areas)
│   │   ├── VS-80-payment-operations-acquirer-settlement/ 24 workflows (3 process areas)
│   │   ├── VS-81-cash-in-transit-vault-armored/    24 workflows (3 process areas)
│   │   ├── VS-82-sari-sari-msme-micro-wholesale/   24 workflows (3 process areas)
│   │   ├── VS-83-occupational-health-clinic-wellness/ 24 workflows (3 process areas)
│   │   ├── VS-84-labor-relations-collective-bargaining/ 24 workflows (3 process areas)
│   │   ├── VS-85-mandatory-discount-eligibility-tax-credit/ 24 workflows (3 process areas)
│   │   ├── VS-86-anti-financial-crime-aml-abc/     24 workflows (3 process areas)
│   │   ├── VS-87-customs-trade-compliance-tariff/  24 workflows (3 process areas)
│   │   ├── VS-88-document-control-records-retention/ 24 workflows (3 process areas)
│   │   ├── VS-89-product-recall-safety-corrective-action/ 24 workflows (3 process areas)
│   │   ├── VS-90-damage-claims-freight-recovery/ 24 workflows (3 process areas)
│   │   ├── VS-91-consumer-data-privacy-protection/ 24 workflows (3 process areas)
│   │   ├── VS-92-kitting-bundling-build-to-order-assembly/ 24 workflows (3 process areas)
│   │   ├── VS-93-dark-store-micro-fulfillment/ 24 workflows (3 process areas)
│   │   ├── VS-94-cooperative-community-enterprise-procurement/ 24 workflows (3 process areas)
│   │   ├── VS-95-marketplace-operator-third-party-seller/ 24 workflows (3 process areas)
│   │   ├── VS-96-equipment-leasing-capital-equipment-finance/ 24 workflows (3 process areas)
│   │   ├── VS-97-corporate-real-estate-property-portfolio/ 24 workflows (3 process areas)
│   │   ├── VS-98-contingent-contract-outsourced-workforce/ 24 workflows (3 process areas)
│   │   ├── VS-99-it-asset-technology-lifecycle-management/ 24 workflows (3 process areas)
│   │   ├── VS-100-legal-operations-litigation-ip-management/ 24 workflows (3 process areas)
│   │   ├── VS-101-merchandise-financial-planning-otb-margin-management/ 24 workflows (3 process areas)
│   │   ├── VS-102-compensation-benefits-total-rewards/ 24 workflows (3 process areas)
│   │   ├── VS-103-hr-shared-services-employee-experience-people-analytics/ 24 workflows (3 process areas)
│   │   ├── VS-104-government-affairs-public-policy-industry-relations/ 24 workflows (3 process areas)
│   │   ├── VS-105-supply-chain-finance-working-capital-management/ 24 workflows (3 process areas)
│   │   ├── VS-106-commodity-input-cost-risk-management/ 24 workflows (3 process areas)
│   │   ├── VS-107-strategic-key-account-enterprise-customer-management/ 24 workflows (3 process areas)
│   │   ├── VS-108-onsite-renewable-energy-prosumer-asset-operations/ 24 workflows (3 process areas)
│   │   ├── VS-109-store-remodel-renovation-lifecycle-refurbishment/ 24 workflows (3 process areas)
│   │   ├── VS-110-freight-procurement-carrier-management-and-freight-audit/ 24 workflows (3 process areas)
│   │   ├── VS-111-packaging-pallet-and-returnable-transport-item-management/ 24 workflows (3 process areas)
│   │   ├── VS-112-corporate-project-and-program-management-office/ 24 workflows (3 process areas)
│   │   ├── VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/ 24 workflows (3 process areas)
│   │   ├── VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-115-calibration-metrology-and-measurement-traceability-management/ 24 workflows (3 process areas)
│   │   ├── VS-116-performance-bond-surety-and-bank-guarantee-management/ 24 workflows (3 process areas)
│   │   ├── VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-118-revenue-assurance-pricing-integrity-and-leakage-management/ 24 workflows (3 process areas)
│   │   ├── VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/ 24 workflows (3 process areas)
│   │   ├── VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/ 24 workflows (3 process areas)
│   │   ├── VS-121-talent-acquisition-employer-brand-candidate-experience/ 24 workflows (3 process areas)
│   │   ├── VS-122-global-sourcing-import-buying-sourcing-agent-management/ 24 workflows (3 process areas)
│   │   ├── VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/ 24 workflows (3 process areas)
│   │   └── VS-124-sales-enablement-product-knowledge-clienteling/ 24 workflows (3 process areas)
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
| Requirements | **733** across 38 categories | `01-model-company/erp-requirements.md` |
| Workflows (total) | **3,708** across 120 value streams, 364 process areas | `01-model-company/workflows/value-stream-index.md` |
| Internal Controls | 67 (31 preventive, 36 detective) | `01-model-company/internal-controls-matrix.md` |
| Must Have Requirements | 431 | `01-model-company/erp-requirements.md` |
| Should Have Requirements | 296 | `01-model-company/erp-requirements.md` |
| Nice to Have Requirements | 6 | `01-model-company/erp-requirements.md` |

## Coverage & Known Gaps

| Coverage Area | Status | Source |
|---|---|---|
| Requirements | 733 fully specified (431 Must / 296 Should / 6 Nice) | `erp-requirements.md` |
| Workflows | 3,708 fully specified across 120 value streams | `workflows/value-stream-index.md` |
| Criticality classification | **1,167 of 3,708 workflows classified** (31%); 2,541 remain unclassified pending review | `workflows/workflow-criticality-classification.md` |
| Internal controls | 67 controls mapped to workflows and requirements | `internal-controls-matrix.md` |
| Retired VS numbers | VS-49, VS-50, VS-51, VS-52 are intentionally retired (placeholder content was removed 2026-06-14). Two 2026-06-14 gap-analysis passes filled all four capability gaps: VS-90 ↔ former VS-50, VS-92 ↔ former VS-51, VS-89 (Product Recall) and VS-91 (Consumer Data Privacy) added new; then VS-93 ↔ former VS-49, VS-94 ↔ former VS-52, plus VS-95 (Marketplace Operator) and VS-96 (Equipment Leasing) added new. A third 2026-06-14 gap-analysis pass added VS-97 (Corporate Real Estate & Property Portfolio), VS-98 (Contingent & Outsourced Workforce), VS-99 (IT Asset & Technology Lifecycle), and VS-100 (Legal Operations, Litigation & IP) to strengthen the previously-thinnest operating families. A fourth 2026-06-14 gap-analysis pass added VS-101 (Merchandise Financial Planning, OTB & Margin Management), VS-102 (Compensation, Benefits & Total Rewards), VS-103 (HR Shared Services, Employee Experience & People Analytics), and VS-104 (Government Affairs, Public Policy & Industry Relations) — each filling a capability previously conflated with an adjacent covered one. A fifth 2026-06-14 gap-analysis pass added VS-105 (Supply Chain Finance & Working Capital Management), VS-106 (Commodity & Input-Cost Risk Management), VS-107 (Strategic Key Account & Enterprise Customer Management), and VS-108 (On-Site Renewable Energy & Prosumer Asset Operations) — each filling a capability previously touched only as a single workflow within another value stream or conflated with an adjacent covered one. A sixth 2026-06-14 gap-analysis pass added VS-109 (Store Remodel, Renovation & Lifecycle Refurbishment Program), VS-110 (Freight Procurement, Carrier Management & Freight Audit), VS-111 (Packaging, Pallet & Returnable Transport Item (RTI) Management), and VS-112 (Corporate Project & Program Management Office (PMO)) — each filling a capability previously uncovered or sprinkled across multiple value streams (remodel-execution vs capex-accounting/opening/closure; freight-spend vs logistics-execution/import; packaging-asset vs DC/inventory/waste; and project-portfolio governance vs capex-accounting/strategic-planning respectively). A seventh 2026-06-14 gap-analysis pass added VS-113 (Enterprise Architecture, Application Portfolio & Technology Strategy), VS-114 (Dangerous Goods & Hazmat Transport, Ecommerce & Regulatory Compliance), VS-115 (Calibration, Metrology & Measurement Traceability Management), and VS-116 (Performance Bond, Surety & Bank Guarantee Management) — each filling a capability previously genuinely uncovered ('enterprise architecture' appeared in zero PA files), sprinkled across 50+ files with no owner (calibration/metrology), distinct from fixed-site HSE storage (DG transport/ecommerce/regulatory), or sprinkled across B2G/B2B/treasury (performance bonds/surety). An eighth 2026-06-14 gap-analysis pass added VS-117 (DTI-BPS Product Standards Certification & PS Mark/ICC Compliance), VS-118 (Revenue Assurance, Pricing Integrity & Leakage Management), VS-119 (Whistleblower, Ethics & Corporate Integrity (Speak-Up) Program), and VS-120 (Energy Efficiency, Conservation & RA 11285 Compliance Program) — three elevating a single workflow within another value stream to a dedicated program (W447 DTI-BPS, W348 Revenue Assurance, W2943 ABC-Whistleblower) and one filling a genuinely-uncovered statutory program (RA 11285). A ninth 2026-06-14 gap-analysis pass added VS-121 (Talent Acquisition, Employer Brand & Candidate Experience), VS-122 (Global Sourcing, Import Buying & Sourcing Agent Management), VS-123 (Skilled-Trade Apprenticeship, Vocational Education & Capability Pipeline), and VS-124 (Sales Enablement, Product Knowledge Mastery & Clienteling) — each filling a capability previously genuinely uncovered or reduced to incidental single-workflow references with no dedicated owner ('candidate experience'/'career site'/'talent community', 'global sourcing'/'sourcing agent'/'overseas buying office', 'apprenticeship program', and 'clienteling' each appeared in zero PA files). The retired numbers remain unused. See [CHANGELOG.md](CHANGELOG.md) | — |

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
    │  erp-requirements.md ←→ workflows/ (3,708 WF)    │
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
    │            (120 VS · 364 process areas)            │
   └───────────────────────────────────────────────────┘
```
