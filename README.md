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
│   ├── erp-requirements.md            728 requirements across 38 categories
│   ├── data-volumes-and-integrations.md  Transaction volumes, integration map (canonical integration diagram)
│   ├── workflows/                      5,363 workflows organized by value stream
│   │   ├── README.md                           Navigation hub & quick stats
│   │   ├── value-stream-index.md              Master index (8 families · 188 value streams · 569 process areas)
│   │   ├── WORKFLOW-FORMAT-GUIDE.md            Workflow format, RACI key & conventions
│   │   ├── workflow-criticality-classification.md  Tier 1/2/3 confirmed priorities (5,372 rows)
│   │   ├── workflow-criticality-proposed.md    Keyword-driven tier proposal register for unclassified workflows (14 post-catalog workflows W5497–W5510 added 2026-08-24/26)
│   │   ├── workflow-dependency-map.md           Prerequisite relationships, critical path
│   │   ├── workflow-system-touchpoint-map.md    ERP module-to-workflow cross-reference
│   │   ├── workflow-gap-analysis.md            Gap-analysis methodology & 30-pass history
│   │   ├── VS-01-merchandise-strategy/         46 workflows (3 process areas)
│   │   ├── VS-02-supply-planning/               38 workflows (3 process areas)
│   │   ├── VS-03-vendor-management/             81 workflows (4 process areas)
│   │   ├── VS-04-dc-warehouse/                  45 workflows (3 process areas)
│   │   ├── VS-05-inventory-lifecycle/           35 workflows (3 process areas)
│   │   ├── VS-06-logistics-fleet/               36 workflows (3 process areas)
│   │   ├── VS-07-store-operations/              147 workflows (4 process areas)
│   │   ├── VS-08-pos-checkout/                  58 workflows (3 process areas)
│   │   ├── VS-09-in-store-services/             158 workflows (3 process areas)
│   │   ├── VS-10-ecommerce-digital/             62 workflows (3 process areas)
│   │   ├── VS-11-trade-project-wholesale/       52 workflows (3 process areas)
│   │   ├── VS-12-installation-services/         40 workflows (3 process areas)
│   │   ├── VS-13-customer-experience/           64 workflows (3 process areas)
│   │   ├── VS-14-marketing/                     40 workflows (3 process areas)
│   │   ├── VS-15-procure-to-pay/                43 workflows (2 process areas)
│   │   ├── VS-16-order-to-cash/                 31 workflows (3 process areas)
│   │   ├── VS-17-record-to-report/              67 workflows (4 process areas)
│   │   ├── VS-18-treasury-cash/                 33 workflows (3 process areas)
│   │   ├── VS-19-hire-to-retire/                75 workflows (5 process areas)
│   │   ├── VS-20-real-estate-construction/      32 workflows (3 process areas)
│   │   ├── VS-21-internal-audit-risk/           49 workflows (3 process areas)
│   │   ├── VS-22-compliance-regulatory/         57 workflows (3 process areas)
│   │   ├── VS-23-loss-prevention/               28 workflows (3 process areas)
│   │   ├── VS-24-health-safety-environment/     27 workflows (3 process areas)
│   │   ├── VS-25-esg-sustainability/            31 workflows (3 process areas)
│   │   ├── VS-26-business-continuity-insurance/ 30 workflows (3 process areas)
│   │   ├── VS-27-it-operations-security/        62 workflows (3 process areas)
│   │   ├── VS-28-data-analytics-bi/             24 workflows (3 process areas)
│   │   ├── VS-29-master-data/                   43 workflows (3 process areas)
│   │   ├── VS-30-innovation-digital/            29 workflows (3 process areas)
│   │   ├── VS-31-quality-management/            23 workflows (3 process areas)
│   │   ├── VS-32-returns-reverse-logistics/     23 workflows (3 process areas)
│   │   ├── VS-33-strategic-planning/            23 workflows (3 process areas)
│   │   ├── VS-34-expense-procurement/           22 workflows (3 process areas)
│   │   ├── VS-35-fixed-asset-management/        24 workflows (3 process areas)
│   │   ├── VS-36-corporate-governance/          24 workflows (3 process areas)
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
│   │   ├── VS-79-tax-management-bir-reporting/     25 workflows (3 process areas)
│   │   ├── VS-80-payment-operations-acquirer-settlement/ 24 workflows (3 process areas)
│   │   ├── VS-81-cash-in-transit-vault-armored/    24 workflows (3 process areas)
│   │   ├── VS-82-sari-sari-msme-micro-wholesale/   24 workflows (3 process areas)
│   │   ├── VS-83-occupational-health-clinic-wellness/ 25 workflows (3 process areas)
│   │   ├── VS-84-labor-relations-collective-bargaining/ 25 workflows (3 process areas)
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
│   │   ├── VS-124-sales-enablement-product-knowledge-clienteling/ 24 workflows (3 process areas)
│   │   ├── VS-125-cross-channel-fraud-management-payment-fraud-protection/ 24 workflows (3 process areas)
│   │   ├── VS-126-customer-data-platform-single-customer-view-identity-resolution/ 24 workflows (3 process areas)
│   │   ├── VS-127-sales-operations-planning-integrated-business-planning/ 32 workflows (4 process areas)
│   │   ├── VS-128-ai-ml-governance-responsible-ai/ 24 workflows (3 process areas)
│   │   ├── VS-129-competition-and-antitrust-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-130-corporate-development-ma-divestiture/ 24 workflows (3 process areas)
│   │   ├── VS-131-human-rights-responsible-supply-chain-due-diligence/ 24 workflows (3 process areas)
│   │   ├── VS-132-corporate-political-engagement-election-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-133-operational-excellence-process-mining-continuous-improvement/ 24 workflows (3 process areas)
│   │   ├── VS-134-organizational-change-management-digital-adoption-transformation-enablement/ 24 workflows (3 process areas)
│   │   ├── VS-135-technology-business-management-it-financial-management-cloud-finops/ 24 workflows (3 process areas)
│   │   ├── VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/ 24 workflows (3 process areas)
│   │   ├── VS-137-product-information-management-and-digital-asset-management/ 24 workflows (3 process areas)
│   │   ├── VS-138-integrated-facilities-management-workplace-services-and-building-automation/ 24 workflows (3 process areas)
│   │   ├── VS-139-trade-show-exhibition-and-field-event-marketing/ 24 workflows (3 process areas)
│   │   ├── VS-140-field-sales-outside-sales-and-route-to-market-force-management/ 24 workflows (3 process areas)
│   │   ├── VS-141-employee-transport-shuttle-and-daily-commute-management/ 24 workflows (3 process areas)
│   │   ├── VS-142-cash-on-delivery-operations-driver-cash-handling-and-reconciliation/ 24 workflows (3 process areas)
│   │   ├── VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/ 24 workflows (3 process areas)
│   │   ├── VS-144-employee-accommodation-dormitory-and-staff-housing/ 24 workflows (3 process areas)
│   │   ├── VS-145-garden-center-live-goods-and-plant-nursery/ 24 workflows (3 process areas)
│   │   ├── VS-146-customer-mystery-shopping-and-service-quality-assurance/ 24 workflows (3 process areas)
│   │   ├── VS-147-customer-safety-premises-liability-and-in-store-risk-management/ 24 workflows (3 process areas)
│   │   ├── VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/ 24 workflows (3 process areas)
│   │   ├── VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/ 24 workflows (3 process areas)
│   │   ├── VS-150-drug-free-workplace-and-substance-abuse-program/ 24 workflows (3 process areas)
│   │   ├── VS-151-auto-id-barcode-rfid-labeling-and-eas-operations/ 24 workflows (3 process areas)
│   │   ├── VS-152-corporate-social-responsibility-foundation-and-community-investment/ 24 workflows (3 process areas)
│   │   ├── VS-153-captive-insurance-reinsurance-and-enterprise-risk-financing/ 24 workflows (3 process areas)
│   │   ├── VS-154-home-construction-finance-loan-brokerage-and-mortgage-referral/ 24 workflows (3 process areas)
│   │   ├── VS-155-trade-in-buy-back-and-certified-pre-owned-product-resale/ 24 workflows (3 process areas)
│   │   ├── VS-156-in-store-value-added-services-and-financial-agency-operations/ 24 workflows (3 process areas)
│   │   ├── VS-157-revenue-recognition-pfrs-15-and-complex-contract-accounting/ 24 workflows (3 process areas)
│   │   ├── VS-158-product-costing-landed-cost-and-cost-accounting/ 24 workflows (3 process areas)
│   │   ├── VS-159-corporate-security-executive-protection-and-travel-risk-management/ 24 workflows (3 process areas)
│   │   ├── VS-160-global-mobility-immigration-and-foreign-worker-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-161-third-party-and-supplier-risk-management-tprm/ 24 workflows (3 process areas)
│   │   ├── VS-162-customer-pickup-truck-and-cargo-van-rental/ 24 workflows (3 process areas)
│   │   ├── VS-163-electric-vehicle-ev-charging-station-host-network-operations/ 24 workflows (3 process areas)
│   │   ├── VS-164-smart-locker-and-automated-parcel-collection-network/ 24 workflows (3 process areas)
│   │   ├── VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/ 24 workflows (3 process areas)
│   │   ├── VS-166-regulatory-license-permit-and-accreditation-portfolio-management/ 24 workflows (3 process areas)
│   │   ├── VS-167-workforce-background-screening-credentialing-and-personnel-vetting/ 24 workflows (3 process areas)
│   │   ├── VS-168-in-store-audio-ambient-media-and-music-royalty-licensing/ 24 workflows (3 process areas)
│   │   ├── VS-169-employee-uniform-workwear-and-ppe-issuance-program/ 24 workflows (3 process areas)
│   │   ├── VS-170-inventory-pledge-asset-based-lending-and-trust-receipt-financing/ 24 workflows (3 process areas)
│   │   ├── VS-171-customer-pickup-loading-zone-and-will-call-counter-operations/ 24 workflows (3 process areas)
│   │   ├── VS-172-third-party-installer-and-contractor-network-pro-referral-management/ 24 workflows (3 process areas)
│   │   ├── VS-173-investor-relations-capital-markets-and-securities-disclosure/ 24 workflows (3 process areas)
│   │   ├── VS-174-self-storage-portable-container-and-mobile-storage-operations/ 24 workflows (3 process areas)
│   │   ├── VS-175-propane-lpg-cylinder-exchange-and-gas-refill-operations/ 24 workflows (3 process areas)
│   │   ├── VS-176-blueprint-reprographics-and-large-format-plan-printing-services/ 24 workflows (3 process areas)
│   │   ├── VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/ 24 workflows (3 process areas)
│   │   ├── VS-178-landbanking-site-acquisition-and-agrarian-lgu-zoning-conversion/ 24 workflows (3 process areas)
│   │   ├── VS-179-extended-producer-responsibility-compliance-and-plastic-recovery-network/ 24 workflows (3 process areas)
│   │   ├── VS-180-disaster-relief-supply-chain-logistics-and-humanitarian-aid-coordination/ 24 workflows (3 process areas)
│   │   ├── VS-181-b2b-project-financing-escrow-account-orchestration-and-lien-release/ 24 workflows (3 process areas)
│   │   ├── VS-182-b2b-bulk-project-custom-import-indent-sourcing-and-brokerage/ 24 workflows (3 process areas)
│   │   ├── VS-183-dual-training-system-dts-and-tesda-partnership-program/ 24 workflows (3 process areas)
│   │   ├── VS-184-post-disaster-store-infrastructure-reconstruction-and-rehabilitation/ 24 workflows (3 process areas)
│   │   ├── VS-185-b2b-cooperative-credit-and-procurement-partnerships/ 24 workflows (3 process areas)
│   │   ├── VS-186-compact-and-heavy-construction-equipment-rental-fleet-operations/ 24 workflows (3 process areas)
│   │   ├── VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/ 24 workflows (3 process areas)
│   │   ├── VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/ 24 workflows (3 process areas)
│   │   ├── VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/ 24 workflows (3 process areas)
│   │   ├── VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/ 24 workflows (3 process areas)
│   │   ├── VS-191-customer-construction-debris-demolition-waste-and-site-cleanup-operations/ 24 workflows (3 process areas)
│   │   └── VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/ 24 workflows (3 process areas)
│   ├── executive-summary.md            1-page C-suite overview
│   ├── assumptions-and-design-decisions.md  Consolidated assumptions & rationale
│   ├── headcount-reality-check.md     HQ headcount vs. workflow-coverage gap analysis
│   ├── requirement-workflow-matrix.md  Cross-reference: requirements ↔ workflows
│   ├── internal-controls-matrix.md     808 internal controls by objective
│   ├── mobile-app-strategy.md          Customer & employee mobile app strategy
│   └── data-migration-mapping.md       Data migration field mapping templates
├── CHANGELOG.md                 ← Revision history
└── 07-methodology/              ← Technical system architecture and guidelines
    ├── README.md                     Methodology index & future document plan
    ├── technical-guidelines.md       POS hardware, infrastructure, integration, security
    ├── validate-repo.sh              Cross-reference validation (53 checks)
    ├── classify-workflows.py         Keyword-driven criticality classifier
    ├── confirm-all-workflows.py      One-time full-coverage confirmation pass (2,596 → 0 unclassified)
    ├── add-automation-controls.py    Automation/Controls field adder
    ├── backfill-controls.py          CTL-XX backfiller for Controls sections
    ├── add-expansion-anchors.py      One-time expansion/legacy-block anchor-control adder (CTL-172–239)
    ├── add-pa-controls.py            Process-area operating-control adder (CTL-240–808; closes CTL mapping to 100%)
    ├── backfill-participants.py      Participants derivation from Steps roles
    ├── backfill-time-estimate.py     Time Estimate derivation from step durations
    ├── finalize-time-estimates.py    Draft Time Estimate finalizer (per-occurrence roll-up + Frequency-derived annualization; Check 49 companion)
    ├── audit-time-estimate-math.py    Inline-arithmetic audit of Time Estimate / Staffing paragraphs (unit-convention-aware chain re-derivation; Check 50 guard)
    ├── reconcile-staffing-claims.py  Headcount-anchor & Volume-product reconciliation vs canonical registers (Check 51 guard)
    ├── audit-st-touchpoints.py       ST-vocabulary \& duplicate-Trigger guard (Check 52)
    ├── defragment-automation.py      One-time fragment-Automation-bullet repairer
    ├── fix-headcount-6757.py         Stale-headcount figure repairer (Check 24 companion)
    ├── fix-toc-anchors.py            Intra-file TOC anchor repairer (Check 23 companion)
    ├── fix-table-structure.py        One-time table delimiter/structure repairer (Check 29 companion)
    ├── fix-toc-completeness.py       PA TOC completeness/stray-fragment repairer (Check 30 companion)
    ├── fix-pa-names.py               PA-name 3-way aligner: H1 ↔ VS README ↔ index (Check 31 companion)
    ├── fix-pa-wrefs.py               Dangling/misdirected W- & CTL-reference repairer inside PA bodies (Check 33 companion)
    ├── fix-ctl-pa-names.py           PA-control objective canonicalizer: matrix ↔ index ↔ PA bodies (Check 34 companion)
    ├── fix-vs-wrefs.py               Workflow-reference-in-VS-namespace repairer inside the catalog (Check 35 companion)
    └── fix-controls-bullets.py       Controls-section list-hygiene/paren/bold repairer (Check 43 companion)
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
| Total Headcount | 6,762 (200 stores × 29 + 600 DC + 362 HQ) |
| Ecommerce | Yes (with BOPIS) |
| Country | Philippines |

