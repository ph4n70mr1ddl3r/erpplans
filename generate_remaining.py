#!/usr/bin/env python3
"""Append VS-56 through VS-68 to the ALL_VS list and regenerate."""

import os, sys

BASE = "/home/riddler/erpplans/01-model-company/workflows"

# Additional VS definitions (VS-56 to VS-68)
# Format: (VS_DIR, VS_NUM, VS_NAME, FAMILY, OVERVIEW, [PAs])
# PA: (PA_NUM, SLUG, TITLE, [WORKFLOWS])
# Workflow: (NAME, TRIGGER, FREQ, VOL, OWNER, PARTICIPANTS, [STEPS])
# Step: (ACTIVITY, ROLE_R, ROLE_A, DURATION)

EXTRA_VS = []

# ─── VS-56: Third-Party Delivery Partner Management ───
EXTRA_VS.append(("VS-56-third-party-delivery-partner", 56,
    "Third-Party Delivery Partner Management", "Make & Move",
    "Manages BuildRight's relationships with third-party logistics (3PL) partners for last-mile delivery, including Lalamove, Transportify, GrabExpress, and owned fleet coordination. Covers partner onboarding, performance monitoring, SLA management, settlement, and cost optimization. BuildRight uses 80% third-party trucks for DC-to-store and customer deliveries.",
    [("PA-56.1", "3pl-partner-onboarding-qualification", "3PL Partner Onboarding & Qualification", [
        ("Delivery Partner Identification & Screening", "Need for new delivery capacity or partner replacement", "Ad-hoc; typically 2–4 new partners/year", "~2–4 evaluations/year; ~10–15 active partners at any time", "Logistics Manager", "Logistics Mgr, Procurement, Legal, Finance",
         [("Logistics Manager identifies potential partners based on geographic coverage, vehicle fleet size, pricing, and reputation in Philippine logistics market", "Logistics Manager", "VP Supply Chain", "1–2 days"),
          ("Procurement conducts due diligence: business registration (DTI/SEC), insurance coverage, safety record, driver credentials, vehicle condition, reference checks", "Procurement", "Logistics Manager", "3–5 days"),
          ("Legal reviews contract: SLA terms, liability, insurance requirements, data privacy (RA 10173), rate card, payment terms, termination clauses", "Legal", "VP Legal", "2–3 days"),
          ("Finance evaluates pricing competitiveness vs. alternatives; approves rate card; sets up vendor master for payment", "Finance", "CFO", "1 day")]),
        ("3PL System Integration & Onboarding", "Contract signed with new delivery partner", "~2–4 integrations/year", "~2–4 integrations/year", "IT Integration Lead", "IT Integration, Logistics Mgr, 3PL Partner",
         [("IT configures API integration with 3PL: order push, delivery status pull, proof of delivery, driver tracking; tests in sandbox environment", "IT Integration Lead", "CIO", "5–10 days"),
          ("Logistics Manager trains partner on BuildRight processes: order acceptance, delivery windows, proof-of-delivery requirements, exception handling", "Logistics Manager", "3PL Partner", "1–2 days"),
          ("Pilot period: 2-week controlled rollout with 1 DC; monitors performance vs. SLA; full rollout upon meeting pilot criteria", "Logistics Manager", "VP Supply Chain", "2 weeks")]),
        ("Driver & Vehicle Compliance Verification", "Partner onboarding or annual re-certification", "Annual re-certification; onboarding as needed", "~200–300 drivers across all 3PL partners", "Logistics Coordinator", "Logistics Coord, 3PL Partner, Safety Officer",
         [("Logistics Coordinator verifies driver credentials: professional driver's license, drug test clearance, background check, BuildRight safety training completion", "Logistics Coordinator", "Logistics Manager", "2–3 days"),
          ("Coordinator verifies vehicle compliance: registration, insurance, roadworthiness, load capacity certification for heavy deliveries (cement, lumber, tiles)", "Logistics Coordinator", "Safety Officer", "1–2 days"),
          ("Annual re-certification: partners submit updated documents; non-compliant drivers/vehicles suspended until cleared", "Logistics Coordinator", "Logistics Manager", "1–2 weeks")]),
        ("3PL Rate Card Negotiation & Renewal", "Annual rate card review or significant cost change", "Annual review; ad-hoc for fuel price changes", "~10–15 rate cards to manage", "Logistics Manager", "Logistics Mgr, Procurement, Finance, 3PL Partner",
         [("Logistics Manager analyzes current spend, delivery volume, and market rates; benchmarks vs. Lalamove/Transportify spot rates and competitor logistics costs", "Logistics Manager", "Procurement", "2–3 days"),
          ("Manager negotiates rates: base per-km rate, weight surcharges, waiting time charges, multi-drop discounts, peak season surcharges", "Logistics Manager", "3PL Partner", "1–2 days"),
          ("Finance validates cost impact; approves or requests further negotiation; updated rate card configured in ERP", "Finance", "CFO", "1 day")]),
        ("3PL Insurance & Liability Management", "Insurance renewal or incident requiring claim", "Annual renewal; ad-hoc for incidents", "~10–15 partner insurance policies to track", "Logistics Manager", "Logistics Mgr, Legal, Finance, Insurance Provider",
         [("Logistics Manager ensures all 3PL partners maintain required insurance: comprehensive vehicle, cargo, and third-party liability; tracks policy expiry dates", "Logistics Manager", "Legal", "2–3 hours/quarter"),
          ("For delivery incidents (damage, loss, accident): Manager files claim with partner's insurer; coordinates with VS-50 for damage documentation", "Logistics Manager", "Legal", "2–4 hours/incident"),
          ("Annual: reviews insurance adequacy; adjusts coverage based on claims history and delivery volume growth", "Logistics Manager / Finance", "CFO", "1 day/year")]),
        ("3PL Capacity Planning & Allocation", "Seasonal capacity review or new store openings", "Quarterly review; ad-hoc for openings", "4 DCs serving 200 stores; ~10,000 deliveries/month", "Logistics Manager", "Logistics Mgr, DC Operations, Store Ops, 3PL Partners",
         [("Logistics Manager forecasts delivery capacity needs: seasonal peaks (holiday, summer), new store openings (~10–15/year), DC-to-store replenishment volume", "Logistics Manager", "VP Supply Chain", "2–3 days/quarter"),
          ("Manager allocates delivery volume across partners based on: capacity, performance score, geographic coverage, cost; ensures no single partner >50% of volume", "Logistics Manager", "VP Supply Chain", "1–2 days"),
          ("Coordinates surge capacity for peak periods: pre-books additional vehicles, arranges temporary partner agreements, adjusts DC scheduling", "Logistics Manager", "DC Operations", "1 week")]),
        ("3PL Partner Performance Scorecard", "Monthly performance review cycle", "Monthly", "~10–15 partner scorecards/month", "Logistics Manager", "Logistics Mgr, DC Operations, Store Ops, VP Supply Chain",
         [("System generates monthly scorecard per partner: (a) on-time delivery rate (target ≥95%), (b) delivery damage rate (target <0.5%), (c) order acceptance rate, (d) average delivery time, (e) customer complaint rate, (f) driver professionalism score", "System", "Logistics Manager", "Automated"),
          ("Logistics Manager reviews scorecards with each partner; discusses improvement areas; sets 30-day corrective action plans for below-target partners", "Logistics Manager", "3PL Partner", "1–2 hours/partner"),
          ("Quarterly: VP Supply Chain reviews portfolio performance; decisions on partner retention, volume reallocation, or new partner sourcing", "VP Supply Chain", "COO", "2–3 hours")]),
        ("3PL Contract Termination & Transition", "Partner underperformance or strategic decision", "Ad-hoc; ~1–2 terminations/year", "~1–2 transitions/year", "Logistics Manager", "Logistics Mgr, Legal, Procurement, IT, 3PL Partners",
         [("Logistics Manager initiates termination per contract terms: provides required notice period (typically 60–90 days); documents performance justification", "Logistics Manager", "VP Supply Chain", "1–2 days"),
          ("Procurement sources replacement partner; IT begins integration; Logistics Manager plans volume transition to minimize delivery disruption", "Procurement / IT", "Logistics Manager", "30–60 days"),
          ("Manager executes transition: redirects delivery volume to replacement partner over 2–4 weeks; closes financial settlement with departing partner", "Logistics Manager", "Finance", "2–4 weeks")])
    ]),
    ("PA-56.2", "delivery-performance-sla", "Delivery Performance & SLA Management", [
        ("Real-Time Delivery Tracking & Monitoring", "Active deliveries in progress", "Continuous; ~10,000 deliveries/month", "~400–500 deliveries/day across 4 DCs", "Logistics Coordinator", "Logistics Coord, DC Dispatch, Store Receiving",
         [("System tracks all 3PL deliveries in real-time: driver location, estimated arrival, delivery status (dispatched/in-transit/delivered/failed)", "System", "Logistics Coordinator", "Real-time"),
          ("Coordinator monitors delivery exceptions: delays >30 minutes, driver no-show, route deviations, vehicle breakdown; coordinates corrective action", "Logistics Coordinator", "Logistics Manager", "Continuous"),
          ("System auto-alerts store of delivery ETA (SMS/app notification); store confirms receipt; exceptions escalated to Logistics Manager", "System", "Store Manager", "Automated")]),
        ("SLA Compliance Monitoring", "Daily SLA report generation", "Daily", "~10,000 deliveries/month; SLA: DC-to-store 1–3 days", "Logistics Coordinator", "Logistics Coord, Logistics Mgr, VP Supply Chain",
         [("System calculates daily SLA compliance: % of deliveries within promised window; tracks by partner, DC, route, and store", "System", "Logistics Coordinator", "Automated"),
          ("Coordinator investigates SLA breaches: root cause (traffic, weather, partner capacity, DC dispatch delay); implements corrective measures", "Logistics Coordinator", "Logistics Manager", "1–2 hours/day")]),
        ("Customer Home Delivery SLA Management", "Ecommerce home delivery orders (~17,200/month)", "Daily; 2–5 business day SLA", "~17,200 home deliveries/month", "Ecommerce Logistics Coordinator", "Ecom Logistics Coord, 3PL Partner, Customer Service",
         [("System assigns home delivery to optimal partner based on: delivery location, package size/weight, partner availability, cost; tracks against 2–5 day SLA", "System", "Ecom Logistics Coord", "Automated"),
          ("Coordinator monitors next-day SLA for Metro Manila and 3–5 day for provincial; proactively contacts customers for delayed deliveries", "Ecom Logistics Coord", "Customer Service", "2–3 hours/day"),
          ("Failed deliveries (customer not available, wrong address): rescheduled within 24 hours; 3 failed attempts → order cancelled, refund per VS-32", "Ecom Logistics Coord", "Customer Service", "15 min/case")]),
        ("Delivery Quality Inspection", "Store receives delivery from 3PL", "~10,000 deliveries/month", "~400–500/day", "Store Receiving Clerk", "Receiving Clerk, Store Manager, Logistics Coord",
         [("Receiving Clerk inspects delivery: checks for damage, counts against delivery manifest, verifies item condition; records goods receipt in system", "Receiving Clerk", "Store Manager", "10–15 min/delivery"),
          ("Damaged items: Clerk photographs, records on delivery receipt, notes on 3PL proof-of-delivery; system creates damage record for VS-50 claim", "Receiving Clerk", "Logistics Coordinator", "5–10 min"),
          ("Weekly: Store Manager reports delivery quality issues to Logistics Coordinator; patterns by partner or route investigated", "Store Manager", "Logistics Manager", "15 min/week")]),
        ("Proof of Delivery & Documentation", "Every delivery completion", "Every delivery (~10,000/month)", "~10,000 PODs/month", "3PL Driver / Store Receiving Clerk", "Driver, Receiving Clerk, Logistics Coord",
         [("Driver obtains proof of delivery: digital signature on tablet/smartphone or paper sign-off; captures GPS location and timestamp", "3PL Driver", "Logistics Coordinator", "2 min/delivery"),
          ("System stores POD with delivery record; auto-matches to shipment for settlement; POD available for customer inquiry and dispute resolution", "System", "Finance", "Automated")]),
        ("Delivery Exception Management", "Delivery issue reported by store, customer, or driver", "~500–800 exceptions/month (~5–8%)", "~500–800/month", "Logistics Coordinator", "Logistics Coord, 3PL Partner, Store Manager, Customer Service",
         [("Coordinator receives exception alert: categorize as (a) delivery delay, (b) damaged goods, (c) wrong items, (d) failed delivery (customer unavailable), (e) vehicle breakdown", "Logistics Coordinator", "Logistics Manager", "5–15 min"),
          ("Coordinator resolves: arranges re-delivery, dispatches replacement, escalates to 3PL partner, coordinates with DC for missing items", "Logistics Coordinator", "3PL Partner", "15–30 min")]),
        ("Multi-Stop Route Optimization", "Daily delivery planning for DC-to-store routes", "Daily; 4 DCs", "~4 DCs × 5–8 routes/day × 2–3 stops/route", "DC Dispatch Supervisor", "DC Dispatch, Logistics Mgr, Route Optimization System",
         [("System generates optimized routes for next-day deliveries: groups orders by geographic zone, minimizes travel distance, balances vehicle capacity utilization", "System", "DC Dispatch Supervisor", "Automated"),
          ("Dispatch Supervisor reviews and adjusts: handles priority deliveries, adds last-minute orders, adjusts for road closures or weather events", "DC Dispatch Supervisor", "Logistics Manager", "1–2 hours/day")]),
        ("Seasonal Delivery Surge Management", "Peak season preparation (Christmas, summer)", "2–3 major peaks/year", "~30–50% volume increase during peaks", "Logistics Manager", "Logistics Mgr, DC Ops, Store Ops, 3PL Partners",
         [("Logistics Manager forecasts peak volume based on historical data and seasonal calendar; pre-books 3PL capacity 4–6 weeks ahead", "Logistics Manager", "VP Supply Chain", "2–3 days"),
          ("Manager implements surge plan: extended delivery windows, additional routes, temporary driver augmentation, DC overtime scheduling", "Logistics Manager", "DC Operations", "1 week"),
          ("Post-peak: analyzes performance vs. plan; adjusts capacity planning for next peak; updates 3PL contracts with peak rate agreements", "Logistics Manager", "VP Supply Chain", "2–3 days")])
    ]),
    ("PA-56.3", "3pl-settlement-cost-optimization", "3PL Settlement & Cost Optimization", [
        ("Monthly 3PL Invoice Processing", "3PL partner submits monthly invoice", "Monthly; ~10–15 invoices", "~10–15 invoices/month; ~PHP 30–50M/month total logistics spend", "Logistics Finance Analyst", "Logistics Finance Analyst, Logistics Mgr, Finance, 3PL Partner",
         [("Analyst matches 3PL invoice against system delivery records: validates delivery count, distances, weight surcharges, SLA penalties or bonuses", "Logistics Finance Analyst", "Finance Manager", "4–6 hours/month"),
          ("Discrepancies investigated with 3PL partner; adjusted invoice approved; payment scheduled per standard AP process (Net 30)", "Logistics Finance Analyst", "3PL Partner", "2–3 hours/month")]),
        ("Per-Delivery Cost Analysis", "Monthly cost analysis", "Monthly", "~10,000 deliveries/month cost-analyzed", "Logistics Finance Analyst", "Logistics Finance Analyst, Logistics Mgr, FP&A",
         [("Analyst calculates per-delivery cost: total 3PL spend ÷ delivery count; segments by partner, route, DC, store, and delivery type", "Logistics Finance Analyst", "Finance Manager", "2–3 hours/month"),
          ("Identifies cost outliers: routes with above-average cost, partners with increasing rates, stores with excessive exception costs", "Logistics Finance Analyst", "Logistics Manager", "1–2 hours/month")]),
        ("3PL Cost Benchmarking", "Quarterly benchmarking exercise", "Quarterly", "10–15 partners benchmarked against market", "Logistics Manager", "Logistics Mgr, Procurement, Finance",
         [("Logistics Manager benchmarks BuildRight's delivery costs against Philippine logistics market rates: per-km, per-delivery, per-kg rates from Lalamove, Transportify, and industry surveys", "Logistics Manager", "Procurement", "1–2 days/quarter"),
          ("Identifies cost savings opportunities: rate renegotiation, partner consolidation, route optimization, volume commitments for discounts", "Logistics Manager", "VP Supply Chain", "1 day/quarter")]),
        ("Fuel Cost Impact Analysis", "Monthly or significant fuel price change", "Monthly; ad-hoc for >5% fuel price change", "Monthly analysis of fuel component across all routes", "Logistics Finance Analyst", "Logistics Finance Analyst, Logistics Mgr, Finance",
         [("Analyst tracks fuel cost component of 3PL rates: monitors Philippine diesel/gasoline prices; calculates impact on per-delivery cost", "Logistics Finance Analyst", "Finance Manager", "2–3 hours/month"),
          ("Significant price changes (>5%): triggers rate card review with partners; adjusts BuildRight delivery fee for ecommerce customers if warranted", "Logistics Finance Analyst", "Logistics Manager", "1–2 days")]),
        ("Owned Fleet vs. 3PL Cost Comparison", "Annual fleet strategy review", "Annual", "Owned fleet: 20%; 3PL: 80%", "VP Supply Chain", "VP Supply Chain, Logistics Mgr, Finance Director, COO",
         [("Finance calculates total cost of ownership for owned fleet (depreciation, maintenance, fuel, driver salaries, insurance) vs. 3PL cost per delivery", "Finance Director", "CFO", "3–5 days"),
          ("VP Supply Chain recommends fleet mix: identifies routes where owned fleet is more cost-effective (high-volume, regular routes) vs. 3PL (variable, peak)", "VP Supply Chain", "COO", "2–3 days")]),
        ("Delivery Fee Revenue Optimization", "Monthly ecommerce delivery fee analysis", "Monthly", "~17,200 home deliveries/month with delivery fees", "Ecommerce Operations Manager", "Ecom Ops Mgr, Finance, Logistics Mgr",
         [("Ecommerce Manager analyzes delivery fee vs. actual delivery cost: fee structure (weight/distance), free delivery threshold (PHP 5,000), average fee collected", "Ecom Ops Manager", "Finance Manager", "2–3 hours/month"),
          ("Adjusts fee structure to maintain margin: increases fees for loss-making routes/weights; maintains free delivery threshold for order value optimization", "Ecom Ops Manager", "VP Marketing", "1 day/quarter")]),
        ("3PL Payment Settlement Automation", "Monthly settlement cycle", "Monthly; ~10–15 partners", "~10–15 settlements/month; ~PHP 30–50M", "Finance Manager", "Finance Mgr, Logistics Finance Analyst, Treasury",
         [("System auto-calculates settlement per partner: delivery fees × volume, SLA penalties, damage deductions, rate adjustments; generates settlement statement", "System", "Finance Manager", "Automated"),
          ("Finance Manager reviews and approves; payment processed via bank transfer on Net 30 terms; settlement statement shared with partner for reconciliation", "Finance Manager", "CFO", "2–3 hours/month")]),
        ("Logistics Total Cost Dashboard", "Monthly dashboard; real-time monitoring", "Continuous; monthly deep analysis", "Full logistics cost: ~PHP 360–600M/year (~0.6–1% of revenue)", "VP Supply Chain", "VP Supply Chain, Logistics Mgr, Finance Dir, COO",
         [("System maintains logistics cost dashboard: total cost, cost per delivery, cost per store, cost per peso of goods delivered, % of COGS, trend vs. budget", "System", "VP Supply Chain", "Automated"),
          ("VP Supply Chain reviews monthly with COO and CFO; identifies cost reduction opportunities; tracks savings initiatives with quarterly targets", "VP Supply Chain", "COO", "2–3 hours/month")])
    ])
]))

