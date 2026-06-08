# Additional Operational Workflows — Batch 8

> Store-level welding gas cylinder exchange & refill service, customer electrical panel & circuit breaker sizing recommendation service, customer bathroom renovation complete project planning & material bundle service, customer termite & pest control product selection & treatment plan recommendation, store-level customer fire suppression system design & product recommendation, customer earthquake-resistant construction material selection & retrofit advisory, customer flood-resistant construction material recommendation, store-level customer building permit documentation package preparation assistance, customer smart home system design & product recommendation service, store-level customer marine & coastal construction material selection advisory, customer house foundation type recommendation & material estimation service, customer home office & workspace design consultation service, customer roof truss & structural frame material estimation service, customer garden & outdoor kitchen design consultation service, store-level customer construction site portable toilet & temporary facility rental coordination, customer rainwater collection & storage system complete package design, customer swimming pool construction material estimation service, store-level customer construction scaffold & ladder safety consultation, customer construction project insurance coverage advisory service, and store-level customer construction material quality verification & grade certification assistance.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain (Cross-Functional Batch)

- [W1063. Store-Level Customer Welding Gas Cylinder Exchange & Refill Service](#w1063-store-level-customer-welding-gas-cylinder-exchange--refill-service)
- [W1064. Customer Electrical Panel & Circuit Breaker Sizing Recommendation Service](#w1064-customer-electrical-panel--circuit-breaker-sizing-recommendation-service)
- [W1065. Customer Bathroom Renovation Complete Project Planning & Material Bundle Service](#w1065-customer-bathroom-renovation-complete-project-planning--material-bundle-service)
- [W1066. Customer Termite & Pest Control Product Selection & Treatment Plan Recommendation](#w1066-customer-termite--pest-control-product-selection--treatment-plan-recommendation)
- [W1067. Store-Level Customer Fire Suppression System Design & Product Recommendation](#w1067-store-level-customer-fire-suppression-system-design--product-recommendation)
- [W1068. Customer Earthquake-Resistant Construction Material Selection & Retrofit Advisory](#w1068-customer-earthquake-resistant-construction-material-selection--retrofit-advisory)
- [W1069. Customer Flood-Resistant Construction Material Recommendation](#w1069-customer-flood-resistant-construction-material-recommendation)
- [W1070. Store-Level Customer Building Permit Documentation Package Preparation Assistance](#w1070-store-level-customer-building-permit-documentation-package-preparation-assistance)
- [W1071. Customer Smart Home System Design & Product Recommendation Service](#w1071-customer-smart-home-system-design--product-recommendation-service)
- [W1072. Store-Level Customer Marine & Coastal Construction Material Selection Advisory](#w1072-store-level-customer-marine--coastal-construction-material-selection-advisory)
- [W1073. Customer House Foundation Type Recommendation & Material Estimation Service](#w1073-customer-house-foundation-type-recommendation--material-estimation-service)
- [W1074. Customer Home Office & Workspace Design Consultation Service](#w1074-customer-home-office--workspace-design-consultation-service)
- [W1075. Customer Roof Truss & Structural Frame Material Estimation Service](#w1075-customer-roof-truss--structural-frame-material-estimation-service)
- [W1076. Customer Garden & Outdoor Kitchen Design Consultation Service](#w1076-customer-garden--outdoor-kitchen-design-consultation-service)
- [W1077. Store-Level Customer Construction Site Portable Toilet & Temporary Facility Rental Coordination](#w1077-store-level-customer-construction-site-portable-toilet--temporary-facility-rental-coordination)
- [W1078. Customer Rainwater Collection & Storage System Complete Package Design](#w1078-customer-rainwater-collection--storage-system-complete-package-design)
- [W1079. Customer Swimming Pool Construction Material Estimation Service](#w1079-customer-swimming-pool-construction-material-estimation-service)
- [W1080. Store-Level Customer Construction Scaffold & Ladder Safety Consultation](#w1080-store-level-customer-construction-scaffold--ladder-safety-consultation)
- [W1081. Customer Construction Project Insurance Coverage Advisory Service](#w1081-customer-construction-project-insurance-coverage-advisory-service)
- [W1082. Store-Level Customer Construction Material Quality Verification & Grade Certification Assistance](#w1082-store-level-customer-construction-material-quality-verification--grade-certification-assistance)

---

## W1063. Store-Level Customer Welding Gas Cylinder Exchange & Refill Service

| Field | Detail |
|---|---|
| **Trigger** | Customer presents empty or near-empty welding gas cylinder (acetylene, argon, CO₂, oxygen, or mixed gas) for exchange or refill at store |
| **Frequency** | ~3,000–5,000 cylinder transactions/month across all stores (welding & metal fabrication services are a high-value B2B segment) |
| **Volume** | 1–4 cylinders per customer visit |
| **Owner** | Tools & Hardware Department Supervisor |
| **Participants** | Sales Associate (Tools/Hardware Section), Receiving Clerk, Customer |

### Background

Welding gas cylinder management is a specialized retail operation critical for BuildRight's professional contractor and metal fabricator customer base. The Philippines has a significant welding and metal fabrication industry — from small barangay-level shops to large construction contractors — and welding gas is a recurring consumable. Cylinders are typically supplier-owned (deposit-based) or customer-owned. The key gases sold through BuildRight are: (a) Acetylene (DA — Dissolved Acetylene) for oxy-acetylene cutting and welding; (b) Argon (Ar) for TIG/MIG welding of stainless steel and aluminum; (c) CO₂ and Argon/CO₂ mixes for MIG welding of mild steel; (d) Oxygen (O₂) for oxy-acetylene cutting; (e) Nitrogen (N₂) for pressure testing and pipe purging. Cylinders come in standard Philippine sizes: Size B (1 m³), Size C (2 m³), Size D (5 m³), and Size E (10 m³). The exchange model (return empty, receive full) is the dominant transaction pattern in Philippine retail because it avoids the customer needing to wait for on-site refilling. Safety is paramount — compressed gases are classified as hazardous materials per W236 (hazmat storage) and W698 (SDS management), and cylinders must be inspected for damage, valve integrity, and hydrostatic test date validity before acceptance for exchange.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Cylinder Inspection & Acceptance**: Sales Associate inspects the returned empty cylinder: (a) check cylinder body for dents, cracks, arc burns, or corrosion; (b) verify valve is intact and functional (no leaks detected by smell or sound); (c) check hydrostatic test date stamp — Philippine DOE/BFSR requires re-testing every 5 years; cylinders past test date must be rejected and customer directed to supplier for re-certification; (d) verify cylinder type matches gas type (color-coded per Philippine standard: acetylene = maroon, argon = dark green, CO₂ = gray, oxygen = black, nitrogen = black with white shoulder); (e) check for customer-owned vs. supplier-owned cylinder (identified by supplier stamp/label); (f) record cylinder serial number and condition in ERP per W92 (inventory adjustment for cylinder tracking) | Sales Associate | Tools & Hardware Dept Supervisor | 3–5 min |
| 2 | **Cylinder Exchange Selection & Inventory Check**: System identifies available full cylinders: (a) system queries real-time cylinder inventory (W533) by gas type, size, and supplier; (b) matching: customer receives same gas type and same size as returned cylinder; (c) for supplier-owned cylinders: system verifies supplier name on returned cylinder matches available exchange pool from same supplier; (d) for customer-owned cylinders: system processes as a refill transaction with customer's own cylinder sent to refilling partner; (e) system displays gas type, cylinder size, fill pressure, and exchange/refill price; (f) if out of stock on specific size, system offers alternative nearest-size option or rain check per W772 | Sales Associate / System | Tools & Hardware Dept Supervisor | 2–3 min |
| 3 | **Companion Product Recommendation**: System recommends welding consumables based on gas type: (a) for acetylene/oxygen customers: welding torch tips, filler rods (RA 6013, 7018 electrodes), flux, cutting torch attachments, striker/lighter; (b) for argon customers: TIG filler rods (ER308L, ER70S-6), tungsten electrodes, gas lenses, collet bodies, cup nozzles; (c) for CO₂/mix customers: MIG wire (ER70S-6), contact tips, nozzle gel, drive rolls; (d) PPE: welding helmet/goggles (auto-darkening lens), leather gloves, leather apron, spats; (e) safety: fire extinguisher per W1051, welding blanket, flash-back arrestor check; (f) system bundles recommendation with exchange transaction | System | Sales Associate | 1–2 min (automated) |
| 4 | **Transaction Processing & Cylinder Handoff**: (a) system processes exchange transaction at POS with cylinder deposit tracking (if supplier-owned): deposit amount held on customer's account, credited on return, new deposit charged on exchange; (b) for trade account B2B customers: transaction charged to account with monthly billing per W8; (c) Sales Associate issues full cylinder to customer with safety briefing: "Keep cylinder upright, secure during transport, do not modify valve, store in well-ventilated area, keep away from ignition sources"; (d) system prints gas safety data sheet summary per W698 (SDS management); (e) for customer-owned refills: issue claim stub with estimated refill date (typically 1–2 business days via refill partner); (f) cylinder serial number of issued full cylinder recorded against customer transaction for traceability | Sales Associate | Tools & Hardware Dept Supervisor | 3–5 min |
| 5 | **Cylinder Inventory Reconciliation & Replenishment**: (a) system updates cylinder count: +1 empty, −1 full for exchange transactions; (b) when empty cylinder count reaches reorder threshold per store (typically 5+ empty cylinders of same gas/size), system triggers automatic refill requisition to gas supplier via W2 (purchase order cycle); (c) for supplier-owned pool cylinders, system generates weekly supplier reconciliation report matching cylinders received vs. cylinders dispatched per location; (d) monthly cylinder inventory audit per W6 (cycle counting) — cylinders tracked individually by serial number; (e) hazmat storage compliance check per W236: ensure cylinder storage area has adequate ventilation, is separated from flammable materials, and has appropriate fire suppression per W1051 | Receiving Clerk / System | Tools & Hardware Dept Supervisor | Daily reconciliation: 15 min; Monthly audit: 2–3 hrs |

### System Touchpoints
- Cylinder inventory tracking module (serialized cylinder tracking by gas type, size, supplier)
- Real-time inventory availability per store (W533)
- POS transaction module with deposit management (W5)
- Hazmat storage compliance module (W236)
- SDS management system (W698)
- Purchase order / supplier requisition system (W2)
- Cycle counting module (W6)
- Trade account / B2B billing module (W8)

### Pain Points / Risks
- **Cylinder safety liability**: Damaged or expired cylinders pose explosion risk; staff must be trained to reject non-compliant cylinders per W237 (hazmat safety training); quarterly safety refresher required per W655
- **Supplier-owned cylinder reconciliation**: Cylinders from different suppliers (Linde/BOC, Air Liquide, Veritas, local refillers) must not be intermixed; supplier-owned cylinders returned to wrong supplier result in deposit disputes and penalty charges
- **Out-of-stock risk**: Welding gas is a just-in-time consumable for fabricators; stockouts drive customers to competitors; safety stock level must account for supplier delivery lead time (2–3 days for refills)
- **Regulatory compliance**: Philippine DOE Bureau of Fire Standards and Regulations (BFSR) requires all compressed gas cylinders to have valid hydrostatic test certification; sale or exchange of expired cylinders is a regulatory violation

### Staffing Implication
- **Sales Associate (Tools/Hardware Section)**: Cylinder inspection and exchange adds 3–5 minutes per transaction; at 15–25 exchanges per store per week, this represents ~1–2 hours/week; absorbed by existing Sales Associates
- **Receiving Clerk**: Cylinder delivery receipt and storage compliance adds ~30 min per delivery (1–2 deliveries/week per store)
- **No permanent incremental headcount**

### Time Estimate
- Cylinder inspection & acceptance: 3–5 min
- Exchange selection & inventory check: 2–3 min
- Companion product recommendation: 1–2 min (automated)
- Transaction & handoff: 3–5 min
- **Total per exchange transaction**: 9–15 min
- Daily reconciliation: 15 min
- Monthly cylinder audit: 2–3 hrs

---

## W1064. Customer Electrical Panel & Circuit Breaker Sizing Recommendation Service

| Field | Detail |
|---|---|
| **Trigger** | Customer requests electrical panel sizing, circuit breaker selection, or load center configuration for residential or small commercial construction project |
| **Frequency** | ~3,000–5,000 customer interactions/month across all stores (electrical is 10% of SKUs, ~3,500 items) |
| **Volume** | 1 panel/load center design per customer visit |
| **Owner** | Electrical Department Supervisor |
| **Participants** | Sales Associate (Electrical Section), Customer |

### Background

Electrical panel and circuit breaker selection is one of the most technical and safety-critical consultations in a home improvement retail environment. The Philippine Electrical Code (PEC) 2017 governs all electrical installations and mandates specific load calculations, conductor sizing, circuit breaker ratings, and panel configurations. The typical Filipino residential construction project involves: (a) a main load center (panel board) rated 100A or 200A depending on total connected load; (b) branch circuits for lighting, convenience outlets, air conditioning, kitchen appliances, water heaters, and special loads; (c) circuit breakers (MCB — miniature circuit breakers) rated 15A, 20A, 30A, 40A, 50A, or 60A per circuit; (d) safety devices: earth leakage circuit breakers (ELCB) or residual current devices (RCD), surge protection devices (SPD), and voltage protectors. Filipino homeowners and small contractors frequently make critical errors: undersized breakers that trip repeatedly, oversized breakers that fail to protect wiring (fire hazard), missing earth grounding, no surge protection (critical in a country with frequent lightning and voltage fluctuations), and incorrect phase balancing. BuildRight's electrical category represents ~PHP 6–7 billion/year in revenue. A consultative sizing service reduces returns of incorrectly-specified breakers (currently ~8–12% return rate in electrical), increases average basket size by recommending companion products (wire, conduit, boxes, accessories), and positions BuildRight as a trusted advisor — differentiating from competitors who sell electrical components without technical guidance. This workflow is distinct from W982 (electrical load calculation service) which covers general wire sizing; this workflow specifically addresses the panel board configuration and circuit breaker selection.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Project Load Assessment**: Sales Associate gathers electrical project details: (a) project type — new residential construction, renovation/addition, small commercial (sari-sari store, bakery, workshop), or appliance upgrade; (b) total floor area (sqm) and number of floors; (c) major electrical loads: air conditioning units (count, type: window/split, HP/BTU rating), electric water heater (yes/no, kW), electric stove/cooker (yes/no, kW), refrigerator, washing machine, microwave, pump motor (HP); (d) lighting load: LED (wattage per room, room count); (e) convenience outlet count by room; (f) special loads: elevator, pool pump, workshop equipment, EV charger; (g) service entrance: MERALCO / Davao Light / local electric cooperative, single-phase or three-phase supply available | Sales Associate | Electrical Department Supervisor | 5–8 min |
| 2 | **Total Connected Load & Demand Calculation**: System computes electrical load per PEC 2017: (a) general lighting load = total floor area × 36 VA/sqm (PEC Table); (b) small appliance branch circuits = minimum two 20A circuits at 1,500 VA each; (c) laundry circuit = 1,500 VA; (d) individual appliance loads per nameplate ratings; (e) largest motor load (typically aircon compressor) × 125% per PEC; (f) demand factor applied per PEC Table (first 3,000 VA at 100%, next 117,000 VA at 35%, remainder at 25% for residential); (g) system outputs: total connected load (VA), estimated demand load (VA after demand factors), recommended service rating (100A, 150A, 200A, or higher), recommended service entrance wire size (AWG) per W982 | System | Sales Associate | 2–3 min (automated) |
| 3 | **Panel Board & Circuit Breaker Configuration**: System designs panel layout: (a) selects main circuit breaker (MCB) rating matching service rating (100A/150A/200A); (b) allocates branch circuits: lighting circuits (15A each, max 10 outlets per circuit per PEC), convenience outlet circuits (20A each, max 6 outlets per circuit), dedicated circuits for major appliances (aircon: 30A/40A per unit, water heater: 30A/40A, electric stove: 50A/60A, pump: 20A/30A); (c) selects wire size per circuit per PEC Table (14 AWG for 15A, 12 AWG for 20A, 10 AWG for 30A, 8 AWG for 40A, 6 AWG for 50A/60A); (d) specifies safety devices: ELCB/GFCI (30mA trip) for wet areas (bathroom, kitchen, outdoor), SPD for main panel, automatic voltage regulator (AVR) recommendation for areas with unstable power; (e) system generates panel schedule diagram showing circuit number, breaker rating, wire size, load description, and phase assignment (for three-phase: balance loads across phases within 10% imbalance tolerance per PEC) | System | Electrical Department Supervisor | 3–5 min (automated) |
| 4 | **Complete Material List & Bill of Quantities**: System generates full BOM: (a) panel board enclosure (surface-mount or flush-mount, indoor/outdoor rated, IP rating for outdoor); (b) main breaker and branch breakers by brand carried in inventory (Schneider/Merte, ABB, GE, Siemens, Panasonic/Fujihoki — major brands available in PH); (c) ELCB/RCD devices; (d) SPD; (e) wire/cable per circuit (length estimated from floor area × 1.5 factor for routing per W982); (f) electrical metallic tubing (EMT) or PVC conduit per circuit; (g) junction boxes, outlet boxes, switch boxes; (h) switches (1-gang, 2-gang, 3-gang) and convenience outlets (with grounding per PEC); (i) panel board accessories: neutral bar, ground bar, panel cover, circuit directory label; (j) electrical tape, wire nuts, cable ties; (k) estimated total material cost; (l) for trade accounts, system applies contracted pricing per W163 | System | Sales Associate | 2–3 min (automated) |
| 5 | **Estimate Generation, Safety Advisory & Customer Handoff**: (a) system generates printable/PDF estimate with: load calculation summary, panel schedule diagram, complete BOM with quantities and prices, total estimated cost; (b) safety advisory printed on estimate: "Electrical installations must comply with the Philippine Electrical Code (PEC) 2017. All work should be performed by a licensed Professional Electrical Engineer (PEE) or Registered Master Electrician (RME). This material list is for quantity estimation only and does not substitute for professional electrical design. BuildRight Depot recommends engaging a licensed electrician for installation."; (c) for B2B/trade customers, estimate converts to project quote per W162; (d) system offers optional: list of licensed electrician partners in customer's area per W904 (contractor referral service); (e) estimate saved to customer loyalty account per W17 | Sales Associate | Electrical Department Supervisor | 3–5 min |

### System Touchpoints
- Electrical load calculation engine (PEC 2017 compliant)
- Panel board configuration generator with circuit schedule
- Product master (W252) — breaker specifications, wire current ratings, panel board specifications
- Real-time inventory availability per store (W533)
- POS quotation module (W542) — estimate-to-sale conversion
- Loyalty account integration (W17)
- B2B quotation module (W162) — trade account project quotes
- Contractor referral database (W904)

### Pain Points / Risks
- **Safety liability**: Incorrect circuit breaker sizing can cause fire or electrocution; system must display prominent disclaimer that recommendations are for material quantity estimation only and do not constitute professional electrical engineering design
- **Brand compatibility**: Circuit breakers from different manufacturers are not interchangeable in the same panel board; system must enforce brand consistency within a single panel configuration
- **Regional power supply variability**: Some provincial electric cooperatives have unstable voltage (brownouts, voltage spikes); system should recommend AVR and SPD for these areas based on store location
- **PEC code updates**: Philippine Electrical Code is updated periodically; product master (W252) and calculation engine must be updated per code revision cycle

### Staffing Implication
- **Sales Associate (Electrical Section)**: Panel sizing consultation adds 8–15 minutes per interaction; at 15–25 electrical consultations per store per week, this represents ~3–6 hours/week; absorbed by existing Sales Associates with electrical section rotation
- **No permanent incremental headcount**; calculator tool reduces consultation time by ~50%

### Time Estimate
- Project load assessment: 5–8 min
- Demand calculation: 2–3 min (automated)
- Panel & breaker configuration: 3–5 min (automated)
- Complete BOM generation: 2–3 min (automated)
- Estimate & handoff: 3–5 min
- **Total per consultation**: 15–24 min (reduced from 30–45 min without calculator tool)

---

## W1065. Customer Bathroom Renovation Complete Project Planning & Material Bundle Service

| Field | Detail |
|---|---|
| **Trigger** | Customer requests comprehensive bathroom renovation material planning, either in-store at the tile/plumbing sections or via ecommerce project planner |
| **Frequency** | ~5,000–8,000 customer interactions/month across all stores (bathroom renovation involves tiles 12%, plumbing 12%, and electrical 10% of SKUs) |
| **Volume** | 1 complete project plan per customer |
| **Owner** | Tile & Flooring Gallery Supervisor (primary), with support from Plumbing and Electrical Department Supervisors |
| **Participants** | Sales Associate (Tile Section), Sales Associate (Plumbing Section), Sales Associate (Electrical Section), Customer |

### Background

Bathroom renovation is one of the highest-value and most complex DIY/professional projects in Philippine home improvement. A typical Filipino bathroom renovation involves 6–12 product categories and 50–150 individual SKUs: tiles (floor and wall), plumbing fixtures (toilet, lavatory, faucet, shower set), waterproofing, plumbing rough-in materials (pipes, fittings, valves), electrical (lighting, exhaust fan, water heater circuit), paint/moisture-resistant finish, accessories (mirror, towel bar, soap dish, toilet paper holder), and consumables (tile adhesive, grout, cement, sand). The average Filipino bathroom renovation costs PHP 30,000–150,000 depending on size and quality tier, making it one of BuildRight's highest-value project types per customer. Currently, customers must visit 3–4 different store sections and manually coordinate product compatibility (e.g., will this faucet fit this lavatory? does this toilet's rough-in distance match the existing plumbing? does this exhaust fan fit the duct opening?). This results in: (a) incomplete purchases (customer forgets necessary items like waterproofing, grout, or valves); (b) compatibility returns (~10–15% return rate on bathroom fixtures due to mismatch); (c) missed cross-sell opportunities (~PHP 5,000–15,000 in companion products per project not captured). This workflow provides a guided, end-to-end project planning experience that bundles all materials into a single quotation, ensures compatibility, and increases average transaction value by an estimated 25–35%. It is distinct from W965 (complete renovation package assembly) which handles order fulfillment; this workflow covers the upstream planning and material selection phase.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Project Scope Assessment & Site Measurement Intake**: Sales Associate gathers project details: (a) bathroom type — master bathroom, common bathroom, powder room, en-suite; (b) current bathroom dimensions: length × width × height (meters); (c) bathroom fixtures to be replaced: toilet, lavatory/sink, faucet, shower set, bathtub (if applicable); (d) scope: full renovation (strip to bare walls and rebuild) or fixture-only replacement; (e) budget tier: economy (PHP 20,000–40,000), standard (PHP 40,000–80,000), premium (PHP 80,000–150,000+); (f) existing plumbing configuration: wall-mounted vs. floor-mounted toilet, exposed vs. concealed shower valve, existing water heater (yes/no); (g) customer preference on style: modern minimalist, classic, industrial, Filipino tropical; (h) for in-store consultation, customer may bring photos of existing bathroom and reference images from BuildRight's design gallery per W211 (3D rendering) | Sales Associate | Tile & Flooring Gallery Supervisor | 8–12 min |
| 2 | **Core Fixture Selection & Compatibility Validation**: System guides fixture selection with compatibility enforcement: (a) **Toilet**: select from inventory — floor-mount (most common in PH) or wall-mount; rough-in distance (standard PH: 12 inches / 305mm); bowl shape (round or elongated); flush type (single-flush, dual-flush); system validates rough-in compatibility with customer's stated measurement; (b) **Lavatory/Sink**: select type — pedestal, wall-hung, under-counter, above-counter vessel, drop-in; number of basins (single or double); system validates faucet compatibility (mounting holes: single-hole, 4-inch centerset, 8-inch widespread); (c) **Faucet**: select per lavatory mounting type; validate hole count and spacing compatibility; (d) **Shower System**: select — showerhead only (wall-mounted), shower system with diverter, rain shower + handheld combo; validate water pressure suitability (Philippine municipal water pressure typically 15–40 PSI; recommend pressure-boosting pump if below 20 PSI); (e) **Water Heater**: if applicable — tankless electric (2.5–4.5 kW, requires dedicated circuit per W1064) or storage type (10–30 liters); validate electrical circuit availability per W1064; (f) system flags any compatibility issues with clear explanation and alternative product suggestions | Sales Associate / System | Tile & Flooring Gallery Supervisor | 10–15 min |
| 3 | **Tile & Wall Finish Selection & Quantity Calculation**: System calculates tile quantities per W963 (tile quantity calculator): (a) floor tile: select material (ceramic, porcelain, vinyl plank), size (30×30cm, 40×40cm, 60×60cm), slip resistance rating (R10 or higher for wet areas); system computes floor area ÷ tile area + 10% waste = floor tile quantity; (b) wall tile: select material, size (20×30cm, 25×40cm, 60×60cm), finish (glossy for easy cleaning, matte for modern look); system computes wall area (all walls minus door opening minus window opening minus fixture cutouts) ÷ tile area + 10% waste = wall tile quantity; (c) waterproofing: system recommends waterproofing membrane (sheet or liquid-applied) for shower area — minimum 1.8m height from floor per Philippine plumbing standards; computes quantity based on shower area dimensions; (d) tile adhesive: system selects adhesive type (standard cement-based for ceramic, modified polymer for porcelain, epoxy for high-moisture areas) and computes quantity per coverage rate; (e) tile grout: system computes grout quantity based on tile size, joint width, and total tiled area per W1061; (f) accent/feature tile: optional decorative band or feature wall — computed per linear meter or area | Sales Associate / System | Tile & Flooring Gallery Supervisor | 8–12 min |
| 4 | **Plumbing Rough-In Materials & Electrical Accessories**: System generates plumbing and electrical BOM: (a) **Plumbing rough-in**: PVC pipe (3/4" or 1" for supply, 3" or 4" for drainage), fittings (elbows, tees, couplings, reducers), gate valves/angle valves (for isolation), P-trap (for lavatory), closet flange (for toilet), flexible supply hoses (for faucet and toilet connection), plumber's tape/teflon tape, PVC solvent cement; (b) **Waterproofing ancillaries**: reinforcing fabric for corners, sealant for pipe penetrations, drain assembly; (c) **Electrical**: waterproof light fixture (IP65 rated for bathroom zone), exhaust fan sized per W1053, GFCI outlet or ELCB-protected circuit per W1064, switches (placed outside bathroom per PEC), wire and conduit for circuit extension; (d) **Accessories**: mirror (frameless or with frame, sized to vanity), towel bar, toilet paper holder, soap dish, toothbrush holder, robe hook, shower niche insert, shower curtain rod (if no glass enclosure), glass shower enclosure (if budget permits); (e) system validates quantities against bathroom dimensions and fixture count | System | Sales Associate | 3–5 min (automated) |
| 5 | **Complete Project Bundle Assembly & Estimate Generation**: (a) system aggregates all materials into single project bundle: fixtures, tiles, plumbing rough-in, electrical, waterproofing, adhesives/grout, accessories; (b) system applies bundle discount pricing (configurable: 5–15% on complete project bundles vs. individual item pricing per W93); (c) system generates comprehensive project estimate: itemized material list with quantities and unit prices, bundle discount applied, total project cost, estimated delivery volume (number of bags/boxes, weight, need for delivery service per W19/W668), recommended installation timeline (typical PH bathroom renovation: 5–10 working days), required tools list (notched trowel, tile cutter, spirit level, wrench set, etc.); (d) system saves estimate to customer's loyalty account; (e) customer can convert full bundle to in-store transaction or B2B project quote per W162; (f) optional: system triggers 3D rendering service per W211 for premium bathroom projects above PHP 80,000 | Sales Associate | Tile & Flooring Gallery Supervisor | 5–8 min |

### System Touchpoints
- Bathroom project planner engine (dimension-based material calculation)
- Product compatibility matrix (fixture-to-fixture, fixture-to-plumbing, fixture-to-electrical)
- Tile quantity calculator (W963 integration)
- Product master (W252) — fixture specifications, compatibility attributes, rough-in dimensions
- Bundle pricing engine (W93 integration)
- Real-time inventory availability per store (W533)
- POS quotation module (W542) — estimate-to-sale conversion
- B2B quotation module (W162) — trade account project quotes
- 3D rendering service integration (W211)
- Loyalty account integration (W17)
- Delivery scheduling module (W19/W668)
- Contractor referral database (W904)

### Pain Points / Risks
- **Fixture compatibility complexity**: The number of possible fixture combinations (toilet × lavatory × faucet × shower × heater) creates a large compatibility matrix; system must be maintained per product master governance (W252) with regular updates as products are added or discontinued
- **Hidden site conditions**: Customer-reported dimensions and existing plumbing configuration may not match reality; system must include disclaimer that actual quantities may vary after demolition reveals hidden conditions; recommend 10% contingency on all materials
- **Waterproofing criticality**: Improper waterproofing is the #1 cause of bathroom renovation failure in PH (water damage to lower floors); system must prominently recommend professional waterproofing application and not allow customers to skip this category
- **Electrical safety**: Bathroom electrical work has strict PEC requirements for GFCI/RCD protection and zone-based fixture ratings; system must enforce these per W1064

### Staffing Implication
- **Sales Associate (Tile Section)**: Bathroom project planning is the most complex in-store consultation (30–50 min total); at 8–15 bathroom projects per store per week, this represents ~5–12 hours/week; requires dedicated "bathroom project advisor" role filled by senior Sales Associates with tile + plumbing cross-training per W567
- **No permanent incremental headcount**; project planner tool reduces consultation time by ~40%
- **Recommended**: 1–2 Sales Associates per store designated as "project advisors" with cross-section training per W567 (skill matrix management)

### Time Estimate
- Project scope assessment: 8–12 min
- Core fixture selection: 10–15 min
- Tile & wall finish selection: 8–12 min
- Plumbing & electrical BOM: 3–5 min (automated)
- Bundle assembly & estimate: 5–8 min
- **Total per project consultation**: 34–52 min (reduced from 60–90 min across multiple sections without project planner)

---

## W1066. Customer Termite & Pest Control Product Selection & Treatment Plan Recommendation

| Field | Detail |
|---|---|
| **Trigger** | Customer reports termite infestation, requests preventive termite treatment, or seeks general pest control product recommendation for residential or commercial property |
| **Frequency** | ~4,000–6,000 customer interactions/month across all stores (Philippine termite infestation rates are among the highest in Southeast Asia due to tropical climate) |
| **Volume** | 1 treatment plan per customer visit |
| **Owner** | Building Materials Department Supervisor |
| **Participants** | Sales Associate (Building Materials / Garden Section), Customer |

### Background

The Philippines has one of the highest termite infestation rates in the world. The Philippine tropical climate (high temperature, high humidity, abundant rainfall) creates ideal conditions for subterranean termites (Coptotermes vastator and Macrotermes gilvus in particular), which cause an estimated PHP 5–10 billion in structural damage annually across the country. Virtually every Filipino homeowner will face a termite issue at some point. BuildRight Depot carries a comprehensive range of termite control and general pest control products across multiple categories: (a) pre-construction soil treatment chemicals (imidacloprid-based, fipronil-based); (b) post-construction remedial treatments (baiting systems, liquid barrier treatments, foam applications); (c) treated lumber and building materials (CCA-treated, ACQ-treated wood); (d) termite shields and physical barriers; (e) general household pest control (cockroach, mosquito, ant, rodent products); (f) agricultural/commercial-grade pesticides and herbicides (requires FPA license per W467). The consultative nature of pest control product selection is critical: wrong product selection wastes money (PHP 2,000–15,000 per treatment), wrong application method is ineffective, and chemical misuse poses health and environmental risks. This workflow provides a structured recommendation engine that matches the customer's specific pest problem, construction stage, and budget to the correct product and application protocol. It is distinct from W467 (specialized hardware permits for FPA-regulated chemicals) which covers regulatory compliance; this workflow covers the customer-facing product recommendation and treatment planning.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pest Problem Identification & Assessment**: Sales Associate identifies the pest issue: (a) pest type: termites (subterranean — most common in PH), cockroaches, mosquitoes, ants, rodents, wood borers, termitaria (mud tubes visible); (b) for termites: construction stage — pre-construction (new build, foundation stage), active construction (ongoing build, framing stage), post-construction (existing structure, infestation discovered), preventive maintenance (no active infestation, annual treatment); (c) for termites: infestation severity — mild (minor mud tubes, no structural damage yet), moderate (visible damage to wood elements, floor sagging), severe (structural compromise, multiple colonies); (d) structure type: single-story residential, multi-story residential, commercial building, wood-framed, concrete-framed with wood elements; (e) property size and perimeter measurement (for soil treatment quantity calculation); (f) presence of children, pets, or pregnant household members (affects product recommendation for indoor applications); (g) customer budget range | Sales Associate | Building Materials Dept Supervisor | 5–8 min |
| 2 | **Treatment Method Recommendation**: System recommends treatment method based on assessment: (a) **Pre-construction (new build)**: soil treatment — apply termiticide to soil beneath and around foundation prior to slab pouring; compute chemical quantity: perimeter × trench width (0.15m) × depth (0.30m) × application rate (5 liters/sqm); recommend imidacloprid 5% SC or fipronil 2.5% EC (products registered with FPA); physical barrier: stainless steel termite mesh or basaltic particle barrier at foundation penetration points; (b) **Post-construction (active infestation)**: combination approach — liquid barrier treatment (inject termiticide into soil along exterior perimeter through drilled holes at 0.5m intervals) plus in-ground baiting stations (install every 3m around perimeter); for severe infestations, recommend professional pest control operator (PCO) referral per W904; (c) **Preventive maintenance**: annual perimeter barrier retreatment or baiting station monitoring; (d) **General pest control**: cockroach gel bait placement (kitchen, bathroom, under sinks), mosquito larvicide (stagnant water treatment), ant bait stations, rodent traps and bait boxes; (e) system checks FPA license requirements per W467 — commercial-grade restricted chemicals require customer FPA license; retail-grade products available to general public | System / Sales Associate | Building Materials Dept Supervisor | 3–5 min |
| 3 | **Product Selection & Quantity Computation**: System selects products and computes quantities: (a) termiticide concentrate: brand (Spectracide, Enforcer, Solignum, local brands), dilution ratio (typically 0.05–0.10% active ingredient), total solution volume based on perimeter and application rate, number of concentrate containers needed; (b) application equipment: compressed air sprayer (5L or 10L capacity), injection rod for soil injection, drill bits (10mm for concrete injection holes); (c) bait stations: number based on perimeter (1 station every 3m), monitoring cards, bait cartridges; (d) safety equipment: chemical-resistant gloves (nitrile), N95 mask or half-face respirator, safety goggles, rubber boots, long-sleeve coveralls; (e) treated wood replacement: if termite-damaged wood elements identified, recommend ACQ-treated lumber replacement per W976 (lumber grade selection) with computed board footage; (f) preventive building materials: termite shield flashing for new construction, borate-treated wood for framing; (g) for general pest control: specific products by pest type with quantity based on property size | System | Sales Associate | 2–3 min (automated) |
| 4 | **Safety Briefing & Application Instructions**: (a) system prints product-specific application instructions: dilution ratios, application rates, re-entry intervals (typically 4–24 hours after treatment for indoor), rain-fastness (do not apply termiticide if rain expected within 2 hours per product label); (b) safety data sheet (SDS) summary printed per W698 — first aid measures, storage requirements, disposal instructions; (c) environmental advisory: do not apply near bodies of water, storm drains, or vegetable gardens; keep away from pet areas; (d) system displays FPA registration numbers on all chemical products for regulatory traceability; (e) for products requiring FPA license: verify customer license before sale per W467; if no license, redirect to retail-grade alternatives or licensed PCO referral per W904; (f) system offers optional: list of licensed PCO partners in customer's area for professional application services | Sales Associate | Building Materials Dept Supervisor | 3–5 min |

### System Touchpoints
- Pest control product recommendation engine (pest type → treatment method → product selection)
- Chemical quantity calculator (perimeter-based computation for soil treatments)
- Product master (W252) — chemical specifications, application rates, FPA registration numbers
- FPA license verification module (W467 integration)
- SDS management system (W698)
- Real-time inventory availability per store (W533)
- POS transaction module (W5)
- Contractor referral database (W904) — licensed PCO partners
- Hazmat storage compliance module (W236) — in-store chemical storage

### Pain Points / Risks
- **Chemical safety liability**: Incorrect application of termiticides can contaminate groundwater and pose health risks; prominent disclaimer required: "Follow product label instructions exactly. BuildRight Depot is not liable for misuse of chemical products."
- **FPA regulatory compliance**: Sale of restricted agricultural/structural pesticides without valid FPA license is a regulatory violation per W467; POS system must enforce license check at transaction time
- **Treatment effectiveness**: Post-construction DIY termite treatment has variable effectiveness (60–80% success rate for barrier treatments); for severe infestations, system must strongly recommend professional PCO referral
- **Product availability**: Termite control chemicals have seasonal demand spikes (pre-rainy season construction surge); safety stock levels must be proactively managed per W57

### Staffing Implication
- **Sales Associate (Building Materials/Garden Section)**: Pest control consultation adds 5–10 minutes per interaction; at 20–30 consultations per store per week, this represents ~3–5 hours/week; absorbed by existing Sales Associates
- **No permanent incremental headcount**

### Time Estimate
- Pest problem identification: 5–8 min
- Treatment method recommendation: 3–5 min
- Product selection & quantity: 2–3 min (automated)
- Safety briefing & instructions: 3–5 min
- **Total per consultation**: 13–21 min

---

## W1067. Store-Level Customer Fire Suppression System Design & Product Recommendation

| Field | Detail |
|---|---|
| **Trigger** | Customer requests fire suppression system components for residential, small commercial, or light industrial application |
| **Frequency** | ~1,500–2,500 customer interactions/month across all stores (fire safety is a growing segment driven by BFP enforcement and insurance requirements) |
| **Volume** | 1 system design per customer visit |
| **Owner** | Safety & PPE Department Supervisor |
| **Participants** | Sales Associate (Safety/PPE Section), Customer |

### Background

Fire safety compliance in the Philippines is governed by RA 9514 (Revised Fire Code of the Philippines) and enforced by the Bureau of Fire Protection (BFP). The Fire Code mandates specific fire suppression equipment for all buildings: fire extinguishers (minimum 1 per 200 sqm of floor area, per BFP rules), fire alarm systems for buildings above 3 stories, automatic sprinkler systems for buildings above 15m in height or specific occupancy types, and fire exits with illuminated signage. BuildRight Depot's customer base increasingly requests fire suppression system components for: (a) residential homes (fire extinguishers, smoke detectors, fire blankets); (b) small commercial establishments (sari-sari stores, eateries, workshops — fire extinguishers, fire hose cabinets, smoke detectors); (c) light industrial/workshop facilities (dry chemical systems for paint booths, CO₂ systems for electrical rooms, foam systems for flammable liquid storage); (d) construction sites (temporary fire suppression during construction per DOLE DO 13 compliance per W789). The Philippine fire safety market is growing at ~10–15% annually due to stricter BFP enforcement, insurance requirements, and increasing urbanization. BuildRight carries fire extinguishers (ABC dry chemical, CO₂, water, foam), smoke detectors, fire alarm panels, fire hose and cabinets, fire sprinkler heads, fire blankets, fire-resistant safes, and emergency lighting. This workflow provides a structured system design recommendation that matches the customer's building type and occupancy to the correct fire suppression products per RA 9514 and BFP rules. It is distinct from W1051 (fire extinguisher monthly inspection) which covers ongoing maintenance; this workflow covers the initial system design and product selection.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Building & Occupancy Assessment**: Sales Associate gathers building details: (a) building type: residential (single detached, townhouse, apartment/condo), commercial (retail, restaurant, office, warehouse), industrial (workshop, manufacturing, storage); (b) total floor area per floor and number of floors; (c) occupancy classification per RA 9514: residential, educational, institutional, assembly, mercantile, business, industrial, storage, hazardous; (d) special hazard areas: kitchen (cooking oil fire risk), electrical room (electrical fire risk), paint/chemical storage (flammable liquid risk), server/IT room (sensitive electronic equipment); (e) existing fire suppression equipment: fire extinguishers (type, age, last inspection date), smoke detectors (present/absent), fire alarm system (present/absent); (f) BFP Fire Safety Inspection Certificate (FSIC) status per W476 — is this a new application or FSIC renewal? | Sales Associate | Safety & PPE Dept Supervisor | 5–8 min |
| 2 | **Fire Suppression System Design per RA 9514**: System designs fire suppression layout based on assessment: (a) **Fire extinguisher placement**: compute minimum number of extinguishers = total floor area ÷ 200 sqm (BFP minimum) + 1 per floor; select extinguisher type per hazard: ABC dry chemical (general purpose — kitchen, workshop, office), CO₂ (electrical rooms, server rooms, sensitive equipment — no residue), foam/water (combustible solid materials — warehouses, storage); compute total extinguisher count by type; (b) **Smoke/heat detectors**: minimum 1 per room for residential; 1 per 50 sqm for commercial spaces per BFP rules; interlinked detectors for multi-room coverage; recommend combination smoke + CO detector for residences with gas appliances; (c) **Fire alarm system**: for commercial/industrial — conventional or addressable fire alarm panel, manual call points at exits, sirens/strobes per floor; (d) **Fire hose cabinet / standpipe system**: required for buildings >2 stories per RA 9514 — hose cabinet per floor landing, fire hose (1.5" diameter × 30m), nozzle, gate valve; (e) **Sprinkler system**: if required by occupancy type — sprinkler heads (pendant, upright, sidewall), piping, control valve, alarm valve; (f) **Kitchen fire suppression**: wet chemical fire suppression system for commercial kitchens (K-class extinguisher or automatic suppression hood) | System | Safety & PPE Dept Supervisor | 5–8 min (automated) |
| 3 | **Product Selection & Quantity Computation**: System selects specific products from inventory: (a) fire extinguishers: brand, capacity (2kg/3kg/5kg/9kg for dry chemical; 2kg/5kg for CO₂), wall-mount brackets, extinguisher cabinets (for commercial/guest-facing areas), signage ("Fire Extinguisher" per BFP standard, location markers); (b) smoke detectors: battery-operated (residential), hardwired with battery backup (commercial), interlinkable models; mounting bases; (c) fire alarm panel: zones based on floor count and room count; smoke/heat detectors per zone; manual call points (per exit); sirens and strobe lights; fire-resistant cabling; (d) fire hose cabinets: cabinet housing, fire hose rack, nozzle, gate valve, glass-front cabinet per BFP standard; (e) accessories: fire blankets (1m×1m for kitchen, 1.8m×1.8m for industrial), emergency exit signs (illuminated, battery-backed), fire escape route floor markings, fire ladder (residential, 2-story); (f) installation hardware: mounting brackets, fire-resistant anchors, conduit for alarm wiring; (g) system computes total material cost with installation supplies | System | Sales Associate | 3–5 min (automated) |
| 4 | **Estimate Generation & Compliance Documentation**: (a) system generates project estimate: floor plan overlay showing recommended extinguisher/detector placement locations, complete BOM with quantities and prices, total project cost; (b) BFP compliance documentation: system generates equipment summary compliant with FSIC application requirements per W476 — listing fire extinguisher types, quantities, locations, smoke detector count, fire alarm system specifications; this document can be attached to customer's FSIC application; (c) maintenance schedule: system generates annual inspection and maintenance schedule per W1051 (monthly visual inspection, annual professional servicing, hydrostatic testing per schedule); (d) safety advisory: "Fire suppression system installation must comply with RA 9514 (Revised Fire Code) and BFP implementing rules. BuildRight recommends professional installation by BFP-accredited fire safety contractors."; (e) optional: list of BFP-accredited fire safety contractor partners per W904 (contractor referral service); (f) estimate saved to customer loyalty account per W17 | Sales Associate | Safety & PPE Dept Supervisor | 5–8 min |

### System Touchpoints
- Fire suppression design engine (RA 9514 and BFP rules compliant)
- Product master (W252) — fire extinguisher specifications, detector coverage areas, alarm panel zone capacity
- Real-time inventory availability per store (W533)
- BFP FSIC compliance document generator (W476 integration)
- POS quotation module (W542) — estimate-to-sale conversion
- Contractor referral database (W904) — BFP-accredited fire safety contractors
- Loyalty account integration (W17)
- Fire extinguisher maintenance schedule module (W1051)

### Pain Points / Risks
- **Regulatory liability**: Fire safety recommendations must strictly follow RA 9514 and BFP rules; any deviation could expose BuildRight to liability; system must use latest BFP rules and include engineering disclaimer
- **Extinguisher type mismatch**: Using wrong extinguisher type (e.g., water on electrical fire, CO₂ on cooking oil fire) can worsen the fire; system must clearly label each extinguisher with its correct application class
- **Installation quality**: DIY fire suppression system installation by untrained customers may not meet BFP standards; recommend professional installation for all commercial/industrial systems
- **Product expiration**: Fire extinguishers require annual inspection and periodic hydrostatic testing per W1051; system should tag each sale with maintenance reminder to customer's loyalty account

### Staffing Implication
- **Sales Associate (Safety/PPE Section)**: Fire suppression system design adds 10–15 minutes per consultation; at 8–15 consultations per store per week, this represents ~2–4 hours/week; absorbed by existing Sales Associates
- **No permanent incremental headcount**

### Time Estimate
- Building assessment: 5–8 min
- System design: 5–8 min (automated)
- Product selection & quantity: 3–5 min (automated)
- Estimate & compliance documentation: 5–8 min
- **Total per consultation**: 18–29 min

---

## W1068. Customer Earthquake-Resistant Construction Material Selection & Retrofit Advisory

| Field | Detail |
|---|---|
| **Trigger** | Customer inquires about earthquake-resistant construction materials, seismic retrofit products, or structural reinforcement solutions for new or existing building in a seismically active zone |
| **Frequency** | ~1,000–2,000 customer interactions/month across all stores (increases significantly after major seismic events; PH sits on Pacific Ring of Fire with 5–10 significant earthquakes per year) |
| **Volume** | 1 advisory session per customer visit |
| **Owner** | Lumber & Building Materials Department Supervisor |
| **Participants** | Sales Associate (Building Materials Section), Customer |

### Background

The Philippines is located on the Pacific Ring of Fire and is one of the most earthquake-prone countries in the world. The Philippine Institute of Volcanology and Seismology (PHIVOLCS) identifies at least 16 active fault lines, including the West Valley Fault (which traverses Metro Manila and surrounding provinces with a potential M7.2 "Big One" scenario), the Philippine Fault Zone (spanning eastern Luzon to Mindanao), and the Cotabato Fault System in Mindanao. The National Structural Code of the Philippines (NSCP) 2015 mandates earthquake engineering requirements for all new construction, with seismic zone classifications determining the level of reinforcement required. BuildRight Depot serves both new construction customers (who need earthquake-compliant materials) and existing building owners (who need seismic retrofit solutions). Key earthquake-resistant construction materials include: (a) deformed steel reinforcing bars (rebar) Grade 60 (415 MPa) per PNS 48 — the minimum grade for structural elements in seismic zones; (b) structural steel sections (wide flange, H-beams, C-purlins) for moment-resisting frames; (c) anchor bolts and base plates for column-to-foundation connections; (d) epoxy injection systems for cracked concrete repair; (e) carbon fiber reinforced polymer (CFRP) wraps for column strengthening; (f) seismic isolation bearings (for premium construction); (g) hold-down anchors and tie-down straps for roof-to-wall-to-foundation load path continuity; (h) braced frame connectors and moment frame connections. This workflow provides a consultative advisory service that helps customers select appropriate earthquake-resistant materials and understand basic seismic construction principles, without providing structural engineering services (which must be performed by licensed civil engineers). It is distinct from W789 (construction safety management) which covers safety during construction; this workflow covers seismic design material selection.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Seismic Risk Assessment & Project Context**: Sales Associate gathers project details: (a) project type: new construction, seismic retrofit/upgrade, post-earthquake repair, or renovation requiring structural modification; (b) building location — determine seismic zone per NSCP seismic zone map: Zone 1 (lowest risk, parts of Palawan), Zone 2 (moderate, most of Visayas and Mindanao), Zone 3 (moderate-high, parts of Luzon), Zone 4 (highest, Metro Manila West Valley Fault zone, Eastern Leyte, Bohol, Surigao); (c) building type: residential (1–2 story, 3–5 story), commercial, industrial; (d) structural system: reinforced concrete frame, steel frame, confined masonry, reinforced masonry, timber frame; (e) soil type: rock/hard soil (Site Class A/B), stiff soil (Site Class C), soft soil (Site Class D/E — amplifies seismic waves and is the most dangerous); (f) scope: full structural system design, specific element reinforcement, or material supply only | Sales Associate | Lumber & Building Materials Dept Supervisor | 5–8 min |
| 2 | **Seismic Material Recommendation**: System recommends materials based on seismic zone and structural system: (a) **Reinforcing steel**: minimum Grade 60 (PNS 48) for all structural elements in Zone 3–4; rebar diameter per structural element: 10mm–12mm for ties/stirrups, 16mm–20mm for beams, 16mm–25mm for columns, 16mm–20mm for slabs; seismic detailing requirements: 135° hooks on ties, close spacing of ties at column-beam joints (plastic hinge zones per NSCP), lapped splices with minimum lap length; (b) **Structural connectors**: hold-down anchors (HDU series or equivalent) at all shear wall ends, tie-down straps from roof to wall, simpson strong-tie or equivalent connectors for all critical load path connections; (c) **Foundation**: anchor bolts (minimum 16mm diameter, embedded 300mm into concrete), base plates for steel columns, foundation reinforcement per NSCP; (d) **Concrete**: minimum compressive strength 25 MPa (3,500 psi) for structural elements in seismic zones, per NSCP 2015; (e) **Masonry**: confined masonry system (concrete columns and beams confining CHB walls) per PHIVOLCS-SATSIE recommendations — horizontal and vertical reinforcement in CHB cells; (f) **Retrofit materials**: CFRP wraps for column jacketing, steel plate bonding for beam strengthening, epoxy injection for crack repair, steel braces for lateral force-resisting system upgrade | System / Sales Associate | Lumber & Building Materials Dept Supervisor | 5–8 min |
| 3 | **Quantity Estimation & Product Selection**: System estimates quantities: (a) rebar: based on structural element type and standard spacing per NSCP (e.g., column ties at 100mm spacing in plastic hinge zone, 200mm elsewhere); system estimates total rebar weight (kg) using element dimensions and reinforcement schedule; (b) structural connectors: count based on number of joints, beam-column connections, and shear wall ends in building layout; (c) concrete volume: per element dimensions plus 5% waste factor per W1044; (d) masonry reinforcement: per linear meter of CHB wall × number of reinforced cells; (e) retrofit materials: per element surface area (CFRP wraps) or crack length (epoxy injection); (f) system selects specific products from inventory: rebar brand (local steel mills: SteelAsia, Capitol Steel, Dragon Steel), connector brand (Simpson Strong-Tie, local equivalent), concrete mix brand, and matches to customer's quality tier preference; (g) system generates BOM with quantities, unit weights, and total estimated cost | System | Sales Associate | 3–5 min (automated) |
| 4 | **Safety Disclaimer, Engineering Referral & Estimate**: (a) system generates estimate with items and quantities; (b) prominent disclaimer: "This material recommendation is for general guidance based on National Structural Code of the Philippines (NSCP) 2015 seismic requirements. BuildRight Depot does not provide structural engineering services. All seismic design must be performed by a licensed Civil Engineer specializing in structural engineering. BuildRight strongly recommends engaging a licensed structural engineer for seismic design, especially in Zone 3 and Zone 4 areas. Incorrect selection or installation of seismic-resistant materials can result in building collapse during an earthquake."; (c) list of licensed structural engineer partners available per W904 (contractor referral service); (d) for B2B/trade customers, estimate converts to project quote per W162; (e) estimate saved to customer loyalty account per W17 | Sales Associate | Lumber & Building Materials Dept Supervisor | 3–5 min |

### System Touchpoints
- Seismic zone classification lookup (NSCP seismic zone map — Philippine GIS data)
- Earthquake-resistant material recommendation engine per NSCP 2015
- Product master (W252) — steel grade specifications, connector load ratings, concrete strength grades
- Real-time inventory availability per store (W533)
- POS quotation module (W542)
- B2B quotation module (W162)
- Contractor referral database (W904) — licensed structural engineers
- Loyalty account integration (W17)

### Pain Points / Risks
- **Engineering liability**: Seismic design is life-safety critical; BuildRight must never provide structural engineering advice; all recommendations must be framed as "typical materials used per NSCP standards" with mandatory engineer referral
- **Substandard rebar risk**: The Philippine market has issues with substandard rebar (undersized, under-strength); BuildRight must ensure all rebar sold is PNS-certified and traceable per mill certification; W110 (supplier quality CAPA) and W819 (material review board) govern incoming quality inspection
- **Post-earthquake demand surge**: After major seismic events, demand for reinforcement materials spikes 300–500%; supply chain must be prepared per W558 (supply disruption contingency planning)
- **Regional variation**: Seismic requirements differ significantly between Zone 1 (Palawan) and Zone 4 (Metro Manila, Surigao); system must accurately classify store location and customer's project location

### Staffing Implication
- **Sales Associate (Building Materials Section)**: Seismic advisory adds 10–15 minutes per consultation; at 5–10 consultations per store per week, this represents ~1–3 hours/week; absorbed by existing Sales Associates
- **No permanent incremental headcount**; post-earthquake surge handled by cross-trained staff per W567

### Time Estimate
- Seismic risk assessment: 5–8 min
- Material recommendation: 5–8 min
- Quantity estimation: 3–5 min (automated)
- Disclaimer & estimate: 3–5 min
- **Total per consultation**: 16–26 min

---

## W1069. Customer Flood-Resistant Construction Material Recommendation

| Field | Detail |
|---|---|
| **Trigger** | Customer requests flood-resistant building materials for new construction, repair of flood-damaged structure, or property elevation/drainage improvement in flood-prone area |
| **Frequency** | ~2,000–3,500 customer interactions/month across all stores (PH experiences 20+ typhoons annually; ~40% of BuildRight stores are in flood-prone areas) |
| **Volume** | 1 recommendation per customer visit |
| **Owner** | Building Materials Department Supervisor |
| **Participants** | Sales Associate (Building Materials Section), Customer |

### Background

The Philippines ranks among the top 5 most climate-vulnerable countries globally and experiences an average of 20 typhoons per year, with 5–8 making landfall as severe storms. Annual flood damage to residential and commercial structures is estimated at PHP 15–30 billion nationwide. BuildRight Depot's 200-store footprint includes ~80 stores (40%) in flood-prone areas: Metro Manila (marikina, Pasig, Mandaluyong flood plains), Central Luzon (Pampanga, Bulacan — lahar-affected and typhoon-prone), Bicol region (typhoon corridor), Eastern Visayas (storm surge zones), and Mindanao river basin areas (Davao, Cotabato, Agusan marsh areas). Filipino homeowners and builders increasingly seek flood-resistant construction solutions including: (a) elevated slab-on-grade construction (raising finished floor level above flood line); (b) waterproof concrete and crystalline waterproofing admixtures; (c) flood-resistant wall materials (concrete block vs. drywall/plywood which disintegrate when submerged); (d) flood-proof doors and windows; (e) surface water drainage systems (French drains, catch basins, channel drains); (f) sump pump systems for below-grade areas; (g) flood barrier systems (temporary and permanent); (h) mold-resistant construction materials for post-flood renovation. This workflow provides structured product recommendations based on flood risk severity and construction type. It is distinct from W1023 (post-typhoon rapid reopening) which covers store operations; this workflow covers customer-facing material selection for flood resilience.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Flood Risk Assessment & Project Context**: Sales Associate gathers flood context: (a) project type: new construction (flood-resilient design), post-flood repair/renovation, property drainage improvement, or flood barrier installation; (b) flood history: does the property flood regularly (annual), occasionally (every 2–5 years), or rarely (historical flood events only)?; (c) typical flood depth at property: ankle-deep (0.15m), knee-deep (0.5m), waist-deep (1.0m), or above 1.0m; (d) flood duration: flash flood (recedes in hours), tidal/storm surge (recedes in 1–2 days), prolonged flooding (3–7 days from river overflow); (e) building type: single-story residential, multi-story residential, commercial/retail, warehouse/storage; (f) existing structure: concrete frame, wood frame, CHB walls, combination; (g) local government flood zone classification if known (LGU flood hazard maps); (h) customer goal: prevent water entry, minimize damage when water enters, or facilitate rapid recovery after flooding | Sales Associate | Building Materials Dept Supervisor | 5–8 min |
| 2 | **Flood-Resilient Material Recommendation**: System recommends materials based on flood risk level: (a) **Low flood risk (ankle-deep, brief)**: perimeter drainage — French drain (gravel + perforated PVC pipe), channel drain at entry points, surface grading away from structure, door flood barrier (removable aluminum barrier), waterproof sealant for ground-floor walls up to 0.5m; (b) **Moderate flood risk (knee-deep, 1–2 days)**: elevated floor slab — raise finished floor level 0.5m above highest recorded flood level using compacted fill + elevated slab per W1044; waterproof concrete (crystalline admixture added to concrete mix) for ground-floor slab and walls up to 1.0m; flood-resistant ground-floor finish (tile, not wood/laminate which warp); elevated electrical outlets (1.2m above floor per PEC); elevated water heater and appliances above flood line; (c) **High flood risk (waist-deep or above, prolonged)**: full elevated construction — stilts/columns raising entire ground floor above flood line; reinforced concrete columns designed for flood water pressure and debris impact; breakaway ground-floor walls (lightweight panels designed to collapse under flood pressure without compromising structural frame); sump pump system (automatic float-activated, with battery backup for power outages during typhoons); non-return valves on all drainage outlets to prevent sewage backflow; stainless steel or hot-dip galvanized hardware for below-flood-line connections (standard mild steel corrodes rapidly) | System / Sales Associate | Building Materials Dept Supervisor | 5–8 min |
| 3 | **Drainage System Design & Material Quantification**: System designs drainage and computes materials: (a) French drain: trench length (perimeter of structure), trench width (0.3m), depth (0.6m), gravel volume (m³), perforated PVC pipe length (4" diameter), geotextile fabric area; (b) catch basins: number based on low-point drainage (1 per 50 sqm of impervious surface); concrete catch basin body, grate (cast iron or HDPE), connection pipe to storm drain or discharge point; (c) channel drain: linear meters at doorways and driveway entries, polymer concrete or HDPE channel body, grate, end outlet; (d) sump pump: pump capacity (liters/minute) based on expected flood inflow rate; sump pit (500L minimum, polyethylene); discharge pipe (1.5" PVC); float switch; battery backup system (deep-cycle marine battery + inverter for DC pumps); (e) surface grading: fill material volume (sand/gravel per W964), compaction equipment rental per W139 | System | Sales Associate | 3–5 min (automated) |
| 4 | **Post-Flood Renovation Material Kit** (if applicable): For customers repairing flood-damaged structures, system generates renovation kit: (a) mold remediation: bleach solution, mold-killing primer, HEPA mask (N95), disposable gloves, plastic sheeting for containment; (b) wall repair: replace water-damaged drywall/plywood with cement board (HardieFlex or equivalent — flood-resistant, does not disintegrate when wet), cement-based skim coat, mold-resistant paint; (c) floor repair: remove warped wood/laminate, install tile or vinyl plank (waterproof WPC/SPC type), tile adhesive and grout per W1061; (d) electrical: replace all submerged outlets, switches, and wiring per PEC (water-damaged electrical components must be replaced, not reused); (e) plumbing: flush all water lines, sanitize water tank, check for pipe joint damage | System | Sales Associate | 2–3 min (automated) |
| 5 | **Estimate Generation & Customer Handoff**: (a) system generates comprehensive estimate: flood risk assessment summary, recommended material list by category (structural, waterproofing, drainage, electrical, renovation), drainage system design sketch with material quantities, total estimated cost; (b) advisory: "Flood-resilient construction should be designed by a licensed civil engineer familiar with local flood conditions and NSCP requirements. BuildRight's material recommendations are for product selection guidance only."; (c) for drainage/flood barrier installation, offer referral to licensed contractors per W904; (d) for B2B customers, convert to project quote per W162; (e) estimate saved to loyalty account per W17 | Sales Associate | Building Materials Dept Supervisor | 3–5 min |

### System Touchpoints
- Flood risk assessment engine (flood depth → material recommendation)
- Drainage system design calculator (perimeter, area, volume-based)
- Product master (W252) — flood-resistant product attributes, waterproofing specifications
- Real-time inventory availability per store (W533)
- POS quotation module (W542)
- B2B quotation module (W162)
- Contractor referral database (W904)
- Loyalty account integration (W17)

### Pain Points / Risks
- **False sense of security**: No building material can guarantee 100% flood protection; disclaimer must state this clearly; recommend insurance coverage per W860 (business interruption) and W857 (property insurance)
- **Post-typhoon demand surge**: After major typhoons, flood-resistant materials sell out in 1–2 days; supply chain pre-positioning per W960 (seasonal forward stock) and W927 (rainy season emergency deployment) is critical
- **Construction quality**: Flood resilience depends as much on construction quality as on material selection; recommend professional installation for all structural and waterproofing work
- **LGU permitting**: Elevated construction and drainage modifications may require LGU building permits; advise customer to check local requirements per W1056

### Staffing Implication
- **Sales Associate (Building Materials)**: Flood resilience consultation adds 8–15 minutes; at 10–18 consultations per store per week (higher in flood-prone areas), this represents ~2–5 hours/week; absorbed by existing staff
- **No permanent incremental headcount**

### Time Estimate
- Flood risk assessment: 5–8 min
- Material recommendation: 5–8 min
- Drainage system design: 3–5 min (automated)
- Post-flood renovation kit (if applicable): 2–3 min (automated)
- Estimate & handoff: 3–5 min
- **Total per consultation**: 18–29 min

---

## W1070. Store-Level Customer Building Permit Documentation Package Preparation Assistance

| Field | Detail |
|---|---|
| **Trigger** | Customer requests assistance in preparing or organizing documentation required for local government building permit application for residential or small commercial construction |
| **Frequency** | ~2,500–4,000 customer interactions/month across all stores (LGU building permit is required for most construction projects in the Philippines) |
| **Volume** | 1 documentation package per customer |
| **Owner** | Pro Desk / Trade Counter Supervisor |
| **Participants** | Sales Associate (Pro Desk), Customer |

### Background

Obtaining a building permit in the Philippines is a multi-step bureaucratic process involving the Local Government Unit (LGU) Office of the Building Official (OBO). The National Building Code of the Philippines (PD 1096) and its Implementing Rules and Regulations (IRR) mandate specific documentation for building permit applications. For a typical residential or small commercial construction project, the required documents include: (a) duly accomplished building permit application form (LGU-specific); (b) lot plan and survey plan (prepared by licensed geodetic engineer); (c) building plans / architectural plans (prepared by licensed architect); (d) structural plans and calculations (prepared by licensed civil engineer); (e) electrical plans (prepared by licensed professional electrical engineer); (f) plumbing plans (prepared by licensed master plumber); (g) sanitary / mechanical plans (if applicable); (h) fire safety evaluation and compliance clearance per W476; (i) barangay clearance; (j) tax declaration and real property tax clearance; (k) DLL (Daily Log of Labor) and construction safety health program per DOLE; (l) contractor's license and PCAB (Philippine Contractors Accreditation Board) registration; (m) structural and geotechnical soil report (if required); (n) environmental compliance certificate (ECC) or certificate of non-coverage from DENR (if applicable); (o) Homeowners' Association (HOA) clearance (if in a subdivision); (p) fire safety inspection certificate from BFP per W476. BuildRight Depot's pro desk frequently encounters customers (especially DIY homeowners and small contractors) who are unfamiliar with the documentation requirements and whose projects are delayed by weeks or months due to incomplete permit applications. This workflow provides a documentation checklist and organizational assistance service — not a permit facilitation or expediting service — to help customers understand and prepare their building permit requirements, reducing project delays and increasing customer goodwill. It is distinct from W1056 (construction permit advisory) which provides general guidance; this workflow specifically addresses the documentation package preparation and organization.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Project Classification & Permit Requirement Determination**: Sales Associate determines permit requirements: (a) project type: new residential construction (1-story, 2-story, 3+ story), residential renovation/extension, new commercial construction, commercial renovation, fence/wall construction, demolition; (b) total floor area and number of floors; (c) project location: LGU name, barangay, subdivision (if applicable); (d) estimated construction cost (for fee computation); (e) system cross-references project parameters against PD 1096 requirements and LGU-specific checklist (system maintains a database of major LGU building permit requirements — initially covering BuildRight's 200 store locations across 150+ LGUs); (f) system determines which professional sign-offs are required: architect, civil engineer, electrical engineer, master plumber, sanitary engineer, fire safety engineer; (g) system determines which LGU offices must be visited: OBO (Building Official), barangay hall, BFP fire station, DENR (if applicable), HOA (if applicable) | Sales Associate / System | Pro Desk Supervisor | 5–8 min |
| 2 | **Documentation Checklist Generation**: System generates a customized permit documentation checklist: (a) system produces a detailed checklist specific to the project type and LGU, organized by submission order; (b) each checklist item includes: document name, issuing authority/professional, required copies (typically 3–5 sets), required format (blueprint, notarized, authenticated), estimated time to obtain (1 day to 6 weeks), and estimated cost of obtaining (professional fees, LGU fees); (c) typical professional fee ranges provided for guidance: architect (PHP 5–15% of construction cost), structural engineer (PHP 3–8%), electrical engineer (PHP 2–5%), master plumber (PHP 2–5%), geodetic engineer for lot plan (PHP 5,000–20,000); (d) LGU fee estimate computed per LGU fee schedule (typically 0.5–1.0% of estimated construction cost for building permit fee + ancillary fees); (e) system highlights critical-path documents (those with longest lead times, typically structural plans and geodetic survey: 2–4 weeks each) and recommends starting those first; (f) system flags documents that require notarization and provides list of nearby notary publics | System | Sales Associate | 2–3 min (automated) |
| 3 | **Professional Referral & Document Organizer**: (a) system offers referral to licensed professionals from BuildRight's partner network per W904: architects, civil engineers, electrical engineers, master plumbers, geodetic engineers — organized by service area (city/municipality); (b) system generates a printable "permit document organizer" folder cover sheet with: project name, applicant name, checklist with checkboxes for tracking completion, submission deadline tracker, LGU office visit log (date, office, person contacted, status); (c) for BuildRight pro/trade account customers: system offers to store digital copies of submitted permit documents in the customer's project file per W255 (electronic document storage) for future reference (e.g., renovation permits, FSIC renewals); (d) system provides LGU office addresses, operating hours, and contact numbers for the relevant OBO, barangay hall, BFP station, and DENR office | Sales Associate | Pro Desk Supervisor | 3–5 min |
| 4 | **Material List Integration & Project Kickstart**: (a) if customer has not yet purchased construction materials, system offers to generate material estimates per relevant workflows: W1044 (concrete), W1064 (electrical panel), W1068 (earthquake-resistant materials), W1069 (flood-resistant materials), W983 (roofing), W989 (plumbing layout), W1043 (paint), W991 (electrical circuit design); (b) system links material estimates to the permit documentation — the structural plans will specify material grades (rebar grade, concrete strength, steel specifications) that must match the materials purchased; (c) for B2B/trade customers converting to project quote per W162, system attaches permit documentation checklist to the project file; (d) system offers notification service: customer can opt in to receive reminders at key permit milestones (e.g., "Your building permit application has been pending for 3 weeks — have you followed up with OBO?") | Sales Associate | Pro Desk Supervisor | 3–5 min |

### System Touchpoints
- LGU building permit requirements database (PD 1096 + LGU-specific rules for 150+ LGUs)
- Professional fee estimation engine
- LGU fee computation engine
- Contractor/professional referral database (W904)
- Electronic document storage integration (W255)
- Material estimation workflow integration (W1044, W1064, W1068, etc.)
- B2B quotation module (W162)
- Loyalty account integration (W17)
- Notification/reminders engine

### Pain Points / Risks
- **LGU variability**: Each of the 150+ LGUs where BuildRight operates may have slightly different requirements; the LGU database must be regularly updated per W657 (regulatory change management); initial coverage should focus on top 50 LGUs by store count and expand incrementally
- **Not a permit facilitation service**: BuildRight does NOT facilitate, expedite, or bribe for permits; the service is strictly informational and organizational; anti-bribery compliance per W656 (ABAC program) must be reinforced with all pro desk staff
- **Professional liability**: BuildRight does not prepare engineering or architectural plans; referrals to licensed professionals are independent third parties and BuildRight is not liable for their work product
- **Corruption risk**: Building permit processes in some LGUs are associated with corruption/facilitation fees; BuildRight staff must never advise customers to pay facilitation fees or "fixers"

### Staffing Implication
- **Sales Associate (Pro Desk)**: Permit documentation assistance adds 10–15 minutes per customer; at 12–20 requests per store per week, this represents ~2–5 hours/week; absorbed by existing Pro Desk staff (1 CSR + 1 supervisor per store)
- **No permanent incremental headcount**

### Time Estimate
- Project classification: 5–8 min
- Checklist generation: 2–3 min (automated)
- Professional referral & organizer: 3–5 min
- Material integration: 3–5 min
- **Total per consultation**: 13–21 min

---

## W1071. Customer Smart Home System Design & Product Recommendation Service

| Field | Detail |
|---|---|
| **Trigger** | Customer requests smart home system design, home automation products, or IoT device integration for residential or small commercial property |
| **Frequency** | ~1,500–2,500 customer interactions/month across all stores (smart home adoption growing at 20–30% annually in PH, driven by upper-middle-class market) |
| **Volume** | 1 system design per customer visit |
| **Owner** | Electrical Department Supervisor |
| **Participants** | Sales Associate (Electrical Section), Customer |

### Background

The Philippine smart home market is in an early-growth stage, driven by increasing smartphone penetration (~75% of Filipino adults), improving internet connectivity (PLDT/Converge/Globe fiber expansion), growing middle-class disposable income, and the rise of affordable smart home brands (Xiaomi, Sonoff, Tuya-based products, TP-Link Kasa, Google Nest, Amazon Echo). BuildRight Depot is uniquely positioned to capture this growing segment because smart home products overlap significantly with existing product categories: smart lighting (electrical), smart locks and security cameras (hardware/security), smart switches and outlets (electrical), smart water leak detectors (plumbing), smart thermostats and aircon controllers (appliances), and smart garage/gate controllers (hardware). The typical Filipino smart home customer is: (a) a homeowner building a new house who wants to pre-wire for smart home; (b) a homeowner retrofitting an existing house with wireless smart devices; or (c) a small business owner wanting smart security and energy management for a store/office. Key technical considerations in the PH context: (a) Wi-Fi reliability — many Philippine homes have Wi-Fi dead spots; mesh Wi-Fi systems are often a prerequisite for smart home; (b) power outages — smart devices require UPS (uninterruptible power supply) to maintain operation during brownouts; (c) internet dependency — cloud-dependent devices become non-functional during internet outages; recommend local-processing devices where possible; (d) compatibility — not all smart home ecosystems are interoperable; recommend a single platform (Google Home, Apple HomeKit, or Tuya/Smart Life) per household. This workflow provides a consultative smart home system design service that ensures product compatibility, estimates total system cost, and integrates with BuildRight's electrical (W1064) and security product recommendations.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Smart Home Needs Assessment**: Sales Associate gathers smart home requirements: (a) project type: new construction (pre-wiring opportunity), existing home retrofit (wireless focus), small commercial (security + energy); (b) desired smart home categories: lighting control, security (cameras, smart locks, motion sensors), climate control (aircon smart controllers, ceiling fan control), entertainment (smart speakers, TV integration), energy management (smart plugs, energy monitoring), water management (leak detection, smart water valve), appliance automation (smart plugs for appliances), voice control (Google Assistant, Amazon Alexa, Apple Siri); (c) home size: number of rooms, floors, and total floor area; (d) existing infrastructure: Wi-Fi router model and coverage, internet speed (minimum 10 Mbps recommended for smart home), existing electrical panel capacity per W1064; (e) platform preference: Google Home (most popular in PH), Apple HomeKit (premium), Tuya/Smart Life (budget), or Amazon Alexa; (f) budget range: starter (PHP 5,000–15,000), standard (PHP 15,000–50,000), premium (PHP 50,000–200,000+) | Sales Associate | Electrical Department Supervisor | 5–10 min |
| 2 | **System Architecture Design**: System designs smart home architecture: (a) **Hub/gateway selection**: recommend appropriate smart home hub or use phone-as-hub approach based on platform; (b) **Wi-Fi infrastructure**: assess if existing Wi-Fi covers all rooms; if not, recommend mesh Wi-Fi system (2–3 node system for 80–150 sqm home); (c) **Device selection per room**: living room (smart lights, smart speaker, smart TV integration, smart aircon controller), bedroom (smart lights, smart plug for fan/appliance, motion sensor for night lighting), kitchen (smart smoke detector, smart plug for rice cooker/coffee maker, water leak sensor under sink), bathroom (smart exhaust fan timer, water leak sensor), main door (smart lock — fingerprint + PIN + app, smart doorbell camera), garage/gate (smart gate controller, motion-activated smart light), outdoor (IP65-rated smart cameras, smart landscape lighting); (d) **Communication protocol**: recommend mix — Wi-Fi for cameras and speakers (high bandwidth), Zigbee/Z-Wave for sensors and switches (low power, mesh network, no Wi-Fi congestion), Bluetooth for proximity-triggered actions; (e) **Power backup**: recommend UPS (650VA–1500VA) for smart home hub, Wi-Fi router, and security cameras to maintain operation during brownouts; (f) system ensures all recommended devices are compatible with customer's chosen platform | System | Sales Associate | 3–5 min (automated) |
| 3 | **Product Selection & Quantity Computation**: System selects products from inventory and computes quantities: (a) smart lights: count per room × bulb type (E27, GU10, downlight) + smart light switches for existing non-smart bulbs; (b) smart plugs: count per appliance to be automated; (c) smart cameras: indoor (pan-tilt) and outdoor (bullet/dome, IP65+) count based on entry points and coverage areas; (d) smart lock: main door unit + optional bedroom/office locks; (e) smart sensors: door/window contact sensors (per entry point), motion sensors (per room/hallway), water leak sensors (under sinks, near water heater, washing machine area), smoke detectors (per room per W1067); (f) smart aircon controllers: count per aircon unit; (g) smart speaker/voice assistant: count per room (recommend minimum: 1 for living room, 1 for bedroom); (h) smart switches: replace existing wall switches with smart switches (per switch count per room); (i) mesh Wi-Fi system: 2-pack or 3-pack based on home size; (j) UPS: sized to hub + router + cameras (typically 650VA–1500VA); (k) installation accessories: smart switch backboxes (deeper boxes required for smart switches), neutral wire adapter (some Philippine homes lack neutral wire in switch boxes), Ethernet cables for hub and camera wiring; (l) system generates total BOM with estimated cost | System | Sales Associate | 3–5 min (automated) |
| 4 | **Integration Advisory & Estimate Generation**: (a) system generates comprehensive estimate: device list organized by room, platform compatibility confirmation, network infrastructure assessment, total system cost; (b) installation advisory: "Smart home device installation ranges from plug-and-play (smart plugs, speakers) to professional installation (smart switches requiring wiring, smart locks, in-wall sensors). BuildRight recommends professional electrical installation for all in-wall devices per PEC requirements."; (c) offer referral to licensed electricians experienced in smart home installation per W904; (d) for new construction: recommend pre-wiring plan (Cat6 Ethernet to camera locations, neutral wire to all switch boxes, deeper backboxes for smart switches) to be incorporated into electrical plans per W1064; (e) system estimates monthly electricity impact of smart devices (typically PHP 100–300/month additional); (f) estimate saved to customer loyalty account per W17; (g) customer can convert to transaction at POS per W542 | Sales Associate | Electrical Department Supervisor | 3–5 min |

### System Touchpoints
- Smart home system design engine (room-based device recommendation)
- Device compatibility matrix (platform × device × protocol)
- Product master (W252) — smart device specifications, power requirements, protocol type
- Real-time inventory availability per store (W533)
- POS quotation module (W542)
- Contractor referral database (W904) — licensed electricians with smart home experience
- Electrical panel sizing integration (W1064)
- Loyalty account integration (W17)

### Pain Points / Risks
- **Rapid technology obsolescence**: Smart home technology evolves rapidly; products recommended today may be discontinued or unsupported within 2–3 years; recommend established brands with track record of long-term support
- **Wi-Fi reliability**: Many Philippine homes have inconsistent Wi-Fi; smart home experience depends on reliable internet and Wi-Fi coverage; system must assess Wi-Fi infrastructure first
- **Neutral wire absence**: Many Philippine homes built before 2010 lack neutral wires in switch boxes, which is required by most smart switches; system must ask about this and recommend no-neutral-wire alternatives or professional rewiring
- **Security/privacy**: Smart home devices collect significant personal data; system should recommend brands with strong privacy policies and recommend regular firmware updates

### Staffing Implication
- **Sales Associate (Electrical Section)**: Smart home consultation adds 10–20 minutes per session; at 8–12 consultations per store per week, this represents ~2–4 hours/week; requires smart home product knowledge training per W518
- **No permanent incremental headcount**; cross-training of existing electrical section staff per W567

### Time Estimate
- Needs assessment: 5–10 min
- System architecture: 3–5 min (automated)
- Product selection & quantity: 3–5 min (automated)
- Integration advisory & estimate: 3–5 min
- **Total per consultation**: 14–25 min

---

## W1072. Store-Level Customer Marine & Coastal Construction Material Selection Advisory

| Field | Detail |
|---|---|
| **Trigger** | Customer requests construction materials for a building project in a coastal or marine environment (within 1 km of coastline) |
| **Frequency** | ~800–1,500 customer interactions/month across all stores (~30% of BuildRight stores are in coastal municipalities; PH has 36,289 km of coastline, 4th longest in the world) |
| **Volume** | 1 advisory session per customer visit |
| **Owner** | Building Materials Department Supervisor |
| **Participants** | Sales Associate (Building Materials Section), Customer |

### Background

The Philippines is an archipelagic country with 36,289 km of coastline and over 60% of the population living in coastal areas. BuildRight Depot has approximately 60 stores (30%) located in coastal municipalities across Luzon, Visayas, and Mindanao. Construction in coastal and marine environments presents unique material challenges due to: (a) salt spray and saltwater exposure causing accelerated corrosion of steel, concrete deterioration (chloride attack), and metal fastener degradation; (b) high humidity (85–95% RH typical in coastal PH) promoting mold, wood rot, and metal oxidation; (c) typhoon-force winds (up to 250+ kph in coastal exposure) requiring enhanced structural connections and roof tie-downs; (d) storm surge and wave action requiring elevated construction and flood-resistant materials per W1069; (e) sand and salt accumulation requiring more frequent maintenance. Standard construction materials used in inland Philippines may have 30–50% shorter service life in coastal environments without proper material selection and protective measures. This workflow provides a specialized material advisory for coastal construction projects, recommending corrosion-resistant alternatives, enhanced protective coatings, and maintenance protocols appropriate for marine environments. It complements W1068 (earthquake-resistant materials) and W1069 (flood-resistant materials) which may apply simultaneously in coastal construction.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Coastal Environment Assessment**: Sales Associate assesses the coastal exposure: (a) distance from shoreline: direct beachfront (0–50m), near-coast (50–200m), coastal zone (200m–1km); (b) exposure type: full ocean exposure (direct wind and spray), sheltered bay (reduced wind and spray), inland waterway (river mouth, mangrove area); (c) wind exposure: typhoon corridor (eastern Visayas, Bicol, eastern Mindanao), moderate wind zone, sheltered; (d) construction type: new build, renovation, seawall/retaining wall, pier/dock, boat house; (e) structural system: reinforced concrete, steel frame, timber, combination | Sales Associate | Building Materials Dept Supervisor | 3–5 min |
| 2 | **Marine-Grade Material Recommendation**: System recommends corrosion-resistant materials: (a) **Reinforcing steel**: use epoxy-coated rebar or galvanized rebar for all concrete within 1km of coastline (instead of standard black rebar); alternatively, increase concrete cover (minimum 50mm cover to rebar in coastal exposure per NSCP, vs. 25mm standard); (b) **Concrete**: use sulfate-resistant Portland cement (Type V) or fly ash-blended cement for coastal foundations and ground-floor slabs; increase concrete grade to minimum 30 MPa for coastal exposure; specify concrete waterproofing admixture per W1069; (c) **Structural steel**: hot-dip galvanized steel sections (minimum 85 micron zinc coating) for all exposed structural steel; stainless steel (Grade 316) for fasteners and hardware within 200m of shoreline; (d) **Fasteners and hardware**: stainless steel bolts, nuts, washers (Grade 316/A4-70) for all exterior connections; stainless steel or silicon-bronze nails for exterior woodwork; avoid standard electro-galvanized fasteners (insufficient corrosion protection); (e) **Roofing**: pre-painted long-span GI roofing with minimum AZ150 zinc-aluminum coating (heavier than standard AZ70); stainless steel roofing screws with EPDM washers (not standard galvanized screws which corrode in 3–5 years in coastal); recommend roof tie-down straps per W1068 for typhoon resistance; (f) **Exterior wood**: use naturally durable timber species (tanguile, apitong, yakal) or pressure-treated wood (CCA or ACQ treatment per AWPA standards); avoid untreated wood which rots in 2–3 years in coastal humidity; (g) **Exterior paint/coating**: use marine-grade paint systems — epoxy primer + polyurethane topcoat for steel, elastomeric paint for concrete walls, wood preservative + marine varnish for timber; (h) **Doors/windows**: aluminum-framed windows (not steel which rusts) with stainless steel hardware; fiberglass or PVC doors (not wood which warps) for exterior | System / Sales Associate | Building Materials Dept Supervisor | 5–8 min |
| 3 | **Maintenance Protocol Recommendation**: System provides coastal maintenance schedule: (a) annual inspection of all steel connections for corrosion — replace any fastener showing red rust; (b) repaint exterior steel every 3–5 years (vs. 5–7 years inland); (c) inspect roof annually for corrosion, especially at screw points and overlaps; (d) clean and re-seal exterior wood annually with marine-grade preservative; (e) inspect concrete for spalling (chloride-induced rebar corrosion) every 2–3 years; (f) wash exterior surfaces monthly with fresh water to remove salt deposit; (g) system generates maintenance schedule card for customer's project file per W17 | System | Sales Associate | 2–3 min (automated) |
| 4 | **Quantity Adjustment & Estimate**: (a) system adjusts material quantities for coastal application: concrete cover increase (+25mm) requires additional concrete volume per pour; epoxy-coated rebar is ordered by the piece (cannot be field-bent, must be pre-fabricated); stainless steel fasteners ordered in bulk boxes; (b) cost comparison: system shows coastal premium over standard materials (typically 15–40% increase per item); (c) system generates estimate with coastal-grade material specifications; (d) advisory: "Coastal construction materials cost more upfront but provide 2–3× the service life of standard materials in marine environments. Using standard inland materials in coastal locations leads to premature failure, higher maintenance costs, and safety risks."; (e) for B2B/trade customers, convert to project quote per W162; (f) estimate saved to loyalty account per W17 | Sales Associate | Building Materials Dept Supervisor | 3–5 min |

### System Touchpoints
- Coastal material recommendation engine (distance from shore → material specification)
- Product master (W252) — corrosion resistance ratings, marine-grade specifications
- Real-time inventory availability per store (W533)
- POS quotation module (W542)
- B2B quotation module (W162)
- Loyalty account integration (W17)

### Pain Points / Risks
- **Cost sensitivity**: Marine-grade materials cost 15–40% more than standard; customers may resist the premium; system should clearly show long-term cost-benefit (total cost of ownership)
- **Product availability**: Marine-grade specialty items (epoxy-coated rebar, stainless steel fasteners, Type V cement) may have longer lead times and lower stock levels; system must check availability and offer pre-order per W38
- **Staff knowledge**: Coastal construction material selection requires specialized knowledge; training per W567 and W518 needed for staff in coastal-area stores
- **Code compliance**: NSCP and local building codes may have specific coastal construction requirements that supersede general recommendations

### Staffing Implication
- **Sales Associate (Building Materials)**: Coastal advisory adds 8–12 minutes per consultation; at 5–10 requests per coastal store per week, this represents ~1–2 hours/week; absorbed by existing staff
- **No permanent incremental headcount**; targeted training for coastal-area store staff per W567

### Time Estimate
- Coastal assessment: 3–5 min
- Material recommendation: 5–8 min
- Maintenance protocol: 2–3 min (automated)
- Estimate: 3–5 min
- **Total per consultation**: 13–21 min

---

## W1073. Customer House Foundation Type Recommendation & Material Estimation Service

| Field | Detail |
|---|---|
| **Trigger** | Customer requests foundation type recommendation and material estimation for new residential construction project |
| **Frequency** | ~3,000–5,000 customer interactions/month across all stores (foundation is the first major material purchase for any new construction project) |
| **Volume** | 1 foundation design per customer project |
| **Owner** | Lumber & Building Materials Department Supervisor |
| **Participants** | Sales Associate (Building Materials Section), Customer |

### Background

The foundation is the most critical structural element of any building — errors in foundation design or construction are extremely costly to rectify after the building is erected. Philippine residential construction uses several foundation types depending on soil conditions, building height, and seismic zone: (a) isolated footing (pad footing) — the most common for 1–2 story residential with reinforced concrete columns, each column has its own footing pad; (b) continuous footing (strip footing) — used for load-bearing wall construction, typically under CHB walls; (c) combined footing — when two columns are close together, their footings are combined; (d) mat/raft foundation — used for large buildings on weak soil, the entire building sits on a single concrete slab; (e) pile foundation — for very soft soil (common in coastal Mindanao, Metro Manila reclaimed areas), concrete or steel piles driven to load-bearing stratum; (f) elevated slab-on-grade — for flood-prone areas per W1069, the slab is raised on compacted fill. The key factors determining foundation type in the Philippines are: (a) soil bearing capacity — PH soils range from very hard limestone (Davao, Cebu) to very soft clay (Metro Manila, Agusan marsh); (b) number of floors — 1 story uses simpler footings than 3+ story; (c) seismic zone per W1068 — higher zones require stronger foundations; (d) flood risk per W1069 — flood-prone sites require elevated foundations; (e) water table depth — high water table (common in Metro Manila, coastal areas) requires waterproofing and dewatering during construction. This workflow provides a foundation type recommendation and material quantity estimation, linking to W1044 (concrete calculator), W1068 (seismic materials), and W1069 (flood-resistant materials).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Site & Building Assessment**: Sales Associate gathers project details: (a) number of floors: 1 story, 2 story, 3+ story; (b) building footprint dimensions (length × width in meters); (c) estimated building weight per floor: lightweight (wood frame, CHB walls) or heavy (concrete block walls, concrete slab floors); (d) soil type from customer's knowledge or geotechnical report: rock/limestone (excellent bearing), gravel/sand (good), stiff clay (fair), soft clay/silt (poor), reclaimed land or marsh (very poor); (e) water table: known high water table, unknown, or deep; (f) slope: flat (0–5%), gentle (5–15%), steep (>15% requiring retaining wall); (g) seismic zone per W1068; (h) flood risk per W1069 | Sales Associate | Lumber & Building Materials Dept Supervisor | 5–8 min |
| 2 | **Foundation Type Recommendation**: System recommends foundation type based on assessment: (a) **Isolated footing** (recommended for: 1–2 story, rock/gravel/sand soil, flat site): square or rectangular concrete pad under each column; typical size 0.80m × 0.80m × 0.25m (1 story) to 1.50m × 1.50m × 0.40m (2 story); rebar mesh top and bottom; (b) **Continuous/strip footing** (recommended for: 1–2 story load-bearing CHB walls, rock/gravel/sand/clay soil): continuous concrete strip under walls; typical width 0.40–0.60m, depth 0.25–0.40m; continuous rebar top and bottom with stirrups; (c) **Mat/raft foundation** (recommended for: 2–3 story, soft clay soil, or weak soil): entire building footprint as a single concrete slab 0.25–0.40m thick; reinforced with top and bottom rebar mesh; distributes load across entire footprint; (d) **Pile foundation** (recommended for: very soft soil, reclaimed land, marsh, high water table): driven or bored concrete piles 6–15m deep; pile cap connecting pile heads; requires piling contractor referral per W904; (e) system combines with W1068 seismic requirements: larger footings, more reinforcement in seismic zones 3–4; and W1069 flood requirements: elevated foundation in flood-prone areas | System | Lumber & Building Materials Dept Supervisor | 3–5 min (automated) |
| 3 | **Material Quantity Estimation**: System computes foundation materials per W1044 (concrete calculator): (a) concrete volume: footing dimensions × number of footings + waste factor (10%); (b) rebar: main bars (length per bar × number of bars per footing × number of footings), ties/stirrups (same computation); computed by rebar diameter and total weight (kg); (c) formwork: plywood sheets and lumber studs for forming footing excavations; (d) anchor bolts: 4 per column base plate, embedded in footing; (e) gravel bedding: 100mm gravel layer under footing for drainage; (f) waterproofing: bituminous coating on footing sides if high water table; (g) vapor barrier: 6mil polyethylene sheet under slab-on-grade; (h) backfill material: sand or gravel for backfilling around footings; (i) system generates complete foundation BOM with quantities and estimated cost | System | Sales Associate | 3–5 min (automated) |
| 4 | **Estimate, Engineering Referral & Customer Handoff**: (a) system generates foundation estimate: recommended foundation type with rationale, footing schedule (dimensions, rebar, concrete per footing), complete BOM, total estimated cost; (b) disclaimer: "Foundation design must be performed by a licensed Civil Engineer based on actual soil bearing capacity from a geotechnical investigation. This material estimate is for budgeting purposes only and does not substitute for professional foundation design. Foundation failures due to inadequate design are catastrophic and life-threatening. BuildRight strongly recommends engaging a licensed structural engineer and conducting a soil boring test before construction."; (c) referral to geotechnical engineers and licensed structural engineers per W904; (d) for B2B/trade customers, convert to project quote per W162; (e) estimate saved to loyalty account per W17 | Sales Associate | Lumber & Building Materials Dept Supervisor | 3–5 min |

### System Touchpoints
- Foundation type recommendation engine (soil type × floors × seismic zone × flood risk)
- Concrete volume calculator (W1044 integration)
- Rebar weight calculator (diameter × length × quantity × unit weight)
- Product master (W252) — rebar grades, concrete specifications, waterproofing products
- Real-time inventory availability per store (W533)
- POS quotation module (W542)
- B2B quotation module (W162)
- Contractor referral database (W904) — structural and geotechnical engineers
- Loyalty account integration (W17)
- Seismic zone classification (W1068 integration)
- Flood risk classification (W1069 integration)

### Pain Points / Risks
- **Geotechnical uncertainty**: Customer self-reported soil type may be inaccurate; geotechnical soil investigation (PHP 20,000–80,000) is essential for proper foundation design but many Filipino homeowners skip this step to save cost; BuildRight should strongly recommend it
- **Foundation failure liability**: Foundation failures are catastrophic; all recommendations must include engineering disclaimer and referral to licensed structural engineer
- **Substandard rebar**: Per W1068 risk note, substandard rebar is a market issue; all rebar sold for foundation use must be PNS-certified Grade 60 per W110 and W819

### Staffing Implication
- **Sales Associate (Building Materials)**: Foundation consultation adds 10–15 minutes; at 15–25 consultations per store per week, this represents ~3–6 hours/week; absorbed by existing staff
- **No permanent incremental headcount**

### Time Estimate
- Site assessment: 5–8 min
- Foundation type recommendation: 3–5 min (automated)
- Material estimation: 3–5 min (automated)
- Estimate & handoff: 3–5 min
- **Total per consultation**: 14–23 min

---

## W1074. Customer Home Office & Workspace Design Consultation Service

| Field | Detail |
|---|---|
| **Trigger** | Customer requests home office furniture, workspace layout design, or ergonomic setup recommendation |
| **Frequency** | ~2,000–3,000 customer interactions/month across all stores (post-pandemic WFH/hybrid work adoption; home office furniture is in the home décor & furniture category, 5% of SKUs) |
| **Volume** | 1 workspace design per customer |
| **Owner** | Home Décor & Furniture Department Supervisor |
| **Participants** | Sales Associate (Furniture/Home Décor Section), Customer |

### Background

The COVID-19 pandemic permanently changed the Philippine work landscape, with an estimated 30–40% of Metro Manila knowledge workers adopting some form of remote or hybrid work arrangement. Even post-pandemic, many Filipino professionals maintain a home office or dedicated workspace. BuildRight Depot's home décor and furniture category (5% of SKUs, ~1,750 items) includes desks, shelving, storage solutions, lighting, and workspace accessories. Additionally, the electrical, lighting, and storage categories overlap significantly with home office requirements. A typical home office setup involves: (a) a desk (standing desk, L-desk, or straight desk); (b) ergonomic seating; (c) shelving and storage (wall-mounted shelves, bookcases, filing cabinets); (d) task lighting (desk lamp, overhead lighting); (e) electrical (additional outlets per W1064, cable management, surge protector); (f) noise management (acoustic panels, weatherstripping for door seal); (g) air quality (exhaust fan, air purifier); (h) technology integration (monitor arm, cable management tray, smart plug per W1071). The average Filipino home office investment is PHP 15,000–50,000. This workflow provides a workspace design consultation that combines ergonomics, lighting, storage, and electrical planning into a single recommendation, increasing average basket size by cross-selling across categories.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Workspace Needs Assessment**: Sales Associate gathers workspace requirements: (a) workspace location: dedicated room, shared room (living room corner, bedroom), or multipurpose area; (b) available floor area (length × width); (c) primary use: computer/desk work, creative/artistic work, hybrid (work + hobby), study/learning; (d) number of monitors: 1, 2, or 3; (e) equipment: laptop, desktop PC, printer, scanner, other peripherals; (f) storage needs: books, files, supplies, equipment; (g) work style: sitting only, standing preference, sit-stand alternation; (h) number of users: 1 or 2+ (couple, parent + child); (i) budget tier: basic (PHP 5,000–15,000), standard (PHP 15,000–35,000), premium (PHP 35,000–80,000) | Sales Associate | Home Décor & Furniture Dept Supervisor | 5–8 min |
| 2 | **Workspace Layout Design**: System generates workspace layout recommendations: (a) desk placement: near window for natural light (but avoid screen glare), facing door if possible (psychological comfort), minimum 0.8m clearance behind chair; (b) desk size recommendation: 120cm × 60cm (single monitor, laptop), 150cm × 75cm (dual monitor), 180cm × 80cm (triple monitor or L-desk); (c) desk type: straight desk, L-desk (corner workspace), standing desk (electric height-adjustable); (d) chair: ergonomic office chair with lumbar support, adjustable height, adjustable armrests; seat height should allow feet flat on floor with 90° knee angle; (e) storage: wall-mounted shelves above desk (floating shelves or bracket shelves), under-desk drawer unit, bookcase or storage cabinet for files; (f) cable management: under-desk cable tray, cable clips/zip ties, power strip with surge protection | System / Sales Associate | Home Décor & Furniture Dept Supervisor | 3–5 min |
| 3 | **Lighting, Electrical & Environment Recommendation**: System recommends supporting elements: (a) task lighting: adjustable LED desk lamp (400–800 lumens, 4000K neutral white for focus), positioned opposite writing hand to avoid shadow; (b) ambient lighting: ceiling light or wall sconce to reduce contrast between screen and room (reduces eye strain); (c) electrical: dedicated outlet circuit or power strip with surge protector, USB charging hub, cable management; (d) acoustic: foam acoustic panels (60cm × 60cm) for echo reduction if room has hard surfaces; weatherstripping for door gap to reduce household noise; (e) air quality: desk fan or ceiling fan, optional air purifier for rooms without windows; (f) smart home integration per W1071: smart plug for automated device power management, smart lights for schedule-based lighting | System | Sales Associate | 2–3 min (automated) |
| 4 | **Product Bundle & Estimate Generation**: (a) system generates workspace bundle: desk, chair, shelving, storage, lighting, cable management, electrical accessories, acoustic treatment; (b) bundle discount applied per W93; (c) estimate includes room layout sketch with furniture placement, complete BOM with prices, total project cost, assembly options (self-assembly vs. delivery + assembly service per W138); (d) estimate saved to loyalty account per W17; (e) customer can convert to transaction at POS per W542 | Sales Associate | Home Décor & Furniture Dept Supervisor | 3–5 min |

### System Touchpoints
- Workspace layout recommendation engine (area-based furniture sizing)
- Ergonomic assessment guidelines
- Product master (W252) — furniture dimensions, weight ratings, lighting specifications
- Real-time inventory availability per store (W533)
- Bundle pricing engine (W93 integration)
- POS quotation module (W542)
- Smart home integration (W1071)
- Loyalty account integration (W17)

### Pain Points / Risks
- **Ergonomic liability**: BuildRight is not an ergonomic consultant; recommendations are general guidance based on industry standards; disclaimer required for specific ergonomic needs or medical conditions
- **Space constraints**: Filipino homes often have limited space for dedicated home offices; layout must work within realistic room dimensions
- **Assembly complexity**: Furniture assembly may require tools and time; offer delivery + assembly service per W138 for an additional fee

### Staffing Implication
- **Sales Associate (Furniture/Home Décor)**: Workspace consultation adds 8–12 minutes per session; at 10–15 sessions per store per week, this represents ~2–3 hours/week; absorbed by existing staff
- **No permanent incremental headcount**

### Time Estimate
- Needs assessment: 5–8 min
- Layout design: 3–5 min
- Lighting & environment: 2–3 min (automated)
- Bundle & estimate: 3–5 min
- **Total per consultation**: 13–21 min

---

## W1075. Customer Roof Truss & Structural Frame Material Estimation Service

| Field | Detail |
|---|---|
| **Trigger** | Customer requests roof truss design, structural frame material estimation, or roof framing material quantities for residential or small commercial construction |
| **Frequency** | ~2,500–4,000 customer interactions/month across all stores (roofing is a major project category; lumber & building materials is 14% of SKUs) |
| **Volume** | 1 roof system estimate per customer |
| **Owner** | Lumber & Building Materials Department Supervisor |
| **Participants** | Sales Associate (Building Materials Section), Customer |

### Background

Roof construction is one of the most material-intensive and structurally critical phases of Philippine residential construction. The roof system typically represents 15–20% of total construction material cost and must be designed to withstand: (a) typhoon-force winds (up to 250+ kph in eastern Visayas and Bicol); (b) earthquake lateral forces per W1068; (c) heavy rainfall (Philippine rainy season brings 200–400mm/month of rainfall); (d) solar heat gain (tropical sun requires insulation and ventilation considerations). The two dominant roof framing systems in the Philippines are: (a) wood/ timber truss — constructed from tanguile, apitong, or coco lumber, most common for 1–2 story residential; and (b) steel truss — constructed from tubular steel (round or square tubing) or C-purlins, increasingly common for 2+ story and commercial construction. BuildRight carries both timber and steel framing materials, plus GI roofing sheets, insulation, fascia boards, gutters, and complete roofing accessories. The typical Filipino homeowner/builder has difficulty estimating roof framing quantities because truss geometry involves angled cuts, varying member lengths, and connection hardware that are not intuitive to calculate. This workflow provides a roof truss material estimation based on building dimensions and roof style, computing complete framing, sheathing, roofing, and accessory quantities.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Roof System Specification**: Sales Associate gathers roof specifications: (a) building dimensions: length × width (meters); (b) number of floors and total building height at eave line; (c) roof style: gable (2-sided, most common in PH), hip (4-sided, better typhoon resistance), lean-to/skillion (single slope, for extensions), flat (concrete deck, for modern design or future 2nd floor); (d) roof pitch/slope angle: standard PH pitch 30°–45° (steeper for heavy rainfall areas, shallower for typhoon-prone areas to reduce wind uplift); (e) eave overhang: typical 0.6m–1.0m on all sides (for rain protection and shade); (f) framing material preference: timber (tanguile/apitong 2×4, 2×6), steel (square tubing 50×50×3mm, C-purlin 0.60mm–1.20mm thickness), or combination; (g) roofing material: long-span GI roofing (most common), tile (premium), or asphalt shingle; (h) insulation requirement: with or without roof insulation (foil insulation, foam board, or blown-in) | Sales Associate | Lumber & Building Materials Dept Supervisor | 5–8 min |
| 2 | **Truss Geometry & Frame Layout Computation**: System computes truss layout: (a) truss spacing: timber trusses every 0.60m–0.80m (2–3 feet), steel trusses every 1.0m–1.5m; (b) number of trusses = (building length ÷ truss spacing) + 1; (c) truss member lengths computed from roof pitch and span using trigonometry: rafter length = (half-span ÷ cos(pitch angle)) + eave overhang; ridge beam length = building length; (d) for gable roof: 2 rafters per truss + 1 ceiling joist (tie) per truss + ridge board + collar ties (every 3rd truss); (e) for hip roof: additional hip rafters (4 diagonals from corners) + jack rafters (shortened rafters against hip); (f) purlins (horizontal members spanning across trusses): number of rows per roof slope (typically 4–5 rows for GI roofing), length = building length + 2 × overhang; (g) system outputs: number of trusses, member lengths per truss type, total linear meters of each member type (rafters, ceiling joists, ridge, purlins, collar ties) | System | Sales Associate | 3–5 min (automated) |
| 3 | **Complete Roofing BOM Generation**: System generates full roof system BOM: (a) framing members: timber (2×4, 2×6, 2×8) in board feet or steel tubing/purlins in linear meters and kilograms; (b) connection hardware: timber — framing anchors, hurricane ties (critical for typhoon resistance per W1068), joist hangers, ridge strap, truss-to-wall anchors, galvanized nails (various sizes); steel — welding rods, self-drilling screws, base plates, anchor bolts; (c) roof decking/covering: long-span GI roofing sheets (compute number of sheets based on roof area ÷ effective coverage width), ridge cap, gable end flashing, valley flashing (for hip/L-roofs), eave flashing, drip edge; (d) waterproofing: roofing underlayment (asphalt felt or synthetic membrane), sealant for flashing joints; (e) insulation: foil insulation (reverse side of roofing, for heat reflection), or foam board insulation between purlins, compute area per roof slope; (f) fascia and soffit: fascia board (tanguile 1×8 or PVC fascia) at eave and gable ends, soffit vents for attic ventilation; (g) gutters and downspouts: continuous gutter length per W1052, downspouts at corners (minimum 1 per 10m gutter run per side), gutter accessories (end caps, corners, hangers); (h) fasteners: roofing screws with EPDM washers (color-matched to roofing), computed per sheet (minimum 12 screws per sheet per manufacturer spec); (i) paint/finish: primer and paint for timber members, rust-inhibitive primer for exposed steel; (j) system generates total BOM with quantities, unit costs, and estimated total cost | System | Sales Associate | 3–5 min (automated) |
| 4 | **Estimate, Wind Resistance Advisory & Customer Handoff**: (a) system generates comprehensive estimate: roof system specification summary, truss layout computation details, complete BOM organized by category (framing, hardware, roofing, insulation, gutters, accessories), total estimated material cost, estimated weight of roof system (for structural loading reference); (b) wind resistance advisory per NSCP and typhoon risk: "Roof framing connections must be designed to resist wind uplift forces per NSCP 2015. Hurricane ties at every rafter-to-wall and rafter-to-ridge connection are mandatory in typhoon-prone regions. BuildRight recommends professional installation by a licensed carpenter/structural engineer per W904."; (c) for B2B/trade customers, convert to project quote per W162; (d) system links to W983 (roofing material calculator) for roofing sheet verification and W1068 for seismic tie-down requirements; (e) estimate saved to loyalty account per W17 | Sales Associate | Lumber & Building Materials Dept Supervisor | 3–5 min |

### System Touchpoints
- Roof truss geometry calculator (pitch, span, overhang, member lengths)
- Framing material quantity engine (timber board feet / steel weight)
- Product master (W252) — lumber dimensions and grades, steel tubing specifications, roofing sheet dimensions
- Real-time inventory availability per store (W533)
- POS quotation module (W542)
- B2B quotation module (W162)
- Contractor referral database (W904)
- Loyalty account integration (W17)
- Seismic zone classification (W1068) for tie-down requirements

### Pain Points / Risks
- **Structural engineering liability**: Roof truss design is structural engineering work; this workflow provides material quantity estimation only; disclaimer must state that actual truss design must be performed by a licensed civil engineer
- **Typhoon wind uplift**: The most common roof failure mode in Philippine typhoons is wind uplift ripping the roof off the building; hurricane ties and proper fastener specification are life-safety critical
- **Timber quality**: Philippine construction timber (tanguile, apitong) varies significantly in quality; grading per W976 (lumber grade selection) must be enforced
- **Steel corrosion**: Steel trusses in coastal areas require galvanizing per W1072 (marine material advisory)

### Staffing Implication
- **Sales Associate (Building Materials)**: Roof estimation adds 10–15 minutes per consultation; at 12–20 consultations per store per week, this represents ~2–5 hours/week; absorbed by existing staff
- **No permanent incremental headcount**

### Time Estimate
- Roof specification: 5–8 min
- Truss computation: 3–5 min (automated)
- BOM generation: 3–5 min (automated)
- Estimate & handoff: 3–5 min
- **Total per consultation**: 14–23 min

---

## W1076. Customer Garden & Outdoor Kitchen Design Consultation Service

| Field | Detail |
|---|---|
| **Trigger** | Customer requests garden design, outdoor kitchen planning, or landscape material estimation for residential property |
| **Frequency** | ~1,500–2,500 customer interactions/month across all stores (garden & outdoor is 3% of SKUs, ~1,050 items; growing segment driven by Filipino lifestyle trends) |
| **Volume** | 1 design consultation per customer |
| **Owner** | Garden & Outdoor Department Supervisor |
| **Participants** | Sales Associate (Garden/Outdoor Section), Customer |

### Background

Outdoor living spaces are a growing trend in Philippine residential construction, driven by: (a) the Filipino cultural tradition of outdoor gathering (fiestas, family reunions, barangay events); (b) the tropical climate enabling year-round outdoor living; (c) the growing popularity of outdoor cooking (Filipino cuisine heavily features grilled and smoked dishes — lechon, BBQ, inihaw); (d) social media influence (Instagram-worthy outdoor spaces); (e) post-pandemic preference for outdoor entertaining spaces. BuildRight's garden and outdoor category (3% of SKUs, ~1,050 items) includes plants, pots, hoses, outdoor furniture, and irrigation, and overlaps significantly with building materials (hardscaping — pavers, retaining wall blocks, gravel), plumbing (water lines for irrigation and outdoor sinks), electrical (outdoor lighting, outlet circuits), and appliances (grills, outdoor refrigeration). This workflow provides a combined garden + outdoor kitchen design consultation that creates a comprehensive outdoor living space plan, cross-selling across multiple BuildRight product categories and increasing average project ticket from ~PHP 5,000 (garden-only) to ~PHP 30,000–100,000 (integrated garden + outdoor kitchen).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Outdoor Space Assessment**: Sales Associate gathers outdoor project details: (a) space type: front yard garden, back yard garden/entertaining area, rooftop garden (condo), balcony (condo/apartment), or vacant lot landscaping; (b) available area: length × width (meters); (c) current condition: bare soil, lawn/grass, concrete/paved, mixed; (d) sun exposure: full sun (6+ hours), partial shade (3–6 hours), full shade (<3 hours); (e) primary use: ornamental garden, vegetable/herb garden, outdoor dining/entertaining, outdoor kitchen/cooking area, children's play area, or combination; (f) budget tier: basic (PHP 5,000–15,000), standard (PHP 15,000–50,000), premium (PHP 50,000–200,000+); (g) existing infrastructure: water source available, electrical outlet available, drainage present | Sales Associate | Garden & Outdoor Dept Supervisor | 5–8 min |
| 2 | **Garden Design & Plant Selection**: System generates garden layout: (a) hardscaping areas: patio/deck area (pavers, tiles, or timber decking), pathway (stepping stones or gravel), retaining walls (if sloped terrain, using hollow blocks or interlocking landscape blocks); (b) planting areas: plant bed area (sqm), raised planters (for vegetable/herb gardens), tree locations (shade trees, fruit trees common in PH — mango, calamansi, papaya); (c) plant recommendation per sun exposure and PH climate: full sun — bougainvillea, frangipani, palms, sansevieria; partial shade — ferns, caladiums, aglaonema; full shade — pothos, philodendron, ZZ plant; vegetables — tomatoes, peppers, okra, eggplant (tropical varieties); herbs — basil, mint, lemongrass, rosemary; (d) irrigation: hose-bib connected drip irrigation kit for plant beds, sprinkler for lawn areas, rain barrel for rainwater harvesting per W1078; (e) outdoor furniture: dining set, lounge chairs, hammock, umbrella/pergola for shade | System / Sales Associate | Garden & Outdoor Dept Supervisor | 5–8 min |
| 3 | **Outdoor Kitchen Design** (if applicable): System designs outdoor kitchen: (a) layout: L-shape, straight line, or U-shape based on available area; (b) core components: grill/BBQ station (built-in or freestanding), countertop (tile, granite, or concrete per W1059), base cabinets (concrete block or stainless steel — must be weather-resistant); (c) plumbing: outdoor sink with cold water supply, drainage connection (if near existing drain), or dry well for greywater; (d) electrical: dedicated circuit for outdoor kitchen per W1064 — GFCI-protected outlet for refrigerator, lighting, and small appliances; (e) ventilation: outdoor rated exhaust hood if grill is under roofed structure; (f) storage: weather-resistant cabinets or built-in masonry storage; (g) shelter: pergola, gazebo, or extended roof overhang (roofing materials per W983); (h) lighting: outdoor-rated LED lighting (IP65+) — task lighting over cooking area, ambient lighting over dining area, pathway lighting; (i) system generates outdoor kitchen BOM: appliances, plumbing materials, electrical materials, hardscaping materials, shelter materials | System | Sales Associate | 3–5 min (automated) |
| 4 | **Complete Project Bundle & Estimate**: (a) system aggregates garden + outdoor kitchen materials into single project bundle; (b) bundle includes: hardscaping materials, plants and soil/garden supplies, irrigation system, outdoor kitchen components, plumbing, electrical, shelter/roofing, lighting, furniture; (c) system applies bundle discount per W93; (d) estimate includes: layout sketch with zone designations (garden, dining, cooking, pathway), complete BOM with quantities and prices, total project cost, estimated delivery requirements (soil/gravel delivery per W964, plant delivery, appliance delivery); (e) optional: 3D rendering per W211 for premium projects; (f) referral to licensed electrician (for outdoor electrical) and plumber (for water/drainage) per W904; (g) estimate saved to loyalty account per W17 | Sales Associate | Garden & Outdoor Dept Supervisor | 3–5 min |

### System Touchpoints
- Garden/outdoor space layout recommendation engine
- Plant selection database (PH climate-appropriate species by sun exposure)
- Outdoor kitchen design module (layout + BOM)
- Product master (W252) — plant specifications, outdoor appliance specs, paver dimensions
- Real-time inventory availability per store (W533)
- Bundle pricing engine (W93)
- POS quotation module (W542)
- B2B quotation module (W162) for contractors
- Contractor referral database (W904)
- 3D rendering integration (W211)
- Loyalty account integration (W17)

### Pain Points / Risks
- **Plant guarantee**: Live plants have variable survival rates; disclaimer needed that plant health depends on customer's care, soil conditions, and weather
- **Outdoor electrical safety**: All outdoor electrical work must be GFCI-protected and use IP65+ rated fixtures per PEC per W1064; critical safety requirement
- **Drainage**: Outdoor kitchens require proper drainage; improper drainage causes flooding and mosquito breeding; recommend professional plumbing installation
- **Weather exposure**: All materials must be rated for outdoor exposure; indoor-rated materials will degrade rapidly

### Staffing Implication
- **Sales Associate (Garden/Outdoor)**: Design consultation adds 10–18 minutes per session; at 8–12 consultations per store per week, this represents ~2–4 hours/week; absorbed by existing staff
- **No permanent incremental headcount**

### Time Estimate
- Outdoor space assessment: 5–8 min
- Garden design: 5–8 min
- Outdoor kitchen design: 3–5 min (automated, if applicable)
- Bundle & estimate: 3–5 min
- **Total per consultation**: 16–26 min

---

## W1077. Store-Level Customer Construction Site Portable Toilet & Temporary Facility Rental Coordination

| Field | Detail |
|---|---|
| **Trigger** | Customer (typically contractor or homeowner managing a construction project) requests portable toilet rental or temporary facility setup for construction site |
| **Frequency** | ~1,000–1,500 requests/month across all stores (tied to active construction projects in BuildRight's trade account base of ~5,000 accounts) |
| **Volume** | 1 rental coordination per construction project |
| **Owner** | Pro Desk / Trade Counter Supervisor |
| **Participants** | Sales Associate (Pro Desk), Third-Party Rental Partner, Customer |

### Background

Construction site facilities are a necessary part of any building project in the Philippines. DOLE Department Order No. 13 (DO 13) and the Philippine Occupational Safety and Health Standards require construction sites to provide adequate sanitation facilities for workers, including: (a) portable toilets (minimum 1 per 25 workers per DO 13); (b) handwashing stations; (c) drinking water supply; (d) temporary worker rest/shade areas; (e) first aid station. BuildRight's trade account customers (5,000+ contractors and builders) frequently request portable toilets and temporary facilities for their construction sites. While BuildRight does not own or operate portable toilet units, it serves as a coordination and referral point, connecting customers with vetted third-party rental partners. This service: (a) provides convenience to BuildRight's trade customers (one-stop-shop experience); (b) generates referral income or commission from rental partners; (c) strengthens trade customer loyalty and BuildRight's position as a project partner; (d) supports DOLE compliance per W789 (construction safety management). This workflow is distinct from W139 (tool rental) which covers BuildRight's own rental inventory; this workflow coordinates third-party rental services that BuildRight does not directly operate.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Site Requirement Assessment**: Sales Associate gathers site details: (a) construction site location (address, barangay, city/municipality); (b) project duration: expected construction period (weeks/months); (c) number of workers on site (determines number of portable toilets required: 1 per 25 workers per DO 13); (d) required facilities: portable toilet, handwashing station, temporary office/storage container, generator rental (if no power connection); (e) site access: is the site accessible by delivery truck? narrow street, gated community, high-rise construction?; (f) customer account: trade account number per W58 or new customer setup | Sales Associate | Pro Desk Supervisor | 3–5 min |
| 2 | **Third-Party Rental Partner Matching**: System identifies available rental partners: (a) system queries rental partner database by service area (city/municipality) and facility type; (b) partner selection criteria: service area coverage, unit availability, pricing, service frequency (how often is the unit cleaned/serviced), partner rating (based on previous BuildRight customer feedback); (c) system displays 2–3 partner options with: unit type, monthly rental rate, service frequency included (e.g., weekly cleaning), delivery/setup fee, pickup/removal fee, security deposit; (d) typical Philippine portable toilet rental: PHP 3,000–6,000/month per unit (includes weekly cleaning and chemical treatment); additional charges for delivery (PHP 1,500–3,000) and pickup (PHP 1,000–2,000) | System | Pro Desk Supervisor | 2–3 min (automated) |
| 3 | **Rental Coordination & Customer Handoff**: (a) customer selects preferred rental partner and confirms rental terms; (b) Sales Associate facilitates initial contact: provides customer's contact details and site address to rental partner, or provides rental partner's contact details to customer for direct booking; (c) BuildRight's role is limited to coordination/referral — the rental contract is directly between the customer and the rental partner; (d) system records referral in customer's project file per W162 (for trade accounts) for tracking and follow-up; (e) Sales Associate provides complementary construction site supplies reminder: PPE (hard hats, gloves, safety vests) per W1067 (fire suppression), W1068 (earthquake-resistant materials), W1069 (flood-resistant materials), DOLE DO 13 compliance requirements per W789; (f) for trade account customers, system generates site facility compliance checklist for DOLE inspection readiness per W505 | Sales Associate | Pro Desk Supervisor | 3–5 min |
| 4 | **Partner Performance Tracking & Follow-Up**: (a) system sends follow-up survey to customer 1 week after rental delivery: Was delivery on time? Is the unit in good condition? Is the partner responsive?; (b) customer feedback recorded in partner rating system; (c) quarterly partner performance review: on-time delivery rate, customer satisfaction score, issue resolution time; (d) underperforming partners removed from referral list; (e) BuildRight does NOT charge the customer for this coordination service — value is in customer loyalty and trade account stickiness | System | Pro Desk Supervisor | Automated follow-up; Quarterly review: 2–3 hrs |

### System Touchpoints
- Rental partner database (service area, pricing, availability, ratings)
- Customer project file integration (W162)
- Trade account management system (W58)
- DOLE compliance checklist generator (W789/W505)
- Customer feedback and survey system
- Partner performance tracking module

### Pain Points / Risks
- **Third-party liability**: BuildRight is not liable for the quality, timeliness, or condition of third-party rental services; coordination agreement must clearly state BuildRight's role as referral only
- **Partner availability**: During peak construction season (dry season, January–May), portable toilet rental demand may exceed partner supply; system should show real-time availability
- **Service quality**: Poor partner service (late delivery, dirty units, unresponsive customer service) reflects badly on BuildRight by association; rigorous partner vetting and performance tracking essential
- **DOLE compliance**: Customers may not be aware of DO 13 sanitation requirements; pro desk staff should proactively inform customers of requirements when discussing construction project materials

### Staffing Implication
- **Sales Associate (Pro Desk)**: Rental coordination adds 3–5 minutes per request; at 5–8 requests per store per week, this represents ~30 min–1 hour/week; absorbed by existing Pro Desk staff
- **No permanent incremental headcount**

### Time Estimate
- Site assessment: 3–5 min
- Partner matching: 2–3 min (automated)
- Coordination & handoff: 3–5 min
- **Total per coordination**: 8–13 min

---

## W1078. Customer Rainwater Collection & Storage System Complete Package Design

| Field | Detail |
|---|---|
| **Trigger** | Customer requests rainwater harvesting system for residential or small commercial property (distinct from W1048 which covers design consultation only; this workflow covers complete system design, material package, and installation coordination) |
| **Frequency** | ~800–1,200 customer interactions/month across all stores (growing interest driven by water scarcity in some PH regions and sustainability awareness per W192) |
| **Volume** | 1 system design per customer |
| **Owner** | Plumbing Department Supervisor |
| **Participants** | Sales Associate (Plumbing Section), Customer |

### Background

Rainwater harvesting is increasingly relevant in the Philippines for several reasons: (a) many Philippine municipalities experience water supply interruptions (Manila Water/Maynilad rationing in Metro Manila, provincial water district shortages during dry season); (b) some rural BuildRight store areas rely on deep wells with unreliable supply; (c) Philippine rainfall is abundant (average 2,000–4,000mm/year, among the highest in the world) making rainwater harvesting highly productive; (d) LGU building codes in some cities (e.g., Davao City) are beginning to mandate rainwater harvesting for new construction; (e) sustainability and water conservation awareness is growing per W692 (water consumption tracking). A rainwater harvesting system captures rainwater from the roof, channels it through gutters and downspouts, filters debris, stores it in tanks, and distributes it for non-potable uses (gardening, toilet flushing, laundry, car washing) or, with additional treatment, for potable use. BuildRight carries all necessary components: gutters and downspouts per W1052, PVC pipes and fittings, water storage tanks (polyethylene, fiberglass, or concrete), water pumps, filters, and treatment systems. This workflow designs a complete rainwater harvesting system package tailored to the customer's roof area, rainfall pattern, water demand, and budget.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Roof & Water Demand Assessment**: Sales Associate gathers system requirements: (a) roof type: GI sheeting (most common), tile, concrete flat roof; (b) roof footprint area (length × width in meters) — this determines collection potential; (c) average annual rainfall for location (system pulls from PAGASA rainfall data by municipality: e.g., Metro Manila ~2,000mm/year, Davao ~2,000mm/year, eastern Visayas ~3,500mm/year); (d) intended water use: non-potable only (gardening, toilet flushing, laundry, car washing) or potable (requires additional treatment); (e) daily water demand for intended use (typical Filipino household: 150–200 liters per capita per day; toilet flushing = ~30% of total, laundry = ~20%, gardening = variable); (f) available tank location: above-ground (beside house, under eave), below-ground (buried tank), rooftop (for small systems); (g) existing gutter system: present (may need modification) or none (full gutter installation per W1052); (h) budget tier: basic (PHP 5,000–15,000 — single barrel/drum), standard (PHP 15,000–50,000 — 1,000–3,000L tank + pump), premium (PHP 50,000–150,000 — underground tank + pump + filtration + treatment) | Sales Associate | Plumbing Dept Supervisor | 5–8 min |
| 2 | **System Sizing & Collection Potential Calculation**: System computes system specifications: (a) annual rainwater collection potential = roof area (sqm) × annual rainfall (mm) × 0.85 (runoff coefficient for GI roofing — 85% of rainfall is captured, 15% lost to evaporation and splash); example: 100 sqm roof × 2,000mm rainfall × 0.85 = 170,000 liters/year = 466 liters/day average; (b) tank sizing: based on longest dry period (Philippine dry season: February–May, ~120 days); tank size = daily demand × dry season days × safety factor (0.7 — assuming some rain during dry season); example: 200 liters/day demand × 120 days × 0.7 = 16,800 liters = 3,000–5,000 gallon tank; practical tank sizes available in PH: 200L drum, 500L, 1,000L, 2,000L, 5,000L, 10,000L (polyethylene); (c) gutter sizing per W1052: computed based on roof area and maximum rainfall intensity (Philippine rainfall can reach 100mm/hour during typhoons); (d) pump sizing: based on tank-to-point-of-use distance and elevation head per W984 | System | Plumbing Dept Supervisor | 3–5 min (automated) |
| 3 | **Complete System Package Design**: System generates full system BOM: (a) **Collection**: gutters (continuous length per roof perimeter per W1052), downspouts (minimum 2 for gable roof), leaf guard/gutter screen (prevent debris entry), first-flush diverter (diverts first 10–20 liters of rainwater containing roof contaminants); (b) **Filtration**: coarse filter at gutter entry (mesh screen), fine filter before tank entry (200 micron cartridge filter), tank inlet filter basket; (c) **Storage**: polyethylene water tank (selected size, UV-stabilized, food-grade for potable systems), tank stand/platform (elevated 0.3–1.0m for gravity feed), tank cover (tight-fitting to prevent mosquito breeding — dengue prevention), overflow pipe (direct excess water to storm drain or garden), tank level indicator (sight glass or ultrasonic sensor); (d) **Distribution**: water pump (centrifugal, 0.5–1.5 HP based on demand and head), pressure tank (20–40L for on-demand pressure), PVC supply pipe (3/4" or 1") from tank to pump to point-of-use, gate valves for isolation, non-return valve to prevent backflow; (e) **Treatment** (if potable): UV sterilizer (40W for 1,000L/hr flow), sediment filter (5 micron), carbon filter (taste and odor), optional: chlorination dosing system; (f) **Electrical**: dedicated pump circuit per W1064, waterproof outdoor outlet at pump location, pump controller with dry-run protection; (g) system generates complete package cost | System | Sales Associate | 3–5 min (automated) |
| 4 | **Estimate, Installation Coordination & Customer Handoff**: (a) system generates estimate: system sizing summary, collection potential, tank capacity rationale, complete BOM organized by subsystem (collection, filtration, storage, distribution, treatment, electrical), total system cost, estimated annual water savings (liters) and PHP savings (at Manila Water rate of PHP 35–50/cu.m.); (b) ROI calculation: system cost ÷ annual PHP savings = payback period (typically 2–5 years for standard systems); (c) installation advisory: "Rainwater harvesting system installation involves plumbing and electrical work. BuildRight recommends professional installation by a licensed plumber per W904. Non-potable systems can be DIY-installed by experienced homeowners."; (d) maintenance advisory: clean gutters quarterly, check and clean filters monthly, inspect tank annually for sediment buildup, check pump operation quarterly, replace UV lamp annually (if potable system); (e) for B2B/trade customers, convert to project quote per W162; (f) estimate saved to loyalty account per W17 | Sales Associate | Plumbing Dept Supervisor | 3–5 min |

### System Touchpoints
- Rainwater collection potential calculator (roof area × PAGASA rainfall data)
- Tank sizing engine (demand-based with dry season buffer)
- Pump sizing calculator (flow rate × head)
- PAGASA rainfall database by municipality
- Product master (W252) — tank specifications, pump curves, filter specifications
- Gutter calculator integration (W1052)
- Electrical circuit integration (W1064)
- Real-time inventory availability per store (W533)
- POS quotation module (W542)
- B2B quotation module (W162)
- Contractor referral database (W904)
- Loyalty account integration (W17)
- ESG water tracking integration (W693)

### Pain Points / Risks
- **Water quality liability**: If customer uses system for potable water, water quality depends on maintenance; disclaimer must state that BuildRight does not guarantee water quality and customer is responsible for regular testing
- **Mosquito breeding**: Standing water in tanks or gutters is a dengue mosquito breeding risk; system must specify tight-fitting tank covers and gutter maintenance per DOH advisory
- **Structural load**: Large water tanks (5,000L+) weigh 5+ tons when full; structural assessment of tank support/stand required; recommend structural engineer referral for tanks above 2,000L
- **Dry season reality**: Rainwater harvesting is least productive during the dry season when water is needed most; system must manage customer expectations about seasonal variability

### Staffing Implication
- **Sales Associate (Plumbing Section)**: Rainwater system design adds 10–15 minutes per consultation; at 4–6 consultations per store per week, this represents ~1–2 hours/week; absorbed by existing staff
- **No permanent incremental headcount**

### Time Estimate
- Roof & demand assessment: 5–8 min
- System sizing: 3–5 min (automated)
- Package design: 3–5 min (automated)
- Estimate & handoff: 3–5 min
- **Total per consultation**: 14–23 min

---

## W1079. Customer Swimming Pool Construction Material Estimation Service

| Field | Detail |
|---|---|
| **Trigger** | Customer requests material estimation for residential swimming pool construction (concrete/gunite pool) |
| **Frequency** | ~400–800 customer interactions/month across all stores (higher in Metro Manila, Cebu, and Davao where residential pools are more common) |
| **Volume** | 1 pool system estimate per customer |
| **Owner** | Building Materials Department Supervisor |
| **Participants** | Sales Associate (Building Materials Section), Sales Associate (Plumbing Section), Customer |

### Background

Residential swimming pool construction is a growing segment in the Philippine home improvement market, driven by: (a) increasing middle-class and upper-middle-class homeownership; (b) the tropical climate making pools usable year-round; (c) resort-style living trends in new subdivisions and condominium developments; (d) hotel/resort construction in tourism areas (Palawan, Boracay, Cebu, Bohol, Siargao). The most common pool type in the Philippines is the concrete/gunite (shotcrete) pool, which involves: (a) excavation; (b) steel reinforcement (rebar cage); (c) shotcrete/gunite application (concrete sprayed onto rebar cage); (d) waterproofing; (e) tiling or plaster finish; (f) plumbing (circulation, filtration, drainage); (g) electrical (pump, lighting, heater); (h) coping and deck construction. BuildRight carries all necessary construction materials: rebar, cement, sand, gravel, waterproofing products, tiles, PVC pipes and fittings, pool pumps, filters, and pool chemicals. A typical Filipino residential pool (3m × 6m × 1.5m average depth = 27,000 liters) requires approximately PHP 200,000–500,000 in construction materials (excluding labor and professional fees). This workflow provides material quantity estimation for pool construction, linking to W1044 (concrete calculator), W989 (plumbing layout), W1064 (electrical), and W1063 (tile quantity). It does NOT cover pool design (which requires a licensed engineer) or pool maintenance.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pool Specification & Dimension Input**: Sales Associate gathers pool specifications: (a) pool type: in-ground concrete/gunite (most common PH type), in-ground vinyl liner (less common), above-ground (budget option); (b) pool shape: rectangular, kidney/organic, freeform, lap pool, plunge pool; (c) pool dimensions: length × width × average depth (meters); (d) total water volume computation: length × width × average depth × shape factor (1.0 for rectangular, 0.85 for kidney/organic); (e) deck/patio area: width of deck around pool (typical 1.5–3.0m perimeter) and deck material (tile, stamped concrete, natural stone); (f) additional features: infinity edge (yes/no), jacuzzi/spa section (yes/no), pool lighting (underwater LED), heating (electric heat pump or solar), water features (waterfall, fountain); (g) site condition: flat terrain or sloped (sloped requires retaining wall) | Sales Associate | Building Materials Dept Supervisor | 5–8 min |
| 2 | **Structural & Waterproofing Material Estimation**: System computes structural materials: (a) excavation volume: pool interior volume + 0.3m clearance on all sides and bottom (for rebar cage and gunite thickness); (b) rebar cage: vertical bars at 200mm spacing × horizontal bars at 200mm spacing on all walls and floor; rebar diameter: 10mm for floor, 12mm for walls; total rebar weight computed per W1060 (rebar estimator); (c) shotcrete/gunite: pool surface area (floor + all walls) × 200mm thickness = concrete volume; mix design: Class A per W1044; (d) structural concrete for deck: deck area × 100mm thickness per W1044; (e) waterproofing: cementitious crystalline waterproofing applied to all pool interior surfaces (2 coats); quantity based on pool interior surface area × coverage rate (1.5 kg/sqm/coat); (f) coping: natural stone or precast concrete coping stones around pool perimeter (linear meters × unit length per piece); (g) deck finish: tile or stamped concrete — quantity per W963 | System | Sales Associate | 3–5 min (automated) |
| 3 | **Plumbing, Filtration & Electrical Material Estimation**: System computes mechanical systems: (a) **Circulation plumbing**: main drain at pool floor (2 units for 3×6m pool), skimmer at water line (1–2 units), return jets (4–6 units), PVC pipes: suction line (2" from drain/skimmer to pump), return line (1.5" from filter to return jets), all PVC Schedule 40; pipe length estimated from pool-to-equipment-room distance; (b) **Filtration system**: pool pump sized per turnover rate (entire pool volume filtered in 6–8 hours): flow rate = pool volume ÷ turnover time ÷ 60; typical residential: 0.75–1.5 HP pump; sand filter or cartridge filter sized to match pump flow rate; (c) **Pool lighting**: underwater LED lights (1 per 10 sqm of pool surface), niche housing, waterproof conduit, transformer (12V AC per PEC); (d) **Electrical**: dedicated circuit for pump per W1064 (typically 20A/30A), GFCI protection mandatory per PEC, timer for pump automation, optional: heat pump circuit (40A), smart control per W1071; (e) **Pool chemicals starter kit**: chlorine (granular or tablets), pH adjuster (sodium bisulfate for lowering, sodium carbonate for raising), algaecide, test kit, pool brush, leaf net, vacuum head and hose | System | Sales Associate | 2–3 min (automated) |
| 4 | **Complete Pool Package & Estimate**: (a) system generates complete pool construction BOM: structural (rebar, concrete, waterproofing), finishes (tile, coping, deck), plumbing (pipes, fittings, valves, drains), filtration (pump, filter, accessories), electrical (circuit, lighting, controls), chemicals and maintenance kit; (b) estimate includes: pool specification summary, water volume, structural material quantities, mechanical system specifications, complete BOM with quantities and prices, total material cost (excluding labor and professional fees); (c) advisory: "Swimming pool construction requires professional design by a licensed civil engineer (structural) and professional mechanical engineer (hydraulics). This material estimate is for budgeting purposes only. BuildRight recommends engaging a qualified pool contractor per W904."; (d) estimated budget range: materials (from estimate) + labor (typically 50–80% of material cost in PH) + professional fees (10–15% of total construction cost) = total project cost estimate; (e) for B2B/trade customers (hotel/resort projects), convert to project quote per W162; (f) estimate saved to loyalty account per W17 | Sales Associate | Building Materials Dept Supervisor | 3–5 min |

### System Touchpoints
- Pool volume calculator (dimensions × shape factor)
- Structural material estimator (rebar weight, concrete volume, waterproofing quantity)
- Plumbing and filtration system sizer (pump HP, filter size, pipe diameters)
- Product master (W252) — rebar grades, pool equipment specifications, tile specifications
- Real-time inventory availability per store (W533)
- POS quotation module (W542)
- B2B quotation module (W162)
- Contractor referral database (W904) — pool contractors
- Loyalty account integration (W17)

### Pain Points / Risks
- **Structural liability**: Pool construction involves significant structural engineering (water pressure on walls, soil pressure, waterproofing integrity); all estimates must include engineering disclaimer
- **Waterproofing failure**: The most common pool construction failure in the Philippines is water leakage through the shell due to inadequate waterproofing; this is costly to repair; system must prominently recommend professional waterproofing application
- **Equipment compatibility**: Pool pump, filter, and pipe sizing must be matched for proper hydraulic performance; system must validate compatibility
- **Chemical safety**: Pool chemicals (chlorine, acid) are hazardous per W236; storage and handling advisory required

### Staffing Implication
- **Sales Associate (Building Materials/Plumbing)**: Pool estimation adds 10–15 minutes per consultation; at 2–4 consultations per store per week, this represents ~30 min–1 hour/week; absorbed by existing staff
- **No permanent incremental headcount**

### Time Estimate
- Pool specification: 5–8 min
- Structural & waterproofing: 3–5 min (automated)
- Plumbing & electrical: 2–3 min (automated)
- Estimate & handoff: 3–5 min
- **Total per consultation**: 13–21 min

---

## W1080. Store-Level Customer Construction Scaffold & Ladder Safety Consultation

| Field | Detail |
|---|---|
| **Trigger** | Customer purchases or rents scaffolding, ladders, or working-at-height equipment for construction project |
| **Frequency** | ~2,000–3,000 customer interactions/month across all stores (scaffolding and ladder safety is critical for construction safety per DOLE DO 13) |
| **Volume** | 1 consultation per customer visit |
| **Owner** | Safety & PPE Department Supervisor |
| **Participants** | Sales Associate (Safety/PPE Section), Customer |

### Background

Falls from height are the #1 cause of construction fatalities in the Philippines, accounting for ~35% of all construction-related deaths per DOLE statistics. DOLE Department Order No. 13 (DO 13), also known as the "Guidelines Governing Occupational Safety and Health in the Construction Industry," mandates specific safety requirements for working at height, including: (a) scaffolding must be erected by competent persons and inspected before use; (b) ladders must be secured at top and bottom, extend 1m above the landing platform, and be angled at 4:1 ratio (1m out for every 4m up); (c) safety harnesses must be worn when working above 1.8m (6 feet) from ground level; (d) hard hats must be worn at all times on construction sites; (e) safety nets must be installed for work above 6m. BuildRight Depot sells and rents (per W139) scaffolding systems, ladders, safety harnesses, hard hats, and related fall protection equipment. This workflow provides a mandatory safety consultation at the point of sale/rental for scaffolding and ladder products, ensuring the customer understands safe setup, usage, and required PPE. It is distinct from W1062 (scaffolding rental service) which covers the rental transaction; this workflow covers the safety consultation that accompanies every scaffolding/ladder sale or rental.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Work-at-Height Assessment**: Sales Associate assesses the work-at-height requirement: (a) task: painting, ceiling installation, roof work, masonry/CHB laying, electrical/plumbing overhead work, general construction; (b) working height: 1.8–3m (ladder or step ladder range), 3–6m (scaffold required), 6m+ (full scaffold system with safety nets); (c) duration: brief task (< 1 hour) or extended work (hours/days); (d) number of workers at height simultaneously; (e) surface condition: flat stable ground, uneven ground, sloped ground, staircase, or over water; (f) load requirements: worker weight + tools + materials (scaffolding must be rated for intended load per manufacturer specification) | Sales Associate | Safety & PPE Dept Supervisor | 3–5 min |
| 2 | **Equipment Selection & Safety Setup Guidance**: System recommends appropriate equipment: (a) **1.8–3m tasks**: step ladder (fiberglass for electrical work, aluminum for general use) — height selected so worker can reach work area without standing on top 2 rungs; extension ladder for access to roofs/upper floors — length computed from working height × 1.136 (4:1 angle factor) + 1m extension above landing; (b) **3–6m tasks**: mobile scaffold tower (modular steel or aluminum frame) with casters, platform boards, toe boards, guardrails, and access ladder; base dimensions selected for stability (minimum 1.2m × 0.6m base); (c) **6m+ tasks**: full ringlock/cuplock scaffold system — modular scaffold erected by trained scaffold erector; system computes number of bays, lift heights, and platform levels based on building dimensions; recommend professional scaffold erection per W904; (d) **Setup guidance**: scaffold must be on level, load-bearing ground; use base plates and screw jacks for leveling; install outriggers or tie to structure at every 4m of height; never use bricks/blocks to level scaffold; lock caster wheels before climbing; do not move scaffold with personnel on it | System / Sales Associate | Safety & PPE Dept Supervisor | 3–5 min |
| 3 | **Required PPE Recommendation**: System generates mandatory PPE list: (a) safety harness (full-body, with dorsal D-ring) — mandatory for all work above 1.8m per DO 13; select harness rated for user weight; (b) shock-absorbing lanyard (1.5–2.0m length) — connects harness D-ring to secure anchor point (scaffold, structural beam); never tie off to a guardrail; (c) hard hat (Type I, Class E for electrical protection) — mandatory on all construction sites per DO 13; (d) safety shoes (steel toe, slip-resistant sole) — mandatory for construction sites; (e) safety goggles — for overhead work where debris may fall; (f) high-visibility vest — for outdoor construction near traffic; (g) system verifies PPE compatibility with scaffold/ladder selection | System | Sales Associate | 1–2 min (automated) |
| 4 | **Safety Briefing & DOLE Compliance Documentation**: (a) Sales Associate conducts verbal safety briefing covering: "Never stand on the top two rungs of a ladder. Always maintain 3 points of contact (two hands + one foot, or two feet + one hand). Face the ladder when climbing up or down. Secure the ladder at top and bottom. Do not exceed the ladder's duty rating. Inspect all equipment before each use. Do not use damaged or bent scaffold components. Wear your safety harness at all times when above 1.8m."; (b) system prints one-page safety briefing summary with diagrams (proper ladder angle, scaffold setup, harness donning) for customer to post at job site; (c) for rental transactions per W1062: customer signs safety acknowledgment form confirming receipt of safety briefing; (d) DOLE DO 13 compliance note: "Philippine construction safety regulations require all employers and contractors to provide fall protection training to workers and maintain records of safety equipment inspection per DOLE DO 13. BuildRight recommends all construction employers engage a DOLE-accredited OSH practitioner for construction safety management."; (e) system records safety briefing delivery in customer's transaction history for liability documentation | Sales Associate | Safety & PPE Dept Supervisor | 3–5 min |

### System Touchpoints
- Work-at-height equipment recommendation engine (height → equipment type)
- Scaffold/ladder sizing calculator
- Product master (W252) — scaffold specifications, ladder duty ratings, harness specifications
- Real-time inventory availability per store (W533)
- POS transaction module (W5) with safety acknowledgment capture
- Rental management module (W139) integration
- DOLE compliance documentation generator (W789)
- Contractor referral database (W904) — professional scaffold erectors

### Pain Points / Risks
- **Safety liability**: Falls from height are life-threatening; safety briefing must be delivered every time, documented, and acknowledged by customer; even with briefing, BuildRight cannot control how equipment is used on site
- **Equipment misuse**: Filipino construction workers frequently misuse ladders and scaffolding (standing on top rung, overloading platforms, using damaged components); safety briefing must address common misuse scenarios
- **Substandard equipment**: The Philippine market has substandard ladders and scaffolding that do not meet load ratings; BuildRight must ensure all products sold meet ANSI/EN standards per W110 (supplier quality)
- **DOLE inspection**: Construction sites are subject to unannounced DOLE inspections per W505; proper equipment and PPE documentation is essential

### Staffing Implication
- **Sales Associate (Safety/PPE Section)**: Safety consultation adds 5–8 minutes per sale/rental transaction; at 10–15 transactions per store per week, this represents ~1–2 hours/week; absorbed by existing staff
- **No permanent incremental headcount**; safety consultation is a non-negotiable part of every scaffolding/ladder transaction

### Time Estimate
- Work-at-height assessment: 3–5 min
- Equipment selection: 3–5 min
- PPE recommendation: 1–2 min (automated)
- Safety briefing: 3–5 min
- **Total per consultation**: 10–17 min

---

## W1081. Customer Construction Project Insurance Coverage Advisory Service

| Field | Detail |
|---|---|
| **Trigger** | Customer (homeowner or contractor) inquires about construction insurance requirements or requests guidance on insurance coverage for an active or planned construction project |
| **Frequency** | ~600–1,000 customer interactions/month across all stores (higher during peak construction season January–May) |
| **Volume** | 1 advisory session per customer |
| **Owner** | Pro Desk / Trade Counter Supervisor |
| **Participants** | Sales Associate (Pro Desk), Customer |

### Background

Construction project insurance is a critical but frequently overlooked aspect of Philippine construction projects. The Philippine construction industry faces multiple insurable risks: (a) property damage from typhoons (20+ typhoons/year), earthquakes (PH sits on Pacific Ring of Fire), floods, and fires; (b) third-party liability for damage to neighboring properties (common in dense urban construction — collapse of excavation into adjacent property, falling debris); (c) worker injury and death (construction has the highest workplace fatality rate in PH); (d) equipment theft and damage; (e) contractor default or abandonment. The key insurance products relevant to Philippine construction are: (a) Contractor's All Risk (CAR) / Erection All Risk (EAR) insurance — covers physical loss or damage to construction works, third-party liability, and sometimes worker injury; typically required by banks for construction loans; (b) Builder's Risk insurance — similar to CAR but focused on property damage during construction; (c) Workmen's Compensation / EC coverage through SSS — mandatory per Philippine law for all employees; (d) DOLE-required construction safety insurance per DO 13; (e) Professional liability insurance for architects and engineers (not carried by BuildRight but relevant to the project ecosystem). BuildRight does not sell insurance but serves as an advisory and referral point, connecting customers with insurance partners. This service: (a) protects BuildRight's reputation by promoting safe construction practices; (b) generates referral income from insurance partners; (c) reduces risk of customer project failures (which could reduce future material purchases). It is distinct from W857–W864 (BuildRight's own insurance workflows) which cover BuildRight's internal insurance needs; this workflow covers customer-facing construction insurance advisory.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Project Insurance Needs Assessment**: Sales Associate assesses insurance needs: (a) project type: residential construction (new build, renovation), commercial construction, government project; (b) estimated construction cost (total project value including materials and labor); (c) project duration: expected construction timeline (months); (d) project financing: bank-financed (insurance typically required by lender), self-financed (insurance optional but recommended), government-funded (insurance requirements per GPPB guidelines); (e) location risk factors: flood-prone per W1069, earthquake zone per W1068, typhoon corridor, fire-prone urban area; (f) number of workers on site (affects worker compensation requirements); (g) adjacent properties: is the construction site adjacent to other buildings? (increases third-party liability risk — excavation damage, falling debris, noise complaints); (h) current insurance coverage: does customer already have construction insurance? if yes, review adequacy | Sales Associate | Pro Desk Supervisor | 3–5 min |
| 2 | **Insurance Coverage Recommendation**: System recommends insurance coverage based on project risk profile: (a) **CAR/EAR Insurance** (recommended for all projects >PHP 1M): covers all risks of physical loss or damage to the construction works during the construction period, including typhoon, earthquake, flood, fire, theft, and vandalism; third-party liability coverage (damage to neighboring properties, injury to bystanders); typical premium: 0.3–0.8% of construction cost; minimum coverage: 100% of estimated construction cost; (b) **Builder's Risk** (alternative to CAR for smaller projects): covers named perils (typhoon, fire, earthquake — check if earthquake is included or requires separate endorsement); (c) **Worker's Compensation**: mandatory per Philippine law — SSS EC coverage for all employees; for construction workers hired as daily-wage, contractor is responsible for SSS coverage; recommend customer verify contractor's SSS compliance per W251; (d) **Professional Indemnity**: recommend customer verify that their architect and engineer carry professional liability insurance; (e) system computes recommended coverage levels and estimated premium ranges based on construction cost and location risk factors | System | Pro Desk Supervisor | 2–3 min (automated) |
| 3 | **Insurance Partner Referral & Documentation**: (a) system displays BuildRight's insurance partner options: 2–3 insurance companies/brokers with construction insurance products (standard Philippine insurers: Malayan Insurance, Pioneer, MAPFRE Insular, BPI/MS, FPG Insurance); (b) for each partner: company name, contact person, phone number, email, products offered, special rates for BuildRight customers (if negotiated); (c) system generates insurance needs summary document for customer to provide to insurance company/broker: project description, construction cost, project duration, location, number of workers, risk factors, recommended coverage; (d) BuildRight's role is advisory and referral only — the insurance contract is directly between the customer and the insurance company; BuildRight is not an insurance agent and does not receive commissions from insurance sales (or if referral agreement exists, this is disclosed transparently); (e) for trade account B2B customers, system saves insurance advisory record in project file per W162 for future reference | Sales Associate | Pro Desk Supervisor | 3–5 min |

### System Touchpoints
- Construction insurance needs assessment engine (project type × cost × location risk)
- Insurance coverage recommendation calculator
- Insurance partner referral database
- Project file integration (W162)
- Trade account management system (W58)
- Seismic zone classification (W1068)
- Flood risk classification (W1069)

### Pain Points / Risks
- **Insurance advisory vs. sales**: BuildRight must clearly position this as advisory only; staff must not recommend specific insurance products or provide coverage advice that could be construed as insurance brokerage
- **Underinsurance risk**: Many Filipino homeowners underinsure or skip construction insurance entirely due to cost sensitivity; advisory should clearly present the risk of no insurance (total loss scenario)
- **Claims complexity**: Philippine insurance claims processes can be slow and contentious; customer expectations must be managed
- **Partner quality**: Insurance partner quality varies; recommend only reputable insurers with strong claims-paying ability and track record

### Staffing Implication
- **Sales Associate (Pro Desk)**: Insurance advisory adds 5–8 minutes per session; at 3–5 requests per store per week, this represents ~20–40 min/week; absorbed by existing Pro Desk staff
- **No permanent incremental headcount**

### Time Estimate
- Needs assessment: 3–5 min
- Coverage recommendation: 2–3 min (automated)
- Partner referral & documentation: 3–5 min
- **Total per consultation**: 8–13 min

---

## W1082. Store-Level Customer Construction Material Quality Verification & Grade Certification Assistance

| Field | Detail |
|---|---|
| **Trigger** | Customer requests material quality verification, grade certification, mill test certificate, or product compliance documentation for construction materials purchased at BuildRight (or being specified for a project) |
| **Frequency** | ~1,500–2,500 requests/month across all stores (driven by government project audit requirements, bank loan collateral verification, and quality-conscious B2B customers) |
| **Volume** | 1 request per material type per project |
| **Owner** | Building Materials Department Supervisor |
| **Participants** | Sales Associate (Building Materials Section), Receiving Clerk (for stock verification), Customer |

### Background

Material quality verification is critical in Philippine construction due to the prevalence of substandard construction materials in the market. The Philippine Department of Trade and Industry (DTI) and the Department of Public Works and Highways (DPWH) have identified recurring issues with: (a) substandard rebar (undersized diameter, below-grade yield strength, uncertified origin); (b) substandard cement (adulterated with ash or limestone powder, expired product); (c) substandard GI sheets (below-specified zinc coating thickness, thinner than labeled gauge); (d) substandard electrical wire (copper content below specification, undersized conductor cross-section); (e) substandard plumbing fittings (brittle PVC, undersized wall thickness). Philippine construction standards that apply: PNS 48 (steel bars for concrete reinforcement), PNS 63 (Portland cement), PNS 67 (GI steel sheets), PNS 35 (PVC pipes), PNS 90 (electrical wires and cables). For government projects, DPWH requires mill test certificates and product testing from accredited laboratories for all critical structural materials. For bank-financed projects, lenders may require material quality documentation before releasing construction loan tranches. For private B2B projects, quality-conscious contractors require traceability and certification to ensure the materials they install meet engineering specifications. BuildRight Depot, as a reputable retailer, must be able to provide quality documentation for the materials it sells. This workflow governs how BuildRight handles customer requests for material quality verification and certification documentation.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Quality Documentation Request Intake**: Sales Associate identifies the request type: (a) product certification request: customer needs mill test certificate (MTC), certificate of conformance (CoC), or product test report for specific materials purchased or being considered for purchase; (b) product inspection request: customer wants to visually inspect and verify product specifications (e.g., rebar diameter measurement, GI sheet thickness gauge) before purchase; (c) batch/lot traceability: customer needs to trace specific material batch to manufacturer and production date; (d) product testing referral: customer needs independent third-party laboratory testing of materials for a specific project requirement; (e) material type: steel/rebar, cement, GI sheets, electrical wire, PVC pipes, timber/lumber, paint, roofing, other; (f) customer type: trade/B2B contractor, government project, bank-financed project, retail homeowner; (g) project requirement: is this for DPWH compliance, bank loan requirement, LGU building permit, or customer's own quality assurance? | Sales Associate | Building Materials Dept Supervisor | 3–5 min |
| 2 | **Product Certification Retrieval**: System retrieves available certification: (a) system queries product master (W252) for material specifications and available certifications; (b) for steel/rebar: retrieve mill test certificate (MTC) from supplier — includes heat number, chemical composition (carbon, manganese, phosphorus, sulfur), mechanical properties (yield strength, tensile strength, elongation), and PNS 48 compliance statement; MTCs are stored in ERP per supplier per heat number per delivery lot; (c) for cement: retrieve certificate of conformance from manufacturer — includes product type (Type I, Type IP, Type V per PNS 63), compressive strength test results (7-day and 28-day), and manufacturing date (for shelf life verification); (d) for GI sheets: retrieve mill certificate — includes zinc coating weight (AZ70, AZ150 per PNS 67), base metal thickness (gauge), and coil/lot number; (e) for electrical wire: retrieve product test report — includes conductor cross-section (mm²), insulation thickness, voltage rating, and PNS 90 compliance; (f) for PVC pipes: retrieve certificate — includes pipe class (Schedule 40, Sch 80 per PNS 35), wall thickness, pressure rating, and lot number; (g) system retrieves stored certificates from document management system per W255; if certificate not available for specific lot, system flags for supplier request | System | Sales Associate | 2–3 min (automated) |
| 3 | **In-Store Product Verification** (if applicable): For customers requesting physical verification: (a) rebar: Sales Associate and customer verify rebar diameter using caliper (10mm rebar must measure 10.0mm ± 0.3mm per PNS 48), check for mill marking/brand stamp, check surface condition (no rust, no cracks, no bends); (b) GI sheets: verify gauge thickness using sheet metal gauge tool, verify zinc coating visually (no bare spots), check corrugation profile matches specification; (c) cement: check bag integrity (no tears, no moisture damage), check manufacturing date (cement older than 3 months should not be sold per PNS 63), check PNS mark and DTI certification mark on bag; (d) electrical wire: verify conductor diameter (strip insulation and measure), verify insulation quality (no nicks, no discoloration), check PNS mark on insulation printing; (e) timber: verify species and grade marking per W976, check moisture content (if moisture meter available), check for defects (knots, splits, warping) | Sales Associate / Receiving Clerk | Building Materials Dept Supervisor | 5–10 min |
| 4 | **Documentation Package & Testing Referral**: (a) system generates quality documentation package: product specifications, available certificates (MTC, CoC, test reports), delivery traceability (supplier → DC → store), BuildRight's supplier quality assurance statement; (b) for government/DPWH projects: documentation package formatted per DPWH requirements for material submission; (c) for projects requiring independent testing: referral to accredited testing laboratories in the Philippines (e.g., DOST-ITDI, UP ICE Structural Engineering Lab, private labs: SGS Philippines, TÜV SÜD Philippines, Intertek) with contact information and typical testing fees (concrete cylinder test: PHP 500–1,500 per set; rebar tensile test: PHP 1,000–2,500 per sample; cement test: PHP 3,000–5,000 per sample); (d) system notes: "BuildRight Depot sources materials from DTI-certified and PNS-compliant manufacturers per supplier quality management program W110. All incoming materials undergo receiving inspection per W681. BuildRight does not perform independent laboratory testing of materials; customers requiring project-specific testing should engage an accredited third-party laboratory."; (e) documentation saved to customer's project file per W162 (trade accounts) or printed for walk-in customers | Sales Associate | Building Materials Dept Supervisor | 3–5 min |

### System Touchpoints
- Product master (W252) — material specifications, PNS standards compliance
- Certificate/document management system (W255) — stored MTCs, CoCs, test reports
- Supplier quality management system (W110)
- Receiving inspection module (W681) — incoming quality records
- Product lot/traceability module (batch tracking from supplier to store)
- Material review board integration (W819) — for quality rejection cases
- POS transaction module (W5) — linking certificates to specific sales transactions
- Trade account project file (W162)

### Pain Points / Risks
- **Certificate availability**: Not all products have MTCs readily available; some certificates must be requested from suppliers (lead time: 1–5 business days); system must manage customer expectations on turnaround time
- **Substandard product risk**: If BuildRight inadvertently stocks substandard materials, customer quality verification could expose the issue; this is actually a positive outcome (prevents use of substandard materials) but requires rapid escalation per W819 (material review board) and W110 (supplier CAPA)
- **Testing cost**: Independent laboratory testing costs PHP 500–5,000 per test; customers may not expect this cost; BuildRight should communicate this upfront
- **Certificate accuracy**: Mill test certificates represent the manufacturing lot's average properties, not individual piece properties; customer must understand this limitation

### Staffing Implication
- **Sales Associate (Building Materials)**: Quality documentation request adds 5–10 minutes per request; at 8–12 requests per store per week, this represents ~1–2 hours/week; absorbed by existing staff
- **Receiving Clerk**: Physical verification inspection adds 10–15 minutes per inspection; at 3–5 inspections per store per week, this represents ~30 min–1.5 hours/week; absorbed by existing Receiving Clerks
- **No permanent incremental headcount**

### Time Estimate
- Request intake: 3–5 min
- Certificate retrieval: 2–3 min (automated)
- In-store verification (if applicable): 5–10 min
- Documentation & referral: 3–5 min
- **Total per request**: 13–23 min (with verification) or 8–13 min (documentation only)
