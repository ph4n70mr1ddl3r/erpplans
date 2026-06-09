# Customer Credit & Collections Management Workflows

> Workflows governing the customer credit lifecycle for BuildRight Depot Corp.'s B2B and institutional accounts, covering credit application, scoring, limit management, collection operations, and bad debt management. With approximately 40% of revenue (PHP 25 billion) coming from Professional/Trade and Corporate/Institutional B2B customers across ~5,200 active AR accounts, these workflows are critical for managing credit exposure, maintaining cash flow, and minimizing bad debt losses while supporting the company's role as a key supplier to the Philippine construction industry.

Back to [Workflow Index](README.md)

---

## Workflows in This Domain

| Workflow | Name | Criticality |
|---|---|---|
| W886 | Customer Credit Application Processing & Scoring | Tier 1 |
| W887 | Customer Credit Limit Review, Adjustment & Approval | Tier 1 |
| W888 | Customer Credit Hold Management & Order Blocking | Tier 1 |
| W889 | Customer AR Aging Analysis & Collection Prioritization | Tier 1 |
| W890 | Customer Collection Call Execution & Promise Tracking | Tier 2 |
| W891 | Customer Bad Debt Write-Off Proposal & Approval | Tier 2 |
| W892 | Customer Statement Generation & Distribution | Tier 2 |
| W893 | Customer Credit Scorecard Annual Review & Portfolio Analysis | Tier 2 |

---

## W886. Customer Credit Application Processing & Scoring

| Field | Detail |
|---|---|
| **Trigger** | New B2B customer applies for credit terms; or existing cash customer requests credit line |
| **Frequency** | ~50–80 new credit applications per month |
| **Volume** | ~5,200 active AR accounts; approval rate: ~60–70% of applications |
| **Owner** | Credit Analyst / Finance Controller |
| **Participants** | Sales Representative, Credit Analyst, Credit Manager, Finance Controller, Customer Contact |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Receive credit application — Sales Representative or customer submits application: (a) company/legal entity details (SEC/DTI registration), (b) trade references (3 minimum), (c) bank references, (d) financial statements (audited if available), (e) authorized signatories, (f) requested credit limit and terms, (g) BIR TIN, (h) business permit | Sales Representative | Credit Analyst | 30 min (intake) |
| 2 | Verify applicant documentation — validate: (a) SEC/DTI registration via online verification, (b) BIR TIN via eFPS, (c) Mayor's permit validity, (d) trade reference legitimacy (call each reference), (e) bank reference verification, (f) financial statement reasonableness; flag discrepancies | Credit Analyst | Credit Manager | 2–4 hours |
| 3 | Conduct credit scoring — apply internal credit scoring model: (a) years in business (> 5 years: positive), (b) industry risk (construction: moderate), (c) financial ratios (current ratio, debt-to-equity, net margin), (d) trade reference feedback, (e) banking relationship, (f) geographic risk (Mindanao vs. Luzon), (g) BuildRight relationship history (if existing cash customer); calculate composite score (0–100) | Credit Analyst | Credit Manager | 1–2 hours |
| 4 | Determine credit recommendation — based on score: (a) Score ≥ 75: approve at requested limit or 80% of requested, (b) Score 50–74: approve at reduced limit (50% of requested) with shorter terms (15 days vs. 30), (c) Score 30–49: approve with COD or secured terms (post-dated checks), (d) Score < 30: decline with counter-offer for cash terms only | Credit Analyst | Credit Manager | 30 min |
| 5 | Credit approval authorization — (a) credit limit ≤ PHP 500,000: Credit Manager approves, (b) PHP 500,001–2,000,000: Finance Controller approves, (c) > PHP 2,000,000: Finance VP approves, (d) > PHP 5,000,000: CEO/CFO approves | Credit Manager | Finance VP | 15–30 min |
| 6 | Notify customer and Sales Representative — communicate credit decision: approved (with limit, terms, and conditions), conditionally approved (with counter-offer), or declined (with reason and reapplication eligibility); send credit agreement for signature | Credit Analyst | Sales Representative | 30 min |
| 7 | Set up customer in AR module — create customer account with: approved credit limit, payment terms (net 15/30/45/60), credit score, review date (6 months for new accounts), authorized signatories, and billing address; activate for credit sales | Credit Analyst | Credit Manager | 30 min |

