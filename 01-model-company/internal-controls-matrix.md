# BuildRight Depot Corp. — Internal Controls Matrix

> Defines the key internal controls embedded in the ERP system and operational processes.
> Organized by control objective. Each control references the workflows that implement it.
> This matrix complements the operational workflows and ERP requirements — it does not
> replace them but provides an auditable controls framework.

---

## How to Read This Matrix

| Field | Meaning |
|---|---|
| **Control ID** | Unique identifier (CTL-XX) |
| **Control Objective** | What the control prevents or detects |
| **Control Type** | Preventive (P) or Detective (D) |
| **Control Activity** | What is done |
| **Owner** | Role accountable for the control |
| **Workflows** | Where this control is exercised |
| **ERP Requirement** | Supporting requirement from erp-requirements.md |

---

## C1. Authorization & Approval Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-01 | Prevent unauthorized purchases | P | PO approval per tiered matrix (> PHP 50K → Category Manager, > PHP 500K → VP, > PHP 2M → CFO for imports) | Category Manager / VP / CFO | W2A.5–6, W2B.2 | PUR-010 |
| CTL-02 | Prevent unauthorized capital expenditure | P | Capex request approval per tiered matrix (> PHP 100K → Finance Mgr, > PHP 500K → CFO, > PHP 5M → CEO, > PHP 50M → Board) | CFO / CEO / Board | W21.4 | FIN-016 |
| CTL-03 | Prevent unauthorized price overrides at POS | P | System requires manager authorization for price overrides > 10% or > PHP 500; logs override with cashier ID, manager ID, reason code | Store Manager | W5B.4a | POS-006 |
| CTL-04 | Prevent unauthorized transaction voids | P | Manager authorization required for all voids; system logs void with cashier ID, manager ID, reason, timestamp; queued void authorization if no manager available | Store Manager | W5B.10 | POS-006 |
| CTL-05 | Prevent unauthorized credit limit overrides | P | Credit hold override requires tiered approval (AR Supervisor ≤ 110%, Finance Mgr ≤ 130%); 24-hour validity; logged with authorizer and reason | AR Supervisor / Finance Manager | W8.3a | CRM-003 |
| CTL-06 | Prevent unauthorized vendor onboarding | P | Category Manager approval required for vendor master creation; Finance validates TIN and business permit; system blocks expired-document vendors from POs | Category Manager / AP Clerk | W36.5, W36 vendor doc tracking | PUR-003, MDM-004 |
| CTL-07 | Prevent unauthorized pricing changes | P | Price changes require Category Manager approval; VP Merchandising approves if aggregate impact > PHP 500K/month | Category Manager / VP | W40.5, W13.3 | MDM-005 |
| CTL-08 | Prevent unauthorized promotional pricing | P | VP Merchandising approves all promotional pricing before push to POS | VP Merchandising | W13.3 | POS-014 |

## C2. Segregation of Duties Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-09 | Separate purchasing from receiving | P | Buyer creates PO; Receiving Clerk processes GR; system validates 3-way match (PO → GR → Invoice) | Buyer / Receiving Clerk / AP Clerk | W2A, W3, W7.2 | PUR-005, FIN-004 |
| CTL-10 | Separate payment initiation from approval | P | AP Clerk generates payment file; Treasury Analyst reviews and approves; CFO authorizes | AP Clerk / Treasury / CFO | W7.9–10 | FIN-004 |
| CTL-11 | Separate inventory counting from adjustment approval | P | Stock Associate counts; Department Supervisor reviews; Store Manager approves adjustments > PHP 10K | Stock Associate / Dept. Supervisor / Store Manager | W6.6–7 | INV-006 |
| CTL-12 | Separate credit approval from sales execution | P | AR Clerk/Credit Committee approves credit; Cashier executes sale; system enforces approved limit | AR Clerk / Cashier | W24.5, W8.3 | CRM-008 |
| CTL-13 | Separate payroll computation from approval | P | Payroll Officer computes; Payroll Manager approves; Treasury transmits to bank | Payroll Officer / Payroll Mgr / Treasury | W10.5–8 | HR-001 |

## C3. Transaction Integrity Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-14 | Ensure AP invoices match PO and GR | P | 3-way match engine auto-approves within tolerance; exceptions routed to AP Clerk; unresolved exceptions escalated at day 5 | AP Supervisor | W7.2–6, W7.6a–b | FIN-004, PUR-005 |
| CTL-15 | Ensure accurate landed cost on imports | D | System auto-calculates landed cost from duty, freight, insurance at GR; Finance reconciles actual vs. estimated | Cost Accountant | W2B.12–13 | FIN-013 |
| CTL-16 | Ensure perpetual WAC accuracy | D | Cost Accountant verifies WAC at month-end by sampling high-value/high-volume SKUs; reconciles total inventory valuation to GL | Cost Accountant | W9A.6a | INV-003 |
| CTL-17 | Ensure GRNI completeness | D | Weekly GRNI aging report; items > 30 days flagged for Buyer follow-up; > 60 days escalated; > 90 days reviewed for accrual | AP Supervisor / Controller | W7 GRNI aging | FIN-004 |
| CTL-18 | Ensure IC balance agreement | D | Monthly IC reconciliation across all entity pairs; mismatches resolved before consolidation | Chief Accountant | W14.4–5 | IC-005 |
| CTL-19 | Ensure bank reconciliation completeness | D | Daily bank statement import; Treasury auto-matches deposits; monthly full reconciliation per entity | Treasury Analyst / Controller | W30.2, W30.9, W89 | FIN-009 |
| CTL-20 | Ensure POS cash accountability | D | Daily Z-report vs. physical cash count; variance > PHP 200 investigated and documented; electronic payment settlement auto-reconciled | Store Manager | W5F.2–4 | POS-009 |
| CTL-21 | Ensure inventory accuracy | D | Cycle counting with blind recounts; quarterly full coverage; adjustments require tiered approval; accuracy target ≥ 97% | Dept. Supervisor / Store Manager | W6, W42 | INV-006, INV-007 |
| CTL-22 | Ensure correct VAT computation | D | System auto-computes VAT per transaction; VAT-exempt/zero-rated customers classified in customer master with supporting docs; monthly VAT return reconciliation | Tax Accountant | W5B.4c, W9A.16 | FIN-006 |

## C4. Asset Safeguarding Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-23 | Detect POS fraud / theft | D | Real-time exception monitoring: excessive voids, manual price overrides, sweet-hearting, no-sale drawer opens; daily summary; LPO investigation | Loss Prevention Officer | W37.1–5 | NFR-007 |
| CTL-24 | Detect receiving fraud | D | GR monitored against PO; frequent damage claims flagged by vendor; receiving outside scheduled appointments flagged | DC Manager | W37.6 | PUR-011 |
| CTL-25 | Safeguard inventory in transit | D | In-transit inventory visibility for all DC→Store and inter-DC transfers; transfer discrepancies investigated per W22.9a | Supply Planner / DC Supervisor | W4.8, W22.9a | INV-014 |
| CTL-26 | Control fixed asset disposals | P | Disposal requires tiered approval based on NBV; IT ensures data wipe for IT assets per RA 10173; gain/loss on disposal auto-calculated | Controller / CFO / CEO | W39 | FIN-011 |
| CTL-27 | Safeguard customer data | P | Role-based access to personal data; encryption at rest and in transit; data subject access request tracking; breach register maintained | DPO | W53 | NFR-010, NFR-016 |
| CTL-28 | Control petty cash funds | D | Per-store and per-DC float limits; replenishment requires voucher submission; monthly reconciliation by custodian; AP reviews replenishment requests | Store Manager / AP Clerk | W25 | FIN-017 |

