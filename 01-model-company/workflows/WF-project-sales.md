# Project-Based B2B & Trade Sales Workflows

> Quotations, bid management, contract pricing, staged deliveries, and project-specific logistics for construction and corporate clients.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W162. Project Quotation & Bid Management](#w162-project-quotation-bid-management)
- [W163. Contract Pricing & Project Price Books](#w163-contract-pricing-project-price-books)
- [W164. Staged Project Delivery & Call-Off Orders](#w164-staged-project-delivery-call-off-orders)
- [W165. Project Retention & Milestone Billing](#w165-project-retention-milestone-billing)
- [W166. Corporate / Institutional Tendering](#w166-corporate-institutional-tendering)
- [W228. Sales Commission Calculation (Trade & Project Sales)](#w228-sales-commission-calculation-trade-project-sales)
- [W229. B2B Customer Credit Limit Exception & Escalation](#w229-b2b-customer-credit-limit-exception-escalation)
- [W421. Batch/Shade Reconciliation for Large Project Sales](#w421-batchshade-reconciliation-for-large-project-sales)
- [W792. Project Change Order Management & Margin Re-Impact Assessment](#w792-project-change-order-management--margin-re-impact-assessment)
- [W793. Project Close-Out, Final Reconciliation & Warranty Handover](#w793-project-close-out-final-reconciliation--warranty-handover)

---

## W162. Project Quotation & Bid Management

| Field | Detail |
|---|---|
| **Trigger** | Customer requests a quote for a specific construction project or bulk purchase |
| **Frequency** | ~300–500 quotes/month |
| **Volume** | Quote value: PHP 100K to PHP 10M+ |
| **Owner** | Sales Rep (B2B) |
| **Participants** | Sales Rep, Category Manager (for deep discounts), Project Manager (Client) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sales Rep receives Bill of Quantities (BOQ) or item list from client project | Sales Rep | — | 1 hour |
| 2 | Sales Rep creates Quote in system: selects items, specifies quantities, sets validity period (typically 15–30 days) | Sales Rep | — | 30 min |
| 3 | System checks current stock (ATP) across all DCs/Stores; flags items with insufficient stock for the project timeline | System | — | Automated |
| 4 | **Pricing Strategy**: (a) If standard B2B price list used: auto-approved; (b) If additional discount requested (> 5% off B2B list): route to Category Manager for approval; (c) If "Loss Leader" pricing for strategic bid: route to VP Merchandising | Sales Rep / Cat. Manager | VP Merchandising | 1–4 hours |
| 5 | System generates Quotation PDF with terms (payment, delivery, lead times, force majeure) | System | — | Automated |
| 6 | Sales Rep presents quote to client; negotiates terms | Sales Rep | Sales Manager | 1–5 days |
| 7 | Client accepts: Sales Rep converts Quote to **Project Contract / Master Sales Order** in system | Sales Rep | — | 15 min |
| 8 | If Quote expires: system auto-cancels; Sales Rep can "re-quote" with updated pricing | System | Sales Rep | Automated |

### System Touchpoints
- Quote-to-Contract conversion engine: Quote → Master Sales Order with full BOQ and terms carry-forward (W162.7)
- ATP check across all DCs and stores with project timeline feasibility assessment (W162.3)
- Tiered pricing approval workflow: standard B2B auto-approve, deep discount route to Category Manager, loss leader route to VP Merchandising (W162.4)
- Quotation PDF generation with configurable terms and conditions templates (W162.5)
- Quote expiry management with auto-cancellation and re-quote capability (W162.8)

### Time Estimate
Per quotation: ~2.5 hours to 5 days total (1 hour BOQ receipt + 30 min quote creation + automated ATP check + 1–4 hours pricing approval + automated PDF + 1–5 days negotiation). With ~300–500 quotes/month across ~50 reps, each rep handles ~6–10 quotes/month.

### Pain Points / Risks
- ATP checks at quotation time may not reflect stock availability at order conversion (weeks later); customers accept quotes based on stock that has since been allocated to other channels, causing fulfillment failures.
- Deep discount approval routing (W162.4) introduces delays — Category Managers may take 1–4 hours to approve, during which the client may receive competing quotes from rivals.
- Quote validity period (15–30 days) is often too short for large government and institutional projects with lengthy procurement cycles; Sales Reps spend significant time re-quoting expired prices.
- No systematic win/loss tracking on quotations — the company cannot analyze why quotes are won or lost (price, stock, terms, competitor), limiting pricing strategy optimization.

---

### Staffing Implication
~300–500 quotes/month across ~50 B2B Sales Reps; each rep handles ~6–10 quotes/month as part of existing duties. Category Managers review deep discount approvals (~1–4 hours/month). VP Merchandising approves loss-leader pricing (~2–4 hours/month). No incremental headcount; absorbed by existing B2B sales and merchandising teams.

## W163. Contract Pricing & Project Price Books

| Field | Detail |
|---|---|
| **Trigger** | Project Contract signed; requires locked-in pricing for duration of project (6–18 months) |
| **Frequency** | ~10–20 new project price books/month; ongoing maintenance for active projects |
| **Volume** | ~30–50 active project price books at any time |
| **Owner** | Pricing Analyst |
| **Participants** | Pricing Analyst, Category Manager, Sales Rep, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Pricing Analyst creates a **Project Price Book** linked to the specific Customer + Project ID | Pricing Analyst | Category Manager | 30 min |
| 2 | Enters locked-in prices for the agreed BOQ items; sets price validity end date | Pricing Analyst | Category Manager | 30 min |
| 3 | System ensures that when this Customer orders for this Project, the Project Price Book takes precedence over standard B2B or Promo price lists | System | — | Automated |
| 4 | **Price Escalation Clause**: If contract allows for price adjustment (e.g., fuel/commodity surcharge), Pricing Analyst updates Price Book based on formula; triggers notification to client | Pricing Analyst | Sales Rep | 30 min |

### System Touchpoints
- Project-specific Price Book module linked to Customer + Project ID with locked-in pricing and validity dates (W163.1–2)
- Price precedence engine ensuring Project Price Book overrides standard B2B and promotional price lists at order entry (W163.3)
- Price escalation formula engine with client notification for contract-allowed adjustments (W163.4)
- Integration with W162 (quotation-to-contract conversion) for initial Price Book population

### Time Estimate
New price book creation: ~1 hour (30 min setup + 30 min price entry). Maintenance: ~30 min per escalation event. With ~10–20 new price books/month and ongoing maintenance, Pricing Analyst spends ~15–25 hours/month on project pricing.

### Pain Points / Risks
- Locked-in pricing for 6–18 months exposes BuildRight to commodity price volatility (cement, steel, copper wire); if purchase costs rise significantly, project margins erode or turn negative with no recovery mechanism unless escalation clauses were negotiated.
- Price precedence logic failures — when Project Price Book and promotional pricing overlap, system conflicts can cause incorrect pricing at order entry, leading to undercharging (margin loss) or overcharging (client disputes).
- Manual price escalation calculations (W163.4) are error-prone; formula complexity varies by contract and requires careful review to avoid client-facing pricing errors that damage commercial relationships.
- Active project price books are not systematically reviewed for margin performance; unprofitable projects are identified only at completion rather than flagged mid-project for corrective action.

---

### Staffing Implication
~10–20 new price books/month + ongoing maintenance = ~15–25 hours/month for Pricing Analyst. Category Manager reviews and approves price book setup (~4–8 hours/month). Sales Rep provides escalation clause inputs. Absorbed by existing Pricing Analyst and Category Manager roles. No incremental headcount.

## W164. Staged Project Delivery & Call-Off Orders

| Field | Detail |
|---|---|
| **Trigger** | Project site requests a partial delivery (Call-Off) against the Master Sales Order |
| **Frequency** | Weekly/Bi-weekly per project |
| **Volume** | Total project may have 10–50 partial deliveries |
| **Owner** | Sales Coordinator |
| **Participants** | Sales Coordinator, Client Project Manager, Logistics Team, Credit Control Clerk, Supply Planner |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Client Project Site sends "Call-Off" request (Item, Quantity, Site Location, Date) | Client / Sales Rep | — | 10 min |
| 2 | Sales Coordinator creates **Release Order (Delivery Order)** against the Master Sales Order | Sales Coordinator | — | 15 min |
| 3 | System validates: (a) Quantity is within Master Order balance, (b) Customer has available credit limit, (c) Customer has no overdue invoices | System | — | Automated |
| 4 | System reserves stock at the designated DC or Store for this release | System | — | Automated |
| 5 | Logistics processes the delivery per W19 (Dispatch) | Logistics Team | — | Per W19 |
| 6 | Upon delivery: System updates Master Order "Remaining Quantity"; posts to AR (W8) if on-account | System | — | Automated |

### System Touchpoints
- Release Order (Delivery Order) creation against Master Sales Order with balance tracking (W164.2–3)
- Multi-condition validation engine: quantity balance, credit limit check including in-flight commitments, and overdue invoice block (W164.3)
- Stock reservation at designated DC or Store for call-off fulfillment (W164.4)
- Master Order "Remaining Quantity" decrement with AR posting upon delivery confirmation (W164.6)
- Integration with W19 (logistics dispatch), W8 (AR), W163 (project price book for pricing)

### Time Estimate
Per call-off: ~25 min order processing (10 min request + 15 min Release Order creation + automated validation/reservation). Logistics per W19. With 10–50 deliveries per project and multiple active projects, Sales Coordinator handles ~20–40 call-offs/week = ~8–17 hours/week.

### Pain Points / Risks
- Credit limit validation (W164.3b) frequently blocks call-off orders for projects where the client has overdue invoices from earlier milestones — the operational urgency of project delivery conflicts with credit control policy.
- Stock reservation for call-off orders removes inventory from general availability, impacting store replenishment (W4) and ecommerce ATP during long project delivery cycles (6–18 months).
- Master Order balance tracking errors accumulate across 10–50 partial deliveries — any discrepancy between system remaining quantity and actual site requirements causes either over-delivery (waste) or under-delivery (project delays).
- Multiple active projects competing for the same limited stock at a single DC create allocation conflicts that require manual Supply Planner intervention, delaying call-off fulfillment.

---

### Staffing Implication
~20–40 call-offs/week = ~8–17 hours/week for Sales Coordinator. Credit Control Clerk supports credit validation (~2–4 hours/week). Supply Planner intervenes for stock allocation conflicts (~2–3 hours/week). Absorbed by existing roles. No incremental headcount.

## W165. Project Retention & Milestone Billing

| Field | Detail |
|---|---|
| **Trigger** | Project milestone achieved; or final billing with retention |
| **Frequency** | Milestone-based; typically 3–6 milestones per project; projects span 6–18 months |
| **Volume** | ~20–40 active projects with milestone billing at any time |
| **Owner** | AR Clerk |
| **Participants** | Sales Rep, AR Clerk, Client Project Manager, Sales Manager, Finance (Controller) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Sales Rep confirms milestone achievement with client (e.g., "Structural Phase Complete") | Sales Rep | — | — |
| 2 | AR Clerk generates Milestone Invoice per contract terms (e.g., 20% of total project value) | AR Clerk | — | 15 min |
| 3 | **Retention Management**: If contract specifies retention (typically 5–10% held until final acceptance), system automatically deducts retention from each milestone invoice and posts to "Retention Receivable" account | System / AR Clerk | — | Automated |
| 4 | Final Acceptance: Client signs off; AR Clerk invoices for the total accumulated Retention balance | AR Clerk | Sales Manager | 30 min |

### System Touchpoints
- Milestone Invoice generation linked to Master Sales Order with contract-defined milestone percentages (W165.2)
- Retention Receivable accounting: automated deduction from milestone invoices and posting to separate retention GL account (W165.3)
- Final acceptance billing for accumulated retention balance with AR posting (W165.4)
- Integration with W164 (call-off deliveries — milestone triggered by cumulative delivery progress), W8 (AR collections), W163 (project price book for billing rates)

### Time Estimate
Per milestone: ~45 min (15 min invoice generation + automated retention deduction + 30 min for final acceptance billing). With ~20–40 active projects and 3–6 milestones each, AR Clerk processes ~10–20 milestone invoices/month = ~8–15 hours/month.

### Pain Points / Risks
- Milestone achievement confirmation is subjective and client-dependent — clients may dispute milestone completion to delay payment, creating AR aging and cash flow pressure on BuildRight.
- Retention amounts (5–10% of project value) accumulate on the balance sheet as Retention Receivable for months until final project acceptance; for large projects (PHP 5M+), this ties up PHP 250K–500K in working capital.
- Final acceptance and retention release require client sign-off, which can take 30–90+ days after project completion as clients conduct their own Punch List reviews; the retention becomes effectively uncollectible during this period.
- Milestone billing tied to delivery progress (W164) can create timing mismatches — goods delivered in one month may not achieve the milestone threshold until the next delivery, delaying invoicing and revenue recognition.

---

### Staffing Implication
~10–20 milestone invoices/month = ~8–15 hours/month for AR Clerk. Sales Rep confirms milestone achievement with client (~1–2 hours/month). Sales Manager approves final acceptance billing (~2–3 hours/month). Finance Controller reviews retention account balances quarterly. Absorbed by existing AR and Finance roles. No incremental headcount.

## W166. Corporate / Institutional Tendering

| Field | Detail |
|---|---|
| **Trigger** | Government (PhilGEPS) or Private Institutional RFP/RFQ issued |
| **Frequency** | ~5–10 active bids at any time; PhilGEPS postings are continuous |
| **Volume** | Government tenders range PHP 500K–20M; institutional RFQs PHP 200K–10M |
| **Owner** | Bid & Tender Manager |
| **Participants** | Bid Manager, Sales Director, Legal Counsel, CFO, Category Manager, Sales Rep |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Bid Manager monitors PhilGEPS/Tender boards; downloads RFP | Bid Manager | — | Daily |
| 2 | Initial Go/No-Go: Evaluate capability, capacity, and margin potential | Bid Manager | Sales Director | 1 day |
| 3 | Coordinate with Legal (Tender Bonds, JV agreements) and Finance (Performance Bonds, Cash Flow) | Bid Manager | Legal / CFO | 3–5 days |
| 4 | Compile Bid Package: Pricing (W162), Technical Specs (W50), Corporate Docs | Bid Manager | — | 1–2 weeks |
| 5 | Submit Bid (Electronic or Physical); track bid opening results | Bid Manager | — | Per RFP |
| 6 | If won: Transition to W163 (Contract Pricing) and W164 (Fulfillment) | Bid Manager | — | — |

### System Touchpoints
- PhilGEPS integration or monitoring dashboard for automated RFP/RFQ alert and download (W166.1)
- Bid Package compilation module: pricing from W162, technical specs from W50, corporate document library (W166.4)
- Bid tracking register with lifecycle status (Identified → Go/No-Go → In Progress → Submitted → Under Evaluation → Won/Lost) (W166.5)
- Integration with W163 (contract pricing for won bids), W164 (staged delivery), and W165 (milestone billing)

### Time Estimate
Per bid cycle: ~3–4 weeks (1 day Go/No-Go + 3–5 days Legal/Finance coordination + 1–2 weeks bid compilation + submission). Bid Manager monitors daily and manages ~5–10 concurrent bids, spending ~30–40 hours/week on tendering activities.

### Pain Points / Risks
- Government procurement in the Philippines is heavily bureaucratic — PhilGEPS compliance requirements, notarization, and documentary submissions are rigid; a single missing document disqualifies the entire bid regardless of commercial competitiveness.
- Performance bond and tender bond requirements tie up bank credit facilities; with ~5–10 active bids, PHP 5M–50M in bank guarantees may be encumbered simultaneously, limiting available credit for operations.
- Government payment terms are notoriously long (60–120 days post-delivery for some agencies), creating severe cash flow strain on projects that require upfront material procurement.
- Win rates for government tenders are often low (< 30%) due to lowest-bid-wins evaluation criteria; significant bid preparation costs (staff time, bond fees, document preparation) are sunk regardless of outcome.

---

### Staffing Implication
1 dedicated Bid & Tender Manager (~30–40 hours/week managing 5–10 concurrent bids). Legal Counsel: ~3–5 days/bid for bond/JV coordination. CFO: reviews performance bonds and financial commitments. Category Manager supports pricing (~1–2 hours/bid). Sales Director approves Go/No-Go decisions. No incremental headcount beyond existing Bid Manager role.

## W228. Sales Commission Calculation (Trade & Project Sales)

| Field | Detail |
|---|---|
| **Trigger** | Monthly sales commission cycle (after month-end close and collection confirmation) |
| **Frequency** | Monthly |
| **Volume** | ~50 B2B/Trade Sales Reps and Store Account Managers |
| **Owner** | Sales Operations Manager |
| **Participants** | Sales Operations, Finance (Payroll), HR, Sales Director, Sales Reps |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Pull**: Sales Operations pulls monthly sales and collections report by Sales Rep / Account Manager from ERP. Commission is calculated based on realized collections (paid invoices), not just invoiced sales, to mitigate bad debt risk (W108). | Sales Operations | — | 2 hours |
| 2 | **Tiered Calculation**: System applies tiered commission rates based on individual margin performance (higher margin items earn higher commission rates) and target achievement (e.g. 80-99% target gets standard commission, 100%+ gets accelerator). | System / Sales Ops | Sales Ops Mgr | 1 hour |
| 3 | **Deductions & Adjustments**: System deducts returns (W12) or credit notes issued against original sales of the rep, and adjusts for any shared commission deals between reps. | System | Sales Ops Mgr | 30 min |
| 4 | **Review & Approval**: Sales Operations generates commission sheets; routes to Sales Director and CFO for approval. | Sales Ops Mgr | CFO | 1 day |
| 5 | **Dispute Window**: Approved sheets published to Sales Reps via portal/email; 3-day window for reps to raise disputes or missing deal inquiries. | Sales Reps | Sales Ops Mgr | 3 days |
| 6 | **Payroll Integration**: Final commission figures approved and pushed to HR/Payroll module (W10) for inclusion in the mid-month payroll run. | Payroll Clerk | HR Manager | 2 hours |

### System Touchpoints
- Commission calculation engine with tiered rates based on margin performance and target achievement (W228.2)
- Collections-based commission trigger: commission calculated on realized collections (paid invoices), not invoiced sales, to mitigate bad debt risk (W228.1)
- Automated deduction of returns (W12) and credit notes against rep commissions with shared-deal split logic (W228.3)
- Commission approval workflow with Sales Director and CFO digital sign-off (W228.4)
- Rep-facing commission portal for transparency and dispute submission (W228.5)
- Payroll integration (W10) for mid-month payroll inclusion of final commission amounts (W228.6)

### Time Estimate
Monthly cycle: ~5.5 days total (2 hours data pull + 1 hour calculation + 30 min adjustments + 1 day approval + 3 days dispute window + 2 hours payroll integration). Sales Operations Manager spends ~4–5 hours/month on commission processing; additional 3-day window is passive (waiting for rep disputes).

### Pain Points / Risks
- Collections-based commission (vs. invoice-based) means reps may wait 60–90+ days after a sale to receive commission, reducing motivational impact and creating cash flow uncertainty for reps, especially on large project sales with milestone billing (W165).
- Tiered margin-based calculation is complex and opaque to reps; disputes during the 3-day window are frequent, consuming Sales Operations time and creating friction between reps and management.
- Shared commission deals between reps (split accounts) require manual allocation adjustments that are error-prone and contested; the system handles splits but does not capture the rationale behind non-standard split percentages.
- Returns and credit notes deducted from current-month commission may relate to sales from prior months, creating perceived unfairness when reps are penalized for issues outside their control (e.g., vendor quality defects leading to customer returns).

---

### Staffing Implication
Monthly cycle requires ~4–5 hours of active Sales Operations Manager time + 1 day for CFO approval + 2 hours Payroll Clerk integration. With ~50 reps, the tiered calculation and dispute window are the main effort areas. Absorbed by existing Sales Operations and Finance roles. No incremental headcount.

### System Touchpoints (Project & Trade Sales)
- Quote-to-Contract (Master Sales Order) conversion
- Project-specific Price Books with locked-in pricing
- ATP (Available-to-Promise) check across multi-location inventory
- Credit limit check including "In-Flight" project commitments
- Staged delivery (Call-Off) management with balance tracking
- Retention Receivable accounting
- Commission calculation engine integrated with AR collections and Payroll (W10)
- Integration with W19 (Logistics) and W8 (AR)

---

## W229. B2B Customer Credit Limit Exception & Escalation

| Field | Detail |
|---|---|
| **Trigger** | Staged delivery (Call-Off) (W164) is blocked at release because customer exceeds credit limit or has overdue invoices |
| **Frequency** | ~30–50 exception requests/month |
| **Volume** | Exception values: PHP 100K to PHP 5M+ |
| **Owner** | B2B Credit Manager |
| **Participants** | B2B Credit Manager, Sales Rep, Credit Control Clerk, VP Sales, CFO, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **System Hold**: System automatically blocks Release Order (W164.3) due to credit limit breach or overdue balance; triggers alert to Sales Rep and Credit Control Clerk | System | B2B Credit Manager | Automated |
| 2 | **Status Verification**: Credit Control Clerk reviews account (AR ledger, average payment days, credit utilization); consults with Sales Rep to check for payments in transit or bank guarantees | Credit Control Clerk | — | 30 min |
| 3 | **Escalation Request**: Sales Rep submits "Credit Exception Request" in system, detailing project urgency, invoice value, payment commitment date, and attachment of client commitment letter | Sales Rep | B2B Credit Manager | 20 min |
| 4 | **Tiered Routing**: System routes the request based on exception value for digital approval:<br>• Up to PHP 100K: Approved by Credit Manager;<br>• PHP 100K to PHP 1M: Approved by Credit Manager + VP Sales;<br>• Above PHP 1M: Approved by CFO | System | — | Automated |
| 5 | **Temporary Release**: Approver grants exception; Credit Manager enters a "Temporary Credit Override" in ERP with a strict expiry date (typically 7–14 days); system releases blocked order for dispatch | B2B Credit Manager / CFO | — | 1 hour |
| 6 | **Auto-Lock Enforcement**: System tracks payment; if commitment not fulfilled within override window, system automatically locks B2B customer account and suspends all subsequent deliveries | System | B2B Credit Manager | Automated |

### System Touchpoints
- Credit control engine (real-time balance and credit-utilization check)
- B2B Credit Exception Request electronic form with file attachments
- Tiered workflow routing based on exception monetary value
- Temporary credit limit overrides with auto-expiry and account locking
- Integration with W164 (call-off fulfillment) and W8 (AR accounts)

### Time Estimate
Per exception: ~1–2 hours total (automated hold + 30 min status verification + 20 min escalation request + automated routing + 1 hour temporary release). With ~30–50 exceptions/month, B2B Credit Manager spends ~30–50 hours/month on credit exception management.

### Pain Points / Risks
- Auto-lock enforcement (W229.6) is operationally blunt — locking a B2B customer's entire account suspends ALL deliveries, including unrelated projects with good payment history, potentially damaging client relationships beyond the specific overdue invoice.
- Temporary credit overrides (7–14 days) are often insufficient for government and institutional clients with 60–120 day payment cycles; exceptions are repeatedly renewed, effectively becoming permanent credit extensions without formal limit increase.
- Sales Rep pressure on Credit Manager to approve exceptions is intense — high-value project relationships and personal sales targets create conflict between commercial urgency and credit risk management.
- CFO approval for exceptions above PHP 1M introduces significant delay (1–3 days for executive review), during which project deliveries are suspended and client relationships deteriorate; project timelines are jeopardized.


### Staffing Implication
~30–50 exceptions/month = ~30–50 hours/month for B2B Credit Manager (primary owner). Credit Control Clerk: ~15–25 hours/month for status verification. VP Sales: ~4–8 hours/month approving mid-tier exceptions. CFO: ~2–4 hours/month for exceptions above PHP 1M. Absorbed by existing Credit and Finance roles. No incremental headcount.

---

## W421. Batch/Shade Reconciliation for Large Project Sales

| Field | Detail |
|---|---|
| **Trigger** | Large-scale quotation (e.g., > 100 sqm) for tiles, flooring, or paint requiring color consistency |
| **Frequency** | Weekly per Project Sales Rep |
| **Volume** | ~5–10 project quotes/month per store |
| **Owner** | Project Sales Lead |
| **Participants** | Sales Rep, Warehouse Supervisor, Inventory Control, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Requirement Definition**: Sales Rep identifies "Single Batch" requirement for a project to ensure color/shade uniformity (e.g., "Must be same shade code for 500 sqm of 60x60 Granite Tiles") | Sales Rep | — | 30 min |
| 2 | **Lot Availability Check**: Sales Rep checks ERP for Lot/Batch attributes (Shade Code, Batch Date) across available inventory in DC and regional stores | Sales Rep | Inventory Control | 15 min |
| 3 | **Physical Verification**: Warehouse Supervisor performs physical check of pallets to confirm shade codes and "Manufacture Date" match ERP records; flags any "Mixed Pallets" | Warehouse Supervisor | DC Manager | 1 hour |
| 4 | **Shade Reservation**: Sales Rep creates a "Shade-Locked" Reservation in ERP; system prevents these specific Lots from being sold to walk-in customers or other orders | Sales Rep | Inventory Control | 10 min |
| 5 | **Sample Approval**: Rep provides physical sample of the specific shade to the customer/architect for sign-off | Sales Rep | — | 1 day |
| 6 | **Staged Release**: As project progresses, Warehouse releases the reserved Lot/Batch for delivery (W164); system warns if any attempt is made to substitute with a different shade | Warehouse Clerk | DC Manager | Per W164 |
| 7 | **Shortage Management**: If project requires more stock than currently available in a single shade: Rep coordinates with Buyer (W2B) to place a special "Single Run" order with the manufacturer | Sales Rep / Buyer | Category Mgr | 2 days |

### System Touchpoints
- ERP Lot/Batch tracking with mandatory "Shade/Tone" attribute (INV-008, INV-013)
- Hard-allocation reservation engine for specific Lots (W421.4)
- Warehouse mobile app for shade verification and pallet scanning during loading
- Integration with W162 (Quotation), W164 (Staged Delivery), and W2B (Import PO for special runs)

### Time Estimate
Total process: 2–3 days (Verification: 1 hour; Sample Approval: 1 day; Coordination: 2 days). Rep spends ~2 hours per project on reconciliation and reservation.

### Pain Points / Risks
- **Inventory Fragmentation**: Having 1,000 units in stock but split across 5 different shade codes makes them unusable for a single large project, leading to "overstock" that is actually a shortage.
- **Loading Errors**: Warehouse staff accidentally picking a "matching" SKU but with a different shade code during high-volume dispatch, leading to costly project rework and tile removal.
- **Batch Exhaustion**: Customer requires a top-up of 10 sqm to finish a project, but the specific shade is sold out; impossible to match perfectly with newer production runs.
- **Reservation Bloat**: Large quantities of stock "locked" for projects that may never materialize, preventing sales to other ready buyers.

### Staffing Implication
- **Project Sales Rep**: ~2 hours/project for shade management; ~10–20 hours/month. Absorbed.
- **Warehouse Supervisor**: ~1 hour/project for physical pallet verification. Absorbed within DC management routines.
- **No incremental headcount.**

---

## W792. Project Change Order Management & Margin Re-Impact Assessment

| Field | Detail |
|---|---|
| **Trigger** | Customer requests scope addition, modification, or deletion during active project execution (W164); or contractor/site condition triggers scope change |
| **Frequency** | Ad-hoc; typically 3-8 change orders per active project |
| **Volume** | ~50-100 change orders/year across all active projects |
| **Owner** | Project Manager (Trade & Project Sales) |
| **Participants** | Customer, Category Manager, Finance, Procurement, VP for Sales |

### Background

BuildRight's project-based B2B sales (W162-W166) handle large construction and renovation projects for developers, contractors, and institutions. During project execution, customers frequently request scope changes: additional materials, quantity changes, product substitutions, delivery schedule changes, or site-specific modifications. Each change order directly impacts project margin and delivery schedule. Without structured change order management, BuildRight delivers additional scope without corresponding revenue recovery, eroding project margins by 5-15%. This workflow ensures every scope change is documented, priced, approved, and tracked.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Change Request Receipt**: Customer submits change request verbally, via email, or through project portal: describes desired change (additional quantity, new product, delivery reschedule, scope deletion); Project Manager logs change request in system with unique Change Order (CO) number and links to parent project per W164 | Project Manager | — | 30 min |
| 2 | **Scope & Cost Impact Assessment**: Project Manager coordinates with Category Manager and Procurement to assess: (a) material availability and lead time for changed scope; (b) cost impact: revised material cost per W163 pricing, additional logistics cost, any expedite fees; (c) schedule impact: does change delay or compress delivery timeline; (d) margin impact: revised project margin calculation comparing original bid margin to post-change margin | Project Manager / Category Manager | VP for Sales | 1-2 days |
| 3 | **Customer Pricing & Proposal**: Project Manager prepares change order proposal for customer: (a) description of change; (b) revised quantity and unit pricing per W163 contract price book or current market price; (c) revised total project value; (d) schedule impact if any; (e) validity period (typically 7 days); (f) for margin-erosive changes: recommend scope trade-offs to maintain original margin target | Project Manager | VP for Sales | 1 day |
| 4 | **Customer Approval**: Customer reviews and approves, negotiates, or rejects the change order: (a) approved: proceed to Step 5; (b) negotiated: iterate pricing or scope until agreement; (c) rejected: document rejection and proceed with original scope | Project Manager | Customer | 1-5 days |
| 5 | **Internal Approval**: For change orders exceeding DOA thresholds: (a) CO value <PHP 100K: Project Manager approves; (b) PHP 100K-500K: VP for Sales approves; (c) >PHP 500K: VP for Sales + CFO approves; (d) system updates project budget, delivery schedule, and revenue forecast | Project Manager / VP for Sales | CFO (if >PHP 500K) | 1-2 days |
| 6 | **Execution**: Procurement and logistics execute changed scope per updated delivery schedule: (a) new Purchase Orders raised if additional materials needed per W2; (b) delivery schedule updated in W164; (c) warehouse team notified of quantity/schedule changes; (d) system links CO to original project for traceability | Procurement / Logistics | Project Manager | Per W164 timeline |
| 7 | **Billing Update**: Finance updates project billing per W165: (a) change order value added to next progress billing or milestone invoice; (b) if CO is a scope reduction: issue credit note per W101; (c) retention computation updated if total project value changed; (d) updated project margin reported in monthly project P&L per W85 | Finance | Project Manager | 1-2 days |

### System Touchpoints

- Project Management module with change order tracking linked to W164 project
- Pricing engine per W163 for real-time margin impact calculation
- Approval routing per W686 for DOA-compliant change order approval
- Procurement integration per W2 for additional PO generation
- Billing integration per W165 for updated progress billing
- Project P&L reporting per W85 for margin monitoring

### Pain Points / Risks

- **Undocumented scope creep**: project team delivers additional scope based on verbal customer requests without formal change order; margin erodes silently; mitigated by mandatory CO logging before any delivery change
- **Margin-erosive change orders**: customer pushes for scope additions at original pricing (no price increase for additional scope); each undocumented change can erode project margin by 1-3%
- **Change order approval delays**: customer takes 1-2 weeks to approve change order while project delivery must continue; BuildRight bears risk of delivering without committed revenue
- **Compounding schedule impact**: multiple change orders on the same project can compound schedule delays, causing penalty clauses to trigger per W165
- **Material availability for changed scope**: change orders requiring new SKUs not in the original project price book may face procurement lead time challenges

### Staffing Implication

- **Project Manager**: 50-100 change orders/year × ~2 days per CO = ~100-200 days/year; absorbed by existing Project Manager team (2-3 FTEs) as part of project execution duties
- **Category Manager**: 2-4 hours/month per active project on cost impact assessments; absorbed by existing Category Manager role
- **No incremental headcount**.

### Time Estimate

- Per change order: 3-10 days from request to approved execution (30 min logging + 1-2 days assessment + 1 day proposal + 1-5 days customer approval + 1-2 days internal approval)
- **Total annual CO management effort**: ~200-400 person-days across all projects

---

## W793. Project Close-Out, Final Reconciliation & Warranty Handover

| Field | Detail |
|---|---|
| **Trigger** | Final project delivery completed; all call-off orders per W164 fulfilled |
| **Frequency** | Per completed project |
| **Volume** | ~20-30 project completions/year |
| **Owner** | Project Manager (Trade & Project Sales) |
| **Participants** | Customer, Finance, Category Manager, Procurement, VP for Sales, Internal Audit |

### Background

BuildRight's project-based B2B sales complete 20-30 large projects per year (construction material supply for developers, contractors, and institutions). After the last delivery, the project enters close-out: final delivery reconciliation, punch list resolution, retention billing, warranty documentation, and financial close. Without structured close-out, BuildRight leaves retention money uncollected, warranty commitments undocumented, and project financial performance unanalyzed. This workflow completes the project lifecycle from W162 quotation through final financial settlement.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Delivery Reconciliation**: Project Manager reconciles all deliveries against the project contract: (a) compare total quantities delivered per W164 call-off orders vs. contracted quantities per W163; (b) identify over-deliveries (customer received more than contracted) and under-deliveries (shortfall); (c) reconcile all change orders (W792) against original scope; (d) produce Delivery Reconciliation Report with variance analysis | Project Manager | VP for Sales | 2-3 days |
| 2 | **Customer Punch List Resolution**: Customer identifies any outstanding issues: (a) damaged or defective materials delivered but not yet replaced; (b) pending deliveries or backorders; (c) quality concerns requiring replacement or credit; (d) Project Manager coordinates resolution with Procurement and warehouse; (e) all punch list items tracked to closure with target dates | Project Manager | Customer | 1-4 weeks |
| 3 | **Final Invoice & Retention Billing**: Finance issues final project invoice: (a) reconcile all progress billings per W165 against total delivered value; (b) bill remaining retention amount per contract terms (typically 10% retention released 30-90 days after completion); (c) adjust for any credit notes from damaged/returned items; (d) final invoice includes all approved change orders per W792 | Finance | Project Manager | 2-3 days |
| 4 | **Warranty Documentation Package**: Project Manager assembles warranty documentation for customer: (a) manufacturer warranties for all products supplied; (b) BuildRight standard warranty terms per product category; (c) warranty claim process instructions (W33); (d) batch/lot traceability for paint and chemical products per W421 shade reconciliation; (e) digital warranty package delivered to customer via project portal | Project Manager | Category Manager | 1-2 days |
| 5 | **Project Financial Close**: Finance closes the project financially: (a) calculate final project margin (actual revenue vs. actual cost including all change orders); (b) compare actual margin to bid margin per W162; (c) post all remaining accruals and provisions; (d) release project-specific inventory reservations; (e) close project in ERP with final P&L | Finance | CFO | 2-3 days |
| 6 | **Project Performance Review**: VP for Sales conducts post-project review with Project Manager: (a) margin performance vs. target; (b) change order frequency and impact; (c) delivery on-time performance; (d) customer satisfaction feedback; (e) lessons learned for future bid pricing per W162; (f) update competitive intelligence database per W403 for win/loss analysis | VP for Sales | Project Manager | 2-4 hours |
| 7 | **Record Archive**: All project documents archived per W255: (a) quotation and bid documents per W162; (b) contract and pricing agreement per W163; (c) all call-off orders per W164; (d) change orders per W792; (e) delivery receipts and proof of delivery; (f) invoices and payment records per W165; (g) warranty documentation; (h) retention: 10 years per BIR requirement for financial records | Project Manager / Finance | VP for Sales | 1 day |

### System Touchpoints

- Project Management module with close-out checklist and milestone tracking
- Delivery reconciliation report generator comparing W164 call-offs to W163 contract
- Billing module per W165 for final invoice and retention release
- Warranty documentation generator linked to Item Master and batch/lot records
- Project P&L module per W85 for final margin analysis
- Competitive intelligence database per W403 for lessons learned
- Document Management System per W255 for record archival
- CRM integration per W103 for customer relationship continuity

### Pain Points / Risks

- **Retention collection delays**: customers often delay retention payment beyond contractual terms; 10% retention on a PHP 50M project = PHP 5M in delayed cash collection; mitigated by automated retention aging alerts per W108
- **Incomplete delivery reconciliation**: without careful reconciliation, BuildRight may have delivered more than contracted without charging, or less than contracted without credit resolution
- **Warranty exposure**: undocumented warranty commitments create open-ended liability; warranty documentation package ensures clear scope and duration
- **Project margin erosion discovered late**: if change orders were not properly tracked during execution, the close-out margin analysis reveals the true erosion — often 5-15% below target
- **Punch list items lingering for months**: customers may delay punch list closure to retain leverage for retention release; BuildRight must enforce contractual timelines
- **Customer insolvency during close-out**: if the customer experiences financial difficulty between final delivery and retention payment, retention may become uncollectible

### Staffing Implication

- **Project Manager**: 2-4 days per project close-out × 20-30 projects/year = 40-120 days/year; absorbed by existing PM team as part of project lifecycle management
- **Finance**: 2-3 days per project for financial close; absorbed by existing Finance team as part of month-end close cycle
- **No incremental headcount**.

### Time Estimate

- Delivery reconciliation: 2-3 days
- Punch list resolution: 1-4 weeks (depends on customer responsiveness)
- Final invoice & retention: 2-3 days
- Warranty documentation: 1-2 days
- Financial close: 2-3 days
- Performance review: 2-4 hours
- Record archive: 1 day
- **Total per project**: 2-6 weeks from last delivery to full close-out (punch list resolution is the variable)

## W918. Customer Project Budget Tracking & Material Cost Variance Management

| Field | Detail |
|---|---|
| **Trigger** | Project quotation acceptance (W162); staged delivery call-off (W164); or monthly project billing cycle for active B2B projects |
| **Frequency** | ~80–120 active B2B projects at any time; ~40–60 monthly budget reviews |
| **Volume** | Average active project value: PHP 500,000–10M; total active project portfolio: ~PHP 200–400M |
| **Owner** | Trade Sales Manager |
| **Participants** | Trade Sales Manager, Customer (project owner/contractor), Category Manager (pricing), Supply Planning (material availability), Finance (billing/collection), Project Coordinator |

### Background

BuildRight's B2B project customers (30% trade + 10% corporate = 40% of revenue) purchase materials for construction, renovation, and fit-out projects spanning weeks to months. Unlike walk-in retail purchases where the transaction is instantaneous, project sales involve: (a) initial quotation with material list (BOM) and estimated quantities per W162; (b) staged deliveries over the project duration per W164; (c) progressive billing and milestone payments per W165; and (d) project close-out with retention release per W793. Throughout this lifecycle, material costs may deviate from the original quotation due to: price changes (vendor price increases, FX fluctuations on imported items), quantity changes (customer adds scope, site waste exceeds estimate, measurement errors), product substitutions (specified item unavailable, customer upgrades), and delivery logistics (split deliveries, urgent requests). Without formal budget tracking, these variances accumulate invisibly — the project that was quoted at PHP 3M may ultimately cost PHP 3.5M, eroding both BuildRight's margin and the customer's budget. This workflow establishes real-time project budget tracking with variance alerts, margin monitoring, and proactive customer communication, ensuring project profitability for BuildRight and budget predictability for the customer.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Project Budget Establishment**: (a) upon quotation acceptance per W162, system creates project budget record from the approved quotation: line items with quoted quantities, quoted unit prices, quoted line totals, and quoted project total; (b) budget categorized by: material categories (lumber, cement, tiles, plumbing, electrical, paint, fixtures), delivery stages (stage 1, 2, 3 per W164), and cost types (materials, delivery fees, installation services, taxes); (c) margin structure: system stores both the quoted sell price and BuildRight's cost (from standard cost per W85 or negotiated purchase price per W163) for real-time margin tracking; (d) project budget shared with customer via project portal or email: itemized material list with quoted prices, delivery schedule, payment schedule, and terms; (e) project budget linked to: customer credit limit per W24 (total project value counts against credit exposure), customer account per W8 (project invoices feed AR), and replenishment planning per W31 (material requirements for active projects factor into demand forecast) | Trade Sales Manager / System | — | 30–60 min per project |
| 2 | **Real-Time Budget Consumption & Variance Tracking**: (a) every project-related transaction automatically updates budget consumption: call-off delivery per W164 (quantity delivered × current sell price), product substitution per W279 (new item price vs. original), additional scope per W792 (change order with revised budget), and credit notes per W101 (returns reduce consumption); (b) system maintains running budget status: total budget, consumed budget (delivered × price), committed budget (confirmed future orders), remaining budget, and margin % (consumed revenue vs. consumed cost); (c) variance types tracked: (i) price variance: actual sell price differs from quoted price (due to price changes, substitutions, upgrades); (ii) quantity variance: actual quantity differs from quoted quantity (due to scope changes, waste, measurement errors); (iii) mix variance: different products purchased than originally quoted; (d) automated variance alerts: (i) Amber: total project variance > 5% or individual line variance > 10% → Trade Sales Manager notification; (ii) Red: total project variance > 10% or margin dropping below minimum threshold → Trade Sales Manager + Finance Manager notification; (iii) Black: total project value exceeding credit limit → automatic order block per W888 until credit limit increased per W229 | System / Trade Sales Manager | Trade Sales Manager | Automated |
| 3 | **Monthly Project Budget Review & Customer Communication**: (a) monthly (or per delivery stage): Trade Sales Manager reviews project budget status with customer: original budget vs. current consumption, remaining budget, known variances and explanations, upcoming deliveries and expected costs, and any anticipated price changes from BuildRight or vendor; (b) if variance is favorable (under budget): customer appreciates transparency and BuildRight strengthens relationship; (c) if variance is unfavorable (over budget): (i) Trade Sales Manager explains root cause (price increase from vendor per W633, quantity increase from scope change, substitution due to unavailability); (ii) options presented to customer: accept variance and adjust project budget, substitute lower-cost alternatives per W279, reduce scope, or negotiate revised pricing per W163; (d) revised budget documented as formal change order per W792 with customer sign-off; (e) margin recovery: if project margin has dropped below target, Trade Sales Manager works with Category Manager to identify: bulk discount renegotiation with vendors per W631, alternative product sourcing, or price adjustment for remaining deliveries (if contract permits); (f) review documented in project file and transmitted to Finance for AR billing accuracy | Trade Sales Manager / Customer / Category Manager | VP Store Operations | 30–60 min per project per review |
| 4 | **Project Margin Monitoring & Intervention**: (a) Finance tracks project margin in real-time: revenue recognized per delivery (PFRS 15 over-time or point-in-time per W487) vs. cost of goods delivered (standard cost or actual cost per W85); (b) weekly margin flash report for top 20 active projects by value; (c) margin intervention triggers: (i) project margin < 20% (below target): Finance Manager review with Trade Sales Manager — identify cause and recovery plan; (ii) project margin < 15% (minimum floor): VP Store Operations escalation — no further deliveries without margin recovery plan approved; (iii) project margin negative: CFO escalation — immediate review, potential contract renegotiation per W792; (d) margin analysis shared with: Merchandising (for pricing strategy per W107), Procurement (for vendor cost negotiation per W631), and Supply Planning (for demand forecast accuracy per W31); (e) at project close-out per W793: final margin calculated and compared to original quotation margin — variance analysis feeds into pricing accuracy improvement for future quotations per W162 | Finance / Trade Sales Manager | CFO | 4–6 hours/week |
| 5 | **Project Budget Analytics & Process Improvement**: (a) monthly: active project portfolio summary — total value, average margin, variance distribution (favorable vs. unfavorable), and average project duration; (b) quarterly: completed project analysis — quotation accuracy (% of projects completed within 5% of original budget), margin achievement rate (% of projects achieving target margin), variance root cause Pareto analysis (top 5 causes of budget overruns), and customer satisfaction correlation (are projects with accurate budgets rated higher?); (c) semi-annual: pricing calibration — adjust quotation pricing models per W162 based on actual project cost data; update material waste factors (e.g., tile breakage allowance) based on actual project data; and refine delivery cost estimates based on actual logistics data per W680; (d) annual: project sales program ROI — revenue, margin, customer retention for project customers vs. non-project customers, and quotation-to-close conversion rate | Trade Sales Manager / Finance / Merchandising / System | VP Store Operations | 6–8 hours/month |

### System Touchpoints

- Project quotation module (W162) for budget establishment from quotation
- Call-off order system (W164) for delivery tracking against budget
- POS/order management for project transaction recording
- Pricing system (W163) for current sell price and margin calculation
- Cost accounting (W85) for real-time margin tracking
- Change order system (W792) for budget revision documentation
- Credit management (W24/W888) for credit limit monitoring
- AR billing (W8/W165) for invoice generation aligned to budget
- Product substitution system (W279) for substitute tracking
- Supply planning (W31) for material availability
- Customer communication module (W708) for budget review notifications
- BI dashboard for project portfolio analytics
- Revenue recognition module (W487) for PFRS 15 compliance

### Pain Points / Risks

- **Customer disputes over variances**: customers may dispute charges that exceed original quotation; mitigated by transparent real-time budget tracking accessible to customer, proactive communication at each variance event, and formal change order documentation per W792
- **Margin erosion from untracked substitutions**: Sales Associates substituting products without updating project budget; mitigated by system-enforced substitution flagging (any substitution on a project-linked order triggers budget update) and Trade Sales Manager review
- **Complexity for small projects**: full budget tracking is overkill for PHP 50,000 projects; mitigated by tiered approach — projects > PHP 500,000 receive full budget tracking, projects PHP 100,000–500,000 receive simplified tracking, projects < PHP 100,000 use standard POS per W5B
- **Data quality**: inaccurate project budgets from poorly prepared quotations; mitigated by quotation accuracy KPI and semi-annual pricing calibration
- **Credit exposure accumulation**: multiple active projects for the same customer may exceed credit limit; mitigated by portfolio-level credit monitoring per W572 and cross-project credit exposure dashboard

### Staffing Implication

- **Trade Sales Manager**: ~4–6 hours/week on budget reviews and customer communication across ~80–120 active projects; absorbed by existing role
- **Finance Analyst (Project)**: ~4–6 hours/week on margin monitoring and intervention; absorbed by existing team
- **Project Coordinator**: ~2–3 hours/week on data entry and documentation; absorbed by existing role
- **No incremental headcount**

### Time Estimate

- Budget establishment: 30–60 min per project
- Monthly budget review: 30–60 min per project
- Weekly margin monitoring: 4–6 hours/week (consolidated)
- Monthly analytics: 6–8 hours
- **Total per active project per month**: ~60–90 min of staff time