### System Touchpoints
- **ERP AR Module** — customer setup, credit limit configuration, terms management
- **Credit Scoring Model** — internal scoring algorithm, historical data reference
- **SEC/DTI Online Portal** — business registration verification
- **BIR eFPS** — TIN validation
- **BI Dashboard** — credit portfolio analytics, scoring distribution
- **Document Management** — application archive, credit agreement storage

### Pain Points / Risks
- Many Philippine SME contractors lack audited financial statements — limited data for scoring
- Trade references are often friends/family — reliability is questionable
- Construction industry credit risk is high — project-based customers may have lumpy cash flows
- Application processing time (3–5 business days) may lose sales to competitors offering instant credit
- Credit scoring model requires periodic recalibration — economic conditions change default rates
- Post-dated check requirement is common in Philippines but adds operational complexity

### Staffing Implication
- 2 Credit Analysts (application processing and scoring)
- 1 Credit Manager (approval authority and model oversight)
- Sales Representatives: application intake and customer relationship

### Time Estimate
- Per application: 5–8 person-hours over 3–5 business days
- **Annual estimate: 780 applications × 6.5 hours = 5,070 person-hours/year**

---

## W887. Customer Credit Limit Review, Adjustment & Approval

| Field | Detail |
|---|---|
| **Trigger** | Scheduled review (semi-annual for new accounts, annual for established); or triggered by credit limit utilization > 85%, payment pattern deterioration, or customer request for increase |
| **Frequency** | ~100–150 credit limit reviews per month (annual cycle for 5,200 accounts = ~430/month; plus ad-hoc reviews) |
| **Volume** | ~15–20% of reviews result in limit adjustment (increase or decrease) |
| **Owner** | Credit Manager / Finance Controller |
| **Participants** | Credit Analyst, Sales Representative, Customer Contact, Finance Controller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Identify accounts due for review — system generates review list based on: (a) scheduled review date, (b) limit utilization > 85% for 3 consecutive months, (c) payment delinquency (any invoice > 30 days past due), (d) customer request for increase, (e) significant order exceeding current limit | Credit Analyst | Credit Manager | 30 min (automated list generation) |
| 2 | Compile review data package — for each account: (a) 12-month payment history, (b) average days-to-pay, (c) credit utilization trend, (d) order frequency and value trend, (e) any disputes or credit memos, (f) updated financial information (if available), (g) industry/economic conditions | Credit Analyst | Credit Manager | 30 min per account |
| 3 | Assess creditworthiness update — recalculate credit score with current data: (a) payment behavior change (improving or deteriorating), (b) order volume trend, (c) outstanding AR aging, (d) any collection activity, (e) external factors (construction industry outlook, regional economic conditions) | Credit Analyst | Credit Manager | 15–30 min per account |
| 4 | Determine credit limit recommendation — options: (a) Maintain current limit, (b) Increase (if utilization consistently high and payment is timely — typically 20–50% increase), (c) Decrease (if payment deterioration — typically to 50–75% of current), (d) Suspend credit (convert to cash terms), (e) Close account (if inactive > 12 months or severe default) | Credit Manager | Finance Controller | 15 min per account |
| 5 | Obtain approval — same authorization matrix as W886: Credit Manager ≤ PHP 500K, Finance Controller ≤ PHP 2M, Finance VP ≤ PHP 5M, CEO > PHP 5M; for limit decreases, Credit Manager can approve all; for suspensions, Finance Controller approval required | Credit Manager | Finance Controller | 15 min |
| 6 | Communicate decision — notify Sales Representative and customer of any limit change; for decreases: explain reason and remediation path; for increases: confirm new terms; for suspensions: coordinate transition to cash terms | Credit Analyst | Sales Representative | 15 min per account |
| 7 | Update AR module — adjust credit limit, update review date, record review notes; if suspended: apply credit hold (W888) | Credit Analyst | Credit Manager | 10 min per account |

