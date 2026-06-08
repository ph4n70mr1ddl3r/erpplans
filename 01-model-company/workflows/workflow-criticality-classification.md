# Workflow Criticality Classification

> Classifies all 1,063 operational workflows into operational criticality tiers.
> Supports resource prioritization and operational focus.
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

1. **Must Have requirements** (429) are overwhelmingly Tier 1, with exceptions for requirements that only apply at scale (e.g., across all 200 stores rather than pilot 5)
2. **Should Have requirements** (295) are split between Tier 1 (operational necessities) and Tier 2
3. **Nice to Have requirements** (6) are Tier 3
4. Domain-specific workflows (governance, audit, ESG, innovation) are classified by their operational impact
5. Master data governance workflows are classified by dependency — foundational masters (item, customer, vendor, location) are Tier 1; advanced masters (planogram, loyalty config, digital assets) are Tier 2

---

## Tier 1: Core Operations (153 Workflows)

These 153 workflows are foundational to daily store and supply chain operations.
Failure in any of these workflows would disrupt store operations or legal compliance.

### Core Finance (31 workflows)

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
| W74 | Employee Expense Reimbursement | Employee payouts |
| W76 | Employee Loans & Advances | HR benefit delivery |
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
| W40 | Regular Price Change Execution | Must Have POS-010 (quantity breaks), ECOM-002 (price sync); stores cannot adjust prices post-go-live |

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

### Core POS & Store Operations (21 workflows)

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

### Core Merchandising & Pricing (1 workflow)

| ID | Workflow | Operational Significance |
|---|---|---|
| W13 | Promotions & Pricing Execution | Must Have POS-014 (promo auto-apply), ECOM-002 (price sync); without it POS cannot auto-apply promotions |

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

### Core HR & Payroll (8 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W10 | Payroll Processing | 6,715 employees; 5 entities × 2 runs/month |
| W15 | Recruitment & Employee Onboarding | ~1,200–1,600 hires/year |
| W34 | Store Shift Scheduling | Store workforce management |
| W43 | Employee Separation & Offboarding | Offboarding compliance |
| W74 | Employee Expense Reimbursement | Expense processing |
| W76 | Employee Loans & Advances | Loan management |
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

### Core Compliance & IT (24 workflows)

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

### Foundational Master Data (16 workflows)

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

## Tier 2: Standard Support (206 Workflows)

These 206 workflows are needed for standard operational support, cost controls, and category management.

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

### Extended Inventory (5 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W23 | Consignment Inventory Operations | Vendor-owned stock management |
| W57 | Promotional Stock Allocation & Pre-Positioning | Promo stock allocation |
| W154 | Proactive Store Inventory Rebalancing (Stock Push) | System-suggested rebalancing |
| W218 | Inter-DC Stock Rebalancing (Stock Push) | DC-to-DC rebalancing |
| W220 | Slow-Moving & Obsolete Inventory (SLOB) Provisioning & Liquidation | SLOB management |
| W439 | In-Store Bulk-to-Retail Repackaging Operations | Bulk-to-retail conversion for hardware items |

### Extended Procurement (9 workflows)

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

### Extended Store Operations (30 workflows)

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

### Extended Finance & Treasury (22 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W59 | Insurance Policy Lifecycle Management | Insurance management |
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

### Extended HR (6 workflows)

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

### Extended Ecommerce (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W180 | Ecommerce Marketplace Integration (Lazada/Shopee) | Marketplace expansion |
| W210 | Ecommerce Fulfillment Hub (Dark Store) Operations | Dark store |
| W266 | Ecommerce Online Fraud Detection & Prevention | Fraud prevention |
| W267 | Ecommerce Digital Payment Reconciliation & Dispute Handling | Payment disputes |

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
| W158 | Business Continuity Drill & Disaster Recovery Testing | BC drills |
| W185 | Product Liability & Consumer Safety Incident Management | Product safety |
| W207 | Store-Level Security Camera (CCTV) Audit & LP Integration | CCTV audit |
| W209 | Barangay & Local Community Relationship Management | Community relations |
| W216 | BIR CAS Compliance Audit | BIR CAS audit |
| W469 | Customer Complaint DTI Escalation & Consumer Adjudication Management | DTI complaint adjudication case management |
| W271 | Data Subject Access & Deletion Requests (DPA Compliance) | DSAR handling |
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

### Other Phase 2 (18 workflows)

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

## Tier 3: Advanced Optimization (124 Workflows)

These 124 workflows deliver advanced capabilities for competitive differentiation, AI-driven automation, and deep business analytics.

### Innovation & Digital Transformation (7 workflows)

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

### Internal Audit (15 workflows)

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

