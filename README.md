# ERP Plans — Model Company & System Architecture

## Purpose

This repository contains the operational specifications, active workflows, and system architecture for **BuildRight Depot Corp.** (the **"Model Company"**), operating with all its capabilities and systems fully enabled under a modern, unified cloud ERP platform. Each subfolder contains the configuration, design, and architecture for running the model company on specific ERP platforms.

## Folder Structure

```
erpplans/
├── README.md                    ← You are here
├── 01-model-company/            ← Complete model company profile, requirements & workflows
│   ├── model-company-profile.md       Company profile, operations, financials
│   ├── erp-requirements.md            730 requirements across 32 categories
│   ├── data-volumes-and-integrations.md  Transaction volumes, integration map
│   ├── workflows/                      1,063 workflows organized by 43 workflow domain files
│   │   ├── README.md                         Workflow index & format guide
│   │   ├── WF-merchandising.md               19 workflows (W1, W13, W27, W40, W50, W63, W64, W68, W93, W97, W102, W107, W129, W130, W181, W262, W264, W279, W329)
│   │   ├── WF-procurement.md                 22 workflows (W2, W20, W36, W38, W44, W60, W62, W88, W110, W115, W136, W150, W155, W160, W161, W244, W245, W422, and sub-variants)
│   │   ├── WF-warehouse.md                   11 workflows (W3, W46, W52, W66, W106, W188, W221, W222, W270, and sub-variants)
│   │   ├── WF-inventory.md                   20 workflows (W4, W6, W22, W23, W42, W56, W57, W91, W92, W105, W154, W204, W214, W218, W219, W220, W439, and sub-variants)
│   │   ├── WF-store-operations.md            52 workflows (W5, W12, W16, W17, W18, W28, W29, W33, W45, W47, W67, W69, W71, W75, W86, W96, W109, W111, W170–W281, W330, W420, W438, W445, W463, and sub-variants)
│   │   ├── WF-ecommerce.md                   11 workflows (W11, W19, W98, W180, W210, W215, W246, W247, W266, W267, and sub-variants)
│   │   ├── WF-finance.md                     42 workflows (W7, W8, W9, W14, W21, W24, W25, W26, W30, W35, W39, W59, W70, W80, W81, W85, W89, W90, W94, W99–W108, W217, W260, W261, W276, W277, W435, W460, W461, W472, W473, and sub-variants)
│   │   ├── WF-hr.md                          16 workflows (W10, W15, W34, W43, W51, W72, W74, W76, W172, W178, W179, W251, W269, W280, W429, W449)
│   │   ├── WF-supply-chain.md                11 workflows (W31, W32, W133, W144, W183, W191, W249, W250, W268, W284, W464)
│   │   ├── WF-customer.md                    13 workflows (W41, W58, W61, W65, W84, W87, W103, W112, W156, W258, W259, W263, W328)
│   │   ├── WF-it-operations.md               44 workflows (W48, W53, W55, W73, W113, W131, W132, W152, W257, W265, W366–W398, W434, and sub-variants)
│   │   ├── WF-compliance.md                  25 workflows (W37, W49, W54, W77, W78, W79, W82, W95, W114, W157, W158, W167, W185, W207, W209, W216, W271, W427, W433, W437, W444, W446, W468, W469)
│   │   ├── WF-marketing.md                   12 workflows (W83, W104, W134, W135, W142, W143, W149, W151, W153, W189, W190, W286)
│   │   ├── WF-property.md                    7 workflows (W116–W119, W275, W430, W441)
│   │   ├── WF-audit.md                       41 workflows (W120–W123, W159, W331–W365, W466, and sub-variants)
│   │   ├── WF-governance.md                  11 workflows (W124–W128, W186, W230, W231, W285, W426, W465)
│   │   ├── WF-engineering-construction.md    5 workflows (W223–W227)
│   │   ├── WF-services.md                    11 workflows (W138, W139, W147, W148, W168, W169, W211, W213, W282, W440, W442)
│   │   ├── WF-treasury.md                    18 workflows (W232–W235, W317–W327, W423–W425)
│   │   ├── WF-hazmat.md                      4 workflows (W236–W239)
│   │   ├── WF-non-store-maintenance.md       4 workflows (W240–W243)
│   │   ├── WF-health-safety.md               4 workflows (W140, W141, W187, W436)
│   │   ├── WF-wholesale.md                   3 workflows (W145, W146, W283)
│   │   ├── WF-project-sales.md               8 workflows (W162–W166, W228, W229, W421)
│   │   ├── WF-esg.md                         5 workflows (W192–W195, W443)
│   │   ├── WF-logistics-fleet.md             5 workflows (W196–W199, W431)
│   │   ├── WF-innovation.md                  5 workflows (W200–W203, W208)
│   │   ├── WF-master-data.md                 41 workflows (W252–W254, W287–W316, W399–W406)
│   │   ├── WF-document-management.md         2 workflows (W255, W256)
│   │   ├── WF-additional-workflows.md       Batch 2: 20 additional cross-functional workflows
│   │   ├── WF-additional-workflows-batch3.md Batch 3: 20 additional cross-functional workflows
│   │   ├── WF-additional-workflows-batch4.md Batch 4: 20 additional cross-functional workflows
│   │   ├── WF-additional-workflows-batch5.md Batch 5: 20 additional cross-functional workflows
│   │   ├── WF-additional-workflows-batch6.md Batch 6: 20 additional cross-functional workflows
│   │   ├── workflow-system-touchpoint-map.md  ERP module-to-workflow cross-reference
│   │   ├── workflow-criticality-classification.md  Phase 1/2/3 implementation priorities
│   │   ├── WF-regulatory-permits.md          3 workflows (W447, W448, W467)
│   │   └── workflow-dependency-map.md    Prerequisite relationships, critical path, go-live checklist
│   ├── executive-summary.md            1-page C-suite overview
│   ├── assumptions-and-design-decisions.md  Consolidated assumptions & rationale
│   ├── requirement-workflow-matrix.md  Cross-reference: requirements ↔ workflows
│   ├── internal-controls-matrix.md     67 internal controls by objective
│   ├── mobile-app-strategy.md          Customer & employee mobile app strategy
│   └── data-migration-mapping.md       Data migration field mapping templates
└── 07-methodology/              ← Technical system architecture and guidelines
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

| Metric | Value |
|---|---|
| Requirements | **730** across 32 categories |
| Workflows | **1,063** across 43 workflow domain files |
| Internal Controls | 67 (31 preventive, 36 detective) |
| Must Have Requirements | 429 |
| Should Have Requirements | 295 |
| Nice to Have Requirements | 6 |