### System Touchpoints
- **ERP AR Module** — credit limit management, review scheduling, payment history
- **Credit Scoring Model** — score recalculation, trend analysis
- **BI Dashboard** — portfolio utilization, aging analysis, review pipeline
- **Sales CRM** — customer relationship notes, sales forecast (for limit increase justification)
- **Document Management** — review documentation, decision trail

### Pain Points / Risks
- Credit limit decrease may damage customer relationship — Sales Representative pushback is common
- Manual review of 430 accounts/month is labor-intensive — risk of superficial review under time pressure
- Payment pattern changes may lag economic downturn — reactive rather than proactive adjustments
- Customer requests for increases are often driven by single large project rather than sustained volume — temporary vs. permanent need
- Construction customers may have seasonal payment patterns (dry season = higher activity) — cyclicality must be factored

### Staffing Implication
- 2 Credit Analysts: 60% of time on credit limit reviews
- Credit Manager: approval and escalation (20% of time)
- Sales Representatives: customer communication support

### Time Estimate
- Per review: 60–90 min
- **Annual estimate: 1,600 reviews × 75 min = 2,000 person-hours/year**

---

## W888. Customer Credit Hold Management & Order Blocking

| Field | Detail |
|---|---|
| **Trigger** | Customer credit limit exceeded; or invoice past due > defined threshold (e.g., > 30 days for Net 30 accounts) |
| **Frequency** | ~30–50 credit holds placed per day; ~25–40 releases per day |
| **Volume** | At any given time, ~200–300 accounts (4–6% of 5,200) are on credit hold |
| **Owner** | Credit Analyst / Credit Manager |
| **Participants** | Sales Representative, Order Processing, Warehouse/Logistics, Customer Contact |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | System detects credit hold trigger — automated checks: (a) new order would exceed credit limit, (b) invoice > 30 days past due (for Net 30), (c) invoice > 45 days (for Net 45), (d) invoice > 60 days (for Net 60), (e) NSF/bounced check from customer; order automatically blocked in order processing | ERP System (automated) | Credit Manager | Instant (automated) |
| 2 | Review and validate hold — Credit Analyst reviews: (a) verify overdue amount and invoice details, (b) check for payments in transit (customer may have paid but not yet posted), (c) review for disputed invoices (hold should not apply to disputed amounts), (d) check for partial payments that may release hold | Credit Analyst | Credit Manager | 10–15 min per hold |
| 3 | Notify Sales Representative and customer — automated email to Sales Rep with hold reason, overdue amount, and suggested action; customer receives notification (if contact configured); Sales Rep contacts customer to arrange payment | Credit Analyst | Sales Representative | 5 min (automated + manual follow-up) |
| 4 | Process credit hold release requests — upon payment receipt or override request: (a) payment received and posted → auto-release, (b) Sales Rep requests override for critical order → Credit Manager reviews and decides, (c) partial payment received → release proportional to payment, (d) dispute resolution → release disputed amount | Credit Analyst | Credit Manager | 10 min per release |
| 5 | Escalation for chronic offenders — accounts with > 3 holds in rolling 90 days flagged for Credit Manager review: consider limit reduction (W887) or terms modification; notify Finance Controller | Credit Manager | Finance Controller | 30 min per escalation |
| 6 | Daily credit hold report — generate report: total accounts on hold, total blocked order value, aging of holds, release rate, and chronic offender list; distribute to Credit Manager and VP Operations | Credit Analyst | Credit Manager | 30 min |

### System Touchpoints
- **ERP AR Module** — credit limit checking, order blocking, hold management
- **Order Processing** — sales order workflow integration, block/release triggers
- **Finance Module** — payment posting, invoice aging
- **Communication Platform** — automated notifications to Sales and customer
- **BI Dashboard** — credit hold metrics, blocked order value, release velocity