## C5. Financial Reporting Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-29 | Ensure accurate consolidated reporting | D | IC elimination automated; consolidated statements generated from verified entity-level closes; CFO reviews consolidated before distribution | CFO / Chief Accountant | W9A.12–15 | FIN-003, IC-003 |
| CTL-30 | Ensure complete month-end close | P | Close checklist with 17 defined steps; period lock after close; Controller signs off | Controller / CFO | W9A.1–17 | FIN-015 |
| CTL-31 | Ensure NRV provisions are adequate | D | Monthly inventory aging review; write-downs where NRV < cost; Controller approves write-downs > PHP 50K | Cost Accountant / Controller | W9A.16b | INV-011 |
| CTL-32 | Ensure loyalty liability accuracy | D | Monthly Cost Accountant estimate of loyalty liability vs. deferred revenue balance; adjusted if estimate differs | Cost Accountant | W17.11a | CRM-001 |
| CTL-33 | Ensure gift card liability accuracy | D | Monthly gift card liability report with aging; breakage recognized at 24-month inactivity expiry; Finance reviews | Cost Accountant | W28.10–11 | POS-015 |
| CTL-34 | Ensure complete tax compliance | D | Monthly VAT, EWT, and statutory contribution reconciliation; quarterly BIR filing review; annual income tax preparation | Tax Accountant / CFO | W9A.16, W10.11 | FIN-008, HR-002 |
| CTL-35 | Ensure budget adherence | D | Monthly budget vs. actual variance report; PO and capex creation checks budget availability; > 10% variance requires explanation | Controller / Department Heads | W26.10–11 | FIN-012 |

## C6. Operational Process Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-36 | Ensure recall execution | P | System blocks recalled items at POS; ecommerce auto-removes; store quarantine tracked; recall coverage measured | VP Merchandising | W29.5–7 | INV-016 |
| CTL-37 | Ensure warranty claim validity | D | System verifies warranty period from original transaction; defect documented with photos; SLA tracking on vendor response | CSR / Buyer | W33 | POS-019 |
| CTL-38 | Ensure consignment settlement accuracy | D | System auto-records sell-through at POS; monthly settlement report confirmed by Buyer before payment; period-end accrual for sold-but-unsettled | Buyer / Cost Accountant | W23.6–9, W23.6a | FIN-018, INV-017 |
| CTL-39 | Ensure vendor rebate accuracy | D | System auto-accrues rebates at purchase/sale; monthly Cost Accountant validates against agreement; Buyer confirms settlement before payment | Cost Accountant / Buyer | W27.3–9 | FIN-019, PUR-015 |
| CTL-40 | Ensure emergency procurement regularization | D | Emergency procurements must be formalized within 5 business days; system auto-escalates if not; monthly Controller review of emergency procurement frequency | Controller | W60.6–7 | PUR-001 |
| CTL-41 | Ensure LGU permit compliance | D | System alerts 60 days before permit expiry; expired permits escalated; locations blocked if permits lapse (operational risk) | Regulatory Officer | W54.2, W54.10 | NFR-017 |

---

## C7. Vendor & Customer Master Data Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-42 | Prevent vendor payment fraud via bank account change | P | All vendor bank account detail changes require out-of-band verification (phone call to known contact, not the change request itself); dual approval (AP Clerk entry + AP Supervisor approval); 48-hour cooling-off period before first payment to new account; first payment flagged for Treasury confirmation of receipt; full audit trail of old/new bank details, verifier, approver, and timestamp | AP Clerk / AP Supervisor / Treasury | W36.7a | PUR-003, NFR-007 |
| CTL-43 | Prevent Sales Rep self-approval of credit limits on own accounts | P | System enforces that the Sales Rep assigned to a trade/corporate account cannot also be the credit approver for that same account; credit limit approval follows the standard W24 tiered matrix (AR Supervisor / Finance Manager / Credit Committee); if Sales Rep requests a credit limit increase, system routes approval directly to AR Supervisor (bypassing the requesting Sales Rep); quarterly: Internal Audit samples credit approvals to verify no self-dealing occurred | AR Supervisor / Finance Manager | W24, W58 | CRM-003, CRM-008 |
| CTL-44 | Detect and prevent duplicate vendor payments | P | System auto-detects duplicate vendor invoices by invoice number, vendor+amount+date, and PO reference+invoice number; blocks duplicates with AP Clerk alert; AP Clerk investigates and either rejects or overrides with documentation; monthly override log reviewed by AP Supervisor | AP Clerk / AP Supervisor | W7 | FIN-020 |
| CTL-45 | Ensure layaway deposit safeguarding | P | Layaway deposits recorded as liability (not revenue) until item release; inventory reserved and excluded from ATP; cancellation fee configurable with approval; forfeiture requires Store Manager approval; monthly liability report reviewed by Store Manager and Regional Manager | Store Manager / Regional Manager | W75 | POS-020 |
| CTL-46 | Ensure loyalty fraud investigation and resolution | D | LPO flags suspected loyalty fraud patterns per W37; Loyalty Manager investigates within 2 business days; confirmed fraud results in account suspension with customer notification; points deducted per approval tier; monthly fraud resolution summary reviewed by Loyalty Manager; permanent ban requires Marketing Head approval | Loyalty Manager / LPO | W17, W37 | CRM-001, NFR-007 |
| CTL-47 | Ensure ecommerce payment reconciliation accuracy | D | Daily reconciliation of payment gateway settlements (PayMongo, GCash, etc.) to ecommerce order records; gateway fees verified against contracted rates; unreconciled settlements investigated by Treasury Analyst; monthly ecommerce payment reconciliation included in bank reconciliation (W89) | Treasury Analyst / Controller | W19, W30, W89, W99 | ECOM-006, FIN-009 |
| CTL-48 | Ensure vendor rebate dispute resolution | D | If vendor disputes rebate settlement amount, Buyer negotiates resolution; Category Manager approves any adjustment; if unresolved, Finance Manager mediates; adjusted settlement posted with Category Manager approval and documentation; rebate dispute frequency tracked in vendor scorecard (W44) | Buyer / Category Manager | W27 | FIN-019 |
| CTL-49 | Prevent unauthorized gift card balance manipulation | P | All manual gift card balance adjustments (corrections, reloads without payment, balance transfers) require dual approval: Store Manager initiates and AP Supervisor approves; system logs adjustment with original balance, new balance, initiator ID, approver ID, reason code, and timestamp; monthly: AP Supervisor reviews gift card adjustment log as part of AP controls review; gift card fraud detection rules monitored by LPO per W37 | Store Manager / AP Supervisor | W28, W37 | POS-015 |

