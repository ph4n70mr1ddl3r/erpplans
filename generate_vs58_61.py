#!/usr/bin/env python3
"""Generate VS-58 through VS-61."""
import os, sys
BASE = "/home/riddler/erpplans/01-model-company/workflows"
wf_counter = 2238  # After VS-57

def next_id():
    global wf_counter; wid = wf_counter; wf_counter += 1; return wid

def write_pa(vs_dir, vs_num, vs_name, family, pa_num, pa_slug, pa_title, workflows):
    toc = []; wf_blocks = []
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
    rows = []; total = 0
    for pn, pt, pc, ps in pa_summaries:
        rows.append(f"| [{pn}]({pn}-{ps}.md) | {pt} | {pc} |"); total += pc
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

# ═══ VS-58 ═══
d = "VS-58-coupon-digital-promotions"; n = 58; nm = "Coupon & Digital Promotions Management"; fam = "Sell & Serve"
ov = "Manages BuildRight's coupon and digital promotions program covering paper coupons, digital vouchers, loyalty point multipliers, and promotional code campaigns. Coordinates with marketing campaigns (VS-14), POS (VS-08), loyalty (VS-13), and ecommerce (VS-10). Targets ~15% of monthly transactions involving a promotional offer."
ps = []
ps.append(("PA-58.1", "Coupon & Voucher Creation & Distribution", write_pa(d, n, nm, fam, "PA-58.1", "coupon-voucher-creation", "Coupon & Voucher Creation & Distribution", [
    ("Coupon Design & Configuration", "Marketing campaign launch", "~18 campaigns/year", "~18 designs/year", "Marketing Promotions Manager", "Marketing, Category Mgr, IT, Legal",
     [("Marketing designs coupon (value, eligible SKUs, validity, channel, max redemptions, segment targeting); IT configures in ERP with validation rules; Legal reviews for Consumer Act compliance", "Marketing / IT / Legal", "VP Marketing", "1–2 days")]),
    ("Digital Voucher Distribution", "Campaign launch via digital channels", "~18 campaigns/year + ad-hoc", "~500K–1M vouchers/year", "Digital Marketing Manager", "Digital Mktg, CRM, Customer",
     [("Distributes via email, SMS, app push, social ads, partner platforms (GCash, Maya); system tracks distribution, open rate, claim rate, redemption rate by channel and segment", "Digital Marketing / System", "VP Marketing", "1–2 days/campaign")]),
    ("In-Store Coupon Printing & Display", "Physical coupon campaign", "~6 major campaigns/year", "~600K physical coupons/campaign", "Marketing Operations Manager", "Marketing Ops, Print Vendor, Store Ops",
     [("Marketing Ops coordinates printing and DC distribution; stores display at entrance and checkout; Store Manager monitors stock and replenishes", "Marketing Ops / Store Manager", "VP Marketing", "1–2 weeks")]),
    ("Coupon Budget & Liability Management", "Campaign launch", "~18/year", "~PHP 50–100M annual promo budget", "Finance Manager", "Finance Mgr, Marketing Dir, CFO",
     [("Finance estimates liability (expected redemption × value × volume); allocates budget; sets accrual; monthly reconciles actual vs. accrual", "Finance Manager", "CFO", "2–3 hours/campaign + 2–3 hours/month")]),
    ("Vendor-Funded Coupon Program", "Vendor co-op promotional funding", "~10–15 vendor-funded promos/year", "~10–15/year", "Category Manager", "Category Mgr, Marketing, Vendor, Finance",
     [("Vendor proposes co-op coupon per VS-39; Marketing designs; system tracks redemptions; Finance submits claim to vendor for funded portion", "Category Manager / Marketing / Finance", "VP Merchandising", "Ongoing")]),
    ("Loyalty Point Multiplier Campaign", "Loyalty campaign (double/triple points)", "~6–8/year", "~600K members per campaign", "Loyalty Program Manager", "Loyalty Mgr, Marketing, CRM, Finance",
     [("Manager designs multiplier (2x/3x/5x), eligible categories, tiers; configures in loyalty engine; Marketing communicates; system auto-applies at POS/online", "Loyalty Manager / Marketing", "VP Marketing", "1–2 days")]),
    ("Coupon Fraud Prevention Design", "Every coupon design before launch", "~18/year", "~18 designs reviewed", "Loss Prevention Analyst", "LP Analyst, Marketing, IT",
     [("LP reviews for fraud vectors: unique barcodes, single-use, purchase validation, digital device-binding; IT implements: per-customer limits, anomaly detection", "LP Analyst / IT", "LP Director", "2–3 hours + 1–2 days/campaign")]),
    ("Coupon Performance Dashboard", "Campaign active period", "Per campaign (~18/year)", "Per campaign", "Marketing Analyst", "Marketing Analyst, VP Marketing, Category Mgr",
     [("Dashboard: distributed, claimed, redeemed, rate, incremental sales, basket with vs. without, cost per redemption; post-campaign ROI report", "System / Marketing Analyst", "VP Marketing", "Automated + 4–6 hours/campaign")])
]), "coupon-voucher-creation"))
ps.append(("PA-58.2", "Coupon Redemption & Fraud Prevention", write_pa(d, n, nm, fam, "PA-58.2", "coupon-redemption-fraud", "Coupon Redemption & Fraud Prevention", [
    ("In-Store Coupon Redemption", "Customer presents coupon at POS", "~50K–80K/month during campaigns", "~50K–80K/month; ~15% of transactions", "Cashier", "Cashier, Customer, POS System",
     [("Cashier scans barcode; system validates (active, eligible items, not previously redeemed, minimum met); discount applied; redemption recorded with transaction/store/cashier ID", "POS System / Cashier", "Cashier", "15–30 sec")]),
    ("Online Coupon & Promo Code Redemption", "Customer enters promo code at checkout", "~8K–12K/month", "~8K–12K/month", "Ecommerce System", "Ecommerce System, Customer, CRM",
     [("Customer enters code; system validates (active, dates, items, minimum, usage limit, segment); valid: discount applied; invalid: specific error message; tracked in CRM", "System", "Ecommerce Ops", "<5 sec")]),
    ("Multi-Coupon Stacking Management", "Customer presents multiple coupons", "~5–10% of coupon transactions", "~5–10%", "Cashier / POS System", "Cashier, Customer, POS System",
     [("POS enforces rules: max 1 manufacturer + 1 store coupon per item, total discount ≤50% of basket, category exclusions; Cashier informed of limits; suggests optimal combination", "POS System / Cashier", "Store Manager", "1–2 min")]),
    ("Coupon Redemption Fraud Detection", "Real-time monitoring", "Real-time + weekly review", "~100–200 flagged/month", "Loss Prevention Analyst", "LP Analyst, Store Manager, Finance",
     [("System monitors: same barcode reused, single customer >5/day, single store abnormally high, employee-customer collusion; LP investigates, reverses, deactivates; weekly fraud report", "System / LP Analyst", "LP Director", "2–3 hours/week")]),
    ("Coupon Return & Reversal", "Customer returns item bought with coupon", "~2K–3K/month", "~2K–3K/month", "Customer Service Rep", "CSR, POS System, Finance",
     [("System determines: full return → coupon reinstated; partial return → prorated refund minus coupon value; reverses redemption; adjusts liability; prevents double-dipping", "POS System / CSR", "Finance", "5–10 min")]),
    ("Expired Coupon Exception Handling", "Customer presents recently expired coupon", "~500–1K/month", "~500–1K/month", "Store Manager", "Store Manager, Customer, Marketing",
     [("Manager reviews: within 7 days → may honor; loyalty member → more lenient; high-value → honor with override; if denied → offer current equivalent promo", "Store Manager", "Regional Ops Mgr", "5 min")]),
    ("Digital Coupon Device & Account Binding", "Customer claims digital coupon", "Per campaign", "~500K–1M claims/year", "IT Integration Lead", "IT Integration, CRM, Digital Marketing",
     [("System binds to customer account (loyalty ID) and device (fingerprint); prevents sharing; IT detects spoofing, multiple accounts per device, VPN abuse; adjusts fraud rules", "System / IT Integration Lead", "CIO", "4–6 hours/month")]),
    ("Coupon Vendor Reconciliation", "Monthly vendor settlement", "Monthly; ~10–15 vendor campaigns", "~10–15 reconciliations/month", "Finance Analyst", "Finance Analyst, Category Mgr, Vendor",
     [("Analyst compiles redemption report per vendor; submits claim per VS-39 co-op agreement; vendor validates; Finance records receivable; collects Net 30; disputes resolved with POS data", "Finance Analyst / Vendor", "Finance Manager", "4–6 hours/month")])
]), "coupon-redemption-fraud"))
ps.append(("PA-58.3", "Digital Promotion Performance Analytics", write_pa(d, n, nm, fam, "PA-58.3", "digital-promotion-analytics", "Digital Promotion Performance Analytics", [
    ("Campaign ROI Analysis", "Post-campaign", "Per campaign (~18/year)", "18 analyses/year", "Marketing Analyst", "Marketing Analyst, VP Marketing, Finance",
     [("Calculates: (incremental sales × margin) minus (coupon + distribution + marketing cost); redemption rate, customer acquisition cost, repeat purchase rate; compares vs. target and benchmarks", "Marketing Analyst", "VP Marketing", "4–6 hours/campaign")]),
    ("Channel-Specific Promotion Effectiveness", "Monthly multi-channel analysis", "Monthly; 4 channels", "4 channels/month", "Digital Marketing Manager", "Digital Marketing, Marketing Analyst, VP Marketing",
     [("Segments performance by channel: redemption rate, basket size, demographics, cost per acquisition; reallocates budget to highest-ROI channels; tests new channels with pilot", "Marketing Analyst / Digital Marketing Mgr", "VP Marketing", "4–6 hours/month")]),
    ("Customer Segment Promotion Response", "Quarterly segment analysis", "Quarterly; 6 segments", "~6 segments/quarter", "CRM Manager", "CRM Mgr, Marketing Analyst, Loyalty Mgr",
     [("Analyzes response by segment: loyalty tiers, trade, new vs. existing, lapsed reactivation; customizes future promotions by segment; tests personalized offers for high-value", "CRM Manager", "VP Marketing", "2–3 days/quarter")]),
    ("Promotion Halo Effect Analysis", "Post-major campaign", "6/year", "6/year", "Analytics Manager", "Analytics Mgr, Category Mgr, VP Merchandising",
     [("Measures: sales uplift in non-promoted categories during promo, incremental foot traffic, basket expansion beyond promo items; recommends cross-merchandising strategies", "Analytics Manager", "VP Merchandising", "1–2 days/campaign")]),
    ("Year-over-Year Promotion Trend", "Annual comprehensive", "Annual", "Full year review", "VP Marketing", "VP Marketing, Marketing Analyst, Finance Dir, VP Merch",
     [("Compiles: total spend, incremental revenue, ROI trend, redemption trend, channel shift, competitive promo frequency; presents to Executive Committee with strategy recommendations", "Marketing Analyst / VP Marketing", "CEO", "3–5 days + 1 day")]),
    ("Digital Coupon Technology Performance", "Monthly tech review", "Monthly; 4 platforms", "4 platforms", "IT Integration Lead", "IT Integration, Digital Marketing, CRM",
     [("Monitors: delivery success rate, claim rate, processing latency, uptime during peaks; addresses issues: email deliverability, SMS failures, app notification reliability", "IT Integration Lead", "CIO", "2–3 hours/month")]),
    ("Competitor Promotion Intelligence", "Ongoing monitoring", "Weekly; 4–5 competitors", "4–5 competitors", "Marketing Analyst", "Marketing Analyst, Pricing Analyst, VP Marketing",
     [("Monitors competitor promos: catalogs, social media, store visits; captures type, discount, duration, items; compares to BuildRight; produces competitive report with response recommendations", "Marketing Analyst", "VP Marketing", "2–3 hours/week")]),
    ("Promotion Calendar Optimization", "Annual planning", "Annual; 18+ events", "~18+ events/year", "VP Marketing", "VP Marketing, VP Merch, Category Mgrs, Finance",
     [("VP leads annual planning: aligns with seasonal calendar, vendor funding, competitive intel, customer patterns; Finance validates budget; calendar communicated to stores 2 months before fiscal year", "VP Marketing / Finance / VP Merchandising", "CEO", "3–5 days")])
]), "digital-promotion-analytics"))
t = write_readme(d, n, nm, fam, ov, ps); grand += t
print(f"VS-{n}: {nm} — {t}")

