# BuildRight Depot Corp. — IT Product Operating Model & Product-Team Design

> How the Information Technology department organizes as long-lived, business-paired **product
> teams** to run and continuously improve the unified cloud ERP across all 188 value streams —
> team structure, membership, roles, RACI, governance, and sizing.

---

## 1. Purpose & Scope

This document defines the target **IT operating model** for BuildRight Depot Corp.: the product
taxonomy, product-team membership, role definitions, RACI, governance bodies, cadence, and
headcount. It is the organizational counterpart to the system landscape defined in
[`technical-guidelines.md`](technical-guidelines.md) and the business process catalog in
[`workflows/value-stream-index.md`](../01-model-company/workflows/value-stream-index.md)
(188 value streams, 569 process areas, 5,363 workflows).

Scope covers the steady state **after** the unified cloud ERP go-live (the "Live & Unified"
landscape of `model-company-profile.md` §14.1). Implementation-phase structures (SI governance,
cutover command centers) are out of scope; see §10 for the transition.

---

## 2. Design Principles

1. **Products, not projects.** A product is a long-lived business capability delivered through
   the ERP (e.g., "Store Systems & POS"). Teams are stable, own outcomes (uptime, adoption,
   value-stream KPIs), and absorb enhancement, defect, regulatory, and tech-debt work into one
   backlog — no temporary project teams that disband at go-live.
2. **Business–IT pairing.** Every product team is co-owned by an **IT Product Owner** and a
   **Business Product Owner (BPO)** — the actual process owner from the department that runs the
   value stream (`model-company-profile.md` §3.3/§11.1). This prevents the "unowned program"
   failure mode previously caught in the S&OP/IBP gap (VS-127).
3. **Value streams map to products; teams own systems.** A value stream is a business process;
   a product team owns the *systems and configuration* that enable it. Every one of the 188 value
   streams has exactly **one primary product team** (gap-free, overlap-free ownership — §4),
   while controls embedded in those workflows remain jointly governed (§6.3).
4. **Configure-first talent model.** The landscape is a single-vendor unified cloud ERP
   (§14.1); therefore domain teams are built around **ERP functional analysts and process
   architects**, not classical software developers. Dedicated engineers concentrate in the
   platform layer (integration, ecommerce app edge, data engineering).
5. **Tier-aware service levels.** The workflow criticality register
   ([`workflow-criticality-classification.md`](../01-model-company/workflows/workflow-criticality-classification.md):
   1,375 Tier-1 / 3,243 Tier-2 / 754 Tier-3) drives each team's regression coverage, incident
   SLAs, and roadmap prioritization. Every Tier-1 workflow in a team's domain maps to at least
   one automated regression test.
6. **Platform thinking.** Domain ("stream-aligned") teams build on shared **platform teams**
   (integration, infrastructure, security, data, field services) that treat domain teams as
   their customers, following Team-Topologies-style separation: stream-aligned, platform, and
   enabling (GRC) team types.

---

## 3. Product Taxonomy — From 188 Value Streams to 12 IT Products

### 3.1 The mapping rule

The 8 value-stream families do not translate 1:1 into teams (188 teams is absurd; 8 teams is too
coarse for the selling side). The taxonomy below groups by **system domain and business
partner**, then assigns every value stream to exactly one primary product team. Two
consequences worth stating explicitly:

- The **Governance & Assurance family (37 VS)** gets **no dedicated team**: those workflows are
  controls *embedded in* other products' configurations, with a small GRC/controls cell (§5.3)
  and Internal Audit/Legal & Compliance as demand-side owners. The mapping in §4 shows which
  product carries each governance VS's system enablement.
- The **Technology & Data family (13 VS)** is IT itself: these value streams are owned directly
  by the platform teams and the CIO Office.

### 3.2 IT product portfolio

| # | Product Team | Code | Type | Primary Business Partner(s) | VS | Workflows |
|---|---|---|---|---|---|---|
| 1 | Merchandising & Supply Chain Systems | MSC | Stream-aligned | VP Supply Chain; VP Merchandising | 16 | 485 |
| 2 | Warehouse, Logistics & Inventory Systems | WLI | Stream-aligned | VP Supply Chain (DC Ops, Fleet & Logistics) | 22 | 571 |
| 3 | Store Systems & POS | SSP | Stream-aligned | Store Operations Director | 25 | 873 |
| 4 | Commerce & Customer Platforms | CCP | Stream-aligned | CMO; Digital Commerce Inc. GM; Trade/Account Mgmt | 27 | 786 |
| 5 | Finance & Treasury Systems | FIN | Stream-aligned | CFO (Controller, Treasurer, Tax) | 30 | 797 |
| 6 | Corporate, Governance & Asset Systems | CORP | Stream-aligned | VP Legal & Compliance; Facilities & Real Estate; Quality; Internal Audit & Risk | 35 | 915 |
| 7 | People Systems | PEO | Stream-aligned | CHRO | 16 | 437 |
| | **Domain subtotal** | | | | **171** | **4,864** |
| 8 | Integration & API Platform | IAP | Platform | All product teams | 0 | 0 |
| 9 | Cloud Infrastructure & SRE | INFRA | Platform | All product teams | 3 | 116 |
| 10 | Cybersecurity, Privacy & OT Security | SEC | Platform + enabling | All product teams; DPO; Internal Audit | 3 | 72 |
| 11 | Data Platform & MDM | DP | Platform | All product teams; Strategy/CPM; Marketing | 7 | 210 |
| 12 | Field & End-User Services | FS | Platform | All 205 locations; 6,762 users | 1 | 24 |
| | CIO Office (EA, Portfolio Governance, FinOps) | CIO | Enabling | CIO; CEO; Finance | 3 | 77 |
| | **Platform + CIO subtotal** | | | | **17** | **499** |
| | **Total** | | | | **188** | **5,363** |

> Team **workload is weighted by Tier-1 density and transaction volume, not raw VS count** —
> CORP's 35 VS are mostly registers and GRC tooling with modest system complexity, while SSP's
> 25 VS include the 600-terminal POS estate with a 99.9% uptime target. Sizing (§9) reflects
> this.

---

## 4. Full Value-Stream → Product-Team Mapping (188 VS)

> Primary team = the product team accountable for the systems enabling the value stream. The
> business process owner is the department that runs the process (§3.3/§11.1 departments).
> Business-side BPO/SME participation per team is defined in §5.2.

### 4.1 Plan & Source (15 VS → all MSC)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-01](../01-model-company/workflows/VS-01-merchandise-strategy/README.md) | Merchandise Strategy | MSC | Merchandising |
| [VS-02](../01-model-company/workflows/VS-02-supply-planning/README.md) | Supply Planning | MSC | Supply Chain (Demand Planning) |
| [VS-03](../01-model-company/workflows/VS-03-vendor-management/README.md) | Vendor Management & Procurement | MSC | Supply Chain (Procurement) with Merchandising (Buying) |
| [VS-41](../01-model-company/workflows/VS-41-private-label-brand/README.md) | Private Label & Exclusive Brand Management | MSC | Merchandising (Private Brand) |
| [VS-45](../01-model-company/workflows/VS-45-consignment-vmi-operations/README.md) | Consignment & Vendor-Managed Inventory Operations | MSC | Merchandising with Supply Chain |
| [VS-57](../01-model-company/workflows/VS-57-competitive-price-intelligence/README.md) | Competitive Price Intelligence & Monitoring | MSC | Merchandising (Pricing) |
| [VS-64](../01-model-company/workflows/VS-64-seasonal-merchandise-clearance/README.md) | Seasonal Merchandise Transition & Clearance | MSC | Merchandising |
| [VS-67](../01-model-company/workflows/VS-67-vendor-scorecard-analytics/README.md) | Vendor Scorecard & Performance Analytics | MSC | Supply Chain (Vendor Management) |
| [VS-94](../01-model-company/workflows/VS-94-cooperative-community-enterprise-procurement/README.md) | Cooperative & Community Enterprise Procurement | MSC | Supply Chain (Procurement) |
| [VS-101](../01-model-company/workflows/VS-101-merchandise-financial-planning-otb-margin-management/README.md) | Merchandise Financial Planning, OTB & Margin Management | MSC | Merchandising with Finance (FP&A) |
| [VS-106](../01-model-company/workflows/VS-106-commodity-input-cost-risk-management/README.md) | Commodity & Input-Cost Risk Management | MSC | Merchandising with Finance |
| [VS-122](../01-model-company/workflows/VS-122-global-sourcing-import-buying-sourcing-agent-management/README.md) | Global Sourcing, Import Buying & Sourcing Agent Management | MSC | Merchandising (Import Buying) with Supply Chain (Imports) |
| [VS-127](../01-model-company/workflows/VS-127-sales-operations-planning-integrated-business-planning/README.md) | Sales & Operations Planning (S&OP) & Integrated Business Planning | MSC | S&OP/IBP sub-team |
| [VS-131](../01-model-company/workflows/VS-131-human-rights-responsible-supply-chain-due-diligence/README.md) | Human Rights, Modern Slavery & Responsible Supply Chain Due Diligence | MSC | Supply Chain (Vendor Management) with Legal & Compliance |
| [VS-182](../01-model-company/workflows/VS-182-b2b-bulk-project-custom-import-indent-sourcing-and-brokerage/README.md) | B2B Bulk-Project Custom Import (Indent Sourcing & Brokerage Operations) | MSC | Merchandising with Trade/Account Management |

