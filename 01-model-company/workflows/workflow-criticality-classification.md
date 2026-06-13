# Workflow Criticality Classification

> Classifies 1,167 operational workflows into operational criticality tiers.
> An additional 1,677 workflows (2,844 total − 1,167 classified) remain unclassified pending review.
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

## Tier 1: Core Operations (439 Workflows)

These 439 workflows are foundational to daily store and supply chain operations.
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

### Core HR & Payroll (6 workflows)

| ID | Workflow | Operational Significance |
|---|---|---|
| W10 | Payroll Processing | 6,715 employees; 5 entities × 2 runs/month |
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

### Core Compliance & IT (28 workflows)

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

## Tier 2: Standard Support (499 Workflows)

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

## Tier 3: Advanced Optimization (229 Workflows)

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

| Phase | Label | Workflow Count | % of Classified |
|---|---|---|---|
| Phase 1 | Go-Live Critical (Tier 1) | 439 | 37.6% |
| Phase 2 | Operational Excellence (Tier 2) | 499 | 42.8% |
| Phase 3 | Innovation & Optimization (Tier 3) | 229 | 19.6% |
| **Classified Total** | | **1,167** | 100% |
| Unclassified (pending review) | Default Tier 2 (pending review) | 1,677 | — |
| **Grand Total** | | **2,844** | — |

### Domain Breakdown

The per-tier subsection headings above (Core Finance, Extended Store Operations, Internal Audit, etc.) provide the authoritative domain-and-phase breakdown of the 1,167 classified workflows, and the [value-stream-index.md](./value-stream-index.md) provides the authoritative value-stream/process-area breakdown of all 2,844 workflows. A rolled-up "by domain" summary table was removed during consistency review because it could not be reconciled with the tier totals and presented stale partial counts.

> **2026-06-14 addition:** Value streams VS-79 through VS-88 (240 workflows, W2753–W2992) were added covering Tax Management & BIR Statutory Reporting, Payment Operations & Acquirer Settlement, Cash-in-Transit & Armored Car Operations, Sari-Sari Store & MSME Micro-Wholesale, Occupational Health & Employee Wellness, Labor Relations & Collective Bargaining, Mandatory Discount & Tax Credit Recovery, Anti-Financial Crime (AML/KYC/ABC), Customs Trade Compliance & Tariff Optimization, and Document Control & Records Retention. These 240 workflows are currently **unclassified** (counted in the 1,677 unclassified above) pending criticality review; many warrant Tier 1 classification (BIR tax filing, AML/STR reporting, CBA administration, mandatory-discount tax credit recovery, CIT operations) and will be assigned in a follow-up classification pass.

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

*Date: 2026-06-14 | Workflow Criticality Classification v7.2 — 1,167 classified workflow references are deduplicated across tiers (Tier 1: 439 · Tier 2: 499 · Tier 3: 229 = 1,167). An additional 1,677 workflows remain unclassified (2,844 total − 1,167 classified). 22 classified references are parent/summary workflows (e.g., W2, W5B, W9A) that appear as `###` sub-headings within PA files. The authoritative tier summary is the `## Summary` table above; a stale `## Updated Summary` duplicate that reported a Tier 3 total of 226 and 0 unclassified (contradicting the correct 229 / 1,533) was removed during consistency review. The 2026-06-14 repo review retired VS-49/50/51/52 (96 placeholder workflows W2022–W2117), reducing the grand total from 2,940 to 2,844 and the unclassified count from 1,773 to 1,677.*
