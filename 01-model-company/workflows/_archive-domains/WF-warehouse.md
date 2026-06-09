# Warehouse & Logistics Workflows

> Receiving, putaway, kit assembly, fleet management, inter-island logistics, DC outbound dispatch & load planning, fleet spare parts & preventive maintenance, cross-docking operations, DC container yard & chassis management, DC daily operations & shift management, DC dock scheduling & appointment management, DC daily KPI dashboard & performance tracking, DC cycle counting & inventory accuracy program, DC safety operations & compliance, warehouse equipment preventive maintenance, reverse logistics processing (customer/store returns at DC), and seasonal warehouse surge planning & execution.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W3. Warehouse Receiving & Putaway](#w3-warehouse-receiving-putaway)
- [W46. Kit / Bundle Assembly & Disassembly](#w46-kit-bundle-assembly-disassembly)
- [W52. Fleet Management](#w52-fleet-management)
- [W66. Inter-Island Logistics & Freight Management](#w66-inter-island-logistics-freight-management)
- [W106. DC Outbound Dispatch & Load Planning](#w106-dc-outbound-dispatch-load-planning)
- [W188. Fleet Spare Parts & Preventive Maintenance (PM) Management](#w188-fleet-spare-parts-preventive-maintenance-pm-management)
- [W221. Cross-Docking Operations for Fast-Moving Bulky Items](#w221-cross-docking-operations-for-fast-moving-bulky-items)
- [W222. DC Container Yard & Chassis Management](#w222-dc-container-yard-chassis-management)
- [W270. Pallet & Returnable Transport Packaging (RTP) Tracking](#w270-pallet-returnable-transport-packaging-rtp-tracking)
- [W584. DC Daily Operations & Shift Management](#w584-dc-daily-operations--shift-management)
- [W585. DC Dock Scheduling & Appointment Management](#w585-dc-dock-scheduling--appointment-management)
- [W586. DC Daily KPI Dashboard & Performance Tracking](#w586-dc-daily-kpi-dashboard--performance-tracking)
- [W648. DC Cycle Counting & Inventory Accuracy Program](#w648-dc-cycle-counting--inventory-accuracy-program)
- [W649. DC Safety Operations & Compliance](#w649-dc-safety-operations--compliance)
- [W650. Warehouse Equipment Preventive Maintenance](#w650-warehouse-equipment-preventive-maintenance)
- [W651. Reverse Logistics Processing (Customer/Store Returns at DC)](#w651-reverse-logistics-processing-customerstore-returns-at-dc)
- [W652. Seasonal Warehouse Surge Planning & Execution](#w652-seasonal-warehouse-surge-planning--execution)

---

## W3. Warehouse Receiving & Putaway

| Field | Detail |
|---|---|
| **Trigger** | Vendor delivery truck arrives at DC (or container from port) |
| **Frequency** | ~6,000 goods receipts/month across all DCs; ~1,200/DC/month; ~40/day per DC |
| **Volume** | ~15 lines per receipt on average |
| **Owner** | DC Receiving Supervisor |
| **Participants** | Receiving Clerk, Quality Checker, Putaway Staff, DC Supervisor, Buyer (if discrepancy) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Truck arrives at DC gate; guard checks delivery schedule vs. appointment log | Guard | DC Supervisor | 5 min |
| 2 | Receiving Clerk pulls up expected PO or Transfer Order in system | Receiving Clerk | DC Supervisor | 2 min |
| 3 | Unload truck; stage in receiving area | Unloading Crew (3–4) | Receiving Clerk | 30–60 min |
| 4 | Scan/verify each item against PO: SKU, quantity, lot/batch (if applicable) | Receiving Clerk | DC Supervisor | 20–40 min |
| 5 | Quality check on sampled items (damage, correctness, expiry if applicable) per category-specific inspection checklist (see Quality Inspection Standards below) | Quality Checker | DC Supervisor | 10–20 min |
| 6 | If discrepancy (shortage, damage, wrong item): flag in system; notify Buyer | Receiving Clerk | DC Supervisor | 5 min |
| 6a | If damaged goods: Receiving Clerk creates damage report with photos; initiates one of: (a) Return to Vendor (RTV) via Buyer, (b) scrap with DC Supervisor authorization, or (c) insurance claim for insured shipments. For insurance claims: Receiving Clerk documents damage with photos and notes on delivery receipt; Import Coordinator or DC Supervisor files claim with insurance provider within required notification window (typically 3–5 business days); system tracks claim status; upon settlement, Finance posts insurance recovery to income and reduces inventory loss | Receiving Clerk | DC Supervisor | 10 min |
| 6b | Buyer reviews RTV request; coordinates with vendor for credit note or replacement shipment | Buyer | Category Manager | 15 min/occurrence |
| 6c | If scrap authorized: DC Supervisor approves scrap disposition; system removes inventory and posts loss to damage/scrapping account | DC Supervisor | DC Manager | 5 min |
| 7 | Confirm Goods Receipt in system; inventory increases in real-time | Receiving Clerk | DC Supervisor | 5 min |
| 8 | System suggests putaway location based on zone, bin capacity, item velocity | System | — | Automated |
| 9 | Putaway staff moves goods to assigned bin; scan-confirm in system | Putaway Staff | DC Supervisor | 15–30 min |
| 10 | Update PO/TO status; trigger vendor invoice matching (AP) | System | — | Automated |

**Total time per receipt**: ~1.5–3 hours from gate to bin

### Quality Inspection Standards (W3 Step 5 Detail)

Quality inspection at receiving uses configurable, category-specific checklists. The system presents the Quality Checker with the appropriate checklist per SKU category on the RF device. AQL (Acceptable Quality Level) sampling is applied per ANSI Z1.4 single sampling plan, normal inspection level II, with configurable AQL per category.

| Category | Inspection Criteria | Sampling Plan | AQL | Reject Action |
|---|---|---|---|---|
| **Tiles & ceramics** | Visual defects (chips, cracks, glaze inconsistencies on sampled pieces); color consistency vs. reference sample; dimensional check (±1mm tolerance on length/width); PEI rating confirmation per packaging | Per lot: ≤ 100 pcs → inspect 5; 101–500 → inspect 20; 501+ → inspect 32 | 2.5% | Reject entire lot if defect rate exceeds AQL; Buyer notifies vendor |
| **Lumber & wood** | Moisture content spot-check (if meter available); warping/bowing check (visual); species/treatment verification; grade stamp verification; length/piece count | Per bundle: inspect 5 pieces from each bundle | 4.0% (visual) | Reject non-conforming pieces; accept remainder; Buyer adjusts PO quantity |
| **Paint & chemicals** | Manufacturing date and shelf-life capture (mandatory per shelf-life management); container integrity (dents, leaks, tamper seal); color match for tinted items; safety data sheet availability check | Per delivery: inspect 10% of cartons, minimum 2 | 1.5% (critical: leaks/tamper) | Reject entire lot if critical defect found; quarantine for Buyer review |
| **Cement & masonry** | Bag integrity (no tears, moisture damage, hardened lumps); manufacturing date check (cement shelf-life typically 3 months); weight spot-check on sampled bags | Per pallet: inspect 5 bags from top, middle, bottom | 2.5% | Reject damaged bags; accept sound bags; Buyer adjusts PO quantity |
| **Plumbing & electrical** | Visual defect check (finish, threads, connectors); brand/model verification against PO; quantity count; packaging integrity | Per line item: inspect 10% of units, minimum 2 | 2.5% | Reject non-conforming units; Buyer coordinates with vendor |
| **Power tools & appliances** | External packaging check; serial number capture for high-value items (> PHP 10,000); physical damage check; accessory completeness vs. product spec | Per unit: 100% inspection for high-value; 10% for standard | 1.0% (high-value); 2.5% (standard) | Reject damaged units; serial-tracked items logged for warranty (W33) |
| **Hardware & fasteners** | Quantity count (weigh-count or piece count); rust/corrosion check; grade/size verification against PO | Per line: weigh-count verification | 4.0% | Reject if count variance > 5%; Buyer adjusts PO |

**Quality hold process**: if inspection fails, system places goods in "Quality Hold" status — inventory is physically segregated in QC hold area and not available for putaway, allocation, or sale; Quality Checker creates quality hold record with defect description, photos, and inspection checklist result; Buyer notified for vendor resolution (replace, credit, or scrap); if not resolved within 5 business days, DC Supervisor escalates to Category Manager.

**Monthly**: DC Supervisor generates quality metrics report per vendor: inspection pass rate, top defect categories, quality hold aging; feeds into vendor scorecard (W44 quality reject rate metric).

### Cross-Dock Flow (Fast-Movers — ~30% of receipts)

For high-velocity items (A-class), steps 8–9 are skipped. Instead:
- After step 7, goods are moved directly to outbound staging area
- Allocated to pending store replenishment orders
- Loaded onto outbound trucks same day

### System Touchpoints (W3 — Warehouse Receiving & Putaway)
- Gate check against delivery schedule / appointment log (W3.1)
- PO / Transfer Order pull-up for receiving validation (W3.2)
- Barcode/RF scanning against PO: SKU, quantity, lot/batch verification (W3.4)
- Quality inspection checklists per category on RF device with AQL sampling (W3.5)
- Discrepancy flagging and Buyer notification (W3.6)
- Damage disposition workflow: RTV initiation, scrap authorization, insurance claim capture (W3.6a–c)
- Goods Receipt posting with real-time inventory increase; perpetual WAC recalculation at each receipt: new WAC = (prior inventory value + receipt value) ÷ (prior quantity + receipt quantity) (W3.7)
- Putaway direction: zone, bin, velocity-based location suggestion (W3.8)
- Cross-dock allocation to outbound orders for fast-movers (W3 cross-dock variant, bypassing putaway)
- DC forward-pick zone replenishment: system monitors forward-pick quantities; when below minimum, generates replenishment task from reserve/bulk to forward-pick; prioritized ahead of picking waves (W3.8 post-putaway, integrated with W4 picking)
- Shelf-life / expiry date management: manufacturing date and shelf-life capture at GR for date-sensitive items; expiry date calculated per batch/lot; items below configurable remaining-shelf-life threshold flagged for priority picking or markdown; expired items blocked from dispatch (W3.4)
- Inventory ownership: all merchandise received into DCs is owned by BuildRight Depot Inc. even though DC facilities are operated by BuildRight Logistics Inc.; Logistics Inc. provides warehousing and distribution services billed monthly per W14; goods are Depot Inc. inventory throughout the DC-to-Store flow
- RTV physical logistics and tracking: Receiving Clerk stages RTV items in designated RTV holding area; system creates RTV shipment record with lifecycle tracking (Initiated → Packed → Shipped → In Transit → Vendor Received → Credit Note Issued → Settled); DC dispatch arranges carrier or vendor pickup per Buyer coordination; system tracks RTV aging by status; for store-initiated RTVs (W6.8a, W12A.8, W33.6), system creates RTV shipment record and Buyer coordinates pickup or shipment to DC for consolidation
- RTV vendor credit note SLA: system enforces configurable SLA per vendor (default 15 business days from vendor receipt to credit note); auto-escalation to Buyer if overdue; unresolved after 30 days escalated to Category Manager for W44 vendor scorecard impact; credit note SLA compliance tracked in W44; monthly AP Clerk generates RTV credit note aging report feeding into W7D reconciliation
- RTV freight cost allocation: freight cost borne by party responsible for return reason — vendor fault (vendor bears cost, deducted from credit note), buyer-initiated (BuildRight bears cost, posted to write-down), carrier damage (claimed from carrier insurance per W3.6a); system captures RTV freight cost as separate line on RTV shipment record
- DC RTV consolidation & vendor return shipment batching: DC Receiving Clerks accumulate RTV items in designated holding area organized by vendor; system maintains DC-level RTV consolidation dashboard with accumulated items, total value, and aging per vendor; weekly, Buyer reviews dashboard and schedules batch shipment per vendor — high-volume vendors when accumulated value exceeds configurable threshold (e.g., PHP 20,000), low-volume vendors held until cost-justified or consolidated with next regular vendor delivery backhaul; system generates RTV shipment manifest per vendor for advance confirmation
- Integration with W2A (auto-replenishment POs), W2B (import container receiving), W4 (outbound picking), W18 (DSD receiving), W22 (transfer order receiving), W44 (vendor scorecard — inspection pass rate, quality reject rate), W52 (carrier performance), W82 (hazardous waste disposal), W88 (RTV workflow)

### Pain Points / Risks
- Quality inspection bottleneck at receiving dock: with ~40 receipts/day per DC and category-specific AQL sampling requiring 10–20 min per receipt, the 1–2 Quality Checkers per DC are a throughput constraint during peak morning receiving hours (8–10 AM).
- Cross-dock flow dependency on pre-existing outbound orders — if the matching replenishment orders (W4) are delayed or cancelled after goods are already diverted to outbound staging, cross-docked inventory has no putaway location assigned and must be manually rerouted.
- Catch-weight measurement at yard receiving (W3B.3) for lumber and rebar is time-consuming and prone to measurement inconsistency between receiving associates; measurement disputes with vendors on quantity discrepancies delay GR posting.
- Shelf-life capture compliance varies across receiving clerks — missed manufacturing date entry for paint, adhesives, and cement means the expiry management engine lacks data, resulting in expired stock being dispatched to stores undetected.
- PO discrepancies (shortage, wrong item, damage) requiring Buyer involvement (W3.6b) create a receiving dock wait-time dependency — the truck and unloading crew are idle while the Buyer coordinates with the vendor, consuming dock door capacity.

### Time Estimate
Total per receipt: ~1.5–3 hours from gate to bin (5 min gate check + 2 min PO pull-up + 30–60 min unloading + 20–40 min scanning + 10–20 min quality check + 5–15 min discrepancy handling if any + 5 min GR posting + 15–30 min putaway). Cross-dock receipts bypass putaway (steps 8–9), reducing to ~1.5–2 hours. Total daily per DC: ~40 receipts requiring ~60–120 labor-hours across shifts.

### Staffing Implication
- **Per DC (Receiving)**: 3–4 Receiving Clerks handling ~40 receipts/day in shifts (~1.5–3 hours per receipt); each clerk processes ~10–12 receipts/day. Absorbed within ~150 DC headcount.
- **Per DC (Quality Check)**: 1–2 Quality Checkers performing category-specific AQL inspections at ~10–20 min per receipt; during peak morning receiving hours (8–10 AM), 2 Quality Checkers are necessary to prevent dock congestion.
- **Per DC (Putaway)**: 4–6 Putaway Staff moving goods from receiving dock to assigned bins at ~15–30 min per receipt; cross-dock receipts (~30% of volume) bypass putaway, reducing average putaway load.
- **Per DC (Unloading Crew)**: 3–4 Unloading Crew members per shift handling physical unloading of vendor trucks and import containers at ~30–60 min per receipt.
- **DC Receiving Supervisor**: 1 per DC overseeing all inbound operations including scheduling (W3C), receiving quality, and discrepancy resolution. Absorbed within existing DC management structure.
- **Total per DC**: ~10–13 staff dedicated to receiving/putaway out of ~150 DC headcount. Reasonable.
- **No incremental headcount beyond planned DC staffing.**

### W3B. Yard & Outdoor Inventory Management

For lumber, building materials, and other bulky items stored in outdoor yard areas (present at all DCs and stores per the Lumber & Building Materials Yard zone):

| Field | Detail |
|---|---|
| **Trigger** | Vendor delivery of lumber, cement, steel/rebar, or other bulky items requiring outdoor yard storage |
| **Frequency** | Daily; ~10–20 yard receipts per DC/day |
| **Volume** | ~30–40% of total DC inventory by volume stored in yard zones across 4 DCs and 200 store yards |
| **Owner** | DC Yard Supervisor (DC); Department Supervisor (Store) |
| **Participants** | Receiving Clerk, Yard Staff, Stock Associate, DC Supervisor / Dept. Supervisor |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Goods received at yard gate (separate from indoor receiving); Receiving Clerk verifies against PO/TO using handheld | Receiving Clerk | DC Supervisor / Dept. Supervisor | 20–40 min |
| 2 | System records receipt into yard zone (zone-level tracking, not individual bin); inventory tracked by yard zone (e.g., Yard-A: Lumber, Yard-B: Cement/Blocks, Yard-C: Steel/Rebar) | System | — | Automated |
| 3 | For catch-weight items (lumber, rebar): associate measures and records actual length/piece count at receipt; system calculates quantity in board feet / linear meters / pieces | Receiving Clerk | Dept. Supervisor | 10–20 min |
| 4 | Goods staged in designated yard zone; organized by SKU type and length/size for easy retrieval | Yard Staff | DC Supervisor | 15–30 min |
| 5 | Physical counting: yard items counted by zone during cycle counts (W6) and annual physical inventory (W42); counted by piece/bundle rather than individual bin scan | Stock Associate | Dept. Supervisor | Per W6/W42 |
| 6 | Weather damage discovered during daily yard walkthrough: Stock Associate reports damage (warped lumber, water-damaged cement, rusted rebar); DC Supervisor/Dept. Supervisor approves disposition (markdown, scrap, RTV, insurance claim) per W3.6a process | Stock Associate | DC Supervisor / Dept. Supervisor | 10 min |
| 7 | Yard-to-sales-floor movement: when yard stock is needed indoors (e.g., small lumber pieces moved to indoor display), Stock Associate transfers items in system from yard zone to indoor location | Stock Associate | Dept. Supervisor | 10 min |

### System Touchpoints (Yard)
- Zone-level location master for yard areas (not bin-level) (W3B.2)
- Catch-weight/variable-length receipt and tracking in yard zones (W3B.3)
- Weather damage reporting and disposition (W3B.6)
- Yard-to-indoor inventory transfer (W3B.7)
- Yard inventory visible in real-time alongside indoor inventory (W3B.2)

### Time Estimate
~1.5–3 hours per yard receipt (gate-in through staging); weather damage response adds ~10 min per incident; yard-to-indoor transfers ~10 min each.

### Pain Points / Risks
- Zone-level (not bin-level) tracking reduces pick accuracy for fast-moving yard SKUs, leading to longer retrieval times and potential miscounts.
- Catch-weight items (lumber, rebar) are prone to measurement disputes between receiving and dispatch, requiring manual re-verification.
- Weather exposure causes accelerated deterioration (warped lumber, water-damaged cement bags, rusted rebar), resulting in higher shrinkage than indoor storage.
- Safety risk during yard operations — heavy loads, forklift traffic in open areas, and inadequate lighting at night increase incident probability.

### Staffing Implication (Yard)
- **Per DC**: 2–3 Yard Staff dedicated to outdoor yard receiving, staging, and inventory management; additional support from Stock Associates during peak receiving periods. Absorbed within ~150 DC headcount.
- **Per Store**: yard management is a collateral duty of Department Supervisor and Stock Associates; ~10–20 min/day for yard walkthrough and weather damage checks. Absorbed.
- **DC Yard Supervisor**: role exists at each DC; oversees yard operations in addition to indoor receiving. Absorbed within existing DC management structure.

### W3C. DC Inbound Delivery Scheduling

| Field | Detail |
|---|---|
| **Trigger** | Purchase order confirmed with vendor or import shipment ETA confirmed |
| **Frequency** | Daily; ~40 receipts/day per DC |
| **Volume** | ~1,200 merchandise receipts/month + ~80–240 blanket releases + ~20–30 import containers + ~30–50 non-merchandise receipts per DC per month |
| **Owner** | DC Receiving Supervisor |
| **Participants** | Buyer, Import Coordinator, DC Receiving Supervisor, DC Dispatch, Vendor/Carrier |

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates inbound delivery forecast from open POs: PO number, vendor, expected delivery date (from PO promised date or import ETA), number of lines, estimated pallet/cube count, and dock door requirements (refrigerated none; hazardous materials for paint/chemicals; standard for general merchandise) | System | — | Automated (nightly) |
| 2 | DC Receiving Supervisor reviews next 3-day inbound forecast each morning; identifies days with high receiving volume (> 50 receipts) or overlapping large deliveries; adjusts dock door assignments and staff scheduling | DC Receiving Supervisor | DC Manager | 15 min/day |
| 3 | For domestic vendor deliveries: Buyer or system transmits delivery appointment to vendor with requested delivery date and time window (typically 8:00 AM – 4:00 PM, 2-hour windows); vendor confirms or proposes alternative; system logs appointment confirmation | Buyer / System | DC Receiving Supervisor | 5 min/PO |
| 4 | For import containers: Import Coordinator books delivery appointment with DC once container is released from port; provides container number, commodity, estimated weight, and special handling requirements; DC Receiving Supervisor confirms appointment and assigns dock door | Import Coordinator | DC Receiving Supervisor | 10 min/container |
| 5 | If vendor arrives without appointment: guard checks against open PO list; if valid PO exists, Receiving Supervisor accepts on a space-available basis (may result in extended wait time); if no valid PO, guard turns delivery away with Buyer notification | Guard / DC Receiving Supervisor | DC Manager | 5 min |
| 6 | System maintains dock door utilization dashboard per DC: shows scheduled appointments, completed receipts, and available capacity by time slot; Receiving Supervisor uses dashboard to optimize dock assignments and avoid congestion | System | — | Automated |
| 7 | Monthly: DC Receiving Supervisor reviews appointment compliance report — vendor on-time arrival %, no-show rate, unscheduled delivery rate; feeds into vendor scorecard (W44) and carrier performance review (W52) | DC Receiving Supervisor | DC Manager | 30 min/month |

### System Touchpoints (DC Scheduling)
- Inbound delivery forecast from open PO data with dock door requirements (W3C.1)
- Delivery appointment booking with vendor confirmation tracking (W3C.3–4)
- Dock door utilization dashboard with real-time capacity visibility (W3C.6)
- Appointment compliance reporting feeding vendor scorecard (W3C.7)
- Unscheduled delivery handling with PO validation at gate (W3C.5)
- Integration with W3 (DC receiving — appointments feed step 1 guard check), W2A (auto-replenishment POs generate appointments), W2B (import container appointments), W18B (DSD scheduling — store equivalent), W44 (vendor scorecard — appointment compliance), W52 (carrier performance)

### Pain Points / Risks (W3C — DC Inbound Delivery Scheduling)
- Unscheduled vendor arrivals (step 5) consume dock door capacity and receiving staff time that was allocated to scheduled appointments; during peak morning hours, even 2–3 unscheduled deliveries can cascade delays across the entire receiving schedule for the day.
- Import container appointment booking (step 4) depends on port release timing, which is unpredictable and subject to Customs inspection holds; last-minute container releases create scheduling chaos when dock doors are already fully booked for domestic vendor appointments.
- Vendor appointment no-show rate of 10–15% (based on Philippine vendor logistics patterns) wastes reserved dock door capacity; with ~40 appointments/day per DC, 4–6 no-shows represent significant lost receiving capacity that cannot be reallocated in real-time.
- Appointment compliance data feeding vendor scorecard (W44) lacks teeth — underperforming vendors face no financial penalty for late or missed appointments, reducing the incentive to comply with delivery windows.
- Monthly appointment compliance review (step 7) is backward-looking; there is no real-time rescheduling mechanism when a morning appointment is cancelled, leaving the dock door idle for the remainder of the time slot.

### Time Estimate (W3C — DC Inbound Delivery Scheduling)
Daily scheduling review (step 2): 15 min/day. Appointment booking per PO (step 3): 5 min/PO. Import container booking (step 4): 10 min/container. Dock door utilization dashboard monitoring: continuous (embedded in receiving operations). Monthly compliance review (step 7): 30 min/month. Total: ~2–3 hours/month for DC Receiving Supervisor scheduling duties.

### Staffing Implication
- Per DC: 3–4 Receiving Clerks (handling ~40 receipts/day in shifts, ~1.5–3 hrs each)
- Per DC: 4–6 Putaway Staff (handling putaway flow across zones)
- Per DC: 1–2 Quality Checkers
- Per DC: 1 Receiving Supervisor overseeing all inbound
- Total per DC: ~10–13 dedicated to receiving/putaway out of ~150 headcount. Reasonable.

---

## W46. Kit / Bundle Assembly & Disassembly

| Field | Detail |
|---|---|
| **Trigger** | Kit demand (auto-assembly) or planned batch assembly schedule |
| **Frequency** | ~200–400 kit assemblies/month across DCs; primarily tool sets, bathroom combo kits, paint starter kits |
| **Volume** | ~50–100 active kit SKUs |
| **Owner** | DC Supervisor |
| **Participants** | Merchandise Planner (BOM setup), DC Assembly Staff, DC Supervisor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Merchandise Planner defines kit Bill of Materials (BOM) in item master: kit SKU + component SKUs with quantities per unit; kit item type = 'Kit / Bundle' | Merchandise Planner | Category Manager | 15 min/kit |
| 2 | Assembly triggered by: (a) demand-driven — system auto-generates assembly order when kit is ordered (ecommerce) or picked (store replenishment) but insufficient kit stock exists, or (b) planned batch — DC Supervisor schedules weekly assembly of popular kits based on forecast | System / DC Supervisor | DC Supervisor | 5 min |
| 3 | System creates assembly order: lists required component quantities; checks component availability at DC; reserves components against assembly order | System | — | Automated |
| 4 | If component shortage: DC Supervisor alerts Buyer for expedited replenishment or suggests substitution (with Merchandise Planner approval) | DC Supervisor | Supply Planning Manager | 10 min |
| 5 | Assembly Staff picks components from DC bins per assembly order; scan-confirms each component | Assembly Staff | DC Supervisor | 10–30 min/kit |
| 6 | Assembly Staff assembles kit (physical packaging, labeling, shrink-wrap); applies kit barcode label | Assembly Staff | DC Supervisor | 5–15 min/kit |
| 7 | System consumes component inventory (decreases) and creates kit inventory (increases); kit cost = sum of component WAC at time of assembly | System | — | Automated |
| 8 | Kit received into finished goods storage location in DC; available for picking and shipping | Assembly Staff | DC Supervisor | 5 min |
| 9 | Kit disassembly (if components needed individually): DC Supervisor initiates disassembly order; system reverses process — consumes kit inventory, restores component inventory at original component WAC; disassembly labor posted to overhead | DC Supervisor | DC Manager | 10 min |

### System Touchpoints
- Kit BOM definition in item master with component quantities (W46.1)
- Assembly order auto-generation triggered by demand or planned schedule (W46.2–3)
- Component availability check and reservation against assembly order (W46.3)
- Component consumption and kit creation with automatic costing (W46.5–7)
- Kit disassembly with component restoration (W46.9)
- Kit inventory tracked separately from components; kit excluded from ROP/replenishment (assembled on demand)

### Pain Points / Risks
- Component availability for kit assembly is volatile — when a single component in a multi-SKU kit is out of stock, the entire assembly order is blocked; this is especially problematic for promotional kits (W57) where all components must be available simultaneously for pre-positioning.
- Kit disassembly (step 9) to reclaim components for individual sale is a manual exception process with no standard frequency trigger — DC Supervisors often defer disassembly decisions until the kit is already aged, recovering less component value than if disassembled earlier.
- Kit cost calculation (sum of component WAC at assembly time) creates margin distortion when component costs fluctuate — a kit assembled during a price spike records higher cost than one assembled during normal pricing, even if sold at the same retail price.
- Assembly labor scheduling conflicts with outbound picking waves (W4) — DC Assembly Staff are typically drawn from the general DC labor pool, and picking demand always takes priority over kit assembly, causing assembly backlogs.
- Kit BOM maintenance burden: with ~50–100 active kit SKUs, Merchandise Planners must update BOMs whenever component SKUs change (vendor substitution, discontinuation), but BOM updates are often delayed, leading to assembly orders with obsolete component references.

### Time Estimate
Kit BOM setup (step 1): 15 min/kit. Assembly order creation (steps 2–3): automated. Component picking (step 5): 10–30 min/kit. Assembly and labeling (step 6): 5–15 min/kit. System posting (step 7): automated. Kit putaway (step 8): 5 min/kit. Disassembly (step 9): 10 min/kit. Total: ~30–60 min per kit from assembly order to finished goods putaway. Monthly DC time: ~15–25 hours/DC for ~40–80 assemblies.

### Staffing Implication
- **DC Assembly Staff**: ~200–400 assemblies/month × 20 min average = ~70–130 hours/month. With 4 DCs, that's ~15–25 hours/DC/month. Absorbed by existing DC staff (within ~150/DC) as a scheduled weekly activity.
- **Merchandise Planner**: ~50–100 active kits × initial setup + occasional BOM updates = ~4–6 hours/month. Absorbed.

---

## W52. Fleet Management

| Field | Detail |
|---|---|
| **Trigger** | Vehicle registration renewal, scheduled maintenance, fuel purchase, driver assignment, route planning review |
| **Frequency** | Continuous; daily operations + periodic scheduled maintenance |
| **Volume** | ~30–40 owned vehicles (20% of total fleet); remainder 80% third-party (Lalamove, Transportify, contracted carriers) |
| **Owner** | Fleet Manager (within Supply Chain team) |
| **Participants** | Fleet Manager, Drivers, DC Dispatch, Finance, External carriers |

### Background

BuildRight's distribution fleet operates with a mixed model: ~20% owned vehicles (primarily 10-wheeler wing vans and 6-wheeler trucks for regular DC-to-store routes) and ~80% third-party carriers (for seasonal surge, inter-island routes, last-mile ecommerce delivery via Lalamove/Transportify). Owned vehicles are registered under BuildRight Logistics Inc. Third-party carrier management for ecommerce is covered in W19 (3PL management) and for general distribution in W4 (outbound logistics).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Driver assignment**: Fleet Manager assigns drivers to owned vehicles based on route schedule, driver qualifications (LTO license type — professional driver's license with restriction codes for heavy vehicles), and duty hour limits | Fleet Manager | Supply Chain Manager | 30 min/week |
| 2 | **Daily pre-trip inspection**: Driver conducts vehicle inspection checklist (tires, brakes, lights, fluid levels, cargo area, safety equipment) before departure; records in system via mobile app; vehicle not cleared for dispatch if critical items fail | Driver | Fleet Manager | 15 min/vehicle/day |
| 3 | **Fuel management**: Driver refuels at designated fuel stations using company fuel card; system captures fuel volume, odometer reading, and cost per transaction; Fleet Manager reviews fuel consumption per vehicle monthly (km/L benchmark per vehicle type; flags vehicles > 15% below benchmark for maintenance investigation) | Driver / Fleet Manager | Fleet Manager | 5 min/refuel + 1 hour/month review |
| 4 | **Scheduled maintenance**: Fleet Manager maintains maintenance calendar per vehicle based on manufacturer intervals (typically every 5,000–10,000 km or 3–6 months): (a) oil change and basic service, (b) tire rotation and replacement, (c) brake inspection, (d) annual comprehensive service; system alerts Fleet Manager 1 week before service due | Fleet Manager | DC Manager | Per schedule |
| 5 | **Unscheduled repair**: Driver reports vehicle issue; Fleet Manager assesses severity: (a) minor — schedule repair at next available slot, substitute 3PL for pending deliveries, (b) major — vehicle taken out of service, substitute vehicle or 3PL arranged | Fleet Manager | DC Manager | 30 min/occurrence |
| 6 | Maintenance or repair executed at company-approved workshop per region; Fleet Manager approves work order and cost; system tracks maintenance history per vehicle | Fleet Manager | DC Manager | Varies |
| 7 | **Vehicle registration & insurance**: Fleet Manager maintains calendar for LTO registration renewal (annual per vehicle), CTPL insurance renewal, and comprehensive insurance; system alerts 60 days before expiry; vehicles with expired registration blocked from dispatch | Fleet Manager | DC Manager | 30 min/vehicle/year |
| 8 | **Route performance review**: monthly, Fleet Manager reviews route metrics per vehicle: km driven, fuel efficiency, delivery punctuality (on-time % per W4 SLA), maintenance cost per km; identifies vehicles with declining performance for maintenance escalation or replacement planning | Fleet Manager | Supply Chain Manager | 2 hours/month |
| 9 | **3PL carrier performance**: Fleet Manager monitors third-party carrier performance per W19 (on-time delivery, damage rate, cost per delivery) in coordination with DC Dispatch; quarterly carrier review per W44 vendor scorecard methodology | Fleet Manager / DC Dispatch | Supply Chain Manager | Per W19/W44 |
| 10 | **Vehicle replacement planning**: annually, Fleet Manager evaluates vehicles > 5 years or > 300,000 km for replacement; submits capex request per W21; considers total cost of ownership (maintenance cost trajectory, fuel efficiency decline, reliability) vs. new vehicle cost plus financing | Fleet Manager | Supply Chain Manager | Annual (4 hours) |

### System Touchpoints
- Vehicle master record: plate number, VIN, model, year, capacity, assigned DC, registration expiry, insurance expiry, assigned driver (W52.1)
- Pre-trip inspection checklist on mobile app with defect reporting and dispatch block for critical failures (W52.2)
- Fuel card integration: automated fuel transaction capture with per-vehicle km/L tracking and anomaly alerting (W52.3)
- Maintenance scheduling with automated alerts per vehicle based on km or calendar interval (W52.4)
- Maintenance history tracking with cost per vehicle and cost per km (W52.6, 8)
- Registration and insurance calendar with expiry alerting and dispatch blocking (W52.7)
- Route and delivery performance tracking per vehicle (W52.8)
- Integration with W4 (route scheduling), W19 (3PL management), W21 (vehicle replacement capex), W39 (vehicle disposal), W30 (fuel expense GL posting)

### Pain Points / Risks
- Mixed fleet model (20% owned, 80% third-party) creates accountability gaps — 3PL carrier performance issues (late delivery, damage) are harder to enforce than with owned vehicles, and 3PL cost escalation during peak construction season (Q4) can be 30–50% above contracted rates.
- Pre-trip inspection compliance (step 2) is inconsistent across regions — Davao and Cebu drivers are less consistent than Manila/Laguna drivers in completing the mobile app checklist, leading to unreported vehicle defects that surface as roadside breakdowns.
- Fuel card fraud risk: drivers may fuel personal vehicles or collude with fuel station attendants to inflate fuel volume; the km/L benchmark review (step 3) catches anomalies only in monthly review, creating a 30-day detection lag.
- Vehicle registration and insurance expiry blocking (step 7) can remove vehicles from service with short notice if the Fleet Manager misses the 60-day alert — during peak periods, losing even one owned vehicle to an expired registration shifts significant volume to more expensive 3PL alternatives.
- Route performance review (step 8) data quality depends on GPS/telematics coverage; owned vehicles have full GPS but 3PL carriers provide only delivery confirmation (no real-time tracking), creating blind spots in the 80% of fleet operations that are third-party.

### Time Estimate
Driver assignment (step 1): 30 min/week. Daily pre-trip inspections (step 2): 15 min/vehicle/day. Fuel management (step 3): 5 min/refuel + 1 hour/month review. Scheduled maintenance coordination (step 4): varies by event. Unscheduled repair (step 5): 30 min/occurrence. Registration/insurance (step 7): 30 min/vehicle/year. Route performance review (step 8): 2 hours/month. Vehicle replacement planning (step 10): 4 hours/year.

### Staffing Implication
- **1 Fleet Manager** (within Supply Chain team): manages owned fleet (30–40 vehicles) and third-party carrier relationships. This role reports to Supply Chain Manager and coordinates daily with DC Dispatch.
- **30–40 Drivers** (BuildRight Logistics Inc. employees): assigned to owned vehicles; each driver covers ~1–2 routes/day, 5–6 days/week. Drivers are part of Logistics Inc. headcount (~600 total DC staff includes drivers).
- **Approved workshops**: 2–3 workshops per region (Davao, Cebu, Laguna, Clark) for scheduled and unscheduled maintenance. Fleet Manager manages workshop relationships and rate negotiations.
- **Fuel card program**: corporate fuel card (e.g., Petron Value Card, Shell Fleet Card) for all owned vehicles. Eliminates cash handling for fuel and enables automated consumption tracking.

---

## W66. Inter-Island Logistics & Freight Management

| Field | Detail |
|---|---|
| **Trigger** | Inter-DC transfer (W22) between islands (e.g., DC3 Luzon → DC2 Visayas, DC1 Mindanao → DC2 Visayas), or direct-to-store delivery to island locations not served by a DC on the same island |
| **Frequency** | ~10–15 inter-island shipments/month (supplementing ~30–40 inter-DC transfers/month in W22); additional ad-hoc shipments during peak season and disaster response (W49) |
| **Volume** | Typically 1–5 TEU containers per shipment; some loose cargo (LCL) for smaller transfers |
| **Owner** | Import Coordinator / Fleet Manager |
| **Participants** | Import Coordinator, Fleet Manager, DC Supervisor, Supply Planner, carrier (ro-ro or cargo vessel), Customs (if applicable) |

### Background

BuildRight's 4-DC footprint spans the Philippine archipelago: DC1 Davao (Mindanao), DC2 Cebu (Visayas), DC3 Laguna (South Luzon and NCR), and DC4 Clark (North/Central Luzon). Inter-DC transfers between islands require sea transport via roll-on/roll-off (ro-ro) ferries or containerized cargo vessels. Lead times are 3–7 days longer than same-island transfers. Cost per TEU for inter-island shipping: ~PHP 20,000–50,000 depending on route and carrier.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Supply Planner identifies need for inter-island transfer (W22) when demand at a DC cannot be met from same-island supply and vendor PO lead time is too long; or when seasonal inventory rebalancing requires inter-island movement | Supply Planner | Supply Planning Manager | Per W22 |
| 2 | Import Coordinator or Fleet Manager selects inter-island carrier and route: (a) **ro-ro ferry** — for truck-loaded cargo; vehicle driven onto ferry; 12–36 hours transit; routes: Manila→Cebu, Cebu→Davao, Manila→Davao (via Matnog); (b) **container vessel** — for containerized cargo; 3–7 days transit depending on route and vessel schedule; (c) **LCL consolidator** — for small transfers that don't fill a container | Import Coordinator / Fleet Manager | Supply Chain Manager | 1–2 hours/shipment |
| 3 | System creates Transfer Order per W22 with "Inter-Island" transport mode flag; extended lead time applied (3–7 days vs. 1–3 days for same-island); in-transit insurance coverage confirmed per W59 (cargo/in-transit policy) | Supply Planner | Supply Planning Manager | Per W22 |
| 4 | Source DC picks and loads goods; for container shipments: DC packs into container and seals; for ro-ro: goods loaded on owned or 3PL truck | DC Team | DC Supervisor | Per W3/W4 |
| 5 | Import Coordinator books shipment with carrier; provides container number or truck plate number, commodity description, and destination DC; receives booking confirmation and estimated arrival date | Import Coordinator | Fleet Manager | 30 min/shipment |
| 6 | In-transit tracking: Import Coordinator monitors shipment status via carrier tracking or direct communication; updates system ETA; for ro-ro: monitors ferry schedule (weather delays common during typhoon season — W49) | Import Coordinator | Supply Chain Manager | 15 min/day per shipment |
| 7 | Goods arrive at destination port/DC; destination DC receives and processes Goods Receipt per W22 step 7; system records inter-island freight cost allocation to transferred inventory | Receiving Clerk (DC) | DC Supervisor | Per W22 |
| 8 | System allocates inter-island freight cost to transferred items: freight cost ÷ total transferred value × per-item value added to destination inventory cost (similar to landed cost allocation in W2B.12 but for domestic inter-island movement) | System | Finance | Automated |
| 9 | Monthly: Import Coordinator and Fleet Manager review inter-island logistics cost and performance: cost per TEU by route, on-time delivery %, damage rate, carrier comparison; recommends route or carrier optimization | Import Coordinator / Fleet Manager | Supply Chain Manager | 1 hour/month |

### System Touchpoints
- Inter-island transfer order with extended lead time and transport mode flag (W66.3)
- Carrier booking integration or manual booking reference capture (W66.5)
- In-transit tracking with ETA updates (W66.6)
- Freight cost allocation to transferred inventory (W66.8)
- Inter-island logistics cost and performance reporting by route and carrier (W66.9)
- Integration with W22 (inter-DC transfers — this is the inter-island variant), W2B (import logistics — similar carrier booking process), W49 (typhoon season — ferry disruptions), W52 (fleet — owned vehicles on ro-ro), W59 (cargo insurance)

### Pain Points / Risks
- Typhoon season (June–November) disrupts ro-ro ferry schedules unpredictably — a single typhoon can delay inter-island shipments by 3–7 days, during which in-transit inventory is unavailable to any demand channel; with PHP 20,000–50,000/TEU of inventory in transit, the working capital impact is significant.
- Inter-island freight cost allocation (step 8) adds to transferred inventory cost, potentially making items uncompetitive at the destination DC's store pricing; the cost allocation decision (absorb vs. pass through) is contentious between Supply Chain and Merchandising.
- Ro-ro ferry booking availability during peak construction season (Q4) is limited — BuildRight competes with general cargo and passenger ferries for space, and late booking can mean waiting 2–3 days for the next available sailing.
- Container seal integrity during inter-island transit is a persistent concern — rough seas and multiple handling points (truck to vessel to truck) increase damage rates compared to same-island transfers; insurance claims (W59) for inter-island damage are more complex and slower to settle.
- Limited visibility into carrier performance for inter-island routes compared to domestic road freight — fewer tracking touchpoints and longer transit times create extended blind spots on the in-transit dashboard.

### Time Estimate
Carrier and route selection (step 2): 1–2 hours/shipment. Transfer order creation (step 3): per W22 standard. Shipment booking (step 5): 30 min/shipment. Daily in-transit monitoring (step 6): 15 min/day per active shipment. Destination receiving (step 7): per W22 standard. Monthly cost review (step 9): 1 hour/month. Total planning and coordination: ~20–30 hours/month for Import Coordinator across ~10–15 shipments.

### Staffing Implication
- **Import Coordinator**: absorbs inter-island coordination as an extension of existing import logistics duties. ~10–15 shipments/month × ~2 hours each = ~20–30 hours/month. Manageable given the Import Coordinator's existing workload managing ~20–30 import POs/month (W2B), as inter-island shipments use similar logistics skills.
- **Fleet Manager**: coordinates owned vehicle ro-ro transport when applicable. Absorbed.

---

## W106. DC Outbound Dispatch & Load Planning

| Field | Detail |
|---|---|
| **Trigger** | Daily outbound dispatch planning cycle (initiated each morning after W4 replenishment orders confirmed) |
| **Frequency** | Daily per DC; 2–3 dispatch waves per day (morning, midday, afternoon) |
| **Volume** | ~33 replenishment orders/DC/day + ~115 home delivery orders/DC/day + occasional inter-DC transfers (W22); loaded onto ~6–10 outbound trucks per DC per day |
| **Owner** | DC Dispatch Supervisor |
| **Participants** | DC Dispatch Supervisor, DC Supervisor, Loaders, Drivers, Fleet Manager, Supply Planner |

### Background

W4 (Store Replenishment) covers the pick/pack/ship process from the perspective of order creation through WMS-directed picking. However, the dispatch process — route planning, truck loading sequence, multi-stop routing, driver assignment, proof of delivery, and delivery confirmation — is not detailed in any existing workflow. This is a core daily warehouse operation that directly impacts delivery SLA (1–3 days from order to store receipt), fleet utilization, and transportation cost (~80% of which is third-party). This workflow fills that gap.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Morning dispatch planning** (6:00 AM): System generates daily outbound dispatch plan from confirmed pick/pack outputs: (a) store replenishment orders ready for dispatch (grouped by destination store and delivery route), (b) home delivery orders packed and staged (grouped by delivery zone), (c) inter-DC transfer orders (W22) if any, (d) promotional pre-positioning shipments (W57) with priority flag | System | — | Automated (nightly batch) |
| 2 | DC Dispatch Supervisor reviews dispatch plan and assigns loads to trucks: (a) **Route optimization**: system suggests optimal multi-stop route per truck based on store delivery addresses, traffic patterns (Metro Manila vs. provincial), and delivery time windows; Dispatch Supervisor accepts or adjusts, (b) **Load consolidation**: system groups multiple store replenishment orders on one truck where stores are on the same route (typical: 3–5 stores per truck for provincial routes; 5–8 for Metro Manila), (c) **Truck assignment**: owned fleet (W52) for regular scheduled routes; 3PL trucks for overflow, home delivery bulk, and inter-island, (d) **Home delivery batching**: system batches home delivery orders by delivery zone; assigns to 3PL carriers per W19 rate cards and zone coverage | DC Dispatch Supervisor | DC Supervisor | 30–60 min/day |
| 3 | DC Dispatch Supervisor prints or transmits load manifests to loaders and drivers: (a) **Load manifest**: truck ID, driver name, stop sequence (store name, address, delivery time window, order number, number of cases/totes, special instructions), (b) **Loading sequence**: system directs loading in reverse stop order (last stop loaded first, first stop loaded last) for efficient unloading at each stop, (c) **Special handling flags**: fragile items, hazardous materials (paint/chemicals), catch-weight items (lumber), temperature-sensitive items | DC Dispatch Supervisor | DC Supervisor | 15 min/truck |
| 4 | **Loading crew** loads truck per load manifest and loading sequence: (a) scan-confirm each case/tote against manifest during loading, (b) secure loads with straps/bars for transit, (c) load hazardous materials per DOT/DENR segregation rules (paint/chemicals separated from general merchandise), (d) load catch-weight items (lumber, rebar) last for easy access and to prevent damage to other goods | Loading Crew | DC Dispatch Supervisor | 30–60 min/truck |
| 5 | **Driver pre-departure**: (a) Driver reviews load manifest and route, (b) signs dispatch confirmation acknowledging load received and route assigned, (c) conducts vehicle pre-trip check per W52.2 (if owned vehicle), (d) departs DC per scheduled departure time (target: first truck departs by 8:00 AM for morning wave) | Driver | DC Dispatch Supervisor | 15 min |
| 6 | **In-transit tracking**: System tracks truck location via GPS (owned fleet) or 3PL carrier tracking API; DC Dispatch Supervisor monitors real-time delivery progress dashboard: (a) trucks en-route, (b) stops completed, (c) deliveries behind schedule (ETE > planned ETA by > 30 min flagged), (d) exceptions (traffic delay, road closure, vehicle breakdown) | System / DC Dispatch Supervisor | DC Supervisor | Continuous (15 min review every 2 hours) |
| 7 | **Store delivery execution**: (a) Driver arrives at store; presents load manifest to Receiving Clerk, (b) Receiving Clerk scans each case/tote against transfer order per W4.10, (c) Driver obtains signed delivery receipt (proof of delivery), (d) if short shipment or damage at delivery: noted on delivery receipt; Driver reports to DC Dispatch for resolution per W22.9a, (e) Driver proceeds to next stop | Driver / Receiving Clerk | DC Dispatch Supervisor / Store Manager | 15–30 min/stop |
| 8 | **Delivery confirmation**: (a) Upon completing all stops, Driver returns to DC (or proceeds to next dispatch wave), (b) Driver submits signed delivery receipts and exception reports to DC Dispatch, (c) DC Dispatch scans delivery receipts into system; system updates transfer order status to "Delivered" or "Partially Delivered" per receiving confirmation, (d) system triggers store inventory receipt posting (W4.12) | Driver / DC Dispatch Supervisor | DC Supervisor | 15 min/truck |
| 9 | **Afternoon wave** (1:00 PM): Repeat steps 1–8 for second dispatch wave using afternoon replenishment orders and remaining home delivery batches; typically lighter volume than morning wave | DC Dispatch Supervisor | DC Supervisor | Per steps 1–8 |
| 10 | **End-of-day dispatch summary**: DC Dispatch Supervisor generates daily dispatch report: (a) total orders dispatched, (b) on-time departure rate (target: ≥ 95% of trucks depart within 30 min of scheduled time), (c) on-time delivery rate (target: ≥ 95% of stores receive within delivery window), (d) truck utilization rate (loaded volume ÷ truck capacity), (e) exceptions and resolution, (f) 3PL carrier performance for the day (feeds W52.9 and W62B) | DC Dispatch Supervisor | DC Supervisor | 15 min/day |
| 11 | **Weekly**: DC Dispatch Supervisor and Fleet Manager review route efficiency metrics: (a) cost per delivery by route, (b) stops per route, (c) average delivery time per stop, (d) route optimization opportunities (new store additions, traffic pattern changes), (e) 3PL vs. owned fleet cost comparison per route; recommendations for route rebalancing or carrier changes | DC Dispatch Supervisor / Fleet Manager | DC Supervisor | 1 hour/week |

### System Touchpoints
- Daily outbound dispatch plan generation from picked/packed orders (W106.1)
- Route optimization engine: multi-stop routing with traffic, time window, and cost optimization (W106.2)
- Load consolidation: multiple orders grouped by route onto single truck (W106.2)
- Load manifest generation with stop sequence and loading order (W106.3)
- Barcode scan-confirmation during loading against manifest (W106.4)
- Driver dispatch confirmation with load acceptance (W106.5)
- Real-time GPS tracking dashboard for owned fleet; 3PL API tracking integration (W106.6)
- Delivery receipt capture and transfer order status update (W106.8)
- Daily dispatch report: departure rate, delivery rate, utilization, exceptions (W106.10)
- Weekly route efficiency analytics (W106.11)
- Integration with W4 (store replenishment — the orders being dispatched), W19 (home delivery — ecommerce dispatch), W22 (inter-DC transfers), W52 (fleet management — owned vehicle dispatch), W62B (3PL carrier management), W66 (inter-island logistics)

### Pain Points / Risks
- Multi-stop route optimization for Metro Manila delivery routes is unreliable due to unpredictable traffic congestion (especially during rush hours and rainy season flooding); planned 3–5 hour routes can extend to 6–8 hours, causing missed delivery windows at downstream stores.
- Truck utilization averaging 60–70% (driven by volumetric mismatches between order volume and truck capacity for building materials) represents significant wasted freight cost across ~6–10 trucks/DC/day.
- Hazardous material segregation compliance (paint/chemicals separated from general merchandise per step 4) is difficult to maintain during high-volume dispatch waves when loading crew are under time pressure; non-compliance risks DOT/DENR penalties.
- Proof-of-delivery capture (step 8) depends on Drivers returning physical signed delivery receipts to DC Dispatch — lost or delayed receipts prevent transfer order status updates, leaving in-transit inventory uncleared in the system.
- 3PL carrier performance variability for the afternoon dispatch wave (step 9) is higher than the morning wave because 3PL trucks are shared across multiple clients; late 3PL arrivals delay the entire afternoon dispatch schedule.

### Time Estimate
Morning dispatch planning (step 1): automated (nightly batch). Load assignment and manifest generation (steps 2–3): 30–60 min/day for DC Dispatch Supervisor. Loading (step 4): 30–60 min/truck. Driver pre-departure (step 5): 15 min/truck. In-transit monitoring (step 6): 15 min review every 2 hours. Delivery confirmation (step 8): 15 min/truck upon return. End-of-day summary (step 10): 15 min/day. Weekly route review (step 11): 1 hour/week. Total DC Dispatch Supervisor time: ~3–5 hours/day dedicated to dispatch management.

### Staffing Implication
- **1 DC Dispatch Supervisor per DC** (within existing ~150 DC headcount): manages daily dispatch planning, loading coordination, and driver management. This role likely already exists but was not formalized.
- **2–3 Loaders per DC** (within existing DC staff): dedicated to outbound loading during dispatch waves. Absorbed within existing pick/pack team.
- **No incremental headcount.**

---

## W188. Fleet Spare Parts & Preventive Maintenance (PM) Management

| Field | Detail |
|---|---|
| **Trigger** | Scheduled maintenance interval or spare part depletion |
| **Frequency** | Ongoing |
| **Volume** | Managing parts for ~40 owned vehicles |
| **Owner** | Fleet Manager |
| **Participants** | Driver, Workshop Supervisor, Procurement (for parts) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System tracks odometer/hours for each vehicle; triggers "Maintenance Alert" (W52.4) | System | — | Automated |
| 2 | Fleet Manager reviews spare parts inventory (tires, batteries, oil, filters, brake pads) | Fleet Manager | — | 30 min |
| 3 | If parts below reorder point: System generates PO for parts (W2A) | System | — | Automated |
| 4 | Vehicle sent to workshop; Fleet Manager issues "Maintenance Work Order" | Fleet Manager | — | 15 min |
| 5 | Workshop performs service; consumes spare parts from fleet inventory | Workshop Staff | — | 4-8 hours |
| 6 | Record maintenance details: parts used, labor hours, costs, next service interval | Fleet Manager | — | 20 min |
| 7 | Update vehicle status in Fleet Module: "Available" | Fleet Manager | — | 5 min |
| 8 | Quarterly: Analyze maintenance cost per km across all vehicle brands/models | Fleet Manager | Supply Chain Mgr | 2 hours |

### System Touchpoints
- Cost-per-Kilometer Analytics Dashboard (W188.8)

### Pain Points / Risks
- Spare parts stockouts for critical components (tires, batteries) can take vehicles off the road for days, disrupting DC delivery schedules and increasing reliance on costly 3PL alternatives.
- No single integrated fleet maintenance system in the current ERP — maintenance history, parts consumption, and cost tracking are fragmented across spreadsheets and workshop records.
- Inconsistent preventive maintenance compliance across regions (Davao, Cebu, Laguna, Clark) leads to uneven vehicle reliability and higher unplanned repair costs.
- Difficulty tracking actual vs. standard maintenance cost per kilometer across vehicle brands and age brackets, making replacement planning subjective rather than data-driven.

---

### Time Estimate
Scheduled PM service: 4–8 hours per vehicle per event; emergency repair: 1–3 days depending on parts availability. Fleet Manager spends ~30 min/week on parts review and ~2 hours/quarter on cost analysis.

### Staffing Implication
- **Fleet Manager**: absorbs spare parts inventory review (~30 min/week) and quarterly cost analysis (~2 hours/quarter) as an extension of existing fleet management duties (W52). No incremental headcount.
- **Workshop Supervisor**: at each approved workshop (2–3 per region), performs maintenance per Fleet Manager work order. External service provider, not BuildRight headcount.
- **Parts procurement**: system-generated POs (W2A) for spare parts are processed by existing Procurement team. ~5–10 spare parts POs/month. Absorbed.

## W221. Cross-Docking Operations for Fast-Moving Bulky Items

| Field | Detail |
|---|---|
| **Trigger** | Advance Shipping Notice (ASN) or incoming import container contains fast-moving bulk items (cement, steel rebar, standard tiles) with active store replenishment demands or backorders |
| **Frequency** | Daily at Distribution Centers |
| **Volume** | ~10–20 container-loads cross-docked per day |
| **Owner** | DC Operations Manager |
| **Participants** | Receiving Clerk, Cross-Dock Coordinator, Forklift Operator, Shipping Clerk |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-Allocation Matching**: System evaluates incoming container ASN against active store replenishment orders (W4) and customer backorders (W56); identifies high-matching fast-moving SKUs suitable for cross-docking | System | DC Operations Mgr | Automated |
| 2 | **Dock Assignment**: Cross-Dock Coordinator assigns inbound container to a receiving dock adjacent to outbound store dispatch doors | Cross-Dock Coord | — | 10 min |
| 3 | **Unloading & Direct Scan**: Forklift Operator unloads pallets; scan-confirms receipt via WMS terminal; system detects pre-allocation and flags pallet for "Direct Cross-Dock Staging" (bypassing normal bulk putaway racks) | Forklift Operator | Receiving Supervisor | 15 min/pallet |
| 4 | **Sorting & Routing**: Receiving Clerk scan-confirms pallet; system generates store-specific routing labels and prints destination tags; Forklift Operator moves pallets directly to the designated outbound lane | Receiving Clerk | — | 5 min/pallet |
| 5 | **Load Integration**: System automatically merges cross-docked pallets into the active outbound DC load planning schedule (W106) for store deliveries | System | — | Automated |
| 6 | **Outbound Loading**: Forklift Operator loads the pallets directly onto the designated store delivery truck; scan-confirms loading; Shipping Clerk generates Outbound Transfer document | Forklift Operator / Shipping Clerk | DC Operations Mgr | 10 min/pallet |

### System Touchpoints
- WMS pre-allocation engine (ASN cross-reference with store demand)
- Cross-dock staging zone barcode/RFID scanning
- Putaway bypass logic and real-time destination tag printing
- Integration with W4 (store replenishment), W106 (outbound dispatch), and W56 (backorders)

### Pain Points / Risks
- Pre-allocation matching accuracy depends on clean ASN data from vendors; incomplete or delayed ASNs force manual cross-dock decisions, increasing error risk and staging time.
- Dock door congestion when multiple cross-dock containers arrive simultaneously — limited adjacent receiving/dispatch doors create bottlenecks during peak morning hours.
- Misrouted pallets (cross-dock items accidentally put away into bulk storage) break the fulfillment chain and cause store delivery shortfalls that are difficult to trace.
- High coordination overhead between Receiving, Cross-Dock Coordinator, and Outbound Dispatch; any communication gap delays the time-sensitive cross-dock window.

---

### Time Estimate
~45–90 min per container from gate-in to outbound staging (bypasses normal putaway); cross-dock coordinator spends ~60–90 min/day on dock assignments and routing. Total dock-to-truck cycle: 2–4 hours for a fully matched container.

### Staffing Implication
- **Cross-Dock Coordinator**: 1 per DC (within existing DC staff), dedicated to cross-dock dock assignments, routing, and staging coordination. Spends ~60–90 min/day on cross-dock activities. Absorbed within existing DC operations team.
- **Forklift Operators**: existing DC forklift operators handle cross-dock pallet movement as part of their standard duties; no incremental operators required.
- **Receiving Clerk**: cross-dock scanning adds ~5 min/pallet to existing receiving workload; with ~10–20 containers/day and cross-dock applicable to ~30% of receipts, this is ~15–30 min/day additional. Absorbed.
- **No incremental headcount.**

## W222. DC Container Yard & Chassis Management

| Field | Detail |
|---|---|
| **Trigger** | Import container arrives at DC gate, or empty container requires scheduling for port return |
| **Frequency** | 20–50 container movements per day |
| **Volume** | 200-slot yard capacity |
| **Owner** | Yard Superintendent |
| **Participants** | Gate Guard, Yard Coordinator, Reach Stacker Operator, Dispatcher, 3PL Truck Driver |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Gate-In Registration**: Gate Guard inspects seal integrity, container physical state, and chassis lease records; scan-registers container number in Yard Management System (YMS); records gate-in timestamp | Gate Guard | Yard Superintendent | 10 min |
| 2 | **Yard Slot Assignment**: YMS automatically assigns slot coordinates (grid lane, stack height) based on container status (Full Import, Empty Return, Hazmat quarantine) and priority | System | — | Automated |
| 3 | **Physical Stacking**: Reach Stacker Operator picks container from truck chassis; places in assigned yard slot; scan-confirms the grid coordinates in YMS to update the real-time yard map | Reach Stacker Operator | Yard Coordinator | 5 min |
| 4 | **Demurrage & Detention Tracking**: YMS starts carrier-specific free-time countdown timers (e.g., 4 days yard free time, 7 days container lease); triggers daily priority warnings to Import Logistics team | System | Yard Superintendent | Automated |
| 5 | **Stripping Scheduling**: Yard Coordinator assigns yard container to a warehouse dock; Reach Stacker Operator moves container to dock chassis; Receiving Clerk scan-registers goods receipt (W3) | Yard Coordinator / Reach Stacker Operator | — | 20 min |
| 6 | **Empty Container Gate-Out**: System marks container "Empty"; Dispatcher books return logistics; Reach Stacker Operator loads empty container to carrier chassis; Gate Guard records gate-out, verifies empty status, and registers time in YMS | Reach Stacker Operator / Gate Guard | Yard Superintendent | 10 min |

### System Touchpoints
- Yard Management System (YMS) visual slot coordinate mapping
- Gate-In / Gate-Out timestamp and seal-verification log
- Carrier demurrage & detention countdown timers with email alert engine
- Integration with W3 (warehouse receiving) and W144 (import operations)

### Pain Points / Risks
- Demurrage and detention costs escalate rapidly (PHP 2,000–5,000/day per container) when stripping is delayed due to dock congestion or labor shortages; with 20–50 containers/day, even one day of delay across a batch can cost PHP 100K+.
- Limited 200-slot yard capacity becomes a binding constraint during peak import seasons (Q4 construction peak), forcing costly off-site container storage.
- Chassis availability from carriers is unpredictable — containers cannot be moved from yard to dock without a chassis, creating deadlock situations when carriers fail to deliver on schedule.
- Manual seal verification and physical condition inspection at gate-in are error-prone; missed damage or broken seals discovered at stripping leads to vendor disputes and insurance claim complications.

---

### Time Estimate
Gate-in to stacking: ~15 min per container; stripping scheduling: ~20 min per container; empty gate-out: ~10 min per container. Yard Superintendent spends ~1–2 hours/day coordinating movements across 20–50 containers.

### Staffing Implication
- **Yard Superintendent**: 1 per DC with significant container yard operations (primarily DC3 Laguna with port proximity); manages yard team and coordinates with Import Logistics. Absorbed within existing DC management structure.
- **Yard Coordinator**: 1 per DC; handles slot assignment, stripping scheduling, and container movement coordination. Spends ~4–6 hours/day on yard coordination for 20–50 container movements. Absorbed within existing DC staff.
- **Gate Guard**: existing gate guard handles container gate-in/gate-out registration as part of standard access control duties; adds ~10 min per container movement. Absorbed.
- **Reach Stacker Operator**: 1–2 per DC; dedicated equipment operator for container stacking and dock movement. Absorbed within existing DC equipment operations team.
- **No incremental headcount.**

## W270. Pallet & Returnable Transport Packaging (RTP) Tracking

| Field | Detail |
|---|---|
| **Trigger** | Receipt of goods on vendor-owned pallets/crates or shipment to stores using internal RTP |
| **Frequency** | Daily |
| **Volume** | Hundreds of pallets/crates per DC per day; ~50–100 vendor RTP exchanges/day across all DCs |
| **Owner** | DC Manager (DC-level); Store Receiving Clerk (store-level) |
| **Participants** | DC Receiving Clerk, Store Receiving Clerk, Yard Coordinator, Vendor Logistics, AP Clerk, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | DC Receiving Clerk logs quantity and type of vendor-owned RTPs (pallets, crates, totes) received alongside each PO Goods Receipt; records RTP type (standard pallet, custom crate, collapsible tote), vendor ID, and quantity in WMS | DC Receiving Clerk | DC Supervisor | 3 min/receipt |
| 2 | System updates the RTP liability balance for the vendor — increases vendor RTP receivable by quantity received; RTPs tracked as non-valuated assets (no inventory value) but with quantity accountability per vendor | System | — | Automated |
| 3 | DC transfers goods to stores using internal (BuildRight-owned) RTPs; system tracks internal RTP location from DC to store and records the store as the current RTP holder | DC Dispatch / Store Receiving Clerk | DC Supervisor | 2 min/dispatch |
| 4 | Store Receiving Clerk or DC Receiving Clerk returns empty vendor-owned RTPs to vendor during next vendor delivery or scheduled pickup; system debits the vendor RTP liability balance by quantity returned; Guard verifies RTP count at gate-out | Store Receiving Clerk / DC Receiving Clerk | Store Manager / DC Supervisor | 5 min/return |
| 4a | Store returns empty BuildRight-owned RTPs to DC via DC delivery truck backhaul; system updates internal RTP location from store to DC | Store Receiving Clerk | Store Manager | 2 min/return |
| 5 | Finance reconciles RTP balances monthly per vendor: system generates RTP aging report showing outstanding vendor RTP receivables by vendor, RTP type, and days outstanding; AP Clerk compares system RTP balance to vendor's RTP statement | AP Clerk | Controller | 1 hour/month |
| 6 | For lost or damaged RTPs: system generates penalty invoice per vendor RTP agreement terms (standard penalty: PHP 300–500 per standard pallet, PHP 1,000–3,000 per custom crate); AP Clerk issues debit memo to vendor or deducts from next payment; if BuildRight-owned RTP lost by store, Store Manager investigates and absorbs cost in store shrinkage | AP Clerk / Store Manager | Controller | 15 min/case |
| 7 | Quarterly: DC Manager reviews RTP return rate per vendor and per store; identifies stores with low RTP return compliance for process improvement; flags vendors with persistent RTP discrepancies for contract renegotiation | DC Manager | Supply Chain Manager | 2 hours/quarter |

### System Touchpoints
- WMS RTP tracking module: non-valuated asset tracking per vendor with quantity and type (W270.1–2)
- Internal RTP location tracking across DC-to-store-to-DC cycle (W270.3, 4a)
- Vendor RTP liability balance with automated debit/credit on receipt and return (W270.2, 4)
- RTP aging report: outstanding vendor RTP receivables by vendor, type, and days outstanding (W270.5)
- Penalty invoice / debit memo generation per vendor RTP agreement terms (W270.6)
- Quarterly RTP return rate analytics per vendor and per store (W270.7)
- Integration with W3 (DC receiving — RTP logging at GR), W4 (store receiving — internal RTP tracking), W7 (AP — penalty invoice processing), W22 (transfers — RTP movement with stock)

### Pain Points / Risks
- High cost of lost pallets and disputes with vendors over unreturned crates — with ~50–100 vendor RTP exchanges/day across DCs, even a 5% loss rate represents PHP 150,000–300,000/month in penalties or unrecovered assets.
- BuildRight-owned RTPs returned from stores via DC truck backhaul compete with store-to-DC returns (W22B) and proactive rebalancing shipments (W154) for limited reverse-logistics space, causing RTP accumulation at stores.
- Vendor RTP statement reconciliation (step 5) frequently shows discrepancies because vendor delivery drivers sometimes exchange RTPs informally (handing over pallets without system recording) during receiving, bypassing the formal RTP logging process.
- Custom crates for tiles and fragile items are expensive (PHP 1,000–3,000 each) and prone to damage during return transit; vendors dispute liability for damaged crates, leading to extended reconciliation cycles.
- Store-level RTP tracking compliance is inconsistent — Store Receiving Clerks focused on product receiving (W4 step 10) sometimes skip the RTP quantity entry, causing the RTP liability balance to drift from actual inventory over time.

### Staffing Implication
- **DC Receiving Clerk**: ~3 min additional per receipt for RTP logging; with ~40 receipts/day/DC, this adds ~2 hours/day across the receiving team. Absorbed.
- **AP Clerk**: ~1 hour/month for RTP reconciliation and penalty processing. Absorbed.
- **DC Manager**: ~2 hours/quarter for RTP return rate review. Absorbed.
- **No incremental headcount.**

### Time Estimate
3–5 min per receipt/return for RTP logging; 1 hour/month for reconciliation; 2 hours/quarter for analytics review.

---

## W584. DC Daily Operations & Shift Management

| Field | Detail |
|---|---|
| **Trigger** | Daily DC operations cycle; shift start (6:00 AM for Day Shift A, 2:00 PM for Night Shift B) |
| **Frequency** | Continuous; 2 shifts per day, 7 days/week per DC |
| **Volume** | 4 DCs; each DC operates ~16 hours/day; ~40 inbound trucks/day + ~30 outbound loads/day per DC; ~150 DC staff on duty per shift per DC |
| **Owner** | DC Manager |
| **Participants** | DC Shift Supervisors (2 per DC), DC Receiving Supervisor, DC Dispatch Supervisor, DC Receiving Clerks, Putaway Staff, Pickers, Loaders, Quality Checkers, Yard Staff, Forklift Operators, Cross-Dock Coordinator, Gate Guard |

### Background

Each BuildRight DC processes ~70 truck movements per day (40 inbound receipts + 30 outbound dispatches) across 8–12 dock doors, with ~150 staff on duty per shift managing receiving, putaway, picking, packing, dispatch, and yard operations. With 2 shifts covering ~16 hours of operation, structured shift management is essential to maintain throughput, ensure labor alignment with daily volume, and prevent operational gaps at shift transitions. This workflow covers the holistic daily command-and-control layer that sits above individual operational workflows (W3 receiving, W106 dispatch, W585 dock scheduling, W586 KPI tracking).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Night-before preparation** (10:00 PM prior day): System generates next-day DC operations plan from: (a) inbound delivery appointments from W585 dock scheduling (confirmed inbound trucks, expected POs, estimated pallet/cube volume per time slot), (b) outbound dispatch plan from W106 (confirmed store replenishment orders, home delivery batches, inter-DC transfers), (c) pending putaway backlog from current shift, (d) pending pick/pack backlog from current shift, (e) staffing availability (planned absences, approved leaves, overtime authorizations); system calculates projected labor-hours required per function (receiving, putaway, picking, packing, dispatch, yard) vs. scheduled staff per shift | System | — | Automated (overnight batch) |
| 2 | **Day Shift A start-up briefing** (6:00 AM): DC Shift Supervisor (A) conducts 15-minute standing briefing with functional leads (Receiving Supervisor, Dispatch Supervisor, Cross-Dock Coordinator, Yard Supervisor) covering: (a) today's volume forecast from step 1 (inbound truck count, outbound load count, total lines to process), (b) critical priorities (promotional pre-positioning shipments per W57, import container appointments, urgent backorder fulfillments per W56), (c) staffing adjustments (reallocate labor from low-volume function to bottleneck function — e.g., shift 2 putaway staff to receiving during 8–10 AM peak), (d) carry-over exceptions from Night Shift B (unresolved receiving discrepancies per W3.6, incomplete picks, delayed dispatches), (e) safety reminders (daily topic: forklift pedestrian zones, hazmat handling, wet floor from yard rain) | DC Shift Supervisor (A) | DC Manager | 15 min |
| 3 | **Labor allocation and task assignment** (6:15 AM): DC Shift Supervisor assigns staff to functional areas based on step 2 briefing: (a) Receiving: 3–4 Receiving Clerks + 3–4 Unloading Crew for ~40 inbound trucks (peak 8–10 AM: 15–20 trucks in 2-hour window requiring maximum receiving staffing); (b) Quality Check: 2 Quality Checkers during peak receiving, 1 during off-peak; (c) Putaway: 4–6 Putaway Staff, prioritizing cross-dock items and forward-pick zone replenishment before standard putaway; (d) Picking: 8–10 Pickers for outbound replenishment orders per W4 picking waves (Wave 1: 8:00 AM, Wave 2: 12:00 PM, Wave 3: 4:00 PM); (e) Dispatch: 2–3 Loaders for outbound truck loading per W106; (f) Yard: 2–3 Yard Staff for outdoor receipts and staging; system records shift labor allocation for W586 labor utilization tracking | DC Shift Supervisor | DC Manager | 15 min |
| 4 | **Mid-morning operational pace check** (9:00 AM): DC Shift Supervisor walks DC floor and reviews real-time operational dashboard on wall-mounted display: (a) dock door utilization per W585 — are all scheduled inbound trucks on time? Any no-shows?; (b) receiving throughput — actual receipts completed vs. planned for the morning window; (c) putaway backlog — staged pallets awaiting putaway should not exceed 2-hour backlog; (d) picking progress — Wave 1 pick completion % (target: 100% by 10:00 AM for morning dispatch); (e) outbound staging — trucks loaded and departing on schedule per W106; (f) any congestion or bottleneck observed during floor walk; DC Shift Supervisor reassigns labor in real-time if any function is behind plan | DC Shift Supervisor | DC Manager | 20 min |
| 5 | **Exception handling** (ongoing throughout shift): DC Shift Supervisor resolves escalated operational exceptions: (a) receiving discrepancies requiring immediate Buyer coordination (W3.6b) — truck occupying dock door while awaiting Buyer response; (b) equipment failures (forklift breakdown, conveyor jam, RF scanner issues) — arrange backup equipment or manual workaround, notify IT per W48 if system-related; (c) staffing emergencies (no-show, medical incident) — cross-trained staff redeployment from lower-priority function; (d) vendor/carrier disputes at gate (unscheduled delivery, documentation issues) — authorize or reject per W585 unscheduled delivery protocol; (e) quality holds blocking putaway (W3 quality hold process) — coordinate with Buyer for expedited vendor resolution; log all exceptions in shift log with resolution and time-to-resolve | DC Shift Supervisor | DC Manager | 5–30 min per exception; ~4–6 exceptions/shift |
| 6 | **Afternoon operational pace check** (1:00 PM): DC Shift Supervisor reviews second operational dashboard snapshot: (a) total inbound receipts completed vs. plan (target: 100% of morning appointments completed by 1:00 PM); (b) total outbound dispatches completed vs. plan; (c) afternoon inbound appointment schedule for 1:00–6:00 PM window; (d) picking progress — Wave 2 completion status; (e) dock door availability for afternoon dispatch wave per W106 step 9; (f) putaway and picking backlogs — should be near-zero before shift handover | DC Shift Supervisor | DC Manager | 15 min |
| 7 | **Shift handover log** (1:45 PM — end of Day Shift A / start of Night Shift B): DC Shift Supervisor (A) completes shift handover log in system and conducts face-to-face handover with incoming DC Shift Supervisor (B). Handover log captures: (a) inbound status: receipts completed (count and lines), receipts pending (with reason — late truck, quality hold, Buyer pending), dock door occupancy, unscheduled deliveries handled; (b) outbound status: dispatches completed, dispatches pending (with reason — pick incomplete, truck late, 3PL no-show), truck utilization rate for completed dispatches; (c) inventory operations: putaway backlog (pallet count and estimated hours to clear), pick wave completion status, cycle count results if any per W6; (d) exceptions: unresolved exceptions from step 5 with current status and required actions; (e) equipment status: forklift availability, RF scanner status, dock leveler issues; (f) staffing: actual headcount vs. planned, overtime hours consumed, any injuries or incidents; incoming Shift Supervisor (B) acknowledges handover in system | DC Shift Supervisor (A) / DC Shift Supervisor (B) | DC Manager | 20 min |
| 8 | **Night Shift B start-up briefing** (2:00 PM): DC Shift Supervisor (B) conducts abbreviated briefing with night shift functional leads covering: (a) carry-over items from Day Shift A handover log; (b) afternoon inbound appointment schedule; (c) afternoon dispatch wave per W106; (d) any night-specific activities (cycle counts per W6, scheduled maintenance per W188, putaway catch-up, next-day preparation tasks) | DC Shift Supervisor (B) | DC Manager | 10 min |
| 9 | **Night shift operations** (2:00–10:00 PM): Night shift focuses on: (a) completing remaining afternoon inbound receipts and outbound dispatches; (b) putaway backlog clearance — target: zero staged pallets in receiving area by end of shift; (c) picking for next-morning dispatch wave (Wave 1 for following day); (d) cycle counting per W6 schedule (if tonight's zone is due); (e) yard organization and staging for next-morning deliveries; (f) next-day preparation: confirm dock appointments for following day per W585, pre-stage outbound loads for early morning dispatch | DC Shift Supervisor (B) | DC Manager | 8 hours |
| 10 | **End-of-day KPI snapshot** (10:00 PM — end of Night Shift B): System automatically calculates end-of-day operational KPIs per DC and posts to W586 dashboard: (a) **Receiving throughput**: total receipts completed vs. planned, average time per receipt (gate-to-bin), receiving accuracy % (correct GRs / total GRs); (b) **Putaway**: total pallets put away, putaway backlog at EOD (target: 0), average putaway time per pallet; (c) **Picking productivity**: lines picked per picker-hour, pick accuracy %, wave completion on-time %; (d) **Dispatch**: outbound loads dispatched vs. planned, on-time departure rate, truck utilization %, delivery on-time rate (from prior-day dispatch POD returns); (e) **Labor utilization**: actual labor-hours vs. planned, overtime hours, labor-hours per unit processed (receipts + dispatches); (f) **Exceptions**: count and category breakdown, average time-to-resolve; DC Shift Supervisor (B) reviews snapshot, adds narrative comments for any KPI below target, and closes shift log | System / DC Shift Supervisor (B) | DC Manager | 15 min (supervisor review) + automated calculation |
| 11 | **DC Manager daily review** (8:00 AM following morning): DC Manager reviews overnight KPI snapshot from step 10, shift handover logs from both shifts, and exception log; identifies: (a) trends requiring corrective action (e.g., receiving throughput declining 3 consecutive days), (b) staffing adjustments needed for today's volume, (c) escalation items for Supply Chain Manager (e.g., chronic carrier no-shows, vendor quality issues); DC Manager documents daily operational summary and submits to VP Supply Chain via automated report | DC Manager | VP Supply Chain | 20 min/day |
| 12 | **Weekly operations review** (Monday 9:00 AM): DC Manager conducts weekly review with Shift Supervisors and functional leads: (a) weekly KPI trend analysis per W586 (comparing daily snapshots across 7 days); (b) labor productivity trend — lines processed per labor-hour, overtime trend; (c) recurring exception analysis — top 5 exception categories by frequency and impact; (d) dock utilization patterns — peak hours, under-utilized slots per W585; (e) staffing forecast for next week based on projected inbound/outbound volume; (f) action items from previous week — status update; (g) improvement initiatives — at least 1 process improvement proposal per month (e.g., new putaway zone strategy, revised pick wave timing) | DC Manager | VP Supply Chain | 1 hour/week |

**Total time per DC per day**: ~3.5–4.5 hours of supervisor/management time on daily operations management (Step 2: 15 min + Step 3: 15 min + Step 4: 20 min + Step 5: ~60–90 min exception handling + Step 6: 15 min + Step 7: 20 min + Step 8: 10 min + Step 10: 15 min + Step 11: 20 min + automated steps). Absorbed within existing DC management roles.

### System Touchpoints (W584 — DC Daily Operations & Shift Management)
- Night-before operations plan generation from inbound appointments (W585), outbound dispatch plan (W106), backlog data, and staffing availability (W584.1)
- Shift labor allocation module: records staff-to-function assignments per shift with real-time reallocability (W584.3)
- Real-time operational dashboard: dock door utilization (W585), receiving throughput, putaway backlog, pick wave progress, outbound staging status (W584.4, 6)
- Exception logging with categorization, time-to-resolve tracking, and escalation triggers (W584.5)
- Shift handover log: structured digital handover with incoming supervisor acknowledgment (W584.7)
- Automated end-of-day KPI snapshot calculation and posting to W586 dashboard (W584.10)
- DC Manager daily operational summary report with automated submission to VP Supply Chain (W584.11)
- Weekly operations review analytics: KPI trends, labor productivity, exception patterns, dock utilization (W584.12)
- Integration with W3 (receiving — throughput and quality data), W106 (dispatch — loading and departure data), W585 (dock scheduling — appointment data and dock utilization), W586 (KPI dashboard — performance data feed), W6 (cycle counting — night shift count data), W48 (IT helpdesk — equipment/system exceptions), W188 (fleet maintenance — equipment availability), W52 (fleet — carrier performance), W57 (promotions — pre-positioning priority)

### Pain Points / Risks
- **Shift handover information loss**: despite structured handover logs (step 7), critical nuances (e.g., "vendor driver said he will return with missing documents after lunch") are often communicated verbally and lost when the incoming shift supervisor was not present during the conversation; mitigated by mandatory handover log acknowledgment but not fully eliminated.
- **Labor reallocation disrupts picking productivity**: when Shift Supervisors pull Pickers to help with receiving during the 8–10 AM inbound peak (step 3), picking Wave 1 completion is delayed, cascading into late morning dispatches; the trade-off between receiving throughput and picking throughput has no optimal answer during high-volume days with > 50 inbound trucks.
- **Exception handling consumes disproportionate supervisor time**: with 4–6 exceptions per shift at 5–30 min each, DC Shift Supervisors spend 30–120 min/shift on exception resolution, pulling them away from proactive operational management (floor walks, pace checks); during typhoon season (June–November in the Philippines), exceptions spike to 8–12 per shift due to delivery delays, flooded yard areas, and carrier cancellations.
- **Night shift staffing gaps for specialized functions**: Quality Checkers (requiring category-specific inspection training) and Reach Stacker Operators (licensed equipment operators) are typically scheduled only on day shift; night shift receiving that requires quality inspection or container movements must wait for the following day, creating a 10-hour process gap.
- **End-of-day KPI snapshot data quality** depends on real-time transaction posting compliance by DC staff; if Receiving Clerks delay GR posting (batch-entering at end of shift instead of real-time), the KPI snapshot understates actual throughput and overstates backlog.

### Staffing Implication
- **DC Manager** (1 per DC): adds ~20 min/day for daily KPI review and operational summary (step 11), plus 1 hour/week for weekly operations review (step 12). Absorbed within existing DC Manager role.
- **DC Shift Supervisors** (2 per DC): each shift supervisor spends ~1.5–2 hours/shift on daily operations management activities (briefing, labor allocation, pace checks, exception handling, handover). These are core supervisory duties absorbed within existing Shift Supervisor roles.
- **No incremental headcount** — all activities are core DC supervisory management functions that formalize existing informal practices into structured workflow steps.

---

## W585. DC Dock Scheduling & Appointment Management

| Field | Detail |
|---|---|
| **Trigger** | Inbound delivery appointment request (from vendor, carrier, or Buyer) or outbound dispatch scheduling requirement |
| **Frequency** | Continuous; ~70 appointment slots managed per day per DC (40 inbound + 30 outbound) |
| **Volume** | ~1,200 inbound appointments/month per DC; ~900 outbound load slots/month per DC; peak receiving window 8:00–10:00 AM with 15–20 inbound trucks arriving |
| **Owner** | DC Receiving Supervisor (inbound) / DC Dispatch Supervisor (outbound) |
| **Participants** | DC Receiving Supervisor, DC Dispatch Supervisor, DC Shift Supervisor, Gate Guard, Buyers, Import Coordinator, Vendors/Carriers, 3PL dispatch, Fleet Manager |

### Background

Each BuildRight DC has 8–12 dock doors serving both inbound and outbound operations. With ~70 total truck movements per day (40 inbound + 30 outbound) and a peak receiving concentration of 15–20 trucks during the 8:00–10:00 AM window, dock door congestion is the single largest throughput constraint in DC operations. Without systematic scheduling, trucks queue at the gate, occupy dock doors beyond their needed time while waiting for receiving staff, and outbound dispatches are delayed because loading doors are occupied by inbound trucks. This workflow establishes structured appointment management to optimize dock door throughput and prevent congestion. It extends the basic scheduling concepts in W3C (DC Inbound Delivery Scheduling) into a comprehensive dock appointment system covering both inbound and outbound movements.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Appointment request intake**: Three sources generate dock appointment requests: (a) **Inbound — domestic vendor**: Buyer or vendor submits delivery appointment request via vendor portal or email to DC Receiving Supervisor with PO number, vendor name, commodity category, estimated pallet/cube count, special requirements (hazmat, catch-weight, oversized); (b) **Inbound — import container**: Import Coordinator submits appointment request with container number, commodity, port release confirmation, estimated weight, and special handling; (c) **Outbound — dispatch**: DC Dispatch Supervisor requests outbound dock slot based on dispatch plan from W106 step 2 (truck type, destination route, estimated loading time, owned vs. 3PL carrier); all requests logged in dock appointment system with request timestamp and requested date/time window | Buyer / Import Coordinator / DC Dispatch Supervisor | DC Receiving Supervisor (inbound) / DC Dispatch Supervisor (outbound) | 5–10 min per request |
| 2 | **Dock door assignment and time slot allocation**: DC Receiving Supervisor reviews appointment requests against dock door availability calendar: (a) each dock door has a configurable capacity per time slot (default: 2-hour slot, 1 truck per slot, extendable to 3 hours for import containers or oversized loads); (b) dock doors are categorized by capability — standard (general merchandise), heavy-duty (cement, steel, lumber — reinforced dock leveler), hazmat-equipped (paint, chemicals — ventilation and spill containment); (c) system suggests optimal dock door assignment based on: door capability match, proximity to staging area (inbound: near receiving staging; outbound: near pick-pack staging), current loading at adjacent doors (avoid congestion at single dock area); (d) DC Receiving Supervisor confirms or adjusts door assignment and time slot; system blocks the assigned slot on the dock calendar | DC Receiving Supervisor / DC Dispatch Supervisor | DC Manager | 5 min per appointment |
| 3 | **Carrier/vendor notification**: System sends automated appointment confirmation to vendor or carrier via: (a) email with appointment details (date, time window, dock door number, DC address, PO reference, special instructions); (b) SMS reminder to driver/contact number 24 hours before appointment; (c) vendor portal update with confirmed appointment status; confirmation includes: DC gate entry requirements (valid ID, delivery receipt, PO copy), estimated unloading time, and contact number for day-of issues; for outbound: system notifies 3PL carrier or owned-fleet Driver of assigned loading slot and dock door via SMS and fleet management system (W52) | System | DC Receiving Supervisor | Automated |
| 4 | **Day-of check-in** (at DC gate): Truck arrives at DC gate; Gate Guard performs check-in: (a) verifies appointment in system — matches truck plate, vendor/carrier name, and PO number against confirmed appointment; (b) if appointment confirmed and on-time (within scheduled 2-hour window): Guard issues gate pass, directs truck to assigned dock door, and updates appointment status to "Arrived — On Time"; (c) if appointment confirmed but early (arrived before scheduled window): Guard directs truck to designated holding area, updates status to "Arrived — Early — Waiting", and instructs driver to wait until scheduled window; (d) if appointment confirmed but late (arrived after scheduled window ended): Guard checks dock availability — if dock door is free, accepts and reassigns; if dock door is occupied by next appointment, places truck in holding area for next available slot and updates status to "Arrived — Late — Rescheduled"; (e) if no appointment (walk-in): Guard follows W3C.5 unscheduled delivery protocol — checks against open PO list, accepts only if dock door available and receiving staff capacity exists; logs as "Unscheduled Walk-In" | Gate Guard | DC Receiving Supervisor | 5 min per truck |
| 5 | **Dock door utilization tracking** (real-time): System maintains real-time dock door status dashboard visible to DC Shift Supervisor, DC Receiving Supervisor, and DC Dispatch Supervisor: (a) each dock door shows current status: Available, Occupied (with truck ID, vendor/carrier, appointment time, elapsed time), Reserved (next appointment with countdown to arrival), Out of Service (maintenance, equipment issue); (b) system calculates live dock utilization rate: occupied doors / total available doors; target utilization: 75–85% (below 75% = underutilized capacity; above 85% = congestion risk); (c) system flags doors occupied beyond scheduled time slot with amber (15 min over) and red (30+ min over) alerts to DC Shift Supervisor for intervention; (d) historical dock utilization data feeds W586 KPI dashboard | System | — | Automated (real-time) |
| 6 | **No-show management**: System monitors appointment status at 30 minutes past scheduled window end: (a) if carrier/vendor has not arrived and no communication received: system marks appointment as "No-Show" and releases dock door back to available pool; (b) DC Receiving Supervisor notifies Buyer (inbound) or Fleet Manager (outbound) of no-show; (c) for recurring no-show vendors (3+ no-shows in rolling 30-day window): system escalates to DC Manager for vendor scorecard impact per W44; (d) released dock door slots from no-shows are immediately available for: unscheduled walk-in acceptance, rescheduling late arrivals, or pulling forward afternoon appointments to fill morning gaps; (e) monthly: DC Receiving Supervisor generates no-show rate report per vendor and per carrier; feeds into W44 vendor scorecard and W242 3PL performance review | System / DC Receiving Supervisor | DC Manager | Automated monitoring + 15 min/day manual follow-up |
| 7 | **Appointment compliance reporting**: System calculates daily appointment compliance metrics: (a) **On-time arrival rate**: % of appointments where truck arrived within scheduled window (target: ≥ 85%); (b) **Dock turn time**: average time from truck dock-in to dock-out, by appointment type (inbound domestic, inbound import, outbound store delivery, outbound home delivery, outbound inter-DC); (c) **Dock door utilization rate**: average % of available dock-door-hours occupied during operating hours; (d) **Unscheduled walk-in rate**: % of total movements that were unscheduled (target: ≤ 5%); (e) **Slot adherence rate**: % of appointments that completed within the scheduled time slot (target: ≥ 80%); daily metrics feed W586 KPI dashboard; weekly trend analysis feeds W584 weekly operations review | System / DC Receiving Supervisor | DC Manager | Automated calculation + 30 min/week review |
| 8 | **Monthly dock capacity planning**: DC Manager reviews monthly dock utilization trends with DC Receiving Supervisor and DC Dispatch Supervisor: (a) identify peak hours and under-utilized windows — consider extending operating hours or adding temporary dock doors during seasonal peaks (e.g., Q4 construction season, Chinese New Year import surge); (b) review vendor appointment compliance trends from W44 — initiate conversation with chronic offenders through Buyer; (c) evaluate dock door configuration changes (e.g., convert standard door to heavy-duty if yard receipts increasing); (d) assess need for overflow staging area expansion; (e) feed capacity planning recommendations into annual DC capacity review and capex planning per W21 | DC Manager | VP Supply Chain | 1 hour/month |

### System Touchpoints (W585 — DC Dock Scheduling & Appointment Management)
- Dock appointment request intake module with PO/container linkage (W585.1)
- Dock door calendar with configurable time slots, door capability categories, and capacity management (W585.2)
- Automated carrier/vendor notification: email, SMS, vendor portal update (W585.3)
- Gate check-in module with appointment verification, walk-in handling, and status update (W585.4)
- Real-time dock door status dashboard with utilization rate, time-over alerts, and availability (W585.5)
- No-show detection, release, and escalation with vendor scorecard feed (W585.6)
- Appointment compliance metrics: on-time rate, dock turn time, utilization rate, walk-in rate, slot adherence (W585.7)
- Monthly dock capacity analytics with peak/valley identification (W585.8)
- Integration with W3 (receiving — appointment feeds gate check, dock door feeds receiving flow), W3C (inbound scheduling — extended appointment management), W106 (dispatch — outbound dock slots, loading schedule), W52 (fleet — owned vehicle scheduling, carrier notification), W44 (vendor scorecard — appointment compliance, no-show rate), W242 (3PL review — carrier appointment compliance), W584 (daily operations — pace check dashboard, labor allocation to dock), W586 (KPI dashboard — dock utilization KPI feed), W57 (promotions — priority pre-positioning appointments), W66 (inter-island — container scheduling)

### Pain Points / Risks
- **Peak morning congestion (8:00–10:00 AM) is structurally unavoidable**: Philippine vendor logistics patterns concentrate domestic deliveries in the morning to avoid Metro Manila afternoon traffic; even with appointment scheduling, 15–20 trucks arriving in a 2-hour window at a DC with 8–12 dock doors creates inevitable queuing; the holding area must accommodate 5–8 waiting trucks during peak.
- **Import container scheduling unpredictability**: port release timing from Manila South Harbor or Batangas port can shift by hours or days due to Customs inspection, port congestion, or berthing delays; a container appointment booked for Tuesday 10:00 AM may need to be rescheduled to Wednesday 4:00 PM with 2 hours' notice, disrupting the carefully planned dock calendar.
- **3PL carrier appointment compliance is weaker than owned-fleet compliance**: 3PL drivers service multiple clients and may prioritize deliveries based on their own route optimization rather than BuildRight's dock schedule; with 80% of fleet operations being 3PL, appointment adherence for outbound dispatch is harder to enforce.
- **Unscheduled walk-ins from local Davao and Cebu vendors**: provincial vendors in Mindanao and Visayas often deliver without advance appointment, relying on personal relationships with DC Receiving Clerks rather than the formal scheduling system; cultural expectations of flexibility conflict with systematic scheduling, creating tension between operational discipline and vendor relationship management.
- **Dock turn time variability is high for catch-weight and oversized items**: lumber, steel rebar, and cement deliveries at yard dock doors take 45–90 minutes to unload and measure (W3B catch-weight process), vs. 20–30 minutes for standard palletized merchandise; the 2-hour default time slot is insufficient for oversized loads, causing appointment overrun and cascading delays to subsequent appointments at the same door.

### Staffing Implication
- **DC Receiving Supervisor**: adds ~30 min/day for appointment review and dock door assignment (steps 1–2, 6), plus 30 min/week for compliance reporting review (step 7). Absorbed within existing DC Receiving Supervisor role — this formalizes scheduling duties already performed informally per W3C.
- **Gate Guard**: adds ~5 min per truck for structured check-in vs. current informal gate process; with ~70 trucks/day, this is ~6 hours/day across 2 guards. Absorbed within existing gate security staffing.
- **DC Manager**: adds 1 hour/month for monthly dock capacity planning review (step 8). Absorbed.
- **No incremental headcount** — the system-automated scheduling, notifications, and compliance tracking reduce manual coordination effort, offsetting the additional structure.

---

## W586. DC Daily KPI Dashboard & Performance Tracking

| Field | Detail |
|---|---|
| **Trigger** | Automated overnight KPI calculation cycle; DC Manager morning review |
| **Frequency** | Daily per DC (overnight calculation, morning review); weekly trend analysis; monthly executive summary |
| **Volume** | 4 DCs; ~20 KPIs tracked per DC across 6 operational categories |
| **Owner** | DC Manager |
| **Participants** | DC Shift Supervisors, DC Receiving Supervisor, DC Dispatch Supervisor, VP Supply Chain, Supply Planning Manager |

### Background

With 4 DCs processing ~6,000 receipts/month and ~3,600 outbound dispatches/month, DC-level operational performance visibility is critical for the VP Supply Chain to identify issues early, benchmark DCs against each other, and drive continuous improvement. Currently, DC performance data is fragmented across WMS (receiving and putaway metrics), TMS (dispatch and delivery metrics), ERP (inventory accuracy and financial metrics), and timekeeping (labor metrics). This workflow establishes a unified daily KPI dashboard that consolidates data from all systems into a single view per DC, with automated exception alerting and corrective action tracking.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Automated overnight KPI calculation** (10:30 PM — after Night Shift B closes): System extracts transaction data from WMS, TMS, ERP, and timekeeping systems for the completed operational day (6:00 AM current day through 10:00 PM current day) and calculates the following KPIs per DC: **(A) Receiving Throughput**: (i) total receipts completed vs. planned (target: ≥ 95% of scheduled appointments), (ii) average receiving time per receipt — gate-to-GR posting (target: ≤ 2 hours), (iii) receiving accuracy — % of GRs with zero discrepancies (target: ≥ 98%), (iv) quality inspection pass rate (target: ≥ 95% per W3 quality standards); **(B) Putaway Performance**: (v) total pallets put away vs. received (target: 100% same-day putaway), (vi) putaway backlog at EOD — pallet count (target: 0), (vii) average putaway time per pallet (target: ≤ 20 min from GR to bin-scan confirmation); **(C) Picking Productivity**: (viii) lines picked per picker-hour (target: ≥ 25 lines/picker-hour for standard merchandise, ≥ 15 for bulky/heavy items), (ix) pick accuracy — % of picks with zero errors (target: ≥ 99.5%), (x) pick wave on-time completion % (target: ≥ 95% of waves completed within scheduled window); **(D) Shipping & Dispatch**: (xi) outbound loads dispatched vs. planned (target: ≥ 95%), (xii) on-time departure rate (target: ≥ 95% depart within 30 min of scheduled time), (xiii) truck utilization rate — loaded volume ÷ capacity (target: ≥ 75%), (xiv) on-time delivery rate from prior-day POD returns (target: ≥ 90%); **(E) Labor Utilization**: (xv) actual labor-hours vs. planned (target: ± 5%), (xvi) overtime hours as % of total labor-hours (target: ≤ 8%), (xvii) labor-hours per receipt processed, (xviii) labor-hours per dispatch processed; **(F) Accuracy & Quality**: (xix) cycle count accuracy — if cycle count conducted today per W6 (target: ≥ 99.5%), (xx) shipping accuracy — % of outbound orders with zero errors (correct items, correct quantities, correct store) (target: ≥ 99%) | System | — | Automated (30 min batch) |
| 2 | **Morning dashboard generation** (5:30 AM): System generates DC daily KPI dashboard with: (a) **Summary scorecard**: green/amber/red status per KPI category (green = within target, amber = within 10% of target threshold, red = below target threshold by > 10%); (b) **DC comparison view**: side-by-side KPI comparison across all 4 DCs (Davao, Cebu, Calamba, Clark) to enable benchmarking; (c) **7-day trend sparklines**: mini-trend charts for each KPI showing daily values for the past week; (d) **Exception list**: KPIs in red status with automatic root-cause suggestions based on correlation analysis (e.g., if receiving throughput is red and dock utilization is red, system suggests "dock congestion — review W585 appointment schedule"); (e) **Corrective action tracker**: open corrective actions from prior days with due-date status; dashboard is accessible via browser on DC Manager's desktop and on wall-mounted displays in each DC's operations office | System | — | Automated |
| 3 | **DC Manager morning review** (8:00 AM): DC Manager opens daily KPI dashboard and reviews: (a) overall DC performance — is the summary scorecard predominantly green?; (b) any red-status KPIs — drill down to underlying transaction data to understand root cause; (c) 7-day trends — are any KPIs showing declining trajectory even if still green?; (d) DC comparison — is this DC underperforming vs. other DCs on any metric?; (e) open corrective actions — are prior corrective actions completed or overdue?; DC Manager documents review notes and action items in dashboard | DC Manager | VP Supply Chain | 15–20 min/day |
| 4 | **Exception flagging and escalation**: System automatically flags exceptions based on configurable rules: (a) **Single-day red alert**: any KPI in red status triggers automated email to DC Manager and DC Shift Supervisor with exception detail and suggested root cause; (b) **3-day amber trend**: any KPI in amber status for 3 consecutive days escalates to DC Manager for investigation; (c) **7-day declining trend**: any KPI showing consistent daily decline over 7 days (even if still green) triggers trend alert to DC Manager and VP Supply Chain; (d) **Cross-DC outlier**: any DC that is > 15% below the 4-DC average on any KPI triggers outlier alert to VP Supply Chain; DC Manager must acknowledge each exception within 4 hours (weekdays) or by next business day (weekends) | System / DC Manager | VP Supply Chain | 5–10 min/day for acknowledgment |
| 5 | **Corrective action assignment**: For each acknowledged exception, DC Manager assigns corrective action: (a) assigns responsible person (Shift Supervisor, Receiving Supervisor, Dispatch Supervisor, or specific staff member), (b) sets target resolution date (default: 5 business days for operational issues, 10 business days for systemic issues), (c) describes corrective action plan, (d) system tracks corrective action through lifecycle: Assigned → In Progress → Completed → Verified; (e) if corrective action not completed by target date: system escalates to VP Supply Chain; (f) completed corrective actions are reviewed for effectiveness in the next weekly trend review (step 7) — did the KPI improve? | DC Manager | VP Supply Chain | 10 min/exception; ~2–3 exceptions/day |
| 6 | **VP Supply Chain multi-DC dashboard review** (9:00 AM): VP Supply Chain reviews consolidated dashboard across all 4 DCs: (a) 4-DC summary scorecard with side-by-side comparison; (b) cross-DC outlier alerts; (c) open corrective action status across DCs; (d) identifies systemic issues affecting multiple DCs (e.g., if all 4 DCs show declining truck utilization, the issue is likely in load planning or fleet management rather than individual DC operations); (e) escalates systemic issues to COO with root-cause analysis and proposed resolution | VP Supply Chain | COO | 20 min/day |
| 7 | **Weekly trend review** (Monday 10:00 AM — part of W584 weekly operations review): DC Manager analyzes 7-day KPI trends: (a) calculate weekly averages for each KPI and compare to prior week; (b) identify KPIs with sustained improvement or decline over 4+ weeks; (c) review effectiveness of corrective actions completed in the past week — did the targeted KPI improve?; (d) identify emerging capacity constraints (e.g., if receiving throughput is steady but inbound volume is increasing, the DC is approaching a capacity ceiling); (e) prepare 1-page weekly DC performance summary for VP Supply Chain with top 3 wins, top 3 concerns, and action plan for the coming week | DC Manager | VP Supply Chain | 30 min/week (in addition to W584 weekly review) |
| 8 | **Monthly executive DC performance report**: System generates monthly DC performance report for VP Supply Chain and COO: (a) monthly KPI averages per DC with month-over-month and year-over-year comparison; (b) 4-DC benchmarking ranking per KPI category; (c) top 10 corrective actions closed with effectiveness assessment; (d) open corrective actions aging report; (e) capacity utilization trend — is the DC approaching physical or labor capacity limits?; (f) cost per unit processed trend (total DC operating cost / units received + dispatched); (g) recommendations for capex investment (dock expansion, automation, equipment) or process changes based on performance trends; report auto-distributed to VP Supply Chain, COO, and CFO | System / DC Manager | VP Supply Chain | Automated generation + 1 hour/month DC Manager review and commentary |

**Total time per DC per day**: ~35–50 min of DC Manager time on KPI review and corrective action management (step 3: 15–20 min + step 4: 5–10 min + step 5: 10–15 min). VP Supply Chain adds ~20 min/day for multi-DC review. Weekly: DC Manager adds 30 min/week for trend analysis. Monthly: DC Manager adds 1 hour/month for executive report review.

### System Touchpoints (W586 — DC Daily KPI Dashboard & Performance Tracking)
- Overnight data extraction from WMS (receiving, putaway, picking transactions), TMS (dispatch, delivery, POD data), ERP (inventory, PO data), and timekeeping (labor-hours, overtime) (W586.1)
- Automated KPI calculation engine with configurable target thresholds per KPI per DC (W586.1)
- Dashboard rendering with summary scorecard (green/amber/red), 4-DC comparison view, 7-day trend sparklines, exception list, and corrective action tracker (W586.2)
- Exception rule engine with single-day red, 3-day amber, 7-day decline, and cross-DC outlier rules (W586.4)
- Corrective action lifecycle tracking: Assigned → In Progress → Completed → Verified, with escalation triggers (W586.5)
- Multi-DC consolidated dashboard for VP Supply Chain (W586.6)
- Weekly trend analytics with corrective action effectiveness assessment (W586.7)
- Monthly executive report generation with KPI trends, benchmarking, capacity analysis, and cost per unit (W586.8)
- Integration with W584 (daily operations — KPI data source from shift management activities), W3 (receiving — receiving throughput, accuracy, quality pass rate), W106 (dispatch — departure rate, utilization, delivery on-time rate), W585 (dock scheduling — dock utilization, appointment compliance), W4 (picking — pick productivity, accuracy, wave completion), W6 (cycle counting — count accuracy), W44 (vendor scorecard — quality data cross-reference), W52 (fleet — truck utilization, delivery performance), W242 (3PL review — carrier performance data), W21 (capex — capacity investment recommendations from monthly report)

### Pain Points / Risks
- **Data latency across systems**: WMS transactions (receiving, putaway, picking) post in near-real-time, but TMS delivery confirmation (POD returns from drivers) lags by 1–2 days because drivers submit physical delivery receipts upon return to DC; this means the on-time delivery rate KPI is always 1–2 days behind, reducing its value as a same-day management tool.
- **KPI target thresholds require DC-specific calibration**: Clark DC (serving Northern/Central Luzon stores with longer delivery routes) will have lower truck utilization than Calamba DC (serving Metro Manila and Southern Luzon with shorter, denser routes); applying uniform targets across all 4 DCs creates misleading red/amber status for DCs with structurally different operating conditions; mitigated by configurable per-DC targets but requires initial calibration effort.
- **Corrective action completion does not guarantee KPI improvement**: many KPIs are influenced by factors outside DC Manager control (e.g., receiving throughput depends on vendor on-time delivery which feeds W44; picking productivity depends on order profile complexity from store replenishment planning); corrective actions assigned to DC staff may not address the true root cause if the root cause is external.
- **Dashboard fatigue and alert desensitization**: with ~20 KPIs tracked per DC and automated exception rules, DC Managers may receive 3–5 exception alerts per day; over time, the alerts may be acknowledged without genuine investigation, reducing the system's effectiveness as an early warning mechanism.
- **4-DC benchmarking can create unhealthy competition**: public side-by-side KPI comparison may incentivize DC Managers to game metrics (e.g., rushing receiving to improve throughput at the expense of accuracy) rather than driving genuine operational improvement; mitigated by pairing throughput KPIs with accuracy/quality KPIs in the same dashboard view.

### Staffing Implication
- **DC Manager** (1 per DC): adds ~35–50 min/day for dashboard review, exception handling, and corrective action management (steps 3–5), plus 30 min/week for trend analysis (step 7), plus 1 hour/month for executive report review (step 8). This is a core management responsibility absorbed within the existing DC Manager role — formalizes performance management that is currently ad hoc.
- **VP Supply Chain**: adds ~20 min/day for multi-DC dashboard review (step 6). Absorbed.
- **IT/Business Intelligence**: initial dashboard development and KPI calculation engine build (~40–80 hours one-time); ongoing maintenance (~4–8 hours/month for threshold calibration, report modifications, data quality issue resolution). This is within planned BI/analytics capabilities.
- **No incremental DC headcount** — the dashboard automates data collection and calculation that would otherwise require manual spreadsheet compilation by DC administrative staff, saving ~3–4 hours/week per DC of manual reporting effort.

---

## W648. DC Cycle Counting & Inventory Accuracy Program

| Field | Detail |
|---|---|
| **Trigger** | Daily per DC zone schedule; triggered by variance alert |
| **Frequency** | Daily zone counting (A-items monthly, B-items quarterly, C-items semi-annually); full annual wall-to-wall per W42 |
| **Volume** | ~7,000 SKUs per DC; ~700 SKUs counted daily per DC; ~2,800 counts/day across 4 DCs |
| **Owner** | DC Inventory Supervisor |
| **Participants** | Cycle Counter, DC Manager, Inventory Planner, LP Analyst (variance investigation) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates daily cycle count task list by zone based on ABC classification frequency schedule and variance-triggered recounts; assigns to Cycle Counter via RF device | System | DC Inventory Supervisor | Automated |
| 2 | Cycle Counter performs physical count at system-directed bin locations using RF scanner; records count quantity; system flags variance against book quantity | Cycle Counter | DC Inventory Supervisor | 4–6 hours/day |
| 3 | For items within tolerance (A-items: ±0.5%, B-items: ±1%, C-items: ±2%): system auto-adjusts book quantity; adjustment posted with cycle count reference | System | DC Inventory Supervisor | Automated |
| 4 | For items outside tolerance: system generates recount task; Cycle Counter performs blind recount (no prior count visible) | Cycle Counter | DC Inventory Supervisor | 30 min/recount |
| 5 | If recount confirms variance: DC Inventory Supervisor investigates root cause (receiving error, miscount, misplacement, picking error, system error, theft); classifies root cause in system | DC Inventory Supervisor | DC Manager | 15 min/item |
| 6 | DC Inventory Supervisor submits adjustment for approval per threshold: DC Manager for adjustments < PHP 50,000; VP Supply Chain for adjustments PHP 50,000–500,000; CFO for adjustments > PHP 500,000 | DC Inventory Supervisor | DC Manager | Varies by threshold |
| 7 | DC Manager reviews daily cycle count accuracy rate; targets ≥ 99.5% accuracy for A-items, ≥ 98% for B-items, ≥ 95% for C-items; investigates recurring variance locations | DC Manager | VP Supply Chain | 30 min/day |
| 8 | Weekly: DC Inventory Supervisor produces cycle count accuracy report feeding DC daily KPI dashboard (W586) and variance investigation queue | DC Inventory Supervisor | DC Manager | 1 hour/week |

### System Touchpoints
- WMS cycle count module, RF devices, inventory management module, approval workflow, DC KPI dashboard (W586)

### Time Estimate
- Daily: 4–6 hours counting + 1 hour investigation; weekly: 1 hour reporting

### Pain Points / Risks
- Counting accuracy compromised by improperly labeled bins; catch-weight items difficult to count precisely; high-velocity items (cement, lumber) require yard counts in weather-exposed conditions; recount fatigue reducing accuracy in afternoon counts

### Staffing Implication
- **Cycle Counter** (2 per DC shift): dedicated counting role; ~6 hours/day on physical counting and recount execution across 4 DCs = 8 FTE minimum (2 per DC, single shift). This is a dedicated role.
- **DC Inventory Supervisor**: ~1 hour/day on variance investigation + 1 hour/week reporting. Absorbed within existing role.
- **DC Manager**: ~30 min/day on accuracy review and approval. Absorbed within existing role.

---

## W649. DC Safety Operations & Compliance

| Field | Detail |
|---|---|
| **Trigger** | Daily safety operations cadence; triggered by incident or near-miss |
| **Frequency** | Daily safety checks; weekly safety meeting; monthly safety audit; annual comprehensive review |
| **Volume** | 4 DCs × daily operations |
| **Owner** | DC Safety Officer |
| **Participants** | DC Manager, Forklift Operators, Safety Committee Members, DOLE-accredited Safety Practitioner |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Daily: DC Safety Officer conducts pre-shift safety walkthrough: forklift pedestrian zone barriers intact, emergency exits clear, fire extinguisher accessibility verified, spill kit availability in hazmat area, PPE compliance check at entry point, dock leveler safety interlocks functional | DC Safety Officer | DC Manager | 30 min/shift |
| 2 | Daily: Forklift operator pre-use inspection checklist (fluid levels, tire condition, horn, lights, seat belt, forks, overhead guard); records on mobile app; out-of-service vehicles tagged and reported | Forklift Operator | DC Safety Officer | 10 min/vehicle |
| 3 | Weekly: DC Safety Officer conducts safety meeting with shift team: reviews near-miss reports, reinforces one safety topic (manual handling, forklift safety, hazmat, dock safety), shares industry incident lessons | DC Safety Officer | DC Manager | 30 min/week |
| 4 | Monthly: DC Safety Officer conducts formal safety audit: fire suppression system test, emergency lighting test, first aid kit replenishment, eyewash station verification, electrical panel clearance check, racking structural integrity visual inspection, housekeeping (5S) assessment | DC Safety Officer | DC Manager | 4 hours/month |
| 5 | For incidents and near-misses: DC Safety Officer completes incident report with root cause analysis (5-Why method); implements immediate corrective action; submits to DC Manager and Safety Committee for review; tracks corrective action to completion | DC Safety Officer | DC Manager | 1–2 hours/incident |
| 6 | Quarterly: DOLE-accredited Safety Practitioner reviews DC safety program; verifies compliance with DOLE OSH Standards; provides recommendations; DC Manager implements | Safety Practitioner | DC Manager | 1 day/quarter |
| 7 | Annual: DC Safety Officer coordinates forklift operator recertification, fire drill execution, emergency evacuation drill, and comprehensive safety training refresh for all DC personnel | DC Safety Officer | DC Manager | 2 days/year |

### System Touchpoints
- Safety management module, incident reporting system, forklift inspection mobile app, training module (certification tracking)

### Time Estimate
- Daily: 40 min; weekly: 30 min meeting + 30 min prep; monthly: 4 hours audit; quarterly: 1 day

### Pain Points / Risks
- High worker turnover requiring continuous safety retraining; forklift-pedestrian interaction risk in busy DCs; hazmat area safety compliance with DENR requirements; seasonal temporary workers (W555) with minimal safety training; racking damage from forklift strikes creating structural collapse risk

### Staffing Implication
- **DC Safety Officer** (1 per DC): ~40 min/day on walkthroughs, ~1 hour/week on safety meetings, ~4 hours/month on audits, ~2 days/year on annual exercises. This is a dedicated safety role per DC (4 FTE total), typically shared with or reporting to the DC Manager.
- **Forklift Operators**: ~10 min/vehicle/day on pre-use inspections. Absorbed within existing role as part of standard operating procedure.

---

## W650. Warehouse Equipment Preventive Maintenance

| Field | Detail |
|---|---|
| **Trigger** | Maintenance schedule trigger; triggered by equipment failure or inspection finding |
| **Frequency** | Weekly inspection; monthly PM for forklifts and reach stackers; quarterly PM for conveyors and dock levelers; annual overhaul |
| **Volume** | ~20–30 forklifts/reach stackers per DC × 4 DCs = ~80–120 units; ~40 dock levelers; ~200 RF devices; misc. equipment |
| **Owner** | DC Maintenance Supervisor |
| **Participants** | Equipment Technician, DC Manager, Equipment Vendor Service Engineer, Finance Analyst (capex) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System generates PM work orders based on equipment maintenance schedule (manufacturer-recommended intervals + usage hours from telematics); assigns to Equipment Technician | System | DC Maintenance Supervisor | Automated |
| 2 | Equipment Technician executes PM per equipment-specific checklist: forklifts (engine/motor, hydraulic system, mast/chain, brakes, steering, tires, battery/charging), reach stackers (hydraulics, spreader, steering), dock levelers (hydraulic cylinder, lip extension, safety legs, weather seal), RF devices (battery, scanner, screen, firmware update), barcode printers (print head cleaning, label sensor, calibration), stretch-wrap machines (tension adjustment, film carriage, turntable) | Equipment Technician | DC Maintenance Supervisor | 1–2 hours/unit |
| 3 | Equipment Technician records PM completion in system: checklist results, parts consumed, hours spent, any findings requiring follow-up repair; system updates next PM due date based on hours/interval | Equipment Technician | DC Maintenance Supervisor | 15 min/unit |
| 4 | For equipment requiring repair beyond PM scope: Equipment Technician creates repair work order with severity (critical: equipment out of service, major: degraded but functional, minor: non-urgent); for critical repairs, DC Maintenance Supervisor authorizes vendor service call | Equipment Technician | DC Maintenance Supervisor | 30 min |
| 5 | For critical equipment failures during operations: DC Maintenance Supervisor activates backup equipment plan (rental forklift from vendor pool, manual pallet jack substitution, manual dock operations); communicates impact to DC Manager for labor reallocation | DC Maintenance Supervisor | DC Manager | 1 hour |
| 6 | Monthly: DC Maintenance Supervisor reviews equipment uptime report (target: ≥ 95% for forklifts and reach stackers); analyzes MTBF and MTTR trends; identifies units approaching end-of-life for replacement planning | DC Maintenance Supervisor | DC Manager | 2 hours/month |
| 7 | Quarterly: Finance Analyst reviews equipment maintenance costs vs. depreciation schedule; recommends repair-vs-replace decisions for units with excessive maintenance cost per W39 | Finance Analyst | Finance Manager | 1 day/quarter |

### System Touchpoints
- Equipment maintenance module (EAM), telematics (W199 for forklifts), parts inventory, vendor service portal, GL (maintenance cost posting)

### Time Estimate
- Weekly: 4–8 hours per DC; monthly PM: 1–2 days per DC; quarterly review: 1 day

### Pain Points / Risks
- Equipment aging in high-utilization DC operations (multi-shift, 6 days/week); spare parts availability delays from Philippine equipment vendors; rental equipment quality variability; equipment breakdown during peak season (Christmas) with limited vendor service availability; unauthorized operator modifications compromising safety

### Staffing Implication
- **Equipment Technician** (2–3 per DC): dedicated maintenance role executing PM and repairs. ~6–8 hours/day per DC. This is a dedicated maintenance team per DC (8–12 FTE total across 4 DCs).
- **DC Maintenance Supervisor** (1 per DC): ~2 hours/month on reporting + ad hoc vendor coordination. Absorbed within existing supervisory role.
- **Finance Analyst**: ~1 day/quarter on equipment cost analysis. Absorbed within existing Finance role.

---

## W651. Reverse Logistics Processing (Customer/Store Returns at DC)

| Field | Detail |
|---|---|
| **Trigger** | Store return shipment received at DC; ecommerce return received at DC |
| **Frequency** | ~2,000–3,000 return items/month across 4 DCs |
| **Volume** | ~50–75 return items/DC/day |
| **Owner** | DC Returns Processor |
| **Participants** | Quality Inspector, DC Inventory Supervisor, Vendor Relations Coordinator, LP Analyst |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | DC Returns Processor receives return shipment from store or ecommerce carrier; scans return authorization (RA) number; verifies shipment matches RA manifest (item, quantity, condition) | DC Returns Processor | DC Inventory Supervisor | 15 min/shipment |
| 2 | Quality Inspector inspects each returned item against return reason code and item condition: Grade A (sealed/original packaging, undamaged — restock to saleable inventory), Grade B (opened, minor cosmetic damage, complete accessories — eligible for discount bin or open-box sale per W549), Grade C (defective, damaged, missing parts — vendor RTV per W88, repair, or destroy), Grade D (safety hazard, contamination — immediate quarantine and destroy) | Quality Inspector | DC Inventory Supervisor | 5 min/item |
| 3 | DC Returns Processor updates system with inspection grade; system routes item to appropriate disposition: Grade A → saleable putaway (W3), Grade B → discount staging area, Grade C → RTV staging (W88) or repair queue, Grade D → quarantine for destruction | DC Returns Processor | DC Inventory Supervisor | 3 min/item |
| 4 | For Grade C vendor-caused defects: Vendor Relations Coordinator initiates vendor claim with evidence (photos, defect description, original GR data); tracks vendor credit receipt per W88 SLA | Vendor Relations Coordinator | DC Inventory Supervisor | 15 min/claim |
| 5 | For LP-flagged returns (high-value items, serial returner items per W605, patterns suggesting return fraud): DC Returns Processor sets aside for LP Analyst investigation before disposition | DC Returns Processor | LP Analyst | As flagged |
| 6 | Weekly: DC Inventory Supervisor produces returns analytics: return rate by category and store, grade distribution, vendor defect rate, processing cycle time, recovery rate (value recovered ÷ value returned) | DC Inventory Supervisor | DC Manager | 2 hours/week |
| 7 | Monthly: DC Manager reviews return trend data with Merchandising (W102) and Supply Chain (W31); identifies systemic quality issues for vendor CAPA (W110) and assortment review (W1) | DC Manager | VP Supply Chain | 1 hour/month |

### System Touchpoints
- WMS returns module, quality inspection module, inventory status management, RTV module (W88), LP analytics, vendor claim system

### Time Estimate
- Daily: 4–6 hours processing; weekly: 2 hours reporting; monthly: 1 hour review

### Pain Points / Risks
- High volume during post-holiday return season (January); subjective grading between Grade A and Grade B leading to inconsistency; vendor resistance to accepting RTV claims; return processing creating bottleneck in DC receiving area; seasonal items returned after season close with no resale opportunity

### Staffing Implication
- **DC Returns Processor** (1 per DC): ~4–6 hours/day on return processing. Dedicated role within DC operations (4 FTE total).
- **Quality Inspector**: shared with receiving quality function; ~2–3 hours/day on return inspection. Absorbed within existing receiving quality role.
- **DC Inventory Supervisor**: ~2 hours/week on returns reporting. Absorbed within existing role.

---

## W652. Seasonal Warehouse Surge Planning & Execution

| Field | Detail |
|---|---|
| **Trigger** | Seasonal demand forecast (W32); triggered 8–12 weeks before peak season |
| **Frequency** | 4 major seasons/year: Christmas (Sep–Dec), Summer (Mar–May), Back-to-School (May–Jun), Rainy Season (Jun–Aug); plus 6 bi-monthly sale events |
| **Volume** | 2–3× normal DC volume during Christmas peak; 1.5–2× during other peaks |
| **Owner** | DC Manager |
| **Participants** | VP Supply Chain, HR Manager (temporary labor), DC Inventory Supervisor, Category Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | T-12 weeks: VP Supply Chain provides seasonal volume forecast per DC (units, lines, orders); DC Manager compares forecast against current DC capacity (receiving docks, putaway zones, pick faces, shipping docks, labor) | DC Manager | VP Supply Chain | 2 days |
| 2 | T-10 weeks: DC Manager develops surge plan: temporary labor requirement (headcount, duration, shift pattern — extended hours or additional shift), equipment rental plan (forklifts, reach stackers, RF devices), overflow staging area activation plan, seasonal SKU forward-pick zone re-slotting | DC Manager | VP Supply Chain | 3 days |
| 3 | T-8 weeks: HR Manager initiates seasonal staffing process (W555): temporary worker recruitment, abbreviated onboarding (safety + basic WMS operation), schedule alignment with surge plan | HR Manager | DC Manager | Per W555 |
| 4 | T-6 weeks: DC Manager executes seasonal re-slotting: high-velocity seasonal SKUs moved to forward-pick zones; reserve storage consolidated to create overflow receiving space; seasonal promotional displays and bulk staging areas designated | DC Manager | VP Supply Chain | 1 week |
| 5 | T-4 weeks: Equipment rental delivery and commissioning; temporary worker first shift with supervised onboarding; extended operating hours commence; overflow area activated and stocked | DC Manager | VP Supply Chain | 1 week |
| 6 | During peak: DC Manager monitors daily volume vs. forecast; adjusts labor allocation daily; activates 3rd shift if volume exceeds 2× normal for 3+ consecutive days; daily stand-up meetings with shift supervisors | DC Manager | VP Supply Chain | 30 min/day |
| 7 | T+2 weeks post-peak: DC Manager executes wind-down: return rental equipment, release temporary workers per W555 offboarding, restore normal slotting, deactivate overflow areas, return to normal operating hours | DC Manager | VP Supply Chain | 1 week |
| 8 | T+4 weeks post-peak: DC Manager produces seasonal surge performance report: volume vs. forecast, labor productivity, overtime cost, equipment utilization, service level maintained, lessons learned for next surge | DC Manager | VP Supply Chain | 2 days |

### System Touchpoints
- Demand planning (W31), WMS (capacity planning, slotting), labor scheduling (W34), DC KPI dashboard (W586), equipment management (W650)

### Time Estimate
- Planning: 5 days; execution monitoring: daily during peak; wind-down: 1 week; post-mortem: 2 days

### Pain Points / Risks
- Seasonal volume forecast underestimation leading to capacity crisis; temporary worker productivity 30–50% lower than permanent staff; rental equipment unfamiliarity causing safety incidents; extended hours causing permanent staff fatigue and turnover; overflow area security and inventory accuracy challenges

### Staffing Implication
- **DC Manager**: ~5 days planning per surge event (4 major + 6 minor = ~20–30 days/year surge planning). Absorbed within existing role but requires dedicated planning time.
- **HR Manager**: seasonal staffing coordination per W555. Absorbed within existing HR role.
- **Temporary workers**: ~20–40 per DC during Christmas peak (80–160 total across 4 DCs); ~10–20 per DC during other peaks. Staffed via W555 seasonal staffing process.
- **No incremental permanent headcount** — surge capacity managed through temporary labor and equipment rental.

---

## W681. DC Quality Control & Vendor Compliance Inspection at Receiving

| Field | Detail |
|---|---|
| **Trigger** | Each inbound delivery at DC receiving dock |
| **Frequency** | Per delivery; ~600-800 inbound deliveries/month across 4 DCs |
| **Volume** | ~150-200 deliveries/DC/month; AQL sampling per PUR-016 on designated categories |
| **Owner** | QC Inspector |
| **Participants** | Receiving Supervisor, DC Operations Manager, Procurement Quality Engineer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Delivery arrives at DC; dock assigned per W585 scheduling; Receiving Supervisor verifies carrier appointment and documentation (delivery receipt, packing list, customs clearance for imports per W464) | Receiving Supervisor | — | 15 min |
| 2 | Receiving Supervisor performs unloading with visual inspection: checks for transit damage (crushed packaging, wet cartons, broken pallets), temperature indicator for sensitive goods per W492, and seal integrity for import containers; segregates suspect items in quarantine zone per W219 | Receiving Supervisor | QC Inspector | 30 min |
| 3 | QC Inspector performs AQL sampling per PUR-016 on designated categories: selects random sample from lot per sampling plan; inspects for product quality (cosmetic defects, dimensional accuracy, finish quality), labeling compliance (barcode readability, required markings per DTI-BPS ICC/SOC per W447), and shelf-life verification for date-sensitive items (paint, adhesives, chemicals) | QC Inspector | — | 30-60 min |
| 4 | QC Inspector records inspection results in quality module: pass, conditional pass (minor issues — accepted with notation), fail (rejected per W110); captures photos of defects | QC Inspector | — | 15 min |
| 5 | For failed inspections: QC Inspector creates quality hold per W219; Procurement Quality Engineer notified; vendor CAPA per W110 initiated; Receiving Supervisor processes partial receipt for accepted quantity | QC Inspector | Procurement Quality Engineer | 1-2 hours |
| 6 | For import shipments: QC Inspector verifies customs documentation completeness per W239, performs landed cost component verification (duty rate applied, freight allocation per FIN-013), and checks product certification compliance per W625 for regulated categories | QC Inspector | — | 30 min |
| 7 | Receiving Supervisor completes goods receipt in ERP for accepted items; system updates inventory with QC status; vendor scorecard per W44 updated with quality data | Receiving Supervisor | — | 15 min |
| 8 | Monthly: DC Operations Manager produces vendor quality report: defect rate by vendor, category, and DC; recurring defect patterns; vendor response time to CAPA | DC Operations Manager | — | 3 hours |
| 9 | Quarterly: Procurement Quality Engineer reviews AQL sampling parameters and inspection criteria per PUR-016; adjusts sampling levels based on vendor quality history | Procurement Quality Engineer | DC Operations Manager | 4 hours |

### System Touchpoints
- WMS receiving module
- Quality inspection module
- AQL sampling engine
- Vendor scorecard (W44)
- CAPA module (W110)
- Quarantine management (W219)

### Time Estimate
- Per delivery: 30-60 min for AQL inspection
- Full-lot inspection (failures): 2-4 hours

### Pain Points / Risks
- Import container inspection time pressure (demurrage clock per W249)
- Paint/chemical quality testing requiring laboratory turnaround
- Inconsistent AQL application across 4 DCs
- Vendor resistance to quality holds

### Staffing Implication
- QC Inspector (1 per DC, 4 total): ~8 hours/day during receiving shifts
- Dedicated role

---

## W784. DC Inventory Slotting Optimization & Periodic Re-Slotting Execution

| Field | Detail |
|---|---|
| **Trigger** | Quarterly slotting review; or significant assortment change per W679; or new DC layout |
| **Frequency** | Quarterly review; semi-annual re-slotting execution |
| **Volume** | 4 DCs × ~35,000 SKUs slotting assessment; ~5,000-10,000 SKU re-slotting moves per execution |
| **Owner** | DC Operations Manager |
| **Participants** | DC Operations Manager, Warehouse Planner, WMS Analyst, Stock Associates |

### Background
Optimal warehouse slotting — assigning each SKU to the most efficient storage location based on pick frequency, size, weight, and compatibility — directly impacts DC labor productivity, pick accuracy, and throughput. With 35,000 active SKUs across 4 DCs handling ~72,000 goods receipts and ~60,000 store replenishment orders annually, even a 5% improvement in pick productivity from better slotting translates to significant cost savings. This workflow manages the periodic analysis and execution of warehouse re-slotting to maintain optimal slot assignments as demand patterns change seasonally.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Slotting analysis data collection**: Warehouse Planner compiles: (a) SKU pick frequency (orders/week from W586 KPI data), (b) order lines per SKU, (c) unit dimensions and weight per W252 item master, (d) current bin/slot locations, (e) zone and aisle layout, (f) seasonal demand shifts per W32 seasonal calendar | Warehouse Planner | DC Ops Manager | 4 hours |
| 2 | **ABC-velocity classification**: System classifies all SKUs: (a) A-velocity: top 20% by pick frequency (golden zone assignment — waist-height, nearest to dispatch), (b) B-velocity: next 30% (standard zone), (c) C-velocity: bottom 50% (remote/upper storage zones), (d) cross-dock candidates: items with > 80% direct-ship rate per W221 | System | — | Automated |
| 3 | **Slotting optimization model**: Warehouse Planner runs slotting optimization: (a) minimize travel distance for pickers (weighted by pick frequency), (b) family grouping (related items stored together — e.g., all tile adhesives near tiles), (c) heavy/bulky items near dock doors, (d) hazmat in compliant zones per W236, (e) high-value items in secured cage per W71, (f) seasonal items in flexible overflow zones | Warehouse Planner | — | 4-8 hours |
| 4 | **Re-slotting proposal review**: DC Operations Manager reviews proposed changes: (a) number of SKU moves required, (b) estimated productivity improvement, (c) execution time and labor required, (d) disruption to ongoing operations, (e) approves, modifies, or defers proposal | DC Ops Manager | VP Supply Chain | 2 hours |
| 5 | **Re-slotting execution**: Approved changes executed during low-volume period (typically weekend night shift): (a) Stock Associates move SKUs to new locations per move list, (b) WMS Analyst updates bin assignments in WMS, (c) barcode labels updated at new locations, (d) verification scan of moved items at new locations | Stock Associates | DC Ops Manager | 8-16 hours per DC |
| 6 | **Post-slotting verification**: (a) WMS Analyst runs location accuracy check: scan 100% of moved items at new locations, (b) DC Ops Manager verifies pick path efficiency: time first 50 pick orders post-slotting vs. pre-slotting baseline, (c) document actual vs. projected productivity improvement | WMS Analyst | DC Ops Manager | 4 hours |
| 7 | **Continuous monitoring**: Monthly: Warehouse Planner monitors: (a) pick rate trends (lines/hour per zone), (b) top 20 SKUs by pick frequency — verify golden zone placement, (c) dead stock locations (SKUs with zero picks in 90 days), (d) slot utilization rate (target: > 85%) | Warehouse Planner | — | 2 hours/month |

### System Touchpoints

- WMS slotting optimization module — velocity analysis and slot assignment engine
- W586 DC daily KPI dashboard — pick productivity data
- W252 item master — SKU dimensions, weight, and attributes
- W297 warehouse location & bin master — bin/slot governance
- W314 planogram template — analogous space planning for DC
- W221 cross-docking operations — cross-dock candidate identification
- W236 hazmat storage compliance — hazmat zone enforcement
- W71 store physical security — high-value cage integration
- W32 seasonal buy planning — seasonal demand pattern input

### Pain Points / Risks

- Execution disruption — re-slotting during operational hours disrupts picking; weekend/night execution reduces but does not eliminate impact
- Incomplete moves — Stock Associates may not complete all moves in one shift; partial re-slotting creates confusion and pick errors
- WMS update accuracy — if physical move and WMS update are not synchronized, pickers are directed to wrong locations; real-time WMS update during move is critical
- Seasonal demand volatility — optimal slotting today may be suboptimal next month as demand shifts; quarterly cadence balances optimization with operational stability
- Change management — pickers develop muscle memory for locations; re-slotting initially slows experienced pickers until they adapt to new layout

### Time Estimate

Analysis: 4-8 hours per DC per quarter. Execution: 8-16 hours per DC per semi-annual event. Monthly monitoring: 2 hours per DC. Total annual: ~80-120 hours per DC.

### Staffing Implication

Absorbed within existing DC Operations Manager, Warehouse Planner, and Stock Associate roles. Semi-annual execution requires additional temporary labor or overtime for move execution. No incremental permanent headcount.

---

## W785. Vendor Returnable Transport Packaging Reconciliation & Settlement

| Field | Detail |
|---|---|
| **Trigger** | Monthly RTP reconciliation cycle; or vendor RTP balance dispute |
| **Frequency** | Monthly reconciliation; quarterly vendor settlement |
| **Volume** | ~12,000-15,000 RTP items (pallets, crates, IBCs) in circulation across 4 DCs |
| **Owner** | DC Operations Manager |
| **Participants** | DC Ops Manager, Receiving Supervisor, AP Accountant, Vendor, 3PL Carrier |

### Background
BuildRight Depot receives goods on returnable transport packaging (RTP) — wooden pallets, plastic crates, intermediate bulk containers (IBCs), and roll cages — from vendors who charge deposits or track ownership. While W270 tracks pallets at a high level, this workflow manages the detailed operational reconciliation of RTP: tracking inbound and outbound RTP movements, reconciling balances per vendor, managing damage and loss, and processing vendor settlements for deposits or rental fees. With ~12,000-15,000 RTP items in circulation and deposit values of PHP 200-1,500 per item, unreconciled RTP represents ~PHP 3-5M in vendor liabilities.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Inbound RTP recording**: At receiving per W3: (a) Receiving Supervisor counts and records all RTP received per delivery: pallet count, crate count, IBC count by vendor, (b) system logs RTP receipt against vendor account, (c) RTP condition assessed: good, damaged, or non-returnable | Receiving Supervisor | — | 5 min/delivery |
| 2 | **Outbound RTP recording**: At dispatch per W106: (a) Receiving Supervisor records RTP returned to vendor (empty pallets/crates on backhaul), (b) system logs RTP return against vendor account, (c) carrier confirms RTP pickup quantity on delivery receipt | Receiving Supervisor | — | 5 min/dispatch |
| 3 | **Inter-DC RTP tracking**: For RTP transferred between DCs per W22: (a) system tracks RTP movement inter-DC, (b) sending DC credits vendor RTP balance, (c) receiving DC debits vendor RTP balance, (d) net vendor balance unchanged | System | — | Automated |
| 4 | **Monthly RTP reconciliation**: DC Operations Manager reconciles per vendor: (a) opening balance + inbound receipts - outbound returns - inter-DC net = closing balance, (b) physical count of RTP at DC (sample count of 20% per month, full count quarterly), (c) variance investigation: missing, damaged, or unrecorded RTP | DC Ops Manager | — | 4 hours/month |
| 5 | **Damage and loss documentation**: For damaged or lost RTP: (a) DC Ops Manager documents damage with photos, (b) classifies cause: carrier damage, DC handling damage, natural wear, unexplained loss, (c) vendor deposit forfeited for DC-caused damage per agreement, (d) carrier claim initiated for carrier-caused damage per W500 | DC Ops Manager | — | 15 min/case |
| 6 | **Quarterly vendor RTP settlement**: AP Accountant processes quarterly settlement: (a) per-vendor RTP balance confirmed with vendor, (b) deposit charges for unreturned/damaged RTP per agreement, (c) vendor credits for excess returns, (d) settlement amount applied to vendor AP balance per W7, (e) vendor statement reconciliation per W100 | AP Accountant | Finance Manager | 2 hours/quarter |
| 7 | **RTP analytics**: Monthly: DC Ops Manager reports: (a) RTP balance by type and vendor, (b) return rate (target: > 95%), (c) damage rate by cause, (d) deposit liability on balance sheet, (e) RTP cost per unit shipped | DC Ops Manager | — | 1 hour/month |

### System Touchpoints

- RTP tracking module — inbound, outbound, and balance management per vendor
- W3 warehouse receiving — RTP receipt recording integration
- W106 DC outbound dispatch — RTP return recording integration
- W22 stock transfers — inter-DC RTP movement tracking
- W270 pallet tracking — high-level pallet management
- W7 AP processing — RTP settlement payment processing
- W100 vendor statement reconciliation — RTP balance on vendor statement
- W500 transfer order damage claim — carrier damage RTP claim

### Pain Points / Risks

- Tracking accuracy — manual RTP counting at receiving/dispatch is error-prone; under-recording inbound or over-recording outbound creates apparent shortages
- Vendor disputes — vendors may claim more RTP returned than DC records show; photographic evidence and signed delivery receipts are essential
- RTP theft — returnable pallets and crates have resale value; loss prevention per W755 applies to RTP as well as merchandise
- Deposit escalation — vendor RTP deposit rates may increase annually; total deposit liability must be monitored and budgeted
- Environmental condition — wooden pallets deteriorate in Philippine tropical climate (humidity, termites); faster depreciation than expected

### Time Estimate

Monthly: reconciliation (4 hours) + analytics (1 hour) = 5 hours per DC. Quarterly: settlement (2 hours). Total: ~28 hours per DC per year.

### Staffing Implication

Absorbed within existing DC Operations Manager and Receiving Supervisor roles. Monthly: ~5 hours per DC. No incremental headcount.

---

## W796. DC Workforce Scheduling, Labor Planning & Productivity Tracking

| Field | Detail |
|---|---|
| **Trigger** | Weekly labor planning cycle; daily shift start; seasonal surge planning per W652 |
| **Frequency** | Weekly scheduling; daily shift execution; monthly productivity review |
| **Volume** | 4 DCs × ~150-250 workers per DC per shift; 2-shift operations (6 AM-2 PM, 2 PM-10 PM); peak seasons require overtime and temporary staffing |
| **Owner** | DC Operations Manager |
| **Participants** | DC Shift Supervisors, HR, Temporary Staffing Agency, VP Supply Chain |

### Background

BuildRight's 4 distribution centers (DC1 Davao, DC2 Cebu, DC3 Laguna, DC4 Clark) each employ 150-250 workers across receiving, putaway, picking, packing, shipping, and value-added services. Labor is the largest controllable cost at DCs (40-50% of DC operating cost). Seasonal demand (ber months September-December) increases throughput by 30-40%, requiring temporary staffing. Without structured workforce scheduling and productivity tracking, DCs face chronic overtime, labor shortages during peak, idle labor during off-peak, and inability to measure individual and team productivity. This workflow governs DC workforce planning, scheduling, and performance management.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Weekly Labor Plan**: DC Operations Manager develops weekly labor plan based on: (a) expected inbound volume (PO schedule per W2, W2B); (b) expected outbound volume (store replenishment orders per W4, ecommerce orders per W11, W19); (c) special activities (cycle counts per W648, seasonal surge per W652, returns processing per W651); (d) available workforce (permanent staff, approved leaves per W7, scheduled training per W655); (e) temporary staffing needs: request to HR per W555 with required headcount, skill level, and dates | DC Ops Manager | VP Supply Chain | 4-6 hours/week |
| 2 | **Shift Schedule Publication**: DC Shift Supervisor publishes detailed shift assignments: (a) assign workers to functional areas (receiving dock, putaway, picking zones, packing, shipping dock, returns); (b) assign team leads per zone; (c) publish schedule 1 week in advance via ERP and mobile app; (d) manage shift swap requests and approval; (e) ensure minimum staffing per zone per DC safety requirements per W649 | Shift Supervisor | DC Ops Manager | 2-3 hours/week |
| 3 | **Daily Shift Briefing**: At shift start, Shift Supervisor conducts 10-minute briefing: (a) safety reminder per W649; (b) volume targets for the shift (units received, picks, shipments); (c) priority orders (urgent store replenishment, ecommerce SLA-critical per W591); (d) special instructions (hazmat receiving per W236, temperature-sensitive goods per W492); (e) attendance check: verify actual vs. planned headcount; (f) if short-staffed: activate overtime or call temporary workers | Shift Supervisor | — | 10-15 min/day |
| 4 | **Real-Time Productivity Monitoring**: During shift, WMS tracks individual and team productivity: (a) receiving: units received per worker per hour; (b) putaway: locations per hour; (c) picking: lines per hour, units per hour; (d) packing: orders per hour; (e) shipping: shipments loaded per hour; (f) system flags workers below minimum productivity threshold (75% of standard rate) for supervisor coaching; (g) real-time dashboard shows DC throughput vs. daily target | System / Shift Supervisor | DC Ops Manager | Continuous |
| 5 | **Overtime Management**: When daily volume exceeds planned capacity: (a) Shift Supervisor requests overtime approval from DC Ops Manager; (b) system calculates required OT hours based on remaining volume; (c) OT limited to maximum 4 hours/day per DOLE labor standards; (d) weekly OT hours tracked per employee per W561 to prevent fatigue and legal non-compliance; (e) monthly OT cost tracked vs. budget per W489 | Shift Supervisor | DC Ops Manager | Daily as needed |
| 6 | **Temporary Worker Integration**: For seasonal surge per W652: (a) HR provides temporary workers per W555; (b) DC Safety Officer conducts safety orientation per W696 before worker enters DC floor; (c) assign temporary workers to low-skill areas (putaway, packing) with permanent worker supervision; (d) track temporary worker productivity separately; (e) end-of-assignment evaluation shared with HR for future reference | Shift Supervisor / HR | DC Ops Manager | Per W555 cycle |
| 7 | **Monthly Productivity Review**: DC Ops Manager reviews monthly productivity metrics: (a) units per labor hour (UPLH) by function; (b) labor cost per unit processed; (c) overtime hours and cost vs. budget; (d) absenteeism rate; (e) temporary worker productivity vs. permanent; (f) productivity trends by shift and zone; (g) benchmark against BuildRight DC peer group; (h) recommendations for process improvement, equipment investment, or staffing adjustments | DC Ops Manager | VP Supply Chain | 4-6 hours/month |

### System Touchpoints

- WMS labor management module with productivity tracking
- ERP workforce scheduling module integrated with HR per W34
- Time & attendance integration per W5
- WMS real-time productivity dashboard
- Temporary staffing management per W555
- Safety training verification per W655, W696
- Overtime tracking per W561
- Budget integration per W489

### Pain Points / Risks

- **Seasonal labor scarcity**: during ber months (September-December), competing logistics companies and retailers all hire temporary workers; BuildRight may not secure enough temporary staff, forcing expensive overtime on permanent workers
- **Temporary worker productivity**: temporary workers typically achieve 50-70% of permanent worker productivity in the first 2 weeks; training investment on workers who leave after peak season is a sunk cost
- **Fatigue-related safety incidents**: extended overtime during peak season increases risk of workplace accidents per W649; DOLE may investigate if accident rate increases during peak
- **Shift handover information loss**: critical information (incomplete picks, pending receiving issues, equipment problems) lost between shift handovers if not formally documented
- **Inaccurate labor planning**: weekly labor plans based on forecast volume that significantly deviates from actual volume lead to over-staffing (wasted cost) or under-staffing (SLA failures)

### Staffing Implication

- **DC Operations Manager**: ~6-8 hours/week on labor planning and scheduling; absorbed by existing role
- **DC Shift Supervisors**: ~2-3 hours/week on schedule creation and daily briefings; absorbed by existing role
- **No incremental headcount**.

### Time Estimate

- Weekly labor planning: 4-6 hours
- Shift schedule publication: 2-3 hours/week
- Daily shift briefing: 10-15 min/day
- Monthly productivity review: 4-6 hours
- **Ongoing**: ~10-15 hours/week of DC Ops Manager + Shift Supervisor time

---

## W797. DC Security Operations, Perimeter Management & Access Control

| Field | Detail |
|---|---|
| **Trigger** | Daily DC operations; security incident; new vendor/visitor arrival; quarterly security review |
| **Frequency** | 24/7 continuous operations; quarterly security review |
| **Volume** | 4 DCs; ~200-300 personnel movements per DC per day (staff, contractors, drivers, visitors) |
| **Owner** | DC Security Supervisor |
| **Participants** | DC Operations Manager, Security Guard Force, LP team per W466, Local Police/Barangay |

### Background

BuildRight's 4 distribution centers hold inventory valued at PHP 2-4 billion at any given time (estimated 35,000 SKUs × 200 stores worth of replenishment stock). DCs are high-value targets for theft, both internal and external. Philippine DCs face additional risks: typhoon damage, flooding, unauthorized entry during off-hours, and organized theft rings. This workflow governs DC physical security, access control, CCTV management, and incident response.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Access Control Management**: All personnel entering DC must: (a) employees: biometric scan (fingerprint) + ID badge; entry/exit time logged in system; (b) contractors/visitors: register at guard house, present valid ID, receive visitor badge, escorted by BuildRight staff at all times; (c) truck drivers: present delivery appointment per W585, present driver's license and vehicle registration, logged in visitor management system; (d) all bags and personal items inspected at exit per LP policy per W37 | Security Guard / System | DC Security Supervisor | 2-3 min per person |
| 2 | **CCTV Operations**: Security guard monitors CCTV system: (a) 24/7 coverage of all entry/exit points, dock doors, yard areas, high-value zones (power tools, appliances); (b) minimum 30-day recording retention per W207; (c) guard logs all incidents observed on CCTV in shift report; (d) system alerts for motion detection during off-hours in restricted areas; (e) monthly camera health check: verify all cameras operational, recording quality acceptable, no blind spots | Security Guard | DC Security Supervisor | Continuous |
| 3 | **Perimeter Security**: Daily perimeter checks at shift start: (a) verify all fence lines intact; (b) verify gate locks and barriers functional; (c) verify exterior lighting operational (especially loading dock and yard per W3B); (d) verify signage: "No Unauthorized Entry," "CCTV Surveillance," "Private Property"; (e) report any damage or security gaps to DC Security Supervisor for immediate resolution | Security Guard | DC Security Supervisor | 30 min/day |
| 4 | **Off-Hours Security**: During non-operating hours (10 PM-6 AM): (a) minimum 2 guards on duty; (b) hourly perimeter patrol logged in guard tour system; (c) all internal doors locked except guard room; (d) alarm system armed; (e) only authorized personnel (DC Ops Manager, Security Supervisor) can authorize off-hours entry; (f) all off-hours entries logged with reason, person, and time | Security Guard | DC Security Supervisor | Nightly |
| 5 | **Security Incident Response**: If security incident occurs (unauthorized entry, theft detected, alarm trigger): (a) guard responds to incident location; (b) assess situation: intruder, employee theft, false alarm; (c) if intruder: do not confront, observe and record, call local police/Barangay per W471; (d) if employee theft: document evidence per W37 LP procedures, detain if safe to do so, notify DC Ops Manager and LP team per W466; (e) incident report filed within 4 hours with CCTV footage preserved | Security Guard | DC Security Supervisor | Per incident |
| 6 | **Quarterly Security Review**: DC Security Supervisor and LP team conduct quarterly review: (a) review all security incidents for the quarter: theft, unauthorized access, alarm events; (b) review CCTV camera coverage for blind spots; (c) review access log analytics: unusual entry patterns (employees entering during off-hours, visitors in restricted areas); (d) review guard force performance; (e) update security procedures as needed; (f) coordinate with local police/Barangay on security situation in the area | DC Security Supervisor / LP Team | VP Supply Chain | 1 day/quarter |

### System Touchpoints

- Access control system (biometric + badge) integrated with HR employee master per W292
- Visitor management system with ID scanning and escort tracking
- CCTV system with 30-day retention and motion detection alerts
- Guard tour system with checkpoint scanning
- Alarm system with 24/7 monitoring
- Incident reporting module linked to W37 LP and W466 LPAP
- Access log analytics dashboard for anomaly detection

### Pain Points / Risks

- **Internal theft**: DC workers with access to high-value inventory (power tools, appliances) are the primary theft risk; mitigated by bag checks, CCTV, and access zone restrictions
- **Guard force reliability**: outsourced security guards may be underpaid, poorly trained, or susceptible to collusion; regular guard force rotation and quarterly performance review mitigates
- **Off-hours vulnerability**: DCs are most vulnerable during off-hours when minimal staff is present; typhoon-related evacuations may leave DC unattended
- **Truck driver access**: hundreds of delivery and pickup truck drivers access DC grounds daily; each driver is a potential theft risk while on premises
- **Cybersecurity-physical security intersection**: unauthorized physical access to server rooms or network cabinets can compromise IT security; server room access restricted to IT personnel only

### Staffing Implication

- **DC Security Supervisor**: 1 per DC, 4 total; manages guard force, conducts quarterly reviews, coordinates with LP and police; absorbed into existing DC management team
- **Security Guard Force**: outsourced to licensed security agency; minimum 6 guards per DC (2 per shift × 3 shifts); 24 total across 4 DCs
- **No incremental BuildRight headcount** beyond DC Security Supervisors.

### Time Estimate

- Access control: 2-3 min per person × 200-300 persons/DC/day = ~10-15 hours/DC/day (absorbed by guard force)
- Perimeter check: 30 min/day
- Off-hours patrols: 8 hours/night (guard tour)
- Quarterly review: 1 day/quarter per DC
- Incident response: variable, 2-8 hours per incident

---

## W798. DC Building Maintenance, Utility Operations & Facility Condition Monitoring

| Field | Detail |
|---|---|
| **Trigger** | Daily operations; preventive maintenance schedule; facility condition assessment per W700; utility meter reading; weather alert |
| **Frequency** | Daily utility monitoring; weekly preventive maintenance; quarterly facility condition assessment; annual major maintenance |
| **Volume** | 4 DCs totaling 130,000 sqm; ~PHP 15-25M annual maintenance budget across all DCs |
| **Owner** | DC Facilities Manager |
| **Participants** | DC Operations Manager, Maintenance Technicians, Utility Providers, External Contractors, VP Supply Chain, Finance |

### Background

BuildRight's 4 DCs (DC1 Davao 35,000 sqm, DC2 Cebu 30,000 sqm, DC3 Laguna 40,000 sqm, DC4 Clark 25,000 sqm) are large industrial facilities with complex building systems: HVAC (for temperature-sensitive goods per W492), electrical systems (high-capacity for material handling equipment), fire suppression (sprinkler systems for BFP compliance), roofing (critical in Philippine tropical climate), loading dock equipment (levelers, doors), and security systems per W797. Building maintenance directly impacts operational continuity — a roof leak damages inventory, an HVAC failure compromises temperature-sensitive goods, and a loading dock breakdown halts outbound shipments.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Daily Utility Monitoring**: DC Facilities Manager monitors utility consumption: (a) electricity meter readings logged daily (main panel and sub-panels for refrigeration, lighting, office); (b) water consumption logged daily; (c) diesel generator fuel level checked daily; (d) compare daily consumption to baseline; (e) flag any abnormal consumption (>20% above baseline) for investigation; (f) monthly utility cost tracked per W701 | Facilities Manager | DC Ops Manager | 30 min/day |
| 2 | **Weekly Preventive Maintenance**: Maintenance Technicians execute weekly PM tasks per W650: (a) inspect and lubricate material handling equipment (forklifts, reach trucks, pallet jacks); (b) inspect loading dock levelers and dock doors; (c) inspect fire suppression system gauges and valves; (d) inspect electrical panels for abnormal heat or damage; (e) inspect roof drainage channels (critical during rainy season); (f) log all PM activities in maintenance management system | Maintenance Technicians | Facilities Manager | 4-6 hours/week |
| 3 | **Monthly Building Systems Check**: Monthly inspection of major building systems: (a) HVAC: check refrigerant levels, condenser coil cleanliness, thermostat calibration for temperature-sensitive zones per W492; (b) fire alarm: test notification devices, verify panel functionality; (c) emergency lighting: test all emergency lights and exit signs; (d) plumbing: check for leaks, verify backflow preventers; (e) structural: visual inspection for cracks, settlement signs, especially after earthquakes | Facilities Manager | DC Ops Manager | 1 day/month |
| 4 | **Weather Preparedness**: During Philippine typhoon season (June-November): (a) pre-typhoon: inspect roof tie-downs, clear drainage channels, test generators, verify emergency supplies; (b) during typhoon: activate emergency protocol per W330, secure dock doors, protect outdoor inventory per W3B; (c) post-typhoon: inspect for damage (roof, walls, flooding), photograph and document for insurance per W610, prioritize repairs for operational continuity | Facilities Manager / DC Ops Manager | VP Supply Chain | As needed during typhoon season |
| 5 | **Corrective Maintenance**: When equipment or building system fails: (a) DC staff submits maintenance work order via system; (b) Facilities Manager triages: emergency (safety risk or operational stoppage — respond within 2 hours), urgent (operational degradation — respond within 24 hours), routine (non-critical — schedule within 1 week); (c) assign to internal maintenance technician or external contractor; (d) track repair completion and verify resolution; (e) update asset maintenance record per W400 | Facilities Manager | DC Ops Manager | Per incident |
| 6 | **Quarterly Facility Condition Assessment**: Facilities Manager conducts quarterly assessment per W700: (a) structural condition: roof, walls, floors, foundation; (b) building systems: HVAC, electrical, plumbing, fire suppression; (c) site: parking lot, fencing, drainage, landscaping; (d) equipment: forklifts, dock levelers, conveyors; (e) rate each element on condition scale (good, fair, poor, critical); (f) estimate remaining useful life and replacement cost; (g) input to annual CAPEX budget per W21 for major maintenance and replacement | Facilities Manager | VP Supply Chain | 2-3 days/quarter |
| 7 | **Annual Major Maintenance**: Schedule major maintenance during lowest-volume period (typically January-February): (a) roof inspection and repair; (b) HVAC system overhaul; (c) floor resurfacing (high-traffic areas); (d) fire suppression system annual certification per BFP requirements; (e) electrical system thermographic survey; (f) loading dock equipment overhaul; (g) plan and budget per W21 CAPEX process | Facilities Manager | VP Supply Chain | 1-2 weeks/year |

### System Touchpoints

- Building Management System (BMS) for HVAC and environmental monitoring
- Maintenance management module (CMMS) integrated with W650
- Utility monitoring dashboard per W701
- Work order system for corrective maintenance
- Asset management per W400 for equipment lifecycle tracking
- Weather alert integration for typhoon preparedness
- Insurance claims module per W610 for weather damage
- CAPEX budget integration per W21 for major maintenance planning

### Pain Points / Risks

- **Roof leaks during typhoon season**: Philippine typhoons (20+ per year) stress warehouse roofing; undetected roof leaks damage inventory before being discovered; regular inspection is critical but often deferred during peak operational periods
- **Generator failure during brownout**: rotational brownouts are common in Philippine provinces; DC generators must be load-tested monthly to ensure reliability; generator failure during brownout risks temperature-sensitive goods loss per W492
- **Contractor availability for emergency repairs**: specialized contractors (HVAC, fire suppression, roofing) may have 1-2 week backlogs during typhoon season when all buildings need repairs simultaneously
- **Aging infrastructure**: DC1 Davao (if older) may require higher maintenance investment; facility condition assessment drives proactive replacement before failure
- **Utility cost escalation**: Philippine electricity rates are among the highest in Southeast Asia (~PHP 10-12/kWh); utility monitoring identifies energy efficiency opportunities per W692

### Staffing Implication

- **1 DC Facilities Manager**: per DC, 4 total; manages daily utility monitoring, weekly PM coordination, corrective maintenance dispatch, and quarterly assessments; absorbed into existing DC management team
- **2-3 Maintenance Technicians per DC**: 8-12 total across 4 DCs; execute weekly PM, respond to corrective maintenance, support major maintenance; mix of BuildRight employees and contracted technicians
- **External Contractors**: HVAC, fire suppression, and roofing specialists on annual framework agreements; not BuildRight headcount
- **Total incremental**: 4 Facilities Managers + 8-12 Technicians (may partially overlap with existing W650 and W240 roles)

### Time Estimate

- Daily utility monitoring: 30 min/day
- Weekly PM: 4-6 hours/week
- Monthly building systems check: 1 day/month
- Corrective maintenance: variable, ~2-8 hours per incident
- Quarterly facility assessment: 2-3 days/quarter
- Annual major maintenance: 1-2 weeks/year

---

## W836. DC Outbound Load Verification & Pre-Dispatch Quality Check

| Field | Detail |
|---|---|
| **Trigger** | DC outbound dispatch ready per W106; truck loaded and awaiting dispatch |
| **Frequency** | Daily; ~60-80 outbound loads per day across 4 DCs |
| **Volume** | 4 DCs × ~15-20 loads/day = ~60-80 loads/day; ~1,800-2,400 loads/month |
| **Owner** | DC Shipping Supervisor |
| **Participants** | Shipping Supervisor, Picker, Driver, Store Receiving Clerk |

### Background

W106 covers DC outbound dispatch and load planning, and W3 covers warehouse receiving. However, neither covers the final quality gate before a loaded truck leaves the DC — verifying that the physical load matches the dispatch documentation. For a hardware retailer shipping 35,000 SKUs including catch-weight items (lumber, wire), hazardous materials (paint, chemicals per W236), fragile items (tiles, ceramics), and high-value items (power tools, appliances), load verification is critical. Incorrect shipments create a cascade of problems: store stock-outs, customer dissatisfaction, intercompany reconciliation issues per W435, and return logistics per W651. Philippine logistics challenges (rough roads, long inter-island transit, variable truck quality) make load verification even more important as damaged goods in transit are costly.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-verification preparation**: Picker completes order fulfillment per W106: items picked, packed, and staged at dock per W585 dock scheduling | Picker | Shipping Supervisor | Per W106 |
| 2 | **Load verification scan**: Shipping Supervisor verifies loaded items against dispatch order: (a) scan each pallet/case barcode against dispatch manifest; (b) verify item count per SKU matches dispatch quantity; (c) for catch-weight items: verify weight/length per W463 catch-weight processing matches dispatch; (d) verify lot/batch numbers for lot-tracked items per INV-008; (e) verify hazmat items properly segregated and labeled per W236 | Shipping Supervisor | DC Ops Manager | 15-30 min per load |
| 3 | **Load quality check**: (a) verify items secured and braced for transport (lumber strapped, tiles on edge, chemicals upright); (b) verify temperature-sensitive items loaded last per W492; (c) check for mixed-load incompatibilities (chemicals with food-grade items, heavy items on top of fragile); (d) verify truck condition (clean, dry, no leaks, proper temperature for sensitive items) | Shipping Supervisor | DC Ops Manager | 10 min per load |
| 4 | **Documentation verification**: (a) dispatch manifest complete with all items; (b) delivery receipts per store included; (c) hazmat shipping papers if applicable per W699; (d) store transfer orders match loaded items per W4 | Shipping Supervisor | — | 5 min per load |
| 5 | **Exception handling**: (a) if item count discrepancy: reconcile with picking records, adjust dispatch quantity, flag for W648 DC cycle count; (b) if damage found during loading: remove damaged item, process per W91, substitute if possible per W279; (c) if missing item from pick: either (i) short-ship with store notification per W708 or (ii) hold dispatch for completion (SLA-dependent) | Shipping Supervisor / Picker | DC Ops Manager | 15-30 min per exception |
| 6 | **Dispatch authorization**: Shipping Supervisor signs off on verified load: (a) system updates dispatch status to "Verified & Released"; (b) driver signs acceptance of cargo; (c) system triggers W250 supply chain control tower tracking; (d) GPS/telematics activated per W199 | Shipping Supervisor / Driver | DC Ops Manager | 5 min per load |
| 7 | **Post-dispatch reconciliation**: upon store delivery per W109/W666: (a) store scans receipt against dispatch manifest; (b) any discrepancies reported within 24 hours; (c) DC receives discrepancy report for root cause per W514 variance analysis; (d) drives continuous improvement in picking accuracy | Store Receiving Clerk / Shipping Supervisor | DC Ops Manager | Per W109/W666 |
| 8 | **Monthly load accuracy analytics**: (a) load verification pass rate (target: >99.5%); (b) discrepancy types and frequency; (c) average verification time per load; (d) store complaint rate related to shipment accuracy | Shipping Supervisor | DC Ops Manager | 2-3 hours/month |

### System Touchpoints

- W106 DC outbound dispatch for dispatch order and load planning
- W585 dock scheduling for dock assignment and staging
- W463 catch-weight processing for weight/length verification
- W236 hazmat segregation for hazardous material compliance
- W4 store replenishment for transfer order matching
- W250 supply chain control tower for shipment tracking
- W199 fleet telematics for GPS and in-transit monitoring
- W109 store receiving for delivery receipt scanning
- W666 receiving QC for store-side quality verification
- W648 DC cycle count for inventory discrepancy investigation
- W91 damaged goods for damage processing
- W279 substitution for item substitution processing
- W514 variance analysis for discrepancy root cause
- W651 reverse logistics for return shipment processing
- W435 IC SLA billing for intercompany reconciliation
- W699 hazmat transport for hazmat shipping documentation
- W492 temperature-sensitive storage for temperature compliance

### Pain Points / Risks

- **Verification bottleneck during peak dispatch hours**: DCs ship 15-20 loads/day within a 4-hour window; scanning and verifying each load creates a bottleneck that can delay dispatch schedules
- **Catch-weight item verification accuracy**: lumber, wire, and chain sold by length/weight are difficult to verify precisely; weight discrepancies may not be caught until store receiving per W109
- **Driver schedule pressure**: drivers on tight schedules may pressure Shipping Supervisors to skip verification steps or accept incomplete loads to meet departure windows
- **High-volume low-value items**: nails, screws, and fasteners are tedious to count by unit; discrepancy tolerance may allow small variances that accumulate over time
- **Dock congestion**: multiple trucks being loaded and verified simultaneously creates dock congestion, especially during peak morning dispatch hours

### Staffing Implication

1 Shipping Supervisor per DC shift (4 DCs × 2 shifts = 8 supervisors); absorbed into existing DC shipping roles. No incremental headcount beyond existing DC Shipping Supervisor positions.

### Time Estimate

Per load: verification scanning (15-30 min) + quality check (10 min) + documentation (5 min) = ~30-45 min. Daily per DC: ~8-15 hours. Monthly: ~320-600 hours across 4 DCs.