### 4.2 Make & Move (19 VS → all WLI)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-04](../01-model-company/workflows/VS-04-dc-warehouse/README.md) | DC & Warehouse Operations | WLI | DC Operations |
| [VS-05](../01-model-company/workflows/VS-05-inventory-lifecycle/README.md) | Inventory Lifecycle | WLI | Inventory Planning |
| [VS-06](../01-model-company/workflows/VS-06-logistics-fleet/README.md) | Logistics & Fleet | WLI | Fleet & Logistics |
| [VS-32](../01-model-company/workflows/VS-32-returns-reverse-logistics/README.md) | Returns & Reverse Logistics | WLI | DC Operations with Store Operations |
| [VS-56](../01-model-company/workflows/VS-56-third-party-delivery-partner/README.md) | Third-Party Delivery Partner Management | WLI | Fleet & Logistics |
| [VS-61](../01-model-company/workflows/VS-61-fuel-fleet-cost-management/README.md) | Fuel & Fleet Cost Management | WLI | Fleet & Logistics |
| [VS-74](../01-model-company/workflows/VS-74-contractor-jobsite-delivery/README.md) | Professional Contractor Job Site Delivery | WLI | Fleet & Logistics |
| [VS-81](../01-model-company/workflows/VS-81-cash-in-transit-vault-armored/README.md) | Cash-in-Transit, Vault & Armored Car Operations | WLI | Treasury with Loss Prevention |
| [VS-90](../01-model-company/workflows/VS-90-damage-claims-freight-recovery/README.md) | Damage, Claims & Freight Recovery Management | WLI | Fleet & Logistics |
| [VS-92](../01-model-company/workflows/VS-92-kitting-bundling-build-to-order-assembly/README.md) | Kitting, Bundling & Build-to-Order Assembly Operations | WLI | DC Operations |
| [VS-93](../01-model-company/workflows/VS-93-dark-store-micro-fulfillment/README.md) | Dark Store & Micro-Fulfillment Operations | WLI | Store Operations with Supply Chain |
| [VS-110](../01-model-company/workflows/VS-110-freight-procurement-carrier-management-and-freight-audit/README.md) | Freight Procurement, Carrier Management & Freight Audit | WLI | Fleet & Logistics |
| [VS-111](../01-model-company/workflows/VS-111-packaging-pallet-and-returnable-transport-item-management/README.md) | Packaging, Pallet & Returnable Transport Item (RTI) Management | WLI | DC Operations |
| [VS-136](../01-model-company/workflows/VS-136-supply-chain-network-design-multi-echelon-inventory-optimization-flow-engineering/README.md) | Supply Chain Network Design, Multi-Echelon Inventory Optimization & Flow Engineering | WLI | VP Supply Chain |
| [VS-143](../01-model-company/workflows/VS-143-bulky-white-goods-delivery-installation-haul-away-and-recycling/README.md) | Bulky & White-Goods Delivery, Installation, Haul-Away & Recycling Operations | WLI | Fleet & Logistics |
| [VS-155](../01-model-company/workflows/VS-155-trade-in-buy-back-and-certified-pre-owned-product-resale/README.md) | Trade-In, Buy-Back & Certified Pre-Owned Product Resale | WLI | Store Operations |
| [VS-180](../01-model-company/workflows/VS-180-disaster-relief-supply-chain-logistics-and-humanitarian-aid-coordination/README.md) | Disaster Relief Supply Chain Logistics & Humanitarian Aid Coordination | WLI | VP Supply Chain |
| [VS-191](../01-model-company/workflows/VS-191-customer-construction-debris-demolition-waste-and-site-cleanup-operations/README.md) | Customer Construction Debris, Demolition Waste & Site Cleanup Operations | WLI | Fleet & Logistics |
| [VS-192](../01-model-company/workflows/VS-192-green-fleet-transition-electric-vehicle-fleet-operations-and-sustainable-transportation/README.md) | Green Fleet Transition, EV Fleet Operations & Sustainable Transportation | WLI | Fleet & Logistics |

