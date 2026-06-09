# Additional Operational Workflows — Batch 3

> Tile & flooring quantity calculator, bulk cement/sand/aggregates delivery, complete renovation packages, construction loan assistance, material takeoff estimation, multi-store aggregated orders, quick reorder from history, post-disaster insurance replacement, power tool battery compatibility checker, franchise/dealer mini-store program, employee long service awards, project staged delivery, home energy audit referral, lumber grade selection, RA 7641 retirement benefits, seasonal product post-season review, B2B blanket purchase agreements, B2B construction site delivery, paint color matching from sample, and electrical load calculation service.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain (Cross-Functional Batch)

- [W963. Customer Tile & Flooring Quantity Calculator & Waste Factor Recommendation](#w963-customer-tile--flooring-quantity-calculator--waste-factor-recommendation)
- [W964. Customer Bulk Cement, Sand & Aggregates Order & Direct-to-Site Delivery](#w964-customer-bulk-cement-sand--aggregates-order--direct-to-site-delivery)
- [W965. Customer Complete Bathroom/Kitchen Renovation Package Assembly & Order](#w965-customer-complete-bathroomkitchen-renovation-package-assembly--order)
- [W966. Customer Construction Loan Documentation Assistance & Partner Bank Referral](#w966-customer-construction-loan-documentation-assistance--partner-bank-referral)
- [W967. Store-Level Customer Project Material Takeoff & Professional Estimation Service](#w967-store-level-customer-project-material-takeoff--professional-estimation-service)
- [W968. Customer Multi-Store Aggregated Order & Consolidated Single Delivery](#w968-customer-multi-store-aggregated-order--consolidated-single-delivery)
- [W969. Customer Quick Reorder from Purchase History (Trade & Loyalty Members)](#w969-customer-quick-reorder-from-purchase-history-trade--loyalty-members)
- [W970. Customer Post-Disaster Insurance Claim Material Replacement Coordination](#w970-customer-post-disaster-insurance-claim-material-replacement-coordination)
- [W971. Customer Power Tool Battery & Accessory Cross-Compatibility Checker & Recommendation](#w971-customer-power-tool-battery--accessory-cross-compatibility-checker--recommendation)
- [W972. Customer Franchise & Dealer Mini-Store Program Management](#w972-customer-franchise--dealer-mini-store-program-management)
- [W973. Employee Long Service Award & Milestone Recognition Management](#w973-employee-long-service-award--milestone-recognition-management)
- [W974. Store-Level Customer Project Staged Delivery & Phased Material Release](#w974-store-level-customer-project-staged-delivery--phased-material-release)
- [W975. Customer Home Energy Audit Referral & Energy-Efficient Product Recommendation](#w975-customer-home-energy-audit-referral--energy-efficient-product-recommendation)
- [W976. Store-Level Customer Lumber & Plywood Grade Selection & Quality Verification](#w976-store-level-customer-lumber--plywood-grade-selection--quality-verification)
- [W977. Employee Retirement Benefit Fund (RA 7641) Administration & Processing](#w977-employee-retirement-benefit-fund-ra-7641-administration--processing)
- [W978. Vendor Seasonal Product Post-Season Performance Review & Assortment Rationalization](#w978-vendor-seasonal-product-post-season-performance-review--assortment-rationalization)
- [W979. Customer B2B Blanket Purchase Agreement & Scheduled Call-Off Management](#w979-customer-b2b-blanket-purchase-agreement--scheduled-call-off-management)
- [W980. Store-Level Customer Construction Site Delivery Scheduling & Multi-Drop Coordination (B2B)](#w980-store-level-customer-construction-site-delivery-scheduling--multi-drop-coordination-b2b)
- [W981. Customer Paint Color Matching from Physical Sample & Digital Photo](#w981-customer-paint-color-matching-from-physical-sample--digital-photo)
- [W982. Customer Electrical Load Calculation & Wire Size Recommendation Service](#w982-customer-electrical-load-calculation--wire-size-recommendation-service)

---

## W963. Customer Tile & Flooring Quantity Calculator & Waste Factor Recommendation

| Field | Detail |
|---|---|
| **Trigger** | Customer requests tile/flooring quantity calculation at store or via ecommerce/ mobile app |
| **Frequency** | ~12,000–15,000 calculations/month chain-wide (~60–75/store/month) |
| **Volume** | 1–3 room calculations per customer visit; average 2.2 rooms |
| **Owner** | Department Supervisor (Tiles & Flooring) |
| **Participants** | Sales Associate (Tile Specialist), Customer, Category Manager (pricing) |

### Background

Tile and flooring purchases are among the highest-value, highest-anxiety transactions in home improvement retail. Unlike most product categories where customers simply count units, tile purchases require calculating area coverage, accounting for room shape complexity, pattern alignment (especially for diagonal layouts), grout gap spacing, and a waste factor that varies by tile size and installation pattern. Ordering too few tiles results in shade variation between batches (dyelot differences) and project delays; ordering too many ties up customer capital and creates return logistics. In the Philippine market, residential rooms are often irregularly shaped, and tile sizes range from 20×20 cm ceramic to 120×120 cm porcelain to 60×120 cm wood-look planks. A professional quantity calculator service differentiates BuildRight from competitors, builds customer confidence, and increases average order value by ensuring customers purchase adequate quantities plus recommended accessories (adhesive, grout, tile spacers, waterproofing membrane, underlayment).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Room Measurement Intake**: Customer provides room dimensions via: (a) physical measurements — length × width (in meters or feet) for rectangular rooms; (b) room sketch — hand-drawn layout with dimensions for L-shaped, irregular, or multi-room areas; (c) floor plan photo — customer photographs a builder's floor plan or sketch for Tile Specialist to interpret; (d) mobile app — customer uses BuildRight app's room measurement tool (AR-based measurement using phone camera) to capture dimensions digitally; Sales Associate records: room shape (rectangular, L-shape, U-shape, irregular), length and width of each section, number of doorways, fixed cabinetry or fixtures to tile around, room type (bathroom, kitchen, living room, garage, outdoor patio) | Sales Associate / Customer | Department Supervisor | 5–10 min |
| 2 | **Tile Selection & Pattern Confirmation**: Customer selects tile product(s) from display; Sales Associate records: (a) tile SKU and dimensions (length × width in cm); (b) tile type — ceramic, porcelain, vitrified, natural stone, vinyl plank, laminate; (c) installation pattern — straight lay (parallel), diagonal (45°), herringbone, brick/basketweave, chevron; (d) grout gap — standard 2–3mm for ceramic/porcelain, 1mm for rectified tiles, 5mm for natural stone; (e) dyelot/batch number — system flags if current stock has multiple dyelots and recommends purchasing from single batch | Sales Associate / Customer | Department Supervisor | 5–10 min |
| 3 | **Automated Quantity Calculation & Waste Factor Application**: System calculates: (a) net floor area — total room area minus deductions for fixed fixtures (if specified); (b) tiles per sqm — calculated from tile dimensions plus grout gap; (c) waste factor — applied based on pattern: straight lay (5–8%), diagonal (10–15%), herringbone/chevron (15–20%), irregular room with many cuts (additional 5%); natural stone (additional 3–5% for breakage); (d) total tiles required = (net area + waste) ÷ tiles per sqm, rounded up to full boxes; (e) accessory quantities — tile adhesive (kg per sqm based on tile size and substrate), grout (kg per sqm based on joint width and tile thickness), tile spacers (packs based on tile count), waterproofing membrane (sqm for wet areas), underlayment (sqm for vinyl/laminate), threshold strips (linear meters), baseboard/skirting tiles (linear meters minus doorways); system presents itemized materials list with quantities, prices, and total | System / Sales Associate | Department Supervisor | 3–5 min (automated) |
| 4 | **Customer Review, Adjustment & Order Creation**: Customer reviews calculated quantities; Sales Associate discusses: (a) recommend purchasing 1–2 extra boxes beyond calculation for future repairs (dyelot matching); (b) explain return policy — unused, unopened boxes returnable within 30 days per W12; (c) offer tile installation service referral per W138; (d) offer tile cutting service per W944 if customer needs custom cuts for corners and edges; customer confirms or adjusts quantities; Sales Associate creates order via POS quotation (W542) for customer approval or direct sale if customer decides immediately; quotation saved to customer's loyalty account for future reference per W894 (Project Vault) | Sales Associate / Customer | Department Supervisor | 5–10 min |
| 5 | **Dyelot Reservation & Stock Allocation**: For orders not immediately fulfilled from store stock: (a) system checks current store inventory for selected tile SKU and dyelot; (b) if insufficient stock in matching dyelot, system checks DC inventory and nearest stores per W22; (c) system allocates stock and places dyelot hold — reserved for customer for 7 days; (d) if no matching dyelot available, Sales Associate notifies customer of potential shade variation and offers alternatives; (e) for special order tiles (imported, premium): Sales Associate creates special order per W545 with estimated delivery date from vendor; customer informed that dyelot consistency cannot be guaranteed for split deliveries | Sales Associate / System | Department Supervisor | 5 min |

### System Touchpoints
- Tile quantity calculator module (POS and mobile app) with pattern-based waste factor engine
- Real-time inventory availability with dyelot/batch tracking per SKU per store (W533)
- POS quotation module (W542) for itemized material list generation
- Customer loyalty account integration for quotation saving (W894)
- Product catalog with tile specifications (dimensions, material, recommended adhesive/grout) per W50
- Ecommerce/mobile app AR measurement tool integration
- Special order processing (W545) for out-of-stock tiles
- Installation service referral (W138) for tile laying

### Pain Points / Risks
- **Measurement accuracy**: Customer-provided measurements are frequently inaccurate (±5–10cm is common in Philippine residential construction); over-reliance on customer measurements leads to under/over-ordering; Tile Specialist must emphasize importance of precise measurements and recommend AR tool or professional measurement per W442 for high-value orders (≥PHP 50,000)
- **Dyelot shade variation**: Tiles from different production batches may have visible color/texture differences; once a dyelot is depleted, matching replacements may be impossible; recommending extra boxes at point of sale mitigates; system must track dyelot at receiving per W3
- **Waste factor disputes**: Customers may challenge the waste factor percentage as excessive, especially for straight lay patterns; transparent calculation breakdown with visual diagram showing where cuts occur educates the customer; waste factor recommendations align with Philippine construction industry standards (NSCP)
- **Return logistics for heavy tiles**: Tile boxes are heavy (20–30 kg each); returning unused boxes requires customer transport or paid pickup; clear return policy communication at sale prevents disputes; store receiving must handle tile returns carefully to prevent breakage per W12

### Staffing Implication
- **Sales Associate (Tile Specialist)**: Tile calculations consume ~3–4 hours/day at 60–75 calculations; absorbed by existing Tiles & Flooring Department Supervisor or Sales Associate with specialized tile training
- **Training**: 16-hour tile quantity calculation and flooring product knowledge certification per W51; includes hands-on measurement exercises and waste factor scenarios
- **No incremental headcount**

### Time Estimate
- Room measurement intake: 5–10 min
- Tile selection & pattern confirmation: 5–10 min
- Quantity calculation (automated): 3–5 min
- Customer review & order creation: 5–10 min
- Dyelot reservation: 5 min
- **Total per calculation**: 25–40 min of staff time

---

## W964. Customer Bulk Cement, Sand & Aggregates Order & Direct-to-Site Delivery

| Field | Detail |
|---|---|
| **Trigger** | Customer (contractor, developer, or homeowner) orders bulk cement, sand, gravel, or aggregates for construction site delivery |
| **Frequency** | ~8,000–10,000 orders/month chain-wide (~40–50/store/month) |
| **Volume** | Average order: 50–100 bags of cement (40kg each) or 1–3 cubic meters of sand/gravel; high-value orders: 500+ bags or 10+ cubic meters |
| **Owner** | Department Supervisor (Lumber & Building Materials) |
| **Participants** | Sales Associate, Customer, Receiving Clerk, Delivery Coordinator, Category Manager, 3PL/Delivery Partner |

### Background

Cement, sand, gravel, and aggregates (crushed stone, base course, filler sand) are the highest-volume, lowest-margin products in a hardware retailer's assortment. These heavy construction materials are impractical to stock in standard store backrooms and are typically sold through direct-to-site delivery arrangements where vendor trucks deliver directly to the customer's construction site, with BuildRight acting as the ordering and billing intermediary. The Philippine construction industry consumes enormous volumes of these materials — a typical residential house construction requires 400–600 bags of cement and 15–25 cubic meters of sand and gravel. BuildRight's 200-store network and vendor relationships enable competitive pricing and reliable delivery scheduling that independent hardware stores cannot match. This workflow handles the full lifecycle: customer order, vendor scheduling, site delivery coordination, proof of delivery, and financial reconciliation. This is a core B2B revenue driver, particularly for the trade and corporate customer segments.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Order Intake & Site Information**: Customer provides: (a) material type — Portland cement (bagged, 40kg), Portland cement (bulk, by ton), sand (fine, coarse, washed), gravel (3/4", 1/2", base course), aggregates as specified; (b) quantity — bags of cement, cubic meters (sand/gravel), or metric tons; (c) delivery address — construction site address with landmark description (Philippine addresses often lack precise street numbering); (d) site access conditions — truck accessibility (10-wheeler, 6-wheeler, or small truck only), road restrictions (LGU truck ban hours per W431), low-clearance obstacles (overhead wires, footbridges), unloading method (manual carry, chute, boom pump); (e) preferred delivery date and time window; (f) customer type — walk-in, trade account (per W897), corporate account (per W460), or project account (per W162) | Sales Associate | Department Supervisor | 10–15 min |
| 2 | **Pricing, Availability & Quotation**: System checks: (a) current cement price per bag — subject to frequent market fluctuations (Philippine cement prices vary PHP 20–50/bag month-to-month); system pulls latest vendor contract price per W62 and adds BuildRight margin; (b) sand/gravel price per cubic meter — varies by source quarry, distance to delivery site, and current market rate; (c) delivery fee — calculated based on: distance from nearest vendor depot or BuildRight yard to delivery site, vehicle type required, unloading method, and LGU truck ban surcharge (if delivery window falls within restricted hours per W431); (d) volume discount — tiered pricing for orders ≥100 bags cement, ≥5 cubic meters sand/gravel; system generates quotation including: materials cost, delivery fee, applicable taxes (VAT 12%), and payment terms (cash on delivery for non-account customers; net 30 for trade/corporate accounts per W24); quotation valid for 3 days due to cement price volatility | Sales Associate / System | Department Supervisor | 5–10 min |
| 3 | **Order Confirmation & Payment**: Customer accepts quotation; payment processing: (a) walk-in/non-account — full payment at POS or upon delivery (COD); (b) trade account — charged to credit account per W24, subject to available credit limit; (c) corporate/project account — per project billing terms per W165, may include progressive billing; Sales Associate creates bulk delivery order in ERP: order type = "Bulk Material Direct Delivery"; linked to customer account; delivery site address and access conditions recorded; preferred delivery date scheduled; system sends order confirmation via SMS/email with delivery details | Sales Associate / Cashier | Department Supervisor | 5–10 min |
| 4 | **Vendor Scheduling & Logistics Coordination**: Back-office Delivery Coordinator (or Sales Associate at smaller stores) contacts vendor/3PL to schedule delivery: (a) confirms material availability at vendor depot or quarry; (b) schedules truck and driver — vendor-supplied truck (standard) or BuildRight-contracted 3PL truck; (c) confirms delivery date and time window with customer via phone/SMS; (d) for multi-drop orders (large quantities requiring multiple truckloads): coordinates sequential deliveries with customer's construction foreman; (e) records truck plate number, driver name, and driver contact number in ERP for tracking; (f) generates delivery receipt (DR) with: material type, quantity ordered, delivery address, customer name, and space for receiving signature | Delivery Coordinator / Sales Associate | Department Supervisor | 10–20 min |
| 5 | **Site Delivery Execution & Proof of Delivery**: Vendor/3PL truck arrives at construction site: (a) driver contacts customer's site contact (construction foreman or homeowner) upon arrival; (b) unloading method executed per order specification: manual carry (crew stacks bags at designated staging area on site), chute (sand/gravel discharged directly from truck bed to ground pile), boom pump (for sites with restricted access — additional fee); (c) customer's site representative counts and verifies quantity received against delivery receipt; (d) driver and customer representative sign delivery receipt — customer copy and driver copy; (e) any quantity discrepancy (short delivery, spillage) noted on DR and photographed; (f) driver returns signed DR to Delivery Coordinator | Delivery Partner / Customer Site Rep | Delivery Coordinator | 30–90 min (varies by volume and unloading method) |
| 6 | **Delivery Reconciliation & Financial Settlement**: Delivery Coordinator reconciles: (a) signed DR quantity vs. ordered quantity — if short delivery: system generates credit note per W101 for undelivered quantity; if over delivery: customer charged for additional quantity; (b) delivery condition — if material damage reported (wet cement bags, contaminated sand): system creates quality complaint per W110 and vendor chargeback per W245; (c) financial posting: revenue recognized at delivery confirmation; COGS posted from vendor; delivery fee revenue recognized; for trade/corporate accounts: invoice generated and posted to AR per W8; for COD: payment reconciled against delivery receipt | Delivery Coordinator / Finance | Department Supervisor | 10–15 min |

### System Touchpoints
- POS bulk order module with material pricing, volume discounts, and delivery fee calculator
- Customer account and credit limit check (W24, W460) for trade/corporate accounts
- Vendor contract pricing integration (W62) for real-time cement/sand price lookup
- Delivery scheduling and route planning module (W196) with LGU truck ban awareness (W431)
- Delivery receipt generation and proof-of-delivery capture (mobile/electronic signature)
- Inventory decrement — materials bypass store inventory; goods-in-transit tracked at vendor depot until delivery
- Revenue and COGS posting triggered by delivery confirmation
- SMS/email notification engine for customer delivery updates
- Vendor 3PL performance tracking per W242

### Pain Points / Risks
- **Cement price volatility**: Philippine cement prices fluctuate due to manufacturer price adjustments, supply disruptions, and seasonal demand; quotations must have short validity (3 days); system must track latest vendor price and update POS pricing promptly; frequent price changes require clear communication to customers at order intake
- **Site access challenges**: Philippine construction sites in dense urban areas (Metro Manila, Cebu) often have narrow streets, overhead obstructions, and limited truck turning radius; incorrect site assessment leads to failed deliveries and redelivery costs; Delivery Coordinator must verify site access conditions at order intake and match appropriate vehicle type
- **Quantity disputes at delivery**: Customer's site representative may dispute the delivered quantity, especially for sand/gravel which is measured by volume (cubic meters) and can settle during transport; standardized volumetric measurement at loading (leveled truck bed measurement) and photographic evidence at delivery mitigate disputes
- **Weather disruption**: Rain damages bagged cement and makes sand/gravel unloading difficult on muddy sites; delivery postponement protocol required; system must support easy rescheduling; pre-positioning under cover or tarpaulin at vendor depot during rainy season per W960
- **Cash handling for COD deliveries**: Driver collects cash payment at site for COD orders; cash security risk for drivers carrying large amounts (a PHP 100,000+ order is common); armored car escort for orders exceeding PHP 200,000; electronic payment (GCash, bank transfer) preferred and incentivized with 1% discount

### Staffing Implication
- **Delivery Coordinator**: 1 per store (may be shared role with Receiving Clerk at smaller stores) handles bulk delivery scheduling; activity consumes ~4–5 hours/day at 40–50 orders; absorbed by existing Receiving Clerk role at stores with <30 bulk orders/month
- **Training**: 8-hour bulk material ordering and logistics coordination training per W51
- **No incremental headcount**

### Time Estimate
- Order intake & site information: 10–15 min
- Pricing & quotation: 5–10 min
- Order confirmation & payment: 5–10 min
- Vendor scheduling & logistics: 10–20 min
- Site delivery execution: 30–90 min (3PL/vendor time)
- Delivery reconciliation: 10–15 min
- **Total per order of BuildRight staff time**: 40–70 min (delivery execution is vendor-performed)

---

## W965. Customer Complete Bathroom/Kitchen Renovation Package Assembly & Order

| Field | Detail |
|---|---|
| **Trigger** | Customer requests a complete renovation package for a bathroom or kitchen at store or via ecommerce |
| **Frequency** | ~2,000–3,000 packages/month chain-wide (~10–15/store/month) |
| **Volume** | 1 package per transaction; average package value PHP 35,000–80,000 (bathroom) or PHP 50,000–150,000 (kitchen) |
| **Owner** | Department Supervisor (cross-departmental) |
| **Participants** | Sales Associate (Package Consultant), Customer, Department Supervisors (Plumbing, Tiles, Electrical, Tools), Installation Partner (W138), Category Manager |

### Background

Complete renovation packages are a high-value, high-margin offering that differentiates home improvement big-box retailers from single-category suppliers. A typical Philippine residential bathroom renovation requires coordinating 8–12 product categories: tiles (floor and wall), toilet bowl, lavatory/wash basin, shower set or bathtub, faucet fixtures, plumbing fittings (pipes, elbows, valves), waterproofing membrane, tile adhesive and grout, bathroom accessories (towel rack, soap dish, mirror), exhaust fan, lighting fixture, and electrical wiring/conduit. Kitchen renovations add cabinetry, countertop, sink, stove/range, range hood, and appliances. Most Filipino homeowners — especially first-time renovators — find the multi-category coordination overwhelming and appreciate a single-point-of-contact package that includes all materials plus installation. BuildRight's pre-configured and custom packages simplify the customer experience, increase average order value by 40–60% compared to individual category purchases, and drive installation service revenue per W138.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Needs Assessment & Space Measurement**: Customer approaches package consultation area (dedicated kiosk or department counter); Sales Associate conducts needs assessment: (a) room type — bathroom (full, half/guest), kitchen, laundry/utility, or outdoor wash area; (b) scope — complete renovation (gut renovation), partial refresh (fixture replacement only), or new construction; (c) room dimensions — customer provides measurements or Sales Associate records from floor plan/app; (d) budget range — customer indicates budget ceiling (critical for package tier selection); (e) style preference — modern, minimalist, classic, industrial; (f) household considerations — number of users, elderly/PWD accessibility needs (grab bars, seated shower), child safety; (g) timeline — target completion date; Sales Associate records all parameters in package configurator module | Sales Associate | Department Supervisor | 15–20 min |
| 2 | **Package Tier Selection & Customization**: Sales Associate presents pre-configured package tiers: (a) **Essential Package** (PHP 25,000–40,000 for bathroom): entry-level fixtures, standard ceramic tiles, basic plumbing, no installation; (b) **Standard Package** (PHP 45,000–70,000): mid-range fixtures, upgraded tiles, complete plumbing materials, standard installation included; (c) **Premium Package** (PHP 75,000–120,000): premium fixtures (American Standard, Toto, Kohler), designer tiles, luxury accessories, professional installation, waterproofing warranty; (d) **Custom Package**: customer selects individual items from each category; Customer selects tier or customizes: Sales Associate adjusts individual components within the selected tier — e.g., upgrades toilet from standard to dual-flush, selects tile color from available options, adds grab bars for elderly; system dynamically recalculates package price with each change | Sales Associate / Customer | Department Supervisor | 15–25 min |
| 3 | **Material List Generation & Availability Check**: System generates complete material list (BOM) for selected package: (a) all items grouped by category (tiles, plumbing, electrical, fixtures, accessories, consumables); (b) quantities calculated based on room dimensions per W963 for tiles, W982 for electrical; (c) system checks real-time inventory per W533 for all items at customer's preferred store; (d) items unavailable at store — system checks DC availability and delivery lead time (1–3 days), or suggests in-stock alternatives; (e) system identifies items requiring special order (imported fixtures, premium tiles) with lead time; (f) total material list with individual and package-level pricing presented to customer | System / Sales Associate | Department Supervisor | 5–10 min |
| 4 | **Order Creation, Payment & Scheduling**: Customer confirms package; Sales Associate: (a) creates package order in POS — single order with multiple line items grouped by delivery phase; (b) payment: full payment for materials (essential/premium packages) or 50% deposit + progress payment for custom packages per W546; (c) installation scheduling: if package includes installation per W138, Sales Associate coordinates with Installation Partner for site survey scheduling within 3–5 days; (d) delivery scheduling: materials scheduled for delivery in phases — (i) phase 1: demolition tools, waterproofing, adhesive, tiles; (ii) phase 2: plumbing fixtures, faucet sets, fittings; (iii) phase 3: accessories, lighting, final fixtures; phased delivery prevents on-site material damage and reduces storage requirements at customer's home | Sales Associate / Cashier / Installation Partner | Department Supervisor | 10–15 min |
| 5 | **Post-Sale Follow-Up & Satisfaction Verification**: After installation completion (typically 5–15 days for bathroom, 15–30 days for kitchen): (a) system triggers post-completion survey per W65 (customer satisfaction); (b) Sales Associate makes courtesy call within 3 days of completion to verify satisfaction; (c) any defects or missing items addressed per W12 (returns) or W795 (service warranty); (d) customer offered loyalty points bonus (500–1,000 points) for completing satisfaction survey; (e) project photos (with customer consent) uploaded to inspiration gallery per W905; (f) customer offered annual maintenance reminder service per W282 (subscription billing for periodic inspection) | Sales Associate / Customer | Department Supervisor | 15–20 min (post-sale) |

### System Touchpoints
- Package configurator module with pre-built templates and dynamic pricing
- Real-time inventory check across all product categories per store (W533)
- POS package order creation with multi-phase delivery scheduling (W546)
- Installation service scheduling integration (W138)
- Customer loyalty system for points bonus on package purchase
- Quotation module (W542) for custom package pricing
- Tile quantity calculator (W963) and electrical load calculator (W982) integration
- Post-sale follow-up and satisfaction survey (W65, W756)
- Project photo gallery integration (W905)

### Pain Points / Risks
- **Multi-category coordination complexity**: Package requires items from 8–12 different product categories, each with its own inventory, vendor, and lead time; any single item stockout delays the entire package; buffer stock planning for package components and proactive substitution lists mitigate
- **Installation quality liability**: BuildRight's brand reputation is tied to installation quality even when installation is performed by third-party partners; strict partner accreditation per W600, quality audit per W213, and service warranty per W795 protect brand; customer disputes over installation quality vs. material quality must be clearly delineated in the sales agreement
- **Customer scope creep**: Customers frequently request additions and changes after package order is confirmed ("while you're here, can you also fix the…"); clear scope definition in the package agreement, formal change order process per W792, and upfront pricing for common additions prevent margin erosion
- **Phased delivery coordination**: Multiple delivery trips to customer's home increase logistics cost and failure risk; precise scheduling, SMS notifications, and customer commitment to delivery windows per phase required; consolidation into minimum number of deliveries balanced against on-site storage constraints

### Staffing Implication
- **Sales Associate (Package Consultant)**: 1 per store trained in multi-category package assembly; package consultations consume ~2–3 hours/day at 10–15 packages; absorbed by existing Department Supervisor or senior Sales Associate with cross-category training per W567
- **Training**: 40-hour bathroom/kitchen product knowledge + package configuration certification per W51; includes hands-on product familiarization across plumbing, tiles, electrical, and fixtures categories
- **No incremental headcount**

### Time Estimate
- Needs assessment & measurement: 15–20 min
- Package selection & customization: 15–25 min
- Material list & availability check: 5–10 min
- Order creation & scheduling: 10–15 min
- Post-sale follow-up: 15–20 min
- **Total per package**: 60–90 min of staff time (across multiple touchpoints)

---

## W966. Customer Construction Loan Documentation Assistance & Partner Bank Referral

| Field | Detail |
|---|---|
| **Trigger** | Customer inquires about financing options for home construction, renovation, or improvement project at store |
| **Frequency** | ~1,500–2,500 referrals/month chain-wide (~8–12/store/month) |
| **Volume** | 1 referral per customer; estimated 30–40% conversion to approved loan |
| **Owner** | Store Manager |
| **Participants** | Sales Associate, Customer, Store Manager, Partner Bank Loan Officer, Category Manager |

### Background

Home construction and major renovation projects in the Philippines typically cost PHP 500,000 to PHP 5,000,000+, well beyond the cash capacity of most Filipino homeowners. Construction financing — through bank home improvement loans, Pag-IBIG (HDMF) housing loans, or SSS salary loans — is a critical enabler for BuildRight's higher-value sales. Many customers begin their renovation journey at BuildRight stores, where they select materials and discover the total project cost exceeds their budget. By offering construction loan documentation assistance and direct referral to partner banks, BuildRight: (a) converts budget-constrained prospects into completed sales; (b) earns referral fees from partner banks (typically 1–2% of loan amount); (c) differentiates from competitors who offer no financing support; (d) builds long-term customer relationships as the materials supplier for the loan-funded project. This workflow covers the in-store assistance and referral process; actual loan processing and approval is performed by the partner bank.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Financing Need Identification**: During any high-value sales interaction (typical trigger: customer's material list exceeds PHP 100,000), Sales Associate or Store Manager identifies financing need when: (a) customer expresses concern about total project cost; (b) customer asks about installment or payment plans; (c) customer is selecting materials for a major renovation/construction project; Sales Associate introduces financing option: "BuildRight works with partner banks to help customers finance their home improvement projects. Would you like to learn about construction loan options?" | Sales Associate | Store Manager | 2–3 min |
| 2 | **Financing Option Presentation & Pre-Qualification**: Store Manager or designated Sales Associate presents financing options: (a) **Bank Home Improvement Loan** — partner banks (BDO, BPI, Metrobank, Security Bank): PHP 100,000–3,000,000 loan amount, 12–60 month terms, 8–14% interest rate, requires proof of income and property documents; (b) **Pag-IBIG (HDMF) Housing Loan** — government housing loan for members: lower interest rates (3–6.5%), longer terms (up to 30 years), requires Pag-IBIG membership; (c) **SSS Salary Loan** — for employed SSS members: smaller amounts (PHP 20,000–40,000), quick processing, deducted from salary; (d) **Credit Card Installment** — 0% interest promos per W747 for qualifying cardholders; (e) **Contractor Micro-Lending** — per W953 for registered trade professionals; Sales Associate performs informal pre-qualification check: customer employment status, estimated monthly income, existing loan obligations, property ownership status; Sales Associate recommends most suitable option(s) | Store Manager / Sales Associate | Store Manager | 10–15 min |
| 3 | **Material Cost Documentation Preparation**: Sales Associate generates BuildRight Material Cost Document: (a) detailed itemized quotation from POS per W542 with all materials, quantities, and prices for the planned project; (b) quotation printed on BuildRight letterhead with store stamp — accepted by partner banks as supporting documentation for loan application; (c) quotation includes: customer name, project description, total material cost, validity period (30 days), and store contact information for bank verification; (d) for larger projects: Sales Associate attaches project scope description and material specifications from W967 (material takeoff) if available; (e) system flags quotation as "Loan Application — Pending" status to track conversion | Sales Associate | Store Manager | 5–10 min |
| 4 | **Partner Bank Referral & Handover**: Sales Associate provides customer with: (a) BuildRight Material Cost Document (quotation); (b) partner bank referral card — includes bank name, branch, loan officer contact, and BuildRight referral code; (c) checklist of required documents for loan application: government-issued ID, proof of income (payslips, ITR, COE), proof of billing address, property documents (tax declaration, land title if applicable), bank statements (3 months); (d) system logs referral: customer ID, estimated project value, referred bank, referral date, referral code; Sales Associate encourages customer to visit partner bank within 7 days and offers to schedule a bank appointment; partner bank loan officer notified of referral via secure portal | Sales Associate / Customer | Store Manager | 5–10 min |
| 5 | **Conversion Tracking & Follow-Up**: System tracks referral lifecycle: (a) partner bank updates referral status via secure portal: Application Submitted → Under Review → Approved → Disbursed / Declined; (b) upon loan approval and disbursement: partner bank notifies BuildRight; Store Manager or Sales Associate contacts customer to convert quotation into confirmed order; customer pays using loan proceeds (bank-to-bank transfer or manager's check); (c) referral fee: system calculates referral fee (1–2% of loan amount) and records as other income; quarterly settlement with partner bank per agreement; (d) for declined referrals: Sales Associate follows up within 7 days to discuss alternative options — smaller project scope, different materials, or alternative financing (credit card installment per W747); (e) monthly: Store Manager reviews referral conversion dashboard — referral count, conversion rate, total loan-funded revenue, referral fee income | System / Sales Associate / Store Manager | Store Manager | Ongoing |

### System Touchpoints
- POS quotation module (W542) with "Loan Application" quotation type
- Partner bank referral portal integration (secure API for referral logging and status updates)
- Customer account integration for referral tracking
- Conversion tracking dashboard (referral → loan → sale)
- Referral fee calculation and settlement tracking
- SMS/email notification for customer follow-up
- Credit card installment integration (W747)

### Pain Points / Risks
- **Referral conversion rate**: Not all referrals convert to approved loans; typical Philippine bank home improvement loan approval rate is 30–40% for referred customers; store staff may invest significant time in non-converting referrals; pre-qualification screening at step 2 improves conversion; referral tracking system provides visibility
- **Customer data privacy**: Sharing customer information with partner banks requires explicit consent per RA 10173 (Data Privacy Act); consent form signed at referral; partner bank portal must comply with NPC requirements per W434; customer data shared only with customer-selected bank
- **Quotation validity vs. loan processing time**: Bank loan processing takes 2–4 weeks; BuildRight material prices may change during this period; quotation extended to 30 days for loan applications (vs. 7 days standard); if prices change significantly (>5%) during loan processing, BuildRight honors original quotation as a goodwill gesture for loan-referred customers
- **Partner bank relationship management**: Bank relationships require ongoing maintenance — joint marketing, co-branded events, staff training on loan products, and quarterly business reviews; Category Manager or Store Manager dedicates ~4 hours/month to bank relationship activities per W617

### Staffing Implication
- **Store Manager**: Primary owner of bank referral program at store level; financing conversations consume ~1–2 hours/day during peak construction season (Jan–May, Sep–Dec); absorbed by existing Store Manager role
- **Training**: 4-hour partner bank loan product training per W51; quarterly refresher from bank loan officers
- **No incremental headcount**

### Time Estimate
- Financing need identification: 2–3 min
- Option presentation & pre-qualification: 10–15 min
- Material cost documentation: 5–10 min
- Bank referral & handover: 5–10 min
- Conversion tracking & follow-up: ongoing (5 min per follow-up call)
- **Total per referral**: 25–40 min of staff time

---

## W967. Store-Level Customer Project Material Takeoff & Professional Estimation Service

| Field | Detail |
|---|---|
| **Trigger** | Customer presents construction plan, blueprint, or project description for comprehensive material estimation |
| **Frequency** | ~1,500–2,500 estimations/month chain-wide (~8–12/store/month) |
| **Volume** | 1 project per estimation; average project value PHP 150,000–500,000 |
| **Owner** | Department Supervisor (Building Materials) |
| **Participants** | Sales Associate (Estimation Specialist), Customer, Department Supervisors (multi-department), Category Manager, Installation Partner |

### Background

Material takeoff — the process of analyzing construction plans to determine exact quantities of all materials needed — is a professional service typically provided by architects, engineers, or contractors. BuildRight's in-store material takeoff service democratizes this expertise, allowing homeowners and small contractors to receive comprehensive material lists and cost estimates without hiring a professional quantity surveyor. This service is particularly valuable in the Philippine market where many residential constructions are designed by independent architects or drafted by municipal engineers, and the homeowner is responsible for purchasing materials independently (the "labor-only" contracting model common in the Philippines). A single residential house takeoff may encompass 500+ line items across all product categories — from structural steel and cement to finishing tiles and paint. The service drives enormous basket sizes, captures the entire project spend (vs. piecemeal purchasing at multiple stores), and builds deep customer loyalty.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Project Document Intake & Scope Definition**: Customer presents project documentation: (a) architectural floor plans and elevations; (b) structural plans (if available); (c) electrical and plumbing layout (if available); (d) scope of work narrative — description of what customer wants to build (e.g., "2-story residential, 120 sqm per floor, 3 bedrooms, 2 bathrooms, 1 kitchen, carport"); (e) budget range and quality tier (economy, standard, premium); Estimation Specialist reviews documents for completeness; if plans are incomplete, Estimation Specialist provides checklist of required information and schedules follow-up; project registered in ERP with unique project ID linked to customer account | Estimation Specialist | Department Supervisor | 20–30 min |
| 2 | **Multi-Category Material Quantification**: Estimation Specialist performs material takeoff by category: (a) **Structural** — concrete volume (cement, sand, gravel, rebar quantity by diameter), hollow blocks, structural steel, form lumber; (b) **Masonry & Finishing** — wall finish area (plastering, paint), ceiling area, floor area per room type; (c) **Tiles & Flooring** — per room calculations using W963; (d) **Plumbing** — pipe lengths (supply and drainage), fittings, fixtures (toilet, lavatory, faucet, shower), water tank; (e) **Electrical** — wire lengths per circuit, switches, outlets, breakers, panel board, lighting fixtures per W982; (f) **Doors & Windows** — door leaves, frames, locks, hinges, window frames, glass; (g) **Roofing** — roofing sheets, ridge caps, gutters, fascia, insulation; (h) **Paint & Finishes** — wall area calculations, paint quantity per coat, primer, putty; (i) **Hardware & Fixtures** — cabinet hardware, door hardware, bathroom accessories; quantification performed using standardized BuildRight material factor tables (e.g., cement bags per cubic meter of concrete at specified mix ratio, hollow blocks per sqm of wall) | Estimation Specialist | Department Supervisor | 60–120 min |
| 3 | **Cost Estimation & Budget Optimization**: System compiles quantified materials into costed BOM: (a) each line item priced at current BuildRight retail or trade price (if customer has trade account per W897); (b) system applies project-level volume discount for total order value exceeding PHP 100,000 (5%), PHP 300,000 (8%), PHP 500,000 (10%); (c) Estimation Specialist presents budget optimization options: (i) quality tier adjustments — e.g., standard tiles vs. premium tiles for specific rooms; (ii) material substitutions — e.g., PVC pipes vs. GI pipes for non-pressure drainage; (iii) phased purchasing — priority items for immediate construction vs. items purchasable later; (d) total project cost presented with breakdown by category and by construction phase; (e) contingency allowance of 5–10% recommended for unforeseen requirements | Estimation Specialist / System | Department Supervisor | 20–30 min |
| 4 | **Estimate Presentation & Customer Review**: Estimation Specialist presents comprehensive estimate to customer: (a) printed/projected estimate document with: project name, customer name, date, room-by-room breakdown, category subtotals, project total, recommended contingency, and validity period (15 days); (b) walk-through of major categories explaining material choices, quantities, and alternatives; (c) customer questions addressed; (d) estimate saved to customer's loyalty account per W894 (Project Vault) for future reference, sharing with contractor, and reorder capability; (e) if customer has trade account, estimate linked to account for credit limit review per W328 | Estimation Specialist / Customer | Department Supervisor | 30–45 min |
| 5 | **Order Conversion & Project Fulfillment Planning**: If customer decides to purchase: (a) estimate converted to sales order in POS; (b) payment terms arranged — full payment, deposit + progress billing per W546, or trade credit per W24; (c) phased delivery scheduled per W974 (staged delivery) aligned with construction timeline: Phase 1 (structural materials), Phase 2 (masonry, tiles, plumbing rough-in), Phase 3 (electrical, finishing, fixtures); (d) installation services offered per W138 for specialized items; (e) project assigned to Store Manager's active project portfolio for ongoing relationship management | Sales Associate / Store Manager | Department Supervisor | 20–30 min |

### System Touchpoints
- Material takeoff estimation module with standardized material factor tables
- Multi-category product catalog integration (W50) with real-time pricing
- Tile quantity calculator (W963) and electrical calculator (W982) integration
- POS quotation conversion (W542) with project-level volume discounts
- Customer loyalty Project Vault (W894) for estimate saving and sharing
- Staged delivery scheduling (W974)
- Trade account credit check (W24, W328)
- Installation service referral (W138)

### Pain Points / Risks
- **Estimation accuracy**: Material takeoff accuracy depends on the quality and completeness of customer-provided plans; incomplete plans lead to inaccurate estimates and customer disappointment when actual quantities differ; Estimation Specialist must clearly communicate assumptions and exclusions; estimate document includes disclaimer that quantities are estimates based on provided information and actual requirements may vary
- **Time investment vs. conversion**: A comprehensive material takeoff takes 2–3 hours of specialist time; not all estimates convert to sales (estimated 40–50% conversion); pre-screening customers for genuine purchase intent (trade account holders, known contractors, customers with approved financing per W966) prioritizes specialist time; non-converting estimates still build goodwill and future pipeline
- **Price volatility during project lifecycle**: Construction projects span 3–12 months; material prices at estimation time may differ significantly from purchase time (especially cement and steel); estimate validity limited to 15 days; price lock option offered for an additional fee (2% of project value, refundable against purchase)
- **Scope liability**: Estimation Specialist is not a licensed engineer or architect; BuildRight provides material quantity estimates, not structural or design advice; clear disclaimer on estimate document that structural engineering consultation is recommended for load-bearing elements; service is a sales enablement tool, not a professional engineering service

### Staffing Implication
- **Estimation Specialist**: 1 per store with construction industry background (former quantity surveyor, engineer, or experienced contractor); estimation consumes 4–6 hours/day at 8–12 projects; role may be shared with Department Supervisor at smaller stores; hiring preference for candidates with civil engineering or architecture background
- **Training**: 40-hour BuildRight product knowledge + material factor table training per W51; annual recalibration of material factors based on actual project data
- **No incremental headcount** (role absorbed by existing Building Materials Department Supervisor or dedicated specialist at high-volume stores)

### Time Estimate
- Document intake & scope definition: 20–30 min
- Multi-category material quantification: 60–120 min
- Cost estimation & optimization: 20–30 min
- Estimate presentation & review: 30–45 min
- Order conversion & planning: 20–30 min
- **Total per project**: 2.5–4.5 hours of specialist time

---

## W968. Customer Multi-Store Aggregated Order & Consolidated Single Delivery

| Field | Detail |
|---|---|
| **Trigger** | Customer wants to purchase items available across multiple BuildRight stores and receive a single consolidated delivery |
| **Frequency** | ~1,000–1,500 orders/month chain-wide (~5–7/store/month) |
| **Volume** | 3–8 items per order; average order value PHP 15,000–45,000 |
| **Owner** | Ecommerce Manager |
| **Participants** | Customer, Sales Associate (or Ecommerce Ops), Store Operations (multiple stores), DC/Logistics, Category Manager |

### Background

With 35,000 active SKUs across 200 stores, no single store stocks every item. Customers — especially B2B trade professionals and homeowners with large project lists — frequently encounter situations where the items they need are distributed across multiple BuildRight locations. Without this workflow, customers must: (a) visit multiple stores personally; (b) place separate delivery orders from each store incurring multiple delivery fees; or (c) forgo purchasing unavailable items from BuildRight and source them from competitors. The multi-store aggregated order capability enables BuildRight to capture the customer's entire spend by consolidating items from multiple stores into a single delivery. Items are either transferred to a designated consolidation store (typically the customer's nearest store) or consolidated at the nearest DC, then delivered to the customer in a single shipment. This workflow is particularly valuable for project-based B2B customers (W162) and large home renovation projects.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Order Placement & Item Sourcing**: Customer places order via: (a) ecommerce website/app — adds all desired items to cart; system automatically identifies items not available at the customer's preferred store and sources from other locations; (b) in-store Sales Associate — customer provides shopping list; Sales Associate checks availability across stores using ERP location inventory view (W533); (c) phone/email to call center — customer provides list; agent creates order and sources items; for each unavailable item at preferred store, system identifies: nearest store with stock, stock quantity, and estimated transfer time to consolidation point | Customer / Sales Associate / System | Ecommerce Manager | 10–15 min |
| 2 | **Consolidation Point Selection & Routing**: System determines optimal consolidation point: (a) if all sourced items can reach a single store within 2 business days — consolidation at customer's preferred store; (b) if items are spread across multiple regions — consolidation at nearest DC which serves as cross-dock point; (c) if any item requires vendor procurement (out of stock at all locations) — system flags item with estimated lead time and offers customer choice: (i) wait for full consolidation, (ii) partial delivery now + remaining items later, (iii) remove item from order; system calculates: transfer costs (inter-store/inter-DC), consolidation handling fee (if applicable), and single delivery fee to customer address | System / Ecommerce Ops | Ecommerce Manager | 5–10 min (automated) |
| 3 | **Inter-Location Transfer Orders Creation**: System automatically creates transfer orders: (a) for each source store: pick list generated for items to ship to consolidation point; (b) transfer orders routed per W22 (inter-store) or W218 (inter-DC); (c) priority flag set based on customer's requested delivery date; (d) source stores pick and ship items within 24–48 hours of transfer order receipt; (e) system tracks in-transit inventory per source location; (f) consolidation point receives items and stages in designated aggregation area (separate from regular BOPIS staging) | System / Store Operations | Ecommerce Manager | Automated (24–48 hrs transfer time) |
| 4 | **Consolidation Quality Check & Delivery Execution**: At consolidation point: (a) Receiving Clerk verifies all transferred items received in good condition against transfer order; (b) any damaged items flagged — replacement sourced or customer notified of refund per W101; (c) all items consolidated into single delivery package/batch; (d) delivery scheduled via: (i) BuildRight own fleet (for bulky items) per W196, (ii) 3PL partner (Lalamove, Transportify) per W548; (e) customer receives consolidated delivery notification with tracking; (f) delivery executed per customer's chosen method: home delivery per W19 or store pickup per W11 | Receiving Clerk / Delivery Team | Ecommerce Manager | 30–60 min |
| 5 | **Financial Reconciliation & Inter-Store Settlement**: System handles financial flows: (a) revenue recognized at consolidation point (delivering store/DC); (b) inter-store inventory movement accounted per W919 (intercompany inventory movement accounting); (c) cost of goods transferred from source stores to consolidation point; (d) single customer invoice generated covering all items regardless of sourcing location; (e) delivery fee charged once (consolidated delivery benefit); (f) monthly: Finance reconciles inter-store transfer settlements per intercompany accounting (W14) | System / Finance | Ecommerce Manager | Automated (monthly reconciliation) |

### System Touchpoints
- Unified order management system (W536) with multi-location sourcing engine
- Real-time inventory availability across all 200 stores and 4 DCs (W533)
- Automated transfer order creation and tracking (W22, W218)
- Consolidation point staging area management
- Delivery scheduling and routing (W196) for consolidated shipment
- Inter-store financial settlement (W14, W919)
- Customer notification engine (W708) for status updates at each phase
- Ecommerce cart with multi-source item visibility

### Pain Points / Risks
- **Transfer delay propagation**: The consolidated delivery timeline is determined by the slowest source store; if one store delays its transfer, the entire order is held; SLA of 24–48 hours for inter-store transfers must be enforced; system escalates overdue transfers to Store Manager
- **Item damage during additional handling**: Each transfer adds handling risk — items are picked at source, transported, received at consolidation point, then delivered to customer; fragile items (tiles, glass, light fixtures) require enhanced packaging at source store; damage claims per W500
- **Customer expectation management**: Customers expect multi-store orders to be as fast as single-store orders; clear communication of consolidated delivery timeline (2–4 business days vs. same-day/next-day for in-stock) at order placement prevents disappointment; real-time status updates per item per location
- **Inventory reservation race condition**: Items identified as available at order placement may be sold to another customer before the transfer pick occurs; system must reserve inventory at source stores upon order confirmation (hard allocation) rather than soft allocation

### Staffing Implication
- **No incremental headcount** — workflow is primarily system-automated with execution absorbed by existing store operations and ecommerce teams
- **Receiving Clerk**: Additional 15–30 min/day for consolidation receiving at designated stores; absorbed by existing role

### Time Estimate
- Order placement & sourcing: 10–15 min
- Consolidation routing (automated): 5–10 min
- Transfer order fulfillment: 24–48 hrs (store operations)
- Consolidation & delivery: 30–60 min
- **Total of active BuildRight staff time per order**: 45–90 min (excluding transfer transit time)

---

## W969. Customer Quick Reorder from Purchase History (Trade & Loyalty Members)

| Field | Detail |
|---|---|
| **Trigger** | Customer (trade professional or loyalty member) requests to reorder from a previous purchase |
| **Frequency** | ~15,000–20,000 reorders/month chain-wide (~75–100/store/month) |
| **Volume** | 3–15 items per reorder; average reorder value PHP 5,000–15,000 |
| **Owner** | Ecommerce Manager |
| **Participants** | Customer, Sales Associate (if in-store), System, Store Operations, Loyalty Program |

### Background

Trade professionals — contractors, plumbers, electricians, and builders — purchase the same materials repeatedly across multiple construction projects. A plumber may buy the same PVC pipes, fittings, and solvent cement 20+ times per year. Similarly, loyal homeowners doing phased home improvements may need to repurchase the same paint color, tile adhesive, or hardware items. Quick reorder capability — allowing customers to repurchase from their order history with a single click or tap — is a powerful convenience feature that: (a) reduces purchase friction, increasing reorder frequency by an estimated 15–25%; (b) prevents customers from defecting to competitors for convenience; (c) increases average order value by suggesting complementary items; (d) provides data for demand forecasting (W31) by identifying repeatable purchase patterns. This workflow covers the reorder experience across in-store, mobile app, and web channels.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Identification & Purchase History Access**: Customer identifies themselves: (a) in-store — presents loyalty card, provides mobile number, or Sales Associate scans customer QR code; (b) mobile app — auto-identified via login; (c) web — auto-identified via login; (d) call center — agent verifies customer via mobile number or account number; system retrieves full purchase history: (i) in-store POS transactions; (ii) ecommerce orders; (iii) B2B invoice history; sorted by date with most recent first; filterable by: product category, date range, order value, store location, project name (if tagged per W894) | System / Sales Associate | Ecommerce Manager | 1–2 min |
| 2 | **Previous Order Selection & Item Review**: Customer browses purchase history and selects a previous order to reorder; system displays order details: (a) all items with product image, SKU, description, quantity previously purchased, and unit price; (b) current price displayed alongside previous price — price changes flagged (higher in red, lower in green); (c) current availability at customer's preferred store — green (in stock), yellow (low stock), red (out of stock with alternatives); (d) customer selects which items to include in reorder: select all, select individual, or select by category; (e) customer can adjust quantities (increase/decrease) per item | Customer / System | Ecommerce Manager | 3–5 min |
| 3 | **Smart Add-On Recommendations**: System presents smart recommendations based on reorder items: (a) frequently bought together — items commonly purchased with the reorder items by other trade customers (e.g., Teflon tape with pipe fittings, wall plugs with screws); (b) project completion suggestions — items needed to complete the typical project associated with reorder items (e.g., grout with tiles, sandpaper with paint); (c) consumables reminder — items likely consumed since last purchase (e.g., drill bits, blades, adhesive tubes); (d) new product alternatives — newer products in same category that may offer better value or performance; recommendations displayed as one-click add to cart; estimated 20–30% of reorders include at least one add-on item | System | Ecommerce Manager | 1–2 min (automated) |
| 4 | **Cart Review, Payment & Fulfillment**: Customer reviews cart: (a) all items with updated quantities and current prices; (b) any unavailable items flagged with alternatives (customer accepts alternative or removes item); (c) fulfillment selection: (i) in-store pickup (BOPIS) per W11 at preferred store; (ii) home delivery per W19; (iii) in-store immediate purchase (customer is at store); (d) payment: (i) in-store — cash, card, e-wallet at POS; (ii) online — credit card, GCash, Maya; (iii) trade account charge per W24; (e) loyalty points automatically applied if customer selects points-as-payment per W550; order confirmed and fulfillment initiated | Customer / Sales Associate / System | Ecommerce Manager | 3–5 min |
| 5 | **Reorder Analytics & Pattern Recognition**: System continuously analyzes reorder data: (a) reorder frequency by customer segment (trade vs. B2C); (b) most frequently reordered SKUs — informs auto-replenishment planning per W2A and demand forecasting per W31; (c) reorder conversion rate by channel (in-store vs. app vs. web); (d) add-on recommendation acceptance rate; (e) price sensitivity analysis — how price changes affect reorder behavior; (f) reorder pattern triggers for consumables subscription offer per W907 (e.g., customer reorders paint rollers every 2 months → offer monthly auto-shipment); insights reported to Merchandising (W1), Supply Chain (W31), and Marketing (W676) monthly | System / BI Team | Ecommerce Manager | Ongoing (automated analytics) |

### System Touchpoints
- Customer purchase history module (cross-channel: POS + ecommerce + B2B invoices)
- Loyalty member identification system (card, mobile, QR)
- Real-time inventory check per store (W533)
- Smart recommendation engine (W200) powered by purchase history analysis
- POS cart creation for in-store reorder
- Ecommerce/mobile app quick reorder button
- Fulfillment routing (W536) — BOPIS, delivery, or in-store
- Payment processing — multi-tender including trade account credit (W24) and loyalty points (W550)
- BI analytics module for reorder pattern analysis

### Pain Points / Risks
- **Product discontinuation between orders**: Products previously purchased may be discontinued or replaced by newer models; system must detect discontinued items and proactively suggest alternatives; "This item is no longer available. Customers who bought this also purchased [alternative]" messaging reduces frustration
- **Price increase friction**: Customers expect to pay the same price as their previous order; significant price increases on frequently reordered items cause complaints; transparent price display at reorder with change percentage; loyalty member price lock option for top-20 reordered SKUs (price guaranteed for 90 days)
- **Privacy perception**: Some customers may not realize BuildRight tracks full purchase history; clear privacy notice at loyalty enrollment per RA 10173; customer ability to delete purchase history per W834; opt-in for purchase history-based recommendations
- **Mobile app UX for large order history**: Trade professionals with years of purchase history have hundreds of orders; effective search, filtering, and tagging (by project, category, date) is essential; AI-powered order grouping (system recognizes that certain items are always bought together and groups them as "plumbing project bundle") simplifies navigation

### Staffing Implication
- **No incremental headcount** — quick reorder is a system feature; in-store execution absorbed by existing Sales Associate and POS workflows

### Time Estimate
- Customer identification: 1–2 min
- Order selection & review: 3–5 min
- Smart recommendations: 1–2 min
- Cart review & payment: 3–5 min
- **Total per reorder**: 8–14 min of customer/staff time (vs. 20–30 min for a fresh selection process)

---

## W970. Customer Post-Disaster Insurance Claim Material Replacement Coordination

| Field | Detail |
|---|---|
| **Trigger** | Customer presents insurance claim document for damaged building materials that need replacement after a natural disaster (typhoon, flood, earthquake, fire) |
| **Frequency** | ~500–1,000 coordination events/month average; surges to 3,000–5,000/month post-major typhoon |
| **Volume** | 1 insurance claim per customer; average claim material value PHP 50,000–300,000 |
| **Owner** | Store Manager |
| **Participants** | Customer, Store Manager, Sales Associate, Insurance Company Representative, Category Manager, Delivery Coordinator |

### Background

The Philippines experiences an average of 20 typhoons per year, with 5–8 making landfall as severe storms. Additionally, earthquakes, flooding, and fires cause regular property damage. Post-disaster rebuilding creates massive demand surges for building materials — roofing sheets, plywood, cement, lumber, nails, paint, electrical wiring, plumbing pipes, and tiles. Customers with property insurance must navigate the claim process: documenting damage, obtaining insurance adjuster assessment, receiving claim approval with a specified payout or material replacement value, and then sourcing replacement materials. BuildRight's post-disaster insurance claim coordination service provides a critical bridge between the insurance claim and material procurement: (a) helping customers interpret their insurance claim scope and match it to BuildRight's product catalog; (b) providing itemized material lists and pricing for insurance documentation; (c) coordinating delivery to damaged properties, often in areas with compromised infrastructure; (d) managing the payment flow between insurance company, customer, and BuildRight. This service positions BuildRight as the preferred post-disaster materials supplier and generates significant community goodwill.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Intake & Insurance Claim Document Review**: Customer arrives at store (or contacts via phone/email) with insurance claim documentation: (a) insurance claim letter/notice of loss — specifies damaged items, approved claim amount, and claim reference number; (b) insurance adjuster's damage assessment report — details scope of damage and approved repair scope; (c) photographs of damage — customer-provided or adjuster documentation; (d) property insurance policy number and insurance company contact; Store Manager or designated Sales Associate reviews claim documents for: completeness, claim validity period, payment terms (reimbursement vs. direct payment to supplier), and any material specification requirements from the insurer | Store Manager / Sales Associate | Store Manager | 15–25 min |
| 2 | **Damage-to-Material Translation & Itemized List**: Sales Associate translates insurance claim scope into BuildRight material list: (a) roofing damage → roofing sheets (specify type: GI corrugated, long-span, ribbed), ridge caps, roofing nails, waterproofing sealant, insulation; (b) flood damage → replacement electrical wiring, outlets, switches, panel board (per electrical code), wall paint, floor tiles, baseboards; (c) structural damage → cement, rebar, hollow blocks, sand, gravel, lumber, plywood, nails; (d) for each item: system identifies matching BuildRight SKU, current price, and availability; (e) quantities estimated based on damage scope per insurance adjuster report; (f) itemized material list generated per W542 (quotation) with BuildRight letterhead — suitable for insurance company review and approval | Sales Associate / System | Store Manager | 20–40 min |
| 3 | **Insurance Company Coordination & Approval**: Store Manager coordinates with insurance company (if direct billing arrangement): (a) sends itemized material list and quotation to insurance adjuster/company for approval; (b) insurance company reviews and may: (i) approve list as-is; (ii) request substitutions (e.g., lower-cost alternative materials); (iii) cap total at claim amount and customer covers difference; (c) payment arrangement confirmed: (i) insurance company issues check to BuildRight directly (direct settlement); (ii) insurance company reimburses customer, customer pays BuildRight; (iii) insurance company issues guarantee letter — BuildRight bills insurance company post-delivery; (d) approved material list finalized and linked to claim reference number in ERP | Store Manager / Sales Associate | Store Manager | 30–60 min (may span multiple interactions over 2–5 days) |
| 4 | **Material Procurement & Delivery Coordination**: Given post-disaster supply constraints: (a) system checks inventory — post-disaster demand surges may deplete local stock; (b) if local stockout: Store Manager escalates to Category Manager for emergency replenishment per W60, inter-store transfer per W22, or DC emergency dispatch per W927; (c) delivery coordination challenges: damaged roads, restricted access, curfew hours, LGU checkpoint permits — Delivery Coordinator plans route per current accessibility conditions; (d) delivery scheduled with customer's site contact (may be construction foreman, not homeowner); (e) proof of delivery documentation required for insurance claim — DR with photographs of delivered materials at site | Delivery Coordinator / Store Manager | Store Manager | 30–60 min |
| 5 | **Post-Delivery Claim Closure & Follow-Up**: After delivery: (a) Store Manager sends delivery confirmation and proof of delivery to insurance company for claim closure; (b) invoice and payment processed per agreed payment arrangement; (c) system tracks insurance claim from intake to closure with full documentation trail; (d) Store Manager follows up with customer within 2 weeks: any additional materials needed? Installation service referral per W138; (e) post-disaster recovery analysis: Category Manager reviews demand surge data to improve forward stock pre-positioning per W960 for future events | Store Manager / Category Manager | Store Manager | 15–30 min |

### System Touchpoints
- POS quotation module (W542) with insurance claim linkage
- Insurance claim tracking module — claim reference, status, documentation, payment tracking
- Real-time inventory check with emergency replenishment trigger (W60)
- Inter-store transfer and DC emergency dispatch (W22, W927)
- Delivery scheduling with disaster-area route planning (W196)
- Proof of delivery with photographic evidence capture
- Insurance company portal (for direct-billing partners) — claim submission, approval, invoicing
- Post-disaster demand analytics for supply chain planning (W960)

### Pain Points / Risks
- **Post-disaster stockout**: Demand surges of 300–500% for key materials (roofing, plywood, cement, nails) can deplete store and DC inventory within hours; emergency procurement and inter-store transfers required; Category Manager pre-positioning per W960 mitigates but cannot eliminate stockout risk; clear customer communication on availability and expected restock timeline
- **Insurance claim processing delays**: Insurance claim approval can take 2–8 weeks; customers may need emergency materials (tarpaulins, temporary roofing) before claim is approved; BuildRight offers emergency materials at cost (no margin) as goodwill gesture to claim-registered customers, with reimbursement upon claim approval
- **Fraud risk**: Post-disaster environment attracts fraudulent claims — inflated damage reports, fictitious claims; Sales Associates must verify claim documentation authenticity (insurance company direct verification, claim reference validation); suspicious claims escalated to Store Manager and LP per W837
- **Infrastructure challenges**: Post-typhoon areas may have impassable roads, downed power lines, flooded access routes; delivery trucks may be unable to reach customer sites; creative solutions: smaller vehicle relay, customer pickup at accessible transfer point, coordination with LGU disaster response for road clearance priority

### Staffing Implication
- **Store Manager**: Primary owner during post-disaster periods; claim coordination consumes 2–4 hours/day during surge periods; absorbed by existing role; support from designated Sales Associate at high-volume stores
- **Training**: 4-hour post-disaster insurance claim coordination training per W51; annual refresher aligned with typhoon season preparation per W576
- **No incremental headcount**

### Time Estimate
- Customer intake & document review: 15–25 min
- Damage-to-material translation: 20–40 min
- Insurance coordination: 30–60 min (over 2–5 days)
- Procurement & delivery coordination: 30–60 min
- Post-delivery closure: 15–30 min
- **Total of active staff time per claim**: 110–215 min (spread over 1–3 weeks)

---

## W971. Customer Power Tool Battery & Accessory Cross-Compatibility Checker & Recommendation

| Field | Detail |
|---|---|
| **Trigger** | Customer requests compatibility check for a power tool battery, blade, bit, or accessory at store or via mobile app |
| **Frequency** | ~10,000–15,000 checks/month chain-wide (~50–75/store/month) |
| **Volume** | 1–3 compatibility checks per customer visit |
| **Owner** | Department Supervisor (Tools/Hardware) |
| **Participants** | Sales Associate (Tool Specialist), Customer, Category Manager |

### Background

Power tool battery and accessory compatibility is one of the most confusing aspects of hardware retail for customers. Each major brand (DeWalt, Makita, Bosch, Milwaukee, Ryobi, Black+Decker, local brands) uses proprietary battery platforms — batteries from one brand do not fit tools from another brand, and even within a brand, different voltage series (12V, 18V/20V, 36V/40V) are incompatible. Furthermore, accessories (circular saw blades, jigsaw blades, drill bits, sanding pads, router bits) have different shank types, arbor sizes, and mounting standards that must match the specific tool model. An incorrect accessory purchase wastes customer time and money, generates returns (per W12), and damages confidence in BuildRight's advisory capability. A cross-compatibility checker — accessible in-store via Sales Associate tablet and customer-facing kiosk, and via mobile app — allows customers to input their tool model number and instantly see all compatible batteries, chargers, blades, bits, and accessories. This drives: (a) higher accessory attach rate (batteries, blades, bits are high-margin items); (b) increased customer confidence and trust; (c) reduced returns; (d) ecosystem lock-in recommendations (when a customer owns multiple tools from one brand, recommend staying within that ecosystem).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Tool Identification**: Customer identifies their power tool via: (a) tool model number — printed on tool nameplate (e.g., Makita HR2470, DeWalt DCD791); (b) tool brand and type — customer describes tool ("yellow DeWalt 20V drill"); (c) barcode/QR scan — Sales Associate scans barcode on customer's tool or battery; (d) photo — customer photographs their tool/battery and system uses image recognition to identify model (mobile app); system retrieves tool specifications: brand, model, voltage/platform, chuck size, blade/arbor type, accessory interface | Sales Associate / Customer / System | Department Supervisor | 2–5 min |
| 2 | **Compatibility Database Lookup & Results Display**: System queries BuildRight's power tool compatibility database: (a) compatible batteries — all battery SKUs that fit the identified tool, with voltage, amp-hour (Ah) rating, price, and availability; highlighted: OEM batteries (same brand) and compatible aftermarket alternatives (lower cost); (b) compatible chargers — matching charger SKUs for identified batteries; (c) compatible accessories — drill bits (by chuck size and material), saw blades (by arbor size and tooth count), sanding pads (by hook-and-loop vs. stick-on, size), router bits (by shank diameter), grinding wheels (by arbor size and material); (d) cross-sell recommendations — other tools on the same battery platform (encourages ecosystem expansion); results displayed with clear compatibility indicators: ✓ Compatible, ⚠ Adapter Required, ✗ Not Compatible | System / Sales Associate | Department Supervisor | 1–2 min (automated) |
| 3 | **Customer Selection & Advisory**: Sales Associate reviews results with customer: (a) recommends best-value battery — e.g., "For your DeWalt 20V drill, the 5.0Ah battery gives you 60% more runtime than the 2.0Ah for only 30% more cost"; (b) explains accessory specifications — e.g., "This circular saw blade has a 5/8" arbor which matches your saw, and 40 teeth is ideal for the plywood cutting you described"; (c) ecosystem advisory — if customer owns 2+ tools from one brand: "Since you have a Makita 18V drill and impact driver, this Makita 18V circular saw uses the same batteries — you'd only need to buy the bare tool at a lower price"; (d) customer selects compatible items | Sales Associate / Customer | Department Supervisor | 5–10 min |
| 4 | **Purchase & Optional Tool Registration**: Customer purchases selected items; optional: Sales Associate offers to register the customer's tool in BuildRight's warranty vault (W911) — records tool model, serial number, purchase date, and compatible accessories; registration provides: (a) warranty tracking for vendor extended warranty; (b) proactive notification when new compatible accessories are launched; (c) future quick reorder of consumable accessories (drill bits, blades) per W969; (d) loyalty points for tool registration (100 points per tool) | Sales Associate / Customer | Department Supervisor | 5 min |

### System Touchpoints
- Power tool compatibility database (maintained by Category Manager with vendor data feeds)
- Tool model search — by model number, brand/type, barcode scan, or photo recognition
- Real-time inventory and pricing for compatible items
- Product attribute master (W50) with tool and accessory specifications
- Customer tool registration in digital warranty vault (W911)
- Loyalty system for tool registration points
- Mobile app tool scanner integration
- POS for purchase and registration

### Pain Points / Risks
- **Database completeness**: The compatibility database must cover all 35,000+ tool and accessory SKUs; vendor data feeds are not always timely or complete; Category Manager must maintain manual curation for new product launches; database accuracy target: ≥98% for top 20 brands
- **Customer tool model confusion**: Customers often misidentify their tool model — confusing similar model numbers, not knowing the exact series, or misreading the nameplate; Sales Associate verification with visual reference (store tool display) mitigates; photo recognition feature reduces misidentification
- **Aftermarket battery liability**: Aftermarket (non-OEM) batteries are significantly cheaper but may void tool warranty or present safety risks (overheating, fire); system must display clear disclaimer: "This is an aftermarket battery not manufactured by [brand]. Use may void your tool warranty. BuildRight recommends OEM batteries for warranty compliance."; product liability per W185
- **Rapid product model turnover**: Power tool brands introduce new models and discontinue old ones frequently; database must be updated within 30 days of new product launch; vendor new product notification integration per W788

### Staffing Implication
- **No incremental headcount** — workflow is primarily system-driven; Sales Associate advisory role absorbed by existing Tools/Hardware department staff

### Time Estimate
- Tool identification: 2–5 min
- Compatibility lookup (automated): 1–2 min
- Customer selection & advisory: 5–10 min
- Purchase & registration: 5 min
- **Total per check**: 13–22 min of staff time

---

## W972. Customer Franchise & Dealer Mini-Store Program Management

| Field | Detail |
|---|---|
| **Trigger** | Prospective franchisee or dealer applies to open a BuildRight-branded mini-store in an underserved location |
| **Frequency** | ~30–50 new applications/year; ~150 active mini-stores under management |
| **Volume** | 1 application per evaluation; ongoing management of active franchise/dealer network |
| **Owner** | VP Store Operations |
| **Participants** | Prospective Franchisee/Dealer, VP Store Operations, Legal, Finance, Merchandising, Supply Chain, IT, HR |

### Background

The Philippine retail landscape includes thousands of small, independent hardware stores (sari-sari hardware) in rural municipalities and urban neighborhoods where big-box retail is not economically viable. BuildRight's franchise and dealer mini-store program extends the brand's reach into these underserved markets through independently owned and operated small-format stores (100–300 sqm) that carry a curated assortment of 2,000–5,000 fast-moving SKUs sourced from BuildRight's supply chain. The mini-store model benefits both parties: (a) the franchisee/dealer gains access to BuildRight's brand, merchandising expertise, centralized procurement pricing, and supply chain; (b) BuildRight extends its geographic reach without capital investment in new big-box stores, captures incremental wholesale revenue, and builds brand awareness in growth markets that may eventually support full-format stores. The program targets municipalities with populations of 20,000–100,000 that are outside the trade area of existing BuildRight big-box stores. This workflow covers the full lifecycle: application, evaluation, agreement, setup, operations support, and periodic review.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Application Intake & Initial Screening**: Prospective franchisee/dealer submits application via: (a) BuildRight website franchise inquiry form; (b) referral from existing BuildRight store manager; (c) walk-in inquiry at any BuildRight store; application includes: applicant background and business experience, proposed location (address, municipality, population, distance to nearest BuildRight store), available capital/investment range, proposed store size, and market knowledge; VP Store Operations reviews application for initial eligibility: (a) proposed location is outside 15km radius of existing BuildRight store; (b) municipality population meets minimum threshold (20,000); (c) applicant has relevant business experience or willingness to undergo training; (d) applicant has minimum investment capacity (PHP 1–3 million for dealer; PHP 3–5 million for franchise) | VP Store Operations / Applicant | VP Store Operations | 30–60 min (review) |
| 2 | **Site Evaluation & Feasibility Assessment**: VP Store Operations conducts site evaluation: (a) on-site visit — assess location visibility, accessibility, parking, building condition, signage potential; (b) market analysis — population within 5km trade area, household income levels, construction activity indicators (building permits, new subdivisions), competitor presence (independent hardware stores, lumber yards); (c) supply chain feasibility — distance from nearest BuildRight DC or hub store for replenishment delivery; delivery route viability considering road conditions and LGU access; (d) financial feasibility — projected monthly revenue based on market analysis, estimated operating costs, projected ROI for both franchisee/dealer and BuildRight; (e) go/no-go recommendation documented and presented to COO for approval | VP Store Operations / Supply Chain | VP Store Operations | 2–3 days (including site visit) |
| 3 | **Agreement Execution & Store Setup**: Upon COO approval: (a) Legal prepares Franchise Agreement or Dealer Agreement per W230 (legal contract review) — terms include: brand license, territory exclusivity, minimum purchase commitments, merchandising standards, POS system requirements, and termination clauses; (b) Finance conducts credit evaluation and sets trade credit terms per W24 (for dealer model — BuildRight extends wholesale credit); (c) Merchandising assigns curated assortment based on local market analysis: 2,000 SKUs (rural dealer) to 5,000 SKUs (urban franchise) from BuildRight's fast-moving catalog; (d) IT provisions: BuildRight-branded POS system with real-time inventory reporting, BuildRight wholesale ordering portal access, and loyalty program integration; (e) HR arranges 2-week training program for franchisee/dealer and staff at nearest BuildRight store per W51; (f) Supply Chain establishes replenishment delivery route — scheduled weekly or bi-weekly delivery from nearest DC or hub store per W196; (g) Marketing provides: BuildRight-branded signage, store layout template, opening promotional materials per W262; (h) store setup timeline: 60–90 days from agreement signing to grand opening | Legal / Finance / Merchandising / IT / HR / Supply Chain / Marketing | VP Store Operations | 60–90 days |
| 4 | **Ongoing Operations & Performance Management**: Active franchise/dealer operations management: (a) **Replenishment**: franchisee/dealer places weekly/bi-weekly wholesale orders via BuildRight ordering portal; orders fulfilled from nearest DC or hub store; delivery per W196; minimum order value enforced per agreement; (b) **Performance monitoring**: system tracks franchisee/dealer KPIs monthly — revenue, SKU velocity, inventory turnover, on-time payment, fill rate, customer satisfaction; (c) **Merchandising support**: Category Manager reviews franchisee/dealer assortment quarterly — adds fast-moving new products, removes slow movers, adjusts for seasonal demand per W264; (d) **Compliance audit**: annual on-site audit per W121 (operational audit) verifying: brand standards, pricing compliance, POS system usage, store condition, and customer experience; (e) **Training**: annual refresher training for franchisee/dealer staff per W51; new product training per W920; (f) **Quarterly business review**: VP Store Operations conducts QBR with each franchisee/dealer (or group review for dealers in same region) per W617 | VP Store Operations / Merchandising / Supply Chain | VP Store Operations | Ongoing (monthly monitoring, quarterly reviews, annual audit) |
| 5 | **Agreement Renewal, Upgrade & Termination**: Annual: (a) agreement renewal review — performance KPIs assessed; underperforming franchises/dealers placed on improvement plan; consistent performers offered territory expansion or upgrade from dealer to franchise model; (b) store upgrade — if mini-store market grows to support big-box format: franchisee offered right of first refusal for BuildRight full-format store development per W223; (c) termination — if franchisee/dealer breaches agreement terms (brand standards non-compliance, payment default, unauthorized product sourcing): Legal manages termination per W230, including brand license revocation, inventory buyback negotiation, and territory reassignment | VP Store Operations / Legal / Finance | COO | Annual review |

### System Touchpoints
- Franchise/dealer application management portal
- POS system provisioning for mini-stores (cloud-based, integrated with BuildRight ERP)
- Wholesale ordering portal (vendor portal adaptation per W865)
- Real-time inventory and sales reporting from mini-stores to BuildRight ERP
- Delivery route planning for mini-store replenishment (W196)
- KPI dashboard for franchise/dealer performance monitoring
- Compliance audit checklist and tracking (W121)
- Loyalty program integration — mini-store customers earn/redeem BuildRight loyalty points
- Financial settlement — wholesale billing, trade credit management (W24), and payment tracking

### Pain Points / Risks
- **Brand reputation risk**: Mini-store operators are independent business owners; poor store conditions, customer service, or pricing practices reflect on BuildRight's brand; stringent brand standards, regular compliance audits, and immediate corrective action requirements in the agreement mitigate; termination clause for repeated non-compliance
- **Credit risk**: Dealer model involves BuildRight extending wholesale credit; dealer default on payments creates bad debt per W81; credit evaluation at agreement execution, credit limits per W24, weekly payment monitoring, and credit insurance mitigate; dealer deposit requirement (10–20% of credit line) as security
- **Operational complexity**: Managing 150+ independently operated stores creates operational complexity — individual replenishment schedules, performance variability, and diverse local market conditions; standardized processes, system automation, and regional management structure (grouping mini-stores by hub store) reduce complexity
- **Channel conflict**: Mini-stores located near BuildRight big-box stores may cannibalize big-box sales; strict 15km minimum distance rule and differentiated assortment (mini-stores carry only fast-moving SKUs; special orders routed to big-box) prevent cannibalization

### Staffing Implication
- **Franchise/Dealer Coordinator**: 2–3 dedicated staff at HQ (reporting to VP Store Operations) managing the mini-store program; handles applications, site evaluations, compliance audits, and franchisee/dealer relationship management
- **Net new headcount**: 2–3 Franchise/Dealer Coordinators (new roles, HQ-based)

### Time Estimate
- Application review: 30–60 min
- Site evaluation: 2–3 days
- Agreement & setup: 60–90 days (cross-functional)
- Ongoing management: ~4 hours/month per active franchise/dealer
- Annual renewal: 2–4 hours per franchise/dealer

---

## W973. Employee Long Service Award & Milestone Recognition Management

| Field | Detail |
|---|---|
| **Trigger** | Employee reaches a service milestone (5, 10, 15, 20, 25 years) with BuildRight |
| **Frequency** | ~200–300 awards/year across all entities |
| **Volume** | 1 award per employee per milestone |
| **Owner** | CHRO |
| **Participants** | HR Manager, Employee, Employee's Direct Manager, HR Service Desk, Finance |

### Background

Employee retention in Philippine retail is challenging — the industry experiences 15–20% annual turnover. Long-service employees represent institutional knowledge, customer relationship capital, and operational stability that directly impact store performance and customer satisfaction. BuildRight's long service award program recognizes and rewards employees at key tenure milestones, reinforcing organizational commitment and signaling to all employees that loyalty is valued. The program includes: (a) monetary awards (increasing with tenure); (b) commemorative items (pin, plaque, certificate); (c) public recognition (store-level ceremony for 5/10 years, corporate event for 15/20/25 years); (d) additional benefits (extra leave days, enhanced HMO coverage). In the Philippine cultural context — where loyalty, respect for tenure, and family-like organizational culture are deeply valued — a well-executed long service program is a powerful retention tool and differentiator in the competitive retail labor market.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Milestone Identification & Verification**: System automatically identifies upcoming service milestones: (a) monthly batch job scans all 6,715 employee records for hire dates falling in the next 60 days that coincide with milestone years (5, 10, 15, 20, 25); (b) system generates milestone eligibility list with: employee name, entity, location, hire date, upcoming milestone, current position, and direct manager; (c) HR Service Desk verifies eligibility: (i) continuous service — no break in employment (approved leaves of absence do not break continuity); (ii) performance standing — employee is not on active PIP (performance improvement plan) or under disciplinary action per W603; (iii) rehired employees — previous tenure counted only if rehired within 12 months of separation; (d) ineligible employees flagged with reason and escalated to HR Manager for review | System / HR Service Desk | CHRO | 2–4 hours/month |
| 2 | **Award Selection & Procurement**: Per milestone tier: (a) **5-Year**: PHP 5,000 cash bonus + BuildRight engraved pin + certificate; (b) **10-Year**: PHP 15,000 cash bonus + engraved plaque + certificate + 2 extra vacation leave days per year going forward; (c) **15-Year**: PHP 30,000 cash bonus + engraved plaque + certificate + HMO upgrade (higher coverage tier) + 3 extra vacation leave days per year; (d) **20-Year**: PHP 50,000 cash bonus + gold watch or equivalent + plaque + certificate + 5 extra vacation leave days + retirement savings top-up (PHP 25,000 to retirement fund per W977); (e) **25-Year**: PHP 100,000 cash bonus + special commemorative gift + plaque + certificate + named parking spot at location (if applicable) + lifetime employee discount (post-retirement); HR Service Desk initiates: cash bonus via payroll (next payroll run per W10), plaque/gift procurement from supplier (2-week lead time), certificate printing, and benefit upgrades (HMO, leave days) in HR system | HR Service Desk / Finance | CHRO | 1–2 hours/employee |
| 3 | **Recognition Event Planning & Execution**: (a) **Store-level (5 & 10 year)**: Store Manager holds brief recognition ceremony during weekly team meeting — reads employee's accomplishments, presents award, team applause; Store Manager posts photo on internal communication platform per W716; (b) **Corporate (15, 20, 25 year)**: HR plans annual Long Service Recognition Event at HQ — invites employee + 1 guest, hosted by CHRO and CEO; formal ceremony with: video tribute (photos from tenure), CEO remarks, award presentation, and team celebration; event budget per W26; travel and accommodation provided for non-HQ employees per W815; (c) **Internal communication**: HR publishes monthly "Service Milestones" feature on company intranet and social media per W716 — employee photo, tenure, position, and brief personal story | HR / Store Manager / Executive Office | CHRO | Store-level: 30 min; Corporate: 1 day event planning |
| 4 | **Benefit Activation & Record Update**: System updates employee record: (a) additional leave days added to annual leave balance per W777; (b) HMO coverage tier upgraded per W642; (c) retirement fund top-up processed per W977; (d) milestone recorded in employee career history; (e) loyalty program enhanced — employee discount tier upgraded per W205 (employee purchase program); Finance processes cash bonus through next regular payroll per W10 — taxed per BIR table (cash awards are taxable compensation); award cost allocated to HR benefits budget per entity | HR Service Desk / Finance / System | CHRO | 15–30 min/employee |

### System Touchpoints
- HR employee master data with hire date and continuous service calculation (W292)
- Payroll system (W10) for cash bonus processing and tax withholding
- Leave management system (W777) for additional leave day credits
- HMO administration module (W642) for coverage tier upgrade
- Retirement fund management (W977) for savings top-up
- Internal communication platform (W716) for recognition posts
- HR benefits budget tracking per entity
- BI dashboard for retention analytics — milestone achievement rate by entity, store, and department

### Pain Points / Risks
- **Missed milestones**: Employees who transfer between entities (W511) may have their continuous service miscalculated if entity transfer dates are not properly tracked; HR must maintain continuous service calculation across all 5 entities regardless of transfer history
- **Cash award taxation**: Cash bonuses are taxable compensation per BIR rules; net amount after tax may be less impressive than gross amount; clear communication that gross amount is subject to withholding tax per BIR tables; some companies gross up the award to ensure net amount matches milestone tier — BuildRight evaluates gross-up policy annually
- **Equity perception**: Employees who leave and return (rehires) may feel disadvantaged if previous tenure is not counted; consistent policy application and clear communication of eligibility rules at onboarding per W15 prevent disputes
- **Cost escalation**: As the company matures (15+ years in operation), the number of 15, 20, and 25-year milestones will increase significantly; annual budget must project long-service award costs 5+ years forward; Finance includes projection in annual HR budget per W26

### Staffing Implication
- **No incremental headcount** — absorbed by existing HR Service Desk and Finance teams; estimated 4–6 hours/month for milestone management

### Time Estimate
- Milestone identification: 2–4 hours/month (batch)
- Award procurement: 1–2 hours/employee
- Recognition event: store-level 30 min, corporate event 1 day (annual)
- Benefit activation: 15–30 min/employee
- **Total per employee**: 2–3 hours of active staff time

---

## W974. Store-Level Customer Project Staged Delivery & Phased Material Release

| Field | Detail |
|---|---|
| **Trigger** | Customer purchases large project order and requests delivery in phases aligned with construction schedule |
| **Frequency** | ~2,500–3,500 staged deliveries/month chain-wide (~12–17/store/month) |
| **Volume** | 1 project with 2–5 delivery phases; average total project value PHP 100,000–500,000 |
| **Owner** | Store Manager |
| **Participants** | Customer, Sales Associate, Delivery Coordinator, Store Manager, Category Manager, Finance |

### Background

Construction projects in the Philippines follow a well-defined sequence: (1) site preparation and excavation, (2) foundation and structural work, (3) framing and roofing, (4) plumbing and electrical rough-in, (5) masonry and plastering, (6) tile and flooring, (7) doors and windows, (8) painting and finishing, (9) fixtures and accessories. Each phase requires different materials delivered at specific times. Delivering all materials at project start creates multiple problems: (a) on-site storage space is limited at Philippine residential construction sites (often just the sidewalk or a small staging area); (b) materials left on-site are exposed to theft, weather damage, and deterioration; (c) the customer's cash flow is strained by paying for materials months before they're needed; (d) damaged or lost materials reduce BuildRight's customer satisfaction. Staged delivery — releasing materials in phases aligned with the construction schedule — solves these problems and increases BuildRight's value proposition for project customers. This workflow manages the full lifecycle of staged delivery from order creation through final phase completion.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Project Order Creation & Phase Definition**: Customer places large project order (via W967 material takeoff, W965 renovation package, or direct list); Sales Associate and customer define delivery phases: (a) system presents construction phase template: Phase 1 (structural — cement, rebar, sand, gravel, hollow blocks, form lumber), Phase 2 (framing & roofing — lumber, plywood, roofing sheets, nails, hardware), Phase 3 (rough-in — pipes, fittings, wires, conduit, electrical panel), Phase 4 (masonry & tiles — cement, tiles, adhesive, grout, waterproofing), Phase 5 (finishing — paint, doors, windows, fixtures, accessories); (b) customer and Sales Associate assign items to phases based on customer's construction timeline; (c) each phase assigned estimated delivery date range (e.g., Phase 1: Jan 5–10, Phase 2: Feb 1–5); (d) system validates: inventory availability per phase, customer credit limit coverage for total order value per W24, and delivery logistics feasibility per W196 | Sales Associate / Customer | Store Manager | 20–30 min |
| 2 | **Payment Arrangement & Financial Setup**: Payment structured per project size: (a) **Full prepayment** (orders ≤ PHP 100,000): customer pays 100% at order creation; each phase delivery debits from prepayment balance; (b) **Deposit + progress billing** (orders PHP 100,000–500,000): 30% deposit at order creation + per-phase payment (each phase invoiced upon delivery confirmation); (c) **Project credit** (orders > PHP 500,000 or trade/corporate accounts): per W546 progress payment collection with milestone billing per W165; system creates: (i) master project order with total value and all line items; (ii) sub-orders per phase with phase-specific items, quantities, and values; (iii) payment schedule aligned with phase delivery dates; (iv) inventory reservation — items allocated to project but not deducted from available-to-promise until phase delivery is confirmed | Sales Associate / Finance | Store Manager | 10–15 min |
| 3 | **Phase Release Trigger & Preparation**: Customer (or customer's contractor/foreman) calls, messages, or uses BuildRight app to trigger phase release: (a) customer requests Phase N delivery by specific date; (b) Delivery Coordinator confirms: (i) phase items available in stock — if any stockout: coordinates with DC replenishment per W4 or inter-store transfer per W22; (ii) delivery date confirmed with customer's site contact; (iii) delivery vehicle and route planned per W196; (c) system generates: phase pick list for store warehouse, delivery receipt with phase-specific items, and customer invoice (for progress billing); (d) Store Associate picks and stages phase materials in designated staging area separate from regular BOPIS orders | Delivery Coordinator / Store Associate | Store Manager | 30–60 min (picking + staging) |
| 4 | **Phase Delivery Execution & Confirmation**: Delivery executed per phase: (a) delivery truck loaded with phase materials; (b) for heavy/bulky items (cement, lumber, tiles): delivery team assists with unloading at customer site; (c) customer's site representative verifies quantity and condition against delivery receipt; (d) signed delivery receipt returned; (e) system posts: (i) goods issue — inventory decremented for delivered items; (ii) revenue recognition — phase value posted to revenue; (iii) customer invoice — for progress billing, invoice sent with delivered items; (iv) remaining balance update — customer visible via app/store | Delivery Team / Customer | Store Manager | 30–90 min |
| 5 | **Phase Close-Out & Next Phase Confirmation**: Post-delivery: (a) Delivery Coordinator calls customer within 24 hours to confirm delivery satisfaction; (b) any discrepancies (short delivery, damage) resolved per W500 (transfer damage claim) or W91 (damaged goods disposition); (c) system updates project order status: Phase N completed; next phase status: upcoming; (d) reminder notification sent to customer 7 days before next estimated phase delivery date: "Your Phase [N+1] materials are scheduled for delivery around [date]. Please confirm readiness."; (e) at project completion (all phases delivered): system sends project completion notification per W914 (project completion celebration); Store Manager makes personal thank-you call; customer offered post-project services: maintenance reminders per W282, future project quotation per W542 | Delivery Coordinator / Store Manager | Store Manager | 15–20 min per phase close-out |

### System Touchpoints
- POS project order module with multi-phase delivery scheduling
- Phase template library (construction phase models for residential, commercial)
- Inventory reservation and phase-specific allocation
- Payment schedule and progress billing module (W546, W165)
- Delivery scheduling per phase (W196)
- Customer notification engine (W708) for phase reminders
- Revenue recognition per phase delivery
- Project order status tracking dashboard
- Inter-store transfer and DC replenishment integration (W4, W22)

### Pain Points / Risks
- **Phase timing uncertainty**: Construction schedules are inherently uncertain — delays due to weather (rainy season), labor availability, permit issues, and design changes are common; phase delivery dates shift frequently; flexible scheduling with 3-day delivery window per phase accommodates delays without requiring order modification
- **Inventory reservation lock**: Items reserved for future phases are held in inventory and unavailable for other customers; for long projects (6–12 months), reserved inventory ties up working capital; solution: reserve only Phase 1–2 items immediately; Phase 3+ items reserved 30 days before estimated delivery, with system monitoring DC replenishment for availability
- **Customer scope changes mid-project**: Customers frequently modify their project — adding rooms, changing tile selections, upgrading fixtures; each change requires order amendment per W792 (change order management); clear change order process with pricing impact visibility prevents margin erosion and customer disputes
- **Abandoned projects**: Some construction projects are abandoned due to budget overruns, disputes, or personal circumstances; remaining phases are cancelled; unused inventory reservations released; prepayment balance refunded per W101 minus delivered phase value; system tracks abandoned project rate for sales analytics

### Staffing Implication
- **Delivery Coordinator**: 1 per store handles staged delivery scheduling alongside regular deliveries; staged delivery coordination adds ~2–3 hours/day at 12–17 active projects per store; absorbed by existing Delivery Coordinator role (or Receiving Clerk at smaller stores)
- **No incremental headcount**

### Time Estimate
- Project order creation & phase definition: 20–30 min (one-time)
- Payment setup: 10–15 min (one-time)
- Phase release preparation: 30–60 min per phase
- Phase delivery: 30–90 min per phase (delivery team)
- Phase close-out: 15–20 min per phase
- **Total per project (all phases)**: 3–6 hours of staff time over project lifecycle

---

## W975. Customer Home Energy Audit Referral & Energy-Efficient Product Recommendation

| Field | Detail |
|---|---|
| **Trigger** | Customer inquires about energy efficiency, high electricity bills, or energy-saving products at store or via ecommerce |
| **Frequency** | ~3,000–4,000 consultations/month chain-wide (~15–20/store/month) |
| **Volume** | 1 consultation per customer; average product recommendation basket value PHP 8,000–25,000 |
| **Owner** | Category Manager (Electrical & Appliances) |
| **Participants** | Sales Associate (Electrical Specialist), Customer, Energy Audit Partner, Category Manager |

### Background

Philippine residential electricity rates are among the highest in Southeast Asia (PHP 9–12 per kWh), and energy costs represent a significant household expense. Homeowners increasingly seek ways to reduce consumption through energy-efficient lighting (LED), inverter air conditioners, solar panels, energy-efficient fans, smart power strips, and insulation. BuildRight's home energy audit referral program connects customers with: (a) basic in-store energy advisory — Sales Associate recommends specific energy-efficient products based on customer's described usage patterns; (b) professional home energy audit referral — for customers wanting a comprehensive assessment, BuildRight refers to accredited energy audit partners who conduct on-site inspection and provide a detailed report with recommended improvements; the audit report includes specific BuildRight product recommendations creating a direct pipeline from audit to sale. This workflow supports BuildRight's ESG commitment (W192, W692) by promoting energy-efficient products and positions BuildRight as a sustainability leader in the Philippine hardware retail market.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Need Identification & Quick Advisory**: Customer's energy efficiency need identified through: (a) direct inquiry — "I want to lower my electric bill"; (b) product browsing — customer looking at LED lights, inverter ACs, solar panels; (c) seasonal trigger — summer (high AC usage), electricity rate increase news; Sales Associate conducts quick energy advisory (5–10 min): (a) current lighting — how many bulbs, what type (incandescent/CFL/LED), hours of use; (b) cooling — aircon type and age, fan usage; (c) major appliances — refrigerator age, washing machine type, water heater; (d) estimated monthly electricity bill; based on quick assessment, Sales Associate provides immediate recommendations: (i) "Replacing 10 incandescent bulbs with LED will save you approximately PHP 800/month"; (ii) "An inverter AC uses 30–50% less electricity than a non-inverter — payback in 18 months" | Sales Associate | Category Manager | 10–15 min |
| 2 | **Product Recommendation & Demonstration**: Sales Associate presents specific BuildRight products: (a) LED lighting — bulb types (A19, tube, panel), wattage, lumens, color temperature, and estimated savings; live demonstration using store display showing LED vs. incandescent energy consumption; (b) Inverter air conditioners — unit sizing based on room area (0.75 HP for 10–15 sqm, 1.0 HP for 15–20 sqm, 1.5 HP for 20–30 sqm, 2.0 HP for 30–45 sqm), energy efficiency ratio (EER), and estimated monthly savings; (c) Solar panels — grid-tied solar photovoltaic (PV) systems for residential: panel wattage, inverter capacity, estimated daily generation (Philippines: 4–5 peak sun hours), ROI calculation; (d) Smart home energy management — smart plugs, energy monitors, programmable timers; (e) Insulation and weather stripping — reducing heat gain for lower AC load; each recommendation includes: product cost, estimated monthly savings, simple payback period, and available financing options per W966 | Sales Associate | Category Manager | 15–20 min |
| 3 | **Professional Energy Audit Referral** (optional): For customers wanting comprehensive assessment: (a) Sales Associate explains professional energy audit: accredited energy auditor visits customer's home, conducts room-by-room assessment, provides detailed report with prioritized recommendations and estimated savings; (b) audit fee: PHP 3,000–5,000 (BuildRight subsidizes 50% for loyalty Gold/Platinum members); (c) Sales Associate books audit appointment via BuildRight app or portal — customer selects preferred date/time; (d) Energy Audit Partner conducts audit within 7–10 days; (e) audit report delivered to customer and uploaded to customer's BuildRight account per W894 (Project Vault); (f) audit report includes BuildRight product-specific recommendations with SKUs and current prices — one-click reorder per W969 | Sales Associate / Energy Audit Partner | Category Manager | 5–10 min (referral booking) |
| 4 | **Purchase & Installation Coordination**: Customer selects recommended products: (a) for simple items (LED bulbs, smart plugs): direct purchase at POS; (b) for complex items (inverter AC, solar panels): Sales Associate coordinates installation per W138 — accredited installer handles mounting, electrical connection, and commissioning; (c) for solar PV systems: full project scope per W967 (material takeoff) including panels, inverter, mounting brackets, wiring, circuit breaker, and net metering application assistance; (d) financing: high-value energy efficiency purchases offered with credit card 0% installment per W747, partner bank green loan referral per W966, or Pag-IBIG housing improvement loan; (e) government incentive information provided — DOE energy efficiency labeling, LGU tax incentives for solar installations; (f) post-installation: Sales Associate schedules 30-day follow-up to verify customer satisfaction and energy savings per W756 | Sales Associate / Installation Partner | Category Manager | 10–15 min |

### System Touchpoints
- Energy efficiency product catalog with savings calculator module
- Professional energy audit booking and scheduling portal
- Customer Project Vault (W894) for audit report storage
- POS with energy-efficient product tagging
- Installation service scheduling (W138)
- Credit card installment integration (W747)
- Loan referral integration (W966)
- Post-sale follow-up module (W756)
- ESG reporting data — energy-efficient product sales tracked for W192 (GHG emissions) and W692 (energy efficiency monitoring)

### Pain Points / Risks
- **Savings estimate accuracy**: Estimated energy savings are projections that depend on actual customer usage patterns, electricity rates, and environmental conditions; overpromising savings leads to customer dissatisfaction; all estimates presented with disclaimer: "Estimated savings based on average household usage and current electricity rates. Actual savings may vary."
- **Energy audit partner quality**: Third-party energy auditors must maintain quality standards; partner accreditation per W600 (service contractor accreditation) with annual review; customer complaints about audit quality addressed per W795
- **Solar PV complexity**: Residential solar PV installation involves electrical work, structural mounting, LGU permits, and utility (DU/EC) net metering application; not all BuildRight installation partners are qualified for solar; dedicated solar installer network maintained separately; customer expectations for net metering timeline (3–6 months for utility processing) must be set early
- **Product knowledge depth**: Energy efficiency advising requires specialized knowledge of electrical systems, appliance specifications, and building science; Sales Associates in Electrical department receive 16-hour specialized training per W51; continuous education on new energy-efficient technologies

### Staffing Implication
- **No incremental headcount** — absorbed by existing Electrical department Sales Associates with specialized training
- **Energy Audit Partners**: Independent contractors (not BuildRight employees); 10–15 partners covering BuildRight's 200-store footprint

### Time Estimate
- Quick advisory: 10–15 min
- Product recommendation: 15–20 min
- Audit referral: 5–10 min
- Purchase coordination: 10–15 min
- **Total per consultation**: 40–60 min of staff time

---

## W976. Store-Level Customer Lumber & Plywood Grade Selection & Quality Verification

| Field | Detail |
|---|---|
| **Trigger** | Customer selects lumber, plywood, or engineered wood product and requests grade verification or assistance choosing the appropriate grade |
| **Frequency** | ~6,000–8,000 selections/month chain-wide (~30–40/store/month) |
| **Volume** | 1–10 pieces per selection; average transaction value PHP 2,000–15,000 |
| **Owner** | Department Supervisor (Lumber & Building Materials) |
| **Participants** | Sales Associate (Lumber Specialist), Customer, Receiving Clerk |

### Background

Lumber and plywood are sold in grades that determine structural suitability, appearance, and price. In the Philippine market, lumber grades include: Select (clear, minimal knots), Common #1 (small tight knots), Common #2 (larger knots, wane), and Utility (structural but with defects). Plywood grades range from A-A (both faces smooth, furniture grade) to B-B (one smooth face, one rough) to C-C (both rough, sheathing grade) to marine plywood (waterproof adhesive for exterior/structural use). Most Filipino homeowners and many small contractors are unfamiliar with grading systems and may: (a) purchase lower-grade material than required (leading to structural issues or aesthetic disappointment); (b) purchase higher-grade material than necessary (overpaying); (c) unknowingly purchase lumber that is wet (high moisture content) that will warp or shrink as it dries. BuildRight's lumber grade selection service helps customers choose the correct grade for their application, verifies quality at point of sale, and provides moisture content testing — building trust and reducing returns.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Application Assessment**: Customer describes their project: (a) application type — structural (joists, beams, rafters, framing), decorative (cabinetry, trim, moulding), exterior (decking, fencing, outdoor furniture), sheathing (wall sheathing, roof decking, subfloor), concrete formwork, or general purpose; (b) load requirements — structural members require grade verification (especially for beams and joists); (c) aesthetic expectations — visible woodwork requires higher appearance grade; (d) environment — indoor (dry), covered outdoor, exposed outdoor, wet area (bathroom, kitchen); (e) budget considerations; Sales Associate recommends appropriate grade: structural → Common #1 or better; decorative → Select or A-grade plywood; exterior → treated lumber or marine plywood; concrete formwork → C-C plywood (single use) or B-B plywood (reusable) | Sales Associate | Department Supervisor | 5–10 min |
| 2 | **Lumber Selection & Visual Quality Check**: Customer selects pieces from lumber rack; Sales Associate conducts visual quality check: (a) grade verification — checking for: knot size and frequency, splits/checks, wane (bark edge), warp/bow/twist/cup, insect damage (termite tunnels), fungal decay (blue stain, rot); (b) moisture content — Sales Associate uses pin-type moisture meter to test selected pieces: acceptable ranges: kiln-dried (12–18%), air-dried (18–25%), green (>25% — not recommended for interior use); high-moisture lumber flagged: customer informed of potential shrinkage/warping and advised to acclimate before installation; (c) dimensional verification — actual dimensions vs. nominal dimensions (e.g., "2×4" actually measures 1.5"×3.5"); Sales Associate measures critical pieces with tape measure for accuracy; (d) straightness check — sighting along the edge to verify no bow or twist beyond acceptable tolerance (≤3mm per 2.4m length) | Sales Associate | Department Supervisor | 5–10 min/piece |
| 3 | **Plywood Selection & Grade Verification**: Customer selects plywood sheets; Sales Associate verifies: (a) face grade — both faces checked against grade standard (A: smooth, no knots; B: tight knots, some repairs; C: open defects, knots); (b) core quality — edge check for voids, delamination, and core species; (c) glue bond type — interior (UREA) vs. exterior (phenolic/melamine) — verified by grade stamp or label; (d) thickness — measured with caliper at multiple points; standard tolerance ±0.5mm; (e) flatness — sheet placed flat on floor to check for warp; warped sheets replaced; (f) marine plywood — verified by branding/stamp; genuine marine plywood uses waterproof phenolic adhesive and has no core voids | Sales Associate | Department Supervisor | 5–8 min/sheet |
| 4 | **Cutting Service & Purchase**: If customer requests lumber cutting per W169: (a) Sales Associate marks cut points on selected pieces; (b) cutting executed per W169; (c) post-cut quality check — cut ends checked for splits; customer verifies cut dimensions; customer proceeds to POS: (a) grade and quality verified pieces processed at POS with grade annotation on receipt; (b) customer receives care instructions: storage (keep dry, elevated, flat for plywood), acclimation (allow 48–72 hours in installation environment for kiln-dried lumber), and treatment recommendations (termite treatment, sealant application for exterior use); (c) warranty information: lumber is a natural product — warranty covers manufacturing/grading defects only (not natural characteristics or post-purchase handling damage) | Sales Associate / Cashier | Department Supervisor | 5–10 min |

### System Touchpoints
- POS with lumber grade and species master data (W50)
- Moisture meter integration — readings recorded against SKU for quality tracking
- Product attribute master with grade specifications, typical applications, and pricing
- Lumber cutting service (W169) integration
- Customer care instruction printing at POS
- Quality feedback loop — customer quality complaints tracked against receiving batch for vendor quality per W110

### Pain Points / Risks
- **Grade inconsistency**: Lumber grading is subjective and varies between vendors and even between individual graders; what one vendor calls "Common #1" another may grade differently; BuildRight's visual quality check at step 2 provides a second verification layer; consistent vendor grading standards enforced per W669 (vendor contract compliance)
- **Moisture content disputes**: Lumber moisture content changes with storage conditions — lumber tested at 15% in the morning may read 18% by afternoon in humid Philippine climate; readings are a snapshot; Sales Associate must explain moisture variability and recommend acclimation; moisture meter calibrated monthly per manufacturer specification
- **Warp after purchase**: Lumber that was straight at point of sale may warp after customer transports and stores it; this is a natural characteristic of wood, not a BuildRight quality issue; care instructions at POS educate customer on proper storage; returns for warp are assessed case-by-case per W12
- **Termite risk in tropical climate**: Philippine lumber is highly susceptible to termite infestation; Sales Associate must recommend treatment (borate treatment, creosote, or chemical preservative) for all structural and exterior applications; treated lumber premium priced; inventory of treated lumber maintained at stores in high-termite-risk areas (most of the Philippines)

### Staffing Implication
- **Sales Associate (Lumber Specialist)**: 1 per store with lumber grading knowledge; lumber quality checks consume ~2–3 hours/day at 30–40 selections; absorbed by existing Lumber & Building Materials department staff
- **Training**: 16-hour lumber and plywood grading certification per W51; includes hands-on moisture meter training, visual grading exercises, and Philippine wood species identification (tanguile, apitong, lauan, yakal)
- **No incremental headcount**

### Time Estimate
- Application assessment: 5–10 min
- Lumber quality check: 5–10 min/piece
- Plywood verification: 5–8 min/sheet
- Cutting & purchase: 5–10 min
- **Total per transaction**: 15–35 min of staff time

---

## W977. Employee Retirement Benefit Fund (RA 7641) Administration & Processing

| Field | Detail |
|---|---|
| **Trigger** | Employee reaches retirement eligibility (per RA 7641 or company policy) or separates from employment with retirement benefit entitlement |
| **Frequency** | ~80–120 retirements/separations per year; growing as workforce ages |
| **Volume** | 1 retirement benefit computation per employee |
| **Owner** | CHRO |
| **Participants** | HR Manager, Employee, Finance, Legal, Payroll |

### Background

Republic Act 7641 (Retirement Pay Law) mandates that Philippine private sector employees who have served at least 5 years with an employer are entitled to retirement pay upon reaching age 60 (optional) or age 65 (mandatory), unless the company has a more favorable retirement plan. The minimum retirement pay is one-half month salary per year of service (where one-half month = 15 days + 5 days incentive leave + 1/12 of 13th month pay = 22.5 days per year of service). BuildRight, as a responsible Philippine employer, provides retirement benefits that meet or exceed RA 7641 requirements. BuildRight's retirement program includes: (a) RA 7641 statutory retirement pay; (b) company-funded retirement savings plan with annual contributions; (c) early retirement option (reduced benefits for employees retiring between 55–59 with 20+ years of service); and (d) post-retirement benefits (continued HMO coverage for 1 year, employee discount for life per W205). With 6,715 employees and a growing proportion approaching retirement age (especially among early-hire store managers and long-tenured HQ staff), systematic retirement benefit administration is essential for compliance, financial planning, and employee relations.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Retirement Eligibility Identification**: System identifies upcoming retirement-eligible employees: (a) monthly batch job scans employee master for: (i) employees turning 60 or 65 in next 6 months; (ii) employees with 5, 10, 15, 20, 25, 30 years of service; (iii) employees who have submitted retirement intention; (b) HR reviews eligibility list and classifies: (i) **Mandatory retirement** — employee reaching age 65; (ii) **Optional retirement** — employee age 60 with ≥5 years service (electing to retire); (iii) **Early retirement** — employee age 55+ with ≥20 years service (applying for early retirement); (iv) **Separation with retirement benefits** — employee separating (resignation, retrenchment) with ≥5 years service entitled to retirement pay proportionally; (c) HR Manager contacts eligible employees for retirement counseling: explains benefits, options, timeline, and required documents | System / HR Manager | CHRO | 4–6 hours/month |
| 2 | **Retirement Benefit Computation**: HR computes retirement benefit package: (a) **Statutory retirement pay (RA 7641)**: (i) one-half month salary per year of service = (daily rate × 22.5 days) × years of service; (ii) daily rate = monthly basic salary ÷ 26 days (or 30 days per company policy); (iii) years of service = from hire date to retirement date (inclusive of approved leaves); (b) **Company retirement savings**: accumulated company contributions + earnings (if any); (c) **13th month pay pro-rated**: for the fraction of the year worked; (d) **Unused leave monetization**: per company leave policy and W777 (leave balance management); (e) **Long service award top-up**: if retirement coincides with a service milestone per W973; (f) **Total retirement package** = statutory + company savings + 13th month + leave monetization + any applicable top-up; (g) Finance reviews computation for accuracy; tax computation: retirement pay is tax-exempt up to PHP 50,000 per year of service (per BIR rules — retirement pay from employer's private retirement plan is exempt from income tax if employee has served ≥10 years and is ≥50 years old; otherwise, excess is taxable) | HR / Finance | CHRO | 2–4 hours/employee |
| 3 | **Retirement Documentation & Approval**: HR prepares retirement documents: (a) retirement benefit computation sheet — detailed breakdown per component; (b) retirement agreement — mutual agreement between BuildRight and employee documenting: retirement date, benefit amount, payment schedule, release and waiver, post-retirement benefits; (c) BIR tax compliance documents — Certificate of Tax Exemption (if applicable), withholding tax computation for taxable portion; (d) employee reviews and signs retirement agreement; (e) HR Manager and CHRO co-approve; (f) for early retirement: COO approval required; (g) Legal reviews agreement per W230 for compliance with RA 7641 and DOLE regulations | HR / Legal / Employee | CHRO | 1–2 hours/employee |
| 4 | **Final Pay Processing & Benefit Disbursement**: Payroll processes retirement pay: (a) retirement pay computed and processed through special off-cycle payroll run per W641 (off-cycle payment processing); (b) tax-exempt portion excluded from taxable income; taxable portion (if any) withheld per BIR graduated tax table; (c) retirement pay disbursed via bank transfer to employee's account; (d) final pay (last salary, 13th month, leave monetization) processed separately per W643 (final pay computation); (e) company retirement savings fund balance transferred to employee's personal account or paid as lump sum per employee election; (f) HR deactivates employee access: system access revoked per W43 (offboarding), company IDs collected, uniforms returned per W172; (g) post-retirement benefits activated: HMO extension (1 year), employee discount for life per W205, optional continued loyalty program membership | Payroll / HR / Finance | CHRO | 2–3 hours/employee |
| 5 | **Retirement Fund Financial Planning & Reporting**: Finance manages retirement fund: (a) annual actuarial valuation — commissioned to assess BuildRight's retirement benefit liability across all 6,715 employees; (b) annual company contribution to retirement fund budgeted per W26 (annual budget) — typically 2–4% of total payroll; (c) fund investment management — retirement fund assets invested per board-approved investment policy (conservative: government securities, time deposits, high-grade corporate bonds); (d) monthly fund performance reporting to CFO; (e) annual retirement fund disclosure in financial statements per PFRS 19 (Employee Benefits) — defined benefit obligation, plan assets, and net liability; (f) quarterly report to SEC (if applicable) per W481 | Finance / CFO | CHRO | Ongoing (annual actuarial + quarterly reporting) |

### System Touchpoints
- HR employee master data with age, hire date, and service computation (W292)
- Retirement eligibility batch job (monthly)
- Payroll system (W10) with retirement pay computation module
- Tax computation module — BIR retirement pay tax exemption rules
- Final pay processing (W643)
- Employee offboarding workflow (W43)
- 13th month pay module (W644)
- Leave balance management (W777)
- Long service award integration (W973)
- Financial reporting — PFRS 19 employee benefit disclosure
- BI dashboard for workforce age profile and retirement liability projection

### Pain Points / Risks
- **Actuarial liability growth**: As BuildRight's workforce ages and grows, the retirement benefit liability increases; Finance must project liability 10+ years forward and ensure adequate funding; annual actuarial valuation is mandatory; underfunding risk mitigated by conservative investment policy and annual board review
- **Early retirement abuse**: Employees may seek early retirement to access retirement pay, then seek re-employment; BuildRight policy: rehired early retirees restart service computation from zero; minimum 12-month separation before rehire eligibility; HR monitors rehire patterns
- **Tax computation complexity**: BIR rules on retirement pay tax exemption are complex — exemption applies only if specific conditions are met (≥10 years service, ≥50 years old, retirement plan approved by BIR); incorrect tax computation exposes BuildRight to BIR penalties; Finance tax accountant (W90) reviews all retirement pay tax computations
- **Emotional sensitivity**: Retirement is an emotionally significant event; HR Manager must handle retirement counseling with sensitivity, especially for involuntary retirement (mandatory at 65); respectful communication, clear benefit explanation, and post-retirement support (HMO, discount) maintain positive employer-employee relationship and employer brand

### Staffing Implication
- **No incremental headcount** — absorbed by existing HR and Finance teams; retirement processing estimated at 4–6 hours/month for eligibility monitoring + 2–4 hours per retiring employee

### Time Estimate
- Eligibility identification: 4–6 hours/month (batch)
- Benefit computation: 2–4 hours/employee
- Documentation & approval: 1–2 hours/employee
- Final pay processing: 2–3 hours/employee
- Financial planning: ongoing (annual actuarial + quarterly reporting)
- **Total per retiring employee**: 6–11 hours of staff time

---

## W978. Vendor Seasonal Product Post-Season Performance Review & Assortment Rationalization

| Field | Detail |
|---|---|
| **Trigger** | End of seasonal selling period (post-Christmas, post-summer, post-rainy season) |
| **Frequency** | 3–4 reviews/year (post each major Philippine season) |
| **Volume** | ~500–800 seasonal SKUs reviewed per season |
| **Owner** | VP Merchandising |
| **Participants** | Category Managers, Buyers, Pricing Analysts, Merchandise Planners, Vendors, Supply Chain Planning, Finance |

### Background

Seasonal merchandise — Christmas decorations, garden/outdoor products, rainy season items (tarpaulins, waterproofing, flood control), summer items (aircons, fans, water tanks) — follows a predictable sales curve: buildup, peak, and sharp decline. The key challenge in seasonal retail is maximizing sales during the peak while minimizing residual inventory that must be cleared at significant markdowns (often 50–70% off) or written off entirely. Philippine seasonal patterns are particularly pronounced: Christmas spending (September–December "ber months") accounts for a disproportionate share of annual retail sales, while typhoon season (June–November) creates unpredictable demand surges for emergency supplies. Post-season performance review is a structured analytical process that evaluates every seasonal SKU's actual performance against plan, identifies root causes of over/underperformance, captures learnings for future seasons, and makes assortment decisions (continue, discontinue, modify) for the next season's buy. This workflow closes the loop between seasonal buy planning (W32) and actual results, driving continuous improvement in seasonal merchandising effectiveness.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Season Close-Out Data Compilation**: Within 2 weeks of season end: (a) Merchandise Planner compiles post-season data pack per category: (i) **Sales performance**: actual vs. plan sales units, revenue, and margin per SKU; (ii) **Sell-through rate**: percentage of purchased quantity sold at full price vs. markdown; (iii) **Inventory position**: remaining units, value, and aging; (iv) **Pricing effectiveness**: number and depth of markdowns taken per W93; (v) **Timeline adherence**: first receipt date vs. plan, in-store date vs. plan, markdown initiation date vs. plan; (vi) **Vendor performance**: fill rate, on-time delivery, quality complaints per W44; (vii) **Store-level performance**: sales by store cluster (high-performing vs. underperforming stores); (viii) **Channel performance**: in-store vs. ecommerce seasonal sales mix | Merchandise Planner | VP Merchandising | 8–12 hours/season |
| 2 | **SKU-Level Performance Classification**: Category Managers classify each seasonal SKU into performance tiers: (a) **Tier 1 — Winners** (top 20%): sold ≥90% of plan at full price or minimal markdown; high margin; customer demand exceeded supply; action: increase buy quantity 15–25% for next season, explore line extensions; (b) **Tier 2 — Solid Performers** (next 30%): sold 70–89% of plan; acceptable markdown depth (≤20%); action: maintain or slightly adjust buy quantity; review pricing and timing; (c) **Tier 3 — Underperformers** (next 30%): sold 50–69% of plan; significant markdown (20–40%); action: reduce or eliminate from next season's assortment; review root cause (wrong product, wrong price, wrong timing, poor display); (d) **Tier 4 — Losers** (bottom 20%): sold <50% of plan; deep markdown (40–70%+); or total dead stock; action: discontinue; return to vendor per W88 if agreement allows; donate per W444 if unsellable; root cause analysis mandatory | Category Manager | VP Merchandising | 4–6 hours/category |
| 3 | **Vendor Performance Review & Negotiation**: For each seasonal vendor: (a) Category Manager evaluates: (i) fill rate — did vendor deliver full ordered quantity on time?; (ii) quality — were there customer returns or complaints due to product quality?; (iii) markdown support — did vendor contribute to markdown costs per W161 (vendor price protection)?; (iv) marketing support — did vendor fund promotional activities per W513?; (b) underperforming vendors: Category Manager initiates discussion — performance improvement plan, markdown cost recovery per W245, or vendor replacement; (c) top-performing vendors: Category Manager negotiates improved terms for next season — volume discounts, earlier delivery, markdown protection, exclusive products; (d) new vendor scouting: Category Manager identifies gaps in seasonal assortment and sources new vendors per W36 (vendor onboarding) to fill gaps | Category Manager / Buyer | VP Merchandising | 2–3 hours/vendor |
| 4 | **Residual Inventory Disposition**: For remaining seasonal inventory: (a) **Markdown acceleration** (within 30 days of season end): progressive markdown schedule — Week 1: 30% off, Week 2: 50% off, Week 3: 70% off; per W93 markdown pricing execution; (b) **Vendor return**: negotiate seasonal buy-back per W901 (vendor seasonal buy-back) for vendors with return agreements; (c) **Store-to-store redistribution**: transfer remaining stock from low-demand stores to stores with continued demand per W204; (d) **Ecommerce clearance**: list remaining inventory on BuildRight website/app with clearance pricing and on marketplace channels (Lazada/Shopee) per W180; (e) **Donation**: unsold items after all disposition channels exhausted → donated to community organizations per W444 (community donation) for tax deduction and ESG reporting per W194; (f) **Write-off**: items with no disposition channel → write-off per W220 (SLOB provisioning) with accounting entry | Category Manager / Finance / Store Operations | VP Merchandising | 1–2 weeks post-season |
| 5 | **Season Retrospective & Next Season Planning Input**: VP Merchandising conducts seasonal retrospective meeting: (a) cross-functional attendees: Category Managers, Buyers, Supply Chain Planning, Store Operations, Marketing, Finance; (b) review: (i) total seasonal revenue vs. plan; (ii) gross margin performance; (iii) inventory turns; (iv) markdown rate as % of seasonal revenue; (v) top 10 winners and losers with root cause; (vi) vendor performance summary; (vii) store execution — seasonal display setup compliance per W262, promotional execution per W13; (c) capture learnings in seasonal knowledge base — documented insights for next season's planning per W32 (seasonal buy planning); (d) initiate next season's buy planning with adjusted parameters; (e) Finance incorporates seasonal margin impact into annual budget and forecast per W639 (rolling forecast) | VP Merchandising / Cross-functional | VP Merchandising | Half-day meeting + documentation |

### System Touchpoints
- BI seasonal performance dashboard — SKU-level sales, margin, sell-through, and inventory
- Markdown pricing execution module (W93)
- Vendor performance scorecard (W44)
- Seasonal inventory disposition tracking
- Inter-store transfer module (W204) for redistribution
- Ecommerce clearance listing module
- Vendor return processing (W88, W901)
- Seasonal buy planning module (W32) for next season parameters
- Financial reporting — seasonal margin analysis, markdown cost tracking, write-off entries
- Seasonal knowledge base (document management per W255)

### Pain Points / Risks
- **Data timeliness**: Post-season analysis requires complete data (all markdown sales, returns, and final inventory counts); delays in store-level data submission (especially from remote stores with connectivity issues per W535) slow analysis; system enforces data submission deadline within 5 business days of season end
- **Vendor relationship strain**: Negative performance reviews and markdown cost recovery demands can strain vendor relationships; Category Manager must balance accountability with partnership — focusing on constructive improvement plans rather than punitive measures; long-term vendor relationships are more valuable than one-season cost recovery
- **Assortment inertia**: There is a tendency to repeat last season's assortment with minor adjustments rather than making bold changes; underperforming SKUs may persist due to buyer familiarity or vendor influence; objective data-driven tier classification (step 2) forces evidence-based decisions; Merchandise Planner provides independent analysis to counter buyer bias
- **Seasonal calendar shift**: Philippine seasonal patterns are shifting — typhoon season is extending, summer heat is intensifying, and Christmas buying patterns are changing; historical performance data may not predict future demand; Merchandise Planner incorporates climate trend data and macroeconomic indicators into next season's planning

### Staffing Implication
- **No incremental headcount** — absorbed by existing Merchandising team (Category Managers, Buyers, Merchandise Planners, Pricing Analysts); post-season review consumes ~40–60 person-hours per season across the team

### Time Estimate
- Data compilation: 8–12 hours/season
- SKU classification: 4–6 hours/category (5 categories = 20–30 hours)
- Vendor review: 2–3 hours/vendor (10–15 vendors = 20–45 hours)
- Inventory disposition: 1–2 weeks
- Retrospective meeting: half-day
- **Total per season**: 80–120 person-hours across the Merchandising team

---

## W979. Customer B2B Blanket Purchase Agreement & Scheduled Call-Off Management

| Field | Detail |
|---|---|
| **Trigger** | B2B customer (contractor, developer, institution) requests a blanket purchase agreement for recurring material orders over a defined period |
| **Frequency** | ~100–150 new agreements/year; ~300–400 active agreements under management at any time |
| **Volume** | 1 agreement per customer; average annual agreement value PHP 1M–20M |
| **Owner** | VP Store Operations |
| **Participants** | Customer (B2B), Store Manager, Category Manager, Finance, Legal, Supply Chain |

### Background

Large B2B customers — construction contractors, property developers, government agencies, and institutional buyers — often require materials delivered in scheduled increments over months or years rather than as single purchases. A blanket purchase agreement (BPA) is a framework contract that establishes: pre-negotiated pricing for specific items, a total estimated quantity/value, a validity period (typically 6–12 months), delivery terms, and payment terms. The customer then "calls off" (releases) quantities against the agreement as needed — weekly, bi-weekly, or monthly — without renegotiating pricing or terms each time. This arrangement benefits both parties: (a) the customer locks in prices (protection from inflation — Philippine construction material prices increase 5–10% annually), secures supply availability, and simplifies procurement; (b) BuildRight secures predictable revenue, reduces sales cycle time for repeat orders, and improves demand forecasting accuracy per W31. BPAs are a critical tool for capturing BuildRight's B2B segment (40% of revenue — trade 30% + corporate 10%).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Negotiation & Agreement Terms**: Customer and BuildRight negotiate BPA terms: (a) **Product list**: specific SKUs with agreed pricing — fixed price (for the agreement period) or price formula (e.g., "cost + 8% margin" with quarterly price review); (b) **Estimated annual quantity/value**: total commitment (not binding minimum, but forecast for supply chain planning per W31); (c) **Validity period**: 6, 12, or 18 months with renewal option; (d) **Call-off mechanism**: how customer places release orders — email, phone, BuildRight portal (W936 B2B self-service), or EDI/cXML integration per W283 (punchout); (e) **Delivery terms**: scheduled delivery days, delivery locations (single site, multiple sites), unloading requirements; (f) **Payment terms**: monthly billing with net 30/60 per W24, or milestone-based per W165; credit limit per W328; (g) **Volume rebate**: tiered rebate if annual purchase exceeds threshold — per W27 (vendor rebate, mirrored for customer rebate); (h) **Price protection**: if BuildRight offers lower prices during agreement period, customer receives the lower price; if market prices increase, customer retains agreement price | Store Manager / Category Manager / Customer | VP Store Operations | 2–4 hours (may span multiple meetings) |
| 2 | **Agreement Documentation & System Setup**: Upon agreement: (a) Legal reviews BPA contract per W230 (legal contract review) — ensures terms comply with Philippine contract law, BuildRight's standard trading terms, and any regulatory requirements (government procurement per W78 if applicable); (b) Finance reviews credit terms and sets credit limit per W24 (trade credit) and W328 (credit limit review); (c) system setup: (i) BPA header created in ERP — customer, validity period, payment terms, delivery terms; (ii) BPA line items — each SKU with agreed price, estimated annual quantity, and call-off unit of measure; (iii) BPA linked to customer account for automatic price application at call-off; (iv) demand planning feed — BPA estimated quantities fed to supply chain planning per W31 for procurement and inventory positioning; (v) BPA available via customer portal (W936) for self-service call-off; (d) Store Manager (or designated account manager) conducts onboarding meeting with customer's procurement team: system access, ordering process, delivery coordination contacts, and escalation matrix | Legal / Finance / System Admin / Store Manager | VP Store Operations | 4–8 hours |
| 3 | **Scheduled Call-Off Processing**: Customer places call-off (release) orders: (a) **Scheduled auto-release**: for standing weekly/monthly orders — system automatically generates release order per agreed schedule; customer receives advance notification 48 hours before release for confirmation or modification; (b) **On-demand release**: customer places order via portal (W936), email, phone, or in-store; system validates: (i) BPA validity — agreement not expired; (ii) price — applies BPA negotiated price; (iii) credit limit — customer's outstanding AR + new release does not exceed credit limit per W888 (credit hold); (iv) inventory availability — if stockout, system alerts customer with estimated replenishment date or alternative pickup location; (c) release order created: references BPA number, applies agreed pricing, and routes to fulfillment — store pickup (W11), delivery (W19/W980), or DC dispatch (W106); (d) system updates BPA quantities: cumulative call-off vs. estimated annual quantity tracked | System / Customer / Store Manager | VP Store Operations | 5–10 min per call-off |
| 4 | **BPA Performance Monitoring & Quarterly Review**: Ongoing: (a) system tracks BPA performance: cumulative call-off value vs. estimated, call-off frequency, fill rate, delivery on-time performance, and customer complaints; (b) monthly: Finance invoices customer for all deliveries in the billing period with consolidated BPA statement; customer receives single invoice per month regardless of number of call-offs; (c) quarterly: Store Manager and Category Manager conduct business review with customer per W617 (B2B customer success) — discuss: (i) call-off pace vs. estimate — is customer buying more or less than planned?; (ii) product satisfaction — any quality issues?; (iii) delivery performance — on-time and complete?; (iv) upcoming project changes — will demand increase/decrease?; (v) volume rebate progress — is customer on track for rebate tier?; (d) annual: BPA renewal negotiation — price adjustment for next period based on market conditions, volume commitments, and competitive landscape | Store Manager / Category Manager / Finance | VP Store Operations | 2–4 hours/quarter per BPA |

### System Touchpoints
- BPA module in ERP — agreement header, line items, pricing, validity, and terms
- Customer B2B portal (W936) for self-service call-off
- EDI/cXML integration (W283) for automated B2B ordering
- Credit limit management (W24, W328, W888)
- Demand planning feed (W31) from BPA estimated quantities
- Fulfillment routing (W536) — store pickup, delivery, DC dispatch
- Consolidated monthly billing and invoicing
- BPA performance dashboard — cumulative value, call-off frequency, fill rate
- Volume rebate tracking (W27) — customer tier threshold monitoring
- Legal contract management (W230)
- BI analytics — BPA revenue, margin, and customer lifetime value

### Pain Points / Risks
- **Price escalation during agreement**: If BuildRight's cost increases significantly during the BPA period (e.g., cement price surge), the fixed-price BPA may become unprofitable; price formula terms (cost + fixed margin) protect BuildRight's margin; quarterly price review clause in agreements longer than 6 months allows adjustment with 30-day notice
- **Under-utilization**: Customer commits to an estimated annual quantity but actual call-offs are significantly lower — leaving BuildRight with excess inventory planned for the BPA; solution: BPA estimates are non-binding forecasts (not take-or-pay); supply chain planning uses BPA estimates as demand signals with safety stock buffers; significant under-utilization (>30% below estimate) triggers customer discussion at quarterly review
- **Credit risk on large BPAs**: A single BPA may represent PHP 5–20M annual spend; customer default on a large BPA creates significant AR exposure; credit limit per W328 caps total exposure; credit insurance considered for BPAs exceeding PHP 10M; Finance monitors AR aging per W889 for BPA customers weekly
- **System complexity**: Managing 300–400 active BPAs with different terms, pricing, and schedules requires robust ERP BPA module; manual workarounds increase error risk; IT ensures BPA module handles: automatic pricing, credit check, scheduled releases, consolidated billing, and performance tracking

### Staffing Impiction
- **No incremental headcount** — BPA management absorbed by existing Store Managers, Category Managers, and Finance team; estimated 4–6 hours/month per active BPA for call-off processing and relationship management

### Time Estimate
- Negotiation & setup: 6–12 hours (one-time per BPA)
- Call-off processing: 5–10 min per call-off (mostly automated)
- Quarterly review: 2–4 hours per BPA
- Annual renewal: 2–4 hours per BPA
- **Ongoing**: ~1 hour/week per active BPA of staff time

---

## W980. Store-Level Customer Construction Site Delivery Scheduling & Multi-Drop Coordination (B2B)

| Field | Detail |
|---|---|
| **Trigger** | B2B customer orders materials for delivery to an active construction site with scheduling and multi-drop requirements |
| **Frequency** | ~4,000–6,000 site deliveries/month chain-wide (~20–30/store/month) |
| **Volume** | 1–4 delivery drops per site per order; average order value PHP 15,000–100,000 |
| **Owner** | Store Manager |
| **Participants** | Customer/Foreman, Delivery Coordinator, Driver, Category Manager, 3PL Partner |

### Background

Construction site delivery is fundamentally different from residential home delivery. Construction sites are dynamic, often chaotic environments with: (a) limited access — narrow roads, temporary gates, no loading dock; (b) time pressure — materials needed by specific work crews on specific days to maintain construction schedule; (c) multiple delivery points within a single site — structural materials to the foundation area, plumbing materials to the rough-in area, tiles to the finishing area; (d) site contact complexity — the person ordering (project manager) is often different from the person receiving (foreman); (e) security concerns — materials left unattended at construction sites are theft targets. BuildRight's construction site delivery coordination service manages these complexities, ensuring materials arrive at the right time, at the right location on site, to the right person, with proper documentation. This service is a key differentiator for BuildRight's B2B trade segment and directly impacts customer satisfaction and retention.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Site Delivery Order Creation & Site Information**: Customer (project manager or procurement officer) places site delivery order: (a) order source: BPA call-off per W979, project order per W162, or ad-hoc purchase; (b) site information recorded: (i) site address with landmark description; (ii) site contact name and mobile number (foreman or site engineer — different from ordering contact); (iii) site access instructions — gate location, vehicle size limit, delivery window (construction sites may restrict delivery to specific hours to avoid disrupting concrete pouring or crane operations); (iv) staging area — where on site to unload (GPS pin drop or photo reference); (v) site safety requirements — hard hat, safety vest, closed-toe shoes mandatory for delivery personnel per W187; (c) delivery schedule: (i) single drop — all items delivered at once; (ii) multi-drop — items split into multiple deliveries aligned with construction phases per W974; (iii) scheduled recurring — weekly standing delivery per BPA per W979 | Sales Associate / Customer | Store Manager | 10–15 min |
| 2 | **Delivery Route Planning & Vehicle Assignment**: Delivery Coordinator plans logistics: (a) for BuildRight own fleet (20% of deliveries): assigns vehicle from store's allocated truck; (b) for 3PL partners (80%): selects partner based on vehicle availability, cost, and site location; vehicle type matched to site access: 10-wheeler (for bulk cement, lumber, structural steel — requires wide road access), 6-wheeler (standard for most deliveries), forward truck/van (for small/medium orders to sites with narrow access), motorcycle/sidecar (for urgent small-item deliveries); (c) route optimization: if multiple site deliveries scheduled for same day, system optimizes route sequence per W196 (route optimization) considering: (i) LGU truck ban hours per W431, (ii) site delivery window preferences, (iii) traffic patterns (Metro Manila traffic, provincial road conditions), (iv) vehicle capacity utilization — maximize truck fill rate; (d) system generates: delivery manifest (all orders on the route), delivery sequence with estimated arrival times, and driver navigation instructions (GPS coordinates + landmark descriptions for Philippine addresses) | Delivery Coordinator / System | Store Manager | 15–30 min |
| 3 | **Pre-Delivery Confirmation & Site Readiness**: Day before delivery: (a) Delivery Coordinator (or automated system) sends SMS/call to site contact: confirming delivery date, estimated arrival time, and items to be delivered; (b) site contact confirms: (i) site will be ready to receive — crew available to unload, staging area cleared; (ii) access conditions unchanged — no road closures, no new obstacles; (c) if site not ready: Delivery Coordinator reschedules within 24–48 hours; (d) driver receives: delivery manifest, navigation instructions, site contact information, and special instructions (e.g., "Ask for foreman Mang Tony, mobile 0917-XXX-XXXX. Gate code: 1234. Unload near the blue tarp on the east side.") | Delivery Coordinator / Driver / Site Contact | Store Manager | 10–15 min |
| 4 | **On-Site Delivery Execution & Documentation**: Driver arrives at construction site: (a) dons required PPE per W187 (hard hat, safety vest) before entering site; (b) meets site contact and verifies delivery details; (c) unloading: (i) materials carefully unloaded at designated staging area; (ii) heavy items (cement bags, lumber bundles) placed on elevated surface (pallets, blocks) to prevent moisture absorption from ground; (iii) fragile items (tiles, glass, fixtures) handled with care; (d) site contact counts and verifies each item against delivery receipt; (e) any discrepancies noted on DR: short delivery, damaged items, wrong items; (f) site contact signs DR; (g) driver photographs: (i) delivered materials at staging area, (ii) signed DR; photographs uploaded to system via driver mobile app as proof of delivery; (h) for multi-drop orders: driver confirms next drop details with Delivery Coordinator | Driver / Site Contact | Delivery Coordinator | 30–90 min per drop |
| 5 | **Post-Delivery Reconciliation & Issue Resolution**: Delivery Coordinator reconciles: (a) signed DR vs. delivery manifest — all items accounted for; (b) any discrepancies flagged: (i) short delivery → system creates backorder or credit note per W101; (ii) damage during transit → claim per W500 (in-transit damage); (iii) wrong item → exchange arranged per W12; (c) delivery confirmation posted in ERP: (i) goods issue for delivered items; (ii) revenue recognition; (iii) customer invoice generated (or monthly consolidated per BPA W979); (iv) delivery cost recorded for freight bill tracking per W277; (d) system logs delivery performance metrics: on-time delivery rate, damage rate, customer satisfaction (from post-delivery SMS survey) | Delivery Coordinator / Finance | Store Manager | 10–15 min |

### System Touchpoints
- Site delivery order module with site information fields (address, contact, access, staging, safety)
- Delivery scheduling and route optimization (W196)
- 3PL partner dispatch and tracking integration
- Driver mobile app with delivery manifest, GPS navigation, and proof-of-delivery photo capture
- Pre-delivery SMS/call notification engine (W708)
- Delivery receipt generation and electronic signature capture
- Post-delivery reconciliation module
- Customer invoice generation (single or consolidated per BPA)
- Delivery performance analytics dashboard
- PPE compliance tracking per W187

### Pain Points / Risks
- **Site access failures**: Construction sites frequently have access issues — locked gates, no one to receive, crane occupying the unloading area, or newly constructed walls blocking the planned route; pre-delivery confirmation (step 3) reduces failures; driver empowered to contact Delivery Coordinator for real-time problem-solving; failed delivery rescheduled within 24 hours
- **Multi-drop complexity**: Coordinating multiple drops across different sites in one route increases the probability of at least one failure; buffer time between drops (30 min); real-time route adjustment via driver app; backup plan for at least one failed drop per route
- **Theft risk at construction sites**: Delivered materials left at construction sites are vulnerable to theft, especially overnight; Delivery Coordinator advises customer to have secure storage or crew member on-site to receive; BuildRight liability ends at delivery confirmation (signed DR); subsequent loss is customer's responsibility
- **Safety liability**: Construction sites are hazardous environments; delivery personnel entering sites face injury risk from falling objects, open excavations, and heavy equipment; mandatory PPE per W187, driver safety briefing at dispatch, and BuildRight liability insurance per W863 (third-party liability) protect against claims; drivers instructed to refuse entry to unsafe sites and escalate to Delivery Coordinator

### Staffing Implication
- **Delivery Coordinator**: 1 per store handles site delivery scheduling alongside regular deliveries; site delivery coordination consumes ~3–4 hours/day at 20–30 deliveries; absorbed by existing Delivery Coordinator or Receiving Clerk role
- **No incremental headcount**

### Time Estimate
- Order creation & site info: 10–15 min
- Route planning & vehicle assignment: 15–30 min
- Pre-delivery confirmation: 10–15 min
- On-site delivery: 30–90 min per drop
- Post-delivery reconciliation: 10–15 min
- **Total per delivery of BuildRight staff time**: 45–75 min (excluding driver time)

---

## W981. Customer Paint Color Matching from Physical Sample & Digital Photo

| Field | Detail |
|---|---|
| **Trigger** | Customer presents a physical color sample (paint chip, fabric swatch, tile piece, wall scrape) or digital photo for paint color matching |
| **Frequency** | ~8,000–12,000 color matches/month chain-wide (~40–60/store/month) |
| **Volume** | 1–3 color matches per customer visit; average paint purchase 2–4 gallons |
| **Owner** | Department Supervisor (Paint & Finishes) |
| **Participants** | Sales Associate (Paint Specialist), Customer, Category Manager |

### Background

Color matching is the paint department's most technically demanding and highest-value service. Customers frequently need to: (a) match an existing wall color for touch-up or extension; (b) match a specific color from a fabric, tile, or décor element for a coordinated design; (c) replicate a color seen in a magazine, social media post, or friend's home (via photo); (d) match a discontinued paint brand or product; (e) replicate a color from another paint brand's swatch at a BuildRight-comparable price. While BuildRight already offers custom paint mixing per W168 (Custom Paint Mixing & Tinting Operations), this workflow specifically addresses the color matching input — how the customer's physical sample or digital photo is translated into a precise tint formula. Accurate color matching requires: spectrophotometer hardware (color measurement device), color formulation software, and experienced Paint Specialists who understand color theory, substrate effects, and lighting conditions. In the Philippine market, where many homes have existing paint from multiple brands and decades of layers, color matching is essential for renovation projects.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Sample Assessment & Preparation**: Customer presents color sample: (a) physical samples: (i) paint chip (ideal — flat, opaque, ≥2cm × 2cm); (ii) wall scrape (drywall/plaster with paint layer); (iii) fabric swatch (textured — may affect reading); (iv) tile piece, laminate chip, or plastic item; (v) dried paint sample on paper/cardboard; (vi) existing object (ceramic vase, pillow cover, etc.); (b) digital samples: (i) customer's smartphone photo — taken in store or shown from gallery; (ii) screenshot from social media, magazine, or design website; (iii) brand-specific color code (if customer knows it — e.g., "Dulux Whisper White", "Boysen Laguna Blue"); Paint Specialist assesses sample quality: (i) physical sample: clean, flat, opaque, ≥2cm × 2cm — ideal for spectrophotometer; textured or glossy samples require manual adjustment; (ii) digital photo: lighting conditions matter — photos taken under warm indoor lighting will read differently from actual color; Paint Specialist advises customer that digital photo matching is approximate (±2 ΔE color difference) vs. physical sample matching (±0.5 ΔE) | Sales Associate (Paint Specialist) | Department Supervisor | 3–5 min |
| 2 | **Spectrophotometer Measurement & Formula Generation**: For physical samples: (a) Paint Specialist calibrates spectrophotometer using white and black calibration tiles (daily calibration at store opening per equipment SOP); (b) places physical sample on spectrophotometer reading surface; (c) takes 3 readings from different areas of sample (to average out surface variations); (d) spectrophotometer measures: L* (lightness), a* (red-green), b* (yellow-blue) values in CIELAB color space; (e) color formulation software matches measured L*a*b* values against: (i) BuildRight's tint database — 10,000+ color formulations across BuildRight paint bases; (ii) competitor brand color libraries — cross-reference charts for major Philippine paint brands (Boysen, Davies, Welcoat, Coat Saver, Dutch Boy) and international brands (Dulux, Nippon Paint, Jotun); (f) software generates: (i) closest BuildRight color match with ΔE value (color difference — ΔE < 1.0 is imperceptible, 1.0–2.0 is barely noticeable, >2.0 is visible); (ii) tint formula — specific volumes of each colorant (tint) to add to selected paint base; (iii) recommended paint base — white base (for light colors), pastel base, mid-tone base, deep base, or clear base (for very dark/vivid colors) | Sales Associate (Paint Specialist) | Department Supervisor | 5–8 min |
| 3 | **Digital Photo Matching** (for photo/screenshot samples): (a) customer places phone/device on color viewing station — a standardized D65 daylight viewing booth that provides consistent illumination; (b) Paint Specialist visually compares photo color against BuildRight color fan deck (physical swatch book with 2,000+ colors); (c) identifies 2–3 closest colors from fan deck; (d) for more precision: Paint Specialist uses BuildRight mobile app's color matching feature — customer photographs sample under the viewing booth's D65 light; app analyzes color and suggests closest BuildRight color (uses same color formulation database as spectrophotometer but via phone camera — accuracy ±2 ΔE vs. ±0.5 ΔE for spectrophotometer); (e) Paint Specialist presents 2–3 options to customer for visual comparison; customer selects closest match | Sales Associate (Paint Specialist) | Department Supervisor | 5–10 min |
| 4 | **Sample Mixing & Customer Approval**: Before mixing full quantity: (a) Paint Specialist mixes a small sample (50ml) using the generated formula per W168 (custom paint mixing); (b) applies sample to a test card (white cardboard) using mini roller (to simulate actual application method); (c) allows to dry — paint color changes as it dries (wet paint appears darker); drying time: 10–15 minutes with quick-dry additive or 30 minutes standard; (d) customer compares dried sample against original color sample under D65 daylight lamp; (e) if customer approves: proceed to full quantity mixing per W168; (f) if customer requests adjustment: Paint Specialist adjusts formula (lighter/darker, warmer/cooler, more/less saturated) based on customer feedback and re-mixes sample; typically 1–2 adjustment cycles; (g) final approved formula saved to BuildRight color database and linked to customer's loyalty account for future reorder per W969; formula printed on paint can label with: color code, formula, date, store, and customer name | Sales Associate (Paint Specialist) | Department Supervisor | 15–25 min (including drying time) |
| 5 | **Full Quantity Mixing & Purchase**: Customer-approved formula mixed to full quantity per W168; Paint Specialist: (a) adds recommended accessories to cart: roller, tray, brush, painter's tape, drop cloth, primer (if needed), sandpaper; (b) provides application guidance: recommended number of coats (typically 2), drying time between coats (2–4 hours), surface preparation requirements; (c) for large projects: offers quantity calculator — room wall area ÷ coverage per gallon (typically 30–40 sqm per gallon per coat × number of coats); (d) customer pays at POS; paint formula saved to customer account per W898 (custom paint formula save/recall/reorder) | Sales Associate / Cashier | Department Supervisor | 5–10 min |

### System Touchpoints
- Spectrophotometer hardware integration with color formulation software
- Color formulation database — 10,000+ formulas with competitor brand cross-reference
- BuildRight mobile app color matching feature (camera-based)
- POS integration with paint mixing system per W168
- Customer loyalty account integration for formula saving per W898
- Color fan deck management (physical inventory of color swatch books)
- Quick reorder from saved formula per W969
- Paint quantity calculator (room area → gallons needed)

### Pain Points / Risks
- **Color metamerism**: Colors that match under one light source (store fluorescent) may appear different under another (home LED, sunlight, incandescent); D65 daylight viewing booth simulates natural daylight for matching; Paint Specialist must warn customer that perceived color may differ slightly under their home lighting; test sample viewed under multiple light sources when possible
- **Digital photo inaccuracy**: Smartphone cameras introduce color cast, white balance errors, and compression artifacts; photos edited with Instagram/filters are especially problematic; Paint Specialist must set customer expectations: "Digital matching is a close approximation. For exact matching, a physical sample is recommended."; ΔE tolerance for digital matching is ±2 vs. ±0.5 for spectrophotometer
- **Substrate color effect**: Paint color appears different on different substrates — the same paint on new drywall, previously painted dark wall, bare concrete, or wood will look different; Paint Specialist recommends appropriate primer per substrate; test sample applied to similar substrate when possible
- **Spectrophotometer calibration drift**: Daily calibration is essential; uncalibrated spectrophotometer produces incorrect readings; Paint Specialist performs calibration at store opening and logs in equipment register per W650; annual professional recalibration by manufacturer

### Staffing Implication
- **Sales Associate (Paint Specialist)**: Color matching consumes ~3–4 hours/day at 40–60 matches; absorbed by existing Paint department Sales Associate with specialized color matching training
- **Training**: 24-hour color theory and spectrophotometer operation certification per W51; includes hands-on matching exercises, color adjustment techniques, and competitor brand color library familiarization
- **No incremental headcount**

### Time Estimate
- Sample assessment: 3–5 min
- Spectrophotometer measurement: 5–8 min
- Digital matching: 5–10 min
- Sample mixing & approval: 15–25 min (including drying)
- Full mixing & purchase: 5–10 min
- **Total per match**: 33–58 min of staff time

---

## W982. Customer Electrical Load Calculation & Wire Size Recommendation Service

| Field | Detail |
|---|---|
| **Trigger** | Customer requests assistance with electrical wiring sizing, circuit design, or load calculation for residential or small commercial construction |
| **Frequency** | ~5,000–7,000 calculations/month chain-wide (~25–35/store/month) |
| **Volume** | 1–3 circuits per consultation; average purchase value PHP 3,000–15,000 |
| **Owner** | Department Supervisor (Electrical) |
| **Participants** | Sales Associate (Electrical Specialist), Customer, Category Manager |

### Background

Electrical wiring is one of the most safety-critical product categories in a hardware store. Undersized wires (too thin for the electrical load) overheat, potentially causing fires — a serious risk in Philippine residential construction where informal (unlicensed) electricians commonly perform wiring work and the Philippine Electrical Code (PEC) is not always followed. BuildRight's electrical load calculation and wire size recommendation service helps customers — homeowners, DIY renovators, and small contractors — select the correct wire size, circuit breaker rating, and accessories for their specific electrical installation. This service: (a) prevents safety hazards from undersized wiring; (b) reduces customer confusion in a technically complex category (THHN wire sizes: AWG 14, 12, 10, 8, 6, 4, 2, 1/0, 2/0, 3/0, 4/0 MCM); (c) increases average transaction value by recommending a complete circuit package (wire + breaker + outlet + switch + conduit + junction box); (d) positions BuildRight as a trusted advisor, not just a materials supplier. The service is available in-store via Electrical Specialist consultation and via BuildRight mobile app with an interactive calculator.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Customer Electrical Project Assessment**: Customer describes their electrical project: (a) project type — new house wiring, room addition, circuit extension, appliance dedicated circuit, lighting circuit, or outlet addition; (b) load information — what will be connected: (i) lighting: type (LED, fluorescent, incandescent), number of fixtures, total wattage; (ii) outlets: number of outlets, intended appliances (aircon, refrigerator, microwave, electric stove, water heater, washing machine); (iii) fixed appliances: air conditioner (HP rating), water heater (kW), electric stove (kW), pump motor (HP); (c) circuit information — dedicated circuit (single appliance) or general purpose circuit (multiple outlets/lights); (d) supply voltage: 220V single-phase (standard Philippine residential) or 380V three-phase (commercial/industrial); (e) wire run distance: from breaker panel to farthest outlet/fixture (affects voltage drop calculation); (f) installation environment: indoor (concealed in wall), outdoor, underground, or wet area | Sales Associate (Electrical Specialist) | Department Supervisor | 5–10 min |
| 2 | **Load Calculation & Wire Size Determination**: Sales Associate performs load calculation using BuildRight electrical calculator (in-store tablet or customer's mobile app): (a) **Total connected load**: sum of all appliance wattages on the circuit; (b) **Continuous load derating**: for loads operating ≥3 hours (lighting, aircon), apply 125% factor per PEC; (c) **Wire ampacity lookup**: system selects minimum wire size that can carry the calculated current (I = P ÷ V) with safety margin; standard Philippine residential wire sizes: (i) AWG 14 (2.0 sqmm) — 15A — lighting circuits, general outlets; (ii) AWG 12 (3.5 sqmm) — 20A — kitchen outlets, general purpose; (iii) AWG 10 (5.5 sqmm) — 30A — window-type aircon (1.0–1.5 HP); (iv) AWG 8 (8.0 sqmm) — 40A — split-type aircon (2.0 HP), electric stove; (v) AWG 6 (14 sqmm) — 55A — sub-feeders, large appliances; (vi) AWG 4 (22 sqmm) — 70A — main feeders; (d) **Voltage drop check**: for wire runs >30 meters, system calculates voltage drop (VD = 2 × I × R × L ÷ 1000); if voltage drop exceeds 3%, wire size is upsized; (e) **Breaker sizing**: circuit breaker rating = next standard size above calculated load current; standard breaker sizes: 15A, 20A, 30A, 40A, 50A, 60A; (f) **Conduit sizing**: conduit diameter sized for number and size of wires per PEC fill ratio (max 40% fill); (g) system generates: recommended wire size, breaker size, conduit size, and total wire length based on run distance | System / Sales Associate | Department Supervisor | 5–8 min (automated calculation) |
| 3 | **Complete Circuit Package Recommendation**: Sales Associate presents recommended materials as a complete circuit package: (a) **Wire**: correct size, type (THHN/THWN for indoor, TF for outdoor), and length (run distance × number of conductors: line + neutral + ground); (b) **Circuit breaker**: correct amperage and pole (1-pole for 220V circuits); (c) **Outlets**: type and quantity — standard outlet (for general use), aircon outlet (heavy-duty, with switch), GFCI outlet (for wet areas — bathroom, kitchen, outdoor); (d) **Switches**: type and quantity — single-pole, 3-way (for staircases), or dimmer; (e) **Conduit and fittings**: PVC conduit, elbows, connectors, couplings, and junction boxes; (f) **Accessories**: wire nuts/terminals, electrical tape, cable clips, and wire markers; (g) **Safety equipment**: wire stripper, voltage tester, and insulated screwdriver (if customer doesn't have); Sales Associate explains each component's purpose and why the specified size is necessary for safety; system displays package price and individual item prices | Sales Associate | Department Supervisor | 5–10 min |
| 4 | **Safety Briefing & Professional Referral**: Before purchase, Sales Associate conducts brief safety briefing: (a) emphasizes: (i) never work on live circuits — always turn off breaker before wiring; (ii) wire size and breaker must be matched — never install a larger breaker on undersized wire; (iii) grounding is mandatory — third wire (green/bare) must be connected; (iv) wet area circuits require GFCI protection; (b) system prints safety information card with purchase receipt; (c) if customer is a homeowner without electrical experience: Sales Associate strongly recommends hiring a licensed electrician and offers referral to BuildRight's installation partner network per W138; (d) for complex projects (3-phase, commercial, or whole-house wiring): Sales Associate recommends consulting a licensed electrical engineer and provides contact list of BuildRight's accredited electrical contractors per W600 | Sales Associate | Department Supervisor | 3–5 min |
| 5 | **Purchase & Project Linking**: Customer purchases complete circuit package; Sales Associate: (a) links purchase to customer's project per W894 (Project Vault) if customer has an active project; (b) for wire sold by length: system captures exact length cut from spool per W463 (catch-weight processing); (c) receipt includes: wire size, breaker size, circuit type, and load calculation summary — serves as documentation for customer's electrician; (d) offers to save circuit specification to customer's account for future reorder per W969 (e.g., customer building multiple houses with identical electrical plans) | Sales Associate / Cashier | Department Supervisor | 5–8 min |

### System Touchpoints
- Electrical load calculator module (POS tablet and mobile app)
- Philippine Electrical Code (PEC) wire ampacity table database
- Voltage drop calculation engine
- Product catalog with wire specifications per W50
- Complete circuit package bundling and pricing
- Catch-weight processing for wire sold by length (W463)
- Customer Project Vault (W894) for circuit specification saving
- Quick reorder integration (W969)
- Installation partner referral (W138)
- Safety information printing at POS

### Pain Points / Risks
- **Liability for electrical recommendations**: BuildRight provides sizing recommendations, not engineering designs; incorrect calculations could lead to safety hazards; clear disclaimer on all outputs: "This calculation is a general guide based on standard Philippine Electrical Code tables. For complex installations, consult a licensed electrical engineer. BuildRight is not liable for installation outcomes."; system calculations follow PEC conservative safety margins
- **Customer DIY risk**: Filipino homeowners frequently perform their own electrical work to save costs; while BuildRight cannot prevent DIY work, the safety briefing (step 4), professional referral, and safety information card fulfill BuildRight's duty of care; product liability insurance per W863 provides coverage
- **Wire size confusion**: Wire sizes are referred to differently — AWG (American), sqmm (metric), and local Filipino trade names ("no. 14 wire", "8-sqmm wire"); Sales Associates must be fluent in all naming conventions; system displays wire size in all three formats for clarity
- **PEC code updates**: The Philippine Electrical Code is updated periodically (current: PEC 2017); wire ampacity tables and installation requirements may change; Category Manager monitors PEC updates and adjusts calculator database accordingly; annual review of calculator parameters per regulatory change management per W657

### Staffing Implication
- **Sales Associate (Electrical Specialist)**: Electrical consultations consume ~3–4 hours/day at 25–35 calculations; absorbed by existing Electrical department Sales Associate with specialized electrical training
- **Training**: 24-hour electrical load calculation and PEC familiarization certification per W51; includes hands-on wire sizing exercises, breaker selection, and safety briefing practice; annual refresher aligned with PEC updates
- **No incremental headcount**

### Time Estimate
- Project assessment: 5–10 min
- Load calculation: 5–8 min
- Package recommendation: 5–10 min
- Safety briefing: 3–5 min
- Purchase: 5–8 min
- **Total per consultation**: 23–41 min of staff time

---

*Document Version: 1.0 | Date: 2026-06-08 | Added 20 new workflows (W963–W982) for BuildRight Depot model company*