## C8. Master Data Governance Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-50 | Prevent unauthorized master data changes | P | All MDM changes require approval per tier: creation by Data Steward, approval by MDM Manager; critical masters (financial COA, tax codes, exchange rates) require Finance approval; emergency changes allowed with next-day validation; full audit trail per W291 | MDM Manager / Finance | W252–W316 | MDM-001–MDM-025 |
| CTL-51 | Detect stale or incomplete master data | D | W291 runs weekly completeness checks on mandatory fields across all master domains; stale-data flags raised for items with no transaction in 180 days, vendors with expired permits, and customers with no activity in 365 days; quarterly MDM Manager reviews dashboard and initiates cleanup | MDM Manager | W291 | MDM-010 |
| CTL-52 | Ensure UOM conversion accuracy | P | UOM conversions locked after Finance approval; changes require dual sign-off (Data Steward + Cost Accountant); system prevents deletion of in-use UOM conversions; quarterly audit of conversion accuracy for high-volume catch-weight items | Cost Accountant / MDM Manager | W294 | MDM-013 |
| CTL-53 | Ensure pricing master integrity | D | System validates pricing hierarchy rules on every change (W289); price gap analysis flags discrepancies > 20% between hierarchy levels; override audit trail reviewed monthly by Category Manager; pricing master change log archived per W256 | Category Manager / MDM Manager | W289, W107 | MDM-005, RPT-012 |
| CTL-54 | Prevent unauthorized employee master data changes | P | Employee master changes (department, position, salary grade) require HR Manager approval; cross-entity transfers require both entity HR Managers; system enforces position-based access provisioning per W292; IT access lifecycle triggered by position change per W152 | HR Manager / MDM Manager | W292 | MDM-011, HR-001 |
| CTL-55 | Ensure tax & regulatory master data accuracy | D | Tax code changes (VAT rates, EWT ATC codes, BIR form mappings) require Tax Accountant validation before activation; quarterly reconciliation of tax master to current BIR regulations; W293 change log reviewed by Tax Accountant monthly | Tax Accountant / MDM Manager | W293 | MDM-012, FIN-008 |
| CTL-56 | Ensure barcode/GTIN master consistency | D | System validates GTIN check digits on entry; duplicate barcode detection across active SKUs; vendor barcode verification at goods receipt (W3) against master records per W311; quarterly GS1 prefix audit | MDM Manager | W311 | MDM-020 |
| CTL-57 | Ensure replenishment parameter governance | P | ROP, safety stock, and EOQ parameter changes require Supply Planning Manager approval; seasonal overrides auto-expire per W306 calendar dates; new-store parameter setup validated against cluster benchmarks per W312; quarterly calibration requires sign-off | Supply Planning Manager / MDM Manager | W312 | MDM-021, SCP-003 |
| CTL-58 | Ensure product lifecycle status cascade accuracy | D | W315 status transitions enforce prerequisites (e.g., cannot set Discontinued with active POs); downstream cascade verified — auto-replenishment stops, planogram positions flagged, promo eligibility removed; quarterly audit of blocked/quarantine items with no resolution | MDM Manager / Category Manager | W315 | MDM-024 |

## C9. Treasury & Corporate Finance Controls

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-59 | Prevent unauthorized bank account changes | P | Bank account opening/closure requires CFO approval; signatory changes require dual approval (CFO + Corporate Secretary); system enforces minimum signatory counts per bank per entity; 48-hour cooling-off on new online banking credentials per W320; full audit trail per W317 | CFO / Corporate Secretary | W317 | FIN-009, NFR-007 |
| CTL-60 | Ensure investment policy compliance | P | Surplus cash investments limited to approved instruments (government securities, time deposits with PDIC banks); placement > PHP 10M requires CFO approval; > PHP 50M requires CEO approval; maturity ladder monitored weekly per W318 | Treasury Manager / CFO | W318 | FIN-010 |
| CTL-61 | Ensure debt covenant monitoring | D | W319 tracks all covenant ratios (D/E, interest coverage, current ratio) with automated quarterly computation; covenant breach triggers immediate CFO notification; monthly dashboard reviewed by Treasury Manager; all covenant certificates filed per W255 | Treasury Manager / CFO | W319 | FIN-010 |
| CTL-62 | Ensure electronic banking security | P | W320 enforces dual-authorization for all electronic payments (maker/checker); payment file formats validated against bank templates; daily payment limits enforced per entity per bank; USB token / OTP required for payment authorization; monthly security audit of user access logs | Treasury Manager / CFO | W320 | NFR-007, FIN-009 |
| CTL-63 | Ensure FX exposure reporting accuracy | D | W321 consolidates FX exposure from import POs (W2B), LC obligations (W232), and intercompany balances (W14); monthly BSP regulatory report validated by Treasury Analyst; hedge effectiveness tested quarterly; unrealized FX gains/losses reconciled at month-end per W326 | Treasury Analyst / CFO | W321 | FIN-014, FIN-021 |
| CTL-64 | Ensure cash pooling integrity | D | W323 cash concentration sweeps validated daily — target balances verified before sweep execution; inter-entity pool balances reconciled at month-end; sweep exceptions investigated by Treasury Analyst; zero-balance structures verified per entity per bank | Treasury Analyst / Treasury Manager | W323 | FIN-010 |
| CTL-65 | Ensure corporate guarantee tracking | D | W325 maintains register of all guarantees with beneficiary, amount, expiry, and contingent liability classification; PFRS/PAS 37 disclosure report generated quarterly; guarantee renewal requires Legal review per W230 and CFO approval; expired guarantees auto-archived | Treasury Manager / Legal | W325 | FIN-010 |
| CTL-66 | Ensure treasury month-end close accuracy | D | W326 treasury close performed after entity-level financial close (W9A); bank position reconciled to GL; inter-entity pool balances agreed to IC reconciliation (W14); FX revaluation validated against W321 exposure; Treasury Manager signs off | Treasury Manager / Controller | W326 | FIN-015, FIN-009 |
| CTL-67 | Ensure dividend declaration compliance | P | W327 dividend declaration requires Board resolution; statutory withholding on dividends computed per Philippine tax law; dividend payment executed only after BIR withholding remittance confirmed; Corporate Secretary maintains dividend register | CFO / Corporate Secretary | W327 | FIN-008, IC-004 |

## C10. Gap-Analysis Domain Controls — Plan & Source

One anchor control per gap-analysis value stream (VS-89–VS-192); each is exercised at the specific
workflows listed and backfilled into those workflows' Controls sections by
`07-methodology/backfill-controls.py`.

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-68 | Ensure cooperative vendor qualification & settlement integrity | D | Cooperative onboarding requires CDA registration and capability certification; quality inspection gates acceptance; livelihood settlements paid only against verified delivered-and-accepted quantities | Community Sourcing Manager | W3115, W3118, W3122, W3125, W3126 | PUR-003, MDM-004 |
| CTL-69 | Ensure merchandise financial plan & OTB discipline | D | Receipts committed only against open-to-buy; markdown spend authorized against budget allocation; weekly plan-vs-actual variance reviewed with reforecast; annual audit of markdown/OTB compliance | Merchandise Financial Planning Director | W3283, W3284, W3285, W3288, W3303 | MER-008, FIN-012 |
| CTL-70 | Ensure commodity exposure & hedge accounting accuracy | D | Commodity value-at-risk measured against approved risk appetite; hedge effectiveness tested with PFRS 9 mark-to-market reconciled monthly; pass-through price actions approved per governance matrix | Commodity Risk Manager | W3404, W3406, W3413, W3417, W3419 | FIN-021, PUR-010 |
| CTL-71 | Ensure import sourcing & social-compliance verification | D | Import vendors qualified with factory and social-compliance audits; sourcing-agent authority bounded by policy; tariff/sanctions screening at PO; total landed cost reconciled to estimates | Global Sourcing Director | W3786, W3790, W3791, W3792, W3795, W3798 | FIN-013, PUR-003 |
| CTL-72 | Ensure S&OP consensus & financial reconciliation | D | Monthly demand-supply consensus signed with unconstrained items escalated; inventory and replenishment plans reconciled to approved S&OP; financial tie-out (revenue/margin/inventory budget) verified before publication | S&OP/IBP Lead | W3905, W3914, W3916, W3921, W3925, W5496 | SCP-003, FIN-012 |
| CTL-73 | Ensure human-rights supply-chain due diligence | D | Salient risks assessed and suppliers tiered; modern-slavery and recruitment-fee controls verified at audit; corrective actions tracked to closure with performance publicly reported | Responsible Sourcing Manager | W4001, W4002, W4006, W4007, W4008, W4009 | GOV-008, PUR-003 |
| CTL-74 | Ensure indent import quality & document control | D | Factory vetting and pre-shipment inspection gate shipment release; LC documents verified with discrepancy audit before bank release; production progress verified weekly against schedule | Indent Sourcing Manager | W5226, W5231, W5232, W5234, W5235, W5237 | FIN-013, DOC-004 |