### 4.3 Sell & Serve (46 VS → 20 SSP, 26 CCP)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-07](../01-model-company/workflows/VS-07-store-operations/README.md) | Store Operations | SSP | Store Operations |
| [VS-08](../01-model-company/workflows/VS-08-pos-checkout/README.md) | POS & Checkout | SSP | Store Operations |
| [VS-09](../01-model-company/workflows/VS-09-in-store-services/README.md) | In-Store Customer Services | SSP | Store Operations with Customer Service |
| [VS-10](../01-model-company/workflows/VS-10-ecommerce-digital/README.md) | Ecommerce & Digital Channels | CCP | Digital Commerce |
| [VS-11](../01-model-company/workflows/VS-11-trade-project-wholesale/README.md) | Trade, Project & Wholesale | CCP | Trade/Account Management |
| [VS-12](../01-model-company/workflows/VS-12-installation-services/README.md) | Installation & Services | CCP | Store Operations (Services) |
| [VS-13](../01-model-company/workflows/VS-13-customer-experience/README.md) | Customer Experience & Loyalty | CCP | Marketing (Loyalty) |
| [VS-14](../01-model-company/workflows/VS-14-marketing/README.md) | Marketing & Communications | CCP | Marketing |
| [VS-37](../01-model-company/workflows/VS-37-store-opening-commissioning/README.md) | Store Opening & Commissioning | SSP | Store Operations with Facilities |
| [VS-43](../01-model-company/workflows/VS-43-trade-professional-program/README.md) | Trade Professional Program & Contractor Services | CCP | Trade/Account Management |
| [VS-44](../01-model-company/workflows/VS-44-consumer-insights-market-research/README.md) | Consumer Insights & Market Research | CCP | Marketing (Insights) |
| [VS-46](../01-model-company/workflows/VS-46-government-institutional-sales/README.md) | Government & Institutional B2G Sales | CCP | Trade/Account Management |
| [VS-47](../01-model-company/workflows/VS-47-subscription-recurring-services/README.md) | Subscription & Recurring Home Services | CCP | Store Operations (Services) |
| [VS-48](../01-model-company/workflows/VS-48-retail-media-network/README.md) | Retail Media Network & Vendor Advertising | CCP | Marketing |
| [VS-53](../01-model-company/workflows/VS-53-warranty-guarantee-management/README.md) | Warranty & Guarantee Management | CCP | Customer Service |
| [VS-55](../01-model-company/workflows/VS-55-store-planogram-space-optimization/README.md) | Store Planogram & Space Optimization | SSP | Merchandising (Assortment & Space) |
| [VS-58](../01-model-company/workflows/VS-58-coupon-digital-promotions/README.md) | Coupon & Digital Promotions Management | CCP | Marketing |
| [VS-60](../01-model-company/workflows/VS-60-omnichannel-order-routing/README.md) | Omnichannel Order Routing & Fulfillment Orchestration | CCP | Digital Commerce with Supply Chain |
| [VS-62](../01-model-company/workflows/VS-62-product-sample-display-management/README.md) | Product Sample & Display Management | SSP | Merchandising |
| [VS-63](../01-model-company/workflows/VS-63-store-communication-task-management/README.md) | Store Communication & Task Management | SSP | Store Operations |
| [VS-65](../01-model-company/workflows/VS-65-ecommerce-marketplace-integration/README.md) | E-Commerce Marketplace Integration | CCP | Digital Commerce |
| [VS-66](../01-model-company/workflows/VS-66-customer-project-design-services/README.md) | Customer Project & Design Services | CCP | Trade/Account Management |
| [VS-70](../01-model-company/workflows/VS-70-solar-renewable-energy/README.md) | Solar & Renewable Energy Product Operations | CCP | Merchandising |
| [VS-75](../01-model-company/workflows/VS-75-digital-engagement-app/README.md) | Digital Engagement & Mobile App Operations | CCP | Digital Commerce |
| [VS-77](../01-model-company/workflows/VS-77-construction-material-staging/README.md) | Construction Project Material Staging & Phased Delivery | CCP | Trade/Account Management |
| [VS-78](../01-model-company/workflows/VS-78-green-building-advisory/README.md) | Green Building & Sustainable Product Advisory | CCP | Merchandising |
| [VS-82](../01-model-company/workflows/VS-82-sari-sari-msme-micro-wholesale/README.md) | Sari-Sari Store & MSME Micro-Wholesale Program | CCP | Trade/Account Management |
| [VS-95](../01-model-company/workflows/VS-95-marketplace-operator-third-party-seller/README.md) | Marketplace Operator & Third-Party Seller Management | CCP | Digital Commerce |
| [VS-107](../01-model-company/workflows/VS-107-strategic-key-account-enterprise-customer-management/README.md) | Strategic Key Account & Enterprise Customer Management | CCP | Trade/Account Management |
| [VS-124](../01-model-company/workflows/VS-124-sales-enablement-product-knowledge-clienteling/README.md) | Sales Enablement, Product Knowledge Mastery & Clienteling | CCP | Marketing with Trade/Account Management |
| [VS-139](../01-model-company/workflows/VS-139-trade-show-exhibition-and-field-event-marketing/README.md) | Trade Show, Exhibition & Field Event Marketing | CCP | Marketing |
| [VS-140](../01-model-company/workflows/VS-140-field-sales-outside-sales-and-route-to-market-force-management/README.md) | Field Sales, Outside Sales & Route-to-Market Force Management | CCP | Trade/Account Management |
| [VS-145](../01-model-company/workflows/VS-145-garden-center-live-goods-and-plant-nursery/README.md) | Garden Center, Live Goods & Plant Nursery Operations | SSP | Store Operations |
| [VS-149](../01-model-company/workflows/VS-149-self-checkout-scan-and-go-and-unattended-retail-technology-operations/README.md) | Self-Checkout, Scan-&-Go & Unattended Retail Technology Operations | SSP | Store Operations |
| [VS-156](../01-model-company/workflows/VS-156-in-store-value-added-services-and-financial-agency-operations/README.md) | In-Store Value-Added Services & Financial Agency Operations | SSP | Store Operations |
| [VS-162](../01-model-company/workflows/VS-162-customer-pickup-truck-and-cargo-van-rental/README.md) | Customer Pickup Truck & Cargo Van Rental (Self-Haul) Operations | SSP | Store Operations |
| [VS-164](../01-model-company/workflows/VS-164-smart-locker-and-automated-parcel-collection-network/README.md) | Smart Locker & Automated Parcel Collection Network | SSP | Digital Commerce with Store Operations |
| [VS-168](../01-model-company/workflows/VS-168-in-store-audio-ambient-media-and-music-royalty-licensing/README.md) | In-Store Audio, Ambient Media & Music Royalty Licensing | SSP | Marketing |
| [VS-171](../01-model-company/workflows/VS-171-customer-pickup-loading-zone-and-will-call-counter-operations/README.md) | Customer Pickup, Loading Zone & Will-Call Counter Operations | SSP | Store Operations |
| [VS-172](../01-model-company/workflows/VS-172-third-party-installer-and-contractor-network-pro-referral-management/README.md) | Third-Party Installer & Contractor Network (Pro-Referral) Management | SSP | Store Operations with Trade/Account Management |
| [VS-174](../01-model-company/workflows/VS-174-self-storage-portable-container-and-mobile-storage-operations/README.md) | Self-Storage, Portable Container & Mobile-Storage Operations | SSP | Store Operations |
| [VS-175](../01-model-company/workflows/VS-175-propane-lpg-cylinder-exchange-and-gas-refill-operations/README.md) | Propane, LPG Cylinder Exchange & Gas Refill Operations | SSP | Store Operations |
| [VS-176](../01-model-company/workflows/VS-176-blueprint-reprographics-and-large-format-plan-printing-services/README.md) | Blueprint, Reprographics & Large-Format Plan Printing Services | SSP | Store Operations |
| [VS-177](../01-model-company/workflows/VS-177-field-retail-operations-regional-district-management-and-multi-store-execution/README.md) | Field Retail Operations, Regional/District Management & Multi-Store Retail Execution Network | SSP | Store Operations (Field Management) |
| [VS-185](../01-model-company/workflows/VS-185-b2b-cooperative-credit-and-procurement-partnerships/README.md) | B2B Cooperative Credit & Procurement Partnerships | CCP | Trade/Account Management |
| [VS-186](../01-model-company/workflows/VS-186-compact-and-heavy-construction-equipment-rental-fleet-operations/README.md) | Compact & Heavy Construction Equipment Rental Fleet Operations | SSP | Store Operations |

### 4.4 Finance (29 VS → all FIN)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-15](../01-model-company/workflows/VS-15-procure-to-pay/README.md) | Procure-to-Pay | FIN | Finance (AP) with Supply Chain (Procurement) |
| [VS-16](../01-model-company/workflows/VS-16-order-to-cash/README.md) | Order-to-Cash | FIN | Finance (AR) |
| [VS-17](../01-model-company/workflows/VS-17-record-to-report/README.md) | Record-to-Report | FIN | Finance (Controller) |
| [VS-18](../01-model-company/workflows/VS-18-treasury-cash/README.md) | Treasury & Cash | FIN | Treasury |
| [VS-34](../01-model-company/workflows/VS-34-expense-procurement/README.md) | Expense & Non-Merchandise Procurement | FIN | Finance with Supply Chain (Procurement) |
| [VS-38](../01-model-company/workflows/VS-38-consumer-credit-financing/README.md) | Consumer Credit & Financing | FIN | Finance with Store Operations |
| [VS-39](../01-model-company/workflows/VS-39-vendor-rebate-incentive/README.md) | Vendor Rebate & Incentive Management | FIN | Finance with Merchandising |
| [VS-40](../01-model-company/workflows/VS-40-capex-project-accounting/README.md) | Capex & Project Accounting | FIN | Finance (Controller) |
| [VS-54](../01-model-company/workflows/VS-54-gift-card-stored-value/README.md) | Gift Card & Stored Value Management | FIN | Finance with Marketing |
| [VS-68](../01-model-company/workflows/VS-68-trade-credit-risk-management/README.md) | Trade Credit Insurance & Risk Management | FIN | Finance (AR) with Trade/Account Management |
| [VS-72](../01-model-company/workflows/VS-72-cross-entity-shared-services/README.md) | Cross-Entity Shared Services & Chargeback | FIN | Finance (Controller) |
| [VS-79](../01-model-company/workflows/VS-79-tax-management-bir-reporting/README.md) | Tax Management & BIR Statutory Reporting | FIN | Tax |
| [VS-80](../01-model-company/workflows/VS-80-payment-operations-acquirer-settlement/README.md) | Payment Operations, Acquirer & Settlement Management | FIN | Finance with Treasury |
| [VS-96](../01-model-company/workflows/VS-96-equipment-leasing-capital-equipment-finance/README.md) | Equipment Leasing & Capital Equipment Finance | FIN | Finance |
| [VS-105](../01-model-company/workflows/VS-105-supply-chain-finance-working-capital-management/README.md) | Supply Chain Finance & Working Capital Management | FIN | Treasury |
| [VS-116](../01-model-company/workflows/VS-116-performance-bond-surety-and-bank-guarantee-management/README.md) | Performance Bond, Surety & Bank Guarantee Management | FIN | Finance with Legal & Compliance |
| [VS-118](../01-model-company/workflows/VS-118-revenue-assurance-pricing-integrity-and-leakage-management/README.md) | Revenue Assurance, Pricing Integrity & Leakage Management | FIN | Finance with Merchandising (Pricing) |
| [VS-125](../01-model-company/workflows/VS-125-cross-channel-fraud-management-payment-fraud-protection/README.md) | Cross-Channel Fraud Management & Payment Fraud Protection | FIN | Finance with Loss Prevention |
| [VS-142](../01-model-company/workflows/VS-142-cash-on-delivery-operations-driver-cash-handling-and-reconciliation/README.md) | Cash-on-Delivery (COD) Operations, Driver Cash Handling & Reconciliation | FIN | Finance with Digital Commerce |
| [VS-148](../01-model-company/workflows/VS-148-lease-accounting-pfrs-16-and-right-of-use-asset-management/README.md) | Lease Accounting (PFRS 16/IFRS 16) & Right-of-Use Asset Management | FIN | Finance (Controller) |
| [VS-153](../01-model-company/workflows/VS-153-captive-insurance-reinsurance-and-enterprise-risk-financing/README.md) | Captive Insurance, Reinsurance & Enterprise Risk Financing | FIN | Finance with Internal Audit & Risk |
| [VS-154](../01-model-company/workflows/VS-154-home-construction-finance-loan-brokerage-and-mortgage-referral/README.md) | Home Construction Finance, Loan Brokerage & Mortgage Referral Services | FIN | Finance with Store Operations |
| [VS-157](../01-model-company/workflows/VS-157-revenue-recognition-pfrs-15-and-complex-contract-accounting/README.md) | Revenue Recognition (PFRS 15) & Complex Contract Accounting | FIN | Finance (Controller) |
| [VS-158](../01-model-company/workflows/VS-158-product-costing-landed-cost-and-cost-accounting/README.md) | Product Costing, Landed-Cost & Cost Accounting | FIN | Finance with Merchandising |
| [VS-170](../01-model-company/workflows/VS-170-inventory-pledge-asset-based-lending-and-trust-receipt-financing/README.md) | Inventory Pledge, Asset-Based Lending & Trust-Receipt (Warehouse-Receipt) Financing | FIN | Treasury |
| [VS-173](../01-model-company/workflows/VS-173-investor-relations-capital-markets-and-securities-disclosure/README.md) | Investor Relations, Capital Markets & Securities Disclosure | FIN | Finance (Controller) with Legal & Compliance |
| [VS-181](../01-model-company/workflows/VS-181-b2b-project-financing-escrow-account-orchestration-and-lien-release/README.md) | B2B Project Financing, Escrow Account Orchestration & Lien Release | FIN | Finance with Trade/Account Management |
| [VS-188](../01-model-company/workflows/VS-188-trade-reseller-floor-plan-and-dealer-inventory-financing/README.md) | Trade Reseller Floor-Plan & Dealer Inventory Financing | FIN | Finance |
| [VS-189](../01-model-company/workflows/VS-189-trade-receivables-factoring-invoice-discounting-and-securitization/README.md) | Trade Accounts Receivable Factoring, Invoice Discounting & Receivables Securitization | FIN | Finance (AR) |

