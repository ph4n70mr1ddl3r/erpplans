#!/usr/bin/env python3
"""Generate VS-62 through VS-68."""
import os
BASE = "/home/riddler/erpplans/01-model-company/workflows"
wf_counter = 2334

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

def mk_vs(d, n, nm, fam, ov, pas_data):
    ps = []
    for pa_num, pa_slug, pa_title, wfs in pas_data:
        ps.append((pa_num, pa_title, write_pa(d, n, nm, fam, pa_num, pa_slug, pa_title, wfs), pa_slug))
    t = write_readme(d, n, nm, fam, ov, ps)
    print(f"VS-{n}: {nm} — {t}")
    return t

grand = 0

# ═══ VS-62: Product Sample & Display Management ═══
grand += mk_vs("VS-62-product-sample-display-management", 62,
    "Product Sample & Display Management", "Sell & Serve",
    "Manages BuildRight's product sample inventory for tiles, flooring, countertops, fabric swatches, and paint color cards. Covers sample procurement and distribution to 200 stores, display maintenance and refresh cycles, sample-to-order conversion tracking, and display ROI analytics. Critical for high-consideration categories where tactile experience drives purchase decisions.",
    [("PA-62.1", "sample-inventory-procurement", "Sample Inventory Procurement & Distribution", [
    ("Tile & Flooring Sample Procurement", "Quarterly sample refresh or new product launch", "Quarterly; ~200 stores × 8–10 tile sample boards", "~1,600–2,000 tile sample boards/quarter", "Category Manager (Tiles)", "Category Mgr, Vendor, Merch Planner, DC Ops",
     [("Category Manager selects tile/flooring SKUs requiring sample displays; coordinates with vendor for sample production (physical tile pieces mounted on display boards with pricing)", "Category Manager", "VP Merchandising", "2–3 days"),
      ("Vendor delivers samples to DC; DC distributes to stores via regular replenishment; Store Manager merchandises samples in Tile Gallery zone per VS-55 planogram", "Vendor / DC / Store Manager", "Category Manager", "1–2 weeks")]),
    ("Paint Color Card & Swatch Management", "Seasonal refresh or new paint line introduction", "Semi-annual; ~200 stores × 200 color cards", "~40,000 color cards per refresh cycle", "Category Manager (Paint)", "Category Mgr, Paint Vendor, Store Ops",
     [("Category Manager orders updated color card sets from paint vendor; includes all available tints with BuildRight pricing; vendor prints and delivers to DC", "Category Manager", "Vendor", "1–2 days"),
      ("DC distributes to stores; Paint Station staff replaces old cards with new; old cards recycled; system tracks distribution and confirms receipt per store", "DC / Store Staff", "Store Manager", "1 week")]),
    ("Countertop & Surface Material Sample Distribution", "New product launch or annual refresh", "Annual + new launches; ~200 stores × 5–8 samples", "~1,000–1,600 countertop samples/cycle", "Category Manager (Building Materials)", "Category Mgr, Vendor, Merch Planner, DC Ops",
     [("Manager selects countertop SKUs for sample display (granite, quartz, laminate); vendor produces sample chips; distributed via DC; stores display in dedicated counter zone", "Category Manager / Vendor", "VP Merchandising", "2–3 days + 1–2 weeks")]),
    ("Sample Inventory Tracking & Replenishment", "Monthly inventory review of sample stock", "Monthly; 200 stores", "~200 store sample inventories/month", "Merchandising Coordinator", "Merch Coordinator, Store Manager, DC Ops",
     [("System tracks sample inventory per store: tile boards, color cards, countertop chips, fabric swatches; flags stores with damaged/missing samples below minimum threshold", "System / Merch Coordinator", "Merchandising Planner", "2–3 hours/month"),
      ("Coordinator generates replenishment orders; samples picked at DC and shipped with regular store delivery; Store Manager confirms receipt and displays", "Merch Coordinator / DC", "Store Manager", "1–2 weeks")]),
    ("Sample Vendor Negotiation & Cost Management", "Annual vendor review for sample costs", "Annual; ~20 sample vendors", "~20 vendor negotiations/year", "Category Manager", "Category Mgr, Procurement, Finance",
     [("Category Manager negotiates sample costs: tile boards, color cards, countertop chips; typically vendor-funded or cost-shared; includes in vendor co-op budget per VS-39", "Category Manager / Procurement", "Finance Manager", "1–2 days/year")]),
    ("Digital Sample & Augmented Reality Tool Management", "Quarterly app update or new feature launch", "Quarterly app updates; continuous availability", "~42,900 ecommerce customers + in-store tablet users", "Digital Product Manager", "Digital PM, IT, Category Mgr, Vendor",
     [("Digital PM manages AR/3D visualization tools in BuildRight app: tile visualizer (see tile in your room), paint color visualizer, countertop preview; updates product catalog quarterly", "Digital PM / IT", "CIO", "Ongoing"),
      ("Category Manager validates color/texture accuracy of digital samples vs. physical; coordinates with vendor for digital assets (3D models, high-res textures)", "Category Manager / Vendor", "Digital PM", "Quarterly")]),
    ("Sample-to-Order Conversion Process", "Customer selects product based on sample display", "Continuous; ~2,000–3,000 sample-assisted sales/month", "~2K–3K/month across tile, flooring, countertop categories", "Sales Associate", "Sales Associate, Customer, CRM",
     [("Sales Associate assists customer at sample display; identifies selected sample; scans sample barcode or looks up SKU in system; checks inventory and pricing; creates quote or sales order", "Sales Associate", "Department Supervisor", "15–30 min"),
      ("System logs sample-assisted sale: sample ID → SKU → transaction; tracks conversion rate per sample per store; feeds sample ROI analytics", "System", "Category Manager", "Automated")]),
    ("Seasonal Sample Refresh Execution", "Seasonal transition (6 rotations/year)", "6/year; 200 stores", "~1,200 seasonal sample refreshes/year", "Merchandising Coordinator", "Merch Coordinator, Store Managers, DC Ops",
     [("Coordinator issues seasonal sample refresh instructions: remove off-season samples, install new season samples; DC pre-stages seasonal sample kits; stores execute during planogram rotation per VS-55", "Merch Coordinator / DC / Store Manager", "Merchandising Planner", "1–2 weeks per rotation")])
    ]),
    ("PA-62.2", "display-maintenance-sample-refresh", "Display Maintenance & Sample Refresh", [
    ("Monthly Display Condition Inspection", "Monthly inspection cycle", "Monthly; 200 stores × 8 zones", "~1,600 zone inspections/month", "Regional Operations Manager", "Regional Ops Mgr, Store Manager, Merch Coord",
     [("Regional Ops Manager or designated inspector checks sample displays: condition, cleanliness, completeness, pricing accuracy, visual merchandising standards; scores each zone", "Regional Ops Mgr", "Store Ops Director", "2–3 hours/store"),
      ("Store Manager remediates issues within 48 hours; damaged samples replaced from store reserve or ordered from DC; persistent issues escalated to Merchandising Coordinator", "Store Manager", "Regional Ops Mgr", "2–4 hours")]),
    ("Damaged Sample Replacement Process", "Store reports damaged or missing sample", "Ad-hoc; ~500–800 replacements/month", "~500–800/month across 200 stores", "Store Department Supervisor", "Dept Supervisor, Merch Coordinator, DC Ops",
     [("Supervisor reports damaged sample in system: sample ID, damage type, photo; system generates replacement order; Merch Coordinator approves; replacement shipped with next DC delivery", "Dept Supervisor / System", "Merch Coordinator", "10 min + 3–5 days delivery")]),
    ("Sample Display Area Cleaning & Maintenance", "Weekly scheduled maintenance", "Weekly; 200 stores", "~200 stores/week", "Store Staff", "Store Staff, Department Supervisor",
     [("Designated staff cleans sample displays weekly: dust tile boards, wipe countertop chips, replace faded color cards, clean display fixtures, organize sample order", "Store Staff", "Department Supervisor", "30–45 min/week")]),
    ("Sample Display Signage & Pricing Update", "Price change or new sample added", "~200–300 updates/month", "~200–300/month", "Store Department Supervisor", "Dept Supervisor, Pricing Analyst, Merch Coord",
     [("System generates sample pricing labels when SRP changes; Supervisor prints and applies to sample display; ensures sample SKU, product name, price, and order availability match current data", "Dept Supervisor / System", "Store Manager", "1–2 hours/month")]),
    ("Interactive Display Technology Maintenance", "Monthly maintenance or malfunction", "Monthly; ~50 stores with tablet/kiosk displays", "~50 stores/month", "IT Support", "IT Support, Store Manager, Digital PM",
     [("IT Support maintains interactive sample displays: in-store tablets with AR visualizer, digital kiosks with product catalog; updates software, replaces damaged tablets, troubleshoots connectivity", "IT Support", "CIO", "2–3 hours/store/month")]),
    ("Vendor-Funded Display Program Management", "Vendor offers branded display fixture", "~10–15 vendor display programs/year", "~10–15 programs/year", "Category Manager", "Category Mgr, Marketing, Vendor, Store Ops",
     [("Vendor proposes branded display (e.g., Bosch power tool wall, Boysen paint station); Category Manager evaluates: brand alignment, customer experience, space requirement, vendor funding level", "Category Manager", "VP Merchandising", "2–3 days/program"),
      ("Approved displays: vendor provides fixture and installation; Store Ops coordinates placement; Category Manager monitors performance (traffic, conversion, sales lift) vs. standard display", "Vendor / Store Ops / Category Manager", "VP Merchandising", "1–2 weeks + ongoing")]),
    ("Sample Display Performance Review", "Quarterly analytics review", "Quarterly; 200 stores", "~200 stores analyzed quarterly", "Analytics Manager", "Analytics Mgr, Category Mgr, VP Merchandising",
     [("Analytics Manager measures display performance: sales per display zone, sample-to-order conversion rate, dwell time at displays, customer feedback; identifies top/bottom performing displays", "Analytics Manager", "Category Manager", "2–3 days/quarter")]),
    ("Sample Display Decommissioning", "Product delisted or display program ended", "~50–100 decommissions/year", "~50–100/year", "Merchandising Coordinator", "Merch Coordinator, Store Manager, Facilities",
     [("Coordinator issues decommission: remove samples, dismantle fixture, return vendor-owned displays, dispose/recycle BuildRight-owned materials; restore zone to standard planogram", "Merch Coordinator / Store Manager / Facilities", "Category Manager", "1–2 weeks")])
    ]),
    ("PA-62.3", "sample-display-roi-analytics", "Sample & Display ROI Analytics", [
    ("Sample Program Cost Tracking", "Monthly financial analysis", "Monthly; all sample programs", "All sample categories", "Finance Analyst", "Finance Analyst, Category Mgr, VP Merchandising",
     [("Tracks: sample procurement cost, distribution cost, display maintenance cost, digital tool cost; calculates total sample program cost per category per quarter", "Finance Analyst", "Finance Manager", "4–6 hours/month")]),
    ("Sample-to-Order Conversion Rate Analysis", "Monthly analysis", "Monthly; 200 stores", "~200 stores/month", "Analytics Manager", "Analytics Mgr, Category Mgr, Sales Associates",
     [("Calculates: % of sample interactions leading to sale; by category, by sample, by store; identifies highest-converting samples and underperformers; recommends display changes", "Analytics Manager", "Category Manager", "4–6 hours/month")]),
    ("Display Zone Sales Attribution", "Quarterly deep analysis", "Quarterly; display zones across 200 stores", "~1,600 zones analyzed", "Analytics Manager", "Analytics Mgr, Category Mgr, VP Merchandising",
     [("Attributes sales to display zones: compares sales per sqm in sample display zones vs. non-display zones in same category; measures uplift from sample presence", "Analytics Manager", "VP Merchandising", "3–5 days/quarter")]),
    ("Sample Program Annual ROI", "Annual comprehensive review", "Annual", "Full sample program", "FP&A Analyst", "FP&A, Category Mgrs, VP Merchandising",
     [("Calculates: total sample program cost vs. incremental revenue attributed to sample displays; ROI by category; recommends budget allocation for next year", "FP&A Analyst", "CFO", "3–5 days")]),
    ("Customer Feedback on Sample Experience", "Quarterly survey", "Quarterly; ~500 respondents", "~500 respondents/quarter", "Customer Experience Manager", "CX Manager, Category Mgr, Marketing Research",
     [("Survey: customer satisfaction with sample displays, usefulness of physical samples, interest in digital/AR tools, suggestions for improvement; feeds into display strategy", "CX Manager", "VP Marketing", "2–3 days/quarter")]),
    ("Digital vs. Physical Sample Effectiveness", "Semi-annual comparison", "Semi-annual", "Digital tool users vs. in-store sample users", "Digital Product Manager", "Digital PM, Analytics Mgr, Category Mgr",
     [("Compares: digital tool usage → conversion rate vs. physical sample interaction → conversion rate; cost per conversion; customer preference; recommends channel investment", "Digital PM / Analytics Manager", "VP Marketing", "3–5 days/semi-annual")]),
    ("Competitor Sample Display Benchmarking", "Annual competitive review", "Annual; 4–5 competitors", "4–5 competitor display programs", "Marketing Analyst", "Marketing Analyst, Category Mgr, VP Merch",
     [("Mystery shops competitor stores: evaluates sample display quality, variety, digital integration, customer experience; compares to BuildRight; identifies gaps and best practices", "Marketing Analyst", "VP Merchandising", "3–5 days")]),
    ("Sample Program Innovation & Technology Roadmap", "Annual strategy review", "Annual", "Full sample program strategy", "VP Merchandising", "VP Merch, CIO, Category Mgrs, COO",
     [("Reviews: emerging display technologies (VR showroom, 3D printing samples, AI color matching); evaluates ROI; recommends technology investments; presents to Executive Committee", "VP Merchandising / CIO", "CEO", "3–5 days")])
    ])
])

