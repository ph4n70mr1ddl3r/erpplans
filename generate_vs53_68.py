#!/usr/bin/env python3
"""Generate VS-53 through VS-68 for BuildRight Depot."""

import os

BASE = "/home/riddler/erpplans/01-model-company/workflows"

# (VS_DIR, VS_NUM, VS_NAME, FAMILY, OVERVIEW, [PAs])
# Each PA: (PA_NUM, SLUG, TITLE, [WORKFLOWS])
# Each Workflow: (NAME, TRIGGER, FREQ, VOL, OWNER, PARTICIPANTS, [STEPS])
# Each Step: (ACTIVITY, ROLE_R, ROLE_A, DURATION)

ALL_VS = []

# ─── VS-53 ───
ALL_VS.append(("VS-53-warranty-guarantee-management", 53,
    "Warranty & Guarantee Management", "Sell & Serve",
    "Manages BuildRight's product warranty lifecycle from registration through claim resolution, covering manufacturer warranties on power tools, appliances, plumbing fixtures, and electrical products; extended warranty/service contracts sold at POS; and building material performance guarantees. Integrates with POS (VS-08), vendor management (VS-03), and customer experience (VS-13). Covers ~35,000 active SKUs with ~60% carrying some form of warranty or guarantee.",
    [("PA-53.1", "warranty-registration-activation", "Product Warranty Registration & Activation", [
        ("POS Warranty Capture at Checkout", "Customer purchases warranty-eligible product at POS or online", "~420,000 warranty-eligible transactions/month", "~420K transactions/month across 200 stores + ecommerce", "Cashier / POS System", "Cashier, Customer, POS System, CRM",
         [("POS auto-identifies warranty-eligible SKU at scan; prompts cashier; captures transaction date, SKU, serial number, store, loyalty ID; generates warranty record in CRM", "POS System", "Cashier", "30–60 sec"),
          ("Cashier prints warranty card with terms, duration, claim instructions, and registration QR code; customer scans for digital warranty wallet", "Cashier", "Store Manager", "30 sec"),
          ("For serial-numbered items: cashier scans or enters serial number; system validates format and links to item+transaction record", "Cashier", "Cashier", "15–30 sec"),
          ("System pushes registration to vendor portal (real-time for top 20 vendors; batch daily for others); customer receives SMS/email confirmation", "System", "IT Integration Lead", "Automated")]),
        ("Online Purchase Warranty Registration", "Ecommerce order with warranty-eligible items fulfilled", "~8,580 warranty registrations/month from ecommerce", "~8,580/month", "Ecommerce System / CRM", "Ecommerce System, CRM, Customer",
         [("Ecommerce platform identifies warranty-eligible SKUs; auto-generates registration upon fulfillment confirmation; sends digital warranty certificate via email", "System", "Ecommerce Ops", "Automated"),
          ("For serial-numbered items: customer prompted to register serial via online form within 14 days; system sends reminders at day 7 and 13", "System", "Customer", "<1 min"),
          ("Warranty data pushed to vendor portal; record linked to customer profile in CRM and visible in mobile app", "System", "CRM", "Automated")]),
        ("Bulk Warranty Registration for Trade Accounts", "Trade/corporate account purchases warranty items in bulk", "~1,050 bulk registrations/month", "~1,050/month; avg 5–15 items per invoice", "Trade Account Manager", "Trade Account Manager, Customer, CRM",
         [("Account Manager creates project warranty file in CRM: links all items to project ID, customer account, delivery addresses", "Trade Account Mgr", "VP Sales", "15–30 min"),
          ("System auto-registers each item with project-level warranty start date (may differ from invoice date for phased deliveries)", "System", "Trade Account Mgr", "Automated"),
          ("Account Manager sends consolidated warranty schedule to customer; system schedules expiry alerts at 30 and 90 days before expiry", "Trade Account Mgr", "Customer", "15 min")]),
        ("Warranty Transfer for Resold Properties", "Homeowner requests warranty transfer to new property owner", "~50–100 requests/month; peaks in summer renovation", "~50–100/month; avg 10–30 items per property", "Customer Service Rep", "CSR, Original Owner, New Owner, CRM",
         [("CSR verifies original purchase in CRM; confirms warranty status, remaining coverage; creates transfer record with new owner details", "CSR", "Customer Service Dir", "10–15 min"),
          ("System sends transfer confirmation to both parties; updates vendor portal; notes expired items and offers extended warranty renewal", "System", "CSR", "Automated")]),
        ("Warranty Master Data Configuration", "New product category or warranty terms change", "~5–10 changes/month; quarterly review", "~60–120 changes/year across 35,000 SKUs", "Merchandise Planner", "Merch Planner, Category Mgr, IT, Legal",
         [("Category Manager defines warranty parameters: type, duration, coverage scope, claim process; Merch Planner configures in ERP item master", "Category Mgr", "VP Merchandising", "30–60 min"),
          ("IT configures POS/ecommerce prompts and serial capture rules; Legal reviews for Consumer Act (RA 7394) compliance", "IT / Legal", "VP Merchandising", "2–3 hours")]),
        ("Warranty Data Quality Audit", "Monthly quality audit schedule", "Monthly audit", "Spot-check ~500 records/month (1%)", "Data Quality Analyst", "Data Quality Analyst, Category Mgr, CS Supervisor",
         [("System generates quality report: registrations without serials, without contacts, duplicates, date anomalies", "System", "Data Quality Analyst", "Automated"),
          ("Analyst spot-checks 500 records; identifies root causes; escalates training gaps, config errors, or vendor API failures", "Data Quality Analyst", "VP Merchandising", "4–6 hours")]),
        ("Warranty Digital Wallet & Customer Portal", "Customer accesses warranty portal via app/web", "~10,000–15,000 views/month", "~150,000 expected activations in Year 1", "Digital Product Manager", "Digital PM, Customer, IT Dev Team",
         [("Customer logs in; sees all warranties by status (active, expiring, expired); can view details, claim history, remaining coverage", "Customer / System", "Digital PM", "<1 min/customer"),
          ("System proactively alerts: warranty expiring in 90 days, product recall notifications, seasonal maintenance reminders", "System", "Customer", "Automated"),
          ("Customer can initiate claim from portal; upload photos; track status in real-time with push notifications", "Customer", "CS Agent", "5–10 min")]),
        ("Warranty Program KPI Monitoring", "Monthly reporting cycle", "Monthly dashboard; weekly metrics", "Full chain: 200 stores + ecommerce + trade", "VP Merchandising", "VP Merch, Category Mgrs, CS Director, VP Supply Chain",
         [("System generates dashboard: active warranties by category, registration rate, claim rate, avg resolution time, warranty cost %, extended warranty attach rate", "System", "VP Merchandising", "Automated"),
          ("Category Managers review high claim rate categories (>5%); CS Director reviews claim satisfaction (target ≥80%); VP reviews warranty P&L", "Various", "VP Merchandising", "2–3 hours")])
    ]),
    ("PA-53.2", "warranty-claim-processing", "Warranty Claim Processing & Resolution", [
        ("In-Store Warranty Claim Initiation", "Customer brings defective product with proof of purchase to store", "~8,000–10,000 claims/month across 200 stores", "~8K–10K/month; peaks Jan–Feb, Jun–Jul", "Customer Service Rep", "CSR, Dept Supervisor, Store Manager, CRM",
         [("CSR verifies warranty in CRM; inspects product; photographs defect; checks serial number match", "CSR", "Store Manager", "10–15 min"),
          ("System classifies claim: standard (auto-approve), borderline (route to Supervisor), out-of-warranty (offer paid repair)", "System", "CSR", "Automated"),
          ("CSR offers resolution: immediate replacement, store credit, service center repair, or DC/vendor replacement (7–14 days)", "CSR", "Customer", "5–10 min"),
          ("Customer selects resolution; system processes inventory adjustment, creates claim record, notifies vendor", "CSR / System", "Store Manager", "5 min")]),
        ("Online Warranty Claim Submission", "Customer submits claim via web portal or mobile app", "~2,000–3,000 online claims/month", "~2K–3K/month (~25% of total)", "Customer Service Agent (Remote)", "CSA, Customer, Store Ops, Logistics",
         [("Customer describes defect, uploads photos/video, selects resolution and preferred store for drop-off", "Customer", "CSA", "5–10 min"),
          ("CSA reviews within 24 hours; validates photos match coverage; approves or requests more info; generates return authorization QR code", "CSA", "CS Supervisor", "10–15 min"),
          ("Customer drops item at store (scans QR) or schedules pickup for bulky items; store receives and triggers resolution", "Customer / Receiving Clerk", "CSA", "14-day window")]),
        ("Vendor Warranty Claim Escalation", "Claim requires manufacturer involvement (high-value >PHP 10K, complex product)", "~1,500–2,000 vendor escalations/month", "~1.5K–2K/month (~20% of claims)", "Vendor Warranty Coordinator", "Coordinator, Vendor, CSR, Category Manager",
         [("System auto-flags for vendor involvement; Coordinator packages claim with photos, purchase proof, serial number", "System / Coordinator", "Category Manager", "30 min"),
          ("Coordinator submits via vendor portal or email; tracks acknowledgment within 48 hours; manages vendor resolution (approve/return/deny)", "Coordinator", "Vendor", "30 min"),
          ("Coordinator tracks 14-day vendor SLA; escalates to Category Manager if breached; monthly vendor warranty scorecard", "Coordinator", "Category Manager", "15 min/case")]),
        ("Service Center Repair Coordination", "Claim requires repair at authorized service center", "~3,000–4,000 repair claims/month", "~3K–4K/month; 7–14 day turnaround", "Service Center Coordinator", "Coordinator, Service Center, CSR, Logistics",
         [("System assigns to nearest authorized service center; generates work order; arranges item transfer from store", "System / Coordinator", "Service Center", "30 min"),
          ("Service center diagnoses: warranty-covered repair → proceed; non-covered → quote customer; beyond repair → replacement authorized", "Service Center", "Coordinator", "7–14 days"),
          ("Repair complete; item returned to store; customer notified for pickup; failure mode data logged for quality analysis", "Service Center / Coordinator", "CS Supervisor", "15 min")]),
        ("Warranty Replacement Fulfillment", "Approved claim resolved via product replacement", "~5,000–6,000 replacement orders/month", "~5K–6K/month (~60% of resolutions)", "Customer Service Supervisor", "CS Supervisor, Store Clerk, DC Ops, Logistics",
         [("System checks replacement availability: in-store (immediate), nearby store (1–2 days), DC (3–5 days), vendor PO (7–21 days)", "System", "CS Supervisor", "Automated"),
          ("For in-stock: inventory reserved, customer picks up. For DC-sourced: included in next shipment, tracking SMS sent", "CSR / DC", "CS Supervisor", "Immediate to 21 days"),
          ("Upon pickup: scans replacement against claim; closes claim; transfers warranty registration to replacement item", "Receiving Clerk", "CS Supervisor", "5 min")]),
        ("Warranty Refund Processing", "Claim resolved via refund (product unrepairable or customer preference)", "~800–1,200 refund claims/month", "~800–1.2K/month (~10% of resolutions)", "Customer Service Supervisor", "CS Supervisor, Store Manager, Finance, Customer",
         [("CSR verifies refund eligibility; determines amount: full refund (<30 days), prorated (based on remaining period), or store credit at 110%", "CSR", "Store Manager", "10–15 min"),
          ("Store Manager approves refunds >PHP 5,000; Finance processes via original payment method; system closes claim", "Store Manager / Finance", "CS Supervisor", "15–20 min")]),
        ("Warranty Claim Dispute Resolution", "Customer disputes denied warranty claim", "~300–500 disputes/month (~3–5%)", "~300–500/month; high-value items", "Customer Service Director", "CS Director, Category Mgr, Legal, Store Manager",
         [("Customer escalates; CSR logs dispute with additional evidence; CS Director reviews documentation, warranty terms, claim history", "CSR / CS Director", "VP Merchandising", "30–60 min"),
          ("Director decides within 5 business days: overturn, uphold (with goodwill gesture), or escalate to Category Manager for vendor dispute", "CS Director", "Legal", "30 min"),
          ("Monthly: Director reviews dispute trends; identifies systemic issues by vendor, category; implements corrective action", "CS Director", "VP Merchandising", "2–3 hours")]),
        ("Warranty Claim Analytics & Trends", "Monthly analytics cycle", "Monthly comprehensive; weekly operational", "Monthly: ~10,000 claims analyzed", "Analytics Manager", "Analytics Mgr, Category Mgrs, Quality Mgr, VP Merch",
         [("System generates analytics: claim volume by category/vendor/store, claim rate by SKU, resolution time, cost, top 20 claim SKUs, repeat claim rate", "System", "Analytics Manager", "Automated"),
          ("Analytics Manager identifies trends: rate increase >2x triggers quality alert; vendor >5% triggers vendor review; store >2x average triggers investigation", "Analytics Manager", "Category Manager", "4–6 hours")])
    ]),
    ("PA-53.3", "extended-warranty-service-contract", "Extended Warranty & Service Contract Management", [
        ("Extended Warranty Product Design & Pricing", "Annual review or new category launch", "Quarterly review; new category as needed", "~10–15 products across 6 categories", "Category Manager", "Category Mgr, Finance (Actuarial), Legal, VP Merch",
         [("Category Manager identifies eligible categories; Finance calculates pricing based on claim rate, repair cost, target margin (40–60%)", "Category Mgr / Finance", "VP Merchandising", "2–3 days"),
          ("Legal reviews contract terms for Consumer Act compliance; Manager configures in ERP with service SKU, pricing tiers, POS upsell rules", "Legal / Category Mgr", "VP Merchandising", "1–2 days")]),
        ("Extended Warranty POS Upsell", "Customer purchases eligible item at POS", "~42,000 upsell opportunities/month", "~42K/month; target 15–20% attach rate", "Cashier", "Cashier, Customer, POS System",
         [("POS auto-prompts with warranty options and price; cashier presents offer using trained script", "Cashier", "Store Manager", "30–60 sec"),
          ("Customer accepts: warranty added to transaction, contract printed on receipt, digital acknowledgment signed; auto-registered in CRM", "Cashier / System", "Cashier", "30 sec"),
          ("Customer declines: recorded for analytics; no repeated offers to protect customer experience", "POS System", "Analytics Manager", "Automated")]),
        ("Extended Warranty Contract Management", "Contract active through coverage period", "~75,000–100,000 active contracts", "~75K–100K active contracts at any time", "Warranty Administrator", "Warranty Admin, Finance, CS, Legal",
         [("System maintains contract lifecycle (active/approaching expiry/expired/cancelled); monthly liability accrual journal generated", "System / Finance", "Finance Manager", "4–6 hours/month"),
          ("Quarterly: review contract portfolio (renewal rate, claim rate vs. estimate, cancellation rate, revenue vs. cost); annual re-pricing", "Warranty Admin / Finance", "VP Merchandising", "4–6 hours/quarter")]),
        ("Extended Warranty Claim Processing", "Customer files claim on product covered by extended warranty", "~1,500–2,500 extended warranty claims/month", "~1.5K–2.5K/month; higher avg value", "Extended Warranty Claims Specialist", "Claims Specialist, CSR, Service Center, Finance",
         [("System verifies active contract, coverage period, claim type; Specialist validates defect is covered (not wear/misuse/accidental)", "System / Specialist", "CS Director", "20–30 min"),
          ("Specialist authorizes: repair at service center, replacement (>70% of replacement cost), or store credit; Finance tracks vs. accrual", "Specialist", "Finance Manager", "15–30 min")]),
        ("Extended Warranty Renewal & Extension", "Contract approaching expiry (90/30/7-day alerts)", "~6,000–8,000 renewal opportunities/month", "~6K–8K/month; target 25–30% renewal", "Warranty Administrator", "Warranty Admin, Customer, Digital Marketing",
         [("System auto-sends renewal notices at 90, 30, and 7 days with pricing and easy renewal link (online/in-store/phone)", "System", "Warranty Admin", "Automated"),
          ("Customer renews via online payment, in-store, or phone; system extends contract, generates new certificate, schedules next expiry cycle", "Customer / CSR", "Warranty Admin", "10–15 min (phone)")]),
        ("Extended Warranty Cancellation & Refund", "Customer requests cancellation", "~200–400 cancellations/month (~3–5%)", "~200–400/month", "Customer Service Rep", "CSR, Finance, Customer",
         [("CSR verifies contract; within 30-day cooling-off: full refund; after: prorated (remaining months / total × price minus claims)", "CSR", "CS Supervisor", "10–15 min"),
          ("System processes refund to original payment method; terminates contract; adjusts warranty liability accrual; posts GL entries", "System / Finance", "Finance Manager", "5 min")]),
        ("Performance Guarantee Management", "Customer invokes building material performance guarantee", "~500–800 guarantee claims/month; peaks rainy season", "~500–800/month; high value (house repaint, re-tile)", "Building Materials Category Manager", "Category Mgr, Technical Specialist, CS, Vendor",
         [("Technical Specialist dispatched to customer site: inspects conditions, takes samples/photos, assesses product defect vs. installation error vs. environmental", "Technical Specialist", "Category Manager", "2–4 hours"),
          ("Specialist submits report: product defect → full claim (material + labor); installation error → deny; mixed cause → partial coverage", "Technical Specialist", "Category Manager", "1–2 days"),
          ("For approved claims: processes material replacement and coordinates re-application; vendor notified for cost recovery", "Category Manager", "VP Merchandising", "7–14 days resolution")]),
        ("Warranty Partner & Insurer Management", "Annual contract renewal or quarterly review", "Annual renewal; quarterly reviews", "1–2 warranty insurance partners; ~PHP 15–20M annual premium", "VP Merchandising", "VP Merch, Finance Director, Legal, Insurance Partner",
         [("Finance reviews program financials: premium vs. claims recovered, loss ratio, admin costs; determines self-insure vs. partner by category", "Finance Director", "CFO", "4–6 hours/quarter"),
          ("VP Merchandising conducts quarterly performance review with partner: claim approval rate, turnaround, customer satisfaction, loss ratio", "VP Merchandising", "Insurance Partner", "2–3 hours/quarter"),
          ("Annual: contract renewal negotiation; Legal reviews terms; VP presents strategy to Executive Committee", "VP Merch / Legal", "CEO", "2–3 days/year")])
    ])
]))

