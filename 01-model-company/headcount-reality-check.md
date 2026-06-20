# Headcount Reality Check — HQ vs. Workflow Coverage

> **STATUS — ACTIONED 2026-06-20.** This analysis identified that HQ (315) was understaffed and omitted 6 functions. Per direction to apply the **minimum** increase that resolves the gaps, HQ was rebalanced **315 → 357** and total **6,715 → 6,757** (see `model-company-profile.md` §3.3/§4 and the CHANGELOG entry for 2026-06-20). The comfortable/fully-cushioned range estimated below (~440–470) was **not** adopted; the implemented 357 is the floor that (a) fixes the Executive inconsistency, (b) breaks out the 6 hidden departments explicitly, and (c) relieves only the contradictions the workflows themselves expose (e.g., AP "10 clerks", IT archipelago field support). The analysis below is retained as the gap record.

**Scope:** Cross-reference the stated HQ department headcounts (`model-company-profile.md` §3.3 / §4) against the actual job roles, volumes, and responsibilities referenced across all **704 workflow markdown files (523 process-area specs across 173 value streams)**.

**Method:** Extracted every `Owner` / `Participants` role title from all workflow PA files (~16,400 internal role mentions after normalization), clustered into role families, mapped to departments, and sized against stated transaction volumes (AP/AR/PO volumes, user counts, store/DC counts, statutory filing frequency).

---

## 1. Bottom Line

The 6,757 total company headcount is **plausible overall**, but the **HQ allocation of 315 was understated**, the department breakdown **omitted 6 entire functions** that appear heavily in the workflows, and at least **4 departments were materially understaffed** for their stated workload (Finance, IT, HR, Legal). Store (5,800) and DC (600) headcounts are defensible.

**Recommended HQ target:** comfortable range ~440–470; **implemented minimum 357** (see status banner above).

---

## 2. Summary Table — Stated vs. Recommended

| HQ Department | Stated | Realistic Range | Verdict | Key Driver |
|---|---|---|---|---|
| Executive Office | 5 | 7 | ❌ Inconsistent | Org chart (§11.1) lists CEO + 6 C-suite; §3.3 omits CHRO & VP Legal |
| Finance & Accounting | 37 | **58–68** | 🔴 Severely understaffed | ~9,000 AP invoices/mo; 5 entities; PFRS 15; monthly VAT ×5 |
| Merchandising & Buying | 40 | 40–45 | 🟡 Right size, wrong mix | Too few planners/pricing analysts for 35K SKUs |
| Supply Chain & Logistics | 31 | **42–50** | 🔴 Understaffed | 800–1K vendors; 40% imports; S&OP; fleet; 4 DCs |
| Information Technology | 33 | **65–80** | 🔴 Severely understaffed | 6,757 users; 600 POS; 200 stores; ERP; cyber; privacy |
| Human Resources | 18 | **38–48** | 🔴 Severely understaffed | 6,757 staff; ~1,400 hires/yr; 5 entities; payroll ×2/mo |
| Marketing | 23 | 28–34 | 🟡 Slightly low | Ecom + loyalty + retail media + insights |
| Store Operations | 24 | 24 | ✅ OK | Regional model fits 200 stores |
| Legal & Compliance | 9 | **18–24** | 🔴 Severely understaffed | 1,872 workflow mentions; AML/ABC; privacy; SEC; multi-LGU |
| Internal Audit | 5 | 8–10 | 🟡 Low | ERM bundled in; 5 entities; PHP 62B |
| Loss Prevention | 20 | 25–30 | 🟡 Low-ish | VS-23 exception monitoring + investigations + shrink |
| Customer Service / Call Center | 30 | 30–45 | ❓ Depends | OK only if decentralized to stores |
| **Health, Safety & Environment** | **0 (hidden)** | **12–15** | 🔴 **MISSING dept** | DOLE RA 11058; "1 Safety Officer per region (~10–12)" |
| **Quality** | **0 (hidden)** | **5–6** | 🔴 **MISSING dept** | VS-31 incoming inspection, vendor QA, recalls |
| **Facilities & Real Estate** | **0 (hidden)** | **10–15** | 🔴 **MISSING dept** | VS-20/97/138; 200 stores + HQ + DCs |
| **Sustainability / ESG** | **0 (hidden)** | **3–4** | 🔴 **MISSING dept** | VS-25; DENR; ESG reporting |
| **Strategy / Corp Planning** | **0 (hidden)** | **4–5** | 🔴 **MISSING dept** | VS-33; annual plan; CPM |
| **Trade / Account Mgmt** | **0 (hidden)** | **6–8** | 🔴 **MISSING dept** | VS-43 Trade Pro program; 5,200 AR accounts |
| **TOTAL HQ** | **315** | **~440–470** | | +6 functions not enumerated |