## C11. Gap-Analysis Domain Controls — Make & Move

One anchor control per gap-analysis value stream (VS-89–VS-192); each is exercised at the specific
workflows listed and backfilled into those workflows' Controls sections by
`07-methodology/backfill-controls.py`.

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-75 | Detect and recover freight & receiving damage | D | Damage documented with photo evidence at receipt; claims filed within vendor/carrier windows with aging tracked to scorecard; monthly recovery rate reviewed; refunds and credits reconciled to GL | Logistics Claims Coordinator | W3019, W3024, W3029, W3032, W3036 | PUR-011, LP-007 |
| CTL-76 | Ensure kit build & component inventory integrity | D | Build verification at pack-out with component lot/serial inherited to the kit; periodic kit-vs-component reconciliation with variance investigation; discontinuation recovers components to sellable stock | DC Operations Manager | W3072, W3075, W3076, W3077 | INV-006, MDM-020 |
| CTL-77 | Ensure dark-store order accuracy & dispatch control | D | Pick/pack accuracy sampled daily with right-box verification at pack station; dispatch reconciled to wave plan before carrier handoff; returns reverse-putaway matched to original orders | Dark Store Operations Manager | W3098, W3099, W3104, W3109 | ECOM-006, INV-006 |
| CTL-78 | Ensure freight invoice accuracy & carrier compliance | D | Freight invoices audited against contract rates and delivery records before payment; routing-guide compliance measured per lane; carrier insurance and regulatory documents current | Freight & Logistics Manager | W3500, W3502, W3504, W3508, W3511, W3513 | PUR-011, FIN-020 |
| CTL-79 | Ensure RTI & pallet asset reconciliation | D | Returnable transport items (totes/cages/pallets) tracked per movement with periodic pool reconciliation; vendor non-compliance charged back per agreement; pool-provider settlements reconciled to counts | Packaging & RTI Manager | W3521, W3527, W3531, W3534, W3536 | WMS-019, INV-014 |
| CTL-80 | Ensure inventory parameter & network optimization governance | D | Replenishment parameters changed only per governance with scenario validation; obsolescence risk monitored with provisioning triggers; network KPIs tracked against the design case | Network Design Lead | W4127, W4134, W4135, W4137, W4141 | SCP-003, INV-011 |
| CTL-81 | Ensure bulky delivery compliance & e-POD closure | D | Crew certified and authorized before dispatch; customer acceptance captured by electronic proof-of-delivery before revenue confirmation; refrigerant recovery and EPR recycling documented per event | Last-Mile Operations Manager | W4292, W4293, W4301, W4306, W4309 | WSL-008, SRV-005 |
| CTL-82 | Ensure trade-in device integrity & data wipe | P | Intake safety screen and certified data wipe performed before resale listing; grading and certification evidenced per unit; non-certified units routed to harvest/recycle with proceeds posted | Certified Resale Operations Manager | W4581, W4586, W4589, W4590, W4591 | NFR-010, INV-006 |
| CTL-83 | Ensure calamity pricing & relief-channel compliance | P | State-of-calamity triggers activate price-freeze monitoring with DTI compliance reporting; fast-track POs and direct-to-store deliveries documented per emergency authority; LGU fee deferrals and permits cleared | Disaster Response Coordinator | W5181, W5182, W5185, W5187, W5188, W5190 | GOV-030, SCP-016 |
| CTL-84 | Ensure C&D debris chain-of-custody | D | Weighbridge tickets captured per load against manifests; DENR-compliant transporter permits verified; demurrage and scrap/rebate recovery billed; diversion documented for ESG reporting | Debris Operations Manager | W5445, W5451, W5452, W5456, W5457, W5460 | GOV-008, ESG-008 |
| CTL-85 | Ensure green-fleet EVIDA & MRV compliance | D | EVIDA registration/incentive and DOE/LTO/LTFRB filings current per vehicle; charging load matched to on-site generation per the demand-response plan; Scope-1 GHG MRV reported with verified data; driver/technician certification tracked | Green Fleet Program Manager | W5470, W5471, W5479, W5481, W5482, W5484 | GOV-007, ESG-008 |

## C12. Gap-Analysis Domain Controls — Sell & Serve