# ─── VS-57: Competitive Price Intelligence ───
EXTRA_VS.append(("VS-57-competitive-price-intelligence", 57,
    "Competitive Price Intelligence & Monitoring", "Plan & Source",
    "Manages BuildRight's competitive pricing intelligence program, including systematic collection of competitor pricing data, price matching decisions, dynamic pricing recommendations, and margin impact analysis. Monitors key competitors (Wilcon, CitiHardware, Handyman Do-It-Best, Mr. DIY) across the Philippine hardware/home improvement market.",
    [("PA-57.1", "competitor-price-data-collection", "Competitor Price Data Collection & Analysis", [
        ("Competitor Price Scraping & Collection", "Weekly data collection cycle", "Weekly; ~500–1,000 SKU-price points per cycle", "~500–1,000 competitive prices/week across 4–5 competitors", "Pricing Analyst", "Pricing Analyst, Category Mgr, IT",
         [("Pricing Analyst coordinates weekly price collection: (a) automated web scraping for competitor ecommerce prices, (b) field team mystery shopping for in-store prices (20 key stores per competitor), (c) marketplace price monitoring (Lazada, Shopee)", "Pricing Analyst / System", "Category Manager", "1–2 days"),
          ("System normalizes and stores price data: matches competitor SKUs to BuildRight SKUs using product attribute mapping; flags significant price changes (>5%)", "System", "Pricing Analyst", "Automated")]),
        ("Price Matching Decision & Execution", "Significant competitive price gap identified (>10%)", "Ad-hoc; typically 20–30 decisions/month", "~20–30 price matching decisions/month", "Category Manager", "Category Mgr, Pricing Analyst, VP Merchandising",
         [("Pricing Analyst prepares price match recommendation: current BuildRight price, competitor price, margin impact, volume estimate, strategic importance of SKU", "Pricing Analyst", "Category Manager", "30–60 min"),
          ("Category Manager decides: match price (if margin acceptable), undercut (if strategically important), or hold (if differentiation justifies premium); approves price change in system", "Category Manager", "VP Merchandising", "15–30 min")]),
        ("Competitor Promotion Monitoring", "Competitor launches promotional event", "Ad-hoc; ~2–3 major competitor promos/quarter", "~2–3 competitor promotional events monitored/quarter", "Pricing Analyst", "Pricing Analyst, Marketing, Category Mgr",
         [("Pricing Analyst monitors competitor promotional activity: catalogs, flyers, social media, in-store signage; captures promotional prices, duration, and terms", "Pricing Analyst", "Category Manager", "2–3 hours/event"),
          ("Analyst assesses impact on BuildRight: overlapping SKUs, potential sales loss, recommended response (match, counter-promote, ignore)", "Pricing Analyst", "VP Merchandising", "1–2 hours/event")]),
        ("Price Positioning Strategy Review", "Quarterly pricing strategy review", "Quarterly; 13 product categories", "~13 category pricing reviews/quarter", "VP Merchandising", "VP Merch, Category Mgrs, Pricing Analysts, Finance",
         [("Pricing Analyst prepares category price positioning analysis: BuildRight avg price vs. competitors, price index by category, margin vs. competition, price perception survey results", "Pricing Analyst", "VP Merchandising", "2–3 days"),
          ("VP Merchandising reviews and sets category pricing strategy: premium (better service/assortment), parity (match market), or value (compete on price)", "VP Merchandising", "COO", "1 day")]),
        ("Dynamic Pricing Rule Management", "Monthly rule review or competitive trigger", "Monthly review; ad-hoc adjustments", "~50–100 dynamic pricing rules active", "Pricing Analyst", "Pricing Analyst, IT, Category Mgr",
         [("Pricing Analyst maintains dynamic pricing rules in ERP: (a) auto-price-match for designated SKUs when competitor price drops below threshold, (b) floor price to protect minimum margin, (c) ceiling price to prevent overpricing, (d) clearance markdown triggers", "Pricing Analyst", "Category Manager", "4–6 hours/month"),
          ("IT implements rule changes; tests in sandbox; Category Manager approves before production deployment", "IT / Pricing Analyst", "Category Manager", "1–2 days")]),
        ("Market Basket Price Comparison", "Quarterly comprehensive comparison", "Quarterly", "~100 SKU market basket per competitor", "Pricing Analyst", "Pricing Analyst, Category Mgr, VP Merchandising",
         [("Analyst constructs standardized market basket: 100 commonly purchased items across categories; prices each basket at BuildRight and 4–5 competitors (in-store + online)", "Pricing Analyst", "Category Manager", "3–5 days"),
          ("Calculates BuildRight basket price index vs. competitors; identifies categories where BuildRight is significantly over/underpriced; recommends adjustments", "Pricing Analyst", "VP Merchandising", "1 day")]),
        ("Price Elasticity Analysis", "Semi-annual or after major price change", "Semi-annual; post-price-change analysis", "~50–100 elasticity analyses per cycle", "Analytics Manager", "Analytics Mgr, Pricing Analyst, Category Mgr",
         [("Analytics Manager analyzes price elasticity for key SKUs: measures volume change vs. price change using historical data; calculates price elasticity coefficient", "Analytics Manager", "Pricing Analyst", "3–5 days"),
          ("Results feed into pricing strategy: inelastic items (necessities) can support higher margins; elastic items (commodities) need competitive pricing", "Analytics Manager", "VP Merchandising", "1 day")]),
        ("Competitor Pricing Intelligence Report", "Monthly reporting cycle", "Monthly", "Monthly report covering 4–5 competitors", "Pricing Analyst", "Pricing Analyst, Category Mgrs, VP Merch, COO",
         [("Analyst compiles monthly intelligence report: competitor price movements, promotional activity, new market entrants, pricing trends, BuildRight price index trend", "Pricing Analyst", "VP Merchandising", "1 day"),
          ("VP Merchandising reviews with Category Managers and COO; identifies strategic implications and action items for next month", "VP Merchandising", "COO", "2–3 hours")])
    ]),
    ("PA-57.2", "price-response-strategy", "Price Response Strategy & Execution", [
        ("Rapid Price Response Workflow", "Competitor makes unexpected price move on key SKU", "Ad-hoc; ~5–10 rapid responses/month", "~5–10 rapid price decisions/month", "Category Manager", "Category Mgr, Pricing Analyst, VP Merch, IT",
         [("Pricing Analyst alerts Category Manager of significant competitor price change on key SKU; prepares impact analysis (volume at risk, margin impact of matching)", "Pricing Analyst", "Category Manager", "30–60 min"),
          ("Category Manager decides response; VP Merchandising approves changes >5% margin impact; IT implements price update in ERP; cascaded to POS within 4 hours", "Category Mgr / VP Merch", "IT", "2–4 hours total")]),
        ("Promotional Price Planning", "Upcoming promotional calendar event", "6 major promos/year + monthly hot deals", "~6 major + 12 monthly promotional pricing cycles/year", "Pricing Analyst", "Pricing Analyst, Category Mgr, Marketing, Finance",
         [("Pricing Analyst recommends promotional prices based on competitive data: target price position (below key competitor), expected volume lift, margin impact, vendor co-op funding", "Pricing Analyst", "Category Manager", "2–3 days"),
          ("Category Manager approves; Finance validates margin floor; Marketing incorporates into promotional materials; POS configured with promotional prices", "Category Mgr / Finance / Marketing", "VP Merchandising", "3–5 days")]),
        ("Markdown Optimization for Clearance", "End-of-season or slow-moving inventory requiring markdown", "Monthly review; seasonal transitions", "~500–1,000 markdown decisions/month", "Category Manager", "Category Mgr, Merch Planner, Pricing Analyst, Finance",
         [("Merch Planner identifies markdown candidates: seasonal items past peak, slow-moving SKUs (>120 days inventory), damaged packaging; Pricing Analyst recommends markdown levels based on competitive pricing and clearance velocity targets", "Merch Planner / Pricing Analyst", "Category Manager", "1–2 days"),
          ("Category Manager approves markdown schedule; system updates prices; POS reflects clearance pricing; Marketing communicates clearance event", "Category Manager", "VP Merchandising", "1 day")]),
        ("Store-Level Price Override Management", "Store requests price override for competitive reason", "~200–400 override requests/month", "~200–400/month across 200 stores", "Store Manager / Regional Ops Manager", "Store Manager, Regional Ops Mgr, Category Mgr",
         [("Store Manager submits price override request in system: SKU, current price, requested price, competitor name and proof (photo of competitor shelf price)", "Store Manager", "Regional Ops Mgr", "15 min"),
          ("Regional Ops Manager reviews; approves if within authorized range (typically up to 10% reduction); Category Manager approves >10%; system updates price for that store/location", "Regional Ops Mgr / Category Mgr", "VP Merchandising", "30 min")]),
        ("Price Change Communication to Stores", "Price change approved and ready for cascade", "~200–300 price changes/month", "~200–300/month across 200 stores", "Merchandising Coordinator", "Merch Coordinator, Store Managers, IT",
         [("System generates price change package: SKU, old price, new price, effective date, reason code; distributes to all affected stores via store manager app", "System", "Merch Coordinator", "Automated"),
          ("Stores print updated shelf labels from RF guns; apply to shelf within 24 hours of effective date; Merch Coordinator verifies compliance via VS-55", "Store Staff", "Store Manager", "2–4 hours")]),
        ("Trade Price Competitive Alignment", "Quarterly trade price review for B2B accounts", "Quarterly; ~5,000 trade accounts", "~5,000 trade accounts reviewed quarterly", "Trade Sales Manager", "Trade Sales Mgr, Pricing Analyst, Category Mgr",
         [("Pricing Analyst compares BuildRight trade prices vs. competitor trade/wholesale prices for top 200 SKUs purchased by trade customers", "Pricing Analyst", "Trade Sales Manager", "2–3 days"),
          ("Trade Sales Manager recommends adjustments to maintain competitiveness while preserving margin; Category Manager approves; system updates trade price lists", "Trade Sales Mgr / Category Mgr", "VP Merchandising", "1 day")]),
        ("Price Audit & Compliance", "Monthly internal price audit", "Monthly; 200 stores", "~200 store price audits/month", "Pricing Analyst", "Pricing Analyst, Store Manager, Regional Ops",
         [("Pricing Analyst runs system price audit: compares POS shelf price to system SRP for all transactions; flags discrepancies", "System / Pricing Analyst", "Category Manager", "2–3 hours"),
          ("Stores with >1% price discrepancies investigated; root causes (delayed label updates, override abuse, system sync errors) corrected", "Pricing Analyst / Store Manager", "VP Merchandising", "1–2 days")]),
        ("Customer Price Match Guarantee Execution", "Customer requests price match at POS", "~3,000–5,000 price match requests/month", "~3K–5K/month; ~0.1% of transactions", "Cashier / Store Manager", "Cashier, Customer, Store Manager, Pricing System",
         [("Customer presents competitor price proof (flyer, photo, website); Cashier verifies: same SKU, current competitor price, within price match policy terms", "Cashier", "Store Manager", "5–10 min"),
          ("For matches within 10%: Cashier approves at POS. For >10% or high-value items: Store Manager approves. System records price match for analytics and fraud monitoring", "Cashier / Store Manager", "Pricing Analyst", "5–10 min")])
    ]),
    ("PA-57.3", "pricing-analytics-margin-optimization", "Pricing Analytics & Margin Optimization", [
        ("Gross Margin Analysis by Category", "Monthly financial analysis", "Monthly; 13 product categories", "13 category margin analyses/month", "Finance Manager", "Finance Mgr, Category Mgr, VP Merchandising",
         [("System calculates gross margin by category: revenue, COGS, promotional markdowns, returns, net margin; compares vs. target and prior periods", "System", "Finance Manager", "Automated"),
          ("Category Manager reviews margin trends; identifies margin erosion causes (competitive price pressure, supplier cost increase, promo overspend)", "Category Manager", "VP Merchandising", "2–3 hours")]),
        ("Price Sensitivity Dashboard", "Weekly dashboard update", "Weekly", "~100 key SKUs monitored for sensitivity", "Pricing Analyst", "Pricing Analyst, Category Mgr, VP Merch",
         [("Dashboard shows: current price, price trend, competitor price, price gap, volume trend, margin, and sensitivity indicator (high/medium/low)", "System", "Pricing Analyst", "Automated"),
          ("Pricing Analyst flags SKUs with diverging price-volume trends; recommends price adjustments to Category Manager", "Pricing Analyst", "Category Manager", "1–2 hours/week")]),
        ("Vendor Cost-Driven Price Adjustment", "Vendor announces cost increase or decrease", "~5–10 vendor cost changes/month affecting pricing", "~5–10 cost-driven price reviews/month", "Category Manager", "Category Mgr, Buyer, Pricing Analyst, Finance",
         [("Buyer receives vendor cost change notification; Pricing Analyst calculates required price adjustment to maintain target margin; assesses competitive impact", "Buyer / Pricing Analyst", "Category Manager", "2–4 hours"),
          ("Category Manager decides: pass through cost increase, absorb (reduce margin), or negotiate with vendor; implements price change if warranted", "Category Manager", "VP Merchandising", "1–2 hours")]),
        ("Pricing Strategy Annual Review", "Annual comprehensive pricing strategy review", "Annual; all 13 categories", "Full category pricing strategy overhaul", "VP Merchandising", "VP Merch, Category Mgrs, Finance Dir, COO, CEO",
         [("VP Merchandising leads annual pricing strategy review: category-by-category assessment of price positioning, margin targets, competitive landscape, and customer value perception", "VP Merchandising", "CEO", "3–5 days"),
          ("Finance Director sets margin floors and pricing guardrails; COO approves operational impact; CEO approves strategy for new fiscal year", "Finance Dir / COO / CEO", "Board", "1–2 days")]),
        ("Promotional Pricing ROI Analysis", "Post-promotional analysis", "After each of 6 major promos + 12 monthly hot deals", "18 promotional analyses/year", "FP&A Analyst", "FP&A, Pricing Analyst, Category Mgr, Marketing",
         [("FP&A calculates promo ROI: incremental sales × margin minus promotional discount cost minus marketing spend; compares vs. non-promotional baseline period", "FP&A Analyst", "Finance Manager", "4–6 hours"),
          ("Pricing Analyst correlates with competitive pricing during promo; identifies whether promo was defensive (matched competitor) or offensive (proactive)", "Pricing Analyst", "Category Manager", "2–3 hours")]),
        ("Price Image & Customer Perception Survey", "Semi-annual customer survey", "Semi-annual; ~1,000 customer respondents", "~1,000 respondents per survey", "Marketing Research Manager", "Marketing Research, Pricing Analyst, VP Marketing",
         [("Marketing Research conducts price perception survey: customers rate BuildRight value for money vs. competitors; identifies categories perceived as overpriced or good value", "Marketing Research Mgr", "VP Marketing", "2–3 weeks"),
          ("Pricing Analyst correlates perception data with actual price positioning; identifies gaps between reality and perception for marketing communication", "Pricing Analyst", "VP Merchandising", "3–5 days")]),
        ("Pricing System & Master Data Accuracy", "Monthly pricing data quality audit", "Monthly; 35,000 active SKUs", "~35,000 price records to maintain", "IT System Admin / Pricing Analyst", "IT, Pricing Analyst, Data Quality Analyst",
         [("System validates pricing data: (a) all active SKUs have current SRP, (b) promotional prices within effective dates, (c) trade prices within approved ranges, (d) no negative margins without approval", "System", "IT System Admin", "Automated"),
          ("Pricing Analyst investigates exceptions; corrects data; implements preventive controls for recurring issues", "Pricing Analyst", "Category Manager", "2–3 hours/month")]),
        ("Cross-Channel Price Consistency Monitoring", "Weekly consistency check", "Weekly; POS, ecommerce, marketplace channels", "3 channels × ~35,000 SKUs", "Ecommerce Operations Manager", "Ecom Ops Mgr, Pricing Analyst, IT",
         [("System compares prices across channels: in-store POS, ecommerce website, marketplace listings; flags inconsistencies >PHP 50 or >5%", "System", "Ecom Ops Manager", "Automated"),
          ("Pricing Analyst investigates root causes (sync delays, marketplace manual overrides, promotional timing differences); corrects and prevents recurrence", "Pricing Analyst", "IT System Admin", "2–3 hours/week")])
    ])
]))