# ═══ VS-63: Store Communication & Task Management ═══
grand += mk_vs("VS-63-store-communication-task-management", 63,
    "Store Communication & Task Management", "Sell & Serve",
    "Manages HQ-to-store communication, task assignment, execution tracking, and compliance monitoring across 200 BuildRight stores. Covers the store communication platform, task lifecycle from HQ assignment through store execution and verification, and communication effectiveness analytics. Essential for maintaining operational consistency across a geographically distributed retail chain spanning Mindanao, Visayas, and Luzon.",
    [("PA-63.1", "hq-store-communication", "HQ-to-Store Communication & Broadcast", [
    ("Corporate Announcement Broadcasting", "Corporate announcement from HQ", "~10–15 announcements/month", "~10–15 broadcasts to 200 stores/month", "VP Corporate Communications", "VP Corp Comms, Store Managers, Regional Ops",
     [("VP Corp Comms drafts announcement in store communication platform: targets (all stores, regional, specific stores), priority (info/action/urgent), category (policy, promo, safety, HR); attaches documents", "VP Corp Comms", "COO", "30–60 min"),
      ("System pushes to store manager app with notification; tracks read receipts per store; auto-escalates unread urgent messages after 4 hours; Regional Ops follows up with non-responsive stores", "System / Regional Ops Mgr", "VP Corp Comms", "Automated")]),
    ("Merchandising Directive Communication", "Planogram change or merchandising directive", "~20–30 directives/month", "~20–30/month to 200 stores", "Merchandising Coordinator", "Merch Coordinator, Store Managers, Regional Ops",
     [("Coordinator creates merchandising directive: action required, affected zones, product details, photos of expected result, deadline, compliance photo requirement; distributes to stores", "Merch Coordinator", "Merchandising Planner", "1–2 hours"),
      ("Store Manager acknowledges receipt; assigns to stock team; executes by deadline; submits compliance photos; Coordinator verifies within 48 hours", "Store Manager / Merch Coordinator", "Merchandising Planner", "1–2 hours + execution time")]),
    ("Emergency Communication Protocol", "Emergency event (typhoon, safety incident, system outage)", "Ad-hoc; ~5–10 emergencies/year", "~5–10 emergency broadcasts/year to 200 stores", "COO", "COO, VP Corp Comms, Store Managers, Regional Ops",
     [("COO or designated executive sends emergency broadcast: mandatory read, audio alert on store devices, clear instructions (close store, evacuate, shelter in place, system workaround)", "COO", "CEO", "15–30 min"),
      ("System tracks real-time acknowledgment; non-responding stores contacted by phone; Regional Ops confirms physical safety; follow-up communications as situation evolves", "System / Regional Ops Mgr", "COO", "Continuous during emergency")]),
    ("Weekly Store Manager Newsletter", "Weekly editorial schedule", "Weekly; 200 Store Managers", "~200 recipients/week", "Store Operations Director", "Store Ops Dir, Merch, Marketing, HR, LP",
     [("Store Ops Dir curates weekly newsletter: top-performing stores, new procedures, upcoming promos, compliance scores, safety tips, HR updates; system distributes every Monday morning", "Store Ops Dir", "COO", "2–3 hours/week")]),
    ("Two-Way Store Feedback Channel", "Store Manager submits feedback or question", "Continuous; ~50–100 feedback items/month", "~50–100/month", "Store Manager", "Store Manager, Regional Ops Mgr, HQ Functions",
     [("Store Manager submits feedback/question via store manager app: category (operations, IT, merch, HR, facilities), priority, description, photos if applicable", "Store Manager", "Regional Ops Mgr", "10–15 min"),
      ("System routes to appropriate HQ function; SLA: 24 hours for urgent, 72 hours for standard; Store Manager receives response and resolution; satisfaction rating on resolution", "System / HQ Function", "Store Ops Director", "24–72 hours SLA")]),
    ("Policy & Procedure Update Distribution", "Policy or procedure change", "~5–10 policy updates/month", "~5–10/month to 200 stores", "VP Legal / VP Store Operations", "VP Legal, VP Store Ops, Store Managers, HR",
     [("VP Legal or VP Store Ops drafts policy update with effective date, rationale, action required, training requirement if applicable; distributes with mandatory acknowledgment", "VP Legal / VP Store Ops", "COO", "2–4 hours"),
      ("Store Managers must acknowledge within 48 hours; system tracks compliance; stores with unacknowledged policies flagged to Regional Ops; non-compliance tracked in store scorecard", "System / Regional Ops Mgr", "VP Store Ops", "48 hours")]),
    ("Seasonal Preparation Communication Package", "Pre-season communication (6 seasons/year)", "6/year; 200 stores", "~1,200 seasonal packages/year", "Merchandising Planner", "Merch Planner, Marketing, Store Ops, HR",
     [("Merch Planner assembles seasonal package: merchandising changes, promotional calendar, expected volume, staffing recommendations, safety considerations for seasonal products", "Merch Planner / Marketing / HR", "VP Merchandising", "2–3 days"),
      ("Distributes to stores 3 weeks before season start; includes training videos, planogram updates, compliance deadlines; Store Managers acknowledge and confirm readiness", "System / Store Manager", "Merchandising Planner", "1 week")]),
    ("Communication Platform Training & Support", "New feature rollout or new user onboarding", "~200 Store Managers trained; ad-hoc feature training", "200 users; ~10–15 new users/year (turnover)", "IT Training Specialist", "IT Training, Store Managers, Regional Ops",
     [("IT Training conducts platform training: new feature walkthrough, best practices, common issues; onboarding for new Store Managers includes communication platform module", "IT Training Specialist", "CIO", "2–3 hours/session"),
      ("Maintains help center with FAQs, video tutorials, and troubleshooting guides; provides helpdesk support for platform issues (response SLA: 4 hours)", "IT Support", "IT Training Specialist", "Ongoing")])
    ]),
    ("PA-63.2", "store-task-compliance", "Store Task Assignment & Compliance Tracking", [
    ("Task Creation & Assignment from HQ", "HQ function creates task for stores", "~100–200 tasks/week across all HQ functions", "~400–800 tasks/month to 200 stores", "HQ Function Manager", "HQ Function Mgr, Store Managers, Regional Ops",
     [("HQ Manager creates task: description, assigned stores (all/regional/specific), priority, category, deadline, required evidence (photo/checkbox/form), responsible role at store", "HQ Function Mgr", "Store Ops Director", "15–30 min"),
      ("System pushes to assigned stores; Store Manager acknowledges and assigns to responsible staff; system tracks status (assigned/in-progress/completed/overdue)", "System / Store Manager", "HQ Function Mgr", "Automated + 10 min")]),
    ("Store-Level Task Execution & Reporting", "Store receives task assignment", "~400–800 tasks/month", "~2–4 tasks/store/week", "Store Manager", "Store Manager, Department Supervisors, Staff",
     [("Store Manager reviews task requirements; assigns to appropriate Department Supervisor or staff member; sets internal deadline ahead of HQ deadline", "Store Manager", "Regional Ops Mgr", "10–15 min"),
      ("Staff executes task; documents completion with required evidence (photo, form, confirmation); submits via store manager app; Store Manager reviews and approves before submission to HQ", "Store Staff / Store Manager", "HQ Function Mgr", "Varies by task")]),
    ("Task Compliance Dashboard", "Real-time; weekly review", "Continuous; weekly deep review", "200 stores; ~400–800 active tasks/month", "Store Operations Director", "Store Ops Dir, Regional Ops Mgr, HQ Functions",
     [("Dashboard: task completion rate by store, region, and function; overdue tasks highlighted; compliance score trending; non-responsive stores flagged for Regional Ops follow-up", "System / Store Ops Dir", "COO", "30 min/day + 2–3 hours/week")]),
    ("Regional Operations Follow-Up", "Store has overdue or non-compliant tasks", "Daily; ~20–30 overdue tasks/week", "~20–30 overdue follow-ups/week", "Regional Operations Manager", "Regional Ops Mgr, Store Manager",
     [("Regional Ops Manager contacts Store Manager for overdue tasks; determines root cause (staffing, training, system issue); provides support or escalates to HQ", "Regional Ops Mgr", "Store Ops Director", "15–30 min/store")]),
    ("Task Template & Standardization Management", "New task type creation or template update", "~5–10 new task templates/quarter", "~20–40 templates maintained", "Store Operations Director", "Store Ops Dir, HQ Functions, IT",
     [("Store Ops Dir standardizes task templates: predefined steps, required evidence, typical duration, responsible role; ensures consistency across HQ functions; IT configures in platform", "Store Ops Dir / IT", "COO", "1–2 days/quarter")]),
    ("Task Completion Quality Audit", "Monthly quality spot-check", "Monthly; ~50 completed tasks audited", "~50 tasks/month", "Regional Operations Manager", "Regional Ops Mgr, Store Manager, HQ Function",
     [("Regional Ops Manager randomly audits completed tasks: verifies evidence quality, accuracy of completion, actual vs. reported execution; identifies patterns of low-quality completion", "Regional Ops Mgr", "Store Ops Director", "4–6 hours/month")]),
    ("Seasonal Task Calendar Management", "Pre-season planning", "6 seasons/year; tasks planned 3 weeks ahead", "~100–200 seasonal tasks/year", "Merchandising Coordinator", "Merch Coordinator, Store Ops Dir, HQ Functions",
     [("Coordinator creates seasonal task calendar: merchandising changes, promotional setup, safety checks, staffing tasks; assigns pre-populated deadlines aligned with seasonal rotation", "Merch Coordinator", "VP Merchandising", "2–3 days/season")]),
    ("Task Analytics & Process Improvement", "Monthly analytics; quarterly improvement review", "Monthly analytics; quarterly review", "200 stores; ~400–800 tasks/month", "Analytics Manager", "Analytics Mgr, Store Ops Dir, HQ Functions",
     [("Analyzes: task completion rate, on-time rate, quality score by function, by store, by region; identifies bottlenecks and improvement opportunities; quarterly process improvement recommendations", "Analytics Manager", "Store Ops Director", "4–6 hours/month + 2–3 days/quarter")])
    ]),
    ("PA-63.3", "communication-effectiveness-analytics", "Communication Effectiveness & Feedback Analytics", [
    ("Communication Read Rate Analysis", "Weekly analysis", "Weekly; all communications sent", "~10–15 broadcasts + ~400–800 tasks/week", "Store Operations Director", "Store Ops Dir, VP Corp Comms, Regional Ops",
     [("System calculates: read rate per communication (target ≥95% within 24 hours for urgent, ≥90% within 48 hours for standard); identifies stores/regions with chronically low read rates", "System / Store Ops Dir", "COO", "30 min/week")]),
    ("Task Completion Rate Trending", "Monthly analysis", "Monthly; all tasks", "~400–800 tasks/month", "Analytics Manager", "Analytics Mgr, Store Ops Dir, HQ Functions",
     [("Tracks: overall completion rate, on-time rate, quality score; trends over 6 months; identifies improving/declining functions and regions; root cause analysis for declining areas", "Analytics Manager", "Store Ops Director", "4–6 hours/month")]),
    ("Store Manager Satisfaction Survey", "Quarterly survey", "Quarterly; 200 Store Managers", "200 respondents/quarter", "HR Manager", "HR Manager, Store Ops Dir, CHRO",
     [("Survey: communication clarity, task relevance, platform usability, response time from HQ, overall satisfaction; identifies pain points and improvement priorities", "HR Manager", "Store Ops Director", "2–3 days/quarter")]),
    ("Communication Channel Effectiveness", "Semi-annual channel review", "Semi-annual", "3 channels: app, email, SMS", "Digital Product Manager", "Digital PM, Store Ops Dir, IT",
     [("Analyzes: delivery success rate, open rate, response time by channel; identifies optimal channel per communication type; recommends channel strategy adjustments", "Digital PM", "CIO", "2–3 days/semi-annual")]),
    ("Information Overload Assessment", "Quarterly review", "Quarterly", "200 stores receiving communications", "Store Operations Director", "Store Ops Dir, VP Corp Comms, HQ Functions",
     [("Reviews volume of communications per store per week; identifies periods of excessive volume (>15 communications/week); recommends consolidation and prioritization to prevent overload", "Store Ops Dir", "COO", "2–3 hours/quarter")]),
    ("Communication Platform Usage Analytics", "Monthly analytics", "Monthly", "200 Store Managers + HQ users", "IT System Admin", "IT System Admin, Store Ops Dir, Digital PM",
     [("Tracks: platform active users, feature adoption, login frequency, app version compliance, device issues; identifies stores needing technical support or training", "IT System Admin", "CIO", "2–3 hours/month")]),
    ("Store Communication Best Practice Sharing", "Quarterly best practice review", "Quarterly; 200 stores", "~5–10 best practices identified/quarter", "Store Operations Director", "Store Ops Dir, Regional Ops, Store Managers",
     [("Identifies top-performing stores in communication compliance; documents their practices (task management routines, staffing for execution, communication habits); shares across chain", "Store Ops Dir", "COO", "1 day/quarter")]),
    ("Communication Strategy Annual Review", "Annual strategy review", "Annual", "Full communication strategy", "VP Corporate Communications", "VP Corp Comms, Store Ops Dir, CIO, COO",
     [("Reviews: platform performance, communication volume trends, satisfaction scores, compliance rates, technology roadmap; presents strategy to Executive Committee with investment recommendations", "VP Corp Comms / Store Ops Dir / CIO", "CEO", "3–5 days")])
    ])
])