### Pain Points / Risks
- Credit hold blocks legitimate customer orders — Sales Representatives push for overrides (pressure on Credit Analyst)
- Payment posting delay — customer pays but hold not released until payment clears (1–2 banking days)
- Disputed invoices complicate hold calculation — system may block for disputed amount incorrectly
- Override frequency indicates inadequate credit limits — root cause analysis needed
- Credit hold during construction season (dry months) impacts revenue — business vs. risk tension
- Manual validation of every hold is time-consuming — 30–50 per day = 5–6 hours

### Staffing Implication
- 2 Credit Analysts: credit hold management is 40% of daily workload
- Credit Manager: override approvals and escalation (1 hour/day)
- Sales Representatives: customer communication and payment facilitation

### Time Estimate
- Per hold management: 15–20 min
- **Daily estimate: 40 holds × 18 min = 12 hours/day × 2 analysts = 6 hours/analyst**
- **Annual estimate: ~3,000 person-hours/year**

---

## W889. Customer AR Aging Analysis & Collection Prioritization

| Field | Detail |
|---|---|
| **Trigger** | Scheduled — daily aging refresh; weekly collection prioritization meeting |
| **Frequency** | Daily aging report; weekly collection prioritization and assignment |
| **Volume** | ~5,200 active AR accounts; total outstanding: PHP 2–4 billion at any time |
| **Owner** | Credit Manager / Collection Supervisor |
| **Participants** | Credit Analyst, Collection Agent, Sales Representative, Finance Controller |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Generate daily AR aging report — system produces: (a) aging buckets (Current, 1–30, 31–60, 61–90, 91–180, > 180 days), (b) total outstanding by bucket, (c) top 50 accounts by overdue amount, (d) accounts crossing bucket thresholds since yesterday, (e) DSO (Days Sales Outstanding) calculation | ERP System (automated) | Credit Manager | 15 min (review) |
| 2 | Analyze aging trends — compare to: (a) prior week aging, (b) same period last year, (c) target DSO (target: 35 days for Net 30 terms), (d) industry benchmark; identify deteriorating segments (by region, by industry, by sales rep) | Credit Analyst | Credit Manager | 30 min |
| 3 | Prioritize collection actions — classify accounts: (a) Critical: > 90 days overdue (immediate collection call + legal consideration), (b) High: 61–90 days overdue (collection call this week), (c) Medium: 31–60 days (collection email + phone), (d) Standard: approaching due date (friendly reminder); assign to Collection Agents based on geography and relationship | Collection Supervisor | Credit Manager | 1 hour weekly |
| 4 | Calculate collection targets — set weekly collection targets by agent based on: (a) total overdue amount assigned, (b) historical collection rate by aging bucket, (c) account complexity, (d) seasonal factors; track against actual collections | Collection Supervisor | Credit Manager | 30 min weekly |
| 5 | Escalate uncollectible accounts — for accounts > 180 days: (a) review collection history, (b) assess customer viability, (c) determine if legal action warranted, (d) propose for bad debt write-off (W891) or external collection agency referral | Credit Manager | Finance Controller | 2 hours weekly |
| 6 | Report to management — weekly collection report: (a) total collections vs. target, (b) aging shift, (c) DSO trend, (d) top 10 overdue accounts with status, (e) write-off recommendations, (f) collection agent performance | Credit Manager | Finance Controller | 1 hour |

### System Touchpoints
- **ERP AR Module** — aging report, DSO calculation, collection tracking
- **Collection Management System** — account assignment, call logging, promise tracking
- **BI Dashboard** — aging visualization, DSO trends, collection heat map
- **CRM** — customer communication history, relationship notes
- **Finance Module** — collection posting, DSO impact calculation

### Pain Points / Risks
- Philippine construction industry payment culture is slow — 60–90 day actual payment on 30-day terms is common
- DSO target of 35 days is aggressive for the industry — may need to accept 45 days as realistic
- Collection agents face verbal abuse and avoidance — high stress, high turnover role
- Large contractor accounts (top 50 by revenue) receive preferential treatment — collection discipline erodes
- Regional collection effectiveness varies — Mindanao accounts are harder to collect than Metro Manila
- Economic downturns (construction slowdown) cause wave of delinquencies — portfolio risk management essential

