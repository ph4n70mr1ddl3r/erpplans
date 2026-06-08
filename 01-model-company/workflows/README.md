# BuildRight Depot Corp. — Operational Workflows


> This document describes the end-to-end operational workflows of BuildRight Depot,
> defining who does what, when, and why. It serves three purposes:
>
> 1. **Validate headcount** — by mapping work volume to roles, we can verify staffing assumptions
> 2. **Inform ERP design** — each workflow reveals system touchpoints, automation opportunities, and integration needs
> 3. **Optimize organization** — by exposing handoffs, bottlenecks, and spans of control

---

## How to Read This Document

Each workflow follows this format:

| Field | Meaning |
|---|---|
| **Workflow ID** | Unique identifier (WF-XX) |
| **Name** | Process name |
| **Trigger** | What initiates the workflow |
| **Frequency** | How often it occurs |
| **Volume** | How many instances per occurrence |
| **Owner** | Role accountable for the outcome |
| **Participants** | All roles involved |
| **Steps** | Sequential activities with responsible role |
| **System Touchpoints** | Where ERP/system support is needed |
| **Time Estimate** | Estimated effort per occurrence |
| **Pain Points / Risks** | What can go wrong |

**RACI Key**: R = Responsible (does the work), A = Accountable (owns the outcome), C = Consulted, I = Informed

---


## Domain Files

Workflows are organized by functional domain for easier navigation and gap analysis:

- **[Merchandising & Pricing Workflows](./WF-merchandising.md)** (32 workflows) — Assortment planning, promotions, pricing, product lifecycle, PIM, vendor rebate management, markdown & clearance pricing, sample & demo inventory management, category performance review & P&L ownership, pricing hierarchy governance, private label development, competitor intelligence, store promotional setup & visual merchandising, seasonal merchandise transition, product substitution rules, store-level price tag printing, competitive price tactical response, loyalty tier re-evaluation & migration processing, new product introduction (NPI) & full store rollout, competitor store visit program & market intelligence operations, product quality lab testing & certification management, multi-channel pricing consistency monitoring & governance, assortment optimization & rationalization review, vendor new product in-store launch event & demonstration coordination, store-level barangay & local fiesta merchandising calendar management, customer product bundle assembly & pre-packaged solution kit management, and vendor consignment shelf space performance monitoring & optimization.
- **[Procurement & Vendor Management Workflows](./WF-procurement.md)** (45 workflows) — Purchase orders, vendor onboarding, VMI, special orders, vendor performance, contracts, return to vendor processing, supplier quality CAPA, supplier diversity, indirect procurement, vendor invoice dispute, vendor performance chargebacks, VMI collaborative data sharing, supplier financial health & credit risk monitoring, vendor-funded promotional activity & co-op advertising management, vendor due diligence & onboarding site visit management, vendor-managed inventory (VMI) daily performance monitoring, strategic sourcing & category strategy, competitive bidding & tender management, purchase price variance (PPV) analysis & cost management, vendor contract compliance monitoring & enforcement, supplier emergency onboarding & rapid activation, commodity price monitoring & procurement strategy, VMI quarterly business review & program optimization, vendor seasonal buy-back & stock return agreement execution, vendor product packaging sustainability assessment & compliance management, vendor catalog price change intake & assessment, and VMI periodic data accuracy audit & reconciliation.
- **[Warehouse & Logistics Workflows](./WF-warehouse.md)** (26 workflows) — Receiving, putaway, kit assembly, fleet management, inter-island logistics, DC outbound dispatch & load planning, cross-docking, container yard, pallet tracking, DC daily operations & shift management, DC dock scheduling & appointment management, DC daily KPI dashboard & performance tracking, DC cycle counting & inventory accuracy program, DC safety operations & compliance, warehouse equipment preventive maintenance, reverse logistics processing (customer/store returns at DC), seasonal warehouse surge planning & execution, DC quality control & vendor compliance inspection at receiving, DC workforce scheduling & productivity tracking, DC security operations & perimeter management, and DC building maintenance & facility condition monitoring.
- **[Inventory Management Workflows](./WF-inventory.md)** (23 workflows) — Replenishment, cycle counting, transfers, consignment, physical inventory, backorders, promo stock allocation, damaged goods disposition, inventory adjustment authorization, multi-channel inventory allocation governance, inter-store/inter-DC stock rebalancing, SLOB provisioning, in-store bulk-to-retail repackaging, inventory count reconciliation & variance root cause analysis, obsolescence identification & write-off management, and seasonal inventory build-down & transition execution.
- **[Store Operations Workflows](./WF-store-operations.md)** (163 workflows) — Daily store selling, POS, returns, loyalty, DSD receiving, gift cards, new store opening/closure, warranty, facility maintenance, performance review, planogram compliance, store renovation projects, store-level inventory receiving & putaway, automated store cash management (Smart Safe), employee purchase program, mobile POS, cashier dispute resolution, endless aisle, third-party financing, mid-day cash sweeps, self-checkout, LP investigation, in-store emergency response, AI shelf monitoring, solo parent discount compliance, yard loading operations, display & demo infrastructure maintenance, PWD accessibility compliance & store facilities audit, first aid & medical emergency response, non-hazardous waste management, pest control & sanitation management, digital signage & content management, self-checkout daily operations, cashier shift handover, cashier training & certification, suspicious transaction & AML reporting, age-restricted product verification, transaction suspend/park/recall, daily transaction review & cashier performance audit, promotional terminal setup & verification, demo/display unit selling, nightly batch synchronization, customer queue management, tax exemption processing, digital receipt delivery, void & refund tiered authorization, high-value transaction documentation, bagging & bag fee compliance, clearance & final sale processing, real-time event streaming & continuous sync, multi-origin/mixed-basket fulfillment orchestration, offline capability scope & local operations, unified order management & cross-channel fulfillment routing, card terminal & acquirer settlement operations, real-time loss prevention exception monitoring & alert response, promotional coupon/voucher & manufacturer coupon processing, BIR invoice reprint/adjustment & credit note issuance, cash office operations & bank deposit preparation, quotation & estimate generation with sales conversion, consignment sell-through transaction processing & vendor settlement trigger, service work order creation & scheduling, special order & customer order processing, deposit & progress payment collection for project orders, scan & go/mobile self-scan checkout, third-party on-demand delivery integration, damaged & open-box item discount processing, loyalty points as payment tender, customer on-the-spot loyalty enrollment & account lookup, donation & charity round-up processing, pricing error detection & immediate correction at checkout, daily shelf replenishment & restocking, non-emergency incident & hazard reporting, loss prevention daily routine, daily communication & memo acknowledgment, daily planogram execution & shelf compliance check, store-level daily closing procedure, weekly sales & operations review, typhoon & severe weather preparedness, holiday season operational ramp-up, payday weekend operational readiness, daily equipment safety check, emergency manual operations protocol, vendor representative access management, fire drill execution & documentation, seasonal promotional transition & display reset, store-level daily HR operations & people management, store-level labor cost monitoring & overtime budget control, store-level employee disciplinary process & DOLE due process compliance, store-level customer experience standards & daily service operations, return fraud detection & serial returner management, store-level water & utility conservation operations, store-level product demo & trial station daily operations, store-level customer feedback collection & daily CX pulse monitoring, store-level new employee buddy system & first-week onboarding, store-level KPI dashboard & daily performance monitoring, store-level inventory receiving quality control, store-level price verification & daily compliance operations, store-level home delivery & third-party logistics coordination, store-level BOPIS order aging & abandoned pickup processing, store-level rain check issuance for out-of-stock promotional items, store-level customer hold & will-call order management, store-level parking lot & exterior facility daily management, store-level customer loyalty card replacement & account recovery, store-level product recall customer notification execution, customer gift card corporate & bulk purchase processing, store-level trade professional verification & pro badge issuance for discount program, store-level customer material sample loan & return management, store-level emergency generator fuel reserve management & DOE compliance, customer trade-in & used power tool buy-back program, store-level vendor-led product knowledge training & staff certification program, customer walk-in bulk purchase negotiation & volume pricing approval, store-level self-service kiosk & interactive product information station management, lost & found item management, customer comfort room & amenity daily operations, customer product registration at POS for vendor extended warranty, customer wheelchair & PWD mobility assistance service, and customer baggage hold & parcel custody service.
- **[Ecommerce Workflows](./WF-ecommerce.md)** (33 workflows) — BOPIS order fulfillment, home delivery fulfillment, ship-from-store, ecommerce order exception & cancellation management, home delivery reverse logistics (returns), marketplace integration, fulfillment hub, drop-ship, smart locker, ecommerce fraud prevention, digital payment reconciliation, ecommerce product return inspection, grading & disposition, ecommerce product review & rating management, abandoned cart recovery & retargeting, SEO & digital merchandising management, flash sale & limited-time offer operations, new product launch & go-live process, ecommerce platform incident management, customer bulk/project delivery scheduling & multi-drop coordination (B2C), customer project photo gallery & social proof/inspiration platform, customer consumables subscription & auto-replenishment service, ecommerce live commerce & social selling operations, ecommerce assembly & installation service upsell at online checkout, customer back-in-stock notification subscription & alert management, customer wishlist & price drop alert, and customer product comparison tool & buying guide content management.
- **[Finance & Treasury Workflows](./WF-finance.md)** (88 workflows) — AP, AR, financial close, intercompany, capex, budget, treasury, insurance, credit/debit notes, management reporting, FX hedging, bad debt management, product costing & margin analysis, bank reconciliation, tax filing & statutory remittance, customer deposit management, payment settlement reconciliation, vendor statement reconciliation, customer refund & credit processing, customer credit collection, intercompany loans/dividends, Senior Citizen/PWD VAT-exemption reporting, BIR eFPS filing, e-wallet settlement reconciliation, asset under construction, freight bill audit, cash-in-transit management, intercompany SLA billing, BOI/PEZA/LGU tax incentive monitoring, BIR EIS e-invoicing compliance, B2B customer withholding tax (Form 2307) collection & reconciliation, BIR annual inventory list submission (RMC 57-2015), related party transaction disclosure (PAS 24), revenue recognition review (PFRS 15 complex scenarios), credit card chargeback dispute management, store-level operating budget & cost control, vendor advance payment & prepayment management, BIR percentage tax computation & payment, transfer order in-transit damage claim & resolution, AP payment run & batch processing execution, customer credit monitoring & automated alert management, insurance claims processing & recovery management, payment gateway daily operations & settlement monitoring, intercompany rate setting & quarterly transfer pricing review, store-level weekly payroll accrual & labor cost flash report, revenue assurance & POS revenue reconciliation, PFRS 16 lease accounting operations, standardized balance sheet account reconciliation, financial controls testing & monitoring, period-end journal entry review & approval, rolling forecast & financial scenario planning, merchant fee analysis & payment cost optimization, fixed asset depreciation run & component accounting operations, AP aging management & vendor payment prioritization, customer credit portfolio periodic review & collection strategy, cash flow variance analysis & liquidity stress testing, store-level daily opening safe count & cash float preparation, multi-entity consolidation monthly execution & elimination processing, customer credit note aging management & unredeemed credit write-off, vendor rebate claim filing & settlement documentation processing, BIR VAT refund claim processing & input VAT recovery, customer overpayment detection & refund processing, AP vendor debit memo processing & account deduction management, intercompany inventory movement accounting & goods-in-transit reconciliation, and customer store credit expiration management & unclaimed credit processing.
- **[HR & Payroll Workflows](./WF-hr.md)** (51 workflows) — Payroll, recruitment, shift scheduling, onboarding/offboarding, training, performance, expenses, employee loans, PPE & uniform, succession & internal mobility, management trainee program, statutory benefits & claims administration, vendor promodizer management, court-ordered wage garnishment, vendor-funded promodizer incentive management, DOLE-174 compliance, labor union & collective bargaining management, employee wellness & mental health program management, employee cross-entity & cross-location transfer processing, store-level health & safety committee operations, seasonal & temporary staffing process, employee attendance exception management, employee cross-training & skill matrix management, employee exit interview & attrition analysis, store-level employee engagement survey & action planning, employee recognition & rewards program management, off-cycle & ad-hoc payment processing, HMO & private benefits administration, final pay computation & separation settlement, 13th month pay reconciliation & compliance, strategic workforce planning, HR service desk operations, employee data privacy compliance operations, employee career development & internal job posting operations, and employee competency assessment & certification management.
- **[Supply Chain Planning Workflows](./WF-supply-chain.md)** (26 workflows) — Demand forecasting, seasonal buy planning, S&OP cycle, international logistics/import operations, supply chain network optimization, incoterm & marine insurance tracking, port demurrage management, supply chain control tower, last-mile tracking, customs bonded warehouse operations, temperature-controlled & sensitive goods logistics, supplier risk assessment & supply disruption contingency planning, mock product recall exercise & recall readiness testing, cross-functional new store opening readiness review, supply chain cost analysis & logistics optimization review, store-level emergency local sourcing & alternative vendor activation, and store-level rainy season emergency product deployment & rapid stock replenishment.
- **[Regulatory Permits & Local Government Compliance](./WF-regulatory-permits.md)** (9 workflows) — DTI-BPS mandatory product certification (ICC/SOC), LGU sanitary & health permit management, specialized hardware permits, LGU/BFP fire safety inspection certificate (FSIC) management, DENR Permit to Operate & Wastewater Discharge Permit compliance, FDA License to Operate (LTO) for Household Hazardous Substances, CAAP Height Clearance Permit compliance, BIR branch registration & RDO transfer management, and LGU local business tax computation & payment management.
- **[Customer Experience Workflows](./WF-customer.md)** (45 workflows) — Complaint resolution, corporate/project accounts, price matching, satisfaction measurement, account reactivation, feedback-to-action loop, trade sales pipeline & territory management, trade counter / pro desk operations, customer data platform, omni-channel customer ticketing & support management, call center daily operations & queue management, loyalty member enrollment & onboarding journey, customer credit limit periodic review, customer complaint root cause analysis & systemic improvement, customer account maintenance & B2B information update, customer account dormancy identification & deactivation, mystery shopping program & CX compliance audit, B2B customer success & quarterly business review operations, customer churn prediction & proactive retention management, customer account merge & deduplication request processing, service recovery & customer retention program, customer segmentation & target marketing operations, customer loyalty program partner management, customer data platform daily operations & data quality management, customer project material list save/share/reorder ("Project Vault"), store-level pro desk appointment scheduling & priority service queue management, store-level contractor referral & customer-contractor matchmaking service, customer digital warranty vault & multi-vendor warranty claim aggregation, customer project completion celebration & review incentive program, customer price protection & price adjustment policy processing, customer loyalty account deceased member processing & points estate transfer, customer B2B self-service portal order management & account access, and customer loyalty family/household account linking & shared benefits management.
- **[IT Operations Workflows](./WF-it-operations.md)** (57 workflows) — Helpdesk, data privacy breach response, disaster recovery, data migration/parallel-run testing, business intelligence & data governance, IT asset lifecycle management, software development & change management, employee IT provisioning & access lifecycle, enterprise API & systems integration lifecycle, POS terminal hardware maintenance, network infrastructure, cybersecurity operations, cloud management, vendor governance, software licensing, MDM, IT FinOps, project intake, privileged access, capacity planning, SSL management, problem management, service requests, alert/event management, knowledge management, backup & recovery, security incident response, environment management, data migration operational lifecycle, IT strategy & roadmap, IT compliance self-assessment, shadow IT governance, data privacy impact assessment, IT service continuity planning, software quality assurance, IT service level management, remote access management, technical skills lifecycle, mobile app store management, ERP data archiving, cyber threat intelligence, IT innovation PoC lifecycle, NPC annual registration, ERP patch, upgrade & release management, data warehouse & ETL pipeline daily operations & monitoring, customer mobile app daily operations & content management, ERP business change request & enhancement backlog management, and business intelligence report development & governance lifecycle.
- **[Compliance & Governance Workflows](./WF-compliance.md)** (39 workflows) — Loss prevention, business continuity, LGU permits, BIR audit, government procurement, grievance/whistleblower, hazardous waste disposal, external audit coordination, sustainability & environmental compliance reporting, BIR CAS compliance audit, e-waste collection, community relations, product liability, security camera audit, data subject access requests, store recycling, DTI sales promotion permits, DENR SMR/CMR reporting, branch de-registration, community solicitation & donation processing, temporary LGU permits for outdoor events, DOLE drug-free workplace program compliance, pandemic/epidemic business response protocol, DOLE labor inspection response protocol, unified regulatory compliance calendar & dashboard, enterprise risk register maintenance & quarterly risk review, product recall effectiveness verification & post-recall review, anti-bribery & anti-corruption (ABAC) compliance program, regulatory change management & impact assessment, general regulatory inspection response protocol, and business continuity plan maintenance & annual BIA refresh.
- **[Marketing Campaign Workflows](./WF-marketing.md)** (23 workflows) — Campaign planning, creative production, multi-channel execution, budget tracking, performance measurement, loyalty program financial governance, crisis communication, CSR program execution, social media & influencer management, PR & corporate communications, bank partnership management, referral program, in-house creative production, retail media network vendor billing, customer loyalty fraud detection & prevention, marketing campaign ROI & attribution analysis, loyalty points expiry management & annual liability cleanup, digital marketing campaign operations & cross-channel execution, marketing budget management & spend analytics, customer loyalty partner reward catalog management & fulfillment, customer trade account co-branded credit card program management, store-level customer loyalty points gifting & transfer between members, and customer loyalty reward physical fulfillment & partner logistics management.
- **[Real Estate & Lease Management Workflows](./WF-property.md)** (8 workflows) — Site selection, lease administration, rent processing, property tax management, IFRS 16/PFRS 16 lease accounting, corporate staff housing & billeting management, and store closure, lease termination & asset recovery management.
- **[Internal Audit & Risk Management Workflows](./WF-audit.md)** (42 workflows) — Audit planning, execution, ERM, fraud investigation, ABC monitoring, ITGC, continuous control monitoring, issue remediation, third-party vendor risk, capex project audits, QAIP, payroll audit, SOD review, regulatory compliance, cash audits, ESG assurance, inventory observation, lease compliance, trade spend audit, logistics audit, construction audit, e-commerce audit, revenue assurance, tax audit, BC/DR audit, external audit coordination, fixed asset audit, ethical sourcing audit, AML screening, IP brand protection audit, treasury audit, master data audit, insurance audit, media spend audit, succession audit, and organized retail crime (ORC) investigation & task force.