# ═══ VS-64: Seasonal Merchandise Transition & Clearance ═══
grand += mk_vs("VS-64-seasonal-merchandise-clearance", 64,
    "Seasonal Merchandise Transition & Clearance", "Plan & Source",
    "Manages BuildRight's seasonal merchandise lifecycle from phase-in planning through active selling to end-of-season markdown and clearance. Aligned with the Philippine seasonal calendar (dry season, rainy season, Christmas ber-months). Covers seasonal assortment planning, inventory positioning, markdown optimization, clearance execution, and post-season analysis.",
    [("PA-64.1", "seasonal-planning-phase-in", "Seasonal Planning & Phase-In Management", [
    ("Seasonal Assortment Planning", "Pre-season planning (3 months before season)", "6 seasons/year; 13 categories reviewed", "~6 seasonal assortment plans/year", "Category Manager", "Category Mgr, Merch Planner, Buyer, VP Merchandising",
     [("Category Manager identifies seasonal opportunities per Philippine calendar: summer (garden, aircon, outdoor), rainy (waterproofing, flood control), ber-months (holiday décor, gifts, appliances); selects seasonal SKUs", "Category Manager", "VP Merchandising", "3–5 days"),
      ("Merch Planner determines store-level assortment by format (flagship/standard/compact); Buyer places seasonal POs with vendors; confirms delivery timeline 6–8 weeks before season start", "Merch Planner / Buyer", "Category Manager", "5–10 days")]),
    ("Seasonal Inventory Positioning at DCs", "Seasonal inventory arriving at DCs", "Pre-season; 6 cycles/year", "~4 DCs receiving seasonal inventory", "DC Operations Manager", "DC Ops Mgr, Merch Planner, Logistics Mgr",
     [("Merch Planner provides DC with seasonal allocation plan: quantity per SKU per store group; DC receives seasonal inventory; stages for store allocation; schedules outbound shipments aligned with store display readiness", "Merch Planner / DC Ops Mgr", "VP Supply Chain", "1–2 weeks/season")]),
    ("Seasonal Planogram & Display Setup", "Seasonal display zone activation", "6/year; 200 stores", "~1,200 display setups/year", "Merchandising Coordinator", "Merch Coord, Store Managers, Regional Ops",
     [("Coordinator distributes seasonal display plan: zone assignment, product list, signage, visual merchandising guide; stores set up within 1-week window; compliance photos submitted and verified", "Merch Coord / Store Manager", "Merchandising Planner", "1 week per season")]),
    ("Seasonal Pricing & Promotion Setup", "Seasonal promotional pricing activation", "6/year; aligned with merchandising calendar", "~6 seasonal pricing events/year", "Pricing Analyst", "Pricing Analyst, Category Mgr, Marketing",
     [("Pricing Analyst sets seasonal pricing: launch price (may include early-bird promo), regular price, planned markdown triggers (based on sell-through rate); configures in ERP per VS-57", "Pricing Analyst", "Category Manager", "1–2 days/season")]),
    ("Seasonal Staff Training & Product Knowledge", "Pre-season staff training", "6/year; 200 stores × ~29 staff", "~5,800 staff training events/year", "HR Training Manager", "HR Training Mgr, Category Mgr, Store Managers",
     [("Category Manager provides product knowledge materials: new seasonal products, features, selling points, FAQs; HR Training distributes via e-learning platform and store meeting guides", "Category Mgr / HR Training Mgr", "CHRO", "1 week/season")]),
    ("Seasonal Launch Monitoring", "First 2 weeks of seasonal selling", "6/year; first 2 weeks of each season", "200 stores × 6 seasons", "Merchandising Planner", "Merch Planner, Category Mgr, Analytics Mgr",
     [("System monitors daily sell-through: compares vs. plan; identifies slow starters (may need markdown acceleration) and fast sellers (may need reorder); daily flash report to Category Manager", "System / Merch Planner", "Category Manager", "30 min/day during launch")]),
    ("Seasonal Vendor Coordination", "Pre-season vendor alignment", "6/year; ~50–100 seasonal vendors", "~50–100 vendors/season", "Buyer", "Buyer, Category Mgr, Vendor",
     [("Buyer confirms with vendors: delivery dates, quantities, quality standards, marketing support (co-op funds), markdown support (return/swap agreements for unsold seasonal inventory)", "Buyer", "Category Manager", "1–2 weeks/season")]),
    ("Multi-Season Inventory Transition Planning", "Transition between seasons", "6/year; overlap period ~2–3 weeks", "~2–3 week transition per season", "Merchandising Planner", "Merch Planner, Category Mgr, DC Ops, Store Ops",
     [("Planner manages transition: outgoing seasonal markdown (clear remaining), incoming seasonal setup (stage new display); coordinates display zone handover; adjusts replenishment from outgoing to incoming", "Merchandising Planner", "Category Manager", "1–2 weeks/transition")])
    ]),
    ("PA-64.2", "markdown-clearance-execution", "Markdown & Clearance Execution", [
    ("Sell-Through Based Markdown Trigger", "Seasonal SKU sell-through falls below plan threshold", "Continuous during season; ~200–300 markdown decisions/season", "~200–300 decisions/season", "Category Manager", "Category Mgr, Pricing Analyst, Merch Planner",
     [("System monitors sell-through vs. plan; auto-flags SKUs below threshold: <40% sold at mid-season, <70% at 75% of season; Pricing Analyst recommends markdown level based on residual inventory and weeks remaining", "System / Pricing Analyst", "Category Manager", "Automated + 30 min/decision"),
      ("Category Manager approves markdown; system updates price; POS reflects new price; shelf labels updated; customer communication if significant price reduction", "Category Manager / IT", "VP Merchandising", "1–2 hours")]),
    ("Progressive Markdown Strategy Execution", "Markdown schedule execution", "Per season; typically 3 markdown phases", "~3 phases × 200 stores × ~100 SKUs", "Merchandising Planner", "Merch Planner, Pricing Analyst, Store Ops",
     [("Phase 1 (mid-season): 10–15% off slow movers. Phase 2 (late season): 25–40% off remaining. Phase 3 (final 2 weeks): 50–75% off clearance. Planner defines phases; system executes per schedule", "Merchandising Planner", "Category Manager", "1 day/phase")]),
    ("Store-Level Clearance Event Execution", "End-of-season clearance event", "6/year; 200 stores", "~1,200 clearance events/year", "Store Manager", "Store Manager, Marketing, Merch Coord",
     [("Marketing promotes clearance event (social media, email, in-store signage); Store Manager sets up clearance zone; staff applies clearance labels; manages customer flow during event", "Marketing / Store Manager", "Regional Ops Mgr", "1–2 weeks")]),
    ("Clearance Inventory Consolidation", "Post-clearance remaining inventory", "Per season; after clearance event", "~5–15% of seasonal inventory unsold after clearance", "Merchandising Planner", "Merch Planner, DC Ops, Store Managers",
     [("Planner identifies remaining clearance inventory across stores; determines disposition: (a) transfer to stores still selling (regional variation), (b) consolidate at DC for bulk sale to discount buyers, (c) return to vendor per markdown agreement, (d) donate for tax benefit", "Merchandising Planner", "Category Manager", "1–2 weeks")]),
    ("Vendor Markdown Allowance Processing", "Vendor agreement includes markdown support", "Per season; ~50–100 seasonal vendors", "~50–100 vendors/season", "Finance Analyst", "Finance Analyst, Category Mgr, Vendor",
     [("Finance calculates vendor markdown allowance per agreement: unsold inventory × agreed support %; submits claim to vendor; vendor validates and credits; Finance records in AP", "Finance Analyst", "Finance Manager", "2–3 days/season")]),
    ("Clearance Pricing Compliance Audit", "During clearance event", "Per clearance event (6/year); 200 stores", "~1,200 compliance checks/year", "Merchandising Coordinator", "Merch Coord, Store Manager, Regional Ops",
     [("Coordinator verifies: clearance prices match system, clearance labels applied, clearance zone properly merchandised, non-clearance items not incorrectly discounted; non-compliance corrected immediately", "Merch Coordinator / Regional Ops Mgr", "Store Ops Director", "2–3 hours per event")]),
    ("Employee Purchase Program for Clearance", "Post-clearance employee discount event", "Per season; after public clearance", "6/year; ~6,715 employees eligible", "HR Manager", "HR Mgr, Store Ops, Finance",
     [("HR coordinates employee clearance event: additional 20–30% off remaining clearance for employees; store opens early or designates specific hours; system applies employee discount on clearance price", "HR Manager / Store Manager", "CHRO", "1 day/event")]),
    ("Clearance Financial Reconciliation", "Post-clearance financial analysis", "Per season; after clearance complete", "6/year", "Finance Manager", "Finance Mgr, Category Mgr, VP Merchandising",
     [("Finance reconciles: seasonal inventory cost, markdown cost, vendor allowance, clearance revenue, net margin on seasonal category; calculates seasonal category profitability vs. plan", "Finance Manager", "CFO", "2–3 days/season")])
    ]),
    ("PA-64.3", "post-season-analysis-learning", "Post-Season Analysis & Learning", [
    ("Post-Season Sales Performance Analysis", "Season complete; all clearance finalized", "6/year; 13 categories", "6 comprehensive analyses/year", "Analytics Manager", "Analytics Mgr, Category Mgr, VP Merchandising",
     [("Analyzes: seasonal sales vs. plan by category, SKU, store, region; sell-through rate; markdown rate; gross margin; identifies best and worst performing seasonal items", "Analytics Manager", "Category Manager", "3–5 days/season")]),
    ("Seasonal Forecast Accuracy Review", "Post-season", "6/year", "6 accuracy reviews/year", "Merchandising Planner", "Merch Planner, Analytics Mgr, Category Mgr",
     [("Compares: forecasted demand vs. actual sales per seasonal SKU; calculates forecast accuracy (MAPE); identifies systematic over/under-forecasting patterns; improves next season's forecast model", "Merchandising Planner / Analytics Manager", "VP Merchandising", "2–3 days/season")]),
    ("Vendor Seasonal Performance Review", "Post-season", "6/year; ~50–100 seasonal vendors", "~50–100 vendor reviews/season", "Buyer", "Buyer, Category Mgr, Quality Manager",
     [("Reviews vendor seasonal performance: on-time delivery, quality, sell-through of vendor's seasonal products, markdown support provided; feeds into vendor scorecard per VS-03", "Buyer / Category Manager", "VP Merchandising", "2–3 days/season")]),
    ("Customer Seasonal Purchase Behavior Analysis", "Post-season", "6/year", "600,000 loyalty members' seasonal purchase data", "CRM Manager", "CRM Mgr, Analytics Mgr, Category Mgr",
     [("Analyzes: customer segments buying seasonal products, average basket with seasonal items, repeat seasonal purchase rate, channel preference for seasonal shopping; informs next season targeting", "CRM Manager", "VP Marketing", "2–3 days/season")]),
    ("Seasonal Planogram Effectiveness Review", "Post-season", "6/year; 200 stores × seasonal zones", "~1,200 zone reviews/season", "Merchandising Planner", "Merch Planner, Analytics Mgr, Store Design Mgr",
     [("Reviews: seasonal display zone productivity (sales/sqm) vs. standard zone; customer traffic in seasonal zones; display conversion rate; recommends zone allocation adjustments for next season", "Merchandising Planner", "Category Manager", "2–3 days/season")]),
    ("Seasonal Markdown Strategy Effectiveness", "Post-season", "6/year", "All seasonal markdowns", "Pricing Analyst", "Pricing Analyst, Merch Planner, Finance",
     [("Evaluates: markdown timing (was earlier markdown better?), depth (which discount level cleared inventory fastest?), phase progression effectiveness; recommends strategy improvements for next season", "Pricing Analyst", "Category Manager", "2–3 days/season")]),
    ("Seasonal Category Profitability Report", "Post-season financial close", "6/year; 13 categories", "6 reports/year", "FP&A Analyst", "FP&A Analyst, Finance Mgr, Category Mgrs, VP Merch",
     [("Calculates: seasonal category P&L (revenue, COGS, markdowns, vendor allowances, net margin); compares vs. plan and vs. prior year same season; identifies most/least profitable seasonal categories", "FP&A Analyst", "CFO", "3–5 days/season")]),
    ("Seasonal Playbook Update", "Annual update after all seasons reviewed", "Annual", "Full seasonal playbook", "VP Merchandising", "VP Merch, Category Mgrs, Merch Planners, Buyers",
     [("VP Merchandising compiles learnings from all 6 seasons into updated seasonal playbook: forecast adjustments, assortment changes, vendor recommendations, markdown strategy refinements, display improvements; distributes to planning team for next year", "VP Merchandising", "COO", "5–10 days")])
    ])
])