### 4.5 People (16 VS → all PEO)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-19](../01-model-company/workflows/VS-19-hire-to-retire/README.md) | Hire-to-Retire | PEO | HR |
| [VS-83](../01-model-company/workflows/VS-83-occupational-health-clinic-wellness/README.md) | Occupational Health, Safety Clinic & Employee Wellness | PEO | HR with HSE |
| [VS-84](../01-model-company/workflows/VS-84-labor-relations-collective-bargaining/README.md) | Labor Relations & Collective Bargaining Management | PEO | HR (Labor Relations) |
| [VS-98](../01-model-company/workflows/VS-98-contingent-contract-outsourced-workforce/README.md) | Contingent, Contract & Outsourced Workforce Management | PEO | HR |
| [VS-102](../01-model-company/workflows/VS-102-compensation-benefits-total-rewards/README.md) | Compensation, Benefits & Total Rewards Strategy | PEO | HR (Compensation & Benefits) |
| [VS-103](../01-model-company/workflows/VS-103-hr-shared-services-employee-experience-people-analytics/README.md) | HR Shared Services, Employee Experience & People Analytics | PEO | HR (Shared Services) |
| [VS-121](../01-model-company/workflows/VS-121-talent-acquisition-employer-brand-candidate-experience/README.md) | Talent Acquisition, Employer Brand & Candidate Experience | PEO | HR (Recruitment) |
| [VS-123](../01-model-company/workflows/VS-123-skilled-trade-apprenticeship-vocational-education-capability-pipeline/README.md) | Skilled-Trade Apprenticeship, Vocational Education & Capability Pipeline | PEO | HR (Training) |
| [VS-134](../01-model-company/workflows/VS-134-organizational-change-management-digital-adoption-transformation-enablement/README.md) | Organizational Change Management, Digital Adoption & Transformation Enablement | PEO | HR with Strategy/Corporate Planning |
| [VS-141](../01-model-company/workflows/VS-141-employee-transport-shuttle-and-daily-commute-management/README.md) | Employee Transport, Shuttle & Daily Commute Management | PEO | HR with Facilities |
| [VS-144](../01-model-company/workflows/VS-144-employee-accommodation-dormitory-and-staff-housing/README.md) | Employee Accommodation, Dormitory & Staff Housing Operations | PEO | HR with Facilities |
| [VS-150](../01-model-company/workflows/VS-150-drug-free-workplace-and-substance-abuse-program/README.md) | Drug-Free Workplace & Substance Abuse Program | PEO | HR with HSE |
| [VS-160](../01-model-company/workflows/VS-160-global-mobility-immigration-and-foreign-worker-compliance/README.md) | Global Mobility, Immigration & Foreign Worker Compliance | PEO | HR with Legal & Compliance |
| [VS-167](../01-model-company/workflows/VS-167-workforce-background-screening-credentialing-and-personnel-vetting/README.md) | Workforce Background Screening, Credentialing & Personnel Vetting | PEO | HR |
| [VS-169](../01-model-company/workflows/VS-169-employee-uniform-workwear-and-ppe-issuance-program/README.md) | Employee Uniform, Workwear & PPE-Issuance Program | PEO | HR with HSE |
| [VS-183](../01-model-company/workflows/VS-183-dual-training-system-dts-and-tesda-partnership-program/README.md) | Dual Training System (DTS) & TESDA Partnership Program | PEO | HR (Training) |

### 4.6 Asset & Infrastructure (13 VS → 12 CORP, 1 SSP)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-20](../01-model-company/workflows/VS-20-real-estate-construction/README.md) | Real Estate & Construction | CORP | Facilities & Real Estate |
| [VS-35](../01-model-company/workflows/VS-35-fixed-asset-management/README.md) | Fixed Asset Management | CORP | Finance (Controller) with Facilities |
| [VS-42](../01-model-company/workflows/VS-42-property-lease-admin/README.md) | Property & Lease Administration | CORP | Facilities (Lease Admin) |
| [VS-59](../01-model-company/workflows/VS-59-store-closure-decommissioning/README.md) | Store Closure & Decommissioning | SSP | Store Operations with Facilities |
| [VS-97](../01-model-company/workflows/VS-97-corporate-real-estate-property-portfolio/README.md) | Corporate Real Estate & Property Portfolio Management | CORP | Facilities & Real Estate |
| [VS-108](../01-model-company/workflows/VS-108-onsite-renewable-energy-prosumer-asset-operations/README.md) | On-Site Renewable Energy & Prosumer Asset Operations | CORP | Facilities with Sustainability/ESG |
| [VS-109](../01-model-company/workflows/VS-109-store-remodel-renovation-lifecycle-refurbishment/README.md) | Store Remodel, Renovation & Lifecycle Refurbishment Program | CORP | Store Operations with Facilities |
| [VS-112](../01-model-company/workflows/VS-112-corporate-project-and-program-management-office/README.md) | Corporate Project & Program Management Office (PMO) | CORP | Strategy/Corporate Planning (PMO) |
| [VS-120](../01-model-company/workflows/VS-120-energy-efficiency-conservation-and-ra-11285-compliance-program/README.md) | Energy Efficiency, Conservation & RA 11285 Compliance Program | CORP | Facilities with Sustainability/ESG |
| [VS-138](../01-model-company/workflows/VS-138-integrated-facilities-management-workplace-services-and-building-automation/README.md) | Integrated Facilities Management, Workplace Services & Building Automation | CORP | Facilities |
| [VS-163](../01-model-company/workflows/VS-163-electric-vehicle-ev-charging-station-host-network-operations/README.md) | Electric Vehicle (EV) Charging Station Host Network Operations | CORP | Facilities with Digital Commerce |
| [VS-178](../01-model-company/workflows/VS-178-landbanking-site-acquisition-and-agrarian-lgu-zoning-conversion/README.md) | Landbanking, Site Acquisition & Agrarian/LGU Zoning Conversion Operations | CORP | Facilities & Real Estate with Strategy |
| [VS-184](../01-model-company/workflows/VS-184-post-disaster-store-infrastructure-reconstruction-and-rehabilitation/README.md) | Post-Disaster Store Infrastructure Reconstruction & Rehabilitation | CORP | Facilities with Store Operations |

