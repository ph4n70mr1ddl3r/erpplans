# Installation & Value-Added Services Workflows

> Home installation, tool rental, DIY workshops & in-store events, design consultancy, custom paint mixing & tinting, lumber & board cutting, in-store 3D kitchen/bathroom design rendering, installation service partner quality audit, and service contractor accreditation & onboarding management.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W138. Home Installation Services Management](#w138-home-installation-services-management)
- [W139. Tool & Equipment Rental Operations](#w139-tool-equipment-rental-operations)
- [W147. DIY Workshop & In-Store Event Management](#w147-diy-workshop-in-store-event-management)
- [W148. Home Design & Consultancy Services](#w148-home-design-consultancy-services)
- [W211. In-Store 3D Kitchen/Bathroom Design Rendering](#w211-in-store-3d-kitchenbathroom-design-rendering)
- [W168. Custom Paint Mixing & Tinting Operations](#w168-custom-paint-mixing-tinting-operations)
- [W169. Lumber & Board Cutting Services](#w169-lumber-board-cutting-services)
- [W213. Installation Service Partner Quality Audit](#w213-installation-service-partner-quality-audit)
- [W282. Subscription Billing for Recurring Home Services](#w282-subscription-billing-for-recurring-home-services)
- [W442. Site Technical Survey & Measurement Services](#w442-site-technical-survey-measurement-services)
- [W600. Service Contractor Accreditation & Onboarding Management](#w600-service-contractor-accreditation--onboarding-management)
- [W794. Service SKU Catalog Management, Pricing & Material Linkage](#w794-service-sku-catalog-management-pricing--material-linkage)
- [W795. Service Customer Complaint, Rework & Warranty Claim Management](#w795-service-customer-complaint-rework--warranty-claim-management)

---

## W138. Home Installation Services Management

| Field | Detail |
|---|---|
| **Trigger** | Customer purchases installation-eligible product (e.g., split-type AC, water heater, floor tiles) and requests service |
| **Frequency** | Daily across 200 stores |
| **Volume** | ~500–800 service orders/week chain-wide |
| **Owner** | Services Manager (HQ); Customer Service Rep (Store) |
| **Participants** | CSR, Installation Contractor (3rd party), Warehouse/Logistics, Finance, Customer |

### Background

As a "Home Building Partner," BuildRight Depot provides professional installation services through a network of accredited 3rd-party contractors. This workflow manages the end-to-end lifecycle from service sale to contractor payout, ensuring quality control and financial reconciliation.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Service Sale**: Customer purchases item + Service SKU at POS; CSR captures site details (address, contact, preferred date) and attaches to Service Order (SO) | CSR | Store Manager | 10 min |
| 2 | **Contractor Assignment**: System auto-assigns SO to nearest accredited contractor based on category (HVAC, Plumbing, Flooring) and current workload; contractor notified via mobile app | System / Services Mgr | Services Mgr | Automated |
| 3 | **Site Inspection (if complex)**: For large flooring or roofing jobs, contractor performs site inspection; updates SO with actual material requirements; system adjusts SO price if needed | Contractor | Services Mgr | 1 day |
| 4 | **Scheduling**: Contractor confirms installation date/time with customer via system; system sends SMS confirmation to customer | Contractor | — | 5 min |
| 5 | **Material Release**: Store/DC releases materials for delivery (W19) or customer pickup (W11); system links material delivery status to SO status | Warehouse / CSR | Store Manager | Per W19 |
| 6 | **Execution**: Contractor performs installation; captures "Before" and "After" photos via mobile app; records any additional materials used from customer's stock | Contractor | — | 2–6 hours |
| 7 | **Completion & Sign-off**: Customer reviews work; signs digital completion certificate on contractor's app; rate service (1–5 stars) | Customer / Contractor | — | 10 min |
| 8 | **Quality Audit**: Services Manager reviews a sample of completed SOs (10%) and all low-rated services; triggers corrective action if needed | Services Mgr | VP Store Ops | 1 hour/day |
| 9 | **Billing & Payout**: System moves SO to "Completed/Ready for Payout"; Finance runs weekly payout batch: Contractor Fee − Commission % = Net Payout | Finance (AP) | Controller | Weekly |
| 10 | **Warranty Tracking**: System records installation date as start of labor warranty; links to product warranty (W33) | System | — | Automated |

### System Touchpoints
- Service SKU integration with material SKUs (prompting for service at POS)
- Contractor Portal/App for assignment, scheduling, photo upload, and sign-off
- Automated customer SMS/Email notifications
- Integration with AP for contractor payouts (W7)
- Service warranty tracking linked to customer profile (W17)

### Time Estimate
End-to-end service order lifecycle: 3–7 days from sale to completion (10 min sale + 1 day contractor assignment/scheduling + 2–6 hours execution + 10 min sign-off). Weekly payout batch: 2–4 hours. Quality audit: 1 hour/day. Services Manager spends ~2–3 hours/day on order management and escalation.

### Pain Points / Risks
- Contractor no-shows or late arrivals are the top customer complaint; with 500–800 orders/week, even a 5% no-show rate generates 25–40 weekly incidents requiring rescheduling and service recovery.
- Installation quality varies significantly across 3rd-party contractors; the 10% audit sample (W138.8) is insufficient to catch chronic underperformers before customer complaints escalate.
- Disputes between contractors and customers over additional materials used during installation (W138.6) delay completion sign-off and payout, creating cash flow friction for contractors.
- Service SKU pricing does not always account for site-specific complexity (e.g., uneven flooring, old plumbing), leading to underpriced jobs and contractor margin pressure that discourages quality work.

### Staffing Implication
Services Manager at HQ dedicates ~2–3 hours/day to order management, escalation, and quality audit across ~500–800 weekly orders. At the store level, each CSR spends ~10 min per service order capture; with 3–4 orders/store/day this is absorbed within existing CSR duties. Finance AP requires ~2–4 hours/week for contractor payout batch processing, handled by existing staff. No incremental headcount required at current volumes.

---

## W139. Tool & Equipment Rental Operations

| Field | Detail |
|---|---|
| **Trigger** | Customer requests rental of professional tools (jackhammers, tile cutters, generators) |
| **Frequency** | Daily; ~5–10 rentals per store/day |
| **Volume** | ~1,500 active rental units chain-wide |
| **Owner** | Store Manager |
| **Participants** | CSR, Warehouse/Stock Associate, Finance, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Rental Request**: CSR checks real-time availability of tool in store; verifies customer ID and loyalty status | CSR | Store Manager | 5 min |
| 2 | **Contract & Deposit**: System generates Rental Agreement; Customer pays Rental Fee + Refundable Security Deposit at POS | CSR / Cashier | — | 5 min |
| 3 | **Tool Release**: Stock Associate performs "Outbound Inspection" with customer: verify tool condition, fuel level, and safety features; Customer signs release form | Stock Associate | Store Manager | 10 min |
| 4 | **In-Use Tracking**: System tracks rental duration; sends SMS reminder 2 hours before scheduled return | System | — | Automated |
| 5 | **Return & Inspection**: Customer returns tool; Stock Associate performs "Inbound Inspection": check for damage, cleanliness, and functionality | Stock Associate | Store Manager | 10 min |
| 6 | **Closing & Refund**: (a) If tool OK: System processes deposit refund; (b) If tool damaged/dirty: CSR applies cleaning/repair fee from deposit; (c) If late: System calculates late fee | CSR / Cashier | Store Manager | 5 min |
| 7 | **Maintenance**: Tool moved to "Maintenance" status; Stock Associate performs standard cleaning/servicing before making "Available" again | Stock Associate | Maintenance | 20 min |
| 8 | **Asset Lifecycle**: System tracks total hours used/rentals per unit; triggers major preventive maintenance (PM) or retirement based on usage thresholds | System | Maintenance | Automated |

### System Touchpoints
- Rental inventory management module with real-time availability, rental status lifecycle (Available → Rented → In Maintenance → Available), and asset tracking per unit (W139.1, 8)
- Rental agreement generation at POS with automatic deposit capture and refund processing (W139.2, 6)
- Outbound and inbound inspection checklist on handheld for condition documentation with photo capture (W139.3, 5)
- Automated SMS reminder system for rental return reminders (W139.4)
- Asset lifecycle dashboard tracking cumulative hours, rental count, and maintenance history per unit (W139.8)

### Time Estimate
Per rental transaction: ~35 min total (5 min request + 5 min contract/deposit + 10 min outbound inspection + 10 min return inspection + 5 min closing/refund). Post-rental maintenance: 20 min per tool. Store processes ~5–10 rentals/day = ~3–6 hours/day of rental operations.

### Pain Points / Risks
- Tool damage disputes between customers and store staff during inbound inspection are frequent and subjective — "normal wear" vs. "customer damage" is hard to adjudicate without detailed baseline condition photos from outbound inspection.
- Late returns disrupt subsequent reservations; with ~1,500 units chain-wide and peak demand on weekends, a 10% late return rate creates cascading availability problems.
- Security deposit amount (typically PHP 2,000–10,000) is insufficient to cover replacement cost for high-value tools (jackhammers, generators), creating loss exposure on unreturned or severely damaged equipment.
- Tool maintenance compliance is inconsistent — Stock Associates prioritize customer-facing duties over post-rental cleaning/servicing, leading to poorly maintained tools being rented to the next customer.

### Staffing Implication
With ~5–10 rentals/store/day requiring ~35 min each plus 20 min post-rental maintenance, stores need ~4–7 hours/day of dedicated Stock Associate time for rental operations. This is typically absorbed by existing Stock Associates at lower-volume stores, but high-traffic flagship locations may require a dedicated Rental Desk Associate (~0.5 FTE) to prevent rental duties from displacing core replenishment tasks.

---

## W147. DIY Workshop & In-Store Event Management

| Field | Detail |
|---|---|
| **Trigger** | Monthly marketing calendar; or new product launch requiring education |
| **Frequency** | Weekly (weekends) at selected flagship stores |
| **Volume** | ~20–40 participants per session |
| **Owner** | Store Marketing Coordinator |
| **Participants** | Store Manager, Category Manager, Vendor Rep (Trainer), Customers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Theme Selection**: Choose DIY topic (e.g., "Basic Plumbing", "Tile Laying") based on seasonal demand | Category Mgr | CMO | 1 hour |
| 2 | **Vendor Coordination**: Invite vendor to provide expert trainer and free sample materials | Category Mgr | — | 2 hours |
| 3 | **Promotion & Registration**: Advertise via social media (W142); manage registrations via Loyalty App | Marketing | Social Mgr | Ongoing |
| 4 | **Set-up**: Prepare demo area in-store; arrange tools, materials, and safety gear | Stock Assoc | Store Mgr | 2 hours |
| 5 | **Execution**: Conduct workshop; capture attendee leads; offer "Same Day" discount on featured tools | Vendor / Marketing | Store Mgr | 2–3 hours |
| 6 | **Feedback & Leads**: Collect survey (W65); update CRM with attendee interests for targeted follow-up | Marketing | — | 30 min |

### System Touchpoints
- Event registration module integrated with Loyalty App for sign-ups, capacity management, and attendee communication (W147.3)
- CRM integration for attendee lead capture with interest tags (DIY category, project type) for post-event targeted marketing (W147.6)
- Survey / feedback collection tool (W65) for post-event satisfaction and NPS measurement (W147.6)
- Social media campaign management integration (W142) for event promotion and RSVP tracking (W147.3)

### Time Estimate
Per event cycle: ~6–9 hours total (1 hour theme selection + 2 hours vendor coordination + ongoing promotion + 2 hours setup + 2–3 hours execution + 30 min feedback). Marketing Coordinator spends ~8–12 hours/week managing 1–2 events at flagship stores.

### Pain Points / Risks
- Vendor trainer availability is unreliable — cancellations on short notice leave the store without a presenter and disappointed registered attendees, damaging brand credibility.
- Workshop-to-sales conversion tracking is weak — "Same Day" discount usage is not systematically measured, making it difficult to justify the operational cost of workshops to management.
- Demo area setup disrupts normal store operations on workshop days (space, staff time, noise), creating tension with store operations priorities during peak weekend traffic.
- Participant registration via Loyalty App captures only existing loyalty members, missing walk-in attendees and potential new customer acquisition opportunities.

### Staffing Implication
Marketing Coordinator spends ~8–12 hours/week managing 1–2 events at flagship stores, covering theme selection, vendor coordination, and on-site execution. Category Managers contribute ~3 hours/month for theme selection across stores. Set-up labor (~2 hours/event) is absorbed by existing Stock Associates. At current weekly frequency, no incremental headcount is required; however, scaling beyond 2 events/week at flagship stores would require a dedicated Events Coordinator (~1 FTE).

---

## W148. Home Design & Consultancy Services

| Field | Detail |
|---|---|
| **Trigger** | Customer requests renovation planning for Kitchen, Bathroom, or Wardrobe |
| **Frequency** | Daily; ~5–10 requests per store/month |
| **Volume** | High-value sales potential (PHP 50,000–500,000 per lead) |
| **Owner** | Design Consultant |
| **Participants** | Customer, Sales Rep, Category Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Discovery**: Interview customer on needs, style, and budget; schedule site measurement if needed | Design Consultant | — | 1 hour |
| 2 | **3D Modeling**: Create kitchen/bath layout using design software; select SKUs from active assortment | Design Consultant | — | 2–4 hours |
| 3 | **Presentation**: Present 3D render and detailed BOM (Bill of Materials) to customer | Design Consultant | Sales Rep | 1 hour |
| 4 | **Quotation**: Generate project quotation (W58.1a) with bundled discount if applicable | Sales Rep | Category Mgr | 30 min |
| 5 | **Order Conversion**: Customer accepts; convert to Sales Order; coordinate delivery and installation (W138) | Sales Rep | Store Mgr | 15 min |

### System Touchpoints
- Design software with ERP Item Master integration for real-time SKU availability and pricing during 3D modeling (W148.2)
- Quotation generation module linked to BOM output from design software (W148.4)
- Sales Order conversion from quotation with automatic stock reservation (W148.5)
- Integration with W138 (installation services) for coordinating delivery and professional installation

### Time Estimate
Per consultancy engagement: 4.5–6.5 hours total (1 hour discovery + 2–4 hours 3D modeling + 1 hour presentation + 30 min quotation + 15 min order conversion). With ~5–10 requests per store per month, a Design Consultant handles ~25–65 hours of consultancy work monthly.

### Pain Points / Risks
- Design-to-order conversion rate is typically only 25–35% — customers use the free design service for inspiration but purchase from competitors or smaller local suppliers offering lower prices, wasting consultant time.
- 3D modeling time (2–4 hours per project) is a bottleneck; design consultants at high-volume stores cannot keep up with demand during renovation season, leading to long customer wait times and abandoned leads.
- SKU availability during design may change between presentation and order conversion (especially for tiles and fixtures with volatile stock levels), requiring redesigns that frustrate customers.
- Bundled discount approvals from Category Managers (W148.4) are slow, delaying quotation delivery and giving competitors time to intercept the customer.

### Staffing Implication
Each consultancy engagement requires ~4.5–6.5 hours of Design Consultant time. With ~5–10 requests/store/month, a full-time Design Consultant at flagship stores handles ~25–65 hours of consultancy monthly, fitting within a single FTE but leaving minimal capacity for walk-in design inquiries during peak renovation season. Stores with fewer than 5 requests/month can share a regional Design Consultant across 2–3 locations rather than dedicated headcount per store.

---

## W211. In-Store 3D Kitchen/Bathroom Design Rendering

| Field | Detail |
|---|---|
| **Trigger** | Customer request for customized kitchen, bathroom, or closet layout |
| **Frequency** | ~20–30 designs per store/month |
| **Volume** | High-value project leads |
| **Owner** | Design Consultant |
| **Participants** | Customer, Sales Rep, Category Manager (for custom SKU approval) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Space Survey**: Consultant captures floor plan dimensions (manual or via laser scanner app) | Consultant | — | 30 min |
| 2 | **Assortment Mapping**: System filters 3D assets library for SKUs currently in stock or available for order (W1) | System | — | Automated |
| 3 | **Interactive Design**: Consultant builds 3D model with customer; applies finishes (tiles, paint), fixtures, and cabinets | Consultant | — | 1–2 hours |
| 4 | **ERP BOM Linkage**: System automatically generates a Bill of Materials (BOM) linked to ERP SKU IDs and real-time prices | System | — | Real-time |
| 5 | **Margin Validation**: System checks total project margin; flags if bundled price falls below threshold (W102) | System | Category Mgr | Automated |
| 6 | **Rendering & Export**: Generate high-quality render; email to customer with link to "Click-to-Purchase" in Web Portal | Consultant | — | 15 min |
| 7 | **Quote Conversion**: Convert design BOM into a Formal Quotation in ERP (W58); reserve stock for 48 hours | Consultant | Sales Rep | 5 min |

### System Touchpoints
- 3D Design software integration with ERP Item Master and Pricing
- Automated BOM generation from design assets
- Margin-check workflow for project-based pricing
- Web portal integration for customer design viewing

### Time Estimate
Per design session: ~2–3.5 hours total (30 min space survey + 1–2 hours interactive design + 15 min rendering/export + 5 min quote conversion). With ~20–30 designs per store per month, a Design Consultant handles ~40–105 hours of 3D rendering work monthly across assigned stores.

### Pain Points / Risks
- 48-hour stock reservation (W211.7) creates allocation conflicts with regular store replenishment and ecommerce BOPIS orders — reserved items sitting unsold while other customers are told out-of-stock.
- Interactive design session (1–2 hours) requires the consultant's undivided attention, blocking them from serving other walk-in customers during peak hours and reducing overall store sales productivity.
- Margin validation flags (W211.5) require Category Manager approval for below-threshold pricing, but response times are slow; customers leave the store before approval is received, losing the sale.
- 3D assets library is not always synchronized with current assortment — discontinued SKUs may appear in the design tool, leading to customer disappointment at the quotation stage when items are unavailable.

### Staffing Implication
With ~20–30 designs/store/month requiring ~2–3.5 hours each, a Design Consultant handles ~40–105 hours of 3D rendering monthly. At high-volume flagship stores this approaches full capacity for a single FTE. Stores with lower demand can share consultants across locations. The 1–2 hour interactive sessions block the consultant from other customers, so stores doing more than 8–10 designs/month should consider a second dedicated Design Consultant to avoid lost walk-in sales.

---

## W168. Custom Paint Mixing & Tinting Operations

| Field | Detail |
|---|---|
| **Trigger** | Customer selects a base paint and a specific color from the swatch/fan deck |
| **Frequency** | High volume; ~15–30 tinting requests per store/day |
| **Volume** | ~100,000+ liters mixed annually chain-wide |
| **Owner** | Paint Department Supervisor |
| **Participants** | Paint Technician (Sales Associate), Customer, Cashier |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Color Selection**: Customer chooses color code from brand swatch; Technician identifies required Base Paint (A, B, C, or Deep) | Paint Technician | — | 3 min |
| 2 | **System Entry**: Technician enters Color Code and Can Size in the tinting machine software; system calculates required colorant dosage | Paint Technician | — | 2 min |
| 3 | **Tinting**: Technician places base can under dispenser; machine injects colorants; system logs colorant consumption per canister | Paint Technician | — | 2 min |
| 4 | **Mixing**: Can is sealed and placed in the Gyroscopic Mixer for 2–3 minutes to ensure uniform color distribution | Paint Technician | — | 3 min |
| 5 | **Quality Check**: Technician performs a "dot test" on the can lid; dries with heat gun; verifies match against physical swatch | Paint Technician | Dept Supervisor | 2 min |
| 6 | **Labeling & POS**: Technician generates a "Custom Tint" barcode label from the system; labels can; customer takes to Cashier | Paint Technician | — | 1 min |
| 7 | **Checkout**: Cashier scans Custom SKU; system deducts Base Paint and Colorants from inventory in real-time | Cashier | — | 30 sec |
| 8 | **Machine Maintenance**: Daily nozzle cleaning and weekly calibration to ensure color accuracy | Paint Technician | Dept Supervisor | 15 min |

### System Touchpoints
- Tinting software integration with ERP Item Master (Base + Colorants)
- Real-time consumption tracking of colorants (milliliters)
- Custom SKU generation at POS linked to original Base SKU for traceability
- Machine maintenance log tracking in W47 (Facility Maintenance)

### Time Estimate
Per tinting request: ~13 min total (3 min color selection + 2 min system entry + 2 min tinting + 3 min mixing + 2 min quality check + 1 min labeling). Machine maintenance: 15 min daily + 30 min weekly calibration. With ~15–30 requests/store/day, Paint Technicians spend ~3.5–7 hours/day on tinting operations.

### Pain Points / Risks
- Color accuracy is customer-subjective — the "dot test" (W168.5) relies on visual comparison against a physical swatch; lighting conditions in-store and customer expectations can differ, leading to re-tint requests and wasted base paint.
- Colorant canister consumption tracking in milliliters is imprecise; actual consumption varies from system-calculated dosage, creating gradual inventory drift between physical colorant stock and system records.
- Tinting machine downtime (nozzle clogs, calibration drift) during peak hours (weekends) creates long customer wait times and lost sales, as customers cannot take paint immediately.
- Base paint stock-outs at the paint department level are not always visible to the tinting machine software — a customer may go through the entire tinting process only to find the base paint is out of stock at the shelf.

### Staffing Implication
Paint Technicians spend ~3.5–7 hours/day on tinting operations at ~15–30 requests/store/day, plus ~15 min daily maintenance. This represents roughly 0.5–1 FTE of dedicated Paint Technician time per store, typically absorbed by existing Paint Department Sales Associates. High-volume stores processing 25+ tinting requests/day should designate one associate as the primary tinting operator to ensure consistent quality and minimize customer wait times.

---

## W169. Lumber & Board Cutting Services

| Field | Detail |
|---|---|
| **Trigger** | Customer purchases whole lumber/plywood and requests specific sizes |
| **Frequency** | Moderate; ~10–20 requests per store/day |
| **Volume** | Primary items: Plywood, Marine Board, 2x4 Lumber |
| **Owner** | Lumber Department Supervisor |
| **Participants** | Cutter (Stock Associate), Customer, Cashier |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Intake**: Customer presents purchased board/lumber or selects from floor; provides cutting list/dimensions | Cutter | — | 5 min |
| 2 | **Calculation**: Cutter calculates number of cuts; system determines "Cutting Fee" (e.g., first 2 cuts free, PHP 10 per subsequent cut) | Cutter | — | 2 min |
| 3 | **Payment**: Customer pays Cutting Fee at POS; receives "Cutting Authorization" slip | Cashier | — | 2 min |
| 4 | **Execution**: Cutter performs cuts using Table Saw or Panel Saw; adheres to safety protocols (PPE, machine guards) | Cutter | Dept Supervisor | 5–15 min |
| 5 | **Scrap Management**: (a) Off-cuts > 1ft offered to customer; (b) if declined, off-cuts moved to "Scrap Bin" for discounted sale or internal use | Cutter | — | 2 min |
| 6 | **Safety Log**: Cutter logs machine hours and blade condition; reports dull blades for sharpening/replacement (W47) | Cutter | Dept Supervisor | 5 min |

### System Touchpoints
- Service SKU for "Cutting Fee" at POS
- Scrap inventory tracking (Optional: creating "Remnant" SKUs for large off-cuts)
- Safety incident logging in W52 (Health & Safety)

### Time Estimate
Per cutting request: ~21–29 min total (5 min intake + 2 min calculation + 2 min payment + 5–15 min cutting + 2 min scrap management + 5 min safety log). With ~10–20 requests/store/day, the Cutter spends ~3.5–10 hours/day on cutting operations. Machine maintenance and blade replacement add ~30 min/day.

### Pain Points / Risks
- Safety risk is significant — table saws and panel saws cause serious injuries; despite PPE requirements and machine guards, complacency during high-volume cutting periods (weekends) increases incident probability.
- Cutting accuracy depends on Cutter skill and experience; inconsistent cuts lead to customer complaints and wasted material, especially for expensive marine-grade plywood.
- Scrap management (W169.5) is largely informal — off-cuts accumulate without systematic tracking, resulting in missed revenue from saleable remnants and cluttered work areas that pose tripping hazards.
- Blade wear and tear is not systematically tracked beyond the manual safety log (W169.6); dull blades cause rough cuts, burn marks on wood, and increased kickback risk, yet replacement is reactive rather than schedule-based.

### Staffing Implication
With ~10–20 cutting requests/store/day requiring ~21–29 min each plus ~30 min daily maintenance, the Cutter role demands ~4–10 hours/day of Stock Associate time. At stores with 15+ daily requests, a dedicated Cutter (~0.5–1 FTE) is warranted to maintain throughput and safety compliance. Lower-volume stores can absorb cutting duties within existing Stock Associate rotations, though peak weekend surges often require temporary reassignment of an additional associate.

---

## W213. Installation Service Partner Quality Audit

| Field | Detail |
|---|---|
| **Trigger** | Scheduled quarterly audit; or high complaint rate for a specific contractor (W138.8) |
| **Frequency** | Quarterly per contractor; or ad-hoc |
| **Owner** | Services Quality Manager |
| **Participants** | Services Quality Mgr, Contractor, Customer (for site visit) |
| **Volume** | ~20-30 contractor audits/month nationwide |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Audit Scoping**: System identifies contractors with high volume or low CSAT (W65) in the past quarter | System | Services Qual Mgr | 30 min |
| 2 | **Site Visit**: Auditor visits 3–5 active/completed sites with the contractor; inspects workmanship against "BuildRight Standard" | Services Qual Mgr | — | 1 day |
| 3 | **Compliance Check**: Verify contractor's team has valid IDs, PPE, and appropriate tools (as required in W138 contract) | Services Qual Mgr | — | 1 hour |
| 4 | **Audit Report**: Auditor logs findings in system: workmanship score, safety score, compliance score | Services Qual Mgr | Services Mgr | 1 hour |
| 5 | **Scorecard Update**: Audit score feeds into the "Contractor Master Scorecard" (linked to W44) | System | — | Automated |
| 6 | **Corrective Action**: If score < 70%, contractor put on "Probation"; requires remedial training or face de-listing | Services Mgr | VP Store Ops | 1 hour |

### System Touchpoints
- Contractor quality audit module with photo upload capability
- CSAT and Complaint data integration for audit triggering
- Integration with Contractor Master Scorecard

### Time Estimate
Per contractor audit: ~1.5 days total (30 min scoping + 1 day site visits + 1 hour compliance check + 1 hour report + 1 hour corrective action if needed). Quarterly cycle covering all active contractors: ~10–15 days per quarter for Services Quality Manager.

### Pain Points / Risks
- Site visits require customer permission and scheduling coordination with contractors; customer refusals or contractor unavailability delay audits and create gaps in quality coverage.
- The "BuildRight Standard" for workmanship assessment is subjective — different auditors may score the same installation differently, undermining scorecard reliability and contractor trust in the process.
- Probation and corrective action follow-through is inconsistent; contractors on probation may continue receiving work orders due to capacity constraints (insufficient alternative contractors in the area).
- CSAT data (W65) driving audit selection is often incomplete — many customers do not complete post-installation surveys, meaning problem contractors may escape detection until formal complaints escalate.

### Staffing Implication
Quarterly audit cycle covering all active contractors requires ~10–15 days/quarter of Services Quality Manager time, roughly equivalent to ~1.5 FTE-days per week sustained throughout the year. This is typically handled by a dedicated Services Quality Manager (1 FTE) who also manages corrective action follow-ups and contractor training coordination. Site visit travel to 200 stores across the chain adds unaccounted time; regional audit deputies may be needed if contractor count exceeds 50 active partners.

---

## W282. Subscription Billing for Recurring Home Services

| Field | Detail |
|---|---|
| **Trigger** | Customer signs up for a recurring maintenance plan (e.g., Quarterly AC cleaning, monthly pest control). |
| **Frequency** | Daily sign-ups, monthly billing runs |
| **Volume** | 100-200 billing events per day enterprise-wide |
| **Owner** | Services Ops Manager |
| **Participants** | Customer, Services Admin, Finance (AR) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer purchases the subscription online or at POS, securely tokenizing their credit card. | Customer | Services Admin | 10 min |
| 2 | ERP Subscription Billing module generates a recurring contract and defers revenue. | System | Services Admin | Automated |
| 3 | System automatically generates a field service work order (W138) 7 days prior to the scheduled quarterly service. | System | Services Admin | Automated |
| 4 | Upon completion of the service, system triggers the payment gateway to bill the tokenized card. | System | Finance AR | Automated |
| 5 | Finance recognizes the deferred revenue for that period. | Finance AR | Controller | Automated |

### System Touchpoints
- Order Management (Subscriptions) — subscription contract creation, renewal, and cancellation lifecycle management
- Field Service — automated work order generation linked to subscription schedule and contractor assignment (W138)
- AR — deferred revenue recognition, billing run processing, and payment reconciliation
- Payment Gateway — secure credit card tokenization, automated billing on service completion, and failed payment retry logic

### Pain Points / Risks
- Expired credit cards causing payment failures; disjointed scheduling resulting in missed service appointments
- Revenue recognition errors if deferred revenue is not properly amortized per period, especially for mid-month cancellations or plan upgrades/downgrades
- PCI-DSS compliance requirements for stored credit card tokens — any data breach exposes BuildRight to significant fines and reputational damage under NPC regulations
- Cancellation disputes — customers disputing charges after service completion or requesting refunds for unused service periods create AR reconciliation complexity and customer service burden

### Time Estimate
**Total**: Automated billing cycle with minimal manual intervention. Per subscription sign-up: ~10 min. Monthly billing run: automated. Exception handling: ~1 hour/day for failed payments, cancellation disputes, and plan modifications. Revenue recognition: automated as part of month-end close (W9A). Services Admin spends ~2–3 hours/day on subscription exception management.

### Staffing Implication
100–200 billing events/day are largely automated. Services Admin: ~2–3 hours/day for exception handling and subscription modifications. Finance AR: ~1 hour/day for failed payment follow-up and revenue recognition review. No incremental headcount; absorbed by existing Services Admin and Finance AR roles.

---

## W440. Power Tool Service & Repair Center Operations

| Field | Detail |
|---|---|
| **Trigger** | Customer brings in a damaged power tool (Makita, Bosch, DeWalt, etc.) for repair (In-Warranty or Out-of-Warranty) |
| **Frequency** | Daily; ~3–5 service intake events per store/day |
| **Volume** | ~20,000–30,000 repairs per year chain-wide |
| **Owner** | Service Center Manager |
| **Participants** | Service Desk Clerk, Technician, Parts Specialist, Cashier |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Intake**: Clerk inspects tool; verifies warranty status; captures customer complaint; system generates Service Ticket | Service Desk Clerk | Store Manager | 10 min |
| 2 | **Diagnostic**: Technician inspects tool; identifies part failure; system checks parts availability | Technician | Service Center Mgr | 30 min |
| 3 | **Quotation**: System generates estimate (Labor + Parts); Clerk notifies customer for approval (via SMS/App) | Service Desk Clerk | — | 5 min |
| 4 | **Part Issue**: Parts Specialist issues spares from "Service Inventory" (non-sales stock) to the ticket | Parts Specialist | — | 10 min |
| 5 | **Repair**: Technician replaces parts; performs safety/functionality test; signs off on ticket | Technician | — | 1–2 hours |
| 6 | **Customer Notification**: System auto-notifies customer that tool is ready for pickup | System | — | Automated |
| 7 | **Release & Billing**: Customer picks up tool; pays at POS (if out-of-warranty); Clerk closes ticket | Service Desk Clerk / Cashier | — | 10 min |

### System Touchpoints
- Service Desk module for ticket creation and customer communication
- Parts inventory management (segregated from retail inventory)
- Warranty verification link with Item Master and Sales History
- Integration with POS for out-of-warranty labor/parts billing

### Pain Points / Risks
- Long lead times due to spare parts stockouts (especially for older models).
- Communication gaps — customers not notified of delays or cost overruns.
- High training requirement for technicians to maintain manufacturer "Authorized Center" status.

### Staffing Implication
High-volume flagship stores require a dedicated Technician (~1 FTE). Regional stores share a regional hub technician.

---

## W442. Site Technical Survey & Measurement Services

| Field | Detail |
|---|---|
| **Trigger** | Customer requests survey for custom/project-based products (Aluminum windows, doors, kitchen cabinets) |
| **Frequency** | Daily; ~1–2 requests per store/day |
| **Volume** | ~300–400 surveys/week chain-wide |
| **Owner** | Project Sales Manager |
| **Participants** | Technical Surveyor, Sales Rep, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Service Sale**: Customer pays for "Survey Service" at POS (often refundable upon order) | Sales Rep | — | 5 min |
| 2 | **Scheduling**: System assigns surveyor based on location/specialty; schedules visit with customer | System / Admin | Project Sales Mgr | 10 min |
| 3 | **Site Visit**: Surveyor visits site; performs precise measurements; takes photos of site conditions | Surveyor | — | 1–2 hours |
| 4 | **Data Upload**: Surveyor uploads measurements and photos into the ERP/Project folder | Surveyor | — | 15 min |
| 5 | **Quotation Feed**: Sales Rep receives "Verified Measurements" alert; updates project quotation (W162) | Sales Rep | — | 15 min |
| 6 | **Technical Review**: Project Manager/Technician reviews feasibility before final contract | Project Manager | Project Sales Mgr | 10 min |

### System Touchpoints
- Field Service mobile app for measurement capture and photo upload
- Project folder integration for storing technical survey data
- Automated refund logic (linking Survey SKU to final Sales Order)

### Pain Points / Risks
- Measurement errors leading to non-fitting custom items and massive fabrication waste.
- Customer no-shows for scheduled site visits wasting surveyor time.

### Staffing Implication
Regional hubs maintain a pool of 2–3 Surveyors serving 10–15 stores.

---

## W600. Service Contractor Accreditation & Onboarding Management

| Field | Detail |
|---|---|
| **Trigger** | Contractor recruitment drive; contractor applies via BuildRight website, job fair, or referral; new store opening requires additional contractor pool; quality audit (W213) identifies need for contractor replacement |
| **Frequency** | ~20–30 new contractor applications/month; ~10–15 new accreditations completed/month (including rejections and withdrawals); annual re-certification for all accredited contractors in Q1 |
| **Volume** | ~500–800 service orders/week fulfilled by third-party contractors; target accredited contractor pool: 300–400 contractors across all service categories (electricians, plumbers, tile setters, AC technicians, carpenters, painters, general handyman); current no-show rate: 25–40 weekly (~5% of orders); geographic coverage: 200 store service areas across Luzon, Visayas, and Mindanao |
| **Owner** | Services Manager |
| **Participants** | Services Manager (R/A), Services Coordinator (R for scheduling and documentation), Quality Inspector (R for skills assessment), Training Manager (R for BuildRight training), HR Business Partner (I for background check coordination), Legal Counsel (I for contractor agreement), Store Manager (I for service area assignment input) |

### Background

W138 covers home installation services management — the end-to-end lifecycle from service sale to contractor payout. W213 covers installation service partner quality audit — periodic quality assessment of accredited contractors. W33 covers warranty claims which often trace back to installation quality. W139 covers tool rental which contractors may use. W442 covers site surveys which accredited contractors may perform. However, no workflow covers the upstream process of recruiting, qualifying, and onboarding the third-party contractors who deliver these services — the accreditation pipeline that feeds the W138 service order fulfillment engine.

Contractor quality is the single biggest operational pain point in BuildRight's services business. With ~500–800 service orders/week fulfilled by 300+ third-party contractors, a 5% no-show rate generates 25–40 weekly incidents requiring emergency rescheduling, customer complaint handling per W41, and service recovery costs. More critically, poor installation quality generates warranty claims per W33, customer complaints per W597, and reputational damage in an industry where word-of-mouth among contractors and homeowners is a powerful driver of business.

The Philippine context adds complexity: (1) **PRC licensing** — professional electricians and plumbers require Philippine Regulation Commission (PRC) licenses; (2) **TESDA certification** — tile setters, carpenters, and AC technicians should have Technical Education and Skills Development Authority (TESDA) National Certificate (NC) II or III; (3) **informal sector prevalence** — many skilled tradespeople in the Philippines operate informally without licenses or certifications, requiring BuildRight to balance quality standards with available supply; (4) **geographic coverage** — 200 stores across the archipelago means contractors are needed in urban centers (Metro Manila, Cebu, Davao) and provincial areas (Ilocos, Bicol, Samar, Zamboanga) where qualified tradespeople are scarcer.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Contractor recruitment/application**: contractor enters the accreditation pipeline through one of four channels — (a) online application via BuildRight website careers/services page: contractor fills in personal details, trade category, years of experience, certifications held, service area, and uploads photos of previous work; (b) BuildRight-organized recruitment event: Services Coordinator conducts on-site recruitment at trade schools, TESDA centers, and regional contractor association events; (c) referral from existing accredited contractor or Store Manager; (d) proactive recruitment: Services Manager identifies geographic coverage gaps from W138 contractor assignment data and targets recruitment in underserved areas (e.g., Mindanao stores with <5 accredited contractors); system creates contractor applicant record with application source, date, and initial information | Services Coordinator / Contractor | Services Manager | 15–20 min per application (data entry + initial screening) |
| 2 | **Credentials verification**: Services Coordinator verifies submitted credentials — (a) PRC license: verify license number and status via PRC online verification system (prc.gov.ph); confirm license is active and not expired; required for: electricians (Registered Master Electrician), plumbers (Registered Master Plumber); (b) TESDA certification: verify NC II/NC III certificate via TESDA online verification; required for: tile setters (NC II Masonry), AC technicians (NC II Refrigeration and Air-Conditioning), carpenters (NC II Carpentry); (c) if contractor does not have PRC/TESDA certification but has >5 years documented experience: Services Coordinator flags for conditional accreditation pathway (step 8 — supervised installations with accelerated certification support); (d) verify government-issued ID (valid passport, driver's license, or postal ID for identity); (e) verify NBI clearance or police clearance (valid within 6 months) per background check requirement; (f) document verification results in contractor applicant record | Services Coordinator | Services Manager | 30–45 min per applicant |
| 3 | **Background check**: Services Coordinator conducts background screening — (a) NBI/police clearance: verify no criminal record; (b) check against BuildRight's internal blacklist: contractors previously terminated for cause (theft, fraud, customer complaints, no-show pattern); (c) contact 2 professional references (previous clients, employers, or trade association officers) — verify quality of work, reliability, and professionalism; (d) for contractors applying for electrical or plumbing categories: additional verification of no pending customer complaints or disciplinary actions with PRC; (e) background check results documented with pass/fail and notes; (f) applicants with criminal record involving theft, fraud, or violence are auto-rejected; applicants with minor issues assessed case-by-case by Services Manager | Services Coordinator | Services Manager | 45–60 min per applicant |
| 4 | **Skills assessment**: qualified applicants attend in-person skills assessment at nearest BuildRight DC or flagship store — (a) practical assessment: applicant completes a supervised hands-on task representative of their trade: (i) electricians: wire a basic residential circuit (switch, outlet, light fixture) — assessed for code compliance, neatness, and safety; (ii) plumbers: install a faucet and connect P-trap — assessed for leak-free joints, proper sealing, and professional finish; (iii) tile setters: tile a 1m × 1m section — assessed for level, grout consistency, pattern alignment, and edge finishing; (iv) AC technicians: install a split-type AC unit on a mock wall — assessed for correct mounting, piping, electrical connection, and system testing; (v) carpenters: build a basic shelf or cabinet — assessed for measurements, joinery, finish quality; (b) assessment conducted by Quality Inspector (from W213 audit team) or senior accredited contractor serving as assessor; (c) scoring rubric: 5-point scale per criterion (workmanship, safety compliance, speed, professionalism, tool proficiency); minimum passing score: 3.5/5.0; (d) applicants scoring 3.0–3.5: conditional pass — eligible for supervised trial period (step 8) with mandatory mentoring; (e) applicants scoring <3.0: fail — may re-apply after 90 days with evidence of skill improvement | Quality Inspector / Services Manager | Services Manager | 2–3 hours per assessment session (can assess 3–5 applicants per session) |
| 5 | **Tool/equipment verification**: Services Coordinator verifies contractor has required tools for their trade — (a) each trade category has a minimum tool list: (i) electricians: multimeter, wire strippers, pliers, voltage tester, conduit bender, power drill; (ii) plumbers: pipe wrench, adjustable wrench, tube cutter, soldering torch, plunger, snake; (iii) tile setters: tile cutter, notched trowel, level, rubber mallet, grout float, wet saw; (iv) AC technicians: manifold gauge, vacuum pump, tubing cutter, flaring tool, refrigerant scale; (v) carpenters: circular saw, miter saw, nail gun, level, tape measure, chisels; (b) contractor presents tools for visual inspection; (c) if contractor lacks specific tools: discuss options — (i) purchase through BuildRight contractor discount program (10% discount on tools), (ii) rent from BuildRight tool rental per W139; (d) tool adequacy documented in contractor record | Services Coordinator | — | 15–20 min per applicant |
| 6 | **BuildRight training completion**: contractor completes mandatory BuildRight orientation and service training — (a) Module 1 — BuildRight Service Standards (4 hours, classroom or virtual): company overview, service expectations, customer interaction standards, uniform and grooming requirements, BuildRight service pledge, escalation procedures per W597; (b) Module 2 — Safety and Compliance (2 hours): PPE requirements per W172, site safety protocols, building code basics, electrical/plumbing code compliance per Philippine National Building Code (PD 1096) and National Electrical Code; (c) Module 3 — BuildRight Systems Training (3 hours): contractor mobile app usage — accepting service orders, scheduling, photo capture, digital completion certificate, payment tracking; (d) Module 4 — Category-Specific Installation Standards (4 hours, by trade): BuildRight installation standards for key product categories — AC installation checklist, tile installation specifications, water heater installation requirements, electrical wiring standards; (e) contractor must pass written assessment at end of each module (minimum score: 80%); (f) training delivered by Training Manager and Services Manager at regional training centers (Metro Manila, Cebu, Davao) or via virtual sessions for remote areas; (g) total training time: ~13 hours (typically delivered over 2 days) | Training Manager / Services Manager | Services Manager | 13 hours per contractor (2 days) |
| 7 | **Service area assignment**: Services Manager assigns accredited contractor to service areas — (a) contractor specifies preferred service area (city/municipality and radius in km from home base); (b) Services Manager reviews current contractor coverage map: identify areas with sufficient coverage (target: 3–5 contractors per trade category per store service area) and areas with gaps; (c) assign contractor to stores where coverage is most needed — prioritize stores with <3 accredited contractors in the contractor's trade category; (d) contractor may be assigned to multiple stores if geographically feasible (e.g., a contractor in Quezon City may serve 3–5 Metro Manila stores); (e) assignment documented in system and contractor visible for auto-assignment in W138 step 2 | Services Manager | — | 15 min per contractor |
| 8 | **Trial period (supervised installations)**: newly accredited contractor enters 90-day trial period — (a) first 5 installations: contractor accompanied by senior accredited contractor (mentor) who observes and provides real-time coaching; mentor submits feedback form per installation: quality score, customer interaction rating, timeliness, areas for improvement; (b) installations 6–15: contractor performs independently but all jobs receive enhanced quality audit (100% review vs. standard 10% per W138 step 8); (c) if any trial installation receives customer complaint or quality score <3/5: Services Manager conducts immediate review — provide additional training, extend trial period, or terminate accreditation; (d) if all 15 trial installations pass: trial period completed — contractor granted full accreditation status; (e) trial period data (quality scores, completion times, customer ratings) establishes baseline performance metrics for ongoing W213 quality audits | Contractor / Quality Inspector / Services Manager | Services Manager | Trial period: 90 days (dependent on installation volume assigned) |
| 9 | **Full accreditation**: upon successful trial completion — (a) system updates contractor status from "Trial" to "Fully Accredited"; (b) contractor added to full auto-assignment pool per W138 step 2 (trial contractors receive limited assignments); (c) contractor receives BuildRight accreditation badge and ID card (valid for 1 year); (d) contractor agreement executed: defines scope of services, payment terms (per-installment fee minus BuildRight commission), liability insurance requirements, no-show penalty policy (3 no-shows in 90 days = suspension), quality standards, and termination conditions; (e) agreement reviewed by Legal Counsel and signed by contractor and Services Manager; (f) contractor receives BuildRight uniform (polo shirt with logo) per W172 | Services Manager / Legal Counsel | Services Manager | 30 min per contractor (documentation + agreement signing) |
| 10 | **Annual re-certification**: all accredited contractors undergo annual re-certification in Q1 — (a) performance review: Services Manager pulls contractor's trailing 12-month performance data from W138/W213 — (i) total installations completed, (ii) average customer rating, (iii) no-show count, (iv) quality audit scores, (v) customer complaint count, (vi) warranty claim rate for contractor's installations per W33; (b) credentials refresh: verify PRC license, TESDA certification, NBI clearance are still current and valid; (c) updated training: contractor must complete any new or updated training modules introduced in the past year (e.g., new product installation procedures, updated safety protocols, system app updates); (d) re-certification decision: (i) contractor meets all performance thresholds (rating ≥3.5, no-shows ≤2/year, zero unresolved complaints) → re-certified for 1 year; (ii) contractor below threshold but showable improvement plan → conditional re-certification with 90-day performance improvement plan; (iii) contractor significantly below threshold (rating <3.0, or 3+ no-shows, or unresolved serious complaint) → accreditation revoked, removed from contractor pool; (e) re-certification results documented and communicated to contractor; (f) contractors who fail re-certification may re-apply after 6 months | Services Manager / Quality Inspector | Services Manager | 30–45 min per contractor |

**Total time per contractor accreditation**: ~20–25 hours over 2–4 weeks (application screening 30 min + credentials verification 45 min + background check 60 min + skills assessment 3 hours + tool verification 20 min + training 13 hours + service area assignment 15 min + trial period 90 days + final accreditation 30 min)

### System Touchpoints (W600 — Contractor Accreditation)

- Contractor management module with applicant tracking, accreditation status, and trial period management (SVC-005)
- Contractor mobile app for service order management, scheduling, photo capture, and digital completion (SVC-001)
- Skills assessment scoring rubric and results tracking (SVC-005)
- Training management integration for mandatory module completion tracking (W51, SVC-005)
- Service area coverage mapping and auto-assignment integration (W138)
- Contractor agreement management with digital signature (SVC-005)
- Performance data integration from W138 (service order history) and W213 (quality audit scores)
- Warranty claims feed from W33 for installation quality tracking
- Tool rental integration per W139 for contractors who rent tools
- NBI/PRC/TESDA external verification integration (manual lookup, system-documented results)
- Contractor payment processing integration per W138 step 9 (AP module)
- Annual re-certification workflow with performance threshold automation (SVC-005)

### Pain Points / Risks

- **PRC/TESDA-certified tradespeople are scarce outside Metro Manila**: many qualified tradespeople in provincial areas operate informally without government certifications; requiring PRC/TESDA certification for all applicants would significantly limit the contractor pool in Visayas and Mindanao; mitigated by conditional accreditation pathway (step 2c) for experienced but uncertified applicants, combined with mandatory BuildRight training (step 6) and supervised trial period (step 8)
- **Skills assessment logistics for 200-store coverage**: conducting in-person skills assessments for applicants across Luzon, Visayas, and Mindanao requires regional assessment centers and Quality Inspector travel; mitigated by establishing 3–4 regional assessment hubs (Metro Manila, Cebu, Davao, and one Northern Luzon location), conducting quarterly assessment batches rather than individual assessments, and using senior accredited contractors as regional assessors
- **13-hour training requirement is a barrier for working contractors**: experienced tradespeople may resist dedicating 2 full days to BuildRight training when they can find work elsewhere; mitigated by offering training on weekends, splitting into evening sessions for virtual modules, and positioning training as a professional development opportunity (BuildRight certification enhances their market value)
- **Trial period length depends on installation volume**: in low-volume stores (provincial, new stores), a newly accredited contractor may not receive 15 installations within 90 days, extending the trial period indefinitely; mitigated by assigning trial contractors to higher-volume stores in their region for initial installations, then transitioning to their assigned store once trial is complete
- **Annual re-certification of 300–400 contractors is administratively heavy**: at ~45 min per re-certification × 350 contractors = ~260 person-hours in Q1; mitigated by automated performance data pull from W138/W213, batch re-certification sessions at regional hubs, and staggered re-certification by region (Luzon in January, Visayas in February, Mindanao in March)

### Staffing Implication

- **Services Manager**: ~30–40 hours/month on accreditation management (application review, skills assessment attendance, trial monitoring, re-certification). Significant portion of Services Manager role alongside W138 service order management.
- **Services Coordinator**: dedicated support role for accreditation administration — application processing, credentials verification, background checks, scheduling, documentation. ~1 FTE justified at current volume (~20–30 applications/month + 350 annual re-certifications + ongoing trial monitoring).
- **Quality Inspector**: skills assessments consume ~6–9 hours/month (3 sessions × 2–3 hours each). Absorbed within existing Quality Inspector role from W213 audit team.
- **Training Manager**: 13 hours × ~12 new accreditations/month = ~156 training hours/month; this is a significant training load. Mitigated by batch training sessions (train 5–8 contractors simultaneously) reducing to ~20–25 training days/year. Absorbed by Training Manager with potential seasonal contractor trainer support.
- **Total accreditation pipeline effort**: ~200–250 person-hours/month for the full pipeline (recruitment through full accreditation), distributed across Services Manager, Services Coordinator, Quality Inspector, and Training Manager.

---

## W794. Service SKU Catalog Management, Pricing & Material Linkage

| Field | Detail |
|---|---|
| **Trigger** | New service offering launch; existing service price revision; seasonal service promotion; vendor/partner capability change |
| **Frequency** | Ad-hoc for new services; quarterly pricing review; monthly for seasonal promotions |
| **Volume** | ~50-80 active service SKUs; ~10-15 new service SKUs/year; ~30-40 price updates/year |
| **Owner** | Services Category Manager |
| **Participants** | VP for Merchandising, Service Partners/Contractors, Finance, Store Operations, IT (ERP) |

### Background

BuildRight's value-added services — home installation (W138), tool rental (W139), DIY workshops (W147), design consultancy (W148), paint mixing (W168), lumber cutting (W169), and 3D design rendering (W211) — are a key differentiator and margin contributor. Unlike merchandise SKUs with vendor-set costs, service SKUs require unique pricing logic: labor cost, material cost linkage (installation of purchased products), equipment depreciation (tool rental), contractor commission rates, and regional price variations. This workflow governs the creation, pricing, maintenance, and lifecycle of service SKUs in the ERP.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Service Concept & Feasibility**: Services Category Manager evaluates new service opportunity: market demand (customer requests per W87), competitive landscape (do competitors offer this service), capability assessment (does BuildRight have trained staff or qualified contractors per W600), profitability estimate (target gross margin 30-45%); presents business case to VP Merchandising | Services Category Mgr | VP Merchandising | 3-5 days |
| 2 | **Service SKU Creation**: Create service SKU in Item Master per W252: (a) service type classification (installation, rental, workshop, consultancy, custom processing); (b) UOM definition (per job, per hour, per day, per square meter, per linear meter); (c) material linkage: map service SKU to required material SKUs (e.g., "Aircon Installation" linked to specific aircon models, copper tubing, electrical conduit); (d) labor standard: estimated labor hours by skill level; (e) equipment linkage: map to rental equipment SKUs if applicable; (f) regional pricing matrix: define pricing per region (Metro Manila, Luzon Provincial, Visayas, Mindanao) to account for contractor rate differentials | Services Category Mgr | VP Merchandising | 1-2 days |
| 3 | **Pricing & Margin Setup**: Finance and Services Category Manager set pricing: (a) cost build-up: labor + material + equipment depreciation + contractor commission + overhead allocation; (b) target margin: 30-45% gross margin depending on service complexity; (c) pricing method: fixed price (standard installation), variable (paint mixing per liter), quotation-based (large installation projects per W162); (d) POS integration: ensure service SKU appears correctly at POS with proper pricing and material prompts per W5B | Finance / Services Category Mgr | VP Merchandising | 1 day |
| 4 | **Contractor/Partner Rate Agreement**: For services delivered by external contractors per W600: (a) negotiate service rate per job type with contractor; (b) define service quality standards and SLA; (c) agree on payment terms (weekly, bi-monthly); (d) register contractor rate in ERP as service cost; (e) contractor rates reviewed quarterly to ensure market competitiveness | Services Category Mgr / Procurement | VP Merchandising | 2-5 days per rate negotiation |
| 5 | **Quarterly Pricing Review**: Quarterly, Services Category Manager reviews all service SKU pricing: (a) compare service margin to target; (b) review material cost changes that affect service profitability (e.g., lumber price increase affects cutting service margin); (c) review contractor rate market benchmarks; (d) adjust pricing as needed per W40; (e) seasonal services (e.g., pre-typhoon roof repair consultation) repriced for peak demand | Services Category Mgr | VP Merchandising | 1 day/quarter |
| 6 | **Service SKU Deactivation**: When a service is discontinued: (a) mark SKU as inactive per W68; (b) ensure no open orders reference the SKU; (c) notify Store Operations and POS team; (d) update store signage and promotional materials per W504; (e) archive service SKU data for historical analysis | Services Category Mgr | VP Merchandising | 1 day |

### System Touchpoints

- Item Master per W252 with service SKU type classification
- Material linkage module connecting service SKUs to required material SKUs
- Pricing engine per W289 with service-specific pricing logic (fixed, variable, quotation-based)
- Contractor rate management module linked to W600 contractor accreditation
- POS integration per W5B for service SKU selling with material prompts
- Service margin reporting per W85 for category profitability analysis
- Service order management per W545/W556 for job scheduling and tracking

### Pain Points / Risks

- **Material cost volatility eroding service margin**: service pricing set at beginning of quarter may become unprofitable if material costs increase (e.g., lumber, paint, copper tubing); quarterly review may not catch mid-quarter spikes
- **Contractor rate disputes**: contractors in high-demand seasons (pre-typhoon, holiday renovation rush) may demand higher rates than contracted; BuildRight must either absorb cost increase or risk contractor availability
- **Regional pricing complexity**: contractor rates vary significantly across Philippine regions (Metro Manila rates 30-50% higher than Mindanao); maintaining accurate regional pricing for 80 service SKUs across 5 regions is complex
- **Service-material linkage maintenance**: when merchandise SKUs are discontinued or replaced per W68, linked service SKUs must be updated to reference new materials; stale linkages cause incorrect POS prompts
- **Unprofitable service SKUs lingering**: low-volume services that don't meet minimum margin thresholds may remain active because no one reviews them for discontinuation

### Staffing Implication

- **Services Category Manager**: ~8-12 hours/month on service SKU management; absorbed by existing category management team
- **Finance**: ~4-6 hours/quarter on service pricing review; absorbed by existing FP&A team
- **No incremental headcount**.

### Time Estimate

- New service SKU creation: 3-7 days (concept through POS activation)
- Pricing review: 1 day/quarter
- Contractor rate negotiation: 2-5 days per contractor
- Service SKU deactivation: 1 day

---

## W795. Service Customer Complaint, Rework & Warranty Claim Management

| Field | Detail |
|---|---|
| **Trigger** | Customer reports dissatisfaction with delivered service (installation quality, equipment rental issue, workshop experience, project outcome); or warranty claim filed for service work per W33 |
| **Frequency** | ~200-300 service complaints/year chain-wide |
| **Volume** | ~15-25 complaints/month across 200 stores |
| **Owner** | Services Category Manager |
| **Participants** | Customer, Store Manager, Service Contractor/Partner, Finance, Quality Assurance, VP for Merchandising |

### Background

BuildRight's value-added services — particularly home installation (W138) and custom processing (W168, W169) — carry unique quality and liability risks distinct from merchandise sales: faulty installation causing property damage, incorrect paint mixing requiring rework, cutting errors wasting material, or contractor no-shows delaying customer projects. Service complaints require specialized handling: contractor performance assessment, rework scheduling, material replacement coordination, and potential liability claims. While W41 covers general customer complaints and W33 covers warranty claims, this workflow addresses service-specific complaint resolution with contractor accountability.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Complaint Receipt & Classification**: Customer reports service issue via store visit, call center per W259, or email: Store Manager or Call Center Agent logs complaint in system with: (a) original service order reference (W138, W139, W147, W148, W168, W169, W211); (b) complaint type: quality (poor workmanship), timeliness (late/no-show), material (wrong product installed), safety (hazard created), billing (overcharge); (c) severity: minor (cosmetic, easily reworkable), major (functional failure, property damage risk), critical (safety hazard, active property damage) | Store Mgr / Call Center | Services Category Mgr | 15-30 min |
| 2 | **Immediate Resolution (Minor)**: For minor complaints (cosmetic issues, small rework): (a) Store Manager contacts contractor to schedule rework within 48 hours; (b) contractor returns to site to correct issue; (c) customer confirms satisfaction; (d) complaint closed; (e) contractor quality record updated in W600 accreditation file | Store Manager | Services Category Mgr | 1-2 days |
| 3 | **Investigation (Major/Critical)**: For major or critical complaints: (a) Services Category Manager reviews complaint details and original service order; (b) contacts contractor for their account of events; (c) if property damage or safety risk: dispatch inspector within 24 hours for site assessment with photos; (d) if billing dispute: Finance reviews original invoice vs. actual service delivered; (e) root cause analysis: was it contractor error, material defect, customer misuse, or scope ambiguity per W794 | Services Category Mgr | VP Merchandising | 2-5 days |
| 4 | **Corrective Action & Rework Scheduling**: Based on investigation: (a) if contractor error: contractor performs rework at their cost per service agreement; (b) if material defect: coordinate replacement per W12 returns process; (c) if BuildRight scope ambiguity: BuildRight bears rework cost and updates W794 service SKU description; (d) schedule rework with customer within 7 days; (e) if rework requires new materials: issue internal PO per W136 indirect procurement | Services Category Mgr / Contractor | VP Merchandising | 1-7 days |
| 5 | **Customer Compensation**: Determine appropriate compensation: (a) full rework at no charge (contractor cost); (b) partial refund for inconvenience (store credit per W781 or cash refund per W101); (c) for critical issues causing property damage: coordinate with Insurance per W610; (d) goodwill gesture (discount on future service, free workshop attendance per W147); (e) Finance processes compensation per W101 | Services Category Mgr / Finance | VP Merchandising | 1-3 days |
| 6 | **Contractor Accountability**: Update contractor performance record: (a) log complaint against contractor in W600 accreditation file; (b) deduct contractor payment for rework costs if contractor error; (c) if 3+ complaints in 6 months: trigger contractor quality audit per W213; (d) if critical safety complaint: suspend contractor pending investigation; (e) annual contractor re-accreditation considers complaint history per W706 | Services Category Mgr | VP Merchandising | 1-2 hours per complaint |
| 7 | **Service Improvement**: Monthly, Services Category Manager reviews all service complaints: (a) complaint rate by service type and store; (b) top complaint root causes; (c) contractor performance by complaint frequency; (d) update W794 service SKU descriptions if scope ambiguity is recurring root cause; (e) update W600 contractor training requirements if skill gaps are identified | Services Category Mgr | VP Merchandising | 2-4 hours/month |

### System Touchpoints

- Service complaint module linked to original service order (W138, W139, W147, W148, W168, W169, W211)
- Contractor performance database per W600 accreditation
- Customer complaint escalation matrix per W597
- Billing adjustment module per W101 for refunds
- Insurance claims module per W610 for property damage
- Store credit issuance per W781 for compensation
- Service analytics dashboard for complaint trend analysis

### Pain Points / Risks

- **Contractor accountability gaps**: external contractors may resist rework at their own cost, dispute fault, or simply stop responding; BuildRight bears the customer relationship risk while contractor disputes drag on
- **Property damage liability**: faulty installation (e.g., electrical work, plumbing) can cause property damage far exceeding the original service fee; liability insurance adequacy per W610 is critical
- **Customer escalation to DTI**: unresolved service complaints may escalate to DTI Consumer Adjudication per W469, creating regulatory exposure and reputational risk
- **Rework scheduling conflicts**: contractor availability for rework may be 1-2 weeks out, leaving customer dissatisfied during the wait period
- **Service quality inconsistency across stores**: 200 stores with different contractors and varying service quality standards; customer experience varies significantly by location
- **Contractor disputes over fault**: contractors may blame material quality (BuildRight's product) while BuildRight blames workmanship; root cause analysis must be objective and evidence-based

### Staffing Implication

- **Services Category Manager**: ~10-15 hours/month on service complaint management; absorbed by existing role
- **Store Managers**: ~2-3 hours/month per store on initial complaint receipt and minor resolution; absorbed by existing role
- **No incremental headcount**.

### Time Estimate

- Minor complaint resolution: 1-2 days
- Major/critical complaint investigation: 2-5 days
- Rework scheduling and execution: 1-7 days
- Customer compensation processing: 1-3 days
- Monthly service improvement review: 2-4 hours
- **Total per complaint**: 2-15 days from receipt to close-out (severity-dependent)