# ═══ VS-59 ═══
d = "VS-59-store-closure-decommissioning"; n = 59; nm = "Store Closure & Decommissioning"; fam = "Asset & Infrastructure"
ov = "Manages the process of closing underperforming BuildRight Depot stores, covering closure decision analysis, lease termination, inventory liquidation, asset recovery, staff redeployment, and post-closure site management. Inverse of VS-37 (Store Opening). Targets: ~2–3 store closures/year with 6-month timeline."
ps = []
ps.append(("PA-59.1", "Store Closure Decision & Planning", write_pa(d, n, nm, fam, "PA-59.1", "store-closure-decision-planning", "Store Closure Decision & Planning", [
    ("Store Performance Trigger Analysis", "Quarterly store performance review", "Quarterly; 200 stores", "~2–3 flagged/quarter", "VP Store Operations", "VP Store Ops, Finance Dir, Regional Ops Mgr",
     [("System flags stores: sales/sqm <60% of chain avg for 4 quarters, negative contribution margin 2+ quarters, lease renewal with unfavorable terms; VP presents to Executive Committee", "System / VP Store Ops", "CEO", "1–2 days")]),
    ("Closure Business Case Development", "Executive Committee approves evaluation", "Ad-hoc; ~2–3/year", "~2–3 business cases/year", "FP&A Director", "FP&A Dir, VP Store Ops, VP Real Estate, Legal, HR",
     [("FP&A develops: closure costs (lease penalty, severance, inventory write-down, asset disposal) vs. savings (rent, staff, utilities); payback period, NPV; VP Real Estate evaluates lease; Legal reviews; HR estimates severance", "FP&A Director / VP Real Estate / Legal / HR", "CFO", "5–10 days")]),
    ("Closure Decision & Board Approval", "Business case ready", "Ad-hoc; ~2–3/year", "~2–3 decisions/year", "CEO", "CEO, CFO, COO, Board",
     [("CEO presents to Board with full business case, impact analysis, timeline; Board approves or requests analysis; approved closures assigned to Project Manager with 6-month timeline", "CEO", "Board", "2–3 hours + 1 day")]),
    ("Store Closure Communication Plan", "Closure approved", "Per closure (~2–3/year)", "~2–3 plans/year", "VP Corporate Communications", "VP Corp Comms, HR, Store Ops, Legal, Marketing",
     [("Develops plan: employee notification (DOLE 30-day notice), customer communication (redirect to nearest store), vendor notification, media/PR, LGU notification; Legal reviews; HR prepares letters; Marketing prepares messaging", "VP Corp Comms / Legal / HR / Marketing", "CEO", "3–5 days + 2–3 days")]),
    ("Closure Project Planning & Timeline", "Board approves closure", "Per closure; 6-month timeline", "~2–3 projects/year", "Store Closure Project Manager", "Closure PM, VP Store Ops, VP Real Estate, HR, Finance",
     [("Develops project plan: employee transition (60 days), inventory liquidation (90 days), asset recovery (30 days), lease termination (per contract), site handover (30 days); weekly steering committee", "Closure PM", "COO", "3–5 days + ongoing")]),
    ("Customer Migration Planning", "Closure approved", "Per closure", "~15K–30K customers per store", "Loyalty Program Manager", "Loyalty Mgr, Marketing, Store Ops, CRM",
     [("Analyzes customer base: active members, frequency, nearest alternative store; develops redirect communications; Marketing executes migration campaign with welcome offer at new store", "Loyalty Manager / Marketing", "VP Marketing", "3–5 days + 2–3 weeks")]),
    ("Vendor & Supplier Notification", "Closure timeline confirmed", "Per closure", "~100–200 vendors per store", "Procurement Manager", "Procurement Mgr, Category Mgr, Vendors",
     [("Notifies vendors: cancels DSD, adjusts PO schedules, coordinates final deliveries/returns; Category Managers adjust surrounding store assortment to absorb demand", "Procurement Manager / Category Manager", "VP Supply Chain", "1–2 weeks")]),
    ("Closure Regulatory & LGU Compliance", "Closure initiated", "Per closure", "LGU, BIR, DOLE compliance", "Legal & Compliance Officer", "Legal, HR, Finance",
     [("Files: LGU permit cancellation, BIR branch closure, DOLE 30-day notice, SSS/PhilHealth/Pag-IBIG update; Finance settles final taxes; HR ensures statutory compliance; Legal retains records 7 years", "Legal / Finance / HR", "CFO", "1–2 weeks + ongoing")])
]), "store-closure-decision-planning"))
ps.append(("PA-59.2", "Store Wind-Down & Asset Recovery", write_pa(d, n, nm, fam, "PA-59.2", "store-wind-down-asset-recovery", "Store Wind-Down & Asset Recovery", [
    ("Inventory Liquidation Planning & Execution", "Month 2–4 of closure", "Per closure; 90-day window", "~35K SKUs; ~PHP 15–25M inventory", "Merchandising Planner", "Merch Planner, Category Mgr, Store Manager, Marketing",
     [("Designs strategy: transfer high-demand to nearby stores, progressive markdown (10→25→50→75%), bulk sale for residual; Marketing promotes; system tracks sell-through; remaining to DC or bulk", "Merch Planner / Marketing / Store Manager", "Category Manager", "1–2 weeks + 90 days")]),
    ("Fixed Asset Recovery & Disposal", "Month 4–5 of closure", "Per closure", "~PHP 3–5M in fixtures/equipment", "Facilities Coordinator", "Facilities Coord, VP Real Estate, Finance",
     [("Inventories assets: POS, shelving, forklifts, tools, office equipment; determines reuse vs. disposal; reusable transferred to new stores/DCs; disposable sold or scrapped; Finance adjusts asset register", "Facilities Coordinator / Finance", "VP Real Estate", "3–5 days + 2–3 weeks")]),
    ("Lease Termination & Handover", "Month 5–6 of closure", "Per closure", "1 lease per store", "VP Real Estate / Legal", "VP Real Estate, Legal, Landlord",
     [("Negotiates termination: executes clause, pays penalty, coordinates site restoration, schedules handover inspection; Legal ensures documentation: inspection report, deposit return, mutual release", "VP Real Estate / Legal", "CEO", "2–4 weeks + 1–2 weeks")]),
    ("Employee Redeployment & Separation", "Month 1–5 of closure", "Per closure; ~29 employees", "~29 employees per store", "HR Director", "HR Dir, Store Manager, Regional Ops, Legal",
     [("Identifies redeployment: transfers to nearby stores (priority performers), DC, HQ, new openings; for non-redeployed: 30-day notice, severance (0.5–1 month/year), clearance, final pay, DOLE reporting", "HR Director", "CHRO", "2–3 weeks + 4–6 weeks")]),
    ("IT Systems Decommissioning", "Month 5 of closure", "Per closure", "3 POS terminals + network", "IT Operations Manager", "IT Ops Mgr, POS Vendor, Network Provider",
     [("Closes POS terminals, disconnects network/VPN, deactivates store in ERP, archives data per retention, secure data destruction; removes from store locator", "IT Ops Manager", "CIO", "3–5 days + 2–3 days")]),
    ("Final Financial Settlement", "Closure complete", "Per closure", "Full store financial close", "Finance Manager", "Finance Mgr, Accountant, VP Real Estate, HR",
     [("Prepares final P&L: closure costs, asset gains/losses, write-downs, severance, lease penalty; closes cost center; settles payables; collects receivables; final tax filings; archives 7 years", "Finance Manager", "CFO", "5–10 days + 2–3 weeks")]),
    ("Post-Closure Site Monitoring", "6–12 months post-closure", "Per closure", "1 site per closure", "VP Real Estate", "VP Real Estate, Legal",
     [("Monitors post-closure obligations: landlord compliance, dispute resolution, non-compete clauses; tracks customer migration at nearby stores for business case validation", "VP Real Estate / VP Store Ops", "Legal", "Ongoing 6–12 months")]),
    ("Closure Lessons Learned", "Post-closure retrospective", "Per closure", "1 retrospective per closure", "Store Closure Project Manager", "Closure PM, COO, VP Store Ops",
     [("Conducts retrospective: timeline vs. actual, cost vs. budget, customer retention, employee redeployment success, vendor transition; updates closure playbook; shares with Executive Committee", "Closure PM", "COO", "1–2 days + 1 day")])
]), "store-wind-down-asset-recovery"))
ps.append(("PA-59.3", "Staff Redeployment & Post-Closure Analytics", write_pa(d, n, nm, fam, "PA-59.3", "staff-redeployment-post-closure", "Staff Redeployment & Post-Closure Analytics", [
    ("Redeployed Employee Onboarding at New Location", "Employee accepts transfer", "Per closure; ~15–20 redeployments", "~15–20 per closure", "HR Manager", "HR Manager, Receiving Store Manager, Employee",
     [("HR processes movement in system, updates location, arranges relocation support; receiving Store Manager plans orientation; 30-day check-in to assess adjustment", "HR Manager / Receiving Store Manager", "CHRO", "3–5 days + 1 week")]),
    ("Customer Migration Success Tracking", "Monthly post-closure", "Monthly for 12 months", "~15K–30K customers per store", "Loyalty Program Manager", "Loyalty Mgr, Analytics Mgr, VP Marketing",
     [("System tracks: loyalty members from closed store → purchases at nearby stores; calculates retention and spend change; re-engagement campaigns for non-migrated customers", "System / Loyalty Manager", "VP Marketing", "2–3 hours/month")]),
    ("Post-Closure Financial Impact Analysis", "Quarterly post-closure", "Quarterly for 4 quarters", "Full impact per closure", "FP&A Director", "FP&A Dir, Finance Dir, VP Store Ops, CEO",
     [("Compares actual costs vs. estimates; tracks quarterly savings vs. projected; calculates actual payback; reviews surrounding store impact; validates network P&L", "FP&A Director", "CEO", "2–3 days/quarter")]),
    ("Store Closure Database & Knowledge Management", "Post-closure", "Per closure", "Central knowledge base", "Store Closure Project Manager", "Closure PM, all functions, IT",
     [("Compiles: business case, plan, timeline, actual costs, lessons learned, contacts, filings; stores in knowledge management system; accessible for future closures and new store openings (VS-37)", "Closure PM / IT", "COO", "3–5 days + 1–2 days")]),
    ("Regional Sales Impact Assessment", "6 and 12 months post-closure", "6 months and 12 months", "3–5 nearby stores", "Analytics Manager", "Analytics Mgr, VP Store Ops, Category Mgr",
     [("Assesses: total regional sales pre vs. post, market share change, competitor activity; identifies if closure created competitor opportunity; recommends defensive actions", "Analytics Manager", "VP Store Ops", "2–3 days + 1 day")]),
    ("Employee Redeployment Success Metrics", "6 months post-redeployment", "6 months after", "~15–20 redeployed employees", "HR Director", "HR Dir, Receiving Store Managers, CHRO",
     [("Surveys: satisfaction, performance, commute, retention at 6 and 12 months; identifies best practices; updates HR policies", "HR Director", "CHRO", "3–5 days + 2–3 days")]),
    ("Network Optimization Analysis", "Annual network review", "Annual; 200 stores", "Full network", "VP Store Operations", "VP Store Ops, VP Real Estate, FP&A Dir, CEO",
     [("Reviews all store performance, identifies future closure candidates, evaluates new opportunities in vacated areas; FP&A models scenarios; optimal network plan to Executive Committee", "VP Store Ops / FP&A Director", "CEO", "5–10 days + 3–5 days")]),
    ("Closure Playbook Maintenance", "Annual or post-closure", "Annual; updated after each closure", "Living document", "Store Closure Project Manager", "Closure PM, COO, all functions",
     [("Updates playbook: process improvements, new regulations, cost benchmarks, contacts; COO reviews and approves; distributes to Regional Ops and VP Real Estate", "Closure PM / COO", "CEO", "2–3 days + 1 day")])
]), "staff-redeployment-post-closure"))
t = write_readme(d, n, nm, fam, ov, ps); grand += t
print(f"VS-{n}: {nm} — {t}")