### 4.7 Governance & Assurance (37 VS → no dedicated team; embedded controls)

> These value streams are enabled by the product teams that own the systems the controls run
> in. Demand-side owners are Internal Audit & Risk, Legal & Compliance, and the respective
> program owners named below; the SEC GRC/controls cell (§5.3) coordinates control design and
> test coverage against the 808-control register in
> [`internal-controls-matrix.md`](../01-model-company/internal-controls-matrix.md).

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-21](../01-model-company/workflows/VS-21-internal-audit-risk/README.md) | Internal Audit & Risk | CORP | Internal Audit & Risk (Board Audit Committee) |
| [VS-22](../01-model-company/workflows/VS-22-compliance-regulatory/README.md) | Compliance & Regulatory | CORP | Legal & Compliance |
| [VS-23](../01-model-company/workflows/VS-23-loss-prevention/README.md) | Loss Prevention & Asset Protection | SSP | Regional Loss Prevention |
| [VS-24](../01-model-company/workflows/VS-24-health-safety-environment/README.md) | Health, Safety & Environment | CORP | HSE |
| [VS-25](../01-model-company/workflows/VS-25-esg-sustainability/README.md) | ESG & Sustainability | CORP | Sustainability/ESG |
| [VS-26](../01-model-company/workflows/VS-26-business-continuity-insurance/README.md) | Business Continuity & Insurance | INFRA | Internal Audit & Risk with CIO Office (DR owner) |
| [VS-31](../01-model-company/workflows/VS-31-quality-management/README.md) | Quality Management & Product Compliance | CORP | Quality Management |
| [VS-33](../01-model-company/workflows/VS-33-strategic-planning/README.md) | Strategic Planning & Corporate Performance Management | DP | Strategy/Corporate Planning |
| [VS-36](../01-model-company/workflows/VS-36-corporate-governance/README.md) | Corporate Governance & Board Management | CORP | Corporate Secretary |
| [VS-69](../01-model-company/workflows/VS-69-typhoon-disaster-response/README.md) | Typhoon & Natural Disaster Preparedness & Response | INFRA | HSE with Store Operations and CIO Office |
| [VS-71](../01-model-company/workflows/VS-71-anti-counterfeit-authentication/README.md) | Anti-Counterfeit & Product Authentication | CORP | Quality Management with Loss Prevention |
| [VS-73](../01-model-company/workflows/VS-73-store-waste-circular-economy/README.md) | Store-Level Waste Management & Circular Economy | CORP | Sustainability/ESG with Store Operations |
| [VS-76](../01-model-company/workflows/VS-76-multi-region-lgu-compliance/README.md) | Philippine Multi-Region LGU & Local Regulatory Compliance | CORP | Legal & Compliance (Regulatory) |
| [VS-85](../01-model-company/workflows/VS-85-mandatory-discount-eligibility-tax-credit/README.md) | Mandatory Discount, Eligibility & Tax Credit Recovery | SSP | Store Operations with Tax |
| [VS-86](../01-model-company/workflows/VS-86-anti-financial-crime-aml-abc/README.md) | Anti-Financial Crime, AML/KYC & Anti-Corruption | FIN | Legal & Compliance (AML/MLRO) with Finance |
| [VS-87](../01-model-company/workflows/VS-87-customs-trade-compliance-tariff/README.md) | Customs Trade Compliance & Tariff Optimization | WLI | Supply Chain (Imports & Customs) |
| [VS-88](../01-model-company/workflows/VS-88-document-control-records-retention/README.md) | Document Control, Records Management & Retention | CORP | Legal & Compliance with Finance |
| [VS-89](../01-model-company/workflows/VS-89-product-recall-safety-corrective-action/README.md) | Product Recall & Safety Corrective Action Management | WLI | Quality Management with Store Operations |
| [VS-91](../01-model-company/workflows/VS-91-consumer-data-privacy-protection/README.md) | Consumer Data Privacy & Data Protection Program | SEC | Legal & Compliance (DPO) |
| [VS-100](../01-model-company/workflows/VS-100-legal-operations-litigation-ip-management/README.md) | Legal Operations, Litigation & Intellectual Property Management | CORP | Legal & Compliance |
| [VS-104](../01-model-company/workflows/VS-104-government-affairs-public-policy-industry-relations/README.md) | Government Affairs, Public Policy & Industry Relations | CORP | Legal & Compliance (Government Affairs) |
| [VS-114](../01-model-company/workflows/VS-114-dangerous-goods-hazmat-transport-ecommerce-regulatory-compliance/README.md) | Dangerous Goods (DG) & Hazmat Transport, Ecommerce & Regulatory Compliance | WLI | Fleet & Logistics with HSE |
| [VS-117](../01-model-company/workflows/VS-117-dti-bps-product-standards-certification-ps-mark-icc-compliance/README.md) | DTI-BPS Product Standards Certification & PS Mark/ICC Compliance | MSC | Quality Management with Merchandising |
| [VS-119](../01-model-company/workflows/VS-119-whistleblower-ethics-and-corporate-integrity-speak-up-program/README.md) | Whistleblower, Ethics & Corporate Integrity (Speak-Up) Program | CORP | Legal & Compliance |
| [VS-129](../01-model-company/workflows/VS-129-competition-and-antitrust-compliance/README.md) | Competition & Antitrust Compliance (RA 10667 / PCC) | CORP | Legal & Compliance |
| [VS-130](../01-model-company/workflows/VS-130-corporate-development-ma-divestiture/README.md) | Corporate Development, Mergers, Acquisitions, Divestiture & Strategic Transactions | CORP | Strategy with Legal & Compliance |
| [VS-132](../01-model-company/workflows/VS-132-corporate-political-engagement-election-compliance/README.md) | Corporate Political Engagement, Election Compliance & Public Affairs Governance | CORP | Legal & Compliance |
| [VS-133](../01-model-company/workflows/VS-133-operational-excellence-process-mining-continuous-improvement/README.md) | Operational Excellence, Process Mining & Continuous Improvement Program | DP | Strategy with COO Office |
| [VS-146](../01-model-company/workflows/VS-146-customer-mystery-shopping-and-service-quality-assurance/README.md) | Customer Mystery Shopping & Service Quality Assurance Program | CCP | Customer Service with Marketing |
| [VS-147](../01-model-company/workflows/VS-147-customer-safety-premises-liability-and-in-store-risk-management/README.md) | Customer Safety, Premises Liability & In-Store Risk Management | SSP | Store Operations with HSE |
| [VS-152](../01-model-company/workflows/VS-152-corporate-social-responsibility-foundation-and-community-investment/README.md) | Corporate Social Responsibility, Foundation & Community Investment | CORP | Sustainability/ESG |
| [VS-159](../01-model-company/workflows/VS-159-corporate-security-executive-protection-and-travel-risk-management/README.md) | Corporate Security, Executive Protection & Travel Risk Management | CORP | Loss Prevention (Corporate Security) with Legal & Compliance |
| [VS-161](../01-model-company/workflows/VS-161-third-party-and-supplier-risk-management-tprm/README.md) | Third-Party & Supplier Risk Management (TPRM) | SEC | Internal Audit & Risk with Legal & Compliance |
| [VS-165](../01-model-company/workflows/VS-165-pcab-contractor-licensing-and-ra-4566-construction-contractor-compliance/README.md) | PCAB Contractor Licensing & RA 4566 Construction Contractor Compliance | CORP | Legal & Compliance (Regulatory) |
| [VS-166](../01-model-company/workflows/VS-166-regulatory-license-permit-and-accreditation-portfolio-management/README.md) | Regulatory License, Permit & Accreditation Portfolio Management | CORP | Legal & Compliance (Regulatory) |
| [VS-179](../01-model-company/workflows/VS-179-extended-producer-responsibility-compliance-and-plastic-recovery-network/README.md) | Extended Producer Responsibility (EPR) Compliance & Plastic Recovery Network | CORP | Sustainability/ESG |
| [VS-187](../01-model-company/workflows/VS-187-household-hazardous-waste-paint-and-product-stewardship-take-back/README.md) | Household Hazardous Waste, Paint & Used-Product Stewardship Take-Back Program | CORP | Sustainability/ESG with Store Operations |

### 4.8 Technology & Data (13 VS → owned by platform teams and CIO Office)