### Fleet & Logistics (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W196 | Route Planning & Dispatch Optimization | Route optimization |
| W197 | Driver Performance & Safety Management | Driver management |
| W198 | Fuel Management & Consumption Monitoring | Fuel management |
| W199 | Fleet Telematics & Real-Time Tracking | Telematics |

### Hazmat & Safety (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W141 | Workplace Safety Inspection & Audit | Safety inspection |
| W187 | Contractor & Third-Party On-site Safety Orientation | Contractor safety |
| W236 | Hazmat Storage & Segregation Compliance (DC) | Hazmat storage |
| W237 | Hazmat Handling & Safety Training (Store) | Hazmat training |

### Extended IT (4 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W131 | IT Asset Lifecycle Management | IT asset management |
| W132 | Software Development & Change Management | Change management |
| W257 | Enterprise API & Systems Integration Lifecycle Management | API lifecycle |
| W265 | POS Terminal Hardware Maintenance & Peripheral Management | POS hardware |

### Advanced Treasury (3 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W318 | Short-Term Investment & Surplus Cash Placement | Investment management |
| W324 | Supply Chain Finance & Dynamic Discounting Program | SCF program |
| W325 | Corporate Guarantee & Contingent Liability Management | Guarantee management |

### Advanced Master Data (3 workflows)

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

| Phase | Label | Workflow Count | % of Total |
|---|---|---|---|
| Phase 1 | Go-Live Critical | 162 | 32.6% |
| Phase 2 | Operational Excellence | 211 | 42.0% |
| Phase 3 | Innovation & Optimization | 125 | 25.4% |
| **Total** | | **498** | **100%** |

### By Domain and Phase

| Domain | Total | Phase 1 | Phase 2 | Phase 3 |
|---|---|---|---|---|
| Store Operations | 69 | 24 | 32 | 13 |
| IT Operations | 44 | 15 | 23 | 6 |
| Finance & Treasury | 43 | 33 | 10 | 0 |
| Internal Audit & Risk Management | 41 | 0 | 0 | 41 |
| Master Data Management (MDM) | 41 | 16 | 25 | 0 |
| Compliance & Governance | 25 | 4 | 19 | 2 |
| Procurement & Vendor Management | 22 | 12 | 10 | 0 |
| Inventory Management | 20 | 14 | 6 | 0 |
| Merchandising & Pricing | 19 | 2 | 17 | 0 |
| Treasury & Corporate Finance | 18 | 4 | 11 | 3 |
| HR & Payroll | 16 | 8 | 8 | 0 |
| Customer Experience | 13 | 1 | 11 | 1 |
| Marketing Campaigns | 12 | 0 | 0 | 12 |
| Warehouse & Logistics | 11 | 7 | 3 | 1 |
| Ecommerce | 11 | 7 | 4 | 0 |
| Supply Chain Planning | 11 | 6 | 5 | 0 |
| Corporate Governance, Legal & Strategy | 12 | 1 | 2 | 9 |
| Installation & Value-Added Services | 11 | 0 | 1 | 10 |
| Project-Based B2B & Trade Sales | 8 | 0 | 8 | 0 |
| Real Estate & Lease Management | 7 | 0 | 7 | 0 |
| Fleet Operations & Driver Management | 5 | 0 | 1 | 4 |
| Innovation & Digital Transformation | 5 | 0 | 0 | 5 |
| ESG & Sustainability Reporting | 5 | 0 | 0 | 5 |
| Engineering & Construction | 5 | 0 | 0 | 5 |
| Health, Safety & Environment | 4 | 1 | 1 | 2 |
| Facility & Asset Maintenance (HQ & DC) | 4 | 0 | 3 | 1 |
| Hazardous Materials (Hazmat) & Compliance | 4 | 0 | 2 | 2 |
| Regulatory Permits & Local Government Compliance | 7 | 7 | 0 | 0 |
| Wholesale & Reseller Operations | 3 | 0 | 0 | 3 |
| Document Management (DOC) | 2 | 0 | 2 | 0 |

### Operational Tier Guidance

1. **Tier 1 workflows** (162) are critical for baseline operations and financial transactions.
2. **Tier 2 workflows** (211) add necessary control and support capabilities to stabilize the business.
3. **Tier 3 workflows** (125) enable optimization, AI integration, and strategic differentiation.
4. **Cross-tier dependencies**: Some Tier 2/3 workflows reference Tier 1 workflows (e.g., W329 references W130); the core Tier 1 workflows must be stable for Tier 2/3 to generate value.

---

*Date: 2026-06-07 | Workflow Criticality Classification v3.4 — classifies 498 workflows into 3 operational tiers. Tier 1: 162 core workflows. Tier 2: 211 standard support workflows. Tier 3: 125 advanced optimization workflows.*
