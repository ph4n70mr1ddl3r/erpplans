# Ecommerce Workflows

> BOPIS order fulfillment, home delivery fulfillment, ship-from-store, ecommerce order exception & cancellation management, marketplace integration (Lazada/Shopee), dark store operations, home delivery reverse logistics (returns), drop-ship vendor fulfillment, BOPIS smart locker & queue management, ecommerce product return inspection, grading & disposition, ecommerce product review & rating management, ecommerce platform incident management, marketplace channel daily operations & order management, ecommerce platform daily health monitoring & performance dashboard, ecommerce product content enrichment & catalog daily operations, customer bulk/project delivery scheduling & multi-drop coordination (B2C), customer project photo gallery & social proof/inspiration platform, and customer consumables subscription & auto-replenishment service.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W11. Ecommerce — BOPIS Order Fulfillment](#w11-ecommerce-bopis-order-fulfillment)
- [W19. Ecommerce — Home Delivery Fulfillment](#w19-ecommerce-home-delivery-fulfillment)
- [W19B. Ship from Store (Store-Fulfilled Home Delivery)](#w19b-ship-from-store-store-fulfilled-home-delivery)
- [W98. Ecommerce Order Exception & Cancellation Management](#w98-ecommerce-order-exception-cancellation-management)
- [W180. E-commerce Marketplace Integration (Lazada/Shopee)](#w180-e-commerce-marketplace-integration-lazadashopee)
- [W210. E-commerce Fulfillment Hub (Dark Store) Operations](#w210-e-commerce-fulfillment-hub-dark-store-operations)
- [W215. Customer Home Delivery Reverse Logistics (Returns)](#w215-customer-home-delivery-reverse-logistics-returns)
- [W246. Drop-Ship Vendor (DSV) Order Fulfillment](#w246-drop-ship-vendor-dsv-order-fulfillment)
- [W247. BOPIS Smart Locker & Queue Management](#w247-bopis-smart-locker-queue-management)
- [W266. Ecommerce Online Fraud Detection & Prevention](#w266-ecommerce-online-fraud-detection-prevention)
- [W267. Ecommerce Digital Payment Reconciliation & Dispute Handling](#w267-ecommerce-digital-payment-reconciliation-dispute-handling)
- [W509. Ecommerce Product Return Inspection, Grading & Disposition](#w509-ecommerce-product-return-inspection-grading-disposition)
- [W510. Ecommerce Product Review & Rating Management](#w510-ecommerce-product-review-rating-management)
- [W557. E-Commerce Abandoned Cart Recovery & Retargeting](#w557-e-commerce-abandoned-cart-recovery-retargeting)
- [W563. E-Commerce SEO & Digital Merchandising Management](#w563-e-commerce-seo-digital-merchandising-management)
- [W568. E-Commerce Flash Sale & Limited-Time Offer Operations](#w568-e-commerce-flash-sale-limited-time-offer-operations)
- [W569. E-Commerce New Product Launch & Go-Live Process](#w569-e-commerce-new-product-launch-go-live-process)
- [W659. Ecommerce Platform Incident Management](#w659-ecommerce-platform-incident-management)
- [W724. Marketplace Channel Daily Operations & Order Management (Lazada/Shopee)](#w724-marketplace-channel-daily-operations-order-management-lazadashopee)
- [W725. Ecommerce Platform Daily Health Monitoring & Performance Dashboard](#w725-ecommerce-platform-daily-health-monitoring-performance-dashboard)
- [W726. Ecommerce Product Content Enrichment & Catalog Daily Operations](#w726-ecommerce-product-content-enrichment-catalog-daily-operations)
- [W899. Customer Bulk/Project Delivery Scheduling & Multi-Drop Coordination (B2C)](#w899-customerbulkproject-delivery-scheduling--multi-drop-coordination-b2c)
- [W905. Customer Project Photo Gallery & Social Proof/Inspiration Platform](#w905-customer-project-photo-gallery--social-proofinspiration-platform)
- [W907. Customer Consumables Subscription & Auto-Replenishment Service](#w907-customer-consumables-subscription--auto-replenishment-service)

---

## W11. Ecommerce — BOPIS Order Fulfillment

| Field | Detail |
|---|---|
| **Trigger** | Customer places BOPIS order on website/app |
| **Frequency** | ~25,700 BOPIS orders/month; ~857/day |
| **Volume** | Avg 3–4 items per order |
| **Owner** | Customer Service Rep (in-store) |
| **Participants** | System (order routing), Stock Associate (picker), Customer Service Rep (handoff), Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer places order on website/app; selects pickup store; pays online | Customer | — | — |
| 2 | System routes order to selected store; creates store pick list | System | — | Automated |
| 3 | Store receives notification (tablet/terminal alert + printed pick list) | System | — | Automated |
| 4 | Stock Associate picks items from sales floor or backroom; scans each item to confirm | Stock Associate | Dept. Supervisor | 5–15 min/order |
| 5 | If item not in stock at store: system offers substitution or cancels line; notifies customer | System / CSR | Store Manager | 3 min |
| 6 | Stock Associate stages picked items at Customer Service counter | Stock Associate | CSR | 2 min |
| 7 | System marks order as "Ready for Pickup"; sends SMS/email to customer | System | — | Automated |
| 8 | Customer arrives at Customer Service counter; presents ID and order number | Customer | — | — |
| 9 | Customer Service Rep verifies ID; scans order; releases items | CSR | Store Manager | 3 min |
| 10 | System marks order as "Completed"; inventory deducted | System | — | Automated |
| 11 | If not picked up within 5 days: auto-cancel; refund initiated; items returned to shelf | System | CSR | Automated (return: 5 min) |

**Pick SLA**: Ready within 4 hours of order placement

### System Touchpoints
- Real-time inventory availability per store on website (W11.1)
- Available-to-Promise (ATP) reservation at order placement: system deducts from available inventory (not physical) at the fulfillment location; ATP = on-hand − allocated to open orders − safety stock buffer; if ATP = 0, item shown as "unavailable" on website for that location (W11.1)
- ATP reservation held until pick confirmation (hard commitment) or order cancellation; BOPIS reservation auto-releases after 5-day hold period if not picked up (W11.11)
- Order routing to store with pick list generation (W11.2–3)
- In-store pick confirmation via scanning (W11.4)
- Out-of-stock substitution/cancellation handling (W11.5)
- Customer notification (SMS/email) (W11.7)
- Order handoff verification with ID check (W11.9)
- Auto-cancel and refund after hold period (W11.11)
- Ecommerce IC settlement for BOPIS: revenue is recognized by Depot Inc. at pickup (goods are Depot Inc. inventory); Digital Commerce Inc. (which collected payment online) remits collected payments to Depot Inc. monthly per W14 ecommerce payment collection IC flow; Digital Commerce Inc. charges Depot Inc. a per-order fulfillment fee per W14 ecommerce fulfillment IC flow; all IC settlements processed monthly via W14
- Ecommerce VAT for BOPIS: BOPIS transactions are subject to 12% VAT identical to in-store; output VAT is recognized by Depot Inc. (the entity recognizing revenue per IC model); Digital Commerce Inc. does not recognize VAT on payment collection (remitted to Depot Inc.); VAT on BOPIS transactions included in Depot Inc.'s BIR 2550M filing

### Time Estimate
- Customer order placement and payment: 5–10 min (customer-driven)
- System order routing and pick list generation: automated (instant)
- Store notification receipt: automated (instant)
- Stock Associate item picking and scan confirmation: 5–15 min/order
- Out-of-stock substitution / cancellation handling: 3 min
- Staging picked items at Customer Service counter: 2 min
- Customer notification (Ready for Pickup): automated (instant)
- Customer arrival and ID verification: 2–5 min (customer-dependent)
- CSR ID check and item release: 3 min
- Order completion and inventory deduction: automated (instant)
- Auto-cancel and refund after 5-day hold: automated + 5 min restocking
- **Total elapsed time (order to handoff)**: ~4 hours (per Pick SLA)

### Pain Points / Risks
- **ATP accuracy and phantom inventory**: BOPIS fulfillment depends on store-level ATP being accurate; if perpetual inventory is off due to shrinkage, missed scans, or delayed cycle counts (W6), customers place orders for items that are not physically on the shelf, leading to pick failures, substitution friction, and customer dissatisfaction
- **Pick SLA compliance during peak hours**: the 4-hour pick SLA is difficult to maintain when store foot traffic peaks (weekends, payday sales) because Stock Associates responsible for BOPIS picks are simultaneously managing sales floor replenishment and customer service; orders placed during peak may exceed the 4-hour window
- **5-day hold period expiry and restocking cost**: approximately 5–8% of BOPIS orders are never picked up, triggering auto-cancellation, refund processing, and restocking labor; high-value items held for 5 days represent tied-up inventory that could have been sold to walk-in customers
- **Customer wait time at pickup counter**: during high-volume periods, multiple customers may arrive simultaneously for BOPIS pickup, creating a queue at the Customer Service counter that is staffed by a single CSR; wait times exceeding 10 minutes negatively impact the BOPIS value proposition vs. in-store shopping

### Staffing Implication
- **1 CSR per store**: 857 BOPIS orders/day ÷ 200 stores = ~4 BOPIS orders/store/day. At ~10 min per order (pick + handoff), that's ~40 min/day. The CSR also handles returns and special orders, so 1 per store is adequate. Current headcount (1 CSR/store) works.
- **Stock Associates absorb picking**: ~4 BOPIS picks/day is minimal additional load for 3 stock associates already doing replenishment and cycle counts.

---

## W19. Ecommerce — Home Delivery Fulfillment

| Field | Detail |
|---|---|
| **Trigger** | Customer places delivery order on website/app (non-BOPIS) |
| **Frequency** | ~17,200 delivery orders/month; ~573/day |
| **Volume** | Avg 3–4 items per order |
| **Owner** | DC Dispatch Supervisor |
| **Participants** | System (order routing), DC Picker, DC Packer, Delivery Partner driver, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer places delivery order on website/app; selects delivery address; pays online | Customer | — | — |
| 2 | System routes order to nearest DC (or store if DC out of stock); creates pick list; **multi-DC order splitting**: if order contains items stocked at different DCs (e.g., bulky items at DC3 Laguna but specialty items only at DC4 Clark), system evaluates fulfillment options — (a) single-DC fulfillment preferred: ship all items from one DC if ATP available, even if not the closest DC for some lines; (b) split fulfillment: if no single DC has ATP for all items, system splits order into sub-orders per fulfillment DC — each sub-order gets its own tracking number, carrier assignment, and delivery timeline; customer receives a single order confirmation with "Items shipping from multiple locations" notice and per-sub-order tracking links; (c) split cost allocation: additional shipping cost from split fulfillment (if any) is absorbed by BuildRight, not charged to customer; (d) partial delivery: first sub-order ships immediately; remaining sub-orders ship as ATP becomes available; customer notified per sub-order status; (e) returns for split orders: customer may return all items to any BuildRight store per W12B regardless of which DC fulfilled; system handles cross-location inventory adjustment per W12C; Supply Planner reviews split fulfillment frequency weekly — high split rates for specific items trigger replenishment parameter review per W31.8 | System | — | Automated |
| 3 | DC receives pick task; assigns to picker by zone | WMS / DC Supervisor | DC Supervisor | 2 min |
| 4 | Picker picks items; scans each for confirmation | Picker | DC Supervisor | 5–15 min/order |
| 5 | If item unavailable: system offers substitution or cancels line; notifies customer | System / CSR | — | 3 min |
| 6 | Packer packs items for shipping; generates shipping label and packing slip | Packer | DC Supervisor | 5 min/order |
| 7 | System creates delivery order with selected partner (Lalamove, Transportify, own fleet) | System | DC Dispatch | Automated |
| 8 | Delivery partner picks up package; system updates order status to "Shipped" | Delivery Partner | DC Dispatch | 5 min |
| 9 | System sends tracking link to customer via SMS/email | System | — | Automated |
| 10 | Delivery partner delivers to customer; obtains proof of delivery (photo, signature) | Delivery Partner | — | Varies by distance |
| 11 | System marks order as "Delivered"; inventory formally deducted | System | — | Automated |
| 12 | If delivery fails (customer unavailable): system initiates failed delivery lifecycle — (a) 1st attempt: delivery partner leaves notification (call/SMS); customer given 2-hour window to respond for same-day re-delivery attempt; (b) if no response or 2nd attempt fails: order returns to DC; system sends customer notification with reschedule options (next available date) or cancellation option; (c) if customer reschedules: system creates new delivery order with carrier; (d) if customer cancels: system initiates refund to original payment method (Dr. Revenue / Cr. Cash) and DC restocks item per W12A.7; (e) if customer does not respond within 3 business days after return-to-DC: system auto-cancels order and initiates refund | Delivery Partner / DC | DC Supervisor | 15 min + carrier transit time |
| 12a | **Home delivery return (reverse logistics)**: for bulky/large items (appliances, lumber, tiles, fixtures) that the customer cannot transport to a store, system schedules carrier pickup via 3PL integration; carrier collects item from customer address and returns to originating DC; DC Receiving Clerk inspects returned item; if resalable: system processes refund to original payment method and restocks per W12A.7; if damaged: disposition per W6.8a (markdown, scrap, RTV); refund processed upon DC inspection confirmation | System / DC Receiving Clerk / CSR | DC Supervisor | 15 min/setup + carrier transit time
12b | **Carrier damage vs. vendor defect liability assignment**: when a home delivery customer reports damaged goods, CSR creates a damage report at intake with customer-provided photos and damage description; system routes damage report for liability determination: (a) **carrier damage** — external packaging damage, dents/scratches consistent with transit handling, item damage on one side, water damage to outer carton — CSR files carrier damage claim via 3PL integration (W19.7); carrier's insurance covers loss; customer receives immediate replacement or refund; system posts Dr. Carrier Claim Receivable / Cr. Inventory; (b) **vendor/manufacturing defect** — item defective out of box with intact packaging, missing parts, functional failure without physical damage — CSR processes vendor warranty claim (W33) or RTV (W3.6a); system posts Dr. Vendor Claim Receivable / Cr. Inventory; (c) **undetermined** — if cause unclear from photos, DC inspects returned item and makes final determination; (d) monthly: DC Supervisor generates delivery damage report — carrier damage rate by carrier (feeds W44/W62B), vendor defect rate by vendor (feeds W44), customer impact (refund vs. replacement) | CSR / DC Receiving Clerk | DC Supervisor | 10 min/classification

### System Touchpoints
- Ecommerce platform order routing, 3PL carrier API integration, POS system (for BOPIS fallback), inventory management (ATP check), payment gateway settlement, customer notification system (SMS/email)

### Pain Points / Risks
- 3PL delivery failures
- Customer not-at-home
- Multi-item order splitting across DCs
- Fragile items damage in transit
- Same-day delivery SLA pressure
- Rural address quality

### Time Estimate
- ~15 min per order (picking + packing + dispatch). Parent workflow oversight: ~1–2 hours daily for monitoring dashboards.

### Staffing Implication
- DC pick/pack staff absorb ecommerce fulfillment volume. 1 Ecommerce Operations Manager monitors daily fulfillment. 3PL coordination absorbed by Supply Chain team.


---

## W19B. Ship from Store (Store-Fulfilled Home Delivery)

| Field | Detail |
|---|---|
| **Trigger** | Customer places home delivery order on website/app; nearest DC out of stock but nearby store has ATP |
| **Frequency** | ~1,000–2,000 ship-from-store orders/month; primarily bulky items (appliances, lumber, tiles) with limited DC coverage |
| **Volume** | Avg 1–3 items per order |
| **Owner** | Store Manager (store execution); DC Dispatch (carrier coordination) |
| **Participants** | System (order routing), Stock Associate (picker), DC Dispatch, 3PL carrier, Customer |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System evaluates order fulfillment options: (a) DC fulfillment (standard W19) preferred, (b) if DC ATP = 0 for any line item, system checks ATP at stores within delivery radius of customer address, (c) if store ATP available, system offers ship-from-store as fulfillment option with estimated delivery date | System | — | Automated |
| 2 | Supply Planner or DC Dispatch reviews ship-from-store suggestion; confirms store has sufficient stock and store is not in a peak selling period (system shows store's current day sales velocity); approves or overrides to wait for DC replenishment | Supply Planner / DC Dispatch | DC Supervisor | 5 min/order |
| 3 | System routes order to selected store; creates store pick list with item locations; creates outbound shipment record | System | — | Automated |
| 4 | Store receives notification (tablet/terminal alert); Stock Associate picks items from sales floor or backroom; scan-confirms each item | Stock Associate | Dept. Supervisor | 10–20 min/order |
| 5 | Stock Associate stages picked items at store receiving/dispatch area; packs for shipping using packaging materials | Stock Associate | Dept. Supervisor | 10 min/order |
| 6 | DC Dispatch creates delivery order with 3PL carrier (same W19.7 integration); carrier picks up from store during scheduled route or on-demand | DC Dispatch / Carrier | DC Supervisor | 15 min/setup + pickup wait |
| 7 | Carrier delivers to customer per standard W19.10; proof of delivery captured | Carrier | — | Varies |
| 8 | System marks order "Delivered"; inventory deducted at store location (not DC); revenue recognized by Depot Inc. per standard ecommerce IC model (W14) | System | — | Automated |
| 9 | If customer returns ship-from-store item: standard W12B (online return) or W19.12a (reverse logistics pickup) — item returns to the originating store (not DC) if store has capacity; otherwise to DC | System / CSR | Store Manager | Per W12/W19 |

**Delivery SLA**: 3–7 business days (slightly longer than DC fulfillment due to carrier pickup from store)

### System Touchpoints (Ship from Store)
- Multi-origin fulfillment engine: DC fulfillment preferred, store fulfillment fallback when DC ATP = 0; configurable delivery radius per store (typically 20–30 km) (W19B.1)
- Store ATP check with real-time available inventory (on-hand − allocated − safety stock buffer) (W19B.1)
- Store pick list generation and scan confirmation (W19B.3–4)
- Outbound shipment creation from store location with 3PL carrier dispatch (W19B.6)
- Inventory deduction at store location upon delivery confirmation (W19B.8)
- Ecommerce IC settlement: identical to standard home delivery — Depot Inc. recognizes revenue; Digital Commerce Inc. remits payment per W14; Logistics Inc. charges per-order fulfillment fee per W14 (store fulfillment may have a different fee rate than DC fulfillment) (W19B.8)
- Integration with W19 (home delivery), W4 (store replenishment — ship-from-store consumption reduces store inventory), W14 (IC settlement)

### Pain Points / Risks
- **Store operations disruption**: ship-from-store adds packing and carrier-handoff duties to Stock Associates and Department Supervisors who are already managing sales floor replenishment, BOPIS picks, and customer service; during peak in-store traffic (weekends, payday sales), store staff deprioritize ship-from-store orders, violating the 3–7 day delivery SLA
- **Store inventory accuracy dependency**: ship-from-store is only viable if store-level ATP (available-to-promise) is accurate; if a store's perpetual inventory is off due to shrinkage, missed scans, or cycle count delays (W6), the customer order is accepted but the item cannot be found at pick time, triggering a W98 pick failure exception
- **Carrier pickup scheduling at stores**: unlike DCs with scheduled carrier routes, stores require ad-hoc carrier dispatch for ship-from-store orders; 3PL carriers (Lalamove, Transportify) may take 2–4 hours to arrive at the store for pickup, extending the fulfillment timeline and making the 3–7 day SLA difficult to meet for same-day or next-day orders
- **Store-level packaging material supply**: stores do not naturally stock shipping cartons, bubble wrap, and packing tape in quantities needed for home delivery fulfillment; without a dedicated replenishment process for packaging materials (separate from merchandise replenishment W4), Stock Associates improvise packaging, increasing carrier damage rates

### Time Estimate
- System fulfillment option evaluation (DC vs. store): automated (instant)
- Supply Planner / DC Dispatch review and approval: 5 min/order
- System order routing and pick list generation at store: automated (instant)
- Store Stock Associate picking and scan confirmation: 10–20 min/order
- Packing and staging at store dispatch area: 10 min/order
- DC Dispatch 3PL carrier booking and carrier pickup from store: 15 min setup + 1–4 hour carrier wait
- Last-mile delivery to customer: varies (1–3 business days)
- Delivery confirmation and inventory deduction: automated (instant)
- **Total elapsed time (order to delivery)**: 3–7 business days (per Delivery SLA)

- Delivery partner order creation and dispatch: automated + 5 min carrier pickup
- Customer tracking notification: automated (instant)
- Last-mile delivery to customer: varies by distance (1–4 hours Metro Manila; 1–3 days provincial)
- Proof of delivery capture and order completion: automated (instant)
- Failed delivery re-attempt / return-to-DC lifecycle: 15 min processing + carrier transit time
- **Total elapsed time (order to delivery)**: 1–5 business days depending on location

### System Touchpoints
- Real-time inventory availability per DC on website (W19.1)
- Available-to-Promise (ATP) reservation at order placement: system deducts from available inventory at the fulfillment DC; ATP = on-hand − allocated to open orders − safety stock buffer; if ATP = 0, item shown as "unavailable" for that delivery zone (W19.1)
- ATP reservation held until pick confirmation (hard commitment) or order cancellation; released if delivery fails and order is cancelled (W19.12)
- Order routing to nearest fulfillment location (W19.2)
- WMS pick task generation and assignment (W19.3–4)
- Out-of-stock substitution/cancellation (W19.5)
- Shipping label and packing slip generation (W19.6)
- Delivery partner API integration for order creation and tracking (W19.7, W19.8, W19.10)
- Customer notification (SMS/email) with tracking link (W19.9)
- Proof of delivery capture (W19.10)
- Failed delivery / return-to-origin handling (W19.12)
- Ecommerce payment reconciliation: system imports daily settlement reports from each payment gateway (PayMongo, Dragonpay, GCash, Maya); matches settlement line items to individual ecommerce orders; reconciles gross payments, gateway fees (per-transaction and percentage), chargebacks, and refunds; posts gateway fees to payment processing expense (Dr. Payment Processing Expense / Cr. Cash); flags unreconciled settlements for investigation; Treasury verifies bank deposits match expected settlement amounts; reconciliation performed daily by Treasury Analyst as part of W30 daily cycle (W19)
- Home delivery reverse logistics: for bulky items requiring carrier pickup, system integrates with 3PL carriers to schedule reverse pickup at customer address; tracks return shipment to DC; DC inspection and disposition (restock, markdown, scrap, RTV); refund triggered upon inspection confirmation (W19.12a)
- 3PL / delivery partner management: carrier master record with rate cards per zone/weight/tier and SLA terms; automated carrier selection by delivery zone, package weight, and cost; carrier performance dashboard tracking on-time delivery %, damage rate, cost per delivery, and customer complaint rate per carrier; monthly carrier invoice reconciliation (carrier fees matched to completed delivery orders); quarterly carrier performance review similar to W44 vendor scorecard; rate renegotiation triggered by SLA breach or market benchmarking (W19.7, W19.8, W19.10)
- Ecommerce IC settlement for home delivery: revenue is recognized by Depot Inc. at delivery (goods are Depot Inc. inventory fulfilled by Logistics Inc. DCs); Digital Commerce Inc. (which collected payment online) remits collected payments to Depot Inc. monthly per W14 ecommerce payment collection IC flow; Logistics Inc. charges Depot Inc. a per-order fulfillment fee per W14 ecommerce fulfillment IC flow; all IC settlements processed monthly via W14
- Ecommerce VAT for home delivery: ecommerce transactions are subject to 12% VAT identical to in-store; output VAT is recognized by Depot Inc. (the entity recognizing revenue per IC model); Digital Commerce Inc. does not recognize VAT on payment collection (remitted to Depot Inc.); system tracks input VAT and output VAT per entity; VAT on ecommerce transactions included in Depot Inc.'s BIR 2550M filing

### Pain Points / Risks
- **3PL carrier reliability for bulky hardware items**: standard on-demand delivery partners (Lalamove, Transportify) are optimized for small parcels; hardware/DIY orders frequently include oversized or heavy items (lumber, cement bags, tile pallets, appliances) that require specialized vehicles and careful handling; carrier damage rates for bulky items run 2–3x higher than standard parcels, directly impacting margin and customer satisfaction
- **Multi-DC order splitting customer confusion**: when a customer's order is split across two DCs, they receive two deliveries at different times; despite system notification, customers frequently contact support believing the order is incomplete after the first partial delivery, generating unnecessary W98 exception cases and CS cost
- **Failed delivery cost accumulation**: each failed delivery attempt (customer unavailable, wrong address) costs ~PHP 150–300 in carrier fees plus DC re-stocking labor; at ~2% failed delivery rate on ~17,000 orders/month, this represents ~PHP 50K–100K/month in wasted logistics spend; failed deliveries also tie up inventory in DC receiving returns for 3–5 days
- **Ecommerce IC settlement timing gap**: Digital Commerce Inc. collects payment at order placement but remits to Depot Inc. only monthly per W14; during high-GMV periods (payday sales, 11.11, 12.12), Depot Inc. carries up to PHP 100M+ in IC receivables from Digital Commerce Inc., creating working capital pressure that Treasury must manage via IC loans (W14 IC Loans)

---

### Time Estimate
- Customer order placement and payment: 5–10 min (customer-driven)
- System order routing and multi-DC split evaluation: automated (instant)
- DC pick task assignment: 2 min
- DC item picking and scan confirmation: 5–15 min/order
- Out-of-stock substitution / cancellation handling: 3 min
- Packing, shipping label, and packing slip generation: 5 min/order
- Delivery partner order creation and dispatch: automated + 5 min carrier pickup
- Customer tracking notification: automated (instant)
- Last-mile delivery to customer: varies by distance (1–4 hours Metro Manila; 1–3 days provincial)
- Proof of delivery capture and order completion: automated (instant)
- Failed delivery re-attempt / return-to-DC lifecycle: 15 min processing + carrier transit time
- **Total elapsed time (order to delivery)**: 1–5 business days depending on location

### Staffing Implication
- **Store-level**: ~1,000–2,000 ship-from-store orders/month ÷ 200 stores = ~5–10 orders/store/month. At ~40 min per order (pick + pack + carrier handoff), that's ~3–7 hours/store/month. Absorbed by existing Stock Associates (3 per store) as a minor additional duty.
- **DC Dispatch incremental load**: carrier coordination for store pickups adds ~5–10 min per order × 1,000–2,000 orders/month = ~83–167 hours/month across 4 DCs. Absorbed by existing DC Dispatch team (3–4 per DC) as a shared responsibility with standard W19 dispatch.
- **Peak period concern**: during promotional events (W13) where ship-from-store volume may spike 3–5x, stores in Metro Manila with high ecommerce density may see 30–50 ship-from-store orders/month; these stores should designate a backup Stock Associate for ship-from-store picking to avoid conflicts with BOPIS and sales floor duties.

**Delivery SLA**: 2–5 business days from order placement

### Staffing Implication
- **Per DC**: Home delivery adds 17,200 orders/month ÷ 30 days ÷ 4 DCs = **~115 orders/DC/day**. At ~15 min pick+pack per order, that's **~29 hours/DC/day** of additional DC labor. This requires 3–4 dedicated pickers/packers per DC for home delivery, within the existing ~150 DC headcount (total DC pick/pack team of 15–20 handles both store replenishment at ~33 orders/day and ~115 home delivery orders/day in shifts). Home delivery orders are typically smaller (3–4 items) and packed individually, while store replenishment orders are larger (~50 lines) and packed in bulk — different skills and pacing.
- **Staffing implication**: Home delivery fulfillment absorbs a significant portion of DC pick/pack capacity. The 25–30 pickers/packers per DC should be sufficient for combined W4 + W19 volume, but DC management should monitor utilization during ecommerce growth. Peak ecommerce periods (sale events at 3× normal volume per data volumes §1.1) may require temporary surge staffing or overtime. During these peak periods, DC Supervisors should coordinate with HR to deploy agency workers (per W10 agency/manpower contractor management) for temporary pick/pack surge capacity, or arrange overtime for existing DC staff. Additionally, 3PL carrier surge capacity should be pre-arranged with delivery partners (W19.7) at least 2 weeks before planned promotional events (W13) to handle elevated home delivery order volumes.

## W98. Ecommerce Order Exception & Cancellation Management

| Field | Detail |
|---|---|
| **Trigger** | BOPIS pick failure; home delivery failure; customer cancellation request; auto-cancellation (hold period expiry, payment failure); order modification request; or payment authorization failure |
| **Frequency** | ~4,000–6,000 exception cases/month (~10–15% of ~42,900 ecommerce orders) |
| **Volume** | ~130–200 exception cases/day across all channels
| **Owner** | CSR (store-level exceptions); DC Dispatch (delivery exceptions); Ecommerce Customer Support (online channel) |
| **Participants** | CSR, DC Dispatch, Ecommerce Customer Support, Stock Associate, Treasury Analyst, Customer |

### Background

W11 (BOPIS) and W19 (Home Delivery) cover the happy-path fulfillment process from order to delivery. However, ~10–15% of ecommerce orders encounter exceptions: items not found during BOPIS picking, delivery failures when the customer is unavailable, customer-initiated cancellations, payment authorization failures, and auto-cancellations when hold periods expire. Without a dedicated exception handling workflow, these cases result in poor customer experience, delayed refunds, inventory discrepancies, and increased customer service contacts. This workflow covers all ecommerce order exception scenarios and ensures timely resolution with proper financial and inventory reconciliation.

### BOPIS Exceptions

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pick failure — item not found in store**: (a) Stock Associate cannot locate item during BOPIS pick (W11.4); (b) system checks: is item in backroom? checked recently? If not found after 10 min search, Stock Associate marks item as "Pick Failed"; (c) system evaluates alternatives: (i) **Substitution**: offer customer a similar item (system suggests substitutes based on category and price range); customer accepts or declines via SMS/email with one-click response; (ii) **Transfer from nearby store**: if item available at store within 10 km, system creates emergency inter-store transfer per W22 for pickup within 24 hours; (iii) **Ship from DC**: convert BOPIS line to home delivery (W19) with system routing to nearest DC; customer notified of new delivery timeline; (iv) **Cancel line**: if customer declines all alternatives, cancel the unfilled line and initiate refund | Stock Associate / System / CSR | Store Manager | 10 min + customer response time |
| 2 | **Pick failure — item damaged on shelf**: (a) Stock Associate finds item but it's damaged; (b) Stock Associate marks as "Damaged at Pick"; system routes to W91 damaged goods process; (c) same substitution/transfer/ship/cancel alternatives as step 1 apply for customer | Stock Associate / CSR | Store Manager | 10 min |
| 3 | **BOPIS hold period expiry** (5-day auto-cancel): (a) System monitors BOPIS orders not picked up within 5 days; (b) **Day 3**: system sends reminder to customer (SMS + email): "Your order is ready for pickup. Please pick up by [date] or your order will be cancelled and refunded."; (c) **Day 4**: CSR calls customer for high-value orders (> PHP 10,000) to confirm pickup intent; (d) **Day 5**: if not picked up, system auto-cancels order; initiates refund to original payment method per W94 deposit refund; items returned to saleable inventory (shelf or backroom); system reverses ATP reservation | System / CSR | Store Manager | Automated + 5 min/call |
| 4 | **BOPIS customer cancellation**: (a) Customer requests cancellation via website/app, phone, or in-store before pickup; (b) if order status is "Ready for Pickup": CSR processes cancellation in system; items returned to shelf; refund initiated per original payment method; (c) if order status is "Being Picked": system attempts to stop pick; if already picked, items staged but customer cancelled — CSR processes cancellation and restocks | CSR / System | Store Manager | 5 min/cancellation |

### Home Delivery Exceptions

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 5 | **Delivery failure — customer unavailable**: (a) Carrier reports failed delivery (per W19.12); (b) system sends customer SMS with reschedule/cancel options; (c) if customer reschedules: system creates new delivery order with carrier; (d) if customer cancels: system processes refund and DC restocks upon carrier return; (e) if no customer response within 3 business days: system auto-cancels and refunds per W19.12 | Carrier / System / DC Dispatch | DC Supervisor | Per W19.12 |
| 6 | **Delivery failure — address issue**: (a) Carrier reports address not found or incorrect; (b) system contacts customer via SMS/email to confirm/correct address; (c) if customer provides corrected address within 24 hours: carrier re-attempts delivery; (d) if customer does not respond: same 3-day auto-cancel as step 5 | Carrier / System | DC Dispatch | 10 min |
| 7 | **Delivery — customer reports wrong item**: (a) Customer contacts Ecommerce Customer Support (chat, email, phone) reporting wrong item delivered; (b) CSR verifies: compares order contents vs. delivery confirmation photo; (c) if carrier error (wrong package delivered): CSR initiates carrier claim (W19.12b) and reships correct item from DC; (d) if DC pick error (DC picked wrong SKU): DC Dispatch investigates pick process; correct item reshipped; wrong item scheduled for carrier pickup (reverse logistics per W19.12a); (e) system creates exception order with priority flag for reshipment | CSR / DC Dispatch | DC Supervisor | 15 min/case |
| 8 | **Delivery — customer reports damaged item**: (a) Customer contacts support with photos of damaged delivery; (b) CSR processes per W19.12b carrier damage vs. vendor defect liability; (c) for carrier damage: immediate replacement order created with priority flag + carrier claim filed; (d) for vendor defect: replacement order created + vendor warranty claim per W33; (e) damaged item returned via reverse logistics per W19.12a | CSR / DC Receiving Clerk | DC Supervisor | 15 min/case |

### Payment & System Exceptions

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 9 | **Payment authorization failure**: (a) Customer places order but payment gateway declines authorization (insufficient funds, expired card, e-wallet limit reached); (b) system holds order in "Payment Pending" status for 1 hour; (c) system sends customer notification: "Payment not completed. Please retry or use a different payment method."; (d) if customer retries within 1 hour: order proceeds to fulfillment; (e) if payment not completed within 1 hour: system auto-cancels order; inventory reservation released | System / Customer | — | Automated |
| 10 | **Partial payment / split payment failure**: (a) For multi-tender orders (e.g., gift card + credit card): if one payment method fails, system holds successful payment as customer credit (W28) and prompts customer to retry failed portion; (b) if customer does not complete within 1 hour: auto-cancel entire order; successful payment portion refunded to gift card or original method | System | — | Automated |
| 11 | **Order modification request**: (a) Customer requests change to order after placement but before fulfillment: change delivery address, add/remove items, change pickup store; (b) **Before pick/ship**: CSR modifies order in system; inventory reservation adjusted; if new items added, system checks ATP and adds if available; if items removed, ATP released; (c) **After pick/ship**: no modification possible; customer must receive order and then initiate return per W12B; exception: delivery address change may be possible if carrier has not dispatched — CSR coordinates with DC Dispatch | CSR / DC Dispatch | Store Manager / DC Supervisor | 5–10 min/request |
| 12 | **System error / duplicate order**: (a) Customer contacts support reporting duplicate order (placed twice accidentally); (b) CSR verifies duplicate: same items, same address, placed within 30 minutes; (c) cancels duplicate order and refunds; (d) if duplicate already shipped: customer may refuse delivery of second package (carrier returns to DC) or return in-store per W12B | CSR | Ecommerce Manager | 10 min/case |

### Exception Monitoring & Analytics

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 13 | **Daily exception dashboard**: System generates daily ecommerce exception dashboard: total orders, exceptions by type (pick failure, delivery failure, cancellation, payment failure), resolution rate, average resolution time, customer satisfaction impact; Ecommerce Manager reviews daily | System / Ecommerce Manager | CMO | 15 min/day |
| 14 | **Weekly exception review**: Ecommerce Manager and DC Dispatch Supervisor review weekly exception trends: (a) BOPIS pick failure rate by store (target: < 3%); stores > 5% investigated for inventory accuracy issues (W6); (b) delivery failure rate by carrier (target: < 2%); carriers > 5% flagged for W62B performance review; (c) cancellation rate (target: < 5%); cancellation reason analysis; (d) top exception SKUs — items that frequently fail picking (possible ATP/inventory sync issue) or frequently get delivery complaints (possible packaging issue) | Ecommerce Manager / DC Dispatch | CMO / COO | 30 min/week |
| 15 | **Monthly exception report**: Ecommerce Manager prepares monthly exception report for CMO and COO: exception rate trend, resolution time trend, root cause analysis, improvement initiatives, and financial impact (lost revenue from cancellations, cost of re-shipping, refund volume); feeds into W35 management reporting | Ecommerce Manager | CMO | 1 hour/month |

### System Touchpoints
- BOPIS pick failure handling with substitution/transfer/ship-from-DC/cancel alternatives (W98.1)
- BOPIS hold period monitoring with escalating reminders and auto-cancellation (W98.3)
- Home delivery failure management with reschedule/cancel and reverse logistics (W98.5–6)
- Wrong/damaged item delivery resolution with carrier claim and reshipment (W98.7–8)
- Payment authorization failure handling with retry window and auto-cancellation (W98.9–10)
- Order modification processing with fulfillment-stage-dependent rules (W98.11)
- Daily exception dashboard and weekly/monthly analytics (W98.13–15)
- Integration with W11 (BOPIS — pick failure originates here), W12 (returns — cancelled order refund processing), W12B (online returns — return after delivery), W19 (home delivery — delivery failure originates here), W22 (inter-store transfer — BOPIS emergency transfer), W28 (gift card — partial payment failure), W33 (warranty — vendor defect replacement), W41 (complaints — customer escalations), W56 (backorder — similar customer notification), W91 (damaged goods — pick failure damage), W94 (deposit refund — cancellation refund processing), W99 (payment settlement — payment failure reconciliation)

### Time Estimate
- BOPIS pick failure (item not found): 10 min + customer response time for substitution decision
- BOPIS pick failure (item damaged on shelf): 10 min
- BOPIS hold period expiry processing: automated + 5 min/call for high-value order follow-up
- BOPIS customer cancellation: 5 min/cancellation
- Home delivery failure (customer unavailable): follows W19.12 timeline (15 min processing + carrier transit)
- Home delivery failure (address issue): 10 min CSR processing
- Wrong item delivery resolution: 15 min/case (CSR investigation + reshipment creation)
- Damaged item delivery resolution: 15 min/case (liability classification + carrier/vendor claim initiation)
- Payment authorization failure: automated (1-hour customer retry window)
- Order modification request: 5–10 min/request
- Duplicate order resolution: 10 min/case
- Daily exception dashboard review: 15 min/day
- Weekly exception review meeting: 30 min/week
- Monthly exception report preparation: 1 hour/month
- **Average exception resolution time**: 10–15 min/case; automated exceptions (payment failure, hold expiry) resolve instantly

### Pain Points / Risks
- **Exception rate correlated with inventory accuracy**: the ~10–15% ecommerce exception rate is heavily driven by BOPIS pick failures (item not on shelf despite ATP showing availability); improving store-level inventory accuracy from the current estimated ~90% to ~97% through better cycle counting (W6) would reduce BOPIS pick failures by an estimated 50–60%, but requires sustained operational discipline across 200 stores
- **Refund processing delay on cancellations**: when an ecommerce order is cancelled (customer-initiated, payment failure, or hold-period expiry), the refund must traverse the payment gateway (PayMongo, Dragonpay) back to the customer's card or e-wallet, taking 3–7 business days; customers frequently re-contact support asking "where is my refund?" during this window, doubling the CS cost per cancellation
- **Carrier damage liability disputes with 3PLs**: when a customer reports damaged delivery (step 8), the carrier damage vs. vendor defect determination (W19.12b) is subjective and often disputed by the 3PL carrier; carriers reject ~30–40% of damage claims, forcing BuildRight to absorb the loss; monthly carrier damage rate must stay below 2% or the W62B carrier performance review triggers contract renegotiation
- **Payment failure rate on high-value orders**: hardware/DIY ecommerce orders average PHP 3,000–5,000 but can reach PHP 50,000+ for appliances and project materials; payment authorization failure rate increases significantly for high-value orders (card limits, e-wallet balance caps), creating a disproportionate number of payment exceptions on the highest-margin orders

---

### Staffing Implication
- **CSRs**: ~2,000–3,000 BOPIS exceptions/month ÷ 200 stores = ~10–15 per store/month × 10 min each = ~2 hours/store/month. Absorbed by existing 1 CSR/store.
- **DC Dispatch**: ~1,000–2,000 delivery exceptions/month ÷ 4 DCs = ~200–400 per DC/month × 15 min each = ~50–100 hours/DC/month. With DC Dispatch team of 3–4, this is ~15–25 hours each/month. Absorbed.
- **Ecommerce Customer Support** (30-person call center): handles chat/email/phone exception cases; ~1,000–1,500 cases/month ÷ 30 agents = ~40–50 cases/agent/month × 10 min each = ~7–8 hours/agent/month. Absorbed within existing call center capacity.
- **No incremental headcount.**

## W180. E-commerce Marketplace Integration (Lazada/Shopee)

| Field | Detail |
|---|---|
| **Trigger** | Order placed on external marketplace (Lazada/Shopee) |
| **Frequency** | High; ~5,000–8,000 orders/month |
| **Volume** | Avg 2–3 items per order; avg order value PHP 1,500–3,000 |
| **Owner** | Ecommerce Operations Manager |
| **Participants** | System (Middleware), DC Picker, Marketplace Courier |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Order Sync**: Middleware pulls orders from Lazada/Shopee APIs; creates Sales Orders in ERP | System | — | Automated |
| 2 | **ATP Verification**: System checks DC stock; if unavailable, system auto-notifies marketplace to cancel or delay | System | — | Automated |
| 3 | **Picking**: DC Picker receives marketplace pick task; scans each item | DC Picker | DC Supervisor | 10 min |
| 4 | **Packaging**: Items packed in marketplace-specific packaging; marketplace shipping labels printed from middleware | DC Packer | — | 5 min |
| 5 | **Handover**: Marketplace Courier (Lex/Shopee Xpress) picks up from DC; pickup confirmation synced to marketplace | DC Dispatch | — | 5 min |
| 6 | **Settlement**: Bi-weekly: Marketplace remits payment (net of commission/fees); Finance reconciles with ERP Sales Orders | Finance Clerk | Controller | 4 hours |

### System Touchpoints
- API integration (Middleware) for Order, Inventory, and Status sync
- Marketplace-specific shipping label generation
- Automated commission/fee deduction accounting

### Time Estimate
- Order sync and ATP verification: automated (real-time)
- Picking and packaging: ~15 min/order
- Handover to marketplace courier: ~5 min/batch
- Bi-weekly settlement reconciliation: 4 hours per cycle
- Monthly commission/fee audit: 2 hours/month

### Pain Points / Risks
- **Commission and fee opacity**: Lazada and Shopee deduct platform commission (2–5%), payment gateway fees, promotional contributions, and penalty fees (late shipping, order cancellation) from gross settlement before remitting net payment; reconciling net settlement to individual orders is extremely complex, and BuildRight typically cannot identify overcharged fees until the monthly deep reconciliation
- **Inventory sync lag causing overselling**: marketplace inventory sync via middleware has inherent latency (5–15 minutes); during flash sales or high-traffic events, marketplace sells items that BuildRight's DC has already allocated to other channels (POS, own website), resulting in forced cancellations, marketplace penalty fees, and seller rating damage
- **Marketplace seller rating sensitivity**: Lazada and Shopee algorithms penalize sellers with cancellation rates > 2% or late shipment rates > 5% by reducing search ranking and removing eligibility for flash sale events; a single inventory sync failure can cascade into weeks of reduced marketplace visibility and lost sales
- **Returns and dispute asymmetry**: marketplace platforms overwhelmingly side with the buyer in return disputes; BuildRight has limited ability to reject returns or contest "item not as described" claims, resulting in higher return rates on marketplace orders (~8–12%) compared to own-website orders (~3–5%)

### Staffing Implication
- **DC Pickers/Packers**: ~5,000–8,000 marketplace orders/month ÷ 30 days = ~170–270 orders/day; at ~15 min pick+pack per order, that's ~42–67 labor-hours/day across all DCs; absorbed within the existing DC pick/pack team that also handles W19 home delivery orders, as marketplace orders use the same pick/pack infrastructure
- **Finance Clerk (settlement reconciliation)**: bi-weekly settlement reconciliation (4 hours/cycle) + monthly commission/fee audit (2 hours/month) = ~10 hours/month; absorbed by existing Finance Clerk within W7 AP processing duties
- **Ecommerce Operations Manager**: oversees marketplace channel health, seller rating, and inventory sync; approximately 5–10 hours/week dedicated to marketplace operations including exception handling and promotional coordination; this is a shared responsibility within the existing Ecommerce Operations Manager role

---

## W210. E-commerce Fulfillment Hub (Dark Store) Operations

| Field | Detail |
|---|---|
| **Trigger** | High online order density in a specific urban zone; or DC congestion |
| **Frequency** | Daily operations |
| **Volume** | Covers selected "Strategic Stores" converted to Hubs; each hub processes ~150–300 online orders/day (vs. ~4 BOPIS orders/day at a standard store); initial rollout to 10–15 hubs in Metro Manila, Cebu, and Davao |
| **Owner** | Ecommerce Operations Manager |
| **Participants** | Hub Coordinator, Hub Pickers (3–5 per hub), Hub Packers (2–3 per hub), 3PL Couriers, Supply Planner, DC Dispatch |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Hub Inventory Reservation**: System prioritizes "Hub-specific" inventory for online orders; prevents "walk-in" sales of designated e-comm stock | System | — | Real-time |
| 2 | **Order Routing**: Intelligent routing engine assigns orders to the nearest Fulfillment Hub (Dark Store) to reduce last-mile cost (W19) | System | — | Real-time |
| 3 | **Wave Picking**: Hub Pickers perform batch picking (multiple orders simultaneously) using RF guns (W3) | Hub Picker | Hub Coordinator | 20 min/wave |
| 4 | **Packing & QC**: Items verified and packed in the store's "Dark Zone" (backroom or dedicated section) | Hub Packer | — | 5 min |
| 5 | **Dispatch**: 3PL Couriers (Lalamove/Transportify) pick up directly from store backroom; avoids DC bottleneck | DC Dispatch (at store) | — | 10 min |
| 6 | **Replenishment**: Hub inventory replenished via priority DC-to-Store "Push" (W154) to ensure high ATP | Supply Planner | — | Daily |

### Time Estimate
- Wave picking (batch of 10–15 orders): 20 min/wave
- Packing and QC: 5 min/order
- Courier dispatch coordination: 10 min/batch
- Hub Coordinator daily management: 4–6 hours/day
- Replenishment monitoring: 30 min/day per hub

### Pain Points / Risks
- **Dual identity conflict (store vs. hub)**: converted "Strategic Stores" must simultaneously serve walk-in customers and process high-volume online fulfillment from the same location; walk-in customers may find fast-selling items "reserved" for online orders (step 1), causing in-store customer complaints and potential lost sales at the physical shelf
- **Hub SKU assortment limitation**: dark stores stock only the ~2,000–3,000 fastest-moving ecommerce SKUs, not the full 35,000-SKU range; when online orders contain non-hub items, the routing engine must redirect to the nearest DC (W19) or another store (W19B), splitting the order and creating customer confusion
- **Hub picker staffing in tight labor market**: each hub requires 5–8 dedicated pickers/packers operating at ecommerce pace (vs. store replenishment pace); competing for warehouse labor in Metro Manila against pure-play e-commerce companies (Shopee, Lazada logistics) who pay premium wages makes hub staffing retention challenging
- **Priority replenishment competing with standard store replenishment**: hub replenishment via priority DC push (W154) consumes DC truck capacity and dock slots that would otherwise serve standard store replenishment (W4); during DC congestion periods, hub replenishment may crowd out replenishment for non-hub stores, causing stockouts in the broader network

### System Touchpoints
- Dark store / fulfillment hub inventory partitioning engine: reserves designated SKUs for online order fulfillment, preventing walk-in sale of hub-allocated stock (W210.1)
- Intelligent order routing engine: assigns ecommerce orders to the nearest fulfillment hub based on customer delivery address, hub ATP, and hub processing capacity (W210.2)
- Wave pick management system: batch picking with RF gun integration supporting multiple simultaneous order picks per wave (W210.3)
- 3PL carrier dispatch integration: automated courier booking and pickup scheduling from hub backroom, with real-time dispatch confirmation (W210.5)
- Priority replenishment integration with W154 (DC-to-store push): triggers priority replenishment when hub ATP falls below safety threshold; feeds into DC replenishment planning

### Staffing Implication
- **Hub Coordinator (1 per hub)**: full-time role managing 10–15 hubs = 10–15 Hub Coordinators; responsible for daily hub operations, picker/packer scheduling, courier coordination, and replenishment monitoring (4–6 hours/day operational + 2–3 hours/day admin/reporting); this is a new dedicated role not present in standard stores
- **Hub Pickers (3–5 per hub)**: each hub requires dedicated pickers operating at ecommerce pace (batch picking 10–15 orders per wave); 3–5 pickers/hub × 10–15 hubs = 30–75 dedicated Hub Pickers; these are additional headcount beyond standard store Stock Associates, as hub picking volume (~150–300 orders/day) far exceeds standard store BOPIS picking (~4 orders/day)
- **Hub Packers (2–3 per hub)**: dedicated packing and QC staff at each hub; 2–3 packers/hub × 10–15 hubs = 20–45 dedicated Hub Packers; may share personnel with Hub Pickers during volume fluctuations
- **DC Dispatch incremental load**: carrier coordination for hub dispatch adds to existing W19 dispatch duties; each hub generates ~150–300 dispatches/day requiring courier booking and handoff; absorbed by existing DC Dispatch team with possible 1 additional dispatcher during peak

---

## W215. Customer Home Delivery Reverse Logistics (Returns)

| Field | Detail |
|---|---|
| **Trigger** | Customer requests return or exchange for an item delivered to their home (W19/W19B) |
| **Frequency** | ~1–2% of home delivery orders |
| **Volume** | ~200–400 returns/month initially |
| **Owner** | Ecommerce Customer Service Manager |
| **Participants** | Customer, CSR, 3PL Carrier, DC Receiving Team, Finance (Refunds) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Return Request**: Customer initiates return via Web/App or Call Center; provides reason and photos of item/packaging | Customer | — | 10 min |
| 2 | **Validation**: CSR reviews request against Return Policy (W12); verifies purchase date and item condition; approves for pick-up | CSR | Ecommerce Ops Mgr | 15 min |
| 3 | **Collection Booking**: System books 3PL carrier (Lalamove/Transportify) for home pick-up; generates "Return Label" for customer | CSR / System | — | 5 min |
| 4 | **Pick-up**: Carrier collects item from customer; verifies "Return ID" and basic condition; issues "Proof of Collection" | 3PL Carrier | — | 10 min |
| 5 | **DC Receipt**: Item arrives at DC (or Hub); Receiving Clerk scans Return Label; system identifies original Order/SO | Receiving Clerk | DC Supervisor | 5 min |
| 6 | **Quality Inspection**: Quality Checker inspects item: (a) Resaleable → return to stock (W91); (b) Damaged → quarantine (W91); (c) Wrong item → flag for investigation | Quality Checker | — | 10 min |
| 7 | **Refund Authorization**: Once receipt is confirmed and QC passed: Finance authorizes refund to original payment method (W101) | Finance (AR) | Controller | 10 min |
| 8 | **Closure**: System notifies customer of refund status; updates inventory and sales analytics | System | — | Automated |

### System Touchpoints
- Online Return Merchandise Authorization (RMA) portal
- 3PL integration for reverse logistics booking
- Linkage between Return ID and original Order ID
- QC status integration with Refund trigger

### Time Estimate
- Customer return request initiation: 10 min (customer-driven)
- CSR return validation and policy check: 15 min
- 3PL carrier booking and return label generation: 5 min
- Carrier pickup from customer address: 10 min + transit time (1–3 days)
- DC receipt and return label scanning: 5 min
- Quality inspection (resalable / damaged / wrong item): 10 min/item
- Finance refund authorization: 10 min
- Customer refund notification and system closure: automated (instant)
- **Total elapsed time (return request to refund)**: 5–10 business days (carrier pickup transit + DC QC queue + refund processing)

### Pain Points / Risks
- **3PL reverse pickup cost**: scheduling a dedicated carrier pickup at the customer's home for a return costs PHP 150–400 per trip; for low-value items (e.g., a PHP 500 hand tool), the reverse logistics cost plus QC inspection plus refund processing can exceed the gross margin on the original sale, making the return a net loss
- **Return fraud and "wardrobing"**: customers returning used or partially consumed items (e.g., power tools used for a single project, paint cans returned half-empty) is difficult to detect during QC inspection; without serial number tracking and photographic evidence at original delivery, fraudulent returns erode margin
- **QC bottleneck at DC**: DC Receiving Team processes inbound returns alongside regular vendor deliveries and inter-DC transfers; returns require individual inspection (step 6) which takes 10 min/item; a spike in returns after a promotional event (W13) can create a QC backlog, delaying refunds and triggering customer complaints
- **Refund timing expectation vs. processing reality**: customers expect immediate refund upon carrier pickup, but refund is only authorized after DC receipt and QC pass (step 7); the 3–7 day gap between customer handing over the item and receiving the refund generates the majority of return-related CS contacts

### Staffing Implication
- **CSR (return validation and booking)**: ~200–400 returns/month × 20 min per return (validation + booking) = ~67–133 hours/month; distributed across the 30-person Ecommerce Customer Support team = ~2–4 hours/agent/month; absorbed within existing call center capacity
- **DC Receiving Team (QC inspection)**: ~200–400 returns/month × 10 min QC inspection per item = ~33–67 hours/month across 4 DCs = ~7–13 hours/DC/month; absorbed by existing DC Receiving Team as part of standard inbound processing, though post-promotional return spikes may require temporary overtime
- **Finance (AR) refund authorization**: ~200–400 refunds/month × 10 min per authorization = ~33–67 hours/month; absorbed by existing AR team within W101 refund processing duties
- **No incremental headcount at current volumes**; if return rate exceeds 3% of home delivery orders (driven by quality issues or marketplace expansion), a dedicated Returns Processing Clerk at each high-volume DC should be considered

---

## W246. Drop-Ship Vendor (DSV) Order Fulfillment

| Field | Detail |
|---|---|
| **Trigger** | Customer orders a specialty, custom, or bulk direct-ship item (custom glass panels, premium cabinets, industrial pumps) on website or POS |
| **Frequency** | ~200–400 orders/month chain-wide |
| **Volume** | Avg PHP 20,000–100,000 per order |
| **Owner** | Ecommerce Fulfillment Manager |
| **Participants** | System, Drop-Ship Vendor (DSV), CSR, virtual Receiving Clerk, Finance (AP) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Order Route**: Customer places order; system identifies SKU as Drop-Ship in Item Master; processes payment; split-routes order to generate back-to-back PO | System | — | Automated |
| 2 | **Vendor Intake**: PO automatically transmitted to the accredited Drop-Ship Vendor via EDI/Vendor Portal; vendor confirms stock and production timeline within 24 hours | Vendor | Ecommerce Fulfillment Mgr | 1 day |
| 3 | **Fulfillment & Labeling**: Vendor picks/produces item; prints co-branded BuildRight packing slip and co-branded shipping label from Vendor Portal | Vendor | — | 1–3 days |
| 4 | **Dispatch**: Vendor dispatches package directly to customer's address using co-branded carrier; enters tracking number in Vendor Portal | Vendor | — | 15 min |
| 5 | **Transit Sync**: System automatically imports tracking status via carrier APIs; triggers tracking updates and SMS alerts to the customer | System | — | Automated |
| 6 | **Virtual Receipt**: Upon carrier delivery confirmation (POD signature): system automatically posts a "Virtual Goods Receipt" in ERP; triggers sales revenue recognition | System | virtual Receiving Clerk | Automated |
| 7 | **Invoice & Reconciliation**: Vendor submits invoice via Portal; system performs 3-way match (PO vs. Virtual GR vs. Invoice); routes to AP for payment settlement (W7) | System / Finance | Accountant | 1 hour |

### System Touchpoints
- Drop-Ship SKU virtual classification in Item Master
- Back-to-back automated Purchase Order generator
- Vendor Portal/EDI integration for tracking sync and document print
- Automated Virtual Goods Receipt triggered by 3PL carrier API delivery status
- Integration with W2A/W2B (procurement), W7 (AP processing), and W19 (ecommerce delivery)

### Time Estimate
- Customer order placement and payment: 5–10 min (customer-driven)
- System order routing and back-to-back PO generation: automated (instant)
- Vendor PO receipt and stock/production timeline confirmation: 24 hours (vendor SLA)
- Vendor fulfillment (pick/produce) and labeling: 1–3 days (depends on item type)
- Vendor dispatch and tracking entry: 15 min (vendor-side)
- Transit and customer tracking updates: automated (ongoing, carrier-dependent)
- Virtual Goods Receipt upon delivery confirmation: automated (instant)
- Invoice submission and 3-way match reconciliation: 1 hour per invoice
- AP payment settlement: per W7 payment terms
- **Total elapsed time (order to delivery)**: 3–7 business days (vendor fulfillment dependent)

### Pain Points / Risks
- **Vendor fulfillment SLA non-compliance**: drop-ship vendors are typically smaller specialty manufacturers who may not have the operational discipline of BuildRight's DCs; vendor confirmation within 24 hours is not always met, and production timelines (1–3 days) can stretch to 5–7 days during the vendor's own peak periods, leaving BuildRight's customer waiting with no visibility into the delay
- **Co-branded packaging and labeling quality**: vendors print co-branded BuildRight packing slips and shipping labels from the Vendor Portal, but print quality, label adhesion, and packaging standards vary significantly across the 30–50 accredited DSVs; poor packaging or illegible labels reflect on BuildRight's brand, not the vendor's, creating brand risk that is difficult to police remotely
- **Virtual Goods Receipt accuracy**: the Virtual GR is triggered by carrier delivery confirmation (POD signature), not by physical inspection; if the customer receives a wrong or damaged item, the system has already recognized revenue and the vendor invoice is in the AP queue, requiring a W98 exception case and a vendor claim to unwind the transaction
- **Customer service gap for vendor-fulfilled orders**: when a customer contacts BuildRight support about a drop-ship order issue (delay, wrong item, damage), the CSR has no direct control over the vendor's fulfillment process; the CSR must contact the vendor via the Vendor Portal or phone, adding a communication layer that delays resolution compared to BuildRight-fulfilled orders
- **Vendor inventory visibility limitation**: BuildRight's system only shows the vendor's stock status at the point of PO creation; the vendor may accept the PO but subsequently run out of stock before shipping, particularly for items with long production lead times; BuildRight has no real-time visibility into the vendor's actual inventory position

### Staffing Implication
- **Ecommerce Fulfillment Manager**: oversees the DSV program including vendor onboarding, SLA monitoring, and exception escalation; ~200–400 orders/month × 10 min oversight/order = ~33–67 hours/month; this is a dedicated responsibility within the existing Ecommerce Fulfillment Manager role
- **Virtual Receiving Clerk**: the "virtual receiving" function (step 6) is automated — no physical goods pass through BuildRight's DC; the virtual Receiving Clerk role monitors Virtual GR exceptions (delivery discrepancies, missing POD) estimated at ~5–10% of DSV orders = ~10–40 exception cases/month × 15 min each = ~2.5–10 hours/month; absorbed by existing DC Receiving Team
- **Finance (AP)**: 3-way match reconciliation and payment settlement for ~200–400 DSV invoices/month × 1 hour each = ~200–400 hours/month shared across the AP team; DSV invoices are high-value (avg PHP 20,000–100,000) and require careful matching; at current volumes, absorbed by existing AP team within W7 processing

---

## W247. BOPIS Smart Locker & Queue Management

| Field | Detail |
|---|---|
| **Trigger** | Ecommerce BOPIS order picked and staged (W11) |
| **Frequency** | Ongoing (daily) |
| **Volume** | ~50–100 transactions per store/day |
| **Owner** | Store Customer Experience Supervisor |
| **Participants** | Store Picker, Customer, Pro Desk Associate |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Staging**: Store Picker picks BOPIS order (W11 step 4). Stages the items in an in-store **Smart Locker** or **Expedited Pick-up Counter** rather than the backroom. | Store Picker | Store Mgr | 5 min |
| 2 | **Locking & Sync**: Associate places the items in a designated smart locker; scans the locker QR code and links it to the order ID in the ERP system. | Store Associate | — | 3 min |
| 3 | **Notification**: Locker system triggers an automated pickup PIN code and QR code to the customer's email and mobile app (W11 step 6). | System | — | Automated |
| 4 | **Customer Arrival**: Customer arrives at the store. (a) For Smart Locker: Scans the QR/enters the PIN at the locker screen; the locker door pops open. (b) For Pickup Counter: Customer checks in on a tablet queueing screen; Pro Desk is alerted. | Customer | — | 2 min |
| 5 | **Reconciliation**: The locker door closing or the associate hand-off scan triggers a real-time order completion status in the ERP (W11 step 8). | System / Associate | Store Mgr | Automated |
| 6 | **Feedback Loop**: System sends an instant SMS survey asking for customer experience rating (CSAT W65). | System | — | Automated |

### System Touchpoints
- Smart Locker API integration (allocating locker space, tracking locker state)
- In-store check-in tablet/queuing system linked to Pro Desk alert system
- Real-time customer pickup notification (SMS/Email/App Push)
- Integration with W11 (BOPIS) and W65 (CSAT)

### Time Estimate
- BOPIS order picking and smart locker staging: 5 min pick + 3 min locker placement = 8 min/order
- Locker QR code scanning and order linking: 3 min/order
- Customer pickup PIN/QR notification delivery: automated (instant)
- Customer arrival and locker scan/counter check-in: 2 min (customer-driven)
- Order completion reconciliation (locker door close or handoff scan): automated (instant)
- CSAT survey delivery: automated (instant)
- **Total per-order processing time (picker + staging + customer pickup)**: ~13 min of staff time + customer arrival time
- **Customer experience time (arrival to item in hand)**: ~2 min for smart locker; ~5 min for counter pickup queue
- **Smart locker capacity mismatch**: smart locker banks are sized for average daily volume (~50–100 BOPIS orders/store/day) but during promotional events (W13), BOPIS volume can spike 3–5x; when all lockers are occupied, overflow orders must be staged at the counter, defeating the self-service locker experience and creating queue congestion at the Pro Desk
- **Oversized item limitations**: hardware/DIY BOPIS orders frequently include items that physically cannot fit in standard smart lockers (e.g., 4x8 plywood sheets, 50kg cement bags, ladders); these items must always be handled through the counter pickup queue, creating a dual-process complexity that confuses customers expecting a uniform locker experience
- **Locker maintenance and hardware reliability**: smart lockers in Philippine retail environments face humidity, dust, and heavy usage; electronic locks and QR scanners fail at an estimated 2–5% monthly rate per unit; a jammed locker with a customer's order inside requires manual override by the Store Associate, causing customer delays
- **PIN/QR code sharing and identity verification gap**: the smart locker system releases items to anyone with the pickup PIN or QR code; unlike counter pickup (W11 step 9) which requires ID verification, locker pickup has no identity check, increasing the risk of wrong-party pickup (e.g., family member picking up without customer authorization, or code intercepted via SMS)

### Pain Points / Risks
- Locker capacity constraints during peak periods (weekends, pay-day weekends)
- Customer forgetting pickup code or locker number
- Items too large for smart locker compartments
- Temperature-sensitive items spoiling in lockers (e.g., paint, adhesives in heat)
- System connectivity issues preventing locker opening
- Maintenance and cleaning of locker compartments

---

### Staffing Implication
- **Store Pickers**: smart locker staging (step 1–2) adds ~8 min per BOPIS order (5 min pick + 3 min locker staging) vs. ~7 min for standard BOPIS counter staging (W11 steps 4–6); at ~50–100 BOPIS orders/store/day, the incremental time is negligible and absorbed by existing Stock Associates
- **Pro Desk Associate**: at stores with smart lockers, the Pro Desk Associate handles counter queue check-ins for oversized items (step 4b) and occasional locker malfunction overrides; estimated 10–20 counter pickups/day for oversized items + 1–2 locker override incidents/day = ~30–50 min/day; absorbed by existing Pro Desk Associate as part of their customer service duties
- **No incremental headcount per store**; the smart locker system reduces CSR counter workload by shifting ~60–80% of BOPIS pickups to self-service locker retrieval, potentially freeing ~30–60 min/day of CSR time for other customer service tasks

## W266. Ecommerce Online Fraud Detection & Prevention

| Field | Detail |
|---|---|
| **Workflow ID** | W266 |
| **Name** | Ecommerce Online Fraud Detection & Prevention |
| **Trigger** | Online order placed on website/app (W11 / W19) |
| **Frequency** | Real-time, per online order (~1,500/day) |
| **Volume** | ~45,000 orders/month |
| **Owner** | Fraud Prevention Specialist |
| **Participants** | System (Rules Engine), Fraud Prevention Specialist (Reviewer), Customer Service Representative, Payment Gateways (PayMongo, Dragonpay) |
| **Time Estimate** | Automated check (instant); Manual review: 5–10 min/case |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Initial Transaction Screening**: Customer submits online order; payment gateway executes 3D Secure 2.0 (3DS) authentication and initial card security check. | Payment Gateway / System | — | Automated |
| 2 | **Risk Evaluation**: ERP Fraud Rules Engine scores transaction based on pre-defined criteria: (a) device fingerprinting score, (b) IP location mismatch vs. shipping address, (c) high-risk email domain / guest checkout status, (d) purchase velocity per IP/email/card, (e) bulk high-risk SKUs in cart (e.g. power tools, copper wires). | System | Fraud Specialist | Automated |
| 3 | **Order Queue Routing**: System routes order based on risk score threshold: (a) Low Risk (<50): Auto-approved, sent to picking queue (W11/W19); (b) Medium Risk (50–85): Held in fraud queue, email notification to specialist; (c) High Risk (>85): Auto-cancelled and blocked. | System | — | Automated |
| 4 | **Manual Fraud Review**: Fraud Prevention Specialist reviews medium-risk held orders: (a) cross-checks social media matching or directory listings, (b) checks address validation maps, (c) reviews previous order history for matching device fingerprint. | Fraud Specialist | Fraud Specialist | 5 min |
| 5 | **Customer Out-of-Band Verification**: If card/billing remains suspect, Specialist contacts customer via phone/email to verify order details (e.g. request proof of ID or secondary contact verification). | CSR / Fraud Specialist | Fraud Specialist | 5 min |
| 6 | **Dispositions & Releases**: Specialist records decision in dashboard: (a) Approved: releases order to picking queue; (b) Rejected: cancels order, initiates automatic payment void/refund per W101, and updates system blacklist. | Fraud Specialist | Store Mgr / Director | 2 min |
| 7 | **Feedback Loop & Machine Learning**: System logs confirmed fraud or chargebacks to the blacklist table (IP, email, card hash, shipping address); updates rules engine parameters to adjust weights. | System | Fraud Specialist | Automated |

### System Touchpoints
- Real-time Fraud Scoring Engine API integration
- Fraud Review Queue and Management Dashboard within Order Management Module
- Acquirer chargeback and dispute feed integration (T+1)
- Integration with W11 (BOPIS), W19 (Home Delivery), and W101 (Refunds & Credit Processing)

### Success Metrics / KPIs
- Auto-approval rate: > 97% of total orders
- False positive rate (declining legitimate transactions): < 0.5%
- Chargeback rate on ecommerce transactions: < 0.1% (target)
- Manual review queue clearing SLA: < 30 minutes

### Risks & Exceptions
- **System Downtime**: If the fraud scoring API is down, orders over PHP 25,000 are placed on manual review hold; orders under PHP 25,000 auto-approved to avoid checkout blockage.
- **High-Value Corporate Purchases**: Corporate buyers placing bulk orders are whitelisted based on validated corporate taxpayer identification number (TIN) and verified corporate accounts (W58).

### Time Estimate
- Initial transaction screening and risk scoring (steps 1–2): automated (instant, < 1 second per order)
- Order queue routing (step 3): automated (instant)
- Manual fraud review for medium-risk orders (step 4): 5 min/case
- Customer out-of-band verification (step 5): 5 min/case (applies to ~10–20% of manual reviews)
- Disposition and order release/rejection (step 6): 2 min/case
- Feedback loop and blacklist update (step 7): automated (instant)
- **Manual review workload**: ~3% of ~45,000 orders/month = ~1,350 reviews/month × 5 min each = ~112 hours/month
- **Manual review queue clearing SLA**: < 30 minutes per held order (from queue entry to disposition)

### Pain Points / Risks
- **False positives on legitimate high-value orders**: power tools, appliances, and construction materials frequently trigger fraud scoring because of high order values (PHP 20,000–100,000+) and first-time customer behavior; manually reviewing these medium-risk orders (5 min/case) at ~3% of ~45,000 orders/month = ~1,350 manual reviews/month, consuming ~112 hours/month of Fraud Specialist time
- **Filipino payment method fragmentation**: GCash, Maya, bank transfers (via Dragonpay), credit cards, and over-the-counter payments each have different fraud profiles and dispute resolution mechanisms; tuning the fraud rules engine across all payment methods without generating excessive false positives requires continuous refinement
- **Chargeback cost double-hit**: on confirmed fraud, BuildRight loses both the merchandise (shipped and unrecoverable) and the payment (chargeback from card issuer); average fraud loss per incident on hardware/DIY items is PHP 8,000–15,000; at a 0.1% fraud rate target on ~45,000 orders, that is ~45 incidents/month × PHP 10,000 = ~PHP 450K/month potential exposure
- **3D Secure 2.0 friction and cart abandonment**: mandatory 3DS authentication adds a step to checkout that causes an estimated 10–15% of customers to abandon their cart; balancing fraud prevention with checkout conversion is a continuous tension, especially during promotional events (W13) where checkout speed is critical

### Staffing Implication
- **Fraud Prevention Specialist**: ~1,350 manual reviews/month (3% of 45,000 orders) × 5 min each = ~112 hours/month; at full capacity (160 hours/month), a single Fraud Specialist can handle this volume with ~48 hours/month remaining for rules engine tuning, blacklist management, and reporting; 1 dedicated Fraud Prevention Specialist is required — this is a new specialized role not covered by existing CSR or Finance positions
- **CSR support for customer verification (step 5)**: ~10–20% of manual reviews require out-of-band customer contact = ~135–270 calls/month × 5 min each = ~11–23 hours/month; absorbed by the 30-person Ecommerce Customer Support team as part of their existing duties
- **During promotional events (W13)**: order volume can spike 3–5x, increasing manual review cases proportionally to ~4,000–6,750 reviews/month; this exceeds 1 Fraud Specialist's capacity; during planned promotions, a second Fraud Specialist or a trained backup from the Ecommerce Customer Support team should be assigned to fraud review for the event duration

---

## W267. Ecommerce Digital Payment Reconciliation & Dispute Handling

| Field | Detail |
|---|---|
| **Workflow ID** | W267 |
| **Name** | Ecommerce Digital Payment Reconciliation & Dispute Handling |
| **Trigger** | Daily payment gateway settlement payout or chargeback notification from gateway/acquirer |
| **Frequency** | Daily reconciliation; Ongoing dispute handling |
| **Volume** | ~45,000 online transactions/month; ~10–20 disputes/month |
| **Owner** | AR & Settlement Accountant |
| **Participants** | AR & Settlement Accountant (1), Payment Gateways (PayMongo, Dragonpay, PayPal), Treasury Analyst, Customer Service Representative |
| **Time Estimate** | 30–45 min/daily settlement; 1–2 hours/dispute case |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Settlement Report Import**: System automatically pulls daily settlement reports from online payment gateways (PayMongo, Dragonpay) via API/SFTP; imports transaction-level details (gross, MDR fee, net payout). | System | Treasury Analyst | Automated |
| 2 | **Auto-Reconciliation 3-Way Match**: System runs match engine: (a) matches online order status "Paid" vs. settlement report transaction ID vs. cash deposit on bank statement (net of MDR fees); (b) flags unmatched transactions or fee discrepancies. | System | AR Accountant | Automated |
| 3 | **Fee Variance Audit**: AR Accountant reviews flagged fee variances: verify if MDR matches negotiated rates (e.g. 1.0% for e-wallets, 2.5% for credit cards); routes fee discrepancies to Treasury Analyst for dispute. | AR Accountant | Treasury Analyst | 10 min |
| 4 | **Dispute / Chargeback Notification**: System receives chargeback notification from gateway/acquirer; creates a payment dispute case in ERP; puts original transaction order on "payment hold". | System | AR Accountant | Automated |
| 5 | **Dispute Investigation**: AR Accountant gathers transaction evidence: (a) order details, (b) digital Proof of Delivery (POD) with customer signature/photos (W268), (c) customer interaction logs (W258). | AR Accountant | AR Supervisor | 30 min |
| 6 | **Dispute Submission**: AR Accountant uploads evidence to gateway/acquirer merchant portal within the representment window (typically 5–10 business days). | AR Accountant | AR Supervisor | 15 min |
| 7 | **Dispute Resolution & Posting**: Once the acquirer makes a ruling: (a) If won: Acquirer releases held funds; system posts debit to Cash-in-Transit / credit to Clearing account; (b) If lost: Acquirer retains funds; system posts debit to chargeback expense / credit to Clearing account; triggers blacklist update per W266.7. | AR Accountant / System | Controller | 15 min |

### System Touchpoints
- Gateway API integrations for daily payout settlement files (Dragonpay, PayMongo, PayPal)
- Automated 3-way matching engine within Accounts Receivable module
- Acquirer chargeback dispute portal integration
- Integration with W99 (Payment Settlement Reconciliation) and W101 (Refunds & Credit Processing)

### Success Metrics / KPIs
- Auto-reconciliation matching rate: > 99.5%
- Average time to submit dispute evidence: < 48 hours
- Dispute win rate on credit card chargebacks: > 60%
- Outstanding reconciliation items aging > 7 days: 0 items (target)

### Risks & Exceptions
- **Refund-Chargeback Double Hit**: If a customer files a chargeback after a refund was already initiated, AR Accountant uploads the refund confirmation transaction hash to the portal immediately to cancel the chargeback.
- **Acquirer Net Settlement Deductions**: Acquirer deducts chargeback amount from daily payout before dispute resolution; ERP routes this deduction to a temporary "Chargeback Clearing Account" to maintain cash ledger alignment.

### Time Estimate
- Settlement report import and auto-reconciliation (steps 1–2): automated (instant; ~5 min/day to review flagged items)
- Fee variance audit (step 3): 10 min per flagged item; ~5–10 flagged items/day = ~50–100 min/day
- Chargeback notification and case creation (step 4): automated (instant)
- Dispute investigation — evidence gathering (step 5): 30 min/case
- Dispute submission to acquirer portal (step 6): 15 min/case
- Dispute resolution and GL posting (step 7): 15 min/case
- **Daily settlement reconciliation**: 30–45 min/day for AR Accountant to review auto-reconciliation results, audit fee variances, and resolve unmatched transactions
- **Per dispute case**: 1–2 hours total (investigation + submission + resolution posting); ~10–20 disputes/month = ~15–30 hours/month
- **Total monthly effort**: ~25–45 hours/month (daily reconciliation + dispute handling)

### Pain Points / Risks
- **MDR fee complexity across multiple gateways**: each payment gateway (PayMongo for cards/e-wallets, Dragonpay for bank transfers/OTC, PayPal for international) applies different MDR rates (1.0% for e-wallets, 2.5% for credit cards, 3.5–4.5% for PayPal) with different settlement cycles (T+1 to T+3); reconciling ~45,000 transactions/month across these gateways requires meticulous matching, and the automated 3-way match engine still flags ~2–5% of transactions daily for manual review
- **Chargeback representment evidence burden**: winning a chargeback dispute requires comprehensive evidence (delivery POD with signature/photos from W268, customer interaction logs from W258, order details) assembled within a 5–10 business day window; for BuildRight's hardware/DIY orders averaging PHP 3,000–5,000 with some exceeding PHP 50,000, the effort per dispute is significant and the ~60% win rate means ~40% of disputed amounts are permanent losses
- **Settlement timing gaps across gateways**: PayMongo settles T+1, Dragonpay settles T+2 to T+3, and PayPal settles on a rolling weekly basis; during high-GMV periods (payday sales, 11.11, 12.12), the AR Accountant must reconcile across multiple settlement dates simultaneously, increasing the risk of missed discrepancies and unreconciled items aging beyond the 7-day target
- **Unreconciled transaction aging**: when the auto-reconciliation engine cannot match a settlement line to an order (partial refunds, split payments, gateway errors), the unmatched item sits in a clearing account; if not resolved within 7 days, it distorts the cash ledger and complicates month-end close (W9A); at ~2–5% daily flag rate on ~1,500 transactions/day, that is ~30–75 unmatched items/day requiring manual investigation

### Staffing Implication
- **AR & Settlement Accountant (1)**: daily settlement reconciliation takes 30–45 min/day (~10–15 hours/month); dispute investigation and submission for ~10–20 disputes/month × 1.5 hours average = ~15–30 hours/month; total ~25–45 hours/month; this is a dedicated role within the existing AR team, consuming roughly 30% of one Accountant's monthly capacity
- **Treasury Analyst**: fee variance escalation review ~5–10 flagged items/month × 10 min each = ~1–2 hours/month; absorbed within existing Treasury Analyst duties as part of W30 daily cycle
- **CSR (dispute evidence support)**: gathering customer interaction logs and delivery evidence for ~10–20 disputes/month × 10 min each = ~2–3 hours/month; absorbed by existing Ecommerce Customer Support team
- **No incremental headcount at current dispute volumes**; if dispute volume exceeds 50/month (driven by fraud spikes or delivery quality issues), a second AR Accountant with payment reconciliation specialization should be considered

---

## W509. Ecommerce Product Return Inspection, Grading & Disposition

| Field | Detail |
|---|---|
| **Trigger** | Returned ecommerce item arrives at DC or designated store for inspection |
| **Frequency** | ~8,000–12,000 returned items/month (ecommerce return rate ~4–6%) |
| **Volume** | ~10,000 items/month average; peaks post-holiday and post-promo (+40%) |
| **Owner** | Returns Processing Supervisor (DC) |
| **Participants** | Returns Inspector, Category Specialist, AP Clerk (for vendor returns) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Returned item received at DC returns processing area; Returns Inspector scans return order barcode; system retrieves original order details, item SKU, return reason, and customer-reported condition | Returns Inspector | Returns Supervisor | 2 min |
| 2 | Returns Inspector performs physical inspection against grading criteria: (a) Sealed/original packaging intact → proceed to Grade A check; (b) Opened but undamaged → detailed inspection; (c) Damaged packaging or item → Grade C candidate | Returns Inspector | Returns Supervisor | 3 min |
| 3 | Grade A assessment: item is unused, all accessories/manuals present, original tags attached, packaging intact; confirmed Grade A → system updates inventory status to "available" and returns to saleable stock | Returns Inspector | Returns Supervisor | 2 min |
| 4 | Grade B assessment: item is unused but packaging opened, minor cosmetic damage to packaging, missing non-essential accessory; confirmed Grade B → system creates discount listing on ecommerce "open box" section at 10–25% discount; inventory status "open-box available" | Returns Inspector | Category Specialist | 5 min |
| 5 | Grade C assessment: item is damaged, defective, missing essential components, or customer-reported malfunction; confirmed Grade C → system routes to disposition decision | Returns Inspector | Returns Supervisor | 3 min |
| 6 | Grade C disposition decision: (a) Vendor-attributable defect → initiate RTV (W88) with defect documentation; (b) Repairable (power tools, appliances) → route to service center (W440); (c) Non-recoverable → write-off with inventory adjustment (W92) | Category Specialist | Returns Supervisor | 5 min |
| 7 | System records grading decision with inspector ID, timestamp, photos, and grading rationale; updates inventory status accordingly | System | — | Automated |
| 8 | Weekly: Returns Supervisor reviews return grading dashboard: Grade A/B/C distribution by category, return reason correlation with grading, vendor defect rate from Grade C RTVs; identifies vendors with >10% defect rate for CAPA (W110) | Returns Supervisor | VP Ecommerce | 2 hours/week |
| 9 | Monthly: system calculates return-to-saleable conversion rate (Grade A %); tracks by category and vendor; feeds into vendor scorecard (W44) and category performance (W102) | System | — | Automated |

### System Touchpoints
- Return order barcode scan with original order retrieval (ECOM-017)
- Grading criteria checklist per product category with guided decision workflow (ECOM-017)
- Inventory status update per grading decision (available, open-box, pending disposition, written off) (ECOM-017)
- Open-box discount listing creation on ecommerce platform (ECOM-017)
- RTV initiation for vendor-attributable defects with evidence package (W88, ECOM-017)
- Repair routing to service center for repairable items (W440)
- Return grading dashboard with A/B/C distribution analytics (ECOM-017)
- Return-to-saleable conversion rate tracking by category and vendor (ECOM-017)
- Integration with vendor CAPA (W110) and vendor scorecard (W44)

### Time Estimate
~5–12 minutes per item depending on complexity. At ~10,000 items/month = ~830–2,000 staff-hours/month. Requires 5–12 Returns Inspectors at DC (absorbed within DC headcount of 150/DC).

### Pain Points / Risks
- Subjective grading between Grade A and Grade B leads to inconsistent restocking decisions — mitigated by category-specific grading criteria with photo examples
- Open-box inventory cannibalizes new product sales — mitigated by limiting open-box to ecommerce channel with clear "open box" labeling
- Vendor disputes RTV grading and refuses credit — mitigated by photo evidence and defect documentation at inspection

### Staffing Implication
- Returns processing requires ~5–8 dedicated Returns Inspectors at the primary DC; absorbed within DC headcount.
- 1 Returns Processing Supervisor at primary DC; absorbed within DC management.

---

## W510. Ecommerce Product Review & Rating Management

| Field | Detail |
|---|---|
| **Trigger** | Customer submits product review; or scheduled weekly review moderation |
| **Frequency** | ~2,000–3,000 new reviews/month across 35,000 SKUs |
| **Volume** | ~2,500 average/month; peaks 2 weeks after major promo (+50%) |
| **Owner** | Digital Content Manager |
| **Participants** | Customer Experience Representative, Category Manager, Vendor Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Customer submits product review via ecommerce platform after verified purchase (post-delivery email prompt or product page review form); review includes star rating (1–5), text, and optional photos | Customer | — | 5 min |
| 2 | System validates: purchase verification (order number match), review completeness (minimum rating and text), duplicate detection (one review per SKU per customer), profanity and inappropriate content filter | System | — | Automated |
| 3 | If auto-filter flags content: review enters manual moderation queue; Digital Content Representative reviews for policy compliance (no hate speech, no personal information, no competitor mentions, no spam); approve, reject, or edit | Content Rep | Digital Content Manager | 5 min/review |
| 4 | If review passes auto-filter: published to product page within 24 hours; rating incorporated into SKU's average rating displayed on product page, search results, and Google Shopping feed | System | — | Automated |
| 5 | If negative review (1–2 stars): system auto-generates customer experience ticket (W258); CX Representative contacts customer within 48 hours to understand issue and offer resolution | System / CX Rep | CX Manager | 15 min/ticket |
| 6 | CX Representative drafts public vendor response for applicable reviews; response posted alongside customer review on product page | CX Rep | Digital Content Manager | 10 min/response |
| 7 | Weekly: Digital Content Manager reviews review analytics: average rating by category, review velocity (reviews per SKU per week), sentiment trend, top-flagged SKUs by negative review volume | Digital Content Manager | VP Ecommerce | 2 hours |
| 8 | Monthly: system identifies SKUs with average rating <3.0 stars AND >5 reviews → auto-alerts Category Manager for product quality investigation; Category Manager coordinates with vendor for corrective action (W110) | System | Category Manager | Automated |
| 9 | Quarterly: Digital Content Manager compiles vendor feedback report: aggregate vendor rating, recurring quality themes from reviews, review response rate; shares with Vendor Manager for JBP discussions (W155) | Digital Content Manager | VP Ecommerce | 4 hours/quarter |

### System Touchpoints
- Verified purchase review validation (ECOM-018)
- Automated content moderation with profanity filter and policy rules (ECOM-018)
- Manual moderation queue with approve/reject/edit workflow (ECOM-018)
- Star rating aggregation per SKU displayed on product page and search results (ECOM-018)
- Negative review auto-escalation to CX ticketing system (W258, ECOM-018)
- Review analytics dashboard with rating, velocity, sentiment, and flagging metrics (ECOM-018)
- Low-rated SKU alerting with vendor feedback loop (ECOM-018, W110)
- Integration with PIM (W50) for review display on product content pages
- Integration with Google Shopping feed for review syndication (W316)

### Time Estimate
Moderation: ~5 min/review × ~500 flagged/month = ~42 hours/month. CX follow-up: ~15 min × ~300 negative reviews/month = ~75 hours/month. Analytics: ~2 hours/week = ~8 hours/month. Total: ~125 staff-hours/month.

### Pain Points / Risks
- Fake or incentivized reviews inflating product ratings — mitigated by verified purchase requirement and fraud detection algorithms
- Review bombing of specific products by competitors — mitigated by velocity monitoring and manual review for sudden spikes
- Negative review response creates legal liability if acknowledging product defect — mitigated by Legal-approved response templates

### Staffing Implication
- 2–3 Digital Content Representatives within Digital Commerce entity (absorbed from existing team).
- Negative review follow-up absorbed by existing CX Representatives (call center team of 30).

---

## W557. E-Commerce Abandoned Cart Recovery & Retargeting

| Field | Detail |
|---|---|
| **Trigger** | Cart abandonment event (customer adds items to cart but does not complete checkout within 30 minutes) |
| **Frequency** | Continuous, ~15,000–20,000 abandoned carts per month (~35–40% of all carts initiated) |
| **Volume** | Higher during promotional periods (3x during 11.11, 12.12, Payday Sales); BOPIS carts have lower abandonment (15%) vs. home delivery (50%) |
| **Owner** | Digital Marketing Manager / E-Commerce Manager |
| **Participants** | Digital Marketing Specialist (R), E-Commerce Manager (A), CRM Analyst (C for segmentation), Content Designer (C for email templates) |

### Background

W83 covers marketing campaign planning, execution, and performance measurement. W50 covers product information management (PIM) including digital content. W156 covers the customer data platform for hyper-personalization. W266 covers ecommerce fraud detection and prevention. However, no workflow covers abandoned cart recovery and retargeting — the automated sequence of communications triggered when a customer abandons their cart, designed to recover the sale through reminders, incentives, and retargeting ads. For an e-commerce channel targeting PHP 150M/month GMV with ~35% cart abandonment, recovering even 5–10% of abandoned carts represents PHP 26–52M additional monthly revenue. Philippine e-commerce consumers are price-sensitive and respond strongly to discount-based recovery offers and free shipping incentives.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Cart abandonment detected by e-commerce platform (30-minute inactivity threshold; excluded: carts under PHP 500, guest checkouts without email/mobile) | System | — | Automated |
| 2 | System checks customer consent (RA 10173 per W405 privacy master) — only enrolled loyalty members or registered customers with marketing consent receive recovery communications | System | — | Automated |
| 3 | **First touch (1 hour after abandonment)**: personalized push notification via BuildRight app or SMS — "Your cart is waiting! Items in [category] are selling fast." | System | Digital Marketing Specialist | Automated |
| 4 | **Second touch (6 hours)**: email with cart summary, item images, and personalized message — "Still thinking about it? Your [item names] are reserved for 24 hours." | System / Content Designer | Digital Marketing Manager | Automated |
| 5 | **Third touch (24 hours, if cart still abandoned)**: email with incentive offer — (a) Free shipping if cart > PHP 3,000, or (b) 5% discount code (single-use, 48-hour validity), or (c) loyalty bonus points (2x earning for 7 days) | System / Content Designer | E-Commerce Manager | Automated |
| 6 | Incentive rules engine applies customer-segment-specific offers: new customers get discount, returning customers get free shipping, VIP members get double points; segment data sourced from CDP (W156) | System / CRM Analyst | E-Commerce Manager | Automated |
| 7 | Retargeting ad activation: abandoned product SKUs added to Facebook/Meta and Google Display Network retargeting pool per W83 campaign management | System / Digital Marketing Specialist | Digital Marketing Manager | 15 min |
| 8 | Recovery tracking: if customer completes purchase from recovery communication, attribute conversion to recovery sequence in analytics; log recovery touchpoint (first, second, third) and incentive type used | System | Digital Marketing Specialist | Automated |
| 9 | Weekly unrecovered cart analysis: review top abandoned categories and SKUs — identify root causes (high shipping cost, out-of-stock, pricing, checkout friction); feed findings into UX improvement backlog | Digital Marketing Specialist / CRM Analyst | E-Commerce Manager | 2 hours/week |
| 10 | Monthly recovery performance dashboard: recovery rate by touch point, incentive cost vs. revenue recovered, abandoned cart trend, top abandoned SKUs | CRM Analyst | Digital Marketing Manager | 2 hours/month |
| 11 | Quarterly optimization: A/B test subject lines, timing, incentive types; update recovery sequence based on results; adjust segment-specific offers based on conversion data | Digital Marketing Specialist / CRM Analyst | E-Commerce Manager | 6 hours/quarter |
| 12 | Annual recovery program ROI calculation feeding into W565 (marketing ROI analysis): total recovered revenue, total incentive cost, net incremental revenue, recovery rate trend | Digital Marketing Specialist | E-Commerce Manager | 4 hours/year |

### System Touchpoints

- ECOM-019 (new requirement for abandoned cart recovery engine with multi-touch communication sequence)
- ECOM-006 (payment gateway — checkout abandonment point and payment failure data)
- CRM-007 (marketing campaign integration — retargeting ad activation)
- W83 (campaign management — Facebook/Meta and Google Display Network ad activation)
- W156 (customer data platform — customer segmentation for personalized offers)
- W50 (PIM — product content and images in recovery emails)
- NFR-010 (data privacy — RA 10173 consent management and marketing opt-in verification)
- POS-045 (unified order management — recovered order fulfillment)

### Time Estimate

- Automated sequence runs continuously (no manual intervention per trigger)
- Weekly unrecovered cart analysis: ~2 hours/week
- Monthly recovery dashboard: ~2 hours/month
- Quarterly optimization: ~6 hours/quarter
- Annual ROI calculation: ~4 hours/year
- **Total**: ~120–130 person-hours/year for Digital Marketing Specialist and CRM Analyst

### Pain Points / Risks

- **Omnichannel delivery complexity**: Philippine consumers use multiple messaging platforms (SMS, Viber, Messenger, email) requiring omnichannel delivery; each channel has different delivery reliability and cost
- **Discount fatigue**: frequent promotional events (Payday Sales, 11.11, 12.12) reduce recovery offer effectiveness — customers may wait for the next sale instead of responding to recovery incentives
- **SMS delivery reliability**: varies by carrier (Globe, Smart) with delivery rates fluctuating during peak periods; critical for first-touch push notifications
- **Guest checkout limitation**: abandoned cart data quality depends on customer login rate — guest checkouts have no contact info and cannot receive recovery communications
- **RA 10173 consent constraints**: recovery communications limited to enrolled customers with marketing consent, excluding a significant portion of guest and non-loyalty shoppers

### Staffing Implication

- **Digital Marketing Specialist**: ~80–100 hours/year for monitoring, optimization, and analysis. Absorbed within existing Digital Marketing Specialist role.
- **CRM Analyst**: ~30–40 hours/year for segmentation and analytics. Absorbed within existing CRM Analyst role.
- **No incremental headcount**.

---

## W563. E-Commerce SEO & Digital Merchandising Management

| Field | Detail |
|---|---|
| **Trigger** | Weekly SEO review cycle; product content update; search algorithm change (Google core update); keyword ranking drop; new product category launch |
| **Frequency** | Weekly SEO review; continuous optimization; monthly comprehensive audit |
| **Volume** | 35,000 SKUs requiring SEO metadata; ~500–1,000 keyword optimizations per month; ~50–100 content refreshes per week |
| **Owner** | Digital Content Manager / SEO Specialist |
| **Participants** | SEO Specialist (R), Digital Content Manager (A), Product Content Writer (R), E-Commerce Manager (C), Category Manager (C for product knowledge) |

### Background

W50 covers product information management (PIM) including digital content standards. W316 covers digital asset and product content master governance. W252 covers centralized item master creation. W564 covers new product introduction rollout to stores. However, no workflow covers e-commerce SEO and digital merchandising management — the ongoing optimization of 35,000 product pages for search engine visibility, organic traffic acquisition, and on-site search relevance. For a Philippine hardware e-commerce platform with PHP 150M/month GMV, organic search is the primary customer acquisition channel (estimated 40–50% of traffic). The Philippine hardware/DIY search landscape is dominated by generic queries ("cement price Philippines", "power tools online", "tiles for sale") where BuildRight must compete with both general marketplaces (Lazada, Shopee) and specialty competitors.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Weekly keyword performance review: Google Search Console data pull for BuildRight.com.ph — track rankings, impressions, click-through rates, and positions for top 500 keywords | SEO Specialist | Digital Content Manager | 2 hours |
| 2 | Identify declining rankings (dropped > 5 positions week-over-week) and rising opportunities (page 2 keywords approaching page 1); prioritize optimization targets | SEO Specialist | Digital Content Manager | 1 hour |
| 3 | Product page audit: sample 50 product pages per week for SEO quality — title tags, meta descriptions, H1 tags, alt text, schema markup (Product, AggregateRating, Offer) | SEO Specialist | Digital Content Manager | 3 hours |
| 4 | On-site search analysis: review BuildRight.com.ph internal search logs — top 100 queries, zero-result searches, low-click searches; identify content gaps and navigation issues | SEO Specialist | E-Commerce Manager | 2 hours |
| 5 | Content gap analysis: identify high-search-volume keywords where BuildRight has no ranking page — create content briefs for Product Content Writer with target keyword, content format, and competitive benchmark | SEO Specialist | Digital Content Manager | 3 hours |
| 6 | Product Content Writer optimizes pages per brief: keyword-rich titles, benefit-focused descriptions, specification tables, FAQ sections, how-to guides for DIY categories | Product Content Writer | Digital Content Manager | 20 hours/week |
| 7 | Category page optimization: update category landing pages with seasonal content (per W264 seasonal calendar), curated collections, and buyer's guides | Product Content Writer / SEO Specialist | Digital Content Manager | 4 hours/week |
| 8 | Technical SEO coordination with IT: page speed optimization, mobile responsiveness, structured data errors, crawl budget optimization, XML sitemap management | SEO Specialist / IT | E-Commerce Manager | 4 hours/week |
| 9 | Local SEO: update Google Business Profile for all 200 stores with accurate hours, services, photos, and BOPIS availability per W254 (location master) | SEO Specialist | Digital Content Manager | 2 hours/week |
| 10 | Monthly comprehensive SEO report: organic traffic, keyword rankings, conversion rate from organic, revenue attribution, competitor benchmark (vs. Ace Hardware, CitiHardware, Wilcon) | SEO Specialist | E-Commerce Manager | 2 hours |
| 11 | Quarterly SEO strategy review: update keyword targets, content calendar, and technical roadmap; align with merchandising priorities and seasonal calendar (W264) | SEO Specialist / Digital Content Manager | E-Commerce Manager | 4 hours/quarter |
| 12 | Annual SEO audit: full technical crawl, content quality assessment, backlink profile review, algorithm update impact analysis; benchmark against prior year performance | SEO Specialist | E-Commerce Manager | 16 hours/year |

### System Touchpoints

- ECOM-020 (new requirement for SEO & digital merchandising management dashboard)
- ECOM-009 (product catalog sync — catalog data source for product pages)
- MDM-002 (item attribute management — attribute data for SEO metadata)
- MDM-025 (digital asset master — image/video optimization for alt text and file naming)
- W50 (PIM — product content repository for content optimization)
- W316 (digital asset master — asset management for media optimization)
- W564 (NPI store rollout — new product content triggers SEO optimization)
- W254 (location master — local SEO data for Google Business Profile)
- W264 (seasonal transition — seasonal content alignment)

### Time Estimate

- Weekly review (steps 1–4): ~8 hours/week
- Content optimization (steps 5–7): ~27 hours/week
- Technical SEO (step 8): ~4 hours/week
- Local SEO (step 9): ~2 hours/week
- Monthly report: ~2 hours
- Quarterly strategy: ~4 hours/quarter
- Annual audit: ~16 hours
- **Total**: ~110–130 person-hours/month

### Pain Points / Risks

- **Thin content at scale**: 35,000 SKUs means most product pages have thin content (manufacturer descriptions only); creating unique, optimized content for all SKUs is resource-intensive
- **Marketplace SEO dominance**: competing with Lazada/Shopee marketplace SEO which benefits from higher domain authority and broader keyword coverage
- **Core Web Vitals compliance**: Google's requirements challenge heavy product pages with multiple images, specification tables, and embedded content
- **Mixed-language search behavior**: Filipino consumer search behavior mixes English and Filipino keywords, requiring bilingual keyword strategy
- **Strong local competitors**: Wilcon, CitiHardware, and Ace Hardware have strong brand recognition and dedicated SEO investment in the Philippine hardware space

### Staffing Implication

- **SEO Specialist**: full-time role dedicated to SEO optimization, keyword research, and technical SEO coordination. Existing role within Digital Commerce entity.
- **Product Content Writer**: ~20 hours/week on SEO content optimization. Absorbed within existing Product Content Writer role.
- **Digital Content Manager**: ~4–6 hours/week on review and strategy. Absorbed within existing role.
- **No incremental headcount**.

---

## W568. E-Commerce Flash Sale & Limited-Time Offer Operations

| Field | Detail |
|---|---|
| **Trigger** | Flash sale event scheduled (Payday Sale, 11.11, 12.12, Lazada/Shopee birthday sale, BuildRight anniversary sale, clearance event) |
| **Frequency** | ~2–4 flash sales per month (1–2 BuildRight proprietary, 1–2 marketplace-partnered) |
| **Volume** | Each sale generates 5,000–15,000 orders in 24–48 hours (vs. ~1,400 daily average); 3–5x normal traffic |
| **Owner** | E-Commerce Operations Manager |
| **Participants** | E-Commerce Manager (A), Digital Marketing Specialist (R), Category Manager (C for pricing), Supply Planning Manager (C for inventory), IT Operations (C for infrastructure), Customer Service Lead (C for support surge) |

### Background

W13 covers promotional pricing execution including campaign setup, pricing, and performance measurement. W98 covers e-commerce order exception and cancellation management. W266 covers e-commerce fraud detection. W57 covers promotional stock allocation and pre-positioning. However, no workflow covers the operational execution of flash sales — the unique challenges of time-limited high-volume events including: inventory pre-reservation, traffic surge infrastructure preparation, real-time inventory monitoring, rapid order fulfillment, payment processing at scale, and post-sale reconciliation. Flash sales in Philippine e-commerce follow a distinct pattern: Payday Sales (15th and 30th), double-digit sales (11.11, 12.12), and marketplace mega-sales. These events can generate more orders in 24 hours than a typical week.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Flash sale planning (T-14 days)**: E-Commerce Manager, Category Manager, and Supply Planning define sale scope — participating SKUs, discount depth, inventory allocation per W57 | E-Commerce Manager / Category Manager | E-Commerce Manager | 4 hours |
| 2 | **Inventory pre-reservation (T-7 days)**: Supply Planning allocates dedicated flash sale inventory pool — excluded from regular ATP per W105 to prevent overselling | Supply Planning Manager | E-Commerce Manager | 4 hours |
| 3 | **Pricing setup (T-5 days)**: Category Manager configures flash sale pricing in e-commerce platform with start/end timestamps; system cross-checks against DTI price freeze status per W468 | Category Manager | E-Commerce Manager | 3 hours |
| 4 | **Infrastructure readiness (T-3 days)**: IT Operations confirms CDN capacity, payment gateway rate limits, server auto-scaling per W376; load test at 5x normal traffic | IT Operations | E-Commerce Manager | 4 hours |
| 5 | **Content staging (T-2 days)**: Digital Marketing stages landing pages, banners, email campaigns, push notification templates — held in draft for go-live | Digital Marketing Specialist | E-Commerce Manager | 4 hours |
| 6 | **Flash sale go-live (T-0)**: system activates pricing at scheduled time; monitoring dashboard live — order rate, inventory depletion, payment success rate, page load time, error rate | System / E-Commerce Manager | E-Commerce Manager | Automated + monitoring |
| 7 | **Real-time monitoring (every 30 minutes during sale)**: inventory depletion alerts (flag at 50%, 75%, 90% sold); payment gateway error rate monitoring; site performance monitoring; escalate anomalies immediately | E-Commerce Manager / IT Operations | E-Commerce Manager | Continuous during sale |
| 8 | **Inventory emergency protocol**: if SKU sells out, system auto-displays "Sold Out" badge and recommends substitutes per W279; if overall inventory error detected, pause sale for affected SKUs | System / E-Commerce Manager | E-Commerce Manager | Event-driven |
| 9 | **Flash sale end**: system reverts pricing; unallocated inventory released back to general ATP; "Sale Ended" messaging displayed | System | E-Commerce Manager | Automated |
| 10 | **Post-sale order fulfillment surge**: DC and store pick teams prioritize flash sale orders per SLA (BOPIS: 4 hours; delivery: 2–3 days); dedicated fulfillment queue for flash sale orders | DC / Store Teams | E-Commerce Manager | 24–72 hours post-sale |
| 11 | **Post-sale reconciliation (T+3 days)**: reconcile sales vs. inventory allocation; identify oversells/undersells; payment reconciliation per W267; fraud review per W266 (flag orders with unusual patterns — bulk buying, new accounts, high-value) | E-Commerce Manager / Finance | E-Commerce Manager | 4–6 hours |
| 12 | **Post-sale performance report (T+7 days)**: revenue, units sold, conversion rate, average discount depth, inventory sell-through %, customer acquisition (new vs. returning), fulfillment SLA compliance, fraud incidents, and ROI feeding into W565 | E-Commerce Manager | VP E-Commerce | 4 hours |

### System Touchpoints

- ECOM-021 (new requirement for flash sale operations with real-time monitoring and inventory controls)
- ECOM-010 (promo/coupon integration — flash sale pricing configuration)
- ECOM-001 (real-time inventory sync — inventory monitoring during sale)
- W13 (promotional pricing — pricing engine for discount configuration)
- W57 (promo stock allocation — inventory pre-reservation)
- W105 (multi-channel allocation — ATP exclusion for flash sale inventory)
- W98 (order exceptions — oversell handling and substitution)
- W266 (fraud detection — fraud screening during high-volume periods)
- W267 (digital payment reconciliation — payment reconciliation post-sale)
- W376 (IT capacity planning — infrastructure scaling and load testing)
- W468 (DTI price freeze — price compliance check)

### Time Estimate

- Pre-sale planning (steps 1–5): ~19 hours per event across all participants
- Real-time monitoring (steps 6–8): ~6–8 hours per event (continuous during sale)
- Post-sale operations (steps 9–12): ~12–16 hours per event
- **Total per flash sale**: ~15–20 person-hours (concentrated effort for E-Commerce Manager core)
- At 2–4 events/month: ~30–80 person-hours/month

### Pain Points / Risks

- **Traffic surge infrastructure risk**: auto-scaling may not provision fast enough if traffic spikes beyond 5x; site downtime during flash sale causes customer frustration and revenue loss
- **Inventory pre-reservation trade-off**: reserved stock that does not sell during the flash sale is tied up and unavailable for regular sales until released, reducing channel availability
- **Marketplace competition**: Lazada/Shopee marketplace flash sales compete directly with BuildRight's own site for the same customer attention and wallet share
- **Payment gateway degradation**: Philippine payment gateway reliability degrades during peak events (GCash/Maya outages during 11.11), causing checkout failures and abandoned orders
- **Fulfillment surge**: order volume exceeds normal DC capacity, requiring overtime staffing and potentially missing SLA commitments

### Staffing Implication

- **E-Commerce Manager**: ~15–20 hours per flash sale event. Absorbed within existing role with concentrated effort during sale periods.
- **DC and store teams**: overtime during fulfillment surge (1–3 days post-sale); budgeted as operational overtime.
- **No permanent incremental headcount**.

---

## W569. E-Commerce New Product Launch & Go-Live Process

| Field | Detail |
|---|---|
| **Trigger** | Merchandising team approves product for e-commerce listing (from W564 NPI process or W1 assortment review) |
| **Frequency** | ~50–80 new product listings per month on e-commerce |
| **Volume** | Includes new-to-range items, seasonal items, and marketplace-exclusive items; ~600–960 new listings per year |
| **Owner** | Digital Content Manager / E-Commerce Manager |
| **Participants** | Product Content Writer (R), Digital Content Manager (A), Category Manager (C for product specs), Photographer/Videographer (R for media), SEO Specialist (C for metadata), E-Commerce Manager (I) |

### Background

W50 covers product information management (PIM) including content standards and channel distribution. W252 covers centralized item master creation and governance. W316 covers digital asset and product content master governance. W564 covers new product introduction and full store rollout (physical stores). However, no workflow covers the e-commerce-specific product launch process — the end-to-end workflow of taking a newly approved product from item master creation through content staging, pricing verification, inventory pre-allocation, quality assurance testing, and live publication on the e-commerce platform. Unlike physical store launches where products appear on shelves, e-commerce launches require optimized product pages with rich content, multiple images, SEO metadata, pricing configuration, and inventory pre-allocation before the product can be discovered by customers online.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Product launch trigger received from Merchandising (from W564 NPI process or W1 assortment review); system creates launch task with SKU details and target go-live date | System / Category Manager | Digital Content Manager | 5 min |
| 2 | Digital Content Manager assigns launch to Product Content Writer with launch deadline based on priority tier (urgent: 3 days, standard: 7 days, routine: 14 days) | Digital Content Manager | E-Commerce Manager | 10 min |
| 3 | Product Content Writer creates product page draft: product title (SEO-optimized per W563), description (benefit-focused, 150+ words), specifications table (dimensions, weight, material, finish, compatibility), category assignment, and related products | Product Content Writer | Digital Content Manager | 45–60 min |
| 4 | Photographer captures product images: minimum 5 images per SKU (front, back, detail, lifestyle/context, dimension reference); video for premium items (power tools, appliances); images processed and uploaded to digital asset master per W316 | Photographer / Videographer | Digital Content Manager | 30–45 min |
| 5 | SEO Specialist reviews and optimizes metadata: title tag, meta description, URL slug, alt text for all images, schema markup (Product type with price, availability, rating) per W563 | SEO Specialist | Digital Content Manager | 15–20 min |
| 6 | Pricing verification: cross-check e-commerce price against POS price master per W289; verify promotional eligibility; configure quantity break pricing if applicable per POS-010 | Product Content Writer | E-Commerce Manager | 10 min |
| 7 | Inventory pre-allocation: Supply Planning confirms ATP for e-commerce channel per W105; configure safety threshold (do not display if < 5 units available) | System / Supply Planning | E-Commerce Manager | 10 min |
| 8 | Quality assurance review: Digital Content Manager reviews complete product page on staging environment — content accuracy, image quality, pricing, inventory display, mobile responsiveness, cross-browser rendering | Digital Content Manager | E-Commerce Manager | 15–20 min |
| 9 | Category Manager approves product page (factual accuracy of specifications); approval triggers staging-to-production readiness | Category Manager | Digital Content Manager | 10 min |
| 10 | Go-live: publish product page on production e-commerce platform; verify indexing by Google within 24 hours; confirm product appears in category navigation and site search | Product Content Writer / System | Digital Content Manager | 10 min |
| 11 | Post-launch monitoring (T+24 hours): verify product appears in search results, category navigation, and sitemap; check inventory display accuracy; monitor initial traffic and engagement | SEO Specialist / Product Content Writer | Digital Content Manager | 15 min |
| 12 | Performance check (T+7 days): page views, add-to-cart rate, search ranking for target keywords, customer questions/reviews; optimize underperforming pages | SEO Specialist | Digital Content Manager | 20 min |

### System Touchpoints

- ECOM-022 (new requirement for e-commerce product launch workflow with staging and QA)
- ECOM-009 (product catalog sync — catalog publication to production)
- MDM-002 (item attributes — specification data for product pages)
- MDM-025 (digital asset master — image/video management and optimization)
- W50 (PIM — content repository for product descriptions and specifications)
- W252 (item master — SKU data source for product attributes)
- W316 (digital asset master — asset governance for images and videos)
- W289 (pricing master — price verification and configuration)
- W563 (SEO management — SEO optimization of product metadata)
- W105 (multi-channel allocation — inventory pre-allocation for e-commerce channel)

### Time Estimate

- Per new product listing: ~2.5–4 hours (content creation, images, SEO, QA, go-live)
- At ~65 listings/month: ~195 person-hours/month across all participants
- Product Content Writer: ~120 hours/month (content creation and go-live)
- SEO Specialist: ~30 hours/month (metadata optimization and monitoring)
- Digital Content Manager: ~30 hours/month (QA review and coordination)
- Photographer: ~15 hours/month (product photography)

### Pain Points / Risks

- **Vendor image quality**: product images from vendors are often low-quality or watermarked, requiring in-house photography that adds time and cost to each listing
- **Multilingual specification data**: specification data from import vendors may be in Chinese/Japanese requiring translation, slowing the listing process
- **SEO optimization overhead**: SEO optimization adds significant time per listing (~15–20 min per SKU), which accumulates across 50–80 monthly listings
- **Mobile rendering complexity**: complex specification tables and multiple images may not render well on mobile devices, requiring responsive design testing
- **Content refresh backlog**: 35,000 existing SKUs require periodic content refresh to maintain quality, competing with new listing capacity

### Staffing Implication

- **Product Content Writer**: primary content creation role; ~120 hours/month dedicated to new product listings. Existing role within Digital Commerce entity.
- **Digital Content Manager**: ~30 hours/month on QA review and coordination. Absorbed within existing role.
- **SEO Specialist**: ~30 hours/month on metadata optimization. Absorbed within existing role.
- **No incremental headcount**.

---

## W591. E-Commerce Fulfillment SLA Monitoring & Exception Escalation

| Field | Detail |
|---|---|
| **Trigger** | Daily SLA monitoring cycle (automated overnight calculation, reviewed by 8:00 AM) |
| **Frequency** | Daily monitoring; weekly trend review; monthly executive SLA report |
| **Volume** | ~42,900 ecommerce orders/month (~1,430/day); mix of BOPIS (~25,700/month), home delivery from DC (~12,900/month), ship-from-store (~2,800/month), and drop-ship vendor (~1,500/month); SLA metrics tracked per order per fulfillment origin |
| **Owner** | E-Commerce Operations Supervisor |
| **Participants** | E-Commerce Operations Supervisor (R/A), Fulfillment Analyst (R), DC Dispatch Supervisor (C for DC-origin orders), Store Operations (C for BOPIS/SFS orders), Drop-Ship Vendor Coordinator (C for DSV orders), Last-Mile Supervisor (C for carrier performance), E-Commerce Manager (A for major/critical escalations), Customer Service Representative (I for customer-impacting breaches) |

### Background

W11 covers BOPIS order fulfillment with a 4-hour pick SLA. W19 covers home delivery fulfillment from DC. W19B covers ship-from-store fulfillment. W98 covers ecommerce order exceptions and cancellations. W246 covers drop-ship vendor order fulfillment. W268 covers last-mile delivery tracking and POD. However, no single workflow provides unified daily SLA monitoring across all ecommerce fulfillment channels with structured escalation when SLAs are breached. Given ~42,900 orders/month across 4 fulfillment origins (DC, store-BOPIS, store-SFS, vendor drop-ship), each with different SLA targets (same-day ship for DC orders before 2 PM, 2-hour BOPIS pickup readiness, next-day metro delivery, 48-hour DSV ship), a dedicated monitoring workflow is essential to: (a) detect SLA breaches in near-real-time before they impact customer experience; (b) identify systemic root causes (carrier delays, DC staffing gaps, DSV non-compliance, store pick failures); (c) escalate per severity to the appropriate resolution owner; (d) generate weekly trend data for process improvement. Philippine ecommerce context adds complexity: Metro Manila traffic congestion affects last-mile delivery SLAs; provincial BOPIS stores have variable staffing levels; drop-ship vendors (primarily based in Metro Manila and Southern China) have different operational cadences; and typhoon season (June–November) disrupts logistics networks.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Overnight SLA performance calculation (automated)**: System calculates SLA metrics for previous day's orders per fulfillment origin — (a) **DC home delivery**: orders received before 2:00 PM — same-day ship rate (target: ≥95%); orders received after 2:00 PM — next-day ship rate (target: ≥98%); ship-to-deliver cycle time (target: 1–3 days Metro Manila, 3–7 days provincial); (b) **BOPIS**: orders received — pickup readiness time (target: ≤2 hours from order confirmation); actual pickup time by customer; auto-cancel rate (target: <5%); (c) **Ship-from-store**: orders received — ship SLA (target: ≤4 hours from order routing to carrier handoff); (d) **Drop-ship vendor**: orders routed to DSV — DSV ship SLA (target: ≤48 hours from order routing); DSV fill rate (target: ≥95%); (e) System calculates aggregate SLA score per origin, per store/DC/DSV, and overall; flags orders that breached SLA with breach duration and classification | System | — | Automated (overnight batch, completed by 6:00 AM) |
| 2 | **Daily SLA dashboard generation and review**: Fulfillment Analyst reviews auto-generated SLA dashboard by 8:00 AM — (a) previous day's overall SLA performance vs. targets; (b) SLA breach list: order ID, fulfillment origin, breach type (pick, pack, ship, deliver, BOPIS readiness), breach duration, customer impact; (c) heat map: breach concentration by store (BOPIS/SFS), DC (home delivery), DSV (drop-ship), or carrier (last-mile); (d) comparison to 7-day rolling average for trend detection; (e) Fulfillment Analyst triages breaches into severity categories per step 3 | Fulfillment Analyst | E-Commerce Ops Supervisor | 30 min/day |
| 3 | **SLA breach severity classification**: Fulfillment Analyst classifies each breach into severity tiers — (a) **Minor**: single order breach, <1 hour over SLA, no customer complaint; action: log for trend analysis, no escalation required (e.g., BOPIS order ready in 2 hours 15 minutes vs. 2-hour SLA); (b) **Major**: multiple orders from same origin breach SLA, or single order breach >2 hours over SLA, or customer complaint received; action: escalate to fulfillment origin owner (DC Supervisor, Store Manager, DSV Coordinator) for root cause and corrective action within 24 hours (e.g., 20+ BOPIS orders at one store exceeding 2-hour readiness SLA due to understaffing); (c) **Critical**: systemic SLA failure affecting >5% of daily orders from any origin, or carrier network failure causing delivery suspensions, or BOPIS system outage affecting multiple stores; action: escalate immediately to E-Commerce Manager with incident report; E-Commerce Manager convenes cross-functional response within 2 hours; customer communication required per W98 | Fulfillment Analyst | E-Commerce Ops Supervisor | 20 min/day |
| 4 | **Root cause analysis for major/critical breaches**: For each major or critical breach, Fulfillment Analyst or designated origin owner conducts root cause analysis — (a) **DC-origin**: picker absenteeism, wave planning delay, carrier no-show, packaging material shortage, WMS system issue; (b) **Store-origin (BOPIS/SFS)**: stock associate not available for pick, ATP accuracy failure (item not on shelf despite system showing available), POS system delay, customer traffic competing for staff attention; (c) **DSV-origin**: vendor did not acknowledge order within SLA, vendor stockout after order routing, vendor shipment delay, vendor system integration failure; (d) **Carrier-origin**: 3PL driver shortage, vehicle breakdown, traffic congestion (Metro Manila EDSA, provincial road conditions), weather disruption (typhoon, flooding); (e) root cause documented in SLA breach log with category code for trend analysis | Fulfillment Analyst / Origin Owner | E-Commerce Ops Supervisor | 15–30 min/breach (major); 1–2 hours (critical) |
| 5 | **Corrective action assignment and tracking**: For each major/critical breach, E-Commerce Ops Supervisor assigns corrective action to responsible party — (a) **DC**: DC Supervisor adjusts wave planning, adds temporary pick staff, or escalates carrier issue to Last-Mile Supervisor; (b) **Store**: Store Manager reallocates staff for BOPIS picks, investigates ATP discrepancy, or requests replenishment for phantom stock items; (c) **DSV**: Drop-Ship Vendor Coordinator contacts vendor for explanation, updates DSV performance scorecard per W246, escalates repeated non-compliance to VP Merchandising for DSV program review; (d) **Carrier**: Last-Mile Supervisor contacts 3PL carrier (Lalamove, Transportify) for service recovery, evaluates backup carrier activation; (e) system tracks corrective action status: assigned → in-progress → completed; unresolved corrective actions >48 hours auto-escalate to E-Commerce Manager | E-Commerce Ops Supervisor | E-Commerce Manager | 15 min/breach |
| 6 | **Carrier/vendor performance feed**: Fulfillment Analyst updates carrier and DSV performance data — (a) per-carrier SLA performance: Lalamove on-time delivery rate, Transportify on-time delivery rate, own-fleet BOPIS readiness rate; (b) per-DSV SLA performance: ship timeliness, order accuracy, fill rate; (c) data feeds into carrier/vendor quarterly business review preparation; (d) carrier/vendor performance data shared with Last-Mile Supervisor (carriers) and Drop-Ship Vendor Coordinator (DSVs) for operational improvement | Fulfillment Analyst | E-Commerce Ops Supervisor | 15 min/day |
| 7 | **Weekly SLA trend review (Friday)**: E-Commerce Ops Supervisor conducts weekly review with origin owners — (a) week's SLA performance by origin vs. target; (b) trend: improving, stable, or deteriorating per origin; (c) top 3 root causes for the week's breaches; (d) corrective action completion rate (target: ≥90% resolved within 48 hours); (e) store-level BOPIS SLA ranking (top 10 / bottom 10 stores); (f) DC ship SLA by wave; (g) DSV compliance rate; (h) carrier on-time rate; (i) action items for next week: staffing adjustments, process changes, carrier performance discussions, DSV compliance warnings; (j) prepare weekly SLA summary for E-Commerce Manager | E-Commerce Ops Supervisor / Origin Owners | E-Commerce Manager | 60 min/week |
| 8 | **Monthly executive SLA report**: E-Commerce Ops Supervisor prepares monthly SLA report for E-Commerce Manager and VP Merchandising — (a) monthly SLA performance by channel: BOPIS, DC home delivery, SFS, DSV; (b) month-over-month trend; (c) customer impact: CSAT scores correlated with SLA performance, NPS impact, complaint rate; (d) financial impact: estimated lost revenue from SLA-related order cancellations, cost of expedited shipping to recover breached orders, cost of customer goodwill gestures (discount codes for SLA breaches); (e) process improvement recommendations; (f) carrier/DSV quarterly review preparation data | E-Commerce Ops Supervisor | E-Commerce Manager | 2 hours/month |

**Total time per daily cycle**: ~1.5 hours (Fulfillment Analyst ~1 hour triage and classification + E-Commerce Ops Supervisor ~30 min on corrective action assignment). Weekly review: ~1 hour. Monthly report: ~2 hours.

### System Touchpoints (W591 — SLA Monitoring)

- Ecommerce SLA monitoring dashboard: real-time and daily batch SLA calculation per fulfillment origin with breach detection (W591.1–2)
- Order management system (OMS): order lifecycle timestamps (placed, confirmed, routed, picked, packed, shipped, delivered, BOPIS-ready, BOPIS-picked-up) for SLA measurement (W591.1)
- SLA breach severity classification engine: configurable rules for minor/major/critical classification with auto-notification (W591.3)
- SLA breach log with root cause codes: standardized root cause taxonomy for trend analysis (W591.4)
- Corrective action tracking module: assignment, status, and escalation workflow with 48-hour auto-escalation (W591.5)
- Carrier performance dashboard: per-carrier on-time delivery rate, delivery time distribution, exception rate (W591.6, cross-reference W268)
- DSV performance scorecard: per-vendor ship SLA, fill rate, accuracy rate (W591.6, cross-reference W246)
- Store-level BOPIS SLA ranking: per-store pickup readiness time with top/bottom store identification (W591.7)
- Weekly SLA trend report: auto-generated trend charts by origin, root cause, and store (W591.7)
- Monthly executive SLA report template: standardized format with CSAT correlation and financial impact (W591.8)
- Integration with W11 (BOPIS fulfillment timestamps), W19 (home delivery fulfillment timestamps), W19B (SFS timestamps), W246 (DSV timestamps), W268 (last-mile delivery timestamps), W98 (exception management)
- Customer notification system: automated customer apology and goodwill gesture triggers for critical SLA breaches (cross-reference W65 customer satisfaction)

### Pain Points / Risks

- **SLA measurement timestamp accuracy**: SLA calculations depend on accurate timestamps at each fulfillment step (order placed, pick started, pick completed, pack completed, carrier handoff, delivery); if store associates forget to scan items at pick confirmation (W11 step 4), the BOPIS readiness timestamp is inaccurate, making SLA measurement unreliable
- **Multi-origin fulfillment complexity**: with 4 different fulfillment origins (DC, store-BOPIS, store-SFS, DSV), each with different SLA definitions and measurement points, the monitoring system must track and compute SLAs differently per origin; adding a new fulfillment channel (e.g., dark store per W210) requires SLA target definition and monitoring configuration
- **Carrier-dependent SLA gaps**: last-mile delivery SLA is dependent on 3PL carriers (Lalamove, Transportify) whose performance BuildRight does not directly control; Metro Manila traffic congestion (average 2.5 hours daily travel time per Metro Manila Development Authority) makes next-day delivery SLAs unreliable, especially during rush hours and rainy season
- **DSV SLA enforcement**: drop-ship vendors are independent businesses with their own operational constraints; BuildRight's contractual SLA requirements (48-hour ship) may not align with DSV's standard processing times, and enforcement relies on commercial leverage (scorecard impact, program removal) rather than operational control
- **BOPIS SLA during store peak hours**: the 2-hour BOPIS pickup readiness SLA competes with in-store customer service during peak periods (weekends, paydays — 15th and 30th); Store Managers prioritize walk-in customers over BOPIS picks, causing systematic SLA breaches during peak periods that are difficult to resolve without dedicated BOPIS staffing
- **Weather and infrastructure disruption**: Philippine typhoon season (June–November, average 20 typhoons/year) and Metro Manila flooding can cause systemic SLA failures across multiple origins simultaneously, overwhelming the exception escalation process and requiring executive-level customer communication decisions

### Staffing Implication

- **Fulfillment Analyst (dedicated)**: ~1 hour/day on SLA dashboard review, breach classification, and root cause analysis + ~15 min/day on carrier/DSV performance data = ~6.5 hours/week. This is a dedicated role within the E-Commerce Operations team.
- **E-Commerce Operations Supervisor**: ~30 min/day on corrective action assignment + ~1 hour/week on weekly review + ~2 hours/month on monthly report = ~6 hours/week. Absorbed within existing role with some reallocation from operational tasks.
- **Origin Owners (DC Supervisor, Store Managers, DSV Coordinator, Last-Mile Supervisor)**: ~15–30 min per major breach on root cause analysis; at ~15–20 major breaches/week across all origins, this represents ~4–6 hours/week distributed across all origin owners. Absorbed within existing roles.
- **E-Commerce Manager**: ~30 min/week on weekly SLA review + ~1 hour/month on monthly report review + ~2 hours/month on critical escalations = ~4 hours/month. Absorbed within existing role.
- **1 incremental Fulfillment Analyst recommended** to provide dedicated SLA monitoring capacity, freeing the E-Commerce Operations Supervisor from daily triage duties.

---

## W592. E-Commerce Customer Delivery Tracking & Proof of Delivery Management

| Field | Detail |
|---|---|
| **Trigger** | Order dispatched from DC, store (SFS), or drop-ship vendor for customer delivery |
| **Frequency** | Ongoing per delivery transaction; ~42,900 orders/month of which ~17,200 are home delivery orders requiring tracking and POD (~573/day); BOPIS orders (~25,700/month) tracked to pickup readiness but POD is pickup confirmation per W11 |
| **Volume** | ~17,200 home delivery orders/month requiring end-to-end tracking and POD capture; mix of carriers: Lalamove (~40% of home delivery volume), Transportify (~30%), own fleet for BOPIS delivery-to-vehicle (~15%), DSV-direct carrier (~15%); delivery coverage across Luzon (~65% of volume), Visayas (~20%), Mindanao (~15%) |
| **Owner** | Last-Mile Operations Supervisor |
| **Participants** | Last-Mile Operations Supervisor (A), Dispatch Coordinator (R), 3PL Driver (R for Lalamove/Transportify), Own-Fleet Driver (R), Customer Service Representative (R for exception handling), Fulfillment Analyst (R for POD reconciliation), Customer (I for notifications and delivery confirmation), Drop-Ship Vendor Coordinator (C for DSV deliveries) |

### Background

W268 covers last-mile home delivery tracking and proof-of-delivery from a logistics operations perspective, focusing on driver loading, GPS tracking, and POD capture at the point of delivery. W19 covers the home delivery fulfillment process from order receipt to dispatch. W98 covers ecommerce order exceptions and cancellations. W12 covers returns. W509 covers ecommerce product return inspection. However, no workflow covers the end-to-end delivery tracking lifecycle from the customer and financial reconciliation perspective — specifically: (a) delivery dispatch confirmation triggering customer notification; (b) real-time tracking link generation and distribution; (c) delivery attempt logging including first-attempt delivery success rate; (d) failed delivery handling with reschedule and return-to-origin options; (e) POD capture (photo + signature) for payment release and revenue recognition per PFRS 15; (f) POD reconciliation against dispatch log to identify unreconciled deliveries; (g) exception handling for damage, wrong item, and partial delivery claims. This workflow is critical because: delivery confirmation is required before revenue recognition for certain ecommerce transactions per PFRS 15 (performance obligation satisfied at delivery); POD (photo + signature) is required for payment release from Digital Commerce Inc. to Depot Inc. per the IC settlement model (W14); and delivery tracking data feeds customer CSAT measurement and SLA monitoring per W591. Philippine context: multi-island geography means deliveries may involve sea freight (RoRo) for Visayas and Mindanao orders; provincial addresses may be imprecise (barangay-level only); cash-on-delivery (COD) orders (~20% of home delivery volume) require driver cash collection and reconciliation per W99.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Delivery dispatch confirmation**: When order is handed off to carrier (3PL driver pickup at DC/DSV warehouse, or own-fleet driver loading at DC), system records dispatch confirmation — (a) DC Dispatch Coordinator scans shipment barcode and assigns to carrier/driver; (b) system records: order ID, shipment ID, dispatch timestamp, carrier name, driver name and contact, vehicle plate number; (c) for DSV shipments: DSV confirms dispatch via EDI/API integration with their own carrier; (d) system changes order status from "Processing" to "Shipped" in OMS; (e) dispatch data transmitted to tracking system per W268 | Dispatch Coordinator / System | Last-Mile Supervisor | 3–5 min/order at DC batch dispatch |
| 2 | **Real-time tracking link generation and customer notification**: System generates unique tracking link and notifies customer — (a) system creates tracking URL with real-time map display showing package location (carrier GPS integration for Lalamove/Transportify; WMS-driven status for DSV shipments); (b) system sends SMS to customer: "Your BuildRight order #[number] has been shipped! Track your delivery: [link]. Estimated delivery: [date/time range]. Contact: [customer service number]"; (c) system sends email with same information plus order summary and delivery instructions; (d) for BOPIS orders, this step is replaced by "Ready for Pickup" notification per W11 step 7; (e) tracking link active from dispatch until delivery confirmation or return-to-origin | System | — | Automated |
| 3 | **In-transit tracking and proactive updates**: System provides continuous tracking updates — (a) **GPS-based location updates**: carrier driver mobile app streams GPS coordinates every 60 seconds for Lalamove/Transportify deliveries; system updates customer tracking page in near-real-time; (b) **Milestone updates**: system sends milestone SMS/email to customer at key points — "Out for Delivery" (driver en route to customer address), "Nearby" (driver within 2 km, proximity alert); (c) **Exception alerts**: if delivery is delayed beyond estimated window by >4 hours, system alerts Last-Mile Supervisor and sends proactive customer notification with revised ETA; (d) **Multi-leg tracking**: for provincial deliveries requiring RoRo (Roll-on/Roll-off) sea crossing (Luzon to Visayas/Mindanao), system tracks each leg — DC to port, sea crossing, port to customer — with estimated time per leg | System / Last-Mile Supervisor | — | Automated (monitoring: 15 min/day by Dispatch Coordinator) |
| 4 | **Delivery attempt logging**: Driver attempts delivery and logs outcome via mobile app — (a) **Successful delivery**: driver marks "Delivered" in app; proceeds to POD capture (step 5); (b) **Customer not available**: driver marks "Attempted — No Response"; system logs attempt with timestamp and GPS coordinates; system auto-calls customer (IVR) and sends SMS: "We attempted delivery. Reschedule: [link] or call [number]. Order held for 3 business days"; (c) **Customer refusal**: driver marks "Refused" with reason code (wrong item visible, damaged packaging, changed mind, duplicate order); system creates exception ticket per W98; (d) **Incomplete address**: driver marks "Address Not Found"; system logs GPS location where driver stopped; CSR contacts customer for address clarification; (e) for COD orders: driver collects cash payment at delivery; driver records cash amount collected in app; system creates COD cash reconciliation entry per W99 | Driver / System | Last-Mile Supervisor | 2 min/delivery attempt |
| 5 | **Failed delivery handling — reschedule or return**: If first delivery attempt fails — (a) **Reschedule (within 3 business days)**: customer responds to reschedule notification within 24 hours; system reschedules delivery for next available date; Dispatch Coordinator reassigns to carrier/driver; customer receives new tracking link and ETA; if customer does not reschedule within 3 business days, order auto-moves to return-to-origin; (b) **Return to origin (store/DC)**: if reschedule window expires or customer explicitly requests return, system initiates return-to-origin — generates return shipment label, notifies carrier to return package to originating DC/DSV warehouse; system changes order status to "Return in Transit"; upon receipt at DC/DSV, inventory restored per W12 return process; customer refund initiated per W101; (c) **Return to nearest store**: customer may opt to pick up order at nearest BuildRight store instead of rescheduled delivery; system converts order to BOPIS at designated store; inventory transferred in system; customer receives BOPIS pickup notification per W11 | CSR / Dispatch Coordinator | Last-Mile Supervisor | 10–15 min per failed delivery |
| 6 | **POD capture (photo + signature)**: Upon successful delivery, driver captures POD via mobile app — (a) **Customer electronic signature**: customer signs on driver's mobile screen; signature stored as encrypted image; (b) **Delivery photo**: driver photographs delivered items at customer's doorstep or staging area; photo must show items and delivery location context; (c) **GPS coordinate stamp**: system auto-tags delivery location coordinates from driver's GPS at time of POD capture; (d) **Delivery confirmation metadata**: order ID, delivery timestamp, customer name, driver name, carrier; (e) POD data uploaded to cloud via mobile app — if offline (no signal at delivery location, common in provincial areas), POD data cached locally on device and auto-uploads when connectivity restored (within 24 hours); (f) for DSV deliveries: DSV carrier captures POD per DSV's own process; DSV transmits POD data to BuildRight via API integration | Driver / System | Last-Mile Supervisor | 3 min/delivery |
| 7 | **POD reconciliation against dispatch log**: Fulfillment Analyst reconciles POD records against dispatch log — (a) **Daily reconciliation**: system matches dispatched shipments (step 1) to POD records (step 6) by order ID; (b) **Matched (delivered with POD)**: POD received, order status "Delivered — POD Confirmed"; revenue recognition confirmed per PFRS 15 for goods-in-transit accounting; (c) **Dispatched but no POD**: shipment dispatched >24 hours ago but no POD received — Fulfillment Analyst investigates: driver did not capture POD, POD upload pending (offline mode), delivery not yet attempted, or shipment lost; (d) **POD received but dispatch missing**: POD exists for order not in dispatch log (system error or manual order); Fulfillment Analyst resolves with Dispatch Coordinator; (e) target: POD reconciliation completion rate ≥98% within 48 hours of delivery; unreconciled items >48 hours escalated to Last-Mile Supervisor | Fulfillment Analyst | Last-Mile Supervisor | 30 min/day |
| 8 | **Exception handling — damage, wrong item, partial delivery**: Customer reports delivery issue via phone, chat, or email — (a) **Damaged in transit**: customer reports damaged item(s); CSR creates exception ticket with photos; system triggers replacement order per W19 or return per W12 based on customer preference; carrier damage claim filed by Last-Mile Supervisor with supporting POD photos; damage liability assigned per carrier contract (Lalamove/Transportify standard liability limited to 10x freight cost); uninsured damage loss absorbed by BuildRight; (b) **Wrong item delivered**: customer reports receiving incorrect item(s); CSR verifies against order and pick/pack records; if picking error at DC, DC Supervisor investigates per W19 quality process and replacement order shipped expedited; if carrier misrouting, carrier claim filed; (c) **Partial delivery**: customer reports missing item(s) from multi-item order; CSR checks if order was split per W19 multi-DC order splitting — if split, customer informed of separate delivery; if not split, DC dispatch verifies packing slip vs. order; missing items shipped separately as expedited replacement; (d) all exceptions logged in delivery exception register with category, resolution, and resolution time per W98 | CSR / Last-Mile Supervisor | E-Commerce Ops Supervisor | 15–30 min per exception |
| 9 | **COD cash reconciliation**: For COD orders (~20% of home delivery = ~3,440 orders/month) — (a) driver records cash collected per order in mobile app at POD capture; (b) driver remits collected cash to DC cashier or designated bank deposit at end of shift; (c) system reconciles driver cash remittance to COD delivery log; (d) discrepancies (cash short/over) flagged for investigation per W99 payment settlement; (e) once reconciled, cash remittance posted to Digital Commerce Inc. (payment collector) for IC settlement to Depot Inc. (revenue recognizer) per W14; (f) unreconciled COD cash >48 hours escalated to Last-Mile Supervisor and Treasury per W30 | Dispatch Coordinator / Treasury Analyst | Last-Mile Supervisor | 30 min/day (COD reconciliation) |
| 10 | **Weekly POD compliance and delivery performance review**: Last-Mile Supervisor reviews weekly metrics — (a) **First-attempt delivery success rate**: target ≥85%; below target triggers carrier performance review; (b) **POD capture compliance rate**: target 100% (photo + signature); below 98% triggers driver coaching; (c) **Average delivery time by carrier**: Lalamove, Transportify, own fleet, DSV-direct; benchmarked against SLA targets per W591; (d) **Failed delivery rate**: target <10%; above target triggers customer address quality review and delivery window optimization; (e) **Exception rate**: damage, wrong item, partial delivery claims as % of deliveries; above 2% triggers DC packing quality review; (f) **COD reconciliation rate**: target ≥98% same-day; below target triggers cash handling process review; (g) **Regional performance**: Luzon vs. Visayas vs. Mindanao delivery times and success rates; provincial delivery SLA gaps identified for process improvement | Last-Mile Supervisor | E-Commerce Ops Supervisor | 60 min/week |

**Total time per daily cycle**: ~2 hours (Dispatch Coordinator ~30 min dispatch and COD reconciliation + Fulfillment Analyst ~30 min POD reconciliation + CSR ~30 min exception handling + Last-Mile Supervisor ~30 min monitoring). Weekly review: ~1 hour.

### System Touchpoints (W592 — Delivery Tracking & POD)

- Order management system (OMS): order status lifecycle from "Shipped" to "Delivered — POD Confirmed" with timestamp tracking at each status change (W592.1, W592.4)
- Carrier integration APIs: Lalamove API, Transportify API for real-time GPS tracking, dispatch confirmation, and POD data exchange (W592.1, W592.3, W592.6)
- Customer notification engine: SMS (via Philippine SMS gateway — Globe/Smart), email, and in-app push notifications for dispatch, milestone, and delivery confirmation (W592.2, W592.3)
- Real-time tracking portal: customer-facing web page with live map, estimated delivery time, and carrier contact (W592.2, W592.3)
- Driver mobile app: delivery attempt logging, POD capture (signature pad, camera, GPS stamp), COD cash recording, offline caching for provincial areas with no connectivity (W592.4, W592.5, W592.6, W592.9)
- POD cloud storage: encrypted POD images and signatures with order ID linking; retention per BIR 7-year document retention requirement (W592.6)
- POD reconciliation engine: automated matching of dispatch log to POD records with exception flagging (W592.7)
- Delivery exception register: categorization and tracking of damage, wrong item, partial delivery, and refusal exceptions linked to W98 (W592.8)
- COD cash reconciliation module: driver cash recording, remittance matching, and IC settlement triggering per W14 (W592.9, cross-reference W99)
- Revenue recognition integration: POD confirmation triggers revenue recognition for goods-in-transit orders per PFRS 15 (W592.7, cross-reference W487)
- Multi-leg shipment tracking: DC-to-port, RoRo sea crossing, port-to-customer tracking for Visayas/Mindanao deliveries (W592.3)
- DSV carrier API integration: POD data reception from drop-ship vendor carriers (W592.6, cross-reference W246)
- Weekly delivery performance dashboard: first-attempt success rate, POD compliance, carrier benchmarking, regional analysis (W592.10)

### Pain Points / Risks

- **POD capture compliance in provincial areas**: drivers in provincial areas with no mobile signal cannot upload POD data in real-time; cached POD data on driver devices may be lost if the device is damaged, stolen, or factory-reset before upload; a 2% POD data loss rate on ~17,200 deliveries/month equals ~344 deliveries/month without POD, creating revenue recognition uncertainty and customer dispute vulnerability
- **Customer address quality in Philippines**: Philippine addressing is inconsistent — many provincial addresses use barangay-level descriptions ("near the church", "behind the public market") rather than street numbers; GPS coordinates may be inaccurate due to limited Google Maps coverage in rural areas; this drives up the "Address Not Found" delivery attempt rate and extends delivery times
- **COD cash handling risk**: ~3,440 COD orders/month with average order value ~PHP 3,500 means ~PHP 12M/month in cash handled by 3PL drivers; cash collection, remittance, and reconciliation is inherently risky — driver theft, loss, or delayed remittance creates cash shortages and reconciliation backlogs; Lalamove and Transportify drivers are not BuildRight employees, limiting cash handling controls
- **Multi-island delivery complexity**: orders to Visayas and Mindanao require sea freight (RoRo) between islands, adding 1–3 days to delivery time and introducing weather-dependent delays; typhoon season can suspend RoRo operations for days, creating delivery backlogs that cascade across the tracking and POD system
- **Carrier liability limitation for damage**: Lalamove and Transportify standard terms limit carrier liability to approximately 10x the freight cost; for a PHP 500 delivery fee, maximum carrier liability is ~PHP 5,000 — far below the value of typical BuildRight orders (power tools PHP 5,000–50,000, appliances PHP 10,000–80,000); this means BuildRight absorbs most damage losses for high-value items, making POD photo quality critical for claim disputes
- **DSV carrier POD data gap**: drop-ship vendors use their own carriers for delivery to BuildRight customers; POD data from DSV carriers may not include photo or GPS stamp (only signature), creating a lower-quality POD record that is harder to use in customer disputes and may not satisfy PFRS 15 delivery confirmation requirements

### Staffing Implication

- **Dispatch Coordinator (dedicated)**: ~30 min/day on dispatch confirmation + ~30 min/day on COD reconciliation = ~5 hours/week. This is an existing role within the DC dispatch team; POD reconciliation and COD handling are additional responsibilities.
- **Fulfillment Analyst**: ~30 min/day on POD reconciliation = ~2.5 hours/week. Absorbed within existing Fulfillment Analyst role (also supporting W591 SLA monitoring).
- **CSR team**: ~30 min/day on delivery exception handling = ~2.5 hours/week distributed across CSR team. At ~15–20 delivery exceptions/day requiring CSR intervention, this represents ~30 min total across the team.
- **Last-Mile Operations Supervisor**: ~30 min/day on monitoring + ~1 hour/week on weekly review = ~3.5 hours/week. Absorbed within existing role.
- **No incremental headcount required**. The delivery tracking and POD management workflow is absorbed by existing DC dispatch, fulfillment, and last-mile operations staff.

---

## W659. Ecommerce Platform Incident Management

| Field | Detail |
|---|---|
| **Trigger** | Website downtime; checkout failure rate exceeds 1%; payment gateway outage; marketplace integration failure; order processing pipeline failure |
| **Frequency** | ~5–10 platform incidents/month; ~1–2 major incidents/quarter |
| **Volume** | Varies from partial degradation to full outage |
| **Owner** | Ecommerce Operations Manager |
| **Participants** | IT On-Call Engineer, Payment Gateway Vendor, Ecommerce Platform Vendor, Customer Service Lead, VP Digital Commerce |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Monitoring system detects platform anomaly: elevated error rate, checkout failure, API latency spike, payment gateway timeout, or marketplace integration disconnect; auto-creates incident ticket with severity classification (P1: total checkout failure, P2: partial degradation, P3: non-critical feature failure, P4: cosmetic/minor) | System | Ecommerce Operations Manager | Automated detection |
| 2 | For P1: IT On-Call Engineer activates major incident protocol within 15 minutes: opens bridge call, notifies Ecommerce Operations Manager and VP Digital Commerce, begins root cause investigation | IT On-Call Engineer | Ecommerce Operations Manager | 15 min |
| 3 | IT On-Call Engineer identifies affected component: website application, payment gateway, order management system, marketplace API, inventory sync, or hosting infrastructure; isolates failing component | IT On-Call Engineer | Ecommerce Operations Manager | 15–30 min |
| 4 | For payment gateway failure: activate multi-gateway failover (route transactions to backup gateway per W611); for marketplace integration failure: pause order pull from affected marketplace; for inventory sync failure: switch to cached inventory with safety buffer deduction | IT On-Call Engineer | Ecommerce Operations Manager | 30 min |
| 5 | Customer Service Lead activates customer communication: banner message on website explaining issue, social media response template, call center script update for affected order inquiries | Customer Service Lead | Ecommerce Operations Manager | 30 min |
| 6 | IT On-Call Engineer implements fix or workaround; verifies recovery; monitors for 30 minutes for stability; declares incident resolved | IT On-Call Engineer | Ecommerce Operations Manager | Varies |
| 7 | Post-incident: Ecommerce Operations Manager conducts blameless post-mortem within 48 hours; documents root cause, timeline, impact (orders affected, revenue lost, customer complaints), resolution, and preventive actions; assigns preventive action items with deadlines | Ecommerce Operations Manager | VP Digital Commerce | 2 hours |

### System Touchpoints
- Platform monitoring (APM), payment gateway management console, marketplace seller center, customer notification system, incident management system

### Time Estimate
- P1 resolution: 1–4 hours; P2: 2–8 hours; post-mortem: 2 hours within 48 hours

### Pain Points / Risks
- Philippine payment gateway instability (GCash/Maya outages during 11.11 and payday weekends); third-party vendor response times during their off-hours; customer trust erosion during checkout failures; flash sale incidents (W568) where traffic spike triggers the failure; revenue loss quantification disputes with platform vendor

### Staffing Implication
- **IT On-Call Engineer**: on-call rotation for P1/P2 incident response; ~5–10 incidents/month requiring engineering response. Absorbed within existing IT operations team on rotation basis.
- **Ecommerce Operations Manager**: ~2 hours/post-mortem for major incidents (~1–2/quarter). Absorbed within existing role.
- **Customer Service Lead**: ~30 min per major incident for communication activation. Absorbed within existing role.

---

## W724. Marketplace Channel Daily Operations & Order Management (Lazada/Shopee)

| Field | Detail |
|---|---|
| **Trigger** | Daily marketplace order processing cycle; or real-time order notification from marketplace platform |
| **Frequency** | Daily; real-time order notifications throughout the day |
| **Volume** | ~200-400 marketplace orders/day (~8,000-12,000/month); ~5-10% of total ecommerce volume |
| **Owner** | Ecommerce Operations Manager |
| **Participants** | Marketplace Specialist, Warehouse Picker, DC Dispatcher, Finance (reconciliation), Customer Service |

### Background

W180 covers the initial integration setup with marketplace platforms (Lazada, Shopee). This workflow covers the daily operational management of marketplace orders — the highest-volume daily ecommerce activity that the integration alone does not address. Marketplace channels have unique requirements: platform-specific fulfillment SLAs (Lazada requires ship-within-24h for standard items), platform commission structures (5-15% depending on category), platform-specific promotional mechanics (Shopee 9.9 sale, Lazada Mid-Year Sale), and platform-managed logistics options that differ from BuildRight's own fulfillment. With marketplace channels growing to represent 5-10% of ecommerce volume, dedicated daily operations are essential.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Morning order sync and prioritization**: at start of business day: (a) system syncs overnight marketplace orders from Lazada and Shopee via API integration per W180; (b) Marketplace Specialist reviews order queue: (i) orders requiring ship-today (received before cutoff, platform SLA requires same-day ship); (ii) orders pending inventory confirmation (ATP check against ERP); (iii) orders with address issues or customer notes requiring clarification; (iv) promotional orders with special fulfillment requirements; (c) prioritize ship-today orders for immediate DC pick | Marketplace Specialist | Ecommerce Ops Mgr | 30-45 min/day |
| 2 | **Inventory and price synchronization**: throughout the day, system maintains real-time sync: (a) inventory levels: ERP inventory changes (POS sales per W533, DC shipments) pushed to marketplace platforms within 5 minutes to prevent overselling; (b) price sync: promotional pricing per W13 activated simultaneously on marketplace and own channels per W678; (c) listing management: new product listings activated per W569 pushed to marketplace; discontinued items delisted; (d) Marketplace Specialist monitors for sync errors and resolves within 1 hour | System / Marketplace Specialist | Ecommerce Ops Mgr | Ongoing |
| 3 | **Fulfillment routing**: for each marketplace order: (a) system determines fulfillment method: (i) DC fulfillment: item picked from nearest DC per W19; (ii) drop-ship: routed to vendor for direct shipment per W246; (iii) ship-from-store: routed to store with inventory per W19B (if marketplace allows); (b) platform-specific logistics: (i) Lazada: choose between BuildRight own logistics or Lazada Logistics (LEX); (ii) Shopee: choose between own logistics or Shopee Xpress (SPX); (c) Marketplace Specialist reviews system routing decisions and adjusts if needed for SLA compliance | System / Marketplace Specialist | Ecommerce Ops Mgr | 15-20 min/day |
| 4 | **Order fulfillment and shipment tracking**: marketplace orders enter standard fulfillment pipeline: (a) DC pick and pack per W19 (home delivery) or W11 (BOPIS equivalent); (b) marketplace-specific label generation: platform-required shipping labels with tracking barcodes; (c) handoff to carrier: for platform logistics, schedule pickup per carrier SLA; for own logistics, dispatch per W106; (d) upload tracking number to marketplace platform via API; (e) monitor delivery status: system tracks marketplace-specific milestones (Ready to Ship → Shipped → Out for Delivery → Delivered) | DC Picker / Dispatcher | Ecommerce Ops Mgr | Per W19/W246 |
| 5 | **Customer service coordination**: for marketplace-specific customer issues: (a) respond to marketplace chat/inquiries within platform SLA (Lazada: 1 hour, Shopee: 30 min); (b) handle order cancellation requests: cancel in marketplace platform and ERP simultaneously; (c) process marketplace-initiated returns per W215 with platform-specific return procedures; (d) manage marketplace seller ratings and dispute resolution; (e) escalate platform account issues (listing takedowns, policy violations) to Ecommerce Operations Manager | Marketplace Specialist / Customer Service | Ecommerce Ops Mgr | 1-2 hours/day |
| 6 | **Daily settlement reconciliation**: at end of day: (a) reconcile marketplace orders shipped vs. orders in ERP; (b) verify tracking number upload completion for all shipped orders; (c) review platform commission calculations: order value × commission rate per category; (d) flag discrepancies: orders in platform but not in ERP (sync failure) or vice versa; (e) Finance receives daily marketplace settlement summary for monthly reconciliation per W99 | Marketplace Specialist / Finance | Ecommerce Ops Mgr | 30-45 min/day |

### System Touchpoints

- Marketplace API integration per W180 (Lazada Seller Center API, Shopee Open Platform API)
- ERP order management for unified order processing
- Real-time inventory sync per ECOM-001
- Price sync engine per W678 (multi-channel pricing consistency)
- Fulfillment routing engine per W536 (unified order management)
- Carrier integration for platform-specific logistics
- Settlement reconciliation per W99 (payment settlement)
- Customer service platform integration per W258

### Pain Points / Risks

- **Platform SLA pressure**: Lazada and Shopee impose strict ship-within-24h requirements; failure results in order cancellation, seller penalty points, and reduced search ranking; mitigated by early morning order processing and DC priority for marketplace orders
- **Commission impact on margins**: marketplace commissions (5-15%) plus payment processing fees reduce gross margin significantly compared to own-channel sales; requires careful SKU selection for marketplace — avoid listing low-margin items where commission eliminates profit
- **Inventory overselling risk**: if inventory sync fails or is delayed, marketplace may sell items already committed to in-store or ecommerce orders; mitigated by safety stock buffer dedicated to marketplace channel per W105
- **Platform policy volatility**: Lazada and Shopee frequently change seller policies, commission rates, and promotional requirements; requires constant monitoring and rapid adaptation
- **Account suspension risk**: marketplace platforms can suspend seller accounts for policy violations (late shipping, customer complaints, counterfeit claims); suspension halts all marketplace revenue immediately

### Staffing Implication

Marketplace Specialist: 1 FTE dedicated to marketplace daily operations (order processing, customer service, platform management). Ecommerce Operations Manager: ~1-2 hours/day oversight. Customer Service: ~1 hour/day on marketplace inquiries. No incremental headcount beyond existing ecommerce team.

### Time Estimate

**Total daily**: 4-6 hours (30-45 min order sync + ongoing inventory/price management + 15-20 min routing + fulfillment per W19 + 1-2 hours customer service + 30-45 min reconciliation).

---

## W725. Ecommerce Platform Daily Health Monitoring & Performance Dashboard

| Field | Detail |
|---|---|
| **Trigger** | Start of ecommerce operations day; or automated alert from monitoring system |
| **Frequency** | Daily review; continuous automated monitoring |
| **Volume** | 1 daily comprehensive review; ~10-20 automated alerts/day |
| **Owner** | Ecommerce Operations Manager |
| **Participants** | IT Operations (per W595), Ecommerce Specialist, Customer Service Lead |

### Background

BuildRight's ecommerce platform processes ~42,900 orders/month representing ~PHP 150M in monthly GMV. Platform uptime, performance, and data integrity directly impact revenue — even 1 hour of downtime during peak shopping hours can cost PHP 200K+ in lost sales. W659 covers platform incident management (what happens when things break). This workflow covers the proactive daily monitoring that prevents incidents: platform health checks, performance metrics review, error log triage, and capacity monitoring. It complements W595 (ERP system daily health check) with ecommerce-specific monitoring.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Morning health check**: at start of business day, Ecommerce Operations Manager reviews overnight platform health: (a) uptime summary: was the platform available 99.9% of the past 24 hours?; (b) page load speed: homepage <3 seconds, product page <2 seconds, checkout <2 seconds (target per NFR-003); (c) error rate: 404 errors, 500 errors, API timeout errors — any exceeding threshold (>0.1% error rate); (d) order processing: all overnight orders successfully received and pushed to ERP per W533?; (e) inventory sync: last successful inventory sync timestamp, any sync failures; (f) payment processing: payment gateway uptime, failed payment rate; (g) if any red flags: escalate to IT per W595 and/or activate W659 incident management | Ecommerce Ops Mgr | — | 20-30 min/day |
| 2 | **Performance dashboard review**: Ecommerce Operations Manager reviews real-time ecommerce dashboard: (a) traffic metrics: unique visitors, page views, bounce rate, traffic source breakdown; (b) conversion funnel: visitors → product views → add to cart → checkout initiation → completed purchase; (c) cart abandonment rate: target <70%; investigate if >75%; (d) mobile vs. desktop split: ensure mobile experience is performing equally; (e) search performance: search usage rate, zero-result searches (indicating catalog gaps), top search terms; (f) category performance: which categories are driving/declining in online sales | Ecommerce Ops Mgr | CMO | 15-20 min/day |
| 3 | **Error log triage**: IT support reviews ecommerce platform error logs: (a) categorize errors: (i) critical: checkout failures, payment failures, inventory sync failures; (ii) warning: slow page loads, intermittent API errors, image loading failures; (iii) informational: bot traffic, invalid search queries; (b) critical errors: investigate immediately, escalate to development team if code-level fix needed per W616; (c) warning errors: batch for weekly review and prioritization; (d) track error trends: are specific error types increasing over time? | IT Support / Ecommerce Ops Mgr | IT Manager | 15-20 min/day |
| 4 | **Capacity and scalability monitoring**: Ecommerce Operations Manager monitors platform capacity: (a) current server utilization: CPU, memory, database connections; (b) CDN utilization: are product images and static assets loading efficiently?; (c) database performance: query response times, connection pool utilization; (d) if approaching capacity thresholds (>80% utilization): coordinate with IT per W376 for scaling; (e) pre-event capacity planning: before major promotions per W568 (flash sales), verify platform can handle 3-5x normal traffic | Ecommerce Ops Mgr / IT | IT Manager | 10 min/day; 1-2 hours pre-event |
| 5 | **Weekly performance report**: Ecommerce Operations Manager compiles weekly ecommerce health report: (a) platform uptime: weekly % vs. 99.9% target; (b) average page load times; (c) error rate trends; (d) conversion rate trends; (e) top 5 issues resolved and top 5 outstanding; (f) upcoming events requiring capacity scaling; (g) report distributed to CMO, CIO, and IT team | Ecommerce Ops Mgr | CMO | 1-2 hours/week |

### System Touchpoints

- Application performance monitoring (APM) tool for uptime, response times, error rates
- Ecommerce analytics dashboard (traffic, conversion, abandonment)
- Error logging and alerting system with threshold-based notifications
- Server and infrastructure monitoring per W376 (capacity planning)
- CDN monitoring for content delivery performance
- Payment gateway monitoring per W611
- ERP integration monitoring per W595

### Pain Points / Risks

- **Alert fatigue**: monitoring systems can generate excessive alerts, leading to important signals being lost in noise; mitigated by threshold tuning and alert categorization
- **Third-party dependency**: ecommerce platform, payment gateway, and CDN are all third-party services; outages are outside BuildRight's direct control and require vendor coordination per W369
- **Performance during flash sales**: traffic spikes during promotional events per W568 can overwhelm platform capacity despite pre-event scaling; requires load testing before every major promotion
- **Mobile performance gaps**: mobile page load speeds are often 2-3x slower than desktop due to network conditions in the Philippines; mobile users are ~60% of traffic, making mobile performance critical

### Staffing Implication

Ecommerce Operations Manager: ~1-1.5 hours/day on monitoring and review. IT Support: ~15-20 min/day on error log triage. Absorbed within existing ecommerce and IT team. No incremental headcount.

### Time Estimate

**Total daily**: ~60-80 min (20-30 min health check + 15-20 min dashboard + 15-20 min error triage + 10 min capacity). **Weekly report**: 1-2 hours.

---

## W726. Ecommerce Product Content Enrichment & Catalog Daily Operations

| Field | Detail |
|---|---|
| **Trigger** | New SKU activation per W564; product content quality alert; daily catalog maintenance schedule |
| **Frequency** | Daily (~50-100 SKUs requiring content attention per day) |
| **Volume** | 35,000 active SKUs in online catalog; ~500-1,000 new/updated SKUs/month |
| **Owner** | Ecommerce Content Manager |
| **Participants** | Merchandising (product data), Photographer/Designer, Ecommerce Specialist, Category Manager |

### Background

W50 covers the Product Information Management (PIM) process at the strategic level. W316 covers digital asset master governance. This workflow addresses the daily operational reality of keeping 35,000 active SKUs' online content accurate, complete, and compelling. Product content quality (images, descriptions, specifications, how-to guides) directly impacts online conversion rates — SKUs with complete content convert 2-3x higher than those with incomplete content. With ~500-1,000 new or updated SKUs flowing through the catalog monthly, daily content operations are essential.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Daily content quality dashboard review**: Ecommerce Content Manager reviews content quality dashboard: (a) content completeness score per SKU: product title, description, specifications, images (minimum 3), dimensions, weight, category attributes, SEO keywords; (b) SKUs flagged for content issues: missing images, incomplete descriptions, incorrect specifications, outdated pricing display; (c) new SKUs from W564 without online content: target is content-ready within 48 hours of SKU activation; (d) SKUs with customer-reported content errors (from product reviews per W510 or customer service per W258); (e) prioritize content work queue: (i) high-priority: active promotional items per W13 with incomplete content; (ii) medium: new SKUs awaiting launch per W569; (iii) low: backlog of C-item content improvements | Ecommerce Content Mgr | Ecommerce Ops Mgr | 20-30 min/day |
| 2 | **New SKU content creation**: for new SKUs entering the catalog: (a) Merchandising provides product data sheet: specifications, features, benefits, use cases, materials, dimensions; (b) Ecommerce Content Manager creates: (i) product title: SEO-optimized, under 200 characters; (ii) product description: detailed HTML description with key features, specifications table, and usage instructions; (iii) category attributes: populate all required and recommended attributes per W298 product attribute template; (iv) search keywords: generate from product category, brand, specifications, common misspellings; (c) Photographer/Designer provides or sources product images: (i) main image: white background, product-only (marketplace requirement); (ii) lifestyle images: product in use context; (iii) detail images: close-ups of key features; (iv) dimension image: visual size reference; (v) minimum 5 images per SKU, 10+ for high-value items | Ecommerce Content Mgr / Photographer | Ecommerce Ops Mgr | 20-30 min per new SKU |
| 3 | **Content review and approval**: Category Manager reviews content for accuracy: (a) verify specifications match physical product and vendor documentation; (b) verify pricing display matches current price per W40; (c) verify promotional content aligns with active promotions per W13; (d) approve content for publication or request revisions; (e) system publishes approved content to: buildright.com.ph, mobile app, marketplace channels (Lazada/Shopee), Google Shopping feed | Category Manager | Ecommerce Ops Mgr | 5-10 min per SKU |
| 4 | **Content performance monitoring**: Ecommerce Content Manager monitors content effectiveness: (a) page view-to-cart rate: identify SKUs with high views but low conversion (content issue? pricing issue?); (b) search ranking: monitor product search position for key category terms; (c) customer review content analysis: extract product feedback from W510 that indicates content gaps (e.g., "dimensions not clear," "color doesn't match photo"); (d) A/B test content variations for high-traffic SKUs: test different images, descriptions, and attribute prominence | Ecommerce Content Mgr | Ecommerce Ops Mgr | 30-60 min/week |
| 5 | **Catalog maintenance**: daily catalog housekeeping: (a) activate new SKU listings approved in step 3; (b) deactivate discontinued SKUs per W68: redirect to replacement products if available; (c) update changed specifications (vendor-initiated product changes); (d) refresh seasonal content: update imagery and descriptions for seasonal relevance per W264; (e) fix broken links and missing images identified by automated scanning | Ecommerce Specialist | Ecommerce Content Mgr | 30-60 min/day |

### System Touchpoints

- PIM (Product Information Management) system per W50 for centralized content management
- Content quality scoring engine with completeness metrics
- Digital asset management per W316 for image and media storage
- Ecommerce platform content management system (CMS)
- Marketplace listing management per W180 for multi-channel content distribution
- SEO analytics for search ranking monitoring
- Customer review integration per W510 for content feedback
- Google Shopping feed management

### Pain Points / Risks

- **Content bottleneck at scale**: creating quality content for 35,000+ SKUs is resource-intensive; at ~20-30 min per new SKU and 500-1,000 new SKUs/month, content creation requires ~150-500 hours/month
- **Image quality inconsistency**: product images come from multiple sources (vendor-provided, in-house photography, catalog images) with varying quality, backgrounds, and angles; inconsistent imagery reduces catalog professionalism
- **Vendor data incompleteness**: many vendors provide minimal product information (basic specs only), requiring BuildRight's content team to enrich with additional research, usage guides, and contextual information
- **Marketplace-specific content requirements**: Lazada and Shopee have different image requirements, character limits, and attribute requirements, requiring content adaptation for each channel per W678
- **Content freshness decay**: product descriptions become outdated as specifications change, new images are available, or seasonal relevance shifts; without systematic refresh, catalog quality degrades over time

### Staffing Implication

Ecommerce Content Manager: 1 FTE dedicated to content management. Photographer/Designer: shared resource from W190 (in-house creative production), ~0.5 FTE on product photography. Ecommerce Specialist: ~30-60 min/day on catalog maintenance. Category Managers: ~5-10 min/SKU on review. At current volume, a dedicated Ecommerce Content Manager is justified.

### Time Estimate

**Daily operations**: ~2-3 hours (20-30 min dashboard + content creation per queue + 30-60 min maintenance). **Per new SKU**: 20-30 min content creation + 5-10 min review. **Weekly performance monitoring**: 30-60 min.

---

## W828. Ecommerce Platform Feature Release, A/B Testing & UX Optimization

| Field | Detail |
|---|---|
| **Trigger** | Feature development completed per W132 software development; UX improvement identified per analytics |
| **Frequency** | Bi-weekly release cycles; ~2-4 A/B tests running concurrently |
| **Volume** | ~24 releases/year; ~50-100 A/B tests/year; ~300-500 UX improvements/year |
| **Owner** | Ecommerce Product Manager |
| **Participants** | Product Manager, UX Designer, Developer, QA Tester, Marketing Manager, Business Analyst |

### Background

BuildRight's ecommerce platform (buildright.com.ph) processes ~42,900 orders/month (~PHP 150M GMV) with a target of growing to ~7% of revenue by Year 3. Continuous improvement through feature releases, A/B testing, and UX optimization is essential for conversion rate improvement. While W132 covers software development change management and W659 covers ecommerce platform incident management, there's no workflow for the structured release process, A/B testing framework, and UX optimization cycle specific to the ecommerce platform. A/B testing is particularly important for: checkout flow optimization, product page layout, search relevance, mobile responsiveness, and promotional landing pages. Philippine ecommerce UX must account for: mobile-first users (80%+ traffic), intermittent connectivity (especially provincial), GCash/Maya payment flow familiarity, and Filipino language preferences.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Feature release plan creation**: Product Manager creates feature release plan: (a) feature description and user stories; (b) success metrics (conversion rate, bounce rate, AOV, cart abandonment); (c) target audience segment per W156 CDP; (d) release strategy (A/B test vs. gradual rollout vs. full release) | Product Manager | Ecommerce Ops Mgr | 2-4 hours |
| 2 | **A/B test feature setup**: for A/B test features: (a) UX Designer creates variant(s) per hypothesis; (b) Developer implements feature flags per W132; (c) QA Tester validates both control and variant experiences per W391; (d) configure traffic split (typically 50/50 or 80/20 for high-risk changes) | UX Designer / Developer / QA Tester | Product Manager | 4-8 hours |
| 3 | **Release deployment**: (a) deploy to staging environment per W384; (b) QA regression test per W391; (c) deploy to production with feature flag off; (d) enable for test group; (e) monitor W725 platform health dashboard for 24 hours | Developer / QA Tester | Product Manager | 4-8 hours |
| 4 | **A/B test monitoring (1-4 weeks)**: (a) daily metric comparison (control vs. variant); (b) statistical significance tracking; (c) segment analysis (mobile vs. desktop, new vs. returning, by region); (d) watch for negative impacts on W557 cart abandonment or W98 cancellation rates | Product Manager / Business Analyst | Ecommerce Ops Mgr | 30 min/day × test duration |
| 5 | **A/B test conclusion**: (a) if variant wins: full rollout to 100% traffic; (b) if no significant difference: revert to control, document learnings; (c) if variant loses: revert immediately, analyze why | Product Manager | Ecommerce Ops Mgr | 2-3 hours |
| 6 | **Non-A/B gradual rollout**: for non-A/B releases: (a) gradual rollout — 10% → 25% → 50% → 100% over 1-2 weeks; (b) monitoring at each stage; (c) instant rollback capability per W659 incident management | Developer / Product Manager | Ecommerce Ops Mgr | 1-2 hours per stage |
| 7 | **Post-release documentation**: (a) Product Manager documents results in feature log; (b) Business Analyst updates conversion funnel analytics per W113 BI; (c) Marketing Manager notified for promotional integration per W83 | Product Manager / Business Analyst | Ecommerce Ops Mgr | 1-2 hours |
| 8 | **Monthly UX optimization review**: (a) conversion funnel analysis; (b) top exit pages; (c) mobile vs. desktop performance; (d) page load time per W725 monitoring; (e) customer feedback per W510 reviews and W41 complaints | Product Manager / UX Designer | Ecommerce Ops Mgr | 4-6 hours/month |

### System Touchpoints

- W132 software development change management for feature flag implementation
- W391 QA testing for control and variant validation
- W384 environment management for staging deployment
- W659 ecommerce platform incident management for rollback capability
- W725 platform health monitoring dashboard for real-time metrics
- W156 CDP segments for audience targeting
- W113 BI analytics for conversion funnel analysis
- W83 campaign execution for promotional integration
- W557 cart abandonment workflow for impact monitoring
- W98 order exceptions for cancellation rate tracking
- W510 product reviews for customer feedback
- W41 complaints for UX issue identification

### Pain Points / Risks

- **A/B test sample size adequacy**: lower-traffic pages (category pages for niche products) may not achieve statistical significance within reasonable test duration, leading to inconclusive results
- **Feature flag technical debt**: accumulating feature flags increase code complexity and maintenance burden; periodic cleanup is required but often deprioritized
- **Mobile device fragmentation**: Philippines has diverse Android versions and screen sizes; A/B test variants may perform differently across device segments, complicating analysis
- **GCash/Maya payment flow changes**: modifications to payment flows require partner coordination and may not be testable in staging environments
- **Staging-production parity**: staging environment may not perfectly replicate production behavior (data volume, third-party integrations, real payment gateways)

### Staffing Implication

Absorbed by Ecommerce Product Manager and UX Designer; ~30-40 hours/month. Product Manager: ~15-20 hours/month on planning, monitoring, and analysis. UX Designer: ~10-15 hours/month on variant design. Business Analyst: ~5 hours/month on analytics. No incremental headcount.

### Time Estimate

Per release: planning (2-4 hours) + testing (4-8 hours) + monitoring (30 min/day × test duration) + analysis (2-3 hours) = ~10-20 hours per release excluding development. Monthly UX review: 4-6 hours.

---

## W829. Customer Ecommerce Order Split & Partial Delivery Proactive Communication

| Field | Detail |
|---|---|
| **Trigger** | Ecommerce order requires splitting across multiple fulfillment locations per POS-021 multi-DC order splitting |
| **Frequency** | Daily; ~15-25% of ecommerce orders require splitting (~6,500-10,700 orders/month) |
| **Volume** | ~6,500-10,700 split orders/month out of ~42,900 total; average 2.1 sub-orders per split order |
| **Owner** | Ecommerce Operations Specialist |
| **Participants** | Operations Specialist, DC Planner, Customer, 3PL Carrier, Customer Service Agent |

### Background

POS-021 requires multi-DC order splitting when no single DC has ATP for all items. With 35,000 SKUs across 4 DCs, ~15-25% of orders will span multiple fulfillment locations. While the system handles the splitting automatically, the customer communication and partial delivery management workflow is not covered by existing workflows. W19 covers home delivery fulfillment and W592 covers delivery tracking, but neither addresses the customer experience when one order becomes 2-3 separate deliveries arriving on different days. Poor communication of split orders is a top driver of customer complaints in omnichannel retail — customers don't understand why they received a partial order and may assume items are missing.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Order split detection**: system detects order requires split per POS-021: creates sub-orders with separate tracking numbers but unified customer order reference | System | Ecommerce Ops Specialist | Automated |
| 2 | **Immediate customer notification**: system sends W708 communication within 5 minutes of order confirmation: (a) "Your order has been split for faster fulfillment" — positive framing; (b) list of items per delivery with estimated delivery dates; (c) separate tracking numbers per sub-order; (d) total amount remains same — no additional charges; (e) single point of contact for any questions per W258 | System / Ecommerce Ops Specialist | Ecommerce Ops Mgr | < 5 min (automated) |
| 3 | **Sub-order routing to DCs**: system routes sub-orders to respective DCs per W536 unified order management: (a) DC1 fulfills items A, B, C; (b) DC3 fulfills items D, E; (c) each DC picks, packs, and dispatches per W106 | System / DC Planner | Ecommerce Ops Specialist | Automated routing |
| 4 | **Sub-order status tracking**: customer sees unified order dashboard: (a) overall order status (% complete by items); (b) individual sub-order status with carrier tracking per W592; (c) delivered items checked off; (d) pending items with countdown to delivery | System | Ecommerce Ops Specialist | Continuous (automated) |
| 5 | **First delivery notification**: system sends notification — "Part 1 of your order has been delivered! Items D and E are on their way, estimated [date]" | System | Ecommerce Ops Specialist | Automated |
| 6 | **Partial delivery gap monitoring**: if more than 3 days between first and last sub-order delivery: (a) system sends proactive status update; (b) if any sub-order delayed beyond estimated date: W708 notification with updated ETA and apology; (c) Customer Service preemptively available for inquiries per W259 | System / Customer Service Agent | Ecommerce Ops Specialist | 15-30 min/case |
| 7 | **Final delivery confirmation**: system sends "Your order is complete!" notification with: (a) delivery confirmation for all items; (b) feedback/review prompt per W510; (c) related product recommendations per W156 CDP | System | Ecommerce Ops Specialist | Automated |
| 8 | **Exception handling**: (a) if one sub-order is cancelled (out of stock after split): immediate customer notification, refund for affected items per W101, option to cancel remaining sub-orders; (b) if customer wants to return items from only one sub-order: process per W215 returns with sub-order reference | Customer Service Agent / Ecommerce Ops Specialist | Ecommerce Ops Mgr | 30 min/exception |
| 9 | **Monthly split order analytics**: (a) split order rate; (b) average sub-orders per split; (c) delivery gap statistics; (d) split order complaint rate vs. non-split; (e) customer satisfaction comparison; (f) SKU availability by DC to identify inventory positioning improvements per W183 | Ecommerce Ops Specialist | Ecommerce Ops Mgr | 3 hours/month |

### System Touchpoints

- POS-021 multi-DC splitting logic for automatic order split detection
- W536 unified order management for sub-order routing
- W106 DC dispatch for individual sub-order fulfillment
- W19 home delivery fulfillment for delivery execution
- W592 delivery tracking for carrier tracking integration
- W708 customer communication for all notifications
- W258 ticketing for customer inquiry management
- W259 call center for preemptive customer service
- W101 refund processing for cancelled sub-order refunds
- W215 returns for partial order returns
- W510 product reviews for post-delivery engagement
- W156 CDP for product recommendations
- W183 supply chain optimization for inventory positioning insights

### Pain Points / Risks

- **Customer confusion about partial deliveries**: despite notifications, some customers will not read or understand split order communications and will contact customer service assuming items are missing
- **Carrier cost increase**: multiple shipments for a single order increase delivery cost; with ~6,500-10,700 split orders/month, this represents significant incremental logistics cost
- **Environmental impact**: multiple deliveries for one order increases carbon footprint; environmentally conscious customers may object
- **Sub-orders arriving out of sequence**: later-submitted sub-orders may arrive before earlier ones due to DC proximity and carrier schedules, further confusing customers
- **Return routing complexity**: customer attempting to return items to wrong sub-order carrier causes return processing delays

### Staffing Implication

Absorbed by Ecommerce Operations Specialist and Customer Service team; ~25-30 hours/month for exception handling. Ecommerce Ops Specialist: ~10-15 hours/month on monitoring and analytics. Customer Service: ~15 hours/month on split order inquiries. No incremental headcount.

### Time Estimate

Mostly automated. Exception handling: ~30 min/case × ~200 exceptions/month = 100 hours/month. Monthly analytics: 3 hours.

---

## W899. Customer Bulk/Project Delivery Scheduling & Multi-Drop Coordination (B2C)

| Field | Detail |
|---|---|
| **Trigger** | Individual B2C customer (non-trade, non-corporate) places a large home renovation or construction order requiring: (a) delivery of bulky/heavy items (cement, lumber, tiles, steel) exceeding standard parcel delivery; (b) staged delivery across multiple dates as construction progresses; (c) delivery to multiple addresses (e.g., contractor's warehouse + project site); (d) delivery requiring special equipment (boom truck, flatbed) |
| **Frequency** | ~800–1,200 bulk/project delivery orders/month chain-wide |
| **Volume** | Avg order value PHP 30,000–150,000; avg 3–5 delivery stages per project |
| **Owner** | Store Logistics Coordinator (Receiving Clerk role) |
| **Participants** | Customer, Store Logistics Coordinator, Delivery Partner (3PL or own fleet), Sales Associate/Pro Desk, Supply Planning |

### Background

BuildRight's standard home delivery (W19) handles ecommerce orders averaging PHP 3,500 with 3–4 items fulfilled from DC via parcel carrier or 3PL. However, a significant segment of walk-in B2C customers — homeowners undertaking major renovations ("building a house," "remodeling the kitchen," "landscaping the garden") — place large orders (PHP 30K–150K) involving cement, lumber, tiles, fixtures, and appliances that require fundamentally different logistics: flatbed or boom truck delivery, multi-drop scheduling aligned with construction phases, and delivery to construction sites (not residential porches). These orders are typically placed in-store with Sales Associate assistance, not online. While W164 handles staged project deliveries for B2B corporate/institutional projects, and W19 handles standard ecommerce home delivery, there is no workflow for B2C project delivery coordination — a gap that affects an estimated 5–8% of B2C walk-in revenue (PHP 150M–250M/month × 5–8% = PHP 7.5M–20M/month in project delivery orders). Poor execution here — late deliveries damaging construction schedules, wrong items delaying masonry work, split deliveries confusing contractors — directly impacts customer satisfaction and repeat business.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Project Delivery Needs Assessment**: During large in-store purchase consultation: (a) Sales Associate or Pro Desk identifies customer needs project delivery based on: (i) order contains bulky items (cement bags, lumber, plywood sheets, tile pallets, steel bars); (ii) order total exceeds PHP 15,000; (iii) customer mentions renovation/construction project; (b) Associate interviews customer on logistics needs: (i) delivery address (residential, construction site, contractor warehouse); (ii) site accessibility (narrow road, high-rise, gated community, rural); (iii) delivery timing constraints (construction schedule, barangay truck ban per W431); (iv) staging preference (single delivery vs. phased delivery aligned with construction stages); (v) unloading requirements (manual carry, crane/boom truck, forklift); (vi) contact person at delivery site (customer, contractor, caretaker) | Sales Associate / Pro Desk | Store Manager | 15–20 min |
| 2 | **Delivery Plan Creation**: Based on needs assessment: (a) system generates delivery plan options: (i) **Single Delivery**: all items in one trip — suitable for accessible site, available storage at destination; (ii) **Phased Delivery**: items grouped by construction phase — (example: Phase 1: cement, sand, gravel, rebar for foundation; Phase 2: hollow blocks, lumber for framing; Phase 3: tiles, adhesives, grout for finishing; Phase 4: fixtures, paint, accessories for installation); each phase scheduled per customer's construction timeline; (iii) **Multi-Address Delivery**: items split across addresses (e.g., heavy materials to site, fixtures to residence for safekeeping); (b) system calculates delivery cost per option based on: distance from store/DC, vehicle type required, number of trips, special equipment; (c) customer selects preferred option; (d) delivery fee: free for orders > PHP 20,000 within 15 km of store; distance-based fee beyond 15 km per W19 delivery fee structure; special equipment surcharge for boom truck/crane | Sales Associate / System | Store Logistics Coordinator | 10–15 min |
| 3 | **Order Splitting & Fulfillment Routing**: (a) system splits order into delivery stages per customer's selection; (b) each stage creates a separate fulfillment order with: (i) assigned items and quantities; (ii) scheduled delivery date/time window; (iii) assigned vehicle type; (iv) assigned delivery partner (own fleet for within-city, 3PL for long-distance); (c) for items stocked at DC: system generates transfer request to ship items to store for consolidated delivery (if store doesn't stock item); (d) for items stocked at store: items pulled from shelf or yard and staged in backroom delivery holding area; (e) system reserves ATP for all staged items across all delivery phases — preventing stock diversion to other orders; (f) if any item unavailable: Sales Associate contacts customer to discuss substitution (W279) or delay affected phase | System / Store Logistics Coordinator | — | 15–30 min |
| 4 | **Delivery Execution per Stage**: For each delivery stage: (a) day before scheduled delivery: system sends reminder to customer (SMS/app) with delivery window, driver name, vehicle plate, and contact number; (b) delivery team loads vehicle at store — Store Logistics Coordinator verifies items against delivery manifest; (c) driver departs with delivery manifest and customer contact; (d) upon arrival: driver contacts customer/site contact; unloads items per agreed method; (e) customer/site contact signs delivery receipt with quantity verification — notes any discrepancies or damage on receipt; (f) driver photographs delivered items at site as proof of delivery; (g) system updates delivery stage status: Delivered, Partially Delivered (with discrepancy notes), or Failed (customer unavailable, site inaccessible) | Delivery Partner / Store Logistics Coordinator | Store Manager | 2–6 hours per delivery trip |
| 5 | **Discrepancy & Issue Resolution**: (a) if delivery discrepancy noted on receipt (wrong item, short quantity, damage): (i) Store Logistics Coordinator contacts customer within 4 hours; (ii) for wrong/short items: schedule corrective delivery within 24–48 hours from store stock or DC replenishment; (iii) for damage: initiate damage claim against delivery partner per W500 transfer order in-transit damage process; (iv) customer issued store credit per W781 for inconvenience if BuildRight-caused; (b) if failed delivery (customer not home, site inaccessible): (i) driver attempts phone contact; (ii) if unreachable: return items to store; (iii) Store Logistics Coordinator contacts customer to reschedule within 24 hours; (iv) second failed delivery attempt: customer responsible for re-delivery fee | Store Logistics Coordinator / Delivery Partner | Store Manager | 1–4 hours per issue |
| 6 | **Project Delivery Completion & Record**: (a) after final delivery stage completed: system marks project delivery order as "Completed"; (b) system generates project delivery summary: total items delivered, delivery stages completed, any outstanding discrepancies; (c) customer satisfaction survey sent per W65 within 48 hours; (d) system logs project delivery record against customer's loyalty account for future reference; (e) if customer has Project Vault (W894): delivery completion updates project list status | System / Store Logistics Coordinator | — | 10–15 min post-completion |

### System Touchpoints

- In-store POS/order management for large order creation
- Delivery planning module with phased scheduling capability
- ATP reservation system across delivery phases (W536)
- Transfer order system for DC-to-store stock replenishment (W4)
- Fleet/3PL dispatch management (W52, W196)
- Customer notification module (W708) for delivery reminders
- Proof-of-delivery capture (mobile app for driver)
- Delivery discrepancy and claims module (W500)
- Store credit issuance (W781) for service recovery
- BI dashboard for project delivery analytics (delivery accuracy, cost per delivery, customer satisfaction by region)
- LGU truck ban compliance module (W431) for delivery time windows

### Pain Points / Risks

- **Construction schedule delays cascading**: if customer's construction is delayed (common in the Philippines due to weather, permit delays, contractor availability), pre-scheduled deliveries must be rescheduled; flexible rescheduling without penalty is essential for customer retention
- **Last-mile site accessibility**: Philippine construction sites in dense urban areas (narrow alleys in Metro Manila, hillside lots in Baguio/Cebu, island locations in Visayas) often cannot accommodate standard 10-wheeler trucks; requires smaller vehicles or manual carry-in — adding cost and time
- **ATP reservation across multiple delivery stages**: reserving stock for a Phase 3 delivery that is 4 weeks out ties up inventory that could be sold to walk-in customers; dynamic ATP allocation with safety stock buffer needed
- **Customer changing mind mid-project**: customer may swap tile selection or add fixtures after initial order; modifying a multi-stage delivery plan mid-execution is operationally complex
- **Delivery partner reliability for project orders**: 3PL partners used to parcel delivery may not handle flatbed/boom truck requirements or construction-site delivery protocols; dedicated project delivery partners needed
- **Cash-on-delivery risk for large orders**: PHP 100K+ orders delivered COD carry risk of customer refusal at delivery point; for project orders > PHP 50K: require at least 50% deposit at order placement per W546

### Staffing Implication

- **Store Logistics Coordinator**: role absorbed by Receiving Clerk (1 of 2 per store) with expanded delivery coordination duties; ~2–3 hours/day on project delivery coordination during peak; existing Receiving Clerk handles inbound receiving and outbound delivery coordination
- **Sales Associates**: ~15–20 min per large order for delivery needs assessment; absorbed by existing floor staff
- **No incremental headcount**.

### Time Estimate

- Needs assessment: 15–20 min
- Delivery plan creation: 10–15 min
- Order splitting and routing: 15–30 min
- Per-stage delivery execution: 2–6 hours (driver + loading + transit + unloading)
- Discrepancy resolution: 1–4 hours per issue
- Post-completion record: 10–15 min
- **Total project coordination**: ~3–6 hours of staff time across all stages (excluding driver time)

---

## W905. Customer Project Photo Gallery & Social Proof/Inspiration Platform

| Field | Detail |
|---|---|
| **Trigger** | Customer-submitted project photos are approved via W914 review program, or ecommerce team creates curated project inspiration content from vendor partnerships; also triggered by customer browsing behavior indicating project research |
| **Frequency** | ~1,000–1,500 new project gallery entries/month |
| **Volume** | Average 4–8 product photos per gallery entry; ~50,000–80,000 gallery views/month |
| **Owner** | Digital Commerce Manager |
| **Participants** | Customer, Marketing Coordinator (content curation), Category Manager (product tagging), Digital Commerce Manager |

### Background

Home improvement purchases are highly visual and research-driven. Before starting a bathroom renovation, a typical BuildRight customer browses 20–30 project images online for inspiration, then researches specific products. BuildRight's ecommerce platform currently has product-centric pages but lacks a dedicated project inspiration gallery — a gap that competitors (both local hardware chains and international platforms like Houzz/Pinterest) exploit to capture the customer early in the purchase journey. This workflow manages the ecommerce "Project Gallery" — a browsable, searchable collection of customer-completed projects and curated inspiration boards, each linked to specific BuildRight products. It serves as both a customer acquisition tool (SEO traffic from project searches) and a conversion tool (project-to-product-to-cart journey). The gallery integrates with Project Vault (W894) for one-click "Get This Look" project list creation and with the Project Completion Celebration program (W914) for user-generated content sourcing.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Content Sourcing & Creation**: Project gallery content sourced from: (a) W914 program — customer-submitted project photos with product tags and reviews (primary source, ~60% of content); (b) vendor co-created content — vendor provides professional project photos featuring their products sold at BuildRight, with co-branding per W513 co-op advertising agreements; (c) BuildRight in-house creative — professional photoshoot of model rooms using BuildRight products for seasonal campaigns (W83); (d) DIY workshop output (W147) — attendee project photos from workshops with consent; (e) social media user-generated content — BuildRight social media team identifies high-quality customer posts tagged with #BuildRightDepot and requests permission for gallery inclusion per RA 10173 | Marketing Coordinator / Vendor / System | Digital Commerce Manager | 10–20 hours/week |
| 2 | **Product Tagging & Enrichment**: (a) each gallery entry tagged with: project type, room/area, style (modern, industrial, minimalist, tropical Filipino, Mediterranean), estimated budget range, difficulty level (DIY-friendly, intermediate, professional recommended), and products used; (b) product tagging: Marketing Coordinator or Category Manager identifies specific SKUs from gallery photos and links to active product pages; if a product is discontinued, system links to current alternative per W279; (c) project metadata: store location where materials were purchased (if known from loyalty data), contractor who executed (if from W904 referral), and related Project Vault templates (W894); (d) SEO optimization: project title, description, and alt-text optimized per W563 SEO strategy for project-related search queries ("small bathroom renovation Philippines", "concrete fence design ideas") | Marketing Coordinator / Category Manager / System | Digital Commerce Manager | 15–20 min per entry |
| 3 | **Gallery Publication & Browsing Experience**: (a) published on BuildRight ecommerce site as dedicated "Project Ideas" section with: (i) category filter (bathroom, kitchen, outdoor, living room, fencing, roofing, electrical, plumbing, flooring, paint); (ii) budget filter (under PHP 20K, PHP 20K–50K, PHP 50K–100K, PHP 100K–500K, above PHP 500K); (iii) difficulty filter; (iv) style filter; (v) search bar for natural language queries; (b) each project entry displays: hero image, project description, before-and-after (if available), product carousel with linked SKUs and current prices, estimated total project cost, "Save to My Projects" button (W894), "Get This Look" button (creates project list in W894), customer rating, and social share buttons; (c) mobile-first design with swipeable image carousels optimized for Philippine market (80%+ mobile traffic per W615) | System / Digital Commerce Manager | — | Ongoing platform feature |
| 4 | **Conversion Path & Attribution**: (a) "Get This Look" flow: customer clicks button → system creates project list in Project Vault (W894) pre-populated with tagged products → customer reviews, modifies quantities, checks ATP → adds items to cart or saves for later; (b) individual product click-through: customer clicks a tagged product in gallery photo → navigates to product detail page with "As seen in [Project Name]" badge → standard product page conversion flow; (c) conversion attribution: system tracks gallery entry → product view → cart → purchase with multi-touch attribution per W565; (d) gallery entries with high conversion rates (>2% gallery-to-purchase) featured on homepage and in marketing campaigns per W83 | System / Customer | Digital Commerce Manager | Automated |
| 5 | **Gallery Performance Analytics & Optimization**: (a) weekly: gallery traffic, top-viewed projects, top-clicked products, conversion rate by project type; (b) monthly: SEO performance (organic traffic from project-related keywords, click-through rate from search results), gallery-to-cart conversion funnel, most-saved projects to Project Vault, social engagement (shares, saves, comments); (c) quarterly: content gap analysis — project types with high search volume but low gallery coverage identified for content creation priority; vendor content contribution review; A/B testing of gallery layout and CTA placement; (d) annual: gallery revenue attribution and ROI analysis | Digital Commerce Manager / System | VP Marketing | 4–6 hours/month |

### System Touchpoints

- Ecommerce platform with dedicated Project Gallery section
- Project Vault (W894) for "Get This Look" project list creation
- Product catalog and detail pages for linked SKU display
- Inventory/ATP system for real-time stock status on tagged products
- Loyalty/CDP system (W156) for customer identification and personalization
- SEO tools (W563) for organic traffic optimization
- Social media management platform (W142) for UGC sourcing
- Content management system for gallery curation and moderation
- BI dashboard for gallery analytics and attribution
- Digital signage (W504) for in-store project inspiration display

### Pain Points / Risks

- **Content freshness**: outdated project photos with discontinued products reduce credibility; automated product availability check on gallery entries with "Last verified" date stamp mitigates; quarterly content audit required
- **Low "Get This Look" conversion**: customers may browse for inspiration but purchase elsewhere; competitive pricing, real-time availability, and seamless cart integration reduce friction; exclusive "Gallery Price" promotions for project bundles tested quarterly
- **Photo quality inconsistency**: user-generated content varies in quality; gallery design with consistent framing (border, overlay text) and curation standards maintain professional appearance
- **Vendor content bias**: vendor-provided content may feature products not available at BuildRight or at non-competitive prices; product tag verification against active assortment per W252 required before publication
- **SEO competition**: competing against established platforms (Houzz, Pinterest) for project-related search traffic; Philippine-specific content and local project context provides differentiation

### Staffing Implication

- **Marketing Coordinator**: ~10–15 hours/week on content sourcing, tagging, and gallery curation; absorbed by existing role
- **Category Manager**: ~3–5 hours/month on product tagging verification; absorbed by existing role
- **Digital Commerce Manager**: ~4–6 hours/month on analytics and optimization; absorbed by existing role
- **No incremental headcount**

### Time Estimate

- Content sourcing and creation: 10–20 hours/week
- Product tagging per entry: 15–20 min
- Gallery publication: automated
- Monthly analytics: 4–6 hours
- Quarterly optimization: 8–10 hours
- **Total ongoing**: ~20–30 hours/week across all participants

---

## W907. Customer Consumables Subscription & Auto-Replenishment Service

| Field | Detail |
|---|---|
| **Trigger** | Customer enrolls eligible SKUs in auto-replenishment subscription via ecommerce, mobile app, or in-store; or system suggests subscription based on repeat purchase pattern analysis |
| **Frequency** | ~2,000–3,000 active subscriptions at steady state; ~500–800 subscription orders/month |
| **Volume** | Average 3–5 SKUs per subscription; monthly or bi-monthly delivery cadence |
| **Owner** | Digital Commerce Manager |
| **Participants** | Customer, Ecommerce Fulfillment Team (W19), Supply Planning (replenishment), Marketing Coordinator (subscription analytics) |

### Background

Many BuildRight customers purchase the same consumable products repeatedly: painters who buy the same paint brand monthly, contractors who restock adhesive and screws bi-weekly, hotels and property managers who need cleaning supplies and lightbulbs on a regular schedule, and DIY enthusiasts who maintain their homes with seasonal supplies. Currently, these customers re-order manually each time — a friction point that competitors with subscription models exploit. A subscription/auto-replenishment service allows customers to set up recurring deliveries of their regular-use items at a discounted price (5–10% subscription discount), with flexible delivery frequency and easy modification. This drives predictable recurring revenue, increases customer lifetime value, reduces customer acquisition cost (subscriber retention is higher than one-time buyer retention), and provides BuildRight with valuable demand forecasting data for replenishment planning (W31). This is especially relevant for the Philippine market where sari-sari stores have traditionally provided informal "running tab" regularity for household consumables — BuildRight's subscription service digitizes this behavior for the home improvement segment.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Subscription Enrollment**: Customer enrolls via: (a) ecommerce product page — "Subscribe & Save" button with frequency selection (weekly, bi-weekly, monthly, bi-monthly, quarterly) and discount display; (b) mobile app — "Auto-Replenish" feature on product detail or from purchase history; (c) in-store Pro Desk or customer service counter — Sales Associate sets up subscription for customer via POS/associate terminal; (d) system-suggested subscription — system identifies repeat purchase patterns (same SKU purchased 3+ times in 6 months) and sends personalized subscription offer via W708 with one-click enrollment; (e) enrollment captures: SKU(s), quantity, frequency, delivery address, payment method (stored card or e-wallet), subscription discount (5% standard, 10% for 5+ SKUs), and preferred delivery day of week | Customer / Sales Associate / System | Digital Commerce Manager | 5–10 min |
| 2 | **Subscription Order Generation**: (a) system auto-generates order based on frequency and last delivery date; (b) 3 days before order generation: customer receives "Upcoming Order" notification with current order details and option to modify (change quantity, skip, add items, change delivery date); (c) system checks ATP at fulfillment location per W536; if any item unavailable: (i) auto-substitute per W279 if customer pre-approved substitution; (ii) customer notification with alternative options; (iii) partial shipment with backorder if customer consents; (d) order created in unified order management system per POS-045 with subscription flag and discount applied; (e) payment authorization attempted on stored payment method; if declined: customer notified with 48-hour resolution window before order cancellation | System / Customer | — | Automated |
| 3 | **Subscription Fulfillment**: (a) subscription orders enter standard fulfillment pipeline: DC pick/pack/ship per W19 for home delivery, or store pick per W11 for BOPIS; (b) subscription orders flagged for priority picking (subscription customers are high-value, high-retention — SLA priority over one-time orders); (c) delivery executed per standard home delivery process (W19) or BOPIS (W11); (d) customer receives tracking notification per W592; (e) delivery confirmation triggers next delivery date calculation and subscription calendar update | Ecommerce Fulfillment Team / System | — | Standard fulfillment time |
| 4 | **Subscription Modification & Management**: Customer modifies subscription via: (a) mobile app "My Subscriptions" dashboard — change items, quantities, frequency, delivery address, payment method, skip next delivery, pause (up to 90 days), or cancel; (b) customer service counter — assisted modification; (c) customer service hotline — CSR modifies subscription in system; (d) cancellation analytics: system captures cancellation reason (price, quality, delivery, no longer needed, competitor) and triggers retention offer for price/competitor cancellations (one-time discount or free shipping for 3 months); (e) subscription reactivation: cancelled subscriptions with reactivation potential flagged at 60 days for re-engagement campaign per W618 | Customer / System / CSR | Digital Commerce Manager | 3–5 min per modification |
| 5 | **Subscription Analytics & Optimization**: (a) weekly: active subscription count, new enrollments, cancellations (churn rate), average items per subscription, average order value; (b) monthly: subscriber cohort analysis (enrollment month → retention rate by month), subscriber vs. non-subscriber LTV comparison, subscription revenue as % of ecommerce revenue, popular subscription SKUs and categories; (c) quarterly: discount profitability analysis (subscription discount cost vs. margin from predictable demand and reduced acquisition cost), subscription program ROI, A/B testing of discount levels and frequency options, supply planning integration for subscription demand forecasting (W31); (d) annual: program expansion plan — new eligible SKU categories, tiered subscription program (Silver/Gold/Platinum with escalating benefits), and partnership subscriptions (e.g., paint manufacturer co-branded subscription with color-of-the-month delivery) | Digital Commerce Manager / Supply Planning / System | VP Marketing | 4–6 hours/month |

### System Touchpoints

- Ecommerce platform with subscription management module
- Mobile app (W615) with "My Subscriptions" dashboard
- POS system for in-store subscription enrollment
- Unified order management (POS-045/W536) for subscription order routing
- Inventory/ATP system for availability checking
- Payment gateway (W611) for stored payment processing and auto-authorization
- Home delivery fulfillment (W19) and BOPIS (W11)
- Customer communication module (W708) for upcoming order notifications
- CDP (W156) for repeat purchase pattern analysis and subscription suggestions
- Supply planning/demand forecasting (W31) for subscription demand integration
- BI dashboard for subscription analytics and cohort analysis

### Pain Points / Risks

- **Payment method expiry/failure**: stored credit cards expire or are declined; pre-authorization check 3 days before order with customer notification for payment update; 2 failed attempts triggers subscription pause with customer alert
- **Cannibalization of full-price sales**: customers who would have purchased at full price subscribe at a discount; mitigate by limiting subscription to designated "subscription-eligible" SKUs (consumables, replacement items, seasonal maintenance products) and excluding new/seasonal items
- **Subscription fatigue**: customers accumulate too many subscriptions and cancel in frustration; recommended maximum of 10 SKUs per subscription with clear per-SKU cost transparency
- **Inventory allocation conflict**: subscription orders competing with one-time orders for limited stock; subscription allocation buffer (5% of safety stock reserved for subscriptions) with dynamic adjustment based on subscriber count
- **Delivery cost erosion**: frequent small subscription orders increase per-order delivery cost; minimum subscription order value (PHP 1,500 for free delivery) or combined delivery batching for customers with multiple subscriptions
- **Data privacy for stored payment**: PCI-DSS compliance for stored card data per POS-049; RA 10173 consent for auto-charging required at enrollment with clear cancellation rights

### Staffing Implication

- **Digital Commerce Manager**: ~4–6 hours/month on program strategy and analytics; absorbed by existing role
- **Ecommerce Fulfillment Team**: subscription orders integrated into standard fulfillment with priority flag; ~10–15% increase in regular orders at steady state; absorbed with incremental volume
- **CSR Team**: ~2–3 subscription modification calls/day chain-wide; absorbed by existing call center capacity (W259)
- **No incremental headcount at store level**

### Time Estimate

- Subscription enrollment: 5–10 min (customer time)
- Order generation: automated
- Subscription modification: 3–5 min
- Monthly analytics: 4–6 hours
- Quarterly optimization: 8–10 hours
- **Total per subscription lifecycle**: ~20–30 min of staff time over 12 months (enrollment + modifications + cancellation handling)

## W917. Ecommerce Live Commerce & Social Selling Operations

| Field | Detail |
|---|---|
| **Trigger** | Scheduled live commerce session on social media platform (Facebook Live, TikTok Live); flash product launch; seasonal campaign event |
| **Frequency** | 4–6 live sessions/week chain-wide (2–3 on Facebook Live, 1–2 on TikTok Live, 1 on buildright.com.ph); ~20–24 sessions/month |
| **Volume** | Average 500–2,000 live viewers per session; ~200–500 orders per session; average order value PHP 2,500–4,000 |
| **Owner** | Digital Commerce Manager |
| **Participants** | Marketing Host/Presenter, Category Manager (product expert), Ecommerce Fulfillment Team (W19, W11), Social Media Manager (W142), Customer Service (W258) |

### Background

Live commerce (selling products through live video streaming on social media) has exploded in the Philippines — the country ranks among the highest in Southeast Asia for social media engagement and live commerce adoption. Facebook Live and TikTok Live are dominant platforms, with Filipino consumers actively purchasing during live streams through integrated checkout (TikTok Shop) or comment-to-order (Facebook Live). For BuildRight, live commerce presents a unique opportunity: (a) demonstrate products in real-time — show how a power drill handles concrete, how paint colors look on actual walls, how tiles appear under different lighting; (b) answer customer questions live — technical advice on product selection for specific projects; (c) drive urgency through limited-time live-only promotions and flash discounts; (d) reach customers in areas without a nearby BuildRight store; (e) build community and trust through authentic, unscripted product demonstrations. Home improvement is particularly suited to live commerce because products are tactile and benefit from visual demonstration. This workflow covers the full live commerce cycle from session planning to order fulfillment and analytics.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Live Commerce Session Planning**: (a) weekly: Digital Commerce Manager and Category Manager select products for upcoming live sessions based on: seasonal calendar per W264 (rainy season = waterproofing products; ber months = holiday décor), trending products from POS data per W522, new product launches per W569, and vendor co-sponsorship availability per W513; (b) session format selection: (i) product demo + Q&A (30–45 min), (ii) flash sale with countdown (15–20 min), (iii) DIY tutorial + product selling (45–60 min), (iv) contractor pro-tips session (30 min, targeting B2B); (c) product selection criteria: visually demonstrable, available ATP at fulfillment DC per W536, live-only promotional pricing approved per W300, and inventory depth sufficient for expected demand (minimum 200 units per featured SKU); (d) promotional pricing: live-only discount (10–20% off SRP) or bundle offer per W910; discount approved by Category Manager per discount authority matrix; (e) session logistics: host/presenter assigned, product samples prepared for studio/staging area, backdrop and lighting set up in ecommerce studio at HQ | Digital Commerce Manager / Category Manager | VP Marketing | 4–6 hours/week |
| 2 | **Pre-Live Promotion & Audience Building**: (a) 48 hours before session: promotional posts on Facebook page, Instagram stories, and TikTok teaser video per W142 announcing date/time, featured products, and live-only discount; (b) email notification to loyalty members in relevant segment per W673 (e.g., DIY enthusiasts for tool demos, contractors for pro-tips sessions); (c) push notification via BuildRight mobile app per W615; (d) session event page created on Facebook with RSVP; (e) product page on buildright.com.ph updated with "Watch Live" badge linking to stream; (f) inventory pre-reservation: system reserves minimum expected quantity for live session orders (released after session if unsold) | Social Media Manager / Digital Commerce Manager | — | 2–3 hours/session |
| 3 | **Live Session Execution**: (a) host goes live on scheduled platform; (b) session flow: introduction and agenda (2 min), product demonstration with close-up camera work (15–20 min), live Q&A from viewer comments (10 min), flash sale announcement with countdown timer (5 min), closing with next session teaser (2 min); (c) purchasing mechanism: (i) TikTok Shop: direct purchase via TikTok Shop integration with real-time inventory check; (ii) Facebook Live: comment-to-order (customer comments "ORDER [product code] [quantity]") → system captures order from comment feed and creates ecommerce order → customer receives DM with payment link; (iii) buildright.com.ph: embedded live stream with "Buy Now" button synced to ecommerce checkout; (d) Category Manager monitors comments and provides technical answers to host via earpiece; (e) Customer Service team monitors order queue and handles payment failures or customer inquiries in real-time; (f) system enforces live-only pricing with automatic price revert when session ends | Marketing Host / Category Manager / Customer Service / System | Digital Commerce Manager | 30–60 min/session |
| 4 | **Post-Session Order Processing & Fulfillment**: (a) within 1 hour of session end: all live commerce orders compiled and batch-processed in unified order management per W536; (b) orders routed to fulfillment: DC pick/pack/ship per W19 for home delivery, or BOPIS per W11; (c) fulfillment SLA: live commerce orders shipped within 24 hours (priority flag over standard ecommerce orders); (d) customer notifications: order confirmation (within 1 hour), shipping confirmation with tracking (within 24 hours), delivery notification per W592; (e) payment reconciliation: all live session payments reconciled against order records per W611; (f) unfilled orders (stock-out from higher-than-expected demand): customer notified with apology and offered: (i) backorder with expected ship date, (ii) substitute product per W279, or (iii) refund per W101 | Ecommerce Fulfillment Team / System / Customer Service | Digital Commerce Manager | 2–3 hours post-session |
| 5 | **Live Commerce Analytics & Optimization**: (a) per session: viewership metrics (peak concurrent viewers, average view duration, total unique viewers), engagement rate (comments, reactions, shares), conversion rate (viewers → orders), average order value, total GMV, top-selling products, cart abandonment rate during session; (b) weekly: session comparison — which format, time slot, and product category performs best; audience growth trend; repeat live-commerce shopper rate; (c) monthly: live commerce as % of total ecommerce revenue, customer acquisition cost via live commerce vs. other channels, return rate for live commerce orders (indicative of product expectation vs. reality), and host/presenter performance rating; (d) quarterly: platform mix optimization (Facebook vs. TikTok vs. own site), vendor co-sponsorship ROI per W513, and live commerce content calendar for next quarter aligned with seasonal calendar per W306; (e) annual: live commerce program ROI, investment in studio equipment and talent, and expansion plan (new platforms, new session formats, regional-language sessions for VisMin markets) | Digital Commerce Manager / Social Media Manager / System | VP Marketing | 4–6 hours/month |

### System Touchpoints

- Ecommerce platform with TikTok Shop and Facebook Live integration
- Unified order management (W536) for live commerce order routing
- Inventory/ATP system for real-time stock reservation and availability check
- Payment gateway (W611) for payment link generation and reconciliation
- Social media management system (W142) for pre-live promotion and session management
- Customer communication module (W708) for order notifications
- Loyalty system (W17) for segment-based email targeting
- Mobile app (W615) for push notification delivery
- Product catalog (W50) for product page "Watch Live" integration
- Promotional pricing system (W300) for live-only discount configuration with automatic expiry
- BI dashboard for live commerce analytics
- CDP (W156) for audience targeting and repeat shopper tracking

### Pain Points / Risks

- **Technical failure during live stream**: internet outage, camera malfunction, or platform crash disrupts session; mitigated by backup internet (mobile hotspot), backup camera, and platform-specific contingency (switch to alternate platform mid-stream); session rescheduled if unrecoverable
- **Higher-than-expected demand**: stock-outs during live session create customer disappointment visible to all viewers; mitigated by inventory pre-reservation, real-time inventory display on product overlay during stream, and immediate backorder communication
- **Negative live comments**: dissatisfied customers may post negative comments visible to all viewers; mitigated by Category Manager monitoring comments and flagging to host for live response; Customer Service immediate follow-up per W258; negative comment pattern triggers session pause
- **Host performance inconsistency**: not all hosts are equally engaging or knowledgeable; mitigated by host training, Category Manager earpiece support, and monthly host performance rating per W31
- **Payment failures**: comment-to-order customers may not complete payment; mitigated by 24-hour payment deadline with automated reminder, and 2 payment reminders before order cancellation
- **Regulatory compliance**: DTI Sales Promotion Permit required for live-only promotions per W427; prices displayed must comply with Consumer Act per W731; "live-only" claims must be genuine (price available only during live session, not simultaneously on website)

### Staffing Implication

- **Marketing Host/Presenter**: 1 dedicated FTE at HQ for live commerce hosting (4–6 sessions/week × 1 hour + preparation = ~20–25 hours/week); new role or absorbed by existing Marketing staff with live commerce aptitude
- **Digital Commerce Manager**: ~4–6 hours/week on planning and analytics; absorbed by existing role
- **Category Manager**: ~1–2 hours/week providing product expertise during sessions; absorbed by existing role
- **Customer Service**: ~2–3 hours/session on live order processing; absorbed by existing call center capacity per W259
- **Ecommerce Fulfillment Team**: live commerce orders integrated into standard fulfillment with priority flag; absorbed with incremental volume
- **Net new**: 1 Marketing Host (PHP 360–480K/year) or absorbed by existing Marketing team

### Time Estimate

- Session planning: 4–6 hours/week (consolidated)
- Pre-live promotion: 2–3 hours/session
- Live session execution: 30–60 min/session
- Post-session processing: 2–3 hours/session
- Monthly analytics: 4–6 hours
- **Total per session**: ~6–9 hours of staff time (planning + execution + post-session)

## W923. Ecommerce Assembly & Installation Service Upsell at Online Checkout

| Field | Detail |
|---|---|
| **Trigger** | Customer adds eligible product to ecommerce cart (appliances, ceiling fans, water heaters, light fixtures, bathroom fixtures, kitchen sinks, air conditioning units) |
| **Frequency** | ~12,000–15,000 eligible transactions/month (products in installation-eligible categories) |
| **Volume** | ~15–20% service attachment rate target; ~1,800–3,000 installation service upsells/month |
| **Owner** | Digital Commerce Manager |
| **Participants** | Customer, Ecommerce Platform, Service Operations Team (W138), Installation Partners (W213), Customer Service (W258) |

### Background

BuildRight sells many products that require professional installation: air conditioning units, ceiling fans, water heaters, light fixtures, kitchen sinks, bathroom fixtures, and built-in appliances. In-store, Sales Associates can recommend installation services during the sales conversation (per W544 POS service work order creation). However, online customers purchasing these products have no equivalent touchpoint — they buy the product, receive it, and then must independently find an installer. This creates a gap: (a) lost service revenue for BuildRight (installation margins are 30–40% vs. 28–32% on merchandise); (b) poor customer experience (customer must coordinate delivery + installation separately); (c) competitive disadvantage (competitors offering bundled installation win the sale); and (d) warranty risk (improper self-installation voids manufacturer warranty, leading to returns and complaints per W33). This workflow adds an automated installation service upsell at online checkout for eligible products, integrating service scheduling, pricing, and fulfillment into the ecommerce purchase flow. It leverages BuildRight's existing installation service infrastructure (W138 home installation, W213 partner quality audit) and service SKU catalog (W794).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Eligibility Detection & Service Presentation**: (a) when customer adds an installation-eligible product to cart, system displays service upsell module on product page and at checkout: "Add Professional Installation for PHP [X,XXX]"; (b) service pricing dynamically calculated based on: product category (each category has a base installation fee in service SKU master per W794), product complexity (e.g., split-type AC installation > window-type), customer location (metro vs. provincial — provincial surcharge for installer travel), and any active service promotions per W13; (c) service module displays: installation description (what's included), estimated timeline ("Installation within 3–5 business days after delivery"), installer资质 ("Certified BuildRight Installation Partner"), warranty information ("90-day installation warranty"), and customer reviews/ratings per W510; (d) customer can select: (i) product only (no installation), (ii) product + standard installation, (iii) product + premium installation (includes old unit removal, additional materials, extended warranty) | System / Customer | — | Automated |
| 2 | **Service Order Creation at Checkout**: (a) if customer selects installation: service SKU added to cart as a line item alongside the product; (b) cart shows: product price + installation price as separate line items (transparency per Consumer Act RA 7394 per W731); (c) at checkout: customer selects delivery date from available slots; system displays available installation dates (starting 1–2 days after delivery to allow for product arrival); (d) customer confirms delivery address and installation address (may differ — e.g., customer buys at home, installs at rental property); (e) payment: total amount (product + installation) charged as single payment; installation revenue deferred per PFRS 15 until service completion per W487; (f) order confirmation sent to customer with: product delivery schedule, installation appointment date/time window, installer contact information, and preparation checklist ("Please ensure old unit is removed and electrical/plumbing connections are accessible") | System / Customer | — | Automated |
| 3 | **Service Fulfillment Coordination**: (a) order splits into: (i) merchandise fulfillment (DC pick/pack/ship per W19 or BOPIS per W11) and (ii) service fulfillment (installation work order created per W544); (b) installation work order assigned to certified Installation Partner per W213 based on: geographic coverage, product specialization, partner rating, and current workload; (c) Installation Partner receives work order via partner mobile app with: customer details, product details, installation address, scheduled date/time, installation instructions, and any special requirements noted by customer; (d) merchandise delivery triggers installation scheduling confirmation to customer: "Your [product] has been delivered. Your installation is confirmed for [date] between [time window]"; (e) if merchandise delivery is delayed: installation date auto-rescheduled and customer notified per W708 | System / Service Operations Team / Installation Partner | Digital Commerce Manager | 5–10 min (system-automated) |
| 4 | **Installation Execution & Quality Verification**: (a) Installation Partner arrives at customer location on scheduled date; (b) partner verifies: product delivered matches work order, installation area is prepared per checklist, and customer is present; (c) installation completed per manufacturer specifications and BuildRight quality standards per W213; (d) partner captures: before/after photos (uploaded to work order), time spent, materials used beyond standard kit, and customer sign-off on work order completion via partner mobile app; (e) customer receives post-installation survey per W756 (3 questions: installation quality, installer professionalism, overall satisfaction); (f) if customer reports issue: service complaint processed per W795 with 48-hour resolution SLA | Installation Partner / Customer | Service Operations Team | Varies by installation |
| 5 | **Revenue Recognition & Partner Settlement**: (a) installation completion confirmed by partner sign-off + customer satisfaction = service revenue recognized per PFRS 15 per W487; (b) Installation Partner payment: partner invoice generated against work order; 3-way match (work order → completion confirmation → partner invoice); payment per partner agreement terms (typically net 15) per W7; (c) monthly: installation attachment rate by product category, average installation revenue per order, customer satisfaction score, partner performance scorecard per W213; (d) quarterly: installation pricing review (are prices competitive with independent installers?), attachment rate optimization (improve upsell copy, add product photos showing installation), and partner capacity planning (hire more partners in underserved areas); (e) annual: installation service program ROI — service revenue, merchandise revenue uplift from bundled offers, customer retention improvement for installed-product buyers, and warranty claim rate comparison (installed vs. self-installed) | Finance / Service Operations Team / System | VP Services | 4–6 hours/month |

### System Touchpoints

- Ecommerce platform checkout module with service upsell integration
- Service SKU catalog (W794) for installation pricing and product eligibility
- Unified order management (W536) for order splitting (merchandise + service)
- Service work order system (W544) for installation scheduling
- Installation partner mobile app for work order management and completion
- Payment gateway (W611) for combined payment processing
- Revenue recognition module (W487) for deferred installation revenue
- Customer communication module (W708) for scheduling notifications
- Customer satisfaction module (W756) for post-installation survey
- Installation partner quality system (W213) for partner rating and assignment
- AP system (W7) for partner payment processing
- BI dashboard for attachment rate and revenue analytics

### Pain Points / Risks

- **Low attachment rate**: customers may skip installation to save cost or because they have their own installer; mitigated by competitive pricing (benchmark against independent installers), convenience messaging, and "protect your warranty" communication
- **Installation scheduling conflicts**: customer not home at scheduled time, or product not yet delivered; mitigated by delivery tracking integration, automated reminders per W708, and rescheduling via customer service per W258
- **Installer quality inconsistency**: some partners deliver poor workmanship; mitigated by W213 quality audit program, customer satisfaction survey, and partner scorecard with minimum rating threshold (partners below 4.0/5.0 for 2 consecutive quarters placed on probation)
- **Liability for installation defects**: BuildRight bears liability for partner-installed work; mitigated by installation warranty (90-day BuildRight warranty), partner liability insurance requirement per W818, and product liability insurance per W185
- **Cannibalization of DIY customers**: some customers who would self-install may opt for paid installation, reducing the DIY brand positioning; mitigated by keeping DIY tutorials freely available per W147 and positioning installation as an option (not default) at checkout

### Staffing Implication

- **Service Operations Team**: ~2–3 hours/day on installation coordination for ecommerce orders; absorbed by existing team per W138
- **Customer Service**: ~1–2 hours/day on installation scheduling inquiries; absorbed by existing capacity per W259
- **Digital Commerce Manager**: ~2–3 hours/week on upsell optimization and analytics; absorbed by existing role
- **No incremental headcount**

### Time Estimate

- Service presentation at checkout: automated
- Service order creation: automated
- Fulfillment coordination: 5–10 min (system-automated)
- Post-installation verification: automated (customer survey)
- Monthly analytics: 4–6 hours
- **Total per installation order**: ~10–15 min of staff time (coordination) + Installation Partner time
