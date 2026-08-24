# Workflow Dependency Map

> Directed dependency graph of classified operational workflows, showing prerequisite
> relationships for system functions. Of 5,355 total workflows, 5,349 are classified into
> criticality tiers (the confirmed register holds 5,372 rows, incl. 23 `###` parent/summary
> sub-workflows); 6 (W5497–W5502, added 2026-08-24 as post-catalog workflow-level gap fills in
> existing core/statutory value streams) are unclassified with keyword-driven proposed tiers
> pending a confirmation pass (see
> [`workflow-criticality-classification.md`](workflow-criticality-classification.md)).
> Use this map to understand data dependencies
> between workflows during business-as-usual operations.
>
> Back to [Workflow Index](README.md) | See also: [Criticality Classification](workflow-criticality-classification.md)

---

## How to Read This Map

- **A → B**: Workflow B cannot function correctly until Workflow A is operational
- **Hard dependency**: B is blocked without A (e.g., W7 AP needs W2 PO to do 3-way match)
- **Soft dependency**: B is degraded but not blocked without A (e.g., W31 demand forecasting is more accurate with W252 item master, but can run with basic data)
- **Integration dependency**: B and A share a critical integration point (e.g., POS ↔ ERP requires both W5B and the ERP to be live)

### Dependency Types

| Symbol | Type | Meaning |
|---|---|---|
| **→** | Hard Prerequisite | Downstream workflow cannot execute without upstream |
| **⇢** | Soft Prerequisite | Downstream workflow can execute but is degraded without upstream |
| **↔** | Bidirectional Integration | Both workflows must be operational simultaneously |

---

## 1. Master Data Dependency Tree

Master data workflows are the deepest foundation. Every transactional workflow depends on the
master data it references.

### 1.1 Foundational Masters (Tier 1 — All Hard Dependencies)

```
W252 (Item Master)
  → W4 (Store Replenishment)
  → W6 (Cycle Counting)
  → W40 (Regular Price Change Execution)
  → W13 (Promotions & Pricing Execution)
  → W2A (Auto-Replenishment)
  → W2B (Import POs)
  → W3 (Warehouse Receiving)
  → W5B (In-Store Selling)
  → W11 (BOPIS)
  → W19 (Home Delivery)
  → W42 (Physical Inventory)
  → W91 (Damaged Goods)
  → W432 (Solo Parent Discount — eligible SKU filtering)
  → W438 (Yard Dispatch — item identification)

W253 (Customer Master)
  → W8 (AR — Trade & Corporate)
  → W5B (In-Store Selling — loyalty lookup)
  → W11 (BOPIS — customer identification)
  → W24 (Credit Application)
  → W108 (Customer Credit Collection)
  → W170 (Senior Citizen/PWD)
  → W263 (Loyalty Enrollment)
  → W328 (Credit Limit Review)
  → W432 (Solo Parent — ID capture & verification)

W254 (Location Master)
  → W4 (Store Replenishment — source/destination)
  → W16 (New Store Opening)
  → W54 (LGU Permits)
  → W54A (BIR CAS Registration)
  → W310 (Address/PSGC Governance)
  → W433 (DENR SMR/CMR — location-based environmental reporting)
  → W437 (Branch De-registration — location decommissioning)

W287 (Vendor Master)
  → W2 (Purchase Orders)
  → W7 (AP Invoice Processing)
  → W36 (Vendor Onboarding)
  → W88 (Return to Vendor)
  → W20 (VMI)
  → W110 (Supplier Quality)

W288 (Financial Master — COA, Cost Centers)
  → W9A (Month-End Close)
  → W9B (Year-End Close)
  → W10 (Payroll — GL posting)
  → W14 (Intercompany Transactions)
  → W26 (Annual Budget)
  → W288 (Cost Center Governance) ⇢ W242 (3PL Performance Review — cost center tracking)

W289 (Pricing Master)
  → W5B (In-Store Selling — price lookup)
  → W40 (Price Change Execution)
  → W13 (Promotions Execution)
  → W107 (Pricing Hierarchy Governance)
  → W329 (Competitive Price Response)

W311 (Barcode/GTIN Governance)
  → W5B (In-Store Selling — barcode scan)
  → W3 (Warehouse Receiving — barcode scan)
  → W11 (BOPIS — item identification)
  → W19 (Home Delivery — item identification)
  → W109 (Store Receiving)

W312 (Replenishment Parameter Governance)
  → W2A (Auto-Replenishment — ROP/EOQ parameters)
  → W4 (Store Replenishment — min/max levels)
  → W31 (Demand Forecasting — parameter inputs)
  → W56 (Backorder Management — reorder thresholds)
```

### 1.2 Extended Masters (Tier 2 — Mixed Hard/Soft)

```
W290 (Category Structure)
  → W1 (Merchandise Planning)
  → W102 (Category P&L)
  → W299 (Assortment/Store Cluster)

W292 (Employee Master)
  → W10 (Payroll)
  → W34 (Shift Scheduling)
  → W15 (Recruitment — hire-to-master)
  → W43 (Offboarding)
  → W72 (Performance Management)
  → W251 (Statutory Benefits)
  → W426 (Annual COI Disclosure)

W297 (Warehouse Location/Bin Master)
  → W3 (Warehouse Receiving — putaway bin)
  → W4 (Store Replenishment — pick bin)
  → W42 (Physical Inventory — bin count)
  → W106 (DC Outbound Dispatch)

W300 (Promotional Rule Master)
  → W13 (Promotions Execution)
  → W57 (Promo Stock Allocation)
  → W262 (Store Promo Setup)

W313 (Loyalty Configuration Master)
  → W17 (Loyalty Program Operations)
  → W104 (Loyalty Financial Governance)
  → W263 (Loyalty Enrollment)

W295 (Payment Terms Master)
  → W2 (PO — payment terms default)
  → W7 (AP — payment due date calculation)
  → W8 (AR — collection due date)
  → W244 (Vendor Invoice Dispute)
```

### 1.3 Advanced Masters (Tier 3)

```
W314 (Planogram Template Master)
  → W86 (Planogram Compliance)
  → W262 (Store Promo Setup)

W315 (Product Lifecycle Master)
  → W68 (Product Discontinuation)
  → W64 (New Product Pilot)
  → W279 (Product Substitution Rules)

W316 (Digital Asset Master)
  → W50 (PIM — product images)
  → W83 (Campaign Planning)
  → W190 (Creative Production)
```

---

## 2. Core Transactional Dependency Chains

### 2.1 Procure-to-Pay Chain

```
W31 (Demand Forecasting)
  → W2A (Auto-Replenishment PO)
  → W3 (Warehouse Receiving)
  → W7 (AP Invoice — 3-way match)
    → W424 (AP PDC Issuance — for lease/rent)
    → W89 (Bank Reconciliation)
    → W90 (Tax Filing)
  → W9A (Month-End Close)
```

