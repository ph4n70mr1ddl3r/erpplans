#!/usr/bin/env python3
"""Generate VS-56 through VS-61 directly."""
import os

BASE = "/home/riddler/erpplans/01-model-company/workflows"
wf_counter = 2118 + 72  # After VS-55's 72 workflows

def next_id():
    global wf_counter
    wid = wf_counter
    wf_counter += 1
    return wid

def write_pa(vs_dir, vs_num, vs_name, family, pa_num, pa_slug, pa_title, workflows):
    toc = []
    wf_blocks = []
    for name, trigger, freq, vol, owner, participants, steps in workflows:
        wid = next_id()
        anchor = f"w{wid}-{name.lower().replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '').replace(',', '').replace('&', '').replace('--', '-')[:60]}"
        toc.append(f"- [W{wid}. {name}](#{anchor})")
        step_rows = ""
        for i, (act, r, a, dur) in enumerate(steps, 1):
            step_rows += f"| {i} | {act} | {r} | {a} | {dur} |\n"
        wf_blocks.append(f"""## W{wid}. {name}

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

""")
    
    count = len(workflows)
    path = os.path.join(BASE, vs_dir, f"{pa_num}-{pa_slug}.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(f"""# {pa_num} — {pa_title}

> Part of **[VS-{vs_num}: {vs_name}](./README.md)** ({family}) · [Value Stream Index](../value-stream-index.md)

---

## Workflows in This Process Area

{chr(10).join(toc)}

{"".join(wf_blocks)}*Workflow Count: {count} · Back to **[VS-{vs_num}: {vs_name}](./README.md)** · [Value Stream Index](../value-stream-index.md)*
""")
    return count

def write_readme(vs_dir, vs_num, vs_name, family, overview, pa_summaries):
    rows = []
    total = 0
    for pn, pt, pc, ps in pa_summaries:
        rows.append(f"| [{pn}]({pn}-{ps}.md) | {pt} | {pc} |")
        total += pc
    rows.append(f"| | **Total** | **{total}** |")
    with open(os.path.join(BASE, vs_dir, "README.md"), 'w') as f:
        f.write(f"""# VS-{vs_num}: {vs_name}

> **{family}** · [Value Stream Index](../value-stream-index.md)

## Overview

{overview}

## Process Areas

| PA | Name | Workflows |
|---|---|---|
{chr(10).join(rows)}

---

*Back to [Value Stream Index](../value-stream-index.md)*
""")
    return total

grand = 0

# ═══ VS-56 ═══
vs_dir = "VS-56-third-party-delivery-partner"
vs_num = 56; vs_name = "Third-Party Delivery Partner Management"; family = "Make & Move"
overview = "Manages BuildRight's relationships with third-party logistics (3PL) partners for last-mile delivery, including Lalamove, Transportify, GrabExpress, and owned fleet coordination. Covers partner onboarding, performance monitoring, SLA management, settlement, and cost optimization. BuildRight uses 80% third-party trucks for DC-to-store and customer deliveries."

pa_summaries = []
pa_summaries.append(("PA-56.1", "3PL Partner Onboarding & Qualification", 
    write_pa(vs_dir, vs_num, vs_name, family, "PA-56.1", "3pl-partner-onboarding-qualification", "3PL Partner Onboarding & Qualification", [
    ("Delivery Partner Identification & Screening", "Need for new delivery capacity or partner replacement", "Ad-hoc; typically 2–4 new partners/year", "~2–4 evaluations/year; ~10–15 active partners", "Logistics Manager", "Logistics Mgr, Procurement, Legal, Finance",
     [("Logistics Manager identifies potential partners based on geographic coverage, vehicle fleet, pricing, and reputation; Procurement conducts due diligence (DTI/SEC registration, insurance, safety record, references)", "Logistics Manager / Procurement", "VP Supply Chain", "3–5 days"),
      ("Legal reviews contract: SLA terms, liability, insurance, data privacy (RA 10173), rate card, payment terms, termination; Finance evaluates pricing and sets up vendor master", "Legal / Finance", "CFO", "2–3 days")]),
    ("3PL System Integration & Onboarding", "Contract signed with new partner", "~2–4 integrations/year", "~2–4/year", "IT Integration Lead", "IT Integration, Logistics Mgr, 3PL Partner",
     [("IT configures API integration: order push, delivery status, proof of delivery, driver tracking; tests in sandbox; Logistics Manager trains partner on BuildRight processes", "IT / Logistics Manager", "CIO", "5–10 days"),
      ("Pilot period: 2-week controlled rollout with 1 DC; monitors performance vs. SLA; full rollout upon meeting pilot criteria", "Logistics Manager", "VP Supply Chain", "2 weeks")]),
    ("Driver & Vehicle Compliance Verification", "Partner onboarding or annual re-certification", "Annual; onboarding as needed", "~200–300 drivers across all 3PL partners", "Logistics Coordinator", "Logistics Coord, 3PL Partner, Safety Officer",
     [("Coordinator verifies driver credentials: professional license, drug test, background check, BuildRight safety training; verifies vehicle compliance: registration, insurance, roadworthiness", "Logistics Coordinator", "Logistics Manager", "2–3 days"),
      ("Annual re-certification: partners submit updated documents; non-compliant drivers/vehicles suspended until cleared", "Logistics Coordinator", "Logistics Manager", "1–2 weeks")]),
    ("3PL Rate Card Negotiation & Renewal", "Annual rate card review or significant cost change", "Annual; ad-hoc for fuel price changes", "~10–15 rate cards", "Logistics Manager", "Logistics Mgr, Procurement, Finance, 3PL Partner",
     [("Logistics Manager analyzes spend, volume, and market rates; benchmarks vs. spot rates; negotiates: base per-km rate, weight surcharges, waiting time, multi-drop discounts, peak surcharges", "Logistics Manager", "Procurement", "1–2 days"),
      ("Finance validates cost impact; approves; updated rate card configured in ERP", "Finance", "CFO", "1 day")]),
    ("3PL Insurance & Liability Management", "Insurance renewal or delivery incident", "Annual renewal; ad-hoc for incidents", "~10–15 partner policies", "Logistics Manager", "Logistics Mgr, Legal, Finance",
     [("Manager ensures all partners maintain required insurance (vehicle, cargo, third-party liability); tracks expiry dates; files claims for incidents (damage, loss, accident)", "Logistics Manager", "Legal", "2–3 hours/quarter"),
      ("Annual: reviews insurance adequacy; adjusts coverage based on claims history and delivery volume growth", "Logistics Manager / Finance", "CFO", "1 day/year")]),
    ("3PL Capacity Planning & Allocation", "Seasonal capacity review or new store openings", "Quarterly; ad-hoc for openings", "4 DCs; ~10,000 deliveries/month", "Logistics Manager", "Logistics Mgr, DC Ops, Store Ops, 3PL Partners",
     [("Manager forecasts capacity needs: seasonal peaks, new stores (~10–15/year), replenishment volume; allocates across partners by capacity, performance, cost; ensures no single partner >50%", "Logistics Manager", "VP Supply Chain", "2–3 days/quarter"),
      ("Coordinates surge capacity for peaks: pre-books vehicles, temporary agreements, adjusts DC scheduling", "Logistics Manager", "DC Operations", "1 week")]),
    ("3PL Partner Performance Scorecard", "Monthly review cycle", "Monthly", "~10–15 scorecards/month", "Logistics Manager", "Logistics Mgr, DC Ops, Store Ops, VP Supply Chain",
     [("System generates scorecard: on-time delivery rate (≥95%), damage rate (<0.5%), order acceptance rate, avg delivery time, complaint rate, driver professionalism; Manager reviews with partner", "System / Logistics Manager", "VP Supply Chain", "1–2 hours/partner"),
      ("Below-target partners get 30-day corrective action plans; quarterly: VP reviews portfolio for retention/reallocation/new sourcing decisions", "Logistics Manager", "COO", "2–3 hours/quarter")]),
    ("3PL Contract Termination & Transition", "Partner underperformance or strategic decision", "Ad-hoc; ~1–2/year", "~1–2 transitions/year", "Logistics Manager", "Logistics Mgr, Legal, Procurement, IT",
     [("Manager initiates termination per contract terms (60–90 days notice); documents justification; Procurement sources replacement; IT begins integration", "Logistics Manager / Procurement / IT", "VP Supply Chain", "30–60 days"),
      ("Executes volume transition over 2–4 weeks; closes financial settlement with departing partner", "Logistics Manager", "Finance", "2–4 weeks")])
]), "3pl-partner-onboarding-qualification"))

pa_summaries.append(("PA-56.2", "Delivery Performance & SLA Management",
    write_pa(vs_dir, vs_num, vs_name, family, "PA-56.2", "delivery-performance-sla", "Delivery Performance & SLA Management", [
    ("Real-Time Delivery Tracking & Monitoring", "Active deliveries in progress", "Continuous; ~10,000 deliveries/month", "~400–500 deliveries/day", "Logistics Coordinator", "Logistics Coord, DC Dispatch, Store Receiving",
     [("System tracks all 3PL deliveries: driver location, ETA, status; Coordinator monitors exceptions (delays >30 min, no-show, breakdown, route deviation); auto-alerts store of ETA", "System / Logistics Coord", "Logistics Manager", "Real-time"),
      ("Store confirms receipt; exceptions escalated to Logistics Manager for corrective action", "Store Manager / System", "Logistics Manager", "Continuous")]),
    ("SLA Compliance Monitoring", "Daily SLA report", "Daily", "~10,000 deliveries/month; 1–3 day SLA", "Logistics Coordinator", "Logistics Coord, Logistics Mgr, VP Supply Chain",
     [("System calculates daily SLA compliance by partner, DC, route, store; Coordinator investigates breaches (traffic, weather, capacity, dispatch delay); implements corrections", "System / Logistics Coord", "Logistics Manager", "1–2 hours/day")]),
    ("Customer Home Delivery SLA Management", "Ecommerce home delivery orders", "Daily; 2–5 business day SLA", "~17,200 home deliveries/month", "Ecommerce Logistics Coordinator", "Ecom Logistics Coord, 3PL, Customer Service",
     [("System assigns to optimal partner by location/size/cost; tracks 2-day Metro / 3–5 day provincial SLA; proactively contacts customers for delays; failed deliveries rescheduled within 24 hours", "System / Ecom Logistics Coord", "Customer Service", "2–3 hours/day")]),
    ("Delivery Quality Inspection", "Store receives delivery from 3PL", "~10,000 deliveries/month", "~400–500/day", "Store Receiving Clerk", "Receiving Clerk, Store Manager, Logistics Coord",
     [("Clerk inspects: damage, count vs. manifest, item condition; records GR; damaged items photographed, noted on POD, damage record created for VS-50", "Receiving Clerk", "Store Manager", "10–15 min/delivery"),
      ("Weekly: Store Manager reports quality issues; patterns by partner or route investigated", "Store Manager", "Logistics Manager", "15 min/week")]),
    ("Proof of Delivery & Documentation", "Every delivery completion", "Every delivery (~10,000/month)", "~10,000 PODs/month", "3PL Driver / Receiving Clerk", "Driver, Receiving Clerk, Logistics Coord",
     [("Driver obtains POD: digital signature + GPS + timestamp; system stores with delivery record; auto-matches for settlement", "3PL Driver / System", "Logistics Coordinator", "2 min/delivery")]),
    ("Delivery Exception Management", "Delivery issue reported", "~500–800 exceptions/month (~5–8%)", "~500–800/month", "Logistics Coordinator", "Logistics Coord, 3PL, Store Manager, CS",
     [("Coordinator categorizes: delay, damage, wrong items, failed delivery, breakdown; resolves: re-delivery, replacement, escalation to 3PL, coordination with DC", "Logistics Coordinator", "Logistics Manager", "5–30 min")]),
    ("Multi-Stop Route Optimization", "Daily delivery planning", "Daily; 4 DCs", "~4 DCs × 5–8 routes × 2–3 stops", "DC Dispatch Supervisor", "DC Dispatch, Logistics Mgr, Route System",
     [("System generates optimized routes: groups by geography, minimizes distance, balances capacity; Supervisor reviews and adjusts for priorities, last-minute orders, road closures", "System / DC Dispatch Supervisor", "Logistics Manager", "1–2 hours/day")]),
    ("Seasonal Delivery Surge Management", "Peak season (Christmas, summer)", "2–3 major peaks/year", "~30–50% volume increase", "Logistics Manager", "Logistics Mgr, DC Ops, Store Ops, 3PL Partners",
     [("Manager forecasts peak volume; pre-books 3PL capacity 4–6 weeks ahead; implements surge plan: extended windows, additional routes, temporary drivers, DC overtime", "Logistics Manager", "VP Supply Chain", "1–3 weeks"),
      ("Post-peak: analyzes vs. plan; adjusts for next peak; updates contracts with peak rate agreements", "Logistics Manager", "VP Supply Chain", "2–3 days")])
]), "delivery-performance-sla"))

pa_summaries.append(("PA-56.3", "3PL Settlement & Cost Optimization",
    write_pa(vs_dir, vs_num, vs_name, family, "PA-56.3", "3pl-settlement-cost-optimization", "3PL Settlement & Cost Optimization", [
    ("Monthly 3PL Invoice Processing", "3PL partner submits monthly invoice", "Monthly; ~10–15 invoices", "~PHP 30–50M/month total logistics", "Logistics Finance Analyst", "Logistics Finance Analyst, Logistics Mgr, Finance",
     [("Analyst matches invoice vs. system delivery records: validates count, distances, surcharges, SLA penalties; investigates discrepancies with partner; approves adjusted invoice; payment Net 30", "Logistics Finance Analyst", "Finance Manager", "4–6 hours/month")]),
    ("Per-Delivery Cost Analysis", "Monthly analysis", "Monthly", "~10,000 deliveries analyzed", "Logistics Finance Analyst", "Logistics Finance Analyst, Logistics Mgr, FP&A",
     [("Analyst calculates per-delivery cost by partner, route, DC, store, type; identifies outliers: above-average routes, increasing rates, excessive exception costs", "Logistics Finance Analyst", "Finance Manager", "2–3 hours/month")]),
    ("3PL Cost Benchmarking", "Quarterly benchmarking", "Quarterly", "10–15 partners vs. market", "Logistics Manager", "Logistics Mgr, Procurement, Finance",
     [("Manager benchmarks costs against market (Lalamove, Transportify, industry surveys); identifies savings: rate renegotiation, partner consolidation, route optimization, volume discounts", "Logistics Manager", "VP Supply Chain", "1–2 days/quarter")]),
    ("Fuel Cost Impact Analysis", "Monthly or significant fuel change", "Monthly; ad-hoc for >5% change", "Monthly analysis", "Logistics Finance Analyst", "Logistics Finance Analyst, Logistics Mgr, Finance",
     [("Analyst tracks fuel cost component of rates; monitors Philippine diesel prices; calculates impact; significant changes trigger rate card review with partners", "Logistics Finance Analyst", "Finance Manager", "2–3 hours/month")]),
    ("Owned Fleet vs. 3PL Cost Comparison", "Annual fleet strategy review", "Annual", "Owned 20%; 3PL 80%", "VP Supply Chain", "VP Supply Chain, Logistics Mgr, Finance Dir, COO",
     [("Finance calculates TCO for owned fleet (depreciation, maintenance, fuel, salaries, insurance) vs. 3PL cost per delivery; VP recommends fleet mix by route", "Finance / VP Supply Chain", "COO", "3–5 days")]),
    ("Delivery Fee Revenue Optimization", "Monthly ecommerce fee analysis", "Monthly", "~17,200 home deliveries/month", "Ecommerce Operations Manager", "Ecom Ops Mgr, Finance, Logistics Mgr",
     [("Manager analyzes fee collected vs. actual delivery cost; adjusts fee structure (weight/distance), free delivery threshold (PHP 5K), to maintain margin on delivery operations", "Ecom Ops Manager", "VP Marketing", "1 day/quarter")]),
    ("3PL Payment Settlement Automation", "Monthly settlement", "Monthly; ~10–15 partners", "~PHP 30–50M", "Finance Manager", "Finance Mgr, Logistics Finance Analyst, Treasury",
     [("System auto-calculates settlement: delivery fees × volume, SLA penalties, damage deductions, rate adjustments; generates statement; Manager reviews and approves; payment via bank transfer Net 30", "System / Finance Manager", "CFO", "2–3 hours/month")]),
    ("Logistics Total Cost Dashboard", "Continuous; monthly deep analysis", "Continuous; monthly deep dive", "~PHP 360–600M/year (~0.6–1% of revenue)", "VP Supply Chain", "VP Supply Chain, Logistics Mgr, Finance Dir, COO",
     [("Dashboard: total cost, cost per delivery, per store, per peso delivered, % of COGS, trend vs. budget; VP reviews monthly with COO/CFO; tracks savings initiatives quarterly", "System / VP Supply Chain", "COO", "2–3 hours/month")])
]), "3pl-settlement-cost-optimization"))

t = write_readme(vs_dir, vs_num, vs_name, family, overview, pa_summaries)
grand += t
print(f"VS-{vs_num}: {vs_name} — {t} workflows")

# ═══ VS-57 ═══
vs_dir = "VS-57-competitive-price-intelligence"
vs_num = 57; vs_name = "Competitive Price Intelligence & Monitoring"; family = "Plan & Source"
overview = "Manages BuildRight's competitive pricing intelligence program, including systematic collection of competitor pricing data, price matching decisions, dynamic pricing recommendations, and margin impact analysis. Monitors key competitors (Wilcon, CitiHardware, Handyman Do-It-Best, Mr. DIY) across the Philippine hardware/home improvement market."

pa_summaries = []
pa_summaries.append(("PA-57.1", "Competitor Price Data Collection & Analysis",
    write_pa(vs_dir, vs_num, vs_name, family, "PA-57.1", "competitor-price-data-collection", "Competitor Price Data Collection & Analysis", [
    ("Competitor Price Scraping & Collection", "Weekly collection cycle", "Weekly; ~500–1,000 price points", "~500–1,000 prices/week across 4–5 competitors", "Pricing Analyst", "Pricing Analyst, Category Mgr, IT",
     [("Analyst coordinates weekly collection: (a) automated web scraping for ecommerce prices, (b) mystery shopping for in-store (20 key stores/competitor), (c) marketplace monitoring (Lazada, Shopee); system normalizes and matches to BuildRight SKUs", "Pricing Analyst / System", "Category Manager", "1–2 days")]),
    ("Price Matching Decision & Execution", "Significant price gap identified (>10%)", "Ad-hoc; ~20–30 decisions/month", "~20–30/month", "Category Manager", "Category Mgr, Pricing Analyst, VP Merchandising",
     [("Pricing Analyst prepares recommendation: current vs. competitor price, margin impact, volume estimate, strategic importance; Category Manager decides: match, undercut, or hold; approves change in system", "Pricing Analyst / Category Mgr", "VP Merchandising", "45–60 min")]),
    ("Competitor Promotion Monitoring", "Competitor launches promo", "Ad-hoc; ~2–3 major events/quarter", "~2–3 events/quarter", "Pricing Analyst", "Pricing Analyst, Marketing, Category Mgr",
     [("Analyst captures competitor promo details: prices, duration, terms; assesses impact on BuildRight (overlapping SKUs, potential sales loss); recommends response", "Pricing Analyst", "VP Merchandising", "2–3 hours/event")]),
    ("Price Positioning Strategy Review", "Quarterly pricing strategy review", "Quarterly; 13 categories", "~13 reviews/quarter", "VP Merchandising", "VP Merch, Category Mgrs, Pricing Analysts, Finance",
     [("Pricing Analyst prepares positioning analysis: BuildRight vs. competitors by category, price index, margin, perception survey; VP sets strategy: premium, parity, or value per category", "Pricing Analyst / VP Merchandising", "COO", "2–3 days")]),
    ("Dynamic Pricing Rule Management", "Monthly rule review", "Monthly; ~50–100 active rules", "~50–100 rules", "Pricing Analyst", "Pricing Analyst, IT, Category Mgr",
     [("Analyst maintains dynamic rules: auto-price-match thresholds, floor prices (min margin), ceiling prices, clearance triggers; IT implements and tests changes", "Pricing Analyst / IT", "Category Manager", "4–6 hours/month")]),
    ("Market Basket Price Comparison", "Quarterly comprehensive", "Quarterly; 100-SKU basket", "~100 SKUs × 4–5 competitors", "Pricing Analyst", "Pricing Analyst, Category Mgr, VP Merchandising",
     [("Analyst constructs standardized 100-item basket; prices at BuildRight and competitors (in-store + online); calculates basket price index; identifies over/underpriced categories", "Pricing Analyst", "VP Merchandising", "3–5 days")]),
    ("Price Elasticity Analysis", "Semi-annual", "Semi-annual; ~50–100 SKUs", "~50–100 elasticity analyses", "Analytics Manager", "Analytics Mgr, Pricing Analyst, Category Mgr",
     [("Analytics Manager measures price elasticity: volume change vs. price change; calculates coefficient; feeds into strategy (inelastic: higher margins; elastic: competitive pricing)", "Analytics Manager", "VP Merchandising", "3–5 days")]),
    ("Competitor Pricing Intelligence Report", "Monthly reporting", "Monthly", "Monthly report covering 4–5 competitors", "Pricing Analyst", "Pricing Analyst, Category Mgrs, VP Merch, COO",
     [("Analyst compiles monthly report: competitor price movements, promotional activity, new entrants, BuildRight price index trend; VP reviews with Category Managers and COO", "Pricing Analyst / VP Merchandising", "COO", "1 day + 2–3 hours")])
]), "competitor-price-data-collection"))

pa_summaries.append(("PA-57.2", "Price Response Strategy & Execution",
    write_pa(vs_dir, vs_num, vs_name, family, "PA-57.2", "price-response-strategy", "Price Response Strategy & Execution", [
    ("Rapid Price Response Workflow", "Competitor unexpected price move on key SKU", "Ad-hoc; ~5–10 rapid responses/month", "~5–10/month", "Category Manager", "Category Mgr, Pricing Analyst, VP Merch, IT",
     [("Analyst alerts with impact analysis; Category Manager decides; VP approves >5% margin impact; IT implements; cascaded to POS within 4 hours", "Pricing Analyst / Category Mgr / VP Merch", "IT", "2–4 hours")]),
    ("Promotional Price Planning", "Upcoming promotional calendar event", "6 major + 12 monthly per year", "~18 cycles/year", "Pricing Analyst", "Pricing Analyst, Category Mgr, Marketing, Finance",
     [("Analyst recommends promo prices based on competitive data; Category Manager approves; Finance validates margin floor; Marketing incorporates; POS configured", "Pricing Analyst / Category Mgr / Finance / Marketing", "VP Merchandising", "3–5 days")]),
    ("Markdown Optimization for Clearance", "End-of-season or slow-moving inventory", "Monthly; ~500–1,000 markdown decisions", "~500–1,000/month", "Category Manager", "Category Mgr, Merch Planner, Pricing Analyst, Finance",
     [("Planner identifies markdown candidates; Analyst recommends levels based on competitive pricing and velocity targets; Manager approves; system updates; Marketing communicates clearance", "Merch Planner / Pricing Analyst / Category Mgr", "VP Merchandising", "1–2 days")]),
    ("Store-Level Price Override", "Store requests override for competitive reason", "~200–400 requests/month", "~200–400/month", "Store Manager / Regional Ops Manager", "Store Manager, Regional Ops Mgr, Category Mgr",
     [("Store Manager submits: SKU, current price, requested price, competitor proof; Regional Ops approves ≤10%; Category Manager approves >10%; system updates for that store", "Store Manager / Regional Ops Mgr / Category Mgr", "VP Merchandising", "30 min")]),
    ("Price Change Communication to Stores", "Price change approved", "~200–300 changes/month", "~200–300/month", "Merchandising Coordinator", "Merch Coordinator, Store Managers, IT",
     [("System distributes change package to stores via app; stores print updated shelf labels from RF guns; apply within 24 hours; Coordinator verifies compliance per VS-55", "System / Store Staff", "Merch Coordinator", "2–4 hours")]),
    ("Trade Price Competitive Alignment", "Quarterly trade price review", "Quarterly; ~5,000 trade accounts", "~5,000 accounts", "Trade Sales Manager", "Trade Sales Mgr, Pricing Analyst, Category Mgr",
     [("Analyst compares trade prices vs. competitor wholesale for top 200 SKUs; Manager recommends adjustments; Category Manager approves; system updates trade price lists", "Pricing Analyst / Trade Sales Mgr", "VP Merchandising", "2–3 days")]),
    ("Price Audit & Compliance", "Monthly internal audit", "Monthly; 200 stores", "~200 audits/month", "Pricing Analyst", "Pricing Analyst, Store Manager, Regional Ops",
     [("System compares POS shelf prices to SRP for all transactions; flags >1% discrepancy stores; investigates root causes; corrects", "System / Pricing Analyst", "VP Merchandising", "2–3 hours + 1–2 days")]),
    ("Customer Price Match Guarantee", "Customer requests price match at POS", "~3,000–5,000 requests/month", "~3K–5K/month", "Cashier / Store Manager", "Cashier, Customer, Store Manager",
     [("Cashier verifies same SKU, current competitor price, within policy terms; ≤10%: Cashier approves; >10%: Store Manager approves; system records for analytics and fraud monitoring", "Cashier / Store Manager", "Pricing Analyst", "5–10 min")])
]), "price-response-strategy"))

pa_summaries.append(("PA-57.3", "Pricing Analytics & Margin Optimization",
    write_pa(vs_dir, vs_num, vs_name, family, "PA-57.3", "pricing-analytics-margin-optimization", "Pricing Analytics & Margin Optimization", [
    ("Gross Margin Analysis by Category", "Monthly financial analysis", "Monthly; 13 categories", "13 category analyses", "Finance Manager", "Finance Mgr, Category Mgr, VP Merchandising",
     [("System calculates gross margin by category (revenue, COGS, markdowns, returns, net); Category Manager reviews trends and identifies margin erosion causes", "System / Category Manager", "VP Merchandising", "2–3 hours")]),
    ("Price Sensitivity Dashboard", "Weekly update", "Weekly; ~100 key SKUs", "~100 SKUs monitored", "Pricing Analyst", "Pricing Analyst, Category Mgr, VP Merch",
     [("Dashboard: current price, trend, competitor price, gap, volume trend, margin, sensitivity indicator; Analyst flags diverging trends and recommends adjustments", "System / Pricing Analyst", "Category Manager", "1–2 hours/week")]),
    ("Vendor Cost-Driven Price Adjustment", "Vendor cost change", "~5–10/month", "~5–10 reviews/month", "Category Manager", "Category Mgr, Buyer, Pricing Analyst, Finance",
     [("Buyer receives cost change; Analyst calculates required adjustment for target margin and competitive impact; Manager decides: pass through, absorb, or negotiate", "Buyer / Pricing Analyst / Category Mgr", "VP Merchandising", "2–4 hours")]),
    ("Pricing Strategy Annual Review", "Annual comprehensive review", "Annual; all 13 categories", "Full category pricing strategy", "VP Merchandising", "VP Merch, Category Mgrs, Finance Dir, COO, CEO",
     [("VP leads category-by-category assessment; Finance sets margin floors; COO approves operational impact; CEO approves strategy for new fiscal year", "VP Merchandising / Finance / COO / CEO", "Board", "3–5 days")]),
    ("Promotional Pricing ROI Analysis", "Post-promotional analysis", "18 analyses/year", "18/year", "FP&A Analyst", "FP&A, Pricing Analyst, Category Mgr, Marketing",
     [("FP&A calculates: incremental sales × margin minus discount cost minus marketing spend; Analyst correlates with competitive pricing; identifies defensive vs. offensive promos", "FP&A Analyst / Pricing Analyst", "Finance Manager", "4–6 hours")]),
    ("Price Image & Customer Perception Survey", "Semi-annual survey", "Semi-annual; ~1,000 respondents", "~1,000 respondents", "Marketing Research Manager", "Marketing Research, Pricing Analyst, VP Marketing",
     [("Survey: customers rate value for money vs. competitors; identifies overpriced-perceived categories; Analyst correlates perception with actual pricing", "Marketing Research / Pricing Analyst", "VP Marketing", "2–3 weeks")]),
    ("Pricing System & Master Data Accuracy", "Monthly data quality audit", "Monthly; 35,000 SKUs", "~35,000 price records", "IT System Admin / Pricing Analyst", "IT, Pricing Analyst, Data Quality Analyst",
     [("System validates: active SKUs have SRP, promo prices within dates, trade prices in range, no negative margins without approval; Analyst investigates exceptions", "System / Pricing Analyst", "Category Manager", "2–3 hours/month")]),
    ("Cross-Channel Price Consistency", "Weekly consistency check", "Weekly; POS, ecommerce, marketplace", "3 channels × ~35,000 SKUs", "Ecommerce Operations Manager", "Ecom Ops Mgr, Pricing Analyst, IT",
     [("System compares prices across channels; flags inconsistencies >PHP 50 or >5%; Analyst investigates (sync delays, overrides, promo timing); corrects and prevents", "System / Pricing Analyst", "IT System Admin", "2–3 hours/week")])
]), "pricing-analytics-margin-optimization"))

t = write_readme(vs_dir, vs_num, vs_name, family, overview, pa_summaries)
grand += t
print(f"VS-{vs_num}: {vs_name} — {t} workflows")

# Print final total
print(f"\nSubtotal VS-56 to VS-57: {grand}")
print(f"Running total with VS-53 to VS-55: {72 + grand}")
print(f"Next workflow ID: W{wf_counter}")