- **[Corporate Governance, Legal & Strategy Workflows](./WF-governance.md)** (14 workflows) — Board operations, legal case management, IP management, strategic planning, project management, legal contract review, SOP governance, management performance reporting, public liability claims, enterprise data governance council, SEC reportorial requirements compliance (GIS, AFS, GAN, MC 28), and annual stockholders' meeting (ASHM) management.
- **[Installation & Value-Added Services](./WF-services.md)** (15 workflows) — Home installation, tool rental, DIY workshops, design consultancy, paint mixing, lumber cutting, 3D rendering, contractor quality audit, subscription billing for recurring services, power tool service & repair center operations, site technical survey & measurement services, service SKU catalog management & pricing, service customer complaint & warranty claim management, and store-level custom paint formula save, recall & reorder service, and store-level community workshop space booking & DIY event management.
- **[Engineering & Construction Workflows](./WF-engineering-construction.md)** (8 workflows) — Site development, new store construction, renovations, commissioning, construction safety management & DOLE DO 13 compliance, construction quality assurance & milestone inspection, and construction document control & as-built management.
- **[Treasury & Corporate Finance Workflows](./WF-treasury.md)** (18 workflows) — LC management, cash flow forecasting, intercompany elimination, transfer pricing, bank account lifecycle & signatory management, surplus cash investment, debt facility & covenant compliance, electronic banking security & payment control, FX exposure analysis & BSP regulatory reporting, treasury policy & risk governance, cash concentration & inter-entity pooling, supply chain finance & dynamic discounting, corporate guarantee & contingent liability management, treasury month-end close & reconciliation, external shareholder dividend declaration & payment, AR post-dated check warehousing, AP post-dated check issuance, and bounced check recovery.
- **[Hazardous Materials (Hazmat) & Compliance](./WF-hazmat.md)** (7 workflows) — Hazmat storage, safety handling, spill response, customs reconciliation, SDS lifecycle management, hazmat transportation & carrier compliance, and hazmat regulatory change management.
- **[Facility & Asset Maintenance (HQ & DC)](./WF-non-store-maintenance.md)** (7 workflows) — DC/HQ maintenance, 3PL performance, POA/Board resolutions, facility condition assessment, utility infrastructure management, and generator preventive maintenance & fuel management.
- **[Health, Safety & Environment Workflows](./WF-health-safety.md)** (13 workflows) — Occupational health & safety (OHS) incident management, workplace safety inspection & audit, contractor & third-party on-site safety orientation, annual OHS statutory reporting (WAIR/AMR), safety training & certification tracking, emergency response & evacuation protocol management, contractor & visitor safety induction, workplace ergonomics assessment, store-level fire safety equipment daily inspection, store-level hazardous material customer advisory, occupational health surveillance & employee medical monitoring, workers' compensation & SSS/ECC claims processing, and annual fire safety system testing & BFP compliance.
- **[Wholesale & Reseller Operations Workflows](./WF-wholesale.md)** (9 workflows) — Wholesale reseller onboarding, bulk fulfillment/cross-docking, B2B punchout catalog integration, wholesale pricing & quotation management, wholesale returns & credit processing, wholesale customer contract renewal, wholesale consignment inventory management, wholesale backorder management & allocation, and wholesale delivery proof & POD reconciliation.
- **[Project-Based B2B & Trade Sales Workflows](./WF-project-sales.md)** (11 workflows) — Quotations, bid management, contract pricing, staged deliveries, project-specific logistics, sales commission, credit limit exception escalation, batch/shade reconciliation, project change order management, project close-out & warranty handover, and customer project budget tracking & material cost variance management.
- **[ESG & Sustainability Reporting Workflows](./WF-esg.md)** (10 workflows) — Carbon footprint, waste management, circular economy, social impact, sustainable sourcing, salvage & scrap monetization, store energy efficiency monitoring, water consumption tracking, ESG data collection & annual report preparation, green building certification (BERDE/LEED), and ESG incident response & regulatory citation management.
- **[Fleet Operations & Driver Management](./WF-logistics-fleet.md)** (8 workflows) — Route optimization, driver performance, fuel management, fleet telematics & real-time tracking, LGU truck ban & route governance, fleet accident & incident management, driver onboarding & certification, and vehicle acquisition, registration, insurance & disposal lifecycle management.
- **[Innovation & Digital Transformation](./WF-innovation.md)** (5 workflows) — AI/ML, RPA, predictive maintenance, computer vision, and retail analytics.
- **[Master Data Management (MDM) Workflows](./WF-master-data.md)** (41 workflows) — Centralized item master, customer deduplication, location hierarchy, vendor data, financial master, pricing, category tree, data quality, employee master, tax & regulatory master, UOM & conversions, payment terms, service/non-stock item master, warehouse location & bin master, product attribute templates, assortment & store cluster master, promotional rule master, reason code & disposition master, kit/BOM structure master, manufacturer/brand master, routing/carrier/transit time master, intercompany transfer pricing rule master, seasonal calendar & event master, currency & exchange rate master, fiscal calendar & posting period master, bank & banking partner master, address & geographic hierarchy master (Philippine-specific), barcode/GTIN & item identification master, replenishment & planning parameter master, loyalty program configuration & rule master, planogram template & space planning master, product lifecycle status & transition rule master, digital asset & product content master, fixed asset master, EAM master, fleet master, contract master, competitor master, POS hardware master, privacy consent master, and ESG metrics master.
- **[Document Management (DOC) Workflows](./WF-document-management.md)** (2 workflows) — ERP-wide document storage, enterprise retention archiving.
- **[Loss Prevention & Asset Protection Workflows](./WF-loss-prevention.md)** (10 workflows) — Daily exception-based reporting & transaction monitoring, CCTV & surveillance system daily operations, internal theft investigation & employee dishonesty case management, organized retail crime (ORC) detection & task force coordination, refund & return fraud detection & prevention, cash handling exception monitoring & sweethearting detection, vendor & delivery fraud detection & dock security audit, store entrance/exit audit & EAS management, shrinkage analysis & reduction program, and loss prevention training & awareness program.
- **[Business Continuity & Disaster Recovery Workflows](./WF-business-continuity.md)** (10 workflows) — BCP annual review & update, typhoon & natural disaster emergency protocol, IT disaster recovery site activation & failover, store emergency closure & reopening, critical system recovery & service restoration, supply chain disruption business impact assessment & recovery, BCP tabletop exercise & drill execution, pandemic/epidemic business continuity activation, communication tree activation & crisis communication, and post-incident review & lessons learned.
- **[Insurance & Claims Management Workflows](./WF-insurance.md)** (8 workflows) — Store & DC property insurance claim filing, typhoon/flood/natural disaster damage assessment & claim, vehicle & fleet insurance claim processing, business interruption insurance claim, employee injury insurance claim coordination & SSS/ECC filing, insurance policy annual renewal & coverage review, third-party liability claim & customer incident response, and insurance claim recovery & settlement accounting.
- **[Vendor Portal & Supplier Collaboration Workflows](./WF-vendor-portal.md)** (8 workflows) — Vendor portal user onboarding & training, vendor self-service PO acknowledgment, vendor self-service invoice submission & payment inquiry, vendor catalog & product information self-service, vendor dispute resolution & issue ticketing, vendor compliance document upload & tracking, supplier scorecard portal publication, and vendor RFQ & bid submission portal management.
- **[Product Recall Management Workflows](./WF-product-recall.md)** (6 workflows) — Product safety incident triage & recall risk assessment, recall customer notification campaign, recall inventory quarantine & disposition, recall regulatory reporting & DTI/BIR/FDA compliance, recall vendor recovery & cost reimbursement, and recall effectiveness audit & close-out.
- **[Business Intelligence & Analytics Operations Workflows](./WF-bi-analytics.md)** (7 workflows) — Daily report distribution & dashboard refresh, BI dashboard development & user request management, data warehouse ETL monitoring & exception handling, self-service BI governance & access provisioning, ad-hoc analytics request fulfillment, data quality monitoring & remediation, and monthly executive reporting package preparation.
- **[Customer Credit & Collections Management Workflows](./WF-credit-collections.md)** (8 workflows) — Customer credit application processing & scoring, credit limit review & adjustment, credit hold management & order blocking, AR aging analysis & collection prioritization, collection call execution & promise tracking, bad debt write-off proposal & approval, customer statement generation & distribution, and credit scorecard annual review & portfolio analysis.

- **[Additional Operational Workflows — Batch 2](./WF-additional-workflows.md)** (20 workflows) — Glass cutting, pipe threading, key duplication, screen fabrication, live video commerce, social commerce, AI renovation visualizer, vehicle loading, bulk breaking, service tip processing, contractor micro-lending, delivery/installation follow-up, daily-wage worker facilitation, employee annual physical exam, tuition assistance, cash variance monitoring, vendor rebate volume compliance, seasonal forward stock pre-positioning, AML covered transaction reporting, and vendor display compliance audit.
- **[Additional Operational Workflows — Batch 3](./WF-additional-workflows-batch3.md)** (20 workflows) — Tile & flooring quantity calculator, bulk cement/sand/aggregates delivery, complete renovation packages, construction loan assistance, material takeoff estimation, multi-store aggregated orders, quick reorder from history, post-disaster insurance replacement, power tool battery compatibility checker, franchise/dealer mini-store program, employee long service awards, project staged delivery, home energy audit referral, lumber grade selection, RA 7641 retirement benefits, seasonal product post-season review, B2B blanket purchase agreements, B2B construction site delivery, paint color matching from sample, and electrical load calculation service.
- **[Additional Operational Workflows — Batch 4](./WF-additional-workflows-batch4.md)** (20 workflows) — Roofing material calculator, water tank/pump sizing, aircon BTU calculation, rebar cutting & bending, fence/gate estimation, welding & metal fabrication, plumbing layout design, solar panel ROI calculator, electrical circuit design, garden/landscape consultation, construction project timeline planner, employee typhoon disaster relief, vendor consignment ageing analysis, contractor VIP retention program, fixture compatibility checker, septic tank sizing, tile sample loan program, ceiling system calculator, employee profit sharing, and vendor product sampling lifecycle.
- **[Additional Operational Workflows — Batch 5](./WF-additional-workflows-batch5.md)** (20 workflows) — Paint mixing station maintenance, material delivery self-service scheduling, shelf stock rotation for paint/chemicals, vendor ASN reconciliation, tool demo reservation, power tool battery station safety, custom order pricing lifecycle, outdoor garden center weather protection, trade account credit insurance, hazardous material spill kit management, last-mile delivery partner review, multi-entity corporate billing, forklift safety checks, installation warranty registration, scrap metal revenue recognition, project progress payment verification, SDS customer access compliance, consignment physical count, loading dock equipment maintenance, and trade account statement dispute resolution.
- **[Additional Operational Workflows — Batch 6](./WF-additional-workflows-batch6.md)** (20 workflows) — Post-typhoon rapid reopening, material escrow & project fund management, shelving/racking safety inspection, vendor product discontinuation & last-time buy, AI chatbot & virtual shopping assistant, shopping cart & customer equipment management, DC environmental monitoring, district manager weekly operations review, delivery service area geo-fencing, employee overtime pre-approval & DOLE cap enforcement, vendor lead time accuracy monitoring, ecommerce payment failure recovery & retry, store-level RTV consolidation & batch shipping, digital product passport & sustainability labeling, annual physical inventory preparation & execution, vendor catalog synchronization & product data quality audit, housewarming & new home gift registry, customer parking lot safety & vehicle management, DC outbound quality sampling & pre-shipment inspection, and employee store-level rotational cross-training & multi-skill certification.
- **[Additional Operational Workflows — Batch 7](./WF-additional-workflows-batch7.md)** (20 workflows) — Customer paint coverage area calculator, concrete mix ratio & volume calculator, PVC pipe cutting & jointing service, door & window measurement & custom order service, rainy season floor safety & anti-slip management, rainwater harvesting system design service, tool sharpening & small engine maintenance service, staircase material calculator, fire extinguisher monthly inspection & BFP compliance, gutter & downspout sizing calculator, bathroom & kitchen exhaust fan sizing service, wire & cable cut-to-length spool service, water filtration system sizing service, construction permit advisory service, insulation material calculator, bulk construction water delivery coordination, kitchen countertop measurement & custom fabrication order, rebar stirrup & tying wire quantity estimator, tile grout & adhesive quantity calculator, and scaffolding rental & safety harness package service.
- **[Workflow-to-System Touchpoint Map](./workflow-system-touchpoint-map.md)** — ERP module-to-workflow cross-reference
- [**Workflow Criticality Classification**](./workflow-criticality-classification.md) — Operational criticality tiers for all 962 workflows

- **[Workflow Dependency Map](./workflow-dependency-map.md)** — Prerequisite relationships, critical path, circular risks, go-live readiness checklist

---

## Complete Workflow Index (W1–W893)