| VS | Value Stream | Team | Business Process Owner |
|---|---|---|---|
| [VS-27](../01-model-company/workflows/VS-27-it-operations-security/README.md) | IT Operations & Security | INFRA | CIO Office (co-owned with SEC) |
| [VS-28](../01-model-company/workflows/VS-28-data-analytics-bi/README.md) | Data, Analytics & BI | DP | CIO Office with Strategy |
| [VS-29](../01-model-company/workflows/VS-29-master-data/README.md) | Master Data Management | DP | CIO Office with Merchandising Operations & Master Data |
| [VS-30](../01-model-company/workflows/VS-30-innovation-digital/README.md) | Innovation & Digital Transformation | CIO Office | CEO with CIO |
| [VS-99](../01-model-company/workflows/VS-99-it-asset-technology-lifecycle-management/README.md) | IT Asset & Technology Lifecycle Management | FS | CIO Office |
| [VS-113](../01-model-company/workflows/VS-113-enterprise-architecture-application-portfolio-and-technology-strategy/README.md) | Enterprise Architecture, Application Portfolio & Technology Strategy | CIO Office | CIO |
| [VS-115](../01-model-company/workflows/VS-115-calibration-metrology-and-measurement-traceability-management/README.md) | Calibration, Metrology & Measurement Traceability Management | CORP | Quality Management (Metrology) with Facilities |
| [VS-126](../01-model-company/workflows/VS-126-customer-data-platform-single-customer-view-identity-resolution/README.md) | Customer Data Platform, Single Customer View & Identity Resolution | DP | Marketing with CIO Office |
| [VS-128](../01-model-company/workflows/VS-128-ai-ml-governance-responsible-ai/README.md) | AI/ML Governance & Responsible AI | DP | CIO Office with Legal & Compliance (AI Governance) |
| [VS-135](../01-model-company/workflows/VS-135-technology-business-management-it-financial-management-cloud-finops/README.md) | Technology Business Management, IT Financial Management & Cloud FinOps | CIO Office | CIO with Finance |
| [VS-137](../01-model-company/workflows/VS-137-product-information-management-and-digital-asset-management/README.md) | Product Information Management (PIM) & Digital Asset Management (DAM) | DP | Merchandising (Master Data) with Digital Commerce |
| [VS-151](../01-model-company/workflows/VS-151-auto-id-barcode-rfid-labeling-and-eas-operations/README.md) | Auto-ID, Barcode, RFID, Price-Tag Labeling & EAS Operations | SSP | Store Operations with Loss Prevention |
| [VS-190](../01-model-company/workflows/VS-190-operational-technology-ot-ics-cybersecurity-and-retail-technology-asset-protection/README.md) | Operational Technology (OT) / ICS Cybersecurity & Retail Technology Asset Protection | SEC | IT Security with Loss Prevention |

### 4.9 Mapping reconciliation

| Team | VS | Workflows |
|---|---|---|
| MSC | 15 (§4.1) + 1 (VS-117) | 485 |
| WLI | 19 (§4.2) + 3 (VS-87, VS-89, VS-114) | 571 |
| SSP | 20 (§4.3) + 1 (VS-59) + 3 (VS-23, VS-85, VS-147) + 1 (VS-151) | 873 |
| CCP | 26 (§4.3) + 1 (VS-146) | 786 |
| FIN | 29 (§4.4) + 1 (VS-86) | 797 |
| CORP | 12 (§4.6) + 22 (§4.7) + 1 (VS-115) | 915 |
| PEO | 16 (§4.5) | 437 |
| INFRA | 2 (VS-26, VS-69) + 1 (VS-27) | 116 |
| SEC | 2 (VS-91, VS-161) + 1 (VS-190) | 72 |
| DP | 2 (VS-33, VS-133) + 5 (VS-28, VS-29, VS-126, VS-128, VS-137) | 210 |
| FS | 1 (VS-99) | 24 |
| CIO Office | 3 (VS-30, VS-113, VS-135) | 77 |
| **Total** | **171 + 17 = 188** | **4,864 + 499 = 5,363** |

---

## 5. Product-Team Membership & Roles

### 5.1 Standard domain-team shape

Every domain team (MSC, WLI, SSP, CCP, FIN, CORP, PEO) is built on the same 6-role core. IT
headcount figures below are FTE; §9 sizes each team.

| Member | IT HC | Reports to | Role & Responsibilities |
|---|---|---|---|
| **IT Product Owner (PO)** | 1 | CIO (solid); product-domain exec (dotted) | Single accountable owner of the product backlog, roadmap, and budget. Prioritizes enhancements, defects, regulatory changes, and tech debt. Owns product KPIs (§8.3). Represents the product at the Product Council. Manages the vendor relationship for the product's ERP modules (escalations, roadmap influence, release intake). |
| **Product/Process Architect** | 1 | Head of EA (solid); team PO (dotted) | Owns end-to-end process design across the team's process areas; enforces fit-to-standard; maintains the team's portion of the enterprise architecture (VS-113); chairs the team's design reviews; prepares customization-exception requests for the Architecture Review Board. |
| **ERP Functional Analysts / Configurators** | 2–4 | Team PO | Day-to-day configuration: approval matrices, pricing rules, WMS parameters, tax setups, workflow conditions. Analyze incidents that are configuration defects. Write functional specifications for integrations and reports. Each analyst owns named sub-domains (e.g., AP vs AR vs tax inside FIN). |
| **Commerce/App Engineer** (CCP only) | 1 | Team PO | Builds and maintains the custom edge on top of the SaaS ecommerce engine — storefront theming, mobile-app releases, marketplace connectors — under platform standards (IAP APIs, CI/CD). |
| **Data & Reporting Analyst** | 1 | Team PO (solid); DP lead (dotted) | Product-specific dashboards and reports on the DP semantic layer; data-quality checks on the product's master-data domains; close-cycle reporting (e.g., FIN's 5-working-day close pack). |
| **QA & Release Analyst** | 1 | Team PO | Owns the regression suite (every Tier-1 workflow in the domain covered), UAT coordination with business SMEs, release notes, cutover checklists, and post-release verification. |

### 5.2 Business-side membership (not IT headcount)

| Member | Source | Commitment | Role & Responsibilities |
|---|---|---|---|
| **Business Product Owner (BPO)** | The department named "Business Process Owner" in §4 | ~30–50% | Owns requirements and business value; accepts releases into the business; drives user adoption; decides process-change vs configuration-change trade-offs; co-signs the roadmap. Named individuals, e.g., the S&OP/IBP Lead is the standing BPO for MSC's VS-127 scope; the Controller for FIN. |
| **Business SMEs** | Named per sub-domain (a buyer, a DC manager, a store manager, an AP clerk, a payroll officer) | ~5–10% each, 2–4 people per team | Consulted continuously on design; participate in UAT as first users; validate training content; feed pain points into the backlog. |
| **Change & Training Lead** | Shared pool under HR (Training) with CIO Office funding | ~0.25–0.5 FTE per team | Training curriculum and materials per release, adoption metrics, floor-walking for major rollouts — essential for 6,762 users of varying tech literacy across the archipelago. |

> These roles sit in their own §3.3 departments and are **not** counted in the 80-FTE IT
> sizing (§9). Their time commitments are agreed in each BPO's objectives, reviewed at the
> Quarterly Business Review.

### 5.3 Platform teams