One anchor control per gap-analysis value stream (VS-89–VS-192); each is exercised at the specific
workflows listed and backfilled into those workflows' Controls sections by
`07-methodology/backfill-controls.py`.

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-86 | Ensure marketplace seller & tax compliance | D | Seller onboarding requires business registration and DPA; counterfeit/policy violations trigger takedown with evidence retained; per-seller VAT/percentage-tax reporting reconciled to BIR filings | Marketplace Operations Manager | W3147, W3156, W3157, W3159 | FIN-006, ECOM-006 |
| CTL-87 | Ensure key-account credit concentration & ethics governance | D | Account credit and concentration reviewed quarterly against limits; quarterly-business-review commitments tracked to delivery; entertainment/gifts and conflicts registered per ethics policy | Key Account Director | W3430, W3432, W3444, W3446 | CRM-003, GOV-013 |
| CTL-88 | Ensure selling-quality & training integrity | D | Product-knowledge certification current per associate with recertification cycle; mystery-shopping and interaction audits sampled against standards; vendor training content approved before use | Sales Enablement Manager | W3833, W3842, W3847, W3848, W3854 | GOV-016, GOV-050 |
| CTL-89 | Ensure event compliance & asset recovery | D | Event permits and promo-prize governance cleared before activation; vendor co-funding reconciled to commitments; teardown assets recovered and reconciled to inventory | Field Marketing Manager | W4197, W4198, W4207, W4214, W4216 | MKT-004, GOV-010 |
| CTL-90 | Ensure field-sales conduct & pipeline integrity | D | Route and call plans verified by GPS telemetry with coverage adherence measured; field pricing within delegated authority; ABC and data-quality compliance audited in-field | Field Sales Director | W4225, W4229, W4232, W4236 | CRM-003, GOV-013 |
| CTL-91 | Ensure live-goods compliance & inventory accuracy | D | Phytosanitary and BPI/FPA permits current per grower and chemical; restricted-species sales blocked without clearance; live-goods cycle counts with shrink reconciled to markdown/compost disposition | Garden Center Category Manager | W4338, W4347, W4355, W4356, W4357, W4358 | INV-006, GOV-008 |
| CTL-92 | Ensure self-checkout loss & compliance control | D | SCO interventions (age-restricted, hazmat) enforced with attendant authorization; session reconciliation with variance investigation; swap/sweethearting fraud detection monitored; BIR CAS and price-tag compliance audited | Store Operations Technology Manager | W4438, W4443, W4444, W4449, W4452, W4453 | POS-009, NFR-007 |
| CTL-93 | Ensure VAS agency cash & BSP compliance | D | KYC verification per transaction with limits enforced; VAS cash counted and reconciled end-of-day under dual custody; principal settlement and float reconciled; suspicious/cash-transaction reports filed per AML rules | VAS Operations Manager | W4605, W4613, W4614, W4617, W4619, W4620 | FIN-006, NFR-007 |
| CTL-94 | Ensure rental fleet safety & settlement integrity | D | Driver license/eligibility verified at rental with telematics monitoring for misuse; return inspection gates re-release with damage recovery; deposits released per settlement terms | Rental Operations Manager | W4747, W4749, W4750, W4754, W4759, W4760 | POS-020, GOV-007 |
| CTL-95 | Ensure locker network custody & uptime | D | Locker access events reconciled to parcel custody with exception handling; uptime/SLA reported with vendor governance; abandoned parcels cleared per policy; PWD accessibility maintained | Smart Locker Network Manager | W4796, W4797, W4800, W4808, W4812, W4814 | ECOM-016, NFR-007 |
| CTL-96 | Ensure music-licensing & audio compliance | D | FILSCAP/OPM licenses current with usage reporting and royalty true-up; equipment health monitored per site; volume zones and price-integrity/voice-privacy compliance audited | In-Store Media Manager | W4891, W4896, W4898, W4900, W4908, W4909 | GOV-019, NFR-010 |
| CTL-97 | Ensure will-call release integrity & loading safety | D | Release authorized against the order with identity verification and fraud controls; forklift operators qualified with equipment inspection per DOLE OSH; hold-expiry restocking posted timely | Will-Call Operations Manager | W4973, W4978, W4980 | CRM-003, GOV-004 |
| CTL-98 | Ensure installer-network vetting & referral integrity | D | Installers vetted (PCAB license, insurance) before network admission with periodic re-verification; referral fees settled only per verified milestones; workmanship inspected with corrective actions tracked | Pro Network Manager | W4987, W4992, W4997, W4998, W5003 | SRV-005, GOV-005 |
| CTL-99 | Ensure storage lien & prohibited-goods control | D | Unit access logged with audit trail; prohibited/hazardous items screened at move-in with enforcement; abandoned-unit lien sales per regulatory procedure; damage assessed at move-out before deposit settlement | Self-Storage Operations Manager | W5043, W5046, W5047, W5051, W5052 | GOV-004, POS-020 |
| CTL-100 | Ensure LPG cylinder safety & deposit accounting | D | Cylinder fleet tracked per serial with leak/damage inspection and condemnation quarantine; DOE accreditation and metrology current; daily safety inspection per BFP; deposit float and shrink reconciled | LPG Program Manager | W5059, W5060, W5063, W5069, W5073, W5074 | HAZ-006, POS-020 |
| CTL-101 | Ensure reprographics IP & file-handling control | D | Customer documents handled per copyright and sensitive-document policy with version control; print quality dimensionally verified per job; stored files purged per retention and consent | Reprographics Services Manager | W5087, W5090, W5093, W5097, W5101 | NFR-010, DOC-010 |
| CTL-102 | Ensure field retail-standards execution | D | Store-visit audits scored against retail standards (planogram, price, signage); action items tracked to closure; multi-store P&L governance with tiering review; Regional-Manager certification current | Regional Operations Director | W5107, W5108, W5109, W5114, W5116, W5118 | GOV-018, MER-001 |
| CTL-103 | Ensure cooperative credit & patronage compliance | D | CDA registration verified annually with credit limits reviewed and renewed; member POS association verified per transaction; patronage-dividend tax certificates issued and accounted | Cooperative Accounts Manager | W5299, W5304, W5305, W5313, W5315, W5318 | CRM-003, FIN-006 |
| CTL-104 | Ensure equipment-rental safety & recovery | D | Operators certified and pre-qualified before handover with pre-rental inspection and safety briefing; telematics misuse detection with intervention; return damage assessed and repair cost recovered | Equipment Rental Operations Manager | W5324, W5326, W5330 | GOV-005, POS-020 |

## C13. Gap-Analysis Domain Controls — Finance

One anchor control per gap-analysis value stream (VS-89–VS-192); each is exercised at the specific
workflows listed and backfilled into those workflows' Controls sections by
`07-methodology/backfill-controls.py`.

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-105 | Prevent unauthorized lease credit extension | P | Lease underwriting per approved credit policy with tiered approval; Truth-in-Lending disclosures on all consumer leases; provisioning reviewed monthly against delinquency tiers | Leasing Credit Manager | W3163, W3171, W3176, W3178, W3182 | CRM-008, POS-020 |
| CTL-106 | Ensure SCF settlement & covenant compliance | D | Approved-payable monetization reconciled to funder settlement daily; facility limits and covenants monitored with breach escalation; discount economics (APR) reconciled monthly | Treasury Manager | W3380, W3382, W3384, W3387, W3388 | FIN-009, FIN-010 |
| CTL-107 | Ensure bond encumbrance & renewal control | D | Register of bonds/guarantees maintained with beneficiary, expiry and encumbrance; renewals initiated ahead of expiry per approval matrix; releases evidenced and archived | Surety Program Manager | W3641, W3646, W3647, W3648, W3654, W3656 | FIN-010, GOV-001 |
| CTL-108 | Ensure revenue leakage detection & recovery | D | Leakage taxonomy monitored across channels with exception thresholds; sales-to-cash and settlement integrity reconciled; recovered leakage posted and reported to the governance committee | Revenue Assurance Manager | W3689, W3690, W3691, W3693, W3694, W3695 | FIN-020, RPT-012 |
| CTL-109 | Ensure cross-channel fraud detection & case governance | D | Fraud rules and models tuned under change governance; cases investigated within SLA with loss recovery tracked; model performance and false-positive rates reviewed monthly | Fraud Management Director | W3857, W3858, W3859, W3860, W3861, W3862 | NFR-007, MKT-001 |
| CTL-110 | Ensure COD cash-chain integrity | D | COD limits enforced per risk tier at order capture; driver custody under segregation of duties with sealed-bag evidence; daily cash-vs-order reconciliation with bank deposit verification to GL | COD Operations Manager | W4266, W4269, W4270, W4271, W4277, W4279 | POS-009, FIN-009 |
| CTL-111 | Ensure PFRS 16 lease-accounting completeness | D | Lease portfolio identified with complete abstracts; ROU-asset and liability schedules reconciled at period-end; modifications and reassessments re-measured with disclosure review; audit trail maintained | Lease Accounting Manager | W4419, W4425, W4426, W4428, W4430, W4432 | FIN-015, IC-004 |
| CTL-112 | Ensure captive risk-transfer adequacy | D | Captive licensed and governed per domicile with investment policy; underwriting guidelines and risk acceptance enforced; risk-transfer testing documented with reinsurance/commutation tracked | Risk Financing Manager | W4529, W4530, W4531, W4533, W4537, W4541 | FIN-010, INS-006 |
| CTL-113 | Ensure construction-finance brokerage compliance | P | Brokerage/referral accreditation current per partner lender; anti-predatory standards and disclosures enforced; draw milestones verified against progress before release; BSP/consumer reporting filed | Construction Finance Manager | W4555, W4557, W4565, W4571, W4573, W4574 | CRM-008, GOV-013 |
| CTL-114 | Ensure PFRS 15 recognition & cut-off control | D | Over-time vs point-in-time assessment documented per contract; contract-liability/asset and AR reconciled with cut-off testing at close; standalone-selling-price evidence retained; audit sampling supported | Revenue Accounting Manager | W4632, W4644, W4647, W4648 | FIN-003, RPT-012 |
| CTL-115 | Ensure cost-master & COGS reconciliation control | D | Cost-master changes per approval matrix with change log; COGS reconciled and cut-off matched monthly; project/job costs absorbed per policy with variance thresholds investigated | Cost Accounting Manager | W4663, W4665, W4670, W4672 | INV-003, FIN-013 |
| CTL-116 | Ensure borrowing-base & covenant compliance | D | Borrowing-base certificates prepared from reconciled inventory/AR data and submitted per frequency; field-exam findings remediated with true-downs; covenant ratios monitored with breach escalation | ABL Facility Manager | W4937, W4939, W4942, W4943, W4944, W4945 | FIN-010, FIN-009 |
| CTL-117 | Ensure disclosure & insider-trading compliance | P | Materiality assessed with fair-disclosure controls on releases; insider list and trading windows enforced per the Securities Regulation Code; rumor-response protocol activated; disclosure-committee sign-off before publication | Investor Relations Officer | W5017, W5018, W5019, W5021, W5022, W5024 | GOV-038, GOV-001 |
| CTL-118 | Ensure escrow draw & lien-release control | D | Escrow funding verified before release; delivery receipts matched to bank-inspector joint-quantity-survey quantities; deviations clarified and documented; lien releases issued only after settled delivery evidence | Project Escrow Manager | W5205, W5206, W5208, W5209, W5210, W5212 | CRM-003, FIN-009 |
| CTL-119 | Ensure floor-plan collateral control | D | Dealer stocking lists reconciled to physical audit with unit-level serial/VIN tracking; disbursements dual-payee to the vendor; curtailments enforced per sale; BSP and Truth-in-Lending disclosures maintained | Floor-Plan Finance Manager | W5369, W5372, W5374, W5376, W5378, W5379 | CRM-008, POS-020 |
| CTL-120 | Ensure factoring settlement & dilution control | D | Drawdowns posted with bank reconciliation; dilution (discounts, short-pays) reconciled with reserve release per agreement; recourse buybacks executed at expiry; pool reports to trustee/investors reconciled | Receivables Finance Manager | W5400, W5402, W5405, W5406, W5407, W5408 | FIN-009, CRM-003 |