# ─── VS-58 through VS-68: Generated with abbreviated but BuildRight-specific content ───

REMAINING = [
    ("VS-58-coupon-digital-promotions", 58, "Coupon & Digital Promotions Management", "Sell & Serve",
     "Manages BuildRight's coupon and digital promotions program covering paper coupons, digital vouchers, loyalty point multipliers, and promotional code campaigns. Coordinates with marketing campaigns (VS-14), POS (VS-08), loyalty (VS-13), and ecommerce (VS-10). Targets ~15% of monthly transactions involving a promotional offer.",
     [("PA-58.1", "coupon-voucher-creation", "Coupon & Voucher Creation & Distribution", [
        ("Coupon Design & Configuration", "Marketing campaign launch requiring coupon", "~6 major + 12 monthly campaigns/year", "~18 coupon designs/year", "Marketing Promotions Manager", "Marketing, Category Mgr, IT, Legal",
         [("Marketing designs coupon: value/type (PHP off, % off, buy-X-get-Y), eligible SKUs/categories, validity period, channel (in-store/online/all), max redemptions, customer segment targeting", "Marketing", "VP Marketing", "1–2 days"),
          ("IT configures in ERP: coupon code/barcode, validation rules, stacking rules (can combine with other promos?), system limits; Legal reviews terms for Consumer Act compliance", "IT / Legal", "Category Manager", "1–2 days")]),
        ("Digital Voucher Distribution", "Campaign launch via digital channels", "~18 campaigns/year + ad-hoc", "~500,000–1,000,000 digital vouchers distributed/year", "Digital Marketing Manager", "Digital Mktg, CRM, Customer",
         [("Digital Marketing distributes vouchers via: (a) email to loyalty segments, (b) SMS blast to targeted customers, (c) push notification via app, (d) social media ads with voucher codes, (e) partner platforms (GCash, Maya rewards)", "Digital Marketing", "CRM Manager", "1–2 days/campaign"),
          ("System tracks distribution: sent count, open rate, claim rate, redemption rate by channel and segment; optimizes future distribution based on performance", "System / Digital Marketing", "VP Marketing", "Ongoing")]),
        ("In-Store Coupon Printing & Display", "Physical coupon campaign for in-store", "~6 major campaigns/year", "~200 stores × ~500 coupons each = ~600,000 physical coupons/campaign", "Marketing Operations Manager", "Marketing Ops, Print Vendor, Store Ops",
         [("Marketing Ops coordinates physical coupon printing: design, barcode, terms, paper stock; distributes to DC for store delivery; stores display at entrance and checkout", "Marketing Ops", "Print Vendor", "1–2 weeks"),
          ("Store Manager displays coupons at entrance rack and checkout counter; monitors stock; requests replenishment from DC during campaign", "Store Manager", "Marketing Ops", "15 min/week during campaign")]),
        ("Coupon Budget & Liability Management", "Campaign launch requiring budget allocation", "Per campaign (~18/year)", "~PHP 50–100M annual promotional budget", "Finance Manager", "Finance Mgr, Marketing Dir, CFO",
         [("Finance estimates coupon liability: expected redemption rate × coupon value × distribution volume; allocates from promotional budget; sets up accrual", "Finance Manager", "CFO", "2–3 hours/campaign"),
          ("Monthly: reconciles actual redemptions vs. accrual; adjusts liability; reports promotional spend vs. budget", "Finance Manager", "CFO", "2–3 hours/month")]),
        ("Vendor-Funded Coupon Program", "Vendor offers co-op promotional funding", "~10–15 vendor-funded promos/year", "~10–15 vendor-funded campaigns/year", "Category Manager", "Category Mgr, Marketing, Vendor, Finance",
         [("Vendor proposes co-op coupon: BuildRight distributes, vendor funds discount portion per VS-39 (co-op marketing); Category Manager negotiates terms", "Category Manager", "Vendor", "1–2 days"),
          ("Marketing designs and distributes coupon; system tracks redemptions; Finance submits claim to vendor for funded portion per VS-39 settlement", "Marketing / Finance", "Category Manager", "Ongoing")]),
        ("Loyalty Point Multiplier Campaign", "Loyalty program campaign (double/triple points)", "~6–8 multiplier campaigns/year", "~600,000 loyalty members reached per campaign", "Loyalty Program Manager", "Loyalty Mgr, Marketing, CRM, Finance",
         [("Loyalty Manager designs multiplier campaign: multiplier (2x/3x/5x), eligible categories, dates, member tiers (Bronze/Silver/Gold/Platinum); configures in loyalty engine", "Loyalty Manager", "VP Marketing", "1–2 days"),
          ("Marketing communicates to members via email, SMS, app push, in-store signage; system auto-applies multiplier at POS/online during campaign period", "Marketing / System", "Loyalty Manager", "1 day")]),
        ("Coupon Fraud Prevention Design", "Coupon design review for fraud resistance", "Every coupon design before launch", "~18 designs reviewed/year", "Loss Prevention Analyst", "LP Analyst, Marketing, IT",
         [("LP Analyst reviews coupon design for fraud vectors: (a) unique barcodes (no photocopying), (b) single-use enforcement, (c) purchase requirement validation, (d) digital coupon device-binding", "LP Analyst", "LP Director", "2–3 hours/campaign"),
          ("IT implements fraud controls: limit redemptions per customer, per store, per day; anomaly detection for unusual redemption patterns", "IT", "LP Analyst", "1–2 days/campaign")]),
        ("Coupon Performance Tracking Dashboard", "Campaign active period", "Real-time during campaigns; post-campaign analysis", "Per campaign (~18/year)", "Marketing Analyst", "Marketing Analyst, VP Marketing, Category Mgr",
         [("Dashboard shows: distributed count, claimed count, redeemed count, redemption rate, incremental sales, average basket with coupon vs. without, cost per redemption", "System", "Marketing Analyst", "Automated"),
          ("Marketing Analyst produces post-campaign report with ROI, channel performance, customer segment performance, and recommendations for next campaign", "Marketing Analyst", "VP Marketing", "4–6 hours/campaign")])
     ]),
     ("PA-58.2", "coupon-redemption-fraud", "Coupon Redemption & Fraud Prevention", [
        ("In-Store Coupon Redemption Processing", "Customer presents coupon at POS", "~50,000–80,000 coupon redemptions/month during active campaigns", "~50K–80K/month; ~15% of transactions", "Cashier", "Cashier, Customer, POS System",
         [("Cashier scans coupon barcode at POS; system validates: (a) coupon is active and within validity, (b) eligible items in basket, (c) coupon not previously redeemed, (d) purchase minimum met", "POS System", "Cashier", "15–30 sec"),
          ("Valid coupon: discount applied to transaction; system records redemption with transaction ID, coupon code, store, cashier ID; customer receives discounted total", "POS System", "Cashier", "Automated")]),
        ("Online Coupon & Promo Code Redemption", "Customer enters promo code at ecommerce checkout", "~8,000–12,000 online coupon redemptions/month", "~8K–12K/month", "Ecommerce System", "Ecommerce System, Customer, CRM",
         [("Customer enters promo code at checkout; system validates: active, within dates, eligible items, minimum purchase, not exceeded usage limit, customer segment eligible", "System", "Customer", "<5 sec"),
          ("Valid: discount applied; invalid: specific error message (expired, minimum not met, already used); redemption tracked in CRM for analytics and fraud monitoring", "System", "Ecommerce Ops", "Automated")]),
        ("Multi-Coupon Stacking Management", "Customer presents multiple coupons for one transaction", "Per coupon policy; ~5–10% of coupon transactions", "~5–10% of coupon redemptions", "Cashier / POS System", "Cashier, Customer, POS System",
         [("POS system enforces stacking rules: (a) max 1 manufacturer + 1 store coupon per item, (b) total discount cannot exceed 50% of basket, (c) certain categories excluded from stacking", "POS System", "Cashier", "Automated"),
          ("Cashier informed by POS if stacking limit reached; explains to customer; suggests optimal coupon combination for maximum savings", "Cashier", "Store Manager", "1–2 min")]),
        ("Coupon Redemption Fraud Detection", "Real-time monitoring during active campaigns", "Real-time alerts; weekly comprehensive review", "~100–200 flagged transactions/month", "Loss Prevention Analyst", "LP Analyst, Store Manager, Finance",
         [("System monitors for fraud patterns: (a) same coupon redeemed multiple times (barcode reuse), (b) single customer redeeming >5 coupons/day, (c) single store with abnormally high redemption rate, (d) employee-customer collusion patterns", "System", "LP Analyst", "Real-time"),
          ("LP Analyst investigates flagged transactions; confirms fraud → reverses transaction, deactivates coupon, escalates to Store Manager; weekly fraud trend report", "LP Analyst", "LP Director", "2–3 hours/week")]),
        ("Coupon Return & Reversal", "Customer returns item purchased with coupon", "~2,000–3,000 coupon-return transactions/month", "~2K–3K/month", "Customer Service Rep", "CSR, Customer, POS System, Finance",
         [("CSR processes return: system determines coupon treatment: (a) full return (all items from coupon transaction) → coupon reinstated for reuse, (b) partial return → prorated refund minus coupon value applied to retained items", "POS System", "CSR", "5–10 min"),
          ("System reverses coupon redemption if reinstated; adjusts promotional liability; prevents double-dipping on reinstated coupons", "System", "Finance", "Automated")]),
        ("Expired Coupon Exception Handling", "Customer presents recently expired coupon with complaint", "~500–1,000 expired coupon requests/month", "~500–1,000/month", "Store Manager", "Store Manager, Customer, Marketing",
         [("Customer presents expired coupon; Store Manager reviews: (a) within 7 days of expiry → may honor as goodwill, (b) loyalty program member → more lenient, (c) high-value customer → honor with manager override", "Store Manager", "Regional Ops Mgr", "5 min"),
          ("If honored: manager override in POS with reason code; system processes as valid redemption; if denied: offer equivalent current promotion as alternative", "Store Manager", "Marketing", "5 min")]),
        ("Digital Coupon Device & Account Binding", "Customer claims digital coupon on mobile app", "Per campaign distribution (~18/year)", "~500,000–1M digital coupon claims/year", "IT Integration Lead", "IT Integration, CRM, Digital Marketing",
         [("System binds claimed digital coupon to customer account (loyalty ID) and device (device fingerprint); prevents sharing/selling of digital coupons", "System", "IT Integration Lead", "Automated"),
          ("IT maintains device binding integrity: detects device spoofing, multiple accounts per device, VPN-based claims from different regions; adjusts fraud rules", "IT Integration Lead", "CIO", "4–6 hours/month")]),
        ("Coupon Vendor Reconciliation", "Monthly vendor-funded coupon settlement", "Monthly; ~10–15 vendor campaigns active", "~10–15 vendor reconciliations/month", "Finance Analyst", "Finance Analyst, Category Mgr, Vendor",
         [("Finance Analyst compiles vendor coupon redemption report: coupon code, redemption count, total discount value, eligible per co-op agreement; submits claim to vendor per VS-39", "Finance Analyst", "Finance Manager", "4–6 hours/month"),
          ("Vendor validates and approves claim; Finance records receivable; collects within agreed terms (typically Net 30); disputes resolved with supporting POS transaction data", "Finance Analyst / Vendor", "Finance Manager", "2–3 hours/month")])
     ]),
     ("PA-58.3", "digital-promotion-analytics", "Digital Promotion Performance Analytics", [
        ("Campaign ROI Analysis", "Post-campaign analysis", "Per campaign (~18/year)", "18 comprehensive analyses/year", "Marketing Analyst", "Marketing Analyst, VP Marketing, Finance",
         [("Analyst calculates campaign ROI: (incremental sales × margin) minus (coupon cost + distribution cost + marketing spend); redemption rate, customer acquisition cost, repeat purchase rate", "Marketing Analyst", "VP Marketing", "4–6 hours/campaign"),
          ("Compares vs. campaign target and historical benchmarks; identifies winning strategies and underperforming tactics; feeds into next campaign planning", "Marketing Analyst", "VP Marketing", "2–3 hours")]),
        ("Channel-Specific Promotion Effectiveness", "Monthly multi-channel analysis", "Monthly; POS, ecommerce, app, marketplace channels", "4 channels analyzed monthly", "Digital Marketing Manager", "Digital Marketing, Marketing Analyst, VP Marketing",
         [("Marketing Analyst segments promotion performance by channel: redemption rate, average basket size, customer demographics, cost per acquisition; identifies highest-ROI channel per promotion type", "Marketing Analyst", "Digital Marketing Mgr", "4–6 hours/month"),
          ("Digital Marketing reallocates budget to highest-performing channels; tests new channels with small pilot before scaling", "Digital Marketing Mgr", "VP Marketing", "1 day/month")]),
        ("Customer Segment Promotion Response", "Quarterly segment analysis", "Quarterly; 4 loyalty tiers + B2B", "~6 customer segments analyzed quarterly", "CRM Manager", "CRM Mgr, Marketing Analyst, Loyalty Mgr",
         [("CRM Manager analyzes promotion response by segment: (a) Bronze/Silver/Gold/Platinum redemption rates, (b) trade account usage, (c) new vs. existing customers, (d) lapsed customer reactivation", "CRM Manager", "VP Marketing", "2–3 days/quarter"),
          ("Identifies segments with highest/lowest response; customizes future promotions by segment; tests personalized offers for high-value segments", "CRM Manager", "Loyalty Manager", "1–2 days")]),
        ("Promotion Halo Effect Analysis", "Post-campaign analysis", "Per major campaign (6/year)", "6 halo analyses/year", "Analytics Manager", "Analytics Mgr, Category Mgr, VP Merchandising",
         [("Analytics Manager measures halo effect: sales uplift in non-promoted categories during promotional periods; incremental foot traffic during promos; basket expansion beyond promoted items", "Analytics Manager", "Category Manager", "1–2 days/campaign"),
          ("Identifies categories that benefit most from promotional traffic; recommends cross-merchandising strategies to maximize halo effect", "Analytics Manager", "VP Merchandising", "1 day")]),
        ("Year-over-Year Promotion Trend Analysis", "Annual comprehensive review", "Annual", "Full year promotional program review", "VP Marketing", "VP Marketing, Marketing Analyst, Finance Dir, VP Merch",
         [("Marketing Analyst compiles annual promotion trend: total promotional spend, total incremental revenue, ROI trend, redemption rate trend, channel mix shift, competitive promo frequency", "Marketing Analyst", "VP Marketing", "3–5 days"),
          ("VP Marketing presents annual review to Executive Committee with strategy recommendations: budget allocation, channel investment, promotion frequency, and competitive positioning", "VP Marketing", "CEO", "1 day")]),
        ("Digital Coupon Technology Performance", "Monthly technology review", "Monthly", "4 technology platforms (app, web, email, SMS)", "IT Integration Lead", "IT Integration, Digital Marketing, CRM",
         [("IT monitors digital coupon technology performance: (a) delivery success rate (email, SMS, push), (b) claim rate, (c) redemption processing latency, (d) system uptime during peak campaigns", "IT Integration Lead", "CIO", "2–3 hours/month"),
          ("Addresses performance issues: optimizes email deliverability, reduces SMS delivery failures, improves app notification reliability", "IT Integration Lead", "Digital Marketing Mgr", "Ongoing")]),
        ("Competitor Promotion Intelligence", "Ongoing monitoring during competitor promo periods", "Weekly monitoring; active during competitor campaigns", "4–5 competitors monitored", "Marketing Analyst", "Marketing Analyst, Pricing Analyst, VP Marketing",
         [("Marketing Analyst monitors competitor promotions: catalogs, social media, store visits; captures promo type, discount level, duration, eligible items; compares to BuildRight's current promotions", "Marketing Analyst", "Pricing Analyst", "2–3 hours/week"),
          ("Produces competitive promo report: BuildRight position during competitor campaigns; sales impact assessment; recommended defensive/offensive response", "Marketing Analyst", "VP Marketing", "4–6 hours/month")]),
        ("Promotion Calendar Optimization", "Annual calendar planning", "Annual; 6 major + 12 monthly + ad-hoc", "~18+ promotional events planned/year", "VP Marketing", "VP Marketing, VP Merch, Category Mgrs, Finance",
         [("VP Marketing leads annual promotion calendar planning: aligns with seasonal calendar, vendor funding availability, competitive intelligence, and customer behavior patterns", "VP Marketing", "CEO", "3–5 days"),
          ("Finance validates budget feasibility; VP Merchandising ensures assortment alignment; calendar finalized and communicated to stores 2 months before fiscal year start", "Finance / VP Merch", "COO", "2–3 days")])
     ])
    ),
    ("VS-59-store-closure-decommissioning", 59, "Store Closure & Decommissioning", "Asset & Infrastructure",
     "Manages the process of closing underperforming BuildRight Depot stores, covering closure decision analysis, lease termination, inventory liquidation, asset recovery, staff redeployment, and post-closure site management. Inverse of VS-37 (Store Opening). Targets: ~2–3 store closures/year in normal operations, with 6-month closure timeline.",
     [("PA-59.1", "store-closure-decision-planning", "Store Closure Decision & Planning", [
        ("Store Performance Trigger Analysis", "Quarterly store performance review identifies underperformer", "Quarterly; 200 stores reviewed", "200 stores; ~2–3 flagged for deep review/quarter", "VP Store Operations", "VP Store Ops, Finance Dir, Regional Ops Mgr",
         [("System flags stores meeting closure trigger criteria: (a) sales/sqm below 60% of chain average for 4 consecutive quarters, (b) negative store contribution margin for 2+ quarters, (c) lease renewal pending with unfavorable terms", "System", "VP Store Operations", "Automated"),
          ("VP Store Operations presents flagged stores to Executive Committee with performance data, market analysis, and options (improve/restructure/close)", "VP Store Ops", "CEO", "1–2 days")]),
        ("Closure Business Case Development", "Executive Committee approves closure evaluation", "Ad-hoc; ~2–3 evaluations/year", "~2–3 business cases/year", "FP&A Director", "FP&A Dir, VP Store Ops, VP Real Estate, Legal, HR",
         [("FP&A develops closure business case: (a) closure costs (lease termination penalty, severance, inventory write-down, asset disposal), (b) ongoing savings (rent, staff, utilities, inventory), (c) payback period, (d) NPV of closure vs. continued operation", "FP&A Director", "CFO", "5–10 days"),
          ("VP Real Estate evaluates lease terms: termination clause, penalty, notice period; Legal reviews contractual obligations; HR estimates severance costs", "VP Real Estate / Legal / HR", "FP&A Director", "3–5 days")]),
        ("Closure Decision & Board Approval", "Business case ready for decision", "Ad-hoc; ~2–3 decisions/year", "~2–3 closure decisions/year", "CEO", "CEO, CFO, COO, Board of Directors",
         [("CEO presents closure recommendation to Board with full business case, impact analysis (market, employees, customers), and execution timeline", "CEO", "Board", "2–3 hours"),
          ("Board approves or requests additional analysis; approved closures assigned to Store Closure Project Manager with 6-month execution timeline", "Board", "CEO", "1 day")]),
        ("Store Closure Communication Plan", "Closure approved by Board", "Per closure (~2–3/year)", "~2–3 communication plans/year", "VP Corporate Communications", "VP Corp Comms, HR, Store Ops, Legal, Marketing",
         [("VP Corp Comms develops communication plan: (a) employee notification timeline (DOLE 30-day notice requirement), (b) customer communication (loyalty members redirected to nearest store), (c) vendor notification, (d) media/PR statement, (e) LGU notification", "VP Corp Comms", "CEO", "3–5 days"),
          ("Legal reviews communication for compliance; HR prepares employee notification letters; Marketing prepares customer redirect messaging", "Legal / HR / Marketing", "VP Corp Comms", "2–3 days")]),
        ("Closure Project Planning & Timeline", "Board approves closure; project initiated", "Per closure (~2–3/year)", "~2–3 closure projects/year; 6-month timeline each", "Store Closure Project Manager", "Closure PM, VP Store Ops, VP Real Estate, HR, Finance",
         [("Closure PM develops detailed project plan: (a) employee transition (60 days), (b) inventory liquidation (90 days), (c) asset recovery (30 days), (d) lease termination (per contract), (e) site handover (final 30 days)", "Closure PM", "COO", "3–5 days"),
          ("Establishes weekly steering committee with VP Store Ops, HR, Finance, Real Estate, Legal; tracks milestones and escalates delays", "Closure PM", "COO", "Ongoing")]),
        ("Customer Migration Planning", "Closure approved; customer impact assessment", "Per closure", "~15,000–30,000 customers per store (loyalty + walk-in)", "Loyalty Program Manager", "Loyalty Mgr, Marketing, Store Ops, CRM",
         [("Loyalty Manager analyzes customer base of closing store: identifies active loyalty members, their purchase frequency, and nearest alternative store; develops redirect communications", "Loyalty Manager", "VP Marketing", "3–5 days"),
          ("Marketing executes customer migration campaign: personalized redirect to nearest store, special welcome offer at new store, extended promotions for displaced customers", "Marketing / Loyalty Manager", "VP Marketing", "2–3 weeks")]),
        ("Vendor & Supplier Notification for Closure", "Closure timeline confirmed", "Per closure", "~100–200 active vendors supplying closing store", "Procurement Manager", "Procurement Mgr, Category Mgr, Vendors",
         [("Procurement Manager notifies vendors: cancels DSD arrangements, adjusts PO delivery schedules, coordinates final deliveries and returns; Vendor Portal updated with store closure date", "Procurement Manager", "VP Supply Chain", "1–2 weeks"),
          ("Category Managers adjust assortment plans for surrounding stores to absorb demand from closed store's customer base", "Category Manager", "VP Merchandising", "1–2 weeks")]),
        ("Closure Regulatory & LGU Compliance", "Closure initiated; regulatory requirements", "Per closure", "LGU business permit cancellation, BIR notification, DOLE compliance", "Legal & Compliance Officer", "Legal, HR, Finance, External (LGU/BIR/DOLE)",
         [("Legal files closure notifications: LGU business permit cancellation, BIR branch registration closure, DOLE 30-day employee notice, SSS/PhilHealth/Pag-IBIG branch update", "Legal Officer", "VP Legal", "1–2 weeks"),
          ("Finance settles final LGU taxes and fees; HR ensures all statutory requirements met for affected employees; Legal retains records per 7-year retention policy", "Finance / HR / Legal", "CFO", "Ongoing")])
     ]),
     ("PA-59.2", "store-wind-down-asset-recovery", "Store Wind-Down & Asset Recovery", [
        ("Inventory Liquidation Planning & Execution", "Closure timeline reaches inventory phase (month 2–4)", "Per closure; 90-day liquidation window", "~35,000 SKUs; ~PHP 15–25M inventory per store", "Merchandising Planner", "Merch Planner, Category Mgr, Store Manager, Marketing",
         [("Merch Planner designs liquidation strategy: (a) transfer high-demand inventory to nearby stores (no markdown needed), (b) progressive markdown for remaining items (10% → 25% → 50% → 75%), (c) bulk sale to discount buyers for residual", "Merch Planner", "Category Manager", "1–2 weeks"),
          ("Marketing promotes liquidation sale; Store Manager executes markdown phases; system tracks sell-through rate; remaining inventory transferred to DC or sold in bulk", "Marketing / Store Manager", "Merch Planner", "90 days")]),
        ("Fixed Asset Recovery & Disposal", "Closure timeline reaches asset phase (month 4–5)", "Per closure", "~PHP 3–5M in fixtures and equipment per store", "Facilities Coordinator", "Facilities Coord, VP Real Estate, Finance",
         [("Facilities Coordinator inventories store assets: POS terminals, shelving, refrigeration (if any), forklifts, tools, office equipment; determines reuse vs. disposal", "Facilities Coordinator", "VP Real Estate", "3–5 days"),
          ("Reusable assets: transferred to new stores or DCs. Disposable assets: sold to used-equipment buyers or scrapped. Finance adjusts fixed asset register per VS-35", "Facilities Coordinator", "Finance Manager", "2–3 weeks")]),
        ("Lease Termination & Handover", "Closure timeline reaches lease phase (month 5–6)", "Per closure", "1 lease per store; typically 5–10 year terms", "VP Real Estate / Legal", "VP Real Estate, Legal, Landlord, Facilities",
         [("VP Real Estate negotiates lease termination: executes termination clause, pays penalty per contract, coordinates site restoration requirements, schedules handover inspection", "VP Real Estate", "Legal", "2–4 weeks"),
          ("Legal ensures full documentation: handover inspection report, condition assessment, deposit return, mutual release; site handed over to landlord on agreed date", "Legal", "VP Real Estate", "1–2 weeks")]),
        ("Employee Redeployment & Separation", "Closure timeline reaches HR phase (month 1–5)", "Per closure; ~29 employees per store", "~29 employees per store closure", "HR Director", "HR Dir, Store Manager, Regional Ops Mgr, Legal",
         [("HR identifies redeployment opportunities: transfers to nearby stores (priority for top performers), transfers to DC, HQ openings, or new store openings", "HR Director", "CHRO", "2–3 weeks"),
          ("For employees not redeployed: processes separation per Philippine Labor Code: 30-day notice, severance pay (0.5–1 month per year of service), clearance, final pay, COE, DOLE reporting", "HR Director", "Legal", "4–6 weeks")]),
        ("IT Systems Decommissioning", "Closure timeline reaches IT phase (month 5)", "Per closure", "3 POS terminals + network + systems per store", "IT Operations Manager", "IT Ops Mgr, POS Vendor, Network Provider",
         [("IT decommissions store systems: (a) closes POS terminals (returns to vendor or repurposes), (b) disconnects network/VPN, (c) deactivates store location in ERP, (d) archives store data per retention policy", "IT Ops Manager", "CIO", "3–5 days"),
          ("Ensures data backup and secure data destruction on local devices; removes store from inventory location master; updates customer-facing store locator", "IT Ops Manager", "Data Protection Officer", "2–3 days")]),
        ("Final Financial Settlement", "Closure complete; final accounting", "Per closure", "Full financial close for closed store entity", "Finance Manager", "Finance Mgr, Accountant, VP Real Estate, HR",
         [("Finance prepares final store P&L: all closure costs, asset disposal gains/losses, inventory write-downs, severance, lease penalty; closes store cost center in GL", "Finance Manager", "CFO", "5–10 days"),
          ("Settles all payables, collects remaining receivables, processes final tax filings for location; archives financial records per 7-year BIR requirement", "Finance Manager", "External Auditor", "2–3 weeks")]),
        ("Post-Closure Site Monitoring", "Site handed over; monitoring period", "6–12 months post-closure", "1 site per closure", "VP Real Estate", "VP Real Estate, Legal, Facilities",
         [("VP Real Estate monitors post-closure obligations: ensures landlord compliance with handover terms, resolves any post-handover disputes, monitors non-compete clauses", "VP Real Estate", "Legal", "Ongoing"),
          ("Tracks customer migration: monitors sales uplift at nearby stores to validate customer retention assumptions from business case", "VP Store Ops", "FP&A Director", "12 months")]),
        ("Closure Lessons Learned & Process Improvement", "Post-closure retrospective", "Per closure", "1 retrospective per closure", "Store Closure Project Manager", "Closure PM, COO, VP Store Ops, all functions",
         [("Closure PM conducts lessons learned: reviews timeline vs. actual, cost vs. budget, customer retention rate, employee redeployment success, vendor transition smoothness", "Closure PM", "COO", "1–2 days"),
          ("Updates closure playbook with improvements; shares learnings with Executive Committee; incorporates into future store opening strategy (VS-37) for better site selection", "Closure PM", "CEO", "1 day")])
     ]),
     ("PA-59.3", "staff-redeployment-post-closure", "Staff Redeployment & Post-Closure Analytics", [
        ("Redeployed Employee Onboarding at New Location", "Employee accepts transfer to new store/DC", "Per closure; ~15–20 redeployments per store", "~15–20 redeployments per closure", "HR Manager", "HR Manager, Receiving Store Manager, Employee",
         [("HR coordinates transfer: processes HR movement in system, updates employee location, arranges any relocation support; receiving Store Manager plans orientation", "HR Manager", "CHRO", "3–5 days"),
          ("Employee receives orientation at new location: store layout, team introduction, schedule assignment; 30-day check-in to assess adjustment", "Receiving Store Manager", "HR Manager", "1 week")]),
        ("Customer Migration Success Tracking", "Monthly post-closure analysis", "Monthly for 12 months post-closure", "~15,000–30,000 customers per closed store", "Loyalty Program Manager", "Loyalty Mgr, Analytics Mgr, VP Marketing",
         [("System tracks customer migration: identifies loyalty members from closed store, tracks their purchases at nearby stores, calculates retention rate and spend change", "System", "Loyalty Manager", "Automated"),
          ("Monthly: Loyalty Manager reviews migration rates; identifies customers who haven't migrated; triggers re-engagement campaigns; reports to VP Marketing", "Loyalty Manager", "VP Marketing", "2–3 hours/month")]),
        ("Post-Closure Financial Impact Analysis", "Quarterly post-closure review", "Quarterly for 4 quarters", "Full financial impact analysis per closure", "FP&A Director", "FP&A Dir, Finance Dir, VP Store Ops, CEO",
         [("FP&A compares actual closure costs vs. business case estimates; tracks quarterly savings from closure vs. projected; calculates actual payback period", "FP&A Director", "CFO", "2–3 days/quarter"),
          ("Reviews impact on surrounding stores: sales uplift, margin changes, operational strain; validates total network P&L impact of closure", "FP&A Director", "CEO", "1–2 days")]),
        ("Store Closure Database & Knowledge Management", "Post-closure documentation", "Per closure; updated into central database", "Central closure knowledge base", "Store Closure Project Manager", "Closure PM, all functions, IT",
         [("Closure PM compiles closure documentation: business case, project plan, execution timeline, actual costs, lessons learned, vendor/landlord contacts, regulatory filings", "Closure PM", "COO", "3–5 days"),
          ("IT stores in knowledge management system; accessible for future closure evaluations and new store opening teams (VS-37) for site selection reference", "IT / Closure PM", "COO", "1–2 days")]),
        ("Regional Sales Impact Assessment", "6-month post-closure analysis", "6 months and 12 months post-closure", "Region surrounding closed store (3–5 nearby stores)", "Analytics Manager", "Analytics Mgr, VP Store Ops, Category Mgr",
         [("Analytics Manager assesses regional impact: (a) total regional sales pre vs. post closure, (b) market share change in area, (c) competitor activity in vacated trade area", "Analytics Manager", "VP Store Ops", "2–3 days"),
          ("Identifies if closure created market opportunity for competitors; recommends defensive actions (enhanced promotions, new store consideration) if needed", "Analytics Manager", "VP Store Ops", "1 day")]),
        ("Employee Redeployment Success Metrics", "6-month post-redeployment review", "6 months after last redeployment", "~15–20 redeployed employees per closure", "HR Director", "HR Dir, Receiving Store Managers, CHRO",
         [("HR surveys redeployed employees: job satisfaction, performance at new location, commute impact, retention (6-month and 12-month); compares to pre-closure baseline", "HR Director", "CHRO", "3–5 days"),
          ("Identifies best practices for future redeployments; updates HR policies based on findings; addresses any systemic issues", "HR Director", "CHRO", "2–3 days")]),
        ("Network Optimization Analysis", "Annual network review incorporating closure learnings", "Annual; 200-store network", "Full network: 200 stores + growth plan", "VP Store Operations", "VP Store Ops, VP Real Estate, FP&A Dir, CEO",
         [("VP Store Ops conducts annual network optimization: reviews all store performance, identifies future closure candidates, evaluates new store opportunities in trade areas vacated by closures", "VP Store Ops", "CEO", "5–10 days"),
          ("FP&A models network scenarios: closures + openings + remodels; presents optimal network plan for next fiscal year to Executive Committee", "FP&A Director", "CEO", "3–5 days")]),
        ("Closure Playbook Maintenance & Update", "Annual or post-closure", "Annual; updated after each closure", "Living document: closure playbook", "Store Closure Project Manager", "Closure PM, COO, all function heads",
         [("Closure PM updates playbook based on latest closure experience: process improvements, new regulatory requirements, updated cost benchmarks, contact lists", "Closure PM", "COO", "2–3 days"),
          ("COO reviews and approves updated playbook; distributes to Regional Ops Managers and VP Real Estate for awareness and preparedness", "COO", "CEO", "1 day")])
     ])
    ),
    ("VS-60-omnichannel-order-routing", 60, "Omnichannel Order Routing & Fulfillment Orchestration", "Sell & Serve",
     "Manages intelligent routing and orchestration of customer orders across multiple fulfillment sources: stores, DCs, vendor drop-ship, and dark stores. Covers the full omnichannel order lifecycle from intelligent source selection through split-order management, fulfillment tracking, and optimization analytics. Critical for mixed-basket orders containing items from multiple origins.",
     [("PA-60.1", "intelligent-order-routing", "Intelligent Order Routing & Source Selection", [
        ("Order Source Selection Engine", "Customer places order (ecommerce, BOPIS, B2B)", "~42,900 ecommerce + ~3,500 B2B orders/month", "~46,400 orders/month requiring routing decisions", "Ecommerce Operations Manager", "Ecom Ops Mgr, System, DC Ops, Store Ops",
         [("System evaluates fulfillment sources per line item: (a) nearest store with available stock, (b) DC with stock, (c) vendor drop-ship, (d) dark store (VS-49); selects optimal source based on: delivery speed, cost, stock availability, item type (bulky vs. standard)", "System", "Ecom Ops Manager", "Automated (<5 sec)"),
          ("For BOPIS: routes to customer-selected store; if stock-out, suggests nearest alternative store with stock. For delivery: routes to source with fastest+cheapest combination", "System", "Customer", "Automated")]),
        ("Mixed-Basket Order Splitting", "Order contains items available from multiple sources", "~30–40% of ecommerce orders require splitting", "~12,000–17,000 split orders/month", "Order Management System", "OMS, DC Ops, Store Ops, Logistics",
         [("System splits order by fulfillment source: (a) store-pickable items → BOPIS/ship-from-store, (b) DC items → DC fulfillment, (c) vendor items → drop-ship, (d) dark store items → micro-fulfillment; creates sub-orders per source with linked parent order", "System", "Ecom Ops Manager", "Automated"),
          ("System communicates split to customer: shows estimated delivery per sub-order, provides combined tracking, manages single payment across sub-orders", "System", "Customer", "Automated")]),
        ("Ship-from-Store Order Processing", "Order routed to store for fulfillment", "~8,000–12,000 ship-from-store orders/month", "~8K–12K/month", "Store Stock Associate", "Stock Associate, Store Manager, Logistics",
         [("System generates pick list at store; Stock Associate picks items from shelf; packs for shipment; system generates shipping label; schedules pickup by 3PL partner per VS-56", "Stock Associate", "Store Manager", "15–30 min/order"),
          ("3PL picks up packed order; system updates tracking; customer receives shipment notification; delivery completed within 2–3 days", "Logistics / System", "Customer", "2–3 days")]),
        ("Vendor Drop-Ship Order Processing", "Order routed to vendor for direct shipment to customer", "~2,000–4,000 drop-ship orders/month", "~2K–4K/month; primarily bulky items and appliances", "Vendor Management Coordinator", "Vendor Coord, Vendor, Customer Service",
         [("System creates drop-ship PO to vendor with customer delivery address; vendor confirms acceptance within 24 hours; ships directly to customer with BuildRight-branded packaging", "System / Vendor", "Vendor Coord", "1–2 days"),
          ("System tracks vendor shipment; customer receives BuildRight tracking; vendor confirms delivery; system closes order; revenue recognized by BuildRight", "System / Vendor", "Finance", "3–7 days")]),
        ("Inventory Reservation & Allocation for Orders", "Order placed that reserves inventory at a source", "~46,400 orders/month requiring inventory reservation", "~46,400 reservations/month", "Order Management System", "OMS, Inventory System, DC Ops, Store Ops",
         [("System reserves inventory at selected source: decrements available-to-promise (ATP) quantity; prevents double-selling; holds reservation for fulfillment window (BOPIS: 5 days, delivery: 24 hours)", "System", "Inventory Manager", "Automated"),
          ("If reservation expires (BOPIS not picked up in 5 days): system cancels order, restores inventory, processes refund; re-routes to alternative if customer requests", "System", "Customer Service", "Automated")]),
        ("Order Routing Exception Management", "Routing failure or source becomes unavailable", "~2,000–3,000 routing exceptions/month", "~2K–3K/month (~5%)", "Ecommerce Operations Manager", "Ecom Ops Mgr, Store Ops, DC Ops, CS",
         [("System detects routing exception: (a) source stock-out after reservation, (b) store unable to fulfill (staffing, closure), (c) vendor rejection, (d) system error", "System", "Ecom Ops Manager", "Real-time"),
          ("Ecom Ops Manager manually re-routes: identifies alternative source, communicates revised timeline to customer, adjusts fulfillment plan; systemic issues escalated to IT", "Ecom Ops Manager", "VP Marketing", "15–30 min/exception")]),
        ("Fulfillment Priority & SLA Management", "Order routing prioritization rules", "Monthly rule review; continuous monitoring", "~46,400 orders/month with SLA tracking", "Ecommerce Operations Manager", "Ecom Ops Mgr, Logistics, Customer Service",
         [("System enforces SLA by order type: (a) BOPIS: ready in 4 hours, (b) Metro delivery: 2 days, (c) Provincial delivery: 5 days, (d) Drop-ship: 7 days; prioritizes routing accordingly", "System", "Ecom Ops Manager", "Automated"),
          ("Daily: monitors SLA compliance; flags orders at risk of breach; triggers escalation to alternate fulfillment source or expedited shipping", "System / Ecom Ops Mgr", "VP Marketing", "1–2 hours/day")]),
        ("Order Routing Cost Optimization", "Monthly cost analysis", "Monthly; ~46,400 routed orders", "~46,400 orders/month with cost tracking", "Logistics Finance Analyst", "Logistics Finance Analyst, Ecom Ops Mgr, FP&A",
         [("Analyst calculates fulfillment cost per channel: store-pick cost, DC fulfillment cost, drop-ship cost, last-mile delivery cost; identifies cost-optimized routing patterns", "Logistics Finance Analyst", "Finance Manager", "4–6 hours/month"),
          ("Recommends routing rule adjustments to minimize cost while maintaining SLA; tests proposed changes in simulation before production deployment", "Logistics Finance Analyst", "Ecom Ops Manager", "2–3 hours/month")])
     ]),
     ("PA-60.2", "split-order-fulfillment", "Split-Order & Mixed-Basket Fulfillment", [
        ("Multi-Source Fulfillment Coordination", "Split order requires coordination across multiple sources", "~12,000–17,000 multi-source orders/month", "~12K–17K/month", "Order Management System", "OMS, Store Ops, DC Ops, Vendors, Logistics",
         [("System orchestrates multi-source fulfillment: (a) triggers pick at store, (b) triggers pick at DC, (c) sends drop-ship PO to vendor; tracks all sub-orders against parent order completion", "System", "Ecom Ops Manager", "Automated"),
          ("System determines customer delivery strategy: (a) consolidate at DC then single delivery, (b) separate deliveries from each source, (c) consolidate at store for customer pickup", "System", "Logistics Manager", "Automated")]),
        ("Consolidated Delivery Management", "Multiple sub-orders consolidated for single delivery", "~5,000–8,000 consolidated deliveries/month", "~5K–8K/month", "Logistics Coordinator", "Logistics Coord, DC Ops, 3PL Partners",
         [("System identifies consolidation opportunities: sub-orders from same DC going to same customer; holds first sub-order for consolidation window (24 hours); ships together", "System", "DC Operations", "Automated"),
          ("Reduces delivery cost (one vs. multiple deliveries) and improves customer experience (single delivery); tracks consolidation rate as fulfillment KPI", "Logistics Coord", "Ecom Ops Manager", "Ongoing")]),
        ("Split Order Customer Communication", "Order split into multiple shipments", "~12,000–17,000 customer notifications/month", "~12K–17K/month", "Customer Communication System", "Communication System, Customer Service",
         [("System sends proactive communication: explains order split, provides sub-order tracking numbers, estimated delivery dates per sub-order, single customer service contact", "System", "Customer", "Automated"),
          ("Customer can view combined order status in app/web; single view showing all sub-orders with real-time status; customer service has unified view for inquiries", "System", "Customer Service", "Automated")]),
        ("Partial Order Cancellation & Modification", "Customer wants to cancel/modify part of split order", "~1,500–2,500 partial cancellations/month", "~1.5K–2.5K/month", "Customer Service Agent", "CSA, OMS, Inventory System, Finance",
         [("CSA processes partial cancellation: system cancels specific sub-order(s), restores inventory at source, processes partial refund, keeps remaining sub-orders active", "CSA / System", "CS Supervisor", "10–15 min"),
          ("Finance adjusts: partial refund to customer, revenue recognition only for fulfilled items, promotional coupon adjustments if threshold no longer met", "Finance / System", "Finance Manager", "5 min")]),
        ("Backorder Management in Split Orders", "One or more items in split order become unavailable", "~1,000–2,000 backorder situations/month", "~1K–2K/month", "Order Management System", "OMS, Customer Service, Merch Planner",
         [("System detects backorder: item reserved but source now out-of-stock; evaluates alternatives: (a) different source with stock, (b) substitute item, (c) partial shipment + backorder remainder", "System", "Ecom Ops Manager", "Automated"),
          ("Customer notified of options; chooses partial shipment now + backorder later, substitute, or cancel backordered item; system adjusts order accordingly", "System / Customer", "CSA", "5–10 min")]),
        ("Cross-Entity Fulfillment Coordination", "Order requires fulfillment across BuildRight entities", "~8,000–12,000 cross-entity orders/month", "~8K–12K/month (Depot Inc. + Digital Commerce Inc.)", "Finance Manager", "Finance Mgr, Ecom Ops, Intercompany Accountant",
         [("System manages cross-entity fulfillment: (a) BuildRight Depot Inc. inventory used to fulfill BuildRight Digital Commerce Inc. order, (b) intercompany transfer pricing applied, (c) revenue recognized by selling entity per intercompany agreement", "System", "Finance Manager", "Automated"),
          ("Monthly: Finance reconciles intercompany fulfillment volumes and transfer pricing; ensures proper consolidation elimination per VS-17", "Finance Manager", "CFO", "4–6 hours/month")]),
        ("Fulfillment Quality Control", "Random quality check on shipped orders", "Weekly; ~100 random checks/week", "~100 checks/week across all sources", "Ecommerce Quality Coordinator", "Ecom Quality Coord, Store Ops, DC Ops",
         [("Coordinator randomly selects 100 orders/week for quality audit: verifies correct items picked, correct quantities, proper packaging, accurate shipping label, timely dispatch", "Ecom Quality Coord", "Ecom Ops Manager", "4–6 hours/week"),
          ("Tracks quality score by source (store vs. DC vs. vendor); identifies sources with >2% error rate for corrective action", "Ecom Quality Coord", "VP Supply Chain", "2–3 hours/week")]),
        ("Same-Day & Express Fulfillment Processing", "Customer selects same-day or express delivery option", "~3,000–5,000 express orders/month (growing)", "~3K–5K/month; premium delivery fee applied", "Ecommerce Operations Manager", "Ecom Ops Mgr, Store Ops, 3PL Partners",
         [("System routes same-day orders only to stores within delivery radius with confirmed stock; cutoff at 12:00 PM for same-day; uses premium 3PL partners (GrabExpress, Lalamove Priority)", "System", "Ecom Ops Manager", "Automated"),
          ("Store must pick and pack within 2 hours; 3PL pickup within 1 hour of pack-ready; delivery within 4 hours of pickup; SLA tracked separately with premium KPI targets", "Store Staff / 3PL", "Ecom Ops Manager", "Same day")])
     ]),
     ("PA-60.3", "fulfillment-performance-analytics", "Fulfillment Performance & Optimization Analytics", [
        ("Fulfillment KPI Dashboard", "Real-time monitoring; monthly deep analysis", "Real-time; monthly comprehensive", "Full omnichannel fulfillment: ~46,400 orders/month", "Ecommerce Operations Manager", "Ecom Ops Mgr, VP Marketing, VP Supply Chain",
         [("Dashboard tracks: (a) order fill rate by source, (b) SLA compliance, (c) split order rate, (d) fulfillment cost per order, (e) customer satisfaction by fulfillment type, (f) return rate by fulfillment source", "System", "Ecom Ops Manager", "Automated"),
          ("Daily: Ecom Ops reviews dashboard, flags KPIs below target. Monthly: comprehensive analysis with root cause and corrective action plan", "Ecom Ops Manager", "VP Marketing", "2–3 hours/day + 4–6 hours/month")]),
        ("Source Performance Comparison", "Monthly comparison", "Monthly", "4 fulfillment sources: store, DC, vendor, dark store", "Analytics Manager", "Analytics Mgr, Ecom Ops Mgr, VP Marketing",
         [("Analytics Manager compares fulfillment sources: cost per order, speed (hours to ship), accuracy (%), customer satisfaction (NPS), return rate; identifies best-performing source by order type", "Analytics Manager", "Ecom Ops Manager", "4–6 hours/month"),
          ("Recommends volume reallocation to highest-performing sources; identifies sources needing improvement; presents findings to VP Marketing and VP Supply Chain", "Analytics Manager", "VP Marketing", "2–3 hours/month")]),
        ("Order Routing Algorithm Optimization", "Quarterly algorithm review and tuning", "Quarterly", "Routing algorithm serving ~46,400 orders/month", "IT Data Science Lead", "Data Science Lead, Ecom Ops Mgr, IT Integration",
         [("Data Science Lead reviews routing algorithm performance: accuracy of source selection, SLA achievement rate, cost optimization effectiveness; A/B tests alternative routing strategies", "Data Science Lead", "CIO", "5–10 days/quarter"),
          ("Implements algorithm improvements: adjusts weightings (speed vs. cost vs. accuracy), adds new data inputs (weather, traffic, real-time stock), deploys to production after testing", "Data Science Lead", "Ecom Ops Manager", "3–5 days")]),
        ("Customer Delivery Experience Analysis", "Monthly customer experience review", "Monthly; post-delivery survey data", "~42,900 ecommerce customers/month", "Customer Experience Manager", "CX Manager, Ecom Ops, Logistics, Marketing",
         [("CX Manager analyzes post-delivery CSAT and NPS: by fulfillment source, by delivery partner, by region, by order type (BOPIS vs. delivery vs. split); identifies bottom-performing combinations", "CX Manager", "VP Marketing", "4–6 hours/month"),
          ("Presents findings with recommendations: improve specific store fulfillment training, switch underperforming 3PL partner, adjust SLA targets for provincial deliveries", "CX Manager", "Ecom Ops Manager", "2–3 hours/month")]),
        ("Omnichannel Inventory Visibility Monitoring", "Daily monitoring; weekly analysis", "Daily; 200 stores + 4 DCs", "~35,000 SKUs across 204 locations", "Inventory Manager", "Inventory Mgr, Ecom Ops, IT Integration",
         [("System monitors real-time inventory sync: POS sales reducing available inventory, DC inventory updates, store-level ATP accuracy; flags sync delays >30 minutes", "System", "Inventory Manager", "Real-time"),
          ("Weekly: Inventory Manager analyzes sync accuracy: % of time inventory data is accurate across channels; identifies SKUs with frequent ATP discrepancies; escalates persistent issues to IT", "Inventory Manager", "VP Supply Chain", "2–3 hours/week")]),
        ("Fulfillment Capacity Planning", "Quarterly capacity review", "Quarterly; peak season preparation", "4 DCs + 200 stores + vendor capacity", "VP Supply Chain", "VP Supply Chain, Ecom Ops Mgr, DC Ops, Store Ops",
         [("VP Supply Chain forecasts fulfillment capacity needs: peak season volume growth, new store additions, dark store capacity (VS-49), vendor drop-ship expansion; identifies bottlenecks", "VP Supply Chain", "COO", "3–5 days/quarter"),
          ("Develops capacity expansion plan: store fulfillment staff augmentation, DC overtime, additional 3PL capacity, vendor capacity commitments; presents to COO for approval", "VP Supply Chain", "COO", "2–3 days")]),
        ("Return Rate by Fulfillment Source Analysis", "Monthly analysis", "Monthly", "~5–8% ecommerce return rate", "Returns Manager", "Returns Mgr, Ecom Ops Mgr, Quality Manager",
         [("Returns Manager analyzes return reasons by fulfillment source: wrong item, damaged, quality issue, customer changed mind; identifies sources with highest return rates", "Returns Manager", "Ecom Ops Manager", "4–6 hours/month"),
          ("Implements corrective actions: additional quality checks at high-return stores, improved packaging standards, vendor quality reviews for drop-ship returns per VS-31", "Returns Manager", "VP Supply Chain", "2–3 hours/month")]),
        ("Omnichannel Fulfillment Strategy Annual Review", "Annual strategy review", "Annual", "Full omnichannel fulfillment strategy", "VP Marketing / VP Supply Chain", "VP Marketing, VP Supply Chain, COO, CIO, CFO",
         [("VP Marketing and VP Supply Chain jointly review omnichannel fulfillment strategy: channel mix, fulfillment source allocation, cost structure, SLA targets, customer satisfaction, competitive positioning", "VP Marketing / VP Supply Chain", "CEO", "3–5 days"),
          ("CIO presents technology roadmap for fulfillment optimization; CFO presents financial impact; COO approves operational plan for next fiscal year", "CIO / CFO / COO", "CEO", "2–3 days")])
     ])
    ),
    ("VS-61-fuel-fleet-cost-management", 61, "Fuel & Fleet Cost Management", "Make & Move",
     "Manages BuildRight's fleet fuel procurement and consumption, toll expenses, and total fleet cost optimization. Covers the owned fleet (20% of trucks) and fuel cost monitoring for 3PL partners. With 4 DCs serving 200 stores across the Philippine archipelago, fuel and toll costs represent ~15–20% of total logistics spend.",
     [("PA-61.1", "fuel-procurement-consumption", "Fuel Procurement & Consumption Management", [
        ("Fleet Fuel Card Program Management", "Fuel procurement for owned fleet", "Continuous; ~20 owned trucks", "~20 fuel cards; ~PHP 2–3M/month fuel spend", "Logistics Manager", "Logistics Mgr, Drivers, Finance",
         [("Logistics Manager manages fleet fuel card program: issues fuel cards per vehicle, sets per-transaction limits, monitors usage patterns, blocks unauthorized fuel types or stations", "Logistics Manager", "VP Supply Chain", "2–3 hours/month"),
          ("Monthly: Finance reviews fuel card statements, matches to vehicle mileage logs, investigates anomalies (excessive consumption, off-route purchases, off-hours usage)", "Finance", "Logistics Manager", "4–6 hours/month")]),
        ("Fuel Price Monitoring & Procurement Optimization", "Weekly fuel price review", "Weekly; Philippine diesel/gasoline prices", "Weekly monitoring; ~PHP 2–3M monthly spend", "Logistics Finance Analyst", "Logistics Finance Analyst, Logistics Mgr, Procurement",
         [("Analyst monitors Philippine fuel prices: tracks DOE (Department of Energy) weekly price adjustments; identifies optimal fueling stations per route; calculates impact on delivery cost", "Logistics Finance Analyst", "Finance Manager", "2–3 hours/week"),
          ("Procurement negotiates fleet fuel discounts with major stations (Petron, Shell, Caltex) for volume commitments; evaluates fuel card provider benefits", "Procurement", "Logistics Manager", "1–2 days/quarter")]),
        ("Vehicle Fuel Efficiency Monitoring", "Monthly vehicle performance review", "Monthly; ~20 owned vehicles", "~20 vehicle efficiency reports/month", "Fleet Supervisor", "Fleet Supervisor, Logistics Manager",
         [("Fleet Supervisor calculates fuel efficiency per vehicle: liters consumed ÷ km driven; benchmarks vs. vehicle specification; flags vehicles with >15% deviation from expected efficiency", "Fleet Supervisor", "Logistics Manager", "4–6 hours/month"),
          ("Investigates inefficient vehicles: engine issues, tire pressure, route congestion, driver behavior; schedules maintenance or driver coaching", "Fleet Supervisor", "Maintenance Coord", "2–3 hours/month")]),
        ("Fuel Consumption Reporting & Analytics", "Monthly reporting", "Monthly; 4 DCs × ~5 vehicles each", "~20 vehicles analyzed monthly", "Logistics Finance Analyst", "Logistics Finance Analyst, VP Supply Chain, CFO",
         [("Analyst produces monthly fuel consumption report: total spend, per-vehicle cost, per-delivery cost, fuel as % of logistics cost, trend vs. prior months and budget", "Logistics Finance Analyst", "Finance Manager", "4–6 hours/month"),
          ("VP Supply Chain reviews with COO; identifies cost reduction opportunities: route optimization, fuel-efficient vehicles, electric vehicle pilot for short-range deliveries", "VP Supply Chain", "COO", "1–2 hours/month")]),
        ("Driver Fuel Efficiency Training", "Quarterly or new driver onboarding", "Quarterly + new hires", "~60 owned-fleet drivers", "Fleet Supervisor", "Fleet Supervisor, HR Training",
         [("Fleet Supervisor conducts fuel efficiency training: (a) optimal gear shifting, (b) steady speed maintenance, (c) idling reduction, (d) route planning, (e) tire pressure awareness", "Fleet Supervisor", "Logistics Manager", "2–3 hours/session"),
          ("Monthly: recognizes most fuel-efficient driver; links fuel efficiency to driver performance scorecard and incentive program", "Logistics Manager", "HR", "1 hour/month")]),
        ("Alternative Fuel Vehicle Evaluation", "Annual fleet strategy review", "Annual; or when EV market develops in Philippines", "20 owned vehicles; evaluate 2–3 replacements/year", "VP Supply Chain", "VP Supply Chain, Fleet Supervisor, Finance, COO",
         [("VP Supply Chain evaluates alternative fuel options: (a) electric vehicles for short-range DC-to-nearby-store deliveries, (b) hybrid vehicles for medium-range, (c) LPG/CNG for high-volume routes", "VP Supply Chain", "COO", "3–5 days/year"),
          ("Finance calculates TCO comparison: acquisition cost, fuel savings, maintenance savings, charging infrastructure cost, government incentives (if any); recommends pilot if positive ROI", "Finance", "CFO", "2–3 days")]),
        ("Fuel Cost Pass-Through to 3PL Partners", "Significant fuel price change (>5%)", "Ad-hoc; ~2–4 times/year", "~10–15 3PL partners affected", "Logistics Manager", "Logistics Mgr, Procurement, Finance, 3PL Partners",
         [("Logistics Manager activates fuel cost adjustment clause in 3PL contracts: adjusts per-delivery rates based on fuel price change; calculates impact using standard fuel cost component formula", "Logistics Manager", "Procurement", "1–2 days"),
          ("Finance validates adjustment; communicates to 3PL partners; implements rate change in ERP; monitors delivery cost impact", "Finance", "CFO", "1 day")]),
        ("Emergency Fuel Supply Management", "Fuel supply disruption (typhoon, geopolitical)", "Ad-hoc; ~1–2 times/year in Philippines (typhoon season)", "1–2 events/year potentially affecting fleet operations", "Logistics Manager", "Logistics Mgr, VP Supply Chain, Procurement, COO",
         [("Logistics Manager activates emergency fuel plan: (a) tops off all vehicle tanks at first warning, (b) activates backup fuel supplier contracts, (c) prioritizes essential deliveries (food/water/relief items if applicable)", "Logistics Manager", "VP Supply Chain", "4–8 hours"),
          ("Post-event: assesses fuel supply normalization; adjusts delivery schedule to clear backlog; reviews emergency plan effectiveness", "Logistics Manager", "COO", "1–2 days")])
     ]),
     ("PA-61.2", "toll-route-cost", "Toll, Parking & Route Cost Management", [
        ("Toll Expense Management & Optimization", "Monthly toll expense review", "Monthly; routes across Luzon, Visayas, Mindanao expressways", "~PHP 1–2M/month toll expenses", "Logistics Finance Analyst", "Logistics Finance Analyst, Fleet Supervisor, Logistics Mgr",
         [("Analyst tracks toll expenses per route: identifies toll roads vs. free alternative routes; calculates time saved vs. additional toll cost; recommends optimal route per delivery window", "Logistics Finance Analyst", "Logistics Manager", "4–6 hours/month"),
          ("Fleet Supervisor implements route decisions: use toll roads for time-sensitive deliveries (SLA-critical), use free roads for non-urgent or backhaul trips", "Fleet Supervisor", "Logistics Manager", "Ongoing")]),
        ("RFID/EasyTrip Fleet Toll Account Management", "Monthly account management", "Monthly; ~20 vehicles with RFID toll stickers", "~20 RFID accounts", "Fleet Supervisor", "Fleet Supervisor, Finance",
         [("Fleet Supervisor manages RFID toll accounts: loads credits, monitors balances, replaces defective stickers, reconciles monthly statements vs. system records", "Fleet Supervisor", "Logistics Manager", "2–3 hours/month"),
          ("Finance reconciles toll expenses: RFID statement vs. ERP toll cost entries; investigates discrepancies", "Finance", "Fleet Supervisor", "2–3 hours/month")]),
        ("Parking & Loading Dock Fee Management", "Monthly review", "Monthly; urban delivery locations (Metro Manila, Cebu)", "~PHP 200K–500K/month parking/loading fees", "Logistics Finance Analyst", "Logistics Finance Analyst, DC Dispatch, Store Ops",
         [("Analyst tracks parking and loading dock fees: identifies stores and delivery points with frequent parking charges; evaluates loading dock reservation programs for frequent delivery locations", "Logistics Finance Analyst", "Logistics Manager", "2–3 hours/month"),
          ("Coordinates with Store Ops for reserved delivery windows at high-traffic urban stores to minimize wait time and parking fees", "Logistics Manager", "Store Ops Director", "1–2 hours/month")]),
        ("Route Cost Benchmarking", "Quarterly benchmarking", "Quarterly; major delivery routes", "~20–30 primary routes benchmarked", "Logistics Manager", "Logistics Mgr, Finance, 3PL Partners",
         [("Logistics Manager benchmarks route costs: BuildRight per-km cost vs. industry average; toll vs. no-toll route cost; owned fleet vs. 3PL cost per route", "Logistics Manager", "VP Supply Chain", "2–3 days/quarter"),
          ("Identifies cost optimization opportunities: route consolidation, backhaul utilization, alternate route testing, delivery window optimization", "Logistics Manager", "DC Operations", "1–2 days")]),
        ("Backhaul Utilization & Revenue", "Monthly backhaul analysis", "Monthly; ~400–500 return trips from store to DC empty", "~400–500 empty backhaul trips/month", "Logistics Manager", "Logistics Mgr, DC Ops, Store Ops",
         [("Logistics Manager identifies backhaul opportunities: (a) store returns to DC (VS-32), (b) inter-DC transfers (VS-05), (c) vendor pickup from store, (d) third-party freight for other companies", "Logistics Manager", "DC Operations", "4–6 hours/month"),
          ("Targets reducing empty backhaul from current ~60% to <40%; tracks backhaul utilization rate as fleet efficiency KPI", "Logistics Manager", "VP Supply Chain", "2–3 hours/month")]),
        ("Fleet Insurance Cost Management", "Annual insurance renewal", "Annual; ~20 owned vehicles", "~20 vehicle insurance policies", "Finance Manager", "Finance Mgr, Logistics Mgr, Insurance Provider",
         [("Finance Manager manages fleet insurance: obtains competitive quotes annually, reviews coverage adequacy, processes claims per VS-26, manages no-claims bonuses", "Finance Manager", "CFO", "3–5 days/year"),
          ("Logistics Manager maintains driver safety records to support favorable insurance rates; implements driver safety programs", "Logistics Manager", "Finance Manager", "Ongoing")]),
        ("Vehicle Maintenance Cost Tracking", "Monthly maintenance review", "Monthly; ~20 owned vehicles", "~20 vehicle maintenance records/month", "Fleet Supervisor", "Fleet Supervisor, Logistics Mgr, Finance",
         [("Fleet Supervisor tracks per-vehicle maintenance costs: scheduled maintenance (oil change, tires, brakes), unscheduled repairs, accident repairs; calculates per-km maintenance cost", "Fleet Supervisor", "Logistics Manager", "4–6 hours/month"),
          ("Finance includes maintenance costs in total fleet cost of ownership; compares vs. industry benchmarks; recommends vehicle replacement when maintenance cost exceeds depreciation savings", "Finance", "VP Supply Chain", "2–3 hours/month")]),
        ("Total Fleet Cost of Ownership Dashboard", "Monthly dashboard", "Monthly; ~20 owned vehicles + 3PL costs", "~20 owned + 10–15 3PL partners tracked", "VP Supply Chain", "VP Supply Chain, Finance Dir, COO",
         [("Dashboard shows: total fleet cost (owned + 3PL), cost per delivery, cost per km, cost per peso of goods delivered, fuel %, toll %, maintenance %, insurance %", "System", "VP Supply Chain", "Automated"),
          ("VP Supply Chain reviews with COO monthly; targets total logistics cost at 8–10% of COGS; adjusts fleet strategy if exceeding target", "VP Supply Chain", "COO", "2–3 hours/month")])
     ]),
     ("PA-61.3", "fleet-total-cost-analytics", "Fleet Total Cost of Ownership Analytics", [
        ("Annual Fleet TCO Analysis", "Annual budget cycle", "Annual; full fleet", "20 owned vehicles comprehensive TCO", "Finance Director", "Finance Dir, VP Supply Chain, COO",
         [("Finance Director calculates annual TCO per vehicle: depreciation + fuel + maintenance + insurance + tolls + driver costs + overhead; compares vs. 3PL cost for same routes", "Finance Director", "CFO", "5–10 days"),
          ("VP Supply Chain presents fleet strategy recommendation: own vs. outsource by route; vehicle replacement schedule; new vehicle acquisition plan", "VP Supply Chain", "COO", "3–5 days")]),
        ("Vehicle Replacement Cost-Benefit Analysis", "Vehicle reaches replacement criteria (age/mileage/cost)", "2–3 evaluations/year", "~2–3 vehicle replacement decisions/year", "Fleet Supervisor", "Fleet Supervisor, Finance, VP Supply Chain",
         [("Fleet Supervisor identifies replacement candidates: vehicles >8 years old, >300,000 km, or maintenance cost >30% of vehicle value; Finance calculates replacement vs. continued maintenance cost", "Fleet Supervisor / Finance", "VP Supply Chain", "3–5 days"),
          ("VP Supply Chain recommends replacement model; Finance approves budget; Procurement sources vehicle; Fleet Supervisor manages transition", "VP Supply Chain", "COO", "2–3 days")]),
        ("Fleet Utilization Rate Analysis", "Monthly utilization review", "Monthly; ~20 vehicles", "~20 utilization reports/month", "Fleet Supervisor", "Fleet Supervisor, Logistics Manager",
         [("Fleet Supervisor calculates fleet utilization: (a) % of available hours actually delivering, (b) % of capacity (weight/volume) utilized per trip, (c) idle time per vehicle per day", "Fleet Supervisor", "Logistics Manager", "4–6 hours/month"),
          ("Identifies underutilized vehicles for redeployment or disposal; targets ≥75% utilization rate for owned fleet", "Fleet Supervisor", "VP Supply Chain", "2–3 hours/month")]),
        ("Fleet Carbon Footprint Estimation", "Annual sustainability reporting per VS-25", "Annual", "20 owned vehicles + 3PL partners", "ESG Manager", "ESG Manager, Logistics Mgr, VP Supply Chain",
         [("ESG Manager calculates fleet carbon footprint: fuel consumption × emission factor per fuel type; estimates 3PL partner emissions based on delivery volume and average emission per km", "ESG Manager", "VP Supply Chain", "3–5 days/year"),
          ("Identifies reduction opportunities: route optimization, fuel-efficient vehicles, alternative fuels, load optimization; feeds into ESG reporting per VS-25", "ESG Manager", "VP Supply Chain", "2–3 days")]),
        ("Fleet Safety Cost Analysis", "Quarterly safety review", "Quarterly", "~20 vehicles; accident/incident records", "Safety Officer", "Safety Officer, Logistics Mgr, Finance",
         [("Safety Officer analyzes fleet safety costs: accident repair costs, cargo damage claims, insurance premium impact, driver injury costs, third-party liability costs", "Safety Officer", "Logistics Manager", "4–6 hours/quarter"),
          ("Recommends safety improvements: driver training, vehicle safety features, route risk assessment; tracks safety cost trend quarterly", "Safety Officer", "VP Supply Chain", "2–3 hours/quarter")]),
        ("3PL Cost Benchmarking & Negotiation", "Quarterly 3PL cost review", "Quarterly; ~10–15 3PL partners", "~10–15 partner rates benchmarked quarterly", "Procurement Manager", "Procurement Mgr, Logistics Mgr, Finance",
         [("Procurement benchmarks 3PL rates against market: per-km, per-delivery, per-kg; identifies partners above market rate; negotiates rate reductions or switches partners", "Procurement", "Logistics Manager", "2–3 days/quarter"),
          ("Finance validates savings projections; Logistics Manager plans partner transition if needed per VS-56", "Finance / Logistics Mgr", "VP Supply Chain", "1–2 days")]),
        ("Logistics Cost as % of Revenue Analysis", "Monthly KPI tracking", "Monthly", "Full logistics spend vs. total revenue", "FP&A Director", "FP&A Dir, VP Supply Chain, CFO, COO",
         [("FP&A calculates logistics cost as % of revenue and % of COGS monthly; tracks trend; benchmarks vs. Philippine retail industry (typically 8–12% of COGS for big-box retail)", "FP&A Director", "CFO", "2–3 hours/month"),
          ("Presents to COO with variance analysis: fuel cost changes, volume changes, rate changes, efficiency improvements/deterioration", "FP&A Director", "COO", "1–2 hours/month")]),
        ("5-Year Fleet Investment Plan", "Annual capital planning cycle", "Annual; 5-year horizon", "20 vehicles + growth fleet needs", "VP Supply Chain / CFO", "VP Supply Chain, CFO, COO, CEO",
         [("VP Supply Chain and CFO develop 5-year fleet investment plan: vehicle replacement schedule, fleet expansion for store growth (10–15 new stores/year), technology investments (GPS, telematics, EV charging)", "VP Supply Chain / CFO", "CEO", "5–10 days"),
          ("CEO and Board approve capital allocation; plan feeds into annual Capex budget per VS-40", "CEO / Board", "CFO", "2–3 days")])
     ])
    ),
]

# Now generate all files
def main():
    import importlib
    # Import the main script's ALL_VS and append
    sys.path.insert(0, '/home/riddler/erpplans')
    
    # Read the main script
    exec(open('/home/riddler/erpplans/generate_vs53_68.py').read(), globals())
    
    # Append extra VS
    for vs in EXTRA_VS:
        ALL_VS.append(vs)
    for vs in REMAINING:
        ALL_VS.append(vs)
    
    # Re-run main
    # Reset output
    wf_id = 2118
    grand_total = 0
    
    for vs_data in ALL_VS:
        vs_dir, vs_num, vs_name, family, overview, pas = vs_data
        
        vs_path = os.path.join(BASE, vs_dir)
        os.makedirs(vs_path, exist_ok=True)
        
        pa_summaries = []
        vs_total = 0
        
        for pa_data in pas:
            pa_num, pa_slug, pa_title, workflows = pa_data
            
            toc = []
            wf_blocks = []
            
            for wf in workflows:
                name, trigger, freq, vol, owner, participants, steps = wf
                wid = wf_id
                wf_id += 1
                
                anchor = f"w{wid}-{name.lower().replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '').replace(',', '').replace('&', '').replace('--', '-')[:60]}"
                toc.append(f"- [W{wid}. {name}](#{anchor})")
                
                step_rows = ""
                for i, step in enumerate(steps, 1):
                    if len(step) >= 4:
                        step_rows += f"| {i} | {step[0]} | {step[1]} | {step[2]} | {step[3]} |\n"
                
                block = f"""## W{wid}. {name}

| Field | Detail |
|---|---|
| **Trigger** | {trigger} |
| **Frequency** | {freq} |
| **Volume** | {vol} |
| **Owner** | {owner} |
| **Participants** | {participants} |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
{step_rows}
### System Touchpoints
- ERP integration point (W{wid})
- Related workflows in VS-{vs_num} and connected value streams

### Pain Points / Risks
- **Execution risk**: Operational variability mitigated by standard procedures and system controls

### Time Estimate
- 30–120 min per occurrence

"""
                wf_blocks.append(block)
            
            count = len(workflows)
            pa_content = f"""# {pa_num} — {pa_title}

> Part of **[VS-{vs_num}: {vs_name}](./README.md)** ({family}) · [Value Stream Index](../value-stream-index.md)

---

## Workflows in This Process Area

{chr(10).join(toc)}

{"".join(wf_blocks)}*Workflow Count: {count} · Back to **[VS-{vs_num}: {vs_name}](./README.md)** · [Value Stream Index](../value-stream-index.md)*
"""
            pa_file = os.path.join(vs_path, f"{pa_num}-{pa_slug}.md")
            with open(pa_file, 'w') as f:
                f.write(pa_content)
            
            pa_summaries.append((pa_num, pa_title, count, pa_slug))
            vs_total += count
        
        pa_rows = []
        for pn, pt, pc, ps in pa_summaries:
            pa_rows.append(f"| [{pn}]({pn}-{ps}.md) | {pt} | {pc} |")
        pa_rows.append(f"| | **Total** | **{vs_total}** |")
        
        readme = f"""# VS-{vs_num}: {vs_name}

> **{family}** · [Value Stream Index](../value-stream-index.md)

## Overview

{overview}

## Process Areas

| PA | Name | Workflows |
|---|---|---|
{chr(10).join(pa_rows)}

---

*Back to [Value Stream Index](../value-stream-index.md)*
"""
        with open(os.path.join(vs_path, "README.md"), 'w') as f:
            f.write(readme)
        
        grand_total += vs_total
        print(f"VS-{vs_num}: {vs_name} — {vs_total} workflows")
    
    print(f"\nGrand total new: {grand_total}")
    print(f"Updated total: {2122 + grand_total}")

if __name__ == "__main__":
    main()