**Hard dependencies**: W31 → W2A → W3 → W7 → W9A

### 2.2 Order-to-Cash Chain (B2C)

```
W289 (Pricing Master)
  → W5B (In-Store Selling)
  → W5F (Store Closing/EOD)
    → W99 (Payment Settlement Reconciliation)
    → W170 (SC/PWD Reporting)
  → W9A (Month-End Close — revenue posting)
```

### 2.3 Order-to-Cash Chain (B2B)

```
W24 (Credit Application)
  → W8 (AR — Trade & Corporate)
    → W1380 (Customer PDC Receipt, Register & Deposit)
    → W1381 (Bounced Check Resolution & BIR Reporting)
    → W108 (Customer Credit Collection)
    → W81 (Bad Debt Provisioning)
    ⇢ W328 (Credit Limit Review)
    → W475 (Customer CWT / Form 2307 Collection)
  → W9A (Month-End Close — AR aging)
```

### 2.4 Ecommerce Fulfillment Chain

```
W19 (Home Delivery Fulfillment)
  ⇢ W5B (In-Store Selling — for ship-from-store W19B)
  → W215 (Home Delivery Returns)
  → W267 (Digital Payment Reconciliation)

W11 (BOPIS)
  ⇢ W5B (In-Store Selling — for in-store pickup)
  → W247 (Smart Locker)
  → W12B (Online-Initiated Returns)
```

### 2.5 Inventory Lifecycle Chain

```
W2B (Import POs)
  → W447 (DTI-BPS Product Certification)
  → W144 (International Logistics)
    → W191 (Incoterm/Marine Insurance)
    → W249 (Port Demurrage)
    → W284 (Customs Bonded Warehouse)
  → W3 (Warehouse Receiving)
  → W4 (Store Replenishment)
  → W5B (In-Store Selling)
  → W12 (Returns & Exchanges)
    → W22B (Store-to-DC Return)
    → W91 (Damaged Goods Disposition)
    → W92 (Inventory Adjustment)
    → W193 (Waste Management)
    → W443 (Salvage & Scrap Disposition)
  → W42 (Annual Physical Inventory)
  → W220 (SLOB Provisioning)
```

### 2.6 Payroll Chain

```
W15 (Recruitment/Onboarding)
  → W10 (Payroll Processing)
    → W251 (Statutory Benefits — SSS/PhilHealth/Pag-IBIG)
    → W280 (Wage Garnishment)
    → W76 (Employee Loans)
    → W74 (Expense Reimbursement)
    → W429 (Promodizer Incentives)
  → W448 (LGU Sanitary & Health Permits)
  → W43 (Separation/Offboarding)

W269 (Vendor Promodizers)
  → W449 (Promodizer Labor Compliance)
```

### 2.7 Store Operations Chain

```
W16 (New Store Opening)
  → W54 (LGU Permits)
    → W430 (LGU On-Site Inspection)
  → W54A (BIR CAS Registration)
  → W5A (Store Opening — daily)
  → W5B (In-Store Selling)
  → W5F (Store Closing/EOD)
  → W5G (Offline POS Recovery)

W5B (In-Store Selling)
  → W12 (Returns & Exchanges)
  → W17 (Loyalty Program)
  → W28 (Gift Card/Store Credit)
  → W33 (Warranty Claims)
  → W75 (Layaway/Installment Sales)
  → W170 (SC/PWD Discount)
    ⇢ W432 (Solo Parent Discount Compliance)
  → W330 (In-Store Emergency Response)
  → W428 (Community Disaster Relief)
  → W438 (Yard Dispatch & Loading)
  → W537 (Card Terminal & Acquirer Settlement — card transactions from selling)
  → W539 (Promotional Coupon/Voucher & Manufacturer Coupon Processing — coupon processing at checkout)
  → W540 (BIR Invoice Reprint/Adjustment & Credit Note Issuance — checkout reprints/credit notes)
  → W542 (Quotation & Estimate Generation with Sales Conversion — quotation converts to sale)
  → W543 (Consignment Sell-Through Transaction Processing — checkout processes consignment items)
  → W544 (Service Work Order Creation & Scheduling — checkout creates service work orders)
  → W545 (Special Order & Customer Order Processing — checkout creates special orders)
  → W546 (Deposit & Progress Payment Collection — checkout collects project deposits)
  → W547 (Scan & Go / Mobile Self-Scan Checkout — scan & go alternative checkout)
  → W548 (Third-Party On-Demand Delivery Integration — checkout triggers on-demand delivery)
  → W549 (Damaged & Open-Box Item Discount Processing — checkout processes damaged items)
  → W550 (Loyalty Points as Payment Tender — checkout accepts loyalty points)
  → W551 (Customer On-the-Spot Loyalty Enrollment — checkout triggers enrollment)
  → W552 (Donation & Charity Round-Up Processing — checkout triggers donation prompt)
  → W553 (Pricing Error Detection & Immediate Correction — checkout detects price errors)

W2747 (DTI Application)
  → W427 (DTI Monitoring & Compliance)

W517 (POS Cashier Shift Handover)
  → W537 (Card Terminal & Acquirer Settlement — shift handover triggers card batch close)
  → W541 (Cash Office Operations & Bank Deposit Preparation — shift handover triggers cash office)

W5F (Store Closing/EOD)
  → W537 (Card Terminal & Acquirer Settlement — EOD triggers settlement)
  → W541 (Cash Office Operations & Bank Deposit Preparation — EOD triggers cash office close)

W533 (POS Real-Time Event Streaming)
  → W538 (Real-Time LP Exception Monitoring — event stream feeds LP monitoring)
  → W543 (Consignment Sell-Through Processing — event stream publishes ownership transfer)
  → W553 (Pricing Error Detection — event stream publishes discrepancy events)

W196 (Route Planning)
  → W431 (LGU Truck Ban Governance)
```

### 2.8 Warehouse Operations Chain

```
W585 (DC Dock Scheduling & Appointment Management)
  → W3C (DC Inbound Scheduling)
  → W3 (Warehouse Receiving)
  → W3B (Yard/Outdoor Management)
  → W4 (Store Replenishment — pick/pack/ship)
    → W106 (DC Outbound Dispatch)
    → W270 (Pallet/RTP Tracking)
  → W46 (Kit/Bundle Assembly)
  → W42 (Physical Inventory — DC count)

W584 (DC Daily Operations & Shift Management)
  ⇢ W3 (Receiving — throughput data)
  ⇢ W106 (Dispatch — loading data)
  ⇢ W585 (Dock Scheduling — appointment data)
  ⇢ W586 (KPI Dashboard — performance data feed)

W586 (DC Daily KPI Dashboard & Performance Tracking)
  ⇢ W44 (Vendor Scorecard — quality data cross-reference)
  ⇢ W52 (Fleet — delivery performance)
  ⇢ W242 (3PL Review — carrier performance data)
```