## C14. Gap-Analysis Domain Controls — People

One anchor control per gap-analysis value stream (VS-89–VS-192); each is exercised at the specific
workflows listed and backfilled into those workflows' Controls sections by
`07-methodology/backfill-controls.py`.

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-121 | Ensure lawful contracting & worker classification | P | Service agreements structured against DOLE D.O. 174 labor-only-contracting tests; classification risk assessed before engagement; contractor workers covered by insurance/bonding with safety orientation before site work | HR Compliance Manager | W3211, W3214, W3215, W3219 | GOV-047, HSE-003 |
| CTL-122 | Ensure pay equity & statutory benefits compliance | D | Multi-region minimum-wage compliance validated per wage order; pay-equity analysis run annually with gaps explained; SSS/PhilHealth/Pag-IBIG contributions reconciled and remitted per statutory calendar | Total Rewards Director | W3310, W3312, W3313, W3314, W3327 | HR-002, HR-044 |
| CTL-123 | Ensure HR service delivery & people-data accuracy | D | HR service-center SLA and CSAT monitored with quality sampling; employment verifications and letters issued from verified records only; people-analytics dashboards reconciled to system-of-record headcount | HR Shared Services Manager | W3334, W3336, W3346, W3348, W3349 | HR-001, MDM-010 |
| CTL-124 | Ensure lawful & consented candidate data handling | P | Recruitment consent captured per RA 10173 with data-minimized retention; equal-opportunity monitoring on hiring funnels; agency/channel spend governed against budget | Talent Acquisition Director | W3768, W3782, W3783, W3784 | NFR-010, HR-044 |
| CTL-125 | Ensure apprenticeship statutory compliance | D | TESDA program registration and dual-training agreements current; stipends and DOLE labor terms enforced; trainee logs and assessments evidenced before certification | Workforce Development Manager | W3811, W3812, W3813, W3815, W3819, W3821 | HR-001, GOV-047 |
| CTL-126 | Ensure change adoption & sustainment | D | Change risks assessed per initiative with mitigation owners; adoption and process-compliance measured post-go-live; benefit realization tracked against the change case | Change Management Lead | W4073, W4078, W4092, W4094, W4095 | GOV-009, GOV-016 |
| CTL-127 | Ensure employee-transport compliance & vendor settlement | D | Shuttle vendors' LTFRB franchise and insurance documents current with a vehicle-inspection registry; monthly invoices reconciled to trips and rosters; DOLE transport standards audited | Employee Transport Manager | W4247, W4259, W4260, W4264 | GOV-007, GOV-047 |
| CTL-128 | Ensure dormitory safety & welfare compliance | D | BFP fire/life-safety inspections current per dormitory; occupancy per allocation policy with visitor access controlled; cost recovery reconciled to payroll deductions monthly | Housing & Welfare Manager | W4318, W4319, W4325, W4331, W4333 | GOV-004, HR-001 |
| CTL-129 | Ensure drug-free workplace program compliance | P | Safety-sensitive roles identified with testing per DOLE D.O. 53-04; certified collection/lab/MRO chain of custody maintained; confidentiality and rehabilitation referral governed; random selection documented | Occupational Health Manager | W4457, W4458, W4459, W4460 | GOV-004, HR-002 |
| CTL-130 | Ensure immigration & foreign-worker compliance | D | AEP/visa categories validated per assignment with expiry calendar; mobility vendors governed per SLA; compliance KPIs and risk register reviewed; cross-border travel-risk linkage enforced | Global Mobility Manager | W4700, W4703, W4704, W4705, W4707, W4709 | GOV-047, HR-001 |
| CTL-131 | Ensure lawful & consented personnel vetting | P | Screening scope per role with RA 10173 consent and data minimization; adverse-action review board with appeals before decisions; periodic re-screening by trigger; agency accountability for contingent workers | Background Screening Program Manager | W4868, W4871, W4872, W4874, W4877, W4879 | NFR-010, HR-001 |
| CTL-132 | Ensure PPE issuance & DOLE compliance | D | PPE entitlement tracked per role with inspection/replacement cycle; usage audited to DOLE standards; separation returns recovered; vendor SLA governed | Uniform & PPE Program Manager | W4920, W4925, W4928, W4930, W4931 | GOV-004, HR-001 |
| CTL-133 | Ensure DTS/TESDA training compliance | D | DTS accreditation and site inspections current; biometric attendance and trainee logbooks verified against output; monthly TESDA compliance reports submitted on time | DTS Program Manager | W5249, W5256, W5257, W5258, W5263, W5267 | HR-001, GOV-047 |

## C15. Gap-Analysis Domain Controls — Asset & Infrastructure