# ═══ VS-65: E-Commerce Marketplace Integration ═══
grand += mk_vs("VS-65-ecommerce-marketplace-integration", 65,
    "E-Commerce Marketplace Integration", "Sell & Serve",
    "Manages BuildRight's presence on third-party Philippine e-commerce marketplaces (Lazada, Shopee, TikTok Shop, Zalora). Covers marketplace onboarding, catalog management, order and inventory synchronization, fulfillment coordination, and marketplace-specific financial reconciliation. Supplements BuildRight's own ecommerce platform (VS-10) with marketplace channels targeting ~5% of total ecommerce revenue.",
    [("PA-65.1", "marketplace-channel-onboarding", "Marketplace Channel Onboarding & Configuration", [
    ("Marketplace Platform Selection & Registration", "Strategic decision to add marketplace channel", "Ad-hoc; 1–2 new platforms/year", "1–2 platforms/year", "Ecommerce Director", "Ecommerce Dir, Legal, Finance, VP Marketing",
     [("Ecommerce Director evaluates marketplace: audience fit (home improvement/DIY buyers), commission structure (5–15%), logistics integration, competition, brand control; presents recommendation to VP Marketing", "Ecommerce Director", "VP Marketing", "5–10 days"),
      ("Legal reviews marketplace seller agreement: terms, IP protection, dispute resolution, data sharing; Finance sets up financial controls; IT begins integration planning", "Legal / Finance / IT", "Ecommerce Director", "5–10 days")]),
    ("Marketplace Store Setup & Branding", "Marketplace platform approved; store setup begins", "Per platform (~1–2/year)", "~1–2 setups/year", "Digital Marketing Manager", "Digital Marketing Mgr, Ecommerce Dir, Brand Manager",
     [("Digital Marketing creates marketplace storefront: BuildRight branding, banner images, product categories, store policies, customer service info, shipping options; launches store in compliance with marketplace guidelines", "Digital Marketing Manager", "Ecommerce Director", "5–10 days")]),
    ("Marketplace Catalog & Pricing Configuration", "Store setup complete; catalog upload", "Initial setup + ongoing catalog updates", "~5,000–10,000 SKUs per marketplace", "Ecommerce Catalog Manager", "Catalog Mgr, Pricing Analyst, IT Integration",
     [("Catalog Manager selects SKUs for marketplace: excludes consignment, heavy/bulky items (unless marketplace supports), low-margin items; creates marketplace-specific listings with optimized titles, descriptions, images", "Catalog Manager", "Ecommerce Director", "5–10 days initial"),
      ("Pricing Analyst sets marketplace prices: BuildRight price + marketplace commission adjustment; competitive pricing vs. marketplace competitors; configures shipping fee structure", "Pricing Analyst", "Ecommerce Director", "2–3 days")]),
    ("Marketplace API Integration", "Catalog and pricing configured; integration begins", "Per platform (~1–2/year)", "~1–2 integrations/year", "IT Integration Lead", "IT Integration Lead, Ecommerce Dir, Marketplace Tech Team",
     [("IT configures API integration: product catalog sync, inventory sync, order download, shipment update push, price sync, return status sync; tests in sandbox; certifies with marketplace", "IT Integration Lead", "CIO", "10–15 days"),
      ("Monitors integration health: sync latency, error rate, data accuracy; addresses issues within marketplace SLA (typically 24 hours)", "IT Integration Lead", "Ecommerce Director", "Ongoing")]),
    ("Marketplace Promotional Campaign Setup", "Marketplace mega-sale event (e.g., 11.11, 12.12)", "6–8 mega-sale events/year per marketplace", "6–8 events × platforms", "Digital Marketing Manager", "Digital Marketing Mgr, Pricing Analyst, Ecommerce Dir",
     [("Digital Marketing plans marketplace campaign: selects products for flash deals, sets discount levels, allocates co-op marketing budget; configures in marketplace seller center", "Digital Marketing Manager", "VP Marketing", "3–5 days/event"),
      ("Monitors campaign performance in real-time: sales velocity, conversion rate, customer reviews; adjusts pricing and inventory allocation as needed during event", "Digital Marketing Manager", "Ecommerce Director", "1–3 days per event")]),
    ("Marketplace Customer Service Setup", "Store launch; CS channel activation", "Per platform; ongoing", "1–2 platforms", "Customer Service Supervisor", "CS Supervisor, Marketplace CS Tools, Ecommerce Dir",
     [("Configures marketplace chat tools: auto-replies for common queries (shipping, returns, product specs); trains CS agents on marketplace-specific policies and procedures", "CS Supervisor", "CS Director", "3–5 days/platform")]),
    ("Marketplace Inventory Allocation Strategy", "Store live with orders flowing", "Monthly review; weekly adjustments", "~5,000–10,000 SKUs per marketplace", "Merchandising Planner", "Merch Planner, Ecommerce Dir, Inventory Mgr",
     [("Merch Planner determines inventory allocation: how much stock reserved for marketplace vs. own ecommerce vs. stores; prevents stock-outs across channels; adjusts weekly based on sell-through", "Merchandising Planner", "Ecommerce Director", "2–3 hours/week")]),
    ("Marketplace Channel Performance Baseline", "First 3 months of marketplace operation", "First 3 months per platform", "1–2 platforms", "Ecommerce Director", "Ecommerce Dir, Analytics Mgr, Finance Analyst",
     [("Ecommerce Director establishes performance baseline: daily orders, AOV, conversion rate, customer acquisition cost, return rate, marketplace fees, net margin; compares to own ecommerce platform", "Ecommerce Director", "VP Marketing", "5–10 days")])
    ]),
    ("PA-65.2", "marketplace-order-inventory-sync", "Marketplace Order & Inventory Sync", [
    ("Marketplace Order Download & Processing", "Continuous order sync from marketplace", "Continuous; ~5,000–10,000 marketplace orders/month", "~5K–10K/month across platforms", "Order Management System", "OMS, Ecommerce Ops, DC Ops, Logistics",
     [("System downloads marketplace orders via API; converts to BuildRight fulfillment orders; reserves inventory; routes to fulfillment source (DC, store, vendor) per VS-60 routing logic", "System", "Ecommerce Operations Manager", "Automated")]),
    ("Marketplace Inventory Synchronization", "Real-time inventory sync", "Continuous; every 15 minutes", "~35,000 SKUs × 1–2 platforms", "IT Integration Lead", "IT Integration, Inventory Mgr, Ecommerce Ops",
     [("System pushes inventory availability to marketplace every 15 minutes: BuildRight available quantity minus marketplace allocation; prevents overselling; handles sync errors and reconciles discrepancies", "System / IT Integration Lead", "Inventory Manager", "Automated + 2–3 hours/week")]),
    ("Marketplace Fulfillment & Shipping", "Marketplace order requires fulfillment", "~5,000–10,000 orders/month", "~5K–10K/month", "Ecommerce Operations Manager", "Ecom Ops Mgr, DC Ops, Marketplace Logistics",
     [("Fulfillment: (a) marketplace-managed logistics (FBS/LazMall) — system generates marketplace shipping label; (b) seller-managed — system routes per VS-60 to optimal source", "System / Ecom Ops Manager", "VP Supply Chain", "Varies"),
      ("DC/store picks, packs, ships; system pushes tracking number to marketplace; customer tracks via marketplace app; delivery confirmation auto-updates order status", "DC Ops / System", "Ecom Ops Manager", "1–5 days")]),
    ("Marketplace Return & Refund Processing", "Marketplace return initiated by customer", "~5–8% return rate; ~300–800 returns/month", "~300–800/month", "Customer Service Agent", "CSA, Returns Mgr, Marketplace Portal",
     [("Customer initiates return via marketplace; system receives return notification; CSA reviews and approves/contests; customer ships item back; system processes refund upon receipt", "CSA / System", "Returns Manager", "5–10 min + 3–7 days")]),
    ("Marketplace Pricing Sync & Competitor Monitoring", "Daily price sync; continuous monitoring", "Daily; ~5,000–10,000 SKUs per platform", "~5K–10K SKUs", "Pricing Analyst", "Pricing Analyst, Ecommerce Dir, IT",
     [("System syncs BuildRight prices to marketplace (adjusted for commission); Analyst monitors competitor pricing on marketplace; recommends price adjustments for competitive positioning", "System / Pricing Analyst", "Ecommerce Director", "1–2 hours/day")]),
    ("Marketplace Listing Quality Management", "Monthly listing audit", "Monthly; ~5,000–10,000 listings per platform", "~5K–10K listings", "Ecommerce Catalog Manager", "Catalog Mgr, Digital Marketing, Analytics Mgr",
     [("Catalog Manager audits listings: image quality, title optimization, description accuracy, keyword relevance, customer review response; updates underperforming listings for better search ranking", "Catalog Manager", "Ecommerce Director", "4–6 hours/month")]),
    ("Marketplace Stock-Out Prevention", "Real-time monitoring", "Continuous", "~35,000 SKUs across platforms", "Merchandising Planner", "Merch Planner, Inventory Mgr, Ecom Ops",
     [("System monitors sell-through by SKU; flags SKUs approaching stock-out on marketplace; Planner adjusts allocation or generates replenishment order; delists SKUs when stock-out to prevent order cancellation", "System / Merchandising Planner", "Ecommerce Director", "Ongoing")]),
    ("Marketplace Customer Review Management", "Customer posts review on marketplace", "Continuous; ~2,000–3,000 reviews/month", "~2K–3K/month", "Customer Service Agent", "CSA, Digital Marketing, Category Mgr",
     [("CSA monitors and responds to marketplace reviews: thanks positive, addresses negative with resolution offer; escalates product quality issues to Category Manager; Digital Marketing incorporates feedback into listing optimization", "CSA / Digital Marketing", "CS Director", "2–3 hours/day")])
    ]),
    ("PA-65.3", "marketplace-performance-settlement", "Marketplace Performance & Settlement", [
    ("Marketplace Financial Reconciliation", "Monthly settlement cycle", "Monthly; 1–2 platforms", "~1–2 reconciliations/month", "Finance Analyst", "Finance Analyst, Ecommerce Dir, Treasury",
     [("Analyst reconciles: marketplace settlement report vs. BuildRight order records; verifies: gross sales, marketplace commission, shipping fee deductions, promotional subsidies, refunds, net settlement", "Finance Analyst", "Finance Manager", "4–6 hours/month"),
      ("Disputes discrepancies with marketplace (missing orders, incorrect commissions, unauthorized refunds); resolves within marketplace dispute window (typically 30 days)", "Finance Analyst", "Ecommerce Director", "2–3 hours/month")]),
    ("Marketplace Commission & Fee Analysis", "Monthly cost analysis", "Monthly; 1–2 platforms", "~1–2 analyses/month", "Finance Analyst", "Finance Analyst, Ecommerce Dir, VP Marketing",
     [("Calculates: effective commission rate, shipping cost subsidy, promotional cost, return processing fees, total marketplace cost as % of marketplace revenue; compares vs. own ecommerce cost-to-serve", "Finance Analyst", "Finance Manager", "2–3 hours/month")]),
    ("Marketplace Channel P&L", "Monthly P&L reporting", "Monthly; 1–2 platforms", "~1–2 P&Ls/month", "FP&A Analyst", "FP&A Analyst, Ecommerce Dir, Finance Dir",
     [("Calculates: marketplace revenue, COGS, commissions, shipping, marketing, returns, net contribution; compares vs. own ecommerce and in-store channel P&L; recommends channel investment", "FP&A Analyst", "CFO", "4–6 hours/month")]),
    ("Marketplace Performance Dashboard", "Daily monitoring; monthly deep analysis", "Daily; 1–2 platforms", "~5K–10K orders/month", "Ecommerce Director", "Ecommerce Dir, Analytics Mgr, VP Marketing",
     [("Dashboard: orders, revenue, AOV, conversion rate, top SKUs, customer ratings, return rate, stock-out rate; daily review for anomalies; monthly deep analysis with optimization recommendations", "System / Ecommerce Director", "VP Marketing", "30 min/day + 4–6 hours/month")]),
    ("Marketplace vs. Own Ecommerce Channel Comparison", "Monthly comparison", "Monthly", "2–3 channels (Lazada, Shopee, own site)", "Analytics Manager", "Analytics Mgr, Ecommerce Dir, VP Marketing",
     [("Compares: revenue, margin, customer acquisition cost, AOV, conversion rate, return rate by channel; identifies which products/categories perform better on marketplace vs. own site; recommends channel-specific assortment", "Analytics Manager", "VP Marketing", "4–6 hours/month")]),
    ("Marketplace Customer Acquisition Analysis", "Quarterly analysis", "Quarterly", "Marketplace customer base", "CRM Manager", "CRM Mgr, Analytics Mgr, Ecommerce Dir",
     [("Analyzes: new customers acquired via marketplace, conversion to BuildRight loyalty program, repeat purchase on marketplace vs. migration to own site, lifetime value comparison", "CRM Manager", "VP Marketing", "2–3 days/quarter")]),
    ("Marketplace Platform Relationship Management", "Quarterly business review with marketplace", "Quarterly; 1–2 platforms", "1–2 platform reviews/quarter", "Ecommerce Director", "Ecommerce Dir, VP Marketing, Marketplace Account Manager",
     [("Ecommerce Director conducts QBR with marketplace: reviews performance, discusses growth opportunities, negotiates commission rates, explores featured placement, addresses platform issues", "Ecommerce Director", "VP Marketing", "2–3 hours/quarter")]),
    ("Marketplace Strategy Annual Review", "Annual strategic review", "Annual; all marketplace channels", "1–2 marketplace channels", "VP Marketing", "VP Marketing, Ecommerce Dir, CFO, COO",
     [("VP Marketing reviews marketplace strategy: channel contribution, profitability, growth trajectory, competitive landscape; recommends: expand, maintain, or sunset each marketplace channel; presents to Executive Committee", "VP Marketing / Ecommerce Director", "CEO", "3–5 days")])
    ])
])