### 2.9 Philippine Statutory Compliance Chain

```
W170 (SC/PWD Discount)
  ⇢ W432 (Solo Parent Discount Compliance)

W140 (OHS Incident Management)
  → W436 (Annual OHS Statutory Reporting)

W54 (LGU Permits)
  → W437 (Regulatory Branch De-registration)
  → W476 (BFP FSIC Management)
    → W54 (LGU Business Permit Renewal)

W114 (Sustainability Reporting)
  ⇢ W433 (DENR SMR/CMR Reporting)

W477 (DENR PTO/WDP Compliance)
  → W433 (DENR SMR/CMR Reporting)

W478 (BIR Annual Inventory List Submission)
  ← W42 (Annual Physical Inventory)
  ← W9A (Month-End Close)
  → W90 (Monthly Tax Filing & Statutory Remittance)

W479 (FDA License to Operate for HHS Compliance)
  → W36 (Vendor Onboarding)
  → W252 (Item Master)

W480 (CAAP Height Clearance Permit Compliance)
  → W116 (Site Selection)
  → W225 (Store Construction Management)

W53 (Data Privacy Breach Response)
  ⇢ W434 (NPC Annual DPO & System Registration)

W5B (POS Selling) / W8 (AR Invoicing)
  → W473 (BIR EIS e-Invoicing Compliance)

W8 (AR Invoicing)
  → W475 (Customer CWT / Form 2307 Collection)
    → W90 (Monthly Tax Filing) / W260 (eFPS Filing) / W140 (Corporate Income Tax)
```

### 2.10 Intercompany & Corporate Chain

```
W14 (Intercompany Transactions)
  → W435 (Intercompany SLA Fee Billing)
```

---

## 3. Cross-Domain Integration Dependencies

These workflow pairs share critical real-time integration points and must be operational
simultaneously.

### 3.1 POS ↔ ERP

| POS Workflow | ERP Module | Integration Dependency |
|---|---|---|
| W5B (In-Store Selling) | Inventory | Real-time inventory deduction per sale |
| W5B (In-Store Selling) | Financials | Revenue posting, VAT computation |
| W5B (In-Store Selling) | CRM/Loyalty | Loyalty point earn/redeem at POS |
| W5F (Store Closing/EOD) | Financials | Cash reconciliation, settlement |
| W5G (Offline Recovery) | Inventory/Financials | Offline transaction sync/replay |
| W12 (Returns & Exchanges) | Inventory | Return to stock or quarantine |
| W12 (Returns & Exchanges) | Financials | VAT reversal, refund processing |
| W170 (SC/PWD) | Financials | VAT-exempt transaction reporting |
| W473 (e-Invoicing) | Tax / Compliance | Real-time sales transaction data transmission |
| W537 (Card Terminal Settlement) | Financials | Card batch close, acquirer settlement reconciliation |
| W538 (Real-Time LP Monitoring) | Loss Prevention | Real-time exception alerting from POS event stream |
| W540 (BIR Invoice Reprint/Credit Note) | Tax / Compliance | BIR-compliant credit note and invoice adjustment |
| W541 (Cash Office Operations) | Financials | Cash reconciliation, bank deposit posting |
| W543 (Consignment Sell-Through) | Inventory/Financials | Consignment ownership transfer, vendor settlement trigger |
| W547 (Scan & Go Checkout) | POS / Inventory | Mobile self-scan basket validation and payment |
| W548 (On-Demand Delivery) | Ecommerce / Logistics | Third-party delivery partner order dispatch |
| W550 (Loyalty Points as Tender) | CRM/Loyalty | Loyalty point redemption and balance update |
| W553 (Pricing Error Detection) | Pricing / Compliance | Real-time price discrepancy alert and correction |

### 3.2 Ecommerce ↔ ERP

| Ecom Workflow | ERP Module | Integration Dependency |
|---|---|---|
| W11 (BOPIS) | Inventory | Real-time store-level stock visibility |
| W11 (BOPIS) | Store Operations | Pick notification, SLA tracking |
| W19 (Home Delivery) | Inventory/WMS | Stock reservation, pick/pack |
| W19 (Home Delivery) | Financials | Payment capture, order invoicing |
| W246 (Drop-Ship) | Procurement | Back-to-back PO auto-generation |
| W215 (Returns) | Inventory | Return-to-stock or QC quarantine |

### 3.3 Finance ↔ Operations

| Finance Workflow | Operations Workflow | Integration Dependency |
|---|---|---|
| W7 (AP Invoice) | W3 (Warehouse Receiving) | 3-way match: PO ↔ GR ↔ Invoice |
| W7 (AP Invoice) | W18 (DSD Receiving) | Store-level 3-way match |
| W8 (AR) | W5B (Trade Account Sales) | Credit limit enforcement at POS |
| W9A (Month-End Close) | W42 (Inventory Count) | Inventory valuation adjustment |
| W9A (Month-End Close) | W4 (Replenishment) | Accrued purchases in-transit |
| W85 (Product Costing) | W2B (Import POs) | Landed cost allocation |
| W277 (Freight Bill Audit) | W2 (PO) | Freight vendor 3-way match |

### 3.4 HR ↔ Operations

| HR Workflow | Operations Workflow | Integration Dependency |
|---|---|---|
| W10 (Payroll) | W251 (Statutory Benefits) | SSS/PhilHealth/Pag-IBIG deduction |
| W34 (Shift Scheduling) | W5A/W5F (Store Open/Close) | Staff coverage verification |
| W34 (Shift Scheduling) | W67 (Store Performance) | Labor cost vs. revenue analysis |
| W172 (PPE/Uniform) | W10 (Payroll) | Lost PPE payroll deduction |
| W584 (DC Daily Operations) | W585 (Dock Scheduling) | Appointment data feeds pace check |
| W584 (DC Daily Operations) | W586 (KPI Dashboard) | Shift log feeds end-of-day KPI snapshot |
| W585 (Dock Scheduling) | W3 (Receiving) | Appointment feeds gate check and dock assignment |
| W585 (Dock Scheduling) | W106 (Dispatch) | Outbound dock slot assignment for load planning |
| W585 (Dock Scheduling) | W44 (Vendor Scorecard) | Appointment compliance and no-show rate |
| W586 (KPI Dashboard) | W584 (DC Daily Operations) | KPI data feeds daily management decisions |
| W586 (KPI Dashboard) | W3 (Receiving) | Receiving throughput and accuracy KPIs |
| W586 (KPI Dashboard) | W106 (Dispatch) | Dispatch on-time rate and truck utilization |
| W586 (KPI Dashboard) | W52 (Fleet) | Delivery performance and carrier metrics |

---

## 4. Dependency Heat Map by Operational Criticality Tier

### Tier 1: Deepest Dependency Chain (Core Operations)