## Key Metrics

> **Single source of truth**: Counts below are derived from actual document content. All documents in this repository reference these figures.

| Metric | Value | Source |
|---|---|---|
| Requirements | **728** across 38 categories | `01-model-company/erp-requirements.md` |
| Workflows (total) | **5,363** across 188 value streams, 569 process areas | `01-model-company/workflows/value-stream-index.md` |
| Internal Controls | 808 (88 preventive, 720 detective) | `01-model-company/internal-controls-matrix.md` |
| Must Have Requirements | 429 | `01-model-company/erp-requirements.md` |
| Should Have Requirements | 293 | `01-model-company/erp-requirements.md` |
| Nice to Have Requirements | 6 | `01-model-company/erp-requirements.md` |

## Coverage & Known Gaps

| Coverage Area | Status | Source |
|---|---|---|
| Requirements | 728 fully specified (429 Must / 293 Should / 6 Nice) | `erp-requirements.md` |
| Workflows | 5,363 fully specified across 188 value streams (5,349 confirmed-classified + 14 post-catalog additions W5497–W5510 with keyword-proposed tiers) | `workflows/value-stream-index.md` |
| Criticality classification | **5,349 of 5,363 workflows classified** — the confirmed register holds 5,372 rows incl. 23 `###` parent/summary sub-workflows; the 2026-06-28 Full-Coverage Confirmation Pass promoted the remaining keyword-proposed workflows (unclassified 2,596 → 0; 65 → Tier 1 statutory, 179 → Tier 3 analytics, 3 demoted to Tier 2, remainder adopted); the fourteen post-catalog workflows W5497–W5510 (added 2026-08-24/26: POSH/Safe Spaces CODI, RA 11165 telecommuting, director education, customer digital accessibility/WCAG, climate risk assessment, employee financial wellness, restricted-substance & chemical-content product compliance, extreme-heat work interruption & occupational heat-stress management, concession item catalog/barcode/price-label governance, concessionaire self-service price change & propagation, concession service-fee billing & cost recovery, fringe benefits tax determination & quarterly BIR 1605 filing, unfulfilled-demand & lost-sales capture, supplier service-fee billing & account deduction for store-rendered services) carry keyword-driven proposed tiers in `workflow-criticality-proposed.md` pending a confirmation pass | `workflows/workflow-criticality-classification.md` |
| Internal controls | 808 controls mapped to workflows and requirements (67 core + 172 domain anchors CTL-68–239 + 569 process-area operating controls CTL-240–808) — CTL-XX citation coverage is 100% of workflows | `internal-controls-matrix.md` |
| Retired VS numbers | VS-49–VS-52 were retired after a 2026-06-14 review found their 96 workflow files contained only auto-generated placeholder content; the numbers remain unused. The resulting gaps — plus additional uncovered capabilities — were filled across thirty gap-analysis passes (2026-06-14 → 2026-06-21), growing the active inventory from 84 to 188 value streams (VS-89–VS-192; W2993–W5488). The canonical per-pass detail (candidates considered/rejected, workflow-ID allocation, family-subtotal impact) lives in [`workflows/workflow-gap-analysis.md`](01-model-company/workflows/workflow-gap-analysis.md) §3–§4 and [CHANGELOG.md](CHANGELOG.md) | — |

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
   │  erp-requirements.md ←→ workflows/ (5,363 WF)    │
   │       ↕                    ↕                      │
   │  internal-controls-   workflow-criticality-      │
   │  matrix.md (808 CTL)  classification.md          │
   │       ↕                    ↕                      │
   │  requirement-workflow- workflow-dependency-       │
   │  matrix.md              map.md                   │
   │       ↕                    ↕                      │
   │  assumptions-and-      workflow-system-           │
   │  design-decisions.md   touchpoint-map.md          │
   │                          ↕                        │
   │                value-stream-index.md              │
   │            (188 VS · 569 process areas)            │
   └───────────────────────────────────────────────────┘
```