### Staffing Implication
- 4 Collection Agents (each manages ~1,300 accounts)
- 1 Collection Supervisor (team management and prioritization)
- Credit Manager: escalation and reporting

### Time Estimate
- Daily aging review: 30 min
- Weekly prioritization: 1.5 hours
- Weekly reporting: 1 hour
- Collection calls: primary activity for Collection Agents (see W890)
- **Annual estimate (analysis + reporting): ~300 person-hours/year for Credit Analyst/Supervisor**

---

## W890. Customer Collection Call Execution & Promise Tracking

| Field | Detail |
|---|---|
| **Trigger** | Collection assignment from weekly prioritization (W889); or daily follow-up on broken promises |
| **Frequency** | ~80–120 collection calls per day across 4 Collection Agents |
| **Volume** | ~20,000–30,000 collection calls per year; promise-to-pay rate: ~40–50% |
| **Owner** | Collection Agent / Collection Supervisor |
| **Participants** | Collection Agent, Customer Contact (AP Clerk, Owner, Finance Manager), Sales Representative |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Prepare for collection call — review account: (a) outstanding invoices and amounts, (b) previous collection call notes, (c) broken promises, (d) customer payment patterns, (e) recent order activity (are they still buying?), (f) Sales Rep context (relationship, upcoming projects) | Collection Agent | Collection Supervisor | 5 min per call |
| 2 | Execute collection call — (a) identify self and purpose, (b) state overdue amount and invoice details, (c) inquire on payment status and reason for delay, (d) negotiate payment date, (e) if customer cannot pay full: propose installment plan, (f) document outcome: promise to pay, partial promise, dispute, or refusal | Collection Agent | Collection Supervisor | 5–15 min per call |
| 3 | Record call outcome — update collection system: (a) call date and time, (b) contact person, (c) payment promise (amount and date) or reason for non-payment, (d) customer concern or dispute, (e) follow-up action and date; auto-schedule follow-up based on promise date | Collection Agent | Collection Supervisor | 3 min per call |
| 4 | Monitor promise fulfillment — on promised payment date: check if payment received; if yes: close collection action; if no: (a) same-day follow-up call, (b) escalate to Sales Rep for relationship leverage, (c) if second broken promise: escalate to Credit Manager for credit hold (W888) | Collection Agent | Collection Supervisor | 2 min per promise |
| 5 | Coordinate with Sales Representative — for high-value or relationship-sensitive accounts: Sales Rep makes parallel contact (softer approach); Collection Agent provides factual overdue information; Sales Rep facilitates payment commitment | Collection Agent | Sales Representative | 10 min per coordination |
| 6 | Weekly collection performance review — Collection Supervisor reviews each agent's: (a) calls made vs. target, (b) promises obtained vs. calls, (c) promises fulfilled vs. promised, (d) total collected vs. target; provide coaching and adjust approach as needed | Collection Supervisor | Credit Manager | 1 hour weekly |

### System Touchpoints
- **Collection Management System** — call logging, promise tracking, follow-up scheduling
- **ERP AR Module** — invoice details, payment confirmation, credit status
- **CRM** — customer contact information, relationship notes
- **Phone System** — call recording (for quality and dispute resolution), auto-dialer
- **BI Dashboard** — agent performance, promise fulfillment rate, collection velocity

### Pain Points / Risks
- Customer avoidance (not answering calls, changing AP contacts) wastes agent time — 30–40% of calls are unanswered
- Collection calls can damage customer relationship — especially for accounts still actively ordering
- Promise-to-pay fulfillment rate is only 50–60% — requires persistent follow-up
- Cultural sensitivity — Filipino business culture values relationships; aggressive collection can be counterproductive
- Sales Representatives may undermine collection efforts by promising extended terms without Credit approval
- Collection agent burnout — high rejection rate and confrontational interactions lead to turnover