> The 6 "hidden" departments sum to ~40–53 people — which almost exactly explains the gap between the **enumerated departments (~275)** and the **stated HQ total (315)**. The profile clearly *included* these functions in the 315, but never broke them out. This is a **documentation defect**, not necessarily a planning omission.

---

## 3. The Severely Understaffed Departments (detail)

### 3.1 Finance & Accounting — stated 37, need 58–68
**Workload evidence from workflows:**
- **~8,500–9,500 AP invoices/month** (~450/day) — VS-17 / PA-17
- **~3,500 AR invoices/month** + 5,200 active AR accounts + collections — W8
- 5 legal entities, each filing **monthly VAT (BIR 2550M)** — VS-79
- Withholding tax / 2307 management across 5 entities
- PFRS 15 multi-element revenue recognition — VS-157
- Multi-entity consolidation + intercompany (~60–80 IC invoices/mo) — PA-17.2
- Fixed assets + Capex (CIP/AUC) — VS-35, VS-40
- Semi-monthly payroll accounting interface for 6,757 staff

**Roles the workflows demand but the 37 doesn't cover:**
AP Manager, AR Supervisor, Credit Manager, Intercompany Accountant, Revenue Accountant, Cost Accountant, Inventory Accountant, Logistics Finance Analyst, GL Accountant (×4–5 for 5 entities), Tax specialists (5 entities × VAT/WHT/income tax needs a team of 4+, not 1 accountant + 1 manager), FP&A team (only 1 generic "Finance Analyst" listed).

### 3.2 Information Technology — stated 33, need 65–80
**Workload evidence:**
- **6,757 end users** to support across 200 stores + 4 DCs + HQ
- 600 POS terminals (real-time inventory sync <30s latency)
- ERP, WMS, TMS, OMS, CRM, PIM, CDP, BI, ecommerce — ~10+ platforms
- Cybersecurity & privacy (VS-27.3, VS-91) — NPC/DPA compliance
- Data engineering + BI + advanced analytics/AI (VS-28, VS-30)
- PMO for the ERP program itself

Industry benchmark for retail IT is **1.5–2.5% of headcount = 100–168**; even a heavily outsourced/lean model floors at ~60–70. **33 is roughly half the minimum.** The workflow mentions 14 distinct IT role families (helpdesk, infra, apps, data eng, BI, data scientist, security, privacy, PMO, architect, DBA, dev, DevOps, sysadmin).

### 3.3 Human Resources — stated 18, need 38–48
**Workload evidence:**
- 6,757 employees, **~1,200–1,600 hires/year** (~15–20% turnover)
- 5 payroll entities, semi-monthly = ~13,430 payslips/month
- Labor relations / CBA / grievance (VS-84) — needs dedicated LR staff
- L&D for store onboarding + ongoing (VS-19.4)
- Drug-free workplace program (VS-150), background screening (VS-167), uniform/PPE (VS-169)

Benchmark for retail HR is **1:100–150 = 45–67**. **18 is ~40% of the lean minimum.** Workflows reference 13 HR role families including Labor Relations Director, Workforce Management, and dedicated recruiters (the roster lists essentially 1 recruiter).

### 3.4 Legal & Compliance — stated 9, need 18–24
**Workload evidence — the most role-intensive function per person:**
- **1,872 workflow mentions** (highest density of any function)
- Contract review/approval (W230), litigation (W125), IP portfolio (W126)
- Corporate secretarial + SEC reportorial (W124, W481, ASHM W482)
- Regulatory compliance across 200 stores in **multiple LGUs** (VS-22, VS-76)
- AML/KYC/CDD/sanctions/STR (VS-86) — requires dedicated MLRO
- Anti-bribery & corruption / COI / gifts (VS-86.3)
- Data privacy / DPA / NPC breach response (VS-91)
- Anti-counterfeit (VS-71), customs/trade (VS-87)
- Consumer financing, leasing, insurance legal (VS-38, VS-96, VS-26)

9 people cannot cover 8 distinct sub-disciplines at this scale. Workflows name 8 role families here (Legal staff, Legal Counsel, VP Legal, Compliance staff/officer/manager, DPO, AML Officer, Corporate Secretary).

---

## 4. Missing Roles (named in workflows, absent from roster)

These specialized roles appear repeatedly in workflows but have **no home in the HQ department list**:

