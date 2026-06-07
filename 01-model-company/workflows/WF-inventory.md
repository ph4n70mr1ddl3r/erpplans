# Inventory Management Workflows

> Replenishment, cycle counting, transfers, consignment, physical inventory, backorders, promo stock allocation, damaged & defective goods disposition, inventory adjustment & shrinkage authorization, multi-channel inventory allocation governance, inter-store/inter-DC stock rebalancing, quarantine & recertification, SLOB provisioning & liquidation, inventory count reconciliation & variance root cause analysis, obsolescence identification & write-off management, and seasonal inventory build-down & transition execution.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W4. Store Replenishment (DC → Store)](#w4-store-replenishment-dc-store)
- [W6. Cycle Counting & Inventory Accuracy](#w6-cycle-counting-inventory-accuracy)
- [W22. Stock Transfers (Store-to-Store & Inter-DC)](#w22-stock-transfers-store-to-store-inter-dc)
- [W23. Consignment Inventory Operations](#w23-consignment-inventory-operations)
- [W42. Annual Physical Inventory Execution](#w42-annual-physical-inventory-execution)
- [W56. Customer Backorder Management](#w56-customer-backorder-management)
- [W57. Promotional Stock Allocation & Pre-Positioning](#w57-promotional-stock-allocation-pre-positioning)
- [W91. Damaged & Defective Goods Disposition](#w91-damaged-defective-goods-disposition)
- [W92. Inventory Adjustment & Shrinkage Authorization](#w92-inventory-adjustment-shrinkage-authorization)
- [W105. Multi-Channel Inventory Allocation & Priority Governance](#w105-multi-channel-inventory-allocation-priority-governance)
- [W154. Proactive Store Inventory Rebalancing (Stock Push)](#w154-proactive-store-inventory-rebalancing-stock-push)
- [W204. Regional Stock Rebalancing & Inter-Store Expedited Transfers](#w204-regional-stock-rebalancing-inter-store-expedited-transfers)
- [W214. Store-to-Store Expedited Transfers (Customer-Initiated)](#w214-store-to-store-expedited-transfers-customer-initiated)
- [W218. Inter-DC Stock Rebalancing (Stock Push)](#w218-inter-dc-stock-rebalancing-stock-push)
- [W219. Store Inventory Quarantine & Recertification](#w219-store-inventory-quarantine-recertification)
- [W220. Slow-Moving & Obsolete Inventory (SLOB) Provisioning & Liquidation](#w220-slow-moving-obsolete-inventory-slob-provisioning-liquidation)
- [W514. Inventory Count Reconciliation & Variance Root Cause Analysis](#w514-inventory-count-reconciliation-variance-root-cause-analysis)
- [W587. Inventory Obsolescence Identification & Write-Off Management](#w587-inventory-obsolescence-identification-write-off-management)
- [W588. Seasonal Inventory Build-Down & Transition Execution](#w588-seasonal-inventory-build-down-transition-execution)

---

## W4. Store Replenishment (DC → Store)

| Field | Detail |
|---|---|
| **Trigger** | System generates replenishment suggestion based on min/max or demand forecast |
| **Frequency** | 2–3 physical deliveries per store per week; ~5,000 replenishment orders/month total (each delivery truck carries 2–3 orders consolidated for that store) |
| **Volume** | ~167 orders/day across all DCs (~33 per DC/day); avg ~50 lines per order |
| **Owner** | Supply Planner |
| **Participants** | Supply Planner, DC Pick/Pack/Ship team, Truck Driver, Store Receiving Clerk, Store Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System calculates replenishment needs per store: current stock vs. min/max or forecast | System | — | Automated (nightly) |
| 2 | Supply Planner reviews suggested orders each morning; adjusts for promotions, seasonality, store-specific factors | Supply Planner | Supply Planning Manager | 2–3 hours/day |
| 3 | Planner confirms orders; system groups into waves by DC and delivery route | Supply Planner | Supply Planning Manager | 1 hour/day |
| 4 | DC receives pick wave; WMS assigns pick tasks to staff by zone | WMS / DC Supervisor | DC Supervisor | 5 min (assignment) |
| 5 | Pickers pick items from bins per RF gun direction; scan-confirm each item | Picker | DC Supervisor | 2–4 hours/wave |
| 6 | Packers pack into store-labeled totes/cases; scan-confirm shipment | Packer | DC Supervisor | 1–2 hours/wave |
| 7 | Load truck per route sequence (multi-drop) | Loading Crew | DC Supervisor | 30–60 min |
| 8 | System creates Transfer Order; in-transit inventory created | System | — | Automated |
| 9 | Truck departs DC; ETA communicated to store | Driver | DC Dispatch | — |
| 10 | Store Receiving Clerk unloads truck; scans each item/case against Transfer Order | Receiving Clerk (Store) | Store Manager | 30–60 min |
| 11 | Discrepancies (shortage, damage) flagged in system; DC notified | Receiving Clerk (Store) | Store Manager | 5 min if any |
| 12 | Store confirms receipt; in-transit inventory becomes store inventory | Receiving Clerk (Store) | Store Manager | 5 min |
| 13 | Replenishment moved to sales floor or backroom stock | Stock Associate | Department Supervisor | 30–60 min |

**Total cycle time**: 1–3 days from order creation to store shelf

### System Touchpoints
- Dual-sourced item management: for SKUs that are replenished through both DC delivery (W4) and DSD (W18) — typically cement, lumber, and bulky building materials — system maintains a primary/secondary supply channel indicator per SKU per store; ATP calculation aggregates on-hand + incoming DC replenishment + incoming DSD orders; when auto-replenishment (W4.1) generates a transfer order for a dual-sourced SKU, system checks if a DSD delivery is already scheduled within the replenishment lead time and adjusts the transfer order quantity accordingly to avoid overstocking; Store Manager can override the default supply channel per SKU via handheld; monthly: Supply Planner reviews dual-sourced SKU inventory levels to identify overstocking or conflicting deliveries (W4, W18)
- Replenishment calculation engine (min/max, forecast-based) (W4.1)
- Constrained allocation rules: when available supply is insufficient for all stores, system applies configurable allocation logic (e.g., equal distribution, rank by store revenue, prioritize A-stores) — Planner reviews and adjusts before confirming (W4.2)
- Store order creation and wave planning (W4.3)
- WMS pick/pack/ship with RF scanning (W4.4–6)
- In-transit inventory visibility (W4.8)
- Store receiving with discrepancy handling (W4.10–12)
- Real-time inventory update at both DC and store (W4.8, W4.12)
- FEFO (First Expired First Out) directed picking: for items with shelf-life tracking (paint, adhesives, chemicals, cement), WMS directs pickers to pick the earliest-expiring batch first; system sequences pick tasks by expiry date within the same SKU; ensures fresher stock remains in DC for later dispatch (W4.5)
- Inventory ownership clarification: goods moving from DC to store in W4 are Depot Inc. inventory at both locations; DC facilities are operated by Logistics Inc. (which charges monthly warehousing/distribution fees per W14), but Depot Inc. owns the merchandise throughout; W4 transfer orders are intra-entity inventory movements (no per-TO IC invoice); IC invoicing applies only to inter-entity goods transfers (W22) or service fees (W14)
- New store demand ramp-up (first 90 days): for newly opened stores (W16), auto-replenishment parameters (ROP, safety stock, min/max) derived from comparable store averages may not reflect actual local demand patterns during the ramp-up period; during the first 90 days post-opening, Supply Planner overrides auto-replenishment with manual review — (a) system flags all replenishment orders for new stores with "Ramp-Up" status requiring Planner confirmation (no auto-release), (b) Planner reviews suggested orders daily against early sell-through data and adjusts quantities based on actual demand velocity observed in the first weeks, (c) Store Manager provides daily feedback on fast-moving and slow-moving items via the W4B store-initiated replenishment request channel, (d) after 90 days, Demand Planner analyzes accumulated sales data to calculate store-specific ROP/safety stock parameters per W31.8; system transitions the store from "Ramp-Up" to standard auto-replenishment; parameters reviewed again at 180 days; this manual override period prevents both overstocking (tying up working capital in a new store) and stockouts (damaging customer first impressions)
- Constrained allocation rule governance: when available supply is insufficient for all stores, system applies configurable allocation logic; Supply Planning Manager defines allocation method per SKU or category (equal distribution, rank by store revenue, prioritize A-stores, proportional to historical demand); allocation rules reviewed and approved by VP Supply Chain; rule changes logged with old method, new method, reason, approver, and effective date; monthly: Supply Planning Manager reviews allocation fairness dashboard showing per-store fill rate and allocation share; fairness disputes escalated by Store Managers through W4B channel feed into allocation rule review; quarterly: allocation methodology reviewed as part of W31.8 parameter governance cycle (W4.2)

### Pain Points / Risks
- Constrained allocation disputes: when DC stock is insufficient, Supply Planners face pressure from Store Managers and Regional Managers to prioritize their stores, creating internal friction that the allocation governance framework (W105) attempts to mediate but cannot fully eliminate.
- New store ramp-up overstocking risk: during the 90-day ramp-up period, manually overriding auto-replenishment parameters is labor-intensive and prone to error — early overestimation ties up working capital in slow-moving stock at new locations.
- Dual-sourced SKU replenishment conflicts: when both DC delivery (W4) and DSD (W18) supply channels are active for the same SKU, timing mismatches can result in double-ordering, especially if the DSD schedule changes after the DC transfer order is already confirmed.
- FEFO picking compliance is inconsistent — WMS directs pickers to earliest-expiring batch, but in high-volume waves pickers sometimes bypass FEFO sequence to meet productivity targets, leading to aged stock accumulation in DC.
- In-transit inventory visibility gaps for inter-island deliveries (W66) mean Supply Planners cannot provide accurate ETAs to Store Managers during typhoon-related delays.

### Time Estimate
Daily replenishment review (steps 2–3): 2–4 hours/day for 2–3 Supply Planners. DC pick/pack/ship (steps 4–7): 4–8 hours per wave across shifts. Store receiving (steps 10–12): 30–60 min per delivery. Total end-to-end cycle: 1–3 days from order creation to store shelf.

### Staffing Implication
- **2–3 Supply Planners** (in HQ): ~167 orders/day to review. At 2–3 hours/day for review + 1 hour for wave management = 3–4 hours/day. 2–3 planners share this plus demand forecasting. Reasonable within the 30-person Supply Chain team.
- **Per DC**: 15–20 Pickers, 8–10 Packers, 4–6 Loading Crew (working in shifts to handle ~33 orders/day with ~50 lines each). Fits within ~150 DC headcount.
- **Store Receiving Clerks**: 30–60 min per delivery × 2–3 deliveries/week = ~1–3 hours/week. Absorbed by existing store receiving staff.
- **No incremental headcount beyond planned staffing.**

### W4B. Store-Initiated Replenishment Request

| Field | Detail |
|---|---|
| **Trigger** | Store Manager or Department Supervisor identifies local demand that exceeds current replenishment plan (e.g., nearby construction project, local event, weather-driven spike) |
| **Frequency** | ~100–200 store-initiated requests/month chain-wide; ~0.5–1 per store per month |
| **Volume** | Typically 5–20 SKUs per request |
| **Owner** | Supply Planner |
| **Participants** | Store Manager / Dept. Supervisor, Supply Planner, Buyer (if new PO needed) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Manager or Dept. Supervisor identifies items needing additional stock beyond automated replenishment; opens replenishment request in system (handheld or terminal) — selects SKUs, enters requested quantity, urgency (routine / expedited / emergency), and business justification (e.g., "new subdivision project starting 2 km away") | Store Manager / Dept. Supervisor | Store Manager | 10 min |
| 2 | System checks: (a) current on-hand at store, (b) current on-hand at serving DC, (c) open POs and incoming replenishment orders, (d) ATP at DC after existing commitments; presents Supply Planner with a dashboard showing the request alongside existing supply position | System | — | Automated |
| 3 | Supply Planner reviews request each morning alongside standard replenishment review (W4 step 2); evaluates: (a) is the demand legitimate and near-term, (b) does DC have available stock to fulfill without depriving other stores, (c) if expedited — can it ride on the next wave, or does it need a separate shipment | Supply Planner | Supply Planning Manager | 5–10 min/request |
| 4 | **If approved — DC has stock**: Supply Planner adds requested quantities to the next replenishment order for that store (W4 step 2); system creates a pick task in the next wave; request status updated to "Approved — Scheduled" | Supply Planner | Supply Planning Manager | 2 min |
| 5 | **If approved — DC has insufficient stock**: Supply Planner requests Buyer to expedite a PO (W2A) or arrange an inter-DC transfer (W22); request status updated to "Approved — Pending Supply"; Supply Planner tracks until supply arrives | Supply Planner / Buyer | Supply Planning Manager | 10 min |
| 6 | **If denied**: Supply Planner rejects request with reason (insufficient DC stock, lower priority than other stores, demand not validated); system notifies Store Manager; Store Manager may escalate to Regional Manager if disagreement | Supply Planner | Supply Planning Manager | 2 min |
| 7 | Fulfillment follows standard W4 pick/pack/ship process; request closed when goods received at store | Per W4 | — | Per W4 |
| 8 | Weekly: Supply Planning Manager reviews store-initiated request report — approval rate, top requesting stores, frequently requested items; flags items with high ad-hoc request frequency for ROP/safety stock adjustment per W31.8 | Supply Planning Manager | VP Supply Chain | 30 min/week |

### System Touchpoints
- Store-initiated replenishment request form in POS/terminal/handheld with SKU selection, quantity, urgency, and justification fields (W4B.1)
- Supply Planner dashboard showing request alongside current supply position (on-hand, ATP, open POs, pending replenishment) (W4B.2)
- Request status lifecycle: Submitted → Under Review → Approved (Scheduled / Pending Supply) / Denied → Fulfilled / Closed (W4B.3–7)
- Weekly request analytics: approval rate, requesting stores, frequently requested items feeding into ROP parameter review (W31.8) (W4B.8)
- Integration with W4 (replenishment order creation), W2A (expedited PO), W22 (inter-DC transfer), W31 (forecast and ROP adjustment)

### Pain Points / Risks
- Store Managers in remote or provincial locations (Visayas, Mindanao) submit a disproportionate share of ad-hoc requests because demand patterns are less predictable than Metro Manila stores, stretching Supply Planner review capacity.
- Denied requests create friction with Store Managers who have local market knowledge that the central planning team may lack; escalation to Regional Manager adds a political dimension that can slow the standard W4 replenishment cycle.
- High-frequency ad-hoc requests for the same SKUs signal that ROP/safety stock parameters are misconfigured (W31.8), but the feedback loop from W4B analytics to parameter adjustment can take 30–60 days, during which stores experience repeated stockouts.
- Emergency expedited requests that require a separate shipment (not riding the next wave) incur incremental 3PL freight cost of PHP 5,000–15,000 per trip, which is rarely tracked back to the requesting store's P&L.

### Time Estimate
Request submission (step 1): 10 min per request. Supply Planner review (steps 3–6): 5–15 min per request. Weekly analytics (step 8): 30 min/week for Supply Planning Manager. Total chain-wide: ~1 hour/day incremental for Supply Planners reviewing ~5–10 requests/day.

### Staffing Implication
- **Supply Planner**: ~100–200 requests/month ÷ 20 working days = ~5–10/day. At ~10 min each for review = ~1 hour/day incremental. Absorbed within existing 2–3 planner team.
- **Store Managers**: ~0.5–1 requests/month × 10 min = negligible.

### Staffing Implication (W4 overall)
- **2–3 Supply Planners** (in HQ): ~167 orders/day to review. At 2–3 hours/day for review + 1 hour for wave management = 3–4 hours/day. 2–3 planners share this plus demand forecasting. Reasonable within the 30-person Supply Chain team.
- **Per DC**: 15–20 Pickers, 8–10 Packers, 4–6 Loading Crew (working in shifts to handle ~33 orders/day with ~50 lines each). Fits within ~150 DC headcount.

---

## W6. Cycle Counting & Inventory Accuracy

| Field | Detail |
|---|---|
| **Trigger** | Daily schedule (rolling through all sections) |
| **Frequency** | Daily per store; each SKU counted at least once per quarter |
| **Volume** | ~700 SKUs/day per store; 200 stores × 700 = 140,000 SKU counts/day chain-wide |
| **Owner** | Department Supervisor |
| **Participants** | Stock Associate (counter), Department Supervisor (reviewer), Store Manager (approver for adjustments) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates daily count assignment by section/aisle | System | — | Automated (nightly) |
| 2 | Stock Associate retrieves count sheet on handheld/RF device | Stock Associate | Department Supervisor | — |
| 3 | Physically count each SKU in assigned section; enter quantity into device (3 Stock Associates each count ~233 SKUs/day, taking ~40 min each at ~10 sec/SKU) | Stock Associate | Department Supervisor | ~40 min per associate |
| 4 | System compares physical count to system count; flags variances | System | — | Automated |
| 5 | For flagged items: Stock Associate recounts (blind recount) | Stock Associate | Department Supervisor | 15–30 min |
| 6 | If variance confirmed: Department Supervisor reviews and approves adjustment | Dept. Supervisor | Store Manager | 15 min |
| 7 | If adjustment > PHP 10,000 or > 5% of SKU value: Store Manager approval required | Store Manager | Store Manager | 5 min each |
| 8 | System posts inventory adjustment; audit trail recorded | System | — | Automated |
| 8a | **In-store damage discovered during operations**: Stock Associate identifies damaged item on sales floor (customer drop, water damage, forklift damage, yard weather damage); creates damage report in system with photo and cause code; Department Supervisor reviews and approves disposition: (a) markdown and sell at reduced price, (b) scrap with supervisor authorization, (c) Return to Vendor per W3.6a process; system posts inventory adjustment and loss to damage/scrapping account | Stock Associate / Dept. Supervisor | Store Manager | 10 min |
| 9 | Root cause analysis for recurring variances (theft, damage, receiving errors) | Dept. Supervisor | Store Manager | Weekly review |

**Cycle**: 35,000 SKUs ÷ 700/day = 50 working days per full cycle (~10 weeks ≈ quarterly)

### System Touchpoints
- Automated count assignment by zone/section (W6.1)
- RF device / handheld count entry (W6.3)
- Variance detection and blind recount workflow (W6.4–5)
- Inventory adjustment with tiered approval (W6.6–7)
- Immutable audit trail for all adjustments (W6.8)
- In-store damage discovery reporting with photo, cause code, and disposition workflow (W6.8a)
- Near-expiry alerting: during cycle counts, system flags items approaching expiry (configurable threshold per category, e.g., 90 days for paint, 60 days for cement); Department Supervisor reviews flagged items and initiates disposition per W13.9a (markdown), W3.6a (RTV), or W13.9b (scrap/liquidation) (W6)
- Negative inventory resolution: system generates daily negative inventory alert listing all SKU-locations where on-hand < 0; at store level, Stock Associate investigates root cause (timing lag from offline POS transactions per W5G, receiving error, mispick, or cycle count needed); at DC level, Inventory Control clerk investigates (pending GR posting, allocation error, picking error); resolution action depends on cause — recount and adjust (W6), wait for pending transaction posting, or force adjustment with supervisor approval; system blocks negative-inventory locations from ecommerce ATP availability until resolved; monthly report of negative inventory frequency by location feeds into inventory accuracy improvement initiatives

### Pain Points / Risks
- With only 3 Stock Associates per store and no slack for absenteeism, cycle counting is the first task deferred during peak trading hours, causing accuracy degradation that compounds over weeks.
- Negative inventory resolution requires immediate investigation that competes with customer-facing duties; unresolved negative inventory blocks ecommerce ATP availability (W11), directly impacting online sales.
- Near-expiry alerting during cycle counts generates disposition decisions (markdown, RTV, scrap) that require Department Supervisor approval — if the Supervisor is unavailable, expired stock accumulates on shelves in categories like paint and adhesives.
- Blind recount process adds 15–30 min per flagged section; during high-variance periods (post-promo, post-typhoon), the recount workload can exceed Stock Associate capacity, causing counting backlogs.
- In-store damage discovery (W6.8a) during cycle counts creates a dual workflow burden — the associate must simultaneously complete the count and document damage with photos and cause codes, slowing both processes.

### Time Estimate
Daily count per Stock Associate: ~40 min for ~233 SKUs. Blind recount: 15–30 min additional for flagged items. Adjustment processing: 5–15 min per adjustment (including approvals). Total per store per day: ~2–3 hours across 3 Stock Associates (counting + recounts + adjustments).

### Staffing Implication
- **3 Stock Associates per store**: Each counts ~233 SKUs/day (~40 min), with remainder of time on replenishment, receiving, damage reporting, and BOPIS picking. Current count of 3 is adequate but has no slack for absenteeism.

---

## W22. Stock Transfers (Store-to-Store & Inter-DC)

| Field | Detail |
|---|---|
| **Trigger** | Stock imbalance between locations; emergency need; inter-DC rebalancing |
| **Frequency** | ~30–40 inter-DC transfers/month; ~50–80 store-to-store transfers/month |
| **Volume** | Variable (typically 5–20 lines per transfer) |
| **Owner** | Supply Planner (inter-DC); Store Manager (store-to-store) |
| **Participants** | Supply Planner, Store Manager, Receiving Clerk, Stock Associate, DC Picker |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Requestor identifies transfer need (stock-out risk, excess inventory, rebalancing) | Supply Planner / Store Manager | Supply Planning Mgr / Regional Mgr | 10 min |
| 2 | Requestor creates Transfer Order in system: source location, destination, items, quantities | Requestor | — | 10 min |
| 3 | System checks availability at source location; confirms or flags shortage | System | — | Automated |
| 4 | Approval: inter-DC → Supply Planning Manager; store-to-store → Regional Manager | Approver | Approver | 10 min |
| 5 | Source location picks items (DC: WMS pick; Store: Stock Associate picks from shelf) | Picker / Stock Associate | DC Supervisor / Store Manager | 15–60 min |
| 6 | Items packed and shipped; system creates in-transit inventory | Shipper / Driver | DC Supervisor / Store Manager | 15–30 min |
| 7 | Destination location receives items; scans against Transfer Order | Receiving Clerk | DC Supervisor / Store Manager | 15–30 min |
| 8 | System updates: source inventory decreases, in-transit clears, destination inventory increases | System | — | Automated |
| 9 | If discrepancy at destination: flag in system; source location notified for investigation | Receiving Clerk | DC Supervisor / Store Manager | 5 min if any |
9a | Transfer discrepancy resolution: (a) if source picking error confirmed → source location absorbs loss (system posts inventory adjustment at source, Dr. Inventory Loss / Cr. Inventory at source location); (b) if carrier damage → DC Supervisor or Store Manager files carrier damage claim with photos and delivery receipt notation per W3.6a insurance claim process; (c) if unexplained shortage after investigation → destination writes off with approval per tier (Store Manager ≤ PHP 10,000, DC Manager ≤ PHP 50,000, Controller > PHP 50,000); system posts adjustment at destination (Dr. Inventory Loss / Cr. Inventory) | Receiving Clerk / DC Supervisor / Store Manager | Controller | 15–30 min

### W22A. Store-Level Outbound Transfer Fulfillment

When a store is the source location for a store-to-store transfer (W22 step 5), the picking, packing, and dispatch process differs from DC operations (no WMS). The following details the store-level outbound process:

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Manager or Dept. Supervisor receives transfer pick list on handheld/terminal from approved Transfer Order | Stock Associate | Dept. Supervisor | 2 min |
| 2 | Stock Associate picks items from sales floor or backroom per pick list; scan-confirms each item using handheld barcode scanner; system validates scanned SKU and quantity against Transfer Order | Stock Associate | Dept. Supervisor | 15–45 min |
| 3 | If item not found or short: Stock Associate enters actual quantity picked; system updates Transfer Order with partial quantity and notifies destination store | Stock Associate | Dept. Supervisor | 2 min |
| 4 | Stock Associate packs items in available shipping cartons or bags; labels each package with destination store name, Transfer Order number, and item count | Stock Associate | Dept. Supervisor | 10–20 min |
| 5 | **Dispatch options**: (a) **DC truck backhaul** (preferred): items ride on the next DC delivery truck returning from this store — Stock Associate stages packed items at receiving dock for driver pickup; (b) **Own fleet or 3PL**: if urgent or no DC truck scheduled within 2 days, Fleet Manager or DC Dispatch arranges separate pickup; (c) **Inter-store courier**: for same-city transfers, Store Manager may arrange direct courier delivery | Stock Associate / Driver | Store Manager | 5–10 min staging |
| 6 | Driver or carrier confirms pickup by scanning transfer shipment barcode on handheld; system updates Transfer Order status to "Shipped" and creates in-transit inventory | Driver / Carrier | Store Manager | 5 min |
| 7 | System deducts picked items from source store inventory at shipment confirmation | System | — | Automated | |

**Transfer lead time**: Inter-DC: 3–7 days; Store-to-Store: 1–3 days (same city) or 3–5 days (inter-region)

### Time Estimate (W22A)
~35–75 min per outbound transfer: 15–45 min picking + 10–20 min packing + 5–10 min staging. DC truck backhaul adds no incremental time (items ride on existing truck); 3PL or inter-store courier adds 4–8 hours transit.

### Pain Points / Risks (W22A)
- Store-level picking lacks WMS-directed guidance — Stock Associates rely on handheld pick lists and manual scanning, increasing mispick rates compared to DC operations.
- Backhaul dependency on DC truck schedules means non-urgent transfers can wait 1–2 days for the next truck, delaying fulfillment to the destination store.
- Packing materials (cartons, labels, protective wrapping) are not consistently stocked at store level, causing ad-hoc sourcing delays during packing.
- Stock Associates juggle transfer fulfillment with customer-facing duties, leading to delayed shipment during peak store hours.

### System Touchpoints
- Transfer Order creation with source/destination (W22.2)
- Real-time availability check at source (W22.3)
- Approval workflow (W22.4)
- In-transit inventory tracking (W22.6)
- Receiving against Transfer Order (W22.7)
- Inventory update at both locations (W22.8)
- Discrepancy handling with financial resolution: source error, carrier damage, or unexplained loss disposition (W22.9a)
- Intercompany model — see W14 for full dual IC framework (service-based vs. goods-based); standard DC→Store replenishment (W4) is NOT an inter-entity transfer — Depot Inc. owns goods at both locations; Logistics Inc. provides warehousing services billed monthly per W14, not per-transfer
- Customer-initiated inter-store transfer: when a customer at Store A requests an item out of stock, Sales Associate checks real-time inventory at nearby stores via handheld or terminal; if available, Associate creates customer transfer request (item, quantity, source store, destination store, customer contact); Store Manager at destination approves; source Store Manager or system auto-confirms if within same region; system creates Transfer Order per W22; source store picks and ships; destination store receives and notifies customer via SMS/app; sale booked at destination store when customer purchases; transport cost absorbed by company as customer service (no charge to customer); real-time cross-store inventory lookup available to Sales Associates via handheld/terminal and to customers via website/app store selector
- Catch-weight / variable-measure items during transfers: for catch-weight items (lumber, wire, bulk nails), source location measures and records actual length/weight/piece count on Transfer Order; destination location re-measures upon receipt; if quantity differs from TO, variance handled per W22.9a with measurement tolerance applied (e.g., ±2% for lumber, ±1% for wire by length); within tolerance: system accepts destination measurement and posts variance as inventory adjustment at source; outside tolerance: source location investigates (measurement error, transit damage); system supports dual-entry measurement capture for catch-weight items on both outbound and inbound transfer processing

### Pain Points / Risks
- Store-level outbound fulfillment (W22A) lacks WMS-directed pick paths — Stock Associates navigate 35,000 SKUs manually, leading to longer pick times and higher mispick rates than DC operations.
- Transfer discrepancy resolution (W22.9a) is contentious when source and destination locations disagree on whether a shortage is a picking error or carrier damage; without photographic evidence at dispatch, disputes can take weeks to resolve.
- Intercompany model complexity: W4 DC-to-store movements are intra-entity (Depot Inc. throughout), but inter-DC transfers between Logistics Inc.-operated warehouses require IC service fee allocation per W14; planners occasionally confuse the two, leading to incorrect accounting treatment.
- Catch-weight item measurement variance (lumber, wire, rebar) between source and destination locations generates frequent tolerance disputes that require manual investigation beyond the ±1–2% system threshold.
- Customer-initiated inter-store transfers absorb transport cost as a customer service — with ~20–30/day (W214), the aggregate monthly courier cost of PHP 500,000–1,500,000 is not tracked against store profitability.

### Time Estimate
Transfer creation and approval (steps 1–4): 20–30 min per transfer. Source picking and packing (steps 5–6): 15–60 min. Receiving at destination (steps 7–9): 15–35 min. Total end-to-end: inter-DC 3–7 days (including transit); store-to-store 1–5 days (same-city to inter-region). Discrepancy resolution (step 9a): 15–30 min per incident.

### Staffing Implication
- **Supply Planners**: ~30–40 inter-DC transfers/month at ~20 min each for creation/approval = ~10–13 hours/month; absorbed within existing Supply Planning team.
- **Store Managers (store-to-store)**: ~50–80 store-to-store transfers/month at ~20 min each = ~17–27 hours/month across 200 stores (~5–8 min per store per month); negligible per-store impact.
- **DC Pickers**: inter-DC transfers add ~15–60 min picking per transfer on top of standard replenishment picking; ~30–40/month = ~8–40 additional DC labor-hours/month across all DCs; absorbed within existing DC picking capacity.
- **Stock Associates (store outbound, W22A)**: ~50–80 store-to-store transfers/month at ~35–75 min each = ~30–100 store-hours/month across 200 stores; each store handles ~0.3–0.5 transfers/month, requiring ~15–35 min — absorbed within existing Stock Associate duties.
- **No incremental headcount required**; all transfer activities are absorbed within existing Supply Planning, DC, and store staffing models.

### W22B. Store-to-DC Return (Excess / Damaged Inventory)

| Field | Detail |
|---|---|
| **Trigger** | Store identifies excess inventory beyond replenishment needs, damaged items requiring DC inspection/disposition, or items recalled/discontinued requiring central processing |
| **Frequency** | ~100–200 store-to-DC returns/month chain-wide; ~0.5–1 per store per month |
| **Volume** | Typically 5–15 lines per return shipment |
| **Owner** | Store Manager (initiation); DC Supervisor (receiving) |
| **Participants** | Store Manager, Stock Associate, Supply Planner, DC Receiving Clerk, DC Supervisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Store Manager or Dept. Supervisor identifies items for return to DC: (a) excess stock — on-hand significantly above max and unlikely to sell before expiry/obsolescence, (b) damaged items — store-damaged goods requiring central disposition (W6.8a), (c) discontinued/recalled items — per W29 or W68 (product discontinuation), (d) vendor-RTV consolidation — items staged for vendor return that are more efficiently processed through DC | Store Manager / Dept. Supervisor | Store Manager | 15 min |
| 2 | Store Manager creates Store-to-DC Return Order in system: select items, quantities, return reason code (excess / damaged / discontinued / RTV consolidation); system validates that items originated from DC (not DSD-only items that should be returned directly to vendor) | Store Manager | — | 10 min |
| 3 | Supply Planner reviews return request: for excess items, confirms DC has demand or storage capacity to absorb returned stock; for damaged items, auto-approved; system routes for approval | Supply Planner | Supply Planning Manager | 5 min/return |
| 4 | Stock Associate picks and packs items for return shipment; scan-confirms each item against Return Order; stages at store receiving area for DC truck pickup | Stock Associate | Dept. Supervisor | 30–60 min |
| 5 | Items shipped on next available DC delivery truck (reverse logistics — truck returns to DC with return shipment); system creates in-transit inventory | Driver / Stock Associate | DC Supervisor | Per W4 schedule |
| 6 | DC Receiving Clerk receives returned items; scans against Return Order; inspects condition | DC Receiving Clerk | DC Supervisor | 15–30 min |
| 7 | **Disposition by return reason**: (a) excess — system returns items to DC saleable inventory at current WAC; (b) damaged — DC Supervisor inspects and decides disposition per W6.8a (markdown, scrap, RTV); (c) discontinued — system routes to clearance/liquidation holding area per W13.9a or W68; (d) RTV consolidation — Buyer coordinates with vendor per W3.6b | DC Receiving Clerk / DC Supervisor / Buyer | DC Manager | 15–30 min |
| 8 | System updates: store inventory decreases, in-transit clears, DC inventory increases (for resalable items) or posts to appropriate disposition account (for damaged/scrap/RTV) | System | — | Automated |
| 9 | Monthly: Supply Planner reviews store-to-DC return report: frequency by store, reason, and category; flags stores with high return frequency for root cause analysis (ordering discipline, receiving quality, demand planning accuracy) | Supply Planner | Supply Planning Manager | 30 min/month |

### System Touchpoints (Store-to-DC Return)
- Store-to-DC Return Order creation with reason codes (excess, damaged, discontinued, RTV consolidation) (W22B.2)
- Supply Planner approval workflow with DC capacity/demand check (W22B.3)
- In-transit inventory tracking for reverse movement (W22B.5)
- Disposition routing based on return reason code with integration to W6.8a (damage), W13.9a (clearance), W3.6b (RTV) (W22B.7)
- Store-to-DC return analytics: frequency, reason, category, store (W22B.9)
- Integration with W4 (reverse logistics on delivery truck), W6 (damage reporting), W13 (clearance), W22 (standard transfers), W29 (recall), W68 (discontinuation)

### Pain Points / Risks
- Store-to-DC returns compete for reverse-logistics space on DC delivery trucks (backhaul capacity) with store-to-store transfers (W204) and proactive rebalancing shipments (W154); during peak periods, return shipments wait 1–2 weeks for available truck space.
- Excess return items that were slow-moving at the store often become slow-moving at the DC too, merely relocating the SLOB problem (W220) rather than resolving it.
- Damaged items returned to DC for inspection require DC Supervisor evaluation (step 7) that competes with outbound dispatch priorities — damaged goods awaiting disposition occupy valuable DC quarantine zone space.
- Return reason code accuracy is inconsistent — Store Managers sometimes code excess stock as "damaged" to expedite auto-approval, distorting the monthly return analytics (step 9) and obscuring true demand planning issues.

### Time Estimate
Return initiation (steps 1–2): 25 min per return. Supply Planner review (step 3): 5 min per return. Store picking and staging (step 4): 30–60 min. DC receiving and disposition (steps 6–7): 30–60 min. Monthly analytics (step 9): 30 min. Total: ~2 hours per return initiation-to-disposition, spread across multiple days due to truck schedule dependency.

### Staffing Implication
- **Store Manager**: ~0.5–1 return initiations/month × 25 min = ~15 min/month. Absorbed.
- **Supply Planner**: 5 min review per return × ~200/month = ~17 hours/month across all stores. Absorbed by existing planner team.
- **DC Receiving**: adds ~15–30 min per return shipment to existing receiving workload. With ~100–200/month ÷ 4 DCs = ~20–40/DC/month. Manageable.

### Staffing Implication (W22 overall)
- Inter-DC transfers are part of Supply Planner's existing duties (within the 30-person Supply Chain team).
- Store-to-store transfers are managed by Store Managers with Regional Manager approval — absorbed into existing roles.

---

## W23. Consignment Inventory Operations

| Field | Detail |
|---|---|
| **Trigger** | Consignment goods received at store/DC; or consignment goods sold |
| **Frequency** | ~15–25 consignment vendors; settlement monthly |
| **Volume** | ~500–1,000 consignment SKUs (primarily appliances, select tiles, fixtures) |
| **Owner** | Buyer (consignment agreements) |
| **Participants** | Buyer, Receiving Clerk, Cashier, AP Clerk, Consignment Vendor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Buyer establishes consignment agreement: vendor, SKUs, consignment price, settlement terms | Buyer | Category Manager | Per vendor setup |
| 2 | System flags consignment items in item master with vendor ownership indicator | Merchandise Planner | Buyer | 5 min/SKU |
| 3 | Vendor delivers consignment goods; Receiving Clerk processes GR (standard receiving) | Receiving Clerk | Dept. Supervisor | Per W3/W18 |
| 4 | System records consignment receipt as non-valuated inventory (vendor-owned) | System | — | Automated |
| 5 | Consignment items displayed and sold on sales floor; POS scans barcode normally | Cashier | — | Part of sale |
| 6 | At sale: system records sell-through event; ownership transfers from vendor to company to customer; system posts GL entries: Dr. Cost of Goods Sold / Cr. Consignment Vendor Payable (at consignment cost); simultaneously Dr. Cash or Accounts Receivable / Cr. Revenue (at selling price) | System | — | Automated |
| 6a | At month-end close (W9): system accrues consignment liability for all consignment goods sold but not yet settled with vendor; Finance reconciles consignment payable sub-ledger to GL | System / Cost Accountant | Controller | Automated + 30 min/month |
| 7 | Monthly: system generates consignment sell-through report per vendor (units sold × consignment price) | System | Buyer | Automated |
| 8 | Buyer reviews and confirms settlement report | Buyer | Category Manager | 1 hour/vendor/month |
| 9 | AP Clerk processes consignment vendor payment based on confirmed sell-through; system generates AP invoice from sell-through data: Dr. Consignment Vendor Payable / Cr. Cash (settles the accrued liability from step 6) | AP Clerk | AP Supervisor | Per W7 |
| 10 | Quarterly: Buyer reviews consignment SKU performance; identifies slow movers for return to vendor; coordinates physical pickup with vendor (vendor arranges collection or Buyer schedules transport); Receiving Clerk processes return shipment in system (reduces non-valuated consignment inventory; no GL posting since goods remain vendor-owned throughout); vendor confirms received quantities and issues updated consignment stock list; system updates consignment on-hand quantities | Buyer / Receiving Clerk | Category Manager | 2 hours/quarter |

### System Touchpoints
- Consignment item flagging in item master (W23.2)
- Non-valuated inventory receipt and tracking (W23.4)
- Ownership transfer at point of sale with automatic GL posting (Dr. COGS / Cr. Consignment Payable) (W23.6)
- Period-end accrual for sold-but-unsettled consignment goods (W23.6a)
- Consignment payable sub-ledger reconciliation to GL (W23.6a)
- Consignment sell-through report generation (W23.7)
- AP settlement from sell-through data with GL posting (Dr. Consignment Payable / Cr. Cash) (W23.9)
- Consignment return logistics: return shipment processing with non-valuated inventory reduction (no GL impact); vendor confirmation and updated stock list; on-hand quantity adjustment (W23.10)
- Quarterly consignment vendor statement reconciliation: Cost Accountant generates consignment reconciliation report per vendor — compares BuildRight's recorded consignment sell-through (units sold × consignment cost) to vendor's statement; reconciles on-hand quantities (system record vs. vendor record of goods shipped minus goods sold); investigates discrepancies (unrecorded sell-through, unreported returns, missing receipts, timing gaps); reconciling items documented and resolved within 15 business days; unreconciled differences > PHP 50,000 escalated to Controller; results feed into vendor scorecard (W44) (W23)

### Pain Points / Risks
- Quarterly vendor reconciliation discrepancies are common — consignment vendors track sell-through independently and their records frequently differ from BuildRight's POS data, requiring 15 business days to resolve and tying up AP resources.
- Consignment items displayed alongside BuildRight-owned stock on the sales floor are visually indistinguishable to customers and staff; accidental damage to consignment goods creates liability disputes with vendors who expect full consignment price reimbursement.
- Non-valuated inventory tracking for consignment items is prone to errors during cycle counts (W6) and annual physical inventory (W42) — count teams must correctly classify items as vendor-owned vs. BuildRight-owned, and misclassification distorts both the consignment payable and owned inventory valuation.
- Slow-moving consignment SKUs that vendors refuse to collect after quarterly review (W23.10) occupy valuable shelf and backroom space in stores with no financial incentive for the vendor to expedite retrieval.
- Period-end accrual complexity: at month-end close (W9), the system must accurately accrue consignment liability for all sold-but-unsettled items across 15–25 vendors and 200 stores; timing differences between POS sell-through and vendor settlement create reconciliation work for Cost Accountant.

### Time Estimate
Vendor setup (steps 1–2): 30–60 min per vendor. Monthly settlement review and confirmation (steps 7–8): 1–2 hours per vendor per month. Quarterly performance review and slow-mover returns (step 10): 2 hours/quarter per vendor. Reconciliation (W23): 30 min/month per vendor. Total ongoing: ~15–25 hours/month across all consignment vendors.

### Staffing Implication
- Consignment management adds ~15–25 hours/month to Buyer workload (review + settlement). Spread across 10–12 buyers handling their respective vendor portfolios, this is ~2 hours/buyer/month. Absorbed within existing headcount.

---

## W42. Annual Physical Inventory Execution

| Field | Detail |
|---|---|
| **Trigger** | Year-end close calendar (typically December 31 or last business day of fiscal year) |
| **Frequency** | Annual; each store and DC counted once per year |
| **Volume** | 35,000 SKUs × 204 locations (200 stores + 4 DCs); executed in coordinated 3–5 day window per region |
| **Owner** | Cost Accountant (overall); Store Manager (per store); DC Manager (per DC) |
| **Participants** | Cost Accountant, Store Managers, DC Managers, all store staff, inventory count teams, IT, Internal Audit |

### Pre-Count Planning (2–3 weeks before count)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Cost Accountant issues physical inventory instructions: count dates, methodology, team assignments, system freeze schedule | Cost Accountant | Controller | 4 hours |
| 2 | IT configures count sheets in system: generate zone-based count sheets per location with expected system quantities (hidden for blind count) | IT Team | Cost Accountant | 1 day |
| 3 | Store Managers organize count teams: assign zones (8 zones per store), designate team leaders, schedule shifts for 2-day count | Store Manager | Store Ops Director | 2 hours/store |
| 4 | Store Managers ensure all receiving and shipments are posted before count; process pending transactions; stage goods in correct locations | Store Manager | Store Ops Director | 4 hours/store |
| 5 | Internal Audit prepares to observe counts at selected locations (sample: 20–30 stores + all DCs) | Internal Audit | CFO | 1 week |

### Count Execution (Day 1 — full count; Days 2–3 — recounts and adjustments; Days 4–5 — residual clean-up if needed)

> **Feasibility note**: Counting 35,000 SKUs per store with 30 staff in 2 days is infeasible for a full wall-to-wall count. BuildRight addresses this with a **tiered counting strategy**: (a) **A/B items** (~10,500 SKUs, 95% of inventory value) receive full physical count during the annual window; (b) **C items** (~24,500 SKUs) are validated by extrapolating from rolling cycle counts (W6) conducted throughout the year — the annual process confirms that cycle count accuracy for C-items meets the ≥ 97% threshold, rather than recounting every C-item. This reduces the per-store counting burden to ~10,500 SKUs ÷ 30 staff ÷ 2 days = ~150 SKUs/person/day, achievable at ~3 min/SKU including travel between locations. DCs, with higher item density and forklift-access racking, allocate 3–5 days for a full count of all SKUs.
>
> **C-item extrapolation methodology**: C-item inventory accuracy is validated using a statistical sampling approach — (a) throughout the year, W6 cycle counts cover all C-item SKUs at least once per quarter (per the quarterly cycle in W6); (b) each C-item's cycle count accuracy (physical vs. system quantity) is recorded per count event; (c) at year-end, Cost Accountant computes the aggregate C-item accuracy rate = (total C-item SKU-locations where physical matched system within tolerance) ÷ (total C-item SKU-locations counted during the year); (d) if aggregate accuracy ≥ 97%, C-items are considered validated and no additional count is required at year-end; (e) if aggregate accuracy < 97%, Cost Accountant identifies the worst-performing C-item categories (by variance rate) and adds them to the annual count scope; (f) sample size for interim confidence: to achieve 95% confidence that the true accuracy rate is within ±1% of the observed rate, a minimum of ~500 C-item SKU-locations must be cycle-counted per quarter per store (approximately 2% of C-item SKU-locations, achievable within W6 daily count volume of ~700 SKUs/day); (g) this methodology is reviewed and approved by Internal Audit annually as part of the W42 physical inventory observation; (h) **below-threshold contingency**: if aggregate C-item accuracy falls below 97%, Cost Accountant quantifies the gap and identifies worst-performing C-item categories by variance rate; additional items added to the annual count scope in priority order (highest-variance categories counted first); if additional scope threatens the 2-day count window, Cost Accountant escalates to Controller with a proposed extended count schedule (up to 5 days with staggered zone freezing per W42 system freeze mitigation); Controller approves or denies extension; if extension denied, Cost Accountant counts the highest-risk C-items within the standard window and accepts a qualified inventory opinion for the remaining C-items — Controller discloses the qualification in the year-end close package (W9B); Internal Audit documents the below-threshold outcome and includes it in the W42 observation report.

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 6 | System freezes inventory transactions at count locations (no sales, receiving, or transfers during count window) | System / IT | Cost Accountant | Automated |
| 7 | Count teams physically count every SKU in assigned zone: two-person teams (one counts, one records on RF device/count sheet) | Count Teams | Team Leader | 6–10 hours/location |
| 8 | Team leaders submit zone counts; system compares to system quantities (blind count — system quantity only revealed after team submits) | Team Leader | Store Manager | Per zone |
| 9 | System generates variance report per zone: items where physical count differs from system count | System | — | Automated |
| 10 | For items with variance: recount team (different from original) performs blind recount | Recount Team | Store Manager | 2–4 hours/location |
| 11 | If recount confirms variance: Team Leader investigates and documents root cause (theft, damage, receiving error, data entry error) | Team Leader | Store Manager | 15 min/item |
| 12 | Store Manager reviews and approves adjustments per tier: (a) adjustment ≤ PHP 10,000: Store Manager, (b) adjustment PHP 10,001–100,000: Regional Manager, (c) adjustment > PHP 100,000: Controller | Approver | Approver | 5–15 min/adjustment |
| 13 | Internal Audit observes counts at sampled locations; validates methodology compliance and count accuracy | Internal Audit | CFO | Full count day |
| 14 | System posts approved inventory adjustments; updates inventory valuation; posts to GL (gain/loss on inventory) | System | — | Automated |

### Post-Count (1 week after)

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 15 | System unfreezes inventory transactions; normal operations resume | IT Team | Cost Accountant | Automated |
| 16 | Cost Accountant reconciles total inventory valuation post-adjustment to GL inventory accounts | Cost Accountant | Controller | 4 hours |
| 17 | Cost Accountant generates physical inventory summary report: total adjustments by location, by category, by variance type (gain/loss), shrinkage as % of sales | Cost Accountant | Controller | 2 hours |
| 18 | Controller and CFO review physical inventory results; identify high-shrinkage locations for loss prevention action (W37) | Controller | CFO | 2 hours |
| 19 | Internal Audit issues observation report with recommendations for count process improvement | Internal Audit | CFO | 1 week |

### System Touchpoints
- System inventory transaction freeze per location (W42.6, W42.15); auto-replenishment orders for frozen stores are automatically queued by the system and released upon unfreeze — no replenishment orders are lost during the count window; queued orders visible on Supply Planner dashboard with "Pending — Store Count Freeze" status
- Zone-based count sheet generation with blind count mode (W42.2, W42.7–8)
- RF device / handheld count entry (W42.7)
- Variance detection after count submission (W42.9)
- Recount tracking (W42.10)
- Adjustment approval workflow with tiered authorization (W42.12)
- Bulk inventory adjustment posting and GL impact (W42.14)
- Vendor-owned inventory (consignment/VMI) during physical count: count teams count consignment (W23) and VMI (W20) items using separate count sheets flagged as "Vendor-Owned — Non-Valuated"; system records vendor-owned counts separately from BuildRight-owned (valuated) inventory; after count, system reconciles physical count of vendor-owned items to vendor's expected quantities per W23/W20 records; discrepancies investigated — if physical < system, potential unrecorded sell-through requiring W20/W23 settlement adjustment; if physical > system, potential unrecorded receipt requiring investigation; vendor-owned count results shared with respective vendors for reconciliation; Internal Audit (W42 step 13) verifies that all counted items are correctly classified as owned (valuated) or vendor-owned (non-valuated) for audit evidence (W42.7–8)
- Physical inventory summary reporting (W42.17)
- System freeze mitigation: to minimize operational disruption during the counting window, system supports **staggered zone freezing** as an alternative to full-location freeze — (a) stores may remain open during count using zone-by-zone freeze: zone being counted is frozen for transactions (no sales, receiving, or transfers for items in that zone); remaining zones continue normal operations; as each zone's count is submitted, system unfreezes that zone; full count completed over 2 days with rotating zone freezes; (b) for DCs: system supports module-by-module freeze (e.g., count inbound module while outbound module continues shipping); critical outbound shipments for same-day delivery commitments are prioritized before the freeze window; (c) if full-location freeze is required (smaller stores or DCs with high inventory interdependency): system freeze window is minimized to non-business hours where possible (overnight freeze with count starting at close of business; completed before next day opening); IT monitors system performance during zone freeze/unfreeze cycles to ensure no transaction loss; Store Manager communicates freeze zones to staff in real-time via handheld notifications (W42)
- Continuous counting alternative for high-volume stores: for the top 20 stores by revenue (where even a 2-day partial disruption is significant), the annual wall-to-wall count may be replaced by a **perpetual inventory validation** program — system generates weekly count tasks covering 1/52 of all SKUs per week (completing a full cycle in 1 year, overlapping with W6 cycle counts); Cost Accountant validates perpetual counts quarterly and Internal Audit observes the process semi-annually; this alternative requires Controller approval and is only available for stores with demonstrated ≥ 98% cycle count accuracy over the prior 12 months (W42)

### Pain Points / Risks
- Full store closure or skeleton-crew operation during the 2-day count window generates revenue loss estimated at PHP 200,000–500,000 per store; the staggered zone freezing alternative mitigates this but adds counting complexity and extends the count window.
- C-item extrapolation methodology carries audit risk — if the aggregate C-item accuracy falls below 97%, the below-threshold contingency requires extended counting that may disrupt post-count operations; Controller must issue a qualified inventory opinion for any uncounted C-items, which external auditors scrutinize.
- Queued replenishment orders during the system freeze (auto-generated per W4) create a post-unfreeze surge in DC pick/pack/ship workload that can overwhelm DC capacity in the 2–3 days following count completion.
- New store ramp-up overlap: stores in their first 90 days (W4 new store ramp-up) that undergo annual physical inventory simultaneously face manual replenishment overrides AND count freezes, creating a perfect storm of inventory uncertainty.
- Internal Audit travel to 20–30 sampled locations across the Philippine archipelago during the coordinated 3–5 day count window requires meticulous logistics planning; typhoon season disruption can prevent auditor observation at critical locations.

### Time Estimate
Pre-count planning: 2–3 weeks (4 hours instructions + 1 day IT setup + 2 hours/store team organization + 4 hours/store transaction posting). Count execution: 2 days per store, 3–5 days per DC. Post-count reconciliation: 1 week (4 hours GL reconciliation + 2 hours reporting + 2 hours management review). Internal Audit observation report: 1 week after count. Total project duration: ~4–6 weeks from planning to final report.

### Staffing Implication
- **All store staff (30/store)**: Mobilized for 2-day count. Stores may close early or operate with skeleton crew during count.
- **DC staff (~150/DC)**: Full DC count requires 1–2 days. Operations paused during count.
- **Cost Accountant**: 20–30 hours for planning, execution support, and reconciliation. Heaviest workload of the year for this role.
- **Internal Audit (3–5 auditors)**: Travel to sampled locations. Absorbed within annual audit plan.
- **IT**: 1 day for count sheet configuration + system freeze/unfreeze support.

---

## W56. Customer Backorder Management

| Field | Detail |
|---|---|
| **Trigger** | Customer requests an item that is out of stock at the store and/or DC level |
| **Frequency** | ~2,000–3,000 backorder requests/month (primarily B2B trade accounts) |
| **Volume** | Concentrated in fast-moving commodity categories (cement, lumber, paint, plumbing fittings, electrical wire) during peak construction season |
| **Owner** | Sales Associate (intake); Supply Planner (fulfillment) |
| **Participants** | Sales Associate, Supply Planner, Buyer, Store Manager, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer requests out-of-stock item at store or via Sales Rep; Sales Associate checks real-time inventory across all locations (stores + DCs) via handheld | Sales Associate | Dept. Supervisor | 3 min |
| 2 | If available at another store: offer customer-initiated inter-store transfer per W22 (customer-initiated transfer) | Sales Associate | Store Manager | 5 min |
| 3 | If unavailable chain-wide or customer prefers to wait: Sales Associate creates backorder in system — item, quantity, customer details (loyalty account or trade account), preferred store for pickup, delivery preference, maximum wait time (customer-stated) | Sales Associate | Dept. Supervisor | 5 min |
| 4 | System links backorder to next expected replenishment: (a) if PO already in progress (W2) with expected GR date — system shows estimated availability date, (b) if no PO exists — system flags to Supply Planner for PO creation (W2A), (c) if import item — shows import PO ETA (W2B) | System | — | Automated |
| 5 | System reserves backorder quantity against incoming PO or replenishment order (allocates to backorder before general store replenishment); backorder takes priority over routine replenishment allocation | System | — | Automated |
| 6 | Sales Associate communicates estimated availability date to customer; for trade/corporate accounts, Sales Rep manages the communication | Sales Associate / Sales Rep | — | 2 min |
| 7 | When goods are received at DC and backorder allocation is fulfilled: system routes allocated quantity to the customer's preferred store in the next replenishment wave (W4); or if customer prefers delivery, system creates home delivery order (W19) | System | Supply Planner | Automated |
| 8 | System sends customer notification (SMS/email/app): "Your item is on the way to [Store Name], expected availability [date]" | System | — | Automated |
| 9 | Item arrives at store; Stock Associate stages for customer pickup (similar to BOPIS W11); system sends "Ready for pickup" notification | Stock Associate / System | Store Manager | 5 min + automated |
| 10 | Customer picks up item; sale processed at POS (standard transaction or trade account per W5B.4c); backorder closed in system | Cashier / Customer | — | 5 min |
| 11 | If customer cancels backorder before fulfillment: Sales Associate cancels in system; allocation released back to general inventory | Sales Associate | Dept. Supervisor | 2 min |
| 12 | If backorder exceeds customer-stated maximum wait time: system auto-notifies customer with options to (a) extend wait, (b) accept substitute item, or (c) cancel; if no response in 7 days, system auto-cancels and releases allocation | System | — | Automated |
| 13 | Weekly: Supply Planner reviews open backorder aging report: items with no incoming PO (step 4b — no supply planned), long-wait backorders (> 14 days), and backorders at risk of cancellation; escalates to Buyer for expedited procurement | Supply Planner | Supply Planning Manager | 1 hour/week |

### System Touchpoints
- Real-time inventory visibility across all locations with cross-store lookup (W56.1)
- Backorder creation linked to customer account (loyalty or trade) with estimated availability (W56.3–4)
- Allocation reservation against incoming PO/replenishment with backorder priority (W56.5)
- Automated customer notification at each status change: created, allocated, in transit, ready for pickup (W56.8–9)
- Backorder aging report with escalation triggers (W56.13)
- Backorder price protection: if a promotional price (W13) or regular price reduction (W40) becomes effective between backorder creation and fulfillment, system automatically applies the lower price to the backorder at fulfillment (customer-friendly policy); system logs the price adjustment with original backorder price, new lower price, and price source (promo or price change); if price increases, the original backorder price is honored (locked at creation); this rule applies to both trade account and retail backorders
- Auto-cancellation after maximum wait time with customer notification (W56.12)
- Integration with W2 (PO creation trigger), W4 (replenishment allocation), W13 (promotional pricing — backorder price protection), W19 (home delivery option), W22 (inter-store transfer alternative), W38 (special order for non-stock items — backorder is for stock items, special order is for non-stock items), W68 (product discontinuation — system auto-cancels open backorders for discontinued SKUs and notifies customers)

### Pain Points / Risks
- Backorder allocation reserves stock against incoming PO/replenishment (step 5) before general store replenishment — during constrained supply periods, this priority mechanism (also reflected in W105 allocation hierarchy) causes routine replenishment shortfalls that cascade across non-backorder stores.
- Auto-cancellation after maximum wait time (step 12) generates customer dissatisfaction when items were nearly available; the 7-day response window is too short for trade account customers (B2B) who may be waiting on project financing confirmation.
- Import item backorders (step 4c — linked to W2B import POs) have ETAs of 30–60 days, far exceeding most customer-stated maximum wait times; the system auto-cancels these prematurely unless the customer explicitly extends, losing sales on high-value import orders.
- Backorder price protection (customer-friendly policy) means the company absorbs margin erosion when promotional pricing activates between creation and fulfillment; during major promos (W13), the volume of backorders receiving retroactive discounts can be material.
- Inter-store transfer alternative (step 2) offered to the customer adds 3PL courier cost and extends the conversation at the Sales Associate level, increasing per-customer interaction time during already-busy trading hours.

### Time Estimate
Customer intake (steps 1–3): 10–13 min per backorder. Automated steps (steps 4–5, 8): real-time. Customer communication (step 6): 2 min. Weekly aging review (step 13): 1 hour/week for Supply Planner. Total ongoing: ~2 hours/store/month for Sales Associates + 1 hour/week for Supply Planner.

### Staffing Implication
- **Sales Associates**: ~2,000–3,000 backorders/month ÷ 200 stores = ~10–15/store/month × ~10 min each = ~2 hours/store/month. Absorbed.
- **Supply Planner**: 1 hour/week for backorder review. Absorbed within existing planning duties.

---

## W57. Promotional Stock Allocation & Pre-Positioning

| Field | Detail |
|---|---|
| **Trigger** | Promotional event confirmed (W13 step 3 — VP Merchandising approves promo pricing) |
| **Frequency** | 6 major bi-monthly promos/year + 12 monthly hot deal cycles |
| **Volume** | 200–500 SKUs per major promo; stock pre-positioned to 200 stores over 1–2 weeks before event |
| **Owner** | Supply Planner |
| **Participants** | Supply Planner, Category Manager, DC Supervisor, Store Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | After promo approval (W13 step 3), Category Manager provides Supply Planner with promo SKU list, expected demand lift (historical lift % × baseline forecast), and maximum shelf capacity per store | Category Manager | VP Merchandising | 2 hours/promo |
| 2 | Supply Planner calculates promotional stock requirement per SKU per store: (base weekly demand × promo lift factor × promo duration weeks) + safety buffer (10–20%) − current store inventory − already-in-transit inventory | Supply Planner | Supply Planning Manager | 2–4 hours/promo |
| 3 | Supply Planner checks DC inventory for promo items; identifies shortfalls; requests Buyer to expedite POs for items with insufficient DC stock to cover promotional allocation (may use air freight for imports if lead time is critical) | Supply Planner / Buyer | Category Manager | 1 hour/promo |
| 4 | System generates promotional replenishment orders per store with "Promo" priority flag; these orders are prioritized ahead of routine replenishment in the pick wave (W4 step 3) | System | Supply Planner | Automated |
| 5 | DC picks and ships promotional stock to stores in waves over 1–2 weeks before promo start date; stores in each region scheduled to receive promo stock 3–5 days before event | DC Team | DC Supervisor | Per W4 |
| 6 | Store Receiving Clerk receives promo stock; Stock Associate stages in backroom or designated promo display area (not commingled with regular shelf stock to preserve promo allocation integrity) | Receiving Clerk / Stock Associate | Store Manager | Per W4 |
| 7 | System tracks promotional stock allocation vs. actual receipt per store; flags stores that have not received their full allocation 2 days before promo start | System | Supply Planner | Automated |
| 8 | During promo: system reports promo stock sell-through daily per store; Supply Planner monitors for stores selling faster than expected and arranges emergency replenishment from DC or transfers from slower-selling stores (W22) | Supply Planner | Supply Planning Manager | 30 min/day during promo |
| 9 | After promo: remaining promo stock disposition per W13.9a (clearance) or return to regular shelf inventory if sell-through ≥ 90% | Pricing Analyst / Stock Associate | Category Manager | Per W13 |

### System Touchpoints
- Promotional demand lift calculation tool integrated with forecast engine (W31) and historical promo performance data (W57.2)
- Promotional replenishment order generation with priority flag and promo allocation tracking (W57.4)
- Promotional stock allocation dashboard: planned vs. shipped vs. received per store (W57.7)
- Promotional sell-through dashboard: real-time sales velocity during promo period with store-level drill-down (W57.8)
- Integration with W2 (expedited POs), W4 (replenishment waves), W13 (promo pricing and clearance), W22 (emergency inter-store transfers), W31 (demand forecast)

### Pain Points / Risks
- Promotional demand lift estimation is often inaccurate for new or seasonal SKUs with limited historical data, leading to over-allocation (tying up working capital) or under-allocation (lost sales and customer disappointment).
- Expedited POs to cover promo shortfalls carry premium freight costs (air freight for imports) that erode promotional margin, sometimes turning profitable promos into loss-makers.
- Store-level promo stock commingling with regular shelf stock — despite segregation procedures — causes inventory tracking confusion and inflates post-promo clearance volumes.
- Last-minute promo SKU additions or changes from Marketing (after allocation planning is complete) force emergency replanning, creating DC picking chaos and missed pre-positioning windows.

---

### Time Estimate
Planning phase: 4–7 hours per major promo event (allocation calculation + DC stock check + expedited POs). Execution phase: 1–2 weeks of incremental pick/pack/ship waves per promo. Post-promo monitoring: 30 min/day during event + 2 hours for sell-through analysis.

### Staffing Implication
- **Supply Planner**: adds ~4–6 hours per major promo event for allocation planning + 30 min/day monitoring during the promo. With 6 major events/year, this is ~30–40 hours/year of incremental planning work, concentrated in the 2 weeks before each event. Absorbed within existing Supply Chain team.
- **DC Team**: promotional pre-positioning adds temporary surge to pick/pack/ship volume in the 1–2 weeks before each event. Managed with shift scheduling adjustments (W34).

## W91. Damaged & Defective Goods Disposition

| Field | Detail |
|---|---|
| **Trigger** | Damaged or defective goods identified during receiving (W3, W18), cycle counting (W6), daily operations (W5), or customer return (W12) |
| **Frequency** | ~500–800 damaged/defective units/month across all locations |
| **Volume** | ~15–25 per store per month; ~50–100 per DC per month |
| **Owner** | Store Manager (store-level); DC Supervisor (DC-level) |
| **Participants** | Store Manager, DC Supervisor, Stock Associate, Receiving Clerk, Buyer, Category Manager, Controller |

### Background

Damaged and defective goods are an inevitable part of retail operations — items damaged in transit (DC→Store or vendor→DC), in-store handling damage, customer-caused damage on display items, vendor manufacturing defects, and age-related deterioration (paint expiry, adhesive hardening). While W88 (Return to Vendor) handles the vendor-liability path and W92 (Inventory Adjustment) handles the accounting authorization, this workflow governs the physical identification, documentation, and disposition decision-making for damaged/defective goods regardless of liability. It fills the gap between discovering damaged inventory and the final resolution.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Identification and documentation**: (a) Store Associate, Stock Associate, or Receiving Clerk discovers damaged/defective item; (b) scans item barcode and selects damage type: (i) transit damage (DC→Store or vendor→DC/Store), (ii) in-store handling damage (dropped, shelving collapse, water damage), (iii) customer-caused damage (opened package, broken seal on display), (iv) vendor manufacturing defect (functional failure, missing parts, cosmetic defect out of box), (v) age/expiry deterioration (expired paint, hardened adhesive, rusted hardware), (vi) environmental damage (flood, typhoon — W49); (c) takes photo of damage; (d) system creates damage report with timestamp, location, item, quantity, damage type, and photo evidence | Stock Associate / Receiving Clerk | Dept. Supervisor / DC Supervisor | 5 min/item |
| 2 | **Quarantine and physical segregation**: System moves damaged items to "Damaged/Defective" inventory status (unavailable for sale, unavailable for replenishment calculation); physical items moved to designated damaged goods area in store backroom or DC quarantine zone | Stock Associate / Receiving Clerk | Store Manager / DC Supervisor | 5 min/item |
| 3 | **Liability assessment**: (a) **Vendor liability** — damage type is vendor defect, transit damage from vendor, or wrong item received: route to W88 (Return to Vendor) for vendor credit or replacement; (b) **Carrier liability** — damage type is transit damage from DC to store or 3PL delivery to customer: route to carrier claim (W19.12b for ecommerce, W66 for inter-island, W52 for fleet); (c) **BuildRight liability** — in-store handling damage, customer-caused damage, environmental damage: no external recovery possible; proceed to disposition decision; (d) **Undetermined** — route to Buyer for vendor negotiation or DC Supervisor for carrier investigation | Dept. Supervisor / DC Supervisor | Store Manager / DC Supervisor | 5 min/item |
| 4 | **Disposition decision** (BuildRight-liability items only — vendor/carrier items follow W88 or carrier claim): (a) **Markdown and sell at discount** — item is cosmetically damaged but functionally usable (e.g., dented can of paint, scratched tile, box-damaged appliance); system routes to W93 (Markdown & Clearance) for discounted sale; (b) **Donate** — item is functional but not saleable at any price (e.g., display model replaced by newer version); coordinate with CSR for community donation program; requires Controller approval; (c) **Scrap/dispose** — item is non-functional, hazardous (paint/chemical per W82), or broken beyond any use; system routes to disposal with proper documentation; (d) **Return to regular stock** — item was incorrectly flagged (e.g., packaging scuff but product perfect); system reverses damage status | Dept. Supervisor / Store Manager / DC Supervisor | Store Manager / DC Supervisor | 5 min/item |
| 5 | **DC-level consolidation**: DC Supervisor consolidates damaged/defective items from DC operations and items returned from stores (via W22B store-to-DC return); sorts by vendor for potential consolidated RTV shipment per W88; disposes of scrap items in bulk per W82 (hazardous materials) or general waste protocols | DC Supervisor | Supply Chain Manager | 1 hour/week |
| 6 | **Financial impact recording**: System calculates damage/defective value at WAC per item; records in damage/defective register: total value by damage type, by location, by category; feeds into shrinkage report per W37 (loss prevention) and W92 (inventory adjustment) | System | Controller | Automated |
| 7 | **Monthly damage analysis**: Category Manager and Controller review monthly damage/defective report: (a) damage rate by category (target: < 0.5% of inventory value), (b) damage rate by location (flag stores > 1% rate), (c) damage rate by damage type (trend analysis), (d) top 20 items by damage frequency (possible packaging improvement or vendor quality issue), (e) vendor defect rate feeds into W44 vendor scorecard; (f) transit damage rate by carrier feeds into W52/W62B carrier performance | Category Manager / Controller | VP Merchandising / CFO | 1 hour/month |

### System Touchpoints
- Damage report creation with barcode scan, damage type classification, and photo evidence (W91.1)
- Inventory status change to "Damaged/Defective" (blocked from sale and allocation) (W91.2)
- Liability assessment routing: W88 (vendor), carrier claim, or BuildRight (W91.3)
- Disposition decision workflow: markdown (W93), donate, scrap/dispose, or reinstate (W91.4)
- Damage/defective register with value tracking by type, location, category (W91.6)
- Monthly damage analysis dashboard with rate tracking and trend analysis (W91.7)
- Integration with W3 (DC receiving — transit damage from vendor), W4 (DC→Store transit damage), W6 (cycle count — discovered damage), W12 (customer returns — damaged items), W18 (DSD — transit damage), W22 (transfers — in-transit damage), W37 (loss prevention — damage as shrinkage component), W44 (vendor scorecard — vendor defect rate), W52/W62B (carrier performance — transit damage rate), W66 (inter-island — transit damage), W82 (hazardous waste disposal), W88 (RTV — vendor liability path), W92 (inventory adjustment — accounting authorization), W93 (markdown — sellable damaged goods)

### Pain Points / Risks
- Quarantine space at store level is limited — with ~15–25 damaged items/store/month accumulating pending disposition decisions, the designated damaged goods area in the backroom can overflow, leading to commingling with saleable stock and accidental re-shelving of damaged items.
- Liability assessment (step 3) for transit damage from DC to store requires distinguishing between carrier-caused damage and in-store handling damage; without photographic evidence at the point of DC dispatch, Store Managers are incentivized to classify all damage as transit damage to recover cost from the carrier or DC.
- DC-level consolidation of damaged items from 200 stores (via W22B return) creates a high-volume sorting operation that requires dedicated DC labor weekly; during peak damage periods (post-typhoon, post-promo), the consolidation queue delays vendor RTV processing (W88).
- Hazardous material disposal (paint, chemicals per W82) from damaged goods requires licensed waste haulers with 5–10 day lead time for pickup; accumulated hazardous damaged goods in store backrooms pose safety and compliance risks during the waiting period.
- Monthly damage rate targets (< 0.5% of inventory value) are difficult to enforce at store level because damage reporting compliance varies significantly — some Store Managers under-report to protect their shrinkage KPIs, distorting the Category Manager's ability to identify systemic vendor quality issues.

### Time Estimate
Identification and documentation (step 1): 5 min/item. Quarantine and segregation (step 2): 5 min/item. Liability assessment (step 3): 5 min/item. Disposition decision (step 4): 5 min/item. DC consolidation (step 5): 1 hour/week. Monthly analysis (step 7): 1 hour/month. Total per store: ~2.5–4 hours/month. Total per DC: ~4–6 hours/week for consolidation and disposition.

### Staffing Implication
- **Store Associates / Stock Associates**: ~15–25 damaged items/store/month × 10 min each = ~2.5–4 hours/store/month. Absorbed.
- **DC Supervisor**: 1 hour/week for consolidation. Absorbed.
- **Category Manager / Controller**: 1 hour/month for damage review. Absorbed.
- **No incremental headcount.**

---

## W92. Inventory Adjustment & Shrinkage Authorization

| Field | Detail |
|---|---|
| **Trigger** | Cycle count discrepancy identified (W6); annual physical inventory variance (W42); confirmed theft or loss (W37); damaged goods write-off (W91); RTV write-off (W88); or system correction needed (negative inventory, data entry error) |
| **Frequency** | ~1,500–2,500 adjustments/month across all locations (mostly from cycle counts) |
| **Volume** | ~8–12 adjustments per store per month; ~30–50 per DC per month |
| **Owner** | Controller |
| **Participants** | Stock Associate, Store Manager, DC Supervisor, Cost Accountant, Controller, Internal Audit |

### Background

W6 (Cycle Counting) identifies discrepancies between system and physical inventory, and W42 (Annual Physical Inventory) produces wall-to-wall variances. However, the resolution — investigating the root cause, authorizing the adjustment, and posting the accounting entry — requires a separate control workflow. Inventory adjustments directly impact the GL (inventory asset and COGS/shrinkage expense), so they require proper authorization tiers, documentation, and segregation of duties. This workflow also covers adjustments from confirmed theft (W37), damage write-offs (W91), and system corrections.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Adjustment request creation**: System automatically creates adjustment request when: (a) cycle count (W6) reveals variance exceeding threshold (±1 unit for A-items, ±3 for B-items, ±5 for C-items), (b) physical inventory (W42) variance confirmed, (c) confirmed theft reported (W37), (d) damaged goods disposition completed (W91 — markdown, scrap, or donate), (e) RTV unresolved > 90 days (W88.9 — auto-write-off), (f) negative inventory detected (system shows on-hand < 0). Alternatively, Stock Associate or DC Supervisor manually creates adjustment request with reason code and supporting documentation | System / Stock Associate / DC Supervisor | Store Manager / DC Supervisor | 5 min/request |
| 2 | **Root cause classification**: Initiator or Supervisor classifies the adjustment reason: (a) shrinkage/theft (unexplained loss), (b) receiving/putaway error (item received but put in wrong location), (c) POS scanning error (wrong item scanned at checkout), (d) damage/spoilage (per W91), (e) vendor short-shipment (received less than PO — per W3), (f) data entry error (incorrect quantity or SKU entered), (g) negative inventory correction (overselling or system timing), (h) RTV write-off (per W88), (i) intercompany/transfer discrepancy (per W22), (j) other (with explanation) | Dept. Supervisor / DC Supervisor | Store Manager / DC Supervisor | 5 min/request |
| 3 | **Investigation** (for material adjustments): (a) A-items with variance > PHP 10,000: Dept. Supervisor investigates — review POS transactions for scanning errors, review receiving logs, check transfer records, review CCTV if theft suspected; (b) confirmed theft: escalate to Loss Prevention per W37; (c) receiving/putaway error: check if item is in adjacent bin location (common in big-box with 35,000 SKUs); (d) document findings in adjustment request | Dept. Supervisor / DC Supervisor | Store Manager / DC Supervisor | 15 min/investigation |
| 4 | **Authorization** (tiered approval): (a) **Level 1 — Store Manager / DC Supervisor**: adjustments ≤ PHP 5,000 per SKU per count event; max 20 adjustments/month per location without escalation; (b) **Level 2 — Cost Accountant**: adjustments > PHP 5,000 and ≤ PHP 50,000; validates GL impact and cost center allocation; (c) **Level 3 — Controller**: adjustments > PHP 50,000; reviews root cause documentation and investigation quality; approves or requests additional investigation; (d) **Level 4 — CFO**: adjustments > PHP 500,000 (typically annual physical inventory major variances); requires Internal Audit observation per CTL-38 in Internal Controls Matrix | Per tier above | Per tier above | 5–15 min/approval |
| 5 | **System posting**: Upon authorization, system posts inventory adjustment: (a) Dr. COGS-Shrinkage / Cr. Inventory (at WAC) — for losses, theft, damage write-offs; (b) Dr. Inventory / Cr. COGS-Shrinkage — for gains (found items, receiving errors corrected); (c) Dr. Vendor Claim Receivable / Cr. Inventory — for vendor short-shipment (pending vendor credit per W88); (d) Dr. Carrier Claim Receivable / Cr. Inventory — for carrier damage (pending carrier claim); (e) adjustment posted with authorization trail, reason code, supporting evidence reference, and GL impact | System | Cost Accountant | Automated |
| 6 | **Negative inventory resolution**: Special handling for negative inventory (system shows < 0 on-hand): (a) system auto-creates adjustment request flagged as high priority; (b) immediate investigation by Dept. Supervisor — most common causes: (i) POS sold item not yet received (timing), (ii) POS sold wrong SKU (scanning error), (iii) cycle count in progress but not posted; (c) resolution within 24 hours; if unresolved, system blocks further sales of that SKU at that location until resolved (prevents cascading negative inventory) | System / Dept. Supervisor | Store Manager | 15 min/case |
| 7 | **Monthly shrinkage reporting**: Cost Accountant prepares monthly shrinkage report: (a) total adjustments by reason code, by location, by category; (b) shrinkage as % of sales (target: < 1.5% per company profile); (c) shrinkage trend by store — identify stores exceeding target; (d) adjustment authorization compliance — verify all adjustments properly approved per tier; (e) top 20 SKUs by shrinkage value; submits to Controller for management reporting per W35 | Cost Accountant | Controller | 2 hours/month |
| 8 | **Quarterly Internal Audit review**: Internal Audit samples adjustments quarterly: (a) verify authorization compliance (right approval tier used), (b) verify documentation completeness (reason code, investigation, evidence), (c) verify segregation of duties (requestor ≠ authorizer for Level 2+), (d) test negative inventory resolution timeliness; findings reported to CFO and Audit Committee | Internal Audit | CFO | 4 hours/quarter |

### System Touchpoints
- Auto-adjustment request creation from cycle count variances, physical inventory variances, negative inventory detection (W92.1)
- Reason code classification with mandatory documentation per code type (W92.2)
- Tiered approval workflow with amount-based routing and authorization trail (W92.4)
- GL posting with WAC recalculation and proper debit/credit routing (W92.5)
- Negative inventory alerting with auto-block on further sales (W92.6)
- Monthly shrinkage report: by reason, location, category, SKU (W92.7)
- Adjustment authorization compliance dashboard for Internal Audit (W92.8)
- Integration with W3 (DC receiving — short-shipment adjustments), W4 (replenishment — in-transit variances), W6 (cycle counting — primary source of adjustments), W12 (returns — cross-store adjustments), W22 (transfers — discrepancy adjustments), W37 (loss prevention — confirmed theft write-offs), W42 (annual physical inventory — major adjustments), W44 (vendor scorecard — vendor short-shipment rate), W88 (RTV — unresolved write-offs), W91 (damaged goods — disposition-driven adjustments)

### Pain Points / Risks
- Authorization tier bypass is a persistent control risk — Level 1 Store Managers sometimes split large adjustments into multiple sub-PHP 5,000 entries to avoid Cost Accountant review, circumventing the tiered approval design and obscuring material shrinkage.
- Negative inventory auto-block on further sales (step 6) can create customer-facing stockout situations when the root cause is a timing lag (POS sold before GR posted) rather than actual inventory loss; the 24-hour resolution SLA is aspirational during peak trading periods.
- Root cause classification accuracy (step 2) is inconsistent across 200 stores — Department Supervisors select generic reason codes ("other") when they lack time to investigate, degrading the value of monthly shrinkage reporting for loss prevention action (W37).
- The 20-adjustment/month limit per location without escalation (step 4) is easily exceeded during post-physical-inventory periods (W42), creating an approval backlog at the Cost Accountant level that delays GL posting and month-end close.
- Segregation of duties (requestor not equal authorizer for Level 2+) is difficult to enforce in small stores with only 3–4 management-level staff — the Stock Associate who identifies the variance, the Department Supervisor who investigates, and the Store Manager who approves may all have overlapping roles.

### Time Estimate
Adjustment request creation (step 1): 5 min. Root cause classification (step 2): 5 min. Investigation for material adjustments (step 3): 15 min. Authorization (step 4): 5–15 min per approval tier. Negative inventory resolution (step 6): 15 min/case. Monthly shrinkage reporting (step 7): 2 hours. Quarterly audit review (step 8): 4 hours. Total ongoing: ~8–12 adjustments/store/month × ~20 min average = ~3–4 hours/store/month across all involved roles.

### Staffing Implication
- **Cost Accountant**: adds ~2 hours/month for shrinkage reporting and Level 2 approvals. Absorbed.
- **Controller**: adds ~1 hour/month for Level 3 approvals and shrinkage review. Absorbed.
- **Internal Audit**: adds ~4 hours/quarter for adjustment testing. Absorbed.
- **No incremental headcount.**

---

## W105. Multi-Channel Inventory Allocation & Priority Governance

| Field | Detail |
|---|---|
| **Trigger** | Quarterly allocation governance review; or ad-hoc triggered by sustained stockout pattern, new channel launch, or allocation conflict escalation |
| **Frequency** | Quarterly governance review; continuous allocation monitoring |
| **Volume** | 35,000 active SKUs allocated across: 200 stores (W4), ecommerce BOPIS from stores (W11), ecommerce home delivery from DCs (W19), B2B trade/corporate orders (W58), promotional pre-positioning (W57), backorder fulfillment (W56) |
| **Owner** | Supply Planning Manager |
| **Participants** | Supply Planning Manager, VP Supply Chain, Category Manager, Ecommerce Manager, Sales Manager, DC Supervisor |

### Background

Multiple workflows reference inventory allocation: W4 (store replenishment with constrained allocation), W11 (BOPIS ATP reservation), W19 (home delivery ATP), W57 (promotional pre-positioning), and W56 (backorder priority). However, there is no unified governance framework defining allocation priorities when multiple demand channels compete for the same limited inventory. During constrained supply periods (vendor delays, seasonal peaks, promotional surges), the absence of clear priority rules leads to ad-hoc decisions, channel conflict, and customer dissatisfaction. This workflow establishes the allocation governance framework.

### Allocation Priority Hierarchy (Constrained Supply)

| Priority | Demand Channel | Rationale | Override Authority |
|---|---|---|---|
| 1 | **Existing customer backorders** (W56) | Customer already committed and waiting; highest service obligation | Supply Planning Manager |
| 2 | **Promotional pre-positioning** (W57) | Committed marketing spend; stockout during promo damages brand | VP Supply Chain + VP Merchandising |
| 3 | **Ecommerce BOPIS** (W11) | Customer already paid; fulfillment SLA of 4 hours | Supply Planning Manager |
| 4 | **Ecommerce home delivery** (W19) | Customer already paid; fulfillment SLA of 2–5 days | Supply Planning Manager |
| 5 | **B2B trade/corporate project orders** (W58) | Contractual obligation; high-value accounts | VP Supply Chain + Sales Manager |
| 6 | **Store replenishment — A-items** (W4) | Top 20% of SKUs generating 80% of revenue; highest retail impact | Supply Planning Manager |
| 7 | **Store replenishment — B-items** (W4) | Mid-tier items; moderate revenue impact | Supply Planning Manager |
| 8 | **Store replenishment — C-items** (W4) | Bottom 50% of SKUs; lowest revenue impact; highest tolerance for stockout | System auto-allocated from residual |

**Safety stock buffers**: each channel's ATP calculation deducts a configurable safety stock buffer that is NOT available for allocation to any channel — this buffer protects against demand variability and prevents complete stockout at any location.

- **DC safety stock**: configurable per SKU per DC (set during W31.8 parameter governance); deducted from DC ATP before any allocation
- **Store safety stock**: configurable per SKU per store; deducted from store ATP for BOPIS availability
- **BOPIS buffer**: stores reserve a configurable buffer (default: 2 units per A-item SKU) so that walk-in customers are not completely displaced by BOPIS orders

### Steps

### Quarterly Allocation Governance Review

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Allocation performance report**: System generates quarterly allocation performance report: (a) fill rate by demand channel (target: A-items ≥ 97%, B-items ≥ 93%, C-items ≥ 85%), (b) allocation conflicts — instances where demand exceeded supply and priority rules were applied, with channel impact, (c) safety stock breaches — instances where actual inventory fell below safety stock buffer (indicates systemic under-supply), (d) channel stockout frequency — how often did each channel experience out-of-stock due to allocation exhaustion?, (e) override log — all instances where default priority was overridden, with approver and justification | System | — | Automated |
| 2 | Supply Planning Manager reviews allocation performance with cross-functional stakeholders: (a) **Ecommerce Manager**: BOPIS and home delivery fill rate, customer impact of stockouts, allocation adequacy for peak events, (b) **Sales Manager**: B2B trade/corporate fill rate, impact on account relationships and revenue, (c) **Category Manager**: category-level fill rate, vendor supply reliability issues, (d) **DC Supervisor**: operational impact of allocation-driven picking priorities (promotional vs. routine orders), capacity conflicts | Supply Planning Manager | VP Supply Chain | 2 hours/quarter |
| 3 | **Allocation rule review**: Supply Planning Manager and VP Supply Chain review and adjust allocation rules: (a) are priority rankings still appropriate given channel revenue contribution and growth trajectory?, (b) are safety stock buffers adequate or excessive? (benchmark: buffer usage rate — how often is buffer consumed?), (c) should any channels be added or removed from the hierarchy? (e.g., new ship-from-store channel per W19B), (d) are ABC classification thresholds (W31.8) correctly driving allocation priority — do A-items get sufficient allocation vs. B/C-items? | Supply Planning Manager / VP Supply Chain | VP Supply Chain | 1 hour/quarter |
| 4 | **Conflict resolution from past quarter**: Review all allocation overrides from the past quarter — were they justified? Were the right approvers involved? Should any override patterns trigger a permanent rule change? (e.g., if B2B orders were frequently prioritized over ecommerce, consider adjusting the default hierarchy) | Supply Planning Manager | VP Supply Chain | 1 hour/quarter |
| 5 | Supply Planning Manager updates allocation configuration in system based on review: priority weights, safety stock parameters, ATP buffer rules; documents changes with effective date, rationale, and VP Supply Chain approval; system logs all configuration changes with audit trail | Supply Planning Manager | VP Supply Chain | 30 min/quarter |

### Continuous Allocation Monitoring

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 6 | System monitors allocation conflicts in real-time: when demand from a higher-priority channel exhausts available allocation for a lower-priority channel, system alerts Supply Planner with: SKU, location, channels affected, quantities short, and suggested action (expedite PO per W2, arrange inter-DC transfer per W22, or accept stockout) | System | — | Automated |
| 7 | Supply Planner reviews daily allocation conflict dashboard; resolves conflicts by: (a) expediting POs with vendors for critical shortfalls, (b) rebalancing safety stock buffers (temporary reduction for low-demand locations), (c) arranging emergency inter-DC transfers per W22, (d) recommending substitution to affected channel (alternative SKU with available inventory) | Supply Planner | Supply Planning Manager | 30 min/day |
| 8 | **Allocation override**: When a business decision requires deviating from the default priority (e.g., prioritizing a large corporate project order over routine store replenishment), requestor (Category Manager, Sales Manager, or Ecommerce Manager) submits allocation override request in system with: SKU, quantity, source location, requested priority channel, business justification, and revenue impact; VP Supply Chain approves overrides affecting > 5% of a location's inventory; system logs override with full audit trail | Requestor / VP Supply Chain | VP Supply Chain | 15 min/override |

### System Touchpoints
- Configurable allocation priority engine with channel-specific weights and safety stock buffers (W105 allocation hierarchy)
- ATP calculation per channel per SKU per location incorporating priority rules, safety stock, and existing commitments (W105 ATP logic)
- Quarterly allocation performance report with fill rate, conflicts, safety stock breaches, and override log (W105.1)
- Daily allocation conflict dashboard with real-time alerts and suggested actions (W105.6)
- Allocation override request workflow with VP Supply Chain approval and audit trail (W105.8)
- Integration with W4 (store replenishment), W11 (BOPIS), W19 (home delivery), W22 (inter-DC transfers), W31 (demand planning parameters), W56 (backorder priority), W57 (promo allocation), W58 (B2B orders)

### Pain Points / Risks
- Priority hierarchy is perceived as biased by channel owners (e.g., Ecommerce feels deprioritized vs. B2B trade), creating internal political friction and frequent override requests that undermine the governance framework.
- Safety stock buffers are difficult to calibrate — too high ties up working capital across 35K SKUs, too low leads to stockouts that trigger costly emergency transfers and expedited POs.
- ATP calculation complexity across 6 demand channels, 200 stores, 4 DCs, and 35K SKUs creates computational latency; stale ATP data leads to over-promising and subsequent cancellation or re-allocation.
- No automated feedback loop between override patterns and rule optimization — override frequency data exists but is not systematically used to improve the default hierarchy.

---

### Time Estimate
Quarterly governance review: 4–5 hours (report generation + cross-functional review + rule updates). Daily monitoring: 30 min/day for conflict dashboard review and resolution. Override approvals: ~15 min each, ad-hoc.

### Staffing Implication
- **Supply Planning Manager**: adds ~4 hours/quarter for governance review + 30 min/day for conflict monitoring = ~28 hours/quarter. Absorbed within existing role.
- **Supply Planner**: 30 min/day for conflict resolution = ~10 hours/month. Absorbed within existing planning duties.
- **VP Supply Chain**: ~2 hours/quarter for governance review + ~30 min/quarter for override approvals. Absorbed.
- **No incremental headcount.**

## W154. Proactive Store Inventory Rebalancing (Stock Push)

| Field | Detail |
|---|---|
| **Trigger** | High inventory variance between stores; slow-mover identification (W1); or localized demand spike |
| **Frequency** | Monthly |
| **Volume** | ~500–1,000 SKUs rebalanced per cycle |
| **Owner** | Supply Planning Manager |
| **Participants** | Supply Planner, Store Managers, Logistics |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Analysis**: Identify SKUs with "Overstock" at Store A and "Understock/High Velocity" at Store B | Supply Planner | Supply Planning Mgr | 4 hours |
| 2 | **Validation**: Store Managers confirm physical stock availability and condition for transfer | Store Manager | — | 30 min/store |
| 3 | **Push Order**: System generates "Push" Stock Transfers (W22); overrides standard ROP to clear excess | Supply Planner | Supply Planning Mgr | 1 hour |
| 4 | **Logistics**: Consolidate transfers into weekly DC-to-Store backhaul or store-to-store courier | Logistics | — | Varies |
| 5 | **Impact Review**: Measure sales lift at receiving store and holding cost reduction at sending store | Supply Planner | CFO | 2 hours |

### System Touchpoints
- Overstock/understock analysis dashboard with store-level inventory health comparison (W154.1)
- Automated push transfer order generation linked to W22 transfer workflow (W154.3)
- DC truck backhaul consolidation planning for store-to-store transfers (W154.4)
- Post-rebalancing impact dashboard: sales lift at receiving store, holding cost reduction at sending store (W154.5)

### Pain Points / Risks
- Store Manager validation delays (30 min/store across 50–100 affected stores) create a bottleneck; without timely confirmation, transfers are generated against phantom stock.
- Push transfers consume DC truck backhaul capacity, competing with store-to-DC returns (W22B) for limited reverse-logistics space on returning delivery trucks.
- Measuring actual impact is difficult — sales lift at the receiving store may be conflated with seasonal demand, making it hard to isolate the rebalancing benefit.
- Over-aggressive push transfers can leave the sending store understocked if demand patterns shift unexpectedly before the next regular replenishment cycle.

---

### Time Estimate
Monthly cycle: ~8 hours total (4 hours analysis + 1 hour order generation + 30 min/store validation + 2 hours impact review). Logistics consolidation varies by volume; typically absorbed into weekly DC backhaul schedules.

### Staffing Implication
- **Supply Planner**: ~8 hours/month for rebalancing analysis, push order generation, and impact review. Absorbed within existing 2–3 planner team.
- **Store Managers**: ~30 min/month for stock validation at affected stores (~50–100 stores). Absorbed.
- **Logistics**: consolidation into existing weekly DC backhaul schedule — no incremental staffing.
- **No incremental headcount.**

## W204. Regional Stock Rebalancing & Inter-Store Expedited Transfers

| Field | Detail |
|---|---|
| **Trigger** | Critical stock-out at Store A; excess stock of same SKU at Store B (within same region/cluster) |
| **Frequency** | Weekly |
| **Volume** | ~50–100 transfers per week |
| **Owner** | Regional Store Operations Manager |
| **Participants** | Store Managers, Supply Planner, Local Courier (3PL) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Opportunity Identification**: Store A Manager identifies "Sold Out" status for high-demand SKU; checks "Regional Inventory" in real-time system (W5) | Store Manager | — | 5 min |
| 2 | **Transfer Request**: Store A Manager initiates an "Expedited Transfer Request" from Store B (nearest location with > 2 weeks cover) | Store Manager | — | 2 min |
| 3 | **Approval**: Regional Manager or Supply Planner approves based on regional inventory health and cost of transfer vs. margin | Regional Manager | — | 1 hour |
| 4 | **Pick & Stage**: Store B Staff picks and stages items in backroom; system records "In-Transit" status (W22) | Stock Associate | Store Manager | 15 min |
| 5 | **Expedited Dispatch**: Local 3PL (Lalamove/Transportify) picks up from Store B; delivers to Store A within 4-8 hours | Logistics | — | 4-8 hours |
| 6 | **Receipt**: Store A Receiving Clerk processes Goods Receipt; inventory available for sale immediately | Receiving Clerk | Store Manager | 10 min |

### System Touchpoints
- Regional real-time inventory visibility dashboard for Store Managers (W204.1)
- Expedited transfer request workflow with Regional Manager approval routing (W204.2–3)
- Integration with W22 (transfer order and in-transit tracking) and W22A (store-level outbound fulfillment)
- Local 3PL booking integration (Lalamove/Transportify) for same-day courier dispatch (W204.5)

### Pain Points / Risks
- 3PL courier costs (PHP 500–2,000 per trip) are not systematically tracked against the margin of transferred items; low-margin SKUs transferred at high courier cost may result in net loss.
- Approval bottleneck when Regional Manager is unavailable — 1-hour SLA for approval is aspirational during peak periods, causing expedited transfers to stall.
- In-transit inventory for 3PL courier shipments lacks real-time tracking (unlike DC fleet GPS), creating blind spots if courier delays or misdelivers.
- High transfer frequency (~50–100/week) strains Store B picking capacity and competes with customer service during peak store hours.

---

### Time Estimate
Total cycle: 5–9 hours from identification to goods receipt (5 min identification + 1 hour approval + 15 min pick/stage + 4–8 hours transit + 10 min receipt). Regional Manager approval is the typical bottleneck at ~1 hour.

### Staffing Implication
- **Regional Store Operations Manager**: weekly oversight of ~50–100 transfers, ~2–3 hours/week for approval and coordination. Absorbed within existing regional management role.
- **Store Managers (source stores)**: ~15 min/week for picking and staging outbound transfers. Absorbed.
- **Store Managers (destination stores)**: ~10 min/week for receiving. Absorbed.
- **3PL courier cost**: PHP 500–2,000 per trip × ~50–100/week = PHP 100,000–800,000/week. Budgeted within regional logistics cost center.
- **No incremental headcount.**

## W214. Store-to-Store Expedited Transfers (Customer-Initiated)

| Field | Detail |
|---|---|
| **Trigger** | Customer requests an out-of-stock item at Store A that is in stock at Store B |
| **Frequency** | Daily |
| **Volume** | ~20–30 customer-initiated transfers per day |
| **Owner** | Store Manager (Store A) |
| **Participants** | Sales Associate, Store Manager B, 3PL Courier, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Inquiry**: Customer requests an out-of-stock item at Store A. Sales Associate checks real-time inventory in ERP and finds stock available at nearby Store B. | Sales Associate | — | 5 min |
| 2 | **Order & Payment**: Sales Associate offers to have the item transferred from Store B via expedited courier. Customer agrees and pays for the item (plus optional transfer fee) at Store A; system generates a "Customer-Initiated Transfer Order" with status "Awaiting Pickup". | Sales Associate | Store Manager A | 10 min |
| 3 | **Notification**: System automatically routes a high-priority pick task to Store B's terminal/handheld. | System | — | Automated |
| 4 | **Pick & Pack**: Store B Stock Associate picks the item, places it in secure packaging, and prints an transfer label with Store A's order number and Customer details. | Stock Associate B | Store Manager B | 15 min |
| 5 | **Dispatch**: Store B books a local 3PL courier (Lalamove/Grab/Transportify) via ERP integration to transport the item to Store A. | Store Manager B | — | 10 min |
| 6 | **Transit & Arrival**: 3PL Courier transports item to Store A. Store A Receiving Clerk receives it in the system; ERP automatically triggers an SMS/email to the Customer ("Your order is ready for pickup!"). | Courier / Store A Clerk | Store Manager A | 1–3 hours |
| 7 | **Customer Collection**: Customer arrives at Store A Pro Desk; Sales Associate scan-confirms collection and closes the transfer order. | Sales Associate | — | 5 min |

### System Touchpoints
- Real-time cross-store inventory lookup for Sales Associates via handheld/terminal (W214.1)
- Customer-initiated transfer order with payment capture and status tracking (W214.2)
- Automated high-priority pick task routing to source store (W214.3)
- 3PL courier booking integration (Lalamove/Grab/Transportify) via ERP (W214.5)
- Automated customer SMS/email notification upon goods receipt at destination store (W214.6)

### Pain Points / Risks
- Customer may not return to collect the item after transfer — system has no auto-cancellation timer, creating stranded inventory at Store A and tied-up payment that requires manual refund processing.
- 3PL courier reliability is inconsistent for inter-store delivery (especially between cities), leading to missed customer expectations on the 1–3 hour delivery promise.
- Optional transfer fee charged to customer is a friction point — some customers refuse, and absorbing the cost erodes margin on lower-value items.
- Source store Stock Associates may deprioritize customer-initiated pick tasks during busy periods, delaying the transfer and degrading the customer experience.

---

### Time Estimate
Total cycle: 2–4.5 hours from customer inquiry to pickup notification (5 min inquiry + 10 min payment + automated pick routing + 15 min pick/pack + 10 min dispatch + 1–3 hours transit + automated notification). Customer collection: 5 min.

### Staffing Implication
- **Sales Associates**: ~20–30 customer-initiated transfers/day ÷ 200 stores = ~0.1–0.15/store/day × 15 min each = ~2 min/store/day. Absorbed.
- **Source Store Stock Associates**: ~15 min per pick task; with ~20–30/day distributed across 200 stores, average < 1 per store per week. Absorbed.
- **3PL courier cost**: PHP 200–500 per trip × ~20–30/day = PHP 120,000–450,000/month. Absorbed within store operations cost center.
- **No incremental headcount.**

## W218. Inter-DC Stock Rebalancing (Stock Push)

| Field | Detail |
|---|---|
| **Trigger** | Supply planning identifies "Overstock" in one DC and "Stock-out Risk" in another |
| **Frequency** | Monthly; or as needed for peak seasons |
| **Volume** | Bulk pallet transfers |
| **Owner** | Supply Planning Manager |
| **Participants** | Supply Planner, DC Managers, Logistics (3PL Carrier) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Imbalance Detection**: Supply Planner reviews "DC-to-DC Inventory Health" report; identifies SKUs where current DC stock > 6 months cover vs. < 2 weeks at another DC | Supply Planner | — | 2 hours |
| 2 | **Transfer Proposal**: System suggests "Rebalancing Transfer" (Push) to move bulk stock to the understocked DC | System / Planner | Supply Planning Mgr | 1 hour |
| 3 | **Fulfillment Booking**: Logistics books heavy-duty transport (tractor head / 10-wheeler) for the bulk move | Logistics | — | 1 hour |
| 4 | **Loading**: Source DC picks from bulk storage; system verifies quantities via WMS (W3) | DC Picker | DC Supervisor | 2 hours |
| 5 | **Transit**: Bulk shipment moves between DCs; system tracks "In-Transit" at WAC | Driver | — | 1–3 days |
| 6 | **Receipt**: Destination DC processes bulk GR; inventory available for sale immediately | Receiving Clerk | DC Manager | 2 hours |
| 7 | **Efficiency Audit**: Review total freight cost vs. margin preserved by avoiding stock-outs | Supply Planning Mgr | — | Quarterly |

### System Touchpoints
- DC-level inventory health and cover analysis dashboard
- Bulk transfer order generation (Push mode)
- WMS bulk zone picking and receiving
- In-transit inventory value tracking between DCs

### Pain Points / Risks
- Inter-DC freight cost for bulk transfers (especially inter-island via W66) can exceed the margin preserved by avoiding stock-outs, making some rebalancing moves economically unjustifiable.
- In-transit inventory tied up for 1–3 days during inter-DC movement is unavailable to any channel, creating temporary allocation conflicts in the source DC's residual inventory.
- Bulk transfer proposals rely on static cover-day thresholds (6 months vs. 2 weeks) that do not account for upcoming promotions (W57) or seasonal demand shifts, leading to poorly timed transfers.
- 3PL carrier availability for heavy-duty transport (10-wheeler, tractor head) is limited during peak construction season, delaying rebalancing execution.

---

### Time Estimate
Planning: 3 hours/month (2 hours imbalance detection + 1 hour transfer proposal). Execution: 1–3 days transit + 4 hours combined loading/receiving. Efficiency audit: 2 hours/quarter.

### Staffing Implication
- **Supply Planning Manager**: ~3 hours/month for imbalance detection and transfer proposal review. Absorbed.
- **Supply Planner**: ~2 hours/month for transfer execution monitoring. Absorbed within existing planner duties.
- **DC Staff (source and destination)**: ~4 hours combined per transfer for loading and receiving. With ~5–10 transfers/month across 4 DCs, this is ~4–8 hours/DC/month. Absorbed.
- **Logistics (3PL carrier)**: heavy-duty transport (10-wheeler, tractor head) for inter-DC bulk movement booked per event. Cost: PHP 15,000–50,000 per trip depending on distance and island. Budgeted within logistics cost center.
- **No incremental headcount.**

## W219. Store Inventory Quarantine & Recertification

| Field | Detail |
|---|---|
| **Trigger** | Customer return (W12), cycle count discrepancy, or receive inspection identifies suspected, damaged, or expired stock |
| **Frequency** | Daily across all stores |
| **Volume** | ~20–50 items/store/month |
| **Owner** | Store Quality Inspector |
| **Participants** | Store Quality Inspector, Stock Associate, Store Manager, Category Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Quarantine Creation**: CSR or Stock Associate flags stock as "Damaged" or "Suspect"; system moves inventory from "Saleable" status to "Quarantined" status (Dr. Quarantined Inventory / Cr. Saleable Inventory) and moves to quarantine location | CSR / Stock Associate | Store Manager | 5 min |
| 2 | **Physical Segregation**: Stock Associate prints "Quarantine Label" from system; attaches to item and physically moves to the secure store quarantine cage | Stock Associate | Dept. Supervisor | 10 min |
| 3 | **Inspection & Evaluation**: Store Quality Inspector performs physical inspection; uploads photo evidence to system; classifies defect (e.g., cosmetic package damage, internal mechanical fault, paint tint mismatch) | Quality Inspector | Store Manager | 15 min |
| 4 | **Disposition Determination**: Inspector enters recommended disposition: (a) *Refurbish & Recertify* (repackage, clean, test); (b) *B-Grade Downgrade* (cosmetic damage, sell on discount); (c) *Scrap / Write-off*; (d) *Return to Vendor (RTV)* | Quality Inspector | Store Manager | 10 min |
| 5 | **Action Execution**: <br>• (a) *Refurbish*: Stock Associate performs repacking; system updates status to "Saleable" (Dr. Saleable Inventory / Cr. Quarantined Inventory);<br>• (b) *B-Grade*: System moves SKU to "B-Grade/Clearance" status and auto-applies standard clearance markdown (W93);<br>• (c) *Scrap*: Store Manager approves; system posts inventory adjustment (Dr. Scrap Expense / Cr. Quarantined Inventory) and schedules disposal (W82);<br>• (d) *RTV*: System generates Return to Vendor request (W88) | Stock Associate / System | Store Manager | 15 min |
| 6 | **Discrepancy Reporting**: Quality Inspector generates monthly quarantine velocity and defect report to highlight recurring SKU failures to Category Managers | Quality Inspector | Store Manager | 1 hour/month |

### System Touchpoints
- Segregated quarantine inventory status (non-ATP)
- Photographic upload and defect category logging in system
- Automated financial posting for status transitions and write-offs
- Integration with W93 (markdowns), W88 (RTV), and W82 (hazmat/scrap)

### Pain Points / Risks
- Quarantine cage space is limited in stores; during high-damage periods (typhoon season, post-promo returns), physically segregating all suspect items becomes impractical, leading to commingling with saleable stock.
- Quality Inspector role is often filled by a Department Supervisor as a collateral duty, creating inspection backlogs during peak periods and inconsistent defect classification.
- Refurbishment (repacking, cleaning, testing) requires labor and materials that may exceed the recovered item value, especially for low-cost SKUs, making the refurbish path uneconomical.
- Monthly defect reports are not consistently actioned by Category Managers — recurring SKU failures from specific vendors persist without systematic vendor quality escalation (W44).

---

### Time Estimate
~45 min per item from quarantine creation through disposition (5 min flag + 10 min segregation + 15 min inspection + 10 min disposition + 15 min action execution). Quality Inspector spends ~1 hour/month on discrepancy reporting. Stores processing 20–50 items/month spend ~15–35 hours/month total.

### Staffing Implication
- **Store Quality Inspector**: ~20–50 items/store/month × 25 min average (inspection + disposition) = ~8–20 hours/store/month. Role is typically a collateral duty filled by Department Supervisor; high-volume stores may require dedicated hours.
- **Stock Associates**: ~15 min per item for quarantine segregation and action execution. With ~20–50 items/month, this is ~5–12 hours/store/month. Absorbed.
- **Store Manager**: ~5 min approval per disposition. Absorbed.
- **No incremental headcount**, but stores processing > 40 items/month should consider formalizing the Quality Inspector collateral duty with protected time allocation.

## W220. Slow-Moving & Obsolete Inventory (SLOB) Provisioning & Liquidation

| Field | Detail |
|---|---|
| **Trigger** | Monthly inventory aging cycle or system alert on aging thresholds |
| **Frequency** | Monthly |
| **Volume** | Reviewing ~500–1,000 slow-moving SKUs chain-wide |
| **Owner** | Inventory Control Manager |
| **Participants** | Inventory Control Manager, Category Manager, CFO, VP Merchandising, Store Managers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Aging Detection**: System generates monthly aging report showing SKUs with > 180 days since last sale or inventory age exceeding category-specific thresholds (e.g., lumber shelf life, paint expiry) | System | Inventory Control Mgr | Automated |
| 2 | **Obsolescence Provisioning**: Finance automatically calculates SLOB provision using standardized logic (e.g., 50% provision for 180–270 days age, 100% provision for > 270 days); system posts journal (Dr. Inventory Obsolescence Expense / Cr. SLOB Inventory Allowance) | System / Financial Analyst | CFO | 2 hours |
| 3 | **Liquidation Campaign Proposal**: Inventory Control Manager routes the aging SKU list to the respective Category Manager with recommended liquidation strategies: (a) in-store clearance markdown (W93); (b) bulk wholesaler buy-out (W146); (c) stock transfer to high-velocity stores (W204); (d) vendor buy-back | Inventory Control Mgr | Category Manager | 2 days |
| 4 | **Strategy Approval**: Category Manager selects liquidation route; CFO/VP Merchandising approves any margin impact exceeding PHP 100K | Category Manager | CFO | 1 day |
| 5 | **Campaign Execution**: <br>• For in-store clearance: system applies pricing markdown;<br>• For redistribution: system auto-generates transfer orders (W204);<br>• For wholesaler: system creates Wholesale Sales Order (W146) | System / Category Manager | — | 1 hour |
| 6 | **Allowance Release**: Upon actual sale of liquidated items or approved physical scrap write-off: system releases the provision allowance (Dr. SLOB Inventory Allowance / Cr. Inventory Asset) to realize the final inventory value | System | Financial Analyst | Automated |

### System Touchpoints
- Automated Inventory Aging Engine (180, 270, 360+ days)
- Financial provisioning logic matrix
- Automated GL posting for obsolescence reserves and allowance release
- Integration with W93 (markdowns), W204 (transfers), and W146 (wholesale sales)

### Pain Points / Risks
- Category Managers resist markdown decisions on SLOB items because aggressive discounting hurts category margin KPIs, creating organizational friction that delays liquidation and deepens write-downs.
- Standardized provisioning logic (50% at 180–270 days, 100% at 270+) is a blunt instrument that does not differentiate between seasonal items with predictable recovery (e.g., construction materials with dry-season demand) and genuinely obsolete products.
- Bulk wholesaler buy-out prices (W146) are typically 20–40% of cost, representing significant loss; the decision between holding for in-store clearance (slow recovery) vs. quick wholesale disposal (fast but steeper loss) is contentious.
- SLOB allowance release timing creates P&L volatility — large scrap events or bulk liquidation in a single month can materially distort monthly margin reporting for affected categories.


### Time Estimate
Monthly cycle: ~4 hours for Inventory Control Manager (report review + campaign proposal routing + execution tracking) + 2 hours for Financial Analyst (provisioning calculation) + 1–2 days for Category Manager approval. Campaign execution: 1 hour system setup.

### Staffing Implication
- **Inventory Control Manager**: ~4 hours/month for aging report review, campaign proposal routing, and execution tracking. Absorbed.
- **Financial Analyst**: ~2 hours/month for SLOB provisioning calculation. Absorbed.
- **Category Manager**: 1–2 days/month for liquidation strategy selection and approval. Absorbed within existing merchandising workload.
- **CFO / VP Merchandising**: ~30 min/month for approvals on margin impact > PHP 100K. Absorbed.
- **Store Managers**: minimal — execution is system-driven (markdowns, transfer orders).
- **No incremental headcount.**

---

## W439. In-Store Bulk-to-Retail Repackaging Operations

| Field | Detail |
|---|---|
| **Trigger** | Store inventory of retail-sized packs (e.g., 1kg nails) falls below ROP while bulk stock (e.g., 50kg crate) is available |
| **Frequency** | Weekly or as needed per department |
| **Volume** | ~10–30 SKUs repacked per week per store |
| **Owner** | Department Supervisor |
| **Participants** | Stock Associate, Receiving Clerk, Department Supervisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Identify Need**: System alert or visual inspection shows retail SKU stockout; Stock Associate confirms bulk SKU availability | Stock Associate | Dept Supervisor | 5 min |
| 2 | **Repack Order**: System generates a "Repack/Conversion Order" linking Bulk SKU (source) to Retail SKU (target) | Dept Supervisor | — | 5 min |
| 3 | **Bulk Release**: Warehouse/Stockroom releases bulk unit (e.g., 1 crate) to the designated repacking area | Stock Associate | — | 10 min |
| 4 | **Repackaging**: Associate weighs/measures bulk stock into retail units (bags, coils); applies consumables (plastic bags, ties, labels) | Stock Associate | — | 30–60 min |
| 5 | **Labeling**: System generates and prints retail barcodes for each unit; Associate applies labels | Stock Associate | — | 15 min |
| 6 | **Verification & Posting**: Supervisor verifies count and weight; posts completion in ERP; system reduces bulk inventory and increases retail inventory | Dept Supervisor | Dept Supervisor | 10 min |
| 7 | **Waste/Loss Recording**: Any weighing loss or "dust" recorded as shrinkage within the repack order | Dept Supervisor | — | 2 min |

### System Touchpoints
- Inventory conversion module (Bulk-to-Retail) supporting 1-to-many SKU relationships
- Automated label printing linked to repack orders
- Consumable tracking (packaging materials) deducted as part of repack cost
- Shrinkage/loss capture per repack transaction

### Pain Points / Risks
- Inaccurate weighing leading to inventory discrepancies and customer complaints (under-weight packs).
- High labor cost for manual repacking; if not tracked, the true margin of retail-sized items is overstated.
- Labeling errors (wrong SKU or price) leading to POS issues.

### Staffing Implication
~1–2 hours per session, typically 2 sessions/week per department. Absorbed by existing Stock Associates during low-traffic hours.

---

## W514. Inventory Count Reconciliation & Variance Root Cause Analysis

| Field | Detail |
|---|---|
| **Trigger** | Cycle count (W6) or physical inventory (W42) completion reveals variance exceeding configurable thresholds |
| **Frequency** | Weekly per store (from daily cycle counts); annually from wall-to-wall physical inventory |
| **Volume** | ~200–300 variance investigations/month across 200 stores; ~50–80 requiring full root cause analysis |
| **Owner** | Inventory Control Manager |
| **Participants** | Store Manager, Stock Associate, Inventory Analyst, Loss Prevention Officer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System flags variances from completed counts against configurable thresholds: A-items >±0.5% or >±PHP 5K; B-items >±1% or >±PHP 3K; C-items >±2% or >±PHP 1K; generates variance exception report per store | System | — | Automated |
| 2 | Store Manager reviews variance exception report for their store; performs initial assessment: (a) obvious data entry error (transposed digits, wrong SKU scanned) → immediate correction with documentation; (b) legitimate unexplained variance → route to Inventory Analyst | Store Manager | Inventory Control Manager | 30 min |
| 3 | For unexplained variances: Inventory Analyst opens variance investigation case; system auto-populates: SKU details, count vs. system quantity, dollar value of variance, last 3 count results for this SKU, recent transaction history (receipts, transfers, sales, adjustments) | Inventory Analyst | Inventory Control Manager | 5 min |
| 4 | Inventory Analyst categorizes suspected root cause: (a) Receiving error (quantity mismatch at GR); (b) Miscount (counter error, counted wrong SKU); (c) Unit-of-measure confusion (case vs. piece); (d) System error (integration failure, duplicate posting); (e) Unpicked/unstorable inventory in wrong location; (f) Shrinkage/theft (no other explanation) | Inventory Analyst | Inventory Control Manager | 15 min |
| 5 | For receiving errors: Inventory Analyst traces to original GR document; contacts DC or vendor to verify shipment quantity; if confirmed short shipment, initiates vendor claim (W88) or DC discrepancy resolution | Inventory Analyst | Inventory Control Manager | 20 min |
| 6 | For suspected shrinkage/theft (variance >PHP 10K or pattern across multiple counts): Inventory Analyst escalates to Loss Prevention Officer for investigation (W248); LP Officer reviews CCTV, EBR exceptions, and employee access logs | Inventory Analyst | LP Manager | 10 min |
| 7 | Inventory Analyst documents root cause finding and recommended corrective action in variance case: (a) process improvement (receiving checklist, count procedure update); (b) system fix (integration correction, master data update); (c) LP referral; (d) no action (within acceptable tolerance) | Inventory Analyst | Inventory Control Manager | 10 min |
| 8 | Inventory Control Manager reviews and closes variance case; approves corrective action; system updates inventory with approved adjustment (W92) referencing variance case number | Inventory Control Manager | VP Supply Chain | 5 min |
| 9 | Monthly: Inventory Control Manager generates variance root cause dashboard: variance rate by store, category, and root cause; top 20 stores by variance rate; top 20 SKUs by recurrence; corrective action completion rate | Inventory Control Manager | VP Supply Chain | 2 hours |
| 10 | Quarterly: Inventory Control Manager presents variance trend analysis to operations leadership: variance rate trend (goal: <1.5% shrinkage), root cause distribution, most improved/declined stores, systemic issues requiring capital investment (e.g., CCTV upgrades, receiving process redesign) | Inventory Control Manager | VP Supply Chain | 4 hours/quarter |

### System Touchpoints
- Automated variance flagging against ABC-classified thresholds (INV-022, INV-004)
- Variance investigation case management with structured root cause taxonomy (INV-022)
- Transaction history retrieval for variance tracing (INV-022)
- Receiving error traceability to original GR document (W3, W18)
- LP escalation integration for theft-related variances (W248, INV-022)
- Corrective action tracking with completion monitoring (INV-022)
- Monthly variance root cause dashboard by store, category, and cause (INV-022)
- Quarterly trend analysis with shrinkage rate tracking (INV-022)
- Integration with cycle counting (W6) and physical inventory (W42)

### Time Estimate
Initial review: ~30 min/store/week. Full root cause analysis: ~30–60 min/case × ~80 cases/month = ~40–80 staff-hours/month. Monthly dashboard: ~2 hours. Total: ~50–90 staff-hours/month. Absorbed by Inventory Control Manager and Inventory Analysts within existing FTE.

### Pain Points / Risks
- Root cause "unknown" selected too frequently, undermining analysis value — mitigated by mandatory investigation documentation for variances >PHP 5K and quarterly unknown-rate target (<15%)
- Variance investigation backlog when multiple stores flag simultaneously — mitigated by tiered approach (A-items prioritized, C-items batch-processed monthly)
- Corrective actions not implemented, causing recurring variances — mitigated by corrective action completion tracking and quarterly trend review

### Staffing Implication
- 1 Inventory Control Manager and 2–3 Inventory Analysts at HQ absorb this within existing FTE.
- Store Managers spend ~30 min/week on initial variance review (absorbed in daily duties).
- LP Officers involved for ~10–15 theft-related escalations/month (absorbed within existing LP team of 20).

---

## W587. Inventory Obsolescence Identification & Write-Off Management

| Field | Detail |
|---|---|
| **Trigger** | Monthly SLOB aging review identifies items that have exhausted all disposition channels (markdown, clearance, RTV, liquidation); or quarterly obsolescence review cycle |
| **Frequency** | Monthly candidate review; quarterly bulk write-off execution |
| **Volume** | ~150–300 SKU-locations per monthly review (~50–100 truly obsolete requiring write-off); annual write-off value estimated at PHP 30–60M (0.05–0.10% of PHP 62.3B revenue) |
| **Owner** | Inventory Control Manager |
| **Participants** | Inventory Control Manager, Financial Analyst, Cost Accountant, Controller, CFO, Category Manager, Store Manager, VP Merchandising, Legal Counsel (for BIR documentation), Board Secretary (for material write-offs) |

### Background

W220 (SLOB Provisioning & Liquidation) identifies slow-moving and obsolete inventory and attempts disposition through markdown (W93), RTV (W88), wholesaler bulk buy-out (W146), inter-store rebalancing (W204), and liquidation campaigns. However, not all SLOB items can be recovered through these channels. Some items reach a terminal state: they cannot be sold at any price, vendors refuse return, liquidators decline them, and they have no residual market value. These items must be formally written off the books and physically disposed of. Philippine Bureau of Internal Revenue (BIR) requires documented evidence for inventory write-offs claimed as deductible losses under Section 34(D)(2) of the National Internal Revenue Code — including board resolution for material amounts, physical inventory count documentation, and proof that all reasonable recovery efforts were exhausted. This workflow governs that final disposition step: identifying truly obsolete inventory, securing approvals, preparing BIR-compliant documentation, executing the system write-off, and managing physical disposal.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Obsolescence candidate identification**: System generates monthly obsolescence candidate report filtering SLOB items where ALL of the following conditions are met: (a) item age > 365 days since last sale across ALL locations (no store has sold a unit in the past 12 months), (b) item has been through at least one markdown cycle per W93 with < 10% sell-through, (c) RTV attempt per W88 was either rejected by vendor or vendor is unresponsive (> 90 days), (d) no active liquidation campaign or wholesaler interest per W220 step 3, (e) current WAC value per unit < PHP 100 (below economic threshold for further disposition effort) OR item is damaged/defective per W91 and classified as scrap, (f) system flags each candidate as "Obsolescence Candidate" with full disposition history attached (markdown attempts, RTV attempts, liquidation offers, aging timeline) | System | Inventory Control Manager | Automated |
| 2 | **Inventory Control Manager review**: Inventory Control Manager reviews obsolescence candidate list; for each SKU validates: (a) confirms disposition history is complete — all channels attempted with documented results, (b) checks if any upcoming seasonal demand per W32 seasonal calendar might recover value (e.g., rainy season items flagged in January may still sell in June), (c) confirms no pending customer backorders (W56) or B2B quotes (W58) referencing the SKU, (d) for high-value items (WAC > PHP 50,000 total across all locations): requests Category Manager to make one final vendor buy-back attempt before write-off, (e) classifies each candidate: "Approve for Write-Off" or "Defer — Recovery Possible" with deferral reason and re-review date | Inventory Control Manager | VP Supply Chain | 3–4 hours/month |
| 3 | **Category Manager concurrence**: For items "Approved for Write-Off," Category Manager reviews and concurs — confirming the item has no strategic assortment value (not part of future seasonal plan per W32, not a core assortment staple, vendor relationship does not require continued stocking). Category Manager may override and request extended markdown or one final disposition attempt. For items with total WAC value > PHP 200,000 per SKU: Category Manager documents rationale for write-off and submits to VP Merchandising for concurrence | Category Manager | VP Merchandising | 2 hours/month |
| 4 | **Financial impact assessment**: Financial Analyst prepares write-off financial impact summary: (a) total units and WAC value by SKU, by category, by location (store vs. DC), (b) SLOB provision already booked per W220 step 2 — net incremental P&L impact (write-off value less existing provision), (c) tax impact — estimated deductible loss under BIR Section 34(D)(2) and tax savings at 30% corporate tax rate, (d) impact on inventory turns (current vs. projected post-write-off), (e) cumulative write-off YTD vs. budget; Financial Analyst groups write-offs into tiers for approval routing | Financial Analyst | Controller | 3 hours/month |
| 5 | **Approval matrix execution**: Write-off requests routed per value threshold: (a) **Store Manager** approves individual store write-offs ≤ PHP 50,000 per SKU per location — limited to items physically located at their store; (b) **Regional Manager** approves cumulative store-level write-offs > PHP 50,000 and ≤ PHP 200,000 per SKU within their region; (c) **VP Supply Chain** approves write-offs > PHP 200,000 and ≤ PHP 1,000,000 per SKU chain-wide; (d) **CFO** approves write-offs > PHP 1,000,000 per SKU chain-wide; (e) **Board of Directors** approves aggregate quarterly write-offs exceeding PHP 5,000,000 per category or PHP 20,000,000 total via board resolution — required for BIR documentation of material inventory losses; each approver reviews financial impact summary and dispositions history before signing; approval documented in system with digital signature and timestamp | Per tier above | Controller (overall accountability) | 5–15 min/approval; Board resolution: 1 board meeting/quarter |
| 6 | **BIR documentation preparation**: For approved write-offs, Legal Counsel and Financial Analyst prepare BIR-compliant documentation package: (a) **Physical inventory count documentation** — system-generated count report confirming physical existence of items to be written off (tied to most recent cycle count per W6 or annual physical inventory per W42), (b) **Disposition history report** — system-generated audit trail showing all recovery attempts: markdown history per W93, RTV attempts per W88, liquidation offers per W220, with dates, prices offered, and outcomes, (c) **Board resolution** (for write-offs > PHP 5M per category) — Board Secretary prepares resolution citing: reason for write-off, total amount, certification that all reasonable recovery efforts were made, authorization for Controller to execute write-off and file BIR deduction, (d) **Affidavit of loss / destruction** (for physical disposal) — notarized statement confirming items were unsalvageable and will be or have been physically destroyed, (e) **Supporting evidence** — photographs of obsolete/damaged items, vendor refusal letters or emails, liquidation broker decline documentation, (f) documentation filed in tax records with retention per BIR requirement (10 years from filing date) | Legal Counsel / Financial Analyst / Board Secretary | Controller | 4–6 hours/quarter for documentation package |
| 7 | **System write-off execution**: Upon final approval: (a) Cost Accountant executes write-off batch in system per approved list; (b) system posts GL entries per item: Dr. Inventory Obsolescence Expense (or Dr. SLOB Inventory Allowance if provision exists per W220) / Cr. Inventory Asset — at WAC per unit × quantity; (c) for items with existing SLOB provision per W220 step 2: Dr. SLOB Inventory Allowance / Cr. Inventory Asset (net impact reduces the provision and removes the asset), with residual (Dr. Inventory Obsolescence Expense / Cr. SLOB Inventory Allowance) for any shortfall between provision and write-off value; (d) system updates inventory on-hand to zero at all affected locations; (e) system removes items from ATP, replenishment planning, and allocation engines; (f) system marks item master status as "Obsolete — Written Off" for items with zero remaining chain-wide inventory; (g) system generates write-off posting report with GL entry references for audit trail | Cost Accountant | Controller | 2–3 hours/batch (quarterly) |
| 8 | **Post-write-off physical disposal**: After system write-off, physical items must be removed from stores and DCs: (a) **Non-hazardous items** (hardware, tools, tiles, fixtures): Stock Associate stages written-off items at receiving dock; DC or store arranges disposal via licensed waste hauler or donation to charitable organization (with donation receipt for documentation — no tax benefit since already written off, but supports CSR); (b) **Hazardous items** (paint, adhesives, chemicals, solvents): disposal per W82 hazardous waste protocol — licensed hazardous waste hauler required; disposal certificate obtained and filed with BIR documentation; (c) **Metal/scrap items** (steel bar, copper wire, aluminum): sold to scrap metal dealer for residual value; residual recovery recorded as other income (Dr. Cash / Cr. Other Income — Scrap Recovery); (d) Department Supervisor confirms physical disposal in system with disposal date, method, and hauler/dealer reference; (e) system closes write-off case | Stock Associate / DC Supervisor | Store Manager / DC Manager | 2–4 hours/location per quarterly batch |
| 9 | **Quarterly write-off reporting**: Controller prepares quarterly inventory write-off report for CFO and Audit Committee: (a) total write-offs by category, by location type (store vs. DC), by root cause (obsolescence, damage, vendor refusal, expired), (b) write-off as % of beginning inventory value (target: < 0.15% of inventory per quarter), (c) SLOB provision adequacy — compare actual write-offs to provisions booked per W220; identify under/over-provisioned categories, (d) aging of write-offs from initial SLOB identification to final write-off (target: < 12 months), (e) physical disposal completion rate — items written off but not yet physically removed from premises, (f) BIR documentation completeness audit — confirm all write-off events have complete documentation packages | Controller | CFO | 3 hours/quarter |
| 10 | **Annual tax filing support**: At year-end tax filing, Financial Analyst compiles all quarterly write-off documentation into annual BIR deductible loss schedule: (a) aggregate inventory write-off claimed as deductible loss per Section 34(D)(2), (b) cross-referenced to board resolutions, physical count reports, and disposal certificates, (c) submitted to external tax advisor for review before BIR filing; external auditor confirms write-off testing as part of annual audit per W9B | Financial Analyst / External Tax Advisor | Controller | 8–10 hours/year |

**Total time per quarterly write-off cycle**: ~25–35 hours (Inventory Control Manager review 12–16 hours, Financial Analyst assessment 9–12 hours, Cost Accountant execution 6–9 hours, Controller reporting 3 hours, Legal documentation 4–6 hours) spread across the quarter with concentrated effort in the final 2 weeks.

### System Touchpoints (W587 — Obsolescence Write-Off)

- Obsolescence candidate identification engine with multi-condition filter: no sale > 365 days, failed markdown, failed RTV, no liquidation interest, WAC threshold (W587.1)
- Disposition history aggregation per SKU: markdown history (W93), RTV history (W88), liquidation attempts (W220), age timeline, linked to candidate report for audit trail (W587.1)
- Seasonal calendar cross-reference to prevent premature write-off of seasonal items with upcoming demand window per W32 (W587.2)
- Pending backorder and B2B quote check to prevent write-off of items with active customer commitments (W587.2)
- Financial impact calculator: WAC value, existing SLOB provision offset, net P&L impact, tax benefit estimation (W587.4)
- Tiered approval workflow with amount-based routing (Store Manager → Regional → VP → CFO → Board) and digital signature capture (W587.5)
- Board resolution template generation with auto-populated write-off amounts and SKU summaries (W587.6)
- Batch write-off GL posting engine: handles provision offset (W220), residual loss recognition, inventory removal, ATP and allocation purge, item master status update (W587.7)
- Physical disposal tracking with method (waste hauler, hazardous disposal per W82, scrap sale, donation), hauler reference, and completion confirmation (W587.8)
- Quarterly write-off reporting dashboard: by category, root cause, location, provision adequacy, disposal completion rate (W587.9)
- Annual BIR deductible loss schedule compilation from quarterly write-off data (W587.10)
- Integration with W6 (cycle count — physical existence confirmation), W42 (annual physical inventory — wall-to-wall count as write-off evidence), W56 (backorder — pending commitment check), W58 (B2B quotes — active quote check), W82 (hazardous waste — regulated disposal), W88 (RTV — disposition history and vendor refusal evidence), W91 (damaged goods — damage-driven obsolescence), W93 (markdown — disposition history and sell-through failure evidence), W146 (wholesale — liquidation attempt history), W220 (SLOB provisioning — provision offset and aging analysis), W32 (seasonal planning — seasonal demand check), W204 (rebalancing — inter-store transfer attempt history)

### Pain Points / Risks

- **Premature write-off of seasonal items**: items flagged as obsolete (no sales in 12 months) may be seasonal with demand in the upcoming season window; the W32 seasonal calendar cross-reference mitigates this but relies on accurate seasonal classification in the item master — misclassified seasonal items risk being written off before their next selling window.
- **Board resolution bottleneck**: material write-offs (> PHP 5M per category) require board resolution that can only be obtained at scheduled quarterly board meetings; if the write-off batch is prepared after the board meeting, it must wait up to 3 months, during which obsolete inventory continues to occupy physical space and distort inventory metrics.
- **BIR documentation completeness risk**: if physical disposal occurs before BIR documentation is fully assembled (photographs, vendor refusal letters, board resolution), the company may lack sufficient evidence to defend the deductible loss claim during a BIR audit; tight coordination between Legal Counsel and Store/DC operations is critical.
- **Physical disposal lag**: items written off in the system (on-hand = 0) but not yet physically removed from premises create a gap between book records and physical reality; during this lag, cycle counts (W6) or physical inventory (W42) will flag variances for items that are physically present but systemically at zero, wasting investigation effort.
- **Scrap recovery leakage**: residual value from scrap metal items (steel bar, copper wire) is small but aggregated across 200 stores and 4 DCs can reach PHP 500K–1M annually; if scrap dealers pay cash to store-level staff without system documentation, the recovery income is lost and poses a fraud risk.
- **Category Manager resistance to concurrence**: write-offs directly reduce category margin KPIs; Category Managers may delay concurrence (step 3) by requesting "one more attempt" at markdown or liquidation, extending the aging timeline and inflating the eventual write-off amount as holding costs accumulate.
- **Inter-entity complexity for DC-held obsolete inventory**: DC facilities are operated by Logistics Inc. per W14; obsolete inventory written off from DC locations requires coordination with Logistics Inc. for physical disposal from their premises and potential IC adjustment if warehousing fees were charged on already-provisioned inventory.

### Staffing Implication

- **Inventory Control Manager**: ~12–16 hours/quarter for candidate review, validation, and coordination. This is the heaviest incremental load and is concentrated in the final 2 weeks of each quarter. Absorbed within existing role but competes with W220 monthly SLOB review (combined SLOB + obsolescence workload is ~20–24 hours/quarter).
- **Financial Analyst**: ~9–12 hours/quarter for financial impact assessment and BIR documentation compilation; ~8–10 hours/year for annual tax filing support. Absorbed within existing Finance team.
- **Cost Accountant**: ~6–9 hours/quarter for write-off batch execution and GL posting. Absorbed.
- **Controller**: ~3 hours/quarter for quarterly write-off reporting and CFO presentation. Absorbed.
- **Legal Counsel**: ~4–6 hours/quarter for BIR documentation review, board resolution preparation, and affidavit of loss/destuction notarization coordination. Absorbed within existing legal function.
- **Category Managers**: ~2 hours/quarter for concurrence review. Absorbed within existing merchandising workload.
- **Store/DC Staff**: ~2–4 hours/location/quarter for physical disposal of written-off items. With ~150–300 SKU-locations per quarterly batch distributed across 204 locations, most locations handle < 5 items per quarter. Absorbed by existing Stock Associates.
- **No incremental headcount**; however, the combined W220 + W587 quarterly cycle (~30–40 hours) creates peak workload for the Inventory Control Manager that should be monitored for sustainability.

---

## W588. Seasonal Inventory Build-Down & Transition Execution

| Field | Detail |
|---|---|
| **Trigger** | Seasonal calendar countdown — 8 weeks before official season end date per W32 seasonal calendar; or Category Manager-initiated early build-down for underperforming seasonal categories |
| **Frequency** | 4 major seasonal build-downs/year: Christmas (build-down starts November week 1), Summer (starts April week 1), Back-to-School (starts July week 1), Rainy Season (starts October week 1); each covering 3,000–5,000 seasonal SKUs |
| **Volume** | ~3,000–5,000 seasonal SKUs per build-down across 200 stores; ~600,000–1,000,000 store-SKU transitions per cycle; estimated seasonal inventory at build-down start: PHP 800M–1.5B (12–24% of total inventory at peak seasonal stocking) |
| **Owner** | Category Manager |
| **Participants** | Category Manager, Buyer, Supply Planner, Pricing Analyst, VP Merchandising, Store Manager, Department Supervisor, Stock Associate, Visual Merchandising Coordinator, Inventory Control Manager, Controller |

### Background

W264 (Seasonal Merchandise Transition & Display Rotation) covers the overall seasonal transition process including incoming season setup, and W32 (Seasonal Buy Planning) governs pre-season procurement. However, the critical final phase of each season — systematically reducing seasonal inventory to minimize residual dead stock while maximizing sell-through at acceptable margins — lacks a dedicated operational workflow. Without a structured build-down process, seasonal inventory reduction is reactive: markdowns are applied too late, disposition decisions are made inconsistently across 200 stores, and seasonal displays are torn down ad-hoc, leaving valuable retail space underutilized during the transition gap. This workflow operates in the final 8 weeks of each season and orchestrates: (a) pre-season-end inventory assessment, (b) markdown escalation schedule, (c) remaining stock disposition decision tree, (d) display teardown coordination, and (e) new season inventory receipt and staging. It works in concert with W574 (store closing), W583 (promo transition), and W554 (shelf replenishment) at the store level.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-season-end inventory review (T-8 weeks)**: Category Manager initiates build-down review 8 weeks before official season end: (a) system generates seasonal inventory position report by SKU by store cluster: current on-hand, weeks of supply at current sell-through rate, total WAC value at risk; (b) system compares current seasonal sell-through to plan per W32 step 10 mid-season review; (c) Category Manager classifies each seasonal SKU into disposition categories: (i) **On-track** — sell-through ≥ 80% of plan, projected to clear before season end with no intervention, (ii) **Behind plan** — sell-through 50–80% of plan, needs markdown acceleration, (iii) **Significantly behind** — sell-through < 50% of plan, needs aggressive intervention or early disposition, (iv) **Surprise hit** — sell-through > 120% of plan, may need supplemental replenishment from other stores or expedited PO; (d) Category Manager presents build-down strategy to VP Merchandising with recommended markdown schedule and projected total markdown/disposition cost | Category Manager | VP Merchandising | 1 day/season |
| 2 | **Markdown escalation schedule — first tier (T-8 to T-4 weeks)**: For "Behind plan" and "Significantly behind" SKUs: (a) Pricing Analyst applies first-tier markdown per W93 authorization workflow: typically 15–25% off seasonal SRP for "Behind plan" items, 25–35% for "Significantly behind"; (b) system pushes markdown prices to POS, ecommerce, and shelf label generation per W93 step 4; (c) Category Manager targets markdown depth to achieve a sell-through rate that will clear 70–80% of remaining seasonal stock by T-4 weeks; (d) for "Surprise hit" items: Supply Planner identifies stores with excess seasonal stock and initiates inter-store transfers per W204 to stores with higher demand; Buyer evaluates expedited PO from domestic vendor if lead time allows | Pricing Analyst / Supply Planner / Buyer | Category Manager | 3–4 hours/season |
| 3 | **Mid-build-down review (T-4 weeks)**: Category Manager and Pricing Analyst review markdown sell-through at T-4: (a) system generates build-down dashboard: markdown price, units sold since markdown, remaining on-hand, sell-through % since markdown, projected weeks to clear at current velocity; (b) Category Manager reclassifies remaining SKUs: (i) **Clearing** — on track to sell out at current markdown, no further action, (ii) **Stuck** — sell-through < 30% since first markdown, needs deeper markdown or alternative disposition; (c) for "Stuck" items: Pricing Analyst applies second-tier markdown per W93: additional 20–30% off (cumulative markdown typically 40–60% off original SRP); requires VP Merchandising approval if cumulative markdown > 50% or below-cost per W93 step 3; (d) Category Manager identifies items for early removal from seasonal display and relocation to clearance area to free prime retail space for incoming season | Category Manager / Pricing Analyst | VP Merchandising | 4 hours/season |
| 4 | **Aggressive clearance (T-2 weeks)**: Final push for remaining seasonal stock: (a) Pricing Analyst applies final markdown tier: cumulative 50–75% off original SRP for items still in stock; below-cost markdowns require CFO approval per W93 step 3; (b) system activates multi-channel clearance: (i) in-store clearance section or dump bin display for remaining units, (ii) ecommerce flash sale or bundle promotion per W13, (iii) Store Manager-initiated local clearance via social media (company-approved Facebook post with seasonal clearance pricing); (c) Category Manager activates disposition decision tree for items unlikely to clear at any markdown: (i) **RTV** — coordinate with Buyer for vendor return per W88 (seasonal vendors may accept return for restocking if item is not season-specific, e.g., power tools vs. Christmas lights), (ii) **Wholesaler bulk sale** — Inventory Control Manager contacts liquidation wholesalers per W220 step 3 for bulk purchase of remaining seasonal stock, (iii) **Inter-store consolidation** — consolidate remaining stock from 200 stores to 20–30 high-traffic clearance stores to maximize sell-through density per W204, (iv) **Donate** — coordinate with CSR for donation of functional seasonal items (e.g., school supplies after Back-to-School, umbrellas after rainy season) to community partners; requires Controller approval; (v) **Write-off** — items with no recovery path routed to W587 obsolescence write-off | Pricing Analyst / Category Manager / Buyer / Inventory Control Manager | VP Merchandising / CFO | 4–6 hours/season |
| 5 | **Final remaining stock disposition decision (T-1 week)**: Category Manager makes final disposition call for each remaining seasonal SKU: (a) system generates final remaining stock report: SKU, quantity, location, current markdown price, WAC value, remaining recovery potential; (b) for items with < 50 units chain-wide: Category Manager approves disposal route (clearance, donate, write-off) — decision is pragmatic, not strategic; (c) for items with > 50 units chain-wide: Category Manager and VP Merchandising jointly decide: (i) continue selling into next season (carry-forward items — perennial seasonal like garden tools, rain gear), (ii) deep discount to PHP 0 recovery threshold and clear through clearance stores, (iii) bulk RTV or write-off; (d) system updates each SKU's disposition status: "Seasonal — Cleared," "Seasonal — Carry Forward," "Seasonal — RTV," "Seasonal — Donated," or "Seasonal — Write-Off (W587)" | Category Manager | VP Merchandising | 3–4 hours/season |
| 6 | **Seasonal display teardown (T-1 week to T+0)**: At store level: (a) Department Supervisor receives teardown instruction from VM Coordinator per W264 step 5: list of outgoing seasonal SKUs, teardown schedule, and disposition for each item (clearance rack, carry-forward shelf position, staging for RTV/donation/disposal); (b) Stock Associates disassemble seasonal displays: endcaps, island displays, promotional fixtures, and seasonal signage per W583; (c) outgoing seasonal stock physically sorted by disposition: (i) clearance items → moved to designated clearance area or dump bins, (ii) carry-forward items → returned to regular shelf position in appropriate category aisle, (iii) RTV/consolidation items → packed and staged at receiving dock for store-to-DC return per W22B or inter-store transfer per W204, (iv) donation items → boxed with itemized list for CSR pickup coordination, (v) disposal items → moved to damaged goods area for disposal per W91/W82; (d) Department Supervisor confirms teardown completion in system with photo evidence of cleared display area | Department Supervisor / Stock Associate | Store Manager | 4–8 hours/store per transition |
| 7 | **New season inventory receipt and staging (T-2 weeks to T+0)**: Overlapping with outgoing season teardown: (a) DC ships incoming seasonal stock per W4 replenishment with seasonal allocation priority per W57; system schedules deliveries to arrive during the T-2 to T+0 window; (b) Store Receiving Clerk receives incoming seasonal stock; Stock Associate stages in backroom or designated seasonal staging area (NOT placed on sales floor until outgoing display teardown is complete to avoid commingling); (c) system tracks incoming seasonal stock receipt vs. allocation plan per W57 step 7; flags stores behind on incoming receipt | Receiving Clerk / Stock Associate | Store Manager | Per W4 receiving; 2–3 hours/store for staging |
| 8 | **New season planogram execution (T+0 to T+1 week)**: After teardown completion: (a) VM Coordinator distributes new season planogram and setup guide to all stores per W264 step 4; (b) Department Supervisor and Stock Associates build new seasonal displays per planogram: (i) high-impact endcap or island display for top 10 incoming seasonal items, (ii) category aisle seasonal section for secondary items, (iii) seasonal cross-merchandising displays (e.g., Christmas: lights + extension cords + outdoor decorations displayed together); (c) Stock Associates place shelf tags and promotional signage per W262; (d) Department Supervisor confirms setup completion in system with planogram compliance photo; (e) system updates shelf labels with new season SRP (not promotional pricing — regular seasonal price per W40); (f) new season merchandise goes live on seasonal calendar start date; system enables full ATP availability for incoming seasonal items across all channels | Department Supervisor / Stock Associate / VM Coordinator | Store Manager | 6–10 hours/store per transition |
| 9 | **Post-transition inventory reconciliation (T+2 weeks)**: Category Manager and Inventory Control Manager review post-transition state: (a) system generates seasonal build-down outcome report: (i) original seasonal inventory value at T-8 weeks, (ii) total sold at full margin, (iii) total sold at markdown (by markdown tier), (iv) total RTV'd, (v) total donated, (vi) total written off per W587, (vii) total carry-forward to next season, (viii) total markdown cost, (ix) total disposition cost; (b) Category Manager calculates seasonal inventory recovery rate: (revenue from sold items + RTV credits + scrap recovery) ÷ original seasonal inventory value; target: > 70% recovery; (c) Inventory Control Manager verifies all disposition actions are physically completed: items marked "cleared" have zero physical on-hand, items marked "RTV" have been shipped, items marked "write-off" have been physically disposed; (d) post-mortem feed into next year's seasonal buy plan per W32 step 11 | Category Manager / Inventory Control Manager | VP Merchandising | 1 day/season |
| 10 | **Cross-seasonal learning integration**: Category Manager documents build-down lessons learned for integration into next year's seasonal planning cycle: (a) markdown timing effectiveness — which markdown tier at which week drove highest sell-through, (b) store cluster performance — which regions cleared faster and why (climate, local events, store execution quality), (c) vendor RTV willingness by vendor — which seasonal vendors accepted returns vs. refused, (d) carry-forward vs. write-off decision quality — were carry-forward items actually sold in next season or did they become SLOB per W220, (e) updated seasonal demand curve per SKU for W31 forecast model recalibration; lessons learned stored in seasonal planning knowledge base linked to W32 | Category Manager | VP Merchandising | 4–6 hours/season |

**Total time per seasonal build-down cycle**: ~35–50 hours at HQ level (Category Manager 18–26 hours, Pricing Analyst 7–10 hours, Supply Planner 3–4 hours, Inventory Control Manager 5–6 hours, Buyer 2–4 hours) over the 8-week build-down period; ~10–18 hours per store (Department Supervisor + Stock Associates) concentrated in the T-1 to T+1 window.

### System Touchpoints (W588 — Seasonal Build-Down)

- Seasonal inventory position report with sell-through vs. plan, weeks of supply, and WAC value at risk by SKU by store cluster (W588.1)
- Seasonal SKU disposition classification engine: on-track, behind plan, significantly behind, surprise hit (W588.1)
- Markdown escalation scheduler with pre-configured tier timing (T-8, T-4, T-2, T-1 weeks) linked to W93 authorization workflow (W588.2–4)
- Multi-channel clearance activation: POS markdown, ecommerce flash sale, social media clearance (W588.4)
- Disposition decision tree with routing to W88 (RTV), W220 (wholesaler liquidation), W204 (inter-store consolidation), donation, or W587 (write-off) (W588.4–5)
- Final remaining stock disposition dashboard with recovery potential per SKU (W588.5)
- Store-level teardown instruction distribution with per-SKU disposition routing (W588.6)
- Incoming seasonal stock receipt tracking vs. allocation plan (W588.7)
- Planogram compliance photo capture and system confirmation (W588.8)
- Seasonal build-down outcome report: original value, sold (full + markdown tiers), RTV, donated, written off, carry-forward, markdown cost, disposition cost, recovery rate (W588.9)
- Cross-seasonal learning knowledge base linked to W32 seasonal buy planning (W588.10)
- Integration with W4 (replenishment — incoming seasonal stock delivery), W13 (promotions — flash sale and bundle promotions for clearance), W22 (transfers — inter-store consolidation of remaining seasonal stock), W31 (demand forecasting — seasonal demand curve recalibration), W32 (seasonal buy planning — feed-in to next year's plan and post-mortem), W40 (price changes — new season SRP setup), W57 (promotional stock allocation — incoming season pre-positioning), W88 (RTV — vendor return for seasonal items), W91 (damaged goods — disposal of unsaleable seasonal items), W93 (markdown — tiered markdown escalation), W146 (wholesale — bulk liquidation of seasonal excess), W204 (rebalancing — inter-store seasonal consolidation), W220 (SLOB — items not cleared become SLOB candidates), W262 (promotional setup — signage and shelf labels for new season), W264 (seasonal transition — overall transition framework), W554 (shelf replenishment — incoming seasonal stock shelving), W574 (store closing — end-of-day procedures during transition), W583 (promo transition — display reset coordination), W587 (obsolescence write-off — terminal disposition for unsalvageable seasonal items)

### Pain Points / Risks

- **Markdown timing vs. margin preservation tension**: starting markdowns too early (T-8) on items that might still sell at full price sacrifices margin; starting too late (T-2) risks being unable to clear stock before season end — the 8-week build-down window attempts to balance this, but Category Manager judgment remains critical and fallible, especially for weather-dependent seasons (rainy season demand is erratic and typhoon-driven).
- **Store execution variability across 200 locations**: teardown and new season setup require coordinated physical labor at all 200 stores simultaneously; stores with staff shortages (absenteeism, high turnover in provincial locations) lag behind, creating a patchwork where some stores are fully transitioned while others still display outgoing seasonal merchandise weeks into the new season, confusing customers and distorting sell-through data.
- **Incoming and outgoing season overlap risk**: the 2-week overlap window (T-2 to T+0) where both incoming seasonal stock arrives and outgoing seasonal stock is being cleared creates backroom congestion — stores with limited staging space must manage dual seasonal inventory physically separated, increasing the risk of commingling (incoming stock sold at old-season clearance prices or vice versa).
- **Disposition decision paralysis at T-1**: the Category Manager's final disposition call (step 5) is often delayed by reluctance to commit to write-offs or deep discounts; every week of delay at T-1 reduces the remaining selling window and increases the volume routed to W587 write-off, creating a self-reinforcing spiral of mounting losses.
- **Carry-forward items becoming SLOB**: items classified as "carry-forward" to next season often sit in backroom storage for 6–10 months occupying space needed for core replenishment; when the next season arrives, demand has shifted and these items end up as SLOB per W220, merely deferring rather than resolving the seasonal excess problem — the W588.10 cross-seasonal learning step tracks this but cannot prevent it.
- **Multi-seasonal overlap in Philippines climate**: unlike temperate markets with clean seasonal transitions, Philippine seasons overlap (rainy season transitions directly to Christmas "ber" months; Back-to-School coincides with summer end); the W32 seasonal calendar defines distinct build-down windows, but stores in Visayas and Mindanao with different climate patterns may not align neatly with the Luzon-centric calendar, requiring regional flexibility that complicates the chain-wide markdown schedule.
- **Donation logistics for seasonal items**: bulk donation of seasonal items (e.g., 5,000 umbrellas after rainy season, 2,000 school supply kits after Back-to-School) requires coordination with CSR partners who may lack capacity to receive and distribute large volumes on short notice; items awaiting donation pickup occupy valuable store receiving space.

### Staffing Implication

- **Category Managers**: ~18–26 hours per seasonal build-down cycle × 4 cycles/year = ~72–104 hours/year (~9–13 days/year). This is the single largest incremental workload from this workflow. With 6 Category Managers, each handles ~1.5–2.5 days/season. Absorbed within existing merchandising team but creates peak workload overlapping with W264 transition execution.
- **Pricing Analysts**: ~7–10 hours per seasonal build-down × 4 cycles = ~28–40 hours/year. Concentrated in the T-8, T-4, and T-2 markdown execution windows. Absorbed.
- **Supply Planners**: ~3–4 hours per cycle for "Surprise hit" replenishment and inter-store consolidation coordination. Absorbed.
- **Inventory Control Manager**: ~5–6 hours per cycle for disposition decision support and post-transition reconciliation. Absorbed (combined with W220 + W587 workload, total ~35–50 hours/quarter).
- **Buyers**: ~2–4 hours per cycle for vendor RTV coordination on seasonal items. Absorbed.
- **Store-level labor**: ~10–18 hours/store per transition cycle (teardown 4–8 hours + staging 2–3 hours + new season setup 6–10 hours) × 4 cycles/year = ~40–72 hours/store/year. With 4 Department Supervisors and 4 Stock Associates per store, this is ~5–9 hours per person per transition, concentrated in the T-1 to T+1 week. This competes with W554 daily shelf replenishment and W574 closing procedures during the transition window — stores should plan dedicated transition shifts to avoid degradation of daily operations.
- **Visual Merchandising Coordinators**: ~2 days per cycle for setup guide distribution and compliance photo review × 4 cycles = ~8 days/year. Absorbed.
- **No incremental headcount**, but the seasonal build-down window (T-1 to T+1) represents the highest-intensity store labor period of the year outside of peak holiday trading; Store Managers should schedule transition shifts and minimize time-off approvals during this window.
