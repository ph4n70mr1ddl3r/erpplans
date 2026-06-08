# Procurement & Vendor Management Workflows

> Purchase orders, vendor onboarding, VMI, special orders, vendor performance, contracts, vendor-funded promotional activity & co-op advertising management, vendor portal content management & self-service operations, vendor due diligence & onboarding site visit management, vendor-managed inventory (VMI) daily performance monitoring, strategic sourcing & category strategy, competitive bidding & tender management, purchase price variance (PPV) analysis & cost management, vendor seasonal buy-back & stock return agreement execution, and vendor product packaging sustainability assessment & compliance management.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W2. Procurement — Purchase Order Cycle](#w2-procurement-purchase-order-cycle)
- [W2C. Blanket Purchase Orders](#w2c-blanket-purchase-orders)
- [W20. Vendor Managed Inventory (VMI)](#w20-vendor-managed-inventory-vmi)
- [W36. Vendor Onboarding](#w36-vendor-onboarding)
- [W38. Special Order / Non-Stock Item Fulfillment](#w38-special-order-non-stock-item-fulfillment)
- [W44. Vendor Performance Review](#w44-vendor-performance-review)
- [W60. Emergency Procurement](#w60-emergency-procurement)
- [W62. Vendor Contract Lifecycle (Non-PO Contracts)](#w62-vendor-contract-lifecycle-non-po-contracts)
- [W88. Return to Vendor (RTV) Processing](#w88-return-to-vendor-rtv-processing)
- [W110. Supplier Quality & CAPA (Corrective and Preventive Action)](#w110-supplier-quality-capa-corrective-and-preventive-action)
- [W115. Supplier Diversity & MSME Development Program](#w115-supplier-diversity-msme-development-program)
- [W136. Indirect / Non-Merchandise Procurement](#w136-indirect-non-merchandise-procurement)
- [W150. Product Quality Testing & Certification](#w150-product-quality-testing-certification)
- [W155. Vendor Strategic Collaboration & Joint Business Planning (JBP)](#w155-vendor-strategic-collaboration-joint-business-planning-jbp)
- [W160. Private Label Factory Audit & Social Compliance](#w160-private-label-factory-audit-social-compliance)
- [W161. Vendor Price Protection & Market Markdown Claims](#w161-vendor-price-protection-market-markdown-claims)
- [W244. Vendor Invoice Dispute & Discrepancy Resolution](#w244-vendor-invoice-dispute-discrepancy-resolution)
- [W245. Vendor Performance Chargebacks & Penalties Management](#w245-vendor-performance-chargebacks-penalties-management)
- [W422. VMI Collaborative Data Sharing & Replenishment Execution](#w422-vmi-collaborative-data-sharing-replenishment-execution)
- [W491. Supplier Financial Health & Credit Risk Monitoring](#w491-supplier-financial-health-credit-risk-monitoring)
- [W513. Vendor-Funded Promotional Activity & Co-op Advertising Management](#w513-vendor-funded-promotional-activity-co-op-advertising-management)
- [W593. Vendor Portal Content Management & Self-Service Operations](#w593-vendor-portal-content-management-self-service-operations)
- [W620. Vendor Due Diligence & Onboarding Site Visit Management](#w620-vendor-due-diligence--onboarding-site-visit-management)
- [W621. Vendor-Managed Inventory (VMI) Daily Performance Monitoring](#w621-vendor-managed-inventory-vmi-daily-performance-monitoring)
- [W631. Strategic Sourcing & Category Strategy](#w631-strategic-sourcing--category-strategy)
- [W632. Competitive Bidding & Tender Management](#w632-competitive-bidding--tender-management)
- [W633. Purchase Price Variance (PPV) Analysis & Cost Management](#w633-purchase-price-variance-ppv-analysis--cost-management)
- [W705. Vendor Self-Service Portal Operations & Supplier Collaboration](#w705-vendor-self-service-portal-operations-supplier-collaboration)
- [W706. Supplier Performance Scorecard & Quarterly Business Review](#w706-supplier-performance-scorecard-quarterly-business-review)
- [W901. Vendor Seasonal Buy-Back & Stock Return Agreement Execution](#w901-vendor-seasonal-buy-back--stock-return-agreement-execution)
- [W915. Vendor Product Packaging Sustainability Assessment & Compliance Management](#w915-vendor-product-packaging-sustainability-assessment--compliance-management)

---

## W2. Procurement — Purchase Order Cycle

### W2A. Auto-Replenishment (Stocking Items)

| Field | Detail |
|---|---|
| **Trigger** | SKU hits reorder point (ROP) in system |
| **Frequency** | Daily review; POs generated daily |
| **Volume** | ~1,200 merchandise POs/month (auto-replenishment + ad-hoc); ~18,000 PO lines/month; excludes ~80–240 blanket/contract release orders/month (W2C), ~20–30 import POs/month (W2B), and ~30–50 non-merchandise POs/month (capex, IT, supplies); total all types: ~1,400–1,600 POs/month |

> **PO-to-GR ratio**: ~1,200 merchandise POs generate ~6,000 DC goods receipts/month (W3) — an average of ~5 GRs per PO. This ratio reflects partial shipments (vendors delivering across multiple drops), scheduled phased deliveries for large POs, and blanket PO releases each generating a separate GR. Import POs (W2B) typically generate 1 GR per container. DSD POs delivered to stores generate store-level GRs (W18) outside the DC receiving workflow.
| **Owner** | Buyer |
| **Participants** | System (auto-suggest), Buyer, Category Manager (approval if > PHP 50K) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System calculates ROP breaches based on: avg daily demand × lead time + safety stock | System | — | Automated |
| 2 | System generates suggested POs grouped by vendor, consolidated across DCs | System | — | Automated |
| 3 | Buyer reviews suggested PO list each morning: check quantities, adjust if needed | Buyer | Category Manager | 1–2 hours/day |
| 4 | Buyer confirms or modifies PO quantities, delivery dates, and DC destinations | Buyer | Category Manager | 1–2 hours/day |
| 5 | If PO total > PHP 50K: route to Category Manager for approval | Category Manager | Category Manager | 15 min/PO |
| 6 | If PO total > PHP 500K: route to VP Merchandising for approval | VP Merchandising | VP Merchandising | 15 min/PO |
| 7 | Approved PO transmitted to vendor (email, EDI, or vendor portal); vendors with portal access can view PO details, confirm delivery dates, and submit invoices through the portal | System / Buyer | Buyer | Automated |
| 8 | Buyer tracks open POs; follows up on overdue deliveries | Buyer | Buyer | 1 hour/day |

**Total buyer effort**: ~3–5 hours/day for daily PO review and follow-up

### PO Lifecycle: Amendment, Cancellation & Close

| Activity | Trigger | Approval | System Action |
|---|---|---|---|
| **PO Amendment** | Buyer needs to change quantity, delivery date, price, or add/remove lines on an approved PO | Re-approval per tiered matrix (same thresholds as original PO: > PHP 50K → Category Manager, > PHP 500K → VP Merchandising, > PHP 2M → CFO for imports) if change exceeds materiality threshold (quantity change > 20%, price change > 5%, or any delivery date change); minor changes (within threshold) auto-approved with Buyer note | System transmits amendment to vendor (email, EDI, or portal); tracks amendment history with full audit trail (original values, amended values, reason code, approver ID, timestamp); for import POs (W2B), Finance notifies bank if LC amendment is required for value changes |
| **PO Cancellation** | Vendor cannot deliver, demand drops, item discontinued, or PO no longer needed | Buyer initiates with reason code; Category Manager approval required for cancellations > PHP 50K; VP Merchandising for > PHP 500K | System checks for existing GR against PO: if no GR, auto-cancels with vendor notification; if partial GR, Buyer confirms close of remaining quantity; system releases budget commitment; cancelled PO retained in audit trail |
| **PO Auto-Close** | PO fully received (GR quantity matches ordered quantity within tolerance) or PO open beyond configured age limit | Automated | System auto-closes fully received POs; system flags POs open > 90 days for Buyer review (dashboard alert); Buyer reviews aged POs weekly and decides: close remaining quantity, extend delivery date (amendment), or escalate to Category Manager |

### System Touchpoints (PO Lifecycle)
- PO amendment workflow with materiality thresholds triggering re-approval (W2A)
- Amendment history with full audit trail: original vs. amended values, reason, approver (W2A)
- Vendor notification on amendment (email/EDI/portal) (W2A)
- Import PO LC amendment trigger (cross-reference W2B) (W2A)
- PO cancellation with reason code and budget release (W2A)
- Partial-receipt PO close workflow (W2A)
- Auto-close rules: tolerance-based for fully received POs; aging threshold for open POs (W2A)

### Pain Points / Risks
- Suggested PO quantities based on ROP may not reflect actual store-level demand patterns, especially during typhoon season or regional construction booms, leading to overstock in some DCs and stockouts in others
- Tiered approval bottleneck: POs above PHP 50K require Category Manager sign-off, and above PHP 500K need VP Merchandising; during peak seasonal buying (Q4), approval queues can delay PO transmission by 1–2 days, risking vendor lead-time slippage
- Aged open POs beyond 90 days indicate vendor delivery failures or buyer neglect; without disciplined weekly review, ghost commitments inflate budget reports and mask real procurement liabilities

### Time Estimate
- System ROP breach calculation and PO suggestion generation: automated (steps 1–2)
- Daily buyer PO review and confirmation: ~2–4 hours/day across all buyers (steps 3–4)
- Approval routing (Category Manager / VP Merch): ~15 min/PO for above-threshold orders (steps 5–6)
- Open PO tracking and overdue follow-up: ~1 hour/day across all buyers (step 8)
- PO amendment, cancellation, and auto-close management: ~2–3 hours/week across all buyers
- Total buyer effort: ~3–5 hours/day for daily PO review and follow-up; ~1,200 merchandise POs/month generated

### Staffing Implication
- **Buyers**: ~1,200 POs/month ÷ 10–12 buyers = ~100–120 POs/buyer/month. Daily review of ~3–5 hours/buyer/day is the core buying workload. Absorbed within existing team.
- **Category Managers**: Approval for POs > PHP 50K — estimated ~30% of POs trigger CM approval = ~360 approvals/month ÷ ~4 CMs = ~90/CM/month × ~15 min = ~22 hours/CM/month. Absorbed but significant.
- **VP Merchandising**: POs > PHP 500K — estimated ~5% of POs = ~60 approvals/month × ~15 min = ~15 hours/month. Absorbed within executive role.

### W2B. Import Purchase Orders

| Field | Detail |
|---|---|
| **Trigger** | Seasonal buy plan or replenishment of import SKUs |
| **Frequency** | ~20–30 import POs/month |
| **Volume** | ~400–600 TEUs/month across all import vendors (per model-company-profile §7.1); ~15–25 TEUs per major import PO |
| **Owner** | Buyer (with Import Coordinator) |
| **Participants** | Buyer, Import Coordinator, Finance (LC), Customs Broker, Warehouse (receiving) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer creates import PO with estimated landed cost (FOB + freight + duty + insurance) | Buyer | Category Manager | 30 min/PO |
| 2 | Route for approval (> PHP 50K → Category Manager; > PHP 500K → VP Merchandising; > PHP 2M → CFO) | Category Manager / VP / CFO | As per tier | 15–30 min/PO |
| 3 | Finance opens Letter of Credit (LC) with bank or arranges TT payment | Treasury Analyst | CFO | 1–2 hours/PO |
| 4 | Buyer confirms order with vendor; vendor provides Proforma Invoice | Buyer | Buyer | 30 min/PO |
| 5 | Import Coordinator arranges freight booking (container) | Import Coordinator | Buyer | 1 hour/PO |
| 6 | Vendor ships; provides Bill of Lading (BL), Packing List, Commercial Invoice | Vendor | — | External |
| 7 | Import Coordinator receives shipping docs; engages customs broker | Import Coordinator | Import Coordinator | 1 hour/PO |
| 8 | Customs broker files import entry; pays duties/taxes | Customs Broker | Import Coordinator | 1–2 days |
| 9 | Import Coordinator tracks shipment status; updates ETA in system | Import Coordinator | Buyer | 15 min/day per PO |
| 10 | Goods arrive at port; customs clearance and release | Customs Broker | Import Coordinator | 1–3 days |
| 11 | Transport to DC; Receiving clerk processes Goods Receipt | Receiving Clerk (DC) | DC Manager | 2–4 hours/container |
| 12 | System calculates actual landed cost (duty, freight, insurance allocated per SKU) using GR exchange rate | System | Finance | Automated |
| 13 | Finance reconciles LC/TT payment with PO and Goods Receipt; system posts FX gain/loss if invoice rate differs from GR rate | Treasury Analyst | CFO | 30 min/PO |

**Total cycle time**: 45–90 days from PO to receipt

### System Touchpoints
- ROP/EOQ auto-calculation per SKU per location (W2A.1–2)
- PO creation with multi-tier approval workflow (W2A.5–6)
- Vendor PO transmission (W2A.7)
- Open PO tracking / overdue alerts (W2A.8)
- Import PO tracking with LC/BL/container fields (W2B.1–9)
- Landed cost calculation engine (W2B.12)
- 3-way match: PO → Goods Receipt → Vendor Invoice (W2B.13)
- FX rate capture at PO creation (budget rate), goods receipt (spot rate or BSR), and invoice (actual rate); automatic FX gain/loss posting (W2B.12–13)
- Month-end FX revaluation of open foreign-currency balances at BIR exchange rate with unrealized FX gain/loss posting and auto-reversal (W9A.5a)

### Pain Points / Risks
- 45–90 day lead time exposes BuildRight to significant PHP/USD or PHP/CNY exchange rate volatility; a 5% adverse FX move on a PHP 2M import PO can erase category margin
- Port congestion in Manila (South Harbor / North Harbor) adds 3–7 days of uncontrolled delay; typhoon-season port closures can push receipt past the selling window for seasonal items
- Landed cost estimation at PO creation relies on estimated freight and duty rates; actual costs at receipt may differ materially, causing margin erosion that is only visible after goods are sold

### Time Estimate
- PO creation and approval (steps 1–2): ~45–60 min/PO
- LC/TT arrangement with Finance (step 3): ~1–2 hours/PO
- Freight booking and shipping coordination (steps 4–7): ~2–3 hours/PO spread over initial weeks
- Shipment tracking and customs clearance (steps 8–10): ~15 min/day/PO for tracking; 1–3 days customs clearance
- Receiving and landed cost calculation (steps 11–12): ~2–4 hours/container
- Payment reconciliation (step 13): ~30 min/PO
- Total active internal time per import PO: ~8–12 hours over 45–90 day cycle
- Aggregate: ~20–30 import POs/month × ~10 hours = ~200–300 hours/month across Buyer, Import Coordinator, and Finance

### Staffing Implication
- **Import Coordinator**: Dedicated role managing ~20–30 import POs/month — shipment tracking, customs broker coordination, document management. ~200–300 hours/month workload confirms this as a full-time position.
- **Buyers**: Import PO creation and vendor communication adds ~1 hour/PO = ~20–30 hours/month. Spread across buyers handling import categories.
- **Treasury Analyst**: LC/TT processing adds ~1–2 hours/PO = ~20–60 hours/month. Absorbed within existing Treasury team.
- **Customs Broker**: External partner; ~1–3 days clearance per shipment. Cost is per-entry fee.

---

## W2C. Blanket Purchase Orders

| Field | Detail |
|---|---|
| **Trigger** | Annual supply agreement negotiation cycle |
| **Frequency** | ~40–60 active contracts at any time; new contracts and renewals throughout the year |
| **Volume** | Primarily with top 50 vendors (by spend); typically covers 20–60% of purchasing volume for staple categories (cement, paint, lumber, electrical cable, plumbing fittings) |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, VP Merchandising, Finance (budget), Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer negotiates annual supply agreement with vendor: product range, pricing tiers, minimum/maximum commitment quantities, delivery schedule, payment terms, rebate structure | Buyer | Category Manager | 4–8 hours/vendor |
| 2 | Category Manager approves contract terms; VP Merchandising approves if total contract value > PHP 5M | Category Manager / VP | VP Merchandising | 30 min |
| 3 | Finance validates contract commitment against annual purchase budget | Controller | CFO | 30 min |
| 4 | Buyer creates Blanket PO in system: vendor, SKU lines with contract price, validity period (typically 1 year), min/max commitment quantities, agreed delivery schedule or release parameters | Buyer | Category Manager | 30–60 min |
| 5 | System enforces contract pricing on all release orders; alerts Buyer if release quantity would exceed maximum commitment | System | — | Automated |
| 6 | Buyer or system creates Release Order against Blanket PO (per agreed schedule or triggered by ROP): specifies exact quantity and delivery date for this release | Buyer / System | Buyer | 10 min |
| 7 | Release Order follows standard PO approval (W2A.5–6) if release value exceeds threshold; otherwise auto-approved within contract parameters | System | — | Automated |
| 8 | Vendor ships per release order; standard receiving (W3) and AP matching (W7) apply | Vendor | Buyer | Per W3/W7 |
| 9 | System tracks cumulative released quantity and value against contract commitment; Buyer monitors to ensure min-commit targets are met | System | Buyer | Automated |
| 10 | Monthly: Buyer reviews contract utilization report; identifies contracts below minimum commitment pace (risk of penalty or unfavorable renegotiation) | Buyer | Category Manager | 1 hour/month |
| 11 | Quarterly: Buyer and Category Manager evaluate contract performance vs. spot buying; decide renewal, renegotiation, or termination | Buyer + Category Manager | VP Merchandising | 2 hours/quarter |
| 12 | At contract expiry: system alerts Buyer 60 days before; if not renewed, system blocks further release orders | System | — | Automated |

**Contract coverage**: ~40–60 active blanket/contract POs at any time, representing ~45% of annual COGS (aligned with top-20 vendor concentration)

### Vendor Rebate Dispute Resolution

| Field | Detail |
|---|---|
| **Trigger** | Vendor disputes rebate settlement amount calculated by BuildRight's system (W27 step 6) |
| **Frequency** | Occasional — estimated 5–10 disputes/year |
| **Dispute SLA** | 15 business days from dispute raised to resolution |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, Cost Accountant, Finance Manager |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Vendor disputes settlement amount: Buyer receives vendor's written objection with vendor's calculation | Buyer | Category Manager | 15 min |
| 2 | Buyer and Cost Accountant jointly review: compare BuildRight's settlement data (qualifying volume, rebate rate applied) to vendor's claim; identify specific discrepancy (volume count difference, rate tier interpretation, timing gap, excluded transactions) | Buyer / Cost Accountant | Category Manager | 30–60 min |
| 3 | If BuildRight calculation confirmed correct: Buyer responds to vendor with supporting data; dispute closed; no settlement adjustment | Buyer | Category Manager | 15 min |
| 4 | If partial vendor claim valid: Buyer proposes adjusted settlement; Category Manager approves adjustment; Cost Accountant posts adjustment with Category Manager approval and documentation in system | Buyer / Category Manager / Cost Accountant | Finance Manager | 30 min |
| 5 | If dispute unresolved within 15 business days: Buyer escalates to Finance Manager for mediation; Finance Manager reviews both calculations and makes binding recommendation within 5 business days | Finance Manager | CFO | 30 min |
| 6 | Monthly: Cost Accountant tracks rebate dispute frequency and resolution time per vendor; feeds into vendor scorecard (W44); chronic disputing vendors flagged for contract renegotiation (W2C) | Cost Accountant | Controller | 15 min/month |

### System Touchpoints
- Blanket/contract PO creation with SKU lines, pricing tiers, validity dates, and commitment quantities (W2C.4)
- Contract pricing enforcement on release orders (W2C.5)
- Release order creation against blanket PO with quantity tracking (W2C.6–7)
- Cumulative commitment tracking: released vs. minimum vs. maximum (W2C.9)
- Contract utilization reporting (W2C.10)
- Contract expiry alerting with release order blocking (W2C.12)
- Integration with W27 (vendor rebates — rebates may be tied to contract commitment achievement; rebate dispute resolution per W27 dispute SLA of 15 business days)

### Pain Points / Risks
- Failing to meet minimum commitment quantities in blanket agreements triggers penalty clauses or unfavorable renegotiation at renewal; conversely, over-committing locks up working capital in excess inventory
- Contract pricing may lag spot-market drops (e.g., cement or steel commodity corrections), leaving BuildRight paying above-market rates for months until the next renegotiation window
- Vendor rebate disputes (step 6 of Vendor Rebate Dispute Resolution) consume significant Buyer and Finance time; chronic disputing vendors erode the administrative savings that blanket contracts are meant to deliver

### Staffing Implication
- **Buyers**: 40–60 contracts ÷ 10–12 buyers = ~4–5 contracts each. Monthly review adds ~1 hour/buyer/month. Quarterly evaluation adds ~2 hours/buyer/quarter. Absorbed within existing team.
- No incremental headcount beyond existing Buyer and Finance teams.

### Time Estimate
- Annual contract negotiation (step 1): ~4–8 hours/vendor
- Monthly contract utilization review (step 10): ~1 hour/month across all contracts
- Quarterly contract performance evaluation (step 11): ~2 hours/quarter
- Vendor rebate dispute resolution (when triggered): ~1–2 hours/dispute
- Total per contract/year: ~8–12 hours active time (concentrated during negotiation and review periods)
- Aggregate: ~40–60 contracts × ~10 hours = ~400–600 hours/year across all buyers

---

## W20. Vendor Managed Inventory (VMI)

| Field | Detail |
|---|---|
| **Trigger** | VMI vendor reviews sell-through data or system sends replenishment signal |
| **Frequency** | Varies by vendor (typically weekly or bi-weekly) |
| **Volume** | ~300 SKUs from 12 key vendors |
| **Owner** | Buyer (oversight) |
| **Participants** | VMI Vendor, Buyer, Receiving Clerk (DC or Store), AP Clerk |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System shares sell-through data and current stock levels with VMI vendor (EDI or portal) | System | Buyer | Automated |
| 2 | VMI vendor analyzes data and determines replenishment quantities | VMI Vendor | VMI Vendor | External |
| 3 | VMI vendor creates shipment; provides Advance Shipping Notice (ASN) to system | VMI Vendor | Buyer | External |
| 4 | Buyer reviews and confirms ASN; or system auto-confirms if within agreed parameters | Buyer / System | Buyer | 10 min/batch |
| 5 | Vendor ships goods to DC or store per agreement | VMI Vendor | — | External |
| 6 | Receiving Clerk processes Goods Receipt against ASN (standard receiving process) | Receiving Clerk | Dept. Supervisor / DC Supervisor | Per W3 or W18 |
| 7 | Goods recorded as vendor-owned inventory in system (non-valuated until sold) | System | — | Automated |
| 7a | At month-end close (W9): system accrues VMI liability for all VMI goods sold but not yet settled with vendor; Cost Accountant includes VMI accrual in monthly close entries | System / Cost Accountant | Controller | Automated + 15 min/month |
| 8 | At POS: system records sell-through event per VMI SKU; ownership transfers at point of sale | System | — | Automated |
| 9 | Monthly: system generates VMI sell-through report per vendor showing units sold × agreed price | System | Buyer | Automated |
| 10 | Buyer reviews sell-through report; confirms settlement | Buyer | Category Manager | 1 hour/month/vendor |
| 11 | System generates AP invoice from sell-through data; vendor payment processed | System / AP Clerk | AP Supervisor | Automated + 30 min |

**Settlement cycle**: Monthly per VMI vendor

### System Touchpoints
- Sell-through data export to vendor (EDI/portal/API) (W20.1)
- ASN receipt and processing from vendor (W20.3)
- Non-valuated (vendor-owned) inventory tracking (W20.7)
- Sell-through event capture at POS (W20.8)
- VMI settlement report generation (W20.9)
- Auto-generation of AP from sell-through (W20.11)
- Quarterly VMI vendor statement reconciliation: Cost Accountant generates VMI statement reconciliation report per vendor — compares BuildRight's recorded VMI sell-through (units sold × agreed price) to vendor's statement of goods shipped and settled; investigates discrepancies (unrecorded sell-through, missing GRs, pricing differences, timing gaps); reconciling items documented and resolved within 15 business days; unreconciled differences > PHP 50,000 escalated to Controller; results feed into annual IC audit and vendor scorecard (W44) (W20)
- Integration with W44 (vendor scorecard), W7 (AP settlement), W42 (physical inventory vendor-owned count)

### Pain Points / Risks
- VMI vendors control replenishment timing and quantities; if a vendor under-stocks, BuildRight loses sales with no penalty; if a vendor over-stocks, shelf space is consumed by slow-moving VMI items at the expense of higher-margin owned inventory
- Month-end VMI liability accrual (step 7a) depends on accurate sell-through capture at POS; system errors or offline POS terminals can understate VMI payable, creating reconciliation gaps and vendor disputes
- VMI settlement is based on agreed pricing, but promotional markdowns applied in-store without vendor notification can cause invoice discrepancies and delayed vendor payment

### Staffing Implication
- **Buyer time**: 12 VMI vendors × 1 hour/month review = 12 hours/month. Spread across 10–12 buyers, this is ~1 hour each per month. Minimal impact.
- **AP**: VMI settlement adds 12 additional AP invoices/month. Negligible incremental load.

### Time Estimate
- ASN review and confirmation: ~10 min/batch per replenishment cycle (weekly or bi-weekly)
- Monthly sell-through review and settlement confirmation: ~1 hour/vendor/month
- AP settlement processing: ~30 min/vendor/month
- Quarterly VMI statement reconciliation: ~1–2 hours/vendor/quarter
- Total per VMI vendor: ~2–3 hours/month ongoing
- Aggregate for 12 VMI vendors: ~24–36 hours/month (~3–5 hours/week)

---

## W36. Vendor Onboarding

| Field | Detail |
|---|---|
| **Trigger** | New vendor identified by Buyer or Category Manager (new product sourcing, alternative supplier, new brand) |
| **Frequency** | ~50–100 new vendors/year (replacing churned vendors + new categories) |
| **Volume** | Peaks during seasonal planning (W32) and new store openings (W16) |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, AP Clerk, Finance (credit assessment), IT (portal setup) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer identifies need for new vendor; collects basic information: company name, contact person, product categories offered, business registration | Buyer | Category Manager | 30 min |
| 2 | Buyer sends vendor application form to prospective vendor; vendor provides: DTI/SEC registration, BIR TIN, business permit, tax compliance certificate, bank certificate, product catalog with SRP | Buyer | Category Manager | External (vendor-dependent) |
| 3 | AP Clerk or Finance validates vendor documents: confirms TIN is valid, business permit is current, bank details verified | AP Clerk | AP Supervisor | 30 min |
| 4 | Buyer evaluates vendor capability: product quality (sample review), pricing competitiveness (vs. current vendors), delivery lead time, minimum order quantities, payment terms offered | Buyer | Category Manager | 2–4 hours |
| 5 | Category Manager approves vendor for onboarding (or rejects with reason) | Category Manager | VP Merchandising | 15 min |
| 6 | Buyer creates vendor master record in system: name, TIN, address, contact details, payment terms, bank account, currency, lead time, assigned category, entity(ies) | Buyer | Category Manager | 15 min |
| 7 | System assigns vendor number; configures: approval tier for PO amounts, default PO delivery location(s), matching tolerance for invoice price variance | System | — | Automated |
| 7a | **Vendor bank account change control**: if an existing vendor requests a change to their bank account details (new account number, new bank), the change requires a mandatory out-of-band verification before system update — (a) AP Clerk receives vendor bank change request (email, letter, or portal submission); (b) AP Clerk contacts vendor using the **known** phone number or contact person from vendor master (NOT the contact information in the change request itself, to prevent authorized push payment fraud); (c) AP Clerk verbally confirms the bank change with an authorized vendor representative; (d) AP Supervisor approves the bank detail change in system with verification notes (who confirmed, date, phone number used); (e) system requires dual approval (AP Clerk entry + AP Supervisor approval) for all bank detail changes; (f) system logs change with old bank details, new bank details, verifying AP Clerk ID, approving AP Supervisor ID, verification method, and timestamp; (g) system temporarily blocks payment to the vendor for 48 hours after bank detail change as a cooling-off period; (h) first payment to new bank account is flagged for Treasury Analyst confirmation of receipt before subsequent payments are auto-processed | AP Clerk / AP Supervisor | AP Supervisor | 30 min/change |
| 7b | **Vendor master data change log**: all changes to vendor master data (bank details, payment terms, address, contact information, tax classification) are logged with full audit trail — old value, new value, changed by, approved by, date, reason; changes to bank details and payment terms require AP Supervisor approval; changes to tax classification require Finance Manager approval; monthly: AP Supervisor reviews vendor master change log as part of AP controls review (cross-reference CTL-42 in Internal Controls Matrix) | System / AP Clerk | AP Supervisor | Automated + 30 min/month review |
| 8 | Merchandise Planner maps vendor's product catalog to item master: creates new SKUs or links to existing SKUs; sets vendor-specific cost, lead time, minimum order quantity, order multiple | Merchandise Planner | Buyer | 1–2 hours/vendor (varies by catalog size) |
| 9 | IT configures vendor portal access (if vendor uses portal): credentials, PO visibility, invoice submission capability | IT Team | Buyer | 15 min |
| 10 | Buyer places trial PO (small initial order) to validate vendor reliability, product quality at scale, and delivery performance | Buyer | Category Manager | Per W2 |
| 11 | After 3 trial orders: Buyer completes vendor scorecard baseline (delivery on-time %, quality reject rate, invoice accuracy) for future performance tracking (W44) | Buyer | Category Manager | 30 min |

**Total onboarding cycle**: 2–4 weeks from identification to first PO

### System Touchpoints
- Vendor master creation with document attachments (W36.6)
- TIN validation and business permit tracking with expiry alerts (W36.3, W36.6)
- Vendor-specific configuration: payment terms, tolerance thresholds, approval tiers (W36.7)
- Item-vendor mapping with cost, lead time, MOQ (W36.8)
- Vendor portal provisioning (W36.9)
- Vendor document tracking with expiry alerts: system tracks business permit, tax compliance certificate, and other regulatory document expiry dates; alerts Buyer and AP Clerk 30 days before expiry; vendor blocked from new POs if documents expired
- Vendor lead time master data lifecycle: initial lead time entered during vendor onboarding per vendor-SKU (W36 step 8); ongoing maintenance — Buyer updates lead times when vendor notifies of changes (new warehouse, route change, seasonal factors); system auto-suggests lead time updates based on actual delivery performance (comparing actual GR date vs. PO promised date) and presents suggestions to Buyer for review and confirmation; quarterly review per W31 step 8 confirms or adjusts stale lead times; system tracks all lead time changes with full audit trail (old value, new value, reason, date, Buyer ID); lead time variance metric feeds vendor scorecard (W44) (W36.6, W36.8)
- Integration with vendor performance scorecard (W36.11 → W44)

### Pain Points / Risks
- Philippine MSME vendors frequently lack complete BIR or DTI documentation, delaying onboarding; some submit expired business permits, requiring re-validation cycles that add 1–2 weeks per vendor
- Vendor bank account change control (step 7a) is critical for preventing authorized push payment (APP) fraud — a rising threat in Philippine retail; failure to enforce out-of-band verification could result in six-figure fraudulent payments
- Incomplete or inaccurate vendor master data (wrong TIN, incorrect payment terms) propagates errors into PO creation, invoice matching (W7), and BIR tax reporting (2307 withholding tax), creating costly downstream corrections

### Staffing Implication
- **Buyer**: 50–100 new vendors/year × ~4–6 hours of buyer time each = 200–600 hours/year = ~1–3 hours/week. Absorbed across 10–12 buyers.
- **AP Clerk**: 30 min per vendor for document validation = ~25–50 hours/year. Negligible.
- **Merchandise Planner**: Item-vendor mapping is the most labor-intensive step at 1–2 hours per vendor. With 50–100 vendors = ~100 hours/year. Absorbed within existing team.

### Time Estimate
- Buyer initial identification and application collection (steps 1–2): ~30 min + vendor-dependent document return time
- AP document validation (step 3): ~30 min/vendor
- Buyer vendor capability evaluation (step 4): ~2–4 hours/vendor
- Category Manager approval (step 5): ~15 min/vendor
- Vendor master creation and configuration (steps 6–7): ~30 min/vendor
- Merchandise Planner item-vendor mapping (step 8): ~1–2 hours/vendor
- IT portal setup (step 9): ~15 min/vendor
- Trial PO and scorecard baseline (steps 10–11): per W2 + ~30 min post-trial scoring
- Total internal effort per vendor: ~5–8 hours; total onboarding cycle: 2–4 weeks elapsed

---

## W38. Special Order / Non-Stock Item Fulfillment

| Field | Detail |
|---|---|
| **Trigger** | Customer requests an item not carried in regular store assortment |
| **Frequency** | ~500–1,000 special orders/month chain-wide; ~2–5 per store per month |
| **Volume** | Primarily professional trade customers (contractors, builders) and project-specific items; avg order value ~PHP 5,000–15,000 |
| **Owner** | Customer Service Rep (order intake); Buyer (fulfillment) |
| **Participants** | CSR, Sales Rep (trade accounts), Buyer, Receiving Clerk, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer requests non-stock item at store (CSR counter) or via Sales Rep; provides product description, specification, quantity needed, and desired delivery date | Customer | — | — |
| 2 | CSR or Sales Rep searches item in system: (a) checks if item exists in item master as non-stock/Special Order type, (b) if not found, creates a non-stock item request with description, specs, and estimated price | CSR / Sales Rep | Dept. Supervisor | 5–10 min |
| 3 | System routes non-stock item creation request to Merchandise Planner for item master setup (category assignment, unit of measure, tax classification) | System | Merchandise Planner | Automated routing |
| 3a | Merchandise Planner creates non-stock SKU in item master with type = "Special Order / Non-Stock"; flags as non-stocking (no ROP, no safety stock, no replenishment) | Merchandise Planner | Category Manager | 10 min |
| 4 | Buyer identifies vendor, obtains quotation (price, lead time, minimum quantity); enters quote in system linked to the non-stock SKU | Buyer | Category Manager | 30–60 min |
| 5 | CSR or Sales Rep communicates quote to customer: price, estimated delivery date, payment terms (typically 50% deposit, 50% on delivery) | CSR / Sales Rep | — | 10 min |
| 6 | Customer confirms order and pays deposit; system records deposit as liability (Cr. Customer Deposits Payable / Dr. Cash); not recognized as revenue until delivery | Customer / Cashier | — | 5 min |
| 6a | **Trade/corporate account customers**: if customer holds an active trade or corporate account (W24), deposit requirement is waived for orders within the customer's available credit limit; system checks credit limit at order creation — if credit available, Sales Associate or CSR selects "Charge to Account" and system posts order value to customer's AR account (W8) upon delivery (no deposit liability); if order exceeds available credit, system prompts for partial deposit covering the excess; for special orders > PHP 50,000 on account, system routes for AR Supervisor approval per W24 tiered matrix | Sales Associate / CSR | AR Supervisor | 2 min |
| 7 | System creates Sales Order linked to non-stock SKU with customer deposit recorded; reservation created against incoming PO | System | — | Automated |
| 8 | Buyer creates Special Order PO (links PO to Sales Order); routes for approval per standard tiered matrix (W2) | Buyer | Category Manager | Per W2 |
| 9 | Buyer tracks PO; follows up with vendor on delivery schedule | Buyer | Buyer | Per W2 |
| 10 | Goods received at store or DC (per W3 or W18); system matches GR to both PO and linked Sales Order | Receiving Clerk | Dept. Supervisor | Per W3/W18 |
| 11 | System alerts CSR that special order has arrived; CSR contacts customer for pickup or arranges delivery | System / CSR | Store Manager | Automated + 5 min |
| 12 | Customer picks up item (or receives delivery); pays remaining balance; system recognizes revenue (Dr. Customer Deposits / Cr. Revenue) and COGS (Dr. COGS / Cr. Inventory) at delivery; Sales Order closed | Cashier / CSR | — | 5 min |
| 13 | If customer cancels before PO is placed: CSR cancels Sales Order; deposit refunded; no PO created | CSR | Store Manager | 5 min |
| 14 | If customer cancels after PO is placed but before shipment: Buyer negotiates with vendor (restocking fee, return); Finance processes partial refund less any costs | Buyer + Finance | Category Manager | 30 min |
| 15 | Unclaimed deposit management: system tracks age of customer deposits linked to completed special orders (goods received but not picked up); after 30 days with no customer response post-delivery notification, system sends reminder notification (SMS/email); after 90 days with no response, system flags deposit for review; Store Manager or Finance approves recognition of abandoned deposit as other income (Dr. Customer Deposits Payable / Cr. Other Income); goods dispositioned per standard clearance (W13.9a), RTV (W3.6a), or return to shelf | System / Store Manager / Finance | Controller | Automated + 5 min/review |
| 16 | **Customer deposit refund (before goods receipt)**: if customer requests cancellation and refund before goods are received from vendor — (a) CSR processes deposit refund in system with reason code (customer cancellation, vendor cannot deliver, project cancelled); (b) system cancels linked Sales Order and triggers Buyer to cancel or reduce the linked PO per W2A PO cancellation process (if PO not yet shipped by vendor); (c) refund issued to original payment method: if deposit paid by cash, CSR disburses from cash drawer with Store Manager authorization; if paid by card/e-wallet, system processes electronic refund (Dr. Customer Deposits Payable / Cr. Cash); if paid by trade account credit, system applies deposit back to customer's AR account; (d) system logs refund with customer ID, original deposit transaction, refund amount, refund method, CSR ID, authorizing manager ID, and reason code; (e) BIR-compliant documentation: system generates official receipt for the refund transaction with all required BIR fields (TIN, registered invoice number, description "Refund of customer deposit — Sales Order #[number]"); refund receipts retained per 7-year BIR retention policy | CSR / Store Manager | Controller | 10 min/refund |

**Total cycle time**: 7–30 days from order to delivery (depends on vendor lead time and whether domestic or import)

### System Touchpoints
- Non-stock item type in item master with no auto-replenishment (W38.3a)
- Item creation request workflow (W38.3)
- Sales Order creation with customer deposit and PO linkage (W38.7–8)
- PO-to-Sales-Order reservation and matching (W38.8, W38.10)
- Customer deposit liability tracking (Cr. Customer Deposits Payable) with revenue recognition trigger at delivery (W38.6, W38.12)
- Customer notification upon receipt (W38.11)
- Sales Order lifecycle: open → PO linked → goods received → customer notified → closed (W38.7–12)
- Cancellation handling with deposit refund workflow (W38.13–14)
- Non-stock SKU archival and cleanup: over time, the item master accumulates non-stock/special-order SKUs (type = "Special Order / Non-Stock" per W38.3a) from one-time customer orders; to prevent item master bloat — (a) monthly: Merchandise Planner generates non-stock SKU aging report listing all non-stock SKUs with no sales activity in the past 12 months; (b) Merchandise Planner reviews each stale non-stock SKU and sets status to "Non-Stock — Archived" — item remains searchable in system for transaction history but is hidden from new Sales Order creation and Sales Associate lookup; (c) archived non-stock SKUs excluded from item count in reporting and system performance metrics; (d) if a customer subsequently requests the same item, Merchandise Planner reactivates the archived SKU (updates status to active) rather than creating a duplicate; system checks for archived SKUs matching the item description before allowing new non-stock SKU creation; (e) annually: Merchandise Planner reviews all archived non-stock SKUs older than 3 years with zero transaction history and proposes permanent deletion per BIR 7-year retention compliance (items with any transaction history retained for full 7 years regardless of archival status)
- Unclaimed deposit aging: system tracks deposit age from goods-receipt date; automated reminder at 30 days; escalation flag at 90 days; abandonment recognition with approval workflow; goods disposition tracking (W38.15)

### Pain Points / Risks
- Non-stock item master bloat: every special order creates a new SKU, and without disciplined archival (step in System Touchpoints), the item master grows by 500–1,000 SKUs/year, degrading system search performance and complicating reporting
- Customer deposits held for unclaimed special orders (step 15) represent a BIR compliance risk if not recognized as income within the prescribed period; premature recognition also risks customer disputes if goods are eventually claimed
- Special orders tie up Buyer time at ~30 hours/buyer/month — diverting attention from core replenishment buying and potentially causing missed ROP signals on stocking items

### Staffing Implication
- **CSR**: ~2–5 special orders/store/month × ~20 min each (intake + communication + handoff) = ~1–1.5 hours/store/month. Absorbed.
- **Buyer**: 500–1,000 special orders/month ÷ 10–12 buyers = ~50–80/buyer/month × ~30 min each = ~30 hours/buyer/month. This is significant. Special orders should be handled by a dedicated 1–2 Buyers who specialize in trade/special orders, with remaining buyers focused on replenishment.
- **Merchandise Planner**: 500–1,000 non-stock SKU creations/year = ~2–4 hours/week. Absorbed within existing team.

### Time Estimate
- CSR intake and customer communication (steps 1–2, 5–6): ~20 min/order
- Merchandise Planner item creation (step 3a): ~10 min/item
- Buyer sourcing and PO creation (steps 4, 8–9): ~30–60 min/order
- Receiving, customer notification, and pickup (steps 10–12): ~15 min/order (internal)
- Total internal effort per special order: ~1–1.5 hours across CSR, Buyer, and Planner
- Total cycle time: 7–30 days from order to delivery (vendor lead time dependent)
- Aggregate: ~500–1,000 orders/month × ~1.25 hours = ~625–1,250 hours/month across all participants

---

## W44. Vendor Performance Review

| Field | Detail |
|---|---|
| **Trigger** | Quarterly review calendar; or ad-hoc triggered by persistent quality/delivery issues |
| **Frequency** | Quarterly for top 50 vendors (by spend); annually for remaining active vendors |
| **Volume** | ~800–1,000 active vendors; top 50 = 45% of COGS |
| **Owner** | Buyer |
| **Participants** | Buyer, Category Manager, VP Merchandising, Receiving Supervisor (quality input), AP Supervisor (invoice accuracy input) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System auto-generates vendor scorecard per vendor for the review period with the following metrics: | System | — | Automated |
| | • **On-time delivery %**: PO lines delivered on or before promised date ÷ total PO lines | | | |
| | • **Fill rate %**: PO lines delivered at full ordered quantity ÷ total PO lines | | | |
| | • **Quality reject rate %**: GR lines rejected for quality ÷ total GR lines | | | |
| | • **Invoice accuracy %**: Invoices matching PO within tolerance on first submission ÷ total invoices | | | |
| | • **Lead time variance**: avg actual lead time vs. agreed lead time (days) | | | |
| | • **Return rate %**: RTV lines ÷ total receipt lines | | | |
| 2 | Buyer reviews scorecard; adds qualitative notes: vendor responsiveness, market reputation, new product pipeline, relationship quality | Buyer | Category Manager | 15–30 min/vendor |
| 3 | Buyer assigns overall rating: A (Preferred), B (Acceptable), C (Watch), D (Probation), F (Exit) | Buyer | Category Manager | 5 min/vendor |
| 4 | For C-rated vendors: Buyer drafts improvement plan with specific targets and timeline; communicates to vendor | Buyer | Category Manager | 30 min/vendor |
| 5 | For D/F-rated vendors: Buyer escalates to Category Manager for decision: (a) put on probation with 90-day improvement deadline, (b) initiate vendor exit process (transition to alternative vendor, settle outstanding obligations) | Buyer | VP Merchandising | 1 hour/vendor |
| 6 | Quarterly: Category Manager and VP Merchandising review top 50 vendor scorecards in portfolio review meeting; discuss strategic vendor relationships, negotiate improved terms for A-rated vendors | Category Manager | VP Merchandising | 2 hours/quarter |
| 7 | Annually: VP Merchandising and CFO review total vendor portfolio performance; approve vendor list for next year; authorize new vendor onboarding (W36) and vendor exits | VP Merchandising + CFO | CEO | 4 hours/year |
| 8 | System maintains vendor scorecard history for trend analysis; supports vendor selection decisions in W2 and W36 | System | — | Automated |
| 9 | **Corrective action execution — Warning**: Buyer communicates performance gaps to vendor in writing (email or letter) with specific metrics from scorecard; establishes 30-day improvement period with clear targets (e.g., on-time delivery must improve from 75% to 90%); Buyer monitors PO performance during improvement period via weekly scorecard snapshot | Buyer | Category Manager | 30 min/vendor |
| 10 | **Corrective action execution — Probation**: if no improvement after Warning, Buyer initiates probation — (a) Category Manager sends formal probation notice to vendor with 90-day review period and specific improvement requirements; (b) system changes vendor master status to "Probation"; (c) system blocks creation of new POs for this vendor (existing committed POs unaffected); (d) Buyer identifies alternative vendor for affected SKUs per W36; (e) Buyer monitors vendor performance weekly during probation; (f) at 90-day mark: Buyer recommends to Category Manager either reinstatement (if targets met) or termination | Buyer / Category Manager | VP Merchandising | 1 hour/vendor (initial) + 30 min/week monitoring |
| 11 | **Corrective action execution — Termination**: VP Merchandising approves termination; (a) Category Manager sends formal termination notice to vendor per contract terms (typically 30–60 day notice); (b) Buyer reviews all open POs — decides per PO: cancel, allow to complete, or expedite; (c) AP Supervisor reviews outstanding invoices and credit memos — resolves all financial obligations; (d) system changes vendor master status to "Inactive"; (e) system blocks all transactions (POs, GRs, invoices); (f) Merchandise Planner reassigns affected SKUs to alternative vendors per W36; (g) termination date, reason, and all supporting documentation recorded in vendor master audit trail | Category Manager / Buyer / AP Supervisor | VP Merchandising | 2–4 hours/vendor |
| 12 | **Corrective action execution — Reactivation**: if Buyer requests reactivation of a previously terminated vendor — (a) Buyer provides evidence of improved capability (new ownership, new processes, reference customers, corrected quality issues); (b) Category Manager reviews evidence and approves or denies; (c) if approved, vendor re-enters abbreviated onboarding per W36 (skip trial PO if recent performance history exists within 12 months); (d) system changes vendor master status back to "Active"; (e) full audit trail of termination and reactivation retained | Buyer / Category Manager | VP Merchandising | 1 hour/vendor |

| Tier | Trigger | Action | System Impact |
|---|---|---|---|
| **Warning** | Scorecard rating drops to C, or single significant incident (major quality failure, delivery causing stockout) | Buyer communicates performance gaps to vendor in writing with specific metrics; establishes 30-day improvement period with clear targets | Vendor master status remains Active; Buyer monitors PO performance during improvement period |
| **Probation** | No improvement after Warning, or scorecard rating drops to D | Vendor suspended from receiving new POs; existing committed POs are fulfilled; 90-day formal review period; Category Manager notifies vendor in writing of probation status and improvement requirements | Vendor master status changed to Probation; system blocks creation of new POs for this vendor; existing POs unaffected |
| **Termination** | No improvement after Probation, or scorecard rating F, or vendor commits fraud/breach | VP Merchandising approves termination; Category Manager notifies vendor; all open POs cancelled or allowed to complete per agreement; vendor master deactivated | Vendor master status changed to Inactive; system blocks all transactions; termination date and reason recorded in audit trail; vendor record retained for regulatory and historical purposes |
| **Reactivation** | Buyer requests reactivation with evidence of improved capability (new ownership, new processes, reference customers) | Category Manager reviews evidence; if approved, vendor re-enters onboarding process per W36 (abbreviated: skip trial PO if recent history exists) | Vendor master status changed back to Active; full audit trail of termination and reactivation retained |

### System Touchpoints
- Automated vendor scorecard generation from operational data (W44.1)
- Multi-metric scoring: on-time delivery, fill rate, quality, invoice accuracy, lead time, return rate (W44.1)
- Vendor rating system with configurable thresholds (W44.3)
- Improvement plan tracking (W44.4)
- Vendor lifecycle status: Active → Warning → Probation → Inactive (terminated) → Active (reactivated); each status change logged with reason, approver, date, and supporting documentation; system enforces PO blocking for Probation and Inactive vendors (W44.5, corrective action tiers)
- Scorecard history and trend analysis (W44.8)
- Integration with W2 (PO performance), W3 (receiving quality), W7 (invoice matching), W36 (vendor onboarding)

### Pain Points / Risks
- Vendor termination (step 11) disrupts supply for affected SKUs; if no alternative vendor is pre-identified, BuildRight faces stockouts during the transition period, especially for sole-source items like specialty electrical cable or proprietary paint formulations
- Scorecard metrics are only as reliable as the underlying data; inconsistent GR timestamp entry by DC Receiving Clerks can distort on-time delivery calculations, penalizing vendors unfairly or masking chronic lateness
- Probation status blocking new POs (step 10) may inadvertently block critical replenishment for fast-moving SKUs if the Buyer does not promptly identify alternative supply, turning a vendor performance issue into a store-level availability crisis

### Staffing Implication
- **Buyers**: Top 50 vendors reviewed quarterly × 30 min = 25 hours/quarter. Remaining ~750 vendors reviewed annually × 15 min = ~190 hours/year. Total ~290 hours/year ÷ 10 buyers = ~29 hours/buyer/year. Absorbed within existing buyer duties.
- **Category Managers**: 2 hours/quarter for portfolio review + 1 hour/quarter for escalations = ~12 hours/year. Absorbed.
- **VP Merchandising**: 2 hours/quarter for top vendor review + 4 hours/year for annual portfolio review = ~12 hours/year. Absorbed.

### Time Estimate
- Quarterly scorecard review (top 50 vendors): ~15–30 min/vendor × 50 vendors = ~12–25 hours/quarter across all buyers
- Annual review (remaining ~750 vendors): ~15 min/vendor = ~190 hours/year across all buyers
- Corrective action (Warning): ~30 min/vendor
- Corrective action (Probation): ~1 hour initial + ~30 min/week monitoring × 12 weeks = ~7 hours/vendor
- Corrective action (Termination): ~2–4 hours/vendor
- Quarterly portfolio review meeting: ~2 hours/quarter
- Annual portfolio review: ~4 hours/year
- Total ongoing: ~290 hours/year across all buyers (~29 hours/buyer/year) + ~16 hours/year Category Manager + ~16 hours/year VP Merchandising

---

## W60. Emergency Procurement

| Field | Detail |
|---|---|
| **Trigger** | Urgent operational need that cannot wait for standard PO cycle (W2) and exceeds petty cash threshold (W25): critical equipment breakdown, emergency facility repair, urgent compliance requirement, sudden supply shortage threatening store operations |
| **Frequency** | ~20–30 emergency procurement events/month across all locations |
| **Volume** | PHP 50,000–500,000 per event; typically for emergency equipment, parts, or services |
| **Owner** | Requestor (Store Manager or Department Head) |
| **Participants** | Store Manager / Dept. Head, Procurement (Buyer), Finance (Controller), Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requestor identifies emergency need and justifies urgency: equipment failure impacting store operations (e.g., POS server failure, HVAC breakdown in peak summer, forklift failure at DC), compliance deadline (regulatory order), or supply emergency (critical stockout on A-item with no PO coverage) | Store Manager / Dept. Head | — | 10 min |
| 2 | Requestor submits emergency procurement request in system: item/service description, estimated cost, urgency justification, required delivery date (typically same day or next day), preferred vendor (if known) | Requestor | — | 10 min |
| 3 | System routes for expedited approval: (a) ≤ PHP 100,000: Store Manager (for stores) or Dept. Head (for HQ/DC) + Controller verbal approval, (b) PHP 100,001–500,000: CFO verbal approval required within 2 hours, (c) > PHP 500,000: CEO verbal approval required within 4 hours; system logs verbal approval with timestamp and approver ID | System | Controller / CFO / CEO | 15 min – 4 hours |
| 4 | Buyer (or Requestor for store-level purchases) contacts vendor immediately — phone call or direct purchase authorized; system allows "confirm vendor later" mode where PO is created with vendor TBD and updated after the fact | Buyer / Requestor | Category Manager | 15–30 min |
| 5 | Goods or services received immediately; standard Goods Receipt (W3) or service confirmation documented | Receiving Clerk / Requestor | Dept. Head | Per W3 |
| 6 | Within 5 business days: Buyer or AP Clerk completes documentation — formalize PO in system (if created informally), obtain vendor invoice, process 3-way match (W7) or 2-way match for services; system enforces that all emergency procurements are regularized within 5 days or escalates to Controller | Buyer / AP Clerk | Controller | 15–30 min |
| 7 | Monthly: Controller reviews emergency procurement report: total spend, frequency by location, category, and requester; flags locations or categories with excessive emergency procurement frequency for root cause analysis (supplier reliability issues, planning gaps, or maintenance neglect) | Controller | CFO | 1 hour/month |

### System Touchpoints
- Emergency procurement request form with urgency justification field (W60.2)
- Expedited approval workflow with verbal approval logging and configurable SLA timers (W60.3)
- "Vendor TBD" PO creation mode for immediate procurement with post-hoc vendor assignment (W60.4)
- Regularization enforcement: system tracks emergency procurements not yet formalized; auto-escalates at day 5 (W60.6)
- Emergency procurement analytics: spend, frequency, category, location, root cause (W60.7)
- Integration with W2 (standard PO — this is the expedited alternative), W3 (goods receipt), W7 (AP matching), W21 (capex — if emergency need is actually capex, route to W21 expedited path), W25 (petty cash — for amounts ≤ PHP 50K), W47 (facility emergency repair), W48 (IT emergency equipment)

### Pain Points / Risks
- Emergency purchases bypass competitive bidding, creating risk of overpayment; a PHP 500K emergency equipment order may cost 15–25% more than the same item sourced through standard procurement channels
- Post-hoc documentation (step 6) is frequently delayed or incomplete; if Buyers or AP Clerks do not regularize within 5 days, the Controller loses visibility into outstanding commitments, and vendor invoices may arrive before the PO is in the system
- Frequent emergency procurement at a specific location signals systemic planning or maintenance failures; without root cause analysis (step 7), the pattern repeats, normalizing a costly workaround instead of fixing the underlying issue

### Staffing Implication
- No incremental headcount. Emergency procurement is absorbed by existing Buyers, Store Managers, and AP Clerks.
- The monthly review by Controller adds ~1 hour/month — absorbed.

### Time Estimate
- Request submission and expedited approval: ~15 min – 4 hours (depends on approval tier and verbal availability)
- Vendor contact and order placement: ~15–30 min/event
- Documentation regularization (within 5 business days): ~15–30 min/event
- Monthly Controller review: ~1 hour/month
- Total internal effort per event: ~1–2 hours active time; same-day or next-day resolution for the emergency need
- Aggregate: ~20–30 events/month × ~1.5 hours = ~30–45 hours/month across all participants

---

## W62. Vendor Contract Lifecycle (Non-PO Contracts)

| Field | Detail |
|---|---|
| **Trigger** | New service vendor engagement, contract renewal, or contract modification |
| **Frequency** | ~100–200 active service contracts at any time (IT services, cleaning, security, pest control, elevator maintenance, waste disposal, equipment leases, carrier contracts, banking services, professional services) |
| **Volume** | Peaks during annual budget cycle (W26) when contracts are reviewed and renewed |
| **Owner** | Requesting Department Head |
| **Participants** | Dept. Head, Procurement/Buyer, Finance, Legal, Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Department Head identifies need for vendor service contract (new vendor, renewal, or replacement); defines scope of work, service level requirements, and budget | Dept. Head | VP / C-Suite | 1–2 hours |
| 2 | Buyer or Dept. Head solicits quotations from 3 vendors (or 2 for specialized services); evaluates on: price, capability, references, compliance (business permits, tax compliance, insurance coverage) | Buyer / Dept. Head | Dept. Head | 2–4 hours |
| 3 | Legal reviews contract terms: liability, termination clause, data privacy (RA 10173 compliance for vendors handling personal data), intellectual property, dispute resolution | Legal | Legal Head | 1–2 hours/contract |
| 4 | Approval per tiered matrix: (a) annual value ≤ PHP 500K: Dept. Head + Finance Manager, (b) PHP 500K–2M: VP + CFO, (c) > PHP 2M: CEO | Approver | Approver | 15–30 min |
| 5 | System creates vendor contract record: vendor, contract type, scope, start/end dates, value, payment terms, SLA terms, auto-renewal flag, document attachments (signed contract, vendor permits, insurance certificates) | Buyer / Dept. Head | Dept. Head | 15–30 min |
| 6 | System alerts Dept. Head 90 days before contract expiry for renewal decision; alerts 30 days before vendor insurance or permit expiry within contract period | System | — | Automated |
| 7 | Monthly: Dept. Head reviews vendor service performance against SLA terms; documents issues; escalates to Buyer or Legal for resolution | Dept. Head | VP / C-Suite | 30 min/vendor/month |
| 8 | Contract renewal: Dept. Head decides to (a) renew at existing terms, (b) renegotiate (repeat steps 2–4), or (c) terminate and re-bid; system blocks vendor invoices after contract expiry if not renewed | Dept. Head | VP / C-Suite | Per contract |
| 9 | Contract termination: Dept. Head provides notice per contract terms; coordinates vendor exit (return of company property, data deletion per RA 10173, final payment); system closes contract record and blocks future invoices | Dept. Head / Legal | VP / C-Suite | 1–2 hours |

### System Touchpoints
- Vendor contract register with full lifecycle: Draft → Active → Renewal Pending → Renewed / Terminated (W62.5, 8–9)
- Contract document storage with expiry alerting for contract, vendor permits, and insurance certificates (W62.6)
- SLA tracking with performance documentation per review period (W62.7)
- Auto-renewal management: system flags auto-renewal contracts 90 days before renewal for Dept. Head decision (W62.6)
- Invoice blocking after contract expiry (W62.8)
- Integration with W2C (blanket/contract POs for merchandise vendors), W7C (non-PO invoice processing), W36 (vendor onboarding), W44 (vendor performance review — service vendors included in annual review), W59 (insurance tracking for vendor insurance certificates)

### Pain Points / Risks
- Service contracts with auto-renewal clauses can lock BuildRight into unfavorable terms for another year if the 90-day alert (step 6) is missed by the Department Head — especially common for low-visibility contracts (e.g., pest control, elevator maintenance)
- Vendor insurance certificate expiry during the contract period exposes BuildRight to uncovered liability; if a security guard vendor's insurance lapses and an incident occurs, BuildRight bears the full cost
- RA 10173 (Data Privacy Act) compliance for vendors handling personal data (IT services, delivery partners, loyalty program vendors) requires ongoing monitoring; a vendor data breach triggers BuildRight's mandatory breach notification obligation to the National Privacy Commission

### Staffing Implication
- No incremental headcount. Contract management is distributed across Department Heads as part of their operational responsibility. Legal reviews add ~1–2 hours/contract — absorbed within Legal team.

### Time Estimate
- Scope definition and vendor solicitation (steps 1–2): ~3–6 hours/contract
- Legal review: ~1–2 hours/contract
- Approval and system setup (steps 4–5): ~30–60 min/contract
- Monthly SLA performance review: ~30 min/vendor/month
- Contract renewal or termination: 1–2 hours/contract
- Total per contract lifecycle: ~6–10 hours active time; 1–3 weeks elapsed for new contracts
- Ongoing management: ~100–200 active contracts × ~30 min/month review = ~50–100 hours/month across all Dept. Heads

### W62B. 3PL / Delivery Partner Onboarding & Offboarding

| Field | Detail |
|---|---|
| **Trigger** | New delivery partner identified (new service area, capacity expansion, carrier diversification); or existing partner termination (performance failure, contract expiry, business exit) |
| **Frequency** | ~5–10 new partner evaluations/year; ~2–3 offboardings/year |
| **Volume** | Active partners: ~5–10 delivery partners (Lalamove, Transportify, own fleet surrogates, regional carriers, inter-island shipping lines) |
| **Owner** | Fleet Manager / DC Dispatch Supervisor |
| **Participants** | Fleet Manager, DC Dispatch, IT (API integration), Finance, Legal |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Fleet Manager or DC Dispatch identifies need for new delivery partner: coverage gap, capacity constraint, cost benchmarking, or service quality issue with existing partner | Fleet Manager | Supply Chain Manager | 30 min |
| 2 | Fleet Manager solicits proposals from 2–3 candidate partners; evaluates on: delivery coverage (zones, islands), rate card per zone/weight/tier, SLA terms (on-time %, damage rate), API integration capability (order creation, tracking, proof of delivery), insurance coverage, business permits, tax compliance | Fleet Manager | Supply Chain Manager | 4–8 hours |
| 3 | IT evaluates API integration feasibility: order creation, real-time tracking, proof of delivery capture, webhook/callback for status updates; estimates integration timeline and cost | IT Team | CIO | 4 hours |
| 4 | Legal reviews contract terms: liability for lost/damaged goods, data privacy (RA 10173 — delivery partner may access customer name, phone, address), insurance requirements, termination clause | Legal | Legal Head | 1–2 hours |
| 5 | Approval per W62 tiered matrix (carrier contracts typically annual value ≤ PHP 2M → VP + CFO; > PHP 2M → CEO) | Approver | Approver | 15–30 min |
| 6 | IT configures API integration in staging environment; conducts integration testing with carrier test environment; validates order creation, status callbacks, and proof of delivery flow; Fleet Manager and DC Dispatch conduct pilot with limited order volume for 1–2 weeks | IT Team / Fleet Manager | CIO | 1–2 weeks |
| 7 | Go-live: IT activates API integration in production; DC Dispatch adds partner to carrier selection logic; system routes orders to new partner per configured zones and rates | IT Team / Fleet Manager | Supply Chain Manager | 1 day |
| 8 | Monthly: Fleet Manager monitors new partner performance per W19.7 3PL management dashboard (on-time %, damage rate, cost per delivery, customer complaint rate); underperformance escalated per W44 vendor scorecard methodology | Fleet Manager | Supply Chain Manager | 30 min/month |
| 9 | **Offboarding**: if partner termination required (performance, contract expiry, or business decision) — Fleet Manager coordinates with DC Dispatch to redirect order volume to alternative partners; IT deactivates API integration; system removes partner from carrier selection; Finance settles outstanding carrier invoices; Legal confirms data deletion per RA 10173 (partner must delete customer data collected during service); system archives partner record with termination date, reason, and performance history | Fleet Manager / IT / Finance / Legal | Supply Chain Manager | 1–2 weeks |

### System Touchpoints (3PL Partners)
- Carrier master record with rate cards per zone/weight/tier, SLA terms, API credentials, insurance details, and integration status (W62B.2, W62B.7)
- API integration: order creation, real-time tracking, status callbacks, proof of delivery capture (W62B.3, W62B.6)
- Carrier selection logic: automated carrier assignment by delivery zone, package weight, and cost (W62B.7)
- Pilot order routing and monitoring dashboard (W62B.6)
- Performance monitoring integrated into W19 3PL management dashboard and W44 vendor scorecard (W62B.8)
- Partner deactivation: API disconnect, carrier removal, data deletion confirmation (W62B.9)
- Carrier rate card maintenance: Fleet Manager receives rate change notification from carrier (quarterly or annual update); enters updated rate card per zone/weight/tier in carrier master record; Finance Manager approves rate card changes before activation (validates against contracted rates and budget impact); system stores rate card history with effective dates for audit trail; auto-calculated delivery fees in W5D and W19 use the currently active rate card; rate card changes effective on configured date — orders already in transit use the rate card active at time of order creation (W62B)
- Integration with W19 (home delivery), W52 (fleet), W44 (vendor scorecard), W62 (non-PO contracts)

### Pain Points / Risks
- API integration failures with 3PL partners (Lalamove, Transportify) during peak order periods (e.g., 12.12 sale) can halt last-mile delivery; if the fallback carrier is not pre-configured, orders sit undelivered while IT troubleshoots
- Carrier rate card changes applied without Finance Manager approval can silently inflate delivery costs; a PHP 20/delivery increase across 200 stores compounds to significant margin erosion before it is detected
- Offboarding a 3PL partner requires confirmation of customer data deletion per RA 10173; if the partner fails to comply after contract termination, BuildRight remains liable under the Data Privacy Act as the data controller

### Staffing Implication (3PL Partners)
- **Fleet Manager**: absorbs 3PL partner management within existing role; ~5–10 evaluations/year × 4–8 hours = ~20–80 hours/year; ~30 min/month ongoing monitoring per partner.
- **IT**: API integration setup ~1–2 weeks per new partner; absorbed within existing IT team.
- No incremental headcount.

### Time Estimate
- New partner evaluation and proposal solicitation: ~4–8 hours/partner
- IT API integration feasibility assessment: ~4 hours/partner
- Legal review: ~1–2 hours/partner
- API integration setup, testing, and pilot: 1–2 weeks elapsed
- Monthly performance monitoring: ~30 min/partner/month
- Offboarding: 1–2 weeks elapsed; ~4–8 hours active coordination
- Total per partner onboarding: ~20–30 hours active time over 3–4 weeks elapsed
- Ongoing management: ~5 hours/month for 5–10 active partners

---

## W88. Return to Vendor (RTV) Processing

| Field | Detail |
|---|---|
| **Trigger** | Defective goods identified at DC or store; wrong items received; overage discovered; vendor-authorized return; or quality hold escalation (W3 AQL inspection) |
| **Frequency** | ~200–300 RTV shipments/month (~2–3% of inbound volume) |
| **Volume** | Avg 5–15 lines per RTV shipment; consolidated by vendor at DC |
| **Owner** | Buyer |
| **Participants** | Buyer, DC Receiving Clerk, Store Receiving Clerk, AP Clerk, AP Supervisor, Category Manager |

### Background

PUR-012 (Return to Vendor) is a Must Have requirement. RTV is currently mentioned as sub-steps W3.6a–b within warehouse receiving, but RTV is a cross-functional process spanning procurement, warehouse, store operations, and finance. Defective, wrong, or overage items must be identified, documented, authorized, physically returned to the vendor (or vendor-authorized disposal), and financially settled (credit memo or replacement). Without a dedicated workflow, RTV decisions are ad-hoc, leading to delayed vendor credits, unresolved inventory, and write-offs.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Identification**: (a) DC Receiving Clerk identifies defective/wrong items during goods receipt inspection (W3 AQL); (b) Store Receiving Clerk identifies issues during DSD receiving (W18) or DC delivery receipt; (c) Store Associate or Stock Associate discovers damaged/defective stock on shelf or in backroom; (d) AP Clerk identifies overage during 3-way match (W7 — vendor invoice quantity exceeds PO + GR); (e) Quality hold escalation from W3 AQL inspection (system blocks inventory and flags for RTV evaluation) | Receiving Clerk / Store Associate / AP Clerk | Buyer | 10 min/case |
| 2 | **Root cause classification**: Initiator classifies the issue: (a) defective/quality failure (vendor manufacturing defect, packaging damage in transit from vendor), (b) wrong item shipped (SKU mismatch vs. PO), (c) overage (vendor shipped more than PO quantity), (d) damaged in transit to DC (carrier damage — see W19.12b for carrier vs. vendor liability), (e) recall-related return (W29), (f) consignment return (W23.10), (g) warranty return (W33.6) | Initiator / Buyer | Buyer | 5 min/case |
| 3 | **Quarantine**: System moves identified items to "RTV Quarantine" inventory status (not available for sale, not available for allocation); physical items moved to designated quarantine area at DC or store backroom | Receiving Clerk / Stock Associate | DC Supervisor / Store Manager | 10 min/case |
| 4 | **Buyer review and authorization**: Buyer reviews RTV request with supporting evidence (photos, inspection report, PO vs. GR discrepancy); determines return action: (a) **Return to vendor** — vendor must physically take back goods and issue credit or replacement, (b) **Vendor-authorized disposal** — vendor authorizes BuildRight to dispose/destroy goods and issues credit memo (saves return freight cost for low-value items), (c) **Vendor-authorized markdown** — vendor agrees to partial credit; BuildRight sells at reduced price per W93 markdown process, (d) **No vendor liability** — damage caused by BuildRight handling (in-transit between DC and store, or in-store damage); disposition per W91 damaged goods process; no vendor credit sought | Buyer | Category Manager | 15 min/case |
| 5 | **Vendor notification**: Buyer contacts vendor (email or vendor portal W36.9) with RTV request: original PO reference, GR reference, item details, quantity, defect description, photos, and requested resolution (credit memo, replacement, or disposal authorization); for blanket/contract PO vendors (W2C), checks contract terms for RTV provisions and return shipping responsibility | Buyer | — | 15 min/case |
| 6 | **Vendor credit memo or replacement**: (a) If vendor agrees to credit: Buyer obtains vendor credit memo reference; (b) If vendor agrees to replacement: Buyer creates replacement PO with reference to original PO and RTV; (c) If vendor disputes: Buyer escalates to Category Manager for negotiation; unresolved disputes > 30 days escalated to VP Merchandising | Buyer / Category Manager | VP Merchandising | 30 min/dispute |
| 7 | **Physical return logistics** (if vendor requires physical return): (a) **DC-initiated**: DC consolidates RTV items by vendor; DC creates outbound shipment; ships via own fleet (W52) or 3PL carrier; (b) **Store-initiated**: Store sends RTV items to assigned DC via next scheduled DC→Store truck backhaul (W22); DC consolidates with other RTV items for same vendor before shipping; (c) **Vendor pickup**: Some vendors (especially local DSD vendors) pick up RTV items directly from store or DC by arrangement | DC Receiving Clerk / Store Receiving Clerk | DC Supervisor / Store Manager | 30 min/consolidated shipment |
| 8 | **Financial settlement**: (a) AP Clerk receives vendor credit memo (from Buyer); posts credit memo against original PO/invoice; system reduces vendor payable and posts GL entry (Dr. AP / Cr. COGS or Inventory); (b) If replacement PO: AP matches replacement invoice against replacement PO and GR per standard W7 3-way match; (c) If vendor-authorized disposal: AP posts credit memo and inventory write-off simultaneously; system removes items from RTV quarantine and posts disposal (Dr. AP / Cr. Inventory — at WAC value) | AP Clerk | AP Supervisor | 10 min/credit memo |
| 9 | **Aging and escalation**: System tracks RTV items in quarantine with aging buckets (0–15, 16–30, 31–60, 60+ days); weekly: Buyer reviews RTV aging report; items > 15 days without vendor response: follow-up call/email; items > 30 days: escalated to Category Manager; items > 60 days: escalated to VP Merchandising with recommendation to auto-dispose and write-off; items > 90 days: auto-write-off per W92 with Category Manager approval | Buyer / Category Manager | VP Merchandising | 30 min/week |
| 10 | **RTV analytics**: Monthly: Category Manager and Buyer review RTV report by vendor — RTV count, RTV value, average resolution time, root cause distribution (defective vs. wrong item vs. overage vs. carrier damage); feeds into W44 vendor performance scorecard as quality and accuracy metric; vendors with RTV rate > 5% of total PO lines flagged for vendor improvement plan or vendor exit per W68 | Category Manager / Buyer | VP Merchandising | 1 hour/month |

### System Touchpoints
- RTV quarantine inventory status: items blocked from sale and allocation while in quarantine (W88.3)
- RTV request creation linked to original PO and GR with defect evidence (photos, inspection report) (W88.4)
- Vendor portal RTV notification: vendor receives return request with documentation and can approve/reject/authorize disposal (W88.5)
- Vendor credit memo matching to original PO/invoice with GL posting (W88.8)
- Replacement PO creation linked to original PO with RTV reference (W88.6)
- RTV aging report with vendor-level drill-down and escalation triggers (W88.9)
- RTV analytics dashboard: RTV rate by vendor, root cause distribution, resolution time, value impact (W88.10)
- Integration with W3 (DC receiving — AQL inspection triggers RTV), W7 (AP — credit memo processing), W12 (returns — customer-returned defective items may be RTV'd), W18 (DSD — receiving discrepancies), W22 (store-to-DC backhaul for RTV consolidation), W23 (consignment returns), W29 (recall-related RTV), W33 (warranty RTV), W44 (vendor scorecard — RTV rate as quality metric), W52 (fleet — physical return logistics), W62 (vendor contract — RTV provisions), W91 (damaged goods disposition — no-vendor-liability cases), W92 (inventory adjustment — write-off for unresolved RTV)

### Pain Points / Risks
- RTV items sitting in quarantine (step 3) consume valuable DC staging space; during peak receiving periods (holiday stocking), quarantined pallets can overflow designated areas, disrupting inbound logistics
- Vendor disputes over RTV liability (step 6) can drag beyond 30 days, especially with import vendors who may contest quality claims across borders; during the dispute, inventory remains in quarantine, unavailable for sale or alternative disposition
- Unresolved RTV items aging beyond 90 days (step 9) are auto-written off, representing a direct margin hit; high RTV write-off rates indicate systemic vendor quality problems that should have been addressed earlier through CAPA (W110) or vendor exit (W44)

### Staffing Implication
- **Buyers**: ~200–300 RTV cases/month ÷ 10–12 buyers = ~20–25 cases/buyer/month × ~45 min each = ~15–19 hours/buyer/month. Absorbed within existing buying workload.
- **DC Receiving Clerks**: RTV consolidation adds ~1–2 hours/week for staging and shipping returns. Absorbed.
- **AP Clerks**: ~200–300 credit memos/month adds ~1–2 hours/week. Absorbed within existing AP team.
- **No incremental headcount.**

### Time Estimate
- Identification, classification, and quarantine: ~25 min/case
- Buyer review, authorization, and vendor notification: ~30 min/case
- Vendor credit memo negotiation or dispute resolution: ~30 min/case (undisputed) to ~2 hours (disputed); 1–4 weeks vendor response elapsed time
- Physical return logistics: ~30 min/consolidated shipment
- Financial settlement (credit memo posting): ~10 min/credit memo
- Weekly RTV aging review: ~30 min/week
- Monthly RTV analytics review: ~1 hour/month
- Total per RTV case: ~45 min–2 hours active time; 1–6 weeks elapsed time depending on vendor response

---

## W110. Supplier Quality & CAPA (Corrective and Preventive Action)

| Field | Detail |
|---|---|
| **Trigger** | Quality failure at DC receiving (W3 AQL inspection failure); customer complaint about product quality (W41); product recall (W29); warranty claim spike (W33); or periodic quality trend review |
| **Frequency** | ~20–30 CAPA cases/month (from AQL rejects, customer complaints, and warranty analysis); quarterly quality trend review |
| **Volume** | ~200–300 quality failures/month from DC AQL inspection (W3); ~600–900 customer quality complaints/month (30% of W41 complaint volume); ~50–100 warranty claims/month potentially quality-related (W33) |
| **Owner** | Buyer (vendor communication); Category Manager (escalation); Quality Coordinator (if dedicated role) |
| **Participants** | Buyer, Category Manager, DC Receiving Supervisor, Quality Checker, VP Merchandising, Customer Service Manager |

### Background

W3 covers quality inspection at DC receiving with AQL sampling. W44 covers vendor scorecards with quality reject rate as a metric. W88 handles RTV processing for defective items. However, there is no systematic workflow for investigating the root cause of quality failures, implementing corrective and preventive actions (CAPA) with the vendor, tracking CAPA effectiveness, and feeding quality trends back into vendor management and assortment decisions. Without CAPA, quality failures recur, vendor scorecards penalize but don't improve performance, and the same defective products reach customers repeatedly.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **CAPA case creation**: System auto-generates CAPA case when: (a) AQL inspection fails at DC receiving (W3 — entire lot rejected or defect rate exceeds AQL), (b) customer quality complaint categorized as product defect (W41), (c) product recall initiated (W29 — systemic quality failure), (d) warranty claim rate for a SKU exceeds threshold (> 2% of units sold), (e) RTV rate for a vendor exceeds threshold (> 5% of PO lines per W88.10); alternatively, Buyer or Category Manager manually creates CAPA case for observed quality trends | System / Buyer / Category Manager | Category Manager | 5 min/case |
| 2 | **Case classification and severity**: Buyer classifies CAPA case: (a) **Critical** — safety hazard (electrical defect, structural failure, chemical hazard), regulatory non-compliance, or widespread customer impact; requires immediate response; (b) **Major** — functional defect affecting usability, high return/complaint rate (> 5%), or significant financial impact (> PHP 100,000); requires vendor corrective action; (c) **Minor** — cosmetic defect, packaging quality, labeling errors; monitored for trend but may not require formal vendor CAPA | Buyer | Category Manager | 10 min/case |
| 3 | **Immediate containment**: (a) For Critical/Major: system places quality hold on all on-hand inventory of affected SKU across all locations (blocked from sale and allocation pending investigation); (b) system blocks pending POs for the SKU from being confirmed (Buyer reviews); (c) if product already sold: Buyer coordinates with W29 recall process for consumer notification (Critical only); (d) DC Supervisor quarantines affected inventory in QC hold area per W3 quality hold process | Buyer / DC Supervisor | Category Manager | 1 hour/case (Critical); 30 min (Major) |
| 4 | **Root cause investigation**: (a) Buyer collects evidence: AQL inspection report, defect photos, customer complaint details, warranty claim photos, lot/batch numbers, manufacturing dates; (b) Buyer contacts vendor with detailed quality failure report: defect description, affected lot/batch, quantity impacted, severity, and request for root cause analysis; (c) vendor conducts root cause investigation (typically 5–15 business days); (d) for Critical cases: Buyer may request on-site vendor factory visit or independent third-party inspection | Buyer | Category Manager | 2–4 hours/case |
| 5 | **Corrective action plan**: Based on root cause findings, Buyer and vendor agree on corrective action: (a) **Process change** — vendor modifies manufacturing process, adds quality checkpoint, changes raw material supplier; (b) **Design change** — product specification modified to eliminate defect mode; (c) **Packaging change** — improved packaging to prevent transit damage; (d) **Batch replacement** — vendor replaces entire affected batch at vendor cost; (e) **Training** — vendor trains production staff on identified gap; Buyer documents agreed corrective actions with specific deliverables, responsible party, and completion deadline in CAPA case | Buyer / Vendor | Category Manager | 1–2 hours/case |
| 6 | **Preventive action**: Buyer identifies systemic preventive measures to avoid recurrence across similar products or vendors: (a) update AQL inspection checklist for the category to catch similar defects (W3); (b) revise vendor onboarding quality requirements for new vendors in the category (W36); (c) update item specification or acceptance criteria in item master (MDM-002); (d) communicate learnings to other Buyers handling similar categories | Buyer | Category Manager | 30 min/case |
| 7 | **Verification and closure**: (a) After corrective action deadline: Buyer verifies vendor implementation — request evidence (photos, updated process documents, test results); (b) for process/design changes: next 3 shipments inspected at tightened AQL level (Level III per ANSI Z1.4) to verify improvement; (c) if quality improvement confirmed: Buyer closes CAPA case with effectiveness verification notes; (d) if quality not improved: Buyer escalates to Category Manager for vendor improvement plan per W44 Warning/Probation/Termination tiers | Buyer | Category Manager | 30 min/case |
| 8 | **Monthly CAPA dashboard**: Buyer generates monthly CAPA dashboard: (a) open CAPA cases by vendor, category, and severity; (b) average time to resolution by severity; (c) corrective action effectiveness rate (cases closed without recurrence ÷ total closed); (d) recurring quality issues (same defect mode from same vendor); (e) vendors with most open/past-due CAPA cases; dashboard shared with Category Managers and VP Merchandising | Buyer | VP Merchandising | 1 hour/month |
| 9 | **Quarterly quality trend review**: Category Manager and VP Merchandising review quality trends quarterly: (a) quality reject rate trend by vendor and category, (b) customer complaint rate related to product quality, (c) CAPA case volume trend, (d) vendors with chronic quality issues (3+ CAPA cases in 12 months), (e) quality-driven assortment decisions — should BuildRight exit vendors with persistent quality failures?; feeds into W44 vendor scorecard and W1 assortment review | Category Manager | VP Merchandising | 2 hours/quarter |

### System Touchpoints
- CAPA case auto-generation from AQL failures, customer complaints, warranty claims, and RTV rate thresholds (W110.1)
- Case classification with severity levels triggering appropriate containment actions (W110.2–3)
- Quality hold on affected inventory across all locations with sales blocking (W110.3)
- Root cause documentation with evidence attachment (photos, inspection reports, vendor communications) (W110.4)
- Corrective action plan with deliverables, responsible party, and deadline tracking (W110.5)
- Verification workflow with tightened inspection for post-CAPA shipments (W110.7)
- Monthly CAPA dashboard with case aging, effectiveness rate, and vendor ranking (W110.8)
- Integration with W1 (assortment — quality-driven vendor exit), W3 (AQL inspection — source of CAPA triggers and tightened inspection post-CAPA), W29 (product recall — Critical CAPA escalation), W33 (warranty — quality-related claims), W36 (vendor onboarding — quality requirements from CAPA learnings), W41 (customer complaints — product quality complaints feed CAPA), W44 (vendor scorecard — CAPA history as quality metric), W88 (RTV — CAPA from high RTV rate), W91 (damaged goods — disposition during containment)

### Pain Points / Risks
- Quality hold on affected inventory (step 3) blocks sales across all 200 stores; for a fast-moving SKU (e.g., best-selling cement brand), even a 5-day hold during CAPA investigation can trigger widespread stockouts and lost revenue
- Vendor root cause investigation timelines (5–15 business days) are not enforced by the system; some vendors stall or provide superficial root cause analyses, leading to repeated CAPA cases for the same defect without real improvement
- Tightened AQL inspection (Level III) for post-CAPA shipments increases DC receiving time per container by 30–50%, creating downstream receiving bottlenecks during peak import seasons when multiple containers arrive simultaneously

### Staffing Implication
- **Buyers**: ~20–30 CAPA cases/month ÷ 10–12 buyers = ~2–3 cases/buyer/month × ~3 hours each = ~6–9 hours/buyer/month. This is a core part of vendor management. Absorbed.
- **Category Managers**: 2 hours/quarter for trend review + 30 min/escalation case. Absorbed.
- **No incremental headcount.**

### Time Estimate
- CAPA case creation and classification: ~15 min/case
- Immediate containment (quality hold, PO blocking): ~1 hour/case (Critical); ~30 min (Major)
- Root cause investigation and vendor communication: ~2–4 hours/case active time; 5–15 business days vendor elapsed time
- Corrective and preventive action planning: ~1.5–2.5 hours/case
- Verification and closure: ~30 min/case; 3 shipment inspection cycles for verification
- Monthly CAPA dashboard: ~1 hour/month
- Quarterly quality trend review: ~2 hours/quarter
- Total per CAPA case: ~5–8 hours active Buyer/Category Manager time over 3–6 weeks elapsed

---

## W115. Supplier Diversity & MSME Development Program

| Field | Detail |
|---|---|
| **Trigger** | Annual supplier diversity review; or ad-hoc triggered by corporate social responsibility (CSR) initiative, LGU requirement, or MSME vendor opportunity identification |
| **Frequency** | Annual program review and target setting; quarterly progress tracking; continuous MSME vendor identification |
| **Volume** | ~800–1,000 active vendors; target: ≥ 20% MSME (Micro, Small, Medium Enterprise) vendor participation by spend or count within 3 years |
| **Owner** | Buyer (MSME identification and onboarding); VP Merchandising (program governance) |
| **Participants** | Buyer, Category Manager, VP Merchandising, Finance, Legal, CSR Coordinator |

### Background

The Philippine government actively promotes MSME development through the Magna Carta for MSMEs (RA 9501) and the Go Negosyo Act (RA 10644). Large enterprises are encouraged to source from MSMEs, and government procurement (W78) has MSME participation requirements. BuildRight sources 60% of goods from local Philippine vendors — many of which may qualify as MSMEs. However, there is no formal program to track MSME vendor participation, identify opportunities to onboard MSME suppliers, or provide development support to help MSMEs meet BuildRight's quality and scale requirements. This workflow creates that governance framework, supporting PUR-003 (vendor management) and contributing to corporate social responsibility objectives.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **MSME vendor classification**: System classifies existing vendors as MSME or non-MSME based on DTI/SEC registration and annual revenue: (a) Micro: < PHP 3M annual revenue, (b) Small: PHP 3M–15M, (c) Medium: PHP 15M–100M, (d) Large: > PHP 100M; classification captured in vendor master during onboarding (W36) or updated annually from BIR tax filing data; system generates MSME vendor register with: vendor name, category, MSME size classification, annual spend, and year-first-onboarded | System / Buyer | VP Merchandising | Automated (classification) + 2 hours/year (verification) |
| 2 | **Annual diversity target setting**: VP Merchandising and Category Managers set annual MSME sourcing targets by category: (a) overall target: ≥ 20% of active vendor count classified as MSME within 3 years, (b) category-specific targets based on MSME availability in the category (e.g., higher MSME % in home décor, garden, hardware where local artisans and manufacturers are prevalent; lower in power tools, appliances where scale requirements favor large manufacturers), (c) geographic diversity target: ensure MSME vendors are distributed across regions (Mindanao, Visayas, Luzon) not concentrated in one region | VP Merchandising | CEO | Annual (4 hours) |
| 3 | **MSME vendor identification**: Buyer actively identifies potential MSME vendors through: (a) trade shows and MSME fairs (DTI-organized events, regional trade fairs), (b) LGU and DTI referrals (DTI has MSME directories per region), (c) industry associations (Chamber of Commerce, sector-specific associations), (d) existing vendor referrals (current vendors may know MSME sub-suppliers), (e) competitor and market scanning for local manufacturers not yet in BuildRight's vendor base | Buyer | Category Manager | Ongoing (~2 hours/week across all buyers) |
| 4 | **MSME vendor evaluation**: Buyer evaluates MSME vendor candidates with modified criteria vs. large vendor onboarding (W36): (a) product quality — sample review (standard W36.4), (b) pricing competitiveness — may be slightly higher than large vendors but justified by uniqueness or local sourcing value, (c) production capacity — must meet minimum order quantity for BuildRight's needs (may be lower than standard MOQ to accommodate MSME scale), (d) delivery capability — must deliver to assigned DC or store within agreed lead time, (e) financial stability — review BIR registration and business permit (standard W36.2–3), (f) scalability potential — can the MSME grow with BuildRight's increasing demand? | Buyer | Category Manager | Per W36 (~4–6 hours/vendor) |
| 5 | **MSME onboarding support**: For MSME vendors that meet quality and capacity requirements but need operational support: (a) Buyer provides guidance on BuildRight's packaging, labeling, and barcode requirements; (b) Category Manager may approve a trial period with smaller initial orders and more frequent quality checks (W3 tightened AQL); (c) Finance may offer shorter payment terms (Net 15 instead of Net 30) to support MSME cash flow — requires Finance Manager approval; (d) IT provides vendor portal access and training for order management (W36.9) | Buyer / Category Manager / Finance | VP Merchandising | 2–4 hours/vendor |
| 6 | **Quarterly progress tracking**: Buyer generates quarterly MSME sourcing report: (a) total MSME vendor count and % of active vendors, (b) total MSME spend and % of total COGS, (c) new MSME vendors onboarded during quarter, (d) MSME vendor geographic distribution, (e) MSME vendor performance summary (quality, delivery, pricing vs. non-MSME benchmarks), (f) progress against annual targets | Buyer | VP Merchandising | 1 hour/quarter |
| 7 | **Annual program review**: VP Merchandising and CEO review annual MSME program performance: (a) year-over-year MSME vendor count and spend trend, (b) MSME vendor retention rate (how many MSME vendors remain active after first year?), (c) MSME vendor success stories and challenges, (d) set next year's targets, (e) evaluate program's contribution to BuildRight's CSR objectives and community impact (especially in Mindanao and Visayas regions) | VP Merchandising | CEO | 2 hours/year |
| 8 | **Government reporting**: If required for government procurement eligibility (W78) or LGU permit compliance (W54): Finance compiles MSME sourcing data for regulatory submissions; CSR Coordinator prepares MSME development program summary for annual CSR report | Finance / CSR Coordinator | VP Legal & Compliance | Annual (4 hours) |

### System Touchpoints
- MSME classification field in vendor master with size category (Micro, Small, Medium, Large) and annual revenue band (W115.1)
- MSME vendor register with spend, category, region, and year-onboarded (W115.1)
- Annual MSME sourcing target configuration by category and region (W115.2)
- Quarterly MSME sourcing report with count, spend, geographic, and performance metrics (W115.6)
- Integration with W36 (vendor onboarding — MSME classification at onboarding), W44 (vendor scorecard — MSME vs. non-MSME performance comparison), W62 (vendor contracts — MSME-specific payment terms), W78 (government procurement — MSME participation reporting), W26 (annual budget — MSME spend target)

### Pain Points / Risks
- MSME vendors may lack the production capacity to scale with BuildRight's 200-store demand; a successful trial with a local furniture maker can collapse when asked to supply 200 stores instead of 10, requiring costly vendor transition mid-season
- Shortened payment terms (Net 15) offered to support MSME cash flow increase BuildRight's working capital requirements; if MSME participation scales to 20% of vendor count, the aggregate payment acceleration can be material
- Government MSME sourcing targets (RA 9501) are aspirational rather than mandated for private enterprises, but public reporting of MSME spend can create reputational risk if targets are missed or if MSME vendors are classified incorrectly due to outdated revenue data

### Staffing Implication
- **Buyers**: MSME identification adds ~2 hours/week total across all buyers.
- **No incremental headcount.**

### Time Estimate
- Annual MSME classification verification: ~2 hours/year (mostly automated)
- Annual diversity target setting: ~4 hours/year (executive session)
- MSME vendor identification: ~2 hours/week ongoing across all buyers (~100 hours/year)
- Individual MSME vendor evaluation and onboarding: ~4–6 hours/vendor per W36
- Quarterly progress reporting: ~1 hour/quarter
- Annual program review and government reporting: ~6 hours/year
- Total program effort: ~150–200 hours/year across the team (excludes per-vendor onboarding time)

---

## W136. Indirect / Non-Merchandise Procurement

| Field | Detail |
|---|---|
| **Trigger** | Requisition for supplies, services, or equipment not for resale |
| **Frequency** | Ongoing |
| **Volume** | ~300–400 indirect POs/month (supplies, fixtures, marketing materials) |
| **Owner** | Indirect Procurement Manager |
| **Participants** | Requesting Dept, Buyer, Vendor, Finance (AP) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requisition: Dept user creates purchase request (PR) in ERP | Requestor | Dept Head | 15 min |
| 2 | Sourcing / Bidding: Buyer obtains 3 quotes for non-contract items | Buyer | Procurement Mgr | 3–5 days |
| 3 | Vendor Selection: Evaluate quotes based on TCO (Total Cost of Ownership) | Buyer | Procurement Mgr | 1 day |
| 4 | PO Creation: Convert approved PR to PO and transmit to vendor | Buyer | Procurement Mgr | 15 min |
| 5 | Receipt & Verification: Requestor confirms receipt of goods or service completion | Requestor | Dept Head | 30 min |
| 6 | Invoice Processing: Finance matches Invoice to PO and Receipt (3-way match) | AP Specialist | AP Supervisor | 15 min |

### System Touchpoints
- Requisition portal with department-level budget commitment check and approval routing
- "3-quote" enforcement rule for indirect spend above configurable threshold
- Service Entry Sheet (SES) module for non-physical services (consulting, janitorial, security)
- PO creation from approved requisition with vendor transmission (email/portal)
- 3-way match (PO → Receipt/SES → Invoice) for indirect AP processing
- Integration with Fixed Asset module (W21/W39) for equipment procurement that triggers capitalization
- Integration with W60 (Emergency Procurement) for indirect urgent requests that bypass standard requisition

### Pain Points / Risks
- Indirect procurement spans 200 stores and multiple departments; without strong "3-quote" enforcement, maverick spending (buying off-contract from preferred vendors) can inflate indirect costs by 10–15% above negotiated rates
- Service Entry Sheets for non-physical services (cleaning, consulting) depend on the requesting Department Head's attestation of service completion; weak verification can result in payment for incomplete or substandard services
- Indirect purchase requisitions compete for the same Buyer bandwidth as merchandise POs; during peak seasonal procurement (Q4), indirect requests are deprioritized, delaying store fixture replacements, marketing material production, and facility maintenance

### Time Estimate
- Requisition creation and approval: ~15 min per PR
- Sourcing and bidding (3 quotes for non-contract items): 3–5 days elapsed; ~4–6 hours active sourcing per PR
- PO creation and vendor transmission: ~15 min per PO
- Receipt verification and invoice matching: ~45 min per PO
- Total cycle: 5–7 business days from PR to PO for non-contract items; ~1 day for contract/consumable items
- Total internal effort: ~5–8 hours per indirect procurement event

### Staffing Implication
- **Indirect Procurement Manager**: ~300–400 indirect POs/month × ~30 min oversight each = ~150–200 hours/month. This is a dedicated role.
- **Buyers**: Sourcing and bidding adds ~4–6 hours per non-contract PR. At ~300–400 POs/month ÷ 2–3 indirect buyers = ~100–130 POs/buyer/month. Absorbed within dedicated indirect procurement team.
- **Requesting departments**: ~15 min per PR × ~300–400 PRs/month = ~75–100 hours/month total across all departments. Distributed impact.

---

## W150. Product Quality Testing & Certification

| Field | Detail |
|---|---|
| **Trigger** | New product onboarding (W1); new vendor onboarding (W36); or scheduled periodic audit |
| **Frequency** | Ad-hoc (new items); Annual (periodic) |
| **Volume** | ~500–1,000 items tested/year (primarily private label and structural materials) |
| **Owner** | Quality Manager |
| **Participants** | Category Manager, Vendor, external testing lab (e.g., TUV, SGS), DC Receiving |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Sample Submission**: Vendor provides physical samples of the product for testing | Vendor | Category Mgr | 1 day |
| 2 | **Documentation Review**: Quality Manager verifies mandatory Philippine certifications (PS Mark for local, ICC for imported regulated items) | Quality Mgr | Quality Mgr | 1 hour |
| 3 | **Internal Testing**: Basic "Fit & Finish" testing at HQ or DC lab (e.g., measuring tile thickness, weighing cement bags) | Quality Mgr | Category Mgr | 2 hours |
| 4 | **External Lab Testing**: Send samples to accredited 3rd-party lab for structural/chemical testing (e.g., steel tensile strength, paint lead content) | Quality Mgr | — | 1–2 weeks |
| 5 | **Decision**: (a) Pass: System flags SKU as "QC Approved"; (b) Fail: Item rejected; Vendor must remediate or SKU is blocked from sale | Quality Mgr | VP Merch | 30 min |
| 6 | **Periodic Audit**: Random samples pulled from DC stock (W3) and sent for re-testing to ensure consistent quality | Quality Mgr | Quality Mgr | Ongoing |

### System Touchpoints
- "QC Approved" status flag in Item Master
- Storage of digital certificates and lab reports linked to the SKU
- Automated block on PO creation (W2) for items with expired or failed QC status
- Integration with W3 (Receiving) for sample pulling during DC arrival

### Pain Points / Risks
- External lab testing turnaround (1–2 weeks per step 4) delays new product onboarding; for seasonal items tied to construction peak season (dry months, January–May), late QC approval can cause BuildRight to miss the selling window entirely
- Products failing PS Mark or ICC certification (step 2) cannot legally be sold in the Philippines; if discovered post-receipt, BuildRight must RTV (W88) or destroy inventory, absorbing both cost and potential BIR customs penalties for imported non-compliant goods
- Periodic re-testing (step 6) of existing SKUs is often deprioritized due to lab costs and operational workload; quality drift in vendor manufacturing goes undetected until customer complaints spike, at which point reputation damage is already done

### Time Estimate
- Documentation review and internal testing (steps 2–3): ~3 hours per item
- External lab testing (step 4): 1–2 weeks elapsed per batch of samples; minimal internal effort (~1 hour to prepare and ship samples)
- Decision and system update (step 5): ~30 min per item
- Periodic audit sampling (step 6): ~2 hours/week ongoing for random DC stock pulls
- Total internal effort: ~4–5 hours per new item tested; periodic audits add ~8–10 hours/month ongoing

### Staffing Implication
- **Quality Manager**: ~500–1,000 items tested/year × ~4–5 hours each = ~2,000–5,000 hours/year. This exceeds a single FTE; requires a dedicated Quality & Compliance team of 2–3 persons.
- **External lab costs**: Budget PHP 3,000–10,000 per test × 500–1,000 tests/year = PHP 1.5M–10M/year. Must be budgeted in annual OpEx.
- **Category Manager**: Approval decisions add ~30 min/item × ~500–1,000 items = ~250–500 hours/year spread across ~4 CMs = ~60–125 hours/CM/year. Absorbed.

---

## W155. Vendor Strategic Collaboration & Joint Business Planning (JBP)

| Field | Detail |
|---|---|
| **Trigger** | Annual planning cycle with "Top 20" strategic vendors |
| **Frequency** | Annual (with quarterly progress reviews) |
| **Volume** | Covers 20 key vendors (~45% of COGS) |
| **Owner** | VP for Merchandising |
| **Participants** | Category Managers, Buyers, Vendor Executives, Supply Chain Planners |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Performance Review**: Jointly review prior year: fill rates (W44), margin, growth, and rebate achievement (W27) | Buyer / Vendor | Category Mgr | 4 hours |
| 2 | **Growth Targets**: Set consensus growth targets and market share goals for the next 12 months | Category Mgr | VP Merch | 2 hours |
| 3 | **Supply Chain Alignment**: Share long-term demand forecasts (W31) to help vendor plan production capacity | Demand Planner | — | 1 hour |
| 4 | **JBP Document**: Sign joint plan covering exclusive SKUs, marketing co-op (W153), and logistics efficiency | VP Merch | CEO | 1 week |

### System Touchpoints
- JBP document repository linked to vendor master for top 20 strategic vendors
- Demand forecast sharing module (W31) with vendor portal access for collaborative planning
- Scorecard integration (W44) for joint performance review data pull
- Rebate and margin tracking (W27, W102) for JBP target measurement
- Marketing co-op fund tracking linked to W153 promotional budget

### Pain Points / Risks
- JBP growth targets are aspirational and based on consensus forecasts; if actual market conditions diverge (e.g., construction slowdown due to government infrastructure delays), both BuildRight and the vendor face unmet commitments, straining the strategic relationship
- Sharing long-term demand forecasts (step 3) with vendors risks competitive intelligence leakage; a vendor may use BuildRight's expansion plans to negotiate better terms with a competitor or prioritize a rival retailer's orders
- JBP exclusive SKU commitments lock up shelf space that may generate lower margin than open-assortment alternatives; if the exclusive product underperforms, BuildRight cannot exit the commitment until the annual JBP cycle resets

### Time Estimate
- Annual performance review with each strategic vendor: ~4 hours/vendor
- Growth target setting and supply chain alignment: ~3 hours/vendor
- JBP document finalization and sign-off: ~1 week elapsed (legal review + executive approval)
- Quarterly progress reviews: ~2 hours/vendor/quarter × 4 quarters = ~8 hours/vendor/year
- Total per strategic vendor: ~15–20 hours/year active time; for 20 vendors = ~300–400 hours/year across the team

### Staffing Implication
- **VP Merchandising**: Leads annual JBP with 20 vendors — ~4 hours/vendor annual session + ~2 hours/quarter review = ~12 hours/vendor/year × 20 vendors = ~240 hours/year (~5 hours/week during planning season). Core executive responsibility.
- **Category Managers**: Support JBP sessions for their categories — ~3–4 hours/vendor/year. With 20 vendors ÷ ~4 Category Managers = ~5 vendors each = ~15–20 hours/CM/year. Absorbed.
- **Buyers**: Preparation and follow-up per vendor — ~2–3 hours/vendor/year. At ~2 vendors/buyer = ~4–6 hours/buyer/year. Minimal.
- **No incremental headcount**, but VP Merchandising time commitment is substantial during annual JBP cycle.

---

## W160. Private Label Factory Audit & Social Compliance

| Field | Detail |
|---|---|
| **Trigger** | Onboarding new private label vendor (W129); or annual compliance cycle |
| **Frequency** | Annual per factory |
| **Volume** | ~30–50 factories audited annually |
| **Owner** | Quality & Compliance Manager |
| **Participants** | Buyer, Legal, External Auditor, Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Self-Assessment**: Vendor submits social compliance questionnaire (labor practices, safety, environmental) | Vendor | Quality Mgr | 1 week |
| 2 | **On-site Audit**: Internal or 3rd-party audit (SGS/TUV) of factory floor, dormitories, and payroll records | External Auditor | Quality Mgr | 1–2 days |
| 3 | **CAPA**: If violations found, vendor must submit and execute Corrective Action Plan (W110) | Vendor | Quality Mgr | 30 days |
| 4 | **Certification**: Issue "BuildRight Approved Factory" status in ERP; linked to W2 PO creation | Quality Mgr | VP Merch | 1 day |

### System Touchpoints
- Vendor master "BuildRight Approved Factory" status flag linked to PO creation (W2) — system blocks POs for uncertified private label factories
- Social compliance questionnaire and audit report document storage linked to vendor master
- CAPA tracking integration (W110) for factory corrective actions following audit findings
- Annual audit scheduling with expiry alerting — system blocks PO creation if factory audit is overdue by > 30 days

### Pain Points / Risks
- Third-party factory audits (SGS/TUV) cost PHP 80,000–150,000 per audit per factory; with 30–50 factories audited annually, the program costs PHP 2.4M–7.5M/year — significant for a private label program that represents a minority of total SKUs
- Chinese and Southeast Asian factories may present staged conditions during scheduled audits; without unannounced follow-up visits, labor or environmental violations can resume immediately after the auditor leaves
- Revoking "BuildRight Approved Factory" status (step 4) due to failed CAPA halts all pending POs for that factory, potentially causing private label stockouts across 200 stores while an alternative factory is sourced and qualified — a process that can take 3–6 months

### Time Estimate
- Vendor self-assessment questionnaire: 1 week (vendor-dependent)
- On-site audit coordination and execution: 1–2 days on-site + ~4 hours scheduling/logistics per factory
- CAPA follow-up and verification: 30 days elapsed; ~2–4 hours internal tracking per factory
- Certification decision and system update: ~1 day
- Total internal effort per factory audit: ~8–12 hours active time; 4–6 weeks elapsed from self-assessment to certification

### Staffing Implication
- **Quality & Compliance Manager**: 30–50 audits/year × ~8–12 hours each = ~240–600 hours/year = ~5–12 hours/week. A significant portion of this role; may require a dedicated compliance coordinator if private label program grows.
- **Buyer**: Audit coordination and vendor communication adds ~2–4 hours/factory. With 30–50 factories ÷ 10–12 buyers = ~3–5 factories/buyer/year = ~10–20 hours/buyer/year. Absorbed.
- **External audit cost**: PHP 2.4M–7.5M/year budget allocation required for third-party auditors (SGS/TUV).

---

## W161. Vendor Price Protection & Market Markdown Claims

| Field | Detail |
|---|---|
| **Trigger** | Retail price reduction (W40, W93) or competitive price match (W61) impacting stocking items |
| **Frequency** | Monthly or per major price event |
| **Volume** | Covers all SKU categories with price protection agreements |
| **Owner** | Pricing Analyst |
| **Participants** | Buyer, Category Manager, Vendor, Finance (AR/AP) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Eligibility Review**: Identify SKUs with active price protection clauses in vendor contracts (W62) upon retail price change | Pricing Analyst | Category Manager | 1 hour |
| 2 | **Stock-on-Hand Capture**: System takes a snapshot of group-wide inventory (stores + DCs) at the moment of price change | System | — | Real-time |
| 3 | **Claim Calculation**: Calculate claim amount = (Old Retail - New Retail) × Inventory Count; or (Old Cost - New Cost) × Inventory Count, depending on contract | Pricing Analyst | Category Manager | 30 min |
| 4 | **Vendor Validation**: Transmit claim report to vendor for verification and approval; negotiate discrepancies | Buyer | Category Manager | 3-5 days |
| 5 | **Credit Note Issuance**: Vendor issues Credit Memo to offset future payables; or system auto-deducts from next PO payment if pre-authorized | Vendor / Finance | Buyer | 5-10 days |
| 6 | **Margin Recovery**: Update product costing (W85) to reflect the recovered margin; update P&L for category (W102) | Finance | Category Manager | 1 hour |

### System Touchpoints
- Price protection clause flag in vendor contract master (W62) identifying eligible SKUs
- Real-time inventory snapshot engine capturing group-wide stock-on-hand (stores + DCs) at point of price change
- Automated claim calculation module: (Old Price - New Price) x Inventory Count per SKU per location
- Vendor portal claim submission with supporting data export for vendor validation
- Credit memo / debit note posting against vendor payable with automated GL entries
- Integration with W40 (price change), W85 (product costing), W93 (markdown), W102 (P&L reporting)

### Pain Points / Risks
- Stock-on-hand snapshot (step 2) must be precisely timed with the retail price change; if stores apply the new price before the system snapshot runs, inventory at the old price is understated, reducing the claim amount payable by the vendor
- Vendor validation (step 4) typically takes 3–5 business days and vendors frequently contest the inventory count, especially for SKUs with high store-level shrink; disputed claims delay margin recovery and require manual reconciliation by the Buyer
- For import vendors with price protection denominated in foreign currency, PHP exchange rate fluctuations between the claim date and credit note issuance can reduce the actual PHP value recovered, partially negating the margin protection intent

### Time Estimate
- Eligibility review and stock-on-hand snapshot: ~1 hour per price event (automated snapshot + manual SKU review)
- Claim calculation and preparation: ~30 min per price event
- Vendor validation and negotiation: 3–5 business days elapsed; ~1–2 hours active Buyer/AP time per claim
- Credit note issuance and margin recovery posting: 5–10 business days elapsed; ~1 hour Finance time
- Total internal effort per price protection claim: ~3–5 hours active time over 1–2 weeks elapsed

### Staffing Implication
- **Pricing Analyst**: Monthly or per major price event — ~2–4 hours/event. With ~4–8 major price events/month = ~8–32 hours/month. Absorbed within existing Pricing Analyst role.
- **Buyer**: Vendor negotiation per claim adds ~1–2 hours/claim; at ~4–8 claims/month ÷ 10–12 buyers = minimal per-buyer impact.
- **Finance (AR/AP)**: Credit note posting and margin recovery adds ~1 hour/claim. Absorbed.

---

## W244. Vendor Invoice Dispute & Discrepancy Resolution

| Field | Detail |
|---|---|
| **Trigger** | 3-Way Match fails (discrepancy between PO, GR, or Vendor Invoice in price or quantity) in W7 |
| **Frequency** | Weekly |
| **Volume** | ~50–100 invoice disputes per month |
| **Owner** | AP Supervisor |
| **Participants** | AP Clerk, Buyer (Merchandising), Vendor Account Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Discrepancy Identification**: System flags 3-way match failure (W7 step 3). AP Clerk isolates invoice in "Disputed" status. | AP Clerk | — | 15 min |
| 2 | **Categorization**: System classifies discrepancy: (a) Price variance (invoice price > PO price), or (b) Quantity variance (invoice quantity > GR quantity). | System | — | Automated |
| 3 | **Internal Review**: AP Clerk routes price variance to the Buyer for review. Buyer either: (a) Approves invoice (PO was outdated, updates contract price books), or (b) Rejects price, generating a Debit Note request in ERP. | AP Clerk / Buyer | Category Manager | 1 day |
| 4 | **Quantity Reconciliation**: For quantity variance, AP Clerk cross-references GR slip and DC warehouse log. If short-shipped, routes to Vendor for confirmation. | AP Clerk | AP Supervisor | 2 hours |
| 5 | **Dispute Communication**: Buyer/AP Supervisor sends automated Dispute Notice with supporting system logs to the vendor via the Vendor Portal (W36). | AP Supervisor | — | 10 min |
| 6 | **Settlement**: Vendor accepts debit note or issues corrected invoice/Credit Note. AP Clerk posts Credit/Debit Note in ERP to match the variance and approves invoice for payment run. | AP Clerk / Vendor | AP Supervisor | 2–5 days |

### System Touchpoints
- Automated 3-way match variance flags (price/qty)
- Dispute workflow router (AP ↔ Buyer ↔ Vendor)
- Debit/Credit Note generation and automated GL posting
- Integration with W7 (AP processing) and W36 (Vendor Portal)

### Pain Points / Risks
- 50–100 invoice disputes per month represent a significant AP workload; each disputed invoice ties up working capital until resolved, and aged disputed payables can strain vendor relationships — especially with small MSME vendors who depend on timely payment
- Price variances often stem from vendor unilateral price increases not yet reflected in the PO; if the Buyer retroactively approves the higher price (step 3a), it sets a precedent that vendors can ship at un-agreed prices and negotiate after the fact
- Quantity variances caused by DC receiving errors (wrong count at GR) rather than vendor short-shipment require internal correction; if AP does not distinguish between vendor-caused and internally-caused discrepancies, the vendor scorecard (W44) is distorted

### Time Estimate
- Discrepancy identification and categorization: ~15 min/invoice
- Internal review and Buyer routing (price variance): ~1 day turnaround per dispute
- Quantity reconciliation and vendor communication: ~2 hours + 10 min for portal notification
- Settlement (credit/debit note posting): 2–5 business days vendor response; ~15 min AP posting
- Total AP/Buyer effort per dispute: ~1–2 hours active time; elapsed time 3–7 business days end-to-end

### Staffing Implication
- **AP Supervisor/Clerk**: 50–100 disputes/month × ~1–2 hours each = ~50–200 hours/month. With ~4–6 AP Clerks, this is ~10–40 hours/clerk/month. Significant but absorbed within existing AP team.
- **Buyer**: Each price variance dispute routed to Buyer for review — ~1 day turnaround per dispute. At ~50–100 disputes/month ÷ 10–12 buyers = ~5–10 disputes/buyer/month × ~30 min = ~2–5 hours/buyer/month. Absorbed.
- **No incremental headcount**, but AP workload from disputes should be monitored; if dispute rate exceeds 100/month, consider a dedicated AP resolution specialist.

---

## W245. Vendor Performance Chargebacks & Penalties Management

| Field | Detail |
|---|---|
| **Trigger** | Incomplete shipment, late delivery, or poor product quality at GR (W3/W18) resulting in scorecard failure (W44) |
| **Frequency** | Ongoing |
| **Volume** | ~100–150 chargeback events/month across all DCs |
| **Owner** | Supplier Compliance Manager |
| **Participants** | DC Receiving Supervisor, Category Manager, Vendor Compliance, AP Specialist |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Log Discrepancy**: DC Receiving Supervisor logs delivery failure at GR (shortage, damage, packaging non-compliance) or late arrival (> 2 hours past SLA). | DC Supervisor | DC Manager | 15 min |
| 2 | **Fines Engine Execution**: System references Supplier Compliance Agreement (W62) and auto-calculates fee/penalty: (a) Fill rate failure: 2% of unfulfilled value; (b) Late delivery: PHP 5,000 flat penalty; (c) Packaging non-compliance: PHP 2,500 penalty. | System | — | Automated |
| 3 | **Notification**: System triggers a "Compliance Infraction Report" with photographs and receiving logs, sending it to the vendor via the Vendor Portal (W36) with copy to the Category Manager. | Supplier Compliance | — | 10 min |
| 4 | **Dispute Window**: Vendor has 5 business days to dispute infraction by uploading carrier proof or force majeure evidence; compliance manager reviews and makes final ruling. | Vendor / Compliance Mgr | Supplier Compliance Mgr | 5 days |
| 5 | **Chargeback Posting**: If infraction upheld, system automatically generates an AR invoice / AP Debit Note (Dr. Vendor Chargeback Receivable / Cr. Procurement Penalty Income) in the vendor's ledger. | System | — | Automated |
| 6 | **Deduction Reconciliation**: At next AP payment cycle (W7), matching engine auto-applies debit note as deduction against vendor's invoice payment, netting the settlement. | AP Specialist | AP Supervisor | 10 min |

### System Touchpoints
- Supplier compliance fine/penalty calculation engine linked to receiving logs and contracts
- Infraction workflow management dashboard with vendor portal linkage
- Automated Debit Note / AR invoice posting in General Ledger
- Auto-application of debit notes at payment cycle (W7)

### Pain Points / Risks
- Automated chargeback posting (step 5) reduces vendor payable balances; vendors who perceive penalties as excessive or unjustified may retaliate by deprioritizing BuildRight orders, reducing fill rates, or refusing to bid on new business — turning a compliance tool into a relationship-damaging mechanism
- The 5-day vendor dispute window (step 4) is tight, especially for vendors in remote provinces or import vendors in different time zones; legitimate disputes excluded from the window are unfairly assessed, creating audit and legal risk
- Chargeback income (Dr. Vendor Chargeback Receivable / Cr. Procurement Penalty Income) must be carefully distinguished from vendor rebates (W27) for BIR tax reporting; misclassification can trigger BIR examination of improperly reported income or deductible expenses

### Time Estimate
- Discrepancy logging and fines engine execution: ~15 min/event (mostly automated)
- Vendor notification and dispute window management: ~10 min/event + 5 business days vendor response time
- Chargeback posting and deduction reconciliation at next payment cycle: ~10 min/event
- Total internal effort per chargeback event: ~35 min; at ~100–150 events/month = ~60–90 hours/month across DC Supervisors, Compliance Manager, and AP Specialists

### Staffing Implication
- **Supplier Compliance Manager**: ~100–150 chargeback events/month × ~25 min/event = ~40–60 hours/month. This is a near-full-time function; may require a dedicated role or reassignment from existing Compliance/AP team.
- **DC Receiving Supervisors**: Logging discrepancies adds ~15 min/event × ~100–150 events = ~25–40 hours/month across all DCs. Absorbed across multiple supervisors.
- **AP Specialists**: Deduction reconciliation at payment cycle adds ~10 min/event = ~15–25 hours/month. Absorbed within existing AP team.

---

## W422. VMI Collaborative Data Sharing & Replenishment Execution

| Field | Detail |
|---|---|
| **Trigger** | Weekly scheduled data sync for Vendor Managed Inventory (VMI) partners (e.g., Boysen, Holcim) |
| **Frequency** | Weekly (typically Sunday night for Monday review) |
| **Volume** | ~20 high-velocity VMI vendors |
| **Owner** | Inventory Planner |
| **Participants** | Buyer, Vendor Sales Rep, IT (Data Integration), DC Receiving |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Export**: System automatically generates and transmits "VMI Data Package" to vendor via EDI/SFTP: (a) SOH by location, (b) Sales-out (sell-through) last 7 days, (c) Open POs/Transfers, (d) Minimum/Maximum stock targets (W312) | System | IT Ops | Automated |
| 2 | **Vendor Planning**: Vendor reviews data; calculates replenishment requirement to maintain target weeks-of-supply; proposes a "VMI PO" in the Vendor Portal | Vendor Rep | — | 4 hours |
| 3 | **Review & Approval**: Inventory Planner reviews vendor-proposed POs; checks against total open budget (OTB) and DC capacity; approves or modifies the PO in ERP | Inventory Planner | Category Mgr | 1 hour/vendor |
| 4 | **PO Conversion**: Approved proposal converts into a live Purchase Order (W2); system notifies Vendor to proceed with shipment | System | Buyer | Automated |
| 5 | **Priority Receiving**: DC Receiving identifies VMI shipments; performs priority tally and putaway to ensure fast data feedback loop | DC Receiving | DC Manager | Per W3 |
| 6 | **Performance Review**: Monthly: Buyer and Vendor review "VMI Service Level" (Fill Rate vs. In-Stock %); adjust Min/Max parameters in W312 if needed | Buyer | Category Mgr | 1 hour |

### System Touchpoints
- Automated EDI/SFTP data export module (W422.1)
- Vendor Portal for PO proposal and collaboration (W20)
- Integration with W312 (Planning Parameters), W2 (PO Cycle), and W44 (Vendor Scorecard)
- DC Receiving priority flagging for VMI vendors

### Time Estimate
Weekly cycle: Automated data sync + 1 hour per vendor for Planner review. Monthly review: 1 hour per vendor. Inventory Planner spends ~20 hours/week managing 20 VMI partners.

### Pain Points / Risks
- **Data Latency**: If the Sunday night data sync fails, the vendor plans on "stale" data, leading to overstocks or shortages for the following week.
- **Over-shipping**: Vendors may "push" slow-moving inventory into BuildRight stores to meet their own sales targets, bloating BuildRight's working capital.
- **In-Transit Invisibility**: If the vendor ships but the EDI ASN (Advanced Shipping Notice) is not processed, BuildRight planners may double-order thinking stock is still low.
- **Conflicting Targets**: BuildRight's goal is high turns; Vendor's goal is high volume. Misaligned Min/Max targets create constant friction in PO approvals.

### Staffing Implication
- **Inventory Planner**: ~20 hours/week for review of 20 VMI vendors. This is a significant portion of a single FTE's workload.
- **IT Support**: ~2 hours/month for monitoring EDI/SFTP health for VMI data flows.
- **No incremental headcount** — offsets time spent by Buyers on manual PO creation for high-velocity items.

---

## W491. Supplier Financial Health & Credit Risk Monitoring

| Field | Detail |
|---|---|
| **Trigger** | Annual supplier risk review cycle; vendor financial distress signal; significant new vendor onboarding; quarterly watchlist review |
| **Frequency** | Annual (comprehensive review); quarterly (watchlist review); event-driven (distress signals) |
| **Volume** | ~800–1,000 active vendors; ~50–100 critical/import vendors requiring deep review |
| **Owner** | Procurement — Supplier Risk Manager (or Category Manager) |
| **Participants** | Category Manager, VP Supply Chain, Finance Manager, Import Coordinator, Legal Head |

### Background

With ~40% of COGS from imports and ~800–1,000 active vendors, BuildRight's supply chain is exposed to supplier financial risk. A vendor's bankruptcy, insolvency, or production halt can disrupt critical supply lines for months — especially for import vendors with long lead times (45–90 days) and limited alternative sources. W44 covers vendor performance scorecard (delivery, quality, fill rate) but does not assess vendor financial health. This workflow addresses the financial risk dimension: monitoring supplier financial stability, identifying early warning signs, and activating contingency plans before a vendor failure disrupts operations.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Vendor Risk Tiering**: Category Manager classifies all active vendors into risk tiers: (a) **Tier 1 — Critical**: Top 20 vendors (45% of COGS), single-source vendors, sole-import vendors for critical categories; requires annual full financial review; (b) **Tier 2 — Important**: Vendors contributing >PHP 5M annual spend or providing >5% of a category's supply; requires annual financial health questionnaire; (c) **Tier 3 — Standard**: All other vendors; requires biennial review; (d) maintain tiering in Vendor Master (W287) with risk classification attribute | Category Manager | VP Supply Chain | 1 week/annual |
| 2 | **Tier 1 — Full Financial Review**: For critical vendors: (a) request audited financial statements (if publicly available — pull from SEC EDVIEW for Philippine corporations); (b) analyze key financial ratios: current ratio, debt-to-equity, interest coverage, revenue trend, net income margin; (c) check for SEC filings indicating financial distress (petition for suspension of payments, rehabilitation proceedings); (d) check business registration status with DTI/SEC (active vs. revoked/suspended); (e) for import vendors: check country risk (political instability, trade restrictions, currency controls); (f) document financial health assessment in vendor risk file | Category Manager / Finance Manager | VP Supply Chain | 4–8 hours/vendor |
| 3 | **Tier 2 — Financial Health Questionnaire**: For important vendors: (a) send annual Financial Health Questionnaire requesting: business registration status, years in operation, key customer references, any pending legal proceedings, any recent ownership or management changes; (b) review responses and flag concerns; (c) cross-reference with vendor performance data (W44) — declining delivery performance may indicate financial distress | Category Manager | — | 1–2 hours/vendor |
| 4 | **Continuous Monitoring Signals**: Category Manager monitors early warning signals throughout the year: (a) **Operational signals**: declining fill rate (W44), increased backorder rate (W56), sudden quality issues (W110), requests for early payment or advance payment (unusual for the vendor); (b) **Market signals**: vendor's industry sector in downturn, competitor retailers reporting issues with same vendor, news reports of vendor's financial difficulties; (c) **Relationship signals**: vendor becomes unresponsive, key account manager leaves, vendor stops attending industry events; (d) log signals in vendor risk file and escalate to VP Supply Chain if material | Category Manager | VP Supply Chain | Ongoing |
| 5 | **Watchlist Management**: Category Manager maintains the Supplier Financial Risk Watchlist: (a) vendors flagged with any distress signal are placed on the watchlist; (b) watchlist reviewed monthly by VP Supply Chain; (c) for watchlist vendors: increase safety stock for their SKUs (W312 parameter override), accelerate sourcing of alternative suppliers, negotiate consignment terms (W23) to reduce exposure; (d) if vendor is sole source: initiate emergency alternative sourcing (single-source mitigation plan) | Category Manager / VP Supply Chain | VP Supply Chain | 4 hours/month |
| 6 | **Vendor Failure Contingency Activation**: If a vendor shows severe financial distress or ceases operations: (a) VP Supply Chain activates contingency plan: (b) immediately increase orders from alternative vendors to cover critical SKUs; (c) if no alternative exists for critical SKUs: authorize emergency procurement (W60) with new vendor onboarding fast-track (W36); (d) assess inventory on hand and pipeline — how many weeks of supply remain; (e) communicate to affected internal stakeholders (Merchandising, Store Ops); (f) work with Legal on any prepaid deposits or outstanding purchase commitments (W2); (g) Finance assesses and recovers any outstanding vendor rebates or deposits (W27) | VP Supply Chain | COO | Event-driven |
| 7 | **Annual Report**: Category Manager prepares annual Supplier Financial Risk Report: (a) summary of vendor risk tiering and movement; (b) financial health scores for Tier 1 vendors; (c) watchlist activity and outcomes; (d) contingency plans activated during the year; (e) single-source dependency analysis; (f) recommendations for vendor diversification; (g) present to VP Supply Chain and CFO | Category Manager | VP Supply Chain | 1 week/annual |

### System Touchpoints
- Vendor Master (W287): risk tiering classification, financial health score attribute
- Vendor Performance Scorecard (W44): performance data correlation with financial health
- Inventory Planning Parameters (W312): safety stock override for watchlist vendors
- Procurement Module (W2): contingency PO generation
- ERP Financial Reporting: vendor spend analysis by tier
- Integration with W36 (vendor onboarding), W44 (vendor scorecard), W56 (backorder management), W60 (emergency procurement), W110 (supplier quality CAPA), W287 (vendor master governance)

### Pain Points / Risks
- **Private company opacity**: Most Philippine vendors (especially MSMEs) are privately held and not required to file public financial statements; obtaining reliable financial data requires direct vendor cooperation, which is limited if the vendor is already in distress
- **Import vendor country risk**: Vendors in China, Taiwan, and Indonesia face different regulatory, political, and economic risks that are difficult to monitor from the Philippines; a sudden factory closure in China can disrupt BuildRight's supply chain before any warning signals are detected
- **Single-source dependency**: For certain categories (e.g., cement from Holcim/Republic, tiles from specific Chinese manufacturers), BuildRight may be dependent on a single vendor; despite financial health monitoring, the loss of a single-source vendor can cause months of supply disruption
- **Vendor reluctance to share financial data**: Vendors may view financial health questionnaires as intrusive or may be reluctant to disclose financial difficulties, providing misleadingly positive responses

### Time Estimate
- Annual vendor risk tiering: 1 week
- Tier 1 full financial review: 4–8 hours per vendor × ~20 vendors = ~80–160 hours
- Tier 2 questionnaire: 1–2 hours per vendor × ~80 vendors = ~80–160 hours
- Watchlist management: 4 hours/month = ~48 hours/year
- Annual report: 1 week
- **Total annual**: ~250–400 hours/year across Category Managers

### Staffing Implication
- **Category Managers**: ~250–400 hours/year collectively across all categories. Absorbed into existing Category Manager duties as part of vendor management responsibility.
- **Finance Manager**: ~20–40 hours/year for Tier 1 financial analysis support. Absorbed.
- **VP Supply Chain**: ~24 hours/year for watchlist review and contingency activation. Absorbed.

---

## W513. Vendor-Funded Promotional Activity & Co-op Advertising Management

| Field | Detail |
|---|---|
| **Trigger** | Annual JBP sets vendor promotional fund budget; or vendor approves promotional activity funding request |
| **Frequency** | ~30–50 active vendor fund agreements/year; ~100–150 promotional activity claims/year |
| **Volume** | ~125 average claims/year across ~40 vendors |
| **Owner** | Trade Marketing Manager |
| **Participants** | Category Manager, Marketing Campaign Manager, AP Clerk, Vendor Account Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | During annual JBP (W155): Category Manager and Vendor Manager negotiate vendor promotional fund allocation for the year; agree on total fund amount, eligible activity types (co-op advertising, in-store displays, digital campaigns, events, price promotions), fund utilization timeline, and proof-of-execution requirements | Category Manager | VP Merchandising | Per JBP |
| 2 | Trade Marketing Manager creates vendor fund agreement in system: fund amount, eligible activity types, fund period (annual with quarterly milestones), proof requirements (photos, invoices, media screenshots, sales data), reimbursement terms (net 30 from claim approval), fund expiration date | Trade Marketing Manager | VP Marketing | 30 min/agreement |
| 3 | When promotional activity occurs (W83, W262): Marketing Campaign Manager logs activity details linked to vendor fund agreement — activity type, channels used, execution dates, estimated cost, expected vendor fund utilization | Campaign Manager | Trade Marketing Manager | 15 min |
| 4 | Trade Marketing Manager submits proof-of-execution to vendor: (a) in-store display photos with date stamp; (b) digital campaign screenshots with impressions/clicks data; (c) print advertising tear sheets; (d) radio/TV broadcast certificates; (e) event attendance records | Trade Marketing Manager | — | 30 min |
| 5 | Vendor reviews and approves/rejects claim; system tracks vendor response with 15-day SLA; if vendor disputes, Trade Marketing Manager provides additional evidence | Trade Marketing Manager | Category Manager | 15 min |
| 6 | Upon vendor approval: AP Clerk processes reimbursement claim — validates against fund agreement balance, confirms proof-of-execution documentation complete, posts vendor credit memo reducing AP balance | AP Clerk | AP Supervisor | 15 min |
| 7 | System tracks fund utilization per vendor: total fund allocated, claims submitted, claims approved, claims pending, fund balance remaining, fund utilization rate; alerts Trade Marketing Manager when utilization <60% at mid-year | System | — | Automated |
| 8 | Monthly: Trade Marketing Manager reviews vendor fund utilization dashboard: fund balance by vendor, pending claims, expiring funds; coordinates with Category Managers to maximize fund utilization before expiration | Trade Marketing Manager | VP Marketing | 2 hours/month |
| 9 | Quarterly: Trade Marketing Manager reports vendor fund ROI per vendor: promotional activity cost (vendor-funded vs. BuildRight-funded), incremental sales lift, cost-per-acquisition, fund utilization rate; feeds into JBP scorecard (W155) | Trade Marketing Manager | VP Marketing | 4 hours/quarter |
| 10 | Annually: Trade Marketing Manager reconciles all vendor fund agreements; identifies unclaimed/expired funds; closes completed agreements; carries forward renewed agreements into next JBP cycle | Trade Marketing Manager | VP Marketing | 8 hours/year |

### System Touchpoints
- Vendor fund agreement creation with budget, eligibility, and proof requirements (PUR-026)
- Promotional activity logging linked to fund agreement and campaign (PUR-026, W83)
- Proof-of-execution document management with vendor submission workflow (PUR-026)
- Vendor claim tracking with response SLA monitoring (PUR-026)
- AP credit memo processing linked to fund agreement balance (W7, FIN-004)
- Fund utilization dashboard with balance tracking and expiration alerts (PUR-026)
- Quarterly ROI reporting with sales lift correlation (PUR-026, W102)
- Integration with JBP workflow (W155) for annual fund allocation
- Integration with campaign planning (W83) and store promotional setup (W262)

### Time Estimate
Fund agreement setup: ~30 min/agreement × ~40 = ~20 hours/year. Activity logging: ~15 min/activity × ~125 = ~31 hours/year. Proof submission: ~30 min/claim × ~125 = ~62 hours/year. Monthly review: ~2 hours × 12 = 24 hours/year. Total: ~137 staff-hours/year.

### Pain Points / Risks
- Vendor disputes proof-of-execution quality and rejects claim — mitigated by clear proof requirements in fund agreement and photo evidence with metadata
- Fund underutilization — vendor funds expire unused; mitigated by monthly utilization review and mid-year alerts
- Disagreement on promotional activity ROI between vendor and BuildRight — mitigated by pre-agreed metrics in JBP and shared sales data

### Staffing Implication
- 1 Trade Marketing Manager within existing Marketing team (23 FTE) absorbs this responsibility.
- AP Clerk absorbs reimbursement processing (~15 min × ~125 claims = ~31 hours/year).

---

## W593. Vendor Portal Content Management & Self-Service Operations

| Field | Detail |
|---|---|
| **Trigger** | New vendor onboarded (W36); scheduled content review (monthly); vendor request for portal access or content update; PO distribution cycle; invoice submission deadline; quarterly feature enhancement cycle |
| **Frequency** | Daily PO distribution monitoring and vendor query response; monthly content review; quarterly feature enhancement; ad-hoc onboarding (~20–40 new vendors/month per W36) |
| **Volume** | ~800–1,000 active vendor portal accounts; ~1,200 POs/month distributed via portal (~60% of all POs); ~4,000–5,000 vendor-submitted invoices/month via portal; ~200–300 vendor queries/month; ~20–40 new vendor portal onboarding/month |
| **Owner** | Vendor Portal Administrator (within Procurement team) |
| **Participants** | Vendor Portal Administrator (R/A), Buyer (R for PO follow-up), AP Clerk (R for invoice reconciliation), Category Manager (A for scorecard visibility), IT Support (R for portal technical issues per W48), Vendor (R for portal usage) |

### Background

W36 covers vendor onboarding into the ERP system. W44 covers vendor performance scoring. W7 covers AP invoice processing. W100 covers vendor statement reconciliation. W287 covers vendor master data governance. However, no workflow covers the day-to-day management of the vendor self-service portal — the digital front door through which ~800–1,000 vendors interact with BuildRight for purchase order acknowledgment, invoice submission, goods receipt confirmation, performance scorecard visibility, catalog content updates, and dispute initiation.

The vendor portal is a critical operational layer: it reduces manual buyer/AP workload by enabling vendors to self-serve on routine transactions, improves data accuracy by eliminating re-keying of invoices and PO acknowledgments, and increases supply chain visibility by giving vendors real-time PO and GR status. For a company processing ~1,200 merchandise POs/month and ~6,000+ GRs/month, the portal is the primary channel for vendor communication. Without active portal management, vendor adoption stagnates, manual fallback increases, and the portal degrades into an underutilized tool rather than a strategic procurement platform.

Philippine context is important: many MSME vendors (constituting ~60% of the vendor base) have limited digital literacy and require hands-on guidance to adopt portal capabilities. International vendors (the remaining ~40%) expect EDI-like functionality and real-time status updates. The portal must serve both audiences.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **New vendor portal onboarding**: when a vendor is approved per W36, Vendor Portal Administrator creates portal account — (a) generates vendor login credentials (unique user ID, temporary password); (b) configures portal access scope based on vendor type: merchandise vendor (full access — PO, invoices, GR, scorecard, catalog), service vendor (limited access — PO, invoices only), import vendor (full + LC/shipping document exchange); (c) assigns vendor to correct purchasing organization and category in portal; (d) sends welcome email with portal URL, login instructions, user guide (English and Filipino), and IT helpdesk contact for technical issues | Vendor Portal Administrator | Category Manager | 15–20 min/vendor |
| 2 | **Vendor portal training (first-time users)**: for vendors new to the portal, Vendor Portal Administrator conducts 30-minute remote walkthrough — (a) PO acknowledgment: how to view PO details, confirm delivery dates, and submit acknowledgment; (b) invoice submission: how to create and upload BIR-compliant invoices (with correct TIN, OR number, and line-item matching to PO); (c) GR confirmation: how to view goods receipt status and quantities; (d) performance scorecard: how to view delivery, quality, and responsiveness scores; (e) dispute initiation: how to open a billing or delivery dispute linked to a specific PO/GR; (f) catalog update: how to submit product information changes (description, unit of measure, packaging). For MSME vendors with limited digital capability, offer in-person training at nearest BuildRight DC or store during vendor visit | Vendor Portal Administrator | — | 30 min/vendor |
| 3 | **Daily PO distribution monitoring**: system automatically publishes approved POs to the vendor portal each morning after buyer confirmation (W2A step 7); Vendor Portal Administrator monitors PO distribution dashboard — (a) POs published today: count, total value, by vendor; (b) PO acknowledgment status: % of POs acknowledged within 24 hours; (c) unacknowledged POs older than 48 hours flagged for buyer follow-up; (d) PO delivery date changes (amendments) reflected in portal in real-time; for vendors not yet on portal (~40% of POs, typically smaller MSME vendors), POs transmitted via email/phone per W2A and tracked separately | Vendor Portal Administrator / Buyer | Buyer | 30 min/day |
| 4 | **Vendor invoice submission guidance**: vendors submit invoices through portal by uploading BIR-compliant invoice (scanned PDF or XML) linked to PO number; system performs automated 3-way match validation: (a) invoice line items vs. PO line items (quantity, unit price, item code); (b) invoice total vs. PO total (within tolerance); (c) GR quantity vs. invoiced quantity; Vendor Portal Administrator monitors invoice submission queue — (a) invoices with matching errors (price variance >5%, quantity mismatch, missing PO reference) flagged for manual review; (b) common MSME vendor errors: incorrect TIN format, missing OR number, wrong UOM, invoice not linked to PO; (c) Administrator provides guidance to vendors on correcting rejected invoices via portal messaging | Vendor Portal Administrator | AP Supervisor | 1–2 hours/day |
| 5 | **Vendor query response**: vendors submit queries through portal messaging system; query categories include: (a) PO status inquiry ("when is my next order?"); (b) payment status inquiry ("has my invoice been paid?" — linked to W100); (c) GR discrepancy ("GR shows 90 units but I shipped 100"); (d) performance scorecard question ("why did my delivery score drop?"); (e) catalog update request ("new packaging size available"); (f) technical issue ("cannot upload invoice"). Administrator triages queries: procurement queries routed to Buyer, payment queries routed to AP Clerk, scorecard queries answered from W44 data, technical issues routed to IT (W48). Target response SLA: 4 hours during business days | Vendor Portal Administrator | Category Manager | 1–2 hours/day (~10–15 queries/day) |
| 6 | **Monthly portal content review**: Vendor Portal Administrator reviews and updates portal content — (a) vendor master data accuracy: cross-reference portal vendor list with W287 vendor master; flag vendors with mismatched TIN, business name, or payment terms; (b) document library: update templates (invoice template, delivery receipt template, credit note template) to ensure BIR compliance; (c) FAQ and help content: update based on recurring vendor queries; (d) price list and catalog synchronization: verify portal catalog matches ERP item master per W278; flag discrepancies; (e) vendor terms and conditions: update if payment terms or procurement policies have changed | Vendor Portal Administrator | Category Manager | 4–6 hours/month |
| 7 | **Quarterly portal analytics review**: Vendor Portal Administrator generates and presents portal analytics to Category Managers and Procurement Director — (a) portal adoption rate: % of active vendors who logged in at least once during the quarter; target: >80% for merchandise vendors; (b) PO acknowledgment rate: % of portal-distributed POs acknowledged within SLA; target: >90% within 48 hours; (c) invoice submission rate: % of invoices submitted via portal vs. email/paper; target: >70% portal-submitted; (d) dispute resolution time: average days from dispute initiation to resolution for portal-initiated disputes vs. non-portal disputes; (e) vendor satisfaction: feedback survey sent to top 100 vendors quarterly; (f) portal uptime and performance metrics (coordinated with IT per W380); (g) identification of vendors with zero portal logins in 90+ days — trigger re-onboarding outreach | Vendor Portal Administrator | Procurement Director | 3–4 hours/quarter (analytics preparation + presentation) |
| 8 | **Quarterly feature enhancement**: based on analytics review findings and vendor feedback, Vendor Portal Administrator submits enhancement requests to IT — (a) prioritized enhancement backlog (e.g., mobile-responsive portal design for vendors using smartphones, Filipino-language interface option, bulk invoice upload capability, real-time chat support integration); (b) IT evaluates feasibility and timeline per W132 change management; (c) UAT testing of new features with 5–10 pilot vendors before full rollout; (d) release notes communicated to all vendors via portal announcement and email | Vendor Portal Administrator / IT | Procurement Director | 2–3 hours/quarter (enhancement specification + UAT coordination) |

**Total time per month**: ~60–80 person-hours/month (daily monitoring ~2 hours/day × 22 days + monthly content review ~6 hours + quarterly activities ~6 hours amortized)

### System Touchpoints (W593 — Vendor Portal Content Management)

- Vendor self-service portal: account management, PO viewing/acknowledgment, invoice submission, GR status, performance scorecard visibility, catalog update submission, dispute initiation, messaging (PUR-027)
- ERP vendor master integration for account creation and data synchronization (W287, PUR-003)
- PO management module for PO distribution to portal (W2A)
- AP invoice processing for 3-way match validation and invoice reconciliation (W7, FIN-004)
- Vendor performance scorecard for score visibility (W44, PUR-012)
- Vendor statement reconciliation for payment status visibility (W100, FIN-006)
- Item master and catalog for product information synchronization (W278, MDM-003)
- IT helpdesk for vendor technical issues (W48)
- Change management for portal enhancements (W132)
- Alert and event management for portal uptime monitoring (W380)

### Pain Points / Risks

- **MSME vendor digital adoption gap**: ~60% of vendors are Philippine MSMEs with limited digital infrastructure — many still operate with paper-based processes, basic email, and smartphone-only internet access; portal adoption targets (>80%) are aggressive for this segment; mitigated by mobile-responsive portal design, Filipino-language support, in-person training at DCs, and phased feature rollout (start with PO acknowledgment, then invoices, then advanced features)
- **Invoice submission quality**: MSME vendors frequently submit invoices with BIR compliance errors (incorrect TIN format, missing OR number, wrong line-item details) that cause automated 3-way match failures and increase manual AP review workload; mitigated by portal invoice template with mandatory field validation, inline error messages, and vendor training
- **Portal system downtime affects vendor operations**: portal downtime during peak PO distribution or invoice submission periods (month-end, quarter-end) disrupts vendor workflows and forces manual fallback; mitigated by IT SLA of 99.5% uptime, scheduled maintenance windows outside business hours, and offline email/phone backup per W2A
- **Vendor master data drift between portal and ERP**: if W287 vendor master data governance is not rigorous, portal vendor information diverges from ERP (outdated payment terms, wrong TIN, incorrect business name), causing invoice matching failures and payment delays; mitigated by monthly content review (step 6) and system-level synchronization
- **Vendor query volume spikes during promotion periods**: during bi-monthly sale events and Christmas season, PO volumes increase ~30–50%, and vendor query volume increases proportionally — overwhelming the single Vendor Portal Administrator; mitigated by Buyer escalation support during peak periods and automated FAQ/chatbot for routine queries

### Staffing Implication

- **1 Vendor Portal Administrator**: dedicated role within the Procurement team; ~60–80 person-hours/month; this is a full-time responsibility combining portal operations, vendor training, and analytics. At current volumes (~800–1,000 vendors), this role is justified.
- **Buyer support**: ~30 min/day for PO follow-up with unacknowledged vendors; absorbed within existing Buyer duties (~10–12 buyers).
- **AP Clerk support**: ~30 min/day for invoice discrepancy resolution with vendors via portal; absorbed within existing AP team.
- **IT support**: portal technical issues consume ~2–4 hours/week of IT helpdesk time per W48; absorbed within existing IT capacity.
- **Future scaling**: at >1,200 vendors, consider adding a second Vendor Portal Administrator or upgrading to AI-assisted vendor query handling.

---

## W620. Vendor Due Diligence & Onboarding Site Visit Management

| Field | Detail |
|---|---|
| **Trigger** | New vendor identified for onboarding (per W36); annual due diligence for critical vendors |
| **Frequency** | Per new vendor onboarding; annual for top 50 vendors; biennial for next 100 |
| **Volume** | ~100-150 new vendor onboardings/year; ~50 annual site visits for critical vendors |
| **Owner** | Procurement Manager |
| **Participants** | Procurement Manager, Buyer, Quality Assurance Specialist, Finance Analyst, Category Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Vendor onboarding initiated (per W36); Buyer determines due diligence level: Tier A (new import vendor, > PHP 10M annual spend, private label supplier) → full due diligence including site visit; Tier B (> PHP 1M spend) → documentary due diligence; Tier C (< PHP 1M) → basic verification only | Buyer | Procurement Manager | 10 min |
| 2 | **Documentary due diligence (Tier B/C)**: Finance Analyst verifies vendor's business registration (SEC/DTI), tax compliance (BIR TIN, VAT registration), business permits, and financial health (audited financials or bank reference for Tier B); system validates TIN against BIR database | Finance Analyst | Procurement Manager | 30 min |
| 3 | **Full due diligence (Tier A)**: Buyer prepares site visit plan — factory/warehouse inspection checklist, product quality assessment, capacity verification, labor practices assessment, environmental compliance check; schedules visit with vendor | Buyer | Procurement Manager | 60 min |
| 4 | Site visit execution: Buyer and Quality Assurance Specialist conduct on-site inspection — (a) facility tour (production area, warehouse, quality lab), (b) production capacity assessment (equipment, workforce, shift patterns), (c) quality management system review (ISO certification, testing procedures), (d) inventory management observation, (e) labor practices assessment (safety equipment, working conditions per W213), (f) environmental compliance (waste disposal, emissions); document findings with photos | Buyer / QA Specialist | Procurement Manager | 4-8 hours |
| 5 | For import vendors: Buyer additionally verifies export licenses, customs compliance history, packaging and labeling standards, and logistics capabilities; checks for trade compliance (no sanctions, no forced labor indicators) | Buyer | — | 2 hours |
| 6 | For private label suppliers (per W129): Quality Assurance Specialist conducts extended factory audit per social compliance checklist (labor rights, child labor prevention, safety standards, environmental practices per W160); scores factory on 100-point scale; minimum score 70 to proceed | QA Specialist | Category Manager | 4 hours |
| 7 | Buyer compiles due diligence report with site visit findings, documentary verification results, and recommendation (approve, approve with conditions, reject); Procurement Manager reviews and approves or requests additional verification | Buyer | Procurement Manager | 60 min |
| 8 | If approved: vendor master created per W36 with due diligence score, site visit date, and next review date; system auto-schedules next due diligence cycle based on tier | Procurement Manager | — | 15 min |
| 9 | Annual: Procurement Manager reviews due diligence calendar; schedules site visits for vendors requiring annual re-assessment; prioritizes vendors with quality issues (per W110) or supply disruptions (per W558) | Procurement Manager | VP Merchandising | 4 hours/year |

### System Touchpoints
- ERP Procurement module: vendor master (per W287), due diligence tracking, site visit scheduling
- ERP Quality module: quality assessment scoring, compliance tracking
- ERP Finance module: vendor financial health verification, TIN validation
- Document management: due diligence reports, site visit photos, vendor certificates (per W255)
- Mobile app: site visit checklist, photo capture, scoring tool

### Pain Points / Risks
- **Vendor misrepresentation**: vendors may stage conditions for site visits; mitigated by unannounced visits for critical suppliers and cross-referencing with third-party audit reports
- **International site visit cost**: visiting overseas vendors (China, Taiwan, Indonesia) costs PHP 100-200K per trip; mitigated by engaging third-party inspection firms (SGS, Bureau Veritas) for initial assessment and reserving in-person visits for top 10 vendors
- **Due diligence bottleneck**: site visit requirement delays vendor onboarding by 2-4 weeks; mitigated by allowing provisional approval for Tier A vendors with site visit to follow within 60 days
- **Corruption risk**: vendor may attempt to influence site visit outcome; mitigated by two-person visit requirement and anti-bribery policy compliance (per W426)

### Staffing Implication
- **Buyer**: ~8 hours per site visit (including preparation and report) × ~50 visits/year = ~400 hours/year. Distributed across buying team (~5 buyers) = ~80 hours/buyer/year.
- **QA Specialist**: ~4 hours per factory audit × ~25 private label audits/year = ~100 hours/year. Dedicated role or shared with quality team.
- **Finance Analyst**: ~30 min per Tier B/C vendor verification × ~100 vendors/year = ~50 hours/year. Absorbed within existing role.

---

## W621. Vendor-Managed Inventory (VMI) Daily Performance Monitoring

| Field | Detail |
|---|---|
| **Trigger** | Start of business day; VMI data exchange scheduled execution; performance threshold breach |
| **Frequency** | Daily monitoring; weekly performance review; monthly vendor scorecard |
| **Volume** | ~300 SKUs from 12 VMI vendors; ~4 DCs; ~200 stores |
| **Owner** | VMI Coordinator (within Supply Planning team) |
| **Participants** | VMI Coordinator, Supply Planner, Buyer, vendor VMI analyst |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Morning: system executes daily VMI data exchange with 12 vendors — exports point-of-sale data, current inventory levels, and forecast data per SKU per location; imports vendor replenishment proposals | System | — | Automated |
| 2 | VMI Coordinator reviews data exchange status dashboard — confirms successful transmission for all 12 vendors; investigates failed or incomplete data feeds; coordinates with IT Integration Specialist for API issues | VMI Coordinator | — | 15 min |
| 3 | System auto-validates vendor replenishment proposals against business rules: (a) proposed quantity within min/max shelf stock parameters, (b) replenishment timing does not create overstock (> 4 weeks supply), (c) proposed items match active assortment, (d) pricing matches contracted rates | System | — | Automated |
| 4 | VMI Coordinator reviews auto-validation exceptions — approves proposals that exceed parameters by < 20% with documented justification; rejects proposals exceeding parameters by > 20%; returns to vendor with explanation | VMI Coordinator | Buyer | 20 min |
| 5 | System monitors VMI stock performance: (a) in-stock rate per VMI SKU (target ≥ 97%), (b) days of supply per SKU per location, (c) forecast accuracy (vendor's forecast vs. actual sales), (d) fill rate on vendor shipments, (e) lead time adherence | System | — | Automated |
| 6 | For SKUs below minimum stock threshold: system auto-alerts VMI Coordinator and vendor; VMI Coordinator verifies vendor is initiating expedited replenishment; if vendor response delayed > 24 hours, Buyer intervenes per vendor SLA | VMI Coordinator | Buyer | 10 min |
| 7 | Weekly: VMI Coordinator generates VMI performance dashboard — in-stock rate by vendor, fill rate, forecast accuracy, excess stock alerts, data quality score; shares with Buyer and Supply Planner | VMI Coordinator | Supply Planner | 30 min |
| 8 | Monthly: VMI data feeds into vendor scorecard (per W44); Buyer reviews VMI vendor performance in monthly vendor review meeting; discusses corrective actions for underperforming vendors; evaluates VMI SKU assortment for additions/removals | Buyer | Procurement Manager | 1 hour/vendor |
| 9 | Quarterly: VMI Coordinator and Supply Planner review VMI program effectiveness — total VMI SKUs, inventory turns for VMI vs. non-VMI SKUs, stockout reduction, working capital impact; recommends program expansion or contraction to Procurement Manager | VMI Coordinator | Procurement Manager | 4 hours |

### System Touchpoints
- ERP Supply Chain module: VMI data exchange, replenishment proposal validation, stock monitoring
- ERP Inventory module: real-time stock levels, days of supply, in-stock rate
- ERP Procurement module: vendor scorecard integration (per W44)
- Integration platform: EDI/API data exchange with 12 VMI vendors
- BI dashboard: VMI performance dashboard, vendor comparison, program analytics

### Pain Points / Risks
- **Data exchange failures**: API/EDI connectivity issues prevent timely data sharing, causing vendor to under- or over-replenish; mitigated by automated monitoring and IT escalation within 2 hours of detected failure
- **Vendor forecasting inaccuracy**: vendor's demand forecast may not account for Philippine-specific patterns (payday spikes, typhoon demand surges); mitigated by enriching vendor data with BuildRight's own forecast (per W31) and local event calendar
- **Overstock accumulation**: VMI vendors may oversupply to meet their own production targets; mitigated by max-stock parameter enforcement in Step 3 and excess stock return policy per vendor agreement
- **VMI vendor dependency**: critical SKUs exclusively managed by VMI create single-source risk; mitigated by maintaining 2-week safety stock buffer and qualified alternative vendor per W558

### Staffing Implication
- **VMI Coordinator**: ~30 min/day on monitoring + ~30 min/week reporting = ~4 hours/week. This is a dedicated role within Supply Planning team.
- **Buyer**: ~1 hour/month per VMI vendor on review meetings × 12 vendors = ~12 hours/month. Distributed across buying team.

---

## W631. Strategic Sourcing & Category Strategy

| Field | Detail |
|---|---|
| **Trigger** | Annual category review cycle or new category identification |
| **Frequency** | Quarterly per category; annual comprehensive review |
| **Volume** | ~20–25 category strategies maintained; 5–8 reviewed per quarter |
| **Owner** | VP Merchandising |
| **Participants** | Category Manager, Senior Buyer, FP&A Analyst, Supply Chain Planner |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Category Manager compiles total spend analysis by vendor, SKU, and sub-category from ERP analytics | Category Manager | VP Merchandising | 2 days/category |
| 2 | FP&A Analyst provides category gross margin trend, cost-to-serve analysis, and demand forecast | FP&A Analyst | VP Merchandising | 1 day |
| 3 | Supply Chain Planner provides vendor risk assessment (W491/W558 data), lead time analysis, and single-source dependency mapping | Supply Chain Planner | VP Merchandising | 1 day |
| 4 | Category Manager performs Kraljic portfolio analysis classifying each sub-category as Strategic, Leverage, Bottleneck, or Routine | Category Manager | VP Merchandising | 1 day |
| 5 | Team develops sourcing strategy per sub-category: single-source vs. multi-source, local vs. import, long-term contract vs. spot purchase, vendor consolidation or expansion targets | Senior Buyer | VP Merchandising | 1 day |
| 6 | VP Merchandising approves category sourcing strategy with documented rationale | VP Merchandising | COO | 0.5 day |
| 7 | Category strategy documented in ERP procurement module with vendor allocation targets, approved vendor list, and sourcing rules | Category Manager | VP Merchandising | 0.5 day |

### System Touchpoints
- Spend analytics module, vendor scorecard (W44), demand planning (W31), procurement parameter master

### Pain Points / Risks
- Incomplete spend data due to maverick purchasing; resistance from buyers accustomed to preferred vendor relationships; strategy execution gap without automated enforcement of approved vendor lists

### Time Estimate
- 5–6 days per category; ~20 days/quarter across 5 categories

---

## W632. Competitive Bidding & Tender Management

| Field | Detail |
|---|---|
| **Trigger** | Procurement requirement exceeding PHP 500,000 for non-blanket-PO categories; new vendor evaluation; contract renewal requiring re-tender |
| **Frequency** | ~15–25 tenders/year |
| **Volume** | ~3–5 active tenders at any time |
| **Owner** | Senior Buyer |
| **Participants** | Category Manager, VP Merchandising (approver), Legal (contract review), Quality (technical evaluation) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Senior Buyer prepares tender specification document: item descriptions, quantities, delivery schedule, quality standards, evaluation criteria, and terms | Senior Buyer | Category Manager | 2 days |
| 2 | Category Manager approves tender specification and evaluation matrix (weighted: price 40%, quality 25%, delivery 20%, financial stability 15%) | Category Manager | VP Merchandising | 0.5 day |
| 3 | Senior Buyer publishes RFQ to qualified vendors via vendor portal (minimum 3 vendors; 5 for strategic categories); sets response deadline (typically 14 business days) | Senior Buyer | Category Manager | 0.5 day |
| 4 | Senior Buyer receives and logs vendor responses; conducts bid opening with Category Manager witness; prepares bid tabulation summary | Senior Buyer | Category Manager | 1 day |
| 5 | Quality evaluates technical compliance (samples, specifications, certifications) for technically qualifying bidders | Quality representative | Category Manager | 3 days |
| 6 | Senior Buyer conducts commercial evaluation using weighted scoring matrix; identifies preferred and backup vendor | Senior Buyer | Category Manager | 1 day |
| 7 | Category Manager reviews evaluation, negotiates final terms with preferred vendor if needed (best-and-final-offer round if competition is close) | Category Manager | VP Merchandising | 1 day |
| 8 | VP Merchandising approves award for bids > PHP 1M; COO approves for bids > PHP 5M | VP Merchandising/COO | COO | 0.5 day |
| 9 | Senior Buyer communicates award and decline notifications; creates blanket PO (W2C) or standard PO (W2) per award outcome | Senior Buyer | Category Manager | 0.5 day |

### System Touchpoints
- Vendor portal for RFQ distribution and response collection, procurement module for bid tabulation and scoring, approval workflow for award authorization

### Pain Points / Risks
- Collusion among bidders in concentrated Philippine vendor market; insufficient qualified bidders for niche hardware categories; specification bias favoring incumbent vendor; lengthy legal review for non-standard contract terms

### Time Estimate
- 10–15 days per tender from specification to award

---

## W633. Purchase Price Variance (PPV) Analysis & Cost Management

| Field | Detail |
|---|---|
| **Trigger** | Monthly PPV report generation; triggered by vendor price increase notification |
| **Frequency** | Monthly analysis; quarterly comprehensive review |
| **Volume** | ~35,000 active SKUs monitored; ~500–800 SKUs with material variance monthly |
| **Owner** | FP&A Analyst |
| **Participants** | Category Manager, Senior Buyer, Cost Accountant |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System auto-generates PPV report comparing standard cost to actual PO cost per SKU per vendor for the period | System | FP&A Analyst | Automated |
| 2 | FP&A Analyst reviews PPV report filtering for material variances (> 3% or > PHP 50 per unit); categorizes as favorable or unfavorable | FP&A Analyst | Finance Manager | 1 day |
| 3 | FP&A Analyst performs root cause classification: vendor price increase, commodity market movement, FX impact on imports, negotiation gap, specification change, UOM error, or data entry error | FP&A Analyst | Finance Manager | 1 day |
| 4 | For commodity-exposed categories (cement, steel, copper wire, lumber), FP&A Analyst compares actual purchase prices against published commodity indices | FP&A Analyst | Finance Manager | 0.5 day |
| 5 | Category Manager reviews unfavorable PPV for top 50 SKUs by financial impact; develops action plan (renegotiate with vendor, seek alternative source per W631, adjust selling price, absorb margin impact) | Category Manager | VP Merchandising | 2 days |
| 6 | Cost Accountant assesses PPV impact on inventory valuation (WAC recalculation) and gross margin by category | Cost Accountant | Finance Manager | 1 day |
| 7 | Senior Buyer executes approved action plan (vendor renegotiation, source switch, PO amendment) | Senior Buyer | Category Manager | 3–5 days |
| 8 | FP&A Analyst updates standard costs quarterly based on PPV trends, commodity outlook, and FX forecast; submits for Finance Manager approval | FP&A Analyst | Finance Manager | 2 days |

### System Touchpoints
- Cost accounting module (standard vs. actual comparison), purchase history analytics, commodity price feed integration, inventory valuation module

### Pain Points / Risks
- Stale standard costs masking real cost increases; FX-driven import PPV distorting vendor performance assessment; commodity price volatility in Philippine construction materials market; resistance from merchandising to selling price increases that PPV demands

### Time Estimate
- Monthly: 4 days; quarterly standard cost update: additional 2 days

---

## W669. Vendor Contract Compliance Monitoring & Enforcement

| Field | Detail |
|---|---|
| **Trigger** | Monthly contract compliance review cycle; contract milestone dates |
| **Frequency** | Monthly monitoring; quarterly comprehensive review |
| **Volume** | ~150-200 active vendor contracts (blanket POs per W2C, annual supply agreements, service contracts) |
| **Owner** | Procurement Manager |
| **Participants** | Senior Buyer, Category Manager, AP Analyst, Legal Counsel |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System auto-generates contract compliance dashboard from active contracts: upcoming renewal dates (90/60/30-day alerts), pricing term adherence, volume commitment tracking (actual vs. committed), rebate threshold progress per W27, delivery performance against SLA per W44 | Senior Buyer | Procurement Manager | 2 hours |
| 2 | Review compliance exceptions: vendor billing above contract price, deliveries outside agreed lead times, quality failures per W110 CAPA, volume shortfalls below minimum commitment | Senior Buyer | Procurement Manager | 3 hours |
| 3 | Escalate material non-compliance: first offense → vendor notification with 15-day remediation period; repeat offense → formal meeting with vendor management; chronic non-compliance → contract termination review with Legal Counsel | Procurement Manager | VP Supply Chain | 2 hours |
| 4 | Cross-reference vendor invoices against contract pricing: flag line items where invoiced price exceeds contract price; auto-generate debit memo for overcharges per W244 | AP Analyst | Procurement Manager | 2 hours |
| 5 | Review volume commitment tracking: identify vendors where BuildRight is under-committing (risking unfavorable terms at renewal) or over-committing (excess inventory risk) | Category Manager | Procurement Manager | 2 hours |
| 6 | Quarterly: produce comprehensive contract compliance report for VP Supply Chain including compliance rate by vendor, financial impact of non-compliance, contract renewal calendar, renegotiation strategy for expiring contracts | Procurement Manager | VP Supply Chain | 1 day |
| 7 | Coordinate with Legal Counsel for contract amendments, renewals, and terminations per W62 review process | Procurement Manager | Legal Counsel | 3 hours |

### System Touchpoints
- Contract management module
- Vendor scorecard (W44)
- AP invoice matching
- Rebate tracking module
- Compliance alert engine

### Time Estimate
- Monthly: 1 day; quarterly comprehensive: 2 days

### Pain Points / Risks
- Contract terms buried in PDF documents not systematically tracked
- Volume commitment tracking across 5 entities and 200 stores
- Informal side agreements undermining contract governance
- Vendor consolidation reducing competitive leverage at renewal

### Staffing Implication
- Procurement Manager: ~1 day/month + 2 days/quarter. Absorbed within existing role.
- Senior Buyer: ~4 hours/month. Absorbed within existing role.

---

## W670. Supplier Emergency Onboarding & Rapid Activation

| Field | Detail |
|---|---|
| **Trigger** | Emergency procurement need (W60), supply disruption requiring alternative source (W558), or single-source vendor failure |
| **Frequency** | As needed; estimated 5-10 emergency activations per year |
| **Volume** | 1-3 vendors per activation event |
| **Owner** | Procurement Manager |
| **Participants** | Senior Buyer, AP Analyst, Quality Engineer, Legal Counsel, Finance Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Trigger event: supply disruption, emergency procurement need, or vendor failure; requesting party submits emergency vendor request with justification, required product/service, timeline urgency, and estimated spend | Category Manager / VP Supply Chain / Store Ops | Procurement Manager | 1 hour |
| 2 | Activate expedited onboarding track: compresses standard W36 onboarding (normally 2-4 weeks) to 3-5 business days | Procurement Manager | VP Supply Chain | 1 hour |
| 3 | Perform accelerated due diligence: TIN verification, business registration check (SEC/DTI), basic financial viability assessment, reference check (2 past customers); waives Tier B/C documentary requirements per W620 for emergency | Senior Buyer | Procurement Manager | 1 day |
| 4 | Perform abbreviated compliance check: sanctions screening, PEP check, basic anti-corruption screening per W656; waived: full site visit, social compliance audit | Legal Counsel | Procurement Manager | 4 hours |
| 5 | Approve temporary payment terms (COD or Net 15 initially; standard terms after full onboarding completion); set temporary credit exposure limit | Finance Manager | VP Finance | 2 hours |
| 6 | Create vendor master record with "Emergency - Provisional" status and 90-day full-activation deadline; provisional status restricts to designated emergency POs only | AP Analyst | Procurement Manager | 1 hour |
| 7 | Establish interim quality protocol: 100% inspection on first 3 shipments per PUR-016 before reverting to standard AQL sampling | Quality Engineer | Procurement Manager | 2 hours |
| 8 | Place emergency PO; system tracks emergency PO performance separately for post-event review | Senior Buyer | Procurement Manager | 2 hours |
| 9 | Within 90 days: ensure full vendor onboarding completion per W620 Tier A/B requirements; if vendor fails full due diligence, initiate transition to qualified alternative | Procurement Manager | VP Supply Chain | 1 day |
| 10 | Post-event: conduct root cause analysis of supply disruption and emergency activation; update approved vendor list and sourcing strategy per W631 | Procurement Manager | VP Supply Chain | 1 day |

### System Touchpoints
- Vendor onboarding module
- Vendor master with provisional status
- PO module
- Quality inspection module
- Sanctions screening tool

### Time Estimate
- Emergency activation: 3-5 business days; post-event review: 2 days

### Pain Points / Risks
- Balancing speed with due diligence rigor
- Provisional vendor quality risk
- Emergency pricing premium
- Post-emergency transition to standard vendor without supply gap

### Staffing Implication
- Procurement Manager: ~4 hours/activation. Absorbed within existing role.
- Senior Buyer: ~2 days/activation. Absorbed within existing roles.

---

## W671. Commodity Price Monitoring & Procurement Strategy

| Field | Detail |
|---|---|
| **Trigger** | Weekly commodity price review; material price movement alerts |
| **Frequency** | Weekly monitoring; monthly strategy review; quarterly sourcing optimization |
| **Volume** | 6 commodity categories: cement, steel/rebar, copper wire, lumber, paint resins/titanium dioxide, PVC/pipe fittings; ~40% of COGS exposed to commodity pricing |
| **Owner** | Category Manager |
| **Participants** | Senior Buyer, FP&A Analyst, VP Supply Chain |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Pull weekly commodity price data from published Philippine market indices: cement (per bag/bulk), steel rebar (per kg), copper (LME + Philippine premium), lumber (per board foot local species), paint raw materials (titanium dioxide, resins), PVC resin; compare against BuildRight's actual PO prices per W633 PPV analysis | FP&A Analyst | Category Manager | 2 hours |
| 2 | Review price trend dashboard: current price vs. 4-week average, 12-month range, and BuildRight contract price; system flags commodities with > 5% weekly movement or > 15% quarterly movement | Category Manager | VP Supply Chain | 1 hour |
| 3 | For commodities in upward trend: assess forward buying opportunity considering storage capacity at 4 DCs, working capital impact, and demand forecast per W31; calculate optimal forward buy quantity | Category Manager | VP Supply Chain | 2 hours |
| 4 | For commodities in downward trend: evaluate spot purchase opportunity vs. existing contract commitments; identify contract buy-out or renegotiation opportunities | Category Manager | VP Supply Chain | 2 hours |
| 5 | Execute commodity procurement strategy: forward contracts for 3-6 month coverage on volatile commodities, spot purchasing for favorable dips, blanket PO adjustments per W2C for stable commodities | Senior Buyer | Category Manager | 4 hours |
| 6 | Monthly: produce commodity market briefing for VP Supply Chain including price outlook (3-month forward), procurement strategy recommendation, margin impact forecast per W85, and hedging consideration per W80 (for import commodities with FX exposure) | Category Manager | VP Supply Chain | 1 day |
| 7 | Quarterly: VP Supply Chain conducts commodity sourcing optimization review: vendor diversification, local vs. import mix, alternative material evaluation, long-term contract structuring | VP Supply Chain | COO | 2 days |

### System Touchpoints
- Commodity price feed integration
- PPV analytics (W633)
- Demand planning module
- Blanket PO management
- Margin analysis module

### Time Estimate
- Weekly: 2 hours; monthly strategy: 1 day; quarterly optimization: 2 days

### Pain Points / Risks
- Philippine cement/steel cartel behavior limiting true market pricing
- Limited local alternatives for import commodities
- Forward buy storage constraints at DCs
- Working capital tied up in commodity inventory
- Construction seasonality mismatching procurement timing

### Staffing Implication
- Category Manager: ~2 hours/week + 1 day/month + 2 days/quarter. Absorbed within existing role.
- FP&A Analyst: ~2 hours/week data pull. Absorbed within existing role.

---

## W672. VMI Quarterly Business Review & Program Optimization

| Field | Detail |
|---|---|
| **Trigger** | Quarterly VMI program review cycle |
| **Frequency** | Quarterly business review with each VMI vendor; annual program optimization |
| **Volume** | 12 VMI vendors covering ~300 SKUs; ~PHP 500M-1B annual VMI spend |
| **Owner** | Procurement Manager |
| **Participants** | Senior Buyer, Category Manager, DC Operations Manager, VMI Vendor Representative |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates quarterly VMI program performance report per vendor: in-stock rate (target ≥ 97%), forecast accuracy (target ≥ 85%), fill rate, days of supply, lead time adherence, inventory turns, write-offs/damages, and sell-through vs. forecast | Senior Buyer | Procurement Manager | 3 hours |
| 2 | Prepare vendor-specific QBR package: performance scorecard with trend (vs. prior quarter, vs. same quarter last year), exception summary from daily monitoring (W621), upcoming seasonal demand changes, and new product introductions | Senior Buyer | Procurement Manager | 3 hours |
| 3 | Review VMI pricing compliance: actual invoice prices vs. contracted terms, rebate accrual status per W27, and any PPV per W633 | Category Manager | Procurement Manager | 2 hours |
| 4 | Provide operational feedback: delivery reliability, ASN accuracy, packaging quality, putaway efficiency, and any receiving exceptions | DC Operations Manager | Procurement Manager | 2 hours |
| 5 | Conduct QBR meeting with VMI vendor representative: review performance, discuss improvement opportunities, address recurring exceptions, and align on upcoming demand changes | Procurement Manager | VP Supply Chain | 2 hours |
| 6 | Document joint action items: vendor commits to specific improvements (e.g., increase safety stock for seasonal items, improve forecast accuracy by 5%); BuildRight commits to information sharing improvements (e.g., more granular demand data, earlier promotional communication) | Procurement Manager | Procurement Manager | 1 hour |
| 7 | Evaluate VMI program holistically: compare VMI performance vs. non-VMI procurement for same categories; assess total cost of ownership (inventory carrying cost, ordering cost, stockout cost); recommend program expansion, modification, or termination per vendor | Procurement Manager | VP Supply Chain | 4 hours |
| 8 | Annual: VP Supply Chain reviews VMI program strategy: vendor selection criteria, SKU eligibility, program expansion roadmap, technology integration improvements | VP Supply Chain | COO | 2 days |

### System Touchpoints
- VMI performance dashboard
- Vendor scorecard (W44)
- Demand planning module
- AP invoice matching
- Inventory analytics

### Time Estimate
- Per vendor QBR: 2-3 hours preparation + 1-2 hour meeting; quarterly program review: 1 day; annual optimization: 2 days

### Pain Points / Risks
- VMI vendor performance inconsistency across 4 DCs
- Demand forecast sharing accuracy
- VMI inventory valuation and ownership boundaries
- Vendor resistance to performance improvement commitments

### Staffing Implication
- Procurement Manager: ~2 days/quarter for 12 vendor QBRs + 1 day program review + 2 days annual. Absorbed within existing role.

---

## W705. Vendor Self-Service Portal Operations & Supplier Collaboration

| Field | Detail |
|---|---|
| **Trigger** | Vendor onboarding completion per W36; ongoing vendor portal usage; vendor inquiry or issue |
| **Frequency** | Continuous portal operations; daily vendor interactions; monthly usage analytics review |
| **Volume** | ~800-1,000 active vendors; ~200-300 vendor portal logins/day; ~5,000-10,000 PO acknowledgments, ASN submissions, and invoice uploads per month |
| **Owner** | Procurement Manager |
| **Participants** | Vendor Portal Administrator (IT), Buyers, AP Clerks, Vendors, Helpdesk |

### Background

BuildRight works with 800-1,000 vendors (60% local, 40% import). The vendor self-service portal enables suppliers to view POs, submit invoices, update product information, check payment status, and communicate with Buyers — reducing manual email and phone communication and improving data accuracy. This workflow manages the day-to-day operations of the vendor portal, vendor access management, and issue resolution.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Portal access provisioning**: upon vendor onboarding completion per W36: (a) Vendor Portal Administrator creates vendor portal account: unique login, role-based access (view-only vs. transactional), entity scope (which BuildRight entities they supply); (b) Vendor designated contact receives activation email with setup instructions and portal user guide; (c) for vendors without reliable internet access (common for small Philippine suppliers): provide alternative channel (email-based PO acknowledgment and invoice submission with manual AP entry) | Vendor Portal Administrator | Procurement Manager | 30 min per vendor |
| 2 | **Daily portal operations**: (a) system pushes new Purchase Orders to vendor portal dashboard; (b) vendor acknowledges PO with confirmed quantities and delivery dates, or submits modification request (partial quantity, revised delivery date); (c) Buyers receive vendor acknowledgments and respond to modification requests; (d) vendor uploads shipping documentation (ASN — Advanced Shipping Notice, bill of lading, packing list) upon shipment; (e) vendor uploads invoices for delivered goods; (f) AP matches vendor invoice to PO and goods receipt per W7 three-way match | Vendor / Buyer / AP Clerk | Procurement Manager | Continuous |
| 3 | **Vendor self-service functions**: portal enables vendors to: (a) view PO status and delivery requirements; (b) submit invoices electronically (reducing manual AP data entry); (c) check payment status and payment schedule; (d) update vendor master data (contact information, banking details per W508 with approval workflow); (e) access product quality feedback and performance scorecard per W706; (f) submit new product proposals to Merchandising per W1; (g) view contract terms and upcoming renewals per W688; (h) download settlement and remittance advice | Vendor | Vendor Portal Administrator | Self-service |
| 4 | **Portal issue resolution**: when vendors report portal issues: (a) Vendor Portal Administrator provides first-level support (password reset, browser compatibility, upload format guidance); (b) for technical issues (portal downtime, data sync errors, upload failures): escalate to IT Helpdesk per W48 with priority classification; (c) for process issues (PO not visible, incorrect quantities, payment status discrepancy): route to Buyer or AP Clerk for resolution; (d) track vendor issues and resolution time in support log | Vendor Portal Administrator | IT Director | 15-60 min per issue |
| 5 | **Vendor banking detail change verification**: when a vendor requests banking detail change via portal (critical fraud risk): (a) system blocks banking detail change pending verification; (b) AP Clerk contacts vendor through independently verified contact details (not contact info from the portal request) to confirm change; (c) AP Clerk verifies change with vendor's authorized signatory; (d) only after verbal verification: AP Clerk approves banking detail change in vendor master per W508; (e) all changes logged with audit trail for fraud prevention per W656 ABAC compliance | AP Clerk | Finance Manager | 30-60 min per change |
| 6 | **Monthly portal analytics**: Vendor Portal Administrator produces monthly usage report: (a) active vendor accounts vs. total registered; (b) portal login frequency by vendor; (c) PO acknowledgment rate via portal (target: >80%); (d) electronic invoice submission rate (target: >60%); (e) ASN submission compliance rate; (f) top support issues and resolution time; (g) portal availability and performance metrics (target: 99.5% uptime); report shared with Procurement Manager and IT Director | Vendor Portal Administrator | Procurement Manager | 2 hours/month |
| 7 | **Quarterly vendor portal training**: for new vendors or vendors with low portal adoption: (a) schedule 30-minute virtual training session; (b) cover: portal navigation, PO acknowledgment, invoice upload, ASN submission, payment status inquiry, banking detail change process; (c) provide updated user guide (English and Filipino versions); (d) track training completion per vendor | Vendor Portal Administrator | Procurement Manager | 30 min per session |

### System Touchpoints

- Vendor self-service portal (PUR-015)
- ERP PO management module (PO push to portal, acknowledgment capture)
- AP invoice matching module per W7 (electronic invoice capture)
- Vendor master data management per W508 (vendor self-service updates with approval workflow)
- ASN module for shipping documentation capture
- Payment status inquiry module
- IT Helpdesk integration per W48
- Fraud prevention controls per W656

### Pain Points / Risks

- **Vendor digital readiness**: many small Philippine suppliers lack reliable internet access or digital literacy for portal usage; paper-based and email-based alternatives must remain available, creating dual-channel management overhead
- **Fraud risk on banking detail changes**: vendor impersonation via portal to redirect payments is a known attack vector; strict verification process per step 5 is essential
- **Portal adoption rate**: despite training efforts, some vendors may default to email and phone communication; Buyer must reinforce portal usage by routing all PO inquiries back to the portal
- **Data quality**: vendor-uploaded invoices may not match PO format requirements (wrong unit of measure, incorrect item codes), causing AP matching failures and manual intervention

### Staffing Implication

- **Vendor Portal Administrator** (1 FTE within IT or Procurement): ~4-6 hours/day on portal support and operations. Dedicated role recommended at current vendor volume (~800-1,000 vendors).
- **Buyers**: ~15-30 min/day reviewing portal acknowledgments and responding to vendor inquiries. Absorbed within existing roles.
- **AP Clerks**: reduced manual data entry as vendors submit invoices electronically; absorbed within existing team.

### Time Estimate

- Portal provisioning: 30 min per vendor
- Daily operations: continuous
- Issue resolution: 15-60 min per issue
- Monthly analytics: 2 hours
- Quarterly training: 30 min per session

---

## W706. Supplier Performance Scorecard & Quarterly Business Review

| Field | Detail |
|---|---|
| **Trigger** | Quarterly review calendar; annual vendor classification review; significant vendor performance issue; vendor escalation |
| **Frequency** | Quarterly scorecards and QBRs for top 100 vendors; annual comprehensive review for all 800-1,000 vendors; monthly monitoring for critical vendors |
| **Volume** | ~100 QBRs/quarter (top vendors by spend); ~800-1,000 annual scorecards; ~20-30 critical vendors with monthly monitoring |
| **Owner** | Procurement Manager |
| **Participants** | Senior Buyer, Category Manager, DC Operations Manager, Quality Inspector, Finance Analyst, Sustainability Lead (for top vendors), VP Supply Chain (for strategic vendors) |

### Background

W44 covers vendor master data and general vendor management. W669 covers vendor contract compliance monitoring. W672 covers VMI quarterly reviews. However, no single workflow covers a comprehensive, structured supplier performance scorecard that aggregates all dimensions of vendor performance — quality, delivery, cost, service, sustainability — and drives quarterly business reviews (QBRs) for systematic vendor relationship management. This workflow provides a unified vendor performance framework applicable across all 800-1,000 vendors with depth proportional to vendor importance.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Scorecard framework maintenance**: Procurement Manager maintains vendor scorecard framework with weighted KPIs: (a) Quality (30% weight): defect rate per W110, quality inspection pass rate per W681, number of quality-related returns per W599/W88, corrective action closure rate; (b) Delivery (30% weight): on-time delivery rate (target: ≥95%), lead time accuracy, ASN accuracy, fill rate on POs; (c) Cost (20% weight): purchase price variance (PPV) per W633, cost competitiveness vs. market benchmarks, invoice accuracy (reducing AP matching exceptions per W7); (d) Service (10% weight): PO acknowledgment speed, responsiveness to inquiries, portal adoption per W705, flexibility on rush orders; (e) Sustainability (10% weight): ethical sourcing score per W195, environmental compliance, sustainability audit findings; (f) weighting adjusted by vendor category: commodity vendors → higher Cost weight; specialty vendors → higher Quality weight | Procurement Manager | VP Supply Chain | 1-2 days/year on framework maintenance |
| 2 | **Quarterly scorecard generation**: system auto-generates quarterly scorecard for top 100 vendors (by spend): (a) pull data from ERP: delivery metrics from PO/GR module, quality metrics from W110/W681 inspection records, cost metrics from AP/PUR modules, service metrics from vendor portal W705, sustainability metrics from W195 audit records; (b) calculate weighted score per vendor: 90-100 = Preferred, 75-89 = Approved, 60-74 = Conditional, <60 = Probation; (c) compare to prior quarter and same quarter prior year for trend analysis; (d) system auto-flags vendors with score change >10 points (positive or negative) for Buyer review | System / Senior Buyer | Procurement Manager | Automated generation + 2-3 hours review |
| 3 | **Vendor classification review**: quarterly, Procurement Manager reviews vendor classification based on scorecard: (a) **Preferred** vendors (score 90+): prioritize for volume allocation, consider for expanded SKU range, include in strategic partnership discussions; (b) **Approved** vendors (75-89): standard business relationship, identify improvement opportunities; (c) **Conditional** vendors (60-74): issue formal performance improvement notice, increase quality inspection frequency per W681, reduce volume allocation; (d) **Probation** vendors (<60): 90-day corrective action plan with specific targets, if not met → vendor de-listing per W36; (e) classification changes communicated to vendor via Buyer and documented in vendor master per W508 | Procurement Manager | VP Supply Chain | 4-6 hours/quarter |
| 4 | **QBR preparation**: for top 100 vendors, Senior Buyer prepares QBR package: (a) vendor scorecard with trend and detailed KPI breakdown; (b) spend analysis: total spend by category, spend trend, share of BuildRight's category spend; (c) contract compliance summary per W669; (d) quality incident summary and open corrective actions per W110; (e) upcoming demand forecast for vendor's categories (new store openings per W702, seasonal demand per W32); (f) action items from prior QBR and closure status | Senior Buyer | Procurement Manager | 2-3 hours per QBR |
| 5 | **QBR meeting**: Procurement Manager (or Senior Buyer for smaller vendors) conducts QBR with vendor: (a) present scorecard results and discuss each KPI dimension; (b) share BuildRight's forward demand outlook; (c) discuss vendor's capacity and investment plans; (d) negotiate improvement targets for underperforming KPIs; (e) document joint action items with owners and deadlines; (f) for strategic vendors (top 20 by spend): VP Supply Chain participates in QBR | Procurement Manager / Senior Buyer | VP Supply Chain | 1-2 hours per QBR |
| 6 | **Annual vendor rationalization**: annually, Procurement Manager and Category Managers conduct vendor rationalization: (a) review vendor portfolio: total active vendors by category, vendor overlap (multiple vendors for same SKU), vendor concentration risk; (b) identify consolidation opportunities: reduce vendor count where multiple vendors supply same category without differentiation; (c) identify sole-source risks: categories with single vendor — develop backup sourcing per W670 emergency onboarding; (d) approve new vendor additions and de-listings for next year; (e) present rationalization plan to VP Supply Chain and VP Merchandising for approval | Procurement Manager / Category Managers | VP Supply Chain | 1 week/year |
| 7 | **Vendor development program**: for Preferred and strategic vendors: (a) Procurement Manager identifies joint development opportunities: vendor-managed inventory expansion per W672, collaborative forecasting, early supplier involvement in new product development per W1, sustainability improvement per W195; (b) fund joint improvement projects (e.g., vendor packaging optimization to reduce DC handling time, vendor investment in quality testing equipment); (c) track development project outcomes and ROI | Procurement Manager | VP Supply Chain | 2-4 hours/quarter per strategic vendor |

### System Touchpoints

- Vendor scorecard engine with configurable KPI weights (PUR-016)
- ERP data feeds: PO/GR, AP, quality inspection W110/W681, returns W599/W88
- Vendor portal analytics per W705
- Sustainability audit records per W195
- Contract compliance data per W669
- Vendor master classification per W508
- Demand planning integration per W31
- QBR meeting documentation per W255
- Vendor rationalization analytics dashboard

### Pain Points / Risks

- **Data completeness for scorecard**: quality metrics rely on inspection data per W681/W110; if inspections are not consistently documented, quality scores may be inaccurate
- **Vendor resistance to scoring**: vendors may dispute unfavorable scores, especially if they believe the data is incomplete or the methodology is unfair; transparent scoring criteria and data sharing via portal per W705 mitigates this
- **QBR resource intensity**: 100 QBRs/quarter at 1-2 hours each plus 2-3 hours preparation = 300-500 hours/quarter; Procurement team capacity may be strained; consider tiered approach (full QBR for top 20, abbreviated for next 80)
- **Scorecard gaming**: vendors may optimize for scorecard metrics at the expense of unmeasured dimensions (e.g., meeting on-time delivery by shipping partial quantities)

### Staffing Implication

- **Procurement Manager**: ~2-3 days/quarter on scorecard review and QBRs. Absorbed within existing role.
- **Senior Buyers**: ~2-3 hours per QBR × ~25 QBRs each/quarter = ~50-75 hours/quarter per Senior Buyer. Absorbed within existing roles.
- **Category Managers**: ~4-6 hours/quarter on vendor rationalization input. Absorbed within existing roles.
- **No incremental headcount**.

### Time Estimate

- Framework maintenance: 1-2 days/year
- Quarterly scorecard review: 2-3 hours
- Per QBR: 2-3 hours preparation + 1-2 hours meeting
- Vendor classification review: 4-6 hours/quarter
- Annual rationalization: 1 week

---

## W760. Vendor-Specific Commodity Price Index Tracking & Procurement Trigger Management

| Field | Detail |
|---|---|
| **Trigger** | Weekly commodity price index update; or daily price alert for volatile commodities |
| **Frequency** | Weekly review; daily monitoring for volatile commodities |
| **Volume** | ~50 key commodity SKUs tracked (cement, steel rebar, lumber, copper wire, PVC pipes, plywood) |
| **Owner** | Procurement Manager (Strategic Sourcing) |
| **Participants** | Procurement Manager, Category Manager, FP&A, CFO (approval for forward buys) |

### Background
Key building materials (cement, steel, lumber, copper) have volatile commodity prices driven by global markets, exchange rates, and local supply conditions. BuildRight Depot's procurement team tracks commodity price indices to optimize purchase timing — buying forward when prices are low and deferring when prices are high. This workflow manages the systematic tracking, alert, and procurement decision process.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Commodity basket definition — Category Manager defines commodity basket per category: primary commodity (e.g., Portland cement), price benchmark (e.g., PH cement wholesale price index), weight in category COGS, and price thresholds for action | Category Manager | Procurement Manager | 8 hours/quarter |
| 2 | Price index monitoring — System automatically pulls weekly commodity price indices from configured sources (DTI price monitoring, Philippine Steel Institute, international lumber futures via API); updates price dashboard | System | — | Automated |
| 3 | Price alert generation — System compares current index against configured thresholds: (a) Green (within 5% of 90-day average), (b) Amber (5–15% deviation — review recommended), (c) Red (> 15% deviation — action required) | System | — | Automated |
| 4 | Weekly commodity review — Procurement Manager reviews commodity dashboard; for Amber/Red alerts: analyzes trend, driver (supply disruption, seasonal, currency), and forecast direction | Procurement Manager | Category Manager | 1 hour/week |
| 5 | Forward buy decision — If price is trending up and current price is favorable: Procurement Manager prepares forward buy proposal: quantity, value, storage capacity check (W584), cash flow impact (W589); presents to CFO for approval | Procurement Manager | CFO | 2 hours |
| 6 | Forward buy execution — If approved: system generates forward purchase order (W2C blanket PO or W2B import PO); coordinates with warehouse for storage capacity planning (W652 seasonal surge) | Procurement Manager | Warehouse Manager | Per W2 |
| 7 | Price decrease deferral — If price is trending down: Procurement Manager instructs buyers to purchase minimum quantities only; monitors for further decrease before committing to larger orders | Procurement Manager | — | Ongoing |
| 8 | Quarterly strategy review — Quarterly: Procurement Manager presents commodity strategy outcomes to leadership: savings achieved, missed opportunities, market outlook, and recommended strategy adjustments | Procurement Manager | VP Merchandising | 4 hours/quarter |

### System Touchpoints
- Commodity price index integration via API (DTI, industry associations, international futures)
- Price alert engine with configurable thresholds and trend analysis
- W2C blanket PO / W2B import PO — forward buy order generation
- W85 product costing — commodity price impact on margin analysis
- W312 replenishment parameters — safety stock override during forward buy
- W584/W652 warehouse capacity — storage capacity check for forward buy quantities
- W589 cash flow forecast — forward buy cash flow impact assessment
- W633 PPV analysis — purchase price variance tracking against commodity benchmarks

### Pain Points / Risks
- Price forecast accuracy — commodity markets are inherently unpredictable; forward buys based on incorrect forecasts can lock in higher prices
- Storage capacity constraints — forward buying large quantities of bulky building materials (cement, lumber) requires significant warehouse space that may not be available
- Cash flow impact — large forward buys tie up working capital; if prices subsequently drop further, the opportunity cost compounds
- Vendor relationship tension — switching vendors based on price may damage long-term relationships that provide supply security during shortages
- Exchange rate compounding — imported commodities (steel, copper) are doubly exposed to commodity price and USD/PHP exchange rate movements

### Time Estimate
Weekly review: 1 hour. Forward buy analysis: 2 hours per decision. Quarterly review: 4 hours. Total monthly: ~12 hours.

### Staffing Implication
Absorbed within existing Procurement Manager and Category Manager roles. 1 Procurement Manager (Strategic Sourcing) oversees commodity basket. No incremental headcount at current scale.

---

## W761. Supplier Innovation & New Product Introduction Collaboration Processing

| Field | Detail |
|---|---|
| **Trigger** | Vendor proposes new product or technology; or BuildRight identifies innovation opportunity during W624 competitor visits or W130 competitive intelligence |
| **Frequency** | Monthly collaboration meetings; ad-hoc proposals |
| **Volume** | ~10–20 active supplier innovation projects at any time |
| **Owner** | Category Manager |
| **Participants** | Category Manager, Procurement Manager, Merchandising Director, Vendor Innovation Team, Quality (W150) |

### Background
Hardware and home improvement retail is driven by product innovation — new power tool technologies, eco-friendly building materials, smart home integration, and DIY-friendly solutions. BuildRight Depot collaborates with key suppliers on new product development, exclusive products, and market-first introductions that differentiate it from competitors and drive margin.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Innovation opportunity identification — Source: (a) vendor proposal during JBP meeting (W155), (b) competitor product gap from W624/W130, (c) customer request trend from W507/W156 CDP, (d) industry trade show intelligence | Category Manager | Merchandising Director | Ongoing |
| 2 | Business case development — Category Manager prepares business case: (a) market size and growth, (b) competitive landscape, (c) BuildRight differentiation potential, (d) estimated volume and margin, (e) investment required (listing fee, display, training) | Category Manager | — | 8 hours |
| 3 | Vendor collaboration meeting — Category Manager meets with vendor innovation team: (a) review product specifications, (b) discuss exclusivity or launch window, (c) agree on sampling and testing plan (W625), (d) negotiate margin and promotional support (W513) | Category Manager | Vendor | 2 hours |
| 4 | Product testing & certification — New product undergoes quality testing per W625 (lab testing) and regulatory certification (W447 DTI-BPS, W479 FDA, W467 FPA as applicable) | Quality Team | Category Manager | 2–8 weeks |
| 5 | Pilot store selection — Category Manager selects 10–20 pilot stores based on: (a) customer demographics, (b) department sales volume, (c) planogram space availability (W314), (d) store manager capability | Category Manager | Merchandising Director | 4 hours |
| 6 | Pilot execution — Execute pilot per W64 (new product pilot): product placement, associate training (W51), promotional activation (W13), and 30-day performance monitoring | Category Manager | Store Operations | Per W64 |
| 7 | Performance review & rollout decision — Category Manager reviews pilot results: sales vs. target, margin, customer feedback (W608), associate feedback; recommends: (a) full rollout per W564, (b) extended pilot, or (c) discontinue | Category Manager | Merchandising Director | 4 hours |
| 8 | Annual innovation review — Merchandising Director presents annual innovation portfolio: products launched, success rate, revenue contribution, and innovation pipeline for next year | Merchandising Director | CEO | 4 hours/year |

### System Touchpoints
- Innovation opportunity tracker — pipeline management from proposal to launch
- W155 JBP collaboration — vendor meeting scheduling and documentation
- W625 product quality testing — lab testing request and result tracking
- W64 new product pilot — pilot store selection and execution
- W564 NPI full rollout — national launch execution
- W156 CDP — customer demand signal data
- W130/W624 competitive intelligence — market gap identification
- W314 planogram master — shelf space availability for new products
- W513 vendor-funded promotional activity — launch promotional support
- W680 supply chain cost analysis — logistics feasibility assessment

### Pain Points / Risks
- Innovation pipeline leakage — many proposals stall between business case and pilot due to competing priorities; without systematic pipeline management, opportunities evaporate
- Pilot store bias — selected pilot stores may be unrepresentative of chain-wide performance potential; results may over- or under-estimate national demand
- Speed-to-market — competitor may launch similar product during BuildRight's extended testing period; time-to-market must balance quality assurance with speed
- Vendor dependency — exclusive innovation partnerships create single-source dependency; if vendor cannot scale, BuildRight cannot fulfill national demand
- Margin erosion on innovation — new products require investment (listing fees, displays, training, marketing) that may not be recouped if the product fails

### Time Estimate
Per innovation project: business case (8 hours) + vendor meeting (2 hours) + pilot review (4 hours) = 14 hours. Monthly pipeline management: ~8 hours. Annual review: 4 hours.

### Staffing Implication
Absorbed within existing Category Manager and Merchandising team. Each Category Manager manages 1–2 active innovation projects alongside routine category management. No incremental headcount.

---

## W788. Vendor New Product Submission Review & Evaluation Processing

| Field | Detail |
|---|---|
| **Trigger** | Vendor submits new product proposal; or procurement identifies product gap per W679 assortment review |
| **Frequency** | Weekly; ~10-15 new product submissions per week |
| **Volume** | ~500-750 new product evaluations per year; ~100-150 advance to trial |
| **Owner** | Category Manager |
| **Participants** | Category Manager, Procurement Analyst, Quality Engineer (W150), Merchandising Director, Vendor |

### Background
Vendors continuously propose new products for BuildRight Depot's assortment — new tools, building materials, paint formulations, smart home devices, and eco-friendly alternatives. While W761 covers supplier innovation collaboration and W564 covers new product rollout, this workflow addresses the initial intake, screening, and evaluation of vendor product submissions — the funnel that determines which products advance to quality testing (W625), pilot store testing (W64), and potentially full rollout (W564). With ~500-750 submissions per year and only ~20-30% advancing, efficient evaluation is critical for assortment freshness without overwhelming the organization.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Product submission intake**: Vendor submits product via W705 vendor portal or direct to Category Manager: (a) product description and specifications, (b) pricing (SRP, wholesale price, volume discounts), (c) minimum order quantity and lead time, (d) product certifications (DTI-BPS ICC/SOC per W447, FDA per W479), (e) product images and marketing materials, (f) competitive advantage statement | Vendor | — | Vendor effort |
| 2 | **Initial screening**: Category Manager screens against criteria: (a) category fit — does product belong in BuildRight assortment per W679 assortment strategy, (b) price positioning — within BuildRight's price architecture (budget, mid, premium per W107), (c) margin potential — meets category margin floor per FIN-026, (d) vendor status — existing approved vendor per W36 or new vendor requiring onboarding, (e) regulatory readiness — certifications available or obtainable per W447/W479 | Category Manager | — | 15 min/submission |
| 3 | **Product gap analysis**: Procurement Analyst evaluates: (a) does BuildRight already carry a similar product? if yes — is new product differentiated enough per W279 substitution rules, (b) does this fill an identified assortment gap per W679 quarterly review, (c) competitive intelligence — do competitors carry this product per W624, (d) customer demand signals — W507 complaint analysis, W563 ecommerce search queries, W156 CDP insights | Procurement Analyst | Category Manager | 30 min |
| 4 | **Go/No-Go decision**: Category Manager decides: (a) Advance to evaluation — product passes initial screening and fills gap, (b) Request more information — promising but incomplete submission, (c) Decline — does not meet criteria; provide constructive feedback to vendor via W705 | Category Manager | — | 10 min |
| 5 | **Product evaluation**: For products advancing: (a) Quality Engineer evaluates: (i) request sample from vendor, (ii) perform quality testing per W625, (iii) verify regulatory certifications, (iv) assess packaging and labeling compliance; (b) Category Manager evaluates: (i) price competitiveness vs. existing alternatives, (ii) margin analysis per FIN-026, (iii) initial volume estimate based on category benchmarks, (iv) planogram space requirement per W314; (c) Supply Chain evaluates: (i) vendor reliability per W44 scorecard if existing vendor, (ii) lead time feasibility, (iii) import/local sourcing logistics per W144 | Quality Engineer / Category Manager | Merchandising Director | 2-5 days elapsed |
| 6 | **Evaluation summary and recommendation**: Category Manager prepares evaluation summary: (a) product strengths and concerns, (b) quality test results, (c) financial analysis (projected margin, volume, annual revenue), (d) recommendation: pilot per W64, direct to assortment (if established vendor), or decline with reason | Category Manager | — | 1 hour |
| 7 | **Merchandising Director approval**: Merchandising Director reviews: (a) strategic fit, (b) financial viability, (c) resource requirements (planogram space, training, display), (d) approves or defers to next assortment review per W679 | Merchandising Director | — | 15 min |
| 8 | **Vendor communication**: (a) Approved: communicate next steps (pilot timeline, initial order, listing requirements per W252), (b) Declined: provide constructive feedback to vendor via W705 with reason and suggestions for future submissions, (c) track all submissions and outcomes in product evaluation log for quarterly reporting | Category Manager | — | 15 min |

### System Touchpoints

- Product evaluation module — submission tracking, screening, evaluation, and decision workflow
- W705 vendor self-service portal — vendor product submission channel
- W679 assortment optimization & rationalization — assortment gap identification
- W625 product quality lab testing — sample evaluation
- W564 NPI full store rollout — advancement pathway
- W64 new product pilot — pilot execution
- W44 vendor performance scorecard — existing vendor reliability data
- W107 pricing hierarchy governance — price positioning validation
- W279 product substitution rules — product differentiation assessment
- W252 item master creation — product data governance
- W314 planogram template — shelf space assessment
- FIN-026 product costing & margin — margin analysis
- W156 CDP — customer demand signal data
- W624 competitor store visit — competitive benchmarking

### Pain Points / Risks

- Evaluation bottleneck — Category Managers are busy with day-to-day operations; new product evaluation often deprioritized, delaying assortment freshness
- Sample management — vendor samples arriving without tracking create DC clutter; sample lifecycle per W97 must be coordinated
- Vendor expectation management — vendors invest in submissions and expect timely feedback; slow responses damage vendor relationships
- Marginal products — products that barely pass screening consume evaluation resources with low probability of success; stricter initial screening criteria needed
- Category Manager bias — personal preferences may influence evaluation; structured scoring rubric and Merchandising Director review mitigate

### Time Estimate

Per submission: initial screening (15 min) + gap analysis (30 min) + evaluation (2-5 days elapsed, ~4 hours of active work) + summary (1 hour) + communication (15 min) = ~6 hours active per advancing product. Weekly: ~10-15 hours for intake and screening of 10-15 submissions.

### Staffing Implication

Absorbed within existing Category Manager and Procurement Analyst roles. Weekly: ~10-15 hours. No incremental headcount.

---

## W818. Vendor Insurance Certificate & Compliance Documentation Tracking

| Field | Detail |
|---|---|
| **Trigger** | New vendor onboarding per W36; annual insurance/certification renewal; compliance audit per W334 |
| **Frequency** | Ongoing; ~800-1,000 active vendors with insurance/certification requirements |
| **Volume** | ~100-150 renewal tracking events per month; ~20-30 new vendor compliance setups |
| **Owner** | Procurement Compliance Analyst |
| **Participants** | Procurement Analyst, Vendor, Legal Counsel, Finance Manager, Insurance Broker |

### Background

BuildRight Depot works with ~800-1,000 vendors, many of whom must maintain valid insurance policies (general liability, product liability, workers compensation, cargo/transit), certifications (ISO, DTI-BPS per W447, DENR per W477), and permits. Non-compliant vendors create liability exposure — if an uninsured vendor's product injures a customer, BuildRight bears full liability per W185 product liability. Philippine procurement best practice and BuildRight's internal controls per the internal controls matrix require current vendor insurance on file. W36 handles vendor onboarding but not the ongoing compliance tracking lifecycle.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **At onboarding per W36**: Procurement Analyst collects required compliance documents per vendor risk tier — Tier 1 (top 20 vendors, 45% COGS): comprehensive insurance + all certifications; Tier 2: general liability insurance + relevant certifications; Tier 3: basic insurance | Procurement Analyst | — | 30-60 min/vendor |
| 2 | **System creates compliance record per vendor**: document type, coverage amount, expiration date, renewal alert trigger (60/30/7 days) | System | Procurement Compliance Analyst | Automated |
| 3 | **System sends automated renewal reminders** to vendor 60 days before expiration via W705 vendor portal | System | — | Automated |
| 4 | **Vendor submits renewed certificate/policy via portal**; Procurement Analyst verifies: coverage adequacy, BuildRight listed as additional insured, policy limits meet contract requirements per W62 | Vendor / Procurement Analyst | Procurement Compliance Analyst | 15-30 min/vendor |
| 5 | **If vendor non-responsive at 30-day mark**: Procurement Analyst sends formal notice; system flags vendor account for potential hold | Procurement Analyst | Procurement Manager | 10 min |
| 6 | **If certificate expired**: system blocks new PO creation for vendor per W2; existing POs continue to completion; Procurement Analyst escalates to Procurement Manager | System / Procurement Analyst | Procurement Manager | 15 min |
| 7 | **Annual compliance audit**: Procurement Compliance Analyst reviews all vendor compliance records; generates compliance scorecard per W706; non-compliant vendors flagged for W160 factory audit or termination | Procurement Compliance Analyst | Procurement Manager | 20-30 hours concentrated |
| 8 | **Insurance claims coordination**: if vendor-caused incident triggers insurance claim, Procurement Analyst coordinates with W59 insurance lifecycle and Legal per W125 | Procurement Analyst | Legal Counsel | Varies |

### System Touchpoints

- W36 vendor onboarding — initial compliance document collection
- W62 vendor contract lifecycle — insurance requirements in vendor contracts
- W705 vendor self-service portal — vendor renewal submission and reminders
- W706 supplier scorecard — compliance scorecard generation
- W334 third-party vendor risk audit — audit-triggered compliance review
- W160 factory audit — non-compliant vendor escalation
- W185 product liability — liability exposure from non-compliant vendors
- W59 insurance lifecycle — claims coordination
- W125 legal case management — legal escalation
- W110 supplier quality CAPA — vendor corrective action
- W447 DTI-BPS certification — product certification compliance
- W477 DENR permits — environmental permit compliance

### Pain Points / Risks

- Vendor non-responsiveness to renewal requests — especially MSME vendors who may lack dedicated compliance staff
- Fraudulent or altered certificates requiring verification — visual inspection and carrier verification needed
- Varying insurance requirements across vendor categories — building materials vendors need different coverage than service providers
- Philippines-specific: many MSME vendors lack formal insurance — requiring alternative risk mitigation strategies
- Tracking burden for 800-1,000 vendors with varying expiration dates creates continuous workload

### Time Estimate

Ongoing monitoring: 2-3 hours/day. Monthly reporting: 2 hours. Annual audit: 20-30 hours concentrated. Total: ~60-80 hours/month.

### Staffing Implication

1 Procurement Compliance Analyst; shared with W706 supplier scorecard duties. No incremental headcount — absorbed within existing procurement compliance function.

---

## W819. Vendor Quality Incoming Inspection Failure & Material Review Board (MRB)

| Field | Detail |
|---|---|
| **Trigger** | Quality inspection failure at DC receiving per W681 or store receiving per W666 |
| **Frequency** | Weekly; ~30-50 quality failures per month across 4 DCs and 200 stores |
| **Volume** | ~30-50 failures/month; ~5-10 escalate to MRB disposition |
| **Owner** | Quality Assurance Analyst |
| **Participants** | QA Analyst, DC Receiving Supervisor, Procurement Analyst, Department Manager, Vendor |

### Background

While W681 covers quality inspection at DC receiving and W110 covers supplier quality CAPA, neither addresses the immediate disposition decision when goods fail inspection. A Material Review Board (MRB) process is standard in hardware retail where failed goods must be quickly dispositioned: return to vendor per W88, accept with concession (use-as-is with price reduction), rework, or scrap. For BuildRight's 35,000 SKUs including lumber (moisture content, dimensional tolerance), tiles (flatness, color consistency), paint (shelf life, color match), and tools (functional testing), quality failures have direct P&L impact and affect store replenishment timelines.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **DC Receiving Inspector identifies quality failure** during inspection per W681: documents defect type, severity, affected quantity, photo evidence | DC Receiving Inspector | — | 10-20 min |
| 2 | **System creates quality hold**: quarantined inventory flagged, PO receipt blocked per W2 | System | DC Receiving Supervisor | Automated |
| 3 | **QA Analyst performs root cause classification**: (a) critical safety defect (e.g., electrical product wiring) — immediate full reject, (b) major quality defect (dimensional, functional) — MRB review required, (c) minor cosmetic defect — accept with concession decision at DC level | QA Analyst | — | 15-30 min |
| 4 | **For critical safety defects**: automatic full reject → RTV per W88; vendor CAPA per W110; product recall risk assessment per W29 | QA Analyst | Procurement Manager | 30-60 min |
| 5 | **For major defects**: QA Analyst convenes MRB within 48 hours — Procurement Analyst, DC Supervisor, category-relevant Department Manager | QA Analyst | Department Manager | Scheduling: 15 min |
| 6 | **MRB evaluates**: (a) vendor negotiation for price concession vs. RTV cost, (b) store demand urgency (can stores wait for replacement?), (c) seasonal timing (near promo period?), (d) rework feasibility and cost, (e) customer impact of stock-out | MRB Panel (QA, Procurement, DC, Dept Mgr) | — | 1-2 hours |
| 7 | **MRB disposition decision**: (a) Return to Vendor (RTV per W88), (b) Accept with Concession (price reduction negotiated, debit memo per W770), (c) Rework and Accept (vendor pays rework cost), (d) Scrap (write-off per W92 inventory adjustment) | MRB Panel | Procurement Manager | 15-30 min |
| 8 | **System executes disposition**: updates inventory status, triggers vendor debit memo per W770 if applicable, adjusts PO line if partial delivery | System / QA Analyst | — | 15-30 min |
| 9 | **QA Analyst creates vendor quality incident record** per W110 for CAPA tracking | QA Analyst | — | 15 min |
| 10 | **Monthly quality failure analytics**: failure rate by vendor, by category, by defect type; MRB disposition distribution; vendor CAPA completion rate | QA Analyst | Quality Assurance Manager | 3 hours/month |

### System Touchpoints

- W681 DC quality inspection — inspection failure trigger
- W666 store receiving QC — store-level quality failure trigger
- W110 supplier quality CAPA — vendor corrective action tracking
- W88 RTV processing — return to vendor execution
- W770 debit memo — vendor cost recovery for concessions
- W92 inventory adjustment — scrap write-off processing
- W2 PO management — PO receipt blocking and adjustment
- W91 damaged goods disposition — related disposition workflow
- W29 product recall — critical safety defect escalation
- W150 product quality testing — lab testing support
- W100 vendor statement reconciliation — financial reconciliation

### Pain Points / Risks

- MRB delays blocking replenishment — while goods are quarantined, stores may stock out; 48-hour MRB SLA must be enforced
- Vendor disputes on defect classification — vendors may contest QA findings; photographic evidence and standardized defect criteria mitigate
- Seasonal items failing near promo period requiring emergency substitution per W279 — time pressure on MRB increases
- Partial quality failures (e.g., 60% of batch good, 40% defective) — splitting disposition adds complexity
- DC quarantine space constraints — high failure volumes may overwhelm designated quarantine areas

### Time Estimate

Per failure: inspection (10-20 min) + classification (15-30 min) + MRB if needed (1-2 hours) + disposition execution (15-30 min) = ~2-4 hours per MRB case. Monthly analytics: 3 hours.

### Staffing Implication

1 QA Analyst per DC (4 total, absorbed into existing DC quality roles) + 1 centralized QA Manager. No incremental headcount beyond existing quality team structure.

---

## W901. Vendor Seasonal Buy-Back & Stock Return Agreement Execution

| Field | Detail |
|---|---|
| **Trigger** | Seasonal merchandise period ends (per seasonal calendar — Christmas décor, flood control items, garden/summer items); or vendor seasonal buy-back agreement clause is triggered by unsold inventory exceeding threshold |
| **Frequency** | ~20–30 seasonal buy-back executions/year (aligned with 6 major seasonal transitions per model company profile) |
| **Volume** | Avg 200–800 units per vendor per seasonal transition; ~15–25 participating vendors |
| **Owner** | Category Manager |
| **Participants** | Category Manager, Merchandise Planner, Store Manager, Vendor, Finance (AP/AR), DC Operations, Procurement |

### Background

BuildRight's seasonal merchandise (Christmas lights/décor, flood control items, garden/summer items) represents a significant inventory risk due to the Philippine seasonal calendar defined in the model company profile. After the Christmas season (November–December), unsold Christmas décor has zero demand until the following year; after rainy season (June–August), unsold flood control items become dead stock. While W68 (Product Lifecycle & Discontinuation) and W830 (Product Phase-Out Inventory Disposition Planning) cover general product discontinuation, and W88 (Return to Vendor) covers defective/wrong-item returns, there is a specific workflow gap for contractual seasonal buy-back agreements where vendors agree to repurchase unsold seasonal inventory at a pre-agreed percentage of cost. These agreements are common in Philippine retail — vendors offer seasonal buy-back terms (typically 50–80% of cost) as an incentive for BuildRight to commit to larger seasonal buys (W32). This workflow manages the end-to-end execution of seasonal buy-back agreements: identifying eligible inventory, negotiating return quantities with vendors, coordinating physical return logistics, and processing vendor settlement.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Seasonal Period End Trigger**: (a) per seasonal calendar, system identifies seasonal SKUs approaching end-of-season: (i) Christmas/holiday items — trigger January 15; (ii) summer/garden items — trigger June 1; (iii) rainy season/flood control items — trigger September 1; (iv) back-to-school/construction items — trigger June 15; (b) system generates "Seasonal Inventory Exposure Report" per seasonal category: (i) total units on-hand across all locations (stores + DCs); (ii) units sold during season vs. units bought; (iii) sell-through rate %; (iv) remaining inventory at cost value; (v) days of inventory at current run-rate (typically near-zero demand post-season); (c) system flags SKUs with buy-back clause in vendor agreement (W62) — identified at seasonal buy planning (W32) | System / Merchandise Planner | Category Manager | Automated report generation |
| 2 | **Buy-Back Eligibility Assessment**: Category Manager reviews each seasonal vendor's agreement: (a) **Buy-back terms** (negotiated at W32 seasonal buy planning): (i) eligible items: specific seasonal SKUs listed in agreement; (ii) buy-back rate: % of original cost vendor will pay (typically 50–80%); (iii) maximum quantity: cap on units vendor will repurchase (e.g., up to 20% of original order quantity); (iv) condition requirements: items must be in saleable condition — no damage, original packaging, no price stickers on product; (v) return window: deadline for physical return (typically 30–45 days post-season end); (vi) return shipping cost: borne by BuildRight or vendor per agreement; (b) Category Manager calculates per vendor: (i) eligible units: min(on-hand units, max buy-back quantity per agreement); (ii) units in saleable condition (exclude damaged per W91, opened per W549); (iii) expected recovery: eligible units × buy-back rate × original cost; (iv) compare recovery vs. alternative disposition: (a) markdown clearance (W93) — likely recovery 20–50% of SRP; (b) carry to next season — storage cost + risk of obsolescence; (c) donate per W444 — no recovery but CSR benefit; (d) recommend buy-back if recovery > best alternative | Category Manager | VP Merchandising | 4–8 hours per seasonal transition |
| 3 | **Vendor Return Negotiation**: (a) Category Manager contacts vendor with buy-back proposal: (i) total units proposed for return; (ii) condition certification (store-level inspection per W91); (iii) proposed return logistics plan (consolidation at DC vs. direct store-to-vendor); (iv) expected settlement timeline; (b) vendor may: (i) accept full proposed quantity at agreed rate; (ii) negotiate reduced quantity (if exceeding max cap or condition disputes); (iii) offer credit note instead of cash refund — Category Manager evaluates: credit note acceptable if (a) vendor is strategic partner with ongoing orders, (b) credit note has no expiry or ≥ 12-month validity; (iv) refuse buy-back (if BuildRight missed return window or condition requirements not met) — escalate to VP Merchandising; (c) Category Manager and vendor agree on: final return quantity, unit price, total settlement amount, return logistics plan, settlement method (cash refund or credit note) | Category Manager | VP Merchandising | 2–5 days (vendor-dependent) |
| 4 | **Physical Return Execution**: (a) **Store-level consolidation**: (i) Store Managers at all stores with eligible seasonal inventory receive return instructions from Category Manager; (ii) store staff pulls eligible items from shelves and backroom; (iii) items inspected for condition compliance per W91 — damaged/non-saleable items excluded; (iv) eligible items packed and labeled with return authorization number; (v) items shipped to designated consolidation DC per W22B store-to-DC return process; (b) **DC consolidation**: (i) DC receives store returns and adds DC-held seasonal inventory; (ii) DC Quality Inspector verifies condition compliance for all items; (iii) non-compliant items separated and dispositioned per W91 damaged goods; (iv) compliant items palletized and staged for vendor pickup or BuildRight-arranged shipment; (c) **Vendor pickup/shipment**: (i) if vendor pickup: DC schedules dock appointment per W585; vendor collects pallets; DC issues goods issue against return authorization; (ii) if BuildRight ships: DC dispatches per W106 outbound dispatch; freight cost allocated per agreement (Step 2); (d) system updates inventory: items in transit to vendor deducted from on-hand; return authorization tracked to settlement | Store Manager / DC Operations / Category Manager | — | 1–2 weeks |
| 5 | **Financial Settlement**: (a) Finance processes vendor buy-back settlement: (i) AP creates vendor debit memo (W770) for return quantity × buy-back rate × original cost; (ii) if vendor issues credit note: AP records credit note against vendor account — applied to future PO invoices per W62; (iii) if vendor issues cash refund: AR records incoming payment against debit memo; (iv) system reverses inventory value at original WAC; (v) any difference between book value and buy-back recovery recognized as seasonal markdown loss in P&L; (b) for items returned but rejected by vendor (condition dispute): Category Manager determines final disposition — markdown per W93, donate per W444, or write-off per W587; (c) Finance reports seasonal buy-back financial impact in monthly category P&L per W102 | Finance (AP) / Category Manager | Finance Manager | 3–5 business days post-return |
| 6 | **Post-Season Buy-Back Review**: (a) per seasonal transition, Category Manager documents: (i) seasonal sell-through rate by vendor and SKU; (ii) buy-back execution: units returned, recovery rate, logistics cost, settlement timeline; (iii) financial impact: markdown loss avoided, net recovery after freight; (iv) vendor performance: responsiveness, condition disputes, settlement timeliness; (b) review feeds into: (i) next year's seasonal buy planning (W32) — adjust buy quantities based on actual sell-through; (ii) vendor agreement renegotiation (W62) — adjust buy-back terms based on vendor cooperation; (iii) seasonal assortment review (W679) — drop seasonal SKUs with consistently poor sell-through even with buy-back | Category Manager | VP Merchandising | 4–6 hours per seasonal transition |

### System Touchpoints

- Seasonal calendar master (W306) for automatic period-end triggers
- Seasonal inventory exposure report (new BI report)
- Vendor agreement/buy-back terms module (W62)
- Store-to-DC return process (W22B)
- DC receiving for store return consolidation (W3)
- DC quality inspection (W681)
- DC outbound dispatch for vendor shipment (W106)
- RTV processing (W88) for return authorization and tracking
- AP vendor debit memo (W770) for settlement
- AR credit note processing (W70)
- Inventory write-off (W587) for rejected/damaged items
- Markdown management (W93) for alternative disposition
- Category P&L reporting (W102)
- Vendor scorecard (W44) for buy-back performance documentation
- Seasonal buy planning (W32) for feed-forward into next season

### Pain Points / Risks

- **Vendor refusing buy-back despite contractual agreement**: vendors may cite condition issues, missed deadlines, or financial distress to avoid repurchasing; clear contractual language with penalty clause per W62 is essential; Category Manager must escalate firmly
- **Store-level condition compliance inconsistency**: 200 stores inspecting items for buy-back eligibility with varying standards; centralized DC re-inspection (Step 4b) catches non-compliant items but creates return logistics waste
- **Logistics cost exceeding recovery value**: for low-value seasonal items (Christmas lights at PHP 150/ea), freight cost to consolidate at DC and ship to vendor may exceed 50% buy-back recovery; local store-level markdown (W93) may be more economical — cost-benefit analysis at Step 2 is critical
- **Seasonal inventory "leaking" before buy-back execution**: high-demand seasonal items (e.g., inflatable pools in a heat wave) may sell through, leaving no buy-back inventory; conversely, slow-moving items flood the buy-back process — the system should track real-time sell-through to adjust buy-back estimates
- **Credit note expiry and utilization risk**: vendor-issued credit notes that expire before BuildRight places next seasonal order with same vendor = lost recovery; Finance must monitor credit note aging per W766
- **Tax implications of buy-back returns**: vendor buy-backs are not standard sales returns; BIR may require specific documentation (debit memo, cargo transfer document) to justify VAT adjustment — Finance must ensure compliance per W90

### Staffing Implication

- **Category Manager**: ~8–14 hours per seasonal transition on buy-back assessment, negotiation, and review; 6 transitions/year = 48–84 hours/year; absorbed by existing category management team
- **Merchandise Planner**: ~4–6 hours per transition on exposure reporting and stock reconciliation; absorbed by existing role
- **Store Managers**: ~1–2 hours per store per transition on item pulling and packing; absorbed by existing role
- **DC Operations**: ~4–8 hours per transition on consolidation and vendor shipment; absorbed by existing DC team
- **Finance**: ~2–3 hours per transition on settlement processing; absorbed by existing AP team
- **No incremental headcount**.

### Time Estimate

- System trigger and report generation: automated
- Buy-back eligibility assessment: 4–8 hours
- Vendor return negotiation: 2–5 days (vendor response-dependent)
- Physical return execution: 1–2 weeks
- Financial settlement: 3–5 business days
- Post-season review: 4–6 hours
- **Total elapsed time per seasonal transition**: 3–5 weeks
- **Total staff time per seasonal transition**: 20–35 hours

---

## W915. Vendor Product Packaging Sustainability Assessment & Compliance Management

| Field | Detail |
|---|---|
| **Trigger** | Annual vendor scorecard cycle; new vendor onboarding (W36); new product introduction (W564); or regulatory change in packaging requirements |
| **Frequency** | Annual assessment for top 200 vendors; continuous monitoring for new products |
| **Volume** | ~200 vendor assessments/year; ~5,000–8,000 product packaging reviews/year |
| **Owner** | Category Manager (Sustainability) |
| **Participants** | Category Manager, Vendor, ESG Manager, Quality Assurance, Merchandising Director |

### Background

BuildRight's ESG strategy (W192–W195, W800–W801) includes a commitment to reducing packaging waste across the supply chain. With ~400–600 TEUs of imports per month and ~800–1,000 active vendors, BuildRight's packaging footprint is significant: wooden pallets, cardboard boxes, plastic shrink wrap, styrofoam inserts, and individual product packaging contribute to the waste stream. Philippine regulations are tightening — the Extended Producer Responsibility (EPR) Act of 2022 (RA 11898) mandates large enterprises to recover and divert plastic packaging waste, with penalties for non-compliance. BuildRight, as a large enterprise, must comply. Beyond compliance, sustainable packaging is a competitive differentiator: environmentally-conscious customers (a growing segment in the Philippine market) prefer vendors with eco-friendly packaging, and sustainable sourcing per W195 is an ESG commitment. This workflow establishes a structured vendor packaging sustainability assessment program that evaluates, scores, and incentivizes vendors to adopt sustainable packaging, while ensuring BuildRight's compliance with RA 11898 EPR requirements.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Packaging Sustainability Assessment Framework**: (a) ESG Manager and Category Manager define assessment criteria per vendor: (i) packaging material composition (% recyclable, % biodegradable, % single-use plastic, % recycled content); (ii) packaging-to-product ratio (weight of packaging as % of product weight); (iii) pallet utilization efficiency (% of pallet space used — under-packed pallets waste transport capacity and increase carbon emissions per W192); (iv) labeling compliance (recyclability symbols, material identification per DENR guidelines); (v) hazardous packaging materials (styrofoam, PVC, non-recyclable multi-layer packaging — flagged for phase-out); (b) scoring model: 100-point scale — Material Sustainability (40 pts), Efficiency (25 pts), Compliance (20 pts), Innovation (15 pts); (c) tier classification: Green (≥80 pts), Yellow (60–79), Orange (40–59), Red (<40); (d) Merchandising Director approves framework | Category Manager / ESG Manager | Merchandising Director | 20–30 hours (one-time framework development) |
| 2 | **Vendor Packaging Data Collection**: (a) for top 200 vendors (by spend): vendor submits packaging data via W705 vendor portal: (i) packaging material breakdown per SKU category; (ii) packaging weight per unit; (iii) pallet configuration (units per pallet, layers, stack pattern); (iv) recyclability certification (if available); (v) sustainable packaging improvement roadmap; (b) for import vendors: Category Manager requests packaging samples at DC receiving for physical assessment; (c) for new vendor onboarding (W36): packaging sustainability questionnaire integrated into onboarding checklist; (d) system validates data completeness and flags incomplete submissions for vendor follow-up per W870 compliance document tracking | Vendor / Category Manager / System | ESG Manager | 15–20 min per vendor |
| 3 | **Assessment Scoring & Vendor Feedback**: (a) system calculates packaging sustainability score per vendor based on submitted data; (b) Category Manager reviews scores, validates against physical samples (for top 50 vendors), and assigns final tier; (c) vendor receives scorecard via W705 portal with: overall score, tier classification, category-level performance, comparison to industry average (anonymized peer benchmark per W871), and improvement recommendations; (d) vendor improvement roadmap request: Orange and Red tier vendors must submit a 12-month improvement plan with specific milestones (e.g., "Replace styrofoam inserts with corrugated cardboard by Q3"); (e) Green tier vendors receive BuildRight "Sustainable Packaging Partner" badge for marketing use and preferential consideration for new product listings per W788 | Category Manager / System / Vendor | Merchandising Director | 30–45 min per vendor |
| 4 | **EPR Compliance & Waste Diversion Tracking**: (a) BuildRight's EPR obligation per RA 11898: annual plastic packaging waste diversion target (starting 30%, increasing to 80% by 2030); (b) system aggregates packaging waste data from: DC receiving (inbound packaging per vendor), store operations (outbound packaging per W502 non-hazardous waste management), and ecommerce (shipping packaging per W19); (c) ESG Manager tracks: total packaging waste generated (by material type), % diverted (recycled, reused, returned to vendor), and EPR compliance status; (d) vendor-specific packaging waste contribution identifies high-waste vendors for targeted improvement; (e) quarterly EPR compliance report prepared for DENR per W433 SMR/CMR reporting; (f) annual: EPR compliance audit per W362 internal audit | ESG Manager / System | VP Supply Chain | 6–8 hours/quarter |
| 5 | **Sustainable Packaging Improvement Incentives**: (a) Green tier vendors: (i) featured in BuildRight sustainability marketing per W694 ESG report; (ii) eligible for vendor co-op advertising funding per W513 with "Sustainable Choice" branding; (iii) preferential shelf placement per W86 planogram; (b) vendor improvement funding: BuildRight allocates annual sustainability improvement fund (PHP 2–5M) to co-invest with Orange/Red tier vendors in packaging redesign; (c) packaging innovation awards: annual BuildRight Sustainable Packaging Award for most improved vendor per W630 recognition program; (d) vendor contract clause per W688: new contracts require packaging sustainability improvement commitment; existing contracts amended at renewal per W704; (e) annual: program effectiveness review — overall packaging waste reduction, vendor tier migration (Orange/Red → Yellow/Green), EPR compliance status, and ROI of sustainable packaging program | Category Manager / ESG Manager / Merchandising Director | VP Merchandising | 8–10 hours/year |

### System Touchpoints

- Vendor portal (W705) for packaging data submission and scorecard access
- Item master (W252) with packaging attributes per SKU (weight, material, recyclability)
- DC WMS receiving module (W3) for inbound packaging tracking
- Store waste management module (W502) for outbound packaging tracking
- ESG metrics master (W406) for sustainability scoring framework
- Vendor scorecard system (W706) for packaging sustainability KPI integration
- EPR compliance tracking module integrated with DENR SMR/CMR reporting (W433)
- Contract management system (W688) for packaging sustainability clause enforcement
- BI dashboard for packaging waste analytics and vendor sustainability scoring
- ESG reporting module (W694) for annual sustainability report data

### Pain Points / Risks

- **Vendor resistance**: many vendors, especially MSMEs, lack resources for sustainable packaging; improvement timeline must be realistic with BuildRight co-investment support; tiered approach (improvement plan vs. immediate compliance) maintains vendor relationships
- **Data quality**: vendor-submitted packaging data may be inaccurate or incomplete; physical sample verification for top vendors and random spot-checks for others mitigate; data quality monitoring per W734
- **Cost pass-through**: sustainable packaging may cost more; vendors may increase prices to cover packaging redesign costs; BuildRight's co-investment fund and volume commitment incentive offset vendor cost
- **Regulatory complexity**: RA 11898 EPR requirements evolving; DENR implementing rules may change; regulatory change management per W657 ensures BuildRight stays ahead of requirements
- **Import vendor control**: BuildRight has less influence over import vendor packaging (packed at origin country); Category Manager works with freight forwarder per W144 to optimize container loading (reducing packaging needs) and requests import vendor participation in program
- **Measurement consistency**: packaging sustainability scoring requires consistent methodology; annual framework calibration with external sustainability consultant ensures accuracy and credibility

### Staffing Implication

- **Category Manager (Sustainability)**: absorbed by existing Category Manager with ESG portfolio; ~8–10 hours/month on vendor packaging assessments; no incremental headcount
- **ESG Manager**: ~6–8 hours/quarter on EPR compliance tracking and reporting; absorbed by existing role
- **No incremental headcount** — program managed within existing merchandising and ESG team capacity

### Time Estimate

- Framework development: 20–30 hours (one-time)
- Vendor data collection: 15–20 min per vendor
- Assessment scoring: 30–45 min per vendor
- EPR compliance tracking: 6–8 hours/quarter
- Annual program review: 8–10 hours
- **Total per vendor per year**: ~1–2 hours of staff time (assessment + monitoring)