The following chains represent the minimum viable path. Every workflow in each chain
must be operational at pilot go-live.

```
[Master Data Layer]
  W252 (Item) → W253 (Customer) → W254 (Location) → W287 (Vendor) → W288 (Financial COA)
  → W289 (Pricing) → W311 (Barcode/GTIN) → W312 (Replenishment Params)

      ↓

[Procurement Layer]
  W2A (Auto-PO) → W2B (Import PO) → W3 (Receiving) → W88 (RTV)

      ↓

[Inventory Layer]
  W4 (Replenishment) → W6 (Cycle Count) → W22 (Transfers) → W56 (Backorders)

      ↓

[Sales Layer]
  W5B (Selling) → W5F (EOD) → W5G (Offline) → W12A (Returns)
  W11 (BOPIS) → W19 (Home Delivery)

      ↓

[Financial Layer]
  W7 (AP) → W7D (AP Statement Rec) → W8 (AR) → W475 (CWT / Form 2307 Collection) → W9A (Month-End) → W14 (IC)
  → W89 (Bank Rec) → W90 (Tax Filing) → W478 (BIR Inventory List) → W99 (Payment Settlement) → W260 (BIR eFPS)
  → W261 (E-Wallet Settlement) → W473 (BIR EIS e-Invoicing Compliance)

      ↓

[HR/Payroll Layer]
  W10 (Payroll) → W251 (Statutory Benefits)

      ↓

[Compliance Layer]
  W37 (LP/Exception) → W54 (LGU Permits) → W476 (BFP FSIC) → W54A (BIR CAS) → W468 (Price Freeze) → W140 (OHS Incidents) → W477 (DENR PTO/WDP) → W479 (FDA LTO) → W480 (CAAP Height Clearance)
```

**Total**: 46 workflows in the deepest dependency chain (all Tier 1)

### Tier 2: Operational Support Chains

These chains add support capabilities on top of Tier 1:

```
Tier 1 Foundation
  ↓
[Merchandising Layer]
  W1 (Assortment) → W27 (Rebates) → W50 (PIM) → W64 (Pilot Test) → W93 (Markdown)
  → W102 (Category P&L) → W107 (Pricing Hierarchy) → W129 (Private Label)
  → W130 (Competitor Intel) → W329 (Tactical Response)
  ↓
[Extended Operations]
  W16 (New Store Opening) → W47 (Facility Maint) → W67 (Performance Review)
  → W86 (Planogram) → W96 (Renovation) → W176 (Reverse Logistics)
  ↓
[Customer Experience]
  W41 (Complaints) → W58 (Corporate Accounts) → W61 (Price Match) → W65 (CSAT)
  → W87 (Feedback Loop) → W103 (Trade Sales) → W112 (Pro Desk) → W258 (Ticketing)
  → W259 (Call Center)
  ↓
[Compliance & Audit]
  W49 (BC/Disaster) → W77 (BIR Audit) → W82 (Hazmat) → W95 (External Audit)
  → W114 (Sustainability) → W158 (BC Drills) → W185 (Product Liability)
```

### Tier 3: Advanced Optimization Layer

Tier 3 workflows depend on Tier 1 and Tier 2 foundations but not each other:

```
Tier 1+2 Foundation
  ↓
W200 (AI Personalization) — depends on W156 (CDP) [Tier 2]
W201 (RPA Lifecycle) — depends on W132 (Change Mgmt) [Tier 3]
W202 (Predictive Maintenance) — depends on W240 (DC Maintenance) [Tier 2]
W203 (Computer Vision) — depends on W86 (Planogram) [Tier 2] + W207 (CCTV) [Tier 2]
W208 (Retail Analytics) — depends on W113 (BI/Data Gov) [Tier 1] + W35 (Reporting) [Tier 1]
```

---

## 5. Critical Path Analysis

### Longest Dependency Chain (End-to-End)

This represents the maximum sequence of hard dependencies a single process must traverse:

```
W31 (Demand Forecasting)
 → W312 (Replenishment Parameters)
 → W2B (Import PO)
 → W144 (International Logistics)
 → W3 (Warehouse Receiving)
 → W4 (Store Replenishment)
 → W5B (In-Store Selling)
 → W5F (Store Closing)
 → W99 (Payment Settlement)
 → W9A (Month-End Close)
 → W35 (Management Reporting)
```

**Chain length**: 11 workflows. **Minimum configuration time**: ~12 weeks (assuming 1 week per major workflow group).

### Top 10 Most Depended-Upon Workflows

These workflows are prerequisites for the largest number of downstream workflows:

| Rank | Workflow | Depended-On By | Reason |
|---|---|---|---|
| 1 | W252 — Centralized Item Master | 45+ workflows | Every item-consuming process |
| 2 | W253 — Customer Master | 30+ workflows | Every customer-facing process |
| 3 | W254 — Location Master | 25+ workflows | Every location-aware process |
| 4 | W287 — Vendor Master | 20+ workflows | Every procurement and AP process |
| 5 | W289 — Pricing Master | 18+ workflows | Every selling process |
| 6 | W288 — Financial Master (COA) | 15+ workflows | Every financial posting |
| 7 | W5B — In-Store Selling | 15+ workflows | Core revenue process; feeds returns, loyalty, reporting |
| 8 | W4 — Store Replenishment | 12+ workflows | Linking inventory to store operations |
| 9 | W9A — Month-End Close | 12+ workflows | Consolidation point for all financial transactions |
| 10 | W10 — Payroll Processing | 10+ workflows | Employee master, statutory, loans, expenses |

---

## 6. Circular Data Loop Risks

The following circular data flows must be managed during steady-state operations:

| Risk ID | Description | Operational Mitigation |
|---|---|---|
| CIRC-001 | W31 (Demand Forecasting) needs historical transaction data from W5B, but W2A (Auto-PO) needs W31 forecasts to generate purchase orders | Rolling 12-month historical sales data is maintained in the data warehouse to seed continuous forecasting runs |
| CIRC-002 | W312 (Replenishment Parameters) needs W4 operating data to tune ROP/EOQ, but W4 needs W312 parameters to calculate replenishment | Baseline planning parameters are set manually and tuned quarterly using active inventory logs |
| CIRC-003 | W9A (Month-End Close) needs W42 (Physical Inventory) results, but W42 needs a frozen system state during count | Schedule physical inventory audits during off-peak windows and briefly freeze posting periods during Z-report reconciliations |
| CIRC-004 | W15 (Recruitment) populates employee master used by W10 (Payroll), but payroll must run even if recruitment is undergoing updates | Maintain active HR onboarding data integrations to feed payroll without latency |

---

## 7. Dependency Matrix (Summary Table)