| Platform Team | Members (§9) | Role & Responsibilities |
|---|---|---|
| **Integration & API Platform (IAP)** | Platform lead; 3 integration engineers; 1 events/monitoring engineer | Owns the integration backbone all domain teams consume: middleware/iPaaS, event streaming (near-real-time POS-to-ERP inventory sync), API standards and contracts, error handling and replay, integration monitoring dashboards. Owns the ~10 external integration clusters of `data-volumes-and-integrations.md` (payment gateways, banks, BIR eFPS, SSS/PhilHealth/Pag-IBIG, delivery partners, loyalty engine, WMS RF, supplier portal). Most engineering-heavy team. |
| **Cloud Infrastructure & SRE (INFRA)** | Lead; 2 cloud engineers; 1 network engineer; 1 SRE; 1 DBA/SaaS administrator | Uptime (POS 99.9%, back-office 99.5%), performance (POS transaction < 3s; standard reports < 30s), environment management, patch intake, DR/BCP execution (typhoon resilience, VS-26/VS-69), capacity planning for the 1,000–1,500 peak concurrent users (§15.3). |
| **Cybersecurity, Privacy & OT Security (SEC)** | Lead; 1 security engineer; 1 security analyst; 2 GRC/controls analysts | SOC liaison and monitoring (with managed-SOC partner), vulnerability management, penetration-test remediation, access reviews and SOD enforcement, RA 10173 privacy program support with the DPO (VS-91), OT/retail-tech security for POS terminals, RF guns, CCTV (VS-190), third-party risk assessments (VS-161). The GRC/controls analysts form the **enabling cell** that coordinates control design, test evidence, and audit responses across all product teams against the 808-control register. |
| **Data Platform & MDM (DP)** | Lead; 2 data engineers; 1 MDM stewardship lead; 1 BI platform administrator | Data warehouse and semantic layer; the item/customer/vendor/employee master-data platforms (55,000-SKU item master; ~600,000 loyalty members); CDP/identity resolution (VS-126); PIM/DAM (VS-137); AI/ML governance tooling (VS-128); process-mining platform (VS-133). Domain data analysts build on DP's certified layer; DP enforces the shared-object change process (§6.3). |
| **Field & End-User Services (FS)** | Supervisor; 2 helpdesk L2 analysts; 1 ITAM administrator; 5 regional field technicians (one per major island region: Mindanao, Visayas, South Luzon, Metro Manila, North/Central Luzon) | L1 (outsourced contact center) and L2 support for 200 stores, 4 DCs, and HQ; hardware lifecycle for the 600-terminal POS estate, RF guns, biometric devices, and printers (VS-99); store-visit SLAs and storm-season readiness stock. This team closes the archipelago field-support gap flagged in `headcount-reality-check.md` §3.2. |
| **CIO Office** | Head of Enterprise Architecture; 1 portfolio-governance lead; 1 FinOps/TBM analyst | Chairs the Architecture Review Board (VS-113); runs the Product Council secretariat and portfolio kanban; IT financial management and cloud FinOps (VS-135); innovation pipeline governance (VS-30). The CIO is counted in the Executive Office (§11.1), not in IT headcount. |

### 5.4 Role definitions (cross-team reference)

| Role | Definition |
|---|---|
| **Accountable (single-wielder) roles** | Each product has exactly one IT PO and one BPO. Each platform has exactly one lead. Single-point accountability mirrors the "single accountable owner" fix applied to VS-127. |
| **Matrixed integration analyst** | IAP integration engineers are matrixed ~0.4 FTE to each domain team as its touchpoint owner; they sit in domain ceremonies and hold the domain's integration health. |
| **Architect community** | The 7 product architects plus IAP/INFRA/SEC/DP leads form the Architecture Review Board quorum, chaired by the Head of EA. |
| **Escalation path** | L1 (outsourced) → FS L2 → domain functional analyst (config defects) or IAP (integration) or INFRA (platform) → PO → Product Council for prioritization conflicts. |

---

## 6. RACI

RACI key per [`WORKFLOW-FORMAT-GUIDE.md`](../01-model-company/workflows/WORKFLOW-FORMAT-GUIDE.md): **R** = Responsible, **A** = Accountable (exactly one per activity), **C** = Consulted, **I** = Informed.

### 6.1 Delivery activities (per domain team)

| Activity | IT PO | BPO | Architect | Functional Analyst | QA/Release | ARB |
|---|---|---|---|---|---|---|
| Product roadmap & backlog prioritization | A/R | C | C | C | I | I |
| Annual funding ask & capacity plan | A/R | C | C | I | I | I |
| Process design & fit-to-standard decision | C | A | R | R | I | C |
| Configuration change (within own domain) | A | C | C | R | C | I |
| Customization-exception request | R | C | R | C | I | A |
| UAT execution | R | A | I | C | R | I |
| Regression-pack maintenance | I | I | C | C | A/R | I |
| Production release (monthly train) | A | C | I | C | R | I |
| Post-release verification & adoption tracking | A | R | I | C | R | I |

### 6.2 Run & operate

| Activity | FS (L1/L2) | Domain Team | INFRA/SRE | SEC | BPO |
|---|---|---|---|---|---|
| P1 incident (e.g., store POS down) | R | A | R | C | I |
| P2/P3 incident & configuration defect | R | A | C | I | C |
| Root-cause analysis & problem record | C | A/R | C | C | I |
| Access request processing & SOD review | R | C | I | A | C |
| Vendor ERP release intake & regression | I | A/R | R | C | C |
| DR exercise (annual, pre-typhoon season) | R | C | A/R | C | I |
| New-store technology commissioning | R | A (SSP) | C | C | I |

### 6.3 Shared-object changes & controls

| Activity | Requesting Team | Owning Team | Platform (DP or IAP) | ARB |
|---|---|---|---|---|
| Item master / pricing object change | R | C | A (DP) | C |
| Chart-of-accounts segment change | R | C (FIN owns) | A (DP) | C |
| Customer master model change | R | C (CCP owns) | A (DP) | C |
| Integration contract change | R | C | A (IAP) | C |
| Control change touching Tier-1 workflows | R | A | C (SEC GRC cell) | I |

> For control changes, the SEC GRC cell validates design, the owning team's QA analyst
> validates test evidence, and Internal Audit is informed through the monthly Tier & Control
> Board (§7).

---

## 7. Governance Bodies

| Body | Cadence | Chair | Members | Decision Rights |
|---|---|---|---|---|
| **Product Council** | Monthly | CIO | 7 domain IT POs; BPOs or executive delegates (CFO/COO/CMO/CHRO offices); Head of EA; FinOps analyst (secretariat) | Capacity allocation between products (funding runs, not projects); roadmap approval above PHP 5M; cross-product priority conflicts; product KPI review; new-product creation or team split/merge recommendations |
| **Architecture Review Board (ARB)** | Bi-weekly | Head of EA | 7 product architects; IAP, INFRA, SEC, DP leads | Customization exceptions; new applications, integrations, or data pipelines; retirement of capabilities; waivers to the unified-ERP single-vendor principle (rare, CEO-noted) |
| **Product Sync** | Weekly | Rotating PO | Domain POs; platform leads; FS supervisor | Dependency sequencing; release-window coordination; matrixed-resource booking; incident-trend review |
| **Tier & Control Board** | Monthly | SEC GRC lead (senior analyst) | Domain QA/release analysts; Internal Audit liaison; Legal & Compliance liaison | Sign-off on changes touching Tier-1 workflows; audit-finding remediation tracking; annual control-test calendar against the 808-control register |
| **Quarterly Business Review (QBR)** | Quarterly | CIO with CEO/CFO/COO | Executive team; POs presenting their products | Outcome review against KPIs; funding continuation; BPO time-commitment health; structural adjustments (headcount reallocation between products) |

**Internal-audit independence:** the Tier & Control Board coordinates with Internal Audit &
Risk, which retains its Board Audit Committee reporting line per `model-company-profile.md`
§11.1 note 1 — the Board does not sit under the CIO.

---

## 8. Operating Cadence, Releases, KPIs & Funding

### 8.1 Cadence

| Rhythm | Activity |
|---|---|
| Continuous | Backlog refinement with BPO; incident and problem management; P2/P3 fixes |
| 2-week | Team build cycles: configuration, integration, and report work items; demo to BPO/SMEs |
| Monthly | Cross-product release train (see §8.2); Product Council; Tier & Control Board |
| Quarterly | Roadmap re-plan fed by S&OP/IBP outputs and seasonal calendar; QBR; funding reallocation |
| Annual | IT plan aligned to corporate budget; DR exercise before typhoon season; penetration test; control-test calendar refresh |

### 8.2 Release train

A single monthly cross-product release window, sequenced by Product Sync and executed by the
QA/release analysts, **avoiding the bi-monthly sale-event windows and the December peak**
(§13.2 seasonal calendar). Vendor ERP releases are intake-tested by INFRA and domain teams in a
staging ring before the train. Each release carries: regression evidence (Tier-1 coverage
mandatory), release notes for BPOs, updated training content, and a rollback plan.

### 8.3 Product KPIs (headline set)

| Team | KPIs (targets per `model-company-profile.md` §12.3/§15.3) |
|---|---|
| SSP | POS uptime ≥ 99.9%; transaction processing < 3s; offline continuity ≥ 8h; store-critical incident MTTR; price-label sync accuracy |
| MSC | Forecast accuracy and bias (S&OP); automated ROP release adoption; vendor-scorecard data freshness |
| WLI | Inventory accuracy ≥ 97%; RF transaction success rate; DC throughput report freshness; transfer-order cycle time |
| CCP | BOPIS 4-hour pick SLA; order-routing success rate; ecommerce uptime; catalog data completeness |
| FIN | Month-end close ≤ 5 working days; 3-way-match automation rate; BIR filing timeliness (zero penalties) |
| PEO | Payroll accuracy and on-time runs (semi-monthly, 5 entities); statutory remittance accuracy |
| CORP | Permit/renewal tracking completeness; GRC platform adoption; audit-finding closure rate |
| IAP | Integration availability; event-streaming latency (inventory sync near-real-time, < 30s per POS-013); contract coverage |
| INFRA | POS 99.9% / back-office 99.5%; report generation < 30s; DR RTO/RPO met in exercises |
| SEC | Vulnerability SLA compliance; access-review completion; privacy DSAR turnaround; zero material incidents |
| DP | Master-data quality scores (item/customer/vendor); dashboard freshness; AI-model governance coverage |
| FS | First-contact resolution; regional store-visit SLA; POS terminal MTTR; asset-register accuracy |