# ═══ VS-66: Customer Project & Design Services ═══
grand += mk_vs("VS-66-customer-project-design-services", 66,
    "Customer Project & Design Services", "Sell & Serve",
    "Manages BuildRight's in-home measurement, design consultation, and project management services for customers undertaking renovation and construction projects. Covers kitchen/bathroom design, material estimation, project quotation, execution tracking, and completion verification. Targets the Professional/Trade (B2B) and walk-in retail (B2C) customer segments undertaking projects worth PHP 50K–5M.",
    [("PA-66.1", "in-home-measurement-design", "In-Home Measurement & Design Consultation", [
    ("Customer Project Inquiry & Qualification", "Customer inquires about project services in-store or online", "~2,000–3,000 project inquiries/month", "~2K–3K/month; ~30% qualify for design consultation", "Sales Associate / Project Consultant", "Sales Associate, Project Consultant, Customer",
     [("Sales Associate qualifies inquiry: project type (kitchen, bathroom, whole house), budget range, timeline, property location; if project >PHP 50K, refers to Project Consultant for design consultation", "Sales Associate", "Project Consultant", "15–30 min"),
      ("Project Consultant schedules in-home measurement visit: confirms date, prepares measurement tools and product samples; provides customer with project intake form", "Project Consultant", "Customer", "10–15 min")]),
    ("In-Home Measurement Visit", "Scheduled measurement appointment", "~600–900 visits/month", "~600–900/month; avg 2–3 hours per visit", "Project Consultant", "Project Consultant, Customer",
     [("Project Consultant visits customer's home: measures rooms, documents existing layout, photographs space, discusses customer's vision and requirements, presents material samples", "Project Consultant", "Customer", "2–3 hours"),
      ("Consultant creates rough sketch with dimensions; identifies potential challenges (plumbing relocation, structural issues); discusses budget alignment; promises design proposal within 5 business days", "Project Consultant", "Customer", "30 min")]),
    ("Kitchen & Bathroom Design Proposal", "Measurement complete; design work begins", "~600–900 designs/month", "~600–900/month", "Design Consultant", "Design Consultant, Project Consultant, Customer",
     [("Design Consultant creates layout design using design software: 2D/3D floor plan with material specifications, fixture placement, color scheme; generates material list with quantities", "Design Consultant", "Project Consultant", "4–8 hours"),
      ("Design package presented to customer: design boards, material samples, 3D rendering, itemized material list, estimated project cost; Customer approves, requests modifications, or declines", "Design Consultant / Project Consultant", "Customer", "1–2 hours")]),
    ("Material Estimation & Specification", "Design approved; detailed material take-off", "~400–600 material estimates/month", "~400–600/month", "Project Consultant", "Project Consultant, Category Mgr, Merch Planner",
     [("Project Consultant performs detailed material take-off from approved design: tile sqm, paint liters, lumber board feet, pipe meters, wire meters, fixture counts, accessory quantities", "Project Consultant", "Design Consultant", "2–4 hours"),
      ("System validates quantities against standard waste factors; checks inventory availability at nearest store/DC; identifies lead-time items (special order, import); generates material specification sheet", "System / Project Consultant", "Category Manager", "1–2 hours")]),
    ("Project Quotation & Pricing", "Material specification complete; pricing required", "~400–600 quotes/month", "~400–600/month", "Project Consultant", "Project Consultant, Pricing Analyst, Finance",
     [("Project Consultant prices all materials at trade/project price per VS-11; includes delivery, installation (if BuildRight-managed), waste allowance; generates comprehensive project quotation", "Project Consultant", "Category Manager", "2–4 hours"),
      ("Finance reviews project margin: material cost vs. project price; ensures minimum margin threshold met; approves or requests pricing adjustment; quotation valid for 30 days", "Finance", "Project Consultant", "1–2 hours")]),
    ("Design Revision & Customer Approval", "Customer requests design or quotation changes", "~200–300 revisions/month (~50% of proposals)", "~200–300/month", "Design Consultant / Project Consultant", "Design Consultant, Project Consultant, Customer",
     [("Customer requests changes: material substitution, layout adjustment, budget reduction; Design Consultant revises design; Project Consultant updates material list and quotation", "Design Consultant / Project Consultant", "Customer", "2–4 hours per revision"),
      ("Customer approves final design and quotation; generates sales order; deposit collected (30–50% of project value); project enters execution phase", "Project Consultant / Cashier", "Customer", "30 min")]),
    ("Design Consultant Training & Certification", "Quarterly training; new product certification", "Quarterly + new product launches", "~10–15 Design Consultants", "HR Training Manager", "HR Training Mgr, Category Mgr, Design Consultant",
     [("Category Manager provides product training: new materials, installation techniques, design trends; HR Training certifies consultants on design software and measurement accuracy", "Category Manager / HR Training Mgr", "VP Merchandising", "1–2 days/quarter")]),
    ("Design Software & Tool Management", "Software update or tool maintenance", "Monthly maintenance; quarterly updates", "~10–15 design workstations", "IT System Admin", "IT System Admin, Design Consultants, Software Vendor",
     [("IT maintains design software licenses, updates product catalog in design tool, ensures measurement tool calibration, manages 3D rendering workstation performance", "IT System Admin", "CIO", "4–6 hours/month")])
    ]),
    ("PA-66.2", "project-quotation-material-estimation", "Project Quotation & Material Management", [
    ("Project Sales Order Processing", "Customer approves quotation", "~300–450 project orders/month", "~300–450/month; avg project value PHP 200K–1M", "Project Consultant", "Project Consultant, Store Manager, Finance",
     [("Project Consultant converts approved quotation to sales order: links all materials to SKUs, confirms pricing, sets delivery schedule, allocates inventory from store/DC; deposit verified", "Project Consultant", "Store Manager", "1–2 hours"),
      ("Finance validates deposit payment; system reserves inventory; generates pick lists for store/DC; project entered into project tracking system with milestones", "Finance / System", "Project Consultant", "30 min")]),
    ("Project Material Procurement", "Project requires materials not in stock", "~100–150 procurement requests/month", "~100–150/month", "Buyer", "Buyer, Project Consultant, Vendor",
     [("Project Consultant identifies non-stock items; Buyer places special order with vendor; system creates PO linked to project; tracks delivery to store/DC; coordinates with project schedule", "Project Consultant / Buyer", "Category Manager", "2–3 days lead time")]),
    ("Project Delivery Coordination", "Materials ready; schedule delivery to customer site", "~300–450 deliveries/month", "~300–450/month; often multi-drop", "Logistics Coordinator", "Logistics Coord, 3PL Partner, Project Consultant, Customer",
     [("Coordinator schedules delivery: coordinates with 3PL per VS-56 for bulky materials (tiles, lumber, cement); ensures customer or representative on-site for receipt; confirms delivery window", "Logistics Coordinator", "Project Consultant", "1–2 days"),
      ("3PL delivers; customer verifies quantity and condition; system updates goods delivered status; discrepancies reported and resolved within 48 hours", "3PL / Customer / System", "Logistics Coordinator", "1 day delivery")]),
    ("Project Installation Coordination", "Customer opts for BuildRight-managed installation", "~150–225 installations/month (~50% of projects)", "~150–225/month", "Installation Coordinator", "Installation Coord, Contractor, Project Consultant, Customer",
     [("Installation Coordinator assigns licensed contractor from BuildRight's installer network (VS-12); provides project specifications; schedules installation dates; contractor confirms", "Installation Coordinator", "Project Consultant", "1–2 days"),
      ("Contractor performs installation; Project Consultant conducts quality check at key milestones; customer signs milestone completions; contractor paid upon completion", "Contractor / Project Consultant", "Customer", "3–30 days per project")]),
    ("Project Change Order Management", "Customer requests change during execution", "~100–150 change orders/month (~30% of projects)", "~100–150/month", "Project Consultant", "Project Consultant, Customer, Finance",
     [("Customer requests change: additional materials, design modification, scope change; Project Consultant evaluates impact on cost and timeline; prepares change order quotation", "Project Consultant", "Customer", "1–2 hours"),
      ("Customer approves change order; Finance adjusts project value and payment schedule; system updates material requirements; additional materials procured and delivered", "Project Consultant / Finance", "Store Manager", "1–3 days")]),
    ("Project Payment Collection & Milestone Billing", "Project milestone completed; payment due", "~600–900 milestone payments/month (2–3 per project)", "~600–900/month", "Finance Analyst", "Finance Analyst, Project Consultant, Customer",
     [("System generates milestone invoice upon milestone completion sign-off; Project Consultant collects payment; Finance tracks project payment status: deposit, progress payments, final payment", "System / Project Consultant / Finance Analyst", "Finance Manager", "30 min per milestone")]),
    ("Project Warranty Handover", "Project completed; warranty documentation", "~300–450 project completions/month", "~300–450/month", "Project Consultant", "Project Consultant, Customer, CRM",
     [("Project Consultant compiles warranty package: all installed products with individual warranty registration, installation warranty (1 year workmanship), care and maintenance guide", "Project Consultant", "Customer", "1–2 hours"),
      ("System registers all product warranties in CRM per VS-53; project record linked to customer profile for future reference and follow-up; customer satisfaction survey sent", "System / Project Consultant", "CRM Manager", "Automated + 30 min")]),
    ("Project Material Returns & Surplus Handling", "Project complete; surplus materials to return", "~200–300 surplus return requests/month", "~200–300/month", "Store Receiving Clerk", "Receiving Clerk, Project Consultant, Finance",
     [("Customer returns unused materials in saleable condition; Receiving Clerk inspects and processes return; system credits customer account or issues refund; material restocked", "Receiving Clerk / System", "Store Manager", "15–30 min per return"),
      ("Finance adjusts project final cost for returned materials; damaged/unsaleable returns processed per vendor return policy", "Finance", "Finance Manager", "Automated")])
    ]),
    ("PA-66.3", "project-tracking-completion", "Project Tracking & Completion", [
    ("Project Dashboard & Status Tracking", "Continuous project monitoring", "Continuous; ~300–450 active projects", "~300–450 active projects/month", "Project Consultant", "Project Consultant, Store Manager, VP Sales",
     [("System maintains project dashboard: status (design/procurement/delivery/installation/completion), milestones, payment status, open issues; Consultant updates daily", "System / Project Consultant", "VP Sales", "30 min/day")]),
    ("Project Timeline Management", "Project execution in progress", "Per project; avg 2–8 weeks", "~300–450 projects in execution", "Project Consultant", "Project Consultant, Contractor, Logistics, Customer",
     [("Project Consultant tracks timeline vs. plan: material delivery dates, installation start/end, milestone completions; identifies delays; adjusts schedule; communicates to customer", "Project Consultant", "Customer", "30 min/day per active project")]),
    ("Project Quality Inspection", "Key milestones during installation", "Per project; 2–3 inspections per project", "~600–1,350 inspections/month", "Project Consultant", "Project Consultant, Contractor, Customer",
     [("Consultant inspects at key milestones: material delivery (quality/quantity), installation start (layout accuracy), mid-installation (workmanship), completion (punch list)", "Project Consultant", "VP Sales", "1–2 hours per inspection")]),
    ("Project Completion & Punch List", "Installation complete; final walkthrough", "~300–450 completions/month", "~300–450/month", "Project Consultant", "Project Consultant, Contractor, Customer",
     [("Consultant conducts final walkthrough with customer: verifies all work per design, identifies punch list items (minor fixes), documents completion with photos; customer signs acceptance", "Project Consultant", "Customer", "1–2 hours"),
      ("Punch list items resolved within 7 days; contractor returns for fixes; Consultant verifies; final payment collected; project closed in system", "Contractor / Project Consultant", "VP Sales", "7 days")]),
    ("Post-Project Customer Follow-Up", "30 days post-completion", "Monthly; ~300–450 follow-ups/month", "~300–450/month", "Customer Service Agent", "CSA, Project Consultant, Customer",
     [("CSA contacts customer 30 days post-completion: satisfaction check, any issues or warranty needs, referral request (recommend BuildRight to friends/family); logs feedback in CRM", "CSA", "CS Director", "10–15 min per follow-up")]),
    ("Project Revenue & Margin Analysis", "Monthly financial analysis", "Monthly; ~300–450 completed projects", "~300–450 projects/month", "FP&A Analyst", "FP&A Analyst, Project Consultants, Finance Dir",
     [("FP&A analyzes: project revenue, material cost, installation cost, delivery cost, net margin by project type and value range; identifies most profitable project types and improvement areas", "FP&A Analyst", "CFO", "4–6 hours/month")]),
    ("Project Consultant Performance Scorecard", "Monthly performance review", "Monthly; ~10–15 Project Consultants", "~10–15 scorecards/month", "VP Sales", "VP Sales, Project Consultants, HR",
     [("Scorecard: projects completed, revenue generated, margin achieved, customer satisfaction score, change order rate, on-time completion rate; used for performance review and incentive calculation", "VP Sales", "COO", "2–3 hours/month")]),
    ("Project Services Annual Strategy Review", "Annual strategic review", "Annual", "Full project services program", "VP Sales / VP Merchandising", "VP Sales, VP Merch, CFO, COO",
     [("Reviews: program revenue, margin, customer satisfaction, market opportunity, competitive positioning, service expansion opportunities; recommends: new service categories, pricing adjustments, contractor network expansion", "VP Sales / VP Merchandising", "CEO", "3–5 days")])
    ])
])