| Upstream → Downstream | Dependency Type | Impact if Missing |
|---|---|---|
| MDM (W252–W316) → All Transactional | Hard | No master data = no transaction processing |
| Procurement (W2) → AP (W7) | Hard | No 3-way match possible |
| Receiving (W3) → Inventory (W4/W6/W22) | Hard | No stock visibility |
| Selling (W5B) → Reporting (W35/W67/W102) | Soft | Reports lack transaction detail |
| Ecommerce (W11/W19) → Returns (W12B/W215) | Hard | No return authorization |
| Payroll (W10) → Statutory (W251/W280) | Hard | Non-compliance with PH labor law |
| Pricing (W289) → All Selling | Hard | Cannot process sales |
| EOD (W5F) → Finance (W89/W99) | Hard | Cash/payment discrepancies unmonitored |
| Month-End (W9A) → Tax (W90) | Hard | Cannot file BIR returns |
| Audit (W120) → All Operations | Soft | No independent verification |
| Import (W2B) → Regulatory (W447) | Hard | Goods blocked at port |
| Onboarding (W15) → Health (W448) | Hard | Non-compliance with LGU sanitary rules |

---

## 8. Cross-Cutting Program Dependencies (VS-79–VS-192)

> The Statutory deepening (VS-79–VS-88) and thirty gap-analysis passes (2026-06-14 through 2026-06-21)
> — with the post-Pass-30 PA-127.4 extension (W5489–W5496) and the post-catalog workflow-level
> additions (W5497 in VS-84.2 and W5502 in VS-83.3) — together added 114 value streams /
> 2,746 workflows that are predominantly
> **cross-cutting overlays** on the Tier-1 core: governance,
> assurance, finance-deepening, and technology-platform programs that consume master
> data and transactions from the foundational value streams. This section captures the
> VS-level prerequisite wiring declared inline in their PA files, so the dependency graph
> is no longer limited to the original classified register. Mined by
> `grep` over every `links to VS-NN` / `VS-NN` reference in VS-79–VS-192 PA and README files.

### 8.1 Anchor value streams (where the gap-analysis programs hook in)

The foundational value streams most referenced by VS-79–VS-192. These confirm that the
**gap-analysis programs are largely Tier 2/3 overlays** (they sit *on top of*
Record-to-Report, Audit, IT Ops, Analytics, HR, and Legal), with the **statutory exceptions
called out in §8.2** that are themselves Tier 1. Counts are freshly recomputed across the full
VS-79–VS-192 range (PA + README files); they supersede the v4.3 snapshot (mined over VS-79–VS-191),
which had drifted as content was added and whose top-10 omitted VS-91 while listing VS-100 — the v4.3
counts themselves superseded the v3.7 snapshot mined over a narrower range.

| Anchor VS | Value Stream | References from VS-79–VS-192 |
|---|---|---|
| VS-17 | Record-to-Report | 1,984 |
| VS-100 | Legal Operations, Litigation & IP | 1,607 |
| VS-21 | Internal Audit & Risk | 1,543 |
| VS-27 | IT Operations & Security | 1,231 |
| VS-28 | Data, Analytics & BI | 1,117 |
| VS-19 | Hire-to-Retire | 998 |
| VS-91 | Consumer Data Privacy & Data Protection Program | 977 |
| VS-13 | Customer Experience & Loyalty | 889 |
| VS-24 | Health, Safety & Environment | 868 |
| VS-22 | Compliance & Regulatory | 844 |

### 8.2 Cross-cutting Tier-1 statutory / revenue-critical programs

These gap-analysis programs are **themselves Tier 1** (statutory or revenue-critical) and
must be sequenced with the core compliance chain in §4. Primary upstream edges:

| Program | Primary upstream dependencies |
|---|---|
| VS-79 Tax Management & BIR Statutory Reporting | VS-17 (R2R postings), VS-87 (customs/duty), VS-16/68 (AR/AP tax), VS-22 (permits) |
| VS-85 Mandatory Discount & Tax Credit Recovery | VS-08 (POS discount execution), VS-16 (AR), VS-79 (tax credit filing) |
| VS-89 Product Recall & Safety Corrective Action | VS-10/65 (channel notification), VS-03/31 (vendor/quality), VS-32 (returns) |
| VS-91 Consumer Data Privacy & Data Protection | VS-88 (records/legal hold), VS-27 (security), VS-13/10/75 (PII channels) |
| VS-114 Dangerous Goods / Hazmat Transport & Compliance | VS-24 (fixed-site HSE), VS-06/110 (transport), VS-87 (customs), VS-10 (ecommerce ship-eligibility) |
| VS-117 DTI-BPS Product Standards / PS Mark / ICC | VS-31 (quality), VS-03 (vendor cert), VS-87 (import clearance), VS-89 (recall) |
| VS-118 Revenue Assurance & Pricing Integrity | VS-08 (POS), VS-17 (revenue), VS-21 (audit), VS-23 (shrink vector split) |
| VS-125 Cross-Channel Fraud Management | VS-80 (payment ops), VS-13/10 (channels), VS-23 (physical shrink), VS-86 (AML) |
| VS-178 Landbanking, Site Acquisition & Agrarian/LGU Zoning Conversion | VS-15 (capex/AP for acquisition), VS-17 (property accounting/RPT), VS-18 (treasury/funding), VS-20 (handoff to construction PMO), VS-97 (portfolio) |
| VS-179 Extended Producer Responsibility (EPR) Compliance & Plastic Recovery | VS-01 (item-master packaging weights), VS-03 (supplier packaging cert), VS-25 (ESG reporting), VS-73 (store waste ops), VS-87 (customs/recovery) |
| VS-180 Disaster Relief Supply Chain Logistics & Humanitarian Aid | VS-06 (fleet/freight), VS-04 (DC staging), VS-02 (supply/replenishment), VS-08 (price-lock execution), VS-79 (tax relief/BIR casualty loss) |
| VS-187 Household Hazardous Waste, Paint & Used-Product Stewardship Take-Back | VS-73 (store waste), VS-25 (ESG), VS-114 (DG transport), VS-179 (EPR), VS-31 (quality) |
| VS-188 Trade Reseller Floor-Plan & Dealer Inventory Financing | VS-16 (AR), VS-18 (treasury/funding line), VS-17 (loan accounting/ECL), VS-03 (vendor dual-payee), VS-68 (credit risk) |
| VS-189 Trade Accounts Receivable Factoring, Invoice Discounting & Securitization | VS-16 (AR eligibility), VS-18 (treasury), VS-17 (PFRS 9 true-sale), VS-80 (lockbox/cash app), VS-68 (credit risk) |
| VS-190 Operational Technology (OT) / ICS Cybersecurity & Retail Tech Asset Protection | VS-27 (IT security), VS-23 (CCTV/EAS ops), VS-24 (life-safety), VS-99 (asset lifecycle), VS-26 (BCP/incident) |
| VS-191 Customer Construction Debris, Demolition Waste & Site Cleanup | VS-06 (hauling/fleet), VS-12/66/143 (jobsite-generating services), VS-25 (ESG), VS-73 (waste), VS-111 (RTI/containers) |
| VS-192 Green Fleet Transition, EV Fleet Operations & Sustainable Transportation | VS-06 (fleet register/telematics/maintenance), VS-166 (LTO/LTFRB license & franchise portfolio), VS-24 (DOLE-OSH high-voltage/battery-fire safety), VS-79 (EVIDA incentives/tax), VS-17 (capital & loan accounting), VS-25 (ESG Scope-1 GHG reporting) |