### 8.4 Funding model

- **Persistent capacity funding**: each product receives an annual envelope sized at Product
  Council and re-allocatable quarterly at the QBR — no project-based funding for steady-state
  work.
- **Central surge pool** (CIO Office): a small bucket for statutory mandates that land on any
  team (e.g., BIR e-invoicing readiness, eFPS form changes), protecting team capacity plans.
- **Innovation fund** (VS-30): competitive bids presented at the Product Council; prototypes
  run through the ARB before production.
- **FinOps discipline** (VS-135): the FinOps analyst reports cloud/SaaS spend per product at
  every QBR, tagging 100% of spend to products.

---

## 9. Sizing & Headcount Reconciliation

### 9.1 Steady-state design (80 IT FTE)

| Team | PO | Architect | Functional Analysts | Engineer | Data Analyst | QA/Release | Platform Roles | Total |
|---|---|---|---|---|---|---|---|---|
| MSC | 1 | 1 | 3 | — | 1 | 1 | — | 7 |
| WLI | 1 | 1 | 3 | — | 1 | 1 | — | 7 |
| SSP | 1 | 1 | 4 | — | 1 | 1 | — | 8 |
| CCP | 1 | 1 | 2 | 1 | 1 | 1 | — | 7 |
| FIN | 1 | 1 | 4 | — | 1 | 1 | — | 8 |
| CORP | 1 | — (¹) | 2 | — | — (¹) | 1 | — | 4 |
| PEO | 1 | 1 | 2 | — | 1 | 1 | — | 6 |
| **Domain subtotal** | 7 | 6 | 20 | 1 | 6 | 7 | — | **47** |
| IAP | — | — | — | — | — | — | lead 1 + integration 3 + events 1 | 5 |
| INFRA | — | — | — | — | — | — | lead 1 + cloud 2 + network 1 + SRE 1 + DBA 1 | 6 |
| SEC | — | — | — | — | — | — | lead 1 + engineer 1 + analyst 1 + GRC 2 | 5 |
| DP | — | — | — | — | — | — | lead 1 + data eng 2 + MDM 1 + BI admin 1 | 5 |
| FS | — | — | — | — | — | — | supervisor 1 + L2 2 + ITAM 1 + field techs 5 | 9 |
| CIO Office | — | — | — | — | — | — | Head of EA 1 + portfolio 1 + FinOps 1 | 3 |
| **Platform + CIO subtotal** | | | | | | | | **33** |
| **Total** | | | | | | | | **80** |

> (¹) CORP is covered by the FIN architect (dotted line) and uses FIN/DP analysts for its
> reporting needs; its GRC-tooling work is co-delivered with the SEC GRC cell.

### 9.2 Reconciliation to the current state and benchmarks

| Reference | Figure | Source |
|---|---|---|
| Current IT department | 50 | `model-company-profile.md` §3.3 |
| Gap-record need band | 65–80 | `headcount-reality-check.md` §3.2 (table row "Information Technology") |
| Industry benchmark | 100–168 (1.5–2.5% of 6,762 headcount); lean outsourced floor ~60–70 | `headcount-reality-check.md` §3.2 |
| This design | 80 (top of the need band; below industry benchmark) | §9.1 |

The design lands at the top of the gap-record band deliberately: the additional mass over the
~60–70 lean floor is concentrated exactly where the gap record flagged failures — archipelago
field coverage (FS), the integration backbone for near-real-time POS/ecommerce sync (IAP), and
the security/privacy regulatory load (SEC). Remaining lean relative to the 100–168 benchmark
is viable because the single-vendor SaaS model transfers DBA, OS, and availability operations
to the ERP provider, and L1 support plus the 24/7 SOC are partner-operated.

### 9.3 Phased build-up (50 → 80)

| Phase | Focus | Net adds | End state |
|---|---|---|---|
| **Phase 0 — Reorganize (next 2 quarters)** | Stand up the 12 teams, name POs/BPOs, adopt single backlogs, Product Council/ARB/Product Sync cadence; fill IAP lead + INFRA lead + FS supervisor from existing staff | +3 | ~53 |
| **Phase 1 — Field & integration first** | FS regional field technicians and L2; IAP integration engineers; SEC lead + engineer | +17 | ~70 |
| **Phase 2 — Data & domain depth** | DP data engineers/MDM; remaining functional-analyst depth in SSP/FIN/MSC; second GRC analyst; FinOps analyst | +10 | 80 |

---

## 10. Adoption Notes

- **Day-1 artifacts per team**: product charter (mission, KPIs, VS coverage from §4), current
  backlog seeded from the workflow gap analysis
  ([`workflow-gap-analysis.md`](../01-model-company/workflows/workflow-gap-analysis.md)),
  named BPO/SME roster, regression inventory mapped to Tier-1 workflows.
- **Anti-patterns to avoid**: project-style exception lanes around the backlog; BPO delegated
  to a junior analyst (the BPO must be the process owner); customization approved outside the
  ARB; domain teams building private integrations outside IAP; per-team data marts outside DP.
- **Split/merge triggers** (reviewed at QBR): a team sustaining > 25% overflow demand for two
  consecutive quarters is a split candidate (first candidate if growth continues: SSP store
  execution vs store-adjacent services); a team below 60% utilization for two quarters is a
  merge candidate.

## 11. Related Documents

| Document | Relationship |
|---|---|
| [`model-company-profile.md`](../01-model-company/model-company-profile.md) | Departments (§3.3), org chart (§11.1), performance targets (§12.3/§15.3), ERP landscape (§14) |
| [`workflows/value-stream-index.md`](../01-model-company/workflows/value-stream-index.md) | The 188-VS / 569-PA / 5,363-WF catalog this model assigns to products |
| [`workflows/workflow-criticality-classification.md`](../01-model-company/workflows/workflow-criticality-classification.md) | Tier 1/2/3 register driving regression coverage and SLAs |
| [`internal-controls-matrix.md`](../01-model-company/internal-controls-matrix.md) | 808-control register governed via the Tier & Control Board |
| [`headcount-reality-check.md`](../01-model-company/headcount-reality-check.md) | §3.2 IT staffing gap record this sizing resolves |
| [`erp-requirements.md`](../01-model-company/erp-requirements.md) | Capability requirements the products deliver |
| [`technical-guidelines.md`](technical-guidelines.md) | Infrastructure, integration, and security reference underpinning the platform teams |
| [`data-volumes-and-integrations.md`](../01-model-company/data-volumes-and-integrations.md) | Transaction volumes and integration touchpoints owned by IAP/INFRA |

---

*Document Version: 1.1 | Date: 2026-09-02 | Consistency review #68: §5.3 IAP integration-cluster
count trued to the canonical integration architecture (the `data-volumes-and-integrations.md`
§2 diagram and §3 detail matrix carry **ten** external clusters; was stated one high), and the
§8.2 release-train profile cross-reference re-pointed to **§13.2**, the Seasonal Calendar
section (was §13.3, Promotional Strategy). This document is now under the permanent regression
guard of `audit-model-docs.py` (validator Check 59). Prior v1.0 (2026-09-01): initial issue.
Defines the 12-product IT operating
model (7 stream-aligned domain teams + IAP/INFRA/SEC/DP/FS platform teams + CIO Office) with
full 188-VS assignment (§4.9 reconciliation: 171 domain + 17 platform = 188 VS; 4,864 + 499 =
5,363 workflows, matching the value-stream index grand totals), standard team membership and
role definitions (§5), RACI (§6), governance bodies (§7), cadence/funding (§8), and an 80-FTE
steady-state sizing (§9) reconciled to the §3.3 current IT headcount of 50, the
`headcount-reality-check.md` §3.2 need band of 65–80, and the 100–168 industry benchmark —
built up 50 → 80 in three phases. All figures quoted from `model-company-profile.md`,
`headcount-reality-check.md`, and `workflows/value-stream-index.md` as of their current
versions.*