One anchor control per gap-analysis value stream (VS-89–VS-192); each is exercised at the specific
workflows listed and backfilled into those workflows' Controls sections by
`07-methodology/backfill-controls.py`.

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-134 | Ensure property income & LGU tax compliance (as owner) | D | Tenant rent, CAM and escalations billed per lease abstract with monthly receivable reconciliation; real property tax assessed and paid per LGU calendar; NOI reconciled to portfolio P&L | Property Portfolio Manager | W3195, W3197, W3201, W3202 | REG-002, IC-005 |
| CTL-135 | Ensure renewable asset registration & net-metering settlement | D | ERC/DU interconnection and net-metering registrations current per site; export/import settlement reconciled to utility billing monthly; generation performance surveilled with underperformance investigation | Renewable Energy Operations Manager | W3456, W3457, W3462, W3463, W3464 | ESG-006, GOV-008 |
| CTL-136 | Ensure remodel capex & handover control | D | Remodel spend tracked against approved capex with variance escalation; permits secured before works; snag-list closure and commissioning verified before handover; post-remodel sales lift tracked against business case | Store Development Director | W3476, W3479, W3488, W3493, W3496 | FIN-016, ENG-002 |
| CTL-137 | Ensure project portfolio approval & cost control | D | Projects registered and approved per stage-gate with business case; budget committed and incurred tracked with tiered variance escalation; portfolio dashboards reported to executives and Board | PMO Director | W3545, W3546, W3550, W3551, W3552, W3555 | FIN-016, PRJ-001 |
| CTL-138 | Ensure RA 11285 energy compliance & M&V integrity | D | Designated-establishment registration current with DOE; mandatory energy audits completed by accredited firms; energy-conservation-measure savings verified by measurement and verification against baseline | Energy Manager | W3737, W3738, W3743, W3745, W3746, W3747 | ESG-006, GOV-008 |
| CTL-139 | Ensure facilities compliance & vendor performance | D | Fire/life-safety and statutory permits current per site with inspection cadence; IFM vendor SLA measured with penalty application; environmental conditions (HVAC, lighting) monitored to standard | Facilities Management Director | W4175, W4176, W4178, W4186 | GOV-004, GOV-048 |
| CTL-140 | Ensure EV-charging uptime & tariff compliance | D | EVSE health monitored with SLA/uptime reporting and penalty administration; PWD-accessible bays maintained; host-revenue settlement reconciled to charge-point-operator records; ERB/LGU/RA 11697 compliance audited | EV Network Operations Manager | W4776, W4785, W4788, W4789, W4790, W4791 | GOV-019, FIN-009 |
| CTL-141 | Ensure land title & acquisition due diligence | D | Title verification and lien/arrears search before acquisition; boundary surveys and technical descriptions validated; NCIP ancestral-domain clearance where required; Registry of Deeds transfer completed and registered | Landbanking Manager | W5130, W5131, W5132, W5133, W5135, W5138 | GOV-003, PROP-001 |
| CTL-142 | Ensure post-disaster recovery & insurance substantiation | D | Loss-adjuster audits coordinated with proof of loss submitted within policy windows; settlements negotiated with recovery accounting posted; rebuilding budget approved before execution; LGU structural clearance before reopening | Reconstruction Program Manager | W5273, W5276, W5278, W5281, W5282, W5286 | INS-002, ENG-002 |

## C16. Gap-Analysis Domain Controls — Technology & Data

One anchor control per gap-analysis value stream (VS-89–VS-192); each is exercised at the specific
workflows listed and backfilled into those workflows' Controls sections by
`07-methodology/backfill-controls.py`.

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-143 | Ensure IT asset & license entitlement integrity | D | Discovered assets reconciled to CMDB monthly; license entitlements vs. deployed counts reconciled before vendor true-up; lost/stolen assets investigated with remote-wipe evidence retained | IT Asset Manager | W3233, W3240, W3241, W3242, W3245, W3246 | NFR-007, DOC-004 |
| CTL-144 | Ensure architecture standards & exception control | D | New systems and changes assessed against approved technology standards; exceptions time-boxed with waiver approval; architecture risk and resilience design reviewed at investment gates | Chief Enterprise Architect | W3569, W3572, W3573, W3586, W3588, W3590 | NFR-007, GOV-009 |
| CTL-145 | Ensure measurement traceability & weights-and-measures compliance | D | Every scale/device on the calibration registry with traceable standards; out-of-tolerance devices quarantined and transaction-impact assessed; DTI weights-and-measures inspections passed and documented | Metrology Manager | W3617, W3620, W3623, W3624, W3633 | INV-003, GOV-019 |
| CTL-146 | Ensure consented single-customer-view governance | D | Identity-resolution accuracy measured with merge/split audit trail; consent state enforced downstream across channels; CDP access governed with DPIA maintained | Customer Data Platform Owner | W3881, W3885, W3888, W3901, W3903 | NFR-010, CRM-001 |
| CTL-147 | Ensure AI model risk & human-oversight control | P | Model inventory tiered by risk with independent validation before deployment; fairness and explainability tested per tier; human override retained on consequential decisions; vendor and open-source models governed | AI Governance Lead | W3929, W3930, W3931, W3932, W3934, W3939 | NFR-010, GOV-009 |
| CTL-148 | Ensure technology spend & license optimization | D | Technology spend mapped to cost towers with showback; SaaS utilization vs. entitlement reconciled before renewal; shadow-IT spend identified and regularized or terminated | TBM / FinOps Manager | W4104, W4110, W4112, W4113, W4117, W4118 | FIN-012, NFR-007 |
| CTL-149 | Ensure product content accuracy & rights compliance | D | Channel-critical content completeness enforced per standard with vendor SLA; SDS and regulatory certificates current per SKU; digital-asset usage rights and brand approvals verified before publication | PIM / DAM Manager | W4147, W4152, W4155, W4157, W4165, W4168 | MDM-010, HAZ-005 |
| CTL-150 | Ensure labeling & Auto-ID data integrity | D | GTIN/serial/expiry data model enforced at label issuance; regulatory labeling (price tag, DG/SDS, energy) verified per channel; label application reconciled to print runs; EAS tag reuse reconciled | Auto-ID Operations Manager | W4482, W4487, W4488, W4496, W4500, W4504 | MDM-020, GOV-019 |
| CTL-151 | Ensure OT/ICS cybersecurity posture | D | OT asset inventory maintained with criticality tiering; hardened configuration baselines with change control; OT-IDS monitored with SIEM correlation; vulnerabilities triaged with compensating controls where patching is deferred | OT Security Manager | W5417, W5419, W5420, W5424, W5425, W5427 | NFR-007, GOV-009 |

## C17. Gap-Analysis Domain Controls — Governance & Assurance

One anchor control per gap-analysis value stream (VS-89–VS-192); each is exercised at the specific
workflows listed and backfilled into those workflows' Controls sections by
`07-methodology/backfill-controls.py`.