# ═══ VS-60 ═══
d = "VS-60-omnichannel-order-routing"; n = 60; nm = "Omnichannel Order Routing & Fulfillment Orchestration"; fam = "Sell & Serve"
ov = "Manages intelligent routing and orchestration of customer orders across multiple fulfillment sources: stores, DCs, vendor drop-ship, and dark stores. Covers order source selection, split-order management, fulfillment tracking, and optimization. Critical for mixed-basket orders containing items from multiple origins."
ps = []
ps.append(("PA-60.1", "Intelligent Order Routing & Source Selection", write_pa(d, n, nm, fam, "PA-60.1", "intelligent-order-routing", "Intelligent Order Routing & Source Selection", [
    ("Order Source Selection Engine", "Customer places order", "~46,400 orders/month", "~46,400 routing decisions/month", "Ecommerce Operations Manager", "Ecom Ops Mgr, System, DC Ops, Store Ops",
     [("System evaluates per line item: nearest store, DC, vendor drop-ship, dark store; selects by speed, cost, availability, item type; BOPIS → customer-selected store; delivery → fastest+cheapest", "System", "Ecom Ops Manager", "<5 sec automated")]),
    ("Mixed-Basket Order Splitting", "Order items from multiple sources", "~30–40% of ecommerce orders", "~12K–17K split orders/month", "Order Management System", "OMS, DC Ops, Store Ops, Logistics",
     [("System splits by source: store → BOPIS/ship-from-store, DC → DC fulfillment, vendor → drop-ship, dark store → micro-fulfillment; creates linked sub-orders; communicates split to customer", "System", "Ecom Ops Manager", "Automated")]),
    ("Ship-from-Store Order Processing", "Order routed to store", "~8K–12K/month", "~8K–12K/month", "Store Stock Associate", "Stock Associate, Store Manager, Logistics",
     [("System generates pick list; Associate picks, packs, generates label; 3PL pickup scheduled per VS-56; system updates tracking; customer notified; delivery in 2–3 days", "Stock Associate / System / 3PL", "Store Manager", "15–30 min + 2–3 days")]),
    ("Vendor Drop-Ship Order Processing", "Order routed to vendor", "~2K–4K/month; bulky/appliances", "~2K–4K/month", "Vendor Management Coordinator", "Vendor Coord, Vendor, Customer Service",
     [("System creates drop-ship PO with customer address; vendor confirms in 24 hours; ships with BuildRight packaging; system tracks; vendor confirms delivery; revenue recognized", "System / Vendor", "Vendor Coord", "1–2 days + 3–7 days")]),
    ("Inventory Reservation & Allocation", "Order placed", "~46,400 orders/month", "~46,400 reservations/month", "Order Management System", "OMS, Inventory System, DC Ops, Store Ops",
     [("System reserves ATP at source; prevents double-selling; holds for window (BOPIS: 5 days, delivery: 24 hours); expired reservations cancelled, inventory restored, refund processed", "System", "Inventory Manager", "Automated")]),
    ("Order Routing Exception Management", "Routing failure", "~2K–3K exceptions/month (~5%)", "~2K–3K/month", "Ecommerce Operations Manager", "Ecom Ops Mgr, Store Ops, DC Ops, CS",
     [("System detects: stock-out after reservation, store unable to fulfill, vendor rejection; Manager re-routes to alternative source; communicates revised timeline; systemic issues to IT", "System / Ecom Ops Manager", "VP Marketing", "15–30 min/exception")]),
    ("Fulfillment Priority & SLA Management", "Continuous SLA tracking", "Continuous; ~46,400 orders/month", "~46,400 SLA-tracked orders/month", "Ecommerce Operations Manager", "Ecom Ops Mgr, Logistics, CS",
     [("SLA: BOPIS 4 hours, Metro delivery 2 days, Provincial 5 days, Drop-ship 7 days; daily monitoring for at-risk orders; escalation to alternate source or expedited shipping", "System / Ecom Ops Manager", "VP Marketing", "1–2 hours/day")]),
    ("Order Routing Cost Optimization", "Monthly cost analysis", "Monthly", "~46,400 routed orders", "Logistics Finance Analyst", "Logistics Finance Analyst, Ecom Ops Mgr, FP&A",
     [("Calculates fulfillment cost per channel; identifies cost-optimized routing patterns; recommends rule adjustments; tests in simulation before production", "Logistics Finance Analyst", "Finance Manager", "4–6 hours/month + 2–3 hours")])
]), "intelligent-order-routing"))
ps.append(("PA-60.2", "Split-Order & Mixed-Basket Fulfillment", write_pa(d, n, nm, fam, "PA-60.2", "split-order-fulfillment", "Split-Order & Mixed-Basket Fulfillment", [
    ("Multi-Source Fulfillment Coordination", "Split order across sources", "~12K–17K/month", "~12K–17K/month", "Order Management System", "OMS, Store Ops, DC Ops, Vendors, Logistics",
     [("System orchestrates: triggers pick at store, DC, sends drop-ship PO; tracks sub-orders against parent; determines delivery strategy: consolidate at DC, separate deliveries, or consolidate at store", "System", "Ecom Ops Manager", "Automated")]),
    ("Consolidated Delivery Management", "Sub-orders consolidated", "~5K–8K/month", "~5K–8K/month", "Logistics Coordinator", "Logistics Coord, DC Ops, 3PL Partners",
     [("System identifies consolidation: same DC, same customer; holds first sub-order 24 hours for consolidation; ships together; reduces cost and improves experience; tracks consolidation rate", "System / Logistics Coord", "Ecom Ops Manager", "Automated + ongoing")]),
    ("Split Order Customer Communication", "Order split", "~12K–17K notifications/month", "~12K–17K/month", "Customer Communication System", "Communication System, CS",
     [("Proactive: explains split, sub-order tracking numbers, delivery dates per sub-order, single CS contact; customer views combined status in app/web; CS has unified view", "System", "Customer", "Automated")]),
    ("Partial Order Cancellation & Modification", "Customer cancels part of split order", "~1.5K–2.5K/month", "~1.5K–2.5K/month", "Customer Service Agent", "CSA, OMS, Inventory, Finance",
     [("System cancels specific sub-order(s), restores inventory, processes partial refund, keeps remaining active; Finance adjusts: partial refund, revenue for fulfilled only, promo adjustments", "CSA / System / Finance", "CS Supervisor", "10–15 min")]),
    ("Backorder Management in Split Orders", "Item becomes unavailable in split order", "~1K–2K/month", "~1K–2K/month", "Order Management System", "OMS, CS, Merch Planner",
     [("System detects: evaluates alternatives (different source, substitute, partial shipment + backorder); customer notified of options; chooses: partial now + backorder later, substitute, or cancel", "System / Customer / CSA", "Ecom Ops Manager", "5–10 min")]),
    ("Cross-Entity Fulfillment Coordination", "Order across BuildRight entities", "~8K–12K/month", "~8K–12K/month", "Finance Manager", "Finance Mgr, Ecom Ops, Intercompany Accountant",
     [("System manages cross-entity: Depot Inc. inventory fulfills Digital Commerce Inc. order; intercompany transfer pricing applied; revenue recognized by selling entity; monthly reconciliation per VS-17", "System / Finance Manager", "CFO", "Automated + 4–6 hours/month")]),
    ("Fulfillment Quality Control", "Weekly random check", "Weekly; ~100 checks/week", "~100/week", "Ecommerce Quality Coordinator", "Ecom Quality Coord, Store Ops, DC Ops",
     [("Random 100 orders/week: correct items, quantities, packaging, label, timely dispatch; quality score by source; >2% error rate triggers corrective action", "Ecom Quality Coord", "Ecom Ops Manager", "4–6 hours/week")]),
    ("Same-Day & Express Fulfillment", "Customer selects express", "~3K–5K/month", "~3K–5K/month", "Ecommerce Operations Manager", "Ecom Ops Mgr, Store Ops, 3PL Partners",
     [("Routes only to stores with stock in radius; cutoff 12 PM; premium 3PL (GrabExpress, Lalamove Priority); store picks/packs in 2 hours; 3PL pickup in 1 hour; delivery in 4 hours; premium SLA tracking", "System / Store Staff / 3PL", "Ecom Ops Manager", "Same day")])
]), "split-order-fulfillment"))
ps.append(("PA-60.3", "Fulfillment Performance & Optimization Analytics", write_pa(d, n, nm, fam, "PA-60.3", "fulfillment-performance-analytics", "Fulfillment Performance & Optimization Analytics", [
    ("Fulfillment KPI Dashboard", "Real-time; monthly deep dive", "Real-time + monthly", "~46,400 orders/month", "Ecommerce Operations Manager", "Ecom Ops Mgr, VP Marketing, VP Supply Chain",
     [("Dashboard: fill rate by source, SLA compliance, split rate, cost per order, satisfaction by fulfillment type, return rate by source; daily flag review + monthly root cause analysis", "System / Ecom Ops Manager", "VP Marketing", "2–3 hours/day + 4–6 hours/month")]),
    ("Source Performance Comparison", "Monthly", "Monthly; 4 sources", "4 sources", "Analytics Manager", "Analytics Mgr, Ecom Ops Mgr, VP Marketing",
     [("Compares: cost per order, speed, accuracy, NPS, return rate by source; recommends volume reallocation to highest-performing; identifies improvement needs", "Analytics Manager", "VP Marketing", "4–6 hours/month + 2–3 hours")]),
    ("Order Routing Algorithm Optimization", "Quarterly", "Quarterly", "Algorithm serving ~46,400/month", "IT Data Science Lead", "Data Science Lead, Ecom Ops Mgr, IT Integration",
     [("Reviews: accuracy, SLA achievement, cost optimization; A/B tests alternatives; adjusts weightings (speed vs. cost vs. accuracy); adds new inputs; deploys after testing", "Data Science Lead", "CIO", "5–10 days + 3–5 days")]),
    ("Customer Delivery Experience Analysis", "Monthly", "Monthly; ~42,900 customers", "~42,900/month", "Customer Experience Manager", "CX Manager, Ecom Ops, Logistics, Marketing",
     [("Post-delivery CSAT/NPS by source, partner, region, type; identifies bottom performers; recommends: store training, 3PL switch, SLA adjustments", "CX Manager", "VP Marketing", "4–6 hours/month")]),
    ("Omnichannel Inventory Visibility Monitoring", "Daily; weekly analysis", "Daily; 204 locations", "~35,000 SKUs × 204 locations", "Inventory Manager", "Inventory Mgr, Ecom Ops, IT",
     [("Monitors real-time sync: POS reducing ATP, DC updates; flags delays >30 min; weekly: sync accuracy analysis; persistent issues escalated to IT", "System / Inventory Manager", "VP Supply Chain", "Real-time + 2–3 hours/week")]),
    ("Fulfillment Capacity Planning", "Quarterly", "Quarterly; 4 DCs + 200 stores", "4 DCs + 200 stores + vendor", "VP Supply Chain", "VP Supply Chain, Ecom Ops Mgr, DC Ops, Store Ops",
     [("Forecasts: peak volume, new stores, dark store capacity, vendor expansion; identifies bottlenecks; develops expansion plan: staff augmentation, DC overtime, 3PL capacity, vendor commitments", "VP Supply Chain", "COO", "3–5 days + 2–3 days")]),
    ("Return Rate by Fulfillment Source", "Monthly", "Monthly; ~5–8% ecommerce return", "All fulfillment sources", "Returns Manager", "Returns Mgr, Ecom Ops Mgr, Quality Mgr",
     [("Analyzes return reasons by source: wrong item, damaged, quality, changed mind; corrective actions: quality checks at high-return stores, packaging improvements, vendor reviews per VS-31", "Returns Manager", "VP Supply Chain", "4–6 hours/month")]),
    ("Omnichannel Fulfillment Strategy Annual Review", "Annual", "Annual", "Full strategy", "VP Marketing / VP Supply Chain", "VP Marketing, VP Supply Chain, COO, CIO, CFO",
     [("Joint review: channel mix, source allocation, cost, SLAs, satisfaction, competitive position; CIO presents tech roadmap; CFO presents financial impact; COO approves plan", "VP Marketing / VP Supply Chain / CIO / CFO", "CEO", "3–5 days + 2–3 days")])
]), "fulfillment-performance-analytics"))
t = write_readme(d, n, nm, fam, ov, ps); grand += t
print(f"VS-{n}: {nm} — {t}")