| ID | Workflow Name | Domain File |
|---|---|---|
| W1 | Merchandise Planning & Assortment Review | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W2 | Procurement — Purchase Order Cycle | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W2A | Auto-Replenishment (Stocking Items) | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W2B | Import Purchase Orders | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W2C | Blanket / Contract Purchase Orders | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W3 | Warehouse Receiving & Putaway | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W3B | Yard & Outdoor Inventory Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W3C | DC Inbound Delivery Scheduling | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W4 | Store Replenishment (DC → Store) | [Inventory Management Workflows](WF-inventory.md) |
| W4B | Store-Initiated Replenishment Request | [Inventory Management Workflows](WF-inventory.md) |
| W5 | Daily Store Operations | [Store Operations Workflows](WF-store-operations.md) |
| W5A | Store Opening | [Store Operations Workflows](WF-store-operations.md) |
| W5B | In-Store Selling | [Store Operations Workflows](WF-store-operations.md) |
| W5D | In-Store Customer Delivery Scheduling | [Store Operations Workflows](WF-store-operations.md) |
| W5E | Store Opening Delay Procedure | [Store Operations Workflows](WF-store-operations.md) |
| W5F | Store Closing & End-of-Day | [Store Operations Workflows](WF-store-operations.md) |
| W5G | Offline POS Recovery & Reconciliation | [Store Operations Workflows](WF-store-operations.md) |
| W6 | Cycle Counting & Inventory Accuracy | [Inventory Management Workflows](WF-inventory.md) |
| W7 | Accounts Payable — Vendor Invoice Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W7C | Non-PO / Recurring Expense Invoice Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W7D | AP Vendor Statement Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W8 | Accounts Receivable — Trade & Corporate Accounts | [Finance & Treasury Workflows](WF-finance.md) |
| W9 | Financial Close & Reporting | [Finance & Treasury Workflows](WF-finance.md) |
| W9A | Month-End Close | [Finance & Treasury Workflows](WF-finance.md) |
| W9B | Year-End Close | [Finance & Treasury Workflows](WF-finance.md) |
| W10 | Payroll Processing | [HR & Payroll Workflows](WF-hr.md) |
| W11 | Ecommerce — BOPIS Order Fulfillment | [Ecommerce Workflows](WF-ecommerce.md) |
| W12 | Returns & Exchanges | [Store Operations Workflows](WF-store-operations.md) |
| W12A | In-Store Returns | [Store Operations Workflows](WF-store-operations.md) |
| W12B | Online-Initiated Returns | [Store Operations Workflows](WF-store-operations.md) |
| W12C | Cross-Store Returns (Purchased at Store A, Returned at Store B) | [Store Operations Workflows](WF-store-operations.md) |
| W13 | Promotions & Pricing Execution | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W14 | Intercompany Transactions & Settlement | [Finance & Treasury Workflows](WF-finance.md) |
| W15 | Recruitment & Employee Onboarding | [HR & Payroll Workflows](WF-hr.md) |
| W16 | New Store Opening | [Store Operations Workflows](WF-store-operations.md) |
| W17 | Customer Loyalty Program Operations | [Store Operations Workflows](WF-store-operations.md) |
| W18 | Direct Store Delivery (DSD) Receiving | [Store Operations Workflows](WF-store-operations.md) |
| W18B | DSD Vendor Delivery Scheduling | [Store Operations Workflows](WF-store-operations.md) |
| W19 | Ecommerce — Home Delivery Fulfillment | [Ecommerce Workflows](WF-ecommerce.md) |
| W19B | Ship from Store (Store-Fulfilled Home Delivery) | [Ecommerce Workflows](WF-ecommerce.md) |
| W20 | Vendor Managed Inventory (VMI) | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W21 | Capital Expenditure (Capex) Request & Approval | [Finance & Treasury Workflows](WF-finance.md) |
| W22 | Stock Transfers (Store-to-Store & Inter-DC) | [Inventory Management Workflows](WF-inventory.md) |
| W22A | Store-Level Outbound Transfer Fulfillment | [Inventory Management Workflows](WF-inventory.md) |
| W22B | Store-to-DC Return (Excess / Damaged Inventory) | [Inventory Management Workflows](WF-inventory.md) |
| W23 | Consignment Inventory Operations | [Inventory Management Workflows](WF-inventory.md) |
| W24 | Trade & Corporate Credit Application | [Finance & Treasury Workflows](WF-finance.md) |
| W25 | Petty Cash Management | [Finance & Treasury Workflows](WF-finance.md) |
| W26 | Annual Budget Preparation & Monthly Variance Review | [Finance & Treasury Workflows](WF-finance.md) |
| W27 | Vendor Rebate Accrual & Settlement | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W28 | Gift Card & Store Credit Lifecycle | [Store Operations Workflows](WF-store-operations.md) |
| W29 | Product Recall Execution | [Store Operations Workflows](WF-store-operations.md) |
| W30 | Daily Treasury & Cash Position Management | [Finance & Treasury Workflows](WF-finance.md) |
| W31 | Demand Forecasting Cycle | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W32 | Seasonal Buy Planning | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W33 | Warranty Claim Processing | [Store Operations Workflows](WF-store-operations.md) |
| W34 | Store Shift Scheduling | [HR & Payroll Workflows](WF-hr.md) |
| W35 | Management Reporting Rhythm | [Finance & Treasury Workflows](WF-finance.md) |
| W36 | Vendor Onboarding | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W37 | Loss Prevention & Exception Reporting | [Compliance & Governance Workflows](WF-compliance.md) |
| W38 | Special Order / Non-Stock Item Fulfillment | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W39 | Fixed Asset Disposal & Retirement | [Finance & Treasury Workflows](WF-finance.md) |
| W40 | Regular Price Change Execution | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W41 | Customer Complaint Resolution | [Customer Experience Workflows](WF-customer.md) |
| W42 | Annual Physical Inventory Execution | [Inventory Management Workflows](WF-inventory.md) |
| W43 | Employee Separation & Offboarding | [HR & Payroll Workflows](WF-hr.md) |
| W44 | Vendor Performance Review | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W45 | Store Closure / Relocation | [Store Operations Workflows](WF-store-operations.md) |
| W46 | Kit / Bundle Assembly & Disassembly | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W47 | Store Facility Maintenance & Work Orders | [Store Operations Workflows](WF-store-operations.md) |
| W48 | IT Operations & Helpdesk Support | [IT Operations Workflows](WF-it-operations.md) |
| W49 | Natural Disaster / Typhoon Business Continuity | [Compliance & Governance Workflows](WF-compliance.md) |
| W50 | Product Information Management (PIM) | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W51 | Employee Training & Skills Development | [HR & Payroll Workflows](WF-hr.md) |
| W52 | Fleet Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W53 | Data Privacy Breach Response | [IT Operations Workflows](WF-it-operations.md) |
| W54 | LGU Business Permit Renewal per Location | [Compliance & Governance Workflows](WF-compliance.md) |
| W54A | BIR Computerized Accounting System (CAS) Registration | [Compliance & Governance Workflows](WF-compliance.md) |
| W55 | IT Disaster Recovery & System Failover | [IT Operations Workflows](WF-it-operations.md) |
| W56 | Customer Backorder Management | [Inventory Management Workflows](WF-inventory.md) |
| W57 | Promotional Stock Allocation & Pre-Positioning | [Inventory Management Workflows](WF-inventory.md) |
| W58 | Corporate / Project Account Management | [Customer Experience Workflows](WF-customer.md) |
| W59 | Insurance Policy Lifecycle Management | [Finance & Treasury Workflows](WF-finance.md) |
| W60 | Emergency Procurement | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W61 | Competitor Price Match Process | [Customer Experience Workflows](WF-customer.md) |
| W62 | Vendor Contract Lifecycle (Non-PO Contracts) | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W62B | 3PL / Delivery Partner Onboarding & Offboarding | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W63 | Shelf Label & Price Tag Distribution | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W64 | New Product Pilot / Store Test | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W65 | Customer Satisfaction Measurement | [Customer Experience Workflows](WF-customer.md) |
| W66 | Inter-Island Logistics & Freight Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W67 | Monthly Store Performance Review | [Store Operations Workflows](WF-store-operations.md) |
| W68 | Product Lifecycle & Discontinuation | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W69 | Price Compliance Audit | [Store Operations Workflows](WF-store-operations.md) |
| W70 | Credit Note & Debit Note Aging Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W71 | Store Physical Security & Access Control | [Store Operations Workflows](WF-store-operations.md) |
| W72 | Employee Performance Management | [HR & Payroll Workflows](WF-hr.md) |
| W73 | Data Migration Validation & Parallel-Run Testing | [IT Operations Workflows](WF-it-operations.md) |
| W74 | Employee Expense Reimbursement | [HR & Payroll Workflows](WF-hr.md) |
| W75 | Layaway / Installment Sales | [Store Operations Workflows](WF-store-operations.md) |
| W76 | Employee Loans & Advances | [HR & Payroll Workflows](WF-hr.md) |
| W77 | BIR Tax Audit Response | [Compliance & Governance Workflows](WF-compliance.md) |
| W78 | Government / Institutional Procurement Participation | [Compliance & Governance Workflows](WF-compliance.md) |
| W79 | Employee Grievance & Whistleblower Process | [Compliance & Governance Workflows](WF-compliance.md) |
| W80 | FX Hedging & Forward Contract Management | [Finance & Treasury Workflows](WF-finance.md) |
| W81 | Bad Debt Provisioning, Write-Off & Recovery | [Finance & Treasury Workflows](WF-finance.md) |
| W82 | Hazardous Waste Disposal Tracking & DENR Compliance | [Compliance & Governance Workflows](WF-compliance.md) |
| W83 | Marketing Campaign Planning, Execution & Performance Measurement | [Marketing Campaign Workflows](WF-marketing.md) |
| W84 | Customer Account Reactivation | [Customer Experience Workflows](WF-customer.md) |
| W85 | Product Costing & Margin Analysis Review | [Finance & Treasury Workflows](WF-finance.md) |
| W86 | Planogram Compliance & Store Layout Verification | [Store Operations Workflows](WF-store-operations.md) |
| W87 | Customer Feedback-to-Action Loop | [Customer Experience Workflows](WF-customer.md) |
| W88 | Return to Vendor (RTV) Processing | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W89 | Bank Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W90 | Monthly Tax Filing & Statutory Remittance | [Finance & Treasury Workflows](WF-finance.md) |
| W91 | Damaged & Defective Goods Disposition | [Inventory Management Workflows](WF-inventory.md) |
| W92 | Inventory Adjustment & Shrinkage Authorization | [Inventory Management Workflows](WF-inventory.md) |
| W93 | Markdown & Clearance Pricing Execution | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W94 | Customer Deposit & Advance Payment Management | [Finance & Treasury Workflows](WF-finance.md) |
| W95 | External Audit Coordination & Support | [Compliance & Governance Workflows](WF-compliance.md) |
| W96 | Store Renovation & Remodel Project | [Store Operations Workflows](WF-store-operations.md) |
| W97 | Sample & Demo Inventory Management | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W98 | Ecommerce Order Exception & Cancellation Management | [Ecommerce Workflows](WF-ecommerce.md) |
| W99 | Payment Settlement Reconciliation (Card / E-Wallet / Online) | [Finance & Treasury Workflows](WF-finance.md) |
| W100 | Vendor Statement Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W101 | Customer Refund & Credit Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W102 | Category Performance Review & P&L Ownership | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W103 | Trade Sales Pipeline & Territory Management | [Customer Experience Workflows](WF-customer.md) |
| W104 | Loyalty Program Financial Governance & Periodic Review | [Marketing Campaign Workflows](WF-marketing.md) |
| W105 | Multi-Channel Inventory Allocation & Priority Governance | [Inventory Management Workflows](WF-inventory.md) |
| W106 | DC Outbound Dispatch & Load Planning | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W107 | Pricing Hierarchy Governance & Compliance Audit | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W108 | Customer Credit Collection & Escalation | [Finance & Treasury Workflows](WF-finance.md) |
| W109 | Store-Level Inventory Receiving & Putaway | [Store Operations Workflows](WF-store-operations.md) |
| W110 | Supplier Quality & CAPA (Corrective and Preventive Action) | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W111 | Store Energy & Utility Consumption Management | [Store Operations Workflows](WF-store-operations.md) |
| W112 | Trade Counter / Pro Desk Operations | [Customer Experience Workflows](WF-customer.md) |
| W113 | Business Intelligence & Data Governance | [IT Operations Workflows](WF-it-operations.md) |
| W114 | Sustainability & Environmental Compliance Reporting | [Compliance & Governance Workflows](WF-compliance.md) |
| W115 | Supplier Diversity & MSME Development Program | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W116 | Site Selection & Feasibility Analysis | [Real Estate & Lease Management Workflows](WF-property.md) |
| W117 | Lease Administration & Renewal | [Real Estate & Lease Management Workflows](WF-property.md) |
| W118 | Rent & CAM Payment Processing | [Real Estate & Lease Management Workflows](WF-property.md) |
| W119 | Real Property Tax (Amillaramento) Management | [Real Estate & Lease Management Workflows](WF-property.md) |
| W120 | Internal Audit Planning & Risk Assessment | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W121 | Operational Audit Execution (Store/DC/HQ) | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W122 | Enterprise Risk Management (ERM) Review | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W123 | Fraud Investigation Protocol | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W124 | Corporate Secretarial & Entity Management | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W125 | Legal Case & Litigation Management | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W126 | Intellectual Property (IP) Portfolio Management | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W127 | Annual Strategic Planning & OKRs | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W128 | Enterprise Project Management (EPM) Lifecycle | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W129 | Private Label / In-house Brand Development | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W130 | Competitor Price Intelligence Gathering | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W131 | IT Asset Lifecycle Management | [IT Operations Workflows](WF-it-operations.md) |
| W132 | Software Development & Change Management | [IT Operations Workflows](WF-it-operations.md) |
| W133 | Sales & Operations Planning (S&OP) Cycle | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W134 | Crisis Communication & Brand Reputation Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W135 | CSR Program Execution | [Marketing Campaign Workflows](WF-marketing.md) |
| W136 | Indirect / Non-Merchandise Procurement | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W137 | Intercompany Dividend & Loan Management | [Finance & Treasury Workflows](WF-finance.md) |
| W138 | Home Installation Services Management | [Installation & Value-Added Services](WF-services.md) |
| W139 | Tool & Equipment Rental Operations | [Installation & Value-Added Services](WF-services.md) |
| W140 | Occupational Health & Safety (OHS) Incident Management | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W141 | Workplace Safety Inspection & Audit | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W142 | Social Media & Influencer Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W143 | Public Relations & Corporate Communications | [Marketing Campaign Workflows](WF-marketing.md) |
| W144 | International Logistics & Import Operations | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W145 | Wholesale Reseller Onboarding & Credit Management | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W146 | Bulk Fulfillment & Cross-Docking for Wholesale | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W147 | DIY Workshop & In-Store Event Management | [Installation & Value-Added Services](WF-services.md) |
| W148 | Home Design & Consultancy Services | [Installation & Value-Added Services](WF-services.md) |
| W149 | Bank & Credit Card Partnership Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W150 | Product Quality Testing & Certification | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W151 | Corporate Social Responsibility (CSR) Impact Measurement & Reporting | [Marketing Campaign Workflows](WF-marketing.md) |
| W152 | Employee IT Provisioning & Access Lifecycle Management | [IT Operations Workflows](WF-it-operations.md) |
| W153 | Retail Media Network (RMN) Operations | [Marketing Campaign Workflows](WF-marketing.md) |
| W154 | Proactive Store Inventory Rebalancing (Stock Push) | [Inventory Management Workflows](WF-inventory.md) |
| W155 | Vendor Strategic Collaboration & Joint Business Planning (JBP) | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W156 | Customer Data Platform (CDP) & Hyper-Personalization | [Customer Experience Workflows](WF-customer.md) |
| W157 | E-waste Collection & Circular Economy Operations | [Compliance & Governance Workflows](WF-compliance.md) |
| W158 | Business Continuity Drill & Disaster Recovery Testing | [Compliance & Governance Workflows](WF-compliance.md) |
| W159 | Anti-Bribery & Corruption (ABC) Monitoring & Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W160 | Private Label Factory Audit & Social Compliance | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W161 | Vendor Price Protection & Market Markdown Claims | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W162 | Project Quotation & Bid Management | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W163 | Contract Pricing & Project Price Books | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W164 | Staged Project Delivery & Call-Off Orders | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W165 | Project Retention & Milestone Billing | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W166 | Corporate / Institutional Tendering | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W167 | Store & DC Recycling Program (Circular Economy) | [Compliance & Governance Workflows](WF-compliance.md) |
| W168 | Custom Paint Mixing & Tinting Operations | [Installation & Value-Added Services](WF-services.md) |
| W169 | Lumber & Board Cutting Services | [Installation & Value-Added Services](WF-services.md) |
| W170 | Senior Citizen & PWD Discount Compliance (PH Legal) | [Store Operations Workflows](WF-store-operations.md) |
| W171 | Store Physical Security & Yard Patrol Routine | [Store Operations Workflows](WF-store-operations.md) |
| W172 | Employee PPE & Uniform Lifecycle | [HR & Payroll Workflows](WF-hr.md) |
| W173 | Store-Level Solar Energy Monitoring | [Store Operations Workflows](WF-store-operations.md) |
| W174 | Store-Level Cash-in-Transit (CIT) & Armored Car Management | [Finance & Treasury Workflows](WF-finance.md) |
| W175 | Employee Gratuity & Retirement Fund Management (RA 7641) | [Finance & Treasury Workflows](WF-finance.md) |
| W176 | Store-to-DC Reverse Logistics (Consolidation) | [Store Operations Workflows](WF-store-operations.md) |
| W177 | Vending & Concessionaire Management | [Store Operations Workflows](WF-store-operations.md) |
| W178 | Employee Succession & Internal Mobility | [HR & Payroll Workflows](WF-hr.md) |
| W179 | Management Trainee (Cadetship) Program | [HR & Payroll Workflows](WF-hr.md) |
| W180 | E-commerce Marketplace Integration (Lazada/Shopee) | [Ecommerce Workflows](WF-ecommerce.md) |
| W181 | Store-Level Price Tag Printing & Verification | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W182 | Gift / Home Registry Lifecycle | [Store Operations Workflows](WF-store-operations.md) |
| W183 | Supply Chain Network Optimization Review | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W184 | Fixed Asset Physical Verification (Audit) | [Finance & Treasury Workflows](WF-finance.md) |
| W185 | Product Liability & Consumer Safety Incident Management | [Compliance & Governance Workflows](WF-compliance.md) |
| W186 | Internal SOP & Policy Governance Lifecycle | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W187 | Contractor & Third-Party On-site Safety Orientation | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W188 | Fleet Spare Parts & Preventive Maintenance (PM) Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W189 | Referral Program & Brand Ambassador Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W190 | In-house Design & Creative Production Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W191 | Global Supply Chain — Incoterm & Marine Insurance Tracking | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W192 | Greenhouse Gas (GHG) Emissions Tracking | [ESG & Sustainability Reporting Workflows](WF-esg.md) |
| W193 | Waste Management & Circular Economy | [ESG & Sustainability Reporting Workflows](WF-esg.md) |
| W194 | Social Impact & Community Development (CSR) | [ESG & Sustainability Reporting Workflows](WF-esg.md) |
| W195 | Sustainable Sourcing & Ethical Vendor Audit | [ESG & Sustainability Reporting Workflows](WF-esg.md) |
| W196 | Route Planning & Dispatch Optimization | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W197 | Driver Performance & Safety Management | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W198 | Fuel Management & Consumption Monitoring | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W199 | Fleet Telematics & Real-Time Tracking | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W200 | AI-Driven Personalization & Recommendation Engine | [Innovation & Digital Transformation](WF-innovation.md) |
| W201 | Robotic Process Automation (RPA) Lifecycle | [Innovation & Digital Transformation](WF-innovation.md) |
| W202 | Predictive Maintenance for Industrial Assets | [Innovation & Digital Transformation](WF-innovation.md) |
| W203 | Computer Vision for Inventory & Planogram Audit | [Innovation & Digital Transformation](WF-innovation.md) |
| W204 | Regional Stock Rebalancing & Inter-Store Expedited Transfers | [Inventory Management Workflows](WF-inventory.md) |
| W205 | Employee Purchase Program & Internal Staff Sales | [Store Operations Workflows](WF-store-operations.md) |
| W206 | Mobile POS (mPOS) & Queue-Busting Operations | [Store Operations Workflows](WF-store-operations.md) |
| W207 | Store-Level Security Camera (CCTV) Audit & LP Integration | [Compliance & Governance Workflows](WF-compliance.md) |
| W208 | Retail Analytics & AI-Driven Inventory Optimization | [Innovation & Digital Transformation](WF-innovation.md) |
| W209 | Barangay & Local Community Relationship Management | [Compliance & Governance Workflows](WF-compliance.md) |
| W210 | E-commerce Fulfillment Hub (Dark Store) Operations | [Ecommerce Workflows](WF-ecommerce.md) |
| W211 | In-Store 3D Kitchen/Bathroom Design Rendering | [Installation & Value-Added Services](WF-services.md) |
| W212 | Automated Store Cash Management & Smart Safe Integration | [Store Operations Workflows](WF-store-operations.md) |
| W213 | Installation Service Partner Quality Audit | [Installation & Value-Added Services](WF-services.md) |
| W214 | Store-to-Store Expedited Transfers (Customer-Initiated) | [Inventory Management Workflows](WF-inventory.md) |
| W215 | Customer Home Delivery Reverse Logistics (Returns) | [Ecommerce Workflows](WF-ecommerce.md) |
| W216 | BIR CAS (Computerized Accounting System) Compliance Audit | [Compliance & Governance Workflows](WF-compliance.md) |
| W217 | Senior Citizen & PWD VAT-Exemption Audit & Reporting | [Finance & Treasury Workflows](WF-finance.md) |
| W218 | Inter-DC Stock Rebalancing (Stock Push) | [Inventory Management Workflows](WF-inventory.md) |
| W219 | Store Inventory Quarantine & Recertification | [Inventory Management Workflows](WF-inventory.md) |
| W220 | Slow-Moving & Obsolete Inventory (SLOB) Provisioning & Liquidation | [Inventory Management Workflows](WF-inventory.md) |
| W221 | Cross-Docking Operations for Fast-Moving Bulky Items | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W222 | DC Container Yard & Chassis Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W223 | New Store Design & Engineering Standards | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W224 | Construction Bidding & Contractor Selection | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W225 | Store Construction Management & Supervision | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W226 | Store Renovation & Retrofitting (CAPEX) | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W227 | Commissioning & Operational Handover | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W228 | Sales Commission Calculation (Trade & Project Sales) | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W229 | B2B Customer Credit Limit Exception & Escalation | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W230 | Legal Contract Review & Approval | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W231 | Management Performance Reporting (QBR) | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W232 | Letter of Credit (LC) & Bank Guarantee Lifecycle | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W233 | Cash Flow Forecasting & Liquidity Management | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W234 | Intercompany Profit Elimination & Consolidation | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W235 | Transfer Pricing Compliance & Documentation | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W236 | Hazmat Storage & Segregation Compliance (DC) | [Hazardous Materials (Hazmat) & Compliance](WF-hazmat.md) |
| W237 | Hazmat Handling & Safety Training (Store) | [Hazardous Materials (Hazmat) & Compliance](WF-hazmat.md) |
| W238 | Hazmat Spill Response & Incident Management | [Hazardous Materials (Hazmat) & Compliance](WF-hazmat.md) |
| W239 | Customs Duty & Tax Reconciliation (BOC) | [Hazardous Materials (Hazmat) & Compliance](WF-hazmat.md) |
| W240 | DC Facility & Warehouse Equipment Maintenance | [Facility & Asset Maintenance (HQ & DC)](WF-non-store-maintenance.md) |
| W241 | HQ Office Facility & Executive Asset Maintenance | [Facility & Asset Maintenance (HQ & DC)](WF-non-store-maintenance.md) |
| W242 | 3PL & Logistics Partner Performance Review | [Facility & Asset Maintenance (HQ & DC)](WF-non-store-maintenance.md) |
| W243 | Power of Attorney (POA) & Board Resolution Lifecycle | [Facility & Asset Maintenance (HQ & DC)](WF-non-store-maintenance.md) |
| W244 | Vendor Invoice Dispute & Discrepancy Resolution | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W245 | Vendor Performance Chargebacks & Penalties Management | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W246 | Drop-Ship Vendor (DSV) Order Fulfillment | [Ecommerce Workflows](WF-ecommerce.md) |
| W247 | BOPIS Smart Locker & Queue Management | [Ecommerce Workflows](WF-ecommerce.md) |
| W248 | Store Inventory Variance & LP Investigation | [Store Operations Workflows](WF-store-operations.md) |
| W249 | Import Port Demurrage & Detention Management | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W250 | Supply Chain Control Tower & Real-Time Shipment Visibility | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W251 | Philippine Statutory Benefits & Claims Administration (SSS, PhilHealth, Pag-IBIG) | [HR & Payroll Workflows](WF-hr.md) |
| W252 | Centralized Item Master Creation & Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W253 | Customer Master Data Governance & Deduplication | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W254 | Location Master Lifecycle & Hierarchy Management | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W287 | Vendor Master Data Governance & Deduplication | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W288 | Financial Master Data Governance (COA & Cost Centers) | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W289 | Pricing Master Governance (Base Prices & Matrices) | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W290 | Hierarchical Category Structure Management | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W291 | Master Data Quality Monitoring & Reporting | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W255 | Electronic Document Storage & Retrieval (ERP-wide) | [Document Management (DOC) Workflows](WF-document-management.md) |
| W256 | Enterprise Document Retention & Archiving Policy | [Document Management (DOC) Workflows](WF-document-management.md) |
| W257 | Enterprise API & Systems Integration Lifecycle Management | [IT Operations Workflows](WF-it-operations.md) |
| W258 | Omni-channel Customer Ticketing & Support Management | [Customer Experience Workflows](WF-customer.md) |
| W259 | Call Center Daily Operations & Queue Management | [Customer Experience Workflows](WF-customer.md) |
| W260 | BIR eFPS Filing & Electronic Payment Submission | [Finance & Treasury Workflows](WF-finance.md) |
| W261 | E-Wallet & Digital Payment Settlement Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W262 | Store Promotional Setup & Visual Merchandising Execution | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W263 | Loyalty Member Enrollment & Onboarding Journey | [Customer Experience Workflows](WF-customer.md) |
| W264 | Seasonal Merchandise Transition & Display Rotation | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W265 | POS Terminal Hardware Maintenance & Peripheral Management | [IT Operations Workflows](WF-it-operations.md) |
| W266 | Ecommerce Online Fraud Detection & Prevention | [Ecommerce Workflows](WF-ecommerce.md) |
| W267 | Ecommerce Digital Payment Reconciliation & Dispute Handling | [Ecommerce Workflows](WF-ecommerce.md) |
| W268 | Last-Mile Home Delivery Tracking & Proof-of-Delivery | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W269 | Vendor Promodizer & Third-Party Staff Management | [HR & Payroll Workflows](WF-hr.md) |
| W270 | Pallet & Returnable Transport Packaging (RTP) Tracking | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W271 | Data Subject Access & Deletion Requests (DPA Compliance) | [Compliance & Governance Workflows](WF-compliance.md) |
| W272 | Cashier Over/Short Dispute & Deduction Resolution | [Store Operations Workflows](WF-store-operations.md) |
| W273 | In-Store Endless Aisle & Vendor Direct-to-Customer Delivery | [Store Operations Workflows](WF-store-operations.md) |
| W274 | Third-Party Customer Financing / Equipment Leasing | [Store Operations Workflows](WF-store-operations.md) |
| W275 | IFRS 16 / PFRS 16 Lease Accounting & Modifications | [Real Estate & Lease Management Workflows](WF-property.md) |
| W276 | Asset Under Construction (AUC) & Mass Capitalization | [Finance & Treasury Workflows](WF-finance.md) |
| W277 | Freight Bill Audit & Payment (FBAP) Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W278 | Mid-Day Cash Skimming / Till Sweeps | [Store Operations Workflows](WF-store-operations.md) |
| W279 | Product Substitution Rules & Governance | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W280 | Court-Ordered Wage Garnishment & Third-Party Deductions | [HR & Payroll Workflows](WF-hr.md) |
| W281 | Self-Checkout (SCO) Exception & Intervention Management | [Store Operations Workflows](WF-store-operations.md) |
| W282 | Subscription Billing for Recurring Home Services | [Installation & Value-Added Services](WF-services.md) |
| W283 | B2B Punchout Catalog Integration (cXML) | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W284 | Customs Bonded Warehouse (CBW) Operations & Duty Deferral | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W285 | Public Liability & Customer Incident Claims Management | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W286 | Retail Media Network (RMN) Vendor Billing & Yield Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W292 | Employee Master Data Governance & Cross-Entity Lifecycle | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W293 | Tax & Regulatory Master Data Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W294 | Unit of Measure (UOM) Master & Conversion Management | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W295 | Payment Terms & Settlement Rule Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W296 | Service & Non-Stock Item Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W297 | Warehouse Location & Bin Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W298 | Product Attribute Template Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W299 | Assortment & Store Cluster Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W300 | Promotional Rule & Campaign Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W301 | Reason Code & Disposition Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W302 | Kit/BOM & Bundle Structure Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W303 | Manufacturer/Brand Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W304 | Routing, Carrier & Transit Time Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W305 | Intercompany Transfer Pricing Rule Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W306 | Seasonal Calendar & Event Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W307 | Currency & Exchange Rate Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W308 | Fiscal Calendar & Posting Period Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W309 | Bank & Banking Partner Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W310 | Address & Geographic Hierarchy Master Governance (Philippine-Specific) | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W311 | Barcode, GTIN & Item Identification Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W312 | Replenishment & Planning Parameter Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W313 | Loyalty Program Configuration & Rule Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W314 | Planogram Template & Space Planning Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W315 | Product Lifecycle Status & Transition Rule Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W316 | Digital Asset & Product Content Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W399 | Fixed Asset Master Data Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W400 | Equipment & Asset Maintenance (EAM) Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W401 | Fleet & Vehicle Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W402 | Contract & Agreement Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W403 | Competitor & Market Intelligence Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W404 | Point-of-Sale (POS) System & Hardware Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W405 | Data Privacy & Consent Preferences Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W406 | ESG & Sustainability Metrics Master Governance | [Master Data Management (MDM) Workflows](WF-master-data.md) |
| W317 | Bank Account Lifecycle & Signatory Management | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W318 | Short-Term Investment & Surplus Cash Placement | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W319 | Debt Facility & Covenant Compliance Management | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W320 | Electronic Banking Security & Payment Control | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W321 | FX Exposure Analysis & BSP Regulatory Reporting | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W322 | Treasury Policy, Governance & Risk Appetite Framework | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W323 | Cash Concentration & Inter-Entity Pooling Operations | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W324 | Supply Chain Finance & Dynamic Discounting Program | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W325 | Corporate Guarantee & Contingent Liability Management | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W326 | Treasury Month-End Close & Reconciliation | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W327 | External Shareholder Dividend Declaration & Payment | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W328 | Customer Credit Limit Periodic Review | [Customer Experience Workflows](WF-customer.md) |
| W329 | Competitive Price Tactical Response | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W330 | In-Store Emergency Response Protocol | [Store Operations Workflows](WF-store-operations.md) |
| W331 | IT General Controls (ITGC) & Cybersecurity Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W332 | Continuous Control Monitoring (CCM) & Exception Management | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W333 | Audit Issue Remediation & CAP Tracking | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W334 | Third-Party Vendor Risk & Compliance Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W335 | Major Capex & Post-Implementation Project Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W336 | Quality Assurance & Improvement Program (QAIP) | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W337 | Payroll & Statutory Compliance Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W338 | Segregation of Duties (SOD) Review & Remediation | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W339 | Regulatory Compliance Audit (DPA, Labor, Consumer Act) | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W340 | Unannounced Store Cash & Vault Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W341 | ESG Assurance & Sustainability Compliance Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W342 | Inventory Observation & Cycle Count Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W343 | Lease & CAM (Common Area Maintenance) Compliance Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W344 | Trade Promotion, Rebate & Marketing Spend Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W345 | Logistics, Fleet & Fuel Management Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W346 | Capex Construction & Store Build-out Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W347 | E-commerce & Omni-channel Operations Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W348 | Revenue Assurance & Payment Gateway Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W349 | Corporate Tax & Statutory Reporting Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W350 | BC/DR Readiness & Crisis Management Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W351 | External Audit Coordination & Statutory Filing Support | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W352 | Fixed Asset Verification & Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W353 | Ethical Sourcing & Social Compliance Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W354 | AML & Sanctions Screening (Wholesale/B2B) Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W355 | Intellectual Property (IP) & Brand Protection Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W356 | Whistleblower System & Non-Retaliation Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W357 | Board Governance & MCG Compliance Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W358 | Physical Security, CCTV & Guard Force Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W359 | AI Governance, Algorithmic Bias & Data Ethics Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W360 | Crisis Response & Incident Management Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W361 | Corporate Treasury, Cash Management & Investment Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W362 | Master Data Governance & Data Quality Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W363 | Insurance Program & Claims Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W364 | Marketing Agency & Media Spend Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W365 | Strategic Workforce Planning & Succession Audit | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W366 | Network Infrastructure & Connectivity Management | [IT Operations Workflows](WF-it-operations.md) |
| W367 | Cybersecurity Operations & Vulnerability Management | [IT Operations Workflows](WF-it-operations.md) |
| W368 | Database & Cloud Infrastructure Management | [IT Operations Workflows](WF-it-operations.md) |
| W369 | IT Vendor SLA Governance & Performance Management | [IT Operations Workflows](WF-it-operations.md) |
| W370 | Software License & SaaS Subscription Management | [IT Operations Workflows](WF-it-operations.md) |
| W371 | Mobile Device Management (MDM) Operations | [IT Operations Workflows](WF-it-operations.md) |
| W372 | IT Policy, Security Awareness & User Training | [IT Operations Workflows](WF-it-operations.md) |
| W373 | IT FinOps & Cloud Cost Management | [IT Operations Workflows](WF-it-operations.md) |
| W374 | IT Project Intake & Demand Management | [IT Operations Workflows](WF-it-operations.md) |
| W375 | Privileged Access Management (PAM) Operations | [IT Operations Workflows](WF-it-operations.md) |
| W376 | IT Capacity & Performance Planning | [IT Operations Workflows](WF-it-operations.md) |
| W377 | Domain, SSL & Digital Certificate Management | [IT Operations Workflows](WF-it-operations.md) |
| W378 | IT Problem Management & Root Cause Analysis | [IT Operations Workflows](WF-it-operations.md) |
| W379 | IT Service Request Fulfillment & Service Catalog | [IT Operations Workflows](WF-it-operations.md) |
| W380 | IT Alert & Event Management | [IT Operations Workflows](WF-it-operations.md) |
| W381 | IT Knowledge Management | [IT Operations Workflows](WF-it-operations.md) |
| W382 | IT Backup & Recovery Operations | [IT Operations Workflows](WF-it-operations.md) |
| W383 | IT Security Incident Response (General) | [IT Operations Workflows](WF-it-operations.md) |
| W384 | ERP Environment Management & Data Masking | [IT Operations Workflows](WF-it-operations.md) |
| W385 | Data Cleansing & Migration Operational Lifecycle | [IT Operations Workflows](WF-it-operations.md) |
| W386 | IT Strategy & Annual Roadmap Development | [IT Operations Workflows](WF-it-operations.md) |
| W387 | IT Compliance & Control Self-Assessment (CSA) | [IT Operations Workflows](WF-it-operations.md) |
| W388 | Shadow IT Discovery & Governance | [IT Operations Workflows](WF-it-operations.md) |
| W389 | Data Privacy Impact Assessment (DPIA) Lifecycle | [IT Operations Workflows](WF-it-operations.md) |
| W390 | IT Service Continuity & BIA Refresh | [IT Operations Workflows](WF-it-operations.md) |
| W391 | Software Quality Assurance (QA) & Testing Lifecycle | [IT Operations Workflows](WF-it-operations.md) |
| W392 | IT Service Level Management (SLM) & BRM | [IT Operations Workflows](WF-it-operations.md) |
| W393 | Remote Access, VPN & Zero Trust Connectivity Management | [IT Operations Workflows](WF-it-operations.md) |
| W394 | IT Technical Skills, Training & Certification Lifecycle | [IT Operations Workflows](WF-it-operations.md) |
| W395 | Mobile App Store Management (Public & Enterprise) | [IT Operations Workflows](WF-it-operations.md) |
| W396 | ERP Data Archiving & Database Tiering Execution | [IT Operations Workflows](WF-it-operations.md) |
| W397 | Cyber Threat Intelligence & Proactive Threat Hunting | [IT Operations Workflows](WF-it-operations.md) |
| W398 | IT Innovation, Emerging Tech & PoC Lifecycle | [IT Operations Workflows](WF-it-operations.md) |
| W420 | AI Shelf Monitoring & Real-time Replenishment Alerting | [Store Operations Workflows](WF-store-operations.md) |
| W421 | Batch/Shade Reconciliation for Large Project Sales | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W422 | VMI Collaborative Data Sharing & Replenishment Execution | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W423 | AR Post-dated Check (PDC) Warehousing & Clearing | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W424 | AP Post-dated Check (PDC) Issuance & Monitoring | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W425 | Bounced Check (DAIF/DAUD) Recovery & Penalty | [Treasury & Corporate Finance Workflows](WF-treasury.md) |
| W426 | Annual Conflict of Interest (COI) & Gift Policy Disclosure | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W427 | DTI Sales Promotion Permit Monitoring | [Compliance & Governance Workflows](WF-compliance.md) |
| W428 | Community Disaster Relief & Emergency Response | [Store Operations Workflows](WF-store-operations.md) |
| W429 | Vendor-Funded Promodizer Incentive Management | [HR & Payroll Workflows](WF-hr.md) |
| W430 | LGU Business Permit & "Amillaramento" (RPT) On-Site Inspection | [Real Estate & Lease Management Workflows](WF-property.md) |
| W431 | LGU-Specific "Truck Ban" & Route Governance | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W432 | Solo Parent Discount Compliance (RA 11861) | [Store Operations Workflows](WF-store-operations.md) |
| W433 | DENR Self-Monitoring (SMR) & Compliance (CMR) Reporting | [Compliance & Governance Workflows](WF-compliance.md) |
| W434 | NPC Annual DPO & System Registration | [IT Operations Workflows](WF-it-operations.md) |
| W435 | Intercompany Service Level Agreement (SLA) Fee Billing | [Finance & Treasury Workflows](WF-finance.md) |
| W436 | DOLE Annual OHS Compliance Reporting (WAIR/AMR) | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W437 | Regulatory Branch De-registration & Permit Cancellation | [Compliance & Governance Workflows](WF-compliance.md) |
| W438 | Yard Dispatch & Customer Vehicle Loading Operations | [Store Operations Workflows](WF-store-operations.md) |
| W439 | In-Store Bulk-to-Retail Repackaging Operations | [Inventory Management Workflows](WF-inventory.md) |
| W440 | Power Tool Service & Repair Center Operations | [Installation & Value-Added Services](WF-services.md) |
| W441 | Corporate Staff Housing & Billeting Management | [Real Estate & Lease Management Workflows](WF-property.md) |
| W442 | Site Technical Survey & Measurement Services | [Installation & Value-Added Services](WF-services.md) |
| W443 | Salvage & Scrap Material Disposition (Waste-to-Cash) | [ESG & Sustainability Reporting Workflows](WF-esg.md) |
| W444 | Community Solicitation & Donation Processing | [Compliance & Governance Workflows](WF-compliance.md) |
| W445 | Display & Demo Infrastructure Maintenance | [Store Operations Workflows](WF-store-operations.md) |
| W446 | Temporary LGU Permits for Outdoor Sales & Events | [Compliance & Governance Workflows](WF-compliance.md) |
| W447 | DTI-BPS Mandatory Product Certification (ICC/SOC) | [Regulatory Permits & Local Government Compliance](WF-regulatory-permits.md) |
| W448 | LGU Sanitary & Health Permit Management | [Regulatory Permits & Local Government Compliance](WF-regulatory-permits.md) |
| W449 | Promodizer Labor Compliance & DOLE 174 Governance | [HR & Payroll Workflows](WF-hr.md) |
| W460 | Corporate & Trade Account Onboarding | [Finance & Treasury Workflows](WF-finance.md) |
| W461 | Intercompany Fulfillment & Logistics Fee Settlement | [Finance & Treasury Workflows](WF-finance.md) |
| W463 | Catch-Weight & Cut-to-Length Processing | [Store Operations Workflows](WF-store-operations.md) |
| W464 | In-House Customs Brokerage & Port Operations | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W465 | Network-Wide Disaster Recovery & BCP | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W466 | Loss Prevention & Asset Protection (LPAP) | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W467 | Specialized Hardware Permits (DENR, FPA) | [Regulatory Permits & Local Government Compliance](WF-regulatory-permits.md) |
| W468 | DTI Price Freeze / Emergency Price Control Implementation (RA 7581) | [Compliance & Governance Workflows](WF-compliance.md) |
| W469 | Customer Complaint DTI Escalation & Consumer Adjudication Management | [Compliance & Governance Workflows](WF-compliance.md) |
| W470 | Store-Level Rotational Brownout / Power Outage Management Protocol | [Store Operations Workflows](WF-store-operations.md) |
| W471 | Store-Level Security Incident & Police/Barangay Reporting Protocol | [Store Operations Workflows](WF-store-operations.md) |
| W472 | BOI/PEZA/LGU Tax Incentive Monitoring & Compliance | [Finance & Treasury Workflows](WF-finance.md) |
| W473 | BIR Electronic Invoicing System (EIS) API Transmission & Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W474 | Enterprise Data Governance Council Operations | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W475 | Customer Creditable Withholding Tax (CWT) Certificate (BIR 2307) Collection & Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W476 | LGU / BFP Fire Safety Inspection Certificate (FSIC) Management | [Regulatory Permits & Local Government Compliance](WF-regulatory-permits.md) |
| W477 | DENR Permit to Operate (PTO) & Wastewater Discharge Permit (WDP) Compliance | [Regulatory Permits & Local Government Compliance](WF-regulatory-permits.md) |
| W478 | BIR Annual Inventory List Submission (RMC 57-2015) | [Finance & Treasury Workflows](WF-finance.md) |
| W479 | FDA License to Operate (LTO) for Household Hazardous Substances Compliance | [Regulatory Permits & Local Government Compliance](WF-regulatory-permits.md) |
| W480 | CAAP Height Clearance Permit Compliance | [Regulatory Permits & Local Government Compliance](WF-regulatory-permits.md) |
| W481 | SEC Reportorial Requirements Compliance (GIS, AFS, GAN, MC 28) | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W482 | Annual Stockholders' Meeting (ASHM) Management | [Corporate Governance, Legal & Strategy Workflows](WF-governance.md) |
| W483 | DOLE Drug-Free Workplace Program Compliance | [Compliance & Governance Workflows](WF-compliance.md) |
| W484 | Pandemic/Epidemic Business Response Protocol | [Compliance & Governance Workflows](WF-compliance.md) |
| W485 | BIR Branch Registration & RDO Transfer Management | [Regulatory Permits & Local Government Compliance](WF-regulatory-permits.md) |
| W486 | Related Party Transaction Disclosure & Reporting (PAS 24) | [Finance & Treasury Workflows](WF-finance.md) |
| W487 | Revenue Recognition Review (PFRS 15 Complex Scenarios) | [Finance & Treasury Workflows](WF-finance.md) |
| W488 | Credit Card Chargeback Dispute Management | [Finance & Treasury Workflows](WF-finance.md) |
| W489 | Store-Level Operating Budget & Cost Control | [Finance & Treasury Workflows](WF-finance.md) |
| W490 | Organized Retail Crime (ORC) Investigation & Task Force | [Internal Audit & Risk Management Workflows](WF-audit.md) |
| W491 | Supplier Financial Health & Credit Risk Monitoring | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W492 | Temperature-Controlled & Sensitive Goods Logistics | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W493 | Labor Union & Collective Bargaining Management | [HR & Payroll Workflows](WF-hr.md) |
| W494 | Employee Wellness & Mental Health Program Management | [HR & Payroll Workflows](WF-hr.md) |
| W495 | ERP Patch, Upgrade & Release Management | [IT Operations Workflows](WF-it-operations.md) |
| W496 | Customer Loyalty Fraud Detection & Prevention | [Marketing Campaign Workflows](WF-marketing.md) |
| W497 | PWD Accessibility Compliance & Store Facilities Audit | [Store Operations Workflows](WF-store-operations.md) |
| W498 | Vendor Advance Payment & Prepayment Management | [Finance & Treasury Workflows](WF-finance.md) |
| W499 | BIR Percentage Tax Computation & Payment | [Finance & Treasury Workflows](WF-finance.md) |
| W500 | Transfer Order In-Transit Damage Claim & Resolution | [Finance & Treasury Workflows](WF-finance.md) |
| W501 | Store-Level First Aid & Medical Emergency Response | [Store Operations Workflows](WF-store-operations.md) |
| W502 | Store-Level Non-Hazardous Waste Management | [Store Operations Workflows](WF-store-operations.md) |
| W503 | Store-Level Pest Control & Sanitation Management | [Store Operations Workflows](WF-store-operations.md) |
| W504 | Store-Level Digital Signage & Content Management | [Store Operations Workflows](WF-store-operations.md) |
| W505 | DOLE Labor Inspection Response Protocol | [Compliance & Governance Workflows](WF-compliance.md) |
| W506 | Unified Regulatory Compliance Calendar & Dashboard | [Compliance & Governance Workflows](WF-compliance.md) |
| W507 | Customer Complaint Root Cause Analysis & Systemic Improvement | [Customer Experience Workflows](WF-customer.md) |
| W508 | Customer Account Maintenance & B2B Information Update | [Customer Experience Workflows](WF-customer.md) |
| W509 | Ecommerce Product Return Inspection, Grading & Disposition | [Ecommerce Workflows](WF-ecommerce.md) |
| W510 | Ecommerce Product Review & Rating Management | [Ecommerce Workflows](WF-ecommerce.md) |
| W511 | Employee Cross-Entity & Cross-Location Transfer Processing | [HR & Payroll Workflows](WF-hr.md) |
| W512 | Store-Level Health & Safety Committee Operations | [HR & Payroll Workflows](WF-hr.md) |
| W513 | Vendor-Funded Promotional Activity & Co-op Advertising Management | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W514 | Inventory Count Reconciliation & Variance Root Cause Analysis | [Inventory Management Workflows](WF-inventory.md) |
| W515 | Loyalty Tier Re-evaluation & Migration Processing | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W516 | Self-Checkout (SCO) Daily Operations | [Store Operations Workflows](WF-store-operations.md) |
| W517 | POS Cashier Shift Handover & Drawer Accountability | [Store Operations Workflows](WF-store-operations.md) |
| W518 | Cashier Onboarding, POS Training & Competency Certification | [Store Operations Workflows](WF-store-operations.md) |
| W519 | POS Suspicious Transaction & AML Compliance Reporting | [Store Operations Workflows](WF-store-operations.md) |
| W520 | Age-Restricted Product Verification & Compliance at POS | [Store Operations Workflows](WF-store-operations.md) |
| W521 | POS Transaction Suspend, Park & Recall | [Store Operations Workflows](WF-store-operations.md) |
| W522 | POS Daily Transaction Review & Cashier Performance Audit | [Store Operations Workflows](WF-store-operations.md) |
| W523 | POS Promotional Terminal Setup & Pre-Live Verification | [Store Operations Workflows](WF-store-operations.md) |
| W524 | Demo / Display Unit Selling at POS | [Store Operations Workflows](WF-store-operations.md) |
| W525 | POS Continuous Near-Real-Time Sync & Nightly Reconciliation | [Store Operations Workflows](WF-store-operations.md) |
| W526 | POS Customer Queue Management & Express Lane Operations | [Store Operations Workflows](WF-store-operations.md) |
| W527 | POS Tax Exemption Processing (Government / PEZA / Institutional) | [Store Operations Workflows](WF-store-operations.md) |
| W528 | POS Digital Receipt / E-Receipt Delivery | [Store Operations Workflows](WF-store-operations.md) |
| W529 | POS Void & Refund Tiered Authorization | [Store Operations Workflows](WF-store-operations.md) |
| W530 | POS High-Value Transaction Documentation & Customer ID | [Store Operations Workflows](WF-store-operations.md) |
| W531 | POS Bagging, Carry-Out & Bag Fee Compliance | [Store Operations Workflows](WF-store-operations.md) |
| W532 | POS Clearance & "Final Sale" Item Processing | [Store Operations Workflows](WF-store-operations.md) |
| W533 | POS Real-Time Event Streaming & Continuous Sync | [Store Operations Workflows](WF-store-operations.md) |
| W534 | Multi-Origin / Mixed-Basket Fulfillment Orchestration | [Store Operations Workflows](WF-store-operations.md) |
| W535 | POS Offline Capability Scope & Local Operations | [Store Operations Workflows](WF-store-operations.md) |
| W536 | Unified Order Management & Cross-Channel Fulfillment Routing | [Store Operations Workflows](WF-store-operations.md) |
| W537 | POS Card Terminal & Acquirer Settlement Operations | [Store Operations Workflows](WF-store-operations.md) |
| W538 | POS Real-Time Loss Prevention Exception Monitoring & Alert Response | [Store Operations Workflows](WF-store-operations.md) |
| W539 | POS Promotional Coupon, Voucher & Manufacturer Coupon Processing | [Store Operations Workflows](WF-store-operations.md) |
| W540 | POS BIR Invoice Reprint, Adjustment & Credit Note Issuance | [Store Operations Workflows](WF-store-operations.md) |
| W541 | POS Cash Office Operations & Bank Deposit Preparation | [Store Operations Workflows](WF-store-operations.md) |
| W542 | POS Quotation & Estimate Generation with Sales Conversion | [Store Operations Workflows](WF-store-operations.md) |
| W543 | POS Consignment Sell-Through Transaction Processing & Vendor Settlement Trigger | [Store Operations Workflows](WF-store-operations.md) |
| W544 | POS Service Work Order Creation & Scheduling | [Store Operations Workflows](WF-store-operations.md) |
| W545 | POS Special Order & Customer Order Processing | [Store Operations Workflows](WF-store-operations.md) |
| W546 | POS Deposit & Progress Payment Collection for Project Orders | [Store Operations Workflows](WF-store-operations.md) |
| W547 | POS Scan & Go / Mobile Self-Scan Checkout | [Store Operations Workflows](WF-store-operations.md) |
| W548 | POS Third-Party On-Demand Delivery Integration | [Store Operations Workflows](WF-store-operations.md) |
| W549 | POS Damaged & Open-Box Item Discount Processing | [Store Operations Workflows](WF-store-operations.md) |
| W550 | POS Loyalty Points as Payment Tender | [Store Operations Workflows](WF-store-operations.md) |
| W551 | POS Customer On-the-Spot Loyalty Enrollment & Account Lookup | [Store Operations Workflows](WF-store-operations.md) |
| W552 | POS Donation & Charity Round-Up Processing | [Store Operations Workflows](WF-store-operations.md) |
| W553 | POS Pricing Error Detection & Immediate Correction at Checkout | [Store Operations Workflows](WF-store-operations.md) |
| W554 | Store-Level Daily Shelf Replenishment & Restocking | [Store Operations Workflows](WF-store-operations.md) |
| W555 | Seasonal & Temporary Staffing Process | [HR & Payroll Workflows](WF-hr.md) |
| W556 | AP Payment Run & Batch Processing Execution | [Finance & Treasury Workflows](WF-finance.md) |
| W557 | E-Commerce Abandoned Cart Recovery & Retargeting | [Ecommerce Workflows](WF-ecommerce.md) |
| W558 | Supplier Risk Assessment & Supply Disruption Contingency Planning | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W559 | Store-Level Non-Emergency Incident & Hazard Reporting | [Store Operations Workflows](WF-store-operations.md) |
| W560 | Customer Account Dormancy Identification & Deactivation | [Customer Experience Workflows](WF-customer.md) |
| W561 | Employee Attendance Exception Management | [HR & Payroll Workflows](WF-hr.md) |
| W562 | Store-Level Loss Prevention Daily Routine | [Store Operations Workflows](WF-store-operations.md) |
| W563 | E-Commerce SEO & Digital Merchandising Management | [Ecommerce Workflows](WF-ecommerce.md) |
| W564 | New Product Introduction (NPI) & Full Store Rollout | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W565 | Marketing Campaign ROI & Attribution Analysis | [Marketing Campaign Workflows](WF-marketing.md) |
| W566 | Mystery Shopping Program & CX Compliance Audit | [Customer Experience Workflows](WF-customer.md) |
| W567 | Employee Cross-Training & Skill Matrix Management | [HR & Payroll Workflows](WF-hr.md) |
| W568 | E-Commerce Flash Sale & Limited-Time Offer Operations | [Ecommerce Workflows](WF-ecommerce.md) |
| W569 | E-Commerce New Product Launch & Go-Live Process | [Ecommerce Workflows](WF-ecommerce.md) |
| W570 | Loyalty Points Expiry Management & Annual Liability Cleanup | [Marketing Campaign Workflows](WF-marketing.md) |
| W571 | Store-Level Daily Communication & Memo Acknowledgment | [Store Operations Workflows](WF-store-operations.md) |
| W572 | Customer Credit Monitoring & Automated Alert Management | [Finance & Treasury Workflows](WF-finance.md) |
| W573 | Store-Level Daily Planogram Execution & Shelf Compliance Check | [Store Operations Workflows](WF-store-operations.md) |
| W574 | Store-Level Daily Closing Procedure | [Store Operations Workflows](WF-store-operations.md) |
| W575 | Store-Level Weekly Sales & Operations Review | [Store Operations Workflows](WF-store-operations.md) |
| W576 | Store-Level Typhoon & Severe Weather Preparedness Protocol | [Store Operations Workflows](WF-store-operations.md) |
| W577 | Store-Level Holiday Season (Ber Months) Operational Ramp-Up | [Store Operations Workflows](WF-store-operations.md) |
| W578 | Store-Level Payday Weekend & Peak Day Operational Readiness | [Store Operations Workflows](WF-store-operations.md) |
| W579 | Store-Level Daily Equipment & Specialized Fixture Safety Check | [Store Operations Workflows](WF-store-operations.md) |
| W580 | Store-Level Emergency Manual Operations Protocol (Total System/Power Failure) | [Store Operations Workflows](WF-store-operations.md) |
| W581 | Store-Level Vendor Representative Access & Activity Management | [Store Operations Workflows](WF-store-operations.md) |
| W582 | Store-Level Fire Drill Execution & Documentation | [Store Operations Workflows](WF-store-operations.md) |
| W583 | Store-Level Seasonal Promotional Transition & Display Reset | [Store Operations Workflows](WF-store-operations.md) |
| W584 | DC Daily Operations & Shift Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W585 | DC Dock Scheduling & Appointment Management | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W586 | DC Daily KPI Dashboard & Performance Tracking | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W587 | Inventory Obsolescence Identification & Write-Off Management | [Inventory Management Workflows](WF-inventory.md) |
| W588 | Seasonal Inventory Build-Down & Transition Execution | [Inventory Management Workflows](WF-inventory.md) |
| W589 | Weekly Cash Flow Forecast & Treasury Planning | [Finance & Treasury Workflows](WF-finance.md) |
| W590 | Monthly Tax Provision & Compliance Review | [Finance & Treasury Workflows](WF-finance.md) |
| W591 | E-Commerce Fulfillment SLA Monitoring & Exception Escalation | [Ecommerce Workflows](WF-ecommerce.md) |
| W592 | E-Commerce Customer Delivery Tracking & Proof of Delivery Management | [Ecommerce Workflows](WF-ecommerce.md) |
| W593 | Vendor Portal Content Management & Self-Service Operations | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W594 | Store-Level Employee Daily Attendance Verification & Exception Processing | [HR & Payroll Workflows](WF-hr.md) |
| W595 | ERP System Daily Health Check & Integration Monitoring | [IT Operations Workflows](WF-it-operations.md) |
| W596 | Store-Level Replenishment Exception Management & Auto-Override | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W597 | Customer Complaint Escalation Matrix & Resolution SLA Tracking | [Customer Experience Workflows](WF-customer.md) |
| W598 | Wholesale Pricing & Quotation Management | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W599 | Wholesale Returns, Credit & Adjustment Processing | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W600 | Service Contractor Accreditation & Onboarding Management | [Installation & Value-Added Services Workflows](WF-services.md) |
| W601 | Store-Level Daily HR Operations & People Management | [Store Operations Workflows](WF-store-operations.md) |
| W602 | Store-Level Labor Cost Monitoring & Overtime Budget Control | [Store Operations Workflows](WF-store-operations.md) |
| W603 | Store-Level Employee Disciplinary Process & DOLE Due Process Compliance | [Store Operations Workflows](WF-store-operations.md) |
| W604 | Store-Level Customer Experience Standards & Daily Service Operations | [Store Operations Workflows](WF-store-operations.md) |
| W605 | Return Fraud Detection & Serial Returner Management | [Store Operations Workflows](WF-store-operations.md) |
| W606 | Store-Level Water & Utility Conservation Operations | [Store Operations Workflows](WF-store-operations.md) |
| W607 | Store-Level Product Demo & Trial Station Daily Operations | [Store Operations Workflows](WF-store-operations.md) |
| W608 | Store-Level Customer Feedback Collection & Daily CX Pulse Monitoring | [Store Operations Workflows](WF-store-operations.md) |
| W609 | Store-Level New Employee Buddy System & First-Week Onboarding | [Store Operations Workflows](WF-store-operations.md) |
| W610 | Insurance Claims Processing & Recovery Management | [Finance & Treasury Workflows](WF-finance.md) |
| W611 | Payment Gateway Daily Operations & Settlement Monitoring | [Finance & Treasury Workflows](WF-finance.md) |
| W612 | Intercompany Rate Setting & Quarterly Transfer Pricing Review | [Finance & Treasury Workflows](WF-finance.md) |
| W613 | Store-Level Weekly Payroll Accrual & Labor Cost Flash Report | [Finance & Treasury Workflows](WF-finance.md) |
| W614 | Data Warehouse & ETL Pipeline Daily Operations & Monitoring | [IT Operations Workflows](WF-it-operations.md) |
| W615 | Customer Mobile App Daily Operations & Content Management | [IT Operations Workflows](WF-it-operations.md) |
| W616 | ERP Business Change Request & Enhancement Backlog Management | [IT Operations Workflows](WF-it-operations.md) |
| W617 | B2B Customer Success & Quarterly Business Review Operations | [Customer Experience Workflows](WF-customer.md) |
| W618 | Customer Churn Prediction & Proactive Retention Management | [Customer Experience Workflows](WF-customer.md) |
| W619 | Customer Account Merge & Deduplication Request Processing | [Customer Experience Workflows](WF-customer.md) |
| W620 | Vendor Due Diligence & Onboarding Site Visit Management | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W621 | Vendor-Managed Inventory (VMI) Daily Performance Monitoring | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W622 | Mock Product Recall Exercise & Recall Readiness Testing | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W623 | Cross-Functional New Store Opening Readiness Review | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W624 | Competitor Store Visit Program & Market Intelligence Operations | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W625 | Product Quality Lab Testing & Certification Management | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W626 | Enterprise Risk Register Maintenance & Quarterly Risk Review | [Compliance & Governance Workflows](WF-compliance.md) |
| W627 | Product Recall Effectiveness Verification & Post-Recall Review | [Compliance & Governance Workflows](WF-compliance.md) |
| W628 | Employee Exit Interview & Attrition Analysis | [HR & Payroll Workflows](WF-hr.md) |
| W629 | Store-Level Employee Engagement Survey & Action Planning | [HR & Payroll Workflows](WF-hr.md) |
| W630 | Employee Recognition & Rewards Program Management | [HR & Payroll Workflows](WF-hr.md) |
| W631 | Strategic Sourcing & Category Strategy | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W632 | Competitive Bidding & Tender Management | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W633 | Purchase Price Variance (PPV) Analysis & Cost Management | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W634 | Revenue Assurance & POS Revenue Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W635 | PFRS 16 Lease Accounting Operations | [Finance & Treasury Workflows](WF-finance.md) |
| W636 | Standardized Balance Sheet Account Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W637 | Financial Controls Testing & Monitoring | [Finance & Treasury Workflows](WF-finance.md) |
| W638 | Period-End Journal Entry Review & Approval | [Finance & Treasury Workflows](WF-finance.md) |
| W639 | Rolling Forecast & Financial Scenario Planning | [Finance & Treasury Workflows](WF-finance.md) |
| W640 | Merchant Fee Analysis & Payment Cost Optimization | [Finance & Treasury Workflows](WF-finance.md) |
| W641 | Off-Cycle & Ad-Hoc Payment Processing | [HR & Payroll Workflows](WF-hr.md) |
| W642 | HMO & Private Benefits Administration | [HR & Payroll Workflows](WF-hr.md) |
| W643 | Final Pay Computation & Separation Settlement | [HR & Payroll Workflows](WF-hr.md) |
| W644 | 13th Month Pay Reconciliation & Compliance | [HR & Payroll Workflows](WF-hr.md) |
| W645 | Strategic Workforce Planning | [HR & Payroll Workflows](WF-hr.md) |
| W646 | HR Service Desk Operations | [HR & Payroll Workflows](WF-hr.md) |
| W647 | Employee Data Privacy Compliance Operations | [HR & Payroll Workflows](WF-hr.md) |
| W648 | DC Cycle Counting & Inventory Accuracy Program | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W649 | DC Safety Operations & Compliance | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W650 | Warehouse Equipment Preventive Maintenance | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W651 | Reverse Logistics Processing (Customer/Store Returns at DC) | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W652 | Seasonal Warehouse Surge Planning & Execution | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W653 | Fleet Accident & Incident Management | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W654 | Driver Onboarding, Training & Certification | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W655 | Safety Training & Certification Tracking | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W656 | Anti-Bribery & Anti-Corruption (ABAC) Compliance Program | [Compliance & Governance Workflows](WF-compliance.md) |
| W657 | Regulatory Change Management & Impact Assessment | [Compliance & Governance Workflows](WF-compliance.md) |
| W658 | General Regulatory Inspection Response Protocol | [Compliance & Governance Workflows](WF-compliance.md) |
| W659 | Ecommerce Platform Incident Management | [Ecommerce Workflows](WF-ecommerce.md) |
| W660 | Service Recovery & Customer Retention Program | [Customer Experience Workflows](WF-customer.md) |
| W661 | Fixed Asset Depreciation Run & Component Accounting Operations | [Finance & Treasury Workflows](WF-finance.md) |
| W662 | AP Aging Management & Vendor Payment Prioritization | [Finance & Treasury Workflows](WF-finance.md) |
| W663 | Customer Credit Portfolio Periodic Review & Collection Strategy | [Finance & Treasury Workflows](WF-finance.md) |
| W664 | Cash Flow Variance Analysis & Liquidity Stress Testing | [Finance & Treasury Workflows](WF-finance.md) |
| W665 | Store-Level KPI Dashboard & Daily Performance Monitoring | [Store Operations Workflows](WF-store-operations.md) |
| W666 | Store-Level Inventory Receiving Quality Control | [Store Operations Workflows](WF-store-operations.md) |
| W667 | Store-Level Price Verification & Daily Compliance Operations | [Store Operations Workflows](WF-store-operations.md) |
| W668 | Store-Level Home Delivery & Third-Party Logistics Coordination | [Store Operations Workflows](WF-store-operations.md) |
| W669 | Vendor Contract Compliance Monitoring & Enforcement | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W670 | Supplier Emergency Onboarding & Rapid Activation | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W671 | Commodity Price Monitoring & Procurement Strategy | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W672 | VMI Quarterly Business Review & Program Optimization | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W673 | Customer Segmentation & Target Marketing Operations | [Customer Experience Workflows](WF-customer.md) |
| W674 | Customer Loyalty Program Partner Management | [Customer Experience Workflows](WF-customer.md) |
| W675 | Customer Data Platform Daily Operations & Data Quality Management | [Customer Experience Workflows](WF-customer.md) |
| W676 | Digital Marketing Campaign Operations & Cross-Channel Execution | [Marketing Campaign Workflows](WF-marketing.md) |
| W677 | Marketing Budget Management & Spend Analytics | [Marketing Campaign Workflows](WF-marketing.md) |
| W678 | Multi-Channel Pricing Consistency Monitoring & Governance | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W679 | Assortment Optimization & Rationalization Review | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W680 | Supply Chain Cost Analysis & Logistics Optimization Review | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W681 | DC Quality Control & Vendor Compliance Inspection at Receiving | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W682 | Employee Career Development & Internal Job Posting Operations | [HR & Payroll Workflows](WF-hr.md) |
| W683 | Employee Competency Assessment & Certification Management | [HR & Payroll Workflows](WF-hr.md) |
| W684 | Business Intelligence Report Development & Governance Lifecycle | [IT Operations Workflows](WF-it-operations.md) |
| W685 | Business Continuity Plan Maintenance & Annual BIA Refresh | [Compliance & Governance Workflows](WF-compliance.md) |
| W686 | Document Approval Routing & Digital Signature Management | [Document Management Workflows](WF-document-management.md) |
| W687 | Document Template Management & Version Control | [Document Management Workflows](WF-document-management.md) |
| W688 | Contract & Agreement Lifecycle Management | [Document Management Workflows](WF-document-management.md) |
| W689 | AI/ML Model Governance, Bias Audit & Ethical Review | [Innovation & Digital Transformation Workflows](WF-innovation.md) |
| W690 | Digital Transformation Initiative Portfolio Management | [Innovation & Digital Transformation Workflows](WF-innovation.md) |
| W691 | Emerging Technology Scouting & Proof-of-Concept Evaluation | [Innovation & Digital Transformation Workflows](WF-innovation.md) |
| W692 | Store Energy Efficiency Monitoring & Utility Cost Optimization | [ESG & Sustainability Reporting Workflows](WF-esg.md) |
| W693 | Water Consumption Tracking & Conservation Management | [ESG & Sustainability Reporting Workflows](WF-esg.md) |
| W694 | ESG Data Collection, Validation & Annual Sustainability Report Preparation | [ESG & Sustainability Reporting Workflows](WF-esg.md) |
| W695 | Emergency Response & Evacuation Protocol Management | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W696 | Contractor & Visitor Safety Induction & Access Control | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W697 | Workplace Ergonomics Assessment & Musculoskeletal Injury Prevention | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W698 | Safety Data Sheet (SDS) Lifecycle Management & Distribution | [Hazmat & Compliance Workflows](WF-hazmat.md) |
| W699 | Hazmat Transportation & Carrier Compliance Management | [Hazmat & Compliance Workflows](WF-hazmat.md) |
| W700 | Facility Condition Assessment & Capital Planning Support | [Facility & Asset Maintenance Workflows](WF-non-store-maintenance.md) |
| W701 | Utility Infrastructure Management & Metering Operations | [Facility & Asset Maintenance Workflows](WF-non-store-maintenance.md) |
| W702 | New Store Opening Project Management & Go-Live Execution | [Store Operations Workflows](WF-store-operations.md) |
| W703 | Store Closure, Consolidation & Asset Recovery | [Store Operations Workflows](WF-store-operations.md) |
| W704 | Wholesale Customer Contract Renewal & Tier Reclassification | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W705 | Vendor Self-Service Portal Operations & Supplier Collaboration | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W706 | Supplier Performance Scorecard & Quarterly Business Review | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W707 | Omnichannel Returns & Refund Orchestration | [Customer Experience Workflows](WF-customer.md) |
| W708 | Customer Communication Management & Proactive Notification Operations | [Customer Experience Workflows](WF-customer.md) |
| W709 | Enterprise Data Governance & Quality Management Operations | [IT Operations Workflows](WF-it-operations.md) |
| W710 | Loss Prevention Analytics & Shrinkage Investigation System Operations | [IT Operations Workflows](WF-it-operations.md) |
| W711 | BIR Withholding Tax (EWT) Certificate Form 2307 Issuance to Vendors | [Finance & Treasury Workflows](WF-finance.md) |
| W712 | Financial Restatement & Prior-Year Adjustment Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W713 | Corporate Credit Card Program Management & Expense Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W714 | Store-Level Daily Financial Summary Reporting & Flash P&L | [Finance & Treasury Workflows](WF-finance.md) |
| W715 | Employee Referral Program Management & Reward Processing | [HR & Payroll Workflows](WF-hr.md) |
| W716 | Internal Communication & Company-Wide Announcement Management | [HR & Payroll Workflows](WF-hr.md) |
| W717 | Workplace Violence Prevention & Response Protocol | [HR & Payroll Workflows](WF-hr.md) |
| W718 | Employee Relocation & Housing Assistance Management | [HR & Payroll Workflows](WF-hr.md) |
| W719 | Diversity, Equity & Inclusion (DEI) Program Management | [HR & Payroll Workflows](WF-hr.md) |
| W720 | Store-Level Daily Safety Briefing & Toolbox Talk | [Store Operations Workflows](WF-store-operations.md) |
| W721 | Store-Level Vendor Promodizer Floor Activity Coordination & Compliance | [Store Operations Workflows](WF-store-operations.md) |
| W722 | Store-Level Exterior Display & Garden Center Daily Operations | [Store Operations Workflows](WF-store-operations.md) |
| W723 | Store-Level Loading Bay Traffic & Truck Queue Management | [Store Operations Workflows](WF-store-operations.md) |
| W724 | Marketplace Channel Daily Operations & Order Management (Lazada/Shopee) | [Ecommerce Workflows](WF-ecommerce.md) |
| W725 | Ecommerce Platform Daily Health Monitoring & Performance Dashboard | [Ecommerce Workflows](WF-ecommerce.md) |
| W726 | Ecommerce Product Content Enrichment & Catalog Daily Operations | [Ecommerce Workflows](WF-ecommerce.md) |
| W727 | Carrier & Freight Forwarder Daily Performance Monitoring | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W728 | Port & Customs Clearance Daily Status Tracking & Escalation | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W729 | Supply Chain Disruption Rapid Response & Escalation Protocol | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W730 | Anti-Money Laundering (AML) Compliance Program Operations | [Compliance & Governance Workflows](WF-compliance.md) |
| W731 | Consumer Act (RA 7394) Compliance Monitoring & Enforcement | [Compliance & Governance Workflows](WF-compliance.md) |
| W732 | Vendor Tax Compliance Monitoring & BIR TIN Validation | [Compliance & Governance Workflows](WF-compliance.md) |
| W733 | Enterprise API Gateway Daily Monitoring & Health Dashboard | [IT Operations Workflows](WF-it-operations.md) |
| W734 | Data Quality Daily Triage & Remediation Operations | [IT Operations Workflows](WF-it-operations.md) |
| W735 | Customer Onboarding Journey Management & First-90-Day Engagement | [Customer Experience Workflows](WF-customer.md) |
| W736 | Marketing Data Platform Daily Operations & Campaign Analytics | [Marketing Campaign Workflows](WF-marketing.md) |
| W737 | Markdown Optimization & Analytics Operations | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W738 | Vendor Trade Fund Management & Promotional Budget Tracking | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W739 | Store-Level Daily Huddle & Morning Team Briefing | [Store Operations Workflows](WF-store-operations.md) |
| W740 | Store-Level Customer Complaint On-the-Spot Resolution & Floor Staff Empowerment | [Store Operations Workflows](WF-store-operations.md) |
| W741 | Store-Level Fuel Inventory & Backup Generator Management | [Store Operations Workflows](WF-store-operations.md) |
| W742 | Store-Level Key, Access Card & Secure Area Daily Management | [Store Operations Workflows](WF-store-operations.md) |
| W743 | Store-Level Daily Cleaning & Sanitation Checklist Execution | [Store Operations Workflows](WF-store-operations.md) |
| W744 | Store-Level Special Order Follow-Up & Proactive Customer Notification | [Store Operations Workflows](WF-store-operations.md) |
| W745 | Store-Level Receiving Dock Scheduling & DSD Vendor Delivery Window Management | [Store Operations Workflows](WF-store-operations.md) |
| W746 | Store-Level Building Material Sample Management & Customer Selection Assistance | [Store Operations Workflows](WF-store-operations.md) |
| W747 | POS Credit Card Installment Selling & 0% Interest Promotion Processing | [Store Operations Workflows](WF-store-operations.md) |
| W748 | POS Customer Loyalty On-the-Spot Upselling & Cross-Selling | [Store Operations Workflows](WF-store-operations.md) |
| W749 | POS Heavy Equipment & Power Tool Safety Acknowledgment & Release Processing | [Store Operations Workflows](WF-store-operations.md) |
| W750 | Credit Card Installment Sales Reconciliation & Bank Settlement Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W751 | Store-Level Emergency Cash Float Request & Expedited Replenishment | [Finance & Treasury Workflows](WF-finance.md) |
| W752 | Intercompany Management Fee Allocation & Monthly Billing | [Finance & Treasury Workflows](WF-finance.md) |
| W753 | Store-Level Employee Meal Break & Rest Period Scheduling & DOLE Compliance | [HR & Payroll Workflows](WF-hr.md) |
| W754 | Store-Level New Hire First-30-Day Performance Check-In & Early Intervention | [HR & Payroll Workflows](WF-hr.md) |
| W755 | Store-Level Employee Internal Theft Prevention Awareness & Compliance Daily Operations | [HR & Payroll Workflows](WF-hr.md) |
| W756 | Customer Post-Purchase Follow-Up & Satisfaction Verification | [Customer Experience Workflows](WF-customer.md) |
| W757 | Customer On-the-Spot Loyalty Tier Upgrade Offer Processing | [Customer Experience Workflows](WF-customer.md) |
| W758 | Store-Level Fire Safety Equipment Daily Inspection & Compliance | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W759 | Store-Level Hazardous Material Customer Advisory & Safe Handling Guidance | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W760 | Vendor-Specific Commodity Price Index Tracking & Procurement Trigger Management | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W761 | Supplier Innovation & New Product Introduction Collaboration Processing | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W762 | Carrier Performance Weekly Review & Freight Rate Benchmarking | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W763 | Supply Chain Vendor Diversification & Alternative Sourcing Maintenance | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W764 | Store-Level Daily Opening Safe Count & Cash Float Preparation | [Finance & Treasury Workflows](WF-finance.md) |
| W765 | Multi-Entity Consolidation Monthly Execution & Elimination Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W766 | Customer Credit Note Aging Management & Unredeemed Credit Write-Off | [Finance & Treasury Workflows](WF-finance.md) |
| W767 | Vendor Rebate Claim Filing & Settlement Documentation Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W768 | BIR VAT Refund Claim Processing & Input VAT Recovery | [Finance & Treasury Workflows](WF-finance.md) |
| W769 | Customer Overpayment Detection & Refund Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W770 | AP Vendor Debit Memo Processing & Account Deduction Management | [Finance & Treasury Workflows](WF-finance.md) |
| W771 | Store-Level BOPIS Order Aging & Abandoned Pickup Processing | [Store Operations Workflows](WF-store-operations.md) |
| W772 | Store-Level Rain Check Issuance for Out-of-Stock Promotional Items | [Store Operations Workflows](WF-store-operations.md) |
| W773 | Store-Level Customer Hold & Will-Call Order Management | [Store Operations Workflows](WF-store-operations.md) |
| W774 | Store-Level Parking Lot & Exterior Facility Daily Management | [Store Operations Workflows](WF-store-operations.md) |
| W775 | Store-Level Customer Loyalty Card Replacement & Account Recovery | [Store Operations Workflows](WF-store-operations.md) |
| W776 | Store-Level Product Recall Customer Notification Execution | [Store Operations Workflows](WF-store-operations.md) |
| W777 | Employee Leave Balance Management & Annual Leave Carry-Forward Processing | [HR & Payroll Workflows](WF-hr.md) |
| W778 | Employee Benefits Annual Open Enrollment & Plan Selection Management | [HR & Payroll Workflows](WF-hr.md) |
| W779 | Store-Level Employee Injury Incident Reporting & Workers' Compensation Claim Processing | [HR & Payroll Workflows](WF-hr.md) |
| W780 | Store-Level Employee Uniform & PPE Periodic Issuance & Replacement Processing | [HR & Payroll Workflows](WF-hr.md) |
| W781 | Customer Store Credit Issuance & Lifecycle Management | [Customer Experience Workflows](WF-customer.md) |
| W782 | Customer B2B Order-to-Cash Cycle Monitoring & Proactive Communication | [Customer Experience Workflows](WF-customer.md) |
| W783 | Customer Credit Application Scoring & Risk Assessment Processing | [Customer Experience Workflows](WF-customer.md) |
| W784 | DC Inventory Slotting Optimization & Periodic Re-Slotting Execution | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W785 | Vendor Returnable Transport Packaging Reconciliation & Settlement | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W786 | DC-to-Store Delivery Route Optimization & Multi-Stop Planning | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W787 | ERP System Monthly Performance Review & Capacity Planning Update | [IT Operations Workflows](WF-it-operations.md) |
| W788 | Vendor New Product Submission Review & Evaluation Processing | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W789 | Construction Safety Management & DOLE DO 13 Compliance | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W790 | Construction Quality Assurance, Milestone Inspection & Material Testing | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W791 | Construction Document Control, Drawing Revision & As-Built Management | [Engineering & Construction Workflows](WF-engineering-construction.md) |
| W792 | Project Change Order Management & Margin Re-Impact Assessment | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W793 | Project Close-Out, Final Reconciliation & Warranty Handover | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W794 | Service SKU Catalog Management, Pricing & Material Linkage | [Installation & Value-Added Services](WF-services.md) |
| W795 | Service Customer Complaint, Rework & Warranty Claim Management | [Installation & Value-Added Services](WF-services.md) |
| W796 | DC Workforce Scheduling, Labor Planning & Productivity Tracking | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W797 | DC Security Operations, Perimeter Management & Access Control | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W798 | DC Building Maintenance, Utility Operations & Facility Condition Monitoring | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W799 | Vehicle Acquisition, Registration, Insurance & Disposal Lifecycle Management | [Fleet Operations & Driver Management](WF-logistics-fleet.md) |
| W800 | Green Building Certification (BERDE/LEED) & Sustainable Store Design Standards | [ESG & Sustainability Reporting Workflows](WF-esg.md) |
| W801 | ESG Incident Response, Regulatory Citation Management & Stakeholder Communication | [ESG & Sustainability Reporting Workflows](WF-esg.md) |
| W802 | LGU Local Business Tax Computation, Payment & Receipt Management | [Regulatory Permits & Local Government Compliance](WF-regulatory-permits.md) |
| W803 | Hazmat Regulatory Change Management & Compliance Update | [Hazardous Materials (Hazmat) & Compliance](WF-hazmat.md) |
| W804 | Occupational Health Surveillance, Employee Medical Monitoring & Record Management | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W805 | Workers' Compensation, SSS/ECC Claims & Return-to-Work Processing | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W806 | Annual Fire Safety System Testing, Certification & BFP Compliance | [Health, Safety & Environment Workflows](WF-health-safety.md) |
| W807 | Store Closure, Lease Termination & Asset Recovery Management | [Real Estate & Lease Management Workflows](WF-property.md) |
| W808 | Generator Preventive Maintenance, Fuel Management & Load Testing | [Facility & Asset Maintenance (HQ & DC)](WF-non-store-maintenance.md) |
| W809 | Wholesale Consignment Inventory Management & Settlement | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W810 | Wholesale Backorder Management, Allocation & Customer Communication | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W811 | Wholesale Delivery Proof, Discrepancy Resolution & POD Reconciliation | [Wholesale & Reseller Operations Workflows](WF-wholesale.md) |
| W812 | Customer Credit Field Collection Operations & Legal Escalation | [Finance & Treasury Workflows](WF-finance.md) |
| W813 | AP Vendor Invoice Duplicate Detection & Resolution | [Finance & Treasury Workflows](WF-finance.md) |
| W814 | Credit Card Settlement Exception & Chargeback Recovery Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W815 | Employee Business Travel Request, Approval & Expense Management | [HR & Payroll Workflows](WF-hr.md) |
| W816 | Multi-Entity Payroll Consolidation & Cross-Entity Reconciliation | [HR & Payroll Workflows](WF-hr.md) |
| W817 | Employee Sabbatical, Study Leave & Secondment Management | [HR & Payroll Workflows](WF-hr.md) |
| W818 | Vendor Insurance Certificate & Compliance Documentation Tracking | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W819 | Vendor Quality Incoming Inspection Failure & Material Review Board (MRB) | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W820 | Customer Project BOM Estimation & Material Planning Service | [Customer Experience Workflows](WF-customer.md) |
| W821 | Customer Project Warranty Registration & Multi-Year Tracking | [Customer Experience Workflows](WF-customer.md) |
| W822 | Customer Loyalty Tier Benefit Fulfillment & Welcome Package Processing | [Customer Experience Workflows](WF-customer.md) |
| W823 | Store-Level Customer Material Calculator & Quantity Estimation Service | [Store Operations Workflows](WF-store-operations.md) |
| W824 | Store-Level Lumber Yard & Outdoor Area Daily Operations | [Store Operations Workflows](WF-store-operations.md) |
| W825 | Store-Level Bulky Item Delivery Proof Collection & Documentation | [Store Operations Workflows](WF-store-operations.md) |
| W826 | Store-Level Layaway Payment Reminder & Forfeiture Processing | [Store Operations Workflows](WF-store-operations.md) |
| W827 | Store-Level Building Material Load Calculation & Safety Advisory | [Store Operations Workflows](WF-store-operations.md) |
| W828 | Ecommerce Platform Feature Release, A/B Testing & UX Optimization | [Ecommerce Workflows](WF-ecommerce.md) |
| W829 | Customer Ecommerce Order Split & Partial Delivery Proactive Communication | [Ecommerce Workflows](WF-ecommerce.md) |
| W830 | Product Phase-Out Inventory Disposition Planning & Execution | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W831 | POS Terminal Emergency Swap & Rapid Replacement Protocol | [IT Operations Workflows](WF-it-operations.md) |
| W832 | ERP User Access Quarterly Recertification & Compliance Review | [IT Operations Workflows](WF-it-operations.md) |
| W833 | Marketing Campaign Compliance Review & Regulatory Approval | [Marketing Campaign Workflows](WF-marketing.md) |
| W834 | Customer Account Data Deletion & RA 10173 Privacy Compliance Processing | [Compliance & Governance Workflows](WF-compliance.md) |
| W835 | Store-Level Replenishment Forecast Accuracy Review & Parameter Tuning | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W836 | DC Outbound Load Verification & Pre-Dispatch Quality Check | [Warehouse & Logistics Workflows](WF-warehouse.md) |
| W837 | Daily Store Exception-Based Reporting & Transaction Monitoring | [Loss Prevention & Asset Protection Workflows](WF-loss-prevention.md) |
| W838 | CCTV & Surveillance System Daily Operations & Incident Review | [Loss Prevention & Asset Protection Workflows](WF-loss-prevention.md) |
| W839 | Internal Theft Investigation & Employee Dishonesty Case Management | [Loss Prevention & Asset Protection Workflows](WF-loss-prevention.md) |
| W840 | Organized Retail Crime Detection, Tracking & Task Force Coordination | [Loss Prevention & Asset Protection Workflows](WF-loss-prevention.md) |
| W841 | Refund & Return Fraud Detection, Investigation & Prevention | [Loss Prevention & Asset Protection Workflows](WF-loss-prevention.md) |
| W842 | Cash Handling Exception Monitoring & Sweethearting Detection | [Loss Prevention & Asset Protection Workflows](WF-loss-prevention.md) |
| W843 | Vendor & Delivery Fraud Detection & Dock Security Audit | [Loss Prevention & Asset Protection Workflows](WF-loss-prevention.md) |
| W844 | Store Entrance/Exit Audit & Electronic Article Surveillance (EAS) Management | [Loss Prevention & Asset Protection Workflows](WF-loss-prevention.md) |
| W845 | Shrinkage Analysis, Root Cause Investigation & Reduction Program | [Loss Prevention & Asset Protection Workflows](WF-loss-prevention.md) |
| W846 | Loss Prevention Training, Awareness & Compliance Program | [Loss Prevention & Asset Protection Workflows](WF-loss-prevention.md) |
| W847 | Business Continuity Plan Annual Review & Update | [Business Continuity & Disaster Recovery Workflows](WF-business-continuity.md) |
| W848 | Typhoon & Natural Disaster Store Emergency Protocol & Response | [Business Continuity & Disaster Recovery Workflows](WF-business-continuity.md) |
| W849 | IT Disaster Recovery Site Activation & Failover Execution | [Business Continuity & Disaster Recovery Workflows](WF-business-continuity.md) |
| W850 | Store Emergency Closure & Reopening Procedure | [Business Continuity & Disaster Recovery Workflows](WF-business-continuity.md) |
| W851 | Critical System Recovery & Service Restoration | [Business Continuity & Disaster Recovery Workflows](WF-business-continuity.md) |
| W852 | Supply Chain Disruption Business Impact Assessment & Recovery | [Business Continuity & Disaster Recovery Workflows](WF-business-continuity.md) |
| W853 | Business Continuity Plan Tabletop Exercise & Drill Execution | [Business Continuity & Disaster Recovery Workflows](WF-business-continuity.md) |
| W854 | Pandemic/Epidemic Business Continuity Activation & Operations | [Business Continuity & Disaster Recovery Workflows](WF-business-continuity.md) |
| W855 | Communication Tree Activation & Crisis Communication Management | [Business Continuity & Disaster Recovery Workflows](WF-business-continuity.md) |
| W856 | Post-Incident Review, Lessons Learned & Plan Update | [Business Continuity & Disaster Recovery Workflows](WF-business-continuity.md) |
| W857 | Store & DC Property Insurance Claim Filing & Documentation | [Insurance & Claims Management Workflows](WF-insurance.md) |
| W858 | Typhoon, Flood & Natural Disaster Damage Assessment & Insurance Claim | [Insurance & Claims Management Workflows](WF-insurance.md) |
| W859 | Vehicle & Fleet Insurance Claim Processing | [Insurance & Claims Management Workflows](WF-insurance.md) |
| W860 | Business Interruption Insurance Claim & Loss Documentation | [Insurance & Claims Management Workflows](WF-insurance.md) |
| W861 | Employee Injury Insurance Claim Coordination & SSS/ECC Filing | [Insurance & Claims Management Workflows](WF-insurance.md) |
| W862 | Insurance Policy Annual Renewal & Coverage Review | [Insurance & Claims Management Workflows](WF-insurance.md) |
| W863 | Third-Party Liability Claim & Customer Incident Insurance Response | [Insurance & Claims Management Workflows](WF-insurance.md) |
| W864 | Insurance Claim Recovery, Settlement & Accounting Entry | [Insurance & Claims Management Workflows](WF-insurance.md) |
| W865 | Vendor Portal User Onboarding, Access Provisioning & Training | [Vendor Portal & Supplier Collaboration Workflows](WF-vendor-portal.md) |
| W866 | Vendor Self-Service Purchase Order Acknowledgment & Confirmation | [Vendor Portal & Supplier Collaboration Workflows](WF-vendor-portal.md) |
| W867 | Vendor Self-Service Invoice Submission & Payment Status Inquiry | [Vendor Portal & Supplier Collaboration Workflows](WF-vendor-portal.md) |
| W868 | Vendor Catalog & Product Information Self-Service Management | [Vendor Portal & Supplier Collaboration Workflows](WF-vendor-portal.md) |
| W869 | Vendor Dispute Resolution & Issue Ticketing | [Vendor Portal & Supplier Collaboration Workflows](WF-vendor-portal.md) |
| W870 | Vendor Compliance Document Upload & Expiration Tracking | [Vendor Portal & Supplier Collaboration Workflows](WF-vendor-portal.md) |
| W871 | Supplier Scorecard Portal Publication & Performance Transparency | [Vendor Portal & Supplier Collaboration Workflows](WF-vendor-portal.md) |
| W872 | Vendor RFQ & Bid Submission Portal Management | [Vendor Portal & Supplier Collaboration Workflows](WF-vendor-portal.md) |
| W873 | Product Safety Incident Triage & Recall Risk Assessment | [Product Recall Management Workflows](WF-product-recall.md) |
| W874 | Product Recall Customer Notification Campaign Execution | [Product Recall Management Workflows](WF-product-recall.md) |
| W875 | Product Recall Inventory Quarantine, Hold & Disposition | [Product Recall Management Workflows](WF-product-recall.md) |
| W876 | Product Recall Regulatory Reporting & DTI/BIR/FDA Compliance | [Product Recall Management Workflows](WF-product-recall.md) |
| W877 | Product Recall Vendor Recovery & Cost Reimbursement | [Product Recall Management Workflows](WF-product-recall.md) |
| W878 | Product Recall Effectiveness Audit & Close-Out | [Product Recall Management Workflows](WF-product-recall.md) |
| W879 | Daily Report Distribution & Automated Dashboard Refresh | [Business Intelligence & Analytics Operations Workflows](WF-bi-analytics.md) |
| W880 | BI Dashboard Development, Enhancement & User Request Management | [Business Intelligence & Analytics Operations Workflows](WF-bi-analytics.md) |
| W881 | Data Warehouse ETL Job Monitoring & Exception Handling | [Business Intelligence & Analytics Operations Workflows](WF-bi-analytics.md) |
| W882 | Self-Service BI Governance, Access Provisioning & Training | [Business Intelligence & Analytics Operations Workflows](WF-bi-analytics.md) |
| W883 | Ad-hoc Analytics Request Fulfillment & SLA Management | [Business Intelligence & Analytics Operations Workflows](WF-bi-analytics.md) |
| W884 | Data Quality Monitoring, Exception Triage & Remediation | [Business Intelligence & Analytics Operations Workflows](WF-bi-analytics.md) |
| W885 | Monthly Executive Reporting Package Preparation | [Business Intelligence & Analytics Operations Workflows](WF-bi-analytics.md) |
| W886 | Customer Credit Application Processing & Scoring | [Customer Credit & Collections Management Workflows](WF-credit-collections.md) |
| W887 | Customer Credit Limit Review, Adjustment & Approval | [Customer Credit & Collections Management Workflows](WF-credit-collections.md) |
| W888 | Customer Credit Hold Management & Order Blocking | [Customer Credit & Collections Management Workflows](WF-credit-collections.md) |
| W889 | Customer AR Aging Analysis & Collection Prioritization | [Customer Credit & Collections Management Workflows](WF-credit-collections.md) |
| W890 | Customer Collection Call Execution & Promise Tracking | [Customer Credit & Collections Management Workflows](WF-credit-collections.md) |
| W891 | Customer Bad Debt Write-Off Proposal & Approval | [Customer Credit & Collections Management Workflows](WF-credit-collections.md) |
| W892 | Customer Statement Generation & Distribution | [Customer Credit & Collections Management Workflows](WF-credit-collections.md) |
| W893 | Customer Credit Scorecard Annual Review & Portfolio Analysis | [Customer Credit & Collections Management Workflows](WF-credit-collections.md) |
| W894 | Customer Project Material List (BOM) Save, Share & Reorder Service ("Project Vault") | [Customer Experience Workflows](WF-customer.md) |
| W895 | Store-Level Pro Desk Appointment Scheduling & Priority Service Queue Management | [Customer Experience Workflows](WF-customer.md) |
| W896 | Customer Gift Card Corporate & Bulk Purchase Processing | [Store Operations Workflows](WF-store-operations.md) |
| W897 | Store-Level Trade Professional Verification & Pro Badge Issuance for Discount Program | [Store Operations Workflows](WF-store-operations.md) |
| W898 | Store-Level Custom Paint Formula Save, Recall & Reorder Service | [Installation & Value-Added Services](WF-services.md) |
| W899 | Customer Bulk/Project Delivery Scheduling & Multi-Drop Coordination (B2C) | [Ecommerce Workflows](WF-ecommerce.md) |
| W900 | Vendor New Product In-Store Launch Event & Demonstration Coordination | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W901 | Vendor Seasonal Buy-Back & Stock Return Agreement Execution | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W902 | Customer Loyalty Partner Reward Catalog Management & Fulfillment | [Marketing Campaign Workflows](WF-marketing.md) |
| W903 | Store-Level Customer Material Sample Loan & Return Management | [Store Operations Workflows](WF-store-operations.md) |
| W904 | Store-Level Contractor Referral & Customer-Contractor Matchmaking Service | [Customer Experience Workflows](WF-customer.md) |
| W905 | Customer Project Photo Gallery & Social Proof/Inspiration Platform | [Ecommerce Workflows](WF-ecommerce.md) |
| W906 | Store-Level Community Workshop Space Booking & DIY Event Management | [Installation & Value-Added Services](WF-services.md) |
| W907 | Customer Consumables Subscription & Auto-Replenishment Service | [Ecommerce Workflows](WF-ecommerce.md) |
| W908 | Store-Level Barangay & Local Fiesta Merchandising Calendar Management | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W909 | Customer Trade Account Co-Branded Credit Card Program Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W910 | Customer Product Bundle Assembly & Pre-Packaged Solution Kit Management | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W911 | Customer Digital Warranty Vault & Multi-Vendor Warranty Claim Aggregation | [Customer Experience Workflows](WF-customer.md) |
| W912 | Store-Level Customer Loyalty Points Gifting & Transfer Between Members | [Marketing Campaign Workflows](WF-marketing.md) |
| W913 | Store-Level Emergency Generator Fuel Reserve Management & DOE Compliance | [Store Operations Workflows](WF-store-operations.md) |
| W914 | Customer Project Completion Celebration & Review Incentive Program | [Customer Experience Workflows](WF-customer.md) |
| W915 | Vendor Product Packaging Sustainability Assessment & Compliance Management | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W916 | Customer Trade-In & Used Power Tool Buy-Back Program | [Store Operations Workflows](WF-store-operations.md) |
| W917 | Ecommerce Live Commerce & Social Selling Operations | [Ecommerce Workflows](WF-ecommerce.md) |
| W918 | Customer Project Budget Tracking & Material Cost Variance Management | [Project-Based B2B & Trade Sales Workflows](WF-project-sales.md) |
| W919 | Intercompany Inventory Movement Accounting & Goods-in-Transit Reconciliation | [Finance & Treasury Workflows](WF-finance.md) |
| W920 | Store-Level Vendor-Led Product Knowledge Training & Staff Certification Program | [Store Operations Workflows](WF-store-operations.md) |
| W921 | Store-Level Emergency Local Sourcing & Alternative Vendor Activation | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W922 | Customer Walk-In Bulk Purchase Negotiation & Volume Pricing Approval | [Store Operations Workflows](WF-store-operations.md) |
| W923 | Ecommerce Assembly & Installation Service Upsell at Online Checkout | [Ecommerce Workflows](WF-ecommerce.md) |
| W924 | Store-Level Self-Service Kiosk & Interactive Product Information Station Management | [Store Operations Workflows](WF-store-operations.md) |
| W925 | Vendor Consignment Shelf Space Performance Monitoring & Optimization | [Merchandising & Pricing Workflows](WF-merchandising.md) |
| W926 | Customer Loyalty Reward Physical Fulfillment & Partner Logistics Management | [Marketing Campaign Workflows](WF-marketing.md) |
| W927 | Store-Level Rainy Season Emergency Product Deployment & Rapid Stock Replenishment | [Supply Chain Planning Workflows](WF-supply-chain.md) |
| W928 | Customer Price Protection & Price Adjustment Policy Processing | [Customer Experience Workflows](WF-customer.md) |
| W929 | Store-Level Lost & Found Item Management | [Store Operations Workflows](WF-store-operations.md) |
| W930 | Customer Back-in-Stock Notification Subscription & Alert Management | [Ecommerce Workflows](WF-ecommerce.md) |
| W931 | Store-Level Customer Comfort Room & Amenity Daily Operations | [Store Operations Workflows](WF-store-operations.md) |
| W932 | Vendor Catalog Price Change Intake, Assessment & ERP Synchronization | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W933 | Customer Loyalty Account Deceased Member Processing & Points Estate Transfer | [Customer Experience Workflows](WF-customer.md) |
| W934 | Ecommerce Customer Wishlist, Save-for-Later & Price Drop Alert | [Ecommerce Workflows](WF-ecommerce.md) |
| W935 | Customer Product Registration at POS for Vendor Extended Warranty | [Store Operations Workflows](WF-store-operations.md) |
| W936 | Customer B2B Self-Service Portal Order Management & Account Access | [Customer Experience Workflows](WF-customer.md) |
| W937 | Store-Level Customer Wheelchair & PWD Mobility Assistance Service | [Store Operations Workflows](WF-store-operations.md) |
| W938 | Vendor Managed Inventory (VMI) Periodic Data Accuracy Audit & Reconciliation | [Procurement & Vendor Management Workflows](WF-procurement.md) |
| W939 | Customer Store Credit Expiration Management & Unclaimed Credit Processing | [Finance & Treasury Workflows](WF-finance.md) |
| W940 | Ecommerce Customer Product Comparison Tool & Buying Guide Content Management | [Ecommerce Workflows](WF-ecommerce.md) |
| W941 | Store-Level Customer Baggage Hold & Parcel Custody Service | [Store Operations Workflows](WF-store-operations.md) |
| W942 | Customer Loyalty Family/Household Account Linking & Shared Benefits Management | [Customer Experience Workflows](WF-customer.md) |
| W943 | Customer Glass Cutting & Custom Flat Glass Service | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W944 | Customer Pipe Threading, Cutting & Fabrication Service | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W945 | Customer Key Duplication & Lock Rekeying Service | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W946 | Customer Screen Door & Window Screen Custom Fabrication Service | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W947 | Ecommerce Live Video Shopping & Virtual Store Walkthrough | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W948 | Social Commerce Order Processing (Facebook, Instagram, TikTok Shop) | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W949 | Customer AI-Powered Home Renovation Visualizer & Material Estimator | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W950 | Store-Level Customer Vehicle Loading Assistance & Load Securing | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W951 | Store-Level Bulk Material Breaking & Custom Quantity Packaging | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W952 | Store-Level Customer Gratuity & Service Tip Processing | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W953 | Customer Contractor Micro-Lending Partnership Program Management | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W954 | Customer Delivery & Installation Quality Follow-Up Verification | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W955 | Customer Daily-Wage Construction Worker Hiring Facilitation Service | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W956 | Employee Annual Physical Examination & Occupational Health Clearance Management | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W957 | Employee Tuition Assistance & Educational Advancement Program Management | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W958 | Store-Level Daily Cash Variance Threshold Monitoring & Exception Escalation | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W959 | Vendor Rebate Volume Tier Compliance Reconciliation & Shortfall Processing | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W960 | Seasonal Forward Stock Pre-Positioning & Regional Buffer Management | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W961 | BSP Anti-Money Laundering (AML) Covered Transaction Reporting | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W962 | Vendor-Sponsored In-Store Display Compliance Audit & Chargeback | [Additional Operational Workflows — Batch 2](WF-additional-workflows.md) |
| W963 | Customer Tile & Flooring Quantity Calculator & Waste Factor Recommendation | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W964 | Customer Bulk Cement, Sand & Aggregates Order & Direct-to-Site Delivery | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W965 | Customer Complete Bathroom/Kitchen Renovation Package Assembly & Order | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W966 | Customer Construction Loan Documentation Assistance & Partner Bank Referral | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W967 | Store-Level Customer Project Material Takeoff & Professional Estimation Service | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W968 | Customer Multi-Store Aggregated Order & Consolidated Single Delivery | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W969 | Customer Quick Reorder from Purchase History (Trade & Loyalty Members) | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W970 | Customer Post-Disaster Insurance Claim Material Replacement Coordination | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W971 | Customer Power Tool Battery & Accessory Cross-Compatibility Checker & Recommendation | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W972 | Customer Franchise & Dealer Mini-Store Program Management | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W973 | Employee Long Service Award & Milestone Recognition Management | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W974 | Store-Level Customer Project Staged Delivery & Phased Material Release | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W975 | Customer Home Energy Audit Referral & Energy-Efficient Product Recommendation | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W976 | Store-Level Customer Lumber & Plywood Grade Selection & Quality Verification | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W977 | Employee Retirement Benefit Fund (RA 7641) Administration & Processing | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W978 | Vendor Seasonal Product Post-Season Performance Review & Assortment Rationalization | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W979 | Customer B2B Blanket Purchase Agreement & Scheduled Call-Off Management | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W980 | Store-Level Customer Construction Site Delivery Scheduling & Multi-Drop Coordination (B2B) | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W981 | Customer Paint Color Matching from Physical Sample & Digital Photo | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W982 | Customer Electrical Load Calculation & Wire Size Recommendation Service | [Additional Operational Workflows — Batch 3](WF-additional-workflows-batch3.md) |
| W983 | Customer Roofing Material Calculator & GI Sheet/Insulation Sizing Recommendation | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W984 | Customer Water Tank & Pump System Sizing Recommendation Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W985 | Store-Level Customer Aircon Sizing & BTU/Horsepower Calculation Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W986 | Store-Level Customer Rebar Cutting, Bending & Fabrication Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W987 | Customer Fence & Gate Material Estimation & Design Recommendation Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W988 | Store-Level Customer Welding & Custom Metal Fabrication Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W989 | Customer Plumbing System Layout Design & Material Takeoff Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W990 | Customer Solar Panel System Sizing & ROI Calculator Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W991 | Customer Electrical Circuit Design & Residential Load Planning Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W992 | Customer Garden & Landscape Design Consultation & Material Estimation Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W993 | Customer Construction Project Timeline & Phased Material Delivery Planner | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W994 | Employee Typhoon Disaster Relief Emergency Assistance & No-Interest Loan Program | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W995 | Vendor Consignment Inventory Ageing Analysis & Automatic Markdown Trigger | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W996 | Store-Level Contractor Loyalty Tier Upgrade & VIP Retention Program Management | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W997 | Customer Bathroom/Kitchen Fixture Compatibility Checker & Bundle Builder | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W998 | Customer Septic Tank & Wastewater System Sizing Recommendation Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W999 | Store-Level Customer Tile & Flooring Sample Loan & Return Program | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W1000 | Customer Ceiling System Material Calculator & Design Recommendation Service | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W1001 | Store-Level Employee Performance-Based Profit Sharing & Incentive Bonus Management | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W1002 | Vendor Product Sampling & Test Batch Inventory Lifecycle Management | [Additional Operational Workflows — Batch 4](WF-additional-workflows-batch4.md) |
| W1003 | Store-Level Paint Mixing Station Daily Cleaning, Calibration & Waste Disposal | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1004 | Customer Material Delivery Scheduling & Rescheduling Self-Service Portal | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1005 | Store-Level Shelf Stock Rotation & Paint/Chemical Expiry Monitoring | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1006 | Vendor Purchase Order ASN Reconciliation & Discrepancy Resolution | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1007 | Customer Tool & Equipment Demo Reservation & Scheduling Service | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1008 | Store-Level Power Tool Battery Charging Station Safety & Maintenance | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1009 | Customer Custom Order Special Pricing Approval & Quotation Lifecycle | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1010 | Store-Level Outdoor Garden Center Weather Protection & Seasonal Display Setup | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1011 | Customer Trade Account Credit Insurance & Bad Debt Protection Processing | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1012 | Store-Level Hazardous Material Spill Kit Inspection & Restocking | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1013 | E-Commerce Last-Mile Delivery Partner Performance Weekly Review | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1014 | Customer Multi-Entity Billing & Consolidated Invoicing for Corporate Accounts | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1015 | Store-Level Forklift & Heavy Equipment Daily Safety Check & Log | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1016 | Customer Product Installation Warranty Registration & Follow-Up Service | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1017 | Store-Level Scrap Metal & Recyclable Material Collection & Revenue Recognition | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1018 | Customer Project Progress Payment Verification & Invoice Matching | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1019 | Store-Level Construction Material Safety Data Sheet (SDS) Customer Access & Compliance | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1020 | Vendor Consignment Inventory Physical Count & Periodic Reconciliation | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1021 | Store-Level Loading Dock Equipment Maintenance & Safety Inspection | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1022 | Customer Trade Account Statement Dispute & Resolution Processing | [Additional Operational Workflows — Batch 5](WF-additional-workflows-batch5.md) |
| W1023 | Store-Level Post-Typhoon Damage Assessment, Cleanup & Rapid Reopening | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1024 | Customer Material Escrow & Project Fund Management for B2B Construction Accounts | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1025 | Store-Level Shelving, Racking & Display Fixture Safety Inspection & Maintenance | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1026 | Vendor Product Discontinuation Notification & Last-Time Buy Management | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1027 | Customer AI-Powered Chatbot & Virtual Shopping Assistant Operations | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1028 | Store-Level Shopping Cart, Basket & Customer Equipment Inventory Management | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1029 | DC-Level Temperature, Humidity & Environmental Monitoring for Sensitive Goods | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1030 | Multi-Store District Manager Weekly Operations Review & Compliance Audit | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1031 | Customer Delivery Service Area Geo-Fencing & Coverage Management | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1032 | Employee Overtime Pre-Approval, Monitoring & DOLE Weekly Cap Enforcement | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1033 | Vendor Lead Time Accuracy Monitoring & Supply Planning Impact Assessment | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1034 | Customer Ecommerce Payment Failure Recovery, Retry & Abandoned Checkout Rescue | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1035 | Store-Level Return-to-Vendor (RTV) Consolidation & Batch Shipping Processing | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1036 | Customer Digital Product Passport & Sustainability Information Access | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1037 | Store-Level Annual Physical Inventory Preparation, Execution & Variance Resolution | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1038 | Vendor Catalog Synchronization & Product Information Quality Audit | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1039 | Customer Housewarming & New Home Gift Registry Service | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1040 | Store-Level Customer Parking Lot Traffic Safety & Exterior Facility Management | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1041 | DC-Level Outbound Quality Sampling & Pre-Shipment Inspection | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1042 | Employee Store-Level Rotational Cross-Training & Multi-Skill Certification Program | [Additional Operational Workflows — Batch 6](WF-additional-workflows-batch6.md) |
| W1043 | Customer Paint Coverage Area Calculator & Primer/Finish Quantity Estimator Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1044 | Customer Concrete Mix Ratio & Volume Calculator for Slab/Foundation/Column Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1045 | Store-Level Customer PVC Pipe Cutting, Jointing & Fabrication Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1046 | Customer Door & Window Measurement, Sizing & Custom Order Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1047 | Store-Level Rainy Season Floor Safety, Anti-Slip Mat & Entrance Canopy Management | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1048 | Customer Rainwater Harvesting System Design & Material Sizing Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1049 | Store-Level Customer Tool Sharpening, Blade Replacement & Small Engine Maintenance Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1050 | Customer Staircase Tread, Riser & Railing Material Calculator Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1051 | Store-Level Fire Extinguisher Monthly Inspection, Annual Recharge & BFP Compliance | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1052 | Customer Gutter, Downspout & Flashing Sizing Calculator Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1053 | Customer Bathroom & Kitchen Exhaust Fan & Ventilation Duct Sizing Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1054 | Store-Level Customer Wire & Cable Cut-to-Length Spool Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1055 | Customer Water Filtration & Purification System Sizing for Residential & Commercial | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1056 | Store-Level Customer Construction Permit Advisory & Municipal Building Requirements Guidance | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1057 | Customer Insulation Material Calculator (Wall, Ceiling, Roof Thermal & Acoustic) | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1058 | Store-Level Customer Bulk Construction Water Delivery & Site Logistics Coordination | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1059 | Customer Kitchen Countertop Measurement & Custom Fabrication Order Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1060 | Customer Rebar Stirrup, Tying Wire & Binding Material Quantity Estimator Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1061 | Customer Tile Grout, Adhesive & Thin-Set Mortar Quantity Calculator Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |
| W1062 | Store-Level Customer Scaffolding Rental, Safety Harness Package & Delivery Service | [Additional Operational Workflows — Batch 7](WF-additional-workflows-batch7.md) |