| Control ID | Control Objective | Type | Control Activity | Owner | Workflows | Req Ref |
|---|---|---|---|---|---|---|
| CTL-152 | Ensure recall regulatory reporting & closure | P | Recall decision notified to DTI/BPS within the statutory window; effectiveness metrics (100% inventory removal, >95% of identifiable customers notified) verified by spot audit before close-out; destruction executed under DENR-compliant disposal with documented trail | Product Safety & Compliance Manager | W2994, W3006, W3008, W3009, W3010 | RCL-004, RCL-006 |
| CTL-153 | Ensure privacy consent, DSAR & processor oversight | D | Lawful basis and consent tracked per processing purpose; data-subject requests fulfilled within NPC timelines; processors governed by DPAs with annual privacy audit; CCTV retention and signage enforced | Data Privacy Officer (DPO) | W3041, W3043, W3044, W3048, W3052 | NFR-010, NFR-016 |
| CTL-154 | Ensure legal matter & IP portfolio control | D | All matters tracked with loss accrual posted per stage; settlements above authority escalated; IP renewals calendared with expiry alerts; contract obligations extracted and tracked to fulfillment | General Counsel | W3261, W3267, W3272, W3274 | GOV-001, GOV-038 |
| CTL-155 | Ensure lawful political engagement & lobbying disclosure | P | Political contributions and lobbying activity pre-approved per policy with public disclosure; election-period protocol enforced per the Omnibus Election Code; gift/interaction logs retained for regulator review | VP Legal & Compliance | W3354, W3360, W3368, W3374 | GOV-013, GOV-048 |
| CTL-156 | Ensure dangerous-goods transport & training compliance | P | DG shipments classified, packaged, documented and carrier-accepted per modal regulation; DG-certified personnel currency tracked; program audited annually with records retained | DG Compliance Manager | W3593, W3596, W3597, W3599, W3600, W3603 | HAZ-006, HAZ-001 |
| CTL-157 | Ensure PS Mark / ICC certification coverage | P | Regulated SKUs blocked from PO and listing without a current PS license or ICC; vendor licenses verified at onboarding and renewal; market-surveillance findings remediated with records retained | Product Compliance Manager | W3665, W3667, W3669, W3670, W3671, W3672 | MER-005, MDM-024 |
| CTL-158 | Ensure whistleblower confidentiality & non-retaliation | P | Anonymous channel operated by an independent provider; cases triaged within SLA with investigation independence; retaliation monitored and sanctioned; regulator/law-enforcement referrals documented | Head of Internal Audit | W3713, W3717, W3719, W3725, W3726, W3727 | GOV-013, NFR-010 |
| CTL-159 | Ensure competition-law conduct | P | Pricing and promotional conduct screened against resale-price-maintenance and collusion risk; competitor interactions and trade-body conduct governed; PCC notification thresholds checked before transactions | Competition Compliance Officer | W3953, W3955, W3956, W3957, W3958, W3959 | GOV-014, GOV-013 |
| CTL-160 | Ensure M&A stage-gate & regulatory clearance | P | Transactions advance only per stage-gate with approval authority; due diligence (financial, ESG, compliance) completed before signing; PCC merger notification filed where thresholds met | Corporate Development Director | W3983, W3990, W3992 | FIN-016, GOV-014 |
| CTL-161 | Ensure election-period & political-contribution compliance | P | Political contributions approved and disclosed per policy; election-period protocol activated per the Omnibus Election Code with employee non-coercion enforced; lobbying registers maintained | VP Legal & Compliance | W4025, W4027, W4028, W4030, W4033 | GOV-013, GOV-048 |
| CTL-162 | Ensure improvement benefit realization | D | Improvement projects gated on a benefit case; realized savings measured against baseline and finance-validated; process-performance control tower monitored with drift triggers | Operational Excellence Director | W4050, W4053, W4063, W4065, W4066 | GOV-009, RPT-012 |
| CTL-163 | Ensure service-quality audit independence | D | Mystery-shop methodology and scoring standardized; auditor independence and ethics enforced; findings validated before store impact; consent and privacy handled per RA 10173 | Service Quality Manager | W4363, W4365, W4367, W4372, W4373, W4374 | GOV-050, NFR-010 |
| CTL-164 | Ensure customer safety & premises-liability control | D | Hazard register maintained with daily inspection; incident reports investigated with corrective action; claims documented with CCTV/evidence preservation; OSH, BFP and local-code compliance audited | Customer Safety Manager | W4386, W4388, W4391, W4393, W4394, W4397 | GOV-004, INS-007 |
| CTL-165 | Ensure CSR / foundation governance & safeguarding | D | Foundation SEC registration and BIR donee status current with PCNC accreditation; fund allocation approved per pillar with disbursements traced; safeguarding and whistleblower linkage active; impact measured per logic model | CSR / Foundation Director | W4505, W4506, W4507, W4508, W4511, W4521 | GOV-001, ESG-008 |
| CTL-166 | Ensure executive-protection & travel-risk control | D | Principal threat profiles reviewed quarterly; GSOC monitoring with incident escalation; travel-risk intelligence briefed with trip approval by risk tier; incident post-mortems fed to the risk register | Corporate Security Director | W4673, W4675, W4676, W4677, W4678, W4679 | GOV-020, BCP-009 |
| CTL-167 | Ensure third-party risk tiering & oversight | D | Third parties tiered by criticality and data access with due diligence at onboarding and periodic reassessment; fourth-party and concentration exposure mapped; risk owners assigned with Board reporting | TPRM Program Owner | W4722, W4724, W4725, W4726, W4727, W4728 | NFR-007, PUR-003 |
| CTL-168 | Ensure PCAB licensing validity & capacity limits | P | PCAB license category and size matched to project scope before bidding; annual renewal tracked with expiry alerts; multi-entity coverage decisions documented; evidence repository kept audit-ready | Contractor Licensing Manager | W4817, W4818, W4819, W4820, W4822, W4823 | GOV-005, GOV-048 |
| CTL-169 | Ensure enterprise license/permit register integrity | D | Unified register of every license/permit with owner and renewal calendar; expiry-risk engine escalates ahead of lapse; evidence repository linked per obligation; regulatory changes impact-assessed to the portfolio | Regulatory Portfolio Manager | W4841, W4842, W4844, W4845, W4846, W4847 | NFR-017, GOV-048 |
| CTL-170 | Ensure EPR recovery & registration compliance | D | Plastic-footprint baseline audited and NSWMC registration current; recovery offsets verified with transport and processor evidence; LGU/MRF and junk-shop network transactions documented to claim level | EPR Program Manager | W5153, W5155, W5158, W5162, W5163, W5164 | ESG-008, GOV-008 |
| CTL-171 | Ensure hazardous-waste take-back compliance | D | DENR-EMB generator/treater registration current; manifests issued per consolidation with licensed transporter and TSD-facility verification; battery storage fire-separated; annual hazardous-waste report filed | Product Stewardship Manager | W5346, W5355, W5360, W5361, W5363, W5364 | HAZ-005, GOV-008 |

---

## Controls Summary by Category

| Category | Preventive Controls | Detective Controls | Total |
|---|---|---|---|
| Authorization & Approval | 8 | 0 | 8 |
| Segregation of Duties | 5 | 0 | 5 |
| Transaction Integrity | 1 | 8 | 9 |
| Asset Safeguarding | 2 | 4 | 6 |
| Financial Reporting | 1 | 6 | 7 |
| Operational Process | 1 | 5 | 6 |
| Vendor & Customer Master Data | 5 | 3 | 8 |
| Master Data Governance | 4 | 5 | 9 |
| Treasury & Corporate Finance | 4 | 5 | 9 |
| Gap-Analysis — Plan & Source | 0 | 7 | 7 |
| Gap-Analysis — Make & Move | 2 | 9 | 11 |
| Gap-Analysis — Sell & Serve | 0 | 19 | 19 |
| Gap-Analysis — Finance | 3 | 13 | 16 |
| Gap-Analysis — People | 4 | 9 | 13 |
| Gap-Analysis — Asset & Infrastructure | 0 | 9 | 9 |
| Gap-Analysis — Technology & Data | 1 | 8 | 9 |
| Gap-Analysis — Governance & Assurance | 9 | 11 | 20 |
| **Total** | **50** | **121** | **171** |

---

*Date: 2026-06-27 (v8 — added C10–C17 Gap-Analysis Domain Controls (CTL-68 to CTL-171, 104 controls): one anchor control per gap-analysis value stream VS-89–VS-192, extending the register beyond the Core workflows. Total controls: 171 (50P/121D). Prior: 2026-06-09 v7 — C8 Master Data Governance (CTL-50–58) and C9 Treasury & Corporate Finance (CTL-59–67).)*