### 8.3 Cross-cutting platform / governance programs (Tier 2/3 overlays) and consumers

These programs provide a shared platform or governance layer consumed by many other
value streams. They depend on the Tier-1 core but are not themselves go-live blocking
(except where noted); schedule them in Phase 2/3.

| Program | Consumers & dependencies |
|---|---|
| VS-126 Customer Data Platform / Single Customer View | Consumers: VS-13 (loyalty), VS-14 (personalization), VS-107 (key account), VS-10/75 (digital). Depends on VS-29 (master data), VS-91 (consent). |
| VS-127 S&OP / Integrated Business Planning | Consumers: VS-02 (supply), VS-101 (merch financial plan), VS-106 (commodity), VS-33 (strategy). Depends on VS-01 (assortment), VS-17 (finance). |
| VS-128 AI/ML Governance & Responsible AI | Governs the AI in VS-125/126/127, VS-30.2 (engineering), VS-28 (analytics). Depends on VS-91 (privacy), VS-27 (security), VS-21 (audit), VS-100 (legal). |
| VS-115 Calibration / Metrology / Measurement Traceability | Underpins revenue & inventory accuracy for VS-08 (POS scales), VS-09 (cutting/paint), VS-31 (quality). Depends on VS-35 (asset), VS-20.3 (facility). |
| VS-113 Enterprise Architecture / Application Portfolio | Governs the landscape for VS-27 (ops), VS-99 (ITAM), VS-30 (innovation), VS-28 (data). Depends on VS-33 (strategy), VS-112 (PMO). |
| VS-105 Supply Chain Finance & Working Capital | Consumers: VS-15 (P2P), VS-18 (treasury). Depends on VS-03 (vendors), VS-39 (rebates). |
| VS-110 Freight Procurement / Carrier Mgmt / Freight Audit | Consolidates freight spend sprinkled across VS-02.2/04/06. Depends on VS-06 (logistics), VS-15 (AP). |
| VS-112 Corporate PMO | Governs portfolios in VS-20/37/109/108/27/06. Depends on VS-40 (capex accounting), VS-33 (strategy). |
| VS-129 Competition & Antitrust Compliance (RA 10667 / PCC) | Conduct controls layered on pricing (VS-57), vendor/trade terms (VS-03/VS-11/VS-43/VS-82), association conduct (VS-104), and marketplace/retail-media (VS-95/VS-48); owns the merger-notification gate on VS-130. Depends on VS-100 (legal), VS-88 (records), VS-21 (audit). |
| VS-130 Corporate Development, M&A & Divestiture | Executes inorganic growth; consumes strategy (VS-33), capex (VS-40), treasury (VS-18); secures PCC clearance via VS-129 and legal/IP via VS-100. Depends on VS-100, VS-17 (finance), VS-36 (governance). |
| VS-131 Human Rights & Responsible Supply Chain Due Diligence | Due-diligence overlay on global sourcing (VS-122) and the vendor base (VS-03/VS-67); feeds ESG reporting (VS-25) and ethics intake (VS-119). Depends on VS-122, VS-03, VS-25. |
| VS-132 Corporate Political Engagement & Election Compliance | Governance of political activity/associations (VS-104), B2G (VS-46), and comms (VS-14); anti-graft/ABC interface (VS-86/VS-119). Depends on VS-104, VS-119, VS-36. |
| VS-133 Operational Excellence, Process Mining & CI | Continuous-improvement OS over the ~5,355 workflows; mines ERP event logs (VS-15/VS-10/VS-04); shares benefit tracking with VS-17.4 and VS-135. Depends on VS-21 (audit), VS-17, VS-30 (innovation). |
| VS-134 Organizational Change Management & Digital Adoption | People-side of transformation; equips PMO portfolio (VS-112), HR/EX (VS-103), training (VS-19.4), and the service desk (VS-27); runs a DAP over cloud ERP. Depends on VS-103, VS-133, VS-112. |
| VS-135 Technology Business Management, IT Financial Mgmt & FinOps | Financial governance of tech spend; consumes ITAM (VS-99), EA portfolio (VS-113), FP&A (VS-17.4), procurement (VS-34), and cloud ops (VS-27). Depends on VS-17, VS-27, VS-99. |
| VS-136 Supply Chain Network Design, MEIO & Flow Engineering | Structural network/inventory engineering; consumes supply planning (VS-02), S&OP (VS-127), logistics (VS-06), DC ops (VS-04), and real estate (VS-97/VS-20). Depends on VS-02, VS-28 (analytics), VS-01. |
| VS-137 Product Information Management (PIM) & DAM | Canonical product-content/DAM platform consumed by ecommerce (VS-10), retail media (VS-48), marketplace (VS-65/VS-95), in-store (VS-09), and master data (VS-29); owns SDS/certificate lifecycle feeding DG (VS-114) and DTI-BPS (VS-117). Depends on VS-29, VS-01, VS-113. |
| VS-138 Integrated Facilities Management, Workplace Services & BMS | Consolidates facilities/building services sprinkled across VS-20.3, VS-07.2, VS-120, VS-98, VS-73, VS-23; owns the BMS executing energy control (VS-120) and the guard-force coordination (VS-23). Depends on VS-20, VS-35, VS-34, VS-97. |
| VS-139 Trade Show, Exhibition & Field Event Marketing | Event-marketing operating model for the ~40% B2B base; feeds leads to field sales (VS-140)/key accounts (VS-107)/trade (VS-11); vendor co-fund via VS-39, permits/ABC via VS-22/VS-86. Depends on VS-14, VS-11, VS-107. |
| VS-140 Field Sales, Outside Sales & Route-to-Market Force Management | Field-force coverage of the ~5,400 B2B accounts; consumes CRM/CDP (VS-11/VS-126), generates trade/project pipeline (VS-11/VS-107), comp via VS-102, enablement via VS-124. Depends on VS-11, VS-107, VS-126. |
| VS-141 Employee Transport, Shuttle & Daily Commute Management | Daily people-movement for ~6,762 staff; distinct from business travel (VS-19.1), goods fleet (VS-06), and facilities (VS-138); allowance via payroll (VS-19.2)/comp (VS-102), vendor via VS-34/VS-56, safety via VS-24. Depends on VS-19, VS-103, VS-34. |
| VS-142 Cash-on-Delivery (COD) Operations & Driver Cash Reconciliation | Enterprise COD cash chain; distinct from acquirer settlement (VS-80), last-mile (VS-06.3), and in-store cash (VS-08.2); cash collected by 3PL drivers (VS-56), reconciled to GL (VS-17.1)/AR (VS-16), fraud via VS-125, treasury/float via VS-18. Depends on VS-80, VS-06.3, VS-17.1, VS-125. |