# ─── VS-54 ───
ALL_VS.append(("VS-54-gift-card-stored-value", 54,
    "Gift Card & Stored Value Management", "Finance",
    "Manages BuildRight's gift card program including physical gift cards sold in-store, digital gift cards sold online, corporate bulk purchases, and stored-value wallet integration with the loyalty program. The gift card program drives ~2% of total revenue and is a key customer acquisition tool during holiday seasons. Integrates with POS (VS-08), ecommerce (VS-10), loyalty (VS-13), and finance (VS-17).",
    [("PA-54.1", "gift-card-issuance-distribution", "Gift Card Issuance & Distribution", [
        ("Physical Gift Card Stock Management", "Gift card inventory reorder point or new design launch", "Monthly reorder; quarterly new designs", "~50,000 cards printed/year; 10,000 in circulation", "Marketing Operations Manager", "Marketing Ops, Print Vendor, Store Manager, Finance",
         [("Marketing Ops monitors stock levels in ERP; reorder at 20 cards/store; places print order with denomination mix and seasonal design", "Marketing Ops Mgr", "VP Marketing", "1–2 hours"),
          ("Vendor delivers to DC; DC distributes to stores; Store Manager receives, scans into inventory as inactive; stores in cash office safe", "DC / Store Manager", "Marketing Ops Mgr", "2–3 days"),
          ("Quarterly: Finance reconciles physical stock vs. system; investigates discrepancies; lost/stolen cards deactivated", "Finance", "Marketing Ops Mgr", "2–3 hours")]),
        ("Gift Card Sale & Activation at POS", "Customer purchases gift card at POS", "~15,000–20,000 gift card transactions/month", "~15K–20K/month; avg PHP 2,000; ~PHP 30–40M/month", "Cashier", "Cashier, Customer, POS System, Finance",
         [("Cashier scans inactive card barcode; POS prompts for load amount (min PHP 300, max PHP 50,000); activates card in real-time", "Cashier", "Store Manager", "1–2 min"),
          ("Customer pays via any tender; transaction as gift card liability (not revenue); receipt with card number, balance, expiry, terms", "Cashier / System", "Finance", "30 sec"),
          ("System sends optional SMS to purchaser confirming activation; gift card liability recorded in GL", "System", "Finance", "Automated")]),
        ("Digital Gift Card Sale & Delivery", "Customer purchases digital gift card online", "~3,000–5,000 digital cards/month; growing 20% QoQ", "~3K–5K/month; avg PHP 2,500", "Ecommerce Operations", "Ecommerce System, Payment Gateway, Customer",
         [("Customer selects design, amount, recipient info, personal message; pays online; system generates unique card number and PIN", "Customer / System", "Ecommerce Ops", "<30 sec"),
          ("System delivers via email (gift card image, barcode, instructions) and/or SMS; records liability in GL; links to purchaser/recipient in CRM", "System", "Finance", "<30 sec"),
          ("Purchaser receives delivery confirmation; system re-sends if delivery fails within 24 hours", "System", "Ecommerce Ops", "Automated")]),
        ("Corporate Bulk Gift Card Program", "Corporate client requests bulk purchase", "~20–30 corporate orders/month; peaks at Christmas", "~20–30 orders/month; 50–500 cards each", "Corporate Sales Manager", "Corp Sales Mgr, Finance, Marketing Ops, Client",
         [("Corp Sales Manager prepares quotation: base value + customization fee; volume discount (>100: 3%, >500: 5%); client approves and pays", "Corp Sales Mgr", "VP Sales", "1–2 hours"),
          ("Marketing Ops coordinates: physical cards (print, activate, custom sleeve, deliver) or digital cards (bulk generate, distribute); Finance records liability", "Marketing Ops / Finance", "Corp Sales Mgr", "7–10 days")]),
        ("Gift Card Promotional Campaign", "Marketing launches gift card promotion (e.g., buy PHP 5K get PHP 500 bonus)", "~4–6 campaigns/year aligned with seasonal calendar", "~4–6 campaigns/year; 30–50% lift during campaign", "Marketing Promotions Manager", "Marketing, Finance, POS IT, Store Ops",
         [("Marketing designs promo (bonus structure, dates, channels, max per customer, budget); Finance reviews cost impact and approves", "Marketing / Finance", "CFO", "2–3 days"),
          ("POS/IT configures promotional rules (auto-bonus, dates, limits, tracking); Store Ops cascades to stores with training and signage", "IT / Store Ops", "Marketing", "1–2 days"),
          ("Post-campaign: analyze results (cards sold vs. baseline, bonus cost vs. incremental revenue, redemption rate, ROI)", "Marketing", "VP Marketing", "2–4 hours")]),
        ("Gift Card Distribution Channel Management", "Monthly performance review or new channel activation", "Monthly review; ad-hoc activation", "4 channels: POS (70%), ecommerce (20%), app (5%), corporate (5%)", "Marketing Operations Manager", "Marketing Ops, Channel Managers, IT, Finance",
         [("Marketing Ops monitors sales by channel (avg value, activation rate, delivery success, cost-to-serve); reviews underperformers; evaluates new channels (Gifted.ph, bank portals, Lazada/Shopee)", "Marketing Ops Mgr", "CMO", "4–6 hours/month"),
          ("Quarterly: presents channel strategy to CMO with investment, onboarding, and sunset recommendations", "Marketing Ops Mgr", "CMO", "2–3 hours/quarter")]),
        ("Gift Card Compliance & Regulatory Management", "BSP regulation update or annual review", "Annual comprehensive; ad-hoc for changes", "BSP stored-value regulations; Consumer Act; AMLA", "Legal & Compliance Officer", "Legal, Finance Director, VP Merch, External Auditor",
         [("Legal monitors BSP regulations (5-year validity, no dormancy fees, consumer disclosures, AML >PHP 500K); reviews T&Cs annually", "Legal Officer", "VP Legal", "2–3 days/year"),
          ("Finance ensures proper accounting (liability at activation, revenue at redemption, breakage per PFRS 15, monthly reconciliation)", "Finance", "External Auditor", "2–3 hours/month")]),
        ("Gift Card Denomination & Pricing Strategy", "Semi-annual pricing review", "Semi-annual", "Standard: PHP 300, 500, 1K, 2K, 3K, 5K, 10K", "Category Manager (Gift Cards)", "Category Mgr, Finance, Marketing, Store Ops",
         [("Category Manager analyzes sales by denomination; benchmarks vs. competitors (Wilcon, SM, Robinsons); recommends adjustments", "Category Mgr", "VP Merchandising", "1–2 days"),
          ("Finance models revenue impact; Store Ops implements: updates POS buttons, trains cashiers, adjusts physical card stock", "Finance / Store Ops", "Category Mgr", "1–2 days")])
    ]),
    ("PA-54.2", "gift-card-redemption-balance", "Gift Card Redemption & Balance Management", [
        ("In-Store Gift Card Redemption at POS", "Customer presents gift card as payment", "~12,000–18,000 redemptions/month", "~12K–18K/month; avg PHP 1,800", "Cashier", "Cashier, Customer, POS System, Finance",
         [("Cashier scans physical card or enters digital card number + PIN; POS validates (active, not expired, sufficient balance, not stolen)", "Cashier", "Store Manager", "30–60 sec"),
          ("If full coverage: processes payment, reduces balance. If partial: applies gift card first, prompts additional tender (split payment)", "POS System", "Cashier", "30–60 sec"),
          ("System records redemption: debits gift card liability, credits revenue; auto-deactivates zero-balance cards", "System", "Finance", "Automated")]),
        ("Online Gift Card Redemption", "Customer applies gift card at ecommerce checkout", "~3,000–5,000 online redemptions/month", "~3K–5K/month; growing", "Ecommerce System", "Ecommerce, Payment Gateway, CRM",
         [("Customer enters card number + PIN at checkout; system validates; applies balance; customer confirms amount (full or partial)", "Customer / System", "Ecommerce Ops", "<5 sec"),
          ("Upon fulfillment: finalizes redemption (debits liability, credits revenue). If cancelled before fulfillment: reverses redemption, restores balance", "System", "Finance", "Automated")]),
        ("Gift Card Balance Inquiry & Statement", "Customer requests balance via any channel", "~8,000–12,000 inquiries/month", "~8K–12K/month across SMS, app, web, in-store", "CSR / Self-Service", "Customer, CRM, SMS Gateway, App",
         [("Customer checks via SMS (text card number), app (scan barcode), web (login), or in-store (cashier scan); system retrieves real-time balance and transaction history", "Customer / System", "IT Integration Lead", "<10 sec"),
          ("System proactively sends expiry alerts at 60 and 30 days for cards with balance >PHP 500; app shows consolidated wallet for multiple cards", "System", "Customer", "Automated")]),
        ("Lost/Stolen Gift Card Management", "Customer reports lost or stolen physical card", "~200–400 reports/month (~1–2%)", "~200–400/month; primarily physical cards", "Customer Service Rep", "CSR, Customer, Finance, Store Manager",
         [("CSR verifies purchase (receipt, loyalty ID, transaction ref); places Lost/Stolen hold on original card (freezes balance)", "CSR", "CS Supervisor", "10–15 min"),
          ("System generates replacement digital card with equivalent balance; sends to customer; original permanently deactivated; Finance logs for audit", "System / CSR", "Finance", "5 min")]),
        ("Gift Card Partial Redemption & Multi-Card Payment", "Customer uses multiple gift cards for one transaction", "~2,000–3,000 multi-card transactions/month", "~2K–3K/month; ~15% of redemptions", "Cashier / POS System", "Cashier, Customer, POS System",
         [("Cashier scans/enters each card sequentially; POS accumulates payments; if insufficient, prompts additional tender", "Cashier", "Store Manager", "1–2 min"),
          ("Each card balance reduced; receipt shows itemized breakdown (Gift Card 1: PHP X, Gift Card 2: PHP Y, Cash: PHP Z); all balances updated in real-time", "POS System", "Finance", "30 sec")]),
        ("Gift Card Reload & Top-Up", "Customer adds value to existing gift card", "~3,000–5,000 reloads/month", "~3K–5K/month; avg PHP 1,500", "Cashier / Ecommerce System", "Cashier, Customer, System, Finance",
         [("Customer presents card and requests reload (min PHP 300, max PHP 50K); pays via any tender; system updates balance in real-time", "Cashier / System", "Store Manager", "1–2 min"),
          ("Receipt shows previous balance, reload amount, new balance, updated expiry (BSP: reload extends 5 years); loyalty points earned on reload", "System", "Customer", "30 sec")]),
        ("Gift Card Expiry & Breakage Management", "Gift card reaches 5-year expiry or monthly analysis", "Daily expiry; monthly breakage analysis", "~5–10% breakage; ~PHP 20–40M/year", "Finance Manager", "Finance Mgr, Accountant, External Auditor",
         [("System auto-monitors expiry; sends 60/30/7-day customer alerts; on expiry: moves balance from liability to breakage tracking", "System", "Finance Manager", "Automated"),
          ("Monthly: Finance reviews breakage estimate (historical patterns, outstanding liability by vintage); quarterly recognizes breakage revenue per PFRS 15", "Finance Manager", "CFO", "4–6 hours/month")]),
        ("Gift Card Refund & Cancellation", "Customer requests cancellation within cooling-off or error correction", "~100–200 cancellations/month (~1%)", "~100–200/month", "CS Supervisor", "CS Supervisor, Customer, Finance, Store Manager",
         [("CSR verifies un-redeemed full balance; processes cancellation within 24-hr (physical) or 48-hr (digital) cooling-off; refunds to original payment", "CSR", "CS Supervisor", "10–15 min"),
          ("Post cooling-off: case-by-case; partial redemption → no refund on redeemed portion; remaining → store credit only; Finance adjusts liability", "CSR / Finance", "Finance Manager", "10 min")])
    ]),
    ("PA-54.3", "gift-card-reconciliation-analytics", "Gift Card Reconciliation & Analytics", [
        ("Daily Gift Card Liability Reconciliation", "End-of-day POS close and ecommerce settlement", "Daily across 200 stores + ecommerce", "~15,000–25,000 daily GC transactions", "Accountant (AP/AR)", "Accountant, Cashiers, Ecommerce Finance, Treasury",
         [("System generates daily reconciliation: activations, redemptions, reloads, cancellations, expiries, net change in liability", "System", "Accountant", "Automated"),
          ("Accountant verifies POS transaction sum matches GL; ecommerce matches payment gateway; investigates discrepancies (timing, errors, operational)", "Accountant", "Finance Manager", "1–2 hours")]),
        ("Monthly Gift Card Financial Reporting", "Monthly financial close per VS-17", "Monthly", "Full GC program for 5 entities", "Finance Manager", "Finance Mgr, Accountant, CFO",
         [("Finance Manager prepares monthly report: opening/closing liability, activations, redemptions, breakage, cancellations, promo liability, aging by quarter", "Finance Manager", "CFO", "4–6 hours"),
          ("Ensures proper intercompany treatment (liability at selling entity, revenue at redemption entity); included in management reporting package", "Finance Manager", "CFO", "1–2 hours")]),
        ("Gift Card Fraud Monitoring & Prevention", "Real-time alerts or weekly review", "Real-time + weekly comprehensive", "~50–100 flagged transactions/week; <0.5% fraud", "Loss Prevention Analyst", "LP Analyst, Finance, CS, Store Manager",
         [("System monitors patterns: rapid activation-redemption, stolen card usage, large purchases (>PHP 50K), multiple cards same payment, high-risk IPs", "System", "LP Analyst", "Real-time"),
          ("LP Analyst reviews flagged: checks patterns, verifies identity for high-value, confirms fraud → freeze, reverse, report; weekly fraud trend report; monthly rule updates", "LP Analyst", "LP Director", "2–3 hours/day")]),
        ("Gift Card Program ROI Analysis", "Quarterly program review", "Quarterly; annual comprehensive", "~PHP 500–600M annual liability; ~PHP 30–50M breakage", "FP&A Analyst", "FP&A, VP Merchandising, CFO, Marketing Dir",
         [("FP&A compiles program P&L (sales, promo costs, processing, breakage, net margin); analyzes customer behavior (time to redeem, basket size, incremental spend, new customer acquisition)", "FP&A Analyst", "Finance Director", "1–2 days/quarter"),
          ("Calculates ROI by channel and denomination; presents quarterly with recommendations to VP Merchandising and CFO", "FP&A Analyst", "CFO", "2–3 hours")]),
        ("Gift Card Customer Satisfaction Monitoring", "Monthly CX review per VS-13", "Monthly analysis; quarterly comprehensive", "~2,000–3,000 feedback items/month", "Customer Experience Manager", "CX Manager, Marketing, Store Ops, IT",
         [("CX Manager analyzes gift card NPS (purchase + redemption experience), common complaints, social media sentiment; identifies top 3 pain points per channel", "CX Manager", "CS Director", "4–6 hours/month"),
          ("Prioritizes improvements (quick wins vs. system enhancements); coordinates with IT, Store Ops, Marketing; tracks KPIs (NPS ≥75, friction <2 min)", "CX Manager", "VP Marketing", "2–3 hours/month")]),
        ("Gift Card System Integration & API Management", "Monthly maintenance or API degradation", "Monthly maintenance; real-time monitoring", "4 integration points: POS, ecommerce, app, CRM", "IT Integration Lead", "IT Integration, POS Vendor, Ecommerce, Finance IT",
         [("IT monitors API performance (activation <2 sec, redemption <1 sec, balance inquiry <1 sec, uptime 99.95%); reviews error logs monthly", "IT Integration Lead", "CIO", "4–6 hours/month"),
          ("Manages version upgrades, data encryption (encrypted at rest/transit, PIN hashed, PCI-DSS compliance); quarterly penetration testing", "IT Integration Lead", "CIO", "2–3 days/quarter")]),
        ("Gift Card Benchmarking & Competitive Analysis", "Semi-annual competitive review", "Semi-annual", "4–6 competitors (Wilcon, CitiHardware, Handyman, SM, Robinsons)", "Marketing Analyst", "Marketing Analyst, VP Merch, Category Mgr",
         [("Analyst researches competitor programs (denominations, physical/digital, expiry, reload, promos, channels); mystery shops for CX evaluation", "Marketing Analyst", "VP Marketing", "3–5 days/semi-annual"),
          ("Prepares competitive matrix; identifies gaps and advantages; recommends new features, differentiators, pricing adjustments", "Marketing Analyst", "VP Merchandising", "1–2 days")]),
        ("Gift Card Channel Profitability Analysis", "Quarterly analysis", "Quarterly", "4 channels", "FP&A Analyst", "FP&A, Marketing Ops, Finance Manager",
         [("FP&A calculates channel profitability: revenue per channel minus processing costs, fraud losses, promotional costs, and channel commissions", "FP&A Analyst", "Finance Director", "4–6 hours/quarter"),
          ("Identifies most/least profitable channels; recommends investment reallocation; evaluates third-party marketplace cost-benefit", "FP&A Analyst", "CFO", "2–3 hours/quarter")])
    ])
]))