| Role | Mentions | Home Dept | Notes |
|---|---|---|---|
| Energy Manager | 42 | Facilities / Sustainability | Utility benchmarking across 200 stores |
| Government Affairs Mgr | 59 | Legal & Compliance | Multi-LGU permits (VS-22, VS-76) |
| Labor Relations Director | 45 | HR | CBA/grievance (VS-84) |
| AML Officer / ABC Officer | 48 | Legal & Compliance | VS-86 — mandatory MLRO |
| Fraud Management | 44 | Loss Prevention / Finance | VS-23.1, VS-80.3 |
| Metrology / Weights & Measures | 28 | Quality | Catch-weight items (lumber, wire) |
| S&OP Lead | 21 | Supply Chain | VS-136 multi-echelon |
| Third-Party Risk Mgmt (TPRM) | 19 | Risk/Audit | Vendor risk |
| BCP Manager | 17 | Risk/Facilities | VS-26 |
| ITAM (IT Asset Mgr) | 20 | IT | VS-99 |
| AI Governance | 26 | IT/Risk | VS-30.2 |
| Marketplace Manager | 41 | Marketing/Merch | VS-95 |
| Surety / Lease Admin | 46 | Legal/Real Estate | VS-42, VS-96 |
| OpEx / Continuous Improvement | 27 | Store Ops/Strategy | |
| Revenue Assurance Lead | 24 | Finance | VS-157 |
| EEO / DEI | 24 | HR | HR-044 requirement |

---

## 5. Inconsistencies in the Profile Document

1. **Executive count mismatch** — §11.1 org chart shows CEO + **6** direct reports (CFO, COO, CIO, CMO, CHRO, VP Legal), but §3.3 lists "Executive Office (5)" omitting CHRO and VP Legal.
2. **Department sum ≠ HQ total** — enumerated departments sum to ~275; stated HQ is 315. The ~40 gap is the 6 un-enumerated functions (HSE, Quality, Facilities/RE, Sustainability, Strategy, Trade Acct Mgmt).
3. **Revenue/employee footnote** (§4) claims HQ "expanded to 315 to include DPO, Tax Accountant, Logistics Finance Analyst, IT Helpdesk, Regional LP" — but these additions are not reflected in the department line items (Finance still shows ~37, IT ~33), so the expansion is double-counted or invisible.
4. **Buying team** (§13.1) named only VP + 5 Category Managers + 10–12 Buyers + 3 Pricing Analysts + 2 Planners (~22) against a 40-person department — the other ~18 were unexplained. **Resolved 2026-06-20:** §13.1 now breaks the 40 into ten role lines (VP, 5 Category Managers, 10 Buyers, 5 Planners/Allocators, 4 Pricing Analysts, 3 Assortment & Space, 3 Direct Sourcing, 3 Private Brand, 2 Promotions, 4 Merch Ops/MD) that sum to 40, rebalanced toward planning/pricing/assortment per §7.4.
5. **Store staffing 29/store** is internally consistent (§12.1) and defensible; the rationale (4 Stock Associates for replenishment/omnichannel) is sound. No change recommended there.

---

## 6. Store (5,800) and DC (600) Assessment — OK

- **Stores: 29/store** for an 8,000–15,000 sqm big-box with 3 POS terminals and curated 35K SKUs is **lean but defensible** (the doc argues it well). 12 Sales Associates across that footprint is tight during peak; consider a peak-season flex pool rather than changing base FTE.
- **DCs: 150/DC × 4** for cross-dock + WMS + special handling (lumber/tiles/paint) is **reasonable**. No change.

---

## 7. Recommendations

1. **Re-baseline HQ to ~440–470** and republish §3.3 with the 6 missing functions broken out (this alone closes the documentation gap).
2. **Prioritize hiring / capacity in Finance, IT, HR, Legal** — these four carry the highest workflow-to-headcount mismatch and the highest regulatory exposure (BIR, NPC, DOLE, SEC, AMLC).
3. **Staff the mandated roles** that Philippine law effectively requires at this scale: MLRO/AML Officer (AMLA), DPO + privacy staff (DPA), Safety Officers per region (RA 11058 / DO 198), Company Nurse/First Aiders (1 per store).
4. **Fix the role-mix in Merchandising** — shift 3–4 headcount from buyers into planners/pricing analysts/assortment to match VS-57 and the 35K-SKU complexity.
5. **Decide & document the Customer Service model** (centralized call center vs. in-store CSR) — it swings that department between 30 and 45.
6. **Correct the Executive count to 7** and reconcile §3.3, §4, and §11.1.
