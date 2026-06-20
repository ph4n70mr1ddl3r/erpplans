# Workflow Criticality Classification

> Classifies 2,297 unique operational workflows into criticality tiers (the confirmed register
> holds 2,320 rows, of which 23 are `###` parent/summary sub-workflows double-counted against
> a `##` parent). An additional 2,684 workflows (4,981 total − 2,297 classified) remain
> unclassified pending review — all 2,684 carry a keyword-driven proposed tier in
> [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (regenerated via
> `07-methodology/classify-workflows.py`).
>
> **Layout note:** each tier's workflows are split into the original register (`## Tier N`) and a
> later `### Tier N Additions` batch added in subsequent review passes; the per-tier counts in the
> section headings and the [`## Summary`](#summary) table include both batches.
>
> Back to [Workflow Index](README.md)

---

### Operational Criticality Tiers

| Criticality Tier | Label | Description | Operational Dependency |
|---|---|---|---|
| **Tier 1** | Core Operations | Revenue-critical, core operations, legal compliance | Hard dependency (business cannot function without) |
| **Tier 2** | Standard Support | Standard support workflows, cost controls | Soft dependency (business experiences operational friction without) |
| **Tier 3** | Advanced Optimization | Advanced analytics, optimization, automation | Enhancement only (improves efficiency) |

### Classification Rules

1. **Must Have requirements** (431) are overwhelmingly Tier 1, with exceptions for requirements that only apply at scale (e.g., across all 200 stores rather than pilot 5)
2. **Should Have requirements** (296) are split between Tier 1 (operational necessities) and Tier 2
3. **Nice to Have requirements** (6) are Tier 3
4. Domain-specific workflows (governance, audit, ESG, innovation) are classified by their operational impact
5. Master data governance workflows are classified by dependency — foundational masters (item, customer, vendor, location) are Tier 1; advanced masters (planogram, loyalty config, digital assets) are Tier 2
6. Store-level daily operational workflows (safety checks, compliance, cash management, closings) are Tier 1
7. Customer-facing estimation/advisory services (material calculators, design consultations) are Tier 2 or Tier 3 based on revenue criticality

---

## Tier 1: Core Operations (672 Workflows)

These 440 workflows are foundational to daily store and supply chain operations.
Failure in any of these workflows would disrupt store operations or legal compliance.

### Core Finance (30 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W7 | AP — Vendor Invoice Processing | 6,715+ invoices/month; 3-way match is a must-have |
| W7C | Non-PO / Recurring Expense Invoice Processing | Recurring vendor payments must continue |
| W7D | AP Vendor Statement Reconciliation | Month-end AP integrity |
| W8 | AR — Trade & Corporate Accounts | 5,200 AR accounts; B2B revenue collection |
| W9 | Financial Close & Reporting | Under CREATE Law / PFRS requirements |
| W9A | Month-End Close | 5-day close SLA |
| W9B | Year-End Close | Statutory auditing dependency |
| W21 | Capex Request & Approval | Capital budgeting & controls |
| W24 | Trade & Corporate Credit Application | Credit risk mitigation |
| W25 | Petty Cash Management | Controls cash across 205 locations |
| W26 | Annual Budget Preparation | Cost controls |
| W30 | Treasury & Cash Management | Sweep cash; ensure liquidity |
| W59 | Insurance Policy Lifecycle | Risk mitigation |
| W74 | Employee Expense Reimbursement | Expense processing |
| W76 | Employee Loans & Advances | Loan management |
| W89 | Bank Reconciliation | Daily/weekly bank matching |
| W90 | Monthly Tax Filing & Statutory Remittance | BIR compliance |
| W94 | Customer Deposit & Advance Payment Management | Deposit tracking |
| W99 | Payment Settlement Reconciliation (Card/E-Wallet/Online) | Payment integrity |
| W100 | Vendor Statement Reconciliation | Vendor relationship |
| W101 | Customer Refund & Credit Processing | BIR-compliant credit notes |
| W108 | Customer Credit Collection & Escalation | Collection for 5,200 accounts |
| W260 | BIR eFPS Filing & Electronic Payment Submission | Mandatory BIR filing |
| W261 | E-Wallet & Digital Payment Settlement Reconciliation | GCash/Maya reconciliation |
| W423 | AR Post-dated Check (PDC) Warehousing & Clearing | Critical for B2B revenue collection in PH |
| W424 | AP Post-dated Check (PDC) Issuance & Monitoring | Critical for lease/rent payments to PH malls |
| W425 | Bounced Check (DAIF/DAUD) Recovery & Penalty | Financial/legal risk management in PH |
| W473 | BIR Electronic Invoicing System (EIS) API Transmission & Reconciliation | Mandatory real-time e-invoicing transmission to BIR for large taxpayers |
| W475 | Customer Creditable Withholding Tax (CWT) Certificate (BIR 2307) Collection & Reconciliation | B2B cash clearing and BIR corporate income tax credit reconciliation |
| W478 | BIR Annual Inventory List Submission (RMC 57-2015) | Mandatory annual inventory list reporting to BIR |

### Core Inventory (14 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W4 | Store Replenishment (DC → Store) | ~5,000 replenishment orders/month |
| W4B | Store-Initiated Replenishment Request | Store-level demand signal |
| W6 | Cycle Counting & Inventory Accuracy | Weekly counts; ≥97% accuracy target |
| W22 | Stock Transfers (Store-to-Store & Inter-DC) | Multi-location transfers |
| W22A | Store-Level Outbound Transfer Fulfillment | Transfer execution |
| W22B | Store-to-DC Return (Excess/Damaged) | Reverse logistics |
| W42 | Annual Physical Inventory Execution | Annual wall-to-wall count |
| W56 | Customer Backorder Management | Customer order fulfillment |
| W91 | Damaged & Defective Goods Disposition | Inventory quality |
| W92 | Inventory Adjustment & Shrinkage Authorization | Shrinkage control |
| W105 | Multi-Channel Inventory Allocation & Priority Governance | Channel reservation rules |
| W204 | Regional Stock Rebalancing & Inter-Store Expedited Transfers | Regional optimization |
| W214 | Store-to-Store Expedited Transfers (Customer-Initiated) | Customer service |
| W219 | Store Inventory Quarantine & Recertification | Quality control |

### Core Procurement (13 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W2 | Procurement — Purchase Order Cycle | Parent workflow |
| W2A | Auto-Replenishment (Stocking Items) | 1,200+ POs/month auto-generated |
| W2B | Import Purchase Orders | 40% of COGS; LC, customs, landed cost |
| W2C | Blanket / Contract Purchase Orders | Annual supply agreements |
| W36 | Vendor Onboarding | 800–1,000 active vendors |
| W38 | Special Order / Non-Stock Item Fulfillment | Customer special orders |
| W44 | Vendor Performance Review | Vendor management |
| W60 | Emergency Procurement | Urgent purchasing |
| W62 | Vendor Contract Lifecycle (Non-PO Contracts) | Contract management |
| W88 | Return to Vendor (RTV) Processing | Defective/wrong item returns |
| W136 | Indirect / Non-Merchandise Procurement | Non-merch POs |
| W244 | Vendor Invoice Dispute & Discrepancy Resolution | AP dispute resolution |
| W328 | Customer Credit Limit Periodic Review | Annual credit risk reassessment |

### Core Warehouse (7 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W3 | Warehouse Receiving & Putaway | DC core operation |
| W3B | Yard & Outdoor Inventory Management | Lumber/building materials |
| W3C | DC Inbound Delivery Scheduling | Inbound coordination |
| W46 | Kit / Bundle Assembly & Disassembly | Kit operations |
| W106 | DC Outbound Dispatch & Load Planning | Outbound coordination |
| W188 | Fleet Spare Parts & Preventive Maintenance | Fleet readiness |
| W270 | Pallet & Returnable Transport Packaging (RTP) Tracking | Pallet management |

### Core POS & Store Operations (23 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W5 | Daily Store Operations | Parent workflow |
| W5A | Store Opening | Daily opening procedure |
| W5B | In-Store Selling | 2.8M transactions/month |
| W5D | In-Store Customer Delivery Scheduling | Bulky item delivery |
| W5E | Store Opening Delay Procedure | System-down protocol |
| W5F | Store Closing & End-of-Day | Cash reconciliation for 200 stores |
| W5G | Offline POS Recovery & Reconciliation | Must sell during outages |
| W12 | Returns & Exchanges | Parent workflow |
| W12A | In-Store Returns | Customer-facing returns |
| W12B | Online-Initiated Returns | Omnichannel returns |
| W12C | Cross-Store Returns | Cross-store return processing |
| W18 | Direct Store Delivery (DSD) Receiving | 30% of goods by value |
| W18B | DSD Vendor Delivery Scheduling | DSD coordination |
| W33 | Warranty Claim Processing | Customer warranty |
| W109 | Store-Level Inventory Receiving & Putaway | Store receiving |
| W330 | In-Store Emergency Response Protocol | Safety compliance (RA 11058) |
| W432 | Solo Parent Discount Compliance (RA 11861) | PH Legal requirement for checkout |
| W438 | Yard Dispatch & Customer Vehicle Loading Operations | Critical for bulky material pickup |
| W537 | POS Card Terminal & Acquirer Settlement Operations | Card settlement — 36% of POS transactions; financial integrity |
| W538 | POS Real-Time Loss Prevention Exception Monitoring & Alert Response | Real-time LP monitoring; fraud/theft prevention |
| W540 | POS BIR Invoice Reprint, Adjustment & Credit Note Issuance | BIR-compliant credit note issuance; statutory requirement |
| W541 | POS Cash Office Operations & Bank Deposit Preparation | Cash office close; bank deposit accuracy for 200 stores |
| W553 | POS Pricing Error Detection & Immediate Correction at Checkout | DTI compliance; price accuracy enforcement at checkout |

### Core Merchandising & Pricing (2 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W13 | Promotions & Pricing Execution | Must Have POS-014 (promo auto-apply), ECOM-002 (price sync); without it POS cannot auto-apply promotions |
| W40 | Regular Price Change Execution | Must Have POS-010 (quantity breaks), ECOM-002 (price sync); stores cannot adjust prices post-go-live |

### Core Ecommerce (7 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W11 | BOPIS Order Fulfillment | ~25,700 orders/month |
| W19 | Home Delivery Fulfillment | ~17,200 orders/month |
| W19B | Ship from Store | Omnichannel fulfillment |
| W98 | Ecommerce Order Exception & Cancellation Management | Order exceptions |
| W215 | Customer Home Delivery Reverse Logistics (Returns) | Delivery returns |
| W246 | Drop-Ship Vendor (DSV) Order Fulfillment | Drop-ship orders |
| W247 | BOPIS Smart Locker & Queue Management | Smart locker pickup |

### Core HR & Payroll (6 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W10 | Payroll Processing | 6,757 employees; 5 entities × 2 runs/month |
| W15 | Recruitment & Employee Onboarding | ~1,200–1,600 hires/year |
| W34 | Store Shift Scheduling | Store workforce management |
| W43 | Employee Separation & Offboarding | Offboarding compliance |
| W251 | Philippine Statutory Benefits & Claims Administration | SSS, PhilHealth, Pag-IBIG |
| W280 | Court-Ordered Wage Garnishment & Third-Party Deductions | Legal compliance |

### Core Supply Chain (5 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W31 | Demand Forecasting Cycle | Drives replenishment |
| W32 | Seasonal Buy Planning | Seasonal procurement |
| W133 | S&OP Cycle | Sales & operations planning |
| W144 | International Logistics & Import Operations | Import operations |
| W250 | Supply Chain Control Tower & Real-Time Shipment Visibility | Shipment visibility |

### Core Compliance & IT (29 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W37 | Loss Prevention & Exception Reporting | POS fraud detection |
| W48 | IT Operations & Helpdesk Support | IT support |
| W53 | Data Privacy Breach Response | RA 10173 compliance |
| W54 | LGU Business Permit Renewal per Location | 200+ local permits |
| W55 | IT Disaster Recovery & System Failover | Failover preparedness |
| W131 | IT Asset Lifecycle Management | Asset tracking |
| W132 | Software Development & Change Management | ERP change management |
| W152 | Employee IT Provisioning & Access Lifecycle Management | Identity & access management |
| W158 | Business Continuity Drill & Disaster Recovery Testing | DR drills |
| W257 | Enterprise API & Systems Integration Lifecycle Management | Integrations management |
| W265 | POS Terminal Hardware Maintenance & Peripheral Management | POS terminal uptime |
| W266 | Ecommerce Online Fraud Detection & Prevention | Fraud block |
| W267 | Ecommerce Digital Payment Reconciliation & Dispute Handling | payment integrity |
| W271 | Data Subject Access Requests (DSAR) Lifecycle Management | RA 10173 DSAR |
| W366 | Network Infrastructure & Connectivity Management | Connectivity for 200+ sites |
| W368 | Database & Cloud Infrastructure Management | ERP performance & integrity |
| W375 | Privileged Access Management (PAM) Operations | Admin access security |
| W377 | Domain, SSL & Digital Certificate Management | Web & API uptime |
| W380 | IT Alert & Event Management | Proactive ops monitoring |
| W460 | Corporate & Trade Account Onboarding | B2B onboarding is revenue-critical for trade/corporate segment |
| W461 | Intercompany Fulfillment & Logistics Fee Settlement | IC settlement between 5 entities |
| W463 | Catch-Weight & Cut-to-Length Processing | Must Have POS-016; critical for hardware retail (lumber, wire, bulk) |
| W464 | In-House Customs Brokerage & Port Operations | Import operations (40% of COGS) |
| W467 | Specialized Hardware Permits (DENR, FPA) | Mandatory regulatory compliance for chemical/fertilizer products |
| W476 | LGU / BFP Fire Safety Inspection Certificate (FSIC) Management | Mandatory for business permit renewal and fire safety compliance |
| W477 | DENR Permit to Operate (PTO) & Wastewater Discharge Permit (WDP) Compliance | Mandatory for standby generator sets and wastewater discharge compliance |
| W479 | FDA License to Operate (LTO) for Household Hazardous Substances Compliance | Mandatory for selling paint, chemical-based goods, and solvents in PH |
| W480 | CAAP Height Clearance Permit Compliance | Mandatory CAAP clearances for store structures/signage near aerodromes |
| W54A | BIR Computerized Accounting System (CAS) Registration | Mandatory BIR CAS permit per entity/location; legal prerequisite for POS invoice/receipt numbering and books-of-accounts generation |

### Core Master Data Governance (16 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W252 | Centralized Item Master Creation & Governance | 55K SKUs; single source of truth |
| W253 | Customer Master Data Governance & Deduplication | 600K+ customer records |
| W254 | Location Master Lifecycle & Hierarchy Management | 200 stores + 4 DCs + HQ |
| W287 | Vendor Master Data Governance & Deduplication | 800–1,000 vendors |
| W288 | Financial Master Data Governance (COA & Cost Centers) | GL and cost center governance |
| W289 | Pricing Master Governance (Base Prices & Matrices) | Pricing control |
| W291 | Master Data Quality Monitoring & Reporting | Data quality |
| W293 | Tax & Regulatory Master Data Governance | BIR tax codes |
| W294 | Unit of Measure (UOM) Master & Conversion Management | Critical for catch-weight |
| W308 | Fiscal Calendar & Posting Period Master Governance | Period control |
| W309 | Bank & Banking Partner Master Governance | Bank master records |
| W311 | Barcode, GTIN & Item Identification Master Governance | Must Have POS-003, ECOM-009, MDM-020; barcode assignment at SKU creation is go-live critical |
| W312 | Replenishment & Planning Parameter Master Governance | Must Have MDM-021; direct dependency for Phase 1 W2A (auto-replenishment) and W4 (store replenishment) |
| W399 | Fixed Asset Master Data Governance | Asset categorization and tracking rules |
| W404 | POS System & Hardware Master Governance | POS terminal and peripheral metadata rules |
| W405 | Data Privacy & Consent Preferences Master Governance | Customer privacy preferences master records |

### Core Reporting (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W35 | Management Reporting Rhythm | Daily/weekly/monthly reporting |
| W113 | Business Intelligence & Data Governance | BI platform |
| W231 | Management Performance Reporting (QBR) | Executive reporting |
| W326 | Treasury Month-End Close & Reconciliation | Treasury operations |

---

## Tier 2: Standard Support (1,258 Workflows)

These 499 workflows are needed for standard operational support, cost controls, and category management.

### Merchandising & Pricing (15 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W1 | Merchandise Planning & Assortment Review | Strategic planning; not Day 1 |
| W27 | Vendor Rebate Accrual & Settlement | Vendor negotiation outcome |
| W50 | Product Information Management (PIM) | Content richness post-go-live |
| W63 | Shelf Label & Price Tag Distribution | Operational efficiency |
| W64 | New Product Pilot / Store Test | Innovation |
| W68 | Product Lifecycle & Discontinuation | Lifecycle management |
| W93 | Markdown & Clearance Pricing Execution | Seasonal clearance |
| W97 | Sample & Demo Inventory Management | Separate tracking |
| W102 | Category Performance Review & P&L Ownership | Category analytics |
| W107 | Pricing Hierarchy Governance & Compliance Audit | Pricing governance |
| W129 | Private Label / In-house Brand Development | PL lifecycle |
| W130 | Competitor Price Intelligence Gathering | Market intelligence |
| W181 | Store-Level Price Tag Printing & Verification | Store execution |
| W262 | Store Promotional Setup & Visual Merchandising Execution | Promotional execution |
| W329 | Competitive Price Tactical Response | Tactical pricing |

### Extended Inventory (6 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W23 | Consignment Inventory Operations | Vendor-owned stock management |
| W57 | Promotional Stock Allocation & Pre-Positioning | Promo stock allocation |
| W154 | Proactive Store Inventory Rebalancing (Stock Push) | System-suggested rebalancing |
| W218 | Inter-DC Stock Rebalancing (Stock Push) | DC-to-DC rebalancing |
| W220 | Slow-Moving & Obsolete Inventory (SLOB) Provisioning & Liquidation | SLOB management |
| W439 | In-Store Bulk-to-Retail Repackaging Operations | Bulk-to-retail conversion for hardware items |

### Extended Procurement (10 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W20 | Vendor Managed Inventory (VMI) | VMI for 12 key vendors |
| W62B | 3PL / Delivery Partner Onboarding & Offboarding | 3PL management |
| W110 | Supplier Quality & CAPA | Quality management |
| W115 | Supplier Diversity & MSME Development Program | MSME program |
| W150 | Product Quality Testing & Certification | Quality testing |
| W155 | Vendor Strategic Collaboration & Joint Business Planning | JBP |
| W160 | Private Label Factory Audit & Social Compliance | PL factory audit |
| W161 | Vendor Price Protection & Market Markdown Claims | Price protection |
| W245 | Vendor Performance Chargebacks & Penalties Management | Penalty management |
| W422 | VMI Collaborative Data Sharing & Replenishment Execution | VMI data collaboration |

### Extended Warehouse (3 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W52 | Fleet Management | Fleet admin |
| W66 | Inter-Island Logistics & Freight Management | Inter-island coordination |
| W221 | Cross-Docking Operations for Fast-Moving Bulky Items | Cross-dock optimization |

### Extended Store Operations (32 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W16 | New Store Opening | Store expansion (10–15/year) |
| W17 | Customer Loyalty Program Operations | Loyalty at POS |
| W28 | Gift Card & Store Credit Lifecycle | Gift card operations |
| W29 | Product Recall Execution | Recall management |
| W45 | Store Closure / Relocation | Store lifecycle |
| W47 | Store Facility Maintenance & Work Orders | Maintenance management |
| W67 | Monthly Store Performance Review | Store analytics |
| W69 | Price Compliance Audit | Price compliance |
| W71 | Store Physical Security & Access Control | Security management |
| W75 | Layaway / Installment Sales | Layaway operations |
| W86 | Planogram Compliance & Store Layout Verification | Planogram compliance |
| W96 | Store Renovation & Remodel Project | Renovation management |
| W111 | Store Energy & Utility Consumption Management | Energy monitoring |
| W470 | Store-Level Rotational Brownout / Power Outage Management Protocol | Power outage operational readiness |
| W471 | Store-Level Security Incident & Police/Barangay Reporting Protocol | Store-level security & legal incident reporting |
| W170 | Senior Citizen & PWD Discount Compliance (PH Legal) | SC/PWD compliance |
| W171 | Store Physical Security & Yard Patrol Routine | Security routine |
| W176 | Store-to-DC Reverse Logistics (Consolidation) | Reverse logistics |
| W205 | Employee Purchase Program & Internal Staff Sales | Employee purchases |
| W248 | Store Inventory Variance & LP Investigation | Variance investigation |
| W278 | Mid-Day Cash Skimming / Till Sweeps | Cash management |
| W428 | Community Disaster Relief & Emergency Response | "Critical Infrastructure" role during PH disasters |
| W445 | Display & Demo Infrastructure Maintenance | Store display maintenance |
| W539 | POS Promotional Coupon, Voucher & Manufacturer Coupon Processing | Coupon/voucher acceptance and reconciliation |
| W542 | POS Quotation & Estimate Generation with Sales Conversion | Quotation-to-order conversion for trade customers |
| W543 | POS Consignment Sell-Through Transaction Processing & Vendor Settlement Trigger | Consignment sell-through processing and vendor settlement |
| W544 | POS Service Work Order Creation & Scheduling | Service work order management at POS |
| W545 | POS Special Order & Customer Order Processing | Special/customer order intake and tracking |
| W546 | POS Deposit & Progress Payment Collection for Project Orders | Project deposit collection and milestone payment tracking |
| W549 | POS Damaged & Open-Box Item Discount Processing | Damaged/open-box item markdown at POS |
| W550 | POS Loyalty Points as Payment Tender | Loyalty point redemption as payment method |
| W551 | POS Customer On-the-Spot Loyalty Enrollment & Account Lookup | Real-time loyalty enrollment during checkout |

### Extended Finance & Treasury (21 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W137 | Intercompany Dividend & Loan Management | IC financial management |
| W174 | Store-Level Cash-in-Transit (CIT) & Armored Car Management | CIT operations |
| W175 | Employee Gratuity & Retirement Fund Management (RA 7641) | Retirement management |
| W184 | Fixed Asset Physical Verification (Audit) | Asset verification |
| W217 | Senior Citizen & PWD VAT-Exemption Audit & Reporting | SC/PWD reporting |
| W232 | LC & Bank Guarantee Lifecycle | LC management |
| W233 | Cash Flow Forecasting & Liquidity Management | Cash forecasting |
| W234 | Intercompany Profit Elimination & Consolidation | IC consolidation |
| W235 | Transfer Pricing Compliance & Documentation | TP compliance |
| W275 | IFRS 16 / PFRS 16 Lease Accounting & Modifications | Lease accounting |
| W276 | Asset Under Construction (AUC) & Mass Capitalization | AUC management |
| W277 | Freight Bill Audit & Payment (FBAP) Reconciliation | Freight cost control |
| W317 | Bank Account Lifecycle & Signatory Management | Bank account management |
| W472 | BOI/PEZA/LGU Tax Incentive Monitoring & Compliance | Tax incentive compliance and optimization |
| W319 | Debt Facility & Covenant Compliance Management | Debt management |
| W320 | Electronic Banking Security & Payment Control | Banking security |
| W321 | FX Exposure Analysis & BSP Regulatory Reporting | FX reporting |
| W322 | Treasury Policy, Governance & Risk Appetite Framework | Treasury governance |
| W323 | Cash Concentration & Inter-Entity Pooling Operations | Cash pooling |
| W327 | External Shareholder Dividend Declaration & Payment | Dividend management |
| W435 | Intercompany Service Level Agreement (SLA) Fee Billing | IC service fee governance |

### Extended HR (8 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W51 | Employee Training & Skills Development | Training programs |
| W72 | Employee Performance Management | Performance reviews |
| W172 | Employee PPE & Uniform Lifecycle | PPE management |
| W178 | Employee Succession & Internal Mobility | Succession planning |
| W179 | Management Trainee (Cadetship) Program | Trainee program |
| W269 | Vendor Promodizer & Third-Party Staff Management | Third-party staff |
| W429 | Vendor-Funded Promodizer Incentive Management | Conflict of interest & labor cost control |
| W449 | Promodizer Labor Compliance & DOLE 174 Governance | Co-employment risk management |

### Extended Supply Chain (5 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W183 | Supply Chain Network Optimization Review | Network optimization |
| W191 | Global Supply Chain — Incoterm & Marine Insurance Tracking | Incoterm management |
| W249 | Import Port Demurrage & Detention Management | Demurrage control |
| W268 | Last-Mile Home Delivery Tracking & Proof-of-Delivery | Last-mile tracking |
| W284 | Customs Bonded Warehouse (CBW) Operations & Duty Deferral | Bonded warehouse |

### Extended Ecommerce (2 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W180 | Ecommerce Marketplace Integration (Lazada/Shopee) | Marketplace expansion |
| W210 | Ecommerce Fulfillment Hub (Dark Store) Operations | Dark store |
### Customer Experience (11 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W41 | Customer Complaint Resolution | Complaint management |
| W58 | Corporate / Project Account Management | Project accounts |
| W61 | Competitor Price Match Process | Price matching |
| W65 | Customer Satisfaction Measurement | CSAT/NPS |
| W84 | Customer Account Reactivation | Dormant accounts |
| W87 | Customer Feedback-to-Action Loop | Feedback loop |
| W103 | Trade Sales Pipeline & Territory Management | Trade sales |
| W112 | Trade Counter / Pro Desk Operations | Trade counter |
| W156 | Customer Data Platform (CDP) & Hyper-Personalization | CDP |
| W258 | Omni-channel Customer Ticketing & Support Management | Customer ticketing |
| W259 | Call Center Daily Operations & Queue Management | Call center ops |

### Extended IT (23 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W367 | Cybersecurity Operations & Vulnerability Management | Proactive security posture |
| W369 | IT Vendor SLA Governance & Performance Management | Vendor service quality |
| W370 | Software License & SaaS Subscription Management | Compliance & cost control |
| W371 | Mobile Device Management (MDM) Operations | RF device readiness |
| W372 | IT Policy, Security Awareness & User Training | Human-factor security |
| W373 | IT FinOps & Cloud Cost Management | Cloud spend governance |
| W374 | IT Project Intake & Demand Management | IT resource alignment |
| W376 | IT Capacity & Performance Planning | Proactive scaling |
| W378 | IT Problem Management & Root Cause Analysis | Systemic issue elimination |
| W379 | IT Service Request Fulfillment & Service Catalog | Standard IT requests |
| W381 | IT Knowledge Management | Operational continuity |
| W384 | ERP Environment Management & Data Masking | Non-prod data security |
| W391 | Software Quality Assurance (QA) & Testing Lifecycle | Release quality & defect management |
| W392 | IT Service Level Management (SLM) & BRM | Business alignment & service uptime governance |
| W394 | IT Technical Skills, Training & Certification Lifecycle | IT team competency & succession |
| W395 | Mobile App Store Management (Public & Enterprise) | App release & mobility governance |
| W396 | ERP Data Archiving & Database Tiering Execution | ERP performance & storage cost control |
| W434 | NPC Annual DPO & System Registration | Mandatory data privacy compliance |
| W386 | IT Strategy & Annual Roadmap Development | IT strategic alignment |
| W387 | IT Compliance & Control Self-Assessment (CSA) | IT control validation |
| W388 | Shadow IT Discovery & Governance | Unauthorized IT risk mitigation |
| W389 | Data Privacy Impact Assessment (DPIA) Lifecycle | RA 10173 DPIA requirement |
| W390 | IT Service Continuity & BIA Refresh | Business continuity foundation |

### Compliance & Governance (19 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W49 | Natural Disaster / Typhoon Business Continuity | BC planning |
| W77 | BIR Tax Audit Response | BIR audit |
| W78 | Government / Institutional Procurement Participation | Government procurement |
| W79 | Employee Grievance & Whistleblower Process | Grievance management |
| W82 | Hazardous Waste Disposal Tracking & DENR Compliance | Hazmat compliance |
| W95 | External Audit Coordination & Support | External audit |
| W114 | Sustainability & Environmental Compliance Reporting | ESG reporting |
| W185 | Product Liability & Consumer Safety Incident Management | Product safety |
| W207 | Store-Level Security Camera (CCTV) Audit & LP Integration | CCTV audit |
| W209 | Barangay & Local Community Relationship Management | Community relations |
| W216 | BIR CAS Compliance Audit | BIR CAS audit |
| W469 | Customer Complaint DTI Escalation & Consumer Adjudication Management | DTI complaint adjudication case management |
| W285 | Public Liability & Customer Incident Claims Management | Liability claims |
| W426 | Annual Conflict of Interest (COI) & Gift Policy Disclosure | Corporate governance & fraud prevention |
| W427 | DTI Sales Promotion Permit Monitoring & In-Store Compliance | Regulatory fine avoidance |
| W433 | DENR Self-Monitoring (SMR) & Compliance (CMR) Reporting | Mandatory environmental reporting |
| W437 | Regulatory Branch De-registration & Permit Cancellation | Final regulatory closure procedure |
| W444 | Community Solicitation & Donation Processing | Community relations governance |
| W446 | Temporary LGU Permits for Outdoor Sales & Events | LGU compliance for promotional events |

### Facility & Asset Maintenance (3 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W240 | DC Facility & Warehouse Equipment Maintenance | DC maintenance |
| W241 | HQ Office Facility & Executive Asset Maintenance | HQ maintenance |
| W242 | 3PL & Logistics Partner Performance Review | 3PL performance |

### Extended Health & Safety (1 workflow)

| ID | Workflow | Operational Significance |
|---|---|---|
| W436 | Annual OHS Statutory Reporting (WAIR/AMR) | Mandatory safety compliance reporting |

### Extended Master Data (25 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W290 | Hierarchical Category Structure Management | Category management |
| W292 | Employee Master Data Governance & Cross-Entity Lifecycle | Employee master |
| W295 | Payment Terms & Settlement Rule Master Governance | Payment terms |
| W296 | Service & Non-Stock Item Master Governance | Service items |
| W297 | Warehouse Location & Bin Master Governance | Bin management |
| W298 | Product Attribute Template Master Governance | Attribute templates |
| W299 | Assortment & Store Cluster Master Governance | Assortment matrix |
| W300 | Promotional Rule & Campaign Master Governance | Promo rules |
| W301 | Reason Code & Disposition Master Governance | Reason codes |
| W302 | Kit/BOM & Bundle Structure Master Governance | Kit structures |
| W303 | Manufacturer/Brand Master Governance | Brand management |
| W304 | Routing, Carrier & Transit Time Master Governance | Routing |
| W305 | Intercompany Transfer Pricing Rule Master Governance | IC pricing |
| W306 | Seasonal Calendar & Event Master Governance | Seasonal calendar |
| W307 | Currency & Exchange Rate Master Governance | FX rate governance |
| W310 | Address & Geographic Hierarchy Master (Philippine-Specific) | PSGC codes |
| W313 | Loyalty Program Configuration & Rule Master Governance | Initial config pre-loaded; ongoing governance matures in Phase 2 |
| W314 | Planogram Template & Space Planning Master Governance | Planogram master |
| W315 | Product Lifecycle Status & Transition Rule Master Governance | Lifecycle master |
| W316 | Digital Asset & Product Content Master Governance | Digital asset master |
| W400 | Equipment & Asset Maintenance Master Governance | EAM equipment classification and tagging metadata |
| W401 | Fleet & Vehicle Master Governance | Logistics fleet registration and specifications metadata |
| W402 | Contract & Agreement Master Governance | Legal contract classification and metadata fields |
| W403 | Competitor & Market Intelligence Master Governance | Competitor profiles and pricing category structures |
| W406 | ESG & Sustainability Metrics Master Governance | Carbon emission factor and environmental indicators metadata |

### Other Phase 2 (22 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W116 | Site Selection & Feasibility Analysis | Real estate expansion |
| W117 | Lease Administration & Renewal | Lease management |
| W118 | Rent & CAM Payment Processing | Rent payments |
| W119 | Real Property Tax (Amillaramento) Management | Property tax |
| W162 | Project Quotation & Bid Management | Trade/project sales |
| W163 | Contract Pricing & Project Price Books | Project pricing |
| W164 | Staged Project Delivery & Call-Off Orders | Staged deliveries |
| W165 | Project Retention & Milestone Billing | Milestone billing |
| W166 | Corporate / Institutional Tendering | Tendering |
| W169 | Lumber & Board Cutting Services | Daily revenue-generating service; system-supported during wave rollout |
| W228 | Sales Commission Calculation | Commission management |
| W229 | B2B Customer Credit Limit Exception & Escalation | Credit exceptions |
| W421 | Batch/Shade Reconciliation for Large Project Sales | Shade consistency |
| W239 | Customs Duty & Tax Reconciliation (BOC) | Customs reconciliation |
| W255 | Electronic Document Storage & Retrieval (ERP-wide) | Document storage |
| W256 | Enterprise Document Retention & Archiving Policy | Document retention |
| W264 | Seasonal Merchandise Transition & Display Rotation | Seasonal transition |
| W279 | Product Substitution Rules & Governance | Substitution rules |
| W441 | Corporate Staff Housing & Billeting Management | Staff housing management |
| W238 | Hazmat Spill Response & Incident Management | Hazmat spill response |
| W430 | LGU Business Permit & "Amillaramento" (RPT) On-Site Inspection | Regulatory compliance for 200 sites |
| W431 | LGU-Specific "Truck Ban" & Route Governance | Delivery window & fine management |

---

## Tier 3: Advanced Optimization (390 Workflows)

These 229 workflows deliver advanced capabilities for competitive differentiation, AI-driven automation, and deep business analytics.

### Innovation & Digital Transformation (8 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W200 | AI-Driven Personalization & Recommendation Engine | AI capability |
| W201 | Robotic Process Automation (RPA) Lifecycle | RPA automation |
| W202 | Predictive Maintenance for Industrial Assets | Predictive capability |
| W203 | Computer Vision for Inventory & Planogram Audit | Computer vision |
| W208 | Retail Analytics & AI-Driven Inventory Optimization | Advanced analytics |
| W420 | AI Shelf Monitoring & Real-time Replenishment Alerting | AI shelf monitoring |
| W397 | Cyber Threat Intelligence & Proactive Threat Hunting | Advanced threat detection maturity |
| W398 | IT Innovation, Emerging Tech & PoC Lifecycle | Structured technology innovation |

### ESG & Sustainability (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W192 | GHG Emissions Tracking | Carbon tracking |
| W193 | Waste Management & Circular Economy | Waste management |
| W194 | Social Impact & Community Development (CSR) | Social impact |
| W195 | Sustainable Sourcing & Ethical Vendor Audit | Ethical sourcing |

### Marketing & Campaigns (13 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W83 | Campaign Planning, Execution & Performance Measurement | Full campaign lifecycle |
| W104 | Loyalty Program Financial Governance & Periodic Review | Loyalty financials |
| W134 | Crisis Communication & Brand Reputation Management | Crisis management |
| W135 | CSR Program Execution | CSR execution |
| W142 | Social Media & Influencer Management | Social media |
| W143 | Public Relations & Corporate Communications | PR management |
| W149 | Bank & Credit Card Partnership Management | Bank partnerships |
| W151 | CSR Impact Measurement & Reporting | CSR measurement |
| W153 | Retail Media Network (RMN) Operations | RMN operations |
| W189 | Referral Program & Brand Ambassador Management | Referral program |
| W190 | In-house Design & Creative Production Management | Creative production |
| W263 | Loyalty Member Enrollment & Onboarding Journey | Enrollment journey |
| W286 | RMN Vendor Billing & Yield Management | RMN billing |

### Corporate Governance & Strategy (8 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W124 | Corporate Secretarial & Entity Management | Corporate secretarial |
| W125 | Legal Case & Litigation Management | Litigation |
| W126 | Intellectual Property (IP) Portfolio Management | IP management |
| W127 | Annual Strategic Planning & OKRs | Strategic planning |
| W128 | Enterprise Project Management (EPM) Lifecycle | EPM |
| W186 | Internal SOP & Policy Governance Lifecycle | SOP governance |
| W230 | Legal Contract Review & Approval | Legal review |
| W474 | Enterprise Data Governance Council Operations | Data quality policy ratification and dispute arbitration |

### Internal Audit (42 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W120 | Internal Audit Planning & Risk Assessment | Audit planning |
| W121 | Operational Audit Execution (Store/DC/HQ) | Operational audit |
| W122 | Enterprise Risk Management (ERM) Review | ERM |
| W123 | Fraud Investigation Protocol | Fraud investigation |
| W159 | Anti-Bribery & Corruption Monitoring & Audit | ABC monitoring |
| W243 | POA & Board Resolution Lifecycle | POA management |
| W331 | ITGC & Cybersecurity Audit | ITGC compliance |
| W332 | Continuous Control Monitoring (CCM) | Real-time controls |
| W333 | Audit Issue Remediation & CAP Tracking | Findings lifecycle |
| W334 | Third-Party Vendor Risk Audit | External risk |
| W335 | Major Capex & Project Audit | Investment control |
| W336 | Quality Assurance & Improvement Program | IA quality |
| W337 | Payroll & Statutory Compliance Audit | Payroll integrity |
| W338 | Segregation of Duties (SOD) Review | Access governance |
| W339 | Regulatory Compliance Audit | Legal risk management |
| W340 | Unannounced Store Cash & Vault Audit | Retail cash control |
| W341 | ESG Assurance & Sustainability Compliance Audit | ESG audit |
| W342 | Inventory Observation & Cycle Count Audit | Inventory audit |
| W343 | Lease & CAM (Common Area Maintenance) Compliance Audit | Lease audit |
| W344 | Trade Promotion, Rebate & Marketing Spend Audit | Trade spend audit |
| W345 | Logistics, Fleet & Fuel Management Audit | Logistics audit |
| W346 | Capex Construction & Store Build-out Audit | Construction audit |
| W347 | E-commerce & Omni-channel Operations Audit | E-commerce audit |
| W348 | Revenue Assurance & Payment Gateway Audit | Revenue audit |
| W349 | Corporate Tax & Statutory Reporting Audit | Tax audit |
| W350 | BC/DR Readiness & Crisis Management Audit | BC/DR audit |
| W351 | External Audit Coordination & Statutory Filing Support | External audit support |
| W352 | Fixed Asset Verification & Audit | Fixed asset audit |
| W353 | Ethical Sourcing & Social Compliance Audit | Ethical sourcing audit |
| W354 | AML & Sanctions Screening (Wholesale/B2B) Audit | AML audit |
| W355 | Intellectual Property (IP) & Brand Protection Audit | IP audit |
| W356 | Whistleblower System & Non-Retaliation Audit | Whistleblower audit |
| W357 | Board Governance & MCG Compliance Audit | Governance audit |
| W358 | Physical Security, CCTV & Guard Force Audit | Physical security audit |
| W359 | AI Governance, Algorithmic Bias & Data Ethics Audit | AI governance audit |
| W360 | Crisis Response & Incident Management Audit | Crisis audit |
| W361 | Corporate Treasury, Cash Management & Investment Audit | Treasury audit |
| W362 | Master Data Governance & Data Quality Audit | MDM audit |
| W363 | Insurance Program & Claims Audit | Insurance audit |
| W364 | Marketing Agency & Media Spend Audit | Media spend audit |
| W365 | Strategic Workforce Planning & Succession Audit | Workforce audit |
| W466 | Loss Prevention & Asset Protection (LPAP) | LP operations audit |

### Advanced Store Operations (10 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W173 | Store-Level Solar Energy Monitoring | Solar monitoring |
| W177 | Vending & Concessionaire Management | Concessionaire |
| W182 | Gift / Home Registry Lifecycle | Gift registry |
| W206 | Mobile POS (mPOS) & Queue-Busting Operations | mPOS |
| W212 | Automated Store Cash Management & Smart Safe Integration | Smart Safe |
| W272 | Cashier Over/Short Dispute & Deduction Resolution | Cashier disputes |
| W281 | Self-Checkout (SCO) Exception & Intervention Management | SCO |
| W547 | POS Scan & Go / Mobile Self-Scan Checkout | Mobile self-scan checkout experience |
| W548 | POS Third-Party On-Demand Delivery Integration | On-demand delivery partner integration |
| W552 | POS Donation & Charity Round-Up Processing | Charity round-up at checkout |

### Services & Value-Added (6 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W138 | Home Installation Services Management | Installation services |
| W139 | Tool & Equipment Rental Operations | Tool rental |
| W147 | DIY Workshop & In-Store Event Management | Workshops |
| W148 | Home Design & Consultancy Services | Design consultancy |
| W168 | Custom Paint Mixing & Tinting Operations | Paint mixing |
| W211 | In-Store 3D Kitchen/Bathroom Design Rendering | 3D rendering |

### Wholesale & B2B (3 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W145 | Wholesale Reseller Onboarding & Credit Management | Wholesale channel |
| W146 | Bulk Fulfillment & Cross-Docking for Wholesale | Bulk fulfillment |
| W283 | B2B Punchout Catalog Integration (cXML) | B2B integration |

### Engineering & Construction (5 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W223 | New Store Design & Engineering Standards | Store design |
| W224 | Construction Bidding & Contractor Selection | Construction bidding |
| W225 | Store Construction Management & Supervision | Construction management |
| W226 | Store Renovation & Retrofitting (CAPEX) | Store renovation |
| W227 | Commissioning & Operational Handover | Commissioning |

### Fleet & Logistics (8 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W196 | Route Planning & Dispatch Optimization | Route optimization |
| W197 | Driver Performance & Safety Management | Driver management |
| W198 | Fuel Management & Consumption Monitoring | Fuel management |
| W199 | Fleet Telematics & Real-Time Tracking | Telematics |
| W1163 | 3PL & Delivery Partner Daily Operations Management | 3PL partner coordination |
| W1164 | Inter-Island Logistics Coordination & Shipping Management | Inter-island shipping |
| W1165 | Last-Mile Delivery Dispatch, Tracking & SLA Management | Last-mile delivery SLA |
| W1166 | Carrier Rate Management, Freight Audit & Cost Optimization | Freight cost management |

### Hazmat & Safety (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W141 | Workplace Safety Inspection & Audit | Safety inspection |
| W187 | Contractor & Third-Party On-site Safety Orientation | Contractor safety |
| W236 | Hazmat Storage & Segregation Compliance (DC) | Hazmat storage |
| W237 | Hazmat Handling & Safety Training (Store) | Hazmat training |

### Advanced Treasury (3 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W318 | Short-Term Investment & Surplus Cash Placement | Investment management |
| W324 | Supply Chain Finance & Dynamic Discounting Program | SCF program |
| W325 | Corporate Guarantee & Contingent Liability Management | Guarantee management |

### Advanced Master Data (7 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W222 | DC Container Yard & Chassis Management | Container yard |
| W273 | In-Store Endless Aisle & Vendor Direct-to-Customer Delivery | Endless aisle |
| W274 | Third-Party Customer Financing / Equipment Leasing | Customer financing |
| W440 | Power Tool Service & Repair Center Operations | Power tool service |
| W442 | Site Technical Survey & Measurement Services | Site survey service |
| W443 | Salvage & Scrap Material Disposition (Waste-to-Cash) | Salvage monetization |
| W465 | Network-Wide Disaster Recovery & BCP | Enterprise BCP governance |

### Advanced MDM, Services, and Other (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W157 | E-waste Collection & Circular Economy Operations | E-waste |
| W167 | Store & DC Recycling Program (Circular Economy) | Recycling |
| W213 | Installation Service Partner Quality Audit | Partner audit |
| W282 | Subscription Billing for Recurring Home Services | Subscription billing |

---

## Summary

### Confirmed classification (hand-reviewed)

| Phase | Label | Workflow Count | % of Classified |
|---|---|---|---|
| Phase 1 | Go-Live Critical (Tier 1) | 672 | 29.0% |
| Phase 2 | Operational Excellence (Tier 2) | 1,258 | 54.2% |
| Phase 3 | Innovation & Optimization (Tier 3) | 390 | 16.8% |
| **Confirmed Total** | | **2,320** | 100% |

> Counts include 23 `###` parent/summary sub-workflows (e.g. W5A/W9A/W54A) that receive their
> own classification row; the remaining 2,297 are canonical `##` workflows.

### Proposed classification (keyword-driven, pending human review)

The **2,684** workflows not yet in the confirmed register above have been assigned a *proposed*
tier by [`07-methodology/classify-workflows.py`](../../07-methodology/classify-workflows.py) using
conservative keyword rules; see the companion file
[`workflow-criticality-proposed.md`](workflow-criticality-proposed.md). On review, promote/demote
rows by moving them into the confirmed sections above.

| Phase | Label | Proposed Count |
|---|---|---|
| Phase 1 | Go-Live Critical (Tier 1) — proposed | 514 |
| Phase 2 | Operational Excellence (Tier 2) — proposed | 2,023 |
| Phase 3 | Innovation & Optimization (Tier 3) — proposed | 147 |
| **Proposed Total** | | **2,684** |

| Coverage | Workflows |
|---|---|
| Confirmed (hand-reviewed) | 2,320 rows (2,297 unique `##` workflows) |
| Proposed (keyword, pending review) | 2,684 |
| Without even a proposal | 0 |
| **Grand Total** | **4,981** unique `##` workflows (2,297 confirmed + 2,684 unclassified, all proposed) |

### Domain Breakdown

The per-tier subsection headings above (Core Finance, Extended Store Operations, Internal Audit, etc.) provide the authoritative domain-and-phase breakdown of the 1,168 classified workflows, and the [value-stream-index.md](./value-stream-index.md) provides the authoritative value-stream/process-area breakdown of all 4,981 workflows. A rolled-up "by domain" summary table was removed during consistency review because it could not be reconciled with the tier totals and presented stale partial counts.

> **2026-06-14 addition:** Value streams VS-79 through VS-88 (240 workflows, W2753–W2992) were added covering Tax Management & BIR Statutory Reporting, Payment Operations & Acquirer Settlement, Cash-in-Transit & Armored Car Operations, Sari-Sari Store & MSME Micro-Wholesale, Occupational Health & Employee Wellness, Labor Relations & Collective Bargaining, Mandatory Discount & Tax Credit Recovery, Anti-Financial Crime (AML/KYC/ABC), Customs Trade Compliance & Tariff Optimization, and Document Control & Records Retention. These 240 workflows are currently **unclassified** (counted in the unclassified total) pending criticality review; many warrant Tier 1 classification (BIR tax filing, AML/STR reporting, CBA administration, mandatory-discount tax credit recovery, CIT operations) and will be assigned in a follow-up classification pass.
>
> **2026-06-14 addition (gap analysis Pass 1):** Value streams VS-89 through VS-92 (96 workflows, W2993–W3088) were added to fill capability gaps identified in a workflow gap analysis: VS-89 Product Recall & Safety Corrective Action Management, VS-90 Damage, Claims & Freight Recovery Management, VS-91 Consumer Data Privacy & Data Protection Program, and VS-92 Kitting, Bundling & Build-to-Order Assembly Operations. These 96 workflows are currently **unclassified** (counted in the unclassified total) pending criticality review; several warrant Tier 1 classification (product recall regulatory notification/stop-sale, DPA breach NPC 72-hour notification, freight/vendor claim notice windows, DSAR statutory fulfillment) and will be assigned in a follow-up classification pass.
>
> **2026-06-14 addition (gap analysis Pass 2):** Value streams VS-93 through VS-96 (96 workflows, W3089–W3184) were added to fill the remaining retired-number gaps and two new capability gaps: VS-93 Dark Store & Micro-Fulfillment Operations (former VS-49 gap), VS-94 Cooperative & Community Enterprise Procurement (former VS-52 gap), VS-95 Marketplace Operator & Third-Party Seller Management, and VS-96 Equipment Leasing & Capital Equipment Finance. These 96 workflows are currently **unclassified** (counted in the unclassified total) pending criticality review; several warrant Tier 1 classification (marketplace seller KYB/payout, lease credit underwriting and Truth-in-Lending disclosure, dark-store dispatch SLA for ecommerce promise, cooperative fair-trade pricing) and will be assigned in a follow-up classification pass.
>
> **2026-06-14 addition (gap analysis Pass 3):** Value streams VS-97 through VS-100 (96 workflows, W3185–W3280) were added to strengthen the previously-thinnest operating families: VS-97 Corporate Real Estate & Property Portfolio Management, VS-98 Contingent, Contract & Outsourced Workforce Management, VS-99 IT Asset & Technology Lifecycle Management, and VS-100 Legal Operations, Litigation & IP Management. These 96 workflows are currently **unclassified** (counted in the unclassified total) pending criticality review; several warrant Tier 1 classification (intercompany rent transfer-pricing benchmarking, DOLE D.O. 174 labor-only-contracting compliance, software license compliance-audit response, litigation loss-contingency accrual under PFRS/IAS 37) and will be assigned in a follow-up classification pass.
>
> **2026-06-14 addition (gap analysis Pass 4):** Value streams VS-101 through VS-104 (96 workflows, W3281–W3376) were added to strengthen the three thinnest operating families (People +2; Plan & Source +1; Governance & Assurance +1): VS-101 Merchandise Financial Planning, OTB & Margin Management, VS-102 Compensation, Benefits & Total Rewards Strategy, VS-103 HR Shared Services, Employee Experience & People Analytics, and VS-104 Government Affairs, Public Policy & Industry Relations. These 96 workflows are currently **unclassified** (counted in the unclassified total) pending criticality review; several warrant Tier 1 classification (open-to-buy/markdown-budget governance, pay-equity analysis and minimum-wage compliance, multi-entity statutory-benefits remittance governance, political-activity/anti-bribery compliance in government affairs) and will be assigned in a follow-up classification pass.

---

## Previously Unclassified Workflows — Now Classified

> The following 681 workflows (previously listed as "additional batch workflows unclassified")
> have been classified by value stream context, process area, and operational criticality.
> Classification: **284 Tier 1** (core) · **293 Tier 2** (support) · **104 Tier 3** (optimization).

### Tier 1 Additions (284 Workflows)

#### Plan & Source

| ID | Workflow | Value Stream |
|---|---|---|
| W558 | Supplier Risk Assessment & Supply Disruption Contingency Planning | Supply Planning |
| W596 | Store-Level Replenishment Exception Management & Auto-Override | Supply Planning |
| W680 | Supply Chain Cost Analysis & Logistics Optimization Review | Supply Planning |
| W727 | Carrier & Freight Forwarder Daily Performance Monitoring | Supply Planning |
| W729 | Supply Chain Disruption Rapid Response & Escalation Protocol | Supply Planning |
| W762 | Carrier Performance Weekly Review & Freight Rate Benchmarking | Supply Planning |
| W763 | Supply Chain Vendor Diversification & Alternative Sourcing Maintenance | Supply Planning |
| W835 | Store-Level Replenishment Forecast Accuracy Review & Parameter Tuning | Supply Planning |
| W921 | Store-Level Emergency Local Sourcing & Alternative Vendor Activation | Supply Planning |
| W1006 | Vendor Purchase Order ASN Reconciliation & Discrepancy Resolution | Vendor Management & Procurement |
| W1020 | Vendor Consignment Inventory Physical Count & Periodic Reconciliation | Vendor Management & Procurement |
| W1026 | Vendor Product Discontinuation Notification & Last-Time Buy Management | Vendor Management & Procurement |
| W1038 | Vendor Catalog Synchronization & Product Information Quality Audit | Vendor Management & Procurement |
| W1137 | Vendor Purchase Order Line-Level Partial Shipment Acceptance & Backorder Management | Vendor Management & Procurement |
| W593 | Vendor Portal Content Management & Self-Service Operations | Vendor Management & Procurement |
| W620 | Vendor Due Diligence & Onboarding Site Visit Management | Vendor Management & Procurement |
| W632 | Competitive Bidding & Tender Management | Vendor Management & Procurement |
| W633 | Purchase Price Variance (PPV) Analysis & Cost Management | Vendor Management & Procurement |
| W669 | Vendor Contract Compliance Monitoring & Enforcement | Vendor Management & Procurement |
| W670 | Supplier Emergency Onboarding & Rapid Activation | Vendor Management & Procurement |
| W671 | Commodity Price Monitoring & Procurement Strategy | Vendor Management & Procurement |
| W760 | Vendor-Specific Commodity Price Index Tracking & Procurement Trigger Management | Vendor Management & Procurement |
| W818 | Vendor Insurance Certificate & Compliance Documentation Tracking | Vendor Management & Procurement |
| W819 | Vendor Quality Incoming Inspection Failure & Material Review Board (MRB) | Vendor Management & Procurement |
| W866 | Vendor Self-Service Purchase Order Acknowledgment & Confirmation | Vendor Management & Procurement |
| W867 | Vendor Self-Service Invoice Submission & Payment Status Inquiry | Vendor Management & Procurement |
| W870 | Vendor Compliance Document Upload & Expiration Tracking | Vendor Management & Procurement |
| W915 | Vendor Product Packaging Sustainability Assessment & Compliance Management | Vendor Management & Procurement |
| W938 | Vendor Managed Inventory (VMI) Periodic Data Accuracy Audit & Reconciliation | Vendor Management & Procurement |
| W959 | Vendor Rebate Volume Tier Compliance Reconciliation & Shortfall Processing | Vendor Management & Procurement |
| W962 | Vendor-Sponsored In-Store Display Compliance Audit & Chargeback | Vendor Management & Procurement |

#### Make & Move

| ID | Workflow | Value Stream |
|---|---|---|
| W1029 | DC-Level Temperature, Humidity & Environmental Monitoring for Sensitive Goods | DC & Warehouse Operations |
| W1041 | DC-Level Outbound Quality Sampling & Pre-Shipment Inspection | DC & Warehouse Operations |
| W585 | DC Dock Scheduling & Appointment Management | DC & Warehouse Operations |
| W649 | DC Safety Operations & Compliance | DC & Warehouse Operations |
| W681 | DC Quality Control & Vendor Compliance Inspection at Receiving | DC & Warehouse Operations |
| W785 | Vendor Returnable Transport Packaging Reconciliation & Settlement | DC & Warehouse Operations |
| W514 | Inventory Count Reconciliation & Variance Root Cause Analysis | Inventory Lifecycle |
| W587 | Inventory Obsolescence Identification & Write-Off Management | Inventory Lifecycle |
| W653 | Fleet Accident & Incident Management | Logistics & Fleet |
| W799 | Vehicle Acquisition, Registration, Insurance & Disposal Lifecycle Management | Logistics & Fleet |

#### Sell & Serve

| ID | Workflow | Value Stream |
|---|---|---|
| W1003 | Store-Level Paint Mixing Station Daily Cleaning, Calibration & Waste Disposal | Store Operations |
| W1005 | Store-Level Shelf Stock Rotation & Paint/Chemical Expiry Monitoring | Store Operations |
| W1008 | Store-Level Power Tool Battery Charging Station Safety & Maintenance | Store Operations |
| W1010 | Store-Level Outdoor Garden Center Weather Protection & Seasonal Display Setup | Store Operations |
| W1012 | Store-Level Hazardous Material Spill Kit Inspection & Restocking | Store Operations |
| W1015 | Store-Level Forklift & Heavy Equipment Daily Safety Check & Log | Store Operations |
| W1019 | Store-Level Construction Material Safety Data Sheet (SDS) Customer Access & Compliance | Store Operations |
| W1021 | Store-Level Loading Dock Equipment Maintenance & Safety Inspection | Store Operations |
| W1023 | Store-Level Post-Typhoon Damage Assessment, Cleanup & Rapid Reopening | Store Operations |
| W1025 | Store-Level Shelving, Racking & Display Fixture Safety Inspection & Maintenance | Store Operations |
| W1028 | Store-Level Shopping Cart, Basket & Customer Equipment Inventory Management | Store Operations |
| W1030 | Multi-Store District Manager Weekly Operations Review & Compliance Audit | Store Operations |
| W1037 | Store-Level Annual Physical Inventory Preparation, Execution & Variance Resolution | Store Operations |
| W1040 | Store-Level Customer Parking Lot Traffic Safety & Exterior Facility Management | Store Operations |
| W1047 | Store-Level Rainy Season Floor Safety, Anti-Slip Mat & Entrance Canopy Management | Store Operations |
| W1051 | Store-Level Fire Extinguisher Monthly Inspection, Annual Recharge & BFP Compliance | Store Operations |
| W1070 | Store-Level Customer Building Permit Documentation Package Preparation Assistance | Store Operations |
| W1125 | Store-Level Seasonal Typhoon Pre-Positioning & Emergency Stock Buffer Management | Store Operations |
| W1156 | Store-Level Customer Construction Site Safety Equipment Rental & Delivery | Store Operations |
| W497 | PWD Accessibility Compliance & Store Facilities Audit | Store Operations |
| W501 | Store-Level First Aid & Medical Emergency Response | Store Operations |
| W502 | Store-Level Non-Hazardous Waste Management | Store Operations |
| W554 | Store-Level Daily Shelf Replenishment & Restocking | Store Operations |
| W559 | Store-Level Non-Emergency Incident & Hazard Reporting | Store Operations |
| W562 | Store-Level Loss Prevention Daily Routine | Store Operations |
| W571 | Store-Level Daily Communication & Memo Acknowledgment | Store Operations |
| W573 | Store-Level Daily Planogram Execution & Shelf Compliance Check | Store Operations |
| W574 | Store-Level Daily Closing Procedure | Store Operations |
| W576 | Store-Level Typhoon & Severe Weather Preparedness Protocol | Store Operations |
| W579 | Store-Level Daily Equipment & Specialized Fixture Safety Check | Store Operations |
| W580 | Store-Level Emergency Manual Operations Protocol (Total System/Power Failure) | Store Operations |
| W582 | Store-Level Fire Drill Execution & Documentation | Store Operations |
| W601 | Store-Level Daily HR Operations & People Management | Store Operations |
| W603 | Store-Level Employee Disciplinary Process & DOLE Due Process Compliance | Store Operations |
| W666 | Store-Level Inventory Receiving Quality Control | Store Operations |
| W667 | Store-Level Price Verification & Daily Compliance Operations | Store Operations |
| W720 | Store-Level Daily Safety Briefing & Toolbox Talk | Store Operations |
| W721 | Store-Level Vendor Promodizer Floor Activity Coordination & Compliance | Store Operations |
| W739 | Store-Level Daily Huddle & Morning Team Briefing | Store Operations |
| W741 | Store-Level Fuel Inventory & Backup Generator Management | Store Operations |
| W743 | Store-Level Daily Cleaning & Sanitation Checklist Execution | Store Operations |
| W771 | Store-Level BOPIS Order Aging & Abandoned Pickup Processing | Store Operations |
| W958 | Store-Level Daily Cash Variance Threshold Monitoring & Exception Escalation | Store Operations |
| W517 | POS Cashier Shift Handover & Drawer Accountability | POS & Checkout |
| W519 | POS Suspicious Transaction & AML Compliance Reporting | POS & Checkout |
| W520 | Age-Restricted Product Verification & Compliance at POS | POS & Checkout |
| W521 | POS Transaction Suspend, Park & Recall | POS & Checkout |
| W522 | POS Daily Transaction Review & Cashier Performance Audit | POS & Checkout |
| W525 | POS Continuous Near-Real-Time Sync & Nightly Reconciliation | POS & Checkout |
| W527 | POS Tax Exemption Processing (Government / PEZA / Institutional) | POS & Checkout |
| W528 | POS Digital Receipt / E-Receipt Delivery | POS & Checkout |
| W529 | POS Void & Refund Tiered Authorization | POS & Checkout |
| W530 | POS High-Value Transaction Documentation & Customer ID | POS & Checkout |
| W531 | POS Bagging, Carry-Out & Bag Fee Compliance | POS & Checkout |
| W532 | POS Clearance & "Final Sale" Item Processing | POS & Checkout |
| W533 | POS Real-Time Event Streaming & Continuous Sync | POS & Checkout |
| W534 | Multi-Origin / Mixed-Basket Fulfillment Orchestration | POS & Checkout |
| W535 | POS Offline Capability Scope & Local Operations | POS & Checkout |
| W536 | Unified Order Management & Cross-Channel Fulfillment Routing | POS & Checkout |
| W749 | POS Heavy Equipment & Power Tool Safety Acknowledgment & Release Processing | POS & Checkout |
| W1056 | Store-Level Customer Construction Permit Advisory & Municipal Building Requirements Guidance | In-Store Customer Services |
| W1062 | Store-Level Customer Scaffolding Rental, Safety Harness Package & Delivery Service | In-Store Customer Services |
| W1067 | Store-Level Customer Fire Suppression System Design & Product Recommendation | In-Store Customer Services |
| W1080 | Store-Level Customer Construction Scaffold & Ladder Safety Consultation | In-Store Customer Services |
| W1098 | Customer Emergency Home Repair Quick-Fix Bundle Curation & Package Service | In-Store Customer Services |
| W1104 | Customer Tool Rental Return Damage Assessment & Billing | In-Store Customer Services |
| W1138 | Customer Construction Worker Safety Gear Bundle Recommendation & Compliance Package | In-Store Customer Services |
| W1144 | Store-Level Customer Hazardous Material Transport Regulation Advisory | In-Store Customer Services |
| W1154 | Store-Level Customer Paint VOC & Indoor Air Quality Compliance Advisory | In-Store Customer Services |
| W827 | Store-Level Building Material Load Calculation & Safety Advisory | In-Store Customer Services |
| W913 | Store-Level Emergency Generator Fuel Reserve Management & DOE Compliance | In-Store Customer Services |
| W1013 | E-Commerce Last-Mile Delivery Partner Performance Weekly Review | Ecommerce & Digital Channels |
| W1034 | Customer Ecommerce Payment Failure Recovery, Retry & Abandoned Checkout Rescue | Ecommerce & Digital Channels |
| W1155 | Customer Ecommerce Same-Day / Express Delivery Operations | Ecommerce & Digital Channels |
| W509 | Ecommerce Product Return Inspection, Grading & Disposition | Ecommerce & Digital Channels |
| W591 | E-Commerce Fulfillment SLA Monitoring & Exception Escalation | Ecommerce & Digital Channels |
| W592 | E-Commerce Customer Delivery Tracking & Proof of Delivery Management | Ecommerce & Digital Channels |
| W659 | Ecommerce Platform Incident Management | Ecommerce & Digital Channels |
| W724 | Marketplace Channel Daily Operations & Order Management (Lazada/Shopee) | Ecommerce & Digital Channels |
| W725 | Ecommerce Platform Daily Health Monitoring & Performance Dashboard | Ecommerce & Digital Channels |
| W829 | Customer Ecommerce Order Split & Partial Delivery Proactive Communication | Ecommerce & Digital Channels |
| W899 | Customer Bulk/Project Delivery Scheduling & Multi-Drop Coordination (B2C) | Ecommerce & Digital Channels |
| W809 | Wholesale Consignment Inventory Management & Settlement | Trade, Project & Wholesale |
| W600 | Service Contractor Accreditation & Onboarding Management | Installation & Services |
| W560 | Customer Account Dormancy Identification & Deactivation | Customer Experience & Loyalty |
| W597 | Customer Complaint Escalation Matrix & Resolution SLA Tracking | Customer Experience & Loyalty |
| W617 | B2B Customer Success & Quarterly Business Review Operations | Customer Experience & Loyalty |
| W619 | Customer Account Merge & Deduplication Request Processing | Customer Experience & Loyalty |
| W660 | Service Recovery & Customer Retention Program | Customer Experience & Loyalty |
| W675 | Customer Data Platform Daily Operations & Data Quality Management | Customer Experience & Loyalty |
| W996 | Store-Level Contractor Loyalty Tier Upgrade & VIP Retention Program Management | Customer Experience & Loyalty |

#### Finance

| ID | Workflow | Value Stream |
|---|---|---|
| W486 | Related Party Transaction Disclosure & Reporting (PAS 24) | Procure-to-Pay |
| W487 | Revenue Recognition Review (PFRS 15 Complex Scenarios) | Procure-to-Pay |
| W488 | Credit Card Chargeback Dispute Management | Procure-to-Pay |
| W498 | Vendor Advance Payment & Prepayment Management | Procure-to-Pay |
| W499 | BIR Percentage Tax Computation & Payment | Procure-to-Pay |
| W556 | AP Payment Run & Batch Processing Execution | Procure-to-Pay |
| W611 | Payment Gateway Daily Operations & Settlement Monitoring | Procure-to-Pay |
| W634 | Revenue Assurance & POS Revenue Reconciliation | Procure-to-Pay |
| W635 | PFRS 16 Lease Accounting Operations | Procure-to-Pay |
| W640 | Merchant Fee Analysis & Payment Cost Optimization | Procure-to-Pay |
| W662 | AP Aging Management & Vendor Payment Prioritization | Procure-to-Pay |
| W713 | Corporate Credit Card Program Management & Expense Reconciliation | Procure-to-Pay |
| W750 | Credit Card Installment Sales Reconciliation & Bank Settlement Processing | Procure-to-Pay |
| W751 | Store-Level Emergency Cash Float Request & Expedited Replenishment | Procure-to-Pay |
| W752 | Intercompany Management Fee Allocation & Monthly Billing | Procure-to-Pay |
| W764 | Store-Level Daily Opening Safe Count & Cash Float Preparation | Procure-to-Pay |
| W765 | Multi-Entity Consolidation Monthly Execution & Elimination Processing | Procure-to-Pay |
| W766 | Customer Credit Note Aging Management & Unredeemed Credit Write-Off | Procure-to-Pay |
| W767 | Vendor Rebate Claim Filing & Settlement Documentation Processing | Procure-to-Pay |
| W768 | BIR VAT Refund Claim Processing & Input VAT Recovery | Procure-to-Pay |
| W769 | Customer Overpayment Detection & Refund Processing | Procure-to-Pay |
| W813 | AP Vendor Invoice Duplicate Detection & Resolution | Procure-to-Pay |
| W814 | Credit Card Settlement Exception & Chargeback Recovery Processing | Procure-to-Pay |
| W919 | Intercompany Inventory Movement Accounting & Goods-in-Transit Reconciliation | Procure-to-Pay |
| W939 | Customer Store Credit Expiration Management & Unclaimed Credit Processing | Procure-to-Pay |
| W572 | Customer Credit Monitoring & Automated Alert Management | Order-to-Cash |
| W663 | Customer Credit Portfolio Periodic Review & Collection Strategy | Order-to-Cash |
| W81 | Bad Debt Provisioning, Write-Off & Recovery | Order-to-Cash |
| W812 | Customer Credit Field Collection Operations & Legal Escalation | Order-to-Cash |
| W886 | Customer Credit Application Processing & Scoring | Order-to-Cash |
| W887 | Customer Credit Limit Review, Adjustment & Approval | Order-to-Cash |
| W888 | Customer Credit Hold Management & Order Blocking | Order-to-Cash |
| W889 | Customer AR Aging Analysis & Collection Prioritization | Order-to-Cash |
| W890 | Customer Collection Call Execution & Promise Tracking | Order-to-Cash |
| W891 | Customer Bad Debt Write-Off Proposal & Approval | Order-to-Cash |
| W893 | Customer Credit Scorecard Annual Review & Portfolio Analysis | Order-to-Cash |
| W14 | Intercompany Transactions & Settlement | Record-to-Report |
| W39 | Fixed Asset Disposal & Retirement | Record-to-Report |
| W407 | Corporate Income Tax — Computation & Deferred Tax (PAS 12) | Record-to-Report |
| W481 | SEC Reportorial Requirements Compliance (GIS, AFS, GAN, MC 28) | Record-to-Report |
| W590 | Monthly Tax Provision & Compliance Review | Record-to-Report |
| W612 | Intercompany Rate Setting & Quarterly Transfer Pricing Review | Record-to-Report |
| W636 | Standardized Balance Sheet Account Reconciliation | Record-to-Report |
| W637 | Financial Controls Testing & Monitoring | Record-to-Report |
| W638 | Period-End Journal Entry Review & Approval | Record-to-Report |
| W661 | Fixed Asset Depreciation Run & Component Accounting Operations | Record-to-Report |
| W70 | Credit Note & Debit Note Aging Reconciliation | Record-to-Report |
| W711 | BIR Withholding Tax (EWT) Certificate Form 2307 Issuance to Vendors | Record-to-Report |
| W873 | Product Safety Incident Triage & Recall Risk Assessment | Record-to-Report |
| W874 | Product Recall Customer Notification Campaign Execution | Record-to-Report |
| W875 | Product Recall Inventory Quarantine, Hold & Disposition | Record-to-Report |
| W876 | Product Recall Regulatory Reporting & DTI/BIR/FDA Compliance | Record-to-Report |
| W877 | Product Recall Vendor Recovery & Cost Reimbursement | Record-to-Report |
| W878 | Product Recall Effectiveness Audit & Close-Out | Record-to-Report |
| W589 | Weekly Cash Flow Forecast & Treasury Planning | Treasury & Cash |
| W664 | Cash Flow Variance Analysis & Liquidity Stress Testing | Treasury & Cash |
| W80 | FX Hedging & Forward Contract Management | Treasury & Cash |

#### People

| ID | Workflow | Value Stream |
|---|---|---|
| W1001 | Store-Level Employee Performance-Based Profit Sharing & Incentive Bonus Management | Hire-to-Retire |
| W1032 | Employee Overtime Pre-Approval, Monitoring & DOLE Weekly Cap Enforcement | Hire-to-Retire |
| W494 | Employee Wellness & Mental Health Program Management | Hire-to-Retire |
| W512 | Store-Level Health & Safety Committee Operations | Hire-to-Retire |
| W561 | Employee Attendance Exception Management | Hire-to-Retire |
| W594 | Store-Level Employee Daily Attendance Verification & Exception Processing | Hire-to-Retire |
| W628 | Employee Exit Interview & Attrition Analysis | Hire-to-Retire |
| W629 | Store-Level Employee Engagement Survey & Action Planning | Hire-to-Retire |
| W630 | Employee Recognition & Rewards Program Management | Hire-to-Retire |
| W642 | HMO & Private Benefits Administration | Hire-to-Retire |
| W643 | Final Pay Computation & Separation Settlement | Hire-to-Retire |
| W644 | 13th Month Pay Reconciliation & Compliance | Hire-to-Retire |
| W645 | Strategic Workforce Planning | Hire-to-Retire |
| W646 | HR Service Desk Operations | Hire-to-Retire |
| W647 | Employee Data Privacy Compliance Operations | Hire-to-Retire |
| W682 | Employee Career Development & Internal Job Posting Operations | Hire-to-Retire |
| W716 | Internal Communication & Company-Wide Announcement Management | Hire-to-Retire |
| W717 | Workplace Violence Prevention & Response Protocol | Hire-to-Retire |
| W718 | Employee Relocation & Housing Assistance Management | Hire-to-Retire |
| W719 | Diversity, Equity & Inclusion (DEI) Program Management | Hire-to-Retire |
| W753 | Store-Level Employee Meal Break & Rest Period Scheduling & DOLE Compliance | Hire-to-Retire |
| W755 | Store-Level Employee Internal Theft Prevention Awareness & Compliance Daily Operations | Hire-to-Retire |
| W777 | Employee Leave Balance Management & Annual Leave Carry-Forward Processing | Hire-to-Retire |
| W778 | Employee Benefits Annual Open Enrollment & Plan Selection Management | Hire-to-Retire |
| W780 | Store-Level Employee Uniform & PPE Periodic Issuance & Replacement Processing | Hire-to-Retire |
| W815 | Employee Business Travel Request, Approval & Expense Management | Hire-to-Retire |
| W816 | Multi-Entity Payroll Consolidation & Cross-Entity Reconciliation | Hire-to-Retire |
| W817 | Employee Sabbatical, Study Leave & Secondment Management | Hire-to-Retire |
| W956 | Employee Annual Physical Examination & Occupational Health Clearance Management | Hire-to-Retire |
| W957 | Employee Tuition Assistance & Educational Advancement Program Management | Hire-to-Retire |
| W973 | Employee Long Service Award & Milestone Recognition Management | Hire-to-Retire |
| W977 | Employee Retirement Benefit Fund (RA 7641) Administration & Processing | Hire-to-Retire |
| W994 | Employee Typhoon Disaster Relief Emergency Assistance & No-Interest Loan Program | Hire-to-Retire |

#### Governance & Assurance

| ID | Workflow | Value Stream |
|---|---|---|
| W448 | LGU Sanitary & Health Permit Management | Compliance & Regulatory |
| W468 | DTI Price Freeze / Emergency Price Control Implementation (RA 7581) | Compliance & Regulatory |
| W483 | DOLE Drug-Free Workplace Program Compliance | Compliance & Regulatory |
| W485 | BIR Branch Registration & RDO Transfer Management | Compliance & Regulatory |
| W505 | DOLE Labor Inspection Response Protocol | Compliance & Regulatory |
| W506 | Unified Regulatory Compliance Calendar & Dashboard | Compliance & Regulatory |
| W656 | Anti-Bribery & Anti-Corruption (ABAC) Compliance Program | Compliance & Regulatory |
| W657 | Regulatory Change Management & Impact Assessment | Compliance & Regulatory |
| W658 | General Regulatory Inspection Response Protocol | Compliance & Regulatory |
| W730 | Anti-Money Laundering (AML) Compliance Program Operations | Compliance & Regulatory |
| W731 | Consumer Act (RA 7394) Compliance Monitoring & Enforcement | Compliance & Regulatory |
| W732 | Vendor Tax Compliance Monitoring & BIR TIN Validation | Compliance & Regulatory |
| W834 | Customer Account Data Deletion & RA 10173 Privacy Compliance Processing | Compliance & Regulatory |
| W837 | Daily Store Exception-Based Reporting & Transaction Monitoring | Loss Prevention & Asset Protection |
| W838 | CCTV & Surveillance System Daily Operations & Incident Review | Loss Prevention & Asset Protection |
| W839 | Internal Theft Investigation & Employee Dishonesty Case Management | Loss Prevention & Asset Protection |
| W840 | Organized Retail Crime Detection, Tracking & Task Force Coordination | Loss Prevention & Asset Protection |
| W841 | Refund & Return Fraud Detection, Investigation & Prevention | Loss Prevention & Asset Protection |
| W842 | Cash Handling Exception Monitoring & Sweethearting Detection | Loss Prevention & Asset Protection |
| W843 | Vendor & Delivery Fraud Detection & Dock Security Audit | Loss Prevention & Asset Protection |
| W844 | Store Entrance/Exit Audit & Electronic Article Surveillance (EAS) Management | Loss Prevention & Asset Protection |
| W845 | Shrinkage Analysis, Root Cause Investigation & Reduction Program | Loss Prevention & Asset Protection |
| W846 | Loss Prevention Training, Awareness & Compliance Program | Loss Prevention & Asset Protection |
| W140 | Occupational Health & Safety (OHS) Incident Management | Health, Safety & Environment |
| W695 | Emergency Response & Evacuation Protocol Management | Health, Safety & Environment |
| W696 | Contractor & Visitor Safety Induction & Access Control | Health, Safety & Environment |
| W697 | Workplace Ergonomics Assessment & Musculoskeletal Injury Prevention | Health, Safety & Environment |
| W698 | Safety Data Sheet (SDS) Lifecycle Management & Distribution | Health, Safety & Environment |
| W699 | Hazmat Transportation & Carrier Compliance Management | Health, Safety & Environment |
| W758 | Store-Level Fire Safety Equipment Daily Inspection & Compliance | Health, Safety & Environment |
| W759 | Store-Level Hazardous Material Customer Advisory & Safe Handling Guidance | Health, Safety & Environment |
| W803 | Hazmat Regulatory Change Management & Compliance Update | Health, Safety & Environment |
| W804 | Occupational Health Surveillance, Employee Medical Monitoring & Record Management | Health, Safety & Environment |
| W847 | Business Continuity Plan Annual Review & Update | Business Continuity & Insurance |
| W848 | Typhoon & Natural Disaster Store Emergency Protocol & Response | Business Continuity & Insurance |
| W849 | IT Disaster Recovery Site Activation & Failover Execution | Business Continuity & Insurance |
| W850 | Store Emergency Closure & Reopening Procedure | Business Continuity & Insurance |
| W851 | Critical System Recovery & Service Restoration | Business Continuity & Insurance |
| W852 | Supply Chain Disruption Business Impact Assessment & Recovery | Business Continuity & Insurance |
| W853 | Business Continuity Plan Tabletop Exercise & Drill Execution | Business Continuity & Insurance |
| W854 | Pandemic/Epidemic Business Continuity Activation & Operations | Business Continuity & Insurance |
| W855 | Communication Tree Activation & Crisis Communication Management | Business Continuity & Insurance |
| W856 | Post-Incident Review, Lessons Learned & Plan Update | Business Continuity & Insurance |
| W857 | Store & DC Property Insurance Claim Filing & Documentation | Business Continuity & Insurance |
| W858 | Typhoon, Flood & Natural Disaster Damage Assessment & Insurance Claim | Business Continuity & Insurance |
| W859 | Vehicle & Fleet Insurance Claim Processing | Business Continuity & Insurance |
| W860 | Business Interruption Insurance Claim & Loss Documentation | Business Continuity & Insurance |
| W861 | Employee Injury Insurance Claim Coordination & SSS/ECC Filing | Business Continuity & Insurance |
| W864 | Insurance Claim Recovery, Settlement & Accounting Entry | Business Continuity & Insurance |

#### Technology & Data

| ID | Workflow | Value Stream |
|---|---|---|
| W382 | IT Backup & Recovery Operations | IT Operations & Security |
| W383 | IT Security Incident Response (General) | IT Operations & Security |
| W385 | Data Cleansing & Migration Operational Lifecycle | IT Operations & Security |
| W393 | Remote Access, VPN & Zero Trust Connectivity Management | IT Operations & Security |
| W495 | ERP Patch, Upgrade & Release Management | IT Operations & Security |
| W595 | ERP System Daily Health Check & Integration Monitoring | IT Operations & Security |
| W614 | Data Warehouse & ETL Pipeline Daily Operations & Monitoring | IT Operations & Security |
| W615 | Customer Mobile App Daily Operations & Content Management | IT Operations & Security |
| W616 | ERP Business Change Request & Enhancement Backlog Management | IT Operations & Security |
| W710 | Loss Prevention Analytics & Shrinkage Investigation System Operations | IT Operations & Security |
| W73 | System Upgrade & New Entity Integration Testing | IT Operations & Security |
| W733 | Enterprise API Gateway Daily Monitoring & Health Dashboard | IT Operations & Security |
| W831 | POS Terminal Emergency Swap & Rapid Replacement Protocol | IT Operations & Security |

### Tier 2 Additions (293 Workflows)

#### Plan & Source

| ID | Workflow | Value Stream |
|---|---|---|
| W515 | Loyalty Tier Re-evaluation & Migration Processing | Merchandise Strategy |
| W564 | New Product Introduction (NPI) & Full Store Rollout | Merchandise Strategy |
| W678 | Multi-Channel Pricing Consistency Monitoring & Governance | Merchandise Strategy |
| W679 | Assortment Optimization & Rationalization Review | Merchandise Strategy |
| W737 | Markdown Optimization & Analytics Operations | Merchandise Strategy |
| W738 | Vendor Trade Fund Management & Promotional Budget Tracking | Merchandise Strategy |
| W830 | Product Phase-Out Inventory Disposition Planning & Execution | Merchandise Strategy |
| W900 | Vendor New Product In-Store Launch Event & Demonstration Coordination | Merchandise Strategy |
| W908 | Store-Level Barangay & Local Fiesta Merchandising Calendar Management | Merchandise Strategy |
| W910 | Customer Product Bundle Assembly & Pre-Packaged Solution Kit Management | Merchandise Strategy |
| W925 | Vendor Consignment Shelf Space Performance Monitoring & Optimization | Merchandise Strategy |
| W1031 | Customer Delivery Service Area Geo-Fencing & Coverage Management | Supply Planning |
| W492 | Temperature-Controlled & Sensitive Goods Logistics | Supply Planning |
| W622 | Mock Product Recall Exercise & Recall Readiness Testing | Supply Planning |
| W623 | Cross-Functional New Store Opening Readiness Review | Supply Planning |
| W786 | DC-to-Store Delivery Route Optimization & Multi-Stop Planning | Supply Planning |
| W1002 | Vendor Product Sampling & Test Batch Inventory Lifecycle Management | Vendor Management & Procurement |
| W1033 | Vendor Lead Time Accuracy Monitoring & Supply Planning Impact Assessment | Vendor Management & Procurement |
| W1035 | Store-Level Return-to-Vendor (RTV) Consolidation & Batch Shipping Processing | Vendor Management & Procurement |
| W1100 | Customer Contractor Project Financing & Supplier Credit Line Partnership Management | Vendor Management & Procurement |
| W1105 | Vendor Early Payment Discount Capture & Dynamic Discounting Optimization | Vendor Management & Procurement |
| W1110 | Vendor-Managed Inventory (VMI) Seasonal Ramp-Up & Wind-Down | Vendor Management & Procurement |
| W1115 | Vendor Performance-Based Shelf Space Allocation Review | Vendor Management & Procurement |
| W1128 | Vendor Catalog New Product Sample Request & In-Store Trial Evaluation | Vendor Management & Procurement |
| W1132 | Vendor Logistics Performance Weekly Scorecard & Carrier Lane Analysis | Vendor Management & Procurement |
| W1141 | Vendor Payment Term Annual Renegotiation & Cost Savings Tracking | Vendor Management & Procurement |
| W1145 | Vendor Seasonal Import Container Consolidation & Optimization Planning | Vendor Management & Procurement |
| W1151 | Vendor Product Recall Cost Recovery & Margin Impact Assessment | Vendor Management & Procurement |
| W491 | Supplier Financial Health & Credit Risk Monitoring | Vendor Management & Procurement |
| W513 | Vendor-Funded Promotional Activity & Co-op Advertising Management | Vendor Management & Procurement |
| W621 | Vendor-Managed Inventory (VMI) Daily Performance Monitoring | Vendor Management & Procurement |
| W631 | Strategic Sourcing & Category Strategy | Vendor Management & Procurement |
| W672 | VMI Quarterly Business Review & Program Optimization | Vendor Management & Procurement |
| W705 | Vendor Self-Service Portal Operations & Supplier Collaboration | Vendor Management & Procurement |
| W706 | Supplier Performance Scorecard & Quarterly Business Review | Vendor Management & Procurement |
| W788 | Vendor New Product Submission Review & Evaluation Processing | Vendor Management & Procurement |
| W868 | Vendor Catalog & Product Information Self-Service Management | Vendor Management & Procurement |
| W869 | Vendor Dispute Resolution & Issue Ticketing | Vendor Management & Procurement |
| W871 | Supplier Scorecard Portal Publication & Performance Transparency | Vendor Management & Procurement |
| W872 | Vendor RFQ & Bid Submission Portal Management | Vendor Management & Procurement |
| W901 | Vendor Seasonal Buy-Back & Stock Return Agreement Execution | Vendor Management & Procurement |
| W932 | Vendor Catalog Price Change Intake, Assessment & ERP Synchronization | Vendor Management & Procurement |
| W978 | Vendor Seasonal Product Post-Season Performance Review & Assortment Rationalization | Vendor Management & Procurement |

#### Make & Move

| ID | Workflow | Value Stream |
|---|---|---|
| W648 | DC Cycle Counting & Inventory Accuracy Program | DC & Warehouse Operations |
| W651 | Reverse Logistics Processing (Customer/Store Returns at DC) | DC & Warehouse Operations |
| W652 | Seasonal Warehouse Surge Planning & Execution | DC & Warehouse Operations |
| W784 | DC Inventory Slotting Optimization & Periodic Re-Slotting Execution | DC & Warehouse Operations |
| W796 | DC Workforce Scheduling, Labor Planning & Productivity Tracking | DC & Warehouse Operations |
| W797 | DC Security Operations, Perimeter Management & Access Control | DC & Warehouse Operations |
| W836 | DC Outbound Load Verification & Pre-Dispatch Quality Check | DC & Warehouse Operations |
| W588 | Seasonal Inventory Build-Down & Transition Execution | Inventory Lifecycle |

#### Sell & Serve

| ID | Workflow | Value Stream |
|---|---|---|
| W1049 | Store-Level Customer Tool Sharpening, Blade Replacement & Small Engine Maintenance Service | Store Operations |
| W1058 | Store-Level Customer Bulk Construction Water Delivery & Site Logistics Coordination | Store Operations |
| W1085 | Store-Level Appliance Display Model Lifecycle & Periodic Refresh Management | Store Operations |
| W1091 | Store-Level Customer Fence & Gate Installation Service Partner Coordination | Store Operations |
| W1103 | Store-Level Outdoor Lumber Yard Rain Protection & Inventory Preservation | Store Operations |
| W1106 | Store-Level Community Building Materials Donation & LGU Partnership | Store Operations |
| W1112 | Store-Level Inventory Age-Based Auto-Markdown & Clearance Trigger | Store Operations |
| W1116 | Store-Level Customer Complaint Trend Analysis & Systemic Issue Escalation | Store Operations |
| W1119 | Store-Level Outdoor Garden Center Seasonal Plant Inventory Lifecycle | Store Operations |
| W1121 | Store-Level Intercom & Public Address System Daily Operations | Store Operations |
| W1123 | Store-Level Customer Project Progress Site Visit & Material Delivery Verification | Store Operations |
| W1130 | Store-Level Paint Tinting Machine Calibration Verification & Color Accuracy Audit | Store Operations |
| W1133 | Store-Level Customer Special Order Cancellation & Partial Refund Processing | Store Operations |
| W1135 | Store-Level Daily Temperature-Sensitive Product Monitoring & Quality Check | Store Operations |
| W1139 | Store-Level Lumber Yard Inventory Seasonal Rotation & Grade Segregation | Store Operations |
| W1142 | Store-Level Customer Waiting Area Comfort & Amenities Daily Management | Store Operations |
| W503 | Store-Level Pest Control & Sanitation Management | Store Operations |
| W524 | Demo / Display Unit Selling at POS | Store Operations |
| W575 | Store-Level Weekly Sales & Operations Review | Store Operations |
| W577 | Store-Level Holiday Season (Ber Months) Operational Ramp-Up | Store Operations |
| W578 | Store-Level Payday Weekend & Peak Day Operational Readiness | Store Operations |
| W581 | Store-Level Vendor Representative Access & Activity Management | Store Operations |
| W583 | Store-Level Seasonal Promotional Transition & Display Reset | Store Operations |
| W602 | Store-Level Labor Cost Monitoring & Overtime Budget Control | Store Operations |
| W606 | Store-Level Water & Utility Conservation Operations | Store Operations |
| W609 | Store-Level New Employee Buddy System & First-Week Onboarding | Store Operations |
| W665 | Store-Level KPI Dashboard & Daily Performance Monitoring | Store Operations |
| W668 | Store-Level Home Delivery & Third-Party Logistics Coordination | Store Operations |
| W702 | New Store Opening Project Management & Go-Live Execution | Store Operations |
| W703 | Store Closure, Consolidation & Asset Recovery | Store Operations |
| W722 | Store-Level Exterior Display & Garden Center Daily Operations | Store Operations |
| W723 | Store-Level Loading Bay Traffic & Truck Queue Management | Store Operations |
| W742 | Store-Level Key, Access Card & Secure Area Daily Management | Store Operations |
| W745 | Store-Level Receiving Dock Scheduling & DSD Vendor Delivery Window Management | Store Operations |
| W774 | Store-Level Parking Lot & Exterior Facility Daily Management | Store Operations |
| W824 | Store-Level Lumber Yard & Outdoor Area Daily Operations | Store Operations |
| W825 | Store-Level Bulky Item Delivery Proof Collection & Documentation | Store Operations |
| W826 | Store-Level Layaway Payment Reminder & Forfeiture Processing | Store Operations |
| W950 | Store-Level Customer Vehicle Loading Assistance & Load Securing | Store Operations |
| W951 | Store-Level Bulk Material Breaking & Custom Quantity Packaging | Store Operations |
| W952 | Store-Level Customer Gratuity & Service Tip Processing | Store Operations |
| W974 | Store-Level Customer Project Staged Delivery & Phased Material Release | Store Operations |
| W999 | Store-Level Customer Tile & Flooring Sample Loan & Return Program | Store Operations |
| W523 | POS Promotional Terminal Setup & Pre-Live Verification | POS & Checkout |
| W526 | POS Customer Queue Management & Express Lane Operations | POS & Checkout |
| W605 | Return Fraud Detection & Serial Returner Management | POS & Checkout |
| W747 | POS Credit Card Installment Selling & 0% Interest Promotion Processing | POS & Checkout |
| W748 | POS Customer Loyalty On-the-Spot Upselling & Cross-Selling | POS & Checkout |
| W896 | Customer Gift Card Corporate & Bulk Purchase Processing | POS & Checkout |
| W935 | Customer Product Registration at POS for Vendor Extended Warranty | POS & Checkout |
| W1000 | Customer Ceiling System Material Calculator & Design Recommendation Service | In-Store Customer Services |
| W1004 | Customer Material Delivery Scheduling & Rescheduling Self-Service Portal | In-Store Customer Services |
| W1007 | Customer Tool & Equipment Demo Reservation & Scheduling Service | In-Store Customer Services |
| W1009 | Customer Custom Order Special Pricing Approval & Quotation Lifecycle | In-Store Customer Services |
| W1014 | Customer Multi-Entity Billing & Consolidated Invoicing for Corporate Accounts | In-Store Customer Services |
| W1016 | Customer Product Installation Warranty Registration & Follow-Up Service | In-Store Customer Services |
| W1018 | Customer Project Progress Payment Verification & Invoice Matching | In-Store Customer Services |
| W1043 | Customer Paint Coverage Area Calculator & Primer/Finish Quantity Estimator Service | In-Store Customer Services |
| W1044 | Customer Concrete Mix Ratio & Volume Calculator for Slab/Foundation/Column Service | In-Store Customer Services |
| W1045 | Store-Level Customer PVC Pipe Cutting, Jointing & Fabrication Service | In-Store Customer Services |
| W1046 | Customer Door & Window Measurement, Sizing & Custom Order Service | In-Store Customer Services |
| W1048 | Customer Rainwater Harvesting System Design & Material Sizing Service | In-Store Customer Services |
| W1050 | Customer Staircase Tread, Riser & Railing Material Calculator Service | In-Store Customer Services |
| W1052 | Customer Gutter, Downspout & Flashing Sizing Calculator Service | In-Store Customer Services |
| W1053 | Customer Bathroom & Kitchen Exhaust Fan & Ventilation Duct Sizing Service | In-Store Customer Services |
| W1054 | Store-Level Customer Wire & Cable Cut-to-Length Spool Service | In-Store Customer Services |
| W1055 | Customer Water Filtration & Purification System Sizing for Residential & Commercial | In-Store Customer Services |
| W1057 | Customer Insulation Material Calculator (Wall, Ceiling, Roof Thermal & Acoustic) | In-Store Customer Services |
| W1059 | Customer Kitchen Countertop Measurement & Custom Fabrication Order Service | In-Store Customer Services |
| W1060 | Customer Rebar Stirrup, Tying Wire & Binding Material Quantity Estimator Service | In-Store Customer Services |
| W1061 | Customer Tile Grout, Adhesive & Thin-Set Mortar Quantity Calculator Service | In-Store Customer Services |
| W1063 | Store-Level Customer Welding Gas Cylinder Exchange & Refill Service | In-Store Customer Services |
| W1064 | Customer Electrical Panel & Circuit Breaker Sizing Recommendation Service | In-Store Customer Services |
| W1065 | Customer Bathroom Renovation Complete Project Planning & Material Bundle Service | In-Store Customer Services |
| W1066 | Customer Termite & Pest Control Product Selection & Treatment Plan Recommendation | In-Store Customer Services |
| W1068 | Customer Earthquake-Resistant Construction Material Selection & Retrofit Advisory | In-Store Customer Services |
| W1069 | Customer Flood-Resistant Construction Material Recommendation | In-Store Customer Services |
| W1072 | Store-Level Customer Marine & Coastal Construction Material Selection Advisory | In-Store Customer Services |
| W1073 | Customer House Foundation Type Recommendation & Material Estimation Service | In-Store Customer Services |
| W1075 | Customer Roof Truss & Structural Frame Material Estimation Service | In-Store Customer Services |
| W1077 | Store-Level Customer Construction Site Portable Toilet & Temporary Facility Rental Coordination | In-Store Customer Services |
| W1078 | Customer Rainwater Collection & Storage System Complete Package Design | In-Store Customer Services |
| W1079 | Customer Swimming Pool Construction Material Estimation Service | In-Store Customer Services |
| W1081 | Customer Construction Project Insurance Coverage Advisory Service | In-Store Customer Services |
| W1083 | Store-Level Customer Plumbing Fixture & Fitting Compatibility Verification Service | In-Store Customer Services |
| W1084 | Customer Home Security & CCTV System Design & Product Recommendation Service | In-Store Customer Services |
| W1086 | Customer Construction Waste Disposal & Skip/Dumpster Rental Coordination | In-Store Customer Services |
| W1089 | Store-Level Customer Tile & Flooring Digital Room Visualizer Kiosk Operations | In-Store Customer Services |
| W1090 | Customer HVAC Ductwork Design & Complete Material Sizing Recommendation | In-Store Customer Services |
| W1093 | Customer Interior Paint Color Scheme Consultation & Material Board Service | In-Store Customer Services |
| W1094 | Customer Construction Equipment Rental Partner Coordination & Booking | In-Store Customer Services |
| W1095 | Store-Level Customer Electrical Residential Wiring Diagram & Material List Service | In-Store Customer Services |
| W1097 | Store-Level Customer Outdoor Deck, Patio & Pergola Material Estimation Service | In-Store Customer Services |
| W1101 | Store-Level Customer Door & Window Security Grille Custom Fabrication Coordination | In-Store Customer Services |
| W1102 | Customer Retaining Wall & Foundation Formwork Material Estimation Service | In-Store Customer Services |
| W1113 | Customer E-Gift Card Purchase & Digital Delivery | In-Store Customer Services |
| W1114 | Customer Product Availability Real-Time Stock Lookup & Reservation Service | In-Store Customer Services |
| W1122 | Customer Project Material Delivery Photo Documentation & Proof Service | In-Store Customer Services |
| W1124 | Customer Construction Material Compatibility Cross-Reference & Substitution Advisory | In-Store Customer Services |
| W1126 | Customer Bulk Cement & Sand Order Direct-to-Site Delivery Tracking | In-Store Customer Services |
| W1129 | Customer Interior Design Material Board Curation & Mood Board Assembly Service | In-Store Customer Services |
| W1131 | Customer Construction Project Milestone Photo Documentation & Progress Tracking Portal | In-Store Customer Services |
| W1140 | Customer Post-Construction Punch List Material Fulfillment & Callback Order | In-Store Customer Services |
| W1143 | Customer Construction Material Pre-Order Reservation & Price Lock Service | In-Store Customer Services |
| W1146 | Store-Level Customer Cement & Bagged Material Shelf Life Monitoring & Freshness Guarantee | In-Store Customer Services |
| W1148 | Store-Level Customer Construction Site Vehicle Access Assessment & Delivery Feasibility | In-Store Customer Services |
| W1150 | Store-Level Customer Lumber & Plywood Moisture Content Testing & Quality Verification | In-Store Customer Services |
| W1152 | Store-Level Customer Project Material Quantity Verification & Completeness Check | In-Store Customer Services |
| W1158 | Store-Level Customer Project Material List Sharing & Contractor Collaborative Shopping | In-Store Customer Services |
| W1159 | Customer Construction Material Price Escalation Protection & Forward Pricing Agreement | In-Store Customer Services |
| W1160 | Store-Level DC-to-Store Delivery Inter-Island Ferry Scheduling & Coordination | In-Store Customer Services |
| W1162 | Store-Level Customer Power Tool & Equipment Pre-Purchase Try-Before-You-Buy Program | In-Store Customer Services |
| W604 | Store-Level Customer Experience Standards & Daily Service Operations | In-Store Customer Services |
| W607 | Store-Level Product Demo & Trial Station Daily Operations | In-Store Customer Services |
| W608 | Store-Level Customer Feedback Collection & Daily CX Pulse Monitoring | In-Store Customer Services |
| W740 | Store-Level Customer Complaint On-the-Spot Resolution & Floor Staff Empowerment | In-Store Customer Services |
| W744 | Store-Level Special Order Follow-Up & Proactive Customer Notification | In-Store Customer Services |
| W746 | Store-Level Building Material Sample Management & Customer Selection Assistance | In-Store Customer Services |
| W772 | Store-Level Rain Check Issuance for Out-of-Stock Promotional Items | In-Store Customer Services |
| W773 | Store-Level Customer Hold & Will-Call Order Management | In-Store Customer Services |
| W775 | Store-Level Customer Loyalty Card Replacement & Account Recovery | In-Store Customer Services |
| W776 | Store-Level Product Recall Customer Notification Execution | In-Store Customer Services |
| W823 | Store-Level Customer Material Calculator & Quantity Estimation Service | In-Store Customer Services |
| W897 | Store-Level Trade Professional Verification & Pro Badge Issuance for Discount Program | In-Store Customer Services |
| W903 | Store-Level Customer Material Sample Loan & Return Management | In-Store Customer Services |
| W916 | Customer Trade-In & Used Power Tool Buy-Back Program | In-Store Customer Services |
| W922 | Customer Walk-In Bulk Purchase Negotiation & Volume Pricing Approval | In-Store Customer Services |
| W924 | Store-Level Self-Service Kiosk & Interactive Product Information Station Management | In-Store Customer Services |
| W929 | Store-Level Lost & Found Item Management | In-Store Customer Services |
| W931 | Store-Level Customer Comfort Room & Amenity Daily Operations | In-Store Customer Services |
| W937 | Store-Level Customer Wheelchair & PWD Mobility Assistance Service | In-Store Customer Services |
| W941 | Store-Level Customer Baggage Hold & Parcel Custody Service | In-Store Customer Services |
| W943 | Customer Glass Cutting & Custom Flat Glass Service | In-Store Customer Services |
| W944 | Customer Pipe Threading, Cutting & Fabrication Service | In-Store Customer Services |
| W945 | Customer Key Duplication & Lock Rekeying Service | In-Store Customer Services |
| W946 | Customer Screen Door & Window Screen Custom Fabrication Service | In-Store Customer Services |
| W954 | Customer Delivery & Installation Quality Follow-Up Verification | In-Store Customer Services |
| W955 | Customer Daily-Wage Construction Worker Hiring Facilitation Service | In-Store Customer Services |
| W960 | Seasonal Forward Stock Pre-Positioning & Regional Buffer Management | In-Store Customer Services |
| W963 | Customer Tile & Flooring Quantity Calculator & Waste Factor Recommendation | In-Store Customer Services |
| W964 | Customer Bulk Cement, Sand & Aggregates Order & Direct-to-Site Delivery | In-Store Customer Services |
| W965 | Customer Complete Bathroom/Kitchen Renovation Package Assembly & Order | In-Store Customer Services |
| W967 | Store-Level Customer Project Material Takeoff & Professional Estimation Service | In-Store Customer Services |
| W968 | Customer Multi-Store Aggregated Order & Consolidated Single Delivery | In-Store Customer Services |
| W971 | Customer Power Tool Battery & Accessory Cross-Compatibility Checker & Recommendation | In-Store Customer Services |
| W976 | Store-Level Customer Lumber & Plywood Grade Selection & Quality Verification | In-Store Customer Services |
| W981 | Customer Paint Color Matching from Physical Sample & Digital Photo | In-Store Customer Services |
| W982 | Customer Electrical Load Calculation & Wire Size Recommendation Service | In-Store Customer Services |
| W983 | Customer Roofing Material Calculator & GI Sheet/Insulation Sizing Recommendation | In-Store Customer Services |
| W984 | Customer Water Tank & Pump System Sizing Recommendation Service | In-Store Customer Services |
| W985 | Store-Level Customer Aircon Sizing & BTU/Horsepower Calculation Service | In-Store Customer Services |
| W986 | Store-Level Customer Rebar Cutting, Bending & Fabrication Service | In-Store Customer Services |
| W987 | Customer Fence & Gate Material Estimation & Design Recommendation Service | In-Store Customer Services |
| W988 | Store-Level Customer Welding & Custom Metal Fabrication Service | In-Store Customer Services |
| W989 | Customer Plumbing System Layout Design & Material Takeoff Service | In-Store Customer Services |
| W991 | Customer Electrical Circuit Design & Residential Load Planning Service | In-Store Customer Services |
| W993 | Customer Construction Project Timeline & Phased Material Delivery Planner | In-Store Customer Services |
| W997 | Customer Bathroom/Kitchen Fixture Compatibility Checker & Bundle Builder | In-Store Customer Services |
| W998 | Customer Septic Tank & Wastewater System Sizing Recommendation Service | In-Store Customer Services |
| W569 | E-Commerce New Product Launch & Go-Live Process | Ecommerce & Digital Channels |
| W905 | Customer Project Photo Gallery & Social Proof/Inspiration Platform | Ecommerce & Digital Channels |
| W923 | Ecommerce Assembly & Installation Service Upsell at Online Checkout | Ecommerce & Digital Channels |
| W948 | Social Commerce Order Processing (Facebook, Instagram, TikTok Shop) | Ecommerce & Digital Channels |
| W1011 | Customer Trade Account Credit Insurance & Bad Debt Protection Processing | Trade, Project & Wholesale |
| W1022 | Customer Trade Account Statement Dispute & Resolution Processing | Trade, Project & Wholesale |
| W1024 | Customer Material Escrow & Project Fund Management for B2B Construction Accounts | Trade, Project & Wholesale |
| W1092 | Customer B2B Recurring Standing Order & Scheduled Auto-Replenishment Management | Trade, Project & Wholesale |
| W1107 | Customer Bulk Purchasing Group / Co-Op Buying Program Management | Trade, Project & Wholesale |
| W1111 | Customer Contractor Crew Registration & Job Site Badge Management | Trade, Project & Wholesale |
| W1117 | Customer Trade Account Statement of Account Auto-Generation & Email Delivery | Trade, Project & Wholesale |
| W1118 | Customer Contractor Project Bidding Support & Material Quote Service | Trade, Project & Wholesale |
| W1134 | Customer B2B Project Retention Money Release & Final Billing Reconciliation | Trade, Project & Wholesale |
| W1147 | Customer B2B Project Material Return Window Management & Excess Inventory Reconciliation | Trade, Project & Wholesale |
| W1149 | Customer Multi-Store Consolidated Purchase & Single Invoice Billing | Trade, Project & Wholesale |
| W1153 | Customer B2B Standing Order Seasonal Volume Adjustment & Forecast Sharing | Trade, Project & Wholesale |
| W1161 | Customer B2B Annual Volume Rebate Tier Qualification Tracking & Earned Benefit Management | Trade, Project & Wholesale |
| W598 | Wholesale Pricing & Quotation Management | Trade, Project & Wholesale |
| W599 | Wholesale Returns, Credit & Adjustment Processing | Trade, Project & Wholesale |
| W704 | Wholesale Customer Contract Renewal & Tier Reclassification | Trade, Project & Wholesale |
| W792 | Project Change Order Management & Margin Re-Impact Assessment | Trade, Project & Wholesale |
| W793 | Project Close-Out, Final Reconciliation & Warranty Handover | Trade, Project & Wholesale |
| W810 | Wholesale Backorder Management, Allocation & Customer Communication | Trade, Project & Wholesale |
| W811 | Wholesale Delivery Proof, Discrepancy Resolution & POD Reconciliation | Trade, Project & Wholesale |
| W918 | Customer Project Budget Tracking & Material Cost Variance Management | Trade, Project & Wholesale |
| W972 | Customer Franchise & Dealer Mini-Store Program Management | Trade, Project & Wholesale |
| W979 | Customer B2B Blanket Purchase Agreement & Scheduled Call-Off Management | Trade, Project & Wholesale |
| W980 | Store-Level Customer Construction Site Delivery Scheduling & Multi-Drop Coordination (B2B) | Trade, Project & Wholesale |
| W1036 | Customer Digital Product Passport & Sustainability Information Access | Customer Experience & Loyalty |
| W507 | Customer Complaint Root Cause Analysis & Systemic Improvement | Customer Experience & Loyalty |
| W508 | Customer Account Maintenance & B2B Information Update | Customer Experience & Loyalty |
| W673 | Customer Segmentation & Target Marketing Operations | Customer Experience & Loyalty |
| W674 | Customer Loyalty Program Partner Management | Customer Experience & Loyalty |
| W707 | Omnichannel Returns & Refund Orchestration | Customer Experience & Loyalty |
| W708 | Customer Communication Management & Proactive Notification Operations | Customer Experience & Loyalty |
| W735 | Customer Onboarding Journey Management & First-90-Day Engagement | Customer Experience & Loyalty |
| W756 | Customer Post-Purchase Follow-Up & Satisfaction Verification | Customer Experience & Loyalty |
| W757 | Customer On-the-Spot Loyalty Tier Upgrade Offer Processing | Customer Experience & Loyalty |
| W781 | Customer Store Credit Issuance & Lifecycle Management | Customer Experience & Loyalty |
| W782 | Customer B2B Order-to-Cash Cycle Monitoring & Proactive Communication | Customer Experience & Loyalty |
| W783 | Customer Credit Application Scoring & Risk Assessment Processing | Customer Experience & Loyalty |
| W820 | Customer Project BOM Estimation & Material Planning Service | Customer Experience & Loyalty |
| W821 | Customer Project Warranty Registration & Multi-Year Tracking | Customer Experience & Loyalty |
| W822 | Customer Loyalty Tier Benefit Fulfillment & Welcome Package Processing | Customer Experience & Loyalty |
| W894 | Customer Project Material List (BOM) Save, Share & Reorder Service ("Project Vault") | Customer Experience & Loyalty |
| W895 | Store-Level Pro Desk Appointment Scheduling & Priority Service Queue Management | Customer Experience & Loyalty |
| W914 | Customer Project Completion Celebration & Review Incentive Program | Customer Experience & Loyalty |
| W928 | Customer Price Protection & Price Adjustment Policy Processing | Customer Experience & Loyalty |
| W933 | Customer Loyalty Account Deceased Member Processing & Points Estate Transfer | Customer Experience & Loyalty |
| W936 | Customer B2B Self-Service Portal Order Management & Account Access | Customer Experience & Loyalty |
| W942 | Customer Loyalty Family/Household Account Linking & Shared Benefits Management | Customer Experience & Loyalty |
| W969 | Customer Quick Reorder from Purchase History (Trade & Loyalty Members) | Customer Experience & Loyalty |

#### Finance

| ID | Workflow | Value Stream |
|---|---|---|
| W489 | Store-Level Operating Budget & Cost Control | Procure-to-Pay |
| W500 | Transfer Order In-Transit Damage Claim & Resolution | Procure-to-Pay |
| W613 | Store-Level Weekly Payroll Accrual & Labor Cost Flash Report | Procure-to-Pay |
| W714 | Store-Level Daily Financial Summary Reporting & Flash P&L | Procure-to-Pay |
| W770 | AP Vendor Debit Memo Processing & Account Deduction Management | Procure-to-Pay |
| W712 | Financial Restatement & Prior-Year Adjustment Processing | Order-to-Cash |
| W892 | Customer Statement Generation & Distribution | Order-to-Cash |
| W482 | Annual Stockholders' Meeting (ASHM) Management | Record-to-Report |
| W610 | Insurance Claims Processing & Recovery Management | Record-to-Report |
| W639 | Rolling Forecast & Financial Scenario Planning | Record-to-Report |
| W85 | Product Costing & Margin Analysis Review | Record-to-Report |

#### People

| ID | Workflow | Value Stream |
|---|---|---|
| W493 | Labor Union & Collective Bargaining Management | Hire-to-Retire |
| W511 | Employee Cross-Entity & Cross-Location Transfer Processing | Hire-to-Retire |
| W555 | Seasonal & Temporary Staffing Process | Hire-to-Retire |
| W567 | Employee Cross-Training & Skill Matrix Management | Hire-to-Retire |
| W641 | Off-Cycle & Ad-Hoc Payment Processing | Hire-to-Retire |
| W754 | Store-Level New Hire First-30-Day Performance Check-In & Early Intervention | Hire-to-Retire |
| W779 | Store-Level Employee Injury Incident Reporting & Workers' Compensation Claim Processing | Hire-to-Retire |

#### Governance & Assurance

| ID | Workflow | Value Stream |
|---|---|---|
| W484 | Pandemic/Epidemic Business Response Protocol | Compliance & Regulatory |
| W626 | Enterprise Risk Register Maintenance & Quarterly Risk Review | Compliance & Regulatory |
| W627 | Product Recall Effectiveness Verification & Post-Recall Review | Compliance & Regulatory |
| W685 | Business Continuity Plan Maintenance & Annual BIA Refresh | Compliance & Regulatory |
| W802 | LGU Local Business Tax Computation, Payment & Receipt Management | Compliance & Regulatory |
| W961 | BSP Anti-Money Laundering (AML) Covered Transaction Reporting | Compliance & Regulatory |
| W805 | Workers' Compensation, SSS/ECC Claims & Return-to-Work Processing | Health, Safety & Environment |
| W862 | Insurance Policy Annual Renewal & Coverage Review | Business Continuity & Insurance |
| W863 | Third-Party Liability Claim & Customer Incident Insurance Response | Business Continuity & Insurance |

#### Technology & Data

| ID | Workflow | Value Stream |
|---|---|---|
| W684 | Business Intelligence Report Development & Governance Lifecycle | IT Operations & Security |
| W709 | Enterprise Data Governance & Quality Management Operations | IT Operations & Security |
| W734 | Data Quality Daily Triage & Remediation Operations | IT Operations & Security |
| W787 | ERP System Monthly Performance Review & Capacity Planning Update | IT Operations & Security |

### Tier 3 Additions (104 Workflows)

#### Plan & Source

| ID | Workflow | Value Stream |
|---|---|---|
| W624 | Competitor Store Visit Program & Market Intelligence Operations | Merchandise Strategy |
| W625 | Product Quality Lab Testing & Certification Management | Merchandise Strategy |
| W728 | Port & Customs Clearance Daily Status Tracking & Escalation | Supply Planning |
| W927 | Store-Level Rainy Season Emergency Product Deployment & Rapid Stock Replenishment | Supply Planning |
| W1087 | Store-Level Power Tool Brand Ambassador & Vendor Demo Day Event Management | Vendor Management & Procurement |
| W1099 | Store-Level Vendor-Sponsored Product Training Academy & Staff Certification Program | Vendor Management & Procurement |
| W1157 | Vendor Sustainable Packaging Assessment & Plastic Reduction Collaboration | Vendor Management & Procurement |
| W761 | Supplier Innovation & New Product Introduction Collaboration Processing | Vendor Management & Procurement |
| W865 | Vendor Portal User Onboarding, Access Provisioning & Training | Vendor Management & Procurement |
| W995 | Vendor Consignment Inventory Ageing Analysis & Automatic Markdown Trigger | Vendor Management & Procurement |

#### Make & Move

| ID | Workflow | Value Stream |
|---|---|---|
| W584 | DC Daily Operations & Shift Management | DC & Warehouse Operations |
| W586 | DC Daily KPI Dashboard & Performance Tracking | DC & Warehouse Operations |
| W650 | Warehouse Equipment Preventive Maintenance | DC & Warehouse Operations |
| W798 | DC Building Maintenance, Utility Operations & Facility Condition Monitoring | DC & Warehouse Operations |
| W654 | Driver Onboarding, Training & Certification | Logistics & Fleet |

#### Sell & Serve

| ID | Workflow | Value Stream |
|---|---|---|
| W1017 | Store-Level Scrap Metal & Recyclable Material Collection & Revenue Recognition | Store Operations |
| W1108 | Store-Level Forklift Operator Daily Certification Check & Compliance | Store Operations |
| W504 | Store-Level Digital Signage & Content Management | Store Operations |
| W516 | Self-Checkout (SCO) Daily Operations | POS & Checkout |
| W518 | Cashier Onboarding, POS Training & Competency Certification | POS & Checkout |
| W1027 | Customer AI-Powered Chatbot & Virtual Shopping Assistant Operations | In-Store Customer Services |
| W1071 | Customer Smart Home System Design & Product Recommendation Service | In-Store Customer Services |
| W1074 | Customer Home Office & Workspace Design Consultation Service | In-Store Customer Services |
| W1076 | Customer Garden & Outdoor Kitchen Design Consultation Service | In-Store Customer Services |
| W1082 | Store-Level Customer Construction Material Quality Verification & Grade Certification Assistance | In-Store Customer Services |
| W1088 | Customer Mortgage & Housing Loan Partner Bank Referral Desk Operations | In-Store Customer Services |
| W1096 | Customer Solar Water Heater System Sizing & Complete Package Recommendation | In-Store Customer Services |
| W1109 | Customer Project Material Surplus Buy-Back & Recycling Program | In-Store Customer Services |
| W1136 | Customer Product Knowledge Video Library & How-To Tutorial Content Management | In-Store Customer Services |
| W920 | Store-Level Vendor-Led Product Knowledge Training & Staff Certification Program | In-Store Customer Services |
| W949 | Customer AI-Powered Home Renovation Visualizer & Material Estimator | In-Store Customer Services |
| W953 | Customer Contractor Micro-Lending Partnership Program Management | In-Store Customer Services |
| W966 | Customer Construction Loan Documentation Assistance & Partner Bank Referral | In-Store Customer Services |
| W970 | Customer Post-Disaster Insurance Claim Material Replacement Coordination | In-Store Customer Services |
| W975 | Customer Home Energy Audit Referral & Energy-Efficient Product Recommendation | In-Store Customer Services |
| W990 | Customer Solar Panel System Sizing & ROI Calculator Service | In-Store Customer Services |
| W992 | Customer Garden & Landscape Design Consultation & Material Estimation Service | In-Store Customer Services |
| W510 | Ecommerce Product Review & Rating Management | Ecommerce & Digital Channels |
| W557 | E-Commerce Abandoned Cart Recovery & Retargeting | Ecommerce & Digital Channels |
| W563 | E-Commerce SEO & Digital Merchandising Management | Ecommerce & Digital Channels |
| W568 | E-Commerce Flash Sale & Limited-Time Offer Operations | Ecommerce & Digital Channels |
| W726 | Ecommerce Product Content Enrichment & Catalog Daily Operations | Ecommerce & Digital Channels |
| W828 | Ecommerce Platform Feature Release, A/B Testing & UX Optimization | Ecommerce & Digital Channels |
| W907 | Customer Consumables Subscription & Auto-Replenishment Service | Ecommerce & Digital Channels |
| W917 | Ecommerce Live Commerce & Social Selling Operations | Ecommerce & Digital Channels |
| W930 | Customer Back-in-Stock Notification Subscription & Alert Management | Ecommerce & Digital Channels |
| W934 | Ecommerce Customer Wishlist, Save-for-Later & Price Drop Alert | Ecommerce & Digital Channels |
| W940 | Ecommerce Customer Product Comparison Tool & Buying Guide Content Management | Ecommerce & Digital Channels |
| W947 | Ecommerce Live Video Shopping & Virtual Store Walkthrough | Ecommerce & Digital Channels |
| W794 | Service SKU Catalog Management, Pricing & Material Linkage | Installation & Services |
| W795 | Service Customer Complaint, Rework & Warranty Claim Management | Installation & Services |
| W898 | Store-Level Custom Paint Formula Save, Recall & Reorder Service | Installation & Services |
| W906 | Store-Level Community Workshop Space Booking & DIY Event Management | Installation & Services |
| W1039 | Customer Housewarming & New Home Gift Registry Service | Customer Experience & Loyalty |
| W1120 | Customer Loyalty Points Donation to Charity / Community Cause | Customer Experience & Loyalty |
| W566 | Mystery Shopping Program & CX Compliance Audit | Customer Experience & Loyalty |
| W618 | Customer Churn Prediction & Proactive Retention Management | Customer Experience & Loyalty |
| W904 | Store-Level Contractor Referral & Customer-Contractor Matchmaking Service | Customer Experience & Loyalty |
| W911 | Customer Digital Warranty Vault & Multi-Vendor Warranty Claim Aggregation | Customer Experience & Loyalty |
| W496 | Customer Loyalty Fraud Detection & Prevention | Marketing & Communications |
| W565 | Marketing Campaign ROI & Attribution Analysis | Marketing & Communications |
| W570 | Loyalty Points Expiry Management & Annual Liability Cleanup | Marketing & Communications |
| W676 | Digital Marketing Campaign Operations & Cross-Channel Execution | Marketing & Communications |
| W677 | Marketing Budget Management & Spend Analytics | Marketing & Communications |
| W736 | Marketing Data Platform Daily Operations & Campaign Analytics | Marketing & Communications |
| W833 | Marketing Campaign Compliance Review & Regulatory Approval | Marketing & Communications |
| W902 | Customer Loyalty Partner Reward Catalog Management & Fulfillment | Marketing & Communications |
| W909 | Customer Trade Account Co-Branded Credit Card Program Management | Marketing & Communications |
| W912 | Store-Level Customer Loyalty Points Gifting & Transfer Between Members | Marketing & Communications |
| W926 | Customer Loyalty Reward Physical Fulfillment & Partner Logistics Management | Marketing & Communications |

#### People

| ID | Workflow | Value Stream |
|---|---|---|
| W1042 | Employee Store-Level Rotational Cross-Training & Multi-Skill Certification Program | Hire-to-Retire |
| W1127 | Store-Level Employee Annual Competency Re-Certification & Skills Refresher | Hire-to-Retire |
| W683 | Employee Competency Assessment & Certification Management | Hire-to-Retire |
| W715 | Employee Referral Program Management & Reward Processing | Hire-to-Retire |

#### Asset & Infrastructure

| ID | Workflow | Value Stream |
|---|---|---|
| W700 | Facility Condition Assessment & Capital Planning Support | Real Estate & Construction |
| W701 | Utility Infrastructure Management & Metering Operations | Real Estate & Construction |
| W789 | Construction Safety Management & DOLE DO 13 Compliance | Real Estate & Construction |
| W790 | Construction Quality Assurance, Milestone Inspection & Material Testing | Real Estate & Construction |
| W791 | Construction Document Control, Drawing Revision & As-Built Management | Real Estate & Construction |
| W807 | Store Closure, Lease Termination & Asset Recovery Management | Real Estate & Construction |
| W808 | Generator Preventive Maintenance, Fuel Management & Load Testing | Real Estate & Construction |

#### Governance & Assurance

| ID | Workflow | Value Stream |
|---|---|---|
| W490 | Organized Retail Crime (ORC) Investigation & Task Force | Internal Audit & Risk |
| W447 | DTI-BPS Mandatory Product Certification (ICC/SOC) | Compliance & Regulatory |
| W655 | Safety Training & Certification Tracking | Health, Safety & Environment |
| W806 | Annual Fire Safety System Testing, Certification & BFP Compliance | Health, Safety & Environment |
| W692 | Store Energy Efficiency Monitoring & Utility Cost Optimization | ESG & Sustainability |
| W693 | Water Consumption Tracking & Conservation Management | ESG & Sustainability |
| W694 | ESG Data Collection, Validation & Annual Sustainability Report Preparation | ESG & Sustainability |
| W800 | Green Building Certification (BERDE/LEED) & Sustainable Store Design Standards | ESG & Sustainability |
| W801 | ESG Incident Response, Regulatory Citation Management & Stakeholder Communication | ESG & Sustainability |

#### Technology & Data

| ID | Workflow | Value Stream |
|---|---|---|
| W832 | ERP User Access Quarterly Recertification & Compliance Review | IT Operations & Security |
| W879 | Daily Report Distribution & Automated Dashboard Refresh | Data, Analytics & BI |
| W880 | BI Dashboard Development, Enhancement & User Request Management | Data, Analytics & BI |
| W881 | Data Warehouse ETL Job Monitoring & Exception Handling | Data, Analytics & BI |
| W882 | Self-Service BI Governance, Access Provisioning & Training | Data, Analytics & BI |
| W883 | Ad-hoc Analytics Request Fulfillment & SLA Management | Data, Analytics & BI |
| W884 | Data Quality Monitoring, Exception Triage & Remediation | Data, Analytics & BI |
| W885 | Monthly Executive Reporting Package Preparation | Data, Analytics & BI |
| W686 | Document Approval Routing & Digital Signature Management | Innovation & Digital Transformation |
| W687 | Document Template Management & Version Control | Innovation & Digital Transformation |
| W688 | Contract & Agreement Lifecycle Management | Innovation & Digital Transformation |
| W689 | AI/ML Model Governance, Bias Audit & Ethical Review | Innovation & Digital Transformation |
| W690 | Digital Transformation Initiative Portfolio Management | Innovation & Digital Transformation |
| W691 | Emerging Technology Scouting & Proof-of-Concept Evaluation | Innovation & Digital Transformation |

### Statutory-Compliance Classification Pass (192 workflows; VS-79/85/89/91/114/117/118/125)

> **Hand-reviewed 2026-06-20.** The classifier's `FAMILY_DEFAULTS` force all 8 wholly-statutory
> value streams to a blanket Tier 1 proposal. This pass confirms the statutory-*execution*
> workflows as Tier 1 and demotes 38 program-support workflows to Tier 2/3 per the documented
> tier definitions (Tier 2 = standard support / training / reporting / change-monitoring /
> cost-or-insurance recovery; Tier 3 = analytics / continuous-improvement / enhancement-only).
> Result: **154 Tier 1** (statutory execution) · **32 Tier 2** (program support) · **6 Tier 3**
> (analytics/enhancement). The 38 demotions are listed inline below each table block for audit.

#### Tier 1 — Statutory execution (154 workflows)

**Finance** (59)

| ID | Workflow | Value Stream |
|---|---|---|
| W2753 | VAT Output/Input Ledger Reconciliation & Monthly Form 2550M Preparation | VS-79 |
| W2754 | Quarterly VAT Return (2550Q) & Transitional Input Tax Processing | VS-79 |
| W2755 | BIR eFPS Filing, e-Payment (PESONet/InstaPay) & Validation | VS-79 |
| W2756 | BIR EIS E-Invoicing Transmission & Daily Sales Report Sync | VS-79 |
| W2757 | VAT-Exempt & Zero-Rated Sale Documentation (PEZA/BOI/Education/Housing) | VS-79 |
| W2758 | Capital Goods Input VAT Spread (120-Month Amortization) Tracking | VS-79 |
| W2759 | Percentage Tax (2551Q) & Entities Below VAT Threshold Management | VS-79 |
| W2760 | POS BIR-Registered Accreditation, CAS Registration & Compliance Audit | VS-79 |
| W2761 | Expanded Withholding Tax (EWT) Determination & Monthly Form 1601E/1601EQ | VS-79 |
| W2762 | Creditable Withholding Tax (CWT) at Source & Vendor 2307 Issuance | VS-79 |
| W2763 | Customer CWT Collection (2307) & AR Application | VS-79 |
| W2764 | Compensation Withholding Tax (1601C) & TRAIN Tax Table Maintenance | VS-79 |
| W2765 | Annual Information Return (1604E/1604C) & Alphabetical Employee List | VS-79 |
| W2766 | Final Withholding Tax (Interest, Dividends, Rentals) Management | VS-79 |
| W2767 | EWT Rate Master Governance & Tax Code Mapping | VS-79 |
| W2768 | Withholding Tax Reconciliation, 2307 Discrepancy & Vendor Dispute Resolution | VS-79 |
| W2769 | Quarterly Corporate Income Tax (1702Q) & Annual Return (1702RT) Preparation | VS-79 |
| W2770 | Tax-Adjusted Financial Income (TAFI) Schedule & Permanent/Temporary Differences | VS-79 |
| W2771 | Local Business Tax (LBT) Computation & LGU Filing per Location | VS-79 |
| W2772 | Documentary Stamp Tax (DST) on Leases, Loans & Documents | VS-79 |
| W2773 | BIR Tax Audit / LOAN Response & Assessment Contestation | VS-79 |
| W2774 | CREATE / CREATE More Tax Incentive Monitoring & Entity Structure Review | VS-79 |
| W2775 | Tax Provision (PAS/IFRS 12) & Deferred Tax Asset / Liability Reconciliation | VS-79 |
| W2776 | Tax Risk Register, Tax Calendar & Tax Controversy Governance | VS-79 |
| W3689 | Revenue Assurance Program Strategy & Governance | VS-118 |
| W3691 | Sales-to-Cash Reconciliation & Settlement Integrity | VS-118 |
| W3692 | POS Transaction Integrity & Data-Flow Assurance | VS-118 |
| W3693 | Revenue Assurance Controls & Exception Monitoring Framework | VS-118 |
| W3694 | Multi-Channel Revenue Consolidation & Reconciliation | VS-118 |
| W3697 | Pricing Accuracy & Price-Override Integrity Monitoring | VS-118 |
| W3698 | Promotion, Discount & Markdown Integrity Assurance | VS-118 |
| W3699 | Loyalty Points, Gift Card & Stored-Value Integrity | VS-118 |
| W3700 | Mandatory Discount & Tax-Exempt Sale Integrity | VS-118 |
| W3701 | Payment, Tender & Settlement Integrity (MDR/Fees) | VS-118 |
| W3702 | Catch-Weight, Cut-Length & Measurement-Based Revenue Assurance | VS-118 |
| W3703 | Ecommerce, Marketplace & 3P Settlement Revenue Assurance | VS-118 |
| W3704 | Refund, Reversal & Return Leakage Monitoring | VS-118 |
| W3705 | Leakage Detection, Quantification & Root-Cause Analysis | VS-118 |
| W3706 | Revenue Leakage Recovery & Corrective Action | VS-118 |
| W3708 | Fraud, Collusion & Abuse Revenue-Loss Investigation | VS-118 |
| W3709 | Pricing & Promo System Governance & Master-Data Integrity | VS-118 |
| W3711 | Multi-Entity Revenue Assurance & Consolidated Reporting | VS-118 |
| W3857 | Enterprise Fraud Management Strategy, Risk Appetite & Governance | VS-125 |
| W3859 | Fraud Detection Rules, Models & Orchestration Platform | VS-125 |
| W3860 | Fraud Case Management & Investigation Workflow | VS-125 |
| W3861 | Fraud Data, Network Analytics & Consortium/Device Intelligence | VS-125 |
| W3865 | POS / Store Transaction Fraud Monitoring | VS-125 |
| W3866 | Ecommerce & Digital Channel Fraud Prevention | VS-125 |
| W3867 | Returns & Refund Abuse Prevention | VS-125 |
| W3868 | Promotion, Coupon & Loyalty Abuse Prevention | VS-125 |
| W3869 | Gift Card & Stored-Value Fraud Prevention | VS-125 |
| W3870 | Payment, Chargeback & First-Party/Friendly Fraud Management | VS-125 |
| W3871 | Account Takeover & Credential Abuse Prevention | VS-125 |
| W3872 | Trade / B2B Account & Application First-Party Fraud Prevention | VS-125 |
| W3873 | Fraud Investigation, Evidence & Case Adjudication | VS-125 |
| W3874 | Fraud Recovery, Restitution & Asset Recovery | VS-125 |
| W3875 | Chargeback Representment & Dispute Management | VS-125 |
| W3876 | Internal / Employee Fraud & Collusion Investigation | VS-125 |
| W3877 | Fraud Reporting, Regulatory & Law-Enforcement Coordination | VS-125 |

**Governance & Assurance** (95)

| ID | Workflow | Value Stream |
|---|---|---|
| W2897 | SC/PWD/Solo Parent ID Validation & Eligibility Verification at POS | VS-85 |
| W2898 | Mandatory Discount Computation, Stack Rules & Basket Validation | VS-85 |
| W2899 | SC/PWD Purchase Book of Sales Transaction Recording | VS-85 |
| W2900 | Discount Abuse, ID Sharing & Fraud Prevention Monitoring | VS-85 |
| W2901 | Medicine & Prime Commodity Discount Compliance (RA 9994/7394) | VS-85 |
| W2902 | Solo Parent Discount Program Configuration & Eligible-SKU Mapping | VS-85 |
| W2904 | Customer Complaint & DTI/NCSD Escalation Handling | VS-85 |
| W2905 | PEZA/BOI VAT-Zero-Rated Sale Customer Onboarding & Certificate Management | VS-85 |
| W2906 | Government / Diplomatic VAT-Exempt Purchase Documentation | VS-85 |
| W2907 | Educational Institution & Housing (PAG-IBIG) VAT-Exempt Sale Processing | VS-85 |
| W2908 | VAT-Exempt Agricultural/Fisherfolk Input Customer Verification | VS-85 |
| W2909 | Export Sale (Direct/Constructive) Zero-Rating Documentation | VS-85 |
| W2910 | BIR Tax-Exempt Entity Master Maintenance & Renewal Tracking | VS-85 |
| W2911 | Mixed Basket (Taxable + Exempt) Allocation & Apportionment | VS-85 |
| W2912 | VAT-Exempt Sale Invoice, ATC & Disclosure Compliance | VS-85 |
| W2913 | SC/PWD/Solo Parent Tax Credit Computation & Monthly Claim Buildup | VS-85 |
| W2914 | BIR Form 2552 (SC/PWD Book) Quarterly Compilation & Submission | VS-85 |
| W2915 | Tax Credit Certificate (TCC) Application & Tracking | VS-85 |
| W2916 | LGU Local Tax Credit & Real Property Tax Exemption Coordination | VS-85 |
| W2918 | BIR Audit of Statutory Discount Books & Tax Credit Defense | VS-85 |
| W2993 | Product Safety Issue Intake, Triage & Hazard Classification | VS-89 |
| W2994 | Recall Risk Assessment & Corrective Action Decision | VS-89 |
| W2995 | DTI-BPS / FDA Regulatory Notification & Filing | VS-89 |
| W2996 | Recall Strategy, Scope & Lot/Shipment Traceability Definition | VS-89 |
| W2997 | Recall Committee Activation & Cross-Functional Command | VS-89 |
| W2998 | Vendor / Manufacturer Coordination & Corrective Action Agreement | VS-89 |
| W2999 | Recall Effectiveness Check Planning & Sample Design | VS-89 |
| W3000 | Stop-Sale, Quarantine & Inventory Hold Execution | VS-89 |
| W3001 | Multi-Channel Customer Recall Notice & Public Communication | VS-89 |
| W3002 | Store-Level Recall Execution, POS Block & Shelf Removal | VS-89 |
| W3003 | Ecommerce & Marketplace Recall Handling (Listing Block, Buyer Notify) | VS-89 |
| W3004 | Customer Return, Refund, Repair & Replacement Processing (Recall) | VS-89 |
| W3005 | Recall Product Retrieval Logistics & Reverse Consolidation | VS-89 |
| W3006 | Trade / B2B Account Recall Outreach & Bulk Recovery | VS-89 |
| W3007 | Field / Job Site Recall Recovery for Delivered Goods | VS-89 |
| W3008 | Recall Progress Tracking, Daily Status Reporting & Effectiveness Measurement | VS-89 |
| W3010 | Recalled Product Destruction, Recycling & Disposal Compliance | VS-89 |
| W3011 | Recall Root Cause Analysis & CAPA (Corrective & Preventive Action) | VS-89 |
| W3013 | Regulatory Close-Out Reporting (DTI-BPS / FDA) & Recall Termination | VS-89 |
| W3041 | Data Privacy Program Governance, NPC Registration & DPO Operations | VS-91 |
| W3042 | Personal Data Inventory, Data Mapping & Records of Processing Activities (ROPA) | VS-91 |
| W3043 | Consent Capture, Preference Management & Lawful Basis Tracking | VS-91 |
| W3044 | Data Subject Access Request (DSAR) Fulfillment & Verification | VS-91 |
| W3045 | Data Rectification, Erasure & Objection Request Processing | VS-91 |
| W3046 | Marketing Consent, Unsubscribe & Communication Preference Sync | VS-91 |
| W3047 | Loyalty Member Data Portability & Account Data Export | VS-91 |
| W3048 | Minors' Data, Sensitive Data & Special Category Processing Controls | VS-91 |
| W3049 | Privacy Impact Assessment (PIA) & DPIA for New Initiatives | VS-91 |
| W3050 | Cross-Border Transfer Assessment & Adequacy Determination | VS-91 |
| W3051 | Data Processing Agreement (DPA) & Vendor Privacy Due Diligence | VS-91 |
| W3052 | Third-Party Processor Oversight & Privacy Audit | VS-91 |
| W3053 | Data Minimization, Retention & Privacy-by-Design Review | VS-91 |
| W3055 | CCTV / Surveillance Privacy Impact & Signage Compliance | VS-91 |
| W3057 | Personal Data Breach Detection, Triage & Incident Activation | VS-91 |
| W3058 | Breach Containment, Forensic Investigation & Scope Assessment | VS-91 |
| W3059 | NPC Breach Notification (72-Hour) & Regulatory Reporting | VS-91 |
| W3060 | Affected Data Subject Notification & Remediation | VS-91 |
| W3064 | Data Privacy Audit, NPC Investigation Response & Remediation | VS-91 |
| W3593 | DG/Hazmat Compliance Program Strategy & Governance | VS-114 |
| W3594 | DG Product Classification (UN/IMDG/IATA/ADR) & Master Data | VS-114 |
| W3595 | Hazmat Inventory, SDS & Chemical Information Management | VS-114 |
| W3598 | DG Transport Packaging, Marking & Labeling Standards | VS-114 |
| W3599 | DG Procurement, Vendor & Import Compliance | VS-114 |
| W3601 | DG Transport Carrier Qualification & Contracting | VS-114 |
| W3602 | DG Transport Documentation & Manifest Management | VS-114 |
| W3603 | DG Ocean / Air / Road Modal Transport Compliance | VS-114 |
| W3604 | DG Ecommerce Ship-Eligibility & Channel Rules | VS-114 |
| W3605 | DG Last-Mile & 3PL DG Shipping Management | VS-114 |
| W3606 | DG Transport Incident, Spill & Emergency Response | VS-114 |
| W3607 | DG Transport Permit, Escort & Port / Airport Handling | VS-114 |
| W3609 | DG Storage Compliance & Fixed-Site Risk Management | VS-114 |
| W3610 | DG Handling Procedures, PPE & Worker Safety | VS-114 |
| W3611 | DG Spill Response, Containment & Remediation | VS-114 |
| W3612 | DG Hazardous Waste Transport, Disposal & DENR-EMB Manifest | VS-114 |
| W3613 | DG Incident Investigation, Reporting & Regulatory Notification | VS-114 |
| W3614 | DG Site Permitting, Fire Code & BFP Compliance | VS-114 |
| W3665 | DTI-BPS Certification Program Strategy & Governance | VS-117 |
| W3666 | Regulated-Product Identification & BPS Standards Mapping | VS-117 |
| W3667 | Vendor/Manufacturer PS Mark License Management | VS-117 |
| W3668 | Product Standards Technical File & Documentation Management | VS-117 |
| W3669 | New-Product Certification & Assortment Compliance Gate | VS-117 |
| W3670 | Vendor Certification Audit, Verification & PS License Renewal | VS-117 |
| W3673 | Import ICC/SOC Application & I-SEAL Portal Management | VS-117 |
| W3674 | Shipment Documentation & BPS Documentary Review | VS-117 |
| W3675 | DTI Inspection, Sampling & Witness Coordination | VS-117 |
| W3676 | Accredited Laboratory Testing & Results Management | VS-117 |
| W3677 | ICC/SOC Certificate Issuance & Customs Release Coordination | VS-117 |
| W3678 | ICC Sticker Procurement, Control & Application | VS-117 |
| W3679 | Sample Failure, Re-export & Disposition Management | VS-117 |
| W3681 | In-Market Compliance Monitoring & Store Shelf Audit | VS-117 |
| W3682 | DTI Market Surveillance Response & Oplan Coordination | VS-117 |
| W3683 | Consumer Complaint & Certification Non-Conformance Investigation | VS-117 |
| W3684 | Stop-Sale, Withdrawal & Certification Corrective Action | VS-117 |
| W3686 | Vendor Recovery, Penalty & Certification Chargeback | VS-117 |
| W3687 | Multi-Entity Certification Coordination & Reporting | VS-117 |


#### Tier 2 — Program support (32 workflows)

**Finance** (11)

| ID | Workflow | Value Stream |
|---|---|---|
| W3690 | Revenue Leakage Taxonomy & Risk Mapping | VS-118 |
| W3695 | Revenue Assurance Policy, Authority & Approval Matrix | VS-118 |
| W3696 | Revenue Assurance Audit, Documentation & Records | VS-118 |
| W3707 | Revenue Assurance Analytics & KPI Reporting | VS-118 |
| W3858 | Fraud Risk Assessment & Cross-Channel Fraud Typology Catalog | VS-125 |
| W3862 | Fraud Policy, Rules Lifecycle & Model Governance | VS-125 |
| W3863 | Fraud Vendor & Third-Party Data/Tool Governance | VS-125 |
| W3864 | Fraud Program Budget, Reporting & Continuous Improvement | VS-125 |
| W3878 | Fraud Controls Assurance & Audit Support | VS-125 |
| W3879 | Fraud Awareness Training & Store/Agent Enablement | VS-125 |
| W3880 | Fraud Analytics, Loss Rates & Program KPI Reporting | VS-125 |

**Governance & Assurance** (21)

| ID | Workflow | Value Stream |
|---|---|---|
| W2903 | Staff Training, ID Recognition & Customer Service Protocol | VS-85 |
| W2917 | Discount Cost Allocation, Store Margin Impact & Reimbursement Policy | VS-85 |
| W2919 | Mandatory Discount Regulatory Change Monitoring & Policy Update | VS-85 |
| W2920 | Statutory Discount Program KPI, Cost & Compliance Reporting | VS-85 |
| W3009 | Vendor Reimbursement, Credit & Cost Recovery for Recalls | VS-89 |
| W3012 | Post-Recall Surveillance & Re-Occurrence Monitoring | VS-89 |
| W3014 | Recall Records Retention, Documentation & Audit File | VS-89 |
| W3015 | Recall Insurance Claim & Recovery Processing | VS-89 |
| W3054 | De-identification, Anonymization & Test Data Management | VS-91 |
| W3056 | Privacy Awareness Training & Employee Compliance Program | VS-91 |
| W3061 | Cyber Insurance Coordination & Breach Cost Recovery | VS-91 |
| W3062 | Breach Post-Incident Review & Corrective Action | VS-91 |
| W3063 | Privacy Metrics, Compliance Reporting & DPO Board Reporting | VS-91 |
| W3596 | DG Regulatory Intelligence & Compliance Monitoring | VS-114 |
| W3597 | DG Training, Certification & Competency Management | VS-114 |
| W3600 | DG Program Audit, Documentation & Records | VS-114 |
| W3608 | DG Transport Audit, Carrier Performance & Analytics | VS-114 |
| W3615 | DG Insurance, Liability & Risk Transfer | VS-114 |
| W3671 | BPS Standards Monitoring & Regulatory Change Management | VS-117 |
| W3672 | Certification Records, Reporting & Program Audit | VS-117 |
| W3680 | Testing Laboratory Relationship, Accreditation & Cost Management | VS-117 |


#### Tier 3 — Analytics / enhancement (6 workflows)

**Finance** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W3710 | Revenue Assurance Technology, Tooling & Automation | VS-118 |
| W3712 | Revenue Assurance Maturity & Continuous Improvement | VS-118 |

**Governance & Assurance** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3016 | Recall Lessons Learned, Process & Quality System Improvement | VS-89 |
| W3616 | DG Compliance Analytics, Loss-Event Review & Continuous Improvement | VS-114 |
| W3685 | Certification Cost, Lead-Time & Landed-Cost Analytics | VS-117 |
| W3688 | Certification Program Analytics & Continuous Improvement | VS-117 |


**Demotion audit (38 workflows moved off the classifier's blanket Tier 1):**

- **→ Tier 2** (32): W2903, W2917, W2919, W2920, W3009, W3012, W3014, W3015, W3054, W3056, W3061, W3062, W3063, W3596, W3597, W3600, W3608, W3615, W3671, W3672, W3680, W3690, W3695, W3696, W3707, W3858, W3862, W3863, W3864, W3878, W3879, W3880
- **→ Tier 3** (6): W3016, W3616, W3685, W3688, W3710, W3712

---

### Support & Governance Classification Pass (192 workflows; VS-100/104/112/113/126/129/133/139)

> **Hand-reviewed 2026-06-20 (batch 2).** Eight family-decisive Tier-2 VSs (legal operations,
> government affairs, PMO, enterprise architecture, customer-data platform, competition/
> antitrust, operational excellence, trade-show marketing). The classifier's conservative
> default put nearly all of these at Tier 2; genuine review against the tier definitions —
> **calibrated to the existing register's placement** of optimization/analytics workflows in
> Tier 3 (Route Optimization, Cost Optimization, Assortment Optimization, Retail Analytics &
> AI, QAIP) and operational performance reviews in Tier 2 — yields:
> **14 Tier 1** (statutory execution the keyword rules missed) · **149 Tier 2** (confirmed
> standard support) · **29 Tier 3** (analytics / optimization / enhancement defaulted to T2).
> The 14 promotions and 29 demotions are audited below; the remaining 149 confirm the
> classifier's Tier 2 default. Result moves Check 1 unclassified 3,644 → 3,452.

#### Tier 1 — Statutory execution (14 workflows)

**Governance & Assurance** (12)

| ID | Workflow | Value Stream |
|---|---|---|
| W3261 | Settlement, Judgment & Loss Accrual Accounting | VS-100 |
| W3262 | Litigation Hold Initiation & Evidence Coordination | VS-100 |
| W3263 | Court Filing, Service & Judgment Enforcement | VS-100 |
| W3275 | Legal Entity Management & Corporate Secretarial Support | VS-100 |
| W3276 | Regulatory & Government Investigation Defense | VS-100 |
| W3277 | Legal Risk Register, Loss Contingency & Disclosure | VS-100 |
| W3360 | Political-Activity Compliance, Lobbying Disclosure & Ethics | VS-104 |
| W3967 | Merger, Acquisition & Joint-Venture Notification (PCC Pre-Filing) Control | VS-129 |
| W3970 | Competition Inquiry, Dawn Raid & Information Request Response | VS-129 |
| W3971 | PCC Investigation, Preliminary Inquiry & Motu Proprio Matter Defense | VS-129 |
| W3973 | Competition Litigation, Appeal (Court of Appeals / SC) & Judgment Management | VS-129 |
| W3974 | Competition Penalty, Fine & Damages Payment & Disclosure Management | VS-129 |

**Technology & Data** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W3900 | Data Subject Access Request (DSAR) & Consumer Rights Workflow | VS-126 |

**Sell & Serve** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W4198 | Event Compliance, Permits & Promo-Prize Governance | VS-139 |


#### Tier 2 — Standard support (149 workflows)

**Governance & Assurance** (68)

| ID | Workflow | Value Stream |
|---|---|---|
| W3257 | Legal Matter Intake, Triage & Matter Master | VS-100 |
| W3258 | Litigation Case Lifecycle & Pre-Trial Management | VS-100 |
| W3259 | Outside Counsel Selection, Engagement & Billing | VS-100 |
| W3260 | Alternative Dispute Resolution, Arbitration & Mediation | VS-100 |
| W3265 | Trademark, Copyright & Industrial Design Portfolio Strategy | VS-100 |
| W3266 | Trademark Search, Prosecution & IPOPHL Filing | VS-100 |
| W3267 | IP Renewal, Maintenance & Portfolio Lifecycle | VS-100 |
| W3268 | IP Enforcement, Cease-and-Desist & Infringement Action | VS-100 |
| W3269 | Brand Licensing, Franchise & IP Commercialization | VS-100 |
| W3270 | Trade Secret, Confidentiality & Non-Disclosure Management | VS-100 |
| W3271 | Domain Name, Anti-Cybersquatting & Digital IP Protection | VS-100 |
| W3273 | Contract Template, Clause Library & Legal Review Support | VS-100 |
| W3274 | Contract Lifecycle Support & Obligation Tracking | VS-100 |
| W3278 | Ethics, Whistleblower & Investigation Case Management | VS-100 |
| W3279 | Legal Operations Technology & e-Billing | VS-100 |
| W3353 | National Government Stakeholder Mapping & Relationship Management | VS-104 |
| W3354 | Legislative & Regulatory Monitoring, Horizon Scanning & Impact Assessment | VS-104 |
| W3355 | Public Policy Position Development & Advocacy Campaign Execution | VS-104 |
| W3356 | Congressional & Executive-Agency Engagement (DTI/DOLE/BIR/BSP/NTC etc.) | VS-104 |
| W3357 | Policy Submission, Consultation & Position-Paper Filing | VS-104 |
| W3358 | Cross-Industry Coalition Building & Joint Advocacy | VS-104 |
| W3359 | Government Affairs Calendar, Briefing & Executive Liaison | VS-104 |
| W3361 | Industry Association Membership Strategy, Selection & Dues Management | VS-104 |
| W3362 | Trade Association Leadership, Committee & Board Representation | VS-104 |
| W3363 | Industry Standard, Code & Best-Practice Development Participation | VS-104 |
| W3364 | Peer-Retailer Benchmarking, Knowledge Exchange & Industry Research | VS-104 |
| W3365 | Industry Event, Conference & Award Program Participation | VS-104 |
| W3366 | Supplier/Channel Industry Forum & Ecosystem Engagement | VS-104 |
| W3367 | Association Sponsorship, Partnership & ROI Evaluation | VS-104 |
| W3368 | Industry Relations Performance & Influence Reporting | VS-104 |
| W3369 | Public Affairs Strategy & Issue Management (Non-Crisis) | VS-104 |
| W3370 | Corporate Positioning & Stakeholder Narrative Development | VS-104 |
| W3371 | Community Relations & Local Stakeholder Engagement (National Brand Level) | VS-104 |
| W3372 | Think-Tank, Academic & Policy-Institution Partnership | VS-104 |
| W3373 | Media & Analyst Relations for Policy/Industry Topics | VS-104 |
| W3374 | Corporate Political & Regulatory Risk Assessment | VS-104 |
| W3376 | External-Affairs Annual Plan, KPI & Board Reporting | VS-104 |
| W3953 | Competition & Antitrust Compliance Program Strategy, Governance & Operating Model | VS-129 |
| W3954 | Market Definition, Market Share & Market Power Assessment | VS-129 |
| W3955 | Pricing & Promotional Conduct Competition Risk Assessment | VS-129 |
| W3956 | Vendor / Trade-Partner Vertical-Restraint & RPM Risk Assessment | VS-129 |
| W3957 | Association, Trade-Body & Competitor-Interaction Risk Assessment | VS-129 |
| W3958 | Procurement, Buyer-Power & Supplier-Coordination Risk Assessment | VS-129 |
| W3959 | Digital, Marketplace & Platform Competition Risk Assessment | VS-129 |
| W3960 | Competition Law Training, Awareness & Culture Program | VS-129 |
| W3961 | Pricing Decision & Competitor-Information-Exchange Controls | VS-129 |
| W3962 | Vendor Agreement, RPM & Exclusivity Clause Review & Contract Controls | VS-129 |
| W3963 | Joint Venture, Strategic Alliance & Cooperation Agreement Clearance | VS-129 |
| W3964 | Trade / B2B Distribution, Resale & Channel Pricing Compliance Controls | VS-129 |
| W3965 | Association Meeting & Industry-Gathering Compliance Protocol | VS-129 |
| W3966 | Market-Allocation, Customer-Allocation & Territory Conduct Controls | VS-129 |
| W3968 | Competition Compliance Monitoring, Audit & Continuous Improvement | VS-129 |
| W3969 | Philippine Competition Commission (PCC) Relationship & Engagement Management | VS-129 |
| W3972 | Leniency, Settlement & Commitment (Whistleblower) Program Management | VS-129 |
| W3975 | Remediation, Conduct Change & Compliance-Monitoring Implementation | VS-129 |
| W4049 | Operational Excellence Strategy, Charter & Operating Model | VS-133 |
| W4050 | Enterprise Process Architecture, Ownership & RACI Governance | VS-133 |
| W4051 | Continuous Improvement Methodology Standards (Lean / Six Sigma / Kaizen) | VS-133 |
| W4052 | Improvement Opportunity Pipeline & Prioritization (Impact-Effort) | VS-133 |
| W4053 | Cross-Functional Improvement Project Governance & Stage-Gate | VS-133 |
| W4054 | Process KPI Library, Baseline Measurement & Target Setting | VS-133 |
| W4055 | OpEx Capability Building, Green Belt / Black Belt Certification | VS-133 |
| W4056 | Continuous Improvement Culture, Suggestion System & Recognition | VS-133 |
| W4057 | Process Discovery & End-to-End Process Mapping | VS-133 |
| W4060 | Process Re-Design, Standard Work & SOP Authoring | VS-133 |
| W4063 | Control Design & Re-Engineering for Risk Reduction | VS-133 |
| W4064 | Improvement Rollout, Change Management & Sustainment | VS-133 |
| W4071 | Improvement Project Portfolio Review & Lessons Learned | VS-133 |

**Asset & Infrastructure** (22)

| ID | Workflow | Value Stream |
|---|---|---|
| W3545 | Enterprise Project Portfolio Strategy & Governance | VS-112 |
| W3546 | Project Intake, Classification & Portfolio Registration | VS-112 |
| W3547 | Project Prioritization, Scoring & Resource Allocation | VS-112 |
| W3548 | Stage-Gate Methodology & Project Lifecycle Standards | VS-112 |
| W3549 | Program Management (Multi-Project Initiatives) | VS-112 |
| W3550 | Project Portfolio Risk, Dependency & Conflict Management | VS-112 |
| W3551 | Project Approval, Charter & Business Case Governance | VS-112 |
| W3552 | Portfolio Dashboards, Reporting & Executive / Board Oversight | VS-112 |
| W3553 | Project Manager Assignment, Resource & Capacity Planning | VS-112 |
| W3554 | Project Planning, Scheduling & WBS Management | VS-112 |
| W3555 | Project Budget & Cost Control | VS-112 |
| W3556 | Project Scope, Change & Configuration Management | VS-112 |
| W3557 | Project Quality, Deliverable & Acceptance Management | VS-112 |
| W3558 | Project Risk, Issue & Decision Management | VS-112 |
| W3559 | Project Communications & Stakeholder Management | VS-112 |
| W3560 | Project Closure, Handover & Lessons Learned | VS-112 |
| W3561 | Project Benefits Realization Tracking & Validation | VS-112 |
| W3562 | Project Management Information System (PMIS) & Tooling | VS-112 |
| W3564 | Program / Project Financial Performance vs Business Case | VS-112 |
| W3566 | Project Management Standards, Templates & Methodology | VS-112 |
| W3567 | Vendor / Contractor Project Performance & Governance | VS-112 |
| W3568 | Enterprise Transformation & Change Management Portfolio | VS-112 |

**Technology & Data** (37)

| ID | Workflow | Value Stream |
|---|---|---|
| W3569 | Enterprise Architecture Strategy, Framework & Governance | VS-113 |
| W3570 | Architecture Principles, Standards & Reference Architecture | VS-113 |
| W3571 | Architecture Review Board & Solution Architecture Review | VS-113 |
| W3572 | Technology Standards & Approved Technology List | VS-113 |
| W3573 | Architecture Compliance, Exception & Waiver Management | VS-113 |
| W3574 | Architecture Capability, Skills & Center of Excellence | VS-113 |
| W3575 | Architecture Repository, Documentation & Knowledge Management | VS-113 |
| W3577 | Application Portfolio Management & Rationalization | VS-113 |
| W3578 | Application Lifecycle, Retirement & Technical Debt Management | VS-113 |
| W3579 | Integration Architecture & API Strategy | VS-113 |
| W3580 | Solution Architecture for New Initiatives & Projects | VS-113 |
| W3581 | Data Architecture & Information Strategy | VS-113 |
| W3582 | Cloud & Infrastructure Architecture | VS-113 |
| W3583 | Security Architecture | VS-113 |
| W3584 | Architecture for ERP Platform & Core Systems Evolution | VS-113 |
| W3585 | Technology Strategy & Multi-Year Technology Roadmap | VS-113 |
| W3587 | Architecture for Digital Transformation Programs | VS-113 |
| W3588 | Technology Investment Governance & Architecture ROI | VS-113 |
| W3589 | Vendor & Platform Strategy for Enterprise Systems | VS-113 |
| W3590 | Architecture Risk, Resilience & Disaster-Recovery Design | VS-113 |
| W3591 | Enterprise Architecture Stakeholder Engagement & Communication | VS-113 |
| W3881 | CDP Strategy, Architecture & Governance | VS-126 |
| W3882 | Customer Data Ingestion & Source-System Integration | VS-126 |
| W3883 | Customer Identity Resolution & Profile Stitching | VS-126 |
| W3884 | Customer Golden Record & Master Profile Management | VS-126 |
| W3885 | Customer Consent, Preference & Compliance Center | VS-126 |
| W3886 | Customer Data Quality, Deduplication & Hygiene | VS-126 |
| W3887 | CDP Data Model, Taxonomy & Segmentation Foundation | VS-126 |
| W3888 | CDP Platform Operations, Security & Access Governance | VS-126 |
| W3889 | Customer Segmentation & Targeting Operations | VS-126 |
| W3891 | Audience Activation & Cross-Channel Syndication | VS-126 |
| W3893 | Customer Journey Orchestration & Trigger Management | VS-126 |
| W3897 | Customer 360 Consumption & Self-Service Access | VS-126 |
| W3898 | B2B / Trade & Key-Account Profile Enrichment | VS-126 |
| W3899 | Loyalty Program Data & Tier/Behavior Enrichment | VS-126 |
| W3901 | Customer Data Privacy, Consent Audit & DPIA | VS-126 |
| W3902 | Customer Data Retention, Archival & Purge | VS-126 |

**Sell & Serve** (22)

| ID | Workflow | Value Stream |
|---|---|---|
| W4193 | Event Marketing Strategy & Channel Role | VS-139 |
| W4194 | Annual Event Portfolio & Calendar Planning | VS-139 |
| W4195 | Event Budget, Business Case & Sponsorship Funding | VS-139 |
| W4196 | Event Audience, Targeting & Trade-Pro Invitation | VS-139 |
| W4197 | Vendor Co-Funding, Co-Exhibition & MDF Coordination | VS-139 |
| W4199 | Event Cross-Functional Team & Resource Planning | VS-139 |
| W4200 | Event Brief, Objectives & Success-Metric Definition | VS-139 |
| W4201 | Booth/Stand Design, Build & Logistics | VS-139 |
| W4202 | Show Registration, Sponsorship & Space Contracting | VS-139 |
| W4203 | Product Display, Demo & Sample Coordination | VS-139 |
| W4204 | On-Site Sales, Engagement & Lead Capture | VS-139 |
| W4205 | Hospitality, VIP & Account-Manager Meetings | VS-139 |
| W4206 | Event Travel, Accommodation & Per-Diem Management | VS-139 |
| W4207 | Show Teardown, Asset Recovery & Return Logistics | VS-139 |
| W4208 | Health, Safety & Incident Management at Events | VS-139 |
| W4209 | Hosted Trade Day & Contractor Event Operations | VS-139 |
| W4210 | Product Launch & New-Arrival Showcase Events | VS-139 |
| W4211 | Store Grand-Opening & In-Store Event Marketing | VS-139 |
| W4212 | Partner, Association & Sponsored-Event Management | VS-139 |
| W4213 | Digital & Hybrid Event / Webinar Operations | VS-139 |
| W4214 | Lead Capture, Qualification & CRM Routing | VS-139 |
| W4215 | Post-Event Nurture, Follow-Up & Sales Conversion | VS-139 |


#### Tier 3 — Analytics / optimization / enhancement (29 workflows)

**Governance & Assurance** (16)

| ID | Workflow | Value Stream |
|---|---|---|
| W3264 | Legal Matter Analytics & Loss Forecasting | VS-100 |
| W3272 | IP Portfolio Valuation & Risk Analytics | VS-100 |
| W3280 | Legal Department Performance & Cost Analytics | VS-100 |
| W3375 | Government Affairs & Industry-Relations Budget, Spend & Analytics | VS-104 |
| W3976 | Competition Compliance Program Analytics, Reporting & Board Oversight | VS-129 |
| W4058 | Process Mining & Task Mining from ERP/System Event Logs | VS-133 |
| W4059 | Bottleneck, Root-Cause & Value-Stream Analysis | VS-133 |
| W4061 | Improvement Pilot Design, Execution & Hypothesis Testing | VS-133 |
| W4062 | Process Automation & Digitization Opportunity Scoping | VS-133 |
| W4065 | Benefit Case Modeling, Tracking & Realization Reporting | VS-133 |
| W4066 | Process Performance Monitoring & Control Tower Dashboard | VS-133 |
| W4067 | Productivity & Labor Efficiency Improvement Program | VS-133 |
| W4068 | Cost-Out / Cost-Reduction Program Management | VS-133 |
| W4069 | Cycle-Time, Throughput & Lead-Time Improvement Tracking | VS-133 |
| W4070 | Quality, Defect & Rework Reduction Program | VS-133 |
| W4072 | OpEx Maturity Assessment & Annual Program Review | VS-133 |

**Asset & Infrastructure** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W3563 | Project Portfolio Performance & KPI Analytics | VS-112 |
| W3565 | PMO Maturity Assessment & Continuous Improvement | VS-112 |

**Technology & Data** (10)

| ID | Workflow | Value Stream |
|---|---|---|
| W3576 | Architecture Maturity Assessment & Continuous Improvement | VS-113 |
| W3586 | Emerging Technology Evaluation & Adoption Governance | VS-113 |
| W3592 | Architecture Metrics, Portfolio Health & Technology Analytics | VS-113 |
| W3890 | Real-Time Customer Profile & Next-Best-Action Serving | VS-126 |
| W3892 | Personalization & Recommendation Engine Operations | VS-126 |
| W3894 | Customer Lifetime Value, Churn & Propensity Modeling | VS-126 |
| W3895 | Marketing Analytics, Attribution & Experimentation | VS-126 |
| W3896 | Campaign & Offer Measurement (Lift, ROI) | VS-126 |
| W3903 | Customer Analytics & Insights Reporting | VS-126 |
| W3904 | CDP Value Realization, ROI & Continuous Improvement | VS-126 |

**Sell & Serve** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W4216 | Event Performance, ROI & Portfolio Analytics | VS-139 |


**Promotion audit (14 → Tier 1, statutory execution the keyword rules missed):**

- **Governance & Assurance** (12): W3261, W3262, W3263, W3275, W3276, W3277, W3360, W3967, W3970, W3971, W3973, W3974
- **Technology & Data** (1): W3900
- **Sell & Serve** (1): W4198

**Demotion audit (29 → Tier 3, analytics/optimization defaulted to Tier 2):**

- **Governance & Assurance** (16): W3264, W3272, W3280, W3375, W3976, W4058, W4059, W4061, W4062, W4065, W4066, W4067, W4068, W4069, W4070, W4072
- **Asset & Infrastructure** (2): W3563, W3565
- **Technology & Data** (10): W3576, W3586, W3592, W3890, W3892, W3894, W3895, W3896, W3903, W3904
- **Sell & Serve** (1): W4216

---

### Operational Support Classification Pass (192 workflows; VS-40/43/55/63/64/65/83/84)

> **Hand-reviewed 2026-06-20 (batch 3).** Eight family-decisive Tier-2 VSs spanning capex
> project accounting, trade-professional program, planogram & space optimization, store
> communication, seasonal merchandise, e-commerce marketplace, occupational health, and
> labor relations. Genuine review yields **21 → Tier 1** (statutory execution: PFRS capex
> accounting, DOLE occupational-health reporting, DOLE/NLRC labor-relations mandatory
> processes, emergency-communication protocol), **30 → Tier 3** (analytics: space/productivity/
> clearance/post-season/channel analysis, churn prediction, ROI analytics, engagement surveys),
> and **141 confirmed Tier 2** (the core operational/program-management workflows).
> Result moves Check 1 unclassified 3,452 → 3,260.

#### Tier 1 — Statutory execution (21 workflows)

**Finance** (3)

| ID | Workflow | Value Stream |
|---|---|---|
| W1823 | Project Cost Capitalization vs. Expense Determination | VS-40 |
| W1824 | Capitalized Interest Calculation & Recording | VS-40 |
| W1829 | CIP-to-Fixed Asset Conversion Processing | VS-40 |

**Sell & Serve** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W2360 | Emergency Communication Protocol | VS-63 |

**People** (17)

| ID | Workflow | Value Stream |
|---|---|---|
| W2850 | Workplace Injury / Illness First Aid & Medical Case Opening | VS-83 |
| W2852 | SSS EC / Sickness Benefit & PhilHealth Claim Coordination | VS-83 |
| W2853 | Work-Relatedness Determination & EC Claim Documentation (DOLE) | VS-83 |
| W2858 | Annual / Periodic Medical Examination (APE) Program Execution | VS-83 |
| W2859 | DOLE-Required Periodic Exam by Hazard Category (Chemical/Physical/Biological) | VS-83 |
| W2863 | DOLE Annual Medical Report (AMR) & OHS Statistics Compilation | VS-83 |
| W2864 | Workplace Exposure Monitoring (Noise/Air/Chemical) & DOLE Compliance | VS-83 |
| W2866 | Mental Health Act (RA 11036) Compliance & DOH Mental Health Program | VS-83 |
| W2873 | Labor Organization Certification, Recognition & Verification (DOLE) | VS-84 |
| W2875 | CBA Negotiation Sessions, Deadlock Management & DOLE Conciliation | VS-84 |
| W2876 | CBA Drafting, Ratification, Registration & Publication | VS-84 |
| W2883 | Preventive Suspension, Due Process & Notice Workflow (2-Notice Rule) | VS-84 |
| W2884 | Disciplinary Investigation, Hearing & Decision | VS-84 |
| W2885 | DOLE Conciliation-Mediation (SENA) & Single-Entry Approach | VS-84 |
| W2886 | Labor Arbitration, NLRC Representation & Appeal Management | VS-84 |
| W2887 | Illegal Dismissal, Reinstatement & Backpay Compliance Execution | VS-84 |
| W2888 | Strike / Lockout Notice, Contingency & Resolution | VS-84 |


#### Tier 2 — Operational support (141 workflows)

**Finance** (19)

| ID | Workflow | Value Stream |
|---|---|---|
| W1811 | Capital Expenditure Request Submission | VS-40 |
| W1812 | Capex Financial Evaluation & Business Case Review | VS-40 |
| W1813 | Capex Approval Workflow & Authorization | VS-40 |
| W1814 | Capex Budget Allocation & Commitment Tracking | VS-40 |
| W1815 | Capex Request Revision & Scope Change Management | VS-40 |
| W1816 | Emergency Capex Request Processing | VS-40 |
| W1817 | Capex Requisition to Purchase Order Conversion | VS-40 |
| W1818 | Capex Approval Documentation & Audit Trail | VS-40 |
| W1819 | Project Cost Capture & Allocation | VS-40 |
| W1820 | Construction Progress Payment & Contractor Billing | VS-40 |
| W1821 | Project Material & Equipment Cost Tracking | VS-40 |
| W1822 | Professional Service & Consulting Fee Tracking | VS-40 |
| W1825 | Project Budget vs. Actual Variance Reporting | VS-40 |
| W1826 | Multi-Entity Project Cost Allocation | VS-40 |
| W1827 | Construction-in-Progress (CIP) Account Management | VS-40 |
| W1828 | Project Completion Certification & Asset Turnover | VS-40 |
| W2749 | Partial Asset Turnover (Phased Project Completion) | VS-40 |
| W2750 | Abandoned Project Write-Off & Cost Recovery | VS-40 |
| W2751 | Project Closeout Documentation & Archiving | VS-40 |

**Sell & Serve** (76)

| ID | Workflow | Value Stream |
|---|---|---|
| W1878 | Trade Professional Account Application & Onboarding | VS-43 |
| W1879 | Trade Account Annual Recertification & Tier Review | VS-43 |
| W1880 | Trade Account Manager Assignment & Coverage Planning | VS-43 |
| W1881 | Trade Account Quarterly Business Review & Relationship Health Assessment | VS-43 |
| W1882 | Trade Account Dormancy Detection & Reactivation Campaign | VS-43 |
| W1884 | Trade Account Offboarding & Account Closure | VS-43 |
| W1885 | Trade Account Master Data Quality & Segmentation Review | VS-43 |
| W1886 | Contractor Loyalty Program Tier Design & Benefit Structure Management | VS-43 |
| W1887 | Contractor Points Earning, Redemption & Statement Management | VS-43 |
| W1888 | Contractor Volume Rebate & Spend-Based Incentive Calculation | VS-43 |
| W1889 | Contractor Referral Program & New Account Acquisition Incentive | VS-43 |
| W1890 | Contractor Early Payment Discount & Supply Chain Finance Program | VS-43 |
| W1891 | Contractor Seasonal Promotion & Project Bundle Pricing Execution | VS-43 |
| W1893 | Contractor Loyalty Program Financial Governance & Liability Management | VS-43 |
| W1894 | Trade Professional Product Training Program Planning & Execution | VS-43 |
| W1895 | Contractor Skills Workshop & Certification Event Management | VS-43 |
| W1896 | Trade Community Online Forum & Knowledge Base Management | VS-43 |
| W1897 | Vendor-Sponsored Trade Seminar & Product Demo Coordination | VS-43 |
| W1898 | Contractor Advisory Board & Feedback Program | VS-43 |
| W1899 | Trade Show Participation & Industry Event Representation | VS-43 |
| W1900 | Contractor Safety Training & Compliance Certification Support | VS-43 |
| W1901 | Trade Professional Recognition Awards & Community Building | VS-43 |
| W2166 | Seasonal Planogram Refresh | VS-55 |
| W2167 | New Product Shelf Placement | VS-55 |
| W2168 | Cross-Merchandising Display Planning | VS-55 |
| W2170 | Planogram Version Control | VS-55 |
| W2171 | Store Layout Zone Optimization | VS-55 |
| W2172 | Category Adjacency Planning | VS-55 |
| W2174 | Planogram Compliance Audit | VS-55 |
| W2175 | Photo-Based Remote Compliance Check | VS-55 |
| W2176 | Shelf Label & Price Accuracy Audit | VS-55 |
| W2177 | Endcap & Promotional Display Compliance | VS-55 |
| W2179 | Fixture & Display Equipment Inventory | VS-55 |
| W2180 | Store Cleanliness & Visual Standards Audit | VS-55 |
| W2181 | Planogram Change Implementation Tracking | VS-55 |
| W2183 | Fixture Procurement & Budgeting | VS-55 |
| W2184 | Shelf Capacity & Stocking Optimization | VS-55 |
| W2186 | Store Format Segmentation | VS-55 |
| W2187 | Seasonal Display Space Rotation | VS-55 |
| W2358 | Corporate Announcement Broadcasting | VS-63 |
| W2359 | Merchandising Directive Communication | VS-63 |
| W2361 | Weekly Store Manager Newsletter | VS-63 |
| W2362 | Two-Way Store Feedback Channel | VS-63 |
| W2363 | Policy & Procedure Update Distribution | VS-63 |
| W2364 | Seasonal Preparation Communication Package | VS-63 |
| W2365 | Communication Platform Training & Support | VS-63 |
| W2366 | Task Creation & Assignment from HQ | VS-63 |
| W2367 | Store-Level Task Execution & Reporting | VS-63 |
| W2368 | Task Compliance Dashboard | VS-63 |
| W2369 | Regional Operations Follow-Up | VS-63 |
| W2370 | Task Template & Standardization Management | VS-63 |
| W2371 | Task Completion Quality Audit | VS-63 |
| W2372 | Seasonal Task Calendar Management | VS-63 |
| W2376 | Store Manager Satisfaction Survey | VS-63 |
| W2378 | Information Overload Assessment | VS-63 |
| W2380 | Store Communication Best Practice Sharing | VS-63 |
| W2381 | Communication Strategy Annual Review | VS-63 |
| W2406 | Marketplace Platform Selection & Registration | VS-65 |
| W2407 | Marketplace Store Setup & Branding | VS-65 |
| W2408 | Marketplace Catalog & Pricing Configuration | VS-65 |
| W2409 | Marketplace API Integration | VS-65 |
| W2410 | Marketplace Promotional Campaign Setup | VS-65 |
| W2411 | Marketplace Customer Service Setup | VS-65 |
| W2412 | Marketplace Inventory Allocation Strategy | VS-65 |
| W2413 | Marketplace Channel Performance Baseline | VS-65 |
| W2414 | Marketplace Order Download & Processing | VS-65 |
| W2415 | Marketplace Inventory Synchronization | VS-65 |
| W2416 | Marketplace Fulfillment & Shipping | VS-65 |
| W2417 | Marketplace Return & Refund Processing | VS-65 |
| W2418 | Marketplace Pricing Sync & Competitor Monitoring | VS-65 |
| W2419 | Marketplace Listing Quality Management | VS-65 |
| W2420 | Marketplace Stock-Out Prevention | VS-65 |
| W2421 | Marketplace Customer Review Management | VS-65 |
| W2422 | Marketplace Financial Reconciliation | VS-65 |
| W2428 | Marketplace Platform Relationship Management | VS-65 |
| W2429 | Marketplace Strategy Annual Review | VS-65 |

**Plan & Source** (18)

| ID | Workflow | Value Stream |
|---|---|---|
| W2382 | Seasonal Assortment Planning | VS-64 |
| W2383 | Seasonal Inventory Positioning at DCs | VS-64 |
| W2384 | Seasonal Planogram & Display Setup | VS-64 |
| W2385 | Seasonal Pricing & Promotion Setup | VS-64 |
| W2386 | Seasonal Staff Training & Product Knowledge | VS-64 |
| W2387 | Seasonal Launch Monitoring | VS-64 |
| W2388 | Seasonal Vendor Coordination | VS-64 |
| W2389 | Multi-Season Inventory Transition Planning | VS-64 |
| W2390 | Sell-Through Based Markdown Trigger | VS-64 |
| W2391 | Progressive Markdown Strategy Execution | VS-64 |
| W2392 | Store-Level Clearance Event Execution | VS-64 |
| W2393 | Clearance Inventory Consolidation | VS-64 |
| W2394 | Vendor Markdown Allowance Processing | VS-64 |
| W2395 | Clearance Pricing Compliance Audit | VS-64 |
| W2396 | Employee Purchase Program for Clearance | VS-64 |
| W2397 | Clearance Financial Reconciliation | VS-64 |
| W2400 | Vendor Seasonal Performance Review | VS-64 |
| W2405 | Seasonal Playbook Update | VS-64 |

**People** (28)

| ID | Workflow | Value Stream |
|---|---|---|
| W2849 | Company Clinic Operations & Occupational Health Nurse Coverage | VS-83 |
| W2851 | Referral to Network Hospital, Specialist & Diagnostics Management | VS-83 |
| W2854 | Return-to-Work Clearance, Restricted Duty & Accommodation | VS-83 |
| W2855 | Medical Record Confidentiality, Consent & DOH Recordkeeping | VS-83 |
| W2856 | Clinic Pharmacy, First-Aid Station & Medical Supply Management | VS-83 |
| W2857 | Pre-Employment Medical Examination & Fitness-to-Work Clearance | VS-83 |
| W2860 | Vaccine & Immunization Program (Flu, Hep-B, Tetanus, COVID) | VS-83 |
| W2861 | Disease Surveillance & Outbreak Response (Store/DC Cluster) | VS-83 |
| W2862 | Ergonomics Assessment & Musculoskeletal Disorder Prevention | VS-83 |
| W2865 | Employee Assistance Program (EAP) Provision & Confidential Counseling | VS-83 |
| W2867 | Critical Incident Stress Debriefing & Crisis Support | VS-83 |
| W2868 | Substance Abuse Policy, Testing & Rehabilitation Support | VS-83 |
| W2869 | Lifestyle Disease (Diabetes/Hypertension) Management & Screening | VS-83 |
| W2870 | Nutrition, Fitness & Workplace Wellness Campaign | VS-83 |
| W2871 | Maternal & Reproductive Health Program | VS-83 |
| W2874 | CBA Negotiation Preparation, Data Assembly & Bargaining Strategy | VS-84 |
| W2877 | CBA Implementation, Wage/Benefit Administration & Compliance Tracking | VS-84 |
| W2878 | CBA Economic Impact Modeling, Costing & Mid-Term Review | VS-84 |
| W2879 | Union Dues Check-Off, Agency Fee & Authorization Management | VS-84 |
| W2880 | Labor-Management Council (LMC) Charter & Joint Governance Operations | VS-84 |
| W2881 | Grievance Intake, Classification & Step-1 Conference | VS-84 |
| W2882 | Grievance Escalation, Step-2/3 Review & CBA Dispute Resolution | VS-84 |
| W2890 | Town Hall, Skip-Level & Communication Forum Operations | VS-84 |
| W2891 | Suggestion Box / Idea Program & Recognition of Contributions | VS-84 |
| W2892 | Whistleblower & Fair Treatment (Non-Retaliation) Program Governance | VS-84 |
| W2893 | Labor Coalition & Industry Association Engagement (ECOP/FWE) | VS-84 |
| W2894 | Government Labor Policy Advocacy & DOLE/BIR/SSS Liaison | VS-84 |
| W2895 | Labor Relations Risk Register & ULP Prevention Audit | VS-84 |


#### Tier 3 — Analytics / analytics (30 workflows)

**Finance** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W2748 | Post-Implementation Review & Actual vs. Projected ROI Analysis | VS-40 |
| W2752 | Annual Capex Portfolio Review & Process Improvement | VS-40 |

**Sell & Serve** (19)

| ID | Workflow | Value Stream |
|---|---|---|
| W1883 | Trade Account Churn Risk Prediction & Retention Intervention | VS-43 |
| W1892 | Contractor Program Cost & ROI Analysis | VS-43 |
| W2169 | Space Productivity Analysis | VS-55 |
| W2173 | Planogram Cost-Benefit Analysis | VS-55 |
| W2178 | Store Walk-In Traffic & Heatmap Analysis | VS-55 |
| W2182 | Sales Per Square Meter Analysis | VS-55 |
| W2185 | Promotional Space ROI Analysis | VS-55 |
| W2188 | Planogram Performance Dashboard | VS-55 |
| W2189 | Space Capital Investment Analysis | VS-55 |
| W2373 | Task Analytics & Process Improvement | VS-63 |
| W2374 | Communication Read Rate Analysis | VS-63 |
| W2375 | Task Completion Rate Trending | VS-63 |
| W2377 | Communication Channel Effectiveness | VS-63 |
| W2379 | Communication Platform Usage Analytics | VS-63 |
| W2423 | Marketplace Commission & Fee Analysis | VS-65 |
| W2424 | Marketplace Channel P&L | VS-65 |
| W2425 | Marketplace Performance Dashboard | VS-65 |
| W2426 | Marketplace vs. Own Ecommerce Channel Comparison | VS-65 |
| W2427 | Marketplace Customer Acquisition Analysis | VS-65 |

**Plan & Source** (6)

| ID | Workflow | Value Stream |
|---|---|---|
| W2398 | Post-Season Sales Performance Analysis | VS-64 |
| W2399 | Seasonal Forecast Accuracy Review | VS-64 |
| W2401 | Customer Seasonal Purchase Behavior Analysis | VS-64 |
| W2402 | Seasonal Planogram Effectiveness Review | VS-64 |
| W2403 | Seasonal Markdown Strategy Effectiveness | VS-64 |
| W2404 | Seasonal Category Profitability Report | VS-64 |

**People** (3)

| ID | Workflow | Value Stream |
|---|---|---|
| W2872 | Wellness Program Effectiveness Analytics & ROI | VS-83 |
| W2889 | Employee Engagement Survey, Pulse & Sentiment Analytics | VS-84 |
| W2896 | Labor Relations KPI, Cost & Partnership Health Reporting | VS-84 |


**Promotion audit (21 → Tier 1, statutory execution):**

- **Finance** (3): W1823, W1824, W1829
- **Sell & Serve** (1): W2360
- **People** (17): W2850, W2852, W2853, W2858, W2859, W2863, W2864, W2866, W2873, W2875, W2876, W2883, W2884, W2885, W2886, W2887, W2888

**Demotion audit (30 → Tier 3, analytics/optimization):**

- **Finance** (2): W2748, W2752
- **Sell & Serve** (19): W1883, W1892, W2169, W2173, W2178, W2182, W2185, W2188, W2189, W2373, W2374, W2375, W2377, W2379, W2423, W2424, W2425, W2426, W2427
- **Plan & Source** (6): W2398, W2399, W2401, W2402, W2403, W2404
- **People** (3): W2872, W2889, W2896

---

### Mixed Operations Classification Pass (192 workflows; VS-57/58/66/69/70/71/74/101)

> **Hand-reviewed 2026-06-20 (batch 4).** Eight family-decisive VSs — competitive price
> intelligence, coupon/promotions, customer project services, typhoon/disaster response,
> solar energy, anti-counterfeit, contractor job-site delivery, merchandise financial
> planning. Genuine review: **15 → Tier 1** (typhoon-BCP emergency response, anti-
> counterfeit enforcement/investigation/regulatory-reporting, electrical-permit compliance,
> open-to-buy financial gate), **36 → Tier 3** (analytics: price-elasticity/markdown-optimization/
> coupon-ROI/halo-effect/trend, project-margin/scorecard, typhoon-after-action/financial-
> impact, solar-degradation/sales-analytics, counterfeit-trend/KPI, delivery-KPI/cost/route,
> markdown-optimization/vendor-margin/cluster-analytics/dashboard), **141 confirmed Tier 2**.
> Moves Check 1 unclassified 3,260 → 3,068.

#### Tier 1 — Statutory / emergency (15)

**Governance & Assurance** (13)

| ID | Workflow | Value Stream |
|---|---|---|
| W2507 | Typhoon Emergency Pricing Freeze Activation | VS-69 |
| W2510 | Store Emergency Closure Decision & Execution | VS-69 |
| W2511 | DC Emergency Shutdown & Asset Protection | VS-69 |
| W2513 | Real-Time Disaster Operations Center Activation | VS-69 |
| W2514 | Emergency Generator & Power Contingency Operations | VS-69 |
| W2517 | Active Typhoon Customer Safety & In-Store Emergency Protocol | VS-69 |
| W2518 | Post-Typhoon Store Damage Assessment & Rapid Reopening | VS-69 |
| W2558 | In-Store Counterfeit Product Detection & Seizure | VS-71 |
| W2559 | Counterfeit Investigation & Evidence Collection | VS-71 |
| W2561 | Law Enforcement & Regulatory Reporting for Counterfeiting | VS-71 |
| W2562 | Customer Counterfeit Product Exchange & Restitution | VS-71 |
| W2563 | Online Marketplace Counterfeit Monitoring & Takedown | VS-71 |
| W2565 | Internal Counterfeit Prevention & Staff Integrity Program | VS-71 |

**Sell & Serve** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W2538 | Solar Electrical Permit & LGU Compliance | VS-70 |

**Plan & Source** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W3283 | Open-to-Buy (OTB) Calculation, Maintenance & Weekly Recalculation | VS-101 |


#### Tier 2 — Operational (141)

**Governance & Assurance** (29)

| ID | Workflow | Value Stream |
|---|---|---|
| W2502 | Typhoon Season Pre-Positioning & Emergency Stock Planning | VS-69 |
| W2503 | Store-Level Typhoon Readiness Checklist Execution | VS-69 |
| W2504 | DC & Warehouse Typhoon Preparedness Protocol | VS-69 |
| W2505 | Emergency Merchandise Demand Surge Forecasting | VS-69 |
| W2506 | Pre-Typhoon Customer Communication & Advisory | VS-69 |
| W2508 | Pre-Typhoon Cash Float & Payment Contingency Setup | VS-69 |
| W2509 | Staff Safety Notification & Deployment Readiness | VS-69 |
| W2512 | Emergency Merchandise Rapid Replenishment Dispatch | VS-69 |
| W2515 | Disaster-Affected Employee Welfare & Deployment Tracking | VS-69 |
| W2516 | Emergency Vendor Coordination & Expedite Procurement | VS-69 |
| W2519 | Post-Disaster Inventory Loss Quantification & Insurance Claim | VS-69 |
| W2520 | Community Building Materials Donation & Relief Operations | VS-69 |
| W2521 | Post-Disaster Emergency Product Pricing & Availability Management | VS-69 |
| W2524 | Post-Disaster Vendor Recovery & Supply Chain Re-Establishment | VS-69 |
| W2525 | Annual Typhoon Season Readiness Program & Drill Execution | VS-69 |
| W2550 | High-Risk Product Serialization & Registration | VS-71 |
| W2551 | QR Code Authentication System Management | VS-71 |
| W2552 | Customer Product Verification Support | VS-71 |
| W2553 | Vendor Serialization Compliance Audit | VS-71 |
| W2554 | Product Authentication Data Platform Management | VS-71 |
| W2555 | Gray Market & Unauthorized Channel Detection | VS-71 |
| W2556 | Serialization Label & Packaging Standard Management | VS-71 |
| W2557 | Product Authentication Staff Training | VS-71 |
| W2560 | Vendor Counterfeit Alert & Coordination | VS-71 |
| W2566 | Vendor Anti-Counterfeit Compliance Program Management | VS-71 |
| W2567 | Supply Chain Integrity Audit & Verification | VS-71 |
| W2570 | Vendor Brand Protection Partnership Management | VS-71 |
| W2572 | Industry Anti-Counterfeit Collaboration & Intelligence Sharing | VS-71 |
| W2573 | Annual Anti-Counterfeit Strategy Review & Program Update | VS-71 |

**Sell & Serve** (59)

| ID | Workflow | Value Stream |
|---|---|---|
| W2238 | Coupon Design & Configuration | VS-58 |
| W2239 | Digital Voucher Distribution | VS-58 |
| W2240 | In-Store Coupon Printing & Display | VS-58 |
| W2241 | Coupon Budget & Liability Management | VS-58 |
| W2242 | Vendor-Funded Coupon Program | VS-58 |
| W2243 | Loyalty Point Multiplier Campaign | VS-58 |
| W2244 | Coupon Fraud Prevention Design | VS-58 |
| W2246 | In-Store Coupon Redemption | VS-58 |
| W2247 | Online Coupon & Promo Code Redemption | VS-58 |
| W2248 | Multi-Coupon Stacking Management | VS-58 |
| W2249 | Coupon Redemption Fraud Detection | VS-58 |
| W2250 | Coupon Return & Reversal | VS-58 |
| W2251 | Expired Coupon Exception Handling | VS-58 |
| W2252 | Digital Coupon Device & Account Binding | VS-58 |
| W2253 | Coupon Vendor Reconciliation | VS-58 |
| W2260 | Competitor Promotion Intelligence | VS-58 |
| W2430 | Customer Project Inquiry & Qualification | VS-66 |
| W2431 | In-Home Measurement Visit | VS-66 |
| W2432 | Kitchen & Bathroom Design Proposal | VS-66 |
| W2433 | Material Estimation & Specification | VS-66 |
| W2434 | Project Quotation & Pricing | VS-66 |
| W2435 | Design Revision & Customer Approval | VS-66 |
| W2436 | Design Consultant Training & Certification | VS-66 |
| W2437 | Design Software & Tool Management | VS-66 |
| W2438 | Project Sales Order Processing | VS-66 |
| W2439 | Project Material Procurement | VS-66 |
| W2440 | Project Delivery Coordination | VS-66 |
| W2441 | Project Installation Coordination | VS-66 |
| W2442 | Project Change Order Management | VS-66 |
| W2443 | Project Payment Collection & Milestone Billing | VS-66 |
| W2444 | Project Warranty Handover | VS-66 |
| W2445 | Project Material Returns & Surplus Handling | VS-66 |
| W2446 | Project Dashboard & Status Tracking | VS-66 |
| W2447 | Project Timeline Management | VS-66 |
| W2448 | Project Quality Inspection | VS-66 |
| W2449 | Project Completion & Punch List | VS-66 |
| W2450 | Post-Project Customer Follow-Up | VS-66 |
| W2453 | Project Services Annual Strategy Review | VS-66 |
| W2526 | Solar Product Assortment Planning & Vendor Selection | VS-70 |
| W2527 | In-Store Solar Consultation & System Sizing | VS-70 |
| W2528 | Solar Package & Bundle Configuration | VS-70 |
| W2529 | Solar Product Pricing & Net Metering ROI Calculator | VS-70 |
| W2530 | Solar Product Staff Training & Certification | VS-70 |
| W2531 | Solar Product Inventory & Lead Time Management | VS-70 |
| W2532 | Solar Lead Capture & CRM Funnel Management | VS-70 |
| W2533 | Solar Promotional Campaign & Trade Show Coordination | VS-70 |
| W2534 | Solar Site Survey & Assessment | VS-70 |
| W2535 | Solar Installation Partner Scheduling & Dispatch | VS-70 |
| W2536 | Net Metering Application & DU Coordination | VS-70 |
| W2537 | Solar Installation Quality Inspection & Commissioning | VS-70 |
| W2539 | Solar Installation Material Staging & Delivery Coordination | VS-70 |
| W2540 | Solar System Grid Connection & Net Metering Activation | VS-70 |
| W2541 | Solar Installation Warranty Registration & Handover | VS-70 |
| W2542 | Solar System Remote Monitoring & Performance Alerting | VS-70 |
| W2544 | Solar Warranty Claim & Vendor Recovery Processing | VS-70 |
| W2545 | Solar Installation Partner Performance Scoring | VS-70 |
| W2546 | Solar Customer Satisfaction & NPS Survey | VS-70 |
| W2548 | Solar Product Return & Exchange Processing | VS-70 |
| W2549 | Solar Market Intelligence & Regulatory Update Monitoring | VS-70 |

**Plan & Source** (34)

| ID | Workflow | Value Stream |
|---|---|---|
| W2214 | Competitor Price Scraping & Collection | VS-57 |
| W2215 | Price Matching Decision & Execution | VS-57 |
| W2216 | Competitor Promotion Monitoring | VS-57 |
| W2217 | Price Positioning Strategy Review | VS-57 |
| W2218 | Dynamic Pricing Rule Management | VS-57 |
| W2221 | Competitor Pricing Intelligence Report | VS-57 |
| W2222 | Rapid Price Response Workflow | VS-57 |
| W2223 | Promotional Price Planning | VS-57 |
| W2225 | Store-Level Price Override | VS-57 |
| W2226 | Price Change Communication to Stores | VS-57 |
| W2227 | Trade Price Competitive Alignment | VS-57 |
| W2228 | Price Audit & Compliance | VS-57 |
| W2229 | Customer Price Match Guarantee | VS-57 |
| W2232 | Vendor Cost-Driven Price Adjustment | VS-57 |
| W2233 | Pricing Strategy Annual Review | VS-57 |
| W2235 | Price Image & Customer Perception Survey | VS-57 |
| W2236 | Pricing System & Master Data Accuracy | VS-57 |
| W2237 | Cross-Channel Price Consistency | VS-57 |
| W3281 | Annual Merchandise Financial Plan & Sales/Margin Budget Development | VS-101 |
| W3282 | Seasonal Merchandise Plan & Department/Category Financial Plan | VS-101 |
| W3284 | Category & Sub-Class Receipt Planning & Commitment Tracking | VS-101 |
| W3285 | Markdown & Clearance Budget Allocation & Spend Authorization | VS-101 |
| W3286 | Gross-Margin Plan, Initial Markup (IMU) & Markdown-Margin Modeling | VS-101 |
| W3287 | Multi-Channel Revenue & Margin Allocation Planning | VS-101 |
| W3288 | Merchandise Plan-vs-Actual Review, In-Season Forecast & Reforecast | VS-101 |
| W3289 | Ending Stock & Weeks-of-Supply (WOS) Target Planning by Category | VS-101 |
| W3290 | Inventory Turn & GMROI Target Setting & Performance Tracking | VS-101 |
| W3291 | Stock-to-Sales Ratio & Flow Planning | VS-101 |
| W3292 | New-Store Inventory Investment Planning & Pre-Open Stock Build | VS-101 |
| W3293 | Discontinuation & Exit Inventory Liquidation Planning | VS-101 |
| W3294 | Aged/Slow-Mover Inventory Provisioning & Reserve Planning | VS-101 |
| W3295 | Import vs Domestic Inventory Investment & Landed-Cost Margin Planning | VS-101 |
| W3298 | Key-Item / Item-Class Performance Review & Reorder/Cancel Decisioning | VS-101 |
| W3303 | Markdown/OTB Audit & Merchandise Financial Control Review | VS-101 |

**Make & Move** (19)

| ID | Workflow | Value Stream |
|---|---|---|
| W2622 | Contractor Job Site Delivery Order Capture & Planning | VS-74 |
| W2623 | Multi-Drop Job Site Delivery Route Optimization | VS-74 |
| W2624 | Crane & Boom Truck Delivery Scheduling | VS-74 |
| W2625 | Phased Construction Delivery Schedule Management | VS-74 |
| W2626 | Emergency & Same-Day Contractor Delivery Processing | VS-74 |
| W2627 | Job Site Delivery Access & Permit Coordination | VS-74 |
| W2628 | Night & Weekend Delivery Scheduling | VS-74 |
| W2629 | Contractor Delivery Special Equipment Coordination | VS-74 |
| W2630 | Job Site Delivery Unloading & Material Placement | VS-74 |
| W2631 | Job Site Delivery Damage & Shortage Resolution | VS-74 |
| W2632 | Delivery Return & Excess Material Pickup | VS-74 |
| W2633 | Job Site Delivery Proof of Delivery & Documentation | VS-74 |
| W2634 | Contractor Site Safety Compliance During Delivery | VS-74 |
| W2635 | Bulk Material Handling at Job Site | VS-74 |
| W2636 | Job Site Delivery Quality Verification | VS-74 |
| W2637 | Job Site Delivery Real-Time Tracking & ETA Communication | VS-74 |
| W2640 | Contractor Delivery Satisfaction Survey & Feedback | VS-74 |
| W2643 | 3PL Partner Performance for Contractor Deliveries | VS-74 |
| W2645 | Annual Contractor Delivery Strategy Review | VS-74 |


#### Tier 3 — Analytics (36)

**Governance & Assurance** (6)

| ID | Workflow | Value Stream |
|---|---|---|
| W2522 | Typhoon Event After-Action Review & Lessons Learned | VS-69 |
| W2523 | Disaster Recovery Financial Impact Reporting & Budget Rebalancing | VS-69 |
| W2564 | Counterfeit Trend Analysis & Threat Assessment | VS-71 |
| W2568 | Anti-Counterfeit Technology Evaluation & Deployment | VS-71 |
| W2569 | Counterfeit Financial Impact & Loss Reporting | VS-71 |
| W2571 | Anti-Counterfeit KPI Dashboard & Executive Reporting | VS-71 |

**Sell & Serve** (12)

| ID | Workflow | Value Stream |
|---|---|---|
| W2245 | Coupon Performance Dashboard | VS-58 |
| W2254 | Campaign ROI Analysis | VS-58 |
| W2255 | Channel-Specific Promotion Effectiveness | VS-58 |
| W2256 | Customer Segment Promotion Response | VS-58 |
| W2257 | Promotion Halo Effect Analysis | VS-58 |
| W2258 | Year-over-Year Promotion Trend | VS-58 |
| W2259 | Digital Coupon Technology Performance | VS-58 |
| W2261 | Promotion Calendar Optimization | VS-58 |
| W2451 | Project Revenue & Margin Analysis | VS-66 |
| W2452 | Project Consultant Performance Scorecard | VS-66 |
| W2543 | Solar Panel Performance Degradation Tracking | VS-70 |
| W2547 | Solar Sales Analytics & Revenue Attribution | VS-70 |

**Plan & Source** (13)

| ID | Workflow | Value Stream |
|---|---|---|
| W2219 | Market Basket Price Comparison | VS-57 |
| W2220 | Price Elasticity Analysis | VS-57 |
| W2224 | Markdown Optimization for Clearance | VS-57 |
| W2230 | Gross Margin Analysis by Category | VS-57 |
| W2231 | Price Sensitivity Dashboard | VS-57 |
| W2234 | Promotional Pricing ROI Analysis | VS-57 |
| W3296 | Inventory Investment Scenario Modeling & Working-Capital Constraint | VS-101 |
| W3297 | Weekly Merchandise P&A Reporting & Variance Analysis | VS-101 |
| W3299 | Markdown Optimization & Price-Engineering Analytics | VS-101 |
| W3300 | Promotion Post-Mortem, Halo & Cannibalization Margin Analysis | VS-101 |
| W3301 | Vendor Margin Contribution, Terms & Rebate Impact Analysis | VS-101 |
| W3302 | Store/Cluster Merchandise Performance & Localization Analytics | VS-101 |
| W3304 | Merchandise KPI Dashboard, Category Scorecard & Executive Review | VS-101 |

**Make & Move** (5)

| ID | Workflow | Value Stream |
|---|---|---|
| W2638 | Contractor Delivery On-Time Performance Measurement | VS-74 |
| W2639 | Contractor Delivery Cost per Order Analytics | VS-74 |
| W2641 | Contractor Delivery Route Optimization Analytics | VS-74 |
| W2642 | Emergency Delivery Frequency & Root Cause Analysis | VS-74 |
| W2644 | Contractor Delivery KPI Dashboard | VS-74 |


**Promotion audit (15 → Tier 1):**
- **Governance & Assurance** (13): W2507, W2510, W2511, W2513, W2514, W2517, W2518, W2558, W2559, W2561, W2562, W2563, W2565
- **Sell & Serve** (1): W2538
- **Plan & Source** (1): W3283

**Demotion audit (36 → Tier 3):**
- **Plan & Source** (13): W2219, W2220, W2224, W2230, W2231, W2234, W3296, W3297, W3299, W3300, W3301, W3302, W3304
- **Sell & Serve** (12): W2245, W2254, W2255, W2256, W2257, W2258, W2259, W2261, W2451, W2452, W2543, W2547
- **Governance & Assurance** (6): W2522, W2523, W2564, W2568, W2569, W2571
- **Make & Move** (5): W2638, W2639, W2641, W2642, W2644

---

### Shared Services & Specialized Support Classification Pass (192 workflows; VS-103/106/107/109/115/116/119/123)

> **Hand-reviewed 2026-06-20 (batch 5).** Eight VSs — HR shared services, commodity-risk,
> strategic key-account, store remodel, calibration/metrology, performance-bond/surety,
> whistleblower/ethics, skilled-trade apprenticeship. **18 → Tier 1** (PFRS 9 hedge
> accounting, DTI Weights & Measures compliance, bid/performance-bond statutory issuance,
> speak-up/whistleblower investigations & anti-retaliation, TESDA apprenticeship compliance);
> **36 → Tier 3** (analytics); **138 confirmed Tier 2**. Moves Check 1 3,068 → 2,876.

#### Tier 1 — Statutory (18)

**People** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3811 | TESDA Program Registration, Dual-Training & Compliance | VS-123 |
| W3812 | Apprenticeship Funding, Stipend & DOLE Labor Compliance | VS-123 |
| W3815 | Apprenticeship Records, Certification Issuance & Compliance Documentation | VS-123 |
| W3831 | Trade-Certification Compliance Audit & External Accreditation Maintenance | VS-123 |

**Plan & Source** (1)

| ID | Workflow | Value Stream |
|---|---|---|
| W3413 | Hedge Accounting (PFRS 9), Effectiveness & Mark-to-Market Reporting | VS-106 |

**Technology & Data** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W3633 | DTI Weights & Measures Compliance & Inspection | VS-115 |
| W3639 | Customer Measurement Dispute & Resolution | VS-115 |

**Finance** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3649 | Bid Bond Application & Issuance | VS-116 |
| W3650 | Performance & Payment Bond Application & Issuance | VS-116 |
| W3658 | Bond Claim, Demand & Default Response Management | VS-116 |
| W3660 | Bond Dispute, Litigation & Resolution | VS-116 |

**Governance & Assurance** (7)

| ID | Workflow | Value Stream |
|---|---|---|
| W3715 | Speak-Up Channel Operations & Multi-Channel Intake | VS-119 |
| W3716 | Whistleblower Anonymity, Confidentiality & Protection Framework | VS-119 |
| W3721 | Investigation Planning, Scoping & Evidence Collection | VS-119 |
| W3722 | Investigation Interview & Witness Management | VS-119 |
| W3723 | Investigation Finding, Conclusion & Adjudication | VS-119 |
| W3725 | Retaliation Monitoring & Protection | VS-119 |
| W3727 | External/Regulatory Reporting & Law-Enforcement Coordination | VS-119 |


#### Tier 2 — Operational (138)

**People** (34)

| ID | Workflow | Value Stream |
|---|---|---|
| W3329 | Employee Service Center (HR Helpdesk) Case Intake, Triage & Resolution | VS-103 |
| W3330 | Employee Self-Service (ESS) & Manager Self-Service (MSS) Portal Operations | VS-103 |
| W3331 | HR Case Management, Knowledge Base & Tiered Escalation | VS-103 |
| W3332 | Multi-Entity HR Shared Services Delivery & Cross-Entity Case Routing | VS-103 |
| W3333 | Employee Document Management, e-Signature & HR Records | VS-103 |
| W3334 | HR Transaction Processing (Verifications, Certifications, Employment Letters) | VS-103 |
| W3335 | Employee Lifecycle Event Service (Onboarding/Change/Separation Ticket Execution) | VS-103 |
| W3337 | Employee Onboarding Experience & Day-1 Readiness Program | VS-103 |
| W3338 | Employee Engagement Pulse, Survey Operations & Action Planning | VS-103 |
| W3339 | Internal Communications, Intranet & Company-Wide Broadcast Operations | VS-103 |
| W3340 | Town Hall, Leadership Communication & All-Hands Event Management | VS-103 |
| W3341 | Recognition & Peer-to-Peer Appreciation Platform Operations | VS-103 |
| W3342 | Employee Feedback Loop, Suggestion & Idea Management | VS-103 |
| W3343 | Diversity, Equity & Inclusion (DEI) Program Operations | VS-103 |
| W3345 | Workforce Planning, Headcount Forecasting & Capacity Planning | VS-103 |
| W3350 | HR Data Governance, Integration & People-Data Quality | VS-103 |
| W3351 | HR Technology (HRIS/Core-HR) Administration & Configuration Management | VS-103 |
| W3809 | Trade-Capability Strategy & Apprenticeship Program Charter | VS-123 |
| W3810 | Apprenticeship Curriculum & Competency Standard Design | VS-123 |
| W3813 | Apprenticeship Governance, Authority & Policy | VS-123 |
| W3814 | Apprentice Recruitment, Selection & Employer-Brand Linkage | VS-123 |
| W3817 | Apprenticeship Cohort Planning, Scheduling & Resource Allocation | VS-123 |
| W3818 | Apprentice On-the-Job Training, Rotation & Store Assignment Operations | VS-123 |
| W3819 | Trade Competency Assessment, Practical Examination & Certification Sign-Off | VS-123 |
| W3820 | Mentor / Master-Tradesperson Network & Coaching Operations | VS-123 |
| W3821 | Apprentice Progress Tracking, Feedback & Welfare Management | VS-123 |
| W3822 | Apprentice-to-Role Conversion, Placement & Career Pathway | VS-123 |
| W3823 | Apprenticeship Safety, PPE & Trade-Specific HSE Integration | VS-123 |
| W3824 | Apprenticeship Vendor/Product Training Integration & Sponsorship | VS-123 |
| W3825 | Vocational School, Senior-High & TESDA Partner Network Management | VS-123 |
| W3826 | Vocational Feeder Pipeline, OJT Placement & School-to-Work Transition | VS-123 |
| W3827 | Instructor / Master-Trainer Pipeline, Qualification & Development | VS-123 |
| W3828 | Assessor Qualification, Standardization & Calibration | VS-123 |
| W3829 | Trade Knowledge Management, Content Library & Curriculum Asset Management | VS-123 |

**Plan & Source** (19)

| ID | Workflow | Value Stream |
|---|---|---|
| W3401 | Commodity Exposure Mapping by SKU / Category / Vendor | VS-106 |
| W3402 | Bill-of-Material (BOM) & Input-Cost Decomposition Modeling | VS-106 |
| W3403 | Commodity Market-Price Intelligence & Benchmark Data Management | VS-106 |
| W3405 | Vendor Cost-Structure & Pass-Through Clause Transparency | VS-106 |
| W3406 | Commodity Risk Register, Appetite & Governance Framework | VS-106 |
| W3407 | Market Outlook, Forecast & Commodity Intelligence Briefing | VS-106 |
| W3409 | Commodity Mitigation Strategy Selection & Hedge Program Design | VS-106 |
| W3410 | Forward Buying, Strategic Inventory & Physical Hedge Execution | VS-106 |
| W3411 | Indexed / Formula / Floating Vendor Contract Structuring | VS-106 |
| W3412 | Financial Commodity Hedge Execution, Broker & Counterparty Management | VS-106 |
| W3414 | Vendor Raw-Material Surcharge & Formula-Price Administration | VS-106 |
| W3415 | Long-Term Supply Agreement & Volume Commitment Negotiation | VS-106 |
| W3416 | Hedge & Mitigation Performance Review and Strategy Adjustment | VS-106 |
| W3417 | Input-Cost-to-Price Pass-Through Governance & SRP/Cost Adjustment | VS-106 |
| W3418 | Rapid Commodity-Shock Price Response & Margin Recovery | VS-106 |
| W3420 | Competitor Price-Sensitivity & Pass-Through Feasibility Assessment | VS-106 |
| W3421 | Vendor Recovery / Claim & Commodity Savings Capture | VS-106 |
| W3422 | Commodity-Driven Markdown & Clearance Discipline | VS-106 |
| W3424 | Commodity Risk Policy Compliance, Audit & Continuous Improvement | VS-106 |

**Sell & Serve** (18)

| ID | Workflow | Value Stream |
|---|---|---|
| W3425 | Strategic Account Definition, Tiering & Selection Criteria | VS-107 |
| W3426 | Strategic Account Identification, Qualification & Onboarding to KAM | VS-107 |
| W3427 | Key Account Plan (KAP) Development & Annual Joint Business Planning | VS-107 |
| W3428 | Account Team Structure, Assignment & Executive Sponsorship | VS-107 |
| W3429 | Strategic Account Relationship Map & Stakeholder Management | VS-107 |
| W3430 | Account Governance Cadence: QBR, Operating Reviews & Joint Planning | VS-107 |
| W3431 | Cross-Functional Account Coordination & Internal Alignment | VS-107 |
| W3432 | Strategic Account Compliance, Ethics & Conflict-of-Interest Governance | VS-107 |
| W3434 | Enterprise Pricing, Contract & Trading-Terms Negotiation | VS-107 |
| W3435 | Solutioning & Value-Proposition Development for Strategic Accounts | VS-107 |
| W3436 | Strategic Project Pursuit, Bid Strategy & Win-Plan | VS-107 |
| W3437 | Customer Success, Adoption & Product/Service Expansion | VS-107 |
| W3438 | Executive-to-Executive Engagement & C-Suite Relationship Programs | VS-107 |
| W3439 | Joint Marketing, CSR & Co-Marketing with Strategic Accounts | VS-107 |
| W3440 | Strategic Account Innovation, Feedback & Co-Creation Loop | VS-107 |
| W3443 | Account Performance Scorecard & Tier Health Assessment | VS-107 |
| W3444 | Strategic Account Credit, Concentration & Receivable Risk Management | VS-107 |
| W3446 | At-Risk Account Identification, Save-Plan & Win-Back | VS-107 |

**Asset & Infrastructure** (20)

| ID | Workflow | Value Stream |
|---|---|---|
| W3473 | Store Lifecycle & Remodel Portfolio Strategy | VS-109 |
| W3474 | Store Performance Assessment & Remodel Trigger / Qualification | VS-109 |
| W3475 | Remodel Concept, Format & Scope Definition | VS-109 |
| W3476 | Remodel Business Case, Capex Funding & Approval | VS-109 |
| W3477 | Store Design, Layout & Fixture Planning | VS-109 |
| W3478 | Remodel Merchandising & Assortment Reset Planning | VS-109 |
| W3479 | Remodel Site Survey, Permitting & Regulatory Compliance | VS-109 |
| W3480 | Remodel Project Plan, Phasing & Live-Operations Continuity | VS-109 |
| W3481 | Remodel Fixture, Equipment & FF&E Procurement | VS-109 |
| W3482 | Remodel Construction Vendor Selection & Contracting | VS-109 |
| W3483 | Remodel Construction Execution & Site Coordination | VS-109 |
| W3484 | Remodel Mechanical, Electrical, Plumbing & HVAC Works | VS-109 |
| W3485 | Store Fixture Installation, Signage & Graphics Rollout | VS-109 |
| W3486 | Remodel Technology & POS / IT Refresh | VS-109 |
| W3487 | Remodel Merchandise Reset, Restock & Planogram Implementation | VS-109 |
| W3488 | Remodel Quality, Snag List & Commissioning / Handover | VS-109 |
| W3489 | Remodel Soft Launch / Grand Re-opening & Marketing | VS-109 |
| W3490 | Remodel Staff Training & Change Management | VS-109 |
| W3495 | Store Refurbishment Cadence & Lifecycle Refresh Planning | VS-109 |
| W3496 | Store Format Innovation & Remodel Program Governance | VS-109 |

**Technology & Data** (18)

| ID | Workflow | Value Stream |
|---|---|---|
| W3617 | Calibration & Metrology Program Strategy & Governance | VS-115 |
| W3618 | Measurement Standards, Traceability & ISO 17025 Alignment | VS-115 |
| W3619 | Calibration Intervals, Tolerance & MRA Methodology | VS-115 |
| W3620 | Calibration Master Data & Device Registry | VS-115 |
| W3621 | External Calibration Lab Qualification & Vendor Management | VS-115 |
| W3622 | In-House Calibration Operations & Standards Lab | VS-115 |
| W3623 | Calibration Training, Competency & Technician Certification | VS-115 |
| W3624 | Calibration Audit, Documentation & Records | VS-115 |
| W3625 | POS Scale & Weight-Based Item Calibration | VS-115 |
| W3626 | Catch-Weight & Bulk Material Scale Calibration | VS-115 |
| W3627 | Cutting Equipment Measurement Calibration | VS-115 |
| W3628 | Paint Mixing & Tinting Dispenser Calibration | VS-115 |
| W3629 | DC Weighbridge & Truck Scale Calibration | VS-115 |
| W3630 | Fuel & Logistics Measurement Calibration | VS-115 |
| W3631 | Environmental & Process Instrument Calibration | VS-115 |
| W3632 | Test & Measurement Tool Calibration | VS-115 |
| W3634 | Out-of-Tolerance Investigation & Measurement Correction | VS-115 |
| W3636 | Device Lifecycle, Repair & Retirement Management | VS-115 |

**Finance** (16)

| ID | Workflow | Value Stream |
|---|---|---|
| W3641 | Surety & Guarantee Program Strategy & Governance | VS-116 |
| W3642 | Surety Facility, Line & Counter-Indemnity Management | VS-116 |
| W3643 | Surety Provider & Bank Guarantee Relationship Management | VS-116 |
| W3644 | Indemnity Agreement, Collateral & Security Management | VS-116 |
| W3645 | Surety Pricing, Cost & Facility Optimization | VS-116 |
| W3646 | Surety Risk, Capacity & Encumbrance Planning | VS-116 |
| W3647 | Surety Program Policy, Authority & Approval Matrix | VS-116 |
| W3648 | Surety Program Audit, Documentation & Records | VS-116 |
| W3651 | Warranty & Retention Bond Management | VS-116 |
| W3652 | Bank Guarantee Issuance & LC-for-Guarantee Management | VS-116 |
| W3653 | Cash Retention, Margin & Escrow Management | VS-116 |
| W3654 | Bond/Guarantee Tracking, Encumbrance & Register Management | VS-116 |
| W3655 | Multi-Entity Bond Coordination | VS-116 |
| W3656 | Bond Amendment, Extension & Renewal Management | VS-116 |
| W3657 | Bond Release, Retrieval & Closeout | VS-116 |
| W3659 | Counter-Indemnity Call, Recovery & Subrogation | VS-116 |

**Governance & Assurance** (13)

| ID | Workflow | Value Stream |
|---|---|---|
| W3713 | Ethics & Integrity Program Strategy & Governance | VS-119 |
| W3714 | Code of Conduct, Ethics Policy & Standards Management | VS-119 |
| W3717 | Report Triage, Classification & Routing | VS-119 |
| W3718 | Ethics Awareness, Training & Culture Program | VS-119 |
| W3719 | Ethics Committee & Case Governance | VS-119 |
| W3720 | Speak-Up Vendor/Platform & Records Management | VS-119 |
| W3724 | Disciplinary, Corrective & Remediation Action | VS-119 |
| W3726 | ABC/AML/Audit/Legal Investigation Coordination | VS-119 |
| W3728 | Case Closure, Documentation & Lessons Learned | VS-119 |
| W3732 | Conflict of Interest & Gifts/Integrity Disclosure Management | VS-119 |
| W3733 | Third-Party & Supply-Chain Integrity Due Diligence | VS-119 |
| W3734 | Ethics Program Audit & Assurance | VS-119 |
| W3735 | Multi-Entity Ethics Coordination & Governance Reporting | VS-119 |


#### Tier 3 — Analytics (36)

**People** (10)

| ID | Workflow | Value Stream |
|---|---|---|
| W3336 | HR Service Center SLA, Quality & CSAT Monitoring | VS-103 |
| W3344 | Employee Value Proposition, Culture & EX Measurement | VS-103 |
| W3346 | Recruitment Analytics, Time-to-Fill & Hiring-Funnel Reporting | VS-103 |
| W3347 | Turnover/Attrition Analytics, Retention Risk & Exit Insight | VS-103 |
| W3348 | Diversity, Pay-Equity & Workforce Composition Reporting | VS-103 |
| W3349 | HR Dashboard, Scorecard & Executive People Report Operations | VS-103 |
| W3352 | HR Process Excellence, Automation & Continuous Improvement | VS-103 |
| W3816 | Apprenticeship Program Continuous Improvement & Curriculum Refresh | VS-123 |
| W3830 | Trade-Capability Workforce Planning & Demand Modeling | VS-123 |
| W3832 | Trade-Capability Analytics, ROI & Program Effectiveness Reporting | VS-123 |

**Plan & Source** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3404 | Commodity Sensitivity, Value-at-Risk (VaR) & Exposure Measurement | VS-106 |
| W3408 | Import-FX-Commodity Interaction & Landed-Cost Exposure Analysis | VS-106 |
| W3419 | Maintained-Margin Impact Analysis & Commodity Variance Reporting | VS-106 |
| W3423 | Input-Cost Risk Dashboard & Executive/Board Reporting | VS-106 |

**Sell & Serve** (6)

| ID | Workflow | Value Stream |
|---|---|---|
| W3433 | Share-of-Wallet, Opportunity & White-Space Analysis | VS-107 |
| W3441 | Account-Level Profitability, Cost-to-Serve & Margin Analytics | VS-107 |
| W3442 | Strategic Account Revenue Forecasting & Pipeline Analytics | VS-107 |
| W3445 | Customer Lifetime Value (CLV), Retention Economics & Churn Prediction | VS-107 |
| W3447 | Strategic Account Loss & Competitive-Displacement Analysis | VS-107 |
| W3448 | KAM Program Performance, ROI & Executive/Board Reporting | VS-107 |

**Asset & Infrastructure** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3491 | Post-Remodel Sales Lift & Performance Tracking | VS-109 |
| W3492 | Remodel Customer Experience & Feedback Assessment | VS-109 |
| W3493 | Remodel Capex Variance & Post-Implementation Review | VS-109 |
| W3494 | Remodel Lessons Learned & Store-Lifecycle Knowledge Management | VS-109 |

**Technology & Data** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3635 | Measurement Variance, Revenue Impact & Loss Analytics | VS-115 |
| W3637 | Calibration Cost, Outsourcing & Service-Level Analytics | VS-115 |
| W3638 | Measurement System Analysis (MSA) & Gage R&R | VS-115 |
| W3640 | Metrology Maturity, Continuous Improvement & Innovation | VS-115 |

**Finance** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3661 | Surety Spend, Encumbrance & Cost Analytics | VS-116 |
| W3662 | Surety Provider Performance & Scorecard | VS-116 |
| W3663 | Contract / Bond Compliance & Performance Analytics | VS-116 |
| W3664 | Surety Program Maturity & Continuous Improvement | VS-116 |

**Governance & Assurance** (4)

| ID | Workflow | Value Stream |
|---|---|---|
| W3729 | Ethics & Speak-Up Analytics & KPI Reporting | VS-119 |
| W3730 | Ethics Risk Assessment & Heat-Mapping | VS-119 |
| W3731 | Culture, Engagement & Trust Measurement | VS-119 |
| W3736 | Ethics Program Maturity & Continuous Improvement | VS-119 |


**Promotion audit (18 → Tier 1):**
- **Finance** (4): W3649, W3650, W3658, W3660
- **Technology & Data** (2): W3633, W3639
- **Governance & Assurance** (7): W3715, W3716, W3721, W3722, W3723, W3725, W3727
- **People** (4): W3811, W3812, W3815, W3831

**Demotion audit (36 → Tier 3):**
- **People** (10): W3336, W3344, W3346, W3347, W3348, W3349, W3352, W3816, W3830, W3832
- **Plan & Source** (4): W3404, W3408, W3419, W3423
- **Sell & Serve** (6): W3433, W3441, W3442, W3445, W3447, W3448
- **Asset & Infrastructure** (4): W3491, W3492, W3493, W3494
- **Technology & Data** (4): W3635, W3637, W3638, W3640
- **Finance** (4): W3661, W3662, W3663, W3664
- **Governance & Assurance** (4): W3729, W3730, W3731, W3736

---

### Sales & Transformation Classification Pass (192 workflows; VS-124/130/132/134/137/140/155/159)

> **Hand-reviewed 2026-06-20 (batch 6).** Eight VSs — sales enablement, corporate development/
> M&A, political engagement, OCM/digital-adoption, PIM/DAM, field sales, trade-in/buy-back,
> corporate security. **10 → Tier 1** (PCC merger notification, political-contribution disclosure,
> election-period compliance, anti-graft controls, K&R/active-assailant response, corporate
> investigations); **24 → Tier 3** (analytics/CI); **158 T2**. → 2,684 unclassified (45.9%).

#### Tier 1 (10)

**Governance & Assurance** (10)

| ID | Workflow | Value Stream |
|---|---|---|
| W3992 | Regulatory Clearance, PCC Merger Notification & Antitrust Approval | VS-130 |
| W4027 | Political Contribution & Donation Policy, Approval & Disclosure | VS-132 |
| W4028 | Lobbying, Advocacy & Public-Affairs Activity Governance & Disclosure | VS-132 |
| W4033 | Election-Period Compliance Protocol (Omnibus Election Code, RA 9006, COMELEC) | VS-132 |
| W4034 | Campaign-Finance, Contribution-Limit & Prohibited-Donation Controls | VS-132 |
| W4037 | Government Official, Employee & Procurement Interaction (Anti-Graft) Controls | VS-132 |
| W4686 | Kidnap & Ransom (K&R), Extortion & Blackmail Response Protocol | VS-159 |
| W4689 | Corporate Investigations: Fraud, Theft, Embezzlement & IP Misappropriation | VS-159 |
| W4692 | Active-Assailant, Civil-Unrest & Protest / Crowd Response Protocol | VS-159 |
| W4693 | Surveillance, Evidence Collection & Coordination with Law Enforcement (PNP/NBI) | VS-159 |


#### Tier 2 (158)

**Sell & Serve** (57)

| ID | Workflow | Value Stream |
|---|---|---|
| W3833 | Sales Enablement Strategy, Operating Model & Governance | VS-124 |
| W3834 | Selling-Skills Curriculum & Consultative Selling Playbook Development | VS-124 |
| W3835 | Department & Category Selling Playbooks (Attachment, Linked, Project Selling) | VS-124 |
| W3836 | Sales Coaching, Field Enablement & Store-Level Reinforcement | VS-124 |
| W3837 | Trade-Pro / B2B Consultative Selling Enablement | VS-124 |
| W3838 | Sales Contest, Incentive & Motivation Program Design | VS-124 |
| W3839 | Sales Enablement Technology & Content Delivery Platform | VS-124 |
| W3841 | Product Knowledge Mastery Program & Role-Based Knowledge Standards | VS-124 |
| W3842 | Product Knowledge Certification, Assessment & Recertification | VS-124 |
| W3843 | New-Product Launch Enablement & Rapid Knowledge Rollout | VS-124 |
| W3844 | Clienteling Tool, Customer-360 & Associate Mobile Selling Assistant | VS-124 |
| W3845 | Loyalty, Identification & Enrollment Enablement at Point of Sale | VS-124 |
| W3846 | Service / Installation / Add-On Selling Enablement | VS-124 |
| W3847 | Selling Quality Assurance, Mystery Shopping & Customer Interaction Audit | VS-124 |
| W3848 | Product Knowledge Content & Vendor Training Governance | VS-124 |
| W3856 | Executive Selling-Performance Review & Commercial Linkage | VS-124 |
| W4217 | Field Sales Strategy & Go-to-Coverage Model | VS-140 |
| W4218 | Force Sizing, Structure & Role Design | VS-140 |
| W4219 | Territory Design, Alignment & Balancing | VS-140 |
| W4220 | Account Segmentation, Tiering & Coverage Plan | VS-140 |
| W4221 | Quota, Target Setting & Capacity Planning | VS-140 |
| W4222 | Route-to-Market & Channel Assignment (Field vs Digital vs Store) | VS-140 |
| W4223 | Field Sales Onboarding, Enablement & Certification | VS-140 |
| W4224 | Field Sales Tooling, CRM & Mobility Platform | VS-140 |
| W4225 | Daily Route & Call Planning | VS-140 |
| W4226 | Customer Visit, Needs Analysis & Relationship Management | VS-140 |
| W4227 | Project Discovery, Estimating & Quoting | VS-140 |
| W4228 | Opportunity, Pipeline & Forecast Management | VS-140 |
| W4229 | Field Order Capture, Pricing & Fulfillment Coordination | VS-140 |
| W4230 | Project Bid, Tender & Specification Pursuit | VS-140 |
| W4231 | Field Sample, Demo & Merchandising Support | VS-140 |
| W4232 | Compliance, ABC & Data-Quality in the Field | VS-140 |
| W4233 | Field Sales Performance & Quota Attainment Management | VS-140 |
| W4234 | Field Sales Compensation & Incentive Administration | VS-140 |
| W4237 | Customer Retention, Churn & Account-Health Management | VS-140 |
| W4238 | Field Sales Coaching, Performance Management & Recognition | VS-140 |
| W4577 | Trade-In Program Strategy, Scope & Economics | VS-155 |
| W4578 | Eligible-Product & Take-Back Channel Policy | VS-155 |
| W4579 | Trade-In Valuation Engine & Condition-Grading Model | VS-155 |
| W4580 | Trade-In Credit, Pricing & New-Purchase Linkage | VS-155 |
| W4581 | Certified Pre-Owned Pricing, Margin & Positioning | VS-155 |
| W4583 | Warranty, Liability & Consumer-Protection Framework | VS-155 |
| W4584 | Systems, Item-Coding & Inventory Setup for Pre-Owned | VS-155 |
| W4585 | Customer Take-Back Intake & Custody Transfer | VS-155 |
| W4586 | Intake Inspection, Safety Screen & Data Wipe | VS-155 |
| W4587 | Triage, Routing & Disposition Decision | VS-155 |
| W4588 | Refurbishment Processing (Repair, Refinish, Parts Replacement) | VS-155 |
| W4589 | Certification Testing, Grading & Certification Issuance | VS-155 |
| W4590 | Parts Harvesting, Recycling & Non-Certified Disposition | VS-155 |
| W4591 | Refurbishment Quality, Cost Tracking & Service-Center Operations | VS-155 |
| W4592 | Refurbisher Safety, HSE & Hazmat Handling | VS-155 |
| W4593 | Certified Pre-Owned Listing, Content & Channel Syndication | VS-155 |
| W4594 | Resale Order, Pricing Integrity & Checkout | VS-155 |
| W4595 | Pre-Owned Fulfillment, Pickup & Delivery | VS-155 |
| W4596 | Certified Pre-Owned Warranty Claim & Service | VS-155 |
| W4597 | Pre-Owned Returns, Refunds & Re-disposition | VS-155 |
| W4598 | Customer Experience, Trust & Reviews Management | VS-155 |

**Governance & Assurance** (79)

| ID | Workflow | Value Stream |
|---|---|---|
| W3977 | Corporate Development & Growth Strategy, Portfolio & Capital Allocation | VS-130 |
| W3978 | Inorganic Growth Strategy & Build-vs-Buy-vs-Partner Framework | VS-130 |
| W3979 | Acquisition Target Sourcing, Pipeline & Deal Origination | VS-130 |
| W3980 | Target Screening, Strategic Fit & Preliminary Assessment | VS-130 |
| W3981 | Financial Modeling, Valuation & Investment Sizing | VS-130 |
| W3982 | Deal Structuring, Term Sheet & Letter of Intent (LOI) Negotiation | VS-130 |
| W3983 | M&A Governance, Approval Authority & Stage-Gate Process | VS-130 |
| W3984 | M&A Project Setup, Deal Team & Deal Management Office | VS-130 |
| W3985 | Commercial & Strategic Due Diligence | VS-130 |
| W3986 | Financial & Tax Due Diligence | VS-130 |
| W3987 | Legal, Regulatory & Corporate Due Diligence | VS-130 |
| W3988 | Operational, IT, Systems & Integration Due Diligence | VS-130 |
| W3989 | HR, People & Culture Due Diligence (incl. Labor/Union) | VS-130 |
| W3990 | ESG, Environmental & Compliance Due Diligence | VS-130 |
| W3991 | Purchase Agreement (SPA), Negotiation & Signing Management | VS-130 |
| W3993 | Post-Merger Integration (PMI) Strategy, Planning & Synergy Realization | VS-130 |
| W3994 | Day-1 Readiness, Cutover & Transaction Close Management | VS-130 |
| W3995 | Systems, Data & ERP Integration for Acquired Entities | VS-130 |
| W3996 | Organization, Culture & Change Integration Management | VS-130 |
| W3997 | Carve-Out, Separation & Transitional Service Agreement (TSA) Management | VS-130 |
| W3998 | Divestiture & Asset/Entity Disposal Execution | VS-130 |
| W3999 | Joint Venture & Strategic Partnership Post-Close Management | VS-130 |
| W4025 | Corporate Political Engagement Policy, Governance & Operating Model | VS-132 |
| W4026 | Political Activity Risk Assessment & Stakeholder / Issue Mapping | VS-132 |
| W4029 | Trade Association, Industry-Body & Third-Party Advocacy Membership Review | VS-132 |
| W4030 | Employee Political Activity, Time-Off & Non-Coercion Governance | VS-132 |
| W4031 | Political-Engagement Vendor, Consultant & PAC (if any) Management | VS-132 |
| W4032 | Political Engagement Records, Transparency & Public Disclosure | VS-132 |
| W4035 | Election-Period Marketing, Advertising & Promotion Restrictions | VS-132 |
| W4036 | Candidate Engagement, Endorsement & Non-Partisanship Governance | VS-132 |
| W4038 | Revolving-Door, Post-Employment & Confidential-Information Controls | VS-132 |
| W4039 | Grassroots & Employee Advocacy Governance & Compliance | VS-132 |
| W4040 | Political Intelligence, Monitoring & Early-Warning System | VS-132 |
| W4041 | Political-Engagement Stakeholder & Relationship Management | VS-132 |
| W4042 | Public-Affairs Position Development, Submission & Advocacy Execution | VS-132 |
| W4044 | Coalition, Partnership & Multi-Stakeholder Initiative Governance | VS-132 |
| W4045 | Crisis Political & Reputational Issue Management | VS-132 |
| W4046 | Political-Engagement Compliance Audit & Assurance | VS-132 |
| W4048 | Political-Engagement Program Review, Continuous Improvement & Board Oversight | VS-132 |
| W4073 | OCM Strategy, Operating Model & Transformation Governance | VS-134 |
| W4074 | Change Portfolio Prioritization & Capacity Planning | VS-134 |
| W4075 | Stakeholder Mapping, Analysis & Engagement Planning | VS-134 |
| W4076 | Change Impact Assessment & Affected-Person Analysis | VS-134 |
| W4077 | Organizational Readiness & Change Culture Assessment | VS-134 |
| W4078 | Change Risk Assessment & Mitigation Planning | VS-134 |
| W4079 | Executive Sponsorship Activation & Alignment | VS-134 |
| W4080 | OCM Resource, Competency & Partner Management | VS-134 |
| W4081 | Change Communications Strategy, Messaging & Channel Plan | VS-134 |
| W4082 | Transformation Roadmap, Sequencing & Change Saturation Management | VS-134 |
| W4083 | Leadership & Manager Change Cascade & "Equip-the-Manager" Program | VS-134 |
| W4084 | Frontline Change Champion / Super-User Network Operations | VS-134 |
| W4085 | Resistance Management & Change Intervention | VS-134 |
| W4086 | Change Event & Engagement Campaign Execution | VS-134 |
| W4087 | Go-Live Readiness, Cutover Support & Hypercare | VS-134 |
| W4088 | Cross-Functional Transformation Coordination | VS-134 |
| W4089 | Digital Adoption Strategy & In-App Guidance (Digital Adoption Platform) | VS-134 |
| W4090 | Role-Based Learning, Training & Enablement for Change | VS-134 |
| W4092 | Behavioral Change & Process Compliance Sustainment | VS-134 |
| W4093 | Post-Implementation Reinforcement & Continuous Improvement Loop | VS-134 |
| W4094 | Employee Experience & Change Fatigue Monitoring | VS-134 |
| W4673 | Corporate Security Strategy, Charter & Risk-Appetite Framework | VS-159 |
| W4674 | Protective Intelligence & Threat Assessment Program | VS-159 |
| W4675 | Open-Source & Human Intelligence (OSINT/HUMINT) Monitoring & Alerting | VS-159 |
| W4676 | Corporate Security Operations Center (GSOC) — 24/7 Monitoring & Coordination | VS-159 |
| W4677 | Physical Security Architecture, Access Control & Guard-Force Standards (Enterprise) | VS-159 |
| W4678 | Executive & Principal Threat Profile, Risk Register & Quarterly Review | VS-159 |
| W4679 | Travel Risk Intelligence, Geopolitical & Kidnap/Extortion Monitoring | VS-159 |
| W4680 | Corporate Security Vendor, Guard-Agency & Investigator Management | VS-159 |
| W4681 | Executive Protection Program Design & Close-Protection Operations | VS-159 |
| W4682 | Principal (Board/Family/CEO) Travel Security & Advance Operations | VS-159 |
| W4683 | Executive Transport, Convoy & Route Security | VS-159 |
| W4684 | Corporate Event, AGM & High-Profile Appearance Security | VS-159 |
| W4685 | Residences, Estate & Perimeter Security for Principals | VS-159 |
| W4687 | Employee Travel Risk, Pre-Travel Briefing & Itinerary Tracking | VS-159 |
| W4688 | Employee Travel Risk, Lost-Contact & Medical-Evacuation Coordination (Duty of Care) | VS-159 |
| W4690 | Insider-Threat Detection, Background Re-Check & Offboarding Risk | VS-159 |
| W4691 | Workplace-Violence Threat Assessment, Intervention & De-escalation | VS-159 |
| W4694 | Security Incident Response, Crisis Management & Executive Notification | VS-159 |
| W4695 | Executive & Corporate Extortion, Defamation & Coordinated-Attack Response | VS-159 |

**Technology & Data** (22)

| ID | Workflow | Value Stream |
|---|---|---|
| W4145 | Product Information Model & Canonical Catalog Architecture | VS-137 |
| W4146 | Attribute Taxonomy, Spec Schema & Category Modeling | VS-137 |
| W4147 | Data Governance, Ownership & Completeness Standards | VS-137 |
| W4148 | New-Product Content Onboarding & Item Setup | VS-137 |
| W4149 | Content Authoring Workflow & Enrichment Roles | VS-137 |
| W4150 | Translation, Multilingual & Unit-of-Measure Localization | VS-137 |
| W4151 | Product Relationship, Cross-Sell & Kit/Bundle Content Modeling | VS-137 |
| W4152 | Vendor-Supplied Content Intake & Supplier Portal Governance | VS-137 |
| W4153 | Digital Asset Repository, Taxonomy & Metadata | VS-137 |
| W4154 | Product Image & Media Production Lifecycle | VS-137 |
| W4155 | Safety Data Sheet (SDS) & Regulatory Certificate Management | VS-137 |
| W4156 | How-To & Rich Content Authoring (Guides, Video, 360°) | VS-137 |
| W4157 | Asset Rights, Licensing & Brand-Approval Management | VS-137 |
| W4158 | Asset Versioning, Localization & Obsolescence | VS-137 |
| W4159 | Channel Content Publishing & Distribution Rules | VS-137 |
| W4160 | Content Quality Assurance & Rendering Validation | VS-137 |
| W4161 | Marketplace & Third-Party Channel Content Syndication | VS-137 |
| W4162 | Price, Promotion & Availability Content Sync | VS-137 |
| W4165 | Vendor & Internal Content SLA Reporting | VS-137 |
| W4166 | Catalog Data Quality, Duplicate & GSR Remediation | VS-137 |
| W4167 | Seasonal & Promotional Catalog Event Management | VS-137 |
| W4168 | PIM/DAM Platform, Integration & Lifecycle Governance | VS-137 |


#### Tier 3 (24)

**Sell & Serve** (15)

| ID | Workflow | Value Stream |
|---|---|---|
| W3840 | Sales Enablement Budget, Vendor/Partner Governance & Continuous Improvement | VS-124 |
| W3849 | Selling-Effectiveness KPI Framework & Associate/Store Performance Scorecard | VS-124 |
| W3850 | Basket, Conversion & Attach Analytics | VS-124 |
| W3851 | Clienteling & Customer-360 Effectiveness Analytics | VS-124 |
| W3852 | Trade-Pro Capture & B2B Selling Analytics | VS-124 |
| W3853 | Loyalty-Driven Selling & Member Behavior Analytics | VS-124 |
| W3854 | Sales-Enablement ROI & Program-Effectiveness Reporting | VS-124 |
| W3855 | Customer-Facing Tool / POS / Mobile Experience Optimization for Selling | VS-124 |
| W4235 | Pipeline Conversion, Win/Loss & Sales Analytics | VS-140 |
| W4236 | Route Efficiency, Coverage Adherence & Field Productivity | VS-140 |
| W4239 | Field Sales Force Cost, ROI & Workforce Planning | VS-140 |
| W4240 | Field Sales Continuous Improvement & Capability Building | VS-140 |
| W4582 | Refurbishment Cost, Yield & Unit-Economics Modeling | VS-155 |
| W4599 | Trade-In/Resale Analytics, Yield & Margin Intelligence | VS-155 |
| W4600 | Circular-Economy Impact, ESG Reporting & Program Review | VS-155 |

**Governance & Assurance** (7)

| ID | Workflow | Value Stream |
|---|---|---|
| W4000 | M&A Portfolio Performance, Value Realization & Lessons-Learned Analytics | VS-130 |
| W4043 | Political & Regulatory Risk Monitoring, Scenario & Exposure Analysis | VS-132 |
| W4047 | Political-Engagement Analytics, ROI & Performance Measurement | VS-132 |
| W4091 | User Adoption Measurement, System Usage & Adoption Analytics | VS-134 |
| W4095 | Change Benefit Realization & Adoption ROI Tracking | VS-134 |
| W4096 | OCM Maturity Assessment & Lessons Learned | VS-134 |
| W4696 | Corporate Security Metrics, Assurance & Post-Incident Review | VS-159 |

**Technology & Data** (2)

| ID | Workflow | Value Stream |
|---|---|---|
| W4163 | Product Content Performance & SEO Analytics | VS-137 |
| W4164 | Content-Driven Conversion, Attach & Basket Analytics | VS-137 |


**Promotion audit (10 → Tier 1):**
- **Governance & Assurance** (10): W3992, W4027, W4028, W4033, W4034, W4037, W4686, W4689, W4692, W4693

**Demotion audit (24 → Tier 3):**
- **Sell & Serve** (15): W3840, W3849, W3850, W3851, W3852, W3853, W3854, W3855, W4235, W4236, W4239, W4240, W4582, W4599, W4600
- **Governance & Assurance** (7): W4000, W4043, W4047, W4091, W4095, W4096, W4696
- **Technology & Data** (2): W4163, W4164

---

*Date: 2026-06-20 | Workflow Criticality Classification v7.24 — sixth batch (Sales & Transformation): 8 VSs (VS-124/130/132/134/137/140/155/159, 192 workflows). **10 → T1** (PCC merger notification, political-contribution/election-compliance/anti-graft, corporate-security K&R/active-assailant/investigations); **24 → T3**; **158 T2**. Confirmed 2,128→2,320 rows (2,105→2,297 unique; T1 662→672, T2 1,100→1,258, T3 366→390); unclassified 2,876→2,684 (46.1%); proposed 514/2,023/147 (zero drift). `validate-repo.sh`: 0/2. Prior v7.23 — fifth batch (Shared Services & Specialized Support): 8 VSs (VS-103/106/107/109/115/116/119/123, 192 workflows). **18 → Tier 1** (PFRS 9 hedge accounting, DTI Weights & Measures, bid/performance-bond statutory issuance/claim/dispute, whistleblower speak-up/investigation/anti-retaliation/external-reporting, TESDA apprenticeship compliance); **36 → Tier 3** (analytics); **138 T2**. Confirmed 1,936→2,128 rows (1,913→2,105 unique; T1 644→662, T2 962→1,100, T3 330→366); unclassified 3,068→2,876 (42.3%); proposed 518/2,209/149 (zero drift). `validate-repo.sh`: 0/2. Prior v7.22 — fourth hand-confirmation batch (Mixed Operations): 8 VSs (VS-57/58/66/69/70/71/74/101, 192 workflows). **15 → Tier 1** (typhoon-BCP emergency, anti-counterfeit enforcement, electrical-permit compliance, OTB financial gate); **36 → Tier 3** (analytics); **141 T2**. Confirmed 1,744→1,936 rows (1,721→1,913 unique; T1 629→644, T2 821→962, T3 294→330); unclassified 3,260→3,068 (38.4%); proposed 525/2,389/154 (zero drift). `validate-repo.sh`: 0/2. Prior v7.21 — third hand-confirmation batch (Operational Support): 8 VSs (VS-40/43/55/63/64/65/83/84, 192 workflows). **21 → Tier 1** (PFRS capex capitalization/interest/conversion, DOLE occupational-health reporting/exposure-monitoring/Mental-Health-Act, DOLE/NLRC labor-relations mandatory: union certification, CBA conciliation/ratification, 2-notice-rule/discipline/SENA, reinstatement, strike-lockout notice, emergency-comm-protocol); **30 → Tier 3** (space/productivity/clearance/channel analytics, churn prediction, planogram/seasonal analytics, engagement surveys, ROI analyses); **141 confirmed Tier 2**. Confirmed 1,552→1,744 rows (1,529→1,721 unique; T1 608→629, T2 680→821, T3 264→294); unclassified 3,452→3,260 (34.6%); proposed regenerated (535/2,566/159, no drift). `validate-repo.sh`: 0/2. Prior v7.20 — second hand-confirmation batch (Support & Governance): 8 family-decisive Tier-2 VSs (VS-100/104/112/113/126/129/133/139, 192 workflows) promoted from the keyword proposal after genuine review calibrated to the register's existing optimization/analytics=Tier 3 placement. **14 → Tier 1** (statutory execution the keyword rules missed: litigation hold/filing/enforcement & loss-contingency, corporate-secretarial/SEC, regulatory-investigation defense, merger-notification/PCC pre-filing, PCC investigation/dawn-raid/litigation/penalty, political-activity/lobbying disclosure, CDP DSAR/consumer-rights, event-permit/prize-withholding); **29 → Tier 3** (analytics/optimization defaulted to Tier 2: process/task mining, cost-out & productivity programs, OpEx maturity, CDP recommendation/CLV/attribution analytics, IP/legal/portfolio analytics); **149 confirmed Tier 2**. Confirmed 1,360→1,552 rows (1,337→1,529 unique; T1 594→608, T2 531→680, T3 235→264); unclassified 3,644→3,452 (30.7% classified); proposed regenerated (543/2,747/162). `validate-repo.sh`: 0 errors / 2 warnings. Prior v7.19 — first hand-confirmation batch: the 8 wholly-statutory value streams (VS-79/85/89/91/114/117/118/125, 192 workflows) promoted from the keyword proposal into the confirmed register after genuine tier review — 154 confirmed Tier 1 (statutory execution), 32 demoted to Tier 2 (program support: training / reporting / change-monitoring / cost-or-insurance recovery), 6 demoted to Tier 3 (analytics / continuous improvement); see the 'Statutory-Compliance Classification Pass' block above. Confirmed 1,168→1,360 rows (1,145→1,337 unique; Tier 1 440→594, Tier 2 499→531, Tier 3 229→235); unclassified 3,836→3,644; proposed register regenerated via `classify-workflows.py --write` (now 548 / 2,929 / 167 — which also dissolved one row of prior proposed-file drift). `validate-repo.sh`: 0 errors / 2 warnings. Prior v7.18 — grand total reconciled to 4,981 unique workflows (1,145 confirmed + 3,836 unclassified) after restoring the VS-12 PA-12.2 ghost workflow's missing `## W1318.` header (Tool Rental Reservation, Waitlist & Scheduling); the §Summary table and intro/banner above now read 4,981/3,836, the proposed register was regenerated via `classify-workflows.py --write`, and `validate-repo.sh` Check 17 (ghost detection) now reports 0. Prior v7.17 — §Summary *Proposed classification* subsection reconciled to the regenerated proposed register: unclassified **3,595 → 3,835** (per-tier **688 / 2,608 / 155 → 741 / 2,927 / 167**), now matching [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) exactly. The drift accumulated across Passes 19–25 (VS-162–VS-177, +240 workflows) because only the proposed file was being regenerated, not this mirror. The Confirmed Total (1,168 rows / 1,145 unique) and Grand Total (4,980) were already correct. v7.16 — Summary-table `% of Classified` percentages corrected (Phase 1 37.6%→37.7%, Phase 2 42.8%→42.7%) to match standard rounding of 440/1,168 and 499/1,168 (Phase 3 19.6% was already correct). v7.15 — W40 (Regular Price Change Execution) moved from Core Finance to Core Merchandising & Pricing (subsection move only; a pricing workflow refiled next to its sibling W13; tier-1 total unchanged). v7.14 — 1,145 unique `##` workflows are classified (Tier 1: 440 · Tier 2: 499 · Tier 3: 229 = 1,168 register rows, of which 23 are `###` parent/summary sub-workflows e.g. W2, W5B, W9A that are double-counted against a `##` parent, so unique classified = 1,145). 3,451 workflows remain unclassified (4,596 unique `##` workflows − 1,145 classified); all 3,451 carry a keyword-driven proposed tier in [`workflow-criticality-proposed.md`](workflow-criticality-proposed.md) (688 Tier 1 / 2,608 Tier 2 / 155 Tier 3). The authoritative tier summary is the `## Summary` table above. VS-49–VS-52 were retired in the 2026-06-14 placeholder-content review (96 placeholder workflows removed; numbers unused); VS-89–VS-161 were added across eighteen gap-analysis passes (W2993–W4744). Full per-pass history — candidates considered, workflow-ID allocation, and the register-rows-vs-unique reconciliation — is in [`workflow-gap-analysis.md`](workflow-gap-analysis.md) and [`CHANGELOG.md`](../../CHANGELOG.md).*