### Staffing Implication
- 4 Collection Agents (full-time calling, 80–120 calls/day each)
- 1 Collection Supervisor (quality monitoring, coaching)
- Sales Representatives: relationship-based collection support

### Time Estimate
- Per call (including preparation and documentation): 13–23 min
- **Daily estimate: 100 calls × 18 min = 30 hours/day across 4 agents**
- **Annual estimate: ~7,500 person-hours/year for Collection Agents**

---

## W891. Customer Bad Debt Write-Off Proposal & Approval

| Field | Detail |
|---|---|
| **Trigger** | Account > 180 days overdue with exhausted collection efforts; or customer bankruptcy/closure confirmed |
| **Frequency** | ~15–25 bad debt write-offs per year |
| **Volume** | Average write-off: PHP 100,000–1,000,000; annual bad debt target: < 0.5% of B2B revenue |
| **Owner** | Credit Manager / Finance Controller |
| **Participants** | Collection Agent, Credit Manager, Finance Controller, Finance VP, Legal Counsel, External Auditor |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Identify write-off candidate — Collection Agent or Credit Manager identifies account meeting write-off criteria: (a) > 180 days overdue, (b) 3+ collection calls with no response or broken promises, (c) no active orders in 90+ days, (d) customer confirmed closed/bankrupt, or (e) legal collection deemed cost-prohibitive | Collection Agent | Credit Manager | 15 min |
| 2 | Compile write-off proposal — document: (a) account history (credit since date, total sales, payment pattern), (b) collection history (calls made, promises broken, last contact), (c) overdue invoice detail, (d) reason for write-off (bankruptcy, unresponsive, dispute, other), (e) legal opinion (if applicable), (f) recovery potential assessment (any assets or guarantors), (g) proposed write-off amount | Credit Manager | Finance Controller | 1–2 hours |
| 3 | Evaluate legal collection option — for amounts > PHP 500,000: Legal Counsel assesses viability of legal action — cost of litigation vs. recovery probability; recommend legal action or write-off | Legal Counsel | Finance VP | 1 hour |
| 4 | Obtain write-off approval — authorization: (a) ≤ PHP 100,000: Finance Controller, (b) PHP 100,001–500,000: Finance VP, (c) PHP 500,001–2,000,000: CEO/CFO, (d) > PHP 2,000,000: Board of Directors; each approver reviews proposal and supporting documentation | Finance Controller | Finance VP / CEO | 30 min per approval level |
| 5 | Execute write-off — (a) post bad debt expense in GL, (b) reverse AR balance, (c) update customer status to "Written Off", (d) apply credit block to prevent future orders, (e) update allowance for doubtful accounts, (f) file BIR documentation for bad debt deduction (requires BIR-permitted evidence of collection efforts) | Finance Controller | Finance VP | 1 hour |
| 6 | External collection agency referral (optional) — for write-offs > PHP 200,000 with identifiable customer: refer to external collection agency on contingency basis (typically 15–25% of recovered amount); track recovery | Credit Manager | Finance Controller | 1 hour |
| 7 | Annual bad debt review — compile annual write-off summary: (a) total write-offs vs. target (< 0.5% of B2B revenue), (b) root cause analysis, (c) industry and geographic concentration, (d) credit scoring model accuracy, (e) recommendations for portfolio improvement | Credit Manager | Finance VP | 4 hours |

### System Touchpoints
- **ERP AR Module** — write-off processing, customer status update, GL posting
- **Collection Management System** — collection history documentation
- **Finance Module** — bad debt expense, allowance for doubtful accounts, BIR documentation
- **Legal Matter Management** — litigation assessment, external collection agency tracking
- **BI Dashboard** — bad debt trends, portfolio risk analysis, scoring model accuracy