### 8.4 Notable per-program anchor edges (strongest declared dependencies)

Top-3 upstream value streams per gap-analysis program (by inline-reference count),
for the programs with the heaviest cross-cutting footprint:

| Program | Top upstream anchors |
|---|---|
| VS-97 | VS-17(26), VS-79(23), VS-20(22) |
| VS-98 | VS-34(28), VS-19(23), VS-24(18) |
| VS-99 | VS-27(71), VS-91(24), VS-34(21) |
| VS-100 | VS-22(27), VS-88(26), VS-21(21) |
| VS-101 | VS-17(34), VS-02(29), VS-03(17) |
| VS-102 | VS-19(63), VS-17(22), VS-103(18) |
| VS-103 | VS-19(44), VS-102(29), VS-27(26) |
| VS-104 | VS-14(26), VS-86(25), VS-88(22) |
| VS-105 | VS-18(43), VS-17(35), VS-15(26) |
| VS-106 | VS-101(50), VS-21(30), VS-17(30) |
| VS-107 | VS-13(51), VS-11(33), VS-01(29) |
| VS-108 | VS-25(26), VS-17(23), VS-35(23) |
| VS-109 | VS-01(35), VS-40(32), VS-20(27) |
| VS-110 | VS-04(45), VS-17(34), VS-03(31) |
| VS-111 | VS-03(32), VS-25(31), VS-31(29) |
| VS-112 | VS-40(55), VS-33(38), VS-36(24) |
| VS-113 | VS-27(82), VS-112(51), VS-99(34) |
| VS-114 | VS-24(45), VS-21(26), VS-06(22) |
| VS-116 | VS-18(58), VS-17(46), VS-100(37) |
| VS-118 | VS-17(47), VS-28(37), VS-08(34) |
| VS-119 | VS-21(65), VS-100(38), VS-36(36) |
| VS-120 | VS-25(60), VS-20(45), VS-17(34) |
| VS-121 | VS-103(64), VS-19(46), VS-28(27) |
| VS-122 | VS-86(32), VS-02(32), VS-87(30) |
| VS-123 | VS-19(64), VS-103(28), VS-07(25) |
| VS-124 | VS-01(36), VS-19(35), VS-13(32) |
| VS-125 | VS-13(40), VS-80(39), VS-10(39) |
| VS-126 | VS-13(57), VS-91(57), VS-28(52) |
| VS-127 | VS-101(42), VS-122(41), VS-02(38) |
| VS-128 | VS-91(55), VS-27(48), VS-21(42) |
| VS-129 | VS-100(25), VS-88(24), VS-104(16) |
| VS-130 | VS-100(34), VS-17(25), VS-36(21) |
| VS-131 | VS-122(49), VS-03(49), VS-25(27) |
| VS-132 | VS-104(45), VS-119(39), VS-36(32) |
| VS-133 | VS-21(27), VS-17(21), VS-28(18) |
| VS-134 | VS-103(57), VS-133(36), VS-27(21) |
| VS-135 | VS-17(46), VS-27(33), VS-99(30) |
| VS-136 | VS-02(63), VS-28(31), VS-01(31) |
| VS-143 | VS-06(44), VS-17(34), VS-25(30) |
| VS-144 | VS-17(38), VS-24(35), VS-19(34) |
| VS-145 | VS-07(40), VS-05(34), VS-01(32) |
| VS-146 | VS-13(75), VS-07(39), VS-21(36) |
| VS-147 | VS-24(52), VS-21(34), VS-07(32) |
| VS-148 | VS-17(65), VS-21(42), VS-18(36) |
| VS-149 | VS-08(78), VS-23(57), VS-13(25) |
| VS-150 | VS-24(51), VS-22(40), VS-19(18) |
| VS-151 | VS-23(64), VS-04(34), VS-01(29) |
| VS-152 | VS-17(36), VS-36(35), VS-21(33) |
| VS-153 | VS-21(65), VS-17(58), VS-26(49) |
| VS-154 | VS-11(39), VS-22(36), VS-21(33) |
| VS-155 | VS-17(52), VS-12(48), VS-05(39) |
| VS-156 | VS-22(55), VS-21(43), VS-17(37) |
| VS-157 | VS-11(26), VS-17(22), VS-13(12) |
| VS-158 | VS-17(39), VS-01(23), VS-11(13) |
| VS-159 | VS-26(50), VS-21(32), VS-14(20) |
| VS-160 | VS-19(52), VS-21(18), VS-17(14) |
| VS-161 | VS-21(51), VS-03(26), VS-26(26) |
| VS-162 | VS-06(30), VS-26(26), VS-23(22) |
| VS-163 | VS-13(29), VS-17(29), VS-25(21) |
| VS-164 | VS-10(45), VS-13(45), VS-23(36) |
| VS-165 | VS-11(46), VS-46(41), VS-12(23) |
| VS-166 | VS-21(39), VS-17(29), VS-28(24) |
| VS-167 | VS-23(29), VS-21(27), VS-28(19) |
| VS-168 | VS-14(45), VS-48(38), VS-07(33) |
| VS-169 | VS-19(61), VS-24(48), VS-03(44) |
| VS-170 | VS-18(72), VS-17(66), VS-05(53) |
| VS-171 | VS-13(54), VS-24(50), VS-10(49) |
| VS-172 | VS-13(37), VS-11(31), VS-28(25) |
| VS-173 | VS-17(52), VS-18(52), VS-36(44) |
| VS-174 | VS-16(40), VS-13(30), VS-23(30) |
| VS-175 | VS-24(55), VS-17(33), VS-06(32) |
| VS-176 | VS-17(27), VS-43(27), VS-13(23) |
| VS-177 | VS-07(34), VS-23(29), VS-28(27) |
| VS-178 | VS-15(8), VS-17(7), VS-18(7) |
| VS-179 | VS-21(34), VS-03(29), VS-06(17) |
| VS-180 | VS-06(45), VS-04(31), VS-03(19) |
| VS-181 | VS-16(23), VS-04(20), VS-18(17) |
| VS-182 | VS-18(10), VS-31(9), VS-17(7) |
| VS-183 | VS-19(22), VS-17(9), VS-07(7) |
| VS-184 | VS-35(6), VS-40(6), VS-24(5) |
| VS-185 | VS-17(12), VS-08(10), VS-16(6) |
| VS-186 | VS-12(23), VS-26(14), VS-06(9) |
| VS-187 | VS-25(17), VS-24(10), VS-21(8) |
| VS-188 | VS-17(18), VS-18(17), VS-16(16) |
| VS-189 | VS-16(33), VS-18(27), VS-17(23) |
| VS-190 | VS-26(28), VS-21(27), VS-24(20) |
| VS-191 | VS-25(26), VS-06(20), VS-24(20) |
| VS-192 | VS-06(79), VS-25(42), VS-138(27) |