# ═══ VS-67: Vendor Scorecard & Performance Analytics ═══
grand += mk_vs("VS-67-vendor-scorecard-analytics", 67,
    "Vendor Scorecard & Performance Analytics", "Plan & Source",
    "Manages comprehensive vendor performance measurement, scoring, and improvement programs for BuildRight's ~800–1,000 active vendors. Covers KPI definition and data collection, periodic performance reviews and ratings, and vendor development and improvement programs. Integrates with vendor management (VS-03), quality management (VS-31), procurement (VS-15), and supply planning (VS-02).",
    [("PA-67.1", "vendor-kpi-data-collection", "Vendor KPI Definition & Data Collection", [
    ("Vendor KPI Framework Management", "Annual KPI review or new vendor category", "Annual review; continuous monitoring", "~20 KPIs tracked for ~800–1,000 vendors", "Procurement Manager", "Procurement Mgr, Category Mgrs, VP Supply Chain",
     [("Procurement Manager maintains KPI framework: (a) on-time delivery rate (target ≥95%), (b) order fill rate (target ≥98%), (c) quality rejection rate (target <2%), (d) invoice accuracy (target ≥99%), (e) responsiveness (target <48 hours), (f) price competitiveness, (g) innovation contribution", "Procurement Manager", "VP Supply Chain", "2–3 days/year + 2–3 hours/month"),
      ("Reviews KPI weights by vendor category: import vs. local, strategic vs. tactical, merchandise vs. non-merchandise; adjusts to reflect current business priorities", "Procurement Manager", "VP Supply Chain", "1–2 days/year")]),
    ("Automated Vendor Data Collection", "Continuous transaction processing", "Continuous; ~1,200 POs and ~6,715 invoices/month", "~800–1,000 vendors with transaction data", "System / Data Quality Analyst", "System, Data Quality Analyst, Procurement",
     [("System auto-collects vendor data from transactions: PO delivery vs. promised date (on-time), PO quantity vs. delivered quantity (fill rate), GR quality flags (rejection rate), invoice matching accuracy, response time to RFQ/orders", "System", "Data Quality Analyst", "Automated")]),
    ("Vendor Quality Data Aggregation", "Monthly quality data compilation", "Monthly; from VS-31 quality inspection results", "~2,400 quality inspections/month feeding vendor scores", "Quality Manager", "Quality Mgr, Procurement Mgr, DC Quality Inspectors",
     [("Quality Manager aggregates quality data per vendor: pass rate, defect types, complaint rate, recall incidents; feeds into vendor scorecard quality dimension; flags vendors with declining quality trends", "Quality Manager", "VP Supply Chain", "4–6 hours/month")]),
    ("Vendor Survey & Qualitative Assessment", "Annual vendor relationship survey", "Annual; ~100 strategic vendors surveyed", "~100 vendors", "Procurement Manager", "Procurement Mgr, Category Mgrs, Buyers",
     [("Procurement conducts internal survey: Category Managers and Buyers rate strategic vendors on communication, flexibility, problem resolution, innovation, strategic alignment; qualitative scores supplement transactional KPIs", "Procurement Manager / Category Managers", "VP Supply Chain", "5–10 days/year")]),
    ("Vendor Score Calculation & Weighting", "Monthly score calculation cycle", "Monthly; ~800–1,000 vendors scored", "~800–1,000 scores/month", "System / Procurement Analyst", "System, Procurement Analyst, Procurement Mgr",
     [("System calculates composite score per vendor: weighted average of all KPI dimensions (quality 30%, delivery 25%, cost 20%, responsiveness 15%, innovation 10%); generates monthly vendor ranking", "System", "Procurement Analyst", "Automated"),
      ("Procurement Analyst reviews scores: validates data accuracy, investigates anomalous scores, adjusts for exceptional circumstances (force majeure, seasonal spikes); publishes monthly vendor scorecard", "Procurement Analyst", "Procurement Manager", "4–6 hours/month")]),
    ("Vendor Scorecard Data Quality Audit", "Quarterly data quality audit", "Quarterly; ~200 vendor scorecards spot-checked", "~200 spot-checks/quarter", "Data Quality Analyst", "Data Quality Analyst, Procurement Analyst",
     [("Audits: validates scorecard data sources, checks for missing data periods, verifies calculation accuracy, identifies data gaps; ensures scorecard integrity for vendor management decisions", "Data Quality Analyst", "Procurement Manager", "4–6 hours/quarter")]),
    ("New Vendor Baseline Performance Establishment", "New vendor onboarded; first 6 months", "~5–10 new vendors/month", "~5–10/month", "Buyer", "Buyer, Procurement Mgr, Quality Mgr",
     [("First 6 months: enhanced monitoring on all KPIs; establishes baseline performance; weekly review instead of monthly; any KPI below threshold triggers immediate corrective discussion", "Buyer / Procurement Mgr", "VP Supply Chain", "1–2 hours/week per new vendor")]),
    ("Vendor KPI Benchmarking & Industry Comparison", "Annual benchmarking exercise", "Annual; top 50 strategic vendors", "~50 vendors benchmarked/year", "Procurement Manager", "Procurement Mgr, Category Mgrs, VP Supply Chain",
     [("Benchmarks vendor KPIs vs. industry standards and peer retailer vendor scores; identifies below-industry performers; shares benchmark data (anonymized) with vendors during performance reviews", "Procurement Manager", "VP Supply Chain", "3–5 days/year")])
    ]),
    ("PA-67.2", "vendor-performance-review-rating", "Vendor Performance Review & Rating", [
    ("Monthly Vendor Performance Report", "Monthly reporting cycle", "Monthly; ~800–1,000 vendors", "~800–1,000 vendor performance reports/month", "Procurement Analyst", "Procurement Analyst, Procurement Mgr, VP Supply Chain",
     [("Generates monthly report: top 20 performers, bottom 20 performers, biggest movers (up/down), new additions, KPI trends; distributes to Category Managers and Buyers for action", "Procurement Analyst", "Procurement Manager", "4–6 hours/month")]),
    ("Quarterly Strategic Vendor Review", "Quarterly review cycle", "Quarterly; top 50 strategic vendors", "~50 vendor reviews/quarter", "Category Manager", "Category Mgr, Procurement Mgr, Vendor, VP Supply Chain",
     [("Category Manager conducts structured review with strategic vendor: presents scorecard, discusses strengths and improvement areas, sets 90-day improvement targets; vendor presents their roadmap", "Category Manager / Vendor", "VP Supply Chain", "1–2 hours/vendor/quarter")]),
    ("Annual Vendor Tier Classification", "Annual classification review", "Annual; ~800–1,000 vendors classified", "~800–1,000 classifications/year", "VP Supply Chain", "VP Supply Chain, Procurement Mgr, Category Mgrs, CFO",
     [("VP Supply Chain classifies vendors into tiers: (a) Strategic/Platinum — top 20 vendors (45% of COGS), (b) Preferred/Gold — next 50, (c) Approved/Silver — standard, (d) Probation/Bronze — underperforming, (e) Watch/At-Risk — potential for delisting", "VP Supply Chain", "CFO", "5–10 days/year"),
      ("Tier determines: PO allocation priority, payment terms, co-op marketing budget, strategic collaboration level, vendor development investment", "VP Supply Chain / CFO", "CEO", "1–2 days")]),
    ("Vendor Performance Improvement Plan (PIP)", "Vendor falls below performance threshold", "~20–30 PIPs/year", "~20–30/year", "Procurement Manager", "Procurement Mgr, Category Mgr, Vendor, VP Supply Chain",
     [("Procurement Manager issues PIP to underperforming vendor: specific KPIs below threshold, required improvement levels, timeline (typically 90 days), consequences if not met (volume reduction or delisting)", "Procurement Manager", "VP Supply Chain", "2–3 hours per PIP"),
      ("Monthly check-ins during PIP; vendor reports corrective actions; Procurement validates improvement; if met → graduate from PIP; if not → escalate to delisting review", "Procurement Manager / Vendor", "VP Supply Chain", "1 hour/month per PIP")]),
    ("Vendor Delisting Decision & Execution", "Vendor consistently underperforms despite PIP", "~5–10 delistings/year", "~5–10/year", "VP Supply Chain", "VP Supply Chain, Category Mgr, Procurement, Finance, Legal",
     [("VP Supply Chain initiates delisting: documents performance history, PIP results, business impact; identifies alternative vendor(s); presents recommendation to Category Manager and CFO", "VP Supply Chain", "CFO", "3–5 days per delisting"),
      ("Category Manager approves alternative sourcing; Procurement transitions volume; Finance settles final payments; Legal reviews contractual obligations; vendor portal access revoked", "Category Mgr / Procurement / Finance / Legal", "VP Supply Chain", "30–60 days")]),
    ("Vendor Recognition & Award Program", "Annual vendor awards", "Annual; top performers recognized", "10–15 vendors recognized/year", "VP Supply Chain", "VP Supply Chain, Procurement Mgr, Category Mgrs, CEO",
     [("VP Supply Chain identifies award recipients: Vendor of the Year (overall score), Quality Excellence, Delivery Reliability, Innovation Partner, Sustainability Champion; coordinates recognition event", "VP Supply Chain", "CEO", "3–5 days/year"),
      ("Awards communicate: increased PO allocation, preferred terms, co-marketing opportunities, strategic partnership discussions; reinforces performance culture", "VP Supply Chain / Procurement Mgr", "Category Mgr", "1 day")]),
    ("Vendor Scorecard System Enhancement", "Quarterly system review", "Quarterly; continuous improvement", "Scorecard system serving ~800–1,000 vendors", "IT Business Analyst", "IT Business Analyst, Procurement Mgr, VP Supply Chain",
     [("IT reviews scorecard system: reporting capabilities, data visualization, integration completeness, user feedback; implements enhancements: new KPIs, better dashboards, mobile access for buyers", "IT Business Analyst", "CIO", "5–10 days/quarter")]),
    ("Cross-Functional Vendor Feedback Integration", "Quarterly cross-functional input", "Quarterly; 5 functions (Procurement, Quality, Finance, Store Ops, Merchandising)", "5 functional inputs/quarter", "Procurement Manager", "Procurement Mgr, Quality Mgr, Finance Mgr, Store Ops Dir, Category Mgrs",
     [("Procurement collects cross-functional feedback: Quality (inspection results), Finance (invoice disputes, payment terms compliance), Store Ops (delivery quality), Merchandising (product quality, trend responsiveness); integrates into composite score", "Procurement Manager", "VP Supply Chain", "4–6 hours/quarter")])
    ]),
    ("PA-67.3", "vendor-development-improvement", "Vendor Development & Improvement Programs", [
    ("Vendor Capability Assessment", "Vendor development need identified", "~20–30 assessments/year", "~20–30/year", "Procurement Manager", "Procurement Mgr, Quality Mgr, Category Mgr, VP Supply Chain",
     [("Procurement conducts capability assessment: production capacity, quality systems, logistics capability, technology readiness, financial stability, sustainability practices; identifies development areas", "Procurement Manager / Quality Manager", "VP Supply Chain", "2–3 days per assessment")]),
    ("Vendor Training & Development Program", "Capability gap identified; training designed", "~10–15 vendor training events/year", "~10–15 events/year", "Procurement Manager", "Procurement Mgr, Quality Mgr, IT, Vendor",
     [("Designs training: quality standards, packaging requirements, delivery scheduling, vendor portal usage, invoice formatting, BIR compliance; delivers on-site or virtual; tracks adoption", "Procurement Manager / Quality Manager", "VP Supply Chain", "1–2 days per event")]),
    ("Vendor Technology Enablement", "Vendor needs system upgrade for BuildRight integration", "~5–10 technology enablement projects/year", "~5–10/year", "IT Integration Lead", "IT Integration Lead, Procurement Mgr, Vendor IT",
     [("IT helps vendors integrate: EDI/API for order processing, ASN for advance shipping notice, e-invoicing for automated AP, vendor portal adoption; provides documentation and technical support", "IT Integration Lead", "CIO", "5–10 days per vendor")]),
    ("Joint Business Planning with Strategic Vendors", "Annual joint business planning cycle", "Annual; top 20 strategic vendors", "~20 joint plans/year", "VP Supply Chain / VP Merchandising", "VP Supply Chain, VP Merch, Category Mgrs, Strategic Vendors",
     [("Joint planning with top 20 vendors: review past year performance, align on next year's growth targets, discuss new product development, agree on volume commitments and pricing, set collaboration goals", "VP Supply Chain / VP Merchandising", "CEO", "1–2 days per vendor")]),
    ("Vendor Sustainability Development", "ESG improvement need identified per VS-25", "~10–15 vendors/year needing sustainability development", "~10–15/year", "ESG Manager / Procurement Mgr", "ESG Mgr, Procurement Mgr, Vendor, VP Supply Chain",
     [("ESG Manager works with vendors: environmental compliance (DENR), labor standards (DOLE), sustainable packaging, carbon footprint reduction; sets improvement targets; tracks progress quarterly", "ESG Manager / Procurement Manager", "VP Supply Chain", "2–3 days/year per vendor")]),
    ("Vendor Financial Health Monitoring", "Quarterly financial review of strategic vendors", "Quarterly; top 50 strategic vendors", "~50 vendors/quarter", "Finance Director", "Finance Dir, Procurement Mgr, VP Supply Chain",
     [("Finance monitors vendor financial health: credit reports, payment behavior trends, news alerts for financial distress; identifies at-risk vendors for supply continuity planning; recommends dual-sourcing for critical categories", "Finance Director", "CFO", "4–6 hours/quarter")]),
    ("Vendor Innovation Partnership Program", "Annual innovation challenge or ongoing partnership", "Annual; ~10–15 innovative vendors", "~10–15 vendors/year", "VP Merchandising", "VP Merch, Category Mgrs, Procurement Mgr, VP Supply Chain",
     [("VP Merchandising invites innovative vendors to propose: new products, packaging improvements, display innovations, sustainability solutions; evaluates proposals; pilots promising innovations in select stores; scales if successful", "VP Merchandising / Category Manager", "CEO", "5–10 days/year")]),
    ("Vendor Development ROI Measurement", "Annual measurement of development program effectiveness", "Annual", "All vendor development activities", "FP&A Analyst", "FP&A Analyst, Procurement Mgr, VP Supply Chain",
     [("Measures ROI: development program cost vs. vendor performance improvement (quality, delivery, cost savings from improved terms); identifies most impactful development activities; recommends budget allocation for next year", "FP&A Analyst", "CFO", "3–5 days/year")])
    ])
])