### Pain Points / Risks
- BIR bad debt deduction requires extensive documentation — 10+ pieces of evidence per write-off
- Write-off may be premature — customer could recover and pay (construction project delays are common)
- External collection agency recovery rate is low (~10–20%)
- Bad debt write-off impacts P&L — management may resist timely write-offs to protect earnings
- Concentrated risk — single large contractor default can exceed annual bad debt budget
- Written-off customers may return with new applications — need clear policy on re-admission

### Staffing Implication
- Credit Manager: write-off proposal preparation (core responsibility)
- Legal Counsel: 1 hour per write-off > PHP 500,000
- Finance Controller: GL processing and BIR documentation
- External collection agency: contingency-based engagement

### Time Estimate
- Per write-off: 4–8 person-hours over 2–4 weeks
- **Annual estimate: 20 write-offs × 6 hours = 120 person-hours/year**

---

## W892. Customer Statement Generation & Distribution

| Field | Detail |
|---|---|
| **Trigger** | Scheduled — monthly (end of month); or on-demand by customer request |
| **Frequency** | Monthly generation for all ~5,200 active AR accounts; ~200 on-demand requests per month |
| **Volume** | ~5,400 statements per month; delivered via email (primary), portal (self-service), and physical mail (for customers without email) |
| **Owner** | AR Accountant / Credit Analyst |
| **Participants** | AR Accountant, Customer Contact, Collection Agent |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Generate monthly statements — system produces statements for all active AR accounts showing: (a) opening balance, (b) invoices issued during month, (c) payments received during month, (d) credit memos applied, (e) closing balance, (f) aging breakdown; include remittance instructions | ERP System (automated) | AR Accountant | 30 min (automated + validation) |
| 2 | Validate statement accuracy — spot-check 50 statements: (a) opening balance matches prior month closing, (b) all invoices and payments included, (c) aging buckets calculated correctly, (d) customer address and contact information current | AR Accountant | Credit Manager | 1 hour |
| 3 | Distribute statements — (a) email PDF statements to customer email on file (primary channel for ~4,500 accounts), (b) publish to customer portal for self-service download, (c) print and mail physical statements for ~700 accounts without email (mostly provincial customers); track delivery confirmation | AR Accountant | Credit Manager | 2 hours |
| 4 | Process on-demand statement requests — customers or Sales Representatives may request statements outside monthly cycle; generate and send within 4 business hours | AR Accountant | Credit Manager | 10 min per request |
| 5 | Monitor statement delivery and bounce-backs — track email delivery success rate (target: 95%); investigate and correct bounced email addresses; update customer contact records | AR Accountant | Credit Manager | 30 min monthly |
| 6 | Follow up on unopened statements — for accounts with overdue balances where statement was not opened (email tracking): Collection Agent proactively contacts customer to confirm receipt and discuss payment | Collection Agent | Credit Manager | Variable |

### System Touchpoints
- **ERP AR Module** — statement generation, aging calculation
- **Email System** — bulk statement distribution, delivery tracking
- **Customer Portal** — self-service statement access, download
- **Document Management** — statement archive, delivery log
- **CRM** — customer contact information, email address management

### Pain Points / Risks
- Customer email addresses change frequently — ~10% of email addresses are stale at any time
- Physical mail delivery in Philippines is unreliable — provincial addresses may not receive statements
- Statement format must comply with BIR requirements for AR documentation
- Customers may dispute statement amounts — reconciliation requests create AR workload
- Email statement attachments may be blocked by customer spam filters — PDF-only format recommended
- Multi-entity customers (Holdings, Depot, Logistics) may receive multiple statements — consolidation requests

### Staffing Implication
- 1 AR Accountant (statement generation and distribution: 40% of monthly workload)
- Collection Agents: follow-up on unopened statements (part of daily calls)

### Time Estimate
- Monthly cycle: 4 hours
- On-demand requests: 200 × 10 min = 33 hours/month
- **Annual estimate: 48 + 400 = 448 person-hours/year**

---

## W893. Customer Credit Scorecard Annual Review & Portfolio Analysis

