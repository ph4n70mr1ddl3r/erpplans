# Supply Chain Planning Workflows

> Demand forecasting, seasonal buy planning, S&OP cycle, international logistics & import operations, supply chain network optimization, global supply chain incoterm & marine insurance tracking, import port demurrage & detention management, supply chain control tower & real-time shipment visibility, store-level replenishment exception management & auto-override, mock product recall exercise & recall readiness testing, and cross-functional new store opening readiness review.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W31. Demand Forecasting Cycle](#w31-demand-forecasting-cycle)
- [W32. Seasonal Buy Planning](#w32-seasonal-buy-planning)
- [W133. Sales & Operations Planning (S&OP) Cycle](#w133-sales-operations-planning-sop-cycle)
- [W144. International Logistics & Import Operations](#w144-international-logistics-import-operations)
- [W183. Supply Chain Network Optimization Review](#w183-supply-chain-network-optimization-review)
- [W191. Global Supply Chain — Incoterm & Marine Insurance Tracking](#w191-global-supply-chain-incoterm-marine-insurance-tracking)
- [W249. Import Port Demurrage & Detention Management](#w249-import-port-demurrage-detention-management)
- [W250. Supply Chain Control Tower & Real-Time Shipment Visibility](#w250-supply-chain-control-tower-real-time-shipment-visibility)
- [W268. Last-Mile Home Delivery Tracking & Proof-of-Delivery](#w268-last-mile-home-delivery-tracking-proof-of-delivery)
- [W284. Customs Bonded Warehouse (CBW) Operations & Duty Deferral](#w284-customs-bonded-warehouse-cbw-operations-duty-deferral)
- [W464. In-House Customs Brokerage & Port Operations](#w464-in-house-customs-brokerage--port-operations)
- [W558. Supplier Risk Assessment & Supply Disruption Contingency Planning](#w558-supplier-risk-assessment--supply-disruption-contingency-planning)
- [W596. Store-Level Replenishment Exception Management & Auto-Override](#w596-store-level-replenishment-exception-management--auto-override)
- [W622. Mock Product Recall Exercise & Recall Readiness Testing](#w622-mock-product-recall-exercise--recall-readiness-testing)
- [W623. Cross-Functional New Store Opening Readiness Review](#w623-cross-functional-new-store-opening-readiness-review)
- [W727. Carrier & Freight Forwarder Daily Performance Monitoring](#w727-carrier--freight-forwarder-daily-performance-monitoring)
- [W728. Port & Customs Clearance Daily Status Tracking & Escalation](#w728-port--customs-clearance-daily-status-tracking--escalation)
- [W729. Supply Chain Disruption Rapid Response & Escalation Protocol](#w729-supply-chain-disruption-rapid-response--escalation-protocol)

---

## W31. Demand Forecasting Cycle

| Field | Detail |
|---|---|
| **Trigger** | Weekly forecast recalculation schedule (Sunday batch) |
| **Frequency** | Weekly recalculation; monthly review; quarterly adjustment |
| **Volume** | 35,000 active SKUs across 204 locations (200 stores + 4 DCs) = up to 7.2M SKU-location forecasts; typically forecasted at DC level (140,000 SKU-DC combinations) and disaggregated to stores |
| **Owner** | Demand Planner |
| **Participants** | Demand Planner, Supply Planner, Category Manager, Pricing Analyst |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System runs automated forecast engine: statistical algorithms (exponential smoothing, seasonal decomposition) applied to 2+ years of historical sales data per SKU per DC | System | — | Automated (Sunday batch, 1–3 hours) |
| 2 | System adjusts raw statistical forecast for known events: promotional calendar (W13), seasonal calendar, new store openings (W16), planned store closures, one-time events (typhoons, pandemic) | System | — | Automated |
| 3 | Demand Planner reviews forecast exception report: SKUs with forecast error > 30%, SKUs with insufficient history, new SKUs with no history, SKUs with sudden demand spikes or drops | Demand Planner | Supply Planning Manager | 2–3 hours/week |
| 4 | Demand Planner adjusts flagged forecasts manually: overrides algorithm, inputs qualitative intelligence (vendor intel, market trends, competitive activity) | Demand Planner | Supply Planning Manager | 1–2 hours/week |
| 5 | Demand Planner reviews forecast accuracy metrics (MAPE, bias) by category; identifies systematic over/under-forecasting patterns | Demand Planner | Supply Planning Manager | 1 hour/week |
| 6 | Adjusted forecast released to replenishment engine (W4.1, W2A.1); system uses forecast instead of simple min/max for forecasted SKUs | System | — | Automated |
| 7 | Monthly: Demand Planner presents forecast vs. actual report to Category Managers; discusses upcoming demand shifts | Demand Planner | VP Merchandising | 1 hour/category/month |
| 8 | Quarterly: Demand Planner recalibrates forecast model parameters (alpha, beta, gamma for exponential smoothing); updates seasonal indices based on latest year of data; reviews and updates safety stock parameters per SKU-location based on forecast error and demand variability changes (feeds into W2A.1 ROP/safety stock calculation); reviews ROP parameter governance: (a) lead time accuracy per vendor — compares actual delivery lead time vs. system lead time and updates for vendors with > 20% variance, flagging chronic late vendors for W44 review; (b) demand averaging period appropriateness by SKU volatility class; (c) service level targets by ABC class (e.g., A-items: 98%, B-items: 95%, C-items: 90% or as configured); (d) order multiple / MOQ accuracy per vendor-SKU; cross-references vendor lead time variance to vendor scorecard (W44) | Demand Planner | Supply Planning Manager | 4–6 hours/quarter |

**Total Demand Planner effort**: ~8–12 hours/week + 4–6 hours/quarter for model recalibration

### System Touchpoints
- Statistical forecast engine with multiple algorithms (W31.1)
- Automated event adjustment from promotional and seasonal calendars (W31.2)
- Forecast exception reporting with error thresholds (W31.3)
- Manual forecast override with audit trail (W31.4)
- Forecast accuracy dashboards (MAPE, bias, weighted MAPE) (W31.5)
- Forecast release to replenishment/MRP engine (W31.6)
- Forecast vs. actual variance reporting by category (W31.7)
- Model parameter maintenance and seasonal index recalculation (W31.8)
- Safety stock parameter review and update linked to ROP calculation in W2A (W31.8)
- Multi-echelon DC replenishment sourcing: when a DC's inventory for a SKU drops below ROP, system evaluates available stock at other DCs, inter-DC transfer cost and lead time, vs. vendor PO cost and lead time; recommends optimal source; if transfer recommended, auto-generates Transfer Order per W22; if PO recommended, auto-generates suggested PO per W2A; Supply Planner reviews sourcing recommendations as part of daily replenishment review (W31.6, W4.2)
- ROP parameter governance and accuracy reporting: quarterly parameter review as part of W31.8 covering (a) lead time variance report per vendor (actual vs. system lead time); (b) service level target monitoring by ABC class; (c) demand averaging period appropriateness by volatility class; (d) order multiple / MOQ accuracy; (e) ROP exception report: SKUs where ROP parameters have not been reviewed in > 6 months; parameter accuracy feeds into vendor scorecard (W44) for lead time performance tracking
- DC multi-dimensional capacity planning dashboard: system aggregates all competing demands on DC resources into a single view per DC — (a) **inbound receiving capacity**: scheduled receipts (W3C) vs. dock door availability vs. receiving crew capacity (labor hours); (b) **outbound pick/pack capacity**: store replenishment orders (W4) + home delivery orders (W19) + promotional pre-positioning (W57) + backorder fulfillment (W56) — total pick lines and labor hours required vs. available pick/pack crew; (c) **outbound dock capacity**: scheduled dispatches vs. dock door availability vs. loading crew capacity; (d) **storage capacity**: current bin utilization vs. incoming inventory from POs and transfers; dashboard shows 3-day forward view with capacity utilization percentage per dimension; Supply Planner and DC Supervisor review daily during morning planning meeting; if any dimension exceeds 90% utilization, system highlights in amber; if exceeds 100%, system highlights in red and suggests mitigation (defer non-critical replenishment waves, redirect home delivery to alternate DC, schedule overtime, or engage agency workers per W10); during peak periods (Christmas season, bi-monthly sale events), Supply Planning Manager reviews capacity dashboard weekly with DC Manager and VP Supply Chain to proactively adjust labor scheduling (W34) and carrier capacity (W52/W62B) (W31)

### Pain Points / Risks
- **New SKU cold-start problem**: New items with no sales history generate unreliable forecasts; Demand Planner must rely on analogous item mapping and judgment, leading to higher forecast error and potential overstock or stockout in the first 90 days
- **Promotional lift uncertainty**: Promotions (W13) create demand spikes that are difficult to model accurately, especially for first-time promotional events; over-forecasting leads to markdowns while under-forecasting causes lost sales and customer dissatisfaction
- **Multi-echelon complexity**: Forecasting at DC level and disaggregating to 200 stores compounds error; store-level forecasts for low-volume SKUs have very high MAPE, making automatic replenishment unreliable for slow movers
- **Vendor lead time volatility**: Philippine port congestion, customs delays (W144), and international shipping disruptions cause actual lead times to diverge significantly from system parameters, degrading safety stock calculations and ROP accuracy

---

### Time Estimate
**Weekly cycle**: ~8–12 hours/week for Demand Planner (data review, model adjustment, exception handling, consensus meeting preparation). **Quarterly recalibration**: Additional 4–6 hours/quarter for statistical model retraining and parameter optimization. **S&OP cycle (W133)**: Additional ~4 hours/month for demand presentation preparation.

### Staffing Implication
- **1–2 Demand Planners** (within the 30-person Supply Chain team): This is a specialized analytical role. With 35,000 SKUs across 4 DCs, weekly review of forecast exceptions + monthly category reviews + quarterly recalibration requires a dedicated person. A 2nd demand planner provides coverage and can focus on new-item forecasting (no history) and promotional lift modeling.
- **Category Managers**: 1 hour/month each for forecast review meetings = ~10 hours/month total. Absorbed into existing duties.

## W32. Seasonal Buy Planning

| Field | Detail |
|---|---|
| **Trigger** | Seasonal calendar milestones (6 months before each season peak) |
| **Frequency** | 4 major seasonal planning cycles/year: Christmas (plan in Jun), Summer/March (plan in Oct), Back-to-School (plan in Nov), Rainy Season/ typhoon prep (plan in Jan) |
| **Volume** | ~3,000–5,000 seasonal SKUs per major event; ~20–30 import POs per season |
| **Owner** | Category Manager |
| **Participants** | Category Manager, Buyer, Demand Planner, Import Coordinator, VP Merchandising, Finance (budget) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Demand Planner generates seasonal forecast: prior-year sales by SKU for the season period, adjusted for current trend and planned promotions | Demand Planner | Category Manager | 4 hours/season |
| 2 | Category Manager reviews seasonal forecast; identifies SKUs to carry forward, new items to add, items to drop | Category Manager | VP Merchandising | 2 hours/season |
| 3 | Buyer solicits vendor quotations for seasonal items; negotiates volume discounts, early-order incentives, and return/excess-stock terms | Buyer | Category Manager | 1 week/season |
| 4 | Category Manager creates seasonal buy plan: SKU-level quantities, vendor allocation, delivery schedule (phased receipts vs. single drop) | Category Manager | VP Merchandising | 4 hours/season |
| 5 | Finance validates seasonal buy plan against working capital budget and inventory plan (max inventory days target) | Controller | CFO | 2 hours/season |
| 6 | VP Merchandising approves seasonal buy plan | VP Merchandising | VP Merchandising | 1 hour/season |
| 7 | Buyer creates import POs (W2B) or domestic POs (W2A) per the seasonal buy plan; times orders to arrive 6–8 weeks before season start | Buyer | Category Manager | Per W2 |
| 8 | System tracks seasonal PO commitments vs. seasonal buy plan budget; alerts if over-committed | System | — | Automated |
| 9 | As season approaches: Pricing Analyst sets up seasonal pricing and promotions (W13) | Pricing Analyst | Category Manager | Per W13 |
| 10 | Mid-season: Category Manager and Buyer review sell-through vs. plan; trigger re-orders for hot items or accelerate markdowns for slow movers | Category Manager | VP Merchandising | 1 hour/week during season |
| 11 | Post-season: Buyer and Category Manager conduct post-mortem: actual vs. plan sales, margin, leftover inventory disposition (clearance, return to vendor, carry forward to next year) | Buyer + Category Manager | VP Merchandising | 2 hours/season |

**Total cycle time**: 6 months from planning start to season peak

### System Touchpoints
- Seasonal forecast generation from historical data with event adjustment (W32.1)
- Seasonal buy plan entry with SKU, quantity, vendor, delivery phasing (W32.4)
- Budget/working capital check against seasonal plan (W32.5)
- PO commitment tracking against seasonal buy plan budget (W32.8)
- Seasonal sell-through dashboard: actual vs. plan by SKU (W32.10)
- Post-season analysis and leftover inventory disposition tracking (W32.11)
- Integration with W1 (assortment review), W2 (PO creation), W13 (promotions)

### Pain Points / Risks
- **Seasonal overstock risk**: Christmas and summer seasonal SKUs that miss sales targets become dead inventory requiring aggressive markdowns (W13.9a) or vendor return negotiation; leftover seasonal inventory ties up working capital for up to 12 months until the next season
- **Long import lead times**: Seasonal items sourced from China and Vietnam require 8–12 week lead times; demand assumptions made 6 months before season may no longer be valid when goods arrive, especially in a volatile Philippine construction market
- **Working capital constraint**: 4 seasonal buying cycles per year compete for limited working capital against ongoing replenishment purchasing; Finance may force seasonal buy plan cuts, leaving high-demand seasonal items under-stocked
- **Cross-seasonal cannibalization**: Poor coordination between seasonal and core assortment planning may result in seasonal SKUs cannibalizing sales of year-round items, reducing overall margin

---

### Time Estimate
**Total cycle time**: 6 months from planning start to season peak. Phase 1 (data gathering & analysis): ~2 weeks. Phase 2 (buy planning & vendor negotiation): ~4 weeks. Phase 3 (PO placement & logistics): ~2 weeks. Ongoing in-season monitoring: ~2–4 hours/week per active season. A Demand Planner and Buyer jointly manage 2–3 overlapping seasons at any time.

### Staffing Implication
- **Category Managers**: Seasonal planning is an extension of their existing W1 duties. Each seasonal cycle adds ~8–10 hours of work per category, spread over several weeks. With 5 Category Managers and 4 seasonal cycles, each handles ~1 major seasonal plan at a time. Absorbed within existing ~40-person Merchandising team.
- **Buyers**: Import PO creation follows standard W2B. Seasonal volume adds ~20–30 import POs per season, concentrated in a few weeks. Manageable within existing team.
- **Demand Planner**: Adds ~4 hours per seasonal cycle for forecast generation. With 4 cycles/year = 16 hours/year. Minimal impact.

## W133. Sales & Operations Planning (S&OP) Cycle

| Field | Detail |
|---|---|
| **Trigger** | Monthly planning calendar (typically starting 10th business day) |
| **Frequency** | Monthly |
| **Volume** | Covers all product categories and all 4 DCs |
| **Owner** | VP for Supply Chain |
| **Participants** | CEO, COO, CFO, VP Merchandising, VP Store Ops, Supply Planning Manager, Demand Planner, Category Managers |

### Background

S&OP is the cross-functional process that aligns demand, supply, and financial plans into a single "consensus plan." It ensures that BuildRight has enough inventory to meet sales targets without exceeding working capital limits or DC capacity.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Demand Review**: Demand Planner and Category Managers review the unconstrained forecast (W31); adjust for planned promos (W83) and new store openings (W16); sign off on "Consensus Demand Plan" | Demand Planner | VP Merch | 2 days |
| 2 | **Supply Review**: Supply Planner and DC Managers evaluate ability to meet demand; check vendor lead times (W44), DC storage/labor capacity, and port congestion (W144); identify supply gaps | Supply Planner | VP Supply Chain | 2 days |
| 3 | **Financial Integration**: Finance translates the volume plan into PHP; compares against budget (W26) and revenue targets; highlights margin risks if high-cost logistics (W66) are needed | Controller | CFO | 1 day |
| 4 | **Pre-S&OP Meeting**: Managers reconcile demand/supply gaps; develop scenarios (e.g., "Air-freight vs. Out-of-stock") for leadership | Supply Planning Mgr | VP Supply Chain | 4 hours |
| 5 | **Executive S&OP Meeting**: C-Suite reviews scenarios; makes trade-off decisions; approves the "Consensus Operating Plan" for the next 3–12 months | CEO | CEO | 2 hours |
| 6 | **Disaggregation**: Approved plan is pushed back to replenishment systems (W4) and Buy Plans (W32) to drive execution | Supply Planner | — | 4 hours |

### System Touchpoints
- S&OP Workbench aggregating Forecast (Demand), Open POs/Inventory (Supply), and Budget (Finance)
- Scenario modeling / "What-if" analysis tools
- Executive dashboard showing Demand/Supply balance and projected stock-outs
- Integration with W31 (Forecasting), W32 (Seasonal Buying), and W26 (Budgeting)

### Time Estimate
- Demand Review: 2 days
- Supply Review: 2 days
- Financial Integration: 1 day
- Pre-S&OP Meeting: 4 hours
- Executive S&OP Meeting: 2 hours
- Disaggregation and plan push: 4 hours
- **Total cycle time**: ~5–6 business days per monthly cycle

### Pain Points / Risks
- **Cross-functional alignment difficulty**: Getting CEO, COO, CFO, VP Merchandising, and VP Store Ops in the same room monthly is challenging; executive S&OP meetings are frequently rescheduled or attended by proxies, undermining decision quality
- **Demand-supply gap scenarios**: When demand significantly exceeds supply capacity (peak Christmas season, simultaneous promotional events), the Pre-S&OP meeting must present difficult trade-offs (air freight cost vs. stockout risk) that require real-time financial modeling
- **Data latency and quality**: Forecast data (W31), open PO positions, and DC capacity figures must be current as of the same snapshot date; data from different system modules with different refresh cycles creates reconciliation overhead
- **Consensus plan commitment drift**: Even after the Consensus Operating Plan is approved, Category Managers and Buyers may deviate through ad-hoc PO creation (W2A/W2B) without S&OP visibility; need system controls to flag plan-vs.-actual purchase commitment variance

---

### Staffing Implication
Monthly S&OP cycle requires ~5–6 business days of cross-functional time. VP Supply Chain chairs the process (~4 hours/month). Demand Planner: ~2 days. Supply Planner: ~2 days. Controller: ~1 day. CEO and C-Suite: 2 hours for Executive S&OP Meeting. All absorbed by existing roles; no incremental headcount.

## W144. International Logistics & Import Operations

| Field | Detail |
|---|---|
| **Trigger** | Import Purchase Order (W2B) approved and sent to overseas vendor |
| **Frequency** | Weekly; ~20–30 containers/month |
| **Volume** | Primary sourcing from China, Vietnam, Thailand, and Europe |
| **Owner** | Import Coordinator |
| **Participants** | Buyer, Import Coordinator, Freight Forwarder, Customs Broker, Finance, DC Receiving |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Proforma Invoice (PI) Review**: Receive PI from vendor; verify against PO (W2B); check payment terms (L/C, T/T, CAD) | Buyer | Category Manager | 1 hour |
| 2 | **L/C Opening (if applicable)**: Finance coordinates with Bank to open Letter of Credit; sends L/C to vendor bank | Finance (Treasury) | CFO | 2–3 days |
| 3 | **Production & Booking**: Vendor confirms production completion; Import Coordinator coordinates with Freight Forwarder for vessel booking (FCL/LCL) | Import Coordinator | — | 2–5 days |
| 4 | **Shipping Documents**: Receive set of documents: Bill of Lading (B/L), Commercial Invoice, Packing List, Certificate of Origin (for FTA benefits like ATIGA/ACFTA) | Import Coordinator | — | 1 day |
| 5 | **In-Transit Tracking**: Update system with vessel name, container ID, and ETA; monitor "Estimated vs. Actual" arrival dates | Import Coordinator | — | Ongoing |
| 6 | **Customs Entry**: Customs Broker files entry via BOC E2M system; calculates Duties & Taxes (VAT + Import Duty) | Customs Broker | Import Coordinator | 1–2 days |
| 7 | **Payment of Duties**: Finance processes payment of duties/taxes to BOC via bank portal; system records as "Inventory in Transit" cost component | Finance | Controller | 4 hours |
| 8 | **Release & Haulage**: BOC releases cargo; Forwarder coordinates haulage from Port to DC; monitor "Port Out" to avoid demurrage/detention fees | Import Coordinator | DC Manager | 1–3 days |
| 9 | **DC Arrival & Stripping**: DC receives container; verifies seal integrity; strips container and performs "Blind Count" against Packing List | DC Receiving | DC Manager | 4 hours |
| 10 | **Cost Finalization**: System aggregates all landed costs (Product + Freight + Duties + Brokerage + Wharfage) to calculate final Landed WAC | System / Finance | Cost Accountant | Automated |

### System Touchpoints
- Import Shipment Tracker (Container level)
- Landed Cost Module (aggregating multiple invoices to a single PO line)
- Integration with BOC E2M (if via API) or manual entry of entry numbers
- Demurrage/Detention alert system based on "Last Free Day"

### Time Estimate
- Proforma Invoice review: 1 hour/shipment
- L/C opening (if applicable): 2–3 days (Finance/Treasury + bank processing)
- Production confirmation and vessel booking: 2–5 days
- Shipping document collection: 1 day
- In-transit tracking: Ongoing (~15 min/day/active shipment)
- Customs entry filing: 1–2 days
- Duty payment processing: 4 hours
- Cargo release and haulage: 1–3 days
- DC container stripping and blind count: 4 hours/container
- Landed cost finalization: Automated
- **Total cycle time (order to DC receipt)**: 4–8 weeks depending on origin and shipping mode

### Pain Points / Risks
- **Philippine port congestion**: Manila International Container Terminal (MICT) and South Harbor experience chronic congestion, especially during pre-Christmas peak (August–October); container dwell times can double, triggering demurrage charges (W249) and delaying DC replenishment
- **Customs clearance unpredictability**: BOC E2M system processing times vary widely; non-compliant documentation (incorrect HS code, missing Certificate of Origin) can add 3–7 days of clearance delay per shipment
- **Foreign exchange exposure**: Import POs are denominated in USD or CNY while revenue is in PHP; the 4–8 week shipment cycle exposes BuildRight to significant FX variance between PO creation and actual payment
- **Container damage and pilferage risk**: Long transit times and multiple handling points (origin port, transshipment, destination port, haulage) increase the risk of cargo damage; inadequate container seal verification at DC receiving can mask pilferage

---

### Staffing Implication
1 Import Coordinator full-time managing 20–30 containers/month (~40–60 hours/week). Finance (Treasury): ~2–3 days/month for L/C opening and duty payments across active shipments. Customs Broker: external partner, budgeted as logistics cost. DC Receiving: ~4 hours/container for stripping and blind count, absorbed by existing DC receiving crew. No incremental headcount.

## W183. Supply Chain Network Optimization Review

| Field | Detail |
|---|---|
| **Trigger** | Annual strategic review; or significant change in logistics costs/fuel prices |
| **Frequency** | Annual full review; ad-hoc triggered by fuel price spikes > 15%, new store cluster openings, or DC lease renewal decisions |
| **Volume** | Covers all 200 stores, 4 DCs, and ~200 delivery routes across Luzon, Visayas, and Mindanao |
| **Owner** | COO |
| **Time Estimate** | Data extraction: 1 day; Network modeling: 1 week; Cost analysis: 3 days; Recommendation and presentation: 2 hours; **Total**: ~2 weeks annual effort |
| **Participants** | Supply Chain Director, Logistics Manager, Finance Analyst, External Logistics Consultant |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Extraction**: Pull historical store sales, DC throughput, and transport costs by route | Finance Analyst | — | 1 day |
| 2 | **Modeling**: Use "Center of Gravity" and "Network Optimization" tools to simulate optimal DC locations vs. 200-store footprint | SC Director | — | 1 week |
| 3 | **Cost Analysis**: Compare current "4-DC" cost vs. potential "6-DC" or "Consolidated DC" scenarios; include lease exit costs (W117) | Logistics Mgr | CFO | 3 days |
| 4 | **Recommendation**: Present optimal network configuration (e.g., "Open DC6 in North Luzon") to Board | COO | CEO | 2 hours |
| 5 | **Implementation Plan**: If approved, trigger W116 (Site Selection) for the new DC | Supply Chain Mgr | — | — |

### System Touchpoints
- Big Data extraction from ERP (Sales + Inventory + Transport costs)
- Simulation/Integration with Logistics Optimization software
- Strategic decision support dashboards

### Pain Points / Risks
- **Data quality for modeling**: Store-level sales data, actual transport costs per route, and DC throughput data must be accurate and complete; Philippine logistics cost data (fuel, toll, driver wages) is volatile and modeling with stale data produces unreliable recommendations
- **DC lease commitment rigidity**: Existing DC leases (typically 3–5 year terms) with early exit penalties (W117) limit the financial viability of recommended network changes; an optimal 6-DC configuration may not be achievable until current leases expire
- **Inter-island logistics complexity**: Modeling optimal DC locations for an archipelagic network (Luzon, Visayas, Mindanao) requires incorporating RoRo ferry schedules, port fees, and inter-island shipping costs that change frequently and are difficult to forecast
- **Executive resistance to change**: Closing or relocating a DC disrupts existing vendor delivery patterns, employee commutes, and store replenishment cycles; the operational risk of network changes may cause leadership to defer action even when the business case is clear

### Time Estimate
- Data extraction from ERP (step 1): 1 day (Finance Analyst pulls historical store sales, DC throughput, and transport costs by route for the full network)
- Network modeling and simulation (step 2): 1 week (Supply Chain Director and External Logistics Consultant run Center of Gravity and network optimization scenarios across 200 stores and 4 DCs; includes modeling 6-DC, 4-DC, and consolidated DC configurations)
- Cost analysis and comparison (step 3): 3 days (Logistics Manager compares current 4-DC cost baseline against alternative scenarios including lease exit costs per W117, transport cost projections, and service level impact)
- Board recommendation and presentation (step 4): 2 hours (COO presents findings and recommendation to Board)
- Implementation plan development (step 5): varies; if new DC approved, triggers W116 site selection process
- **Total annual review effort**: ~2 weeks concentrated effort (1 day data extraction + 1 week modeling + 3 days cost analysis + 2 hours presentation); primarily Supply Chain Director and External Logistics Consultant with Finance Analyst and Logistics Manager support

---

### Staffing Implication
Annual review requiring ~2 weeks of effort. Supply Chain Director leads (~1 week). Finance Analyst: ~1 day for data extraction. External Logistics Consultant: ~1 week for modeling (project-based fee). Logistics Manager: ~3 days for cost analysis. All absorbed by existing roles plus external consultant engagement. No incremental headcount.

## W191. Global Supply Chain — Incoterm & Marine Insurance Tracking

| Field | Detail |
|---|---|
| **Trigger** | Import PO creation (W2B) or Shipment Booking (W144) |
| **Frequency** | Ongoing per import shipment |
| **Volume** | ~400–600 TEUs/month |
| **Owner** | Import Coordinator |
| **Participants** | Buyer, Insurance Provider, Finance, Freight Forwarder |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Incoterm Selection**: Buyer selects Incoterm (EXW, FOB, CFR, CIF) during PO negotiation (W2B); system calculates risk transfer point | Buyer | — | 15 min |
| 2 | **Insurance Booking**: If Incoterm requires BuildRight to provide insurance (EXW, FOB, CFR), Import Coordinator issues "Marine Insurance Declaration" | Import Coordinator | — | 30 min |
| 3 | **Risk Monitoring**: System tracks shipment location vs. risk transfer point (e.g., "On Board" for FOB); alerts if insurance coverage gap exists | System | — | Automated |
| 4 | **Claim Initiation**: If damage/loss occurs during transit (W3.6a), Import Coordinator gathers B/L, Survey Report, and Invoice | Import Coordinator | — | 2 hours |
| 5 | **Claim Filing**: Submit claim to Marine Insurance provider; track status in ERP | Import Coordinator | Finance Mgr | 1 hour |
| 6 | **Settlement**: Finance records insurance recovery; offsets against inventory loss (W3.6a) | Finance | — | 30 min |

### System Touchpoints
- Incoterm Master Data in Vendor/PO (W191.1)
- Marine Insurance Declaration Portal (W191.2)
- Risk Transfer Point Monitoring (W191.3)
- Insurance Claim Tracking Module (W191.5)

### Time Estimate
- Incoterm selection and risk transfer setup: 15 min/PO
- Insurance booking (marine declaration): 30 min/shipment
- Risk monitoring: Automated
- Claim initiation (damage/loss): 2 hours/claim
- Claim filing with provider: 1 hour/claim
- Settlement recording: 30 min/claim
- **Total per shipment**: ~45 min routine processing; ~4 hours if claim required

### Pain Points / Risks
- **Insurance coverage gaps on FOB/EXW shipments**: If Import Coordinator fails to issue the Marine Insurance Declaration promptly after booking, cargo may transit without coverage; a total loss during the gap period is uninsured and directly hits the P&L
- **Claim documentation complexity**: Marine insurance claims require synchronized documentation (Bill of Lading, Survey Report, Commercial Invoice, Packing List) within strict time windows; Philippine port conditions (humidity, handling) make damage claims common but documentation is often incomplete
- **Incoterm misunderstanding**: Buyers negotiating EXW terms may not account for the full cost of arranging origin pickup, export clearance, and inland transport; actual landed costs can significantly exceed the quoted FOB equivalent
- **Insurance recovery timeline**: Marine insurance claim settlement can take 3–6 months, tying up working capital in the SSS Receivable-equivalent insurance receivable ledger and complicating period-end inventory valuation

---

### Staffing Implication
~400–600 TEUs/month × 45 min routine processing = ~300–450 hours/month. Insurance claims: ad-hoc, ~4 hours each. Import Coordinator manages this as part of W144 import operations (~30 min/shipment for insurance booking). Finance Manager reviews claims. Absorbed by existing Import Coordinator and Finance roles. No incremental headcount.

## W249. Import Port Demurrage & Detention Management

| Field | Detail |
|---|---|
| **Trigger** | Import container vessel arrival at Philippine port (Manila/Cebu/Davao) (W144) |
| **Frequency** | Ongoing per import shipment (~20–30 shipments/month) |
| **Volume** | Covers ~400–600 TEUs/month |
| **Owner** | Logistics Manager |
| **Participants** | Import Coordinator, Customs Broker, Finance Specialist, Shipping Line |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Vessel Arrival**: System pulls actual arrival time from Port Authority API; calculates free-time expiration date (standard: 5 days demurrage, 3 days detention). | System | — | Automated |
| 2 | **Clearance Tracking**: Import Coordinator monitors customs brokerage clearance progress (W239). If delayed (> 3 days), triggers warning. | Import Coordinator | Logistics Mgr | 10 min |
| 3 | **Demurrage Alert**: System auto-calculates potential demurrage fees if containers are not gate-outed before free-time expiry; alerts Logistics Manager to prioritize pickup. | System | — | Automated |
| 4 | **Gate-Out & Return**: Containers are hauled to DC (W3). Hauler returns empty container to designated port yard within shipping line's free-time window. | Hauler / DC Clerk | Logistics Mgr | 1–2 days |
| 5 | **Charges Auditing**: If demurrage/detention occurs: Shipping line issues invoice; Finance Specialist audits charges against system-captured arrival/gate-out/gate-in logs. | Finance Specialist | Controller | 1 hour |
| 6 | **Dispute / Payment**: If charges valid, approve payment to avoid port hold; if invalid, initiate dispute via shipping line portal with log evidence. | Finance Specialist | Logistics Mgr | 2 hours |

### System Touchpoints
- Port Authority vessel tracking API integration
- Automated demurrage/detention free-time calculations and system alerting
- Hauler empty container gate-in/gate-out logs tracking
- Landed cost integration for port penalty allocations (W2B/W13)

### Time Estimate
- Vessel arrival tracking and free-time calculation: Automated
- Clearance progress monitoring: 10 min/shipment/day during clearance window
- Demurrage alert review: Automated
- Gate-out and container return coordination: 1–2 days
- Demurrage/detention charge auditing: 1 hour/charge
- Dispute or payment processing: 2 hours/charge
- **Total**: ~15 min/shipment routine monitoring; ~3 hours per demurrage/detention incident

### Pain Points / Risks
- **Demurrage cost escalation**: Philippine port free time is typically only 5 days; customs clearance delays of even 1–2 days (common during BOC system outages or document queries) can trigger PHP 5,000–15,000/day demurrage charges per container, adding 2–5% to landed cost
- **Shipping line detention fee opacity**: Container detention fees (charged by shipping lines for late empty return) are calculated on different schedules than port demurrage; the dual-clock system is confusing and shipping line invoices are difficult to audit without precise gate-in/gate-out timestamps
- **Weekend and holiday compounding**: Philippine holidays (average 18 national holidays/year plus local LGU holidays) reduce effective working days for clearance and haulage; containers arriving mid-week before a long weekend are especially vulnerable to demurrage
- **Dispute resolution leverage**: BuildRight has limited negotiating power against major shipping lines (Maersk, CMA CGM, COSCO) when disputing demurrage charges; disputes are time-consuming and shipping lines may hold subsequent container releases pending payment

---

### Staffing Implication
~20–30 shipments/month with routine monitoring absorbed by Import Coordinator as part of W144. Demurrage/detention incidents: ~5–10/month × 3 hours = ~15–30 hours/month from Finance Specialist for auditing and disputes. Logistics Manager provides oversight. Absorbed by existing Import Coordinator and Finance roles. No incremental headcount.

## W250. Supply Chain Control Tower & Real-Time Shipment Visibility

| Field | Detail |
|---|---|
| **Trigger** | Shipment of import PO (W144 / W2B) or inter-island freight dispatch (W66) |
| **Frequency** | Ongoing per shipment |
| **Volume** | ~20–30 import containers and ~40–50 inter-island shipments/month |
| **Owner** | Supply Chain Director |
| **Participants** | Logistics Manager, Import Coordinator, Store Operations Rep, 3PL Partners |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Shipment Dispatch**: 3PL partner dispatches shipment and transmits Container ID / GPS tracker link via API/EDI to BuildRight. | 3PL Partner | — | Automated |
| 2 | **Milestones Tracking**: Control Tower system aggregates tracking data (vessel GPS, port gate-out/gate-in, inland truck GPS) to trace shipment in transit. | System | — | Automated |
| 3 | **Dynamic ETA Update**: System dynamically recalculates estimated time of arrival (ETA) based on weather, port speed, and transit history. | System | — | Automated |
| 4 | **Geofence Alerts**: System detects container entering port/DC zone; auto-alerts DC gate crew (W3) and Import Coordinator to prepare receiving. | System | — | Automated |
| 5 | **Exception Trigger**: If a shipment is delayed > 24 hours from original ETA, system triggers alert. Import Coordinator investigates bottleneck. | Import Coordinator | Logistics Mgr | 1 hour |
| 6 | **Re-routing / Mitigation**: If critical delay threatens store stockout, Supply Chain Director authorizes inventory reallocation (W105) or alternative local sourcing (W60). | Supply Chain Director | VP Supply Chain | 2 hours |
| 7 | **Carrier Review**: Monthly, Logistics Manager reviews carrier lead-time performance and delay metrics in S&OP dashboard (W133). | Logistics Manager | Supply Chain Director | 2 hours |

### System Touchpoints
- Control Tower Dashboard with GIS integration
- Carrier EDI/API tracking integrations
- Dynamic ETA recalculation engine
- Automated SMS/Email delay exception notifications

### Time Estimate
- Shipment dispatch integration: Automated
- Milestone tracking and ETA recalculation: Automated
- Geofence alert processing: Automated
- Delay investigation (per exception): 1 hour
- Re-routing/mitigation decision: 2 hours (only when critical delays threaten stockout)
- Monthly carrier performance review: 2 hours/month
- **Total**: Largely automated; ~3 hours/week for exception management across 60–80 active shipments

### Pain Points / Risks
- **Carrier API reliability**: Not all 3PL partners and shipping lines provide reliable real-time API/EDI feeds; smaller inter-island carriers may only offer manual phone/SMS updates, creating visibility gaps for ~20–30% of shipments
- **Alert fatigue**: With 60–80 active shipments, minor delays generate frequent alerts; operations teams may start ignoring non-critical exceptions, potentially missing a genuine stockout-threatening delay
- **GPS coverage gaps in provincial routes**: Cellular/GPS coverage is unreliable in remote Philippine provincial areas (mountainous terrain in Cordillera, rural Mindanao), causing tracking blackouts during the last-mile portion of inter-island delivery
- **Reactive vs. proactive limitation**: Control Tower is primarily reactive (alerting after delay occurs); true proactive supply chain management would require predictive analytics based on port congestion patterns, weather forecasts, and carrier historical performance

---

### Staffing Implication
Largely automated tracking. Import Coordinator spends ~3 hours/week on exception investigation. Supply Chain Director: ~2 hours/month for re-routing/mitigation decisions. Logistics Manager: 2 hours/month for carrier performance review. All absorbed by existing roles. No incremental headcount.

## W268. Last-Mile Home Delivery Tracking & Proof-of-Delivery

| Field | Detail |
|---|---|
| **Trigger** | Order dispatched from DC or Store for home delivery (W19 / W19B) |
| **Frequency** | Ongoing per delivery transaction (~573 delivery orders/day) |
| **Volume** | Covers ~17,200 deliveries/month |
| **Owner** | Last-Mile Operations Supervisor |
| **Participants** | WMS, Dispatch Crew, Driver (Fleet/3PL), Customer Service Representative, Customer |
| **Time Estimate** | Dispatch: 5 min; In-transit updates: Automated; Delivery & POD: 10 min |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Driver Loading & Scan**: Dispatch crew loads delivery vehicle; driver scans order barcodes using the last-mile mobile app, changing order status in ERP to "Out for Delivery". | Driver / Dispatch Crew | Last-Mile Supervisor | 5 min |
| 2 | **Customer Dispatch Alert**: System automatically triggers SMS/email notifications to customer with an updated ETA, contact details for the driver, and a link to the real-time tracking map. | System | — | Automated |
| 3 | **Real-Time GPS Tracking**: Driver's mobile app streams GPS location to the ERP Supply Chain Control Tower (W250); system dynamically recalculates ETA based on traffic conditions. | Driver / System | Last-Mile Supervisor | Automated |
| 4 | **Proximity Alert**: When the delivery vehicle enters a 2 km geofenced radius of the destination, the system sends an automated proximity SMS alert to the customer. | System | — | Automated |
| 5 | **Delivery & Site Inspection**: Driver arrives at address; unloads goods (cement, tiles, fixtures); customer inspects items to verify correct SKUs and quantity. | Driver / Customer | Last-Mile Supervisor | 5–15 min |
| 6 | **POD Capture**: Driver captures digital Proof of Delivery (POD) via mobile app: (a) customer's electronic signature, (b) photo of items staged at the site, (c) GPS coordinate stamp confirming vehicle was at delivery location. | Driver | Last-Mile Supervisor | 3 min |
| 7 | **Delivery Completion**: Mobile app uploads POD data; ERP changes order status to "Delivered", posts inventory reduction, generates official sales invoice to customer, and sends CSAT rating request (W65). | System | — | Automated |

### System Touchpoints
- Last-Mile Driver Mobile App (barcode scanning, signature & photo capture, offline sync capability)
- Real-time customer tracking web portal (GIS integrated route map & ETA update)
- ERP Control Tower tracking dashboard integration
- Integration with W19 (Home Delivery), W19B (Ship from Store), and W250 (Control Tower)

### Success Metrics / KPIs
- On-Time In-Full (OTIF) Delivery rate: > 95%
- Failed delivery rate: < 2.0%
- Delivery ETA notification accuracy: ±15 minutes
- Proof of Delivery (POD) capture compliance (photo + signature): 100%

### Time Estimate
- Driver loading and barcode scan confirmation (step 1): 5 min per delivery stop; ~573 delivery orders/day across all DCs, batch-loaded per route with ~10–15 orders per vehicle = ~5 min/stop
- Customer dispatch alert and ETA notification (step 2): automated (instant)
- Real-time GPS tracking and ETA recalculation (step 3): automated (continuous; no manual effort)
- Proximity alert to customer via SMS (step 4): automated (instant)
- Delivery, site inspection, and customer verification (step 5): 5–15 min depending on item count and size (bulky items like cement bags, tiles, and lumber require longer unloading and staging time)
- Digital POD capture — signature, photo, and GPS stamp (step 6): 3 min per delivery
- Delivery completion, inventory posting, invoice generation, and CSAT request (step 7): automated (instant)
- **Per delivery (staff time)**: ~15–25 min total (5 min loading/scan + 5–15 min delivery/inspection + 3 min POD capture + automated steps)
- **Daily delivery volume**: ~573 deliveries/day across all DCs; ~17,200 deliveries/month requiring ~170–240 driver-hours/day
- **Exception handling**: failed deliveries (~2% rate = ~11/day) add 15–30 min each for return-to-DC processing per W19.12

### Pain Points / Risks
- **Connectivity Blackout (Offline Mode)**: In remote areas with no cellular signal, the mobile app caches signature and photo data locally, syncing with the ERP automatically once connection is restored.
- **Delivery Refusal / Damaged Goods**: If customer rejects delivery due to damage, driver marks "Refused - Damaged" in app, takes photo of damage, and returns goods to DC. ERP automatically flags case to CSR for expedited replacement order or refund processing (W19 step 12).
- **POD compliance gaps**: Drivers may forget to capture photos or signatures during high-volume delivery days, creating incomplete POD records that complicate dispute resolution and AR collection for large B2B deliveries.
- **GPS accuracy in dense urban areas**: Multi-story construction sites and dense Metro Manila neighborhoods produce inaccurate GPS stamps, undermining the geofence proximity alert and delivery location verification for disputed deliveries.

### Staffing Implication
~17,200 deliveries/month. Last-Mile Operations Supervisor manages driver fleet and POD compliance (~4–6 hours/day). CSR handles delivery exception escalations (~1–2 hours/day). Driver POD capture: 3 min/delivery, absorbed into delivery routine. No incremental headcount beyond existing Last-Mile Supervisor and driver pool.

---

## W284. Customs Bonded Warehouse (CBW) Operations & Duty Deferral

| Field | Detail |
|---|---|
| **Trigger** | Arrival of imported goods designated for the CBW to defer customs duties until final store allocation. |
| **Frequency** | Weekly |
| **Volume** | 10-20 containers per week |
| **Owner** | Logistics Manager / Import Compliance |
| **Participants** | Customs Broker, Bureau of Customs (BOC), DC Manager, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Import container arrives and is received into a designated logical/physical CBW location in the WMS without paying duties (under customs bond). | Logistics Coordinator | Import Compliance Mgr | 4 hours |
| 2 | System tags the inventory as bonded and unavailable for standard retail sale. | Warehouse Supervisor | Logistics Manager | 1 hour |
| 3 | When store replenishment (W4) demands the stock, a formal withdrawal request is generated. | Supply Planner | Import Compliance Mgr | 30 min |
| 4 | Finance pays the specific duties/taxes for only the withdrawn quantity (W239). | Finance Specialist | Controller | 2 hours |
| 5 | BOC approves, and the WMS releases the stock from the CBW location to the standard picking area. | Import Coordinator | Import Compliance Mgr | 1–2 days |

### System Touchpoints
- WMS (Bonded Locations) — logical segregation of duty-unpaid inventory with CBW zone management
- AP (Duties) — duty payment processing linked to withdrawal quantity
- Logistics Management — container receipt and CBW location assignment
- BOC E2M Integration — electronic lodgment of withdrawal declarations and duty calculations
- Customs Bond Tracking — bond utilization monitoring against total CBW capacity

### Pain Points / Risks
- Massive BOC penalties or license revocation if bonded stock is accidentally shipped without duty payment
- Duty rate changes between import date and withdrawal date can cause landed cost variances not captured at original import
- CBW storage capacity limits — if bonded inventory accumulates beyond CBW physical capacity, overflow must be re-routed to standard duty-paid locations, negating the deferral benefit
- Withdrawal approval delays from BOC can block urgent store replenishment, forcing expedited duty payments that compress the cash flow advantage of the deferral program

### Time Estimate
**Total per withdrawal**: 1–2 days for BOC approval + 4 hours container receipt + 1 hour system tagging + 30 min withdrawal request + 2 hours duty payment. Routine container receipt: ~5 hours. Withdrawal cycle: ~2–3 days elapsed. Weekly management: ~8–12 hours for Import Compliance Mgr across 10–20 containers.

### Staffing Implication
10–20 containers/week × ~5 hours receipt processing = ~50–100 hours/week. Withdrawal requests: ~5–10/week × 30 min each = ~3–5 hours. Duty payments: ~5–10/week × 2 hours = ~10–20 hours. 1 Import Compliance Manager + 1 Logistics Coordinator dedicated. Finance Specialist support for duty payments absorbed by existing AP team.

---

## W464. In-House Customs Brokerage & Port Operations

| Field | Detail |
|---|---|
| **Trigger** | Import container arrives at port (Manila/Davao/Cebu) |
| **Frequency** | ~400–600 TEUs/month |
| **Volume** | High; multiple containers per day |
| **Owner** | Import Coordinator (Licensed Broker) |
| **Participants** | Customs Broker (In-house), Logistics Manager, BOC, Haulier (Trucker) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Entry Lodgment**: Broker submits "Import Entry" via BOC e2m system; calculates duties/taxes (W239) | In-house Broker | — | 4 hours |
| 2 | **Documentary Review**: BOC verifies manifest vs. packing list and commercial invoice | BOC Officer | — | 1-2 days |
| 3 | **Physical Inspection**: If flagged (Red/Yellow lane), Broker attends physical inspection at the port | In-house Broker | Import Coordinator | 1 day |
| 4 | **Gate Pass & Release**: Upon payment of duties (W239), BOC issues "Release Instruction" and Port Gate Pass | BOC / Broker | — | 1 day |
| 5 | **Drayage (Hauling)**: Broker coordinates with haulier to pick up container and deliver to DC | In-house Broker | Logistics Mgr | 4-8 hours |
| 6 | **Empty Return**: Haulier returns empty container to port/yard to avoid detention fees (W249) | Haulier | — | 1 day |

### System Touchpoints
- BOC e2m System Integration
- Landed Cost Module (Duty/Tax/Hauling allocation)
- Container Tracking Dashboard (Port Arrival -> Released -> DC Received -> Empty Returned)

### Pain Points / Risks
- **Demurrage & Detention**: Delays in BOC release or haulier availability lead to heavy per-day fines (W249).
- **Misclassification**: Incorrect HS Code selection leads to re-assessment and BOC penalties.

---

## W492. Temperature-Controlled & Sensitive Goods Logistics

| Field | Detail |
|---|---|
| **Trigger** | Inbound shipment of temperature-sensitive goods; seasonal temperature extremes (Philippine dry season March–May); quality hold at goods receipt |
| **Frequency** | Ongoing (~15–20% of SKUs require temperature or humidity control during storage/transport) |
| **Volume** | ~5,000–7,000 temperature-sensitive SKUs (paint, adhesives, chemicals, solvents, resins, sealants); ~300–500 inbound shipments/month containing sensitive goods |
| **Owner** | DC Operations Manager |
| **Participants** | DC Receiving, Warehouse Supervisor, Quality Inspector, Transport Coordinator, Buyer, Store Receiving |

### Background

A significant portion of BuildRight's merchandise requires temperature, humidity, or light-protection controls during storage and transport: (a) **paints and coatings** (degrade above 35°C, freeze below 0°C — rare in the Philippines but possible in air-conditioned environments); (b) **adhesives and sealants** (lose bonding strength with temperature cycling); (c) **solvents and thinners** (flammability risk increases with temperature — intersects with W236/W237 hazmat); (d) **PVC pipes and fittings** (become brittle with UV exposure and extreme heat); (e) **electrical wire insulation** (degrades with prolonged heat exposure); (f) **wood treatments and preservatives** (chemical degradation in high humidity); (g) **seasonal items** (Christmas lights — electronics degrade in heat/humidity storage). The Philippine tropical climate (average 27–35°C, 70–90% humidity) makes temperature-controlled logistics critical for product quality. Existing workflows cover hazmat storage (W236) and hazmat handling (W237) but do not address the broader category of temperature-sensitive goods that are not classified as hazardous but still require controlled storage and transport.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Sensitive Goods Classification**: At SKU creation (W252), Merchandising classifies each item's storage requirements: (a) **Temperature-controlled**: specify temperature range (e.g., paint: 15–30°C); (b) **Humidity-controlled**: specify humidity range (e.g., adhesives: < 60% RH); (c) **Light-protected**: specify UV protection required; (d) **Ambient but covered**: shelter from direct sun/rain only; (e) **Standard**: no special requirements; classification stored in Item Master (W252) and Product Attribute Template (W298) | Merchandising / Category Manager | VP Merchandising | Per W252 |
| 2 | **DC Storage Zone Management**: DC Operations Manager maintains temperature-controlled storage zones: (a) **Climate-controlled room** (air-conditioned, 18–25°C) for paints, adhesives, chemicals — continuously monitored; (b) **Covered warehouse** (ventilated, protected from direct sun) for PVC, electrical, wood treatments; (c) **Standard warehouse** for non-sensitive goods; (d) temperature and humidity sensors with real-time alerts to DC Operations Manager; (e) daily temperature logs archived for quality audit trail | DC Operations Manager | VP Supply Chain | Continuous |
| 3 | **Inbound Quality Check (Temperature-Sensitive)**: At DC receiving (W3), Receiving Clerk performs additional checks for sensitive goods: (a) verify transport vehicle condition (was the container/truck properly ventilated?); (b) for imported goods: verify container temperature log (reefer containers if applicable); (c) visual inspection for heat damage (swollen paint cans, melted adhesive packaging, discolored PVC); (d) if quality concern: place on quality hold per W3 procedures and notify Quality Inspector (W110); (e) expedite putaway to climate-controlled zone | DC Receiving / Quality Inspector | DC Operations Manager | 15 min/shipment |
| 4 | **Outbound Transport Planning**: Transport Coordinator plans temperature-sensitive outbound shipments: (a) schedule sensitive goods delivery during cooler hours (early morning or evening) during dry season (March–May); (b) use covered/enclosed trucks for sensitive goods (not open-wing vans during rain or extreme heat); (c) for multi-drop routes: load sensitive goods last (deliver first) to minimize time in truck; (d) include temperature indicator cards in sensitive goods shipments for high-value or quality-critical deliveries | Transport Coordinator | DC Operations Manager | Per W106 |
| 5 | **Store Receiving & Storage**: Store Receiving Clerk handles sensitive goods at store: (a) verify condition upon receipt (check for heat damage during transport); (b) expedite putaway to designated store storage area (air-conditioned backroom or covered shelving — not in outdoor yard during dry season); (c) ensure shelf display of sensitive items is in climate-controlled store interior (not near store entrance or loading dock where temperature fluctuates); (d) rotate stock using FEFO (First Expiry, First Out) for items with shelf life affected by temperature | Store Receiving Clerk | Store Manager | Per W109 |
| 6 | **Seasonal Alert Protocol**: DC Operations Manager activates seasonal protocols: (a) **Dry season (March–May)**: increase monitoring frequency, restrict sensitive goods loading to early morning, activate backup ventilation in DC; (b) **Rainy season (June–October)**: increase humidity monitoring, protect covered-only items from water ingress, increase inspection of containers for condensation damage; (c) issue seasonal storage and handling bulletins to all stores and DCs | DC Operations Manager | VP Supply Chain | 1 day/season |
| 7 | **Quality Incident Investigation**: If temperature-related quality issue is reported (customer complaint W41, product return W12A, quality hold W110): (a) pull temperature logs from DC storage zone and transport records; (b) determine if temperature excursion occurred and when; (c) assess scope: how many SKUs, which batches, which stores affected; (d) if confirmed: initiate product recall W29 or targeted withdrawal; (e) update storage/transport procedures to prevent recurrence; (f) document in quality incident register (W110) | Quality Inspector / DC Operations Manager | VP Supply Chain | 1–3 days/incident |
| 8 | **Annual Storage Compliance Review**: Annually, DC Operations Manager reviews temperature-controlled storage infrastructure: (a) audit temperature and humidity sensor accuracy; (b) assess climate-controlled room capacity vs. sensitive SKU volume (capacity planning W376); (c) evaluate HVAC system maintenance status (W240); (d) review temperature log archives for any excursion patterns; (e) recommend capital improvements (W21) if capacity insufficient; (f) update sensitive goods storage map in Warehouse Location & Bin Master (W297) | DC Operations Manager | VP Supply Chain | 1 week/annual |

### System Touchpoints
- Item Master (W252): storage requirement classification per SKU
- Product Attribute Template (W298): temperature, humidity, and light sensitivity attributes
- Warehouse Location & Bin Master (W297): climate-controlled zone mapping
- WMS (W3/W4): putaway logic routing sensitive goods to correct zones
- Temperature/Humidity Monitoring System: real-time alerts, historical logs
- Transport Management System (W106/W196): route planning with temperature considerations
- Quality Management (W110): quality hold and incident tracking
- Integration with W3 (DC receiving), W106 (dispatch planning), W109 (store receiving), W236 (hazmat storage), W240 (DC maintenance), W252 (item master), W297 (warehouse location master), W298 (product attributes)

### Pain Points / Risks
- **Philippine tropical climate**: Average temperatures of 30–35°C during dry season (March–May) and humidity of 70–90% year-round create constant stress on temperature-sensitive goods; even covered warehouse storage may not be sufficient during peak heat, leading to product degradation before the item reaches the customer
- **Last-mile heat exposure**: During store delivery (W4), sensitive goods may sit on the loading dock or in the truck for extended periods during multi-drop routes; a 2-hour exposure to direct Philippine sunlight can damage paint or adhesives
- **Lumber yard challenge**: Outdoor lumber yard storage (W3B) has no temperature control; pressure-treated lumber and wood preservatives stored in the yard are subject to full tropical conditions
- **Sensor coverage gaps**: Temperature sensors monitor zone averages but may miss hot spots (near loading dock doors, near roof, near HVAC vents); localized temperature excursions can damage goods without triggering alerts
- **Cost of climate-controlled storage**: Expanding climate-controlled storage capacity at 4 DCs is capital-intensive; the cost of expanded capacity must be justified against the cost of temperature-related product losses

### Time Estimate
- Ongoing monitoring: ~2–4 hours/week (DC Operations Manager — absorbed from existing duties)
- Inbound quality check: ~15 min per sensitive goods shipment
- Outbound transport planning: ~30 min additional per route containing sensitive goods
- Seasonal alert protocol: 1 day/season (2x/year for dry and wet seasons)
- Annual compliance review: 1 week
- **Total incremental annual effort**: ~150–200 hours/year for DC Operations Manager

### Staffing Implication
- **DC Operations Manager**: ~150–200 hours/year additional for temperature-sensitive goods management. Absorbed within existing role.
- **DC Receiving Clerks**: ~15 min additional per sensitive goods shipment. Absorbed.
- **Store Receiving Clerks**: ~5–10 min additional per sensitive goods receipt. Absorbed.

---

## W558. Supplier Risk Assessment & Supply Disruption Contingency Planning

| Field | Detail |
|---|---|
| **Trigger** | Annual supplier risk review cycle (Q1); ad hoc disruption event (typhoon, port congestion, supplier bankruptcy, geopolitical trade restriction, raw material shortage) |
| **Frequency** | Annual full review of all ~1,000 vendors; continuous monitoring of ~50 critical/single-source vendors; ~4–6 significant disruption events per year |
| **Volume** | ~1,000 vendors assessed annually; ~20–30 critical single-source dependencies identified; ~8–12 contingency plan activations per year |
| **Owner** | VP Supply Chain / Procurement Director |
| **Participants** | Procurement Director (A), Category Manager (R), Supply Planning Manager (R), VP Merchandising (C), Finance Manager (C for cost impact), Customs Broker (C for import disruptions) |

### Background

W44 covers vendor performance scorecards (quality, delivery, cost). W491 covers supplier financial health and credit risk monitoring. W60 covers emergency procurement. W56 covers customer backorder management. W31 covers demand forecasting. However, no workflow covers holistic supplier risk assessment and supply disruption contingency planning — the systematic identification, assessment, and mitigation of supply chain risks including: single-source dependency, geographic concentration, financial instability, geopolitical trade restrictions, natural disaster exposure, and logistics bottleneck vulnerability. For a Philippine hardware retailer with ~40% of COGS from imports (China, Taiwan, Indonesia, Malaysia, Japan, Europe) and operations across an archipelago with 20+ typhoons per year, supply disruption risk is a constant operational reality. The company imports ~400–600 TEUs per month and relies on Manila North/South Harbor and regional ports that experience periodic congestion.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Annual supplier risk assessment cycle initiation (Q1): Procurement Director assigns risk assessment to each Category Manager for vendors in their category; provides assessment template with risk dimensions, scoring criteria, and deadline; Category Managers responsible for assessing all vendors with annual spend > PHP 500K and all single-source vendors regardless of spend | Procurement Director | VP Supply Chain | 1 day (kickoff) |
| 2 | Risk classification for each vendor across six dimensions: (a) **Financial risk** — pull W491 financial health data, payment behavior trends, credit reports (where available), years in business; (b) **Geographic risk** — country of origin political stability, distance from Philippines, port dependency (Manila vs. regional port), shipping route vulnerability; (c) **Single-source dependency** — count SKUs exclusive to this vendor with no alternative source identified, percentage of category spend concentrated with this vendor; (d) **Logistics risk** — shipping route exposure (South China Sea, Pacific typhoon belt), port congestion history (Manila North/South Harbor delays), inter-island dependency for domestic vendors; (e) **Regulatory risk** — import restriction exposure, tariff change probability, customs clearance delay history (BOC red lane frequency); (f) **Quality risk** — defect rate history per W44, product recall history, quality audit findings | Category Manager | Procurement Director | 15–20 min/vendor |
| 3 | Risk scoring: each dimension scored 1–5 (1 = Low risk, 2 = Minor, 3 = Moderate, 4 = High, 5 = Critical); weighted composite score calculated with configurable weights: financial risk (25%), geographic risk (15%), single-source dependency (25%), logistics risk (15%), regulatory risk (10%), quality risk (10%); system auto-calculates composite and flags dimension scores ≥ 4 for individual attention | Category Manager / System | Procurement Director | 5 min/vendor (system calculation) |
| 4 | Vendor classification by risk tier: (a) **Tier A — Critical** (composite score >4.0, OR single-source dependency score = 5, OR annual spend > PHP 50M); (b) **Tier B — Important** (composite score 3.0–4.0); (c) **Tier C — Standard** (composite score <3.0); system generates risk-tiered vendor list with drill-down by category and risk dimension; Procurement Director reviews and approves tier classifications | Category Manager / Procurement Director | VP Supply Chain | 4–6 hours (review session) |
| 5 | For Tier A Critical vendors: mandatory contingency plan per SKU category — Category Manager develops contingency plan in collaboration with Supply Planning Manager; plan must address: (a) qualified alternative source (minimum 2 qualified vendors per critical SKU per W36 vendor qualification); (b) safety stock policy override (increase safety stock per W312 for disruption-prone items — target: 45 days of supply for Tier A vendor SKUs vs. standard 21 days); (c) pre-positioned buffer inventory at alternate DC (e.g., if primary vendor supplies through Manila, pre-position buffer at Cebu DC); (d) emergency logistics route (alternative port, air freight for critical items — air freight cost premium documented and pre-approved per W60); (e) customer communication template for potential stockouts (pre-drafted per W571 store communication format) | Category Manager / Supply Planning Manager | Procurement Director | 4–8 hours/Tier A vendor |
| 6 | Contingency plan approval and activation readiness: Procurement Director reviews all Tier A contingency plans — verifies alternative vendor qualification status per W36, confirms safety stock levels are updated per W312, validates emergency logistics route feasibility with Logistics Manager; approved contingency plans loaded into supply chain control tower per W250 for activation when triggered | Procurement Director | VP Supply Chain | 2–4 hours (review session) |
| 7 | Supply disruption response protocol — **disruption detected**: (a) disruption signal received (supplier notification of force majeure, PAGASA typhoon warning Signal No. 3+, port closure advisory, BOC congestion alert, news of supplier bankruptcy, geopolitical trade restriction announcement); (b) Supply Planning Manager assesses impact within 4 hours: affected SKUs, current inventory on hand at DCs, days of supply by SKU, affected stores, customer order exposure (open SOs for affected SKUs); (c) **If >30 days of supply**: monitor only — increase monitoring frequency to daily, no immediate action | Supply Planning Manager | VP Supply Chain | 2–4 hours (initial assessment) |
| 8 | Supply disruption response — **escalation tiers**: (d) **If 14–30 days of supply**: activate safety stock buffer per contingency plan, expedite alternative vendor quotes per W36 (fast-track qualification for pre-identified alternatives), notify Category Manager for demand-side management; (e) **If <14 days of supply**: emergency procurement per W60, customer allocation per W105 (allocate remaining stock to highest-margin channels and B2B contractual obligations), substitute product recommendation per W279 (Merchandising identifies acceptable substitute SKUs); (f) VP Supply Chain authorizes emergency response expenditure > PHP 5M (air freight, spot-market premium purchases, expedited customs clearance fees) | Supply Planning Manager / Category Manager | VP Supply Chain | 4–8 hours/response |
| 9 | Disruption communication: Category Manager notifies stakeholders per disruption communication matrix — (a) Store Operations per W571 (store communication): affected SKUs, expected stockout dates, substitute product recommendations, customer messaging guidance; (b) Merchandising for assortment adjustment per W279: temporary product substitution, website/catalog update for out-of-stock items; (c) Customer Service for affected B2B orders: proactive outreach to top B2B accounts with open orders for affected SKUs, offer substitutes or revised delivery dates; (d) Finance Manager for cost impact assessment: emergency procurement premium, air freight cost, revenue at risk from stockouts | Category Manager | Procurement Director | 2–4 hours/disruption |
| 10 | Post-disruption review (within 2 weeks of resolution): (a) root cause analysis — what caused the disruption, was it predictable, could it have been prevented; (b) response effectiveness — how quickly was the disruption detected, how effective was the contingency plan, were alternative vendors able to supply, what was the stockout impact (lost sales, customer complaints); (c) contingency plan update — revise plan based on lessons learned; (d) vendor scorecard impact per W44 — document disruption in vendor performance record, adjust vendor risk score if warranted; (e) cost impact report — total disruption cost (premium freight, lost sales, substitute product margin impact) submitted to Finance Manager | Supply Planning Manager / Category Manager | VP Supply Chain | 4–8 hours/post-mortem |
| 11 | Quarterly disruption risk dashboard: Procurement Director presents to VP Supply Chain and VP Merchandising — (a) active disruptions and response status; (b) Tier A vendor risk score trends (improving/worsening); (c) contingency plan coverage (% of Tier A SKUs with qualified alternative source); (d) response time metrics (time from disruption detection to contingency activation); (e) disruption cost trend (quarterly comparison); (f) new risks identified during quarter (geopolitical, regulatory, market) | Procurement Director | VP Supply Chain | 4 hours/quarter (dashboard + presentation) |

### System Touchpoints

- Supplier risk assessment module with scoring and tiering (SCP-009)
- Purchase recommendation — alternative vendor suggestion (SCP-007)
- Vendor management — vendor data source (PUR-003)
- Import POs — import risk assessment (PUR-004)
- Vendor performance scorecard — quality/delivery data (W44)
- Supplier financial health — financial risk data (W491)
- Emergency procurement — disruption response (W60)
- Backorder management — customer impact (W56)
- Demand forecasting — demand data (W31)
- Replenishment parameters — safety stock override (W312)
- Multi-channel allocation — allocation during shortage (W105)
- Product substitution — substitute recommendation (W279)
- Store communication — disruption notification (W571)
- Supply chain control tower — real-time visibility (W250)

### Time Estimate

Annual full review: ~320 person-hours (1,000 vendors × ~20 min each). Per-disruption response: ~8–16 hours (initial assessment + escalation + communication). Quarterly dashboard: ~4 hours. Total annual effort: ~450–500 person-hours. Distributed across Category Managers (assessment), Supply Planning Manager (response), and Procurement Director (review).

### Pain Points / Risks

- Philippine port congestion (especially Manila North/South Harbor) is chronic and unpredictable — container dwell times can spike from 5 days to 15+ days during peak periods (Ber months, pre-Christmas); mitigated by diversifying port of entry (Subic, Batangas, Cebu) per W144 and maintaining safety stock buffers per W312
- Typhoon paths are difficult to forecast beyond 3 days — PAGASA provides 3-day tropical cyclone warnings; supply chain decisions must be made quickly once a typhoon track is confirmed; mitigated by pre-positioned buffer inventory and pre-qualified alternative vendors
- Chinese New Year factory closures affect ~40% of import vendors for 2–3 weeks every January–February — this is a predictable annual disruption but requires significant pre-buying and inventory build; mitigated by W32 seasonal buy planning and W312 safety stock adjustment
- Alternative vendor qualification takes 3–6 months per W36 — during an active disruption, there is no time to qualify a new vendor; mitigated by pre-qualifying alternative vendors during the annual review (step 5) and maintaining a bench of warm standby vendors
- Political instability in source countries (Myanmar, Indonesia) can disrupt supply overnight — government-imposed export restrictions, currency controls, or civil unrest; mitigated by geographic diversification of source countries and maintaining inventory buffers for politically unstable source regions

### Staffing Implication

- Covered by existing Supply Planning Manager and Category Managers; no incremental headcount needed.
- Annual review adds ~320 person-hours in Q1 distributed across ~10 Category Managers (~32 hours each).
- Per-disruption response (~8–16 hours) absorbed by Supply Planning Manager and Category Managers as part of operational duties.
- Procurement Director quarterly review (~4 hours) absorbed within existing reporting cadence.
- **Capital expenditure**: Temperature monitoring sensors, climate-controlled storage expansion, and HVAC maintenance are Capex items (W21/W240).

---

## W596. Store-Level Replenishment Exception Management & Auto-Override

| Field | Detail |
|---|---|
| **Trigger** | System flags replenishment exceptions in the automated suggested order queue; Supply Planner identifies override need; Store Manager escalates stock-out emergency |
| **Frequency** | Daily exception queue review; ~150–250 exceptions/week across all DCs |
| **Volume** | ~5,000 replenishment orders/month total (W4); ~5–8% generate exceptions requiring manual intervention = ~250–400 exceptions/month; exception types: new store ramp-up (~10%), promotional spike (~25%), store-specific demand anomaly (~20%), supply shortage allocation override (~30%), system parameter error (~15%) |
| **Owner** | Supply Planner |
| **Participants** | Supply Planner (R/A), Supply Planning Manager (A for high-value overrides), Category Manager (A for allocation conflicts), Store Manager (R for stock-out escalation), DC Supervisor (R for expedited picking), Logistics Coordinator (R for expedited transport) |

### Background

W4 covers the standard store replenishment process (DC to Store) using an automated ROP/min-max or demand forecast-driven system. W22 covers stock transfers (store-to-store and inter-DC). W57 covers promotional stock allocation and pre-positioning. W31 covers demand forecasting. W214 covers expedited store-to-store transfers. However, no workflow covers the management of exceptions to the automated replenishment system — the situations where the system's suggested orders are wrong, insufficient, or require human judgment.

In a 200-store chain with 35,000 SKUs, the automated replenishment system generates ~5,000 orders/month. The system is effective for steady-state items with predictable demand, but it struggles with: (a) new stores in their ramp-up phase (first 3–6 months) where demand history does not yet exist; (b) promotional demand spikes that exceed the system's forecast; (c) store-specific anomalies (a local construction boom drives demand for cement and steel at one store, but the system does not detect this micro-demand signal); (d) supply shortage situations where available inventory must be allocated across stores based on strategic priority rather than system logic; (e) system parameter errors (incorrect ROP, safety stock, or lead time) that generate nonsensical suggestions.

Without exception management, the replenishment system either overstocks stores (tying up working capital) or understocks them (causing lost sales and customer dissatisfaction). The exception management workflow ensures that human judgment supplements system logic where needed, while maintaining the efficiency of automation for the ~92–95% of orders that do not require intervention.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Exception queue review**: Supply Planner opens the replenishment exception dashboard each morning — system has pre-classified exceptions into categories: (a) **new store ramp-up**: replenishment suggestions for stores <6 months old that have no reliable demand history — system generates suggested orders based on analogous store profiles but confidence is low; (b) **promotional spike**: SKUs where the promotional demand forecast (W57) significantly exceeds the system's normal replenishment suggestion — system flags items where promo allocation is insufficient to cover forecasted lift; (c) **demand anomaly**: SKUs at specific stores where actual sales velocity in the past 7 days exceeds the rolling 30-day average by >50% — indicates a local demand event the system has not captured; (d) **supply shortage allocation**: SKUs where total DC inventory is insufficient to fulfill all store replenishment suggestions — system requires allocation decision; (e) **parameter anomaly**: system detects suggested order quantities that exceed 3× the normal order quantity for an SKU-store combination, suggesting a possible parameter error; Supply Planner reviews queue prioritized by business impact: supply shortage (highest — potential stock-out across multiple stores) > demand anomaly > promotional spike > new store ramp-up > parameter anomaly | Supply Planner | Supply Planning Manager | 30–60 min/day |
| 2 | **Root cause classification**: for each exception, Supply Planner determines root cause — (a) **new store ramp-up**: review analogous store profile accuracy — is the reference store a good match? Has the new store's actual demand diverged from the profile?; (b) **promotional spike**: cross-reference with W13 promotional calendar and W57 promo allocation — was the promo allocation already consumed? Did the promo perform above expectations?; (c) **demand anomaly**: check for local events — is there a construction project, government infrastructure project, typhoon rebuilding effort, or seasonal event driving demand at this specific store? Check with Store Manager if needed; (d) **supply shortage**: check PO status with Buyer — is a replenishment PO in transit? When is the next DC receipt? Is the shortage temporary or extended?; (e) **parameter anomaly**: review ROP, safety stock, lead time, and demand averaging period for the SKU — identify which parameter is driving the anomaly | Supply Planner | Supply Planning Manager | 5–15 min per exception |
| 3 | **Manual override request and approval**: based on root cause analysis, Supply Planner prepares override action — (a) **quantity override**: increase or decrease the suggested order quantity for specific SKU-store combinations; (b) **allocation override**: redistribute available DC inventory across stores based on strategic priority (high-volume stores first, stores with active promotional commitments first, stores in construction boom areas first); (c) **priority override**: mark specific replenishment orders as urgent to move to front of DC pick queue; (d) **parameter correction**: fix incorrect ROP, safety stock, or lead time parameters and regenerate the suggested order; approval requirements: (i) overrides affecting <10 stores and <PHP 100K total value: Supply Planner self-approves with documentation; (ii) overrides affecting 10–50 stores or PHP 100K–500K: Supply Planning Manager approval; (iii) overrides affecting >50 stores or >PHP 500K: Category Manager and Supply Planning Manager joint approval | Supply Planner | Supply Planning Manager / Category Manager | 5–10 min per override (plus approval wait time) |
| 4 | **Expedited order creation**: for urgent stock-out situations where the normal replenishment cycle (1–3 days per W4) is too slow — (a) Supply Planner creates expedited replenishment order with "Urgent" priority flag; (b) system routes to DC Supervisor for priority picking — bumps to front of pick queue; (c) Logistics Coordinator arranges next-available truck or LTL shipment per W52 rather than waiting for next scheduled delivery day; (d) expedited orders carry a cost premium (partial truck utilization, possible overtime at DC); (e) Supply Planner tracks expedited order cost for monthly exception cost analysis (step 7) | Supply Planner / DC Supervisor | Supply Planning Manager | 15–20 min per expedited order |
| 5 | **Allocation conflict resolution**: when multiple stores need the same SKU and DC inventory is insufficient — (a) system generates allocation conflict report: SKU, available DC inventory, total store demand, shortfall quantity; (b) Supply Planner applies allocation rules in priority order: (i) stores with active promotional commitments (W57) — promo stock must be protected; (ii) top 20% stores by sales volume for the SKU category — protect highest-revenue locations; (iii) stores with zero on-hand — prioritize complete stock-out locations over partial stock locations; (iv) geographic distribution — ensure no region is completely stocked out of essential items (cement, electrical, plumbing basics); (v) remaining inventory distributed proportionally; (c) for critical allocation conflicts (e.g., cement during typhoon rebuilding season, plywood during construction peak): escalate to Category Manager and Supply Planning Manager for strategic allocation decision | Supply Planner | Category Manager | 15–30 min per allocation conflict |
| 6 | **Emergency inter-store transfer trigger**: when a store is completely stocked out of a critical item and DC replenishment cannot arrive fast enough — (a) Supply Planner searches inventory at nearby stores (within same city or region) for the needed SKU; (b) if available: initiate emergency inter-store transfer per W214 — system creates Transfer Order, Store Manager at source store confirms availability, Logistics arranges pickup; (c) transfer cost (transport, labor) vs. lost sales cost calculation documented — if transfer cost < estimated lost sales, transfer is justified; (d) for transfers between stores in different legal entities: system generates intercompany transfer pricing per W22 governance | Supply Planner / Store Manager | Supply Planning Manager | 15–20 min per emergency transfer |
| 7 | **Exception pattern analysis**: monthly, Supply Planning Manager reviews exception patterns to identify systemic issues — (a) exception volume trend: are exceptions increasing or decreasing month-over-month?; (b) exception category distribution: which categories dominate?; (c) SKU concentration: are the same SKUs repeatedly generating exceptions? (indicates parameter correction needed at W31 level); (d) store concentration: are specific stores generating disproportionate exceptions? (new store ramp-up issue, or store-specific demand pattern not captured by system); (e) expedited order cost trend: are expedited orders increasing? What is the cost premium?; (f) feed findings into W31 quarterly forecast recalibration (parameter corrections), W4 replenishment model tuning (algorithm adjustments), and W34 scheduling (DC overtime planning for expedited picking) | Supply Planning Manager | VP Supply Chain | 2–3 hours/month |

**Total time per week**: ~8–12 hours/week for Supply Planner (daily exception review ~45 min + override actions ~30 min + allocation conflicts ~30 min + emergency transfers ~30 min). Monthly analysis adds ~3 hours.

### System Touchpoints (W596 — Replenishment Exception Management)

- Replenishment exception dashboard with categorized exception queue (SCP-001)
- Automated ROP/min-max replenishment engine — exception detection layer (W4, SCP-001)
- Demand forecasting module for anomaly detection and promotional demand overlay (W31)
- Promotional allocation and pre-positioning — promo commitment protection (W57)
- Store inventory visibility for inter-store transfer sourcing (W4, W22)
- Transfer order creation for emergency inter-store transfers (W214)
- PO tracking for supply shortage root cause analysis (W2)
- DC pick wave priority management for expedited orders (W4)
- Logistics and transportation booking for expedited shipments (W52)
- Exception analytics and pattern reporting (SCP-001)
- Intercompany transfer pricing for cross-entity transfers (W22)

### Pain Points / Risks

- **Exception volume overwhelms Supply Planner**: at ~5–8% exception rate on ~5,000 monthly orders, the Supply Planner must process ~250–400 exceptions/month (~15–20 per business day); during peak periods (Christmas, bi-monthly sales, typhoon rebuilding), exception rates can spike to 12–15%, doubling the workload; mitigated by continuously improving forecast accuracy (W31) and replenishment parameters to reduce the exception rate, and by prioritizing exceptions by business impact
- **Allocation decisions are inherently political**: when inventory is short, deciding which stores get stock and which do not creates tension between Supply Planning, Category Management, and Store Operations; mitigated by transparent allocation rules (step 5b), documented rationale, and Category Manager involvement for strategic decisions
- **Emergency inter-store transfers are costly and slow**: moving product between stores requires a truck, driver, and labor at both stores; the transfer cycle can take 1–2 days — not much faster than an expedited DC delivery; mitigated by reserving inter-store transfers for truly critical items (top 100 revenue SKUs) and using DC expedited delivery for less critical situations
- **New store ramp-up takes 3–6 months to stabilize**: without demand history, the system generates unreliable replenishment suggestions; manual override is required for nearly every order in the first 3 months; mitigated by assigning a dedicated Supply Planner to new store openings (W16) for the first 90 days, with daily exception review
- **Typhoon rebuilding demand is impossible to forecast**: a typhoon hitting a region creates sudden, massive demand for construction materials (cement, roofing, nails, plywood, electrical wire) that no statistical model can predict; mitigated by pre-positioning emergency inventory buffers in typhoon-prone regions (Luzon, Eastern Visayas) during typhoon season per W558, and by accepting high exception rates as a cost of disaster response

### Staffing Implication

- **Covered by existing Supply Planners** (within the 30-person Supply Chain team); no incremental headcount needed.
- ~8–12 hours/week for exception management is a core Supply Planner responsibility, representing ~20–30% of a Supply Planner's weekly capacity.
- **During peak periods** (October–December, post-typhoon): exception workload may require temporary assignment of a second Supply Planner or Category Manager support for allocation decisions.
- **Monthly exception analysis** (~3 hours) absorbed by Supply Planning Manager within existing reporting cadence.

---

## W622. Mock Product Recall Exercise & Recall Readiness Testing

| Field | Detail |
|---|---|
| **Trigger** | Annual calendar; semi-annual for high-risk product categories |
| **Frequency** | Annual company-wide; semi-annual for paint, chemicals, electrical items |
| **Volume** | 1 company-wide mock exercise/year; 2 category-specific exercises/year |
| **Owner** | VP Merchandising |
| **Participants** | VP Merchandising, Supply Chain Director, LP Manager, Store Operations Director, Communications Manager, Quality Assurance Specialist, affected Category Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | VP Merchandising selects mock recall scenario: (a) product category (paint, electrical, lumber treatment, appliance), (b) recall reason (safety defect, regulatory non-compliance, contamination), (c) scope (nationwide or regional), (d) exercise timeline (target: 48-hour completion) | VP Merchandising | — | 30 min |
| 2 | Supply Chain Director identifies affected SKU(s) and traces forward in ERP: (a) total quantity manufactured/procured, (b) all locations holding stock (DCs, stores, in-transit, ecommerce inventory), (c) all customer transactions (POS sales, ecommerce orders, wholesale) with customer contact details for notification | Supply Chain Director | — | 60 min |
| 3 | System executes simulated recall actions: (a) block affected SKU at all POS terminals (200 stores), (b) remove from ecommerce and marketplace listings, (c) quarantine in-transit shipments, (d) flag DC stock for hold; all actions timestamped for speed measurement | System | — | 5 min (simulated) |
| 4 | Store Operations Director coordinates simulated store-level actions: (a) Stock Associates locate and quarantine affected product on shelves, (b) customer-facing signage posted, (c) Store Manager confirms quarantine completion via mobile app; time-to-completion measured per store | Store Ops Director | — | 4 hours (simulated) |
| 5 | Communications Manager drafts simulated customer notification: (a) press release, (b) social media announcement, (c) customer email/SMS to affected transaction customers, (d) DTI/FDA notification (simulated); reviews with Legal Counsel for accuracy and liability considerations | Communications Manager | VP Legal | 2 hours |
| 6 | VP Merchandising compiles mock recall performance metrics: (a) time from decision to POS block, (b) time from decision to ecommerce removal, (c) store quarantine completion rate at 4/12/24/48 hours, (d) customer notification completion rate, (e) percentage of affected stock accounted for (target: 100% within 48 hours) | VP Merchandising | — | 2 hours |
| 7 | Post-exercise debrief (within 1 week): all participants review performance metrics, identify gaps in process or system, document lessons learned, and create improvement action items with owners and deadlines | VP Merchandising | COO | 2 hours |
| 8 | Improvement actions tracked in project management system (per W128); system updates made to recall workflow (W29) based on findings; next exercise scenario designed to test improved areas | VP Merchandising | — | 4 hours |

### System Touchpoints
- ERP Inventory module: forward and backward lot/serial traceability
- ERP POS module: SKU blocking capability, store-level quarantine confirmation
- ERP Ecommerce module: product listing removal, customer notification
- ERP CRM module: affected customer identification and contact details
- ERP Supply Chain module: in-transit shipment hold, DC quarantine

### Pain Points / Risks
- **Exercise disruption to operations**: mock recall exercise diverts store staff from selling activities; mitigated by scheduling exercises during low-traffic periods and limiting to 2-3 test stores for detailed execution
- **Incomplete traceability**: if affected SKU cannot be fully traced to all locations and customers, the recall cannot be effectively executed; mitigated by exercise revealing traceability gaps for remediation before actual recall
- **Exercise fatigue**: if exercises are too frequent or poorly designed, staff may not take them seriously; mitigated by varying scenarios and including realistic elements (mock media inquiry, simulated regulatory inspection)
- **Customer notification gap**: exercise may reveal that customer contact data is incomplete or outdated for loyalty/B2B accounts; mitigated by periodic data quality review (per W253)

### Staffing Implication
- **VP Merchandising**: ~8 hours/exercise for planning, execution, and debrief. Absorbed within existing role.
- **Supply Chain Director**: ~4 hours/exercise for tracing and coordination. Absorbed within existing role.
- **Store Operations Director**: ~4 hours/exercise for store coordination. Absorbed within existing role.
- **Participating stores**: ~2-4 hours per exercise for quarantine simulation (limited to 10-20 stores per exercise to minimize disruption).

---

## W623. Cross-Functional New Store Opening Readiness Review

| Field | Detail |
|---|---|
| **Trigger** | New store construction reaches 80% completion milestone (per W225/W227) |
| **Frequency** | Per new store; ~10-15 new stores/year |
| **Volume** | 1 readiness review per new store |
| **Owner** | Store Operations Director |
| **Participants** | Store Operations Director, IT Manager, HR Coordinator, Merchandising Coordinator, Finance Analyst, Supply Planner, Facilities Coordinator, Regional Manager, new Store Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Engineering team confirms 80% construction completion (per W227); triggers readiness review process; Store Operations Director schedules readiness review meeting (T-30 days before target opening) | Engineering Lead | Store Ops Director | 15 min |
| 2 | Each department completes readiness checklist on shared project dashboard: (a) **IT**: network installed, POS terminals configured, RF devices ready, CCTV operational, WiFi tested, ERP access provisioned (per W152), (b) **HR**: Store Manager hired and trained, all positions filled or in final interview, payroll entity configured, biometric system installed, (c) **Merchandising**: initial stock order placed (per W2), planogram loaded, shelf labels printed, promotional materials prepared, (d) **Finance**: GL cost center created, bank deposit account opened, petty cash fund released, LGU business permit secured (per W54), BIR registration complete (per W485), (e) **Supply Chain**: first replenishment delivery scheduled, DC-to-store route confirmed, receiving area prepared, (f) **Facilities**: utilities connected, safety equipment installed, signage erected, parking lot completed | Department Leads | Store Ops Director | 4 hours (each) |
| 3 | Store Operations Director conducts on-site readiness inspection: verifies physical construction completion, fixture installation, signage, safety equipment, receiving dock, customer areas, and backroom; documents findings with photos | Store Ops Director | — | 4 hours |
| 4 | Readiness review meeting (all stakeholders): each department presents readiness status (Green/Yellow/Red); Store Operations Director compiles overall readiness scorecard; critical Red items assigned owners and resolution deadlines before opening | Store Ops Director | COO | 2 hours |
| 5 | Go/No-Go decision: COO approves opening date if (a) all critical items are Green, (b) no more than 3 Yellow items remain, (c) no Red items are safety or compliance related; if criteria not met, opening delayed with revised target date | COO | CEO | 30 min |
| 6 | T-14 days: Store Operations Director conducts follow-up review on all Yellow items; confirms resolution or escalates to COO; new Store Manager begins on-site for pre-opening preparation (per W16) | Store Ops Director | — | 2 hours |
| 7 | T-7 days: soft opening rehearsal — conduct full store operations simulation for 1 day: POS transactions, inventory receiving, customer service scenarios, emergency procedures; identify and resolve operational issues before public opening | Store Ops Director | Regional Manager | 8 hours |
| 8 | T-0: Grand opening; Store Operations Director and Regional Manager on-site for first 3 days; daily check-in calls for first 2 weeks; formal 30-day review per W16 | Store Ops Director | COO | 3 days |
| 9 | Post-opening (T+30): Store Operations Director conducts 30-day review — sales vs. plan, operational issues, customer feedback (per W608), staffing adequacy, system stability; documents lessons learned for next store opening | Store Ops Director | COO | 4 hours |

### System Touchpoints
- ERP Project Management module: readiness checklists, task tracking, milestone management (per W128)
- ERP Store Master: new location creation, configuration activation
- ERP Finance module: cost center creation, budget allocation
- ERP HR module: employee provisioning, payroll entity setup
- ERP POS module: terminal configuration, testing
- Mobile app: readiness checklist with photo documentation

### Pain Points / Risks
- **Construction delays pushing readiness**: if construction completion slips, all downstream readiness activities are compressed; mitigated by 80% trigger point and T-14 follow-up allowing 2-week contingency
- **Cross-functional coordination gaps**: departments may not communicate dependencies (e.g., IT needs network before POS, HR needs payroll entity before hiring); mitigated by shared project dashboard with dependency visualization
- **Initial stock timing**: merchandise must arrive 3-5 days before opening for shelf stocking, but early arrival requires security and insurance coverage; mitigated by phased delivery schedule and temporary security arrangements
- **LGU permit delays**: LGU business permit processing varies by municipality and can be unpredictable; mitigated by initiating permit applications at construction start (not at 80% completion)

### Staffing Implication
- **Store Operations Director**: ~8 hours per new store for readiness process. With 10-15 stores/year = ~80-120 hours/year. Absorbed within existing role.
- **Department Leads**: ~4 hours each per new store. With 10-15 stores/year = ~40-60 hours/year per department. Absorbed within existing roles.
- **Regional Manager**: ~3 days on-site per opening = ~30-45 days/year. Dedicated regional coverage for new store openings.

---

## W680. Supply Chain Cost Analysis & Logistics Optimization Review

| Field | Detail |
|---|---|
| **Trigger** | Monthly cost analysis cycle; quarterly optimization review |
| **Frequency** | Monthly cost analysis; quarterly optimization review; annual strategic assessment |
| **Volume** | ~PHP 3-4B annual supply chain cost (inbound freight, DC operations, outbound distribution, 3PL, port/customs); ~60,000 store replenishment orders/year |
| **Owner** | VP Supply Chain |
| **Participants** | DC Operations Manager, Logistics Manager, FP&A Analyst, Procurement Manager |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | FP&A Analyst extracts monthly supply chain cost data from GL: inbound freight (vendor-to-DC), import logistics (port/customs/brokerage per W464), DC operating costs (labor, equipment, utilities per W584), outbound distribution (DC-to-store, 3PL per W242), inter-island freight (W66), last-mile delivery (W268), and fleet costs (W198 fuel + W199 telematics) | FP&A Analyst | VP Supply Chain | 4 hours |
| 2 | VP Supply Chain reviews cost-per-unit metrics: cost per case received, cost per case shipped, cost per store delivery, cost per ecommerce order fulfilled, cost per TEU imported; compares against prior month, same period last year, and industry benchmarks | VP Supply Chain | — | 3 hours |
| 3 | DC Operations Manager provides DC cost analysis: labor cost per unit handled (receiving, putaway, picking, shipping), equipment cost per hour, facility cost per sqm, overtime as % of total DC labor; identifies cost reduction opportunities | DC Operations Manager | VP Supply Chain | 3 hours |
| 4 | Logistics Manager analyzes distribution cost: owned fleet vs. 3PL cost per km per kg, route efficiency (deliveries per route, utilization rate per W196), fuel cost per delivery (per W198), port demurrage avoidance per W249 | Logistics Manager | VP Supply Chain | 3 hours |
| 5 | VP Supply Chain identifies optimization opportunities: DC network rebalancing (can any DC serve more stores with shorter routes), consolidation opportunities (combining shipments to reduce truck count), mode shift evaluation (DSD vs. DC fulfillment for specific categories), 3PL contract renegotiation per W242 | VP Supply Chain | COO | 4 hours |
| 6 | Monthly: VP Supply Chain produces cost trend dashboard for COO: total supply chain cost as % of revenue (target ≤ 6%), per-unit cost trends, and top 3 cost reduction initiatives in progress | VP Supply Chain | COO | 2 hours |
| 7 | Quarterly: VP Supply Chain conducts optimization review with COO and CFO: presents cost reduction roadmap, capital investment proposals (e.g., DC automation, fleet replacement), and make-vs-buy analysis for logistics | VP Supply Chain | COO, CFO | 4 hours |
| 8 | Annual: VP Supply Chain develops 3-year logistics strategy aligned with store expansion plan (10-15 new stores/year): DC capacity planning, fleet sizing, 3PL partner strategy, and technology roadmap | VP Supply Chain | COO, CFO | 5 days |

### System Touchpoints
- GL cost accounting
- DC labor management system
- Fleet telematics (W199)
- 3PL billing module
- Freight audit (W277)
- BI analytics

### Time Estimate
- Monthly: 2 days
- Quarterly review: 2 days
- Annual strategy: 5 days

### Pain Points / Risks
- Philippine island geography limiting distribution optimization
- Port congestion (Manila, Cebu) causing unpredictable dwell time costs
- 3PL rate escalation in provinces with limited carrier options
- DC labor cost rising faster than productivity improvements

### Staffing Implication
- VP Supply Chain: ~2 days/month + 2 days/quarter + 5 days/year
- FP&A Analyst: ~1 day/month data extraction
- Absorbed within existing roles

---

## W727. Carrier & Freight Forwarder Daily Performance Monitoring

| Field | Detail |
|---|---|
| **Trigger** | Start of supply chain operations day; or carrier SLA breach alert |
| **Frequency** | Daily review; real-time SLA monitoring |
| **Volume** | ~20-30 active carriers/freight forwarders; ~100-150 truck movements/day; 400-600 TEU shipments/month (imports) |
| **Owner** | Logistics Manager |
| **Participants** | DC Dispatch Supervisor, Carrier Account Manager, Supply Chain Planner |

### Background

W242 covers periodic 3PL performance reviews (quarterly/annual). W44 covers vendor performance scoring. Neither addresses the daily operational monitoring of carrier and freight forwarder performance that is essential for a 4-DC, 200-store logistics network processing ~5,000 replenishment orders/month. Daily carrier performance monitoring enables early detection of service degradation, proactive issue resolution, and data-driven carrier selection. This workflow complements W250 (supply chain control tower) which provides real-time shipment visibility, by adding the carrier performance management layer.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Daily carrier performance dashboard review**: Logistics Manager reviews carrier performance dashboard: (a) on-time delivery (OTD) rate per carrier: target ≥95% for DC-to-store deliveries; (b) on-time pickup rate for DC outbound per W106; (c) transit time adherence: actual vs. promised delivery lead time per W304 routing master; (d) damage rate: % of shipments with damage claims per W500; (e) truck utilization: % of truck capacity used per shipment (target ≥85%); (f) documentation compliance: delivery receipts, proof of delivery, fuel surcharge documentation; (g) SLA breaches in past 24 hours highlighted for immediate action | Logistics Manager | VP Supply Chain | 20-30 min/day |
| 2 | **SLA breach investigation and escalation**: for each SLA breach: (a) Logistics Manager identifies root cause: (i) carrier-caused: vehicle breakdown, driver no-show, overbooking, routing error; (ii) BuildRight-caused: late dispatch from DC, incorrect loading, documentation error; (iii) external: traffic, weather, road closure, port congestion; (b) for carrier-caused delays: (i) first occurrence: verbal notification to carrier account manager; (ii) repeat occurrence within 30 days: formal written notice and improvement plan; (iii) three occurrences in 90 days: carrier review meeting with VP Supply Chain and potential volume reduction; (c) document investigation and resolution in carrier performance log | Logistics Manager | VP Supply Chain | 15-30 min per breach |
| 3 | **Carrier allocation decision**: Logistics Manager makes daily carrier allocation decisions: (a) review upcoming 48-hour dispatch plan from W106; (b) allocate shipments to carriers based on: (i) current performance score (weighted: OTD 40%, damage 20%, cost 20%, documentation 20%); (ii) geographic coverage: carrier has routes serving destination store; (iii) capacity availability: carrier has vehicles available; (iv) cost: lane-specific rate competitiveness; (c) for underperforming carriers: reduce allocation until performance improves; (d) for top-performing carriers: offer volume commitments and preferred status | Logistics Manager | VP Supply Chain | 20-30 min/day |
| 4 | **Import freight forwarder monitoring**: for import shipments: (a) track freight forwarder performance per shipment: (i) booking confirmation timeliness; (ii) container availability for stuffing; (iii) documentation accuracy (bill of lading, packing list); (iv) customs clearance speed per W464; (v) port-to-DC delivery timeliness; (b) compare forwarder performance across trade lanes (China, Taiwan, Indonesia, Japan, Europe); (c) flag forwarders with recurring issues for review | Logistics Manager / Import Coordinator | VP Supply Chain | 15-20 min/day |
| 5 | **Weekly carrier performance summary**: Logistics Manager compiles weekly carrier scorecard: (a) all carriers ranked by composite performance score; (b) trend analysis: improving vs. declining carriers; (c) cost analysis: cost per ton-km by carrier and lane; (d) volume allocation vs. performance alignment; (e) recommendations: carrier additions, removals, volume shifts; (f) report submitted to VP Supply Chain | Logistics Manager | VP Supply Chain | 1-2 hours/week |

### System Touchpoints

- Carrier performance dashboard with automated SLA monitoring
- TMS (Transportation Management System) for shipment tracking and delivery confirmation
- W106 DC outbound dispatch integration for pickup and delivery data
- W250 supply chain control tower for real-time shipment visibility
- Carrier scorecard system linked to W44 vendor performance
- Cost analysis module for rate benchmarking per lane
- W304 routing/carrier master for performance history

### Pain Points / Risks

- **Carrier consolidation in Philippines**: limited number of reliable trucking companies, especially for provincial routes (Mindanao, Visayas); over-reliance on few carriers creates vulnerability
- **Informal carrier practices**: some Philippine carriers operate informally with inconsistent documentation, making performance tracking difficult
- **Seasonal capacity shortages": during peak periods (Christmas, back-to-school), carrier availability drops and rates increase; Logistics Manager must secure capacity early
- **Subjective damage claims**: distinguishing carrier-caused damage from inadequate packaging or DC loading errors is frequently disputed, delaying resolution per W500

### Staffing Implication

Logistics Manager: ~1-1.5 hours/day on carrier monitoring and allocation. Import Coordinator: ~15-20 min/day on freight forwarder tracking. Absorbed within existing team. No incremental headcount.

### Time Estimate

**Total daily**: ~60-90 min (20-30 min dashboard + 15-30 min breach investigation + 20-30 min allocation + 15-20 min import monitoring). **Weekly summary**: 1-2 hours.

---

## W728. Port & Customs Clearance Daily Status Tracking & Escalation

| Field | Detail |
|---|---|
| **Trigger** | Start of supply chain operations day; or customs/broker status update |
| **Frequency** | Daily review; real-time status updates from customs broker |
| **Volume** | ~400-600 TEUs/month import containers; ~15-25 containers in clearance pipeline at any time |
| **Owner** | Import Coordinator |
| **Participants** | Customs Broker, Logistics Manager, Finance (LC/duty payments), Warehouse Manager |

### Background

W144 covers international logistics and import operations at the strategic level. W464 covers in-house customs brokerage operations. W249 covers port demurrage management. This workflow addresses the daily operational tracking of import containers through the Philippine Bureau of Customs (BOC) clearance process — the critical path for ~40% of BuildRight's COGS. Philippine port clearance is notoriously complex (average 5-10 days from vessel arrival to gate-out) with multiple handoff points (discharge → customs examination → assessment → payment → release → haulage). Daily status tracking enables early identification of bottlenecks and proactive escalation to prevent demurrage and stockouts.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Morning import pipeline status review**: Import Coordinator reviews import pipeline dashboard: (a) vessels expected to arrive in next 7 days: vessel name, ETA, number of BuildRight containers, port of discharge (Manila South Harbor, Manila North Harbor, Cebu, Davao, Clark); (b) containers currently at port: days since vessel arrival, current clearance status (discharged, under customs examination, assessed, payment pending, released for haulage, gated out); (c) containers in transit to DC: estimated arrival at DC per W250 tracking; (d) containers exceeding standard clearance timeline (>7 days from discharge): flag as potential demurrage risk per W249 | Import Coordinator | Logistics Manager | 20-30 min/day |
| 2 | **Customs broker status update**: Import Coordinator obtains daily status from customs broker: (a) for each container in clearance pipeline: (i) current status and next step; (ii) expected timeline for next milestone; (iii) any issues: missing documentation, customs hold, examination required, assessment dispute, BOC system downtime; (b) for containers requiring customs examination: (i) examination type: green lane (no exam), yellow lane (document exam), red lane (physical exam); (ii) red lane: coordinate with broker for examination scheduling, prepare supporting documentation; (iii) estimate additional clearance time for examinations; (c) document all status updates in tracking system with timestamps | Import Coordinator / Customs Broker | Logistics Manager | 15-30 min/day |
| 3 | **Escalation management**: for containers stuck at specific stages: (a) stuck at discharge (>2 days): contact shipping line for container availability; (b) stuck awaiting customs examination (>3 days): escalate to broker for examination scheduling; contact BOC if broker unable to resolve; (c) stuck at assessment (>2 days): verify all documentation submitted; escalate duty assessment disputes per W239; (d) stuck at payment: coordinate with Finance for immediate duty payment via IPAY/Pass5 per W239 step 1; (e) stuck at release (>1 day after payment): escalate to broker for gate-out coordination; (f) for each escalation: document actions taken and timeline for resolution | Import Coordinator | Logistics Manager | 15-30 min/day |
| 4 | **Supply chain impact assessment**: Import Coordinator communicates clearance timeline impact: (a) for containers carrying critical stock (A-items, promotional items per W57): notify Supply Chain Planner of expected DC receipt date; (b) assess impact on store replenishment: will clearance delays cause stockouts at stores?; (c) for promotional items: alert Merchandising if promotional launch per W13 may be affected by delayed import receipt; (d) for seasonal items per W32: assess whether seasonal buy will arrive in time for seasonal window | Import Coordinator / Supply Chain Planner | VP Supply Chain | 10-15 min/day |
| 5 | **Demurrage and storage cost monitoring**: daily, Import Coordinator tracks cost exposure: (a) containers exceeding free time at port (typically 5-7 days free, then PHP 5,000-8,000/day demurrage): calculate daily cost exposure; (b) total monthly demurrage cost vs. budget; (c) identify root causes of demurrage incidents: documentation delays, customs holds, payment delays, carrier no-show for haulage; (d) demurrage cost data feeds into W680 supply chain cost analysis | Import Coordinator | Finance Manager | 10 min/day |

### System Touchpoints

- Import container tracking system with BOC status integration
- Customs broker communication portal with status update workflow
- Shipping line tracking integration for vessel ETA and container availability
- W250 supply chain control tower for in-transit visibility
- W249 demurrage management for cost tracking
- Finance integration for duty payment processing per W239
- Supply chain planning module for stock impact assessment
- W680 supply chain cost analysis for demurrage cost analytics

### Pain Points / Risks

- **BOC system downtime**: the Bureau of Customs electronic system (e2m) frequently experiences downtime, halting the entire clearance process with no workaround; BuildRight has no control over this
- **Red lane examination randomness**: BOC randomly selects containers for physical examination (red lane), adding 3-7 days to clearance time unpredictably; cannot be anticipated in supply planning
- **Port congestion**: Manila ports (South Harbor, North Harbor) regularly experience congestion, especially during peak import seasons (pre-Christmas, pre-back-to-school), extending vessel waiting time to 3-5 days before discharge
- **Customs broker capacity constraints**: during peak periods, customs brokers are overloaded with multiple clients, slowing document processing and examination coordination for BuildRight containers
- **Document accuracy dependency**: a single error in customs documentation (wrong HS code, missing certificate of origin, incorrect declared value) can trigger examination, assessment dispute, or rejection, adding 5-15 days to clearance

### Staffing Implication

Import Coordinator: ~1-2 hours/day on import pipeline tracking. Customs Broker: external service, cost absorbed in brokerage fees. Finance: ~15-30 min/day on duty payment processing. Absorbed within existing team. No incremental headcount.

### Time Estimate

**Total daily**: ~60-90 min (20-30 min pipeline review + 15-30 min broker update + 15-30 min escalation + 10-15 min impact assessment + 10 min demurrage tracking).

---

## W729. Supply Chain Disruption Rapid Response & Escalation Protocol

| Field | Detail |
|---|---|
| **Trigger** | Major supply disruption: supplier force majeure, port closure, natural disaster, geopolitical event, critical quality failure, carrier strike, or any event threatening >10% of planned supply |
| **Frequency** | Ad-hoc (2-4 significant disruptions per year) |
| **Volume** | Each disruption potentially affecting 100-1,000 SKUs across multiple categories |
| **Owner** | VP Supply Chain |
| **Participants** | Supply Chain Planner, Category Manager, Procurement Manager, Logistics Manager, VP Merchandising, CFO |

### Background

W558 covers supply chain risk assessment and contingency planning at the strategic level. This workflow addresses the operational rapid response when a disruption actually occurs — the critical first 24-72 hours when decisions must be made quickly to minimize stockout impact on 200 stores. Philippine supply chains face frequent disruptions: typhoons closing ports and roads, volcanic activity affecting Central Luzon, port strikes, supplier bankruptcies, global shipping disruptions (Suez Canal, Red Sea), and pandemic-related restrictions. With 35,000 active SKUs and ~40% import dependency, a major disruption can cascade quickly through the supply chain.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Disruption identification and initial assessment** (within 2 hours): (a) disruption alert received from: customs broker, supplier, carrier, news monitoring, or supply chain control tower per W250; (b) Supply Chain Planner conducts rapid impact assessment: (i) which suppliers/POs/shipments are affected?; (ii) estimated duration of disruption; (iii) which SKUs and categories are at risk?; (iv) current inventory position: weeks of supply for affected SKUs at DC and store level; (v) impact severity: Critical (>100 SKUs, A-items, promotional items), Major (50-100 SKUs, B-items), Moderate (<50 SKUs, C-items); (c) escalate to VP Supply Chain with initial assessment | Supply Chain Planner | VP Supply Chain | 1-2 hours |
| 2 | **Cross-functional response team activation** (within 4 hours): VP Supply Chain activates response team: (a) participants: Supply Chain Planner, affected Category Manager(s), Procurement Manager, Logistics Manager, Finance representative; (b) for Critical disruptions: include VP Merchandising and CFO; (c) initial war room meeting (virtual or physical): (i) review initial assessment; (ii) align on disruption severity and response level; (iii) assign action items with owners and deadlines; (iv) establish communication cadence: daily standups until resolved | VP Supply Chain | — | 1 hour |
| 3 | **Inventory triage and allocation** (within 8 hours): Supply Chain Planner executes inventory triage: (a) for each affected SKU: calculate days of supply remaining at DC level; (b) classify affected SKUs by urgency: (i) Red (<1 week supply): immediate action required; (ii) Amber (1-2 weeks supply): alternative sourcing within 2 weeks; (iii) Green (>2 weeks supply): monitor only; (c) for Red SKUs: implement emergency allocation per W105: prioritize allocation to top-performing stores and B2B key accounts; (d) activate demand reduction: (i) reduce ecommerce ATP for affected SKUs; (ii) notify Category Manager to pause promotional plans for affected items; (iii) notify Store Operations to manage customer expectations for product availability | Supply Chain Planner | VP Supply Chain | 2-4 hours |
| 4 | **Alternative sourcing activation** (within 24 hours): Procurement Manager activates alternative sourcing: (a) identify alternative suppliers for affected SKUs from pre-qualified vendor list per W670 (emergency onboarding); (b) for import-dependent items: check if local suppliers can provide temporary supply; (c) for single-source items: activate emergency procurement from secondary markets (regional distributors, spot market); (d) evaluate cost impact of alternative sourcing (spot pricing typically 10-30% above contract pricing); (e) obtain VP Merchandising approval for any product substitution or quality deviation per W279 (substitution rules); (f) place emergency POs per W60 with expedited logistics | Procurement Manager | VP Supply Chain / VP Merchandising | 4-8 hours |
| 5 | **Customer and store communication** (within 24-48 hours): (a) for stores: communicate affected SKUs, expected outage duration, substitute products, and customer messaging per W571; (b) for ecommerce: update product availability on website; if item is BOPIS-listed, show "Temporarily Unavailable" or offer alternative per W536; (c) for B2B key accounts: proactive outreach from Trade Sales per W617 with inventory status and alternative product recommendations; (d) for promotional items: coordinate with Marketing per W83 on promotional plan adjustment or substitution | Category Manager / Ecommerce Ops Mgr / Trade Sales | VP Merchandising | 2-4 hours |
| 6 | **Daily disruption status tracking** (until resolution): VP Supply Chain conducts daily disruption standup: (a) update on disruption status: is it worsening, stable, or resolving?; (b) inventory position update: days of supply trend for affected SKUs; (c) alternative sourcing progress: PO status, expected delivery dates; (d) financial impact estimate: lost sales, expedited freight cost, alternative sourcing premium; (e) adjust response actions based on evolving situation; (f) document all decisions and rationale for post-disruption review | VP Supply Chain | CFO | 30-60 min/day |
| 7 | **Post-disruption review** (within 2 weeks of resolution): VP Supply Chain conducts post-disruption review: (a) timeline reconstruction: what happened, when, and how did BuildRight respond?; (b) effectiveness assessment: how quickly was the disruption detected? How effective was the response? What was the financial impact?; (c) lessons learned: what worked well, what could be improved?; (d) action items for risk mitigation: update contingency plans per W558, qualify additional alternative suppliers, adjust safety stock levels for vulnerable SKUs; (e) update supply chain risk register per W626; (f) report to COO and CFO | VP Supply Chain | COO | 1-2 days |

### System Touchpoints

- Supply chain control tower per W250 for real-time disruption detection
- Inventory visibility across all locations per INV-002
- ABC classification per INV-004 for SKU prioritization
- W105 multi-channel inventory allocation for emergency allocation
- W60 emergency procurement for rapid PO creation
- W670 supplier emergency onboarding for alternative vendor activation
- W279 product substitution rules for substitute product authorization
- W571 store communication for store-level disruption messaging
- Financial impact tracking for lost sales and expedited cost documentation

### Pain Points / Risks

- **Speed vs. accuracy trade-off**: rapid response requires making decisions with incomplete information; wrong assessments can lead to over-reaction (expensive unnecessary alternative sourcing) or under-reaction (stockouts)
- **Alternative supplier quality risk**: emergency suppliers activated per W670 may not meet BuildRight's standard quality requirements; customers receiving substitute products may notice quality differences
- **Cost escalation**: emergency procurement, expedited freight, and spot-market pricing can increase COGS by 15-30% for affected items, eroding margins
- **Cascading disruption effects**: a disruption affecting one supplier or port can cascade through the supply chain: affected SKUs out of stock → customers buy alternatives → alternative SKUs run low → further stockouts
- **Communication lag to stores**: with 200 stores across the archipelago, ensuring all store managers receive and act on disruption communications within 24 hours is challenging

### Staffing Implication

Ad-hoc (2-4 times/year). Each disruption response requires 10-30 person-days of concentrated effort over 2-4 weeks. VP Supply Chain: 1-2 hours/day during disruption. Supply Chain Planner: 4-6 hours/day during active response. Procurement Manager: 4-8 hours for alternative sourcing. Category Managers: 2-4 hours for product decisions. Absorbed by existing team with reprioritization. No incremental headcount.

### Time Estimate

**Initial response (first 24 hours)**: 8-16 hours across the team. **Daily tracking**: 30-60 min/day. **Post-disruption review**: 1-2 days. Total disruption lifecycle: typically 2-4 weeks from detection to full resolution.

---

## W762. Carrier Performance Weekly Review & Freight Rate Benchmarking

| Field | Detail |
|---|---|
| **Trigger** | Weekly carrier performance review schedule |
| **Frequency** | Weekly |
| **Volume** | ~15–20 active carriers (own fleet + 3PL partners) |
| **Owner** | Logistics Manager |
| **Participants** | Logistics Manager, Procurement (W62B 3PL onboarding), Finance (W277 freight bill audit), VP Supply Chain |

### Background
BuildRight Depot relies on a mix of owned fleet (7 trucks per DC × 4 DCs = 28 trucks) and third-party carriers (3PL partners) to move merchandise from DCs to 200 stores. Weekly carrier performance review ensures delivery SLA compliance, identifies cost optimization opportunities through freight rate benchmarking, and maintains carrier accountability for the ~20,000 store deliveries per month.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Weekly data compilation — System compiles carrier performance data for the past week: (a) on-time delivery rate (delivery within scheduled window), (b) transit time vs. standard, (c) damage rate (W500), (d) delivery exception rate (refused, short-shipped, wrong store), (e) cost per delivery vs. budget | System | — | Automated |
| 2 | Carrier scorecard generation — System generates weekly scorecard per carrier: KPI performance, trend vs. prior 4 weeks, SLA compliance status (Green/Amber/Red), and cost variance | System | — | Automated |
| 3 | Performance review — Logistics Manager reviews scorecards; identifies: (a) carriers below SLA threshold, (b) cost outliers, (c) emerging trends (declining performance, increasing damage) | Logistics Manager | VP Supply Chain | 1 hour |
| 4 | Carrier escalation — For Amber/Red carriers: Logistics Manager contacts carrier account manager; documents performance concerns; agrees on corrective action plan with timeline; follows up next week | Logistics Manager | Carrier Account Manager | 30 min per carrier |
| 5 | Freight rate benchmarking — Monthly: Logistics Manager benchmarks carrier rates against: (a) market rates from industry sources, (b) alternative carrier quotes, (c) internal fleet cost per kilogram; identifies rate renegotiation opportunities | Logistics Manager | Procurement | 4 hours/month |
| 6 | Rate renegotiation — For carriers with rates above benchmark: Logistics Manager initiates rate renegotiation with Procurement support (W62B); presents data-driven proposal with alternative carrier options | Logistics Manager | Procurement Manager | Per W62B |
| 7 | Carrier rotation optimization — Based on performance and cost data: Logistics Manager adjusts carrier allocation — awarding more volume to high-performing, cost-effective carriers and reducing volume to underperformers | Logistics Manager | VP Supply Chain | 2 hours/month |
| 8 | Monthly executive report — Logistics Manager presents carrier performance summary to VP Supply Chain: overall delivery performance, cost per delivery trend, carrier portfolio health, and recommended actions | Logistics Manager | VP Supply Chain | 2 hours/month |

### System Touchpoints
- Carrier performance data warehouse: delivery records, transit times, damage claims, exception logs
- Automated scorecard generation with configurable KPI thresholds
- W277 freight bill audit — cost data source
- W500 transfer order damage claims — damage data source
- W62B 3PL onboarding/offboarding — carrier lifecycle management
- W199 fleet telematics — own fleet performance data
- W242 3PL performance review — quarterly strategic review integration
- Freight rate benchmarking module with market rate API integration

### Pain Points / Risks
- Carrier data quality — 3PL carriers may provide incomplete or delayed delivery data; real-time tracking (W199/W250) mitigates but requires carrier technology investment
- Market rate volatility — fuel price surges (W198) and seasonal demand (Ber months) make benchmarking a moving target
- Carrier concentration risk — over-reliance on a single high-performing carrier creates vulnerability if that carrier experiences disruption
- Own fleet vs. 3PL cost comparison — internal fleet costs (depreciation, driver wages, fuel, maintenance) must be fully loaded to enable fair comparison with 3PL rates
- Renegotiation cycle time — carrier rate renegotiations may take 2–3 months; during this period, BuildRight pays above-market rates

### Time Estimate
Weekly review: 1 hour. Monthly benchmarking: 4 hours. Monthly report: 2 hours. Carrier escalation: 30 min × 2–3 carriers = ~1.5 hours/week. Total monthly: ~15 hours.

### Staffing Implication
Absorbed within existing Logistics Manager role. 1 Logistics Manager per DC (4 DCs) conducts weekly review for their carrier portfolio. No incremental headcount.

---

## W763. Supply Chain Vendor Diversification & Alternative Sourcing Maintenance

| Field | Detail |
|---|---|
| **Trigger** | Annual category sourcing review; or supply disruption event (W558) |
| **Frequency** | Annual comprehensive review; quarterly updates; ad-hoc during disruptions |
| **Volume** | ~50 critical categories requiring diversification plans |
| **Owner** | Procurement Manager (Strategic Sourcing) |
| **Participants** | Category Manager, Procurement Manager, Quality (W150), Logistics Manager, VP Supply Chain |

### Background
BuildRight Depot's 35,000 SKUs include critical categories where supply concentration creates risk: cement (2–3 dominant suppliers), steel (import-dependent), lumber (limited domestic sources), and electrical supplies. Supply chain disruptions from typhoons, import delays, and vendor financial distress (W491) expose BuildRight to stockout risk. This workflow maintains vendor diversification plans and alternative sourcing readiness for critical categories.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Category criticality assessment — Annual: Procurement Manager classifies all categories by supply risk: (a) Critical — single/dual source, high revenue, long lead time, (b) Important — limited sources, moderate revenue, (c) Standard — multiple sources, short lead time | Procurement Manager | VP Supply Chain | 2 days/year |
| 2 | Concentration risk scoring — For each Critical category: system calculates vendor concentration using Herfindahl-Hirschman Index (HHI); flags categories where top vendor supplies > 60% of volume | System | — | Automated |
| 3 | Alternative vendor identification — For high-concentration categories: Procurement Manager identifies 2–3 alternative vendors through: (a) industry trade shows, (b) competitor intelligence (W130), (c) PH vendor directories, (d) international sourcing for import-eligible categories | Procurement Manager | Category Manager | 2 days/quarter |
| 4 | Alternative vendor qualification — Each alternative vendor undergoes abbreviated qualification: (a) W36 vendor onboarding (financial review, TIN verification), (b) W625 product quality testing (sample evaluation), (c) W620 site visit (factory/warehouse inspection) | Procurement Manager | Quality Team | Per W36/W625 |
| 5 | Trial order execution — Place trial order with alternative vendor: 5–10% of category volume; monitor delivery performance, quality, and cost vs. incumbent | Procurement Manager | Logistics Manager | Per W2 |
| 6 | Dual-sourcing implementation — If trial successful: establish dual-sourcing agreement with volume split (e.g., 70/30 incumbent/alternative); system configures split allocation in W312 planning parameters | Procurement Manager | Category Manager | 1 day |
| 7 | Quarterly diversification review — Quarterly: Procurement Manager reviews diversification status per category: concentration score, alternative vendor readiness, trial results, and recommended volume adjustments | Procurement Manager | VP Supply Chain | 4 hours/quarter |
| 8 | Disruption activation — When supply disruption occurs (W558): Procurement Manager activates alternative vendor from diversification plan; issues emergency PO (W60); system adjusts replenishment parameters to redirect volume | Procurement Manager | VP Supply Chain | Per W558 |

### System Touchpoints
- Category vendor concentration dashboard with HHI calculation
- W36 vendor onboarding — alternative vendor qualification workflow
- W44 vendor scorecard — alternative vendor performance tracking
- W625 product quality testing — sample evaluation tracking
- W312 replenishment parameters — dual-source allocation configuration
- W558 supplier risk assessment — risk data integration
- W60 emergency procurement — disruption activation workflow
- W491 supplier financial health — vendor viability monitoring
- W680 supply chain cost analysis — dual-sourcing cost comparison

### Pain Points / Risks
- Incumbent vendor resistance — existing vendors may resist volume reduction; must be managed diplomatically through JBP (W155) discussions
- Alternative vendor quality risk — new vendors may not meet BuildRight quality standards during initial trials; customer-facing quality issues damage brand
- Minimum order quantity constraints — alternative vendors may require higher MOQs than BuildRight's trial volume, making qualification uneconomical
- Philippine market limitations — some categories genuinely have limited domestic supply options; diversification may require import sourcing with longer lead times
- Dual-sourcing complexity — managing two vendors per category increases procurement administration, quality testing, and logistics coordination overhead

### Time Estimate
Annual assessment: 2 days. Quarterly review: 4 hours. Alternative vendor identification: 2 days/quarter. Trial order management: absorbed in W2. Total annual: ~120 hours.

### Staffing Implication
Absorbed within existing Procurement Manager and Category Manager roles. 1 Procurement Manager (Strategic Sourcing) oversees diversification program across all critical categories. No incremental headcount.

---

## W786. DC-to-Store Delivery Route Optimization & Multi-Stop Planning

| Field | Detail |
|---|---|
| **Trigger** | Daily dispatch planning cycle; or weekly route optimization review |
| **Frequency** | Daily route planning; weekly optimization review |
| **Volume** | 4 DCs × ~15-25 delivery routes per DC per day × ~2-3 stores per route = ~60-100 route plans/day |
| **Owner** | Logistics Planner |
| **Participants** | Logistics Planner, DC Dispatcher, Fleet Manager, 3PL Carrier Coordinator |

### Background
BuildRight Depot's 4 DCs serve 200 stores with 2-3 deliveries per store per week (~5,000 replenishment orders/month per W4). Each delivery truck typically serves 2-3 stores on a multi-stop route. Route planning directly impacts: delivery cost per store (fuel, driver hours, truck utilization), on-time delivery rate (target ≥ 95% per W44), and DC-to-store lead time (target 1-3 days). While W196 covers route planning at the governance level and W52 covers fleet management, this workflow manages the daily operational route optimization — balancing delivery SLAs, truck capacity, store time windows, and route efficiency.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Daily order-to-store assignment**: System groups approved transfer orders by delivery date and DC: (a) priority orders (perishable, promotional stock per W57, emergency per W596), (b) standard replenishment orders, (c) store delivery time windows (7AM-5PM standard; some LGU truck ban restrictions per W431) | System | Logistics Planner | Automated |
| 2 | **Route optimization run**: Logistics Planner runs route optimization: (a) inputs: store locations per W310 geographic master, order volumes per store (cubic meters, weight), truck capacity (6-wheeler: 5 tons / 20 CBM; 10-wheeler: 10 tons / 40 CBM), delivery time windows, LGU truck ban hours per W431, traffic pattern data; (b) constraints: max 8-hour route duration, max 3 stops per route (for manageable unloading time), refrigerated/hazmat items on compliant trucks per W699; (c) outputs: optimized route plans minimizing total distance and time | Logistics Planner | — | 30-60 min |
| 3 | **Route plan review and adjustment**: Logistics Planner reviews system-generated routes: (a) verify priority orders on earliest routes, (b) balance loads across available trucks (owned per W52 + 3PL per W242), (c) adjust for known road closures or construction, (d) confirm driver availability per W654 certification, (e) finalize dispatch sequence | Logistics Planner | DC Ops Manager | 30 min |
| 4 | **Driver and carrier assignment**: DC Dispatcher assigns: (a) owned fleet drivers per W197 driver management, (b) 3PL carriers per W242 contract and W727 daily performance, (c) provide driver with: route plan, store contact numbers, delivery documents (manifest, transfer orders), GPS device per W199 telematics | DC Dispatcher | — | 30 min |
| 5 | **Real-time route monitoring**: Throughout delivery day: (a) Logistics Planner monitors fleet via telematics per W199, (b) tracks on-time delivery vs. planned schedule, (c) reroutes for traffic incidents or road closures, (d) communicates delays to receiving stores per W708 | Logistics Planner | — | Continuous during delivery hours |
| 6 | **Delivery completion reconciliation**: End of delivery day: (a) system reconciles planned vs. actual deliveries per route, (b) records on-time delivery rate, (c) captures store receipt confirmations per W109, (d) logs route exceptions (missed deliveries, access issues, partial deliveries) | System | Logistics Planner | 15 min |
| 7 | **Weekly route optimization review**: Logistics Planner analyzes: (a) average stops per route, (b) average delivery time per stop, (c) truck utilization rate (target ≥ 85%), (d) on-time delivery rate by route and carrier, (e) fuel consumption per delivery per W198, (f) route efficiency improvement opportunities (store clustering, time window optimization) | Logistics Planner | Fleet Manager | 2 hours/week |

### System Touchpoints

- Route optimization engine — multi-stop route planning with constraints
- W196 route planning & dispatch optimization — governance level
- W52 fleet management — truck availability and maintenance status
- W199 fleet telematics — GPS tracking and real-time monitoring
- W197 driver performance — driver availability and certification
- W198 fuel management — fuel consumption tracking
- W431 LGU truck ban — time window constraints
- W242 3PL performance review — 3PL carrier availability
- W727 carrier performance monitoring — carrier scorecard
- W109 store inventory receiving — delivery receipt confirmation
- W310 geographic hierarchy master — store location data

### Pain Points / Risks

- LGU truck ban complexity — different cities/municipalities have different truck ban hours per W431; route planning must account for jurisdiction boundaries
- Philippine traffic unpredictability — Manila/Cebu traffic can double planned delivery times; real-time rerouting capability essential
- Multi-stop unloading time — each store stop takes 30-60 minutes for unloading and goods receipt; underestimated unloading time delays subsequent stops
- Truck capacity constraints — oversized items (lumber, plywood sheets) consume disproportionate truck space; cubic capacity often constrains before weight
- 3PL reliability — 80% of trucks are third-party per model company profile; 3PL no-shows disrupt route plans; backup carrier contracts per W242 essential

### Time Estimate

Daily: route optimization (30-60 min) + review (30 min) + assignment (30 min) + monitoring (continuous) + reconciliation (15 min) = ~2-3 hours focused time. Weekly review: 2 hours.

### Staffing Implication

Absorbed within existing Logistics Planner and DC Dispatcher roles. Daily: ~2-3 hours per DC. No incremental headcount.

---

## W835. Store-Level Replenishment Forecast Accuracy Review & Parameter Tuning

| Field | Detail |
|---|---|
| **Trigger** | Monthly replenishment review cycle; store-level stock-out rate exceeds 3% or overstock rate exceeds 5% |
| **Frequency** | Monthly per store cluster; weekly for problem stores |
| **Volume** | 200 stores reviewed monthly; ~20-30 stores flagged for parameter tuning |
| **Owner** | Supply Planning Analyst |
| **Participants** | Supply Planning Analyst, Store Manager, Merchandise Planner, DC Operations Manager |

### Background

W312 covers replenishment parameter master governance and W596 covers store-level replenishment exception management. However, neither covers the periodic review of forecast accuracy at the store level — comparing predicted demand (which drives auto-replenishment per W2A) against actual sell-through, and adjusting planning parameters (safety stock, ROP, EOQ, lead time) accordingly. With ~7.2 million SKU-location parameter sets (35,000 SKUs × 205 locations) driving auto-replenishment, parameter drift over time leads to systematic stock-outs or overstock. Philippine retail demand patterns are particularly volatile: typhoon-driven surges (W576), payday peaks (W578), seasonal swings (W32), and local events (fiestas, LGU construction projects). Monthly accuracy review ensures parameters stay calibrated.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Monthly forecast accuracy report generation**: Supply Planning Analyst generates report per store cluster: (a) forecast vs. actual demand by SKU category; (b) MAPE (Mean Absolute Percentage Error) by store and category; (c) stock-out incidents per store; (d) overstock indicators (inventory > 1.5× target weeks of supply); (e) fill rate by DC per store | System / Supply Planning Analyst | — | 2-3 hours |
| 2 | **Problem store identification**: identify stores with: (a) MAPE > 30% for any major category; (b) stock-out rate > 3%; (c) overstock rate > 5%; (d) abnormal demand patterns (sudden spikes or drops) | Supply Planning Analyst | Merchandise Planner | 1-2 hours |
| 3 | **Root cause analysis per problem store**: investigate: (a) seasonal/event — typhoon, fiesta, local construction project causing demand spike; (b) competitive — new competitor store opening nearby per W130; (c) assortment change — new products introduced per W564 cannibalizing existing SKU demand; (d) promotional impact — promo per W13 pulling forward demand creating post-promo trough; (e) parameter drift — ROP/SS/EOQ not adjusted for changed demand pattern | Supply Planning Analyst | Merchandise Planner | 1-2 hours per problem store |
| 4 | **Parameter tuning recommendations**: (a) adjust safety stock — increase for volatile categories, decrease for stable ones; (b) adjust ROP — recalculated based on updated average daily demand and lead time; (c) adjust EOQ — modify batch sizes based on updated demand; (d) adjust lead time — if DC-to-store delivery performance changed; (e) seasonal override — apply seasonal multipliers per W306 seasonal calendar for upcoming periods | Supply Planning Analyst | Merchandise Planner | 30-60 min per problem store |
| 5 | **Parameter change submission**: Supply Planning Analyst submits parameter change requests per W312 governance: (a) changes documented with justification; (b) Merchandise Planner approval for category-level changes; (c) system updates W312 parameters with effective date | Supply Planning Analyst | Merchandise Planner | 15-30 min per change batch |
| 6 | **Store Manager feedback loop**: (a) Supply Planning Analyst shares tuned parameters with Store Manager; (b) Store Manager provides ground-level demand intelligence (upcoming local events, construction projects, school semesters); (c) qualitative input incorporated into next forecast cycle per W31 | Supply Planning Analyst / Store Manager | Merchandise Planner | 30 min per problem store |
| 7 | **Monthly accuracy dashboard update**: (a) store cluster performance ranking; (b) improvement tracking for tuned stores; (c) benchmark against chain average; (d) top 10 most improved and most deteriorated stores | Supply Planning Analyst | VP Supply Chain | 2 hours |
| 8 | **Quarterly comprehensive calibration**: (a) full parameter recalculation for all A-items per W312; (b) annual calibration for B/C-items; (c) methodological review — is forecast model still appropriate for demand pattern | Supply Planning Analyst / Merchandise Planner | VP Supply Chain | 20-30 hours/quarter |

### System Touchpoints

- W31 demand forecasting for forecast generation and accuracy measurement
- W2A auto-replenishment for parameter-driven replenishment execution
- W312 replenishment parameters for parameter governance and updates
- W596 replenishment exceptions for exception-driven flagging
- W32 seasonal planning for seasonal demand pattern integration
- W306 seasonal calendar for seasonal multiplier application
- W13 promotions for promotional demand impact analysis
- W564 new product introduction for assortment change tracking
- W130 competitor intelligence for competitive impact assessment
- W106 DC dispatch for delivery performance data
- W4 store replenishment for replenishment order generation
- W102 category performance for category-level accuracy benchmarking
- W584 DC daily operations for DC fill rate data

### Pain Points / Risks

- **Parameter change governance bureaucracy**: W312 governance may require multiple approvals for parameter changes, slowing response to rapidly changing demand patterns
- **Insufficient demand history for new stores**: stores open less than 6 months lack sufficient historical data for accurate forecasting; parameter tuning relies heavily on planner judgment
- **Demand volatility from external events**: typhoons, COVID lockdowns, and economic shifts create demand patterns that no forecast model can predict, making parameter tuning reactive rather than proactive
- **Balancing overstock and stock-out costs**: reducing safety stock lowers carrying cost but increases stock-out risk; the optimal balance is difficult to calculate and varies by category and store
- **Parameter change lag effect**: parameter changes take 2-4 weeks to show measurable impact on stock-out and overstock rates, making it difficult to assess tuning effectiveness quickly

### Staffing Implication

Absorbed by Supply Planning Analyst team; ~40-60 hours/month. Supply Planning Analysts: ~30-40 hours/month on reviews, analysis, and tuning. Merchandise Planners: ~5-10 hours/month on approval decisions. Store Managers: ~30 min per problem store on feedback. No incremental headcount.

### Time Estimate

Per store review: 30-60 min. Per month: 200 stores reviewed (mostly automated flagging) + 20-30 problem stores deep-dive (1-2 hours each) = ~40-60 hours/month. Quarterly calibration: 20-30 hours.