# ─── VS-55 through VS-68: Abbreviated but still BuildRight-specific ───

# VS-55: Store Planogram & Space Optimization
ALL_VS.append(("VS-55-store-planogram-space-optimization", 55,
    "Store Planogram & Space Optimization", "Sell & Serve",
    "Manages store layout planning, planogram design, space productivity analysis, and fixture management across 200 big-box stores. Ensures optimal product placement for maximum sales per square meter (target: PHP 22,000–28,000/sqm/year). Covers planogram creation, compliance auditing, fixture procurement, and space analytics.",
    [("PA-55.1", "planogram-design-space-allocation", "Planogram Design & Category Space Allocation", [
        ("Seasonal Planogram Refresh", "Seasonal calendar trigger (6 rotations/year)", "Bi-monthly; 200 stores × 8 zones", "~1,600 planogram updates per rotation", "Merchandising Planner", "Merch Planner, Category Mgr, Store Ops Director",
         [("Planner reviews category performance (sales/sqm, margin/sqm, turns); designs planogram with space planning software assigning linear meterage per category", "Merchandising Planner", "Category Manager", "2–3 days"),
          ("Category Manager validates assortment alignment and cross-merchandising; Store Ops Director reviews format-specific adaptations for large/standard/compact stores", "Category Mgr / Store Ops Dir", "VP Merchandising", "4–6 hours"),
          ("System generates store-specific planogram packages; distributes to stores via VS-63 communication system", "System", "Merchandising Planner", "Automated")]),
        ("New Product Shelf Placement", "New SKU introduction (~200–300/month)", "~200–300 placement decisions/month", "~200–300/month", "Category Manager", "Category Mgr, Merch Planner, Buyer",
         [("Buyer submits new SKU with dimensions, category, expected velocity; Planner evaluates shelf space and optimal position", "Buyer / Merch Planner", "Category Manager", "45 min"),
          ("Planner assigns position, facing count, min shelf quantity; determines displaced SKU; system pushes update to stores with shelf labels", "Merchandising Planner", "Category Manager", "30 min")]),
        ("Cross-Merchandising Display Planning", "Seasonal promotion requiring cross-merch display", "~10–15 displays per rotation", "~2,000 implementations per rotation", "Merchandising Planner", "Merch Planner, Category Mgr, Marketing",
         [("Planner identifies opportunities (bathroom set, electrical corner, garden starter); designs display layout with fixtures and signage", "Merchandising Planner", "Category Manager", "6–8 hours"),
          ("Marketing designs POP materials; coordinates print for 200 stores; Store Ops communicates display requirements with compliance photos", "Marketing / Store Ops", "VP Marketing", "3–5 days")]),
        ("Space Productivity Analysis", "Monthly analytics cycle", "Monthly; 200 stores × 8 zones", "~1,600 zone-level analyses/month", "Analytics Manager", "Analytics Mgr, Category Mgr, Merch Planner",
         [("System calculates sales/sqm, margin/sqm, turns/sqm per zone; identifies top-performing and underperforming zones and stores", "System / Analytics Mgr", "Category Manager", "2–3 hours"),
          ("Category Manager reviews underperformers; Planner adjusts planogram for next rotation (expand high-productivity, reduce low-productivity)", "Category Mgr / Merch Planner", "VP Merchandising", "4–6 hours")]),
        ("Planogram Version Control", "Every planogram change", "Continuous; ~500–800 changes/month", "~500–800 version updates/month", "Merchandising Planner", "Merch Planner, IT, Store Ops",
         [("System auto-versions changes (date, user, zones, SKUs, reason); Planner reviews change log weekly; 24-month history maintained per store", "System / Merch Planner", "IT System Admin", "1–2 hours/week")]),
        ("Store Layout Zone Optimization", "Annual review or new store design", "Annual per store; ~10–15 new stores/year", "~10–15 new + 20–30 optimizations/year", "Store Design Manager", "Store Design Mgr, Store Ops Dir, VP Merch",
         [("Store Design Manager analyzes traffic flow, dwell time, conversion by zone; designs optimized layout with expanded high-conversion zones", "Store Design Manager", "COO", "3–5 days"),
          ("VP Merchandising and COO review and approve with expected ROI; scheduled for low-sales periods", "VP Merch / COO", "CEO", "2–3 hours")]),
        ("Category Adjacency Planning", "Quarterly review", "Quarterly; 13 categories", "~13 adjacency reviews/quarter", "Merchandising Planner", "Merch Planner, Category Mgr, Store Design Mgr",
         [("Planner reviews adjacency map and cross-category purchase patterns from POS data; proposes changes for logical complementary placement", "Merchandising Planner", "Category Manager", "6–8 hours"),
          ("Category Manager approves; incorporates into next seasonal planogram refresh", "Category Manager", "VP Merchandising", "1 hour")]),
        ("Planogram Cost-Benefit Analysis", "Bi-monthly (seasonal rotations)", "6 analyses/year", "6 analyses/year", "FP&A Analyst", "FP&A, Merch Planner, Category Mgr",
         [("FP&A calculates change cost (labor, labels, fixtures, signage) vs. projected benefit (sales uplift, margin improvement, inventory cost reduction)", "FP&A Analyst", "Finance Manager", "6–8 hours"),
          ("Post-rotation: measures actual vs. projected uplift; incorporates learning into next projection model", "FP&A Analyst", "VP Merchandising", "2–3 hours")])
    ]),
    ("PA-55.2", "planogram-compliance-audit", "Planogram Compliance & Audit", [
        ("Planogram Compliance Audit", "Monthly per store", "Monthly; 200 stores", "~200 audits/month", "Regional Operations Manager", "Regional Ops Mgr, Store Manager, Merch Planner",
         [("Regional Ops Manager walks store zone by zone comparing actual to planogram; scores compliance (SKU position, facing count, labels, displays)", "Regional Ops Mgr", "Store Ops Director", "2–3 hours/store"),
          ("Photographs non-compliant zones; uploads to compliance system; Store Manager remediates within 48 hours; monthly scorecard (target ≥90%)", "Regional Ops Mgr / Store Manager", "Store Ops Director", "2–4 hours")]),
        ("Photo-Based Remote Compliance Check", "Weekly photo submission", "Weekly from 200 stores", "~200 submissions/week", "Merchandising Coordinator", "Merch Coordinator, Store Manager, Regional Ops",
         [("Store staff photographs each zone per protocol; uploads via store manager app with timestamps and geo-tags", "Store Staff", "Store Manager", "30 min"),
          ("Coordinator spot-checks 40 stores/week; scores and flags issues; sends feedback within 48 hours; escalates non-responsive stores", "Merch Coordinator", "Merch Planner", "4–6 hours/week")]),
        ("Shelf Label & Price Accuracy Audit", "Monthly or price change event", "Monthly per store + ad-hoc", "~200 audits/month + ad-hoc", "Department Supervisor", "Dept Supervisor, Store Manager, Pricing Analyst",
         [("Supervisor audits shelf labels vs. system SRP: checks price match, missing/damaged labels, promo accuracy; corrects issues with RF gun", "Department Supervisor", "Store Manager", "1–2 hours/section"),
          ("Store Manager reviews monthly accuracy score (target ≥99%); below 97% triggers retraining", "Store Manager", "Regional Ops Mgr", "30 min")]),
        ("Endcap & Promotional Display Compliance", "Promotional period start + mid-period", "~12 checks/year × 200 stores", "~2,400 compliance checks/year", "Merchandising Coordinator", "Merch Coordinator, Store Manager, Marketing",
         [("Coordinator issues display brief; Store Manager sets up within 48 hours and submits photos; Coordinator reviews within 24 hours", "Merch Coordinator / Store Manager", "Marketing Manager", "4–6 hours/period"),
          ("Mid-period: verifies display maintained (restocked, clean, signage intact); flags depleted displays for replenishment", "Merch Coordinator", "Store Ops Director", "2–3 hours/period")]),
        ("Store Walk-In Traffic & Heatmap Analysis", "Monthly analytics from CCTV/counters", "Monthly; 200 stores", "~200 analyses/month", "Analytics Manager", "Analytics Mgr, Store Design Mgr, Store Ops",
         [("System compiles traffic data (visitors, conversion, dwell time, peaks); generates heatmaps (hot/cold zones, flow patterns)", "System / Analytics Mgr", "Store Design Manager", "2–3 hours"),
          ("Correlates with sales data; identifies high-traffic/low-conversion zones (opportunity) and low-traffic/high-conversion (optimize access)", "Analytics Manager", "Store Ops Director", "1–2 hours")]),
        ("Fixture & Display Equipment Inventory", "Quarterly; 200 stores", "Quarterly", "~200 fixture inventories/quarter", "Store Manager", "Store Manager, Facilities Coord, Merch Planner",
         [("Store Manager inventories fixtures (gondolas, pegboards, endcaps, specialty displays); records condition; photographs damage", "Store Staff", "Store Manager", "2–3 hours"),
          ("Facilities Coordinator reviews repairs/replacements by priority and budget; Merch Planner orders new fixtures for seasonal rotation", "Facilities Coord / Merch Planner", "Store Ops Director", "2–3 hours")]),
        ("Store Cleanliness & Visual Standards Audit", "Weekly self-audit; monthly Regional audit", "Weekly + monthly", "~800 self + 200 Regional audits/month", "Store Manager / Regional Ops Mgr", "Store Manager, Regional Ops Mgr, Store Staff",
         [("Store Manager conducts weekly visual walk (cleanliness, obstructions, lighting, signage); records issues with photos; resolves within 24 hours", "Store Manager", "Store Ops Director", "45 min"),
          ("Regional Ops Manager monthly surprise audit; 50-point scorecard; results factor into Store Manager performance review", "Regional Ops Mgr", "Store Ops Director", "45–60 min")]),
        ("Planogram Change Implementation Tracking", "Every planogram deployment to stores", "~1,500–2,000 implementations/year", "~125–170/month", "Merchandising Coordinator", "Merch Coordinator, Store Manager, Regional Ops",
         [("System distributes change package via app (zone maps, labels, instructions, deadline); Store Manager acknowledges and assigns stock team", "System / Store Manager", "Merch Coordinator", "15 min + 4–8 hrs execution"),
          ("Store Manager submits completion photos; Coordinator verifies within 48 hours; non-compliant stores receive remediation request", "Store Manager / Merch Coordinator", "Regional Ops Mgr", "15 min")])
    ]),
    ("PA-55.3", "space-productivity-fixture-mgmt", "Space Productivity & Fixture Management", [
        ("Sales Per Square Meter Analysis", "Monthly analytics", "Monthly; 200 stores", "~1,600 zone-level analyses", "Analytics Manager", "Analytics Mgr, Category Mgr, VP Merch, Store Ops Dir",
         [("System calculates monthly sales/sqm per zone per store; benchmarks vs. chain average and top-quartile", "System", "Analytics Manager", "Automated"),
          ("Category Manager drills into underperformers; Store Ops Director works with Store Managers on improvement plans for bottom-quartile", "Category Mgr / Store Ops Dir", "VP Merchandising", "3–4 hours")]),
        ("Fixture Procurement & Budgeting", "Annual budget cycle or replacement need", "Annual; ~PHP 20–30M budget", "~10–15 new store packages + replacements/year", "Facilities Coordinator", "Facilities Coord, Store Design Mgr, VP Finance",
         [("Coordinator compiles needs (new stores, replacements, specialty); solicits 3–5 vendor bids; recommends to VP Finance; manages delivery", "Facilities Coordinator", "Store Ops Director", "3–5 days")]),
        ("Shelf Capacity & Stocking Optimization", "Monthly replenishment planning", "Monthly; 35,000 SKUs per store", "35,000 SKU capacity analyses/store", "Merchandising Planner", "Merch Planner, DC Ops, Store Manager",
         [("System calculates shelf capacity per SKU (facings × units vs. weekly velocity); identifies overfaced (reduce) and underfaced (increase) SKUs", "System / Merch Planner", "Category Manager", "2–3 hours"),
          ("Planner adjusts min shelf quantities and replenishment triggers per store format; feeds into automated replenishment per VS-02", "Merchandising Planner", "DC Operations", "2–3 hours")]),
        ("Promotional Space ROI Analysis", "Post-promotional period", "6/year (bi-monthly)", "6 analyses/year", "FP&A Analyst", "FP&A, Marketing Mgr, Category Mgr",
         [("FP&A calculates incremental display sales vs. standard shelf, display cost vs. incremental margin; compares endcap vs. power aisle vs. inline effectiveness", "FP&A Analyst", "Finance Manager", "3–4 hours")]),
        ("Store Format Segmentation", "Annual strategy review", "Annual; 200 stores in 3 formats", "200 stores across 3 segments", "Store Design Manager", "Store Design Mgr, VP Merch, COO",
         [("Manager segments stores (large flagship 20, standard 120, compact 60); develops format-specific planogram templates with curated assortments", "Store Design Manager", "COO", "3–5 days"),
          ("COO approves format strategy; annual re-evaluation based on 12-month performance; stores may upgrade/downgrade format", "COO", "CEO", "2–3 hours")]),
        ("Seasonal Display Space Rotation", "Pre-season planning (6 seasons/year)", "6 rotations/year; 200 stores", "~1,200 rotations/year", "Merchandising Planner", "Merch Planner, Marketing, Store Ops",
         [("Planner allocates seasonal space per format; Marketing designs visual package; coordinates DC staging and 1-week store changeover window", "Merch Planner / Marketing", "VP Marketing", "1–2 weeks")]),
        ("Planogram Performance Dashboard", "Real-time; monthly deep analysis", "Continuous; monthly deep dive", "Chain-wide + 200 store views", "Analytics Manager", "Analytics Mgr, Merch Planner, Category Mgrs",
         [("Real-time dashboard: sales/sqm, compliance rate, stock-out rate by zone/store; daily flag review (compliance drop, stock-out >5%, sales decline >15%)", "System / Analytics Mgr", "VP Merchandising", "30 min/day"),
          ("Monthly deep-dive on 2–3 zones/categories; quarterly comprehensive report to Executive Committee with capital recommendations", "Analytics Manager", "VP Merchandising", "4–6 hours")]),
        ("Space Capital Investment Analysis", "Annual capital planning", "Annual; 10–20 renovation decisions", "10–20 analyses/year", "FP&A Director", "FP&A Dir, Store Design Mgr, COO, CFO",
         [("FP&A compiles requests; calculates ROI (projected uplift, margin, payback, NPV over 5 years); COO/CFO prioritize by ROI and budget", "FP&A Director", "CFO", "2–3 days"),
          ("Post-renovation: tracks actual vs. projected for 12 months; feeds into future projection models", "FP&A Director", "CFO", "ongoing")])
    ])
]))

# Continue with remaining VS in compact format...

def write_vs_files(vs_dir, vs_num, vs_name, family, overview, pas):
    """Write all files for a value stream."""
    wf_counter = [2118 + sum(
        len(pa[3]) for prev_vs in ALL_VS[:next(i for i, v in enumerate(ALL_VS) if v[1] == vs_num)]
        for pa in prev_vs[5]
    )]
    # Simpler: just count from start
    pass

def main():
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
            
            # Build PA file
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
        
        # Write README
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