| Field | Detail |
|---|---|
| **Trigger** | Scheduled — annual comprehensive portfolio review; or triggered by significant economic event affecting default risk |
| **Frequency** | 1 comprehensive annual review; quarterly portfolio health check |
| **Volume** | Full portfolio of ~5,200 AR accounts analyzed; top 200 accounts by exposure reviewed in detail |
| **Owner** | Credit Manager / Finance VP |
| **Participants** | Credit Analyst, Finance Controller, Finance VP, Risk Management, External Credit Agency (for scoring model validation) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | Compile portfolio performance data — extract from trailing 12 months: (a) total credit sales, (b) total collections, (c) bad debt write-offs, (d) DSO trend, (e) aging distribution, (f) credit limit utilization, (g) credit score distribution, (h) new account volume and default rate | Credit Analyst | Credit Manager | 4 hours |
| 2 | Analyze portfolio risk concentration — assess: (a) top 20 accounts as % of total AR (concentration risk), (b) geographic concentration, (c) industry concentration (construction, manufacturing, government), (d) terms distribution, (e) aging migration (accounts moving to higher risk buckets) | Credit Analyst | Credit Manager | 4 hours |
| 3 | Validate credit scoring model — compare predicted default rates (by score band) to actual default/write-off rates: (a) score ≥ 75: actual default rate vs. expected (< 1%), (b) score 50–74: actual vs. expected (1–3%), (c) score < 50: actual vs. expected (> 3%); recalibrate model if deviation > 20% | Credit Manager | External Credit Agency | 8 hours |
| 4 | Conduct top 200 account deep-dive — for top accounts by exposure: (a) review credit score and payment trend, (b) assess industry and project risk, (c) evaluate limit adequacy, (d) identify early warning indicators (slowing payments, reduced order frequency), (e) recommend action (maintain, increase, decrease, suspend) | Credit Analyst | Credit Manager | 40 hours |
| 5 | Calculate portfolio expected loss — apply probability of default (PD) and loss given default (LGD) by score band to current portfolio: (a) expected loss = Σ (exposure × PD × LGD), (b) compare to allowance for doubtful accounts balance, (c) recommend reserve adjustment if under/over-provisioned | Credit Manager | Finance Controller | 4 hours |
| 6 | Present portfolio review to Finance VP and CFO — key findings: (a) portfolio health score, (b) risk concentration concerns, (c) scoring model performance, (d) expected loss vs. reserves, (e) top account recommendations, (f) policy and process improvement proposals | Credit Manager | Finance VP | 2 hours |
| 7 | Implement approved changes — update: (a) credit scoring model weights, (b) approval thresholds, (c) collection strategy for high-risk segments, (d) credit policy amendments, (e) allowance for doubtful accounts reserve | Credit Manager | Finance VP | 4–8 hours |

### System Touchpoints
- **ERP AR Module** — portfolio data extraction, aging analysis
- **Credit Scoring Model** — performance validation, recalibration
- **BI Dashboard** — portfolio visualization, risk heat map, concentration analysis
- **Finance Module** — expected loss calculation, reserve adjustment
- **External Credit Agency** — model validation, benchmark data
- **Risk Management System** — portfolio risk metrics, early warning indicators

### Pain Points / Risks
- Credit scoring model may not capture construction industry cyclicality — sector-specific factors needed
- Portfolio concentration in top 20 accounts may be unavoidable (large contractors dominate B2B revenue)
- Expected loss calculation requires assumptions about LGD that are difficult to validate
- Scoring model recalibration may result in significant portfolio shifts — widespread limit changes disruptive
- External credit agency data for Philippine SMEs is limited — model relies heavily on internal payment history
- Annual review timing must align with financial year-end audit — external auditor reviews credit portfolio

### Staffing Implication
- Credit Manager: 50% of time for 2 weeks during annual review
- Credit Analysts: full support during review period (2 weeks)
- Finance VP: 4 hours for review and approval
- External credit agency: 1-week engagement for model validation

### Time Estimate
- Annual review: 60–80 person-hours over 3–4 weeks
- Quarterly health checks: 8 hours each
- **Annual estimate: 70 + 32 = 102 person-hours/year**