---

*Total: 1,062 workflows across 38 domains + 6 cross-functional batches: Store Operations (166), Ecommerce (36), Finance & Treasury (90), Master Data Management (41), Treasury & Corporate Finance (18), Merchandising & Pricing (32), Compliance & Governance (40), Procurement (45), Customer Experience (48), Marketing Campaigns (23), HR & Payroll (53), Inventory Management (23), IT Operations (57), Supply Chain Planning (27), Warehouse & Logistics (26), Corporate Governance, Legal & Strategy (14), Services (19), Internal Audit & Risk Management (42), Engineering & Construction (8), Real Estate & Lease Management (8), Innovation & Digital Transformation (8), ESG & Sustainability (10), Hazmat & Compliance (7), Logistics Fleet (8), Non-Store Maintenance (7), Project-Based B2B Sales (11), Health Safety & Environment (13), Wholesale & Reseller (9), Document Management (5), Regulatory Permits & Local Government Compliance (9), Loss Prevention & Asset Protection (10), Business Continuity & Disaster Recovery (10), Insurance & Claims Management (8), Vendor Portal & Supplier Collaboration (8), Product Recall Management (6), Business Intelligence & Analytics Operations (7), Customer Credit & Collections Management (8), Additional Workflows Batch 2 (20), Additional Workflows Batch 3 (20), Additional Workflows Batch 4 (20), Additional Workflows Batch 5 (20), Additional Workflows Batch 6 (20), Additional Workflows Batch 7 (20). All 1,062 workflows have full requirement traceability.*

