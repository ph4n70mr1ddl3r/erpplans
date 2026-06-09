# Additional Operational Workflows — Batch 5

> Paint mixing station maintenance, material delivery self-service scheduling, shelf stock rotation for paint/chemicals, vendor ASN reconciliation, tool demo reservation, power tool battery station safety, custom order pricing lifecycle, outdoor garden center weather protection, trade account credit insurance, hazardous material spill kit management, last-mile delivery partner review, multi-entity corporate billing, forklift safety checks, installation warranty registration, scrap metal revenue recognition, project progress payment verification, SDS customer access compliance, consignment physical count, loading dock equipment maintenance, and trade account statement dispute resolution.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain (Cross-Functional Batch)

- [W1003. Store-Level Paint Mixing Station Daily Cleaning, Calibration & Waste Disposal](#w1003-store-level-paint-mixing-station-daily-cleaning-calibration--waste-disposal)
- [W1004. Customer Material Delivery Scheduling & Rescheduling Self-Service Portal](#w1004-customer-material-delivery-scheduling--rescheduling-self-service-portal)
- [W1005. Store-Level Shelf Stock Rotation & Paint/Chemical Expiry Monitoring](#w1005-store-level-shelf-stock-rotation--paintchemical-expiry-monitoring)
- [W1006. Vendor Purchase Order ASN Reconciliation & Discrepancy Resolution](#w1006-vendor-purchase-order-asn-reconciliation--discrepancy-resolution)
- [W1007. Customer Tool & Equipment Demo Reservation & Scheduling Service](#w1007-customer-tool--equipment-demo-reservation--scheduling-service)
- [W1008. Store-Level Power Tool Battery Charging Station Safety & Maintenance](#w1008-store-level-power-tool-battery-charging-station-safety--maintenance)
- [W1009. Customer Custom Order Special Pricing Approval & Quotation Lifecycle](#w1009-customer-custom-order-special-pricing-approval--quotation-lifecycle)
- [W1010. Store-Level Outdoor Garden Center Weather Protection & Seasonal Display Setup](#w1010-store-level-outdoor-garden-center-weather-protection--seasonal-display-setup)
- [W1011. Customer Trade Account Credit Insurance & Bad Debt Protection Processing](#w1011-customer-trade-account-credit-insurance--bad-debt-protection-processing)
- [W1012. Store-Level Hazardous Material Spill Kit Inspection & Restocking](#w1012-store-level-hazardous-material-spill-kit-inspection--restocking)
- [W1013. E-Commerce Last-Mile Delivery Partner Performance Weekly Review](#w1013-e-commerce-last-mile-delivery-partner-performance-weekly-review)
- [W1014. Customer Multi-Entity Billing & Consolidated Invoicing for Corporate Accounts](#w1014-customer-multi-entity-billing--consolidated-invoicing-for-corporate-accounts)
- [W1015. Store-Level Forklift & Heavy Equipment Daily Safety Check & Log](#w1015-store-level-forklift--heavy-equipment-daily-safety-check--log)
- [W1016. Customer Product Installation Warranty Registration & Follow-Up Service](#w1016-customer-product-installation-warranty-registration--follow-up-service)
- [W1017. Store-Level Scrap Metal & Recyclable Material Collection & Revenue Recognition](#w1017-store-level-scrap-metal--recyclable-material-collection--revenue-recognition)
- [W1018. Customer Project Progress Payment Verification & Invoice Matching](#w1018-customer-project-progress-payment-verification--invoice-matching)
- [W1019. Store-Level Construction Material Safety Data Sheet (SDS) Customer Access & Compliance](#w1019-store-level-construction-material-safety-data-sheet-sds-customer-access--compliance)
- [W1020. Vendor Consignment Inventory Physical Count & Periodic Reconciliation](#w1020-vendor-consignment-inventory-physical-count--periodic-reconciliation)
- [W1021. Store-Level Loading Dock Equipment Maintenance & Safety Inspection](#w1021-store-level-loading-dock-equipment-maintenance--safety-inspection)
- [W1022. Customer Trade Account Statement Dispute & Resolution Processing](#w1022-customer-trade-account-statement-dispute--resolution-processing)

---

## W1003. Store-Level Paint Mixing Station Daily Cleaning, Calibration & Waste Disposal

| Field | Detail |
|---|---|
| **Trigger** | Daily scheduled maintenance (morning before store opening) and end-of-day close |
| **Frequency** | Daily (2 cycles per day: pre-opening and post-closing) × 200 stores |
| **Volume** | 1 paint mixing station per store |
| **Owner** | Department Supervisor (Paint & Finishes) |
| **Participants** | Sales Associate (Paint Specialist), Maintenance/Utility Staff, Environmental Compliance Officer (regional) |

### Background

BuildRight Depot operates a custom paint mixing station in every store (Section 3.1 per-store layout: Paint Mixing Station). Each station contains a computerized color-matching spectrophotometer, tint dispensing machine with 12–16 colorant canisters, paint shaker, sample drying cabinet, and associated plumbing/ventilation. Colorant residue builds up in dispensing nozzles and trays after each day's mixing operations (~40–80 custom paint orders per store per day). If not cleaned daily, dried colorant causes inaccurate tint dispensing (leading to customer color-mismatch complaints), nozzle blockages (requiring costly service calls), and cross-contamination between color batches. The spectrophotometer requires daily white-tile calibration to maintain color accuracy within ΔE < 1.0 (imperceptible color difference). Waste paint and colorant rinse water are classified as hazardous waste under DENR AO 2013-22 and must be collected in approved containers, stored in the store's hazmat area per W236, and collected by DENR-accredited transporter per scheduled pickup. Failure to maintain the mixing station results in customer complaints, product returns, expensive equipment repair (PHP 15,000–30,000 per service call), and potential DENR citation for improper hazardous waste handling.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-Opening Equipment Power-On & Diagnostic**: Sales Associate (Paint Specialist) arrives 30 minutes before store opening; powers on spectrophotometer, tint dispenser, and paint shaker; runs automated self-diagnostic (system checks nozzle pressure, canister levels, colorant viscosity, and electronic calibration status); system flags any canister below 15% fill level for priority refill from backup stock; records self-diagnostic pass/fail in equipment log; if diagnostic fails, Sales Associate contacts IT helpdesk per W48 and places station in "limited service" mode (pre-mixed paint sales only, no custom mixing) | Sales Associate | Department Supervisor | 10 min |
| 2 | **Spectrophotometer Calibration**: Place certified white calibration tile on measurement aperture; system runs auto-calibration routine; verify calibration accuracy by measuring a known reference color swatch (store-kept calibration standard, replaced quarterly); ΔE must be < 1.0 for pass; if ΔE > 1.0, repeat calibration; if second attempt fails, escalate to Category Manager for equipment service ticket; log calibration result with timestamp in system | Sales Associate | Department Supervisor | 5 min |
| 3 | **Nozzle & Dispensing Tray Cleaning**: Wipe all tint dispensing nozzles with approved solvent-wetted cloth (mineral spirits for solvent-based, water for water-based colorants); clean dispensing tray and splash guard; inspect nozzle openings for dried colorant blockage; clear blockages with approved cleaning pin; verify drip-free dispensing by running a test dispense of each colorant into waste container; system logs cleaning completion timestamp | Sales Associate | Department Supervisor | 8–12 min |
| 4 | **Colorant Canister Level Check & Refill**: Check all 12–16 colorant canister levels via dispenser display; refill any canister below 25% from backup inventory stock in hazmat storage area; record refill volumes in inventory system for consumption tracking; verify correct colorant is loaded in correct canister position (cross-loading causes incorrect tinting); colorant expiry dates checked (shelf life: 24 months unopened, 12 months once loaded in dispenser); expired colorant flagged for removal and disposal per W82 | Sales Associate | Department Supervisor | 5–10 min |
| 5 | **End-of-Day Waste Collection & Disposal**: After store closing: collect all waste paint, colorant residue, solvent rinse, and used cleaning materials; deposit in DENR-approved hazardous waste containers (clearly labeled with waste code per AO 2013-22); weigh and record waste volume in hazmat tracking log; store containers in designated hazmat storage area per W236; verify waste container capacity — if >80% full, notify Environmental Compliance Officer for priority transporter pickup scheduling; clean and dry all mixing surfaces, splash guards, and drip trays | Sales Associate / Maintenance Staff | Department Supervisor | 10–15 min |
| 6 | **Equipment Shutdown & Security**: Power down spectrophotometer and tint dispenser (paint shaker may remain on standby for overnight agitation of pre-mixed stock); lock colorant cabinet; cover mixing station with protective cover to prevent dust accumulation; verify ventilation hood is operational; record end-of-day station status in equipment log; if any equipment issues noted during the day, create maintenance request in system for repair scheduling | Sales Associate | Department Supervisor | 5 min |

### System Touchpoints
- Paint mixing station equipment management module with daily cleaning/calibration checklist
- Spectrophotometer calibration log with ΔE tolerance tracking
- Colorant canister inventory module with automated low-level alerts
- Hazardous waste tracking log with DENR waste codes (W82, W236)
- Equipment maintenance request system (W48, W47)
- Inventory system for colorant consumption and refill tracking
- Compliance reporting module for DENR SMR/CMR submission (W433)

### Pain Points / Risks
- **Equipment downtime**: A malfunctioning tint dispenser takes 3–5 business days for manufacturer service; store loses all custom paint mixing revenue (~PHP 40,000–80,000/day in paint sales); Category Manager should maintain one backup manual tint dispenser per region for emergency use
- **Calibration drift**: In high-temperature, high-humidity Philippine stores, spectrophotometer calibration can drift faster than manufacturer-recommended daily calibration; ΔE > 2.0 leads to visible color mismatch and customer complaints; stores in humid locations should perform mid-day calibration check during peak season
- **Hazardous waste non-compliance**: DENR-improper storage or disposal of paint waste carries fines of PHP 10,000–200,000 per violation per DAO 2021-19; waste containers must be clearly labeled, closed, and stored in designated areas; monthly waste volume must not exceed DENR-permitted generator limits per location
- **Colorant cross-contamination**: Loading wrong colorant into wrong canister position causes systematic color errors across all subsequent mixes until discovered; each canister position must be barcode-scanned during refill to verify correct colorant assignment

### Staffing Implication
- **Sales Associate (Paint Specialist)**: Daily paint station maintenance adds ~40–50 minutes/day (pre-opening + end-of-day); absorbed by existing Paint & Finishes Sales Associate as part of daily opening/closing duties
- **Training**: 8-hour paint mixing station operation and maintenance certification per W51; includes DENR hazardous waste handling awareness per W82
- **No incremental headcount**

### Time Estimate
- Pre-opening diagnostic & calibration: 15 min
- Nozzle cleaning & canister check: 13–22 min
- End-of-day waste collection & disposal: 10–15 min
- Equipment shutdown: 5 min
- **Total per store per day**: 43–57 min

---

## W1004. Customer Material Delivery Scheduling & Rescheduling Self-Service Portal

| Field | Detail |
|---|---|
| **Trigger** | Customer places ecommerce order or creates a delivery order requiring scheduled delivery |
| **Frequency** | ~18,000–20,000 delivery scheduling events/month (~600–650/day) |
| **Volume** | 1 delivery per event; ~10% reschedule rate |
| **Owner** | Ecommerce Operations Manager |
| **Participants** | Customer, Delivery Partner (3PL), Store/DC Fulfillment Team, Customer Service Agent |

### Background

BuildRight Depot's ecommerce platform processes ~42,900 orders/month (Section 8.5), of which ~40% (17,200) require home delivery. In addition, in-store customer delivery orders (W5D) add ~5,000–8,000 deliveries/month for bulky items. Customers currently contact the call center or store to reschedule deliveries, creating ~1,800–2,000 reschedule calls/month that consume call center capacity and often result in missed delivery windows. The self-service portal allows customers to select delivery date/time slots, reschedule, add delivery instructions, and track delivery status without agent intervention. This is critical for Philippine retail where delivery failures are common due to traffic congestion, typhoons, and address ambiguity (many Philippine addresses lack standardized street numbering). Allowing customer self-service reduces call center volume by 15–20% and improves delivery first-attempt success rate from ~75% to ~85%.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Delivery Date/Time Slot Selection**: After order placement (ecommerce or in-store), system presents available delivery slots: (a) slot availability calculated from real-time carrier capacity, store/DC fulfillment workload, and delivery zone coverage; (b) delivery zones: Zone 1 (within 5 km of store, same-day or next-day), Zone 2 (5–15 km, 1–2 business days), Zone 3 (15–30 km, 2–3 business days), Zone 4 (30+ km, 3–5 business days, DC-fulfilled); (c) time slots: 8AM–12PM, 12PM–4PM, 4PM–8PM (Philippine daylight hours); (d) premium slots (specific 2-hour window) available for surcharge; (e) customer selects preferred slot; system confirms with SMS/email notification containing tracking link | Customer / System | Ecommerce Operations Manager | 2–3 min |
| 2 | **Delivery Instructions & Address Verification**: Customer enters delivery instructions: (a) detailed address with landmark description (standard Philippine practice — "beside Jollibee", "across from Barangay Hall"); (b) gate code or access instruction for gated communities; (c) preferred drop-off location (front door, garage, side gate); (d) contact person if different from orderer; (e) system verifies address against Philippine postal code database and PSA PSGC hierarchy (MDM-019); (f) for known difficult addresses (high-rise condominiums with strict receiving hours, remote barangay roads), system warns customer of potential delivery challenges and suggests alternative pickup per W11 (BOPIS) | Customer / System | Ecommerce Operations Manager | 3–5 min |
| 3 | **Rescheduling & Modification**: Customer accesses order via mobile app or web portal to reschedule: (a) system shows current slot and available alternatives; (b) reschedule allowed up to 4 hours before original delivery window; (c) within 4 hours, customer must call customer service; (d) system calculates any fee difference (zone change, premium slot surcharge); (e) customer confirms reschedule; system updates carrier dispatch plan and fulfillment schedule; (f) new confirmation sent via SMS/email; (g) maximum 2 reschedules per order; after 2nd reschedule, customer service agent outreach for resolution | Customer / System | Ecommerce Operations Manager | 2–3 min |
| 4 | **Delivery Day Communication**: On delivery day: (a) system sends "out for delivery" SMS with driver name, vehicle plate, and estimated arrival window; (b) GPS tracking link shared with customer for real-time location; (c) driver sends "arriving in 15 minutes" SMS notification; (d) upon delivery, driver captures proof-of-delivery (photo of delivered goods at location + customer signature on tablet); (e) system marks order as delivered; customer receives delivery confirmation SMS with photo | System / Delivery Partner | Ecommerce Operations Manager | Automated |
| 5 | **Failed Delivery Handling**: If delivery fails: (a) system logs failure reason (customer not available, wrong address, access denied, item damaged in transit); (b) customer receives SMS with failure reason and reschedule link; (c) system auto-schedules redelivery attempt for next available slot (default 2 business days); (d) after 2 failed attempts, order is returned to originating store/DC per W215 and customer receives refund per W101; (e) failed delivery analytics feed into carrier performance scorecard per W1013 | System / Customer Service Agent | Ecommerce Operations Manager | 3–5 min per failure |

### System Touchpoints
- Customer self-service portal (web and mobile app) with delivery scheduling module
- Real-time carrier capacity API integration with 3PL partners (Lalamove, Transportify, own fleet)
- GPS tracking integration for real-time driver location
- Address verification module with PSA PSGC hierarchy (MDM-019)
- SMS gateway integration (Philippine telcos: Globe, Smart, DITO)
- Order management system (W536) for fulfillment status
- Payment gateway for slot surcharge processing
- Carrier performance scorecard (W1013)
- Failed delivery analytics dashboard

### Pain Points / Risks
- **Address ambiguity**: Philippine addresses are notoriously non-standard; reliance on landmarks and barangay descriptions creates delivery confusion; system should capture free-text landmark descriptions in addition to structured address fields and share with drivers
- **Typhoon/weather disruption**: During typhoons, delivery capacity drops 40–60% in affected areas while demand for emergency supplies (tarpaulins, plywood, nails) surges; system must support mass rescheduling notifications and carrier capacity reallocation
- **3PL reliability**: Third-party delivery partners may over-promise capacity during peak periods (payday weekends, ber-months); system should maintain real-time capacity feeds and enforce hard booking limits per carrier per zone
- **Customer no-show**: Approximately 10–15% of delivery attempts fail because customer is unavailable despite confirmation; pre-delivery confirmation SMS/call 2 hours before arrival reduces no-show rate

### Staffing Implication
- **Customer Service Agent**: Self-service portal reduces ~1,800–2,000 reschedule calls/month; freed capacity redirected to complex issue resolution; no headcount change
- **Ecommerce Operations Manager**: Delivery scheduling analytics and carrier management add ~2–3 hours/week; absorbed by existing role
- **No incremental headcount**

### Time Estimate
- Slot selection: 2–3 min (customer self-service)
- Address/instructions: 3–5 min (customer self-service)
- Rescheduling: 2–3 min (customer self-service)
- Delivery day communication: automated
- Failed delivery handling: 3–5 min (agent-assisted for exceptions)
- **Total customer effort**: 5–11 min per delivery event
- **Total agent effort**: < 1 min per event (system-automated with exception handling)

---

## W1005. Store-Level Shelf Stock Rotation & Paint/Chemical Expiry Monitoring

| Field | Detail |
|---|---|
| **Trigger** | Daily scheduled task; also triggered by new batch receipt and product expiry alert |
| **Frequency** | Daily per store, focused on paint, adhesives, sealants, chemicals, and consumables |
| **Volume** | ~800–1,200 SKUs monitored per store (paint, chemical, adhesive, consumable categories) |
| **Owner** | Department Supervisor (Paint & Finishes) |
| **Participants** | Sales Associate (Stock Associate rotation), Category Manager (expiry policy) |

### Background

BuildRight Depot carries ~2,800 paint & finishes SKUs, plus ~1,750 adhesives, sealants, solvents, and chemical products across the store network. Unlike hardware items (nails, screws, tools) that have indefinite shelf life, paint and chemical products have finite shelf lives: water-based paint (12–24 months unopened), solvent-based paint (24–36 months), epoxy adhesive (12–18 months), contact cement (12 months), silicone sealant (9–18 months), and PVC solvent cement (12 months). Philippine warehouse-style stores with open ventilation and high ambient temperatures (30–38°C in summer) accelerate product degradation. Selling expired or degraded paint/adhesives leads to customer project failures (paint peeling, adhesive failure, sealant cracking), costly returns, brand damage, and potential consumer safety liability under RA 7394 (Consumer Act). The FIFO (First-In, First-Out) rotation must be rigorously enforced for these categories. This workflow also feeds into markdown optimization (W93, W737) for approaching-expiry products and SLOB provisioning (W220) for expired stock.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Daily FIFO Shelf Rotation Check**: Stock Associate walks assigned aisles (paint, adhesives, sealants, chemicals); for each SKU batch on shelf: (a) check batch/lot date label (arrival date sticker applied at receiving per W109); (b) verify older stock is positioned in front of newer stock; (c) re-arrange any out-of-sequence batches to ensure FIFO compliance; (d) scan shelf barcode with RF gun to confirm rotation check completion; (e) system logs rotation check with timestamp and associate ID | Stock Associate | Department Supervisor | 20–30 min |
| 2 | **Expiry Date Scan & Alert Processing**: Stock Associate uses RF gun to scan batch/lot barcodes of all monitored SKUs; system compares batch date against shelf life master data per SKU: (a) **Green (> 6 months to expiry)**: no action; (b) **Amber (3–6 months to expiry)**: system generates markdown recommendation per W93 — progressive markdown: 10% at 6 months, 20% at 4 months, 30% at 3 months; markdown applied by Category Manager approval; (c) **Red (< 3 months to expiry)**: system flags for priority clearance — 40–50% markdown, bundle with compatible products, or return to vendor per W88 if vendor has return agreement; (d) **Expired**: immediate shelf removal, quarantine in backroom hazmat area, disposition per W91 (damaged/defective goods) | Stock Associate / System | Department Supervisor | 15–25 min |
| 3 | **Approaching-Expiry Markdown Execution**: For Amber/Red items: (a) Department Supervisor reviews system-generated markdown recommendations; (b) applies markdown per authority matrix (up to 20% markdown: Supervisor approval; 20–40%: Store Manager approval; >40%: Category Manager approval); (c) system updates POS price file and shelf label per W181; (d) new price labels printed and applied to shelf; (e) if ecommerce-eligible, markdown reflected on buildright.com.ph per ECOM-002; (f) markdown tracked per SKU for margin impact analysis | Department Supervisor / Category Manager | Department Supervisor | 10–20 min |
| 4 | **Expired Product Quarantine & Disposal**: For expired items: (a) Stock Associate removes from shelf and places in quarantine bin in backroom; (b) scan-out from active inventory with "expired" disposition code per W91; (c) system creates disposal request for Department Supervisor approval; (d) hazardous expired products (solvents, chemicals) stored per W236 and collected by DENR-accredited transporter per W82; (e) non-hazardous expired products disposed per store waste management (W502); (f) inventory write-off posted to GL with expiry loss account; (g) monthly expiry loss report generated for Category Manager review and supplier quality follow-up | Stock Associate / Department Supervisor | Department Supervisor | 5–10 min |
| 5 | **Supplier Quality Feedback Loop**: Monthly: (a) Department Supervisor compiles store-level expiry and quality issue summary by SKU and vendor; (b) report submitted to Category Manager; (c) recurring expiry issues (same SKU expiring within 6 months of receipt) indicate supplier sending aged stock or shelf life master data needs correction; (d) Category Manager escalates to vendor per W110 (Supplier Quality & CAPA) and W44 (Vendor Performance Review); (e) if vendor consistently sends short-dated stock, Buyer renegotiates delivery terms or evaluates alternative supplier per W631 (Strategic Sourcing) | Department Supervisor / Category Manager | Category Manager | Monthly: 30–45 min |

### System Touchpoints
- Shelf life master data per SKU (batch/lot tracking per INV-013, INV-016)
- RF gun barcode scanning with batch date capture
- FIFO compliance tracking dashboard per store
- Automated expiry alerting engine with amber/red/expired thresholds
- Markdown management module (W93, W737) with tiered approval workflow
- POS price file update integration (ECOM-002)
- Disposition code management (W91, W301)
- Hazardous waste tracking (W82, W236)
- Vendor performance scorecard (W44, W706)

### Pain Points / Risks
- **Batch date visibility**: Many suppliers do not print batch dates or expiry dates on product packaging; BuildRight must apply its own date-sticker at receiving (W109); if receiving clerk fails to sticker, the SKU is invisible to the expiry monitoring system; compliance rate of date-sticking at receiving must be ≥95%
- **Short-dated vendor deliveries**: Some vendors ship product with only 6–9 months remaining shelf life (e.g., a paint manufacturer shipping 18-month-old stock); receiving inspection (W109) should reject or flag deliveries with <50% shelf life remaining; threshold configurable per SKU category
- **Customer dissatisfaction with markdown**: Customers may perceive short-dated markdown items as "BuildRight sells old stock"; markdown signage should frame as "clearance sale" rather than "near-expiry"
- **Ambient temperature impact**: Products stored near the store entrance or in the lumber yard (outdoor area) degrade faster than products in the climate-controlled interior; shelf life monitoring thresholds should be adjusted for storage zone

### Staffing Implication
- **Stock Associate**: FIFO rotation and expiry scanning adds ~45–90 minutes/day; absorbed by existing 3 Stock Associates per store as part of daily replenishment duties (W554)
- **Department Supervisor**: Markdown review and monthly reporting adds ~2 hours/month; absorbed by existing role
- **No incremental headcount**

### Time Estimate
- FIFO rotation check: 20–30 min/day
- Expiry date scan: 15–25 min/day
- Markdown execution (as needed): 10–20 min/day
- Expired product handling (as needed): 5–10 min
- Monthly supplier feedback: 30–45 min/month
- **Total per store per day**: 40–85 min (Stock Associate) + 5–10 min (Supervisor)

---

## W1006. Vendor Purchase Order ASN Reconciliation & Discrepancy Resolution

| Field | Detail |
|---|---|
| **Trigger** | Vendor transmits Advance Shipping Notice (ASN) for a confirmed Purchase Order |
| **Frequency** | ~800–1,000 ASN receipts/month (~60% of merchandise POs have ASN capability) |
| **Volume** | 1 ASN per PO; average 15 lines per ASN |
| **Owner** | Procurement Specialist |
| **Participants** | Vendor, DC Receiving Supervisor, AP Clerk, Buyer |

### Background

BuildRight Depot processes ~1,200 merchandise POs/month (Section 6.5) with ~800–1,000 vendors capable of transmitting ASNs through the vendor portal (W866). An ASN is the vendor's pre-shipment notification detailing what will actually be shipped, including item quantities, lot/batch numbers, expected ship date, and carrier/tracking information. Comparing the ASN against the original PO before physical receipt allows BuildRight to: (a) detect short-shipments (vendor shipping fewer units than ordered), over-shipments (vendor shipping more than ordered), wrong items, and substitutions before goods arrive at the DC; (b) pre-allocate receiving dock labor and staging space (W585); (c) update expected inventory positions for more accurate ATP calculations across all channels; (d) pre-generate goods receipt templates for faster DC receiving (W3); and (e) identify discrepancies early for vendor performance tracking (W44). Currently, ASN-vs-PO discrepancies affect ~15–20% of shipments, causing receiving delays, inventory inaccuracies, and AP matching failures. Proactive reconciliation before physical receipt reduces 3-way match exceptions by ~40% and DC receiving cycle time by ~25%.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **ASN Receipt & Auto-Match to PO**: Vendor transmits ASN via vendor portal (W866) or EDI (cXML/JSON API); system auto-matches ASN to open PO by PO number: (a) match on PO number, vendor code, and expected ship date window (±7 days); (b) system performs line-by-line comparison of ASN quantities vs. PO quantities; (c) auto-match outcomes: **Full Match** (ASN qty = PO qty for all lines, no discrepancies), **Partial Match** (some lines have qty differences within tolerance ±5%), **Mismatch** (significant qty difference, wrong items, or extra items not on PO) | System | Procurement Specialist | 1–2 min (automated) |
| 2 | **Discrepancy Classification & Auto-Action**: System classifies discrepancies and takes automated action: (a) **Minor short-shipment** (ASN qty ≤ PO qty, within 5% tolerance): system auto-accepts, updates PO expected quantity, and adjusts ATP; Buyer notified for information; (b) **Major short-shipment** (ASN qty < 90% of PO qty): system flags for Buyer review; auto-generates vendor notification requesting confirmation; if confirmed, PO qty reduced and DC receiving updated; (c) **Over-shipment** (ASN qty > PO qty): system blocks excess quantity; Buyer must approve or reject over-shipment; excess units received but held in quarantine until Buyer decision; (d) **Substitution** (vendor ships different item than ordered): system flags substitution; Buyer must approve alternative item or reject; if rejected, vendor notified to recall shipment; (e) **Extra items not on PO**: system blocks completely; vendor notified to arrange return pickup at vendor's cost | System / Buyer | Procurement Specialist | 2–5 min per exception |
| 3 | **Buyer Review & Resolution**: Buyer reviews flagged discrepancies: (a) short-shipments: assess impact on store replenishment plan; if critical items shorted, trigger emergency procurement per W60 or alternative supplier activation per W921; confirm partial receipt is acceptable; (b) over-shipments: evaluate if excess inventory is needed (seasonal demand, promotional stock); if accepted, PO quantity amended with appropriate approval; if rejected, vendor notified to arrange return at their cost; (c) substitutions: compare substitute item specifications against original order requirements; if quality-equivalent, accept with same PO price; if inferior, reject; (d) resolution logged in system with buyer comments and vendor notification sent | Buyer | Procurement Specialist | 5–15 min per discrepancy |
| 4 | **Pre-Receipt DC Notification**: System sends pre-receipt notification to DC Receiving Supervisor: (a) expected delivery date/time (from ASN carrier data); (b) confirmed receipt quantities (post-reconciliation); (c) receiving dock assignment (W585); (d) special handling notes (hazmat, temperature-sensitive, oversized); (e) pre-generated goods receipt template for DC scan-receiving; (f) vendor performance scorecard updated with ASN accuracy metrics (ASN qty match rate, on-time ASN submission rate) | System | DC Receiving Supervisor | Automated |
| 5 | **Post-Receipt Variance Analysis**: After physical goods receipt at DC (W3): (a) system compares GR quantities against both ASN quantities and PO quantities; (b) three-way comparison: PO → ASN → GR; (c) if GR ≠ ASN (i.e., vendor shipped differently than ASN stated): system generates carrier damage claim (if transit damage) or vendor discrepancy notification; (d) if GR = ASN ≠ PO (vendor partial shipment as notified): normal partial receipt processing; (e) monthly ASN accuracy report generated for vendor scorecard (W44, W706): metrics include ASN submission rate, ASN-to-PO match rate, ASN-to-GR accuracy rate; (f) vendors with ASN accuracy < 85% for 3 consecutive months placed on ASN compliance improvement plan per W110 | Procurement Specialist / System | Procurement Specialist | 10–15 min/week (batch analysis) |

### System Touchpoints
- Vendor portal ASN submission module (W866) with cXML/EDI/JSON API
- PO-ASN auto-matching engine with configurable tolerance thresholds (±5% default)
- Pre-receipt notification to WMS (W585, W3)
- ATP recalculation engine upon ASN confirmation
- Vendor performance scorecard (W44, W706) with ASN accuracy metrics
- DC goods receipt template auto-generation
- AP 3-way match (FIN-004) pre-populated from reconciled ASN data

### Pain Points / Risks
- **Vendor ASN adoption**: Only ~60% of vendors currently submit ASNs; long-tail vendors (small local suppliers) lack EDI/API capability; vendor onboarding (W36) should include ASN capability as a requirement for new vendors; existing non-ASN vendors encouraged to use vendor portal (W866) for manual ASN entry
- **ASN data quality**: Some vendors submit ASNs with inaccurate quantities (estimated rather than actual pack quantities); DC still discovers discrepancies at physical receipt; ASN data must be treated as "preliminary" until GR confirms actual quantities
- **Timing**: ASNs received < 24 hours before physical delivery provide limited value for pre-planning; vendors should submit ASNs ≥ 48 hours before shipment for optimal DC labor planning; vendor scorecard should track ASN lead time

### Staffing Implication
- **Buyer**: ASN discrepancy resolution adds ~15–30 minutes/day across 5–10 daily discrepancies; absorbed by existing Buyer team (10–12 Buyers)
- **Procurement Specialist**: Monthly ASN accuracy analysis adds ~1–2 hours/month; absorbed by existing role
- **DC Receiving Supervisor**: Pre-receipt planning from ASN data saves ~30 minutes/day in dock scheduling and labor allocation; net time neutral
- **No incremental headcount**

### Time Estimate
- Auto-match (system): 1–2 min per ASN
- Discrepancy classification (system): 2–5 min per exception
- Buyer review: 5–15 min per flagged discrepancy
- Post-receipt analysis: 10–15 min/week
- **Total procurement effort**: ~45–90 min/day across all buyers

---

## W1007. Customer Tool & Equipment Demo Reservation & Scheduling Service

| Field | Detail |
|---|---|
| **Trigger** | Customer requests in-store tool demonstration or equipment trial |
| **Frequency** | ~6,000–8,000 demo requests/month chain-wide (~30–40/store/month) |
| **Volume** | 1 demo per reservation; average 2–3 customers per group demo |
| **Owner** | Department Supervisor (Tools & Hardware) |
| **Participants** | Sales Associate (Power Tool Specialist), Customer, Service Coordinator |

### Background

Power tools and equipment are among BuildRight's highest-margin categories (~5% of active SKUs, 1,750 items, but disproportionate margin contribution). Philippine customers — both professional contractors and serious DIYers — strongly prefer to "try before they buy" for power tools costing PHP 3,000 and above. A hands-on demonstration that lets the customer feel the tool's weight, vibration, speed, and cutting/drilling power is the single most effective sales conversion technique for this category. BuildRight stores have dedicated demo stations for power tools (drill press, grinder station, circular saw station) and a trial area for outdoor equipment (pressure washers, generators). However, demo stations have limited throughput (one customer at a time per station, ~10–15 minutes per demo), creating bottlenecks during peak hours (payday weekends, promotional periods). A reservation system ensures demo station availability, reduces customer wait time, and allows Sales Associates to prepare the appropriate materials (wood, metal, tile samples) for the scheduled demo. Reservations can be made via mobile app, website, or phone. This workflow drives a 15–20% higher conversion rate for demoed items vs. non-demoed items.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Demo Reservation Request**: Customer requests demo via: (a) BuildRight mobile app — selects product, views available demo slots at preferred store, books slot; (b) website — same flow as app; (c) phone — customer calls store, Sales Associate books slot; (d) walk-in — Sales Associate checks availability and books next open slot; customer provides: product(s) to demo, preferred date/time, skill level (beginner/intermediate/professional), and specific material they plan to work with (concrete, wood, tile, metal) | Customer / Sales Associate | Department Supervisor | 3–5 min |
| 2 | **Demo Preparation**: Sales Associate (Power Tool Specialist) receives reservation notification and prepares: (a) verify demo tool is operational, charged (cordless), or connected to power; (b) verify safety guards and accessories are in place; (c) prepare appropriate test materials based on customer's stated use (e.g., 2x4 lumber for circular saw demo, concrete block for hammer drill demo, ceramic tile for angle grinder demo); (d) set up safety equipment (safety glasses, ear protection, gloves) per W140; (e) prepare product comparison cards (this tool vs. competitors in same price range) per W130; (f) print quotation with current pricing and any active promotions per W542 | Sales Associate | Department Supervisor | 10–15 min |
| 3 | **Demo Execution**: Customer arrives for scheduled demo: (a) Sales Associate conducts safety briefing (mandatory per W140, W512) — proper grip, kickback awareness, safety guard function, emergency shutoff; (b) customer signs safety acknowledgment form per W749; (c) Sales Associate demonstrates tool operation on test material; (d) customer operates tool under supervision; (e) Sales Associate provides technique tips, answers questions about specifications, battery life, warranty, and compatible accessories; (f) if customer wants to compare multiple tools, repeat demo with alternative model; (g) demo station cleaned and reset for next reservation | Sales Associate / Customer | Department Supervisor | 15–25 min |
| 4 | **Post-Demo Sales Conversion**: After demo: (a) Sales Associate presents quotation per W542 with tool, batteries, charger, accessories, and extended warranty options; (b) if customer decides to purchase, process sale at POS per W5B; (c) if customer needs time to decide, quotation saved to loyalty account per W894 (Project Vault) valid for 14 days; (d) offer tool rental per W139 as trial alternative for undecided customers; (e) for trade/professional customers, offer trade account discount per W112 (Pro Desk) and credit application per W24; (f) system logs demo completion and links to subsequent sale for conversion rate tracking | Sales Associate | Department Supervisor | 5–10 min |
| 5 | **Demo Station Maintenance & No-Show Handling**: Post-demo station maintenance: (a) clean test material residue; (b) check tool for damage or wear from demo usage; (c) recharge cordless batteries; (d) replace consumed test materials; (e) for no-shows: system auto-cancels reservation after 15-minute grace period; slot released for walk-in customers; customer receives SMS notification and offer to rebook; serial no-show customers (>3 in 6 months) flagged for manual rebooking confirmation | Sales Associate / System | Department Supervisor | 5–10 min |

### System Touchpoints
- Demo reservation module (mobile app, web, POS terminal)
- Demo station calendar with real-time availability per store
- Product catalog with demo-eligible flag and required materials per product
- Safety acknowledgment form (W749) digital capture
- POS quotation module (W542)
- Customer loyalty account integration (W894)
- Tool rental system integration (W139)
- Demo-to-sale conversion tracking analytics
- Demo station equipment maintenance log (W47)

### Pain Points / Risks
- **Demo station wear and tear**: Power tools used for daily demos have significantly shorter lifespans than display-only units; demo tools should be retired from demo service after manufacturer-recommended usage hours and sold as "demo units" at discount per W524; annual demo tool replacement budget of ~PHP 50,000–80,000 per store
- **Safety liability**: Customer injury during demo is a significant liability risk; safety briefing (step 3a) and signed acknowledgment (step 3b) are mandatory; one Sales Associate must supervise at all times; store's public liability insurance per W285 and W863 must cover demo activities
- **Peak demand bottlenecks**: During promotional periods (bi-monthly sales), demo demand can exceed station capacity by 200%; mobile demo cart with portable battery-powered tools can supplement fixed stations; consider reserving peak slots for high-value prospects (trade customers)
- **Noise disruption**: Power tool demos generate significant noise that disturbs adjacent departments; demo stations should be positioned away from customer service counter and quiet product areas; noise-dampening enclosures or scheduled demo windows (10AM–4PM only) may be necessary

### Staffing Implication
- **Sales Associate (Power Tool Specialist)**: 30–40 demos/month × 20–30 min each = 10–20 hours/month per store; absorbed by existing Tools & Hardware Sales Associates with power tool certification per W51
- **No incremental headcount**

### Time Estimate
- Reservation booking: 3–5 min
- Demo preparation: 10–15 min
- Demo execution: 15–25 min
- Post-demo conversion: 5–10 min
- Station maintenance: 5–10 min
- **Total per demo**: 38–65 min of Sales Associate time

---

## W1008. Store-Level Power Tool Battery Charging Station Safety & Maintenance

| Field | Detail |
|---|---|
| **Trigger** | Daily scheduled check (morning before store opening) and ongoing monitoring during store hours |
| **Frequency** | Daily × 200 stores; continuous monitoring during store hours |
| **Volume** | 1 charging station per store; ~20–40 batteries charging at any time |
| **Owner** | Department Supervisor (Tools & Hardware) |
| **Participants** | Sales Associate (Power Tool Specialist), Maintenance/Utility Staff |

### Background

BuildRight Depot stores maintain a battery charging station for power tool demonstration units (W1007), cordless display models, and customer-facing battery test/kiosk stations. Each station contains 4–8 multi-bay chargers supporting lithium-ion (Li-ion) and nickel-cadmium (NiCd) batteries from major brands (DeWalt, Makita, Bosch, Milwaukee). Lithium-ion battery fires are a growing safety concern in retail environments — a thermal runaway event in a Li-ion battery can reach 700°C and release toxic hydrogen fluoride gas. Philippine retail stores with limited fire suppression systems and high ambient temperatures (30–38°C) face elevated risk. BFP (Bureau of Fire Protection) Fire Safety Code (RA 9514) requires proper electrical safety measures for battery charging operations. This workflow ensures daily safety checks, temperature monitoring, proper ventilation, and emergency procedures are in place to prevent battery-related fire incidents and ensure BFP compliance.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-Opening Charging Station Inspection**: Sales Associate conducts daily check before store opening: (a) visual inspection of all charging bays — no cracked, swollen, or deformed batteries; (b) verify ventilation fan is operational (temperature-sensitive sticker on station showing < 40°C); (c) check charging bay contacts are clean and free of debris; (d) verify fire extinguisher (ABC dry chemical) is present within 3 meters, unobstructed, and inspection current (monthly tag per W758); (e) verify charging station is plugged into surge-protected outlet with correct amperage; (f) log inspection pass/fail in system; if any safety issue found, station powered down until resolved | Sales Associate | Department Supervisor | 5–8 min |
| 2 | **Battery Health Assessment & Charging Cycle Management**: Sales Associate assesses battery inventory: (a) identify batteries needing charge (fuel gauge < 25%); (b) place on charger with correct brand-specific charging bay; (c) set charging priority — demo batteries first (needed for customer demos per W1007), display batteries second; (d) never charge damaged, swollen, or overheated batteries — quarantine immediately in fireproof container and arrange vendor return per W88; (e) batteries reaching full charge removed promptly to prevent overcharging (smart chargers auto-stop but must not be left indefinitely); (f) maximum 8 batteries charging simultaneously per station to prevent circuit overload | Sales Associate | Department Supervisor | 5–10 min |
| 3 | **Continuous Temperature Monitoring**: During store hours: (a) charging station temperature sensor transmits continuous readings to store monitoring dashboard; (b) amber alert at > 40°C — Sales Associate reduces charging load (remove 2–3 batteries) and checks ventilation; (c) red alert at > 50°C — immediate station shutdown, all batteries removed, fire extinguisher on standby, Department Supervisor notified; (d) if any battery shows swelling, hissing, or smoke — activate fire emergency protocol per W330, evacuate immediate area, use fire extinguisher; (e) all temperature alerts logged in system for fire safety compliance records per W758, W806 | System / Sales Associate | Department Supervisor | Continuous (automated) |
| 4 | **Monthly Deep Maintenance & Battery Inventory**: Monthly deep maintenance: (a) power down entire charging station; (b) clean all charging contacts with isopropyl alcohol; (c) inspect charging cables for fraying or damage; (d) test all batteries with brand-specific diagnostic tool (charge capacity, internal resistance); (e) batteries below 70% of rated capacity removed from demo use and disposed per W82 (Li-ion batteries are hazardous waste per DENR); (f) replacement batteries ordered per procurement process; (g) charging station electrical inspection by licensed electrician (annual requirement per BFP); (h) update battery inventory list with current health status per battery | Sales Associate / Maintenance Staff | Department Supervisor | 30–45 min/month |
| 5 | **Incident Reporting & Continuous Improvement**: If any battery safety incident occurs: (a) immediate response per W330 (emergency response) and W140 (OHS incident); (b) incident documented in OHS reporting system per W436 (DOLE WAIR); (c) damaged battery secured as evidence for vendor investigation; (d) root cause analysis: charger malfunction, battery defect, environmental (heat, humidity), or procedural failure; (e) corrective action implemented and communicated chain-wide if systemic; (f) vendor notified per W110 (Supplier Quality & CAPA); (g) BFP fire incident report filed if fire occurred per W806 | Department Supervisor / OHS Officer | Store Manager | Per incident: 60–120 min |

### System Touchpoints
- Charging station IoT temperature sensor with store monitoring dashboard integration
- Battery inventory module with health status tracking (charge cycles, capacity %)
- Daily safety checklist module with pass/fail logging
- OHS incident reporting system (W140, W436)
- Fire safety equipment inspection log (W758, W806)
- Vendor quality CAPA system (W110)
- Hazardous waste disposal tracking (W82)

### Pain Points / Risks
- **Li-ion thermal runaway**: The most severe risk; a lithium-ion battery fire cannot be extinguished with water (reacts violently); ABC dry chemical extinguisher is the minimum requirement; sand bucket is recommended as additional suppression; staff must be trained to never use water on a Li-ion battery fire
- **Generic/counterfeit batteries**: Customers or staff may inadvertently charge non-genuine batteries (counterfeit or third-party replacement) on brand-specific chargers; these have higher failure rates; charging station should be clearly labeled: "Only genuine [Brand] batteries. No third-party batteries."
- **Power outage during charging**: When power is restored after an outage, multiple chargers may restart simultaneously, causing circuit overload; charging station should be on a dedicated circuit with surge protection and delayed-start capability
- **Ambient temperature**: Philippine store temperatures regularly exceed 30°C; Li-ion batteries degrade faster and have higher thermal runaway risk at elevated temperatures; charging station should be positioned in the coolest area of the store (away from direct sunlight and lumber yard)

### Staffing Implication
- **Sales Associate**: Daily charging station check adds ~10–18 minutes/day; absorbed by existing Tools & Hardware Sales Associate
- **Maintenance Staff**: Monthly deep maintenance adds ~30–45 min/month; absorbed by existing Maintenance/Utility Staff (1 per store)
- **No incremental headcount**

### Time Estimate
- Pre-opening inspection: 5–8 min/day
- Battery charging management: 5–10 min/day
- Continuous monitoring: automated
- Monthly deep maintenance: 30–45 min/month
- **Total per store per day**: 10–18 min + automated monitoring

---

## W1009. Customer Custom Order Special Pricing Approval & Quotation Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | Customer requests custom order or non-standard pricing for special items or large quantities |
| **Frequency** | ~8,000–10,000 custom orders/month chain-wide (~40–50/store/month) |
| **Volume** | 1 quotation per custom order request |
| **Owner** | Department Supervisor |
| **Participants** | Sales Associate, Customer, Store Manager, Category Manager (pricing), Buyer (sourcing) |

### Background

BuildRight Depot handles ~40–50 custom order requests per store per month for items not in regular stock: non-standard sizes (custom door dimensions, special-length pipes, non-catalog tile designs), large-quantity orders (bulk cement for a construction project, full-container lumber orders), or special materials (imported fixtures, designer hardware). These orders require individual pricing because standard SRP does not apply — the price depends on sourcing cost, order volume, delivery logistics, and competitive situation. The quotation lifecycle from customer request to order confirmation involves multiple approvals (standard pricing authority: Sales Associate up to 5% discount, Department Supervisor up to 10%, Store Manager up to 15%, Category Manager up to 20%, VP Merchandising above 20%). Long quotation turnaround times (>24 hours) lose deals to competitors. This workflow standardizes the quotation process, ensures margin protection through tiered approval, and tracks conversion rates. Custom orders represent ~5% of store revenue but carry higher average order values (PHP 15,000–500,000) and stronger customer loyalty.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Requirements Capture**: Sales Associate captures custom order details: (a) item description, specifications, dimensions, and quantity; (b) desired quality/grade (e.g., "marine-grade plywood", "structural steel"); (c) customer's intended use (helps recommend appropriate product); (d) required delivery date; (e) customer type (walk-in, trade account, corporate/project); (f) customer's budget indication (optional but helpful for pricing strategy); (g) customer's urgency level (standard 7–14 days, expedited 3–5 days, emergency 1–2 days with premium) | Sales Associate / Customer | Department Supervisor | 10–15 min |
| 2 | **Sourcing & Cost Estimation**: Sales Associate or Department Supervisor sources the item: (a) check if item exists in SKU master (55K total SKUs) but is non-stocked — if yes, system shows last purchase price and lead time; (b) check vendor catalog via vendor portal (W868) for available products and wholesale pricing; (c) for truly custom items, contact Buyer for vendor quotation — vendor quotes item cost, minimum order quantity, and lead time; (d) for large-quantity standard items, Buyer negotiates volume discount with vendor; (e) calculate landed cost (item cost + freight + handling + import duty if applicable per FIN-013); (f) determine delivery cost to store or customer site per W5D; (g) total cost estimated with margin target per category (minimum gross margin: 20% for custom orders) | Sales Associate / Buyer | Department Supervisor | 15–60 min (depends on sourcing complexity) |
| 3 | **Quotation Preparation & Pricing**: Sales Associate prepares quotation: (a) calculate selling price = landed cost ÷ (1 - target margin %); (b) compare to standard SRP for similar items (if available) — custom price should be within ±15% of comparable SRP to remain competitive; (c) apply customer-type pricing: trade account discount (5–15% per W24), corporate/project pricing per W163; (d) add delivery fee if applicable; (e) calculate and display total order value; (f) system auto-generates quotation number with 14-day validity; (g) quotation includes itemized breakdown, payment terms, delivery timeline, and cancellation policy; (h) if discount exceeds Sales Associate authority (>5%), quotation routed for approval per tiered authority matrix | Sales Associate / System | Department Supervisor | 10–15 min |
| 4 | **Tiered Pricing Approval Workflow**: System routes quotation for approval: (a) **≤ 5% below target margin**: auto-approved (Sales Associate authority); (b) **5–10% below target margin**: Department Supervisor approval (≤ 30 min SLA); (c) **10–15% below target margin**: Store Manager approval (≤ 2 hour SLA); (d) **15–20% below target margin**: Category Manager approval (≤ 4 hour SLA); (e) **> 20% below target margin**: VP Merchandising approval (≤ 24 hour SLA); (f) approver reviews: margin %, competitive situation, customer relationship value, strategic importance (e.g., new corporate account), and order volume potential; (g) approver approves, rejects, or modifies price; (h) if modified, quotation updated and re-presented to customer | System / Approvers | Category Manager | 2–30 min per approval level |
| 5 | **Customer Presentation & Order Conversion**: Sales Associate presents approved quotation to customer: (a) explain pricing, delivery timeline, payment terms, and warranty; (b) customer accepts: convert quotation to Sales Order → create PO for vendor (if non-stock item) or reserve inventory (if stocked item); (c) customer payment: 50% deposit required for custom orders (per W94), balance on delivery; (d) customer negotiates: return to step 3 with revised pricing request; (e) customer declines: log decline reason in system (price, lead time, competitor offer, project cancelled); (f) quotation saved to customer's loyalty account per W894; (g) post-declination: if customer is trade/corporate account, Category Manager review for competitive pricing adjustment | Sales Associate / Customer | Department Supervisor | 10–20 min |
| 6 | **Quotation Analytics & Follow-Up**: Weekly: (a) system generates quotation analytics: quotation volume by store, conversion rate, average margin, average turnaround time, top reasons for decline; (b) open quotations nearing 14-day expiry auto-trigger Sales Associate follow-up call/SMS to customer; (c) expired quotations analyzed for win-back opportunity; (d) Category Manager reviews quotations with margin > 20% below target for systemic pricing issues; (e) quarterly: quotation conversion benchmark by store category, best practices shared across stores | Department Supervisor / Category Manager | Category Manager | Weekly: 30 min; Quarterly: 2 hours |

### System Touchpoints
- Quotation management module with auto-numbering and 14-day validity tracking
- Tiered pricing approval workflow engine with SLA monitoring
- SKU master (55K items) and vendor catalog integration (W868)
- POS quotation module (W542) for in-store generation
- Customer loyalty account integration (W894) for quotation saving
- Deposit and payment management (W94)
- Margin calculation engine with landed cost roll-up (FIN-013)
- Quotation analytics dashboard with conversion rate tracking

### Pain Points / Risks
- **Slow vendor response**: Custom item sourcing often depends on vendor quotation turnaround (24–72 hours for domestic vendors, 5–10 days for import); long sourcing delays cause customer attrition; Buyer should maintain "quick quote" relationships with key vendors for fast turnaround
- **Margin erosion from over-discounting**: Sales Associates under pressure to close deals may push for lower margins; tiered approval workflow (step 4) prevents unauthorized discounting; Category Manager should audit discount patterns quarterly
- **Custom order fulfillment risk**: Vendor may fail to deliver custom-ordered items on time or at quoted quality; deposit collected (50%) mitigates financial exposure; customer must be informed of potential delays promptly; backup vendor per W921 should be identified for critical custom orders
- **Quotation expiry management**: Customers often return after the 14-day quotation validity expires expecting the same price; if costs have changed, Sales Associate must re-quote; extending validity to 30 days for trade/corporate accounts reduces re-quoting overhead

### Staffing Implication
- **Sales Associate**: Custom order processing adds ~30–50 min per quotation; at 40–50 quotes/month per store, this is ~20–40 hours/month; absorbed by 12 Sales Associates per store
- **Department Supervisor**: Approval processing adds ~5–10 min/approval; at ~10–15 approvals/month, this is ~1–2.5 hours/month
- **Buyer**: Sourcing support adds ~15–30 min/custom item quote; absorbed by existing 10–12 Buyers
- **No incremental headcount**

### Time Estimate
- Requirements capture: 10–15 min
- Sourcing & cost estimation: 15–60 min
- Quotation preparation: 10–15 min
- Approval workflow: 2–30 min
- Customer presentation: 10–20 min
- **Total per custom order**: 47–140 min of combined staff time

---

## W1010. Store-Level Outdoor Garden Center Weather Protection & Seasonal Display Setup

| Field | Detail |
|---|---|
| **Trigger** | Seasonal calendar event (quarterly rotation) and weather alerts (typhoon, monsoon) |
| **Frequency** | Quarterly seasonal rotation + weather-triggered emergency protection (6–12 events/year in typhoon belt stores) |
| **Volume** | 1 garden center per store (~200–400 sqm outdoor area) |
| **Owner** | Department Supervisor (Garden & Outdoor) |
| **Participants** | Sales Associate (Garden), Maintenance/Utility Staff, Store Manager |

### Background

BuildRight Depot stores include a Garden & Outdoor section (~3% of active SKUs, ~1,050 items — plants, pots, hoses, sprinklers, outdoor furniture). In the Philippines, this section is typically an outdoor or semi-covered area adjacent to the store building. The tropical climate creates unique operational challenges: (a) intense sun (UV index 10–12) degrades plastic outdoor furniture, hoses, and packaging within weeks; (b) monsoon rains (June–November, 2,000–4,000mm annual rainfall in many regions) flood outdoor displays and damage cardboard-packaged goods; (c) typhoons (average 20 per year entering Philippine Area of Responsibility) generate sustained winds of 100–200+ kph that can destroy entire outdoor displays and turn unsecured items into dangerous projectiles; (d) dry season heat (March–May, 35–40°C) kills live plants and makes outdoor shopping uncomfortable. Proper weather protection infrastructure (shade netting, canopy systems, wind barriers, drainage) and seasonal display rotation directly impact sales and shrinkage for this category. The garden center contributes ~3% of store revenue but has disproportionate impact on store appearance and customer traffic (live plants and seasonal displays are a visual draw from the parking lot).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Quarterly Seasonal Display Planning**: Category Manager (Garden & Outdoor) communicates seasonal display plan: (a) **Dry Season (Mar–May)**: heat-tolerant plants (cacti, succulents, bougainvillea), garden irrigation systems, outdoor shade solutions, summer garden furniture; (b) **Rainy Season (Jun–Nov)**: waterproofing products, rain barrels, indoor plants, covered garden solutions; (c) **Ber Months (Sep–Dec)**: Christmas plants (poinsettia), holiday décor, gift-ready potted arrangements; (d) **Post-Holiday (Jan–Feb)**: garden renovation, new plant arrivals, spring prep; Department Supervisor reviews planogram per W86 and allocates garden center floor space | Department Supervisor / Category Manager | Department Supervisor | 30–45 min/quarter |
| 2 | **Seasonal Display Setup & Rotation**: Sales Associate executes seasonal rotation: (a) remove outgoing seasonal products — markdown per W93 if still sellable, return to vendor per W88 if vendor has buy-back agreement (W901), or dispose per W502 if damaged/unsellable; (b) install seasonal display infrastructure: shade netting (dry season), rain covers (rainy season), Christmas lighting and canopy (ber months); (c) set up new product displays per planogram; (d) price and label all items per W181; (e) update POS planogram location for new items; (f) photograph completed display for compliance verification per W86 | Sales Associate / Maintenance Staff | Department Supervisor | 4–6 hours/quarter |
| 3 | **Weather Alert Response — Pre-Typhoon Protection**: When PAGASA raises Signal No. 1 or higher for store location: (a) Store Manager activates emergency protocol per W576; (b) for garden center specifically: (i) move all lightweight items indoors (pots, small plants, hoses, packaged goods); (ii) secure heavy items (large potted plants, outdoor furniture) with tie-downs or move against wind-sheltered wall; (iii) remove and store all canopy/shade structures — these become wind hazards; (iv) lower and secure display tables; (v) cover remaining ground-level items with heavy-duty tarps secured with sandbags; (vi) ensure drainage channels are clear of debris; (c) photograph pre-typhoon condition for insurance claim per W858 if damage occurs | Sales Associate / Maintenance Staff | Store Manager | 60–90 min per event |
| 4 | **Post-Typhoon Recovery**: After typhoon passes and PAGASA lowers signal: (a) inspect garden center for damage and safety hazards; (b) photograph all damage for insurance documentation per W858; (c) remove debris, standing water, and damaged merchandise; (d) assess salvagable inventory — re-price damaged-but-functional items per W549; (e) unsalvagable items written off per W92 with storm damage disposition code; (f) reinstall canopy/shade structures if intact; (g) restock from backroom reserves or DC replenishment per W927 (rainy season emergency deployment); (h) system logs storm damage loss value for insurance claim and financial reporting | Sales Associate / Maintenance Staff | Store Manager | 3–6 hours per event |
| 5 | **Daily Weather Maintenance**: Daily routine: (a) check weather forecast (PAGASA) for 48-hour outlook; (b) if heavy rain expected: deploy rain covers over sensitive displays; (c) if extreme heat expected: deploy shade netting, mist live plants; (d) after any rain event: check drainage, remove standing water, dry affected merchandise; (e) weekly: inspect shade structures, canopy integrity, and anchoring systems; (f) maintain garden center appearance: sweep, remove fallen leaves, organize displaced items | Sales Associate / Maintenance Staff | Department Supervisor | 15–20 min/day |

### System Touchpoints
- PAGASA weather alert integration with store notification system
- Seasonal display planogram module per garden center zone
- Inventory disposition module (W91, W92) with storm damage codes
- Insurance claim documentation module (W858)
- Markdown management (W93) for seasonal clearance
- POS planogram location management
- DC emergency replenishment (W927)

### Pain Points / Risks
- **Live plant shrinkage**: Live plants have the highest shrinkage rate of any category (~8–12% vs. 1.5% chain average) due to weather damage, neglect, and customer handling; daily watering, shade management, and turnover are critical; markdown at first sign of decline rather than waiting for full deterioration
- **Typhoon infrastructure damage**: Shade structures and canopy systems cost PHP 50,000–150,000 per garden center; failure to remove these before a typhoon results in total destruction (not covered by insurance if negligence is established); pre-typhoon dismantling protocol must be non-negotiable
- **Seasonal timing mismatch**: Philippine seasons are less predictable than the calendar suggests; early rainy season (May) or late typhoons (December) can catch displays unprepared; flexible transition timing based on actual weather rather than rigid calendar dates
- **Customer comfort**: Philippine customers avoid outdoor shopping during midday heat (11AM–2PM) and heavy rain; misting systems and covered walkways in the garden center extend the comfortable shopping window

### Staffing Implication
- **Sales Associate**: Garden center weather maintenance adds ~15–20 min/day; absorbed by existing Sales Associates as part of daily opening/closing duties
- **Maintenance Staff**: Pre-typhoon protection adds 60–90 min per event (infrequent); absorbed by existing Maintenance/Utility Staff
- **No incremental headcount**

### Time Estimate
- Seasonal rotation: 4–6 hours/quarter
- Pre-typhoon protection: 60–90 min per event
- Post-typhoon recovery: 3–6 hours per event
- Daily weather maintenance: 15–20 min/day
- **Ongoing daily**: 15–20 min; **Quarterly**: 4–6 hours; **Per typhoon event**: 4–8 hours

---

## W1011. Customer Trade Account Credit Insurance & Bad Debt Protection Processing

| Field | Detail |
|---|---|
| **Trigger** | New trade account credit approval, annual credit insurance renewal, or trade credit insurance claim event |
| **Frequency** | ~500 new credit insurance enrollments/year; ~5,200 annual renewals; ~50–80 claims/year |
| **Volume** | 1 policy per trade account; claims per default event |
| **Owner** | Credit Manager |
| **Participants** | Credit Analyst, Finance Manager, Insurance Broker, Credit Insurance Provider, VP Finance |

### Background

BuildRight Depot extends trade credit to ~5,200 trade accounts and ~200 corporate accounts (Section 9.2). The combined AR exposure at any time is ~PHP 1.5–2.5 Billion (based on ~PHP 3,500/month AR invoices × 5,400 accounts, with Net 30–90 terms). Bad debt write-offs average ~0.5–1.0% of AR annually (PHP 7.5–25M/year). Trade credit insurance protects BuildRight against customer insolvency, protracted default (>90 days), and catastrophic concentration risk (single large corporate account default could be PHP 10–50M). In the Philippine market, trade credit insurance is offered by a limited number of providers (Philippine Export-Import Credit Agency Philguarantee, Coface, Euler Hermes, Atradius). BuildRight's Credit Manager maintains a portfolio-level policy covering ~70% of trade account exposure (top 500 accounts by outstanding balance, representing ~80% of AR value). This workflow manages the credit insurance lifecycle: new account enrollment, annual renewal, coverage limit management, claim filing, and recovery.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **New Account Credit Insurance Assessment**: When Credit Analyst approves a new trade account per W24 (Credit Application): (a) assess whether account qualifies for credit insurance — minimum exposure threshold PHP 100,000/year; (b) submit account to credit insurer for coverage approval — insurer runs independent credit assessment using SEC/DTI records, financial statements, and trade references; (c) insurer assigns coverage limit (typically 80–90% of approved credit limit); (d) premium rate quoted (0.15–0.50% of covered sales annually, based on risk tier); (e) Credit Analyst reviews insurer's assessment vs. BuildRight's internal scoring — if insurer declines coverage, Credit Analyst may apply stricter terms (lower limit, shorter terms, COD) per W572; (f) approved coverage loaded into credit management system | Credit Analyst / Credit Insurance Provider | Credit Manager | 30–60 min per new account |
| 2 | **Annual Policy Renewal & Portfolio Review**: Annual: (a) Credit Manager reviews portfolio performance with insurer: claim rate, recovery rate, covered vs. uncovered exposure; (b) insurer adjusts premium rates based on portfolio loss experience; (c) Credit Manager negotiates: aggregate coverage limit (total portfolio cap), per-account sub-limits, deductible per claim, and waiting period; (d) accounts with adverse changes (payment deterioration, industry downturn, negative SEC filings) flagged for coverage reduction or exclusion; (e) new accounts added to policy; closed/inactive accounts removed; (f) premium payment scheduled per policy terms; (g) coverage documentation filed with Treasury per FIN-023 (insurance policy lifecycle) | Credit Manager / Insurance Broker | VP Finance | 4–8 hours/year |
| 3 | **Ongoing Coverage Monitoring**: Continuous: (a) credit insurer monitors all covered accounts and issues alerts: downgrade notifications (insurer reduces or withdraws coverage for specific accounts due to adverse information); (b) Credit Analyst receives insurer alerts in real-time; (c) on insurer downgrade: Credit Analyst immediately reviews account status — if internal assessment also negative, reduce credit limit or place on hold per W572; (d) if internal assessment remains positive, document disagreement with insurer and maintain current terms (BuildRight bears uninsured risk for the difference); (e) monthly: reconcile covered exposure vs. actual AR outstanding per covered account | Credit Analyst / System | Credit Manager | 15–30 min/week |
| 4 | **Claim Filing & Recovery**: When a covered account defaults (payment > 90 days overdue per W108): (a) Credit Analyst initiates claim with insurer; (b) documentation package: credit agreement, delivery receipts, invoices, statement of account, demand letters, evidence of collection efforts per W108, and any legal filings per W812; (c) insurer reviews claim within 30–60 days; (d) if approved: insurer pays coverage percentage (80–90%) of outstanding amount minus deductible; (e) insurer subrogates rights and pursues recovery from debtor; (f) BuildRight assigns receivable to insurer and cooperates in legal proceedings; (g) if insurer recovers more than claim payment, BuildRight receives proportional share of recovery; (h) claim payment posted to GL: insurance recovery offset against bad debt provision per W81 | Credit Analyst / Credit Manager | VP Finance | 2–4 hours per claim |
| 5 | **Coverage Gap Analysis & Self-Insurance Decision**: Quarterly: (a) Credit Manager analyzes uncovered exposure: accounts below insurance threshold, accounts declined by insurer, coverage gaps (limits lower than actual exposure); (b) calculate self-insurance reserve requirement: uncovered exposure × expected default rate (historical 0.5–1.0%); (c) recommend to VP Finance: increase coverage limits (higher premium), tighten credit terms for uncovered accounts, or increase bad debt provision per W81; (d) report to CFO in monthly financial review per W35 | Credit Manager | VP Finance | 2–3 hours/quarter |

### System Touchpoints
- Credit management system with insurance coverage tracking per account
- Credit insurer API integration for real-time account status monitoring
- AR aging system (W108, W889) with insurance flag per account
- Insurance claim documentation module (FIN-023, W610)
- GL bad debt provision module (W81)
- Credit scoring engine (W572) with insurer assessment data
- Financial reporting module (W35) for coverage gap analysis

### Pain Points / Risks
- **Insurer coverage withdrawal**: Credit insurers may suddenly withdraw coverage for entire industry sectors (e.g., construction companies during a building downturn) or geographic regions (e.g., typhoon-devastated areas); BuildRight must have contingency plans for rapid credit tightening when insurer coverage is withdrawn
- **Claim documentation burden**: Insurers require extensive documentation (delivery receipts, demand letters, legal filings) to process claims; AP/AR Clerks must maintain meticulous records for covered accounts; incomplete documentation delays or jeopardizes claim payment
- **Premium cost vs. bad debt cost**: Trade credit insurance premiums (0.15–0.50% of covered sales) must be weighed against historical bad debt rates (0.5–1.0% of AR); the ROI depends on coverage percentage and claim recovery efficiency; VP Finance should review annually
- **Subrogation conflicts**: When insurer pursues legal recovery against a BuildRight customer, the legal action may damage the customer relationship beyond repair; Credit Manager should coordinate with Sales Manager on accounts where both recovery and relationship preservation are priorities

### Staffing Implication
- **Credit Analyst**: Insurance monitoring and claim processing adds ~30–60 min/week; absorbed by existing Credit Analyst team
- **Credit Manager**: Annual renewal and quarterly analysis adds ~15–20 hours/year; absorbed by existing role
- **No incremental headcount**

### Time Estimate
- New account assessment: 30–60 min per account
- Annual renewal: 4–8 hours/year
- Ongoing monitoring: 15–30 min/week
- Claim filing: 2–4 hours per claim
- Quarterly gap analysis: 2–3 hours/quarter

---

## W1012. Store-Level Hazardous Material Spill Kit Inspection & Restocking

| Field | Detail |
|---|---|
| **Trigger** | Weekly scheduled inspection; triggered after any spill event |
| **Frequency** | Weekly inspection × 200 stores; restocking as needed (average 2–3 spill events/store/year) |
| **Volume** | 3–5 spill kits per store (paint area, chemical aisle, receiving dock, hazmat storage, lumber yard) |
| **Owner** | Department Supervisor (safety liaison) |
| **Participants** | Sales Associate (safety marshal), Maintenance/Utility Staff, Environmental Compliance Officer (regional) |

### Background

BuildRight stores carry ~4,900 hardware & fastener SKUs, ~2,800 paint & finishes SKUs, and various solvents, adhesives, and chemicals classified as hazardous materials under DENR AO 2013-22. Each store maintains 3–5 spill kits strategically placed near high-risk areas: the paint mixing station (W1003), chemical/solvent aisle, receiving dock (where inbound chemical containers may leak), hazmat storage area, and the lumber yard (treated lumber chemicals). A typical spill kit contains: absorbent pads, absorbent socks (for containing spill spread), neutralizing agents (for acid/base spills), nitrile gloves, safety goggles, disposal bags, and a laminated instruction card. DENR and BFP require functional spill response equipment at all times. Expired absorbent materials, missing gloves, or depleted kits leave BuildRight non-compliant and unable to safely respond to spills — which can range from a minor paint spill (cleaned by Sales Associate) to a major solvent leak (requiring evacuation per W238 and DENR notification). Each spill kit costs ~PHP 3,000–5,000 and must be inspected weekly and restocked within 24 hours of use.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Weekly Spill Kit Inspection**: Sales Associate (safety marshal) inspects all spill kits in assigned store: (a) visual inspection of each kit — verify all components present per inventory checklist (absorbent pads: 20 minimum, absorbent socks: 4 minimum, neutralizing agent: 2 bottles, nitrile gloves: 4 pairs, safety goggles: 2 pairs, disposal bags: 5 minimum, instruction card: 1); (b) check expiration dates on neutralizing agents and absorbent materials (shelf life: 3 years unopened); (c) verify kit container is intact and properly sealed; (d) verify kit location signage is visible and unobstructed; (e) log inspection result (pass/partial/fail) per kit in safety management system | Sales Associate | Department Supervisor | 15–20 min/week |
| 2 | **Restocking Order Generation**: If inspection reveals depleted or expired items: (a) system generates restocking requisition automatically from inspection log; (b) restocking items sourced from: (i) store backroom safety supply inventory (maintained at 2 spare spill kits per store), or (ii) if backroom stock depleted, requisition submitted to Safety Officer for central procurement; (c) SLA: restocking within 24 hours of inspection for any kit with missing critical items (absorbent pads, disposal bags, gloves); (d) non-critical restocking (instruction card replacement, signage) within 7 days | System / Sales Associate | Department Supervisor | 5 min per kit |
| 3 | **Post-Spill Kit Replenishment**: After any hazmat spill event per W238: (a) Sales Associate or LP Officer who used the spill kit logs usage in safety management system: items consumed, type of spill, quantity absorbed; (b) system automatically flags kit for priority restocking (same-day SLA); (c) used disposal bags (containing absorbed hazardous material) placed in DENR-approved hazmat waste container per W82; (d) replacement items pulled from backroom stock immediately; (e) if backroom stock insufficient, emergency procurement from nearest BuildRight store per W22 (inter-store transfer) or local safety supply vendor per W921 | Sales Associate / Maintenance Staff | Department Supervisor | 15–30 min post-spill |
| 4 | **Annual Spill Kit Replacement & Compliance Audit**: Annual: (a) all absorbent materials replaced regardless of expiration (absorbency degrades over time in tropical humidity); (b) neutralizing agents replaced if within 6 months of expiry; (c) instruction cards updated with current emergency contact numbers and DENR reporting requirements; (d) Safety Officer conducts annual spill kit compliance audit per store: kit count, placement, contents, condition, inspection log completeness; (e) audit results included in DOLE OHS annual report per W436; (f) store compliance score included in Store Manager KPI per W67 | Safety Officer / Department Supervisor | Store Manager | 2–3 hours/year per store |

### System Touchpoints
- Spill kit inventory module with location tracking per kit per store
- Weekly inspection checklist with digital logging
- Automated restocking requisition from inspection data
- Safety incident management system (W238, W140)
- Hazardous waste tracking log (W82)
- DOLE OHS reporting module (W436)
- Store compliance scorecard (W67)

### Pain Points / Risks
- **Kit accessibility during emergency**: Spill kits placed behind stock or in locked cabinets are inaccessible when needed most; kits must be wall-mounted or on open shelves with clear signage at eye level; monthly spot-checks by Store Manager verify accessibility
- **Staff unfamiliarity**: Sales Associates who have never responded to a spill may not know how to use the kit; annual spill response training per W237 (hazmat safety training) should include hands-on practice with kit contents; simulated spill drill during annual safety training
- **Tropical degradation**: Absorbent materials stored in high-humidity Philippine stores absorb ambient moisture over time, reducing their capacity to absorb actual spills; annual replacement (step 4) mitigates this; kits should be stored in sealed containers with desiccant packets
- **Cross-store restocking delays**: When backroom stock is depleted and no local vendor has compatible supplies, inter-store transfer (W22) takes 1–3 days; Safety Officer should maintain a list of local emergency supply vendors per W921 for same-day procurement

### Staffing Implication
- **Sales Associate (safety marshal)**: Weekly inspection adds ~15–20 min/week; absorbed by designated safety marshal as part of safety duties
- **No incremental headcount**

### Time Estimate
- Weekly inspection: 15–20 min/store/week
- Restocking: 5 min per kit (as needed)
- Post-spill replenishment: 15–30 min per event
- Annual replacement: 2–3 hours/year/store
- **Ongoing weekly**: 15–20 min

---

## W1013. E-Commerce Last-Mile Delivery Partner Performance Weekly Review

| Field | Detail |
|---|---|
| **Trigger** | Weekly scheduled review (every Monday morning) |
| **Frequency** | Weekly × 52 weeks/year |
| **Volume** | Review of 5–10 active delivery partner scorecards |
| **Owner** | Ecommerce Logistics Manager |
| **Participants** | 3PL Partner Account Managers, Ecommerce Operations Manager, Supply Chain Manager |

### Background

BuildRight Depot's ecommerce channel processes ~17,200 home delivery orders/month (Section 8.5) through a mix of third-party logistics (3PL) partners: Lalamove, Transportify, own fleet (for bulky items), and potentially Grab Express and Entrego. The last-mile delivery experience directly impacts customer satisfaction, repeat purchase rate, and brand perception. Philippine last-mile delivery faces unique challenges: traffic congestion (Metro Manila averages 15–20 km/h during peak hours), address ambiguity (many areas lack standardized addresses), typhoon-related disruptions, and variable 3PL service quality. A weekly performance review ensures BuildRight maintains delivery SLAs, identifies underperforming partners before they cause systemic customer dissatisfaction, and provides data-driven input for contract renewals and partner allocation decisions. Delivery partner performance directly affects BuildRight's ecommerce NPS score and costs — failed deliveries cost ~PHP 150–300 per attempt (redelivery labor, return shipping, customer service handling).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Automated Performance Data Compilation**: System auto-generates weekly performance dashboard for each active delivery partner: (a) **On-Time Delivery (OTD) Rate**: % of deliveries within promised time window (target: ≥ 90%); (b) **First-Attempt Delivery Success Rate**: % of deliveries completed on first attempt (target: ≥ 85%); (c) **Customer Delivery Satisfaction Score**: post-delivery survey rating on 1–5 scale (target: ≥ 4.2); (d) **Delivery Damage Rate**: % of deliveries with reported product damage (target: < 0.5%); (e) **Average Delivery Time**: order dispatch to proof-of-delivery (target: Zone 1 < 4 hrs, Zone 2 < 8 hrs, Zone 3 < 24 hrs, Zone 4 < 48 hrs); (f) **Cost Per Delivery**: average delivery cost per order by zone (benchmarked against contracted rates); (g) **Proof-of-Delivery (POD) Compliance**: % of deliveries with proper POD documentation (photo + signature) (target: ≥ 98%); (h) **Exception Rate**: % of deliveries requiring manual intervention (address not found, customer not available, wrong item) | System | Ecommerce Logistics Manager | Automated |
| 2 | **Scorecard Review & Partner Ranking**: Ecommerce Logistics Manager reviews dashboard and: (a) ranks all partners by composite score (weighted: OTD 30%, First-Attempt 25%, Satisfaction 20%, Damage 15%, Cost 10%); (b) identifies partners below threshold (composite score < 80 or any individual metric < 70%); (c) compares partner performance by delivery zone — some partners may excel in Metro Manila but underperform in provincial areas; (d) analyzes trends: improving, stable, or declining performance over rolling 4-week period; (e) identifies systemic issues (e.g., all partners showing lower OTD in a specific week indicates external factor like typhoon, not partner deficiency) | Ecommerce Logistics Manager | Ecommerce Operations Manager | 30–45 min |
| 3 | **Underperformer Discussion & Action Plan**: For partners below threshold: (a) Ecommerce Logistics Manager contacts 3PL Account Manager with specific performance data; (b) joint root cause analysis: driver capacity, routing issues, geographic coverage gaps, technology failures, seasonal demand spikes; (c) agree on corrective action with timeline: additional drivers, updated routing algorithm, address geocoding improvements, driver training; (d) set performance improvement target for next 2-week review cycle; (e) if partner fails to improve for 4 consecutive weeks, escalate to Supply Chain Manager for potential volume reduction or partner replacement per W242 (3PL Performance Review) | Ecommerce Logistics Manager / 3PL Account Manager | Ecommerce Operations Manager | 30–60 min per underperformer |
| 4 | **Volume Allocation Adjustment**: Based on weekly performance review: (a) shift delivery volume allocation toward higher-performing partners (within contract minimum volume commitments); (b) reduce allocation to underperformers while they implement corrective actions; (c) for new geographic zones or peak periods, provisionally allocate to best-performing partner; (d) if no partner meets SLA in a specific zone, evaluate onboarding new partner per W62B (3PL Onboarding) or increase own fleet capacity; (e) monthly: review volume allocation strategy with Supply Chain Manager for cost optimization | Ecommerce Logistics Manager | Supply Chain Manager | 15–30 min |
| 5 | **Monthly Executive Summary & Quarterly Business Review**: Monthly: (a) Ecommerce Logistics Manager compiles monthly delivery performance summary for Ecommerce Operations Manager; (b) key metrics: total deliveries, composite partner score, cost per delivery trend, customer satisfaction trend, failed delivery cost impact; (c) quarterly: formal QBR with top 3 partners — review SLA performance, discuss contract terms, plan for seasonal peaks (ber months, payday weekends), agree on technology improvements (API integration, real-time tracking enhancements) per W312 (routing/carrier master governance) | Ecommerce Logistics Manager | Ecommerce Operations Manager | Monthly: 60 min; Quarterly QBR: 2–3 hours |

### System Touchpoints
- Delivery partner performance dashboard with real-time metrics
- Order management system (W536) with delivery tracking integration
- 3PL API integration for automated performance data collection
- Customer satisfaction survey module (post-delivery NPS/CSAT)
- Proof-of-delivery capture system (photo + digital signature)
- Volume allocation management module
- Contract management system with SLA thresholds
- Cost per delivery analytics engine

### Pain Points / Risks
- **Data completeness**: 3PL partner APIs may have gaps (missing POD, delayed status updates); Ecommerce Logistics Manager must verify data completeness before drawing conclusions; partner contracts should mandate API uptime ≥ 99% and data completeness ≥ 98%
- **Attribution fairness**: Some delivery failures are not the partner's fault — incorrect customer address, customer not available, store fulfillment delay causing late dispatch; root cause analysis (step 3b) must correctly attribute failures before penalizing partners
- **Partner concentration risk**: Over-reliance on a single 3PL partner (e.g., 60%+ of delivery volume) creates risk if that partner experiences a system outage or labor action; BuildRight should maintain at least 3 active delivery partners per zone with no single partner handling >50% of volume
- **Seasonal capacity**: During ber months (Sep–Dec), delivery demand increases 30–50% while 3PL capacity is also constrained by overall e-commerce season; early capacity booking (August) and temporary partner onboarding (W62B) are essential

### Staffing Implication
- **Ecommerce Logistics Manager**: Weekly review adds ~2–3 hours/week; absorbed by existing role
- **No incremental headcount**

### Time Estimate
- Data compilation: automated
- Scorecard review: 30–45 min/week
- Underperformer discussion: 30–60 min as needed
- Volume allocation: 15–30 min/week
- Monthly/quarterly reporting: 60 min/month + 2–3 hours/quarter
- **Total weekly**: 60–120 min

---

## W1014. Customer Multi-Entity Billing & Consolidated Invoicing for Corporate Accounts

| Field | Detail |
|---|---|
| **Trigger** | Corporate account customer requests consolidated billing across multiple store purchases or project sites |
| **Frequency** | ~200–300 consolidated invoices/month (affects ~200 corporate accounts) |
| **Volume** | 1 consolidated invoice per billing period per corporate account; average 8–15 individual transactions consolidated |
| **Owner** | Credit Manager |
| **Participants** | AR Analyst, Corporate Account Manager, Customer (B2B), Finance Manager |

### Background

BuildRight Depot's ~200 corporate/institutional accounts (Section 9.2) include property developers, government agencies, construction companies, and large enterprises that purchase from multiple store locations simultaneously (e.g., a national developer buying materials from BuildRight stores in Manila, Cebu, and Davao for different project sites). These corporate accounts expect a single consolidated invoice per billing period rather than separate invoices per store — this simplifies their AP processing, enables centralized payment, and supports their own project cost allocation. However, BuildRight's ERP records sales by store (which may belong to different legal entities per Section 2 — BuildRight Depot Inc. vs. BuildRight Digital Commerce Inc.), requiring intercompany revenue allocation before consolidated invoicing. The consolidated invoice must include: all transactions across stores for the billing period, broken down by store/project site, with subtotals per location and a grand total. Philippine BIR regulations require individual sales invoices per transaction (per CAS registration per store per W485), so the consolidated invoice serves as a summary billing statement rather than replacing individual BIR-registered invoices. This workflow supports PFRS 15 revenue recognition and PAS 24 related-party disclosure when the corporate account is a related entity.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Billing Period Close & Transaction Aggregation**: At billing period close (monthly, per corporate account terms): (a) system auto-aggregates all completed transactions (POS sales, ecommerce orders, project orders) for the corporate account across all 200 stores and 4 DCs; (b) transactions categorized by: store location, project site (if project-tagged per W162), document type (sales invoice, delivery receipt, credit memo), and entity (BuildRight Depot Inc. vs. Digital Commerce Inc.); (c) system flags any unmatched transactions (delivery without invoice, pending returns, outstanding credit memos); (d) unmatched items resolved before consolidation | System / AR Analyst | Credit Manager | 30–60 min per account |
| 2 | **Intercompany Revenue Allocation**: For transactions spanning multiple legal entities: (a) identify which transactions belong to BuildRight Depot Inc. (in-store sales) vs. BuildRight Digital Commerce Inc. (ecommerce orders); (b) allocate revenue to correct entity per intercompany agreement (Section 2 — Digital Commerce charges Depot Inc. a per-order fulfillment fee); (c) intercompany elimination entries created per W14 (IC Transactions & Settlement); (d) consolidated invoice shows net BuildRight group position to customer; (e) behind the scenes: each entity records its portion of revenue with corresponding IC entries per W752 | System / AR Analyst | Credit Manager | 15–30 min per account |
| 3 | **Consolidated Invoice Generation**: System generates consolidated invoice: (a) header: corporate account name, billing period, consolidated invoice number (sequential per BIR CAS registration); (b) body: grouped by project site (if applicable) → then by store location → then by individual transaction (with BIR sales invoice reference number for each); (c) each transaction shows: date, invoice number, item description, quantity, unit price, total, VAT amount; (d) subtotals per project site and per store location; (e) grand total with VAT breakdown; (f) credit memos and adjustments applied as deductions; (g) payment terms and due date; (h) BIR-compliant formatting (TIN, CAS permit number, registered address) per DOC-002 | System / AR Analyst | Credit Manager | 10–15 min per invoice (automated generation, manual review) |
| 4 | **Customer Delivery & Dispute Window**: Consolidated invoice delivered to customer: (a) emailed to customer's designated AP contact (PDF with digital signature per W686); (b) uploaded to customer B2B self-service portal per W936; (c) 5-business-day dispute window — customer may dispute individual line items; (d) disputes handled per W1022 (Trade Account Statement Dispute & Resolution); (e) undisputed invoices proceed to payment per terms (Net 30/60/90) | AR Analyst / System | Credit Manager | 5–10 min per delivery |
| 5 | **Payment Collection & Allocation**: Customer remits single payment for consolidated invoice: (a) AR Analyst receives payment (bank transfer per FIN-043, or check per W423); (b) payment allocated against all individual transactions in consolidated invoice; (c) system auto-reconciles: payment amount vs. consolidated invoice total; (d) if short payment (customer took unauthorized discount or withheld disputed amounts): short payment allocated to disputed line items per W1022; (e) if overpayment: excess recorded per W769 (Overpayment Detection & Refund); (f) payment confirmation sent to customer; (g) AR aging updated per W108 | AR Analyst / System | Credit Manager | 10–20 min per payment |

### System Touchpoints
- Consolidated billing module with multi-store, multi-entity transaction aggregation
- Intercompany revenue allocation engine (W14, W752)
- BIR-compliant invoice generation (DOC-002, W540)
- Customer B2B self-service portal (W936)
- AR aging and payment allocation system (W108, W889)
- Credit memo management (W101, W766)
- Payment gateway integration (ECOM-006)
- Document management system (W255) for invoice archiving

### Pain Points / Risks
- **Transaction matching complexity**: Corporate accounts with high transaction volumes (50–100+ per month across multiple stores) create complex matching challenges; individual sales invoice reference numbers must be accurately linked to the consolidated invoice; any discrepancy delays payment
- **Intercompany complexity**: When a single corporate purchase involves both in-store (Depot Inc.) and ecommerce (Digital Commerce Inc.) transactions, revenue allocation between entities must be accurate for consolidation per W14; errors cascade into IC elimination failures during month-end close per W9A
- **BIR compliance**: The consolidated invoice is a billing summary, not a replacement for individual BIR sales invoices; customers must retain both the consolidated statement and individual sales invoices for their own BIR compliance (input VAT claims per BIR Form 2550M); the consolidated invoice must clearly reference all individual invoice numbers
- **Customer dispute volume**: Large consolidated invoices with many line items have higher dispute probability; disputes on individual line items delay payment of the entire consolidated invoice; partial payment processing must be carefully managed to avoid aging disputes on undisputed portions

### Staffing Implication
- **AR Analyst**: Consolidated invoice generation and review adds ~60–100 min/month per active corporate account; at ~150 active accounts/month, this is ~150–250 hours/month; absorbed by existing AR team (37 Finance & Accounting staff)
- **Credit Manager**: Approval and exception handling adds ~10–15 hours/month
- **No incremental headcount**

### Time Estimate
- Transaction aggregation: 30–60 min per account
- IC allocation: 15–30 min per account
- Invoice generation: 10–15 min per invoice
- Delivery: 5–10 min per invoice
- Payment allocation: 10–20 min per payment
- **Total per corporate account per month**: 70–135 min

---

## W1015. Store-Level Forklift & Heavy Equipment Daily Safety Check & Log

| Field | Detail |
|---|---|
| **Trigger** | Daily before first use of forklift or heavy equipment (receiving dock, lumber yard) |
| **Frequency** | Daily × 200 stores (stores with forklifts: ~150 stores with lumber yards); ~2 forklifts per store on average |
| **Volume** | 1 safety check per piece of equipment per day |
| **Owner** | Receiving Clerk |
| **Participants** | Department Supervisor (Lumber), Maintenance/Utility Staff, Safety Officer (regional) |

### Background

Approximately 150 of BuildRight Depot's 200 stores have forklifts and/or pallet jacks for lumber yard operations (W3B, W438), receiving dock heavy lifting, and bulk material handling. Forklifts are classified as hazardous equipment under DOLE Department Order No. 13 series of 1998 (DO 13) — "Guidelines Governing Occupational Safety and Health in the Construction Industry" and DO 132-13 for materials handling equipment. Philippine regulations require: (a) daily pre-operation safety inspection; (b) operator certification (40-hour forklift training per TESDA); (c) annual equipment certification by DOLE-accredited testing organization; (d) documented maintenance log. Forklift accidents are among the most severe workplace incidents — a loaded forklift can weigh 3–5 tons and cause fatal crushing injuries. Philippine retail stores with customer-accessible lumber yards face additional risk of forklift-customer collisions if equipment is operated during store hours in customer areas. This workflow ensures daily pre-operation safety checks are completed and logged, operators are certified, and equipment is maintained in safe operating condition.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-Operation Safety Inspection**: Receiving Clerk (certified forklift operator) conducts daily pre-use inspection before store opening: (a) **Visual**: tire condition (no cuts, bulges, or excessive wear), fork condition (straight, no cracks), mast and chains (no visible damage, adequate lubrication), overhead guard (intact, no cracks), body panels (no damage); (b) **Fluid levels**: engine oil, hydraulic fluid, coolant (IC forklifts), battery water level and charge (electric forklifts); (c) **Operational tests**: service brake, parking brake, steering, horn, headlights, tail lights, backup alarm, fork tilt/lift/lower functions; (d) **Safety devices**: seat belt, fire extinguisher (mounted and charged), load backrest, overhead guard; (e) log all checks on daily inspection form (paper or tablet-based); (f) any failed check: equipment tagged "OUT OF SERVICE" with red tag, Store Manager notified, maintenance request submitted per W47 | Receiving Clerk | Department Supervisor | 10–15 min per forklift |
| 2 | **Operator Certification Verification**: Before operating: (a) system verifies operator's TESDA forklift certification is current (valid for 3 years); (b) system checks operator has completed BuildRight-specific forklift safety orientation per W51; (c) if certification expired or orientation incomplete: operator prohibited from operating equipment; (d) all certified operators listed on equipment-specific authorization board in receiving dock area; (e) only authorized operators may use forklift — no exceptions | System / Department Supervisor | Store Manager | Automated (system check) |
| 3 | **Operating Hours Safety Protocol**: During store hours when forklift operates in customer-accessible lumber yard: (a) designated spotter (Sales Associate) walks ahead of forklift to warn customers and ensure clear path; (b) forklift operates at walking speed (≤ 5 kph) in customer areas; (c) audible backup alarm must be functional; (d) forklift prohibited from operating in main sales floor areas during store hours; (e) heavy lifting (>500 kg) performed only in receiving dock or lumber yard — not in customer areas; (f) if forklift must cross a customer pathway: temporary barrier and Sales Associate controls pedestrian traffic | Receiving Clerk / Sales Associate | Department Supervisor | Continuous during operation |
| 4 | **Post-Operation Shutdown & Parking**: At end of day: (a) park forklift in designated area (receiving dock or lumber yard storage position); (b) forks lowered to ground level; (c) mast tilted forward slightly; (d) parking brake engaged; (e) key removed and stored in lockbox (accessible only to certified operators); (f) for electric forklifts: plug in for overnight charging in ventilated area (not in enclosed room due to hydrogen off-gassing from lead-acid batteries); (g) note any operational issues in shift log for next-day operator awareness | Receiving Clerk | Department Supervisor | 5–10 min |
| 5 | **Monthly Maintenance & Annual Certification**: Monthly: (a) Maintenance Staff performs scheduled preventive maintenance per manufacturer manual: lubrication, filter change, brake inspection, hydraulic system check; (b) maintenance logged in equipment management system per W188; (c) Annual: DOLE-accredited testing organization inspects and certifies forklift; (d) certification sticker affixed to forklift; (e) if forklift fails certification: removed from service until repairs completed and re-certified; (f) certification records maintained per W436 (DOLE OHS reporting) | Maintenance Staff / External Certifier | Store Manager | Monthly: 60–90 min; Annual: 4–6 hours |

### System Touchpoints
- Equipment management module with daily inspection checklist
- Operator certification tracking with expiration alerts (W51, HR-010)
- Maintenance scheduling system (W188, W47)
- DOLE OHS compliance reporting (W436)
- Incident reporting system (W140)
- Equipment authorization board module

### Pain Points / Risks
- **Operator certification gap**: Stores with only 1 certified forklift operator face disruption when that employee is absent; each store with a forklift should have minimum 2 certified operators (Receiving Clerks cross-trained per W567); DOLE fines for uncertified operation: PHP 5,000–50,000 per violation
- **Customer area operation**: Forklifts operating in customer-accessible lumber yards during store hours are the highest-risk activity in BuildRight stores; strict spotter protocol (step 3) is mandatory; any forklift-customer near-miss must be reported per W140 and triggers safety review
- **Equipment age**: Forklifts in Philippine retail stores experience heavy use (2–4 hours/day, 6 days/week) in hot, humid, and dusty conditions; replacement cycle should be 7–10 years; aging equipment increases maintenance costs and failure risk
- **Overnight charging safety**: Electric forklift batteries produce hydrogen gas during charging; charging area must be well-ventilated; no smoking or open flame within 5 meters; fire extinguisher required at charging station per W758

### Staffing Implication
- **Receiving Clerk**: Daily forklift inspection adds ~15–25 min/day; absorbed by 2 Receiving Clerks per store
- **Maintenance Staff**: Monthly maintenance adds ~60–90 min/month; absorbed by existing Maintenance/Utility Staff
- **No incremental headcount**

### Time Estimate
- Pre-operation inspection: 10–15 min per forklift per day
- Certification check: automated
- Operating hours safety: continuous during forklift use
- Post-operation shutdown: 5–10 min per forklift
- Monthly maintenance: 60–90 min per forklift
- **Total per store per day**: 15–25 min per forklift

---

## W1016. Customer Product Installation Warranty Registration & Follow-Up Service

| Field | Detail |
|---|---|
| **Trigger** | Customer purchases product with installation service or extended warranty |
| **Frequency** | ~8,000–10,000 warranty registrations/month chain-wide (~40–50/store/month) |
| **Volume** | 1 warranty registration per installation order |
| **Owner** | Service Coordinator |
| **Participants** | Sales Associate, Installation Partner, Customer, Service Warranty Specialist |

### Background

BuildRight Depot offers installation services (W138) for products such as aircon units, water heaters, ceiling fans, kitchen fixtures, bathroom fixtures, and solar panels. Each installation comes with: (a) a manufacturer product warranty (1–5 years depending on product); (b) an installation workmanship warranty provided by BuildRight (typically 90 days for installation quality); and (c) an optional extended warranty for purchase (covering parts and labor beyond manufacturer warranty, typically 1–3 additional years). Currently, warranty registration is manual and inconsistent — customers receive paper warranty cards that they may or may not mail in, and BuildRight has no systematic record of which installations are under warranty, what the warranty covers, or when warranties expire. This leaves BuildRight unable to: proactively contact customers for warranty service (revenue opportunity), track installation partner quality (partner audit per W213), or manage warranty claim costs against manufacturer reimbursement. A digital warranty registration process at POS, combined with automated follow-up, transforms warranty from a cost center into a customer retention and revenue tool.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Warranty Registration at POS**: At time of purchase with installation service: (a) Sales Associate creates installation work order per W544; (b) system auto-generates warranty registration record: product serial number (scanned at POS), installation date (scheduled), customer details (from loyalty account or guest info), installation partner assigned; (c) warranty coverage displayed: manufacturer warranty period, BuildRight installation warranty (90 days from installation completion), and extended warranty offer (if customer opts for purchase); (d) customer selects extended warranty (optional): premium added to transaction, warranty terms printed on receipt per DOC-002; (e) warranty registration confirmed via SMS to customer with registration number and coverage details | Sales Associate / System | Service Coordinator | 5–8 min |
| 2 | **Post-Installation Warranty Activation**: After installation completion (W138): (a) Installation Partner confirms completion in system with photo documentation and customer sign-off; (b) system activates warranty coverage: manufacturer warranty start date = installation date; installation workmanship warranty = installation date + 90 days; extended warranty = manufacturer warranty end date + extended period; (c) customer receives warranty activation confirmation SMS/email with: coverage summary, claim process instructions, service hotline number, and BuildRight app warranty wallet link per W911 (Digital Warranty Vault) | Installation Partner / System | Service Coordinator | 3–5 min (automated) |
| 3 | **30-Day Post-Installation Follow-Up**: System triggers 30-day post-installation follow-up: (a) automated SMS/email to customer: "How is your [product] working? Reply 1 (Great), 2 (Issue), 3 (Need Service)"; (b) if customer responds "Great" — system logs satisfaction; (c) if customer responds "Issue" or "Need Service" — auto-generates service ticket routed to Service Coordinator per W795; (d) Service Coordinator contacts customer within 24 hours to schedule service visit; (e) if issue is installation-related (covered by 90-day workmanship warranty): no charge to customer, installation partner dispatched for rework at partner's cost per W213; (f) if issue is product-related: warranty claim processed per manufacturer warranty per W33 (Warranty Claim Processing); (g) follow-up response and satisfaction logged in CRM per W756 | System / Service Coordinator | Service Coordinator | 5–10 min per response |
| 4 | **Pre-Expiry Warranty Extension Offer**: 30 days before manufacturer warranty expiry: (a) system identifies all customers with approaching warranty expiry; (b) automated notification sent: "Your [product] manufacturer warranty expires in 30 days. Extend your coverage with BuildRight Extended Warranty — [price]. Reply YES to add."; (c) customer accepts: extended warranty purchased via phone payment or next store visit; (d) customer declines: reminder logged for next annual outreach; (e) conversion rate tracked for warranty extension revenue analysis | System / Service Coordinator | Service Coordinator | 2–3 min per notification (automated) |
| 5 | **Warranty Analytics & Partner Quality Scoring**: Monthly: (a) Service Coordinator compiles warranty analytics: claim rate by product category, claim rate by installation partner, average time to resolution, warranty cost recovery from manufacturers, extended warranty conversion rate, customer satisfaction post-claim; (b) installation partners with claim rates > 5% flagged for quality audit per W213; (c) products with high claim rates reported to Category Manager for vendor quality escalation per W110; (d) extended warranty revenue and profitability reported to Finance per FIN-023 | Service Coordinator | Service Coordinator | 2–3 hours/month |

### System Touchpoints
- Warranty registration module integrated with POS (W544)
- Installation work order system (W138)
- Customer notification engine (SMS/email/CRM)
- Digital warranty vault (W911) in customer mobile app
- Service ticket management system (W795)
- Installation partner quality scoring (W213)
- Extended warranty billing and revenue recognition (FIN-023)
- Manufacturer warranty claim portal integration (W33)
- Customer satisfaction tracking (W65, W756)

### Pain Points / Risks
- **Serial number capture accuracy**: Products without scannable serial numbers (or with damaged barcodes) require manual entry; manual serial numbers have ~5% error rate, causing warranty claim rejections; POS must enforce serial number scan at sale for warranty-eligible products
- **Installation partner non-compliance**: Installation partners may fail to confirm completion in system, delaying warranty activation; Service Coordinator should have escalation path to partner manager for completion confirmation; partner payment should be contingent on system-confirmed completion
- **Warranty claim disputes**: Customer may claim product defect when issue is actually improper use or DIY modification; warranty terms must be clearly documented; installation photo documentation (step 2) protects against false installation-related claims
- **Manufacturer reimbursement delays**: Manufacturer warranty reimbursements can take 30–90 days, creating cash flow impact on BuildRight's warranty operations; Service Coordinator should track manufacturer reimbursement aging per W108

### Staffing Implication
- **Service Coordinator**: Warranty registration adds ~5–8 min per installation order; 30-day follow-up adds ~5–10 min per response; monthly analytics adds 2–3 hours; total: ~15–20 hours/month; absorbed by existing Service Coordinator role
- **No incremental headcount**

### Time Estimate
- POS registration: 5–8 min per order
- Post-installation activation: 3–5 min (automated)
- 30-day follow-up: 5–10 min per response
- Pre-expiry offer: 2–3 min (automated)
- Monthly analytics: 2–3 hours/month
- **Total per installation order**: ~15–20 min staff time (excluding automated steps)

---

## W1017. Store-Level Scrap Metal & Recyclable Material Collection & Revenue Recognition

| Field | Detail |
|---|---|
| **Trigger** | Accumulation of scrap metal, cardboard, and recyclable materials from store operations |
| **Frequency** | Weekly collection per store; daily accumulation |
| **Volume** | ~100–200 kg scrap metal/store/week; ~300–500 kg cardboard/store/week; ~50–100 kg plastic/store/week |
| **Owner** | Department Supervisor |
| **Participants** | Maintenance/Utility Staff, Scrap Metal Collector (accredited buyer), Finance Analyst (revenue recognition) |

### Background

BuildRight Depot's 200 stores generate significant recyclable waste from daily operations: damaged lumber (off-cuts, broken boards), scrap metal (damaged fixtures, wire offcuts, hardware returns), cardboard packaging (from inbound shipments), and plastic packaging. Philippine recycling infrastructure has matured significantly — accredited junk shops and scrap metal collectors (locally called "bote dyaryo" or "scrap buyers") serve every commercial area and pay market rates for sorted recyclable materials. Current market rates (2026): clean cardboard ~PHP 3–5/kg, scrap steel ~PHP 10–15/kg, scrap copper ~PHP 250–350/kg, aluminum ~PHP 50–70/kg, clean plastic ~PHP 5–8/kg. For a store generating 400–800 kg/week of recyclable material, this represents PHP 5,000–15,000/month in potential revenue (PHP 1,000–3,000/month per store) that is currently lost to improper disposal or untracked collection. Chain-wide, this represents PHP 12–36M/year in recyclable material value. Beyond revenue, proper recycling supports BuildRight's ESG commitments per W192 (GHG Emissions Tracking) and W193 (Waste Management & Circular Economy), reduces waste disposal costs per W502, and provides verifiable data for DENR waste diversion reporting per W433.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Daily Recyclable Material Segregation**: During daily operations: (a) Sales Associates and Receiving Clerks segregate waste into designated bins: (i) cardboard bin (flattened boxes, no food contamination), (ii) scrap metal bin (steel, copper, aluminum separated), (iii) plastic bin (clean packaging plastic, no chemical residue), (iv) wood/lumber bin (off-cuts, damaged boards — clean, no paint/treatment), (v) general waste bin (non-recyclable, per W502); (b) bins located at receiving dock and backroom; (c) hazardous materials (paint cans, solvent containers, chemical packaging) never placed in recycling bins — handled per W82 and W236 | All Store Staff | Department Supervisor | Ongoing (5–10 min/day per staff member) |
| 2 | **Weekly Collection & Weighing**: Weekly: (a) accredited scrap collector arrives at scheduled time (registered vendor in ERP per W36); (b) Maintenance Staff and collector weigh each category of recyclable material using calibrated scale at receiving dock; (c) collector issues weigh ticket per category with unit price and total amount; (d) Maintenance Staff verifies weigh ticket accuracy and signs receipt; (e) collector pays cash or issues check per agreed terms; (f) system records collection: material category, weight (kg), unit price, total revenue, collector vendor code | Maintenance Staff / Scrap Collector | Department Supervisor | 30–45 min/week |
| 3 | **Revenue Recording & Cash Handling**: (a) cash received from scrap collector: counted by Maintenance Staff in presence of Department Supervisor; (b) cash deposited in store safe per W541 (Cash Office Operations); (c) system records revenue: debit cash, credit "Other Income — Scrap/Recycling Revenue" per GL account mapping; (d) revenue recognized in period collected per PFRS (realized revenue from recyclable sales); (e) if collector pays by check: check deposited per W89 (Bank Reconciliation) and W764 (Daily Opening Safe Count); (f) monthly scrap revenue reported in store P&L per W67 (Store Performance Review) and W489 (Store Operating Budget) | Maintenance Staff / Department Supervisor | Department Supervisor | 10–15 min/week |
| 4 | **Quarterly Recycling Metrics & ESG Reporting**: Quarterly: (a) system aggregates recycling data: total weight by material category per store per region; (b) total revenue from recycling per store; (c) waste diversion rate = total recycled weight ÷ total waste generated; (d) carbon offset estimate: recycled cardboard saves ~3.5 kg CO2/kg, recycled steel saves ~1.5 kg CO2/kg per DENR conversion factors; (e) metrics included in ESG data collection per W694 (ESG Data Collection & Annual Report Preparation); (f) Store Manager reviews recycling performance in quarterly store performance review per W67; (g) stores with waste diversion rate < 30% flagged for improvement action plan | System / Department Supervisor | Store Manager | 30–60 min/quarter |

### System Touchpoints
- Waste tracking module with material category and weight logging
- Vendor master for accredited scrap collectors (W36)
- Cash handling and revenue recognition module (W541, W714)
- Store P&L reporting (W67, W489)
- ESG data collection module (W192, W694)
- Waste diversion rate analytics dashboard
- DENR waste reporting integration (W433)

### Pain Points / Risks
- **Theft risk**: Scrap metal (especially copper and aluminum) has high street value and is a common theft target; scrap bins must be in secured receiving dock area (not accessible to customers); collector access logged per W581 (Vendor Representative Access); CCTV coverage per W838
- **Accreditation integrity**: Scrap collector must be DENR-accredited per W82 and properly registered as BuildRight vendor per W36; unaccredited collectors may illegally dump materials or resell to unregistered smelters; Finance team should verify collector accreditation annually
- **Revenue accuracy**: Manual weighing creates opportunity for under-weighing (collector benefit) or over-reporting (staff collusion); calibrated scale with digital readout and CCTV at weighing point per W838 mitigates risk; Department Supervisor must co-sign all weigh tickets
- **PFRS revenue recognition**: Scrap revenue is peripheral to BuildRight's core retail business; PFRS 15 requires recognition when collection occurs and payment is received; revenue should be immaterial to financial statements but must be properly recorded for tax compliance (BIR requires declaration of all income)

### Staffing Implication
- **Maintenance Staff**: Weekly collection adds ~30–45 min/week; absorbed by existing Maintenance/Utility Staff
- **Department Supervisor**: Revenue recording and quarterly reporting adds ~15–20 min/week + 30–60 min/quarter
- **No incremental headcount**

### Time Estimate
- Daily segregation: 5–10 min/day per staff (absorbed into workflow)
- Weekly collection: 30–45 min/week
- Revenue recording: 10–15 min/week
- Quarterly reporting: 30–60 min/quarter
- **Total per store per week**: ~45–70 min dedicated time

---

## W1018. Customer Project Progress Payment Verification & Invoice Matching

| Field | Detail |
|---|---|
| **Trigger** | Project milestone completion triggers progress billing per project contract terms |
| **Frequency** | ~300–500 progress billing events/month across all active B2B projects |
| **Volume** | 1–3 milestone invoices per project per month; ~150–200 active projects at any time |
| **Owner** | Project Account Manager |
| **Participants** | Project Coordinator, Delivery Supervisor, Customer Project Manager, AR Analyst, Credit Manager |

### Background

BuildRight Depot's project-based B2B sales (W162–W166) involve staged deliveries and progress billing for large construction and renovation projects. A typical corporate project: (a) contract signed for PHP 5–50M in materials over 3–12 months; (b) materials delivered in phases aligned with construction milestones (foundation, structural, finishing); (c) billing tied to delivery milestones with progress payment terms (e.g., 30% on contract signing, 30% at structural completion, 30% at finishing, 10% retention payable 90 days after project completion per W165). Each progress billing must be matched against: delivered quantities (GR per project site), contracted prices (project price book per W163), and any approved change orders (W792). Verification is critical because: (a) billing ahead of delivery violates PFRS 15 revenue recognition (revenue must be earned before recognized); (b) billing below delivery value creates cash flow pressure; (c) mismatched billing causes customer disputes and delayed payment. Philippine B2B projects frequently experience scope changes, quantity adjustments, and delivery discrepancies — this workflow ensures accurate, timely billing that maintains customer trust and protects BuildRight's revenue.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Milestone Delivery Verification**: Project Coordinator confirms milestone delivery completion: (a) all scheduled deliveries for the milestone period have been completed per W164 (Staged Project Delivery); (b) delivery receipts signed by customer's project representative at each site; (c) Goods Receipt confirmed in system per delivery; (d) any delivery discrepancies (short quantities, damaged items) resolved per W500 (Transfer Order In-Transit Damage); (e) change orders (W792) executed during the milestone period are completed and signed off by customer; (f) Project Coordinator certifies milestone delivery completion with supporting documentation | Project Coordinator | Project Account Manager | 30–60 min per milestone |
| 2 | **Progress Invoice Generation**: AR Analyst generates progress invoice: (a) system aggregates all GR-confirmed deliveries for the milestone period; (b) quantities matched against project contract price book (W163) — unit prices, applicable discounts, and terms; (c) change order items priced per approved change order (W792) — including margin re-impact assessment; (d) retained amounts per contract terms (e.g., 10% retention) deducted from current billing and tracked separately; (e) VAT computed per BIR requirements (12% output VAT on taxable items); (f) invoice generated: itemized by material category with delivery dates, quantities, unit prices, and totals; (g) BIR-registered sales invoice per DOC-002 with project reference and milestone number | AR Analyst / System | Project Account Manager | 20–40 min per invoice |
| 3 | **Internal Three-Way Verification**: Before sending to customer: (a) AR Analyst performs three-way match: **Contract Price Book** × **Actual Deliveries (GR)** × **Progress Invoice**; (b) verify: all delivered items are invoiced (no unbilled deliveries), all invoiced items were delivered (no unbilled delivery), quantities match (no quantity discrepancy), prices match contract (no pricing errors); (c) flag exceptions: items delivered but not in contract (change order items — verify approved), items in contract but not yet delivered (backorder — do not bill); (d) Project Account Manager reviews and approves invoice; (e) Credit Manager verifies total outstanding exposure remains within approved credit limit per W572 | AR Analyst / Project Account Manager | Credit Manager | 15–30 min per invoice |
| 4 | **Customer Invoice Presentation & Dispute Resolution**: (a) invoice delivered to customer Project Manager with supporting delivery receipts and GR documentation; (b) customer reviews against their own project records; (c) if customer disputes: handled per W1022 (Trade Account Statement Dispute); (d) common disputes: quantity discrepancy (customer says they received less than invoiced), quality issue (customer claims damaged items should not be billed), price dispute (customer claims agreed price differs from invoiced); (e) AR Analyst investigates with Project Coordinator: delivery documentation, site photos, GR sign-off; (f) if dispute valid: credit memo issued per W101; if dispute rejected: provide evidence to customer; (g) SLA: dispute resolution within 10 business days | AR Analyst / Project Account Manager | Credit Manager | 15–60 min per dispute |
| 5 | **Payment Collection & Retention Management**: (a) customer pays progress invoice per contract terms (typically Net 30 from invoice date); (b) payment collected per W108 (AR & Collections); (c) retention amounts tracked in separate retention receivable account; (d) retention released per contract terms (typically 90 days after project completion and sign-off per W793); (e) final retention release triggers: project completion certificate from customer, no outstanding claims or disputes, all warranties registered per W1016; (f) project margin analysis: actual revenue vs. contract value, actual COGS, gross margin %, margin impact of change orders per W918 | AR Analyst / Credit Manager | Credit Manager | 10–20 min per payment |

### System Touchpoints
- Project management module with milestone tracking (W162–W166)
- Delivery receipt and GR system with project tagging
- Contract price book module (W163)
- Change order management (W792) with margin impact tracking
- Progress billing module with automated invoice generation
- Three-way match engine (contract × delivery × invoice)
- Credit limit monitoring (W572, W888)
- AR aging and collection system (W108, W889)
- Retention receivable tracking with automated release scheduling
- BIR-compliant sales invoice generation (DOC-002)
- Project profitability analytics (W918)

### Pain Points / Risks
- **Billing lag**: Manual milestone verification and invoice generation can take 5–10 business days after milestone completion, delaying cash collection; system automation of invoice generation (step 2) reduces billing cycle to 2–3 days
- **PFRS 15 revenue recognition**: Progress billing must be matched to actual delivery completion per PFRS 15; billing ahead of delivery (common in Philippine construction practice where "down payments" are requested) must be recorded as customer deposit (W94) and not recognized as revenue until delivery occurs
- **Retention collection risk**: 10% retention across 150–200 active projects represents PHP 50–100M in outstanding retention receivables; retention is at risk if customer disputes project quality or becomes insolvent before retention release; Credit Manager should monitor retention aging and escalate overdue retention per W108
- **Scope creep and unbilled work**: Change orders executed verbally without formal documentation per W792 lead to unbilled work; Project Coordinator must document all scope changes before execution and obtain customer sign-off before delivery

### Staffing Implication
- **AR Analyst**: Progress billing adds ~20–40 min per invoice; at ~300–500 invoices/month, this is ~100–330 hours/month; distributed across AR team
- **Project Account Manager**: Verification and approval adds ~15–30 min per invoice
- **No incremental headcount** (absorbed by existing Finance & Accounting team of 37 staff)

### Time Estimate
- Delivery verification: 30–60 min per milestone
- Invoice generation: 20–40 min per invoice
- Internal verification: 15–30 min per invoice
- Customer presentation: 15–60 min per dispute
- Payment collection: 10–20 min per payment
- **Total per progress billing event**: 90–210 min

---

## W1019. Store-Level Construction Material Safety Data Sheet (SDS) Customer Access & Compliance

| Field | Detail |
|---|---|
| **Trigger** | Customer requests SDS for a purchased product; regulatory requirement for SDS availability |
| **Frequency** | ~2,000–3,000 SDS requests/month chain-wide (~10–15/store/month); continuous SDS compliance maintenance |
| **Volume** | 1 SDS per product per request; ~800–1,200 SDS documents maintained per store |
| **Owner** | Department Supervisor (safety liaison) |
| **Participants** | Sales Associate, Customer, Environmental Compliance Officer (regional), Category Manager |

### Background

BuildRight Depot sells ~2,800 paint & finishes SKUs, ~1,750 adhesives and sealants, and various solvents, chemicals, and treated lumber products classified as hazardous or potentially hazardous. Under Philippine DENR AO 2013-22 (Toxic Chemicals and Hazardous Wastes) and DOLE Department Order 136-14 (Chemical Safety), Safety Data Sheets (SDS, formerly MSDS) must be available for all hazardous chemicals in the workplace. While this primarily applies to BuildRight's own employees, the Consumer Act (RA 7394) and DENR regulations also create an expectation that retailers make product safety information available to consumers upon request. An SDS provides critical information: product identification, hazard identification, composition, first-aid measures, fire-fighting measures, handling and storage, exposure controls, physical properties, stability, toxicological information, ecological information, disposal considerations, and transport information. Currently, SDS documents are maintained in binders at the store level (often incomplete or outdated) with no digital access. This workflow establishes a digital SDS library accessible to both staff (via ERP) and customers (via QR code on shelf labels), ensures SDS currency, and supports DENR compliance per W698 (SDS Lifecycle Management).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **SDS Digital Library Maintenance**: Environmental Compliance Officer (regional) maintains the SDS digital library: (a) all hazardous product SKUs require an SDS on file before product can be sold (SDS gate in SKU creation per W252); (b) SDS sourced from manufacturer/vendor during vendor onboarding (W36) and updated per vendor revision schedule (typically every 3 years or when formulation changes); (c) SDS must comply with GHS (Globally Harmonized System) format — 16 sections per DENR AO 2013-22; (d) SDS reviewed for completeness and Philippine-specific regulatory information (BIR registration not required, but DENR and DOLE references must be accurate); (e) digital SDS stored in document management system per W255 with product SKU linkage; (f) SDS version tracking: current version, previous versions, revision dates; (g) any SDS older than 3 years flagged for vendor refresh request per W698 | Environmental Compliance Officer / Category Manager | Category Manager | Ongoing: 8–12 hours/month chain-wide |
| 2 | **Shelf Label QR Code Integration**: For all products requiring SDS: (a) shelf label includes QR code that links to the product's current SDS in the digital library; (b) customer scans QR code with smartphone → opens SDS in mobile-friendly format (language options: English and Filipino); (c) alternatively, customer can search by product name or SKU on buildright.com.ph/sds; (d) SDS access is free and does not require login; (e) system tracks SDS access analytics: most-accessed products, access frequency by store; (f) QR code printing integrated into shelf label process per W181 | System / Category Manager | Category Manager | Automated (QR code generation per SKU) |
| 3 | **In-Store Customer SDS Request Handling**: When customer requests SDS in-store: (a) Sales Associate searches product in ERP terminal; (b) system displays SDS availability status (current, outdated, missing); (c) if SDS available: Sales Associate prints SDS for customer from in-store printer (BIR-compliant format per DOC-002 is not required for SDS; standard A4 printout sufficient); or directs customer to scan shelf QR code; (d) if SDS outdated or missing: Sales Associate informs customer that SDS will be emailed within 24 hours; system generates SDS request ticket sent to Environmental Compliance Officer; (e) SDS request logged for compliance tracking | Sales Associate | Department Supervisor | 5–10 min per request |
| 4 | **Employee SDS Access & Training**: All employees handling hazardous products must have access to SDS: (a) ERP terminal in each department provides instant SDS lookup; (b) during safety training per W51 and W237 (Hazmat Safety Training), employees trained on SDS structure and how to find critical information (first aid, PPE requirements, spill response); (c) new employees receive SDS awareness training during onboarding per W15; (d) annual refresher: quiz on SDS interpretation included in safety certification per W655; (e) in emergency (customer exposure, spill): employee accesses SDS via ERP terminal or mobile app for immediate first-aid guidance per W501 | All Store Staff / System | Department Supervisor | Training: 2 hours/year per employee |
| 5 | **Regulatory Compliance Audit & Reporting**: Quarterly: (a) Environmental Compliance Officer audits SDS coverage rate: % of hazardous SKUs with current SDS on file (target: 100%); (b) audit sample: 20 SKUs per store, verify SDS currency and QR code functionality; (c) stores with coverage < 95%: corrective action plan with 30-day remediation deadline; (d) SDS compliance metrics included in DENR SMR/CMR reporting per W433; (e) annual: full SDS library audit — every SDS reviewed for currency, accuracy, and GHS compliance; (f) SDS compliance score included in store safety KPI per W67 | Environmental Compliance Officer | Category Manager | Quarterly: 4–6 hours; Annual: 15–20 hours |

### System Touchpoints
- SDS digital library in document management system (W255, W698)
- Shelf label QR code generation module (W181)
- ERP product master with SDS linkage and currency flag
- Customer-facing SDS web portal (buildright.com.ph/sds)
- SDS request ticketing system
- Employee training module (W51, W237)
- DENR compliance reporting (W433)
- Mobile app SDS viewer

### Pain Points / Risks
- **SDS coverage gaps**: New product introductions (W564, W788) may be fast-tracked to shelves before SDS is obtained from vendor; SKU creation workflow (W252) must enforce SDS gate — no product can be activated for sale without SDS on file for hazardous categories
- **Language accessibility**: Most vendor-provided SDS are in English; Philippine customers (especially DIY homeowners) may struggle with technical language; Filipino-language summary hazard pictograms and first-aid instructions should supplement the full English SDS
- **Vendor SDS timeliness**: Some vendors (especially smaller Philippine manufacturers) are slow to provide updated SDS; Environmental Compliance Officer must follow up aggressively; products without current SDS should be flagged for potential delisting per W698
- **QR code maintenance**: If product SDS is updated but shelf label QR code still points to old version, customers receive outdated safety information; QR codes should link to a dynamic URL that always serves the current SDS version (not a static PDF URL)

### Staffing Implication
- **Environmental Compliance Officer**: SDS library maintenance adds ~8–12 hours/month chain-wide; absorbed by existing regional Environmental Compliance Officer role
- **Sales Associate**: Customer SDS requests add ~5–10 min/request × 10–15 requests/month = 50–150 min/month; absorbed by existing staff
- **No incremental headcount**

### Time Estimate
- Library maintenance: 8–12 hours/month (centralized)
- Customer request handling: 5–10 min per request
- Employee training: 2 hours/year per employee
- Compliance audit: 4–6 hours/quarter
- **Per store per month**: ~60–150 min (customer requests + training)

---

## W1020. Vendor Consignment Inventory Physical Count & Periodic Reconciliation

| Field | Detail |
|---|---|
| **Trigger** | Monthly scheduled reconciliation and quarterly wall-to-wall physical count of consignment inventory |
| **Frequency** | Monthly reconciliation × 200 stores; quarterly physical count × 200 stores |
| **Volume** | ~300 consignment SKUs from 12 key vendors (Section 6.5) across all stores; ~15–25 consignment SKUs per store |
| **Owner** | Inventory Analyst |
| **Participants** | Stock Associate, Department Supervisor, Vendor Account Manager, AP Analyst |

### Background

BuildRight Depot carries ~300 consignment SKUs from 12 key vendors (Section 6.5, INV-009, INV-017). Consignment items are physically present in the store but remain vendor-owned until sold to a customer — ownership transfers at the point of sale. Consignment inventory is not on BuildRight's balance sheet (not valued in WAC inventory) until sold, at which point BuildRight recognizes COGS and records a payable to the vendor. This creates a unique reconciliation challenge: BuildRight's system must track: (a) physical quantity on hand (what's actually in the store); (b) system quantity on hand (what ERP thinks is in the store based on sales since last replenishment); (c) vendor's system quantity (what the vendor believes is at the store based on their shipment and sell-through data). Discrepancies between these three views are common due to: unrecorded sales (offline POS, system downtime per W535), theft/shrinkage (consignment items are often high-value — appliances, premium tiles), and receiving discrepancies (vendor ships more/less than documented). Monthly reconciliation ensures BuildRight pays the vendor only for items actually sold, and quarterly physical counts catch accumulated drift. Unresolved discrepancies impact vendor relationships and BuildRight's margin on consignment sales (~8–15% commission vs. regular margin of 28–32%).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Monthly System Reconciliation**: Monthly: (a) Inventory Analyst runs system reconciliation report per vendor per store: system on-hand quantity vs. vendor-reported on-hand quantity; (b) system on-hand calculated as: opening balance + receipts since last reconciliation − POS sales since last reconciliation − adjustments (returns, damages, write-offs); (c) vendor on-hand calculated from: vendor's last confirmed physical count + vendor shipments − vendor-reported sell-through data (from POS integration per W543); (d) discrepancy = system on-hand − vendor on-hand; (e) acceptable tolerance: ±2% of quantity or ±3 units (whichever is greater); (f) discrepancies outside tolerance flagged for investigation | System / Inventory Analyst | Inventory Analyst | 30–60 min/month per vendor (centralized) |
| 2 | **Discrepancy Investigation**: For flagged discrepancies: (a) Inventory Analyst requests store-level investigation: Stock Associate performs spot count of consignment items for the specific vendor; (b) common causes: (i) unrecorded sales during POS offline mode (W535) — resolved by uploading offline transaction logs; (ii) theft/shrinkage — identified if physical count < system count; investigated per W837 (LP Exception Reporting); (iii) receiving discrepancy — vendor shipped more/less than recorded; cross-referenced with delivery receipts; (iv) return not recorded — customer returned consignment item but return not coded as consignment return; (v) inter-store transfer without consignment flag — item moved but ownership tracking not updated | Stock Associate / Inventory Analyst | Inventory Analyst | 15–30 min per discrepancy |
| 3 | **Quarterly Physical Wall-to-Wall Count**: Quarterly: (a) Stock Associate counts all consignment inventory in store — physical count by SKU by location; (b) count recorded on RF gun with SKU barcode scan; (c) system compares physical count to system on-hand; (d) physical count to vendor on-hand; (e) three-way reconciliation: physical vs. system vs. vendor; (f) any physical count discrepancy (system vs. physical): (i) if physical < system (shrinkage): inventory adjustment per W92 with consignment shrinkage disposition code; vendor notified — BuildRight pays for lost items (shrinkage is BuildRight's liability per consignment agreement, similar to owned inventory); (ii) if physical > system (unrecorded receipt or system error): investigate and correct; (g) results documented and shared with vendor | Stock Associate / Inventory Analyst | Inventory Analyst | 60–120 min per store per quarter |
| 4 | **Vendor Settlement Reconciliation**: Monthly: (a) AP Analyst reconciles vendor consignment settlement: (i) POS sell-through data: quantity sold × agreed consignment price = amount payable to vendor; (ii) adjustments: shrinkage (BuildRight bears cost), returns to vendor (W88), damaged items (W91); (iii) net settlement = sell-through amount + shrinkage cost − returns; (b) settlement statement generated per vendor with line-by-line detail; (c) vendor reviews settlement statement via vendor portal (W867); (d) vendor confirms or disputes; (e) if confirmed: AP processes payment per FIN-043 (Payment Run); (f) if disputed: reconciled per W869 (Vendor Dispute Resolution); (g) GL entries: debit COGS (consignment), credit AP (vendor); ownership transfer recorded at POS per W543 | AP Analyst / System | Inventory Analyst | 30–60 min/month per vendor |
| 5 | **Consignment Performance Review**: Quarterly: (a) Inventory Analyst compiles consignment performance dashboard: sell-through rate by SKU by store, shrinkage rate, days on hand, margin (commission) vs. owned inventory margin; (b) identify slow-moving consignment SKUs: items with < 2 units sold/month/store for 3 consecutive months; (c) recommend action: (i) maintain (seasonal item, strategic value), (ii) convert to owned inventory (if selling well, better margin), (iii) return to vendor (if not selling, occupying valuable shelf space), (iv) replace with faster-moving consignment SKU; (d) review results shared with Category Manager for vendor negotiation per W155 (Vendor Strategic Collaboration) | Inventory Analyst | Category Manager | 2–3 hours/quarter |

### System Touchpoints
- Consignment inventory tracking module (INV-009, INV-017)
- POS sell-through recording with consignment flag (W543)
- Receiving module with consignment receipt tracking (non-valuated)
- Three-way reconciliation engine (physical × system × vendor)
- Vendor portal settlement statement (W867)
- AP payment processing (FIN-043)
- Inventory adjustment module (W92) with consignment disposition codes
- Consignment performance analytics dashboard
- Cycle counting module (W6) with consignment category

### Pain Points / Risks
- **Ownership ambiguity**: During physical counts, store staff may not distinguish consignment from owned inventory (especially if items look identical); consignment items must have distinct shelf labels/tags indicating "Consignment — Vendor-Owned" per INV-017; RFID or barcode prefix differentiation helps
- **Shrinkage liability**: Consignment shrinkage (theft, damage) is BuildRight's liability per standard consignment agreements; BuildRight pays the vendor for items stolen or damaged on BuildRight's premises; high-value consignment items (appliances, premium tiles) should have EAS tags per W844
- **Vendor data mismatch**: If vendor's sell-through data doesn't match BuildRight's POS data (due to timing differences, offline transactions, or integration errors), reconciliation becomes contentious; real-time sell-through data sharing per W422 (VMI Data Sharing) reduces mismatch
- **Shelf space opportunity cost**: Consignment SKUs occupying shelf space that could be used for higher-margin owned inventory must be continuously evaluated; slow-moving consignment items erode overall category profitability

### Staffing Implication
- **Inventory Analyst**: Consignment reconciliation adds ~4–6 hours/month centralized; absorbed by existing Inventory Analyst or Supply Chain team
- **Stock Associate**: Quarterly physical count adds ~60–120 min/store/quarter; absorbed by existing 3 Stock Associates per store
- **AP Analyst**: Settlement reconciliation adds ~30–60 min/vendor/month; absorbed by existing AP team
- **No incremental headcount**

### Time Estimate
- Monthly system reconciliation: 30–60 min/vendor/month (centralized)
- Discrepancy investigation: 15–30 min per discrepancy
- Quarterly physical count: 60–120 min/store
- Vendor settlement: 30–60 min/vendor/month
- Quarterly performance review: 2–3 hours/quarter
- **Per store per month**: ~30–60 min (Stock Associate) + centralized analysis

---

## W1021. Store-Level Loading Dock Equipment Maintenance & Safety Inspection

| Field | Detail |
|---|---|
| **Trigger** | Monthly scheduled maintenance; triggered by equipment malfunction or safety concern |
| **Frequency** | Monthly preventive maintenance × 200 stores; daily visual check |
| **Volume** | 1–2 loading docks per store; equipment: dock leveler, dock seal/shelter, dock light, dock bumper, door/gate |
| **Owner** | Maintenance/Utility Staff |
| **Participants** | Department Supervisor (Receiving), External Maintenance Contractor, Safety Officer (regional) |

### Background

Each BuildRight Depot store has 1–2 loading docks at the receiving area where inbound deliveries (DC replenishment trucks, DSD vendor trucks) and outbound customer deliveries (bulky item delivery) are loaded and unloaded. Loading dock equipment includes: hydraulic or mechanical dock levelers (bridge the gap between truck bed and dock floor), dock seals/shelters (weatherproof the truck-to-building connection), dock bumpers (protect building wall from truck impact), dock lights (illuminate truck interior for safe unloading), and overhead doors or rolling gates. Equipment failure creates safety hazards: a malfunctioning dock leveler can cause forklift tip-over (serious injury risk), a damaged dock seal allows rain ingress (product damage), and a broken dock light creates poor visibility (trip/slip hazard). Loading dock accidents are among the top causes of warehouse injuries globally — truck creep (truck slowly rolling away from dock during unloading), dock plate failure, and falls from dock height. Philippine stores face additional challenges: heavy tropical rainfall testing dock seals, salt-air corrosion in coastal store locations, and uneven truck bed heights from the diverse Philippine truck fleet (6-wheelers to 18-wheelers).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Daily Visual Safety Check**: Receiving Clerk performs daily visual check before receiving operations: (a) dock leveler: verify plate sits flush with dock floor when retracted, no visible damage or warping, safety legs/struts functional; (b) dock bumper: verify rubber bumpers intact, not compressed beyond 50% of original thickness; (c) dock seal/shelter: verify foam pads intact, fabric not torn, head curtain functional; (d) dock light: verify operational, bright enough to illuminate truck interior; (e) overhead door/gate: opens and closes smoothly, no unusual noises, safety sensors functional; (f) dock area floor: clean, no standing water, no oil/grease spills, no cracks or uneven surfaces; (g) wheel chocks available and in good condition; (h) any safety concern: dock taken out of service until resolved; receiving rerouted to alternative dock or manual unloading | Receiving Clerk | Department Supervisor | 5–10 min/day |
| 2 | **Monthly Preventive Maintenance**: Monthly: Maintenance Staff performs scheduled maintenance: (a) **Dock leveler**: lubricate hinges and moving parts per manufacturer schedule; check hydraulic fluid level (hydraulic models); test safety legs and automatic return mechanism; verify lip extension reaches minimum 10 cm onto truck bed at all common truck heights; check for metal fatigue or cracks in platform; (b) **Dock bumper**: measure remaining rubber thickness — replace if < 50% original; verify mounting bolts tight; (c) **Dock seal/shelter**: clean fabric, check for tears or UV degradation (tropical sun accelerates fabric deterioration), replace foam pads if compressed >30%; (d) **Dock light**: replace bulbs/LED if dimming, clean lens, verify articulating arm holds position; (e) **Overhead door**: lubricate tracks and rollers, check spring tension, test auto-reverse safety mechanism; (f) **General**: clear floor drains in dock area, check for water pooling, verify exterior lighting for nighttime deliveries; (g) all maintenance logged in equipment management system per W188 | Maintenance Staff / External Contractor | Department Supervisor | 60–90 min/month |
| 3 | **Quarterly Safety Inspection**: Quarterly: (a) Safety Officer (regional) conducts dock safety inspection: (i) dock leveler load capacity rating verified against actual use (forklift + load weight must not exceed rated capacity); (ii) dock height and leveler range verified against BuildRight truck fleet specifications (dock must accommodate truck bed heights from 100–160 cm); (iii) safety signage posted: maximum speed, wheel chock requirement, no unauthorized personnel; (iv) dock area CCTV coverage verified per W838; (v) emergency stop button accessible and functional; (b) inspection report filed in safety management system; (c) any critical findings: dock taken out of service until remediated; (d) non-critical findings: scheduled for repair within 14 days | Safety Officer / Department Supervisor | Store Manager | 30–45 min/quarter |
| 4 | **Emergency Repair & Escalation**: When dock equipment fails during operations: (a) Receiving Clerk immediately stops unloading at affected dock; (b) dock taken out of service with physical barrier and signage; (c) if alternative dock available: receiving operations shifted; if no alternative: manual unloading (increased time, additional staff needed); (d) Maintenance Staff assesses: minor repair (performed in-house, same-day) vs. major repair (external contractor, 1–3 days); (e) emergency repair request submitted per W47 with "safety-critical" priority; (f) external contractor dispatched same-day for safety-critical repairs; (g) dock returned to service only after Maintenance Staff verification and Safety Officer sign-off (for safety-critical items) | Receiving Clerk / Maintenance Staff | Department Supervisor | Per event: 15–60 min assessment + repair time |

### System Touchpoints
- Equipment management module (W188, W47) with dock equipment asset tracking
- Daily safety checklist module
- Monthly PM scheduling system with task lists per equipment type
- Safety inspection report module (W140, W436)
- Emergency repair request system (W47)
- Contractor management module (W242)

### Pain Points / Risks
- **Dock leveler failure during truck unloading**: A dock leveler that fails while a forklift is on it can cause the forklift to tip or fall — catastrophic safety risk; daily visual check and monthly maintenance are non-negotiable; if any doubt about leveler integrity, dock must be taken out of service immediately
- **Truck creep**: Philippine trucks on inclines (many store receiving areas are not perfectly level) may slowly roll during unloading; wheel chocks are mandatory; drivers must set chocks before dock plate is extended; dock lock systems (vehicle restraint) should be considered for new store construction per W223
- **Coastal corrosion**: Stores in coastal locations (Cebu, coastal Mindanao, Bicol) experience accelerated metal corrosion on dock equipment; stainless steel or galvanized components should be specified per W223 (New Store Design); more frequent inspections (monthly instead of quarterly) for coastal stores
- **Rainwater intrusion**: Failed dock seals during tropical downpours cause significant water damage to inbound merchandise; dock seal integrity is particularly critical during rainy season (June–November); Maintenance Staff should inspect dock seals weekly during rainy season

### Staffing Implication
- **Maintenance Staff**: Daily check (absorbed by Receiving Clerk); monthly PM adds ~60–90 min/month; absorbed by existing Maintenance/Utility Staff (1 per store)
- **Receiving Clerk**: Daily visual check adds ~5–10 min/day; absorbed by existing 2 Receiving Clerks
- **No incremental headcount**

### Time Estimate
- Daily visual check: 5–10 min/day
- Monthly preventive maintenance: 60–90 min/month
- Quarterly safety inspection: 30–45 min/quarter
- Emergency repair: variable
- **Ongoing weekly**: ~35–70 min/week (daily checks) + 60–90 min/month (PM)

---

## W1022. Customer Trade Account Statement Dispute & Resolution Processing

| Field | Detail |
|---|---|
| **Trigger** | Trade account customer disputes line items on their AR statement or consolidated invoice |
| **Frequency** | ~400–600 disputes/month across ~5,200 trade accounts (~8–10% dispute rate) |
| **Volume** | 1–5 disputed line items per dispute event |
| **Owner** | AR Analyst |
| **Participants** | Customer (B2B), Sales Associate/Store, AR Analyst, Credit Manager, AP Analyst (for vendor-side resolution) |

### Background

BuildRight Depot's ~5,200 trade account customers (Section 9.2) receive monthly statements (W892) or consolidated invoices (W1014) listing all transactions for the billing period. Approximately 8–10% of statements generate disputes — common reasons include: (a) **pricing disputes** (customer believes trade discount was not applied, or promotional price differs from invoiced price); (b) **quantity disputes** (customer claims they received fewer items than invoiced — receiving discrepancy or delivery shortage); (c) **unrecognized transactions** (customer doesn't recognize a charge — possible mis-posting to wrong account or fraudulent use of trade account); (d) **duplicate billing** (same transaction appears twice — system error or re-invoicing); (e) **credit memo not reflected** (customer returned items per W12 but credit memo not yet applied); (f) **payment not credited** (customer paid but payment not yet posted to their account — timing difference or misallocation). Timely dispute resolution is critical for customer satisfaction and cash collection — disputed amounts are typically withheld from payment, reducing BuildRight's cash position. SLA: initial response within 48 hours, resolution within 10 business days for standard disputes, 20 business days for complex disputes requiring vendor or third-party involvement.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Dispute Receipt & Logging**: Customer submits dispute: (a) via B2B self-service portal (W936) — customer selects disputed line items and enters dispute reason and supporting documentation; (b) via email to AR team — AR Analyst manually logs dispute in system; (c) via phone to Customer Service — agent logs dispute and assigns to AR Analyst; (d) system generates dispute ticket with unique tracking number; (e) customer receives acknowledgment within 4 hours with expected resolution timeline; (f) disputed amounts flagged in AR aging — excluded from collection activity per W108 while dispute is open (prevents over-aggressive collection on disputed amounts) | Customer / AR Analyst / Customer Service Agent | AR Analyst | 5–10 min per dispute |
| 2 | **Initial Investigation & Classification**: AR Analyst investigates: (a) **Pricing dispute**: verify POS transaction price vs. trade price agreement (W163) and any active promotions (W13); check if cashier applied correct trade discount at POS; (b) **Quantity dispute**: verify delivery receipt (DR) quantities vs. invoice quantities; check Goods Receipt record at customer site (if available) or store delivery confirmation (W592); (c) **Unrecognized transaction**: verify customer account assignment — was transaction posted to correct account? Check loyalty card number used at POS vs. trade account number; (d) **Duplicate billing**: system auto-checks for duplicate invoice numbers, same amount/same date/same items; (e) **Missing credit memo**: check if return was processed per W12 and credit memo generated per W101; verify credit memo posting to account; (f) **Payment not credited**: check bank statement for customer payment per W89; verify payment allocation to correct account | AR Analyst | Credit Manager | 15–45 min per dispute |
| 3 | **Internal Resolution & Documentation**: Based on investigation: (a) **Dispute valid — BuildRight error**: (i) pricing error: credit memo issued for difference per W101; (ii) quantity error: if customer was overbilled, credit memo for excess quantity; if underbilled, customer notified and additional invoice issued; (iii) duplicate billing: duplicate invoice reversed; (iv) missing credit memo: credit memo re-issued; (v) payment misallocated: payment re-posted to correct account; (b) **Dispute valid — third-party error** (e.g., delivery partner lost goods): AR Analyst coordinates with logistics team; claim filed with carrier per W610; customer issued credit memo pending carrier recovery; (c) **Dispute invalid**: AR Analyst documents evidence (delivery receipt signed by customer, POS price file showing correct trade price, Goods Receipt confirmation) and responds to customer with supporting documentation; (d) **Partially valid**: partial credit memo for agreed portion; remaining disputed amount escalated to Credit Manager for judgment call | AR Analyst | Credit Manager | 15–30 min per dispute |
| 4 | **Customer Communication & Resolution Confirmation**: (a) AR Analyst communicates resolution to customer: email with dispute tracking number, investigation summary, and resolution action taken; (b) if credit memo issued: amount and credit memo number specified; customer sees credit on next statement; (c) if additional invoice issued: customer notified with explanation and payment terms; (d) if dispute rejected: evidence provided; customer may escalate to Credit Manager; (e) customer confirms resolution by acknowledging in B2B portal, email response, or phone confirmation; (f) disputed amounts unblocked in AR aging; undisputed portion of withheld payment becomes due per original terms | AR Analyst | Credit Manager | 10–15 min per dispute |
| 5 | **Dispute Analytics & Systemic Issue Identification**: Monthly: (a) AR Analyst compiles dispute analytics: dispute volume by type, by store, by customer; resolution time by type; dispute rate trend; credit memo value from disputes; (b) identify systemic issues: (i) specific store with high pricing dispute rate → retraining per W518 (Cashier Training); (ii) specific product category with high quantity disputes → receiving process review per W666; (iii) specific customer with recurring disputes → account review per W328 (Credit Limit Review); (c) systemic issues reported to: Store Manager (store-level issues), Category Manager (pricing issues), Supply Chain Manager (delivery issues); (d) quarterly: dispute analytics included in credit portfolio review per W663 | AR Analyst / Credit Manager | Credit Manager | 2–3 hours/month |

### System Touchpoints
- Dispute management module with ticket tracking and SLA monitoring
- B2B self-service portal (W936) for customer dispute submission
- AR aging system with dispute flag and payment hold functionality
- POS transaction lookup with price audit trail
- Delivery receipt and Goods Receipt verification (W109, W3)
- Credit memo module (W101, W766)
- Bank reconciliation (W89) for payment verification
- Duplicate invoice detection (FIN-020)
- Dispute analytics dashboard with root cause categorization

### Pain Points / Risks
- **High dispute volume on aging AR**: Disputed amounts sitting in AR aging distort the true aging profile; credit collection team must distinguish disputed vs. genuinely overdue amounts; AR aging reports should have a "disputed" column separate from "current", "30-day", "60-day", "90-day+" buckets
- **Evidence availability**: Dispute resolution depends on documentation availability; if delivery receipts were not collected or Goods Receipt was not recorded at the customer site, BuildRight has limited evidence to defend its position; digitizing all delivery documentation per W255 and W592 is critical
- **Customer relationship balance**: Aggressive dispute rejection damages customer relationships; AR Analyst should approach disputes with a "customer-first" mindset — if evidence is ambiguous, lean toward customer-favorable resolution for trade accounts with good payment history and high lifetime value
- **Timeliness**: Philippine B2B customers expect rapid dispute resolution; if BuildRight takes > 10 business days, customers may withhold future payments or switch to competitors; SLA monitoring (step 4) and escalation for overdue disputes are essential

### Staffing Implication
- **AR Analyst**: Dispute resolution adds ~45–100 min per dispute × 400–600 disputes/month = ~300–1,000 hours/month; distributed across existing AR team (37 Finance & Accounting staff includes AR Analysts)
- **Credit Manager**: Escalation review adds ~5–10 hours/month
- **No incremental headcount**

### Time Estimate
- Dispute logging: 5–10 min
- Investigation: 15–45 min
- Resolution & documentation: 15–30 min
- Customer communication: 10–15 min
- **Total per dispute**: 45–100 min
- Monthly analytics: 2–3 hours
