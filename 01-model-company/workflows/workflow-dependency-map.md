# Workflow Dependency Map

> Directed dependency graph of all 498 operational workflows, showing prerequisite
> relationships for system functions. Use this map to understand data dependencies
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
    → W423 (AR PDC Warehousing)
    → W425 (Bounced Check Recovery)
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

W331 (DTI Application)
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

**Total**: 48 workflows in the deepest dependency chain (all Tier 1)

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

## 5. Circular Data Loop Risks

The following circular data flows must be managed during steady-state operations:

| Risk ID | Description | Operational Mitigation |
|---|---|---|
| CIRC-001 | W31 (Demand Forecasting) needs historical transaction data from W5B, but W2A (Auto-PO) needs W31 forecasts to generate purchase orders | Rolling 12-month historical sales data is maintained in the data warehouse to seed continuous forecasting runs |
| CIRC-002 | W312 (Replenishment Parameters) needs W4 operating data to tune ROP/EOQ, but W4 needs W312 parameters to calculate replenishment | Baseline planning parameters are set manually and tuned quarterly using active inventory logs |
| CIRC-003 | W9A (Month-End Close) needs W42 (Physical Inventory) results, but W42 needs a frozen system state during count | Schedule physical inventory audits during off-peak windows and briefly freeze posting periods during Z-report reconciliations |
| CIRC-004 | W15 (Recruitment) populates employee master used by W10 (Payroll), but payroll must run even if recruitment is undergoing updates | Maintain active HR onboarding data integrations to feed payroll without latency |

---

## 6. Dependency Matrix (Summary Table)

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

*Date: 2026-06-09 | Workflow Dependency Map v2.0 — covers 483 classified workflows across 30 domains with hard/soft/integration dependencies. 48-workflow Tier 1 critical path. Top 10 most-depended-upon workflows: W252 (Item Master), W253 (Customer Master), W254 (Location Master), W287 (Vendor Master), W289 (Pricing Master), W288 (Financial COA), W5B (In-Store Selling), W4 (Replenishment), W9A (Month-End Close), W10 (Payroll). Total repository workflows: 1,163.*