> **Note on §8.3 / §8.4 coverage:** the curated program tables above cover every gap-analysis program in VS-79–VS-192 — §8.3 platform/governance programs (Tier 2/3 overlays) through VS-142, §8.4 top-anchor edges through VS-192, and §8.2 the Tier-1 statutory programs (including the Pass 26–29 additions VS-178/179/180/187/188/189/190/191 and the VS-192 statutory programs — W5482 DOE/LTO/LTFRB green-fleet compliance and W5483 DOLE-OSH EV/battery safety — confirmed Tier 1 by the 2026-06-28 Full-Coverage Confirmation Pass; VS-192's 24 workflows are classified 3 T1 / 15 T2 / 6 T3). The §8.1 anchor reference counts are mined across the full VS-79–VS-192 range.

*Date: 2026-08-24 | Workflow Dependency Map v4.10 — consistency review #26: §8.1 anchor-table VS-13 count refreshed 888 → 889 (the review's W673/W3889 segmentation layer-notes add one inbound VS-13 reference from the VS-126 block; membership unchanged). Prior v4.9 — post-catalog workflow-level additions incorporated: W5497 (VS-84.2) and W5502 (VS-83.3) joined the VS-79–VS-192 block, so the §8 intro block size is corrected 114 value streams / 2,744 → 2,746 workflows and the §8.1 anchor table is freshly recomputed from disk (VS-100 1,602→1,607; VS-27 1,229→1,231; VS-19 990→998; VS-91 972→977; VS-13 887→888; membership unchanged). The four core-value-stream additions (W5498 VS-19.3, W5499 VS-36.1, W5500 VS-10.1, W5501 VS-21.2) sit outside the §8 block and require no edge changes here; their step-level edge incorporation into §1–§7 follows their confirmation pass. Intro totals re-pointed to 5,355 workflows / 5,349 classified / 6 keyword-proposed. Prior v4.8 — PDC consistency repair: the §2.3 Order-to-Cash (B2B) chain nodes W423/W425 are re-pointed to the canonical customer-side workflows W1380 (Customer PDC Receipt, Register & Deposit) and W1381 (Bounced Check Resolution & BIR Reporting), both defined in VS-16; the treasury-side companions W423 (vault custody, maturity monitoring, on-date deposit, clearing, forecast feed) and W425 (GL reversal, penalty, NSF flag) remain in VS-18 as execution scope downstream of the canonical pair. No edge-count changes. Prior v4.7 — consistency review #15: §8.2 gains the VS-192 row (its Tier-1 statutory programs — W5482 DOE/LTO/LTFRB green-fleet compliance, W5483 DOLE-OSH high-voltage/battery-fire safety — were confirmed by the 2026-06-28 Full-Coverage Confirmation Pass; upstream edges mined from VS-192's own PA/README references: VS-06, VS-166, VS-24, VS-79, VS-17, VS-25), and the §8 coverage note's claim that VS-192 still awaited criticality review (true when v4.5 shipped earlier that day, superseded hours later by the confirmation pass) is corrected — all 24 VS-192 workflows are classified (3 T1 / 15 T2 / 6 T3). Validator Check 27 Part B now guards against unclassified-workflow claims in this map. Prior v4.6 — intro and footer counts updated for the 2026-06-28 Full-Coverage Confirmation Pass (all 5,349 workflows now classified; register 5,372 rows; proposed register empty; post-v4.1 confirmed pending edge incorporation 1,608 → 4,204). Prior v4.5 — §8 extended to the full VS-79–VS-192 block, executing the incorporation v4.4 had flagged as pending: heading, §8.1 header, and §8.4 coverage note ranges now end at VS-192; the intro's block size corrected to 114 value streams / 2,744 workflows (including the post-Pass-30 PA-127.4 extension, W5489–W5496); the §8.1 anchor table freshly recomputed from disk — the recompute also repairs the v4.3 table's membership error (it omitted VS-91 — Consumer Data Privacy, 972 references — from the top-10 while listing in-block VS-100, and VS-07 at 828 now ranks #11) and refreshes counts drifted by post-v4.3 content; §8.4 gains the VS-192 row (top anchors VS-06(79), VS-25(42), VS-138(27), mined with the rule verified to reproduce the VS-191 row exactly). Validator Check 26 now guards the block's self-declared range, block counts, §8.4 end-row, and §8.1 top-10. Prior v4.4 (2026-06-21): covers prerequisite relationships across all 188 value streams / 5,349 workflows (Pass 23 added VS-173, W5009–W5032; Pass 24 added VS-174–VS-176, W5033–W5104; Pass 25 added VS-177, W5105–W5128; Pass 26 added VS-178–VS-181, W5129–W5224; Pass 27 added VS-182–VS-185, W5225–W5320; Pass 28 added VS-186–VS-189, W5321–W5416; Pass 29 added VS-190–VS-191, W5417–W5464; Pass 30 added VS-192, W5465–W5488). §1–§7 cover the dependency edges among the 1,168 confirmed-classified register rows as of v4.1 (the 4,204 workflows confirmed since v4.1 — 1,272 across the seven 2026-06-20 classification batches v7.19 statutory, v7.20 support & governance, v7.21 operational support, v7.22 mixed operations, v7.23 shared services, v7.24 sixth batch, v7.25 final family-decisive batch, plus 336 in the Pass 26–29 confirmation v7.26 — are pending edge incorporation into the detailed step-level chains); §8 added the VS-79–VS-191 cross-cutting program dependencies mined from inline `links to VS-NN` references in PA and README files (§8.1 anchor counts recomputed across the full VS-79–VS-191 range in v4.3; curated program tables §8.2–§8.4 then extended through VS-191, closing the prior VS-143–VS-191 follow-up tabulation gap; VS-192 (Pass 30) edge/program incorporation into §8 was flagged pending and was completed in v4.5). v4.3 recomputed §8.1 anchor reference counts across all VS-79–VS-191 workflow files (PA + README) — those superseded the v3.7 snapshot, which was mined over VS-79–VS-161 and had drifted slightly as content was added (the counts were always mined from PA *and* README files, not PA files alone). The final batch was confirmed by the 2026-06-28 Full-Coverage Confirmation Pass (unclassified 2,596 → 0; workflow-criticality-proposed.md now empty); their step-level edge incorporation into §1–§7 follows the same incremental path as the batches before them. The retired VS numbers (49–52) remain unused; see [`workflow-gap-analysis.md`](workflow-gap-analysis.md) for the thirty-pass history.*