# ═══ VS-68: Trade Credit Insurance & Risk Management ═══
grand += mk_vs("VS-68-trade-credit-risk-management", 68,
    "Trade Credit Insurance & Risk Management", "Finance",
    "Manages BuildRight's trade credit risk for ~5,200 trade and corporate accounts representing ~30% of revenue (PHP 18.7B/year). Covers credit risk assessment and scoring, credit limit management and monitoring, bad debt recovery and write-off management, and credit insurance program administration. Integrates with order-to-cash (VS-16), customer experience (VS-13), and finance (VS-17).",
    [("PA-68.1", "trade-credit-risk-assessment", "Trade Credit Risk Assessment & Scoring", [
    ("New Trade Account Credit Application", "New B2B customer applies for trade credit", "~200–300 new credit applications/month", "~200–300/month", "Credit Analyst", "Credit Analyst, Trade Account Mgr, Finance Mgr",
     [("Trade Account Manager collects application: business registration (DTI/SEC), financial statements, trade references, banking references; Credit Analyst verifies documents and runs background check", "Trade Account Mgr / Credit Analyst", "Finance Manager", "1–2 days"),
      ("Credit Analyst assesses risk: business viability, payment history (via credit bureau), financial ratios (current ratio, debt-to-equity), industry risk, relationship potential; assigns risk score (A–E)", "Credit Analyst", "Finance Manager", "4–6 hours")]),
    ("Credit Scoring Model Maintenance", "Quarterly model recalibration", "Quarterly; model serves ~5,200 active accounts", "Model recalibration quarterly", "Credit Analyst / Data Scientist", "Credit Analyst, Data Scientist, Finance Dir",
     [("Data Scientist recalibrates credit scoring model: updates weightings based on actual default experience, adds new predictive variables (payment trend, order frequency changes), backtests against portfolio performance", "Data Scientist / Credit Analyst", "Finance Director", "3–5 days/quarter")]),
    ("Existing Account Periodic Credit Review", "Annual review for all accounts; quarterly for high-risk", "Annual ~5,200 reviews; quarterly ~500 high-risk", "~5,200 annual + ~2,000 quarterly high-risk reviews", "Credit Analyst", "Credit Analyst, Trade Account Mgr, Finance Mgr",
     [("System auto-triggers annual review: refreshes credit bureau data, analyzes 12-month payment behavior, updates financial ratios, recalculates risk score; recommends credit limit adjustment (increase/decrease/maintain)", "System / Credit Analyst", "Finance Manager", "4–6 hours/account"),
      ("Quarterly high-risk reviews: accounts with score decline, late payments >15%, or exceeding 80% of credit limit; Credit Analyst conducts deep review; recommends corrective action", "Credit Analyst", "Finance Director", "2–3 hours/account")]),
    ("Credit Bureau & External Data Integration", "Monthly data refresh from credit bureaus", "Monthly; ~5,200 accounts", "~5,200 accounts refreshed/month", "IT Integration Lead", "IT Integration, Credit Analyst, Credit Bureau",
     [("System pulls monthly credit bureau updates: credit score changes, legal filings, negative events; auto-flags accounts with significant score decline (>20 points) for analyst review", "System / IT Integration Lead", "Credit Analyst", "Automated + 2–3 hours/month")]),
    ("Customer Financial Statement Analysis", "Customer provides updated financial statements", "Annual for top 200 accounts; on request for others", "~200+ analyses/year", "Credit Analyst", "Credit Analyst, Finance Manager",
     [("Credit Analyst reviews financial statements: revenue trend, profitability, liquidity ratios, leverage, cash flow adequacy; compares to industry benchmarks; adjusts risk score accordingly", "Credit Analyst", "Finance Manager", "2–4 hours/account")]),
    ("Industry & Economic Risk Factor Assessment", "Quarterly macro-economic review", "Quarterly; Philippine construction/retail sector", "Quarterly review", "Finance Director", "Finance Dir, VP Sales, CFO",
     [("Finance Director assesses macro risks: Philippine construction sector outlook, interest rate trends, government infrastructure spending, competitor health; adjusts portfolio risk appetite and sector concentration limits", "Finance Director", "CFO", "1–2 days/quarter")]),
    ("Trade Credit Insurance Policy Assessment", "Annual insurance review or portfolio change", "Annual; ~PHP 15–20B in insured receivables", "Annual review + ad-hoc for significant changes", "Finance Director", "Finance Dir, Insurance Broker, CFO",
     [("Finance Director reviews credit insurance policy: coverage adequacy, premium vs. claims experience, policy terms (deductible, exclusions, country limits), insurer financial strength; recommends renewal or re-marketing", "Finance Director", "CFO", "3–5 days/year")]),
    ("Portfolio Risk Concentration Analysis", "Monthly concentration analysis", "Monthly; ~5,200 accounts", "~5,200 accounts analyzed/month", "Credit Analyst", "Credit Analyst, Finance Dir, CFO",
     [("System analyzes portfolio concentration: by customer tier, by industry, by geographic region, by account age; flags concentrations exceeding policy limits (e.g., single customer >5% of portfolio); recommends diversification", "System / Credit Analyst", "Finance Director", "2–3 hours/month")])
    ]),
    ("PA-68.2", "credit-limit-management-monitoring", "Credit Limit Management & Monitoring", [
    ("Credit Limit Setting & Approval", "New account approved or existing account review", "~200–300 new + ~1,000 adjustments/month", "~1,200–1,300/month", "Credit Analyst", "Credit Analyst, Finance Mgr, Finance Dir, CFO",
     [("Credit Analyst recommends limit based on: risk score, financial capacity, order history, relationship potential, credit insurance coverage; approval per matrix: Analyst ≤PHP 500K, Manager ≤PHP 2M, Director ≤PHP 10M, CFO >PHP 10M", "Credit Analyst / Finance Manager / Finance Director / CFO", "CFO", "30 min + approval chain")]),
    ("Real-Time Credit Limit Monitoring", "Order placed against trade account", "Continuous; ~3,500 AR invoices/month", "~3,500/month", "System / Credit Analyst", "System, Credit Analyst, Trade Account Mgr",
     [("System monitors real-time: outstanding balance vs. credit limit; auto-blocks orders exceeding limit; auto-flags accounts at 80% utilization for analyst review; sends alert to Trade Account Manager", "System", "Credit Analyst", "Automated")]),
    ("Credit Limit Increase Request", "Customer or Sales requests higher credit limit", "~100–200 increase requests/month", "~100–200/month", "Trade Account Manager", "Trade Account Mgr, Credit Analyst, Finance Mgr",
     [("Trade Account Manager submits request with justification: sales growth, payment history, new project opportunity; Credit Analyst evaluates; approves or counteroffers; applies to account within 24 hours", "Trade Account Mgr / Credit Analyst", "Finance Manager", "2–4 hours per request")]),
    ("Credit Limit Reduction & Suspension", "Account risk increase detected", "~20–30 reductions/suspensions/month", "~20–30/month", "Credit Analyst", "Credit Analyst, Finance Mgr, Trade Account Mgr, VP Sales",
     [("Credit Analyst reduces or suspends limit based on: payment deterioration, credit bureau alert, financial statement weakness, industry downturn; notifies Trade Account Manager; manages customer relationship impact", "Credit Analyst", "Finance Director", "1–2 hours per action")]),
    ("Overdue Payment Monitoring & Escalation", "Customer payment past due", "Daily monitoring; ~5–8% of accounts typically past due", "~260–416 past-due accounts at any time", "Collections Specialist", "Collections Specialist, Credit Analyst, Finance Mgr",
     [("System generates daily past-due report: aging buckets (30/60/90/120+ days); Collections Specialist contacts customers: 30-day (friendly reminder), 60-day (formal demand), 90-day (hold shipments), 120+ day (legal escalation)", "System / Collections Specialist", "Finance Manager", "2–3 hours/day")]),
    ("Customer Payment Behavior Scoring", "Monthly payment behavior update", "Monthly; ~5,200 active accounts", "~5,200 scores/month", "System / Credit Analyst", "System, Credit Analyst, Collections Specialist",
     [("System calculates payment behavior score: on-time payment %, average days past due, payment trend (improving/deteriorating), promise-to-pay fulfillment rate; feeds into composite risk score", "System", "Credit Analyst", "Automated")]),
    ("Credit Hold Order Management", "Customer on credit hold attempts to place order", "~100–200 credit hold orders/month", "~100–200/month", "Order Management System / Credit Analyst", "OMS, Credit Analyst, Trade Account Mgr, Customer",
     [("System blocks order; notifies Trade Account Manager and Credit Analyst; Analyst evaluates: partial release (up to available credit), conditional release (with payment commitment), or full hold; overrides logged for audit", "System / Credit Analyst", "Finance Manager", "15–30 min per hold")]),
    ("Aging Report & Provisioning Analysis", "Monthly aging analysis", "Monthly; ~5,200 accounts", "Monthly aging report", "Finance Manager", "Finance Mgr, Credit Analyst, Collections Specialist, CFO",
     [("System generates AR aging report: current, 30, 60, 90, 120+ day buckets by account, region, and segment; Finance Manager calculates bad debt provision per PFRS 9 expected credit loss model; adjusts monthly", "System / Finance Manager", "CFO", "4–6 hours/month")])
    ]),
    ("PA-68.3", "bad-debt-recovery-writeoff", "Bad Debt Recovery & Write-Off Management", [
    ("Pre-Legal Collections & Negotiation", "Account reaches 90+ days past due", "~50–80 accounts in pre-legal at any time", "~50–80 accounts", "Collections Manager", "Collections Mgr, Credit Analyst, Legal, VP Sales",
     [("Collections Manager conducts intensive collection: phone, email, in-person visit for high-value accounts; negotiates payment plan (structured payments over 3–6 months); documents all collection activity", "Collections Manager", "Finance Director", "4–6 hours/account")]),
    ("Legal Collection Escalation", "Account reaches 120+ days and pre-legal exhausted", "~20–30 legal escalations/year", "~20–30/year", "Legal Counsel", "Legal, Collections Mgr, Finance Dir, External Counsel",
     [("Legal issues formal demand letter; if no response, files collection case with Philippine courts; manages legal process with external counsel; tracks cases through judicial system", "Legal Counsel", "VP Legal", "2–3 days per case + ongoing")]),
    ("Bad Debt Write-Off Decision", "Account determined uncollectible after all recovery efforts", "~10–15 write-offs/year", "~10–15/year; ~PHP 5–15M total write-offs/year", "Finance Director", "Finance Dir, Credit Analyst, Legal, CFO",
     [("Credit Analyst presents write-off recommendation: collection history, legal status, customer financial situation, recovery probability; Finance Director reviews; CFO approves; Board approves >PHP 1M per account", "Credit Analyst / Finance Director", "CFO", "2–3 days per write-off"),
      ("Finance processes write-off: removes from AR, adjusts bad debt provision, records in GL, updates customer account status; account flagged for no future credit; COD only", "Finance", "CFO", "1 day")]),
    ("Bad Debt Recovery from Written-Off Accounts", "Written-off customer makes partial or full payment", "Ad-hoc; ~5–10 recoveries/year from written-off accounts", "~5–10 recoveries/year", "Collections Specialist", "Collections Specialist, Finance",
     [("Collections Specialist receives payment from written-off account; Finance processes recovery: credits bad debt recovery income, updates customer account; evaluates reinstatement only after 12 months of good behavior", "Collections Specialist / Finance", "Finance Manager", "1–2 hours per recovery")]),
    ("Credit Insurance Claim Filing", "Insured account becomes uncollectible", "~5–10 claims/year", "~5–10/year", "Finance Analyst", "Finance Analyst, Insurance Broker, Credit Insurer",
     [("Analyst files credit insurance claim: customer details, outstanding amount, collection history, reason for non-payment; insurer investigates; approves claim per policy terms; payout received within 60–90 days", "Finance Analyst", "Finance Director", "2–3 days per claim + 60–90 days")]),
    ("Bad Debt Trend Analysis & Prevention", "Monthly trend analysis", "Monthly", "Full portfolio: ~5,200 accounts", "Credit Analyst", "Credit Analyst, Finance Dir, VP Sales",
     [("Analyzes: bad debt rate trend, default predictors, high-risk segments, industry concentration, geographic patterns; recommends: tighter credit criteria, insurance coverage adjustments, portfolio rebalancing", "Credit Analyst", "Finance Director", "4–6 hours/month")]),
    ("Credit Policy Annual Review & Update", "Annual policy review", "Annual", "Full credit policy", "Finance Director", "Finance Dir, CFO, VP Sales, VP Legal",
     [("Reviews and updates: credit approval matrix, limit setting criteria, risk scoring thresholds, collection escalation procedures, write-off criteria, insurance coverage; presents to CFO for approval", "Finance Director", "CFO", "3–5 days/year")]),
    ("Credit Portfolio Performance Dashboard", "Monthly dashboard; real-time alerts", "Continuous; monthly comprehensive", "Full portfolio: ~5,200 accounts", "Finance Director", "Finance Dir, Credit Analysts, CFO, VP Sales",
     [("Dashboard: total AR, aging distribution, DSO (days sales outstanding), bad debt rate, collection effectiveness index, credit utilization rate, insurance coverage ratio; real-time alerts for significant risk events", "System / Finance Director", "CFO", "2–3 hours/month")])
    ])
])

print(f"\nGrand total VS-62 to VS-68: {grand}")
print(f"Running total with VS-53 to VS-61: {216 + grand}")
print(f"Total new workflows: {120 + grand}")
print(f"Updated total (including existing 2,122): {2122 + 120 + grand}")
print(f"Last workflow ID: W{wf_counter - 1}")
