# Treasury & Corporate Finance Workflows

> Letter of Credit (LC) management, bank guarantees, cash flow forecasting, intercompany profit elimination, transfer pricing, bank account lifecycle, surplus cash investment, debt facility management, electronic banking security, and BSP regulatory reporting.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W232. Letter of Credit (LC) & Bank Guarantee Lifecycle](#w232-letter-of-credit-lc-bank-guarantee-lifecycle)
- [W233. Cash Flow Forecasting & Liquidity Management](#w233-cash-flow-forecasting-liquidity-management)
- [W234. Intercompany Profit Elimination & Consolidation](#w234-intercompany-profit-elimination-consolidation)
- [W235. Transfer Pricing Compliance & Documentation](#w235-transfer-pricing-compliance-documentation)
- [W317. Bank Account Lifecycle & Signatory Management](#w317-bank-account-lifecycle-signatory-management)
- [W318. Short-Term Investment & Surplus Cash Placement](#w318-short-term-investment-surplus-cash-placement)
- [W319. Debt Facility & Covenant Compliance Management](#w319-debt-facility-covenant-compliance-management)
- [W320. Electronic Banking Security & Payment Control](#w320-electronic-banking-security-payment-control)
- [W321. FX Exposure Analysis & BSP Regulatory Reporting](#w321-fx-exposure-analysis-bsp-regulatory-reporting)
- [W322. Treasury Policy, Governance & Risk Appetite Framework](#w322-treasury-policy-governance-risk-appetite-framework)
- [W323. Cash Concentration & Inter-Entity Pooling Operations](#w323-cash-concentration-inter-entity-pooling-operations)
- [W324. Supply Chain Finance & Dynamic Discounting Program](#w324-supply-chain-finance-dynamic-discounting-program)
- [W325. Corporate Guarantee & Contingent Liability Management](#w325-corporate-guarantee-contingent-liability-management)
- [W326. Treasury Month-End Close & Reconciliation](#w326-treasury-month-end-close-reconciliation)
- [W327. External Shareholder Dividend Declaration & Payment](#w327-external-shareholder-dividend-declaration-payment)

---

## W232. Letter of Credit (LC) & Bank Guarantee Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | Approved Import PO (W2B) requiring LC; or contract requirement for Bank Guarantee |
| **Frequency** | 10–20 LCs/month (imports); 5–10 Bank Guarantees/year |
| **Volume** | High-value import shipments (Machinery, bulk construction materials) |
| **Owner** | Treasury Manager |
| **Participants** | Import Coordinator, Buyer, Bank, Finance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Application**: Import Coordinator requests LC issuance based on Pro-forma Invoice and PO | Import Coord | Treasury Mgr | 1 day |
| 2 | **Bank Submission**: Treasury submits LC application to partner bank via electronic portal | Treasury Mgr | CFO | 1 day |
| 3 | **LC Issuance**: Bank issues LC; notifies Vendor's bank (Advising Bank) | Bank | — | 2–3 days |
| 4 | **Document Negotiation**: Vendor ships goods; submits shipping documents (Bill of Lading, Invoice, Packing List) to bank | Vendor | — | 1 week |
| 5 | **Discrepancy Check**: Treasury and Bank review documents for discrepancies vs. LC terms | Treasury Mgr | — | 2 days |
| 6 | **Payment/Acceptance**: Treasury authorizes payment or acceptance of draft; Bank releases documents to BuildRight for customs clearance (W233) | Treasury Mgr | CFO | 1 day |
| 7 | **Closure**: LC closed in system once goods received (W3) and payment settled | Treasury Mgr | — | 1 day |

### System Touchpoints

- Treasury Management Module (LC tracking, bank limits, LC aging report)
- Import Management module linked to W2B (Import PO)
- Accounts Payable module for payment settlement linked to W7 (Payments)
- Bank portal integration for electronic LC submission and status tracking

### Pain Points / Risks

- **BSP foreign exchange regulations**: All LC transactions above USD 50,000 require BSP reporting; non-compliance risks penalties and delayed shipments
- **Document discrepancy delays**: 30–40% of first-time LC presentations contain discrepancies, adding 2–5 days per occurrence and demurrage risk at Philippine ports
- **Bank credit line saturation**: High LC volumes during construction season may exhaust available credit lines across the 5 banking relationships
- **Currency exposure**: PHP volatility against USD/CNY can materially increase landed cost between LC issuance and payment settlement
- **Regulatory risk**: BIR requires withholding tax documentation on LC-related import service fees; missed WTD deductions trigger audit flags

### Staffing Implication

10–20 LCs/month plus 5–10 bank guarantees/year. Each LC requires 2–3 days of processing (application, bank liaison, discrepancy review, payment authorization). This workload is absorbed by the Treasury Manager (1 FTE) with support from the Import Coordinator for documentation preparation. Peak periods (major infrastructure project orders) may require temporary overtime approval.

### Time Estimate

**Total**: 2–3 days per LC (end to end, including bank processing time); ~30 minutes per bank guarantee renewal

---

## W233. Cash Flow Forecasting & Liquidity Management

| Field | Detail |
|---|---|
| **Trigger** | Weekly treasury cycle |
| **Frequency** | Weekly (Daily monitoring) |
| **Volume** | Covers 5 entities and ~50 bank accounts |
| **Owner** | Treasury Analyst |
| **Participants** | CFO, Controller, AP/AR Managers |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Aggregation**: Pull expected receipts (AR) and planned payments (AP, Payroll, Tax) from ERP | System | Treasury Analyst | 1 hour |
| 2 | **Non-ERP Inputs**: Add manual forecasts for CAPEX, loan repayments, and dividends | Treasury Analyst | Treasury Mgr | 2 hours |
| 3 | **Analysis**: Identify liquidity gaps or excess cash across entities | Treasury Analyst | Treasury Mgr | 2 hours |
| 4 | **Cash Positioning**: Execute intercompany transfers (sweeping) to optimize interest or cover deficits | Treasury Mgr | CFO | 1 day |
| 5 | **Reporting**: Weekly Cash Position Report to Executive Team | Treasury Mgr | CFO | 1 hour |

### System Touchpoints

- Cash Flow Forecasting tool (direct/indirect methods, 13-week rolling forecast)
- Treasury Management Module (bank account balances, intercompany transfer execution)
- Integration with W8 (Receipts) for incoming cash, W7 (Payments) for outgoing disbursements
- Bank statement auto-import via BPI, BDO, Metrobank, and Security Bank portals
- Consolidated dashboard across 5 legal entities and ~50 bank accounts

### Pain Points / Risks

- **Multi-entity cash visibility**: 50 bank accounts across 5 entities with different banking portals create latency in real-time balance visibility; bank API outages at BPI or BDO can delay positioning by half a day
- **Intercompany sweep timing**: Peso fund transfers between BuildRight entities settle same-day (PCHC), but USD sweeps may take T+1 or T+2, creating temporary liquidity gaps
- **Forecast accuracy**: AP/AR timing assumptions are frequently disrupted by customer payment delays (Philippine construction industry standard terms of 30–60 days often extend to 90+ days)
- **BSP reserve requirements**: Changes to reserve requirement ratios for corporate deposits impact available liquidity across entities
- **SEC reporting**: Large intercompany fund movements may require disclosure in related-party transaction notes under SEC Philippine reporting guidelines

### Staffing Implication

Weekly cycle covering 5 entities and ~50 bank accounts. Data aggregation and analysis require approximately 6 hours/week for the Treasury Analyst, with an additional 1–2 hours for the Treasury Manager to review positioning decisions. This is absorbed by the existing Treasury Analyst (1 FTE). Daily monitoring during month-end and payroll weeks increases to ~8 hours/week.

### Time Estimate

**Total**: 6 hours per weekly cycle (data aggregation 1 hr + manual inputs 2 hrs + analysis 2 hrs + reporting 1 hr); daily monitoring adds ~30 minutes/day

---

## W234. Intercompany Profit Elimination & Consolidation

| Field | Detail |
|---|---|
| **Trigger** | Month-end close (W9) |
| **Frequency** | Monthly |
| **Volume** | Sales between Logistics Inc., Property Inc., and Depot Inc. |
| **Owner** | Consolidation Manager |
| **Participants** | Entity Controllers, CFO |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Reconciliation**: Match intercompany sales/purchases and AR/AP balances between entities | Entity Accountant | Consolidation Mgr | 1 day |
| 2 | **Profit Identification**: Identify "Unrealized Profit" in ending inventory for goods sold between entities (e.g., Depot Inc. holding stock bought from Logistics Inc.) | Consolidation Mgr | Controller | 1 day |
| 3 | **Elimination Entries**: Post elimination journals in the Consolidation Ledger (Dr. Revenue / Cr. COGS; Dr. COGS / Cr. Inventory) | Consolidation Mgr | CFO | 4 hours |
| 4 | **Validation**: Verify Consolidated Trial Balance reflects zero intercompany balances | Consolidation Mgr | — | 2 hours |

### System Touchpoints

- Consolidation Engine with automated elimination rules
- Intercompany matching workbench for AR/AP balance reconciliation
- Integration with W14 (Logistics Billing) for intercompany freight charges
- Integration with general ledger for entity-level trial balance extraction

### Pain Points / Risks

- **Unrealized profit complexity**: Multi-tier inventory transfers (Logistics Inc. → Depot Inc. → retail stores) create nested unrealized profit layers that manual elimination entries may miss
- **PFRS 16 / IFRS 16 intercompany leases**: Property Inc. leases warehouse space to Depot Inc.; right-of-use asset and lease liability elimination requires careful matching of lease terms and depreciation schedules
- **Timing differences**: Entities close on different schedules during month-end; Depot Inc. retail POS closes Day 1 but Logistics Inc. freight billing closes Day 3, creating reconciliation gaps
- **Tax-basis divergence**: Elimination entries for consolidated reporting differ from individual entity tax filings; BIR requires separate entity-level income tax returns, so consolidated adjustments must be tracked in a separate overlay ledger
- **Management fee elimination**: Intercompany management fees between BuildRight Holdings and operating entities require precise matching of accrual vs. cash basis

### Staffing Implication

Monthly process at close, covering 5 entities. Reconciliation and elimination require approximately 2 days/month from the Consolidation Manager, with 1 day of support from Entity Accountants for balance confirmations. This is absorbed by the existing Consolidation Manager (1 FTE). Quarter-end and year-end cycles are heavier due to PFRS 16 intercompany lease adjustments, requiring an additional 1 day per quarter.

### Time Estimate

**Total**: 2 days per monthly cycle (reconciliation 1 day + profit identification 1 day + elimination entries 4 hrs + validation 2 hrs); quarter-end adds 1 additional day

---

## W235. Transfer Pricing Compliance & Documentation

| Field | Detail |
|---|---|
| **Trigger** | Annual tax cycle; or major change in intercompany service agreements |
| **Frequency** | Annual (Documentation); Quarterly (Review) |
| **Volume** | 5 related entities in the Philippines |
| **Owner** | Tax Manager |
| **Participants** | External Tax Advisor, CFO, Controller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Benchmarking**: Conduct annual comparability study for intercompany markups (Logistics services, Rent) | Tax Manager | CFO | 2 weeks |
| 2 | **Local File Prep**: Prepare "Transfer Pricing Documentation" (TPD) per BIR RR No. 19-2020 | Tax Manager | External Advisor | 1 month |
| 3 | **Quarterly Monitoring**: Review actual intercompany margins against the Arm's Length Range | Tax Manager | Controller | 1 day |
| 4 | **Adjustments**: If margins are outside range, trigger true-up/true-down entries | Tax Manager | CFO | 1 day |
| 5 | **Reporting**: File BIR Form 1709 (RPT Form) with the Annual Income Tax Return | Tax Manager | CFO | Per schedule |

### System Touchpoints

- Transfer Pricing module or dedicated TPD software for benchmarking analysis
- Intercompany transaction reporting extracted from the Consolidation Engine
- Integration with W14 (Logistics Billing) for intercompany service revenue analysis
- Tax compliance calendar linked to BIR Form 1709 filing deadline

### Pain Points / Risks

- **BIR RR 19-2020 compliance**: Transfer Pricing Documentation must meet specific Philippine requirements (organizational structure, industry analysis, comparability analysis); non-filing or late filing of BIR Form 1709 carries penalties of PHP 1,000 per return plus compromise penalties
- **Limited Philippine comparables**: Few publicly listed Philippine companies in hardware/logistics for benchmarking; must rely on regional (ASEAN) comparables with adjustments, which BIR may challenge
- **TRAIN law impact**: CREATE (Corporate Recovery and Tax Incentives for Enterprises) law reduced corporate tax rates but introduced stricter transfer pricing scrutiny; related-party transactions are now a priority BIR audit area
- **SEC reporting**: Related-party transactions must be disclosed in SEC annual reports (GIS) with transfer pricing methodology descriptions; inconsistencies between TPD and SEC filings trigger examination
- **Margin volatility**: Actual intercompany margins fluctuate due to fuel costs (Logistics Inc.) and occupancy rates (Property Inc.); quarterly monitoring may flag frequent out-of-range results requiring adjustments
- **Competent authority risk**: While all entities are Philippine-domiciled, BuildRight's foreign supplier relationships and potential offshore intercompany arrangements could attract additional scrutiny

### Staffing Implication

Annual documentation cycle requires approximately 1 month of focused effort (spread over 6–8 weeks) from the Tax Manager, with External Tax Advisor engagement for benchmarking and Local File review. Quarterly monitoring requires 1 day each quarter. This is absorbed by the existing Tax Manager (1 FTE). External advisor fees are budgeted at PHP 500K–800K/year for comparability study and TPD preparation.

### Time Estimate

**Total**: Annual documentation cycle — 1 month over 6–8 weeks (Tax Manager) + 2 weeks (External Advisor); Quarterly monitoring — 1 day per quarter; Adjustment entries — 1 day per occurrence as needed

---

## W317. Bank Account Lifecycle & Signatory Management

| Field | Detail |
|---|---|
| **Trigger** | New store opening (W16), new entity setup, new banking relationship, signatory role change, employee separation (W43), or store closure (W45) |
| **Frequency** | ~10–15 new accounts/year (new stores); ~5–8 signatory updates/month (employee turnover); ~2–3 account closures/year |
| **Volume** | ~210 bank accounts across 5 entities and 4 banks (BDO, BPI, Metrobank, Chinabank): ~200 store deposit accounts, 4 DC operating accounts, 5 entity main operating accounts, 5 USD import accounts, and additional payroll, savings, and investment accounts per entity |
| **Owner** | Treasury Manager |
| **Participants** | Treasury Analyst, CFO, Legal (Board Resolutions), HR (separation alerts), Store Operations (new store setup) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Account opening request**: triggered by new store (W16), new entity, or operational need — Treasury Analyst prepares account opening checklist per bank requirements: Board Resolution (per entity), Secretary's Certificate, authorized signatory list with specimen signatures, business registration documents (SEC, DTI, BIR, LGU permit), latest audited financial statements | Treasury Analyst | Treasury Mgr | 2–3 hours/account |
| 2 | **Legal documentation**: Legal prepares Board Resolution authorizing account opening and designating authorized signatories; Secretary's Certificate signed by Corporate Secretary | Legal / Corp Secretary | CFO | 1–2 days |
| 3 | **Bank submission**: Treasury Analyst submits complete documentation package to bank; tracks application status via bank portal or relationship manager | Treasury Analyst | — | 1–2 weeks (bank processing) |
| 4 | **Account activation**: upon bank confirmation, Treasury Analyst records new account in system — account number, bank name, entity, account type (operating, deposit, payroll, USD, investment), purpose, signatory tier (single, dual, any-two-of-three), opening date; links to entity in GL | Treasury Analyst | Treasury Mgr | 30 min/account |
| 5 | **Signatory management — ongoing**: system tracks authorized signatories per account with signatory tier, specimen signature on file, and last update date; when a signatory changes role (promotion, transfer) or separates (W43), HR alerts Treasury Analyst within 5 business days; Treasury Analyst prepares signatory update documentation per bank requirements and submits within 10 business days of trigger event | Treasury Analyst | Treasury Mgr | 1–2 hours/signatory change |
| 6 | **Signatory staleness review**: system alerts Treasury Manager when any account has had no signatory update in > 12 months; Treasury Analyst reviews all signatories for current employment status and authority level; updates if needed | System / Treasury Analyst | Treasury Mgr | Quarterly review (2 hours) |
| 7 | **Account closure request**: triggered by store closure (W45), account consolidation, or banking relationship termination — Treasury Analyst confirms zero balance (or arranges final transfer), obtains bank closure confirmation letter, and deactivates account in system | Treasury Analyst | Treasury Mgr | 1–2 hours/account |
| 8 | **Banking relationship review**: annually, Treasury Manager reviews banking relationships across all 4 banks — fee structures, service quality, credit facility availability, digital banking capabilities, and geographic coverage for provincial stores; recommends relationship changes to CFO | Treasury Mgr | CFO | 4–6 hours/year |
| 9 | **Bank fee monitoring**: monthly, Treasury Analyst reviews bank fee and charge schedule per account; compares actual fees charged (from bank statements during W89) against agreed fee schedules; disputes unexpected charges with bank relationship manager within 30 days | Treasury Analyst | Treasury Mgr | 1 hour/month |

### System Touchpoints

- Bank account register: centralized register across all entities and banks with account number, type, entity, purpose, signatories, opening/closure dates, and status (W317.4)
- Signatory tracking with specimen signature document storage, last-update date, and staleness alerting at 12 months (W317.5–6)
- HR integration: automated alert to Treasury when signatory employee separates (W43) or transfers; system cross-references active signatories against active employee roster (W317.5)
- Account lifecycle status: Pending → Active → Pending Closure → Closed; linked to store/DC location in system (W317.4, W317.7)
- Bank fee tracking: fee schedule per bank per account type; actual fees charged from bank statement import (W89) compared against schedule; variance dashboard (W317.9)
- Integration with W16 (new store opening — triggers account opening), W30 (daily cash position — all active accounts feed cash position), W43 (employee separation — triggers signatory update), W45 (store closure — triggers account closure), W89 (bank reconciliation — validates account activity)

### Pain Points / Risks

- **Signatory update lag after employee separation**: with ~15–20% annual turnover across 6,715 employees, signatory-authorized staff separate frequently; if HR does not promptly alert Treasury, separated employees may retain system and bank portal access, creating a fraud and unauthorized transaction risk
- **Board Resolution delays blocking account opening**: new store openings (W16) follow a tight timeline; if Legal cannot produce Board Resolutions and Secretary's Certificates within the project schedule, bank account opening is delayed, preventing store deposit functionality for the first days of operations
- **Inconsistent bank documentation requirements**: each of the 4 banks (BDO, BPI, Metrobank, Chinabank) has different documentation requirements for account opening and signatory changes; maintaining a current requirements matrix per bank is manual and error-prone
- **Provincial store banking access challenges**: new stores in remote areas (e.g., Bicol, Mindanao provincial towns) may not have branches of BuildRight's preferred banks nearby; Treasury must identify alternative banks or arrange cash-in-transit (W174) for deposit logistics
- **Dormant account risk**: store closures (W45) that do not complete the account closure process leave dormant accounts exposed to unauthorized access and incurring ongoing maintenance fees

### Staffing Implication

~10–15 new accounts/year + ~60–90 signatory updates/year (~5–8/month) + ~2–3 closures/year. Each account opening requires 2–3 hours of Treasury Analyst time for documentation preparation and bank liaison; each signatory update requires 1–2 hours. Total: ~100–150 hours/year (~8–12 hours/month), absorbed by the Treasury Analyst within the existing 2–3 analyst team. The Treasury Manager adds ~4–6 hours/year for banking relationship review and quarterly signatory staleness review.

### Time Estimate

**Total**: Account opening — 2–3 hours preparation + 1–2 weeks bank processing per account; Signatory update — 1–2 hours per change; Quarterly signatory staleness review — 2 hours; Annual banking relationship review — 4–6 hours; Monthly bank fee review — 1 hour; Account closure — 1–2 hours per account

---

## W318. Short-Term Investment & Surplus Cash Placement

| Field | Detail |
|---|---|
| **Trigger** | Weekly cash flow forecast (W233) identifies surplus cash exceeding 14-day operational requirements; or ad-hoc surplus from large customer collection, asset sale, or dividend receipt |
| **Frequency** | Weekly assessment; placements made as needed (typically 2–4 placements/month) |
| **Volume** | Surplus cash availability varies; estimated average surplus of PHP 200–500M available for short-term placement at any given time across 5 entities |
| **Owner** | Treasury Manager |
| **Participants** | Treasury Manager, Treasury Analyst, CFO, Banks |

### Background

BuildRight's high cash generation (PHP 62B annual revenue with ~42% cash sales) creates regular surplus cash that exceeds immediate operational needs. Placing surplus cash in short-term instruments earns interest income that contributes to net finance income. This workflow governs the identification, placement, monitoring, and redemption of short-term investments across all entities.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Surplus identification**: Treasury Analyst reviews weekly cash flow forecast (W233) and daily cash position (W30); identifies cash balances exceeding 14-day projected operational requirements across each entity; calculates available surplus per entity and in total | Treasury Analyst | Treasury Mgr | 30 min/week |
| 2 | **Placement decision**: Treasury Manager evaluates placement options based on: (a) amount and duration of surplus (when is the cash needed next?), (b) available instruments: bank time deposits (7-day, 30-day, 60-day, 90-day), Philippine Treasury Bills (T-bills) via bank brokerage, money market placement (overnight to 7-day), Special Deposit Account (SDA) with BSP-qualified banks; (c) current market rates vs. BuildRight's weighted average cost of capital; (d) counterparty bank exposure limits (no single bank to hold > 40% of total investment portfolio); (e) entity-level cash needs (surplus at one entity cannot be invested if intercompany sweep to another entity is pending per W233) | Treasury Mgr | CFO | 30 min/placement |
| 3 | **Approval**: placement approvals by tier — (a) ≤ PHP 50M: Treasury Manager approves; (b) PHP 50M–200M: CFO approves; (c) > PHP 200M: CEO approves; placement approval includes instrument type, amount, tenor, counterparty bank, and expected yield | Approver | Approver | 15 min/placement |
| 4 | **Execution**: Treasury Analyst places investment via bank portal (electronic time deposit placement) or bank relationship manager; confirms placement details — principal, rate, maturity date, rollover instruction (auto-rollover or manual redemption); records placement in investment register | Treasury Analyst | Treasury Mgr | 15 min/placement |
| 5 | **Investment register maintenance**: system tracks all active placements — institution, instrument type, principal amount, interest rate, placement date, maturity date, rollover status, entity, linked bank account; auto-generates maturity calendar | System / Treasury Analyst | Treasury Mgr | Ongoing (30 min/week) |
| 6 | **Maturity monitoring**: system alerts Treasury Analyst 3 business days before each placement maturity; Treasury Analyst recommends action to Treasury Manager — (a) redeem to fund operational needs, (b) roll over at current market rate, or (c) roll over and adjust amount based on updated surplus calculation (step 1) | System / Treasury Analyst | Treasury Mgr | 15 min/placement |
| 7 | **Interest income tracking**: system records interest earned per placement; at maturity or periodic payout, posts interest income to GL (Dr. Cash / Cr. Interest Income); tracks accrued interest for month-end reporting (W9A) | System | Controller | Automated |
| 8 | **Monthly portfolio review**: Treasury Manager prepares monthly investment portfolio summary for CFO — total portfolio value, weighted average yield, portfolio by instrument type and counterparty bank, maturity ladder (0–30, 31–60, 61–90, 90+ days), interest income month-to-date vs. budget, counterparty concentration analysis | Treasury Mgr | CFO | 1 hour/month |
| 9 | **Quarterly investment policy review**: CFO reviews investment portfolio performance vs. policy parameters — (a) portfolio yield vs. benchmark (91-day T-bill rate), (b) counterparty concentration vs. limits, (c) average portfolio duration vs. liquidity needs, (d) any credit events at counterparty banks; adjusts policy parameters if needed | CFO | CEO | 1 hour/quarter |

### System Touchpoints

- Investment register: centralized tracking of all active placements across entities and banks with full details and maturity calendar (W318.5)
- Automated maturity alerting at 3 business days before maturity (W318.6)
- Surplus cash identification from cash flow forecast (W233) and daily cash position (W30) integration (W318.1)
- Interest income accrual and posting integration with GL (W9A month-end close) (W318.7)
- Counterparty bank exposure dashboard: total placement amount per bank with limit monitoring (W318.2, W318.8)
- Investment portfolio summary report with yield, duration, concentration, and maturity ladder analysis (W318.8)
- Integration with W30 (daily cash position — placement cash flows reflected), W233 (cash flow forecast — investment maturities and interest income included in forecast), W89 (bank reconciliation — placement redemptions and interest income matched), W9A (month-end — accrued interest posting)

### Pain Points / Risks

- **Surplus estimation error leading to premature placement**: if the weekly cash flow forecast (W233) overestimates surplus, funds may be locked in a 30-day time deposit when needed for an unexpected payment (large vendor early-payment discount opportunity per W7.7a, emergency capex per W60, or payroll shortfall); premature redemption incurs penalty and lost interest
- **Counterparty bank credit risk**: Philippine bank credit quality varies; while BDO, BPI, and Metrobank are systemically important, smaller banks offering higher yields carry higher credit risk; the 40% single-bank concentration limit mitigates but does not eliminate this exposure
- **Interest rate environment mismatch**: in a rising rate environment, locking surplus in 90-day time deposits at current rates means missing higher rates available in 30 days; conversely, in a falling rate environment, longer placements are advantageous; the tenor decision requires judgment on rate direction that Treasury may not consistently get right
- **Multi-entity surplus fragmentation**: surplus cash may be concentrated in one entity (e.g., Depot Inc.) while another entity has a deficit; intercompany sweeping (W233) must be executed before surplus at the holding entity can be invested, adding latency and intercompany loan complexity (W137)
- **PDIC insurance coverage limit**: Philippine Deposit Insurance Corporation (PDIC) covers deposits up to PHP 500,000 per depositor per bank; large placements exceeding this limit are partially uninsured, creating potential loss exposure in a bank failure scenario

### Staffing Implication

2–4 placements/month requiring 30 min assessment + 15 min execution each = ~2–3 hours/month; weekly surplus review adds 30 min/week; monthly portfolio review adds 1 hour/month; quarterly policy review adds 1 hour/quarter. Total: ~6–8 hours/month, absorbed by the Treasury Manager and Treasury Analyst within existing headcount.

### Time Estimate

**Total**: Surplus assessment — 30 min/week; Placement decision and execution — 45 min/placement (2–4/month); Portfolio register maintenance — 30 min/week; Monthly portfolio review — 1 hour/month; Quarterly policy review — 1 hour/quarter

---

## W319. Debt Facility & Covenant Compliance Management

| Field | Detail |
|---|---|
| **Trigger** | Annual credit facility renewal; new loan drawdown request (capex, working capital); quarterly covenant testing date; or loan maturity |
| **Frequency** | Ongoing monitoring; covenant testing quarterly; facility review annually; drawdowns as needed (estimated 4–8 per year for expansion-related capex and seasonal working capital) |
| **Volume** | Estimated 3–5 active credit facilities across the group: revolving credit line (working capital), term loan (store expansion capex), USD credit line (import LCs), and potentially a bilateral loan per major bank relationship |
| **Owner** | Treasury Manager |
| **Participants** | Treasury Manager, Treasury Analyst, CFO, Controller, Legal, Banks, External Auditors |

### Background

BuildRight's expansion plan of 10–15 new stores/year requires significant capital investment (estimated PHP 80–120M per new store for land, construction, fixtures, and initial inventory). This capital is funded through a combination of operating cash flow, credit facilities, and term loans. Managing the debt portfolio — drawdowns, repayments, covenant compliance, lender reporting, and facility renewals — is a core treasury responsibility that directly impacts the company's ability to fund growth.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Facility register maintenance**: system tracks all active credit facilities — lender, facility type (revolving credit, term loan, USD line, bilateral), committed amount, drawn amount, available headroom, interest rate (fixed or floating + benchmark), maturity date, covenants, and security/collateral pledged | Treasury Analyst | Treasury Mgr | Ongoing (2 hours/month) |
| 2 | **Drawdown request**: triggered by capex funding need (W21 approved), seasonal working capital requirement, or LC issuance (W232) exceeding available bank limits — Treasury Manager prepares drawdown request: amount, purpose, facility to draw from, repayment source, and timeline | Treasury Mgr | CFO | 30 min/drawdown |
| 3 | **Drawdown approval**: tiered by amount — (a) ≤ PHP 50M: CFO approves, (b) PHP 50M–200M: CEO approves, (c) > PHP 200M: Board approves; approval includes confirmation that drawdown will not breach any financial covenant | Approver | Approver | 15 min/drawdown |
| 4 | **Execution**: Treasury Analyst coordinates drawdown with lender bank; confirms disbursement to designated bank account; system records drawdown with loan reference, amount, interest rate, repayment schedule (if term loan), and linked capex or working capital purpose | Treasury Analyst | Treasury Mgr | 1 hour/drawdown |
| 5 | **Debt service management**: system generates debt service schedule per facility — monthly interest payments (for revolving credit and term loans), principal repayments (for term loans per agreed amortization), and balloon payments at maturity; Treasury Analyst confirms upcoming debt service payments are included in weekly cash flow forecast (W233) and daily cash position (W30) | System / Treasury Analyst | Treasury Mgr | 30 min/month |
| 6 | **Quarterly covenant testing**: within 30 days of each quarter-end, Controller computes financial covenants from consolidated and entity-level financial statements — typical covenants include: (a) Debt-to-Equity ratio (maximum, e.g., 2.0:1), (b) Current ratio (minimum, e.g., 1.5:1), (c) Debt Service Coverage Ratio (DSCR) (minimum, e.g., 1.5x), (d) Net Worth minimum, (e) Capital Expenditure ceiling (if applicable); system compares actual vs. covenant requirement per facility; flags any breach or near-breach (within 10% of limit) | Controller | CFO | 4 hours/quarter |
| 7 | **Covenant compliance reporting**: Treasury Manager prepares compliance certificate per lender's required format; CFO signs compliance certificate; Treasury Analyst transmits to lender within required timeframe (typically 45 days from quarter-end); Controller provides audited or reviewed financial statements if required by facility agreement | Treasury Mgr / CFO | CFO | 2 hours/quarter |
| 8 | **Covenant breach escalation**: if any covenant is breached or within 10% of the limit — (a) Treasury Manager immediately notifies CFO and CEO, (b) CFO assesses whether waiver negotiation with lender is required, (c) if waiver needed: Treasury Manager coordinates with Legal and CFO to prepare waiver request with remediation plan and timeline, (d) CFO negotiates waiver with lender, (e) system tracks all waiver requests, outcomes, and amended covenant terms | Treasury Mgr / CFO | CEO | As needed |
| 9 | **Facility renewal negotiation**: 6 months before facility maturity, Treasury Manager begins renewal discussions with lender — (a) reviews current utilization and headroom, (b) assesses whether facility size and terms remain appropriate for BuildRight's growth plans, (c) obtains competitive proposals from at least 2 other banks, (d) presents renewal recommendation to CFO with comparison of terms (interest rate, fees, covenants, commitment amount), (e) CFO approves renewal terms; if changes to security or covenants require Board approval, Legal prepares Board Resolution | Treasury Mgr | CFO | 8–16 hours/renewal |
| 10 | **Annual lender relationship management**: Treasury Manager maintains relationship with lending banks — periodic meetings, information sharing, site visits to new stores; ensures BuildRight is positioned favorably for future credit needs and rate negotiations | Treasury Mgr | CFO | 4–8 hours/year |
| 11 | **Year-end**: Controller includes long-term and short-term debt balances, debt maturity schedule, and covenant compliance status in year-end financial statement notes per PFRS requirements | Controller | CFO | Part of W9B |

### System Touchpoints

- Debt facility register: centralized tracking of all facilities across entities with committed/drawn amounts, interest rates, maturity, covenants, and collateral (W319.1)
- Loan drawdown workflow with approval tiers and covenant breach pre-check (W319.2–4)
- Debt service schedule auto-generation with payment calendar integration to W233 (cash flow forecast) and W30 (daily cash position) (W319.5)
- Covenant testing module: automated computation of financial ratios from GL and financial statement data; comparison against covenant thresholds; breach/near-breach alerting (W319.6)
- Compliance certificate generation in lender-required format (W319.7)
- Covenant breach escalation tracking with waiver management (W319.8)
- Debt maturity ladder: visualization of debt maturities over next 1–5 years (W319.1)
- Integration with W21 (capex — drawdown funding for approved capex), W30 (daily cash position — debt service payments), W89 (bank reconciliation — loan disbursements and repayments), W137 (intercompany loans — separate from external debt), W232 (LC — utilization counts against credit facility limits), W233 (cash flow forecast — debt service included), W9A (month-end — interest accrual and loan balance reconciliation), W9B (year-end — PFRS debt disclosures)

### Pain Points / Risks

- **Covenant breach during rapid expansion**: opening 10–15 stores/year increases both debt (to fund construction per W223–226) and capex (to fit out stores per W21); if revenue ramp at new stores lags projections, Debt-to-Equity and DSCR covenants may be breached, triggering lender remedies including accelerated repayment or facility freeze
- **Floating rate exposure on revolving credit**: if credit facilities are priced at PDSF (Philippine Dealing System Fixing Rate) or PHIBOR + spread, rising benchmark rates increase interest expense; BuildRight does not hedge interest rate risk (no interest rate swaps), making debt service cost volatile
- **Cross-entity facility allocation**: a revolving credit facility at BuildRight Holdings may fund operations at Depot Inc. or Logistics Inc.; tracking utilization per entity vs. facility-level covenants requires separate sub-ledgers that may not reconcile cleanly with lender reporting
- **Loan documentation compliance**: Philippine banks require extensive ongoing compliance — updated financial statements, board resolutions, SEC filings, and insurance certificates; missing any required document can trigger a technical default even when financial covenants are met
- **Refinancing risk at maturity**: if a major term loan matures during a period of tight credit conditions (e.g., BSP tightens monetary policy, Philippine credit rating downgrade), refinancing may be unavailable or available only at significantly higher rates, impacting BuildRight's ability to fund continued expansion
- **Security and collateral tracking**: properties, receivables, or inventory pledged as collateral must be tracked per facility; if BuildRight disposes of pledged assets (W39) without lender consent, it constitutes a covenant breach

### Staffing Implication

Ongoing monitoring adds ~2 hours/month for register maintenance + ~30 min/month for debt service management; quarterly covenant testing adds ~6 hours/quarter (4 hours Controller + 2 hours Treasury Manager); annual renewal negotiations add 8–16 hours per renewal; drawdown processing adds ~2 hours/drawdown (4–8 per year). Total: ~15–25 hours/month during peak periods, ~8–12 hours/month steady-state. Absorbed by Treasury Manager and Controller within existing headcount.

### Time Estimate

**Total**: Facility register maintenance — 2 hours/month; Drawdown processing — 2 hours/drawdown (4–8/year); Debt service monitoring — 30 min/month; Quarterly covenant testing — 6 hours/quarter; Compliance reporting — 2 hours/quarter; Facility renewal — 8–16 hours/renewal; Annual relationship management — 4–8 hours/year

---

## W320. Electronic Banking Security & Payment Control

| Field | Detail |
|---|---|
| **Trigger** | Daily payment operations; new user onboarding; periodic access review; or security incident |
| **Frequency** | Daily (payment operations); quarterly (access review); annual (policy review); ad-hoc (incident response) |
| **Volume** | ~210 bank accounts across 4 banks; ~25–35 payment runs/month (W7 twice-weekly + payroll + tax + capex + intercompany); ~30–40 authorized payment users across Finance and Treasury |
| **Owner** | Treasury Manager |
| **Participants** | Treasury Manager, Treasury Analyst, AP Supervisor, CFO, IT Security, Banks |

### Background

Electronic banking security is the control framework that prevents unauthorized, fraudulent, or erroneous payments across BuildRight's banking relationships. With ~210 bank accounts, PHP 62B annual revenue flowing through electronic channels, and 4 banking portals, the risk of payment fraud (external cyber-attack, internal unauthorized payment, or social engineering) is material. This workflow establishes maker-checker controls, user access governance, payment approval workflows, and incident response procedures.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Payment initiation (Maker)**: authorized AP Clerk or Treasury Analyst creates payment batch in ERP — system generates payment file (vendor payments, payroll, tax, intercompany transfers); payment file includes payee name, bank account, amount, payment reference, and cost center | AP Clerk / Treasury Analyst | AP Supervisor / Treasury Mgr | Per W7, W10, W90 |
| 2 | **First-level approval (Checker)**: AP Supervisor or Treasury Manager reviews payment batch — verifies payee details, amount vs. approved invoice/purpose, bank account vs. vendor master; approves batch in ERP; system locks payment details from further modification after first approval | AP Supervisor / Treasury Mgr | — | 15–30 min/batch |
| 3 | **Second-level approval (Authorizer)**: for payments above threshold — (a) ≤ PHP 5M: Treasury Manager or AP Supervisor, (b) PHP 5M–20M: CFO, (c) > PHP 20M: CEO + CFO; authorizer reviews and releases payment batch in bank portal (or ERP-to-bank integration); system records approver ID, timestamp, and authorization level | Treasury Mgr / CFO / CEO | CFO | 10–15 min/batch |
| 4 | **Bank portal access control**: Treasury Manager maintains bank portal user access matrix — (a) user roles: inquiry-only (view balances), payment initiator (create payment), payment approver (release payment), admin (manage users); (b) segregation of duties: no single user may both create and approve payments for the same account; (c) user access reviewed quarterly (step 8) | Treasury Mgr | CFO | Ongoing |
| 5 | **New user onboarding**: when a new Treasury Analyst or AP Clerk joins (W15), Treasury Manager requests bank portal access based on role; user completes bank's identity verification; initial access set to inquiry-only for first 30 days; elevated to payment initiator after training and competency confirmation | Treasury Mgr | CFO | 1–2 hours/user |
| 6 | **User deactivation**: when a payment user separates (W43) or transfers out of Treasury/AP, Treasury Manager immediately (same day) deactivates bank portal access; HR separation notification triggers automated alert to Treasury Manager; system cross-references bank portal user list against active employee roster weekly | Treasury Mgr | CFO | 30 min/user |
| 7 | **Token and credential management**: bank security tokens (hardware or software OTP) are issued per user; tokens are stored securely and never shared; lost or compromised tokens reported to bank immediately and replaced; token inventory tracked per user with issuance and expiry dates | Treasury Analyst | Treasury Mgr | Ongoing |
| 8 | **Quarterly access review**: Treasury Manager reviews all bank portal users — (a) confirms each user's access level is appropriate for current role, (b) identifies any users with access who have changed roles or should no longer have access, (c) reviews payment approval logs for any unusual patterns (payments approved outside business hours, rapid sequential approvals, payments to new vendors without recent PO), (d) documents review results with sign-off | Treasury Mgr | CFO | 2–3 hours/quarter |
| 9 | **Payment anomaly detection**: system flags payment exceptions for Treasury Manager review — (a) payment to vendor bank account changed within last 7 days, (b) payment amount > 200% of average payment to same vendor, (c) payment to vendor not in active vendor master, (d) multiple payments to same vendor on same day exceeding PHP 5M cumulative, (e) payment initiated outside business hours (before 7 AM or after 8 PM) | System / Treasury Mgr | CFO | 30 min/week |
| 10 | **Security incident response**: if suspected unauthorized payment or bank portal breach is detected — (a) Treasury Manager immediately contacts bank to freeze affected account(s), (b) CFO and IT Security notified within 1 hour, (c) bank conducts investigation with BuildRight cooperation, (d) if confirmed unauthorized payment: Legal assesses recovery options and insurance claim (W59 cyber liability), (e) post-incident: Treasury Manager conducts root cause analysis and implements additional controls, (f) incident reported to Internal Audit for control assessment (W120) | Treasury Mgr / CFO / IT Security | CEO | As needed |
| 11 | **Annual policy review**: CFO reviews and updates electronic banking security policy — maker-checker thresholds, approval tiers, user access standards, token management procedures, and incident response protocol; policy changes approved by CEO; updated policy communicated to all payment users; annual training completion required for continued bank portal access | CFO | CEO | 4 hours/year |

### System Touchpoints

- Payment approval workflow: configurable maker-checker-approver tiers per bank account per entity; payment details locked after first approval; full audit trail of initiator, approver, and authorizer per payment batch (W320.1–3)
- Bank portal user access matrix: centralized tracking of all bank portal users with role, access level, accounts accessible, and last review date (W320.4)
- HR integration: automated alerts when payment users separate or transfer; weekly cross-reference of bank portal users vs. active employee roster (W320.6)
- Payment anomaly detection rules: configurable rules engine flagging unusual payment patterns for review (W320.9)
- Token inventory tracking per user with issuance and expiry dates (W320.7)
- Quarterly access review documentation with sign-off (W320.8)
- Security incident log with root cause analysis and control improvement tracking (W320.10)
- Integration with W7 (AP payment runs), W10 (payroll bank files), W30 (treasury transfers), W43 (employee separation — triggers user deactivation), W89 (bank reconciliation — validates authorized payments), W120 (internal audit — annual controls assessment)

### Pain Points / Risks

- **Business email compromise (BEC) targeting vendor bank account changes**: attackers impersonate vendors and request bank account details be updated in BuildRight's vendor master; if the change is processed without verification (callback to confirmed vendor contact number), subsequent payments are diverted to the attacker's account — this is the most common payment fraud vector in Philippine corporate treasury
- **Same-day deactivation enforcement**: with payment users across HQ and DCs, ensuring same-day bank portal deactivation for every separation is operationally challenging; any gap creates a window for unauthorized payments
- **Approval bottleneck for high-value payments**: payments > PHP 20M requiring CEO + CFO dual approval may be delayed if either is unavailable (travel, sick leave, meetings); delay may result in missed vendor payment deadlines and late payment penalties
- **Social engineering of Treasury staff**: attackers may call or message Treasury staff impersonating senior management (CEO, CFO) and request urgent payment transfers; the approval tier structure mitigates this but cannot eliminate it entirely without callback verification procedures
- **Bank portal downtime during critical payment windows**: if a bank portal is unavailable during payroll or tax payment deadlines, Treasury must have contingency procedures (alternative payment method, manual check issuance, or bank branch over-the-counter payment) to avoid regulatory penalties

### Staffing Implication

Daily payment operations add ~15–30 min/batch for review and approval (absorbed within W7 and W30 staffing). Quarterly access review adds 2–3 hours/quarter. Annual policy review adds 4 hours/year. New user onboarding adds 1–2 hours/user (~5–10 users/year). Total: ~4–6 hours/month incremental Treasury Manager time, absorbed within existing role.

### Time Estimate

**Total**: Payment review and approval — 15–30 min/batch (~25–35 batches/month); Quarterly access review — 2–3 hours/quarter; New user onboarding — 1–2 hours/user; Annual policy review — 4 hours/year; Payment anomaly review — 30 min/week; Incident response — as needed

---

## W321. FX Exposure Analysis & BSP Regulatory Reporting

| Field | Detail |
|---|---|
| **Trigger** | Weekly FX exposure review; monthly BSP reporting cycle; or significant change in import purchasing pattern or exchange rate movement |
| **Frequency** | Weekly exposure analysis; monthly BSP reporting; quarterly strategy review |
| **Volume** | ~40% of COGS from imports ≈ PHP 1.4B/month in foreign-currency payables; USD-denominated bank accounts across 5 entities; ~10–20 active forward contracts (W80) |
| **Owner** | Treasury Analyst |
| **Participants** | Treasury Analyst, Treasury Manager, CFO, Import Coordinator, Cost Accountant |

### Background

While W80 covers FX hedging execution (forward contract placement and settlement), this workflow addresses the broader FX risk management framework: systematic identification of FX exposure across all entities, natural hedging strategy, exposure reporting, and compliance with Bangko Sentral ng Pilipinas (BSP) regulatory requirements for foreign exchange transactions. The Philippines maintains a managed float exchange rate regime with specific BSP reporting obligations for corporate foreign currency transactions.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Weekly FX exposure report**: system generates consolidated FX exposure across all entities — (a) open foreign-currency payables by currency (USD, CNY, EUR) from import POs (W2B), (b) open foreign-currency receivables (if any), (c) foreign-currency bank balances (USD accounts per entity), (d) open forward contracts (W80) with notional amounts and forward rates, (e) net unhedged exposure per currency, (f) FX exposure trend over trailing 4 weeks | System | Treasury Analyst | Automated (weekly) |
| 2 | **Natural hedging assessment**: Treasury Analyst evaluates opportunities to offset FX payables with natural hedges — (a) maintain USD bank account balances to cover near-term (30–60 day) import payment obligations, (b) time USD conversions to take advantage of favorable spot rates when cash position (W30) permits, (c) negotiate with international vendors to invoice in PHP where commercially feasible (limited applicability but worth exploring for ASEAN-based suppliers) | Treasury Analyst | Treasury Mgr | 30 min/week |
| 3 | **Exposure-to-hedge gap analysis**: Treasury Analyst compares net unhedged exposure (step 1) against W80 hedging policy targets (50–80% coverage of forecasted USD payables); identifies any shortfall below 50% coverage and recommends additional forward contracts to Treasury Manager | Treasury Analyst | Treasury Mgr | 15 min/week |
| 4 | **Monthly FX exposure summary**: Treasury Analyst prepares monthly FX exposure summary for CFO — (a) total FX exposure by currency and entity, (b) hedged vs. unhedged breakdown, (c) realized FX gain/loss for the month (from settled transactions), (d) unrealized FX gain/loss on open items (using month-end BSP closing rate), (e) FX impact on import landed cost vs. budget (variance analysis), (f) forward contract portfolio MTM (mark-to-market) summary (from W80) | Treasury Analyst | Treasury Mgr | 1 hour/month |
| 5 | **BSP reporting — FX transactions**: Treasury Analyst compiles and submits required BSP reports for foreign exchange transactions — (a) Foreign Exchange Transactions Report: all purchases and sales of foreign currency above BSP threshold (currently USD 500,000 single transaction or USD 1M aggregate monthly per entity) reported to authorized agent banks; (b) BSP Form 1 (Purchase/Sale of Foreign Exchange): for large FX conversions through banks; (c) Document compliance: all FX purchases above USD 10,000 require supporting documentation (import documents, PO, LC) per BSP Manual of Regulations on Foreign Exchange (FX Manual); Treasury Analyst maintains documentation file per BSP audit trail requirements | Treasury Analyst | Treasury Mgr | 2–4 hours/month |
| 6 | **BSP reporting — cross-border payments**: for outward remittances related to import payments (LC/TT settlement per W232) and other cross-border fund transfers — (a) ensure all outward remittances above BSP threshold are reported through authorized agent banks, (b) maintain records of BSP-approved outward investment or lending (if any intercompany cross-border transactions arise), (c) confirm compliance with BSP rules on permissible outward remittances per FX Manual | Treasury Analyst | Treasury Mgr | Part of step 5 |
| 7 | **BSP examination preparation**: if BSP selects BuildRight for FX compliance examination, Treasury Manager coordinates preparation — (a) compile documentation file: FX transaction reports, supporting import documents, LC copies, bank confirmations, Board Resolutions authorizing FX transactions, (b) Legal reviews documentation completeness, (c) Treasury Manager and CFO attend BSP examination; (d) post-examination: address any BSP findings within required timeframe | Treasury Mgr / CFO | CEO | As needed (8–16 hours per examination) |
| 8 | **Quarterly FX strategy review**: CFO reviews FX management strategy with Treasury Manager — (a) total FX cost (realized + unrealized) vs. budget and vs. prior quarter, (b) hedging effectiveness (W80 quarterly review feeds into this), (c) natural hedging utilization rate, (d) BSP regulatory environment changes (new FX rules, reporting threshold changes), (e) vendor currency mix analysis (opportunities to shift sourcing to PHP-denominated suppliers), (f) adjustment to hedging policy parameters if needed | CFO | CEO | 1 hour/quarter |
| 9 | **Annual FX policy update**: CFO documents and updates FX risk management policy — exposure limits, hedging instruments, counterparty limits, natural hedging strategy, BSP compliance procedures; policy approved by CEO; communicated to all Treasury staff | CFO | CEO | 2 hours/year |

### System Touchpoints

- Consolidated FX exposure report: auto-generated from import POs (W2B), AP open items, USD bank balances (W30), and forward contracts (W80) (W321.1)
- Natural hedging dashboard: USD bank balances vs. near-term USD payables; net USD position per entity (W321.2)
- Hedge coverage ratio: automated calculation of hedged vs. unhedged exposure with policy target comparison (W321.3)
- Monthly FX exposure summary with realized/unrealized FX gain/loss (W321.4)
- BSP reporting document tracker: FX transaction reports filed, supporting documents attached, BSP examination findings tracker (W321.5–7)
- FX policy document management: version-controlled policy with annual review tracking (W321.9)
- Integration with W2B (import POs — source of FX exposure), W30 (daily cash position — USD balances), W80 (FX hedging — forward contracts and MTM), W89 (bank reconciliation — FX transaction confirmation), W232 (LC — BSP reporting for import LCs), W233 (cash flow forecast — FX cash flow projections)

### Pain Points / Risks

- **BSP regulatory changes catching BuildRight unprepared**: BSP periodically updates the FX Manual, reporting thresholds, and documentary requirements; if Treasury does not actively monitor BSP circulars, the company may fail to comply with new requirements, risking penalties, account restrictions, or adverse BSP examination findings
- **USD cash hoarding vs. investment trade-off**: maintaining large USD bank balances for natural hedging earns minimal interest (Philippine banks offer near-zero rates on USD deposits); Treasury must balance the natural hedge benefit against the opportunity cost of not converting surplus USD to PHP for investment (W318)
- **Multi-currency exposure beyond USD**: while ~85% of imports are USD-denominated, BuildRight sources some goods from China (CNY), Japan (JPY), and Europe (EUR); managing multiple currency exposures with limited hedging tool availability in the Philippine market (forward contracts readily available for USD/PHP only) creates residual unhedged exposure in minor currencies
- **BSP examination resource disruption**: a BSP FX compliance examination requires Treasury to compile extensive documentation across multiple months and entities; this disrupts normal treasury operations for 1–2 weeks during preparation and examination
- **Intercompany FX complexity**: intercompany transactions (W14) between BuildRight entities are PHP-denominated, but if any entity holds USD, the intercompany settlement creates internal FX transactions that must be tracked separately from external FX exposure for both BSP reporting and intercompany elimination (W234)

### Staffing Implication

Weekly exposure analysis adds ~45 min/week; monthly BSP reporting adds 2–4 hours/month; quarterly strategy review adds 1 hour/quarter; annual policy update adds 2 hours/year; BSP examination preparation (if triggered) adds 8–16 hours. Total: ~5–7 hours/month steady-state, absorbed by Treasury Analyst and Treasury Manager within existing headcount.

### Time Estimate

**Total**: Weekly FX exposure review — 45 min/week; Monthly BSP reporting — 2–4 hours/month; Monthly FX exposure summary — 1 hour/month; Quarterly strategy review — 1 hour/quarter; Annual policy update — 2 hours/year; BSP examination preparation — 8–16 hours per examination (infrequent)

---

## W322. Treasury Policy, Governance & Risk Appetite Framework

| Field | Detail |
|---|---|
| **Trigger** | Annual policy review cycle; material change in business strategy, regulatory environment, or risk profile; new entity formation; post-incident policy revision (W320.10, W319.8) |
| **Frequency** | Annual comprehensive review; quarterly limit monitoring; ad-hoc revisions as triggered |
| **Volume** | 1 comprehensive annual review; 4 quarterly monitoring cycles; ~2–3 ad-hoc revisions/year driven by business changes |
| **Owner** | CFO |
| **Participants** | CFO, Treasury Manager, Controller, CEO, Board (Audit & Risk Committee), External Auditors |

### Background

BuildRight's treasury function manages PHP 62B annual revenue flows, ~210 bank accounts across 4 banking partners, an estimated PHP 200–500M surplus investment portfolio, 3–5 credit facilities, and ~40% of COGS exposed to foreign exchange risk. This workflow establishes the overarching treasury policy framework that governs all other treasury workflows (W232–W235, W30, W80, W137, W174, W317–W321). Without a formalized and board-approved policy, individual treasury workflows operate with inconsistent risk parameters, undefined escalation thresholds, and fragmented governance.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Policy scope definition**: Treasury Manager drafts the Treasury Policy document covering: (a) Investment Policy — permissible instruments (time deposits, T-bills, money market, SDA), counterparty credit quality minimums, single-counterparty concentration limits, maximum portfolio duration, benchmark yield target; (b) Funding Policy — permissible debt instruments, leverage limits, covenant thresholds, refinancing risk management; (c) FX Risk Policy — hedging mandate (50–80% coverage per W80), permissible hedging instruments, maximum unhedged exposure, natural hedging guidelines; (d) Operational Risk Policy — maker-checker thresholds (per W320), bank portal access standards, incident response escalation; (e) Liquidity Policy — minimum cash buffer (14-day operational requirement per W318), intercompany funding guidelines, emergency liquidity procedures; (f) Counterparty Risk Policy — bank counterparty minimum credit rating, single-bank exposure limits, counterparty review triggers; (g) Delegation of Authority (DOA) matrix — approval tiers for investments (per W318.3), debt drawdowns (per W319.3), FX contracts (per W80), intercompany transfers (per W137), payment authorizations (per W320.3) | Treasury Mgr | CFO | 2–3 days |
| 2 | **Risk appetite quantification**: CFO and Treasury Manager translate policy parameters into measurable risk appetite statements — (a) maximum portfolio loss tolerance (e.g., no single investment loss > PHP 10M without Board notification), (b) maximum FX unhedged exposure as % of forecasted payables, (c) maximum Debt-to-Equity ratio (aligned with W319.6 covenant, typically 2.0:1), (d) minimum liquidity buffer (PHP X days of operating expenses), (e) maximum single-counterparty credit exposure as % of total portfolio | CFO / Treasury Mgr | CEO | 1 day |
| 3 | **Board approval**: CFO presents Treasury Policy and Risk Appetite Framework to Audit & Risk Committee; Committee reviews and recommends to full Board; Board approves policy; policy effective date set; previous policy version archived | CFO | Board | 2–3 hours (Board meeting) |
| 4 | **Communication and training**: Treasury Manager communicates approved policy to all Treasury staff (2 analysts), AP team (3–5 clerks), and Controller; conducts briefing session on key changes from prior year; all staff acknowledge receipt and understanding in writing; policy document stored in controlled document repository (W255) | Treasury Mgr | CFO | 2–4 hours |
| 5 | **Quarterly limit monitoring**: Treasury Manager reviews actual treasury activity against policy parameters quarterly — (a) investment portfolio: counterparty concentration, duration, yield vs. benchmark, credit quality; (b) debt portfolio: leverage ratios, covenant headroom, maturity ladder; (c) FX: hedge coverage ratio, unhedged exposure vs. limit; (d) liquidity: cash buffer vs. minimum requirement; (e) operational: payment anomaly trends, security incidents, access review findings (W320.8); flags any policy breaches to CFO with remediation plan | Treasury Mgr | CFO | 4 hours/quarter |
| 6 | **Policy breach reporting**: if any quarterly monitoring review (step 5) or ongoing operation identifies a policy breach — (a) Treasury Manager documents breach: parameter breached, magnitude, duration, root cause; (b) CFO assesses materiality; (c) if material: CFO reports to Audit & Risk Committee at next meeting; (d) if immaterial: CFO approves remediation plan and monitors implementation; (e) all breaches logged in policy breach register with remediation status | Treasury Mgr / CFO | CEO | As needed |
| 7 | **Annual comprehensive review**: Treasury Manager and CFO conduct full policy review annually — (a) assess effectiveness of current policy parameters using trailing 12-month data; (b) benchmark policy terms against Philippine corporate treasury best practices and peer companies; (c) incorporate lessons from any policy breaches, security incidents (W320.10), covenant near-breaches (W319.8), or BSP examination findings (W321.7); (d) update policy for regulatory changes (BSP circulars, BIR rulings, SEC requirements); (e) update DOA matrix for organizational changes (new roles, departed staff); (f) draft updated policy and repeat steps 2–4 | Treasury Mgr / CFO | Board | 3–5 days |

### System Touchpoints

- Treasury policy document repository: version-controlled policy document with approval history, effective dates, and acknowledgement tracking (W322.1, W322.3–4)
- Counterparty limit dashboard: real-time counterparty exposure vs. approved limits per policy, with breach alerting (W322.5)
- Delegation of Authority (DOA) matrix: system-enforced approval tiers linked to user roles and transaction types — investment approval (W318.3), debt drawdown (W319.3), payment authorization (W320.3), FX contract approval (W80) (W322.1)
- Policy breach register: log of all policy breaches with root cause, materiality assessment, remediation plan, and closure confirmation (W322.6)
- Risk appetite dashboard: visual summary of key risk metrics vs. approved limits — leverage, liquidity buffer, FX hedge coverage, counterparty concentration, portfolio duration (W322.2, W322.5)
- Integration with W318 (investment — counterparty limits and DOA), W319 (debt — leverage limits and DOA), W320 (electronic banking — maker-checker thresholds), W321 (FX — hedge coverage mandates), W80 (FX hedging — instrument limits), W137 (intercompany — DOA), W255 (document management — policy storage), W120 (internal audit — annual treasury controls assessment)

### Pain Points / Risks

- **Policy-out-of-sync with business growth**: BuildRight is opening 10–15 new stores/year; policy parameters set at the start of a fiscal year may be obsolete by mid-year as revenue, debt, and cash balances grow; the annual review cycle may not keep pace, leaving Treasury operating under outdated limits
- **DOA matrix complexity across 5 entities**: each BuildRight entity may require different approval tiers based on entity size, board composition, and banking arrangements; maintaining a single group-wide DOA that is both practical and compliant with each entity's board resolutions creates governance complexity
- **Board bottleneck for policy changes**: any policy revision requiring Board approval must wait for the next scheduled Board or Audit & Risk Committee meeting; if an urgent policy change is needed (e.g., after a security incident per W320.10), the delay may leave Treasury operating under inadequate policy coverage
- **Insufficient policy awareness among operational staff**: if Treasury Analysts and AP Clerks are not thoroughly trained on policy parameters, they may execute transactions that inadvertently breach limits (e.g., placing an investment with a counterparty that exceeds concentration limits per W318); written acknowledgement alone does not ensure operational compliance
- **Regulatory evolution**: BSP, BIR, and SEC periodically issue new regulations affecting treasury operations (e.g., BSP FX Manual updates per W321, BIR transfer pricing rules per W235, SEC related-party disclosure requirements); the annual policy review must incorporate all regulatory changes since the last review

### Staffing Implication

Annual policy review and drafting requires 3–5 days from the Treasury Manager with CFO oversight. Quarterly monitoring requires 4 hours/quarter. Policy breach investigation requires ad-hoc time depending on severity. Communication and training requires 2–4 hours per policy update (annually). Total: ~8–10 days/year concentrated effort + 4 hours/quarter monitoring, absorbed by Treasury Manager and CFO within existing headcount. No incremental headcount required.

### Time Estimate

**Total**: Annual policy review and drafting — 3–5 days; Board approval — 2–3 hours; Communication and training — 2–4 hours; Quarterly limit monitoring — 4 hours/quarter; Policy breach investigation — ad-hoc (1–8 hours per breach)

---

## W323. Cash Concentration & Inter-Entity Pooling Operations

| Field | Detail |
|---|---|
| **Trigger** | Daily treasury cycle (morning); automated sweep execution; or ad-hoc request from entity controller |
| **Frequency** | Daily (automated sweeps); weekly manual review (aligned with W233 weekly cycle) |
| **Volume** | ~210 bank accounts across 5 entities and 4 banks; estimated daily sweep volume of PHP 500M–1.5B across all accounts |
| **Owner** | Treasury Analyst |
| **Participants** | Treasury Analyst, Treasury Manager, CFO (escalation only) |

### Background

BuildRight operates 5 legal entities with ~210 bank accounts across BDO, BPI, Metrobank, and Chinabank. Each store collects cash daily (PHP 2.1M average per store), and each entity maintains operating accounts for AP disbursements, payroll, and tax payments. Without systematic daily cash concentration, cash sits idle in ~200 store deposit accounts earning zero or minimal interest while the parent entity may simultaneously borrow to fund capex or working capital. This workflow governs the daily mechanics of moving cash from peripheral accounts to centralized operating accounts, managing target balances, and optimizing the group's consolidated cash position. It is the operational execution layer beneath the strategic cash flow forecasting in W233.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Morning cash position snapshot**: Treasury Analyst reviews overnight bank balances across all accounts via bank portal or API — (a) store deposit account balances (post-CIT deposit per W174), (b) DC operating account balances, (c) entity main operating account balances, (d) USD import accounts, (e) payroll and tax accounts, (f) investment accounts (per W318); system consolidates into a single multi-entity, multi-bank cash position dashboard | Treasury Analyst | Treasury Mgr | 30 min/day |
| 2 | **Zero-balance sweep execution — store accounts**: system automatically initiates zero-balance sweeps (ZBA) from store deposit accounts to each entity's main operating account — (a) BDO store accounts sweep to entity BDO operating account, (b) BPI store accounts sweep to entity BPI operating account, (c) Metrobank and Chinabank store accounts sweep similarly; sweep timing aligned with CIT deposit crediting (W174 step 6); Treasury Analyst confirms sweep completion and investigates any failed sweeps | System / Treasury Analyst | Treasury Mgr | 15 min/day |
| 3 | **Entity-to-entity concentration sweep**: Treasury Analyst evaluates each entity's consolidated position after store sweeps — (a) if a subsidiary entity (e.g., Logistics Inc.) has surplus cash exceeding its 3-day operational needs, initiate intercompany transfer to BuildRight Holdings operating account (per W137 IC loan framework); (b) if a subsidiary has a deficit, initiate intercompany loan drawdown from Holdings; (c) all intercompany sweeps documented as IC loans per W137 with arm's-length interest calculation | Treasury Analyst | Treasury Mgr | 30 min/day |
| 4 | **Target balance management**: Treasury Analyst maintains target balance per operating account type — (a) store deposit accounts: target PHP 0 (full sweep daily); (b) DC operating accounts: target PHP 5M per DC (to cover next-day vendor payments and operating expenses); (c) entity main operating accounts: target based on 14-day forecast from W233; (d) USD accounts: target based on next 30-day import payment schedule per W2B; (e) payroll accounts: target 0 except 1 day before payroll date; (f) tax accounts: target 0 except 2 days before tax filing date per W90; excess above target is swept to investment per W318 | Treasury Analyst | Treasury Mgr | 15 min/day |
| 5 | **Multi-bank coordination**: Treasury Analyst manages concentration across 4 banks — (a) if one bank has a surplus and another has a deficit, execute interbank transfer (PCHC PesoNet/InstaPay for PHP; wire transfer for USD); (b) optimize to minimize interbank transfer fees while ensuring all accounts meet target balances; (c) monitor bank API connectivity — if one bank's API is down, use manual bank portal transfers and flag for follow-up | Treasury Analyst | Treasury Mgr | 15 min/day |
| 6 | **Failed sweep resolution**: if any automated sweep fails (insufficient balance, bank system error, API outage, cut-off time miss) — (a) system alerts Treasury Analyst with failure reason; (b) Treasury Analyst investigates and re-initiates manually or schedules for next sweep cycle; (c) if failure results in account falling below target balance, Treasury Analyst executes manual interbank transfer to cover the gap; (d) tracks failed sweep frequency per bank for relationship review (W317.8) | Treasury Analyst | Treasury Mgr | As needed (15–30 min/occurrence) |
| 7 | **Weekly concentration report**: as part of W233 weekly cycle, Treasury Analyst prepares weekly concentration summary — (a) total cash concentrated per entity, (b) sweep success rate by bank, (c) failed sweep incidents and root causes, (d) average daily idle cash (cash sitting in non-operating accounts above target), (e) recommendations for sweep timing or target balance adjustments | Treasury Analyst | Treasury Mgr | 30 min/week |

### System Touchpoints

- Multi-bank cash position dashboard: real-time consolidated view of all 210 accounts across 4 banks with entity-level and bank-level subtotals (W323.1)
- Automated zero-balance sweep engine: configurable sweep rules per account — sweep direction (account A → account B), sweep timing (morning/afternoon), minimum sweep threshold, and exception handling; supports ZBA, target balance, and threshold-based sweep types (W323.2)
- Intercompany sweep integration: entity-to-entity concentration sweeps automatically create IC loan entries per W137 framework with interest accrual (W323.3)
- Target balance configuration per account with automated excess-to-investment routing (integration with W318) (W323.4)
- Interbank transfer execution via PCHC PesoNet/InstaPay integration; manual transfer logging for contingency scenarios (W323.5)
- Failed sweep alerting and resolution tracking with bank-level failure rate reporting (W323.6)
- Weekly concentration report: auto-generated summary with sweep analytics (W323.7)
- Integration with W30 (daily cash position — primary data source), W174 (CIT — store cash deposits feed concentration), W233 (weekly forecast — target balance inputs), W318 (surplus investment — excess sweep destination), W137 (IC loans — entity sweeps create IC loan records), W89 (bank reconciliation — sweep transactions matched), W317 (bank accounts — account structure and sweep configuration)

### Pain Points / Risks

- **Bank API outages disrupting concentration**: BPI and BDO bank APIs experience periodic downtime during month-end and quarter-end processing; if the automated sweep engine cannot connect, Treasury must execute manual transfers across 200+ store accounts, which is operationally impossible within the same-day window — resulting in idle cash remaining in store accounts earning zero interest
- **PCHC settlement timing**: interbank Peso transfers settle via PCHC at specific cut-off times (typically 2:00 PM for same-day settlement); if Treasury Analyst misses the cut-off while resolving a failed sweep, the transfer settles T+1, leaving the receiving account below target for an additional day
- **USD concentration limitations**: USD interbank transfers require wire transfer (not PesoNet) with longer settlement (T+1 or T+2) and higher fees; concentrating USD from entity accounts to the main USD import account adds cost and latency, creating a trade-off between USD pooling efficiency and transfer fees
- **Intercompany tax implications of daily sweeps**: each entity-to-entity concentration sweep creates an IC loan per W137; the volume of daily IC loan movements (potentially 5–10 per day) creates significant IC loan reconciliation complexity at month-end, and BIR may scrutinize the arm's-length interest rate treatment on high-frequency, short-duration IC loans
- **Store deposit timing variability**: CIT vendor (W174) deposits store cash to bank accounts at varying times during the day; if the ZBA sweep executes before the CIT deposit credits the store account, the day's cash collection is not concentrated until the next sweep cycle (T+1), leaving cash idle overnight

### Staffing Implication

Daily concentration operations require approximately 1.5–2 hours/day of Treasury Analyst time (position snapshot 30 min + sweep confirmation 15 min + entity concentration 30 min + target balance management 15 min + multi-bank coordination 15 min). Weekly reporting adds 30 min/week. Failed sweep resolution adds variable time (estimated 15–30 min/day average across all incidents). Total: ~10–12 hours/week, which is a core responsibility of the Treasury Analyst role. This workload is a primary driver for the 2–3 Treasury Analyst FTEs in the staffing plan.

### Time Estimate

**Total**: Morning cash position snapshot — 30 min/day; ZBA sweep confirmation — 15 min/day; Entity-to-entity concentration — 30 min/day; Target balance management — 15 min/day; Multi-bank coordination — 15 min/day; Failed sweep resolution — 15–30 min/day (average); Weekly concentration report — 30 min/week

---

## W324. Supply Chain Finance & Dynamic Discounting Program

| Field | Detail |
|---|---|
| **Trigger** | Vendor early-payment discount opportunity; quarterly SCF program review; new vendor onboarding to SCF platform; or strategic working capital optimization initiative |
| **Frequency** | Ongoing (transaction-level); quarterly program review; annual bank SCF facility renewal |
| **Volume** | Estimated 50–100 key vendors eligible for SCF (representing ~60% of total procurement spend); dynamic discounting applicable to ~200–500 invoices/month during peak construction season |
| **Owner** | Treasury Manager |
| **Participants** | Treasury Manager, AP Manager, Procurement Director, CFO, SCF Bank Partner, Key Vendors |

### Background

BuildRight's procurement spend is approximately PHP 37B/year (COGS), with ~50–100 key vendors representing 60% of total spend. Standard payment terms are 30–60 days per W7. Two mechanisms can optimize working capital: (a) **Supply Chain Finance (SCF)** — a bank-funded program where the bank pays BuildRight's vendors early (at a discount to face value) and BuildRight pays the bank at the original invoice due date, extending effective payment terms without impacting vendor cash flow; (b) **Dynamic Discounting** — BuildRight self-funds early payment to vendors in exchange for a sliding-scale discount (e.g., 2% for payment at 10 days, 1% at 20 days, 0.5% at 30 days vs. standard 45-day terms). Both mechanisms improve working capital efficiency but require distinct operational, legal, and risk management workflows.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Vendor eligibility assessment**: AP Manager and Procurement Director identify vendors eligible for SCF or dynamic discounting based on: (a) annual spend > PHP 10M, (b) payment history (no chronic disputes per W244), (c) strategic importance (JBP vendors per W155), (d) vendor willingness to participate, (e) vendor's cost of borrowing vs. SCF discount rate (if SCF is cheaper than vendor's own borrowing, vendor benefits) | AP Manager / Procurement | Treasury Mgr | 1–2 days/quarter |
| 2 | **SCF program setup**: Treasury Manager coordinates with SCF bank partner to establish the program — (a) negotiate SCF facility terms: facility limit, discount rate or margin over benchmark, recourse vs. non-recourse structure, eligible invoice criteria, vendor onboarding process; (b) Legal reviews SCF agreement (per W230) including recourse provisions, dispute resolution, and set-off rights; (c) configure SCF platform integration with ERP: auto-upload approved invoices eligible for SCF, vendor portal for discount acceptance, bank payment confirmation feed | Treasury Mgr | CFO | 2–4 weeks (initial setup) |
| 3 | **Dynamic discounting configuration**: Treasury Manager configures dynamic discounting parameters in ERP — (a) discount tiers: sliding-scale discount rates by early-payment day range (e.g., 2%/10 net 45, 1.5%/20 net 45, 1%/30 net 45); (b) minimum invoice amount for dynamic discounting (e.g., PHP 100K); (c) maximum early-payment budget per month (tied to cash position per W233); (d) auto-offer vs. manual-offer mode (auto-offer for tier-1 vendors, manual approval for others) | Treasury Mgr | CFO | 1 day (initial); 2 hours/quarter (review) |
| 4 | **Invoice-level early-payment decision**: for each eligible approved invoice (post W7 3-way match), system evaluates — (a) SCF option: if vendor is enrolled in SCF program, offer invoice to SCF bank for early payment; bank pays vendor at discount and BuildRight pays bank at original due date; (b) Dynamic discounting option: if BuildRight has surplus cash (per W318.1 surplus identification) and the discount yield exceeds the investment return rate (per W318), self-fund early payment for the discount; (c) neither: pay at standard terms per W7; Treasury Analyst reviews system recommendation and confirms action | Treasury Analyst | Treasury Mgr | 15 min/batch (daily) |
| 5 | **SCF transaction execution**: SCF bank pays vendor early; system records: (a) reduction of AP to vendor (replaced by obligation to SCF bank), (b) SCF financing cost accrual (discount charged by bank), (c) SCF payable to bank at original invoice due date; at original due date, Treasury executes payment to SCF bank via standard payment run (W7) | System / Treasury Analyst | Treasury Mgr | Automated |
| 6 | **Dynamic discounting execution**: Treasury Analyst executes early payment to vendor — (a) system calculates discount amount based on payment date and discount tier, (b) system generates payment for invoice face value less discount, (c) AP module records discount taken (Dr. AP full / Cr. Cash net / Cr. Purchase Discount), (d) vendor confirms receipt; system tracks discount income vs. investment return foregone for yield comparison | Treasury Analyst | Treasury Mgr | Automated (within W7 payment run) |
| 7 | **Quarterly program review**: Treasury Manager reviews SCF and dynamic discounting program performance — (a) total invoices processed through SCF vs. dynamic discounting vs. standard terms, (b) total discount income earned (both programs), (c) SCF financing cost vs. BuildRight's cost of debt (W319), (d) dynamic discount yield vs. investment return (W318), (e) vendor participation rate and satisfaction, (f) working capital impact (DSO/DPO improvement), (g) SCF bank facility utilization vs. limit; recommends adjustments to program parameters and vendor eligibility | Treasury Mgr | CFO | 4 hours/quarter |
| 8 | **Annual SCF facility renewal**: Treasury Manager negotiates SCF facility renewal with bank partner — reviews facility limit, pricing, recourse terms, and platform functionality; presents renewal recommendation to CFO with competitive analysis if alternative SCF providers are available; CFO approves renewal terms | Treasury Mgr | CFO | 4–8 hours/year |

### System Touchpoints

- SCF platform integration: ERP-to-SCF bank platform connection for automated invoice upload, vendor portal, bank payment confirmation, and reconciliation (W324.2, W324.5)
- Dynamic discounting engine: configurable discount tiers with auto-calculation of discount amount based on payment date; auto-offer and manual-approve modes; budget constraint enforcement (maximum early-payment budget per month) (W324.3, W324.6)
- Early-payment decision dashboard: for each eligible invoice, system shows SCF cost, dynamic discount yield, investment return alternative, and recommended action (W324.4)
- SCF transaction tracking: SCF payables tracked separately from regular AP; SCF financing cost accrual; SCF maturity calendar (W324.5)
- Discount income analytics: total discount earned by program, vendor, and period; yield comparison vs. investment alternatives; working capital impact measurement (W324.7)
- Integration with W7 (AP payment runs — SCF and dynamic discount payments executed through standard payment process), W30 (daily cash position — early payment cash outflows reflected), W233 (cash flow forecast — SCF and discounting cash flows incorporated), W318 (surplus investment — dynamic discount yield vs. investment return comparison), W155 (vendor JBP — strategic vendors prioritized for SCF enrollment), W230 (legal contract review — SCF agreement), W244 (vendor disputes — disputed invoices excluded from SCF/discounting)

### Pain Points / Risks

- **SCF bank dependency and concentration**: reliance on a single SCF bank partner creates concentration risk — if the bank reduces its SCF facility limit or withdraws from the Philippine SCF market, BuildRight must quickly onboard an alternative provider, disrupting vendor payment expectations
- **Dynamic discounting cash drain during deficit periods**: if Treasury aggressively self-funds early payments during a period of surplus, and an unexpected cash need arises (emergency capex, debt service), the cash used for dynamic discounting may not be recoverable quickly enough; the monthly budget constraint (step 3c) mitigates but does not eliminate this risk
- **Vendor gaming of payment terms**: if key vendors learn that BuildRight will consistently pay early via SCF or dynamic discounting, they may inflate standard invoice prices or extend quoted standard terms to capture the early-payment economics for themselves, negating BuildRight's benefit
- **Accounting treatment complexity**: SCF transactions in the Philippines may require careful presentation under PFRS — recourse SCF may need to be presented as borrowing (increasing reported debt) rather than as trade payable settlement, impacting covenant calculations per W319; BIR treatment of SCF costs as interest expense vs. purchase discount requires clarification
- **Vendor onboarding friction**: Philippine MSME vendors (many of BuildRight's suppliers) may lack the sophistication or banking infrastructure to participate in SCF programs; the vendor onboarding process may be perceived as burdensome, reducing participation among the vendor base that would benefit most

### Staffing Implication

Initial SCF program setup requires 2–4 weeks of concentrated Treasury Manager effort (one-time). Ongoing operations add ~15 min/day for early-payment decisions and ~4 hours/quarter for program review. Dynamic discounting configuration requires 1 day initially and 2 hours/quarter for review. Annual SCF facility renewal requires 4–8 hours. Total: ~8–10 hours/month after initial setup, absorbed by Treasury Manager and Treasury Analyst within existing headcount.

### Time Estimate

**Total**: Initial SCF program setup — 2–4 weeks; Dynamic discounting configuration — 1 day; Daily early-payment decisions — 15 min/day; Quarterly program review — 4 hours/quarter; Annual SCF facility renewal — 4–8 hours/year

---

## W325. Corporate Guarantee & Contingent Liability Management

| Field | Detail |
|---|---|
| **Trigger** | New corporate guarantee issuance request; performance bond requirement; bid bond for government procurement (W78); subsidiary covenant support; annual contingent liability review; or guarantee expiry/termination |
| **Frequency** | ~10–15 new guarantees/bonds per year; annual comprehensive review; ongoing monitoring of contingent exposure |
| **Volume** | Estimated 20–30 active guarantees and contingent liabilities at any given time across 5 entities (construction performance bonds, government bid bonds, subsidiary corporate guarantees, lease guarantees) |
| **Owner** | Treasury Manager |
| **Participants** | Treasury Manager, Treasury Analyst, CFO, Legal, Procurement, Engineering (for construction bonds), Compliance |

### Background

W232 covers bank guarantees related to import LCs, but BuildRight issues and receives multiple other types of guarantees and contingent liabilities: (a) **Performance bonds** for store construction (W223–227) — contractors provide performance bonds to guarantee completion; BuildRight may also issue counter-guarantees to contractor banks; (b) **Bid bonds** for government/institutional procurement participation (W78) — guarantee that BuildRight will honor its bid if awarded; (c) **Corporate guarantees** for subsidiary entities — BuildRight Holdings may guarantee debt facilities of Depot Inc., Logistics Inc., or Property Inc.; (d) **Lease guarantees** — landlords of leased store locations (W117) may require corporate guarantees from BuildRight Holdings as lease security; (e) **Utility and vendor deposits** — guaranteed by parent entity. These contingent liabilities are not reflected on the balance sheet but must be tracked, monitored, and disclosed under PFRS (PAS 37 Provisions, Contingent Liabilities and Contingent Assets).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Guarantee issuance request**: triggered by contract award, lease signing, or subsidiary funding need — requesting department (Engineering for construction bonds, Procurement for bid bonds, Real Estate for lease guarantees, Treasury for subsidiary guarantees) submits guarantee request: type, beneficiary, amount, duration, underlying obligation, and expiry date | Requesting Dept | Treasury Mgr | 30 min/request |
| 2 | **Risk assessment**: Treasury Manager evaluates the guarantee request — (a) underlying obligation risk: what is the probability of the guarantee being called? (construction non-performance, bid withdrawal, subsidiary default); (b) maximum exposure: guaranteed amount plus any penalties or interest; (c) cross-guarantee netting: is the exposure offset by a counter-guarantee or holdback? (e.g., contractor performance bond offsets BuildRight's guarantee to the bank); (d) existing contingent liability portfolio concentration: does adding this guarantee create excessive exposure to a single beneficiary or contractor? | Treasury Mgr | CFO | 1–2 hours/guarantee |
| 3 | **Approval**: tiered by guarantee amount and type — (a) ≤ PHP 50M standard guarantee: CFO approves; (b) PHP 50M–200M: CEO approves; (c) > PHP 200M or subsidiary debt guarantee: Board approves; (d) government bid bonds ≤ PHP 10M: Treasury Manager approves (routine, low risk) | Approver | Approver | 15 min/guarantee |
| 4 | **Documentation and issuance**: Legal prepares guarantee instrument (per W230 review if non-standard); Treasury Manager coordinates with bank for bank-issued guarantees (bank charges issuance fee, typically 1–2% per annum of guaranteed amount) or executes corporate guarantee letter for direct entity guarantees; guarantee recorded in contingent liability register with: guarantor entity, beneficiary, amount, type, start date, expiry date, underlying reference (contract/lease/loan), and status (Active/Expired/Called/Released) | Legal / Treasury Mgr | CFO | 1–2 days |
| 5 | **Ongoing monitoring**: Treasury Analyst monitors active guarantees — (a) track approaching expiry dates (system alerts 60 days before expiry); (b) confirm whether underlying obligation is fulfilled (construction completed per W227, lease terminated per W117, bid awarded/lost); (c) if underlying obligation is fulfilled, initiate guarantee release with beneficiary; (d) if underlying obligation is extended (e.g., construction delay), arrange guarantee extension with bank and beneficiary | Treasury Analyst | Treasury Mgr | 1 hour/month |
| 6 | **Guarantee call management**: if a beneficiary calls a guarantee — (a) Treasury Manager immediately notifies CFO and Legal; (b) Legal reviews call validity (is the call justified under guarantee terms?); (c) if valid: Treasury arranges payment to beneficiary within guarantee timeline; system records guarantee call as actual liability (Dr. Guarantee Call Expense / Cr. Cash, and if recoverable from contractor/subsidiary: Dr. Receivable from Contractor / Cr. Cash); (d) if disputed: Legal engages with beneficiary to contest the call; Treasury ensures cash is available for potential payment pending resolution | Treasury Mgr / Legal | CFO | As needed (urgent) |
| 7 | **Release and closure**: when underlying obligation is fulfilled and guarantee is no longer needed — (a) Treasury Analyst requests release confirmation from beneficiary; (b) for bank-issued guarantees, instructs bank to release and return any collateral; (c) updates contingent liability register status to "Released"; (d) for performance bonds: release is triggered by certificate of completion (W227) | Treasury Analyst | Treasury Mgr | 30 min/guarantee |
| 8 | **PFRS disclosure preparation**: quarterly, Treasury Manager provides contingent liability summary to Controller for financial statement disclosure — (a) list of active guarantees with amounts and beneficiaries, (b) guarantees called during the period, (c) probability assessment of guarantee calls (per PAS 37: remote, possible, probable), (d) movement in contingent liabilities (new issuances, expirations, releases, calls), (e) contingent liability note for quarterly and annual financial statements | Treasury Mgr | Controller | 2 hours/quarter |
| 9 | **Annual comprehensive review**: Treasury Manager reviews all contingent liabilities — (a) assess each active guarantee for continued necessity, (b) identify guarantees for underlying obligations that have been fulfilled but not yet released, (c) evaluate guarantee portfolio concentration (by beneficiary, contractor, entity), (d) review guarantee costs (bank issuance fees) vs. budget, (e) update risk assessments for each guarantee, (f) report to CFO and Audit & Risk Committee | Treasury Mgr | CFO | 4–6 hours/year |

### System Touchpoints

- Contingent liability register: centralized tracking of all guarantees, bonds, and contingent liabilities across entities with full lifecycle management (Issuance → Active → Expired/Called/Released) (W325.4)
- Guarantee expiry alerting: automated alerts at 60, 30, and 7 days before expiry (W325.5)
- Integration with underlying workflows: W223–227 (construction — performance bond tracking), W78 (government procurement — bid bond tracking), W117 (lease admin — lease guarantee tracking), W319 (debt facilities — subsidiary corporate guarantees), W230 (legal review — guarantee instrument drafting)
- PFRS PAS 37 disclosure report: auto-generated contingent liability movement schedule and probability assessment (W325.8)
- Guarantee call tracking: payment execution, recovery receivable creation, and resolution documentation (W325.6)
- Integration with W89 (bank reconciliation — guarantee fee payments), W9A (month-end — contingent liability disclosure), W9B (year-end — PAS 37 note), W120 (internal audit — contingent liability controls review), W322 (treasury policy — guarantee DOA)

### Pain Points / Risks

- **Forgotten guarantees remaining active after obligation fulfillment**: with 20–30 active guarantees and construction projects spanning 6–18 months, it is easy for a performance bond to remain active (and incurring annual issuance fees from the bank) after the construction is completed and commissioned (W227); without systematic expiry monitoring and release triggers, BuildRight pays unnecessary guarantee fees
- **Guarantee call liquidity impact**: if a major contractor fails to complete a store construction project (e.g., PHP 80–120M project) and BuildRight calls the performance bond, the bank may simultaneously call BuildRight's counter-guarantee; the sudden cash outflow (potentially PHP 50–100M) must be funded from operating cash or credit facility (W319), disrupting liquidity planning
- **Subsidiary guarantee cross-default risk**: if BuildRight Holdings guarantees a Depot Inc. credit facility and Depot Inc. experiences financial distress, the guarantee call could trigger cross-default provisions in Holdings' own debt facilities (W319), cascading liquidity pressure to the parent entity
- **Government procurement bid bond lock-up**: BuildRight participates in government/institutional procurement (W78); bid bonds are held by the government agency for the duration of the bidding process (often 3–6 months in the Philippines due to procurement delays); the bank's contingent exposure against BuildRight's credit facility reduces available headroom during the bid period
- **PFRS PAS 37 disclosure incompleteness**: if the contingent liability register is not comprehensive (e.g., verbal guarantees or informal commitments are not recorded), the financial statement disclosure under PAS 37 will be incomplete, creating audit qualification risk and SEC reporting non-compliance

### Staffing Implication

~10–15 new guarantees per year requiring 1–2 hours each for risk assessment, documentation, and issuance = 15–30 hours/year. Ongoing monitoring requires 1 hour/month. PFRS disclosure preparation requires 2 hours/quarter. Annual review requires 4–6 hours. Total: ~6–8 hours/month, absorbed by Treasury Manager and Treasury Analyst within existing headcount.

### Time Estimate

**Total**: Guarantee issuance — 1–2 days per guarantee (including legal documentation and bank processing); Risk assessment — 1–2 hours/guarantee; Ongoing monitoring — 1 hour/month; PFRS disclosure — 2 hours/quarter; Annual review — 4–6 hours/year; Guarantee call management — urgent, 4–8 hours per call event

---

## W326. Treasury Month-End Close & Reconciliation

| Field | Detail |
|---|---|
| **Trigger** | Month-end close (W9A) calendar — typically Day 1–3 of the following month |
| **Frequency** | Monthly |
| **Volume** | ~210 bank accounts, 3–5 credit facilities, investment portfolio, 10–20 active FX forward contracts, 5 entities |
| **Owner** | Treasury Manager |
| **Participants** | Treasury Manager, Treasury Analyst, Controller, Chief Accountant |

### Background

W9A covers the overall month-end close process, but treasury has specific month-end activities that are operationally distinct and must be completed before the Controller can finalize the general ledger. These include: investment interest accrual, loan interest accrual, FX revaluation of open items, intercompany loan interest calculation, bank fee verification, and treasury account reconciliation. If treasury month-end tasks are delayed, the entire close timeline (target: Day 5 working days) is at risk. This workflow defines the treasury-specific month-end checklist and sequencing.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Bank statement finalization**: Treasury Analyst confirms all bank statements (per entity, per bank) are received and imported for the closed month — (a) BDO, BPI, Metrobank, Chinabank statements for all ~210 accounts; (b) flag any missing statements and request from bank relationship manager; (c) system auto-matches bank statement lines to ERP transactions (first pass of W89) | Treasury Analyst | Treasury Mgr | 2 hours/month |
| 2 | **Investment portfolio accrual**: Treasury Analyst calculates and posts month-end investment interest accrual — (a) for each active time deposit/placement (per W318 register): accrued interest = principal × rate × days elapsed / 360; (b) system posts accrual journal (Dr. Accrued Interest Receivable / Cr. Interest Income); (c) for matured placements during the month: confirm interest income posted correctly at redemption | Treasury Analyst | Treasury Mgr | 1 hour/month |
| 3 | **Loan interest accrual**: Treasury Analyst calculates and posts month-end loan interest accrual — (a) for each active credit facility/drawdown (per W319 register): accrued interest = outstanding balance × interest rate × days in month / 360 (for floating rate: use rate at month-end); (b) system posts accrual journal (Dr. Interest Expense / Cr. Accrued Interest Payable); (c) verify that monthly interest payments made during the month are not double-counted in accrual | Treasury Analyst | Treasury Mgr | 1 hour/month |
| 4 | **FX revaluation**: Treasury Analyst performs month-end FX revaluation of open foreign currency items — (a) open AP in foreign currency (import payables per W2B): revalue at BSP closing rate at month-end; (b) open AR in foreign currency (if any); (c) USD bank account balances: revalue at BSP closing rate; (d) open forward contracts (per W80): mark-to-market at month-end forward rate; (e) system posts unrealized FX gain/loss journals (Dr./Cr. Unrealized FX Gain/Loss and corresponding balance sheet account); (f) document FX rates used (BSP published closing rates) for audit trail | Treasury Analyst | Treasury Mgr | 2 hours/month |
| 5 | **Intercompany loan interest calculation**: Treasury Analyst calculates monthly interest on intercompany loans (per W137) — (a) for each active IC loan: interest = outstanding balance × arm's-length rate × days in month / 360; (b) post IC interest accrual (Dr. IC Interest Receivable from Borrower Entity / Cr. IC Interest Income at Lender Entity); (c) ensure elimination entries in consolidation (W234) will net IC interest to zero at group level | Treasury Analyst | Treasury Mgr | 1 hour/month |
| 6 | **Bank fee verification**: Treasury Analyst reviews bank fees charged during the month across all accounts — (a) compare actual fees charged (from bank statements imported in step 1) against agreed fee schedules per bank (per W317.9); (b) flag any unexpected or excess fees; (c) initiate dispute with bank for any overcharges; (d) post bank fee expense journal if not auto-posted by bank statement import | Treasury Analyst | Treasury Mgr | 1 hour/month |
| 7 | **Treasury account reconciliation**: Treasury Analyst reconciles key treasury general ledger accounts — (a) Cash and Cash Equivalents: GL balance vs. sum of all bank statement balances; (b) Short-Term Investments: GL balance vs. investment register (W318); (c) Loans Payable (current and non-current): GL balance vs. loan register (W319); (d) Accrued Interest Receivable (investments): GL balance vs. calculated accrual (step 2); (e) Accrued Interest Payable (loans): GL balance vs. calculated accrual (step 3); (f) IC Loans Receivable/Payable: GL balance vs. IC loan sub-ledger (step 5); (g) investigates and resolves any variances | Treasury Analyst | Treasury Mgr | 2 hours/month |
| 8 | **Treasury close certification**: Treasury Manager reviews all treasury month-end tasks (steps 1–7) and confirms completion to Controller — (a) all bank statements received and imported, (b) all accruals posted, (c) FX revaluation completed, (d) all reconciling items resolved or documented, (e) sign-off on treasury month-end checklist; Controller incorporates treasury sign-off into overall month-end close gate (W9A) | Treasury Mgr | Controller | 1 hour/month |

### System Touchpoints

- Month-end treasury checklist: configurable task list with completion tracking, assignee, and deadline per task; integrated with W9A overall close calendar (W326.8)
- Bank statement import and auto-matching: automated import of bank statements from all 4 banks; first-pass matching for W89 reconciliation (W326.1)
- Investment accrual calculator: auto-calculates interest accrual per active placement based on principal, rate, and days elapsed; generates accrual journal (W326.2)
- Loan accrual calculator: auto-calculates interest accrual per active loan/drawdown; generates accrual journal (W326.3)
- FX revaluation engine: revalues all open foreign currency items (AP, AR, bank balances, forward contracts) at month-end BSP rate; generates unrealized FX gain/loss journals; maintains rate audit trail (W326.4)
- IC loan interest calculator: auto-calculates IC loan interest per arm's-length rate; generates IC interest accrual with automatic elimination flag for consolidation (W326.5)
- Bank fee variance dashboard: actual fees vs. agreed schedule with variance flagging and dispute tracking (W326.6)
- Treasury GL reconciliation: automated reconciliation of treasury accounts with variance investigation workflow (W326.7)
- Integration with W9A (month-end close — treasury close gate), W89 (bank reconciliation — statement import feeds treasury close), W318 (investments — register for accrual), W319 (debt — register for accrual), W80 (FX hedging — forward contract MTM), W137 (IC loans — interest calculation), W234 (consolidation — IC interest elimination), W317 (bank accounts — fee schedules), W322 (treasury policy — month-end procedures)

### Pain Points / Risks

- **Bank statement delays cascading into close timeline**: if any of the 4 banks delays statement availability (BDO and Metrobank are known to have slower month-end processing in the Philippines), Treasury cannot complete step 1, which blocks steps 2–7; this cascades into the overall W9A close timeline, potentially pushing the close beyond the target Day 5 working day deadline
- **FX revaluation complexity with multiple forward contracts**: with 10–20 active forward contracts (per W80) at different notional amounts, forward rates, and maturity dates, the month-end MTM revaluation requires careful calculation; an error in any single contract's MTM misstates the unrealized FX gain/loss, which flows through to the income statement
- **IC loan interest timing mismatch**: IC loan interest must be accrued at each entity individually for tax purposes, but must eliminate perfectly at consolidation; if one entity accrues on an actual/360 basis and another on a 30/360 basis, or if the outstanding balance on the last day of the month differs between lender and borrower sub-ledgers (due to a late sweep per W323), the elimination fails and creates a reconciliation gap in W234
- **Treasury close workload concentration**: all 7 treasury month-end tasks must be completed within Day 1–3 of the close to unblock the Controller's remaining close tasks; this creates peak workload for the Treasury Analyst at the exact time when daily operations (W323 concentration, W30 cash position) also continue without pause
- **Audit scrutiny of treasury accruals**: external auditors (per W95) focus heavily on treasury month-end entries — investment valuation, loan balances, FX revaluation, and IC transactions — because these are high-value, judgment-intensive areas susceptible to management bias; incomplete documentation or unsupported assumptions in any accrual attract audit queries that extend the close timeline

### Staffing Implication

Monthly treasury close requires approximately 10–11 hours (statement finalization 2 hrs + investment accrual 1 hr + loan accrual 1 hr + FX revaluation 2 hrs + IC interest 1 hr + bank fee verification 1 hr + reconciliation 2 hrs + certification 1 hr). This work is concentrated in Day 1–3 of the monthly close and is performed by the Treasury Analyst with Treasury Manager review. The workload is absorbed within existing headcount but represents peak intensity during close periods.

### Time Estimate

**Total**: Bank statement finalization — 2 hours; Investment accrual — 1 hour; Loan interest accrual — 1 hour; FX revaluation — 2 hours; IC loan interest — 1 hour; Bank fee verification — 1 hour; Treasury GL reconciliation — 2 hours; Treasury close certification — 1 hour; **Total: ~11 hours/month** (concentrated in Day 1–3 of close)

---

## W327. External Shareholder Dividend Declaration & Payment

| Field | Detail |
|---|---|
| **Trigger** | Board decision to declare dividend; annual stockholders' meeting; or special dividend declaration |
| **Frequency** | Annual (typical for Philippine corporations); occasionally semi-annual or special |
| **Volume** | 1–2 dividend declarations per year; single payment run to all shareholders |
| **Owner** | Treasury Manager |
| **Participants** | CFO, Corporate Secretary, Legal, Board of Directors, Controller, Tax Manager, External Auditor, Stock Transfer Agent (if applicable) |

### Background

W137 covers intercompany dividends between BuildRight entities, which involve internal fund transfers and IC tax withholding. This workflow covers the distinctly different process of BuildRight Holdings declaring and paying dividends to its external shareholders. Under the Revised Corporation Code of the Philippines (RCC), dividend declarations require board resolution, compliance with statutory solvency tests, withholding tax (10% final withholding tax for Philippine resident individuals per TRAIN law, 15% for resident foreign corporations), SEC filing of the board resolution, and timely payment execution. For a company of BuildRight's scale, even a modest dividend yield on estimated equity represents a material cash outflow and a significant governance event.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Dividend feasibility assessment**: Controller and CFO assess BuildRight Holdings' capacity to pay dividends — (a) verify retained earnings availability per latest audited financial statements (W9B); (b) confirm compliance with RCC solvency test: assets must exceed liabilities by at least the dividend amount after payment; (c) verify no debt covenant restrictions on dividend payment (per W319 facility agreements — some credit facilities include dividend restriction covenants); (d) assess cash availability post-dividend using cash flow forecast (W233) — dividend payment must not breach minimum liquidity buffer (per W322 policy); (e) Tax Manager estimates withholding tax liability for dividend payment | Controller / Tax Mgr | CFO | 1–2 days |
| 2 | **Board resolution preparation**: Corporate Secretary prepares draft Board Resolution for dividend declaration — (a) dividend amount per share, (b) record date (date determining which shareholders are entitled), (c) ex-dividend date (for listed or quasi-listed entities), (d) payment date (typically 30–45 days after declaration per RCC), (e) dividend type (cash, property, or stock); Legal reviews compliance with RCC and company by-laws (per W124) | Corp Secretary / Legal | CFO | 1–2 days |
| 3 | **Board approval**: Board of Directors reviews and approves dividend declaration at Board meeting or via written assent; Board Resolution signed by Corporate Secretary; dividend becomes a legally binding obligation of the corporation upon Board approval | Board / Corp Secretary | Board Chair | Board meeting |
| 4 | **SEC filing**: Corporate Secretary files Board Resolution with SEC (if required per corporate governance standards or if BuildRight is registered with SEC as a reporting entity); files GIS (General Information Sheet) update if dividend affects ownership disclosures | Corp Secretary | CFO | 1–2 days |
| 5 | **Shareholder notification**: Corporate Secretary notifies all shareholders of declared dividend — (a) dividend amount per share, (b) record date, (c) payment date, (d) withholding tax rate applicable, (e) net amount to be received, (f) payment method (direct bank deposit or check); notification sent at least 15 days before payment date | Corp Secretary | — | 1 day |
| 6 | **Withholding tax computation**: Tax Manager computes final withholding tax per shareholder — (a) Philippine resident individuals: 10% final withholding tax (per TRAIN law, Republic Act 10963); (b) Philippine resident domestic corporations: exempt from withholding tax on dividends received (intercorporate dividend exemption); (c) Philippine resident foreign corporations: 15% final withholding tax (unless reduced by tax treaty); (d) non-resident individuals: 25% (unless reduced by tax treaty); Tax Manager prepares withholding tax schedule per shareholder | Tax Manager | CFO | 1 day |
| 7 | **Dividend accrual**: Controller posts dividend payable accrual in GL — (a) Dr. Retained Earnings / Cr. Dividends Payable (gross amount); (b) Dr. Dividends Payable / Cr. Expanded Withholding Tax Payable (withholding tax per step 6); (c) net dividend payable = gross minus withholding tax | Controller | CFO | 2 hours |
| 8 | **Payment execution**: on payment date, Treasury Analyst executes dividend payment — (a) for shareholders receiving direct bank deposit: generate payment file from shareholder register (bank account details on file); (b) for shareholders receiving check: Treasury Manager signs dividend checks per signatory authority (W317); (c) system records payment: Dr. Dividends Payable / Cr. Cash (net amount per shareholder); (d) remit withholding tax to BIR via eFPS (per W260) within the prescribed deadline (10th day of the month following withholding or 25th for eFPS filers) | Treasury Analyst / Treasury Mgr | CFO | 1 day |
| 9 | **Post-payment reconciliation**: Treasury Analyst reconciles dividend payments — (a) confirm all shareholders received payment (bank confirmation for deposits, check clearing for checks); (b) for uncashed dividend checks: follow up with shareholders; uncashed dividends held in trust per RCC requirements; (c) Controller posts final dividend entries and clears Dividends Payable; (d) Tax Manager confirms withholding tax remittance via BIR eFPS receipt (W260) | Treasury Analyst / Controller | Treasury Mgr | 1 day |
| 10 | **Year-end disclosure**: Controller includes dividend information in year-end financial statement notes — (a) dividends declared and paid during the year, (b) dividends per share, (c) dividend payout ratio, (d) dividends in arrears (if any, for preferred shares), (e) dividend withholding tax remitted; External Auditor verifies dividend computation, solvency compliance, and withholding tax (per W95) | Controller | CFO | Part of W9B |

### System Touchpoints

- Dividend declaration module: records Board Resolution details — amount per share, record date, payment date, dividend type; linked to shareholder register (W327.2–3)
- Shareholder register integration: maintains shareholder list with ownership, tax classification (resident individual, domestic corp, foreign corp), and bank account details for direct deposit (W327.5–8)
- Withholding tax calculator: auto-computes final withholding tax per shareholder based on tax classification per TRAIN law rates (W327.6)
- Dividend accrual and payment journal: automated GL posting for dividend declaration, withholding tax, and payment (W327.7–8)
- Uncashed dividend tracking: tracks dividend checks/bank deposits not yet claimed; alerts for dividends held in trust per RCC requirements (W327.9)
- Integration with W9B (year-end — dividend disclosure), W124 (corporate secretarial — board resolution), W233 (cash flow forecast — dividend outflow planning), W260 (BIR eFPS — withholding tax remittance), W317 (bank accounts — signatory authority for dividend checks), W319 (debt covenants — dividend restriction check), W322 (treasury policy — dividend DOA), W137 (IC dividends — separate process)

### Pain Points / Risks

- **Covenant-restricted dividends blocking declaration**: if any credit facility (W319) includes a covenant restricting dividend payment (common in Philippine bank lending — e.g., dividend payout ratio capped at 50% of net income, or dividends prohibited if Debt-to-Equity exceeds 1.5:1), the Board may be unable to declare dividends despite adequate retained earnings; Treasury must coordinate dividend feasibility with debt covenant compliance assessment
- **RCC solvency test failure**: under the Revised Corporation Code, a corporation may declare dividends only if, after payment, assets equal or exceed liabilities; if BuildRight's rapid expansion (10–15 new stores/year funded partly by debt) compresses the asset-to-liability ratio, the solvency test may limit dividend capacity even when cash flow is healthy
- **Withholding tax rate errors by shareholder classification**: Philippine tax law prescribes different withholding rates for different shareholder types; if the shareholder register contains outdated tax classification (e.g., a shareholder changed from individual to corporate status, or a foreign corporation relocated), the wrong withholding rate may be applied, creating BIR assessment risk
- **Timing conflict with IC dividend process**: BuildRight must receive IC dividends from subsidiaries (W137) before it can declare external dividends to shareholders; if the IC dividend process is delayed (Board scheduling, documentation delays), the external dividend declaration may be delayed, disappointing shareholder expectations
- **Uncashed dividend checks accumulating**: for shareholders who cannot receive direct bank deposit (no bank account on file, or the shareholder is an individual who moved), uncashed dividend checks must be held in trust; tracking and eventual escheatment under RCC adds administrative burden

### Staffing Implication

Each dividend declaration cycle (1–2 per year) requires approximately 1 week of coordinated effort: feasibility assessment 1–2 days (CFO + Controller + Tax Manager), Board resolution preparation 1–2 days (Corp Secretary + Legal), payment execution 1 day (Treasury), post-payment reconciliation 1 day (Treasury + Controller). Total: ~5–10 days/year, distributed across Treasury, Tax, Legal, and Controller — absorbed within existing headcount.

### Time Estimate

**Total**: Feasibility assessment — 1–2 days; Board resolution preparation — 1–2 days; Board approval — Board meeting agenda item; SEC filing — 1–2 days; Shareholder notification — 1 day; Withholding tax computation — 1 day; Dividend accrual — 2 hours; Payment execution — 1 day; Post-payment reconciliation — 1 day; Year-end disclosure — part of W9B; **Total cycle: ~5–8 business days per dividend declaration**

---

## W423. AR Post-dated Check (PDC) Warehousing & Clearing

| Field | Detail |
|---|---|
| **Trigger** | Receipt of post-dated check (PDC) from trade customer/wholesale account |
| **Frequency** | Daily |
| **Volume** | ~50–100 PDCs per week (B2B and trade customers) |
| **Owner** | Treasury Manager |
| **Participants** | AR Clerk, Treasury Analyst, Store Vault Custodian, Bank Relationship Manager |

### Background

In the Philippine market, B2B and trade customers (contractors, developers, wholesale resellers) commonly pay via a series of post-dated checks (PDCs). Managing these requires a distinct "warehousing" process where the physical checks are securely vaulted and the ERP record reflects the future payment commitment without immediately increasing the cash balance. This workflow ensures physical security of PDCs and timely deposit exactly on the check date to maintain liquidity.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **PDC Receipt & Entry**: AR Clerk receives PDC from customer; verifies check details (payee: BuildRight Depot Corp., amount in words matches figures, date is future-dated, signature present); enters PDC into ERP PDC module — records check number, bank, amount, maturity date, and linked AR invoice(s) | AR Clerk | AR Supervisor | 10 min |
| 2 | **Physical Warehousing**: AR Clerk transfers physical check to Store/HQ Vault Custodian; Custodian verifies check matches ERP entry and places in "PDC Warehouse" (secure safe/vault) sorted by maturity date | Vault Custodian | Treasury Mgr | 5 min |
| 3 | **ERP Status Update**: ERP reflects "Warehoused" status; the customer's AR balance is memo-credited (showing payment is pending), but the GL Cash account is not yet debited | System | — | Automated |
| 4 | **Daily Maturity Review**: Treasury Analyst runs "Daily PDC Maturity Report" (T+1 day) to identify checks maturing tomorrow | Treasury Analyst | Treasury Mgr | 15 min |
| 5 | **Pulling & Verification**: Vault Custodian pulls maturing checks from the vault; Treasury Analyst verifies physical checks against the maturity report | Vault Custodian / Treasury Analyst | Treasury Mgr | 30 min |
| 6 | **Check Deposit**: Treasury Analyst prepares deposit slip (or remote deposit capture/RDC scanning); deposits checks in the bank exactly on the maturity date | Treasury Analyst | Treasury Mgr | 1 hour |
| 7 | **Clearing Confirmation**: On T+1 after deposit, Treasury Analyst confirms check clearing via online banking; ERP status updated from "Warehoused" to "Cleared"; system posts GL entry: Dr. Cash / Cr. Accounts Receivable | Treasury Analyst | Treasury Mgr | 30 min |

### System Touchpoints

- PDC Warehousing Module: dedicated sub-ledger for future-dated checks with maturity date tracking and AR linkage (W423.1)
- Daily PDC Maturity Report: automated report of checks due for deposit (W423.4)
- Integration with W8 (AR — invoice matching), W30 (Cash Management — cash position update upon clearing), W108 (Collections — PDC as a promise to pay)

### Pain Points / Risks

- **Premature Deposit**: Depositing a PDC before its maturity date leads to bank penalties and customer disputes (Philippine banks strictly enforce date compliance)
- **Misplaced Physical Checks**: Lost PDCs in the "warehouse" safe require stop-payment orders and customer re-issuance, damaging trade relationships
- **Check Alteration**: Manual entry errors in the PDC module (wrong maturity date) result in missed deposits or premature presentment

---

## W424. AP Post-dated Check (PDC) Issuance & Monitoring

| Field | Detail |
|---|---|
| **Trigger** | Lease agreement requirements or vendor payment terms specifying PDC issuance |
| **Frequency** | Monthly (for lease PDCs) or ad-hoc (for vendors) |
| **Volume** | ~200–300 lease PDCs issued annually to mall developers |
| **Owner** | Treasury Manager |
| **Participants** | AP Clerk, Treasury Analyst, CFO, Lease Manager |

### Background

Philippine mall developers (SM, Ayala, Robinsons) typically require 12 to 24 months of post-dated checks (PDCs) for rent and CAM payments at the start of a lease or renewal. Managing these "issued but unreleased" liabilities is critical for accurate cash flow forecasting and bank reconciliation.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **PDC Batch Generation**: AP Clerk prepares a batch of PDCs for the lease term (e.g., 12 checks for 12 months); system prints checks with future maturity dates | AP Clerk | AP Supervisor | 30 min |
| 2 | **Signatory Approval**: Checks are routed for physical signature per DOA (W317); signed checks are returned to Treasury | Treasury Analyst | CFO / Treasury Mgr | 1 hour |
| 3 | **PDC Issuance Recording**: Treasury Analyst records the PDCs in the ERP "Issued PDC Register"; system creates a memo liability (Unreleased PDCs) but does not yet deduct from GL Cash | Treasury Analyst | Treasury Mgr | 15 min |
| 4 | **Vendor Handover**: PDCs are delivered to the mall developer/vendor; receiver signs an acknowledgment receipt (AR) | Treasury Analyst | — | 1 hour |
| 5 | **Monthly Monitoring**: Treasury Analyst monitors the "Daily AP PDC Maturity Report"; as checks reach their maturity date, they are expected to clear the bank | Treasury Analyst | Treasury Mgr | 15 min |
| 6 | **Clearing Reconciliation**: Treasury Analyst confirms check clearing via bank statement (W89); ERP updates status to "Cleared"; system posts GL entry: Dr. Accounts Payable / Cr. Cash | Treasury Analyst | Treasury Mgr | 20 min |

### System Touchpoints

- Issued PDC Register: tracks all future-dated checks released to vendors (W424.3)
- Cash Flow Forecast Integration: W233 automatically includes maturing AP PDCs as committed outflows (W424.5)
- Integration with W117 (Lease Administration) and W89 (Bank Reconciliation)

### Pain Points / Risks

- **Bank Account Funding**: Failure to fund the specific disbursement account before a high-value lease PDC matures results in a "bounced check" and legal complications (Batas Pambansa Blg. 22)
- **Canceled Leases**: If a store closes before the lease term ends, Treasury must physically retrieve and cancel the remaining PDCs held by the developer

---

## W425. Bounced Check (DAIF/DAUD) Recovery & Penalty

| Field | Detail |
|---|---|
| **Trigger** | Bank notification of a returned customer check (DAIF - Drawn Against Insufficient Funds or DAUD - Drawn Against Uncleared Deposits) |
| **Frequency** | Ad-hoc (approx. 2–5 cases per month) |
| **Volume** | Low frequency but high financial/legal impact |
| **Owner** | Treasury Manager |
| **Participants** | AR Clerk, Treasury Analyst, Collection Team, Legal Department |

### Background

When a customer check (PDC or current-dated) is returned by the bank, it is classified as "bounced." In the Philippines, this has serious legal implications under Batas Pambansa Blg. 22 (Anti-Bouncing Check Law). This workflow manages the immediate financial reversal, penalty charging, and legal escalation.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Bank Notification**: Treasury Analyst receives debit advice from bank for the returned check | Treasury Analyst | Treasury Mgr | 5 min |
| 2 | **Financial Reversal**: AR Clerk reverses the payment in ERP; the customer's AR balance is re-instated (Dr. Accounts Receivable / Cr. Cash); system auto-places account on "Credit Hold" (W8.1) | AR Clerk | AR Supervisor | 15 min |
| 3 | **Penalty Charging**: AR Clerk generates a debit memo for the "Returned Check Fee" (standard penalty + bank charges); system posts: Dr. Accounts Receivable / Cr. Other Income | AR Clerk | AR Supervisor | 10 min |
| 4 | **Customer Notification**: Collection Team contacts customer immediately via phone and sends "Notice of Dishonor" via registered mail (legal requirement for BP 22) | Collection Team | — | 30 min |
| 5 | **Redemption**: Customer settles the amount (including penalty) via cash, manager's check, or bank transfer; Treasury confirms receipt | Collection Team / Treasury Analyst | Treasury Mgr | 1 day |
| 6 | **Legal Escalation**: If not settled within 5 business days of notice, the case is referred to Legal (W125) for formal demand and potential BP 22 filing | Collection Team | Legal Mgr | 1 hour |

### System Touchpoints

- Bounced Check Incident Log: tracks check details, reason for return, and recovery status (W425.1)
- Auto-Credit Hold: system automatically blocks further sales to any account with an uncleared bounced check (W425.2)
- Integration with W108 (Collections) and W125 (Legal)