# ═══ VS-61 ═══
d = "VS-61-fuel-fleet-cost-management"; n = 61; nm = "Fuel & Fleet Cost Management"; fam = "Make & Move"
ov = "Manages BuildRight's fleet fuel procurement and consumption, toll expenses, and total fleet cost optimization. Covers the owned fleet (20% of trucks) and fuel cost monitoring for 3PL partners. With 4 DCs serving 200 stores across the Philippine archipelago, fuel and toll costs represent ~15–20% of total logistics spend."
ps = []
ps.append(("PA-61.1", "Fuel Procurement & Consumption Management", write_pa(d, n, nm, fam, "PA-61.1", "fuel-procurement-consumption", "Fuel Procurement & Consumption Management", [
    ("Fleet Fuel Card Program Management", "Fuel procurement for owned fleet", "Continuous; ~20 trucks", "~20 cards; ~PHP 2–3M/month", "Logistics Manager", "Logistics Mgr, Drivers, Finance",
     [("Manages fuel card program: issues per vehicle, limits per transaction, monitors patterns, blocks unauthorized; Finance reviews statements, matches mileage, investigates anomalies", "Logistics Manager / Finance", "VP Supply Chain", "2–3 hours/month + 4–6 hours/month")]),
    ("Fuel Price Monitoring & Procurement Optimization", "Weekly review", "Weekly; Philippine diesel/gas prices", "~PHP 2–3M monthly", "Logistics Finance Analyst", "Logistics Finance Analyst, Logistics Mgr, Procurement",
     [("Monitors DOE weekly prices; identifies optimal stations per route; calculates delivery cost impact; Procurement negotiates fleet discounts with Petron, Shell, Caltex for volume", "Logistics Finance Analyst / Procurement", "Finance Manager", "2–3 hours/week + 1–2 days/quarter")]),
    ("Vehicle Fuel Efficiency Monitoring", "Monthly vehicle review", "Monthly; ~20 vehicles", "~20 reports/month", "Fleet Supervisor", "Fleet Supervisor, Logistics Manager",
     [("Calculates: liters ÷ km; benchmarks vs. spec; flags >15% deviation; investigates: engine, tires, congestion, driver behavior; schedules maintenance or coaching", "Fleet Supervisor", "Logistics Manager", "4–6 hours/month + 2–3 hours")]),
    ("Fuel Consumption Reporting & Analytics", "Monthly reporting", "Monthly; 4 DCs × ~5 vehicles", "~20 vehicles/month", "Logistics Finance Analyst", "Logistics Finance Analyst, VP Supply Chain, CFO",
     [("Monthly report: total spend, per-vehicle, per-delivery, fuel as % of logistics cost, trend vs. budget; VP reviews with COO; identifies reduction opportunities", "Logistics Finance Analyst / VP Supply Chain", "CFO", "4–6 hours/month + 1–2 hours")]),
    ("Driver Fuel Efficiency Training", "Quarterly + new hires", "Quarterly; ~60 drivers", "~60 drivers", "Fleet Supervisor", "Fleet Supervisor, HR Training",
     [("Training: gear shifting, steady speed, idling reduction, route planning, tire pressure; monthly recognition for most efficient; linked to driver scorecard and incentive", "Fleet Supervisor / Logistics Manager", "HR", "2–3 hours/session + 1 hour/month")]),
    ("Alternative Fuel Vehicle Evaluation", "Annual fleet review", "Annual; evaluate 2–3 replacements", "20 vehicles", "VP Supply Chain", "VP Supply Chain, Fleet Supervisor, Finance, COO",
     [("Evaluates: EV for short-range, hybrid for medium, LPG/CNG for high-volume; Finance calculates TCO: acquisition, fuel savings, maintenance, charging, incentives; recommends pilot if positive ROI", "VP Supply Chain / Finance", "COO", "3–5 days + 2–3 days")]),
    ("Fuel Cost Pass-Through to 3PL", "Significant fuel change (>5%)", "Ad-hoc; ~2–4/year", "~10–15 partners", "Logistics Manager", "Logistics Mgr, Procurement, Finance, 3PL",
     [("Activates adjustment clause in contracts; adjusts per-delivery rates; Finance validates; communicates to partners; implements in ERP", "Logistics Manager / Finance", "CFO", "1–2 days + 1 day")]),
    ("Emergency Fuel Supply Management", "Fuel disruption (typhoon)", "Ad-hoc; ~1–2/year", "1–2 events/year", "Logistics Manager", "Logistics Mgr, VP Supply Chain, Procurement, COO",
     [("Tops off tanks at warning; activates backup suppliers; prioritizes essential deliveries; post-event: adjusts schedule to clear backlog; reviews emergency plan", "Logistics Manager", "VP Supply Chain", "4–8 hours + 1–2 days")])
]), "fuel-procurement-consumption"))
ps.append(("PA-61.2", "Toll, Parking & Route Cost Management", write_pa(d, n, nm, fam, "PA-61.2", "toll-route-cost", "Toll, Parking & Route Cost Management", [
    ("Toll Expense Management & Optimization", "Monthly review", "Monthly; expressway routes", "~PHP 1–2M/month", "Logistics Finance Analyst", "Logistics Finance Analyst, Fleet Supervisor, Logistics Mgr",
     [("Tracks toll per route vs. free alternatives: time saved vs. toll cost; recommends optimal: toll for time-sensitive, free for non-urgent/backhaul", "Logistics Finance Analyst / Fleet Supervisor", "Logistics Manager", "4–6 hours/month")]),
    ("RFID Fleet Toll Account Management", "Monthly account management", "Monthly; ~20 vehicles", "~20 RFID accounts", "Fleet Supervisor", "Fleet Supervisor, Finance",
     [("Loads credits, monitors balances, replaces stickers, reconciles statements vs. system; Finance reconciles toll expenses", "Fleet Supervisor / Finance", "Logistics Manager", "2–3 hours/month + 2–3 hours/month")]),
    ("Parking & Loading Dock Fee Management", "Monthly review", "Monthly; urban locations", "~PHP 200K–500K/month", "Logistics Finance Analyst", "Logistics Finance Analyst, DC Dispatch, Store Ops",
     [("Tracks fees; evaluates loading dock reservations for frequent locations; coordinates delivery windows at high-traffic urban stores to minimize wait and fees", "Logistics Finance Analyst / Logistics Manager", "Store Ops Director", "2–3 hours/month + 1–2 hours/month")]),
    ("Route Cost Benchmarking", "Quarterly", "Quarterly; ~20–30 routes", "~20–30 routes", "Logistics Manager", "Logistics Mgr, Finance, 3PL Partners",
     [("Benchmarks: per-km cost vs. industry; toll vs. no-toll; owned vs. 3PL; identifies: route consolidation, backhaul utilization, alternate routes, delivery window optimization", "Logistics Manager", "VP Supply Chain", "2–3 days/quarter + 1–2 days")]),
    ("Backhaul Utilization & Revenue", "Monthly analysis", "Monthly; ~400–500 empty return trips", "~400–500 trips/month", "Logistics Manager", "Logistics Mgr, DC Ops, Store Ops",
     [("Identifies backhaul: returns to DC, inter-DC transfers, vendor pickup, third-party freight; targets reducing empty backhaul from ~60% to <40%; tracks utilization rate", "Logistics Manager", "VP Supply Chain", "4–6 hours/month + 2–3 hours/month")]),
    ("Fleet Insurance Cost Management", "Annual renewal", "Annual; ~20 vehicles", "~20 policies", "Finance Manager", "Finance Mgr, Logistics Mgr, Insurance Provider",
     [("Obtains competitive quotes; reviews coverage; processes claims per VS-26; manages no-claims bonuses; Logistics Manager maintains driver safety records for favorable rates", "Finance Manager / Logistics Manager", "CFO", "3–5 days/year")]),
    ("Vehicle Maintenance Cost Tracking", "Monthly", "Monthly; ~20 vehicles", "~20 records/month", "Fleet Supervisor", "Fleet Supervisor, Logistics Mgr, Finance",
     [("Tracks per-vehicle: scheduled maintenance, unscheduled repairs, accident repairs; per-km maintenance cost; Finance includes in TCO; recommends replacement when cost exceeds depreciation savings", "Fleet Supervisor / Finance", "VP Supply Chain", "4–6 hours/month + 2–3 hours/month")]),
    ("Total Fleet Cost of Ownership Dashboard", "Monthly dashboard", "Monthly", "20 owned + 10–15 3PL partners", "VP Supply Chain", "VP Supply Chain, Finance Dir, COO",
     [("Dashboard: total cost (owned + 3PL), per delivery, per km, per peso delivered, fuel %, toll %, maintenance %, insurance %; targets logistics cost at 8–10% of COGS", "System / VP Supply Chain", "COO", "2–3 hours/month")])
]), "toll-route-cost"))
ps.append(("PA-61.3", "Fleet Total Cost of Ownership Analytics", write_pa(d, n, nm, fam, "PA-61.3", "fleet-total-cost-analytics", "Fleet Total Cost of Ownership Analytics", [
    ("Annual Fleet TCO Analysis", "Annual budget cycle", "Annual", "20 owned vehicles", "Finance Director", "Finance Dir, VP Supply Chain, COO",
     [("Calculates TCO per vehicle: depreciation + fuel + maintenance + insurance + tolls + driver + overhead; compares vs. 3PL cost; VP recommends own vs. outsource by route", "Finance Director / VP Supply Chain", "CFO", "5–10 days + 3–5 days")]),
    ("Vehicle Replacement Cost-Benefit Analysis", "Vehicle replacement criteria met", "2–3/year", "~2–3 evaluations/year", "Fleet Supervisor", "Fleet Supervisor, Finance, VP Supply Chain",
     [("Identifies: >8 years, >300K km, maintenance >30% of value; Finance calculates replacement vs. continued maintenance; VP recommends model; Finance approves budget", "Fleet Supervisor / Finance / VP Supply Chain", "COO", "3–5 days + 2–3 days")]),
    ("Fleet Utilization Rate Analysis", "Monthly", "Monthly; ~20 vehicles", "~20 reports/month", "Fleet Supervisor", "Fleet Supervisor, Logistics Manager",
     [("Calculates: % available hours delivering, % capacity utilized per trip, idle time; targets ≥75% utilization; identifies underutilized for redeployment or disposal", "Fleet Supervisor", "Logistics Manager", "4–6 hours/month")]),
    ("Fleet Carbon Footprint Estimation", "Annual sustainability reporting", "Annual", "20 owned + 3PL", "ESG Manager", "ESG Manager, Logistics Mgr, VP Supply Chain",
     [("Calculates: fuel × emission factor; estimates 3PL emissions from volume; identifies reduction: route optimization, fuel-efficient, alternative fuels, load optimization; feeds VS-25", "ESG Manager", "VP Supply Chain", "3–5 days/year + 2–3 days")]),
    ("Fleet Safety Cost Analysis", "Quarterly", "Quarterly", "~20 vehicles", "Safety Officer", "Safety Officer, Logistics Mgr, Finance",
     [("Analyzes: accident repair, cargo damage, insurance premium impact, driver injury, third-party liability; recommends: training, safety features, route risk assessment", "Safety Officer", "VP Supply Chain", "4–6 hours/quarter + 2–3 hours")]),
    ("3PL Cost Benchmarking & Negotiation", "Quarterly", "Quarterly; ~10–15 partners", "~10–15 partners", "Procurement Manager", "Procurement Mgr, Logistics Mgr, Finance",
     [("Benchmarks vs. market; identifies above-market partners; negotiates reductions; Finance validates savings; Logistics plans transition if needed per VS-56", "Procurement / Finance / Logistics Mgr", "VP Supply Chain", "2–3 days + 1–2 days")]),
    ("Logistics Cost as % of Revenue", "Monthly KPI", "Monthly", "Full logistics vs. revenue", "FP&A Director", "FP&A Dir, VP Supply Chain, CFO, COO",
     [("Calculates: logistics cost % of revenue and COGS; benchmarks vs. Philippine retail (8–12% of COGS); presents to COO with variance analysis", "FP&A Director", "CFO", "2–3 hours/month + 1–2 hours")]),
    ("5-Year Fleet Investment Plan", "Annual capital planning", "Annual; 5-year horizon", "20 vehicles + growth", "VP Supply Chain / CFO", "VP Supply Chain, CFO, COO, CEO",
     [("Develops: replacement schedule, expansion for store growth (10–15/year), technology (GPS, telematics, EV charging); CEO/Board approve; feeds VS-40 Capex budget", "VP Supply Chain / CFO", "CEO", "5–10 days + 2–3 days")])
]), "fleet-total-cost-analytics"))
t = write_readme(d, n, nm, fam, ov, ps); grand += t
print(f"VS-{n}: {nm} — {t}")

print(f"\nSubtotal VS-58 to VS-61: {grand}")
print(f"Running total: {120 + grand}")
print(f"Next workflow ID: W{wf_counter}")
