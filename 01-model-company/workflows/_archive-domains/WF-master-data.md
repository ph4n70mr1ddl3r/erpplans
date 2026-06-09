# Master Data Management (MDM) Workflows

> Centralized item master creation & governance, customer master data governance & deduplication, location master lifecycle & hierarchy management, vendor master data governance, financial master data governance, employee master data lifecycle, tax & regulatory master, UOM & conversions, payment terms, service/non-stock item master, warehouse location & bin master, product attribute templates, assortment & store cluster master, promotional rule master, reason code & disposition master, kit/BOM structure master, manufacturer/brand master, routing/carrier/transit time master, intercompany transfer pricing rule master, seasonal calendar & event master, currency & exchange rate master, fiscal calendar & posting period master, bank & banking partner master, address & geographic hierarchy master (Philippine-specific), barcode/GTIN & item identification master, replenishment & planning parameter master, loyalty program configuration & rule master, planogram template & space planning master, product lifecycle status & transition rule master, and digital asset & product content master.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W252. Centralized Item Master Creation & Governance](#w252-centralized-item-master-creation-governance)
- [W253. Customer Master Data Governance & Deduplication](#w253-customer-master-data-governance-deduplication)
- [W254. Location Master Lifecycle & Hierarchy Management](#w254-location-master-lifecycle-hierarchy-management)
- [W287. Vendor Master Data Governance & Deduplication](#w287-vendor-master-data-governance--deduplication)
- [W288. Financial Master Data Governance (COA & Cost Centers)](#w288-financial-master-data-governance-coa--cost-centers)
- [W289. Pricing Master Governance (Base Prices & Matrices)](#w289-pricing-master-governance-base-prices--matrices)
- [W290. Hierarchical Category Structure Management](#w290-hierarchical-category-structure-management)
- [W291. Master Data Quality Monitoring & Reporting](#w291-master-data-quality-monitoring--reporting)
- [W292. Employee Master Data Governance & Cross-Entity Lifecycle](#w292-employee-master-data-governance--cross-entity-lifecycle)
- [W293. Tax & Regulatory Master Data Governance](#w293-tax--regulatory-master-data-governance)
- [W294. Unit of Measure (UOM) Master & Conversion Management](#w294-unit-of-measure-uom-master--conversion-management)
- [W295. Payment Terms & Settlement Rule Master Governance](#w295-payment-terms--settlement-rule-master-governance)
- [W296. Service & Non-Stock Item Master Governance](#w296-service--non-stock-item-master-governance)
- [W297. Warehouse Location & Bin Master Governance](#w297-warehouse-location--bin-master-governance)
- [W298. Product Attribute Template Master Governance](#w298-product-attribute-template-master-governance)
- [W299. Assortment & Store Cluster Master Governance](#w299-assortment--store-cluster-master-governance)
- [W300. Promotional Rule & Campaign Master Governance](#w300-promotional-rule--campaign-master-governance)
- [W301. Reason Code & Disposition Master Governance](#w301-reason-code--disposition-master-governance)
- [W302. Kit/BOM & Bundle Structure Master Governance](#w302-kitbom--bundle-structure-master-governance)
- [W303. Manufacturer/Brand Master Governance](#w303-manufacturerbrand-master-governance)
- [W304. Routing, Carrier & Transit Time Master Governance](#w304-routing-carrier--transit-time-master-governance)
- [W305. Intercompany Transfer Pricing Rule Master Governance](#w305-intercompany-transfer-pricing-rule-master-governance)
- [W306. Seasonal Calendar & Event Master Governance](#w306-seasonal-calendar--event-master-governance)
- [W307. Currency & Exchange Rate Master Governance](#w307-currency--exchange-rate-master-governance)
- [W308. Fiscal Calendar & Posting Period Master Governance](#w308-fiscal-calendar--posting-period-master-governance)
- [W309. Bank & Banking Partner Master Governance](#w309-bank--banking-partner-master-governance)
- [W310. Address & Geographic Hierarchy Master Governance (Philippine-Specific)](#w310-address--geographic-hierarchy-master-governance-philippine-specific)
- [W311. Barcode, GTIN & Item Identification Master Governance](#w311-barcode-gtin--item-identification-master-governance)
- [W312. Replenishment & Planning Parameter Master Governance](#w312-replenishment--planning-parameter-master-governance)
- [W313. Loyalty Program Configuration & Rule Master Governance](#w313-loyalty-program-configuration--rule-master-governance)
- [W314. Planogram Template & Space Planning Master Governance](#w314-planogram-template--space-planning-master-governance)
- [W315. Product Lifecycle Status & Transition Rule Master Governance](#w315-product-lifecycle-status--transition-rule-master-governance)
- [W316. Digital Asset & Product Content Master Governance](#w316-digital-asset--product-content-master-governance)
- [W399. Fixed Asset Master Data Governance](#w399-fixed-asset-master-data-governance)
- [W400. Equipment & Asset Maintenance (EAM) Master Governance](#w400-equipment--asset-maintenance-eam-master-governance)
- [W401. Fleet & Vehicle Master Governance](#w401-fleet--vehicle-master-governance)
- [W402. Contract & Agreement Master Governance](#w402-contract--agreement-master-governance)
- [W403. Competitor & Market Intelligence Master Governance](#w403-competitor--market-intelligence-master-governance)
- [W404. Point-of-Sale (POS) System & Hardware Master Governance](#w404-point-of-sale-pos-system--hardware-master-governance)
- [W405. Data Privacy & Consent Preferences Master Governance](#w405-data-privacy--consent-preferences-master-governance)
- [W406. ESG & Sustainability Metrics Master Governance](#w406-esg--sustainability-metrics-master-governance)

---

## W252. Centralized Item Master Creation & Governance

| Field | Detail |
|---|---|
| **Trigger** | Merchandising department requests a new SKU/Item to be added to the assortment |
| **Frequency** | Daily (approx. 50–100 new SKUs/week across all categories) |
| **Owner** | Master Data Manager |
| **Participants** | Category Manager, Pricing Analyst, Supply Chain Planner, Master Data Analyst |
| **Volume** | ~500–800 new SKUs created/month; ~1,000–1,500 SKU updates/month |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Request Initiation (Vendor Portal)**: Vendor submits a New Item Request via the Vendor Portal / PIM, providing core product data, images, and marketing copy. | Vendor | — | Variable |
| 2 | **Commercial Review & Categorization**: Category Manager reviews the vendor submission, assigns the hierarchy category, confirms standard cost, and flags any ESG/Sustainability attributes. | Category Manager | — | 10 min |
| 3 | **Attribute Enrichment — Supply Chain & Compliance**: Supply Chain Planner adds logistical attributes (dimensions, weight, pallet tie/high, default supply DC, minimum order quantity) and assigns Hazardous Materials (Hazmat) classifications if required. | Supply Chain Planner | — | 10 min |
| 4 | **Attribute Enrichment — Pricing**: Pricing Analyst adds retail pricing parameters (base retail price, price family grouping, initial margin) | Pricing Analyst | — | 5 min |
| 5 | **Validation & Quality Check**: Master Data Analyst reviews the completed request, ensuring no duplicates exist (checking GTIN/UPC/EAN) and all naming conventions are strictly followed | Master Data Analyst | Master Data Manager | 10 min |
| 6 | **Approval & Activation**: Master Data Manager approves the item. System assigns internal SKU number, activates the item across the relevant location matrix (store assortments), and syncs to POS and Ecommerce platforms | Master Data Manager | Master Data Manager | 5 min |

### System Touchpoints
- Vendor Portal / Product Information Management (PIM)
- ERP Item Master Module (centralized creation, attribute fields)
- ERP Compliance Module (Hazmat / ESG tracking)
- ERP Approval Workflow Engine
- POS / Ecom Integration (downstream sync)

### Pain Points / Risks
- Incomplete dimensional data causing warehouse slotting failures.
- Duplicate SKU creation leading to fragmented sales history and over-purchasing.

### Staffing Implication
50-100 new SKUs/week. Each SKU request ~30 min end-to-end (10 min request + 10 min enrichment + 5 min pricing + 10 min validation/approval). 2 Master Data Analysts full-time (~80 hours/week handling ~75 SKUs). 1 Master Data Manager oversight.

### Time Estimate
**Total**: ~30 minutes per new SKU (excluding queue time)

---

## W253. Customer Master Data Governance & Deduplication

| Field | Detail |
|---|---|
| **Trigger** | Ongoing customer data ingestion from POS loyalty sign-ups, Ecommerce registrations, and B2B Trade Account creations |
| **Frequency** | Continuous automated ingestion; Monthly manual deduplication review |
| **Owner** | CRM Data Steward |
| **Participants** | Store Cashier, B2B Sales Rep, Customer Service Rep, CRM Data Steward |
| **Volume** | ~10,000 new loyalty enrollments/month; deduplication script runs weekly |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Ingestion & Verification**: Customer data is captured at POS (phone number lookup/creation), Ecommerce, or B2B Portal. System mandates real-time One-Time Password (OTP) verification for mobile numbers to prevent dummy account creation and immediate duplicates. | Store Cashier / Customer | — | 2 min |
| 2 | **Automated Matching**: ERP/CDP runs daily batch matching algorithms (Levenshtein distance on names, exact match on email/mobile) to flag potential duplicate profiles | System | — | Automated |
| 3 | **Exception Management**: CRM Data Steward reviews the "Potential Duplicates" queue | CRM Data Steward | — | 15 min/batch |
| 4 | **Merge & Consolidate**: Steward executes a merge. System consolidates loyalty points, purchase history, and contact details into the surviving "Golden Record", and leaves a tombstone on the deprecated record | CRM Data Steward | CRM Data Steward | 10 min/merge |
| 5 | **Downstream Sync**: The Golden Record updates are pushed to Ecommerce, POS offline databases, and Marketing Automation tools | System | — | Automated |

### System Touchpoints
- ERP Customer Master / CRM Module
- Customer Data Platform (CDP) deduplication engine
- SMS Gateway (for OTP delivery)
- POS and Ecommerce APIs

### Pain Points / Risks
- OTP delivery delays (SMS gateway issues) causing friction at the checkout lane.
- Merging two distinct customers (e.g., family members sharing a phone number) causing privacy issues.

### Staffing Implication
Continuous automated ingestion. Monthly dedup review ~4 hours by CRM Data Steward. Real-time matching is automated. 1 CRM Data Steward FTE.

### Time Estimate
**Total**: ~15 minutes per merge/review; automated matching runs daily

---

## W254. Location Master Lifecycle & Hierarchy Management

| Field | Detail |
|---|---|
| **Trigger** | Real estate team confirms a new store/DC opening, relocation, or closure |
| **Frequency** | 5–10 times per year |
| **Owner** | IT ERP Administrator |
| **Participants** | Real Estate Manager, Operations Director, Finance Controller, Master Data Manager |
| **Volume** | ~1-2 new store locations added/month; hierarchy updates quarterly |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Location Request**: Operations submits a Location Master request specifying store type, region, GL company code, and tax registration details (TIN/Branch Code) | Operations Director | — | 15 min |
| 2 | **Financial Setup**: Finance Controller defines the cost center, profit center, and fixed asset location mappings for the new entity | Finance Controller | — | 20 min |
| 3 | **Logistical Setup**: Supply Chain assigns the supplying DC, default transit times, and delivery schedules to the location profile | Supply Chain Planner | — | 15 min |
| 4 | **Hierarchy Assignment**: Master Data Manager places the location in the enterprise hierarchy (e.g., Region: Visayas → Area: Cebu → Store: Mandaue City) | Master Data Manager | — | 10 min |
| 5 | **System Activation**: ERP Administrator activates the location. This triggers automated setup in POS polling routines, replenishment MRP runs, and financial reporting roll-ups | IT ERP Administrator | IT ERP Administrator | 30 min |

### System Touchpoints
- ERP Location/Site Master
- Finance GL Mapping
- Supply Chain Network configuration

### Pain Points / Risks
- Misaligned tax branch codes leading to BIR filing errors.
- Failure to update the hierarchy resulting in missing stores in regional sales reports.

### Staffing Implication
5-10 times/year. Each setup ~90 minutes (15 min request + 20 min financial + 15 min logistical + 10 min hierarchy + 30 min activation). Absorbed by IT ERP Administrator.

### Time Estimate
**Total**: ~90 minutes per new location setup

---

## W287. Vendor Master Data Governance & Deduplication

| Field | Detail |
|---|---|
| **Trigger** | Vendor onboarding requests, continuous automated deduplication checks, and manual update requests (e.g., bank detail changes) |
| **Frequency** | Continuous deduplication checks; daily vendor changes |
| **Owner** | Master Data Manager |
| **Participants** | Buyer, AP Clerk, AP Supervisor, Finance Manager, Master Data Analyst |
| **Volume** | ~10-20 vendor setups/week; ~30-50 updates/week; weekly deduplication script run |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Data Entry & Validation**: Vendor data is initially entered during onboarding (W36) or an update is requested. System enforces mandatory fields (TIN, address, bank details) and checks TIN uniqueness to prevent duplicates. | AP Clerk / Vendor | — | 10 min |
| 2 | **Automated Matching**: System runs nightly matching algorithm across vendor names, addresses, and TINs to flag potential duplicate vendor profiles or parent-child relationships. | System | — | Automated |
| 3 | **Exception Management**: Master Data Analyst reviews flagged potential duplicate vendors. If duplicates are found, analyst investigates (e.g., matching TINs for different branches vs. duplicate creation). | Master Data Analyst | — | 15 min/batch |
| 4 | **Merge & Consolidate**: For confirmed duplicates, analyst executes a merge. System consolidates PO history, payment history, and leaves a tombstone on the deprecated record. | Master Data Analyst | Master Data Manager | 10 min/merge |
| 5 | **Audit Trail Logging**: All changes to critical fields (bank details, TIN, tax classification) are captured in an immutable audit log. Bank detail changes trigger a 48-hour cooling-off period and require secondary approval (W36.7a). | System / Master Data Analyst | AP Supervisor | Automated |
| 6 | **Classification Governance**: Analyst verifies vendor classification (Local, Import, Service, MSME) using BIR/DTI records to ensure accurate reporting and MSME compliance tracking. | Master Data Analyst | Finance Manager | 5 min |

### System Touchpoints
- ERP Vendor Master Module
- Vendor Portal Integration (for self-service updates)
- ERP Audit Trail Engine
- Deduplication Engine

### Pain Points / Risks
- Vendor payment fraud due to unverified bank account changes.
- Duplicate vendors leading to fragmented spend visibility and missed volume discounts.

### Staffing Implication
Continuous automated ingestion. Weekly deduplication review ~2 hours. Master Data Analyst handles validation and merging.

### Time Estimate
**Total**: ~15 minutes per merge/review; automated checks run daily.

---

## W288. Financial Master Data Governance (COA & Cost Centers)

| Field | Detail |
|---|---|
| **Trigger** | Business expansion, new department creation, or annual budget preparation requiring new GL accounts or Cost Centers |
| **Frequency** | Monthly (for Cost Centers), Annually/Quarterly (for GL Accounts) |
| **Owner** | Corporate Controller |
| **Participants** | Finance Controller, Department Head, FP&A Manager, IT ERP Administrator |
| **Volume** | ~5-10 cost center changes/month; ~10-20 GL account changes/year |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Request Initiation**: Department Head or Finance Controller submits a request for a new Cost Center or GL Account via the MDM/Finance portal, providing justification and mapping details. | Finance Controller | — | 15 min |
| 2 | **Review & Standardization**: FP&A Manager reviews the request against the standardized Chart of Accounts structure to prevent proliferation and ensure consistency across the 5 legal entities. | FP&A Manager | — | 20 min |
| 3 | **Approval**: Corporate Controller approves the creation of the new financial master data object, confirming alignment with financial reporting standards and tax requirements. | Corporate Controller | CFO | 10 min |
| 4 | **System Setup & Mapping**: IT ERP Administrator configures the new GL/Cost Center in the ERP, sets up the required dimensions, maps it to the relevant financial statement roll-ups, and assigns security/access controls. | IT ERP Administrator | Corporate Controller | 30 min |
| 5 | **Communication**: System notifies relevant stakeholders (Finance, Operations) that the new financial master data is available for use in POs, invoices, and journal entries. | System | — | Automated |

### System Touchpoints
- ERP General Ledger / Finance Module
- ERP Organizational Hierarchy Configuration
- FP&A / Budgeting Software (if separate)

### Pain Points / Risks
- Cost center proliferation leading to overly complex budgeting and variance analysis.
- Inconsistent GL account usage across legal entities complicating consolidation.

### Staffing Implication
Ad-hoc requests. Handled by existing Finance and IT staff as part of their regular duties. FP&A review is critical for governance.

### Time Estimate
**Total**: ~75 minutes per request (excluding approval queue time)

---

## W289. Pricing Master Governance (Base Prices & Matrices)

| Field | Detail |
|---|---|
| **Trigger** | Initial setup of pricing rules, creation of new price lists, or structural changes to store/region pricing matrices |
| **Frequency** | Monthly structural updates; Daily operational price changes (handled in W40/W13) |
| **Owner** | VP Merchandising |
| **Participants** | Pricing Manager, Category Manager, Master Data Manager |
| **Volume** | ~2-5 structural matrix changes/month |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Strategy Definition**: Pricing Manager defines structural rules for a new base price list or regional markup matrix based on margin targets. | Pricing Manager | — | 2 hours |
| 2 | **Validation & Margin Simulation**: Master Data Manager reviews the matrix logic against existing promotional rules. System runs a sandbox simulation using historical 90-day basket data to project the overall margin impact and identify margin bleed. | Master Data Manager | — | 30 min |
| 3 | **Approval**: VP Merchandising reviews the margin simulation output and approves the new pricing master structure (MDM-005). | VP Merchandising | VP Merchandising | 10 min |
| 4 | **System Configuration**: Pricing Manager configs the new list in ERP, setting effective dates and linking it to the relevant Location Master (W254) hierarchies or Customer Trade accounts. | Pricing Manager | — | 45 min |

### System Touchpoints
- ERP Pricing Module / Rule Engine
- Pricing Sandbox / Margin Simulation Engine
- Location Master (for regional linking)
- POS / Ecom Integration (syncing the master rule engine)

### Pain Points / Risks
- Misconfigured logic leading to unintended global price drops.
- Overlapping discount matrices causing margin bleed.

### Staffing Implication
Managed by central Pricing team. ~3 hours per structural matrix change.

### Time Estimate
**Total**: ~3.5 hours per matrix structural setup.

---

## W290. Hierarchical Category Structure Management

| Field | Detail |
|---|---|
| **Trigger** | Introduction of new product lines or reorganization of existing merchandising departments |
| **Frequency** | Quarterly/Semi-Annually |
| **Owner** | Master Data Manager |
| **Participants** | VP Merchandising, Category Manager, BI/Data Analyst, Master Data Analyst |
| **Volume** | ~1-2 tree reorganizations per year; minor node additions monthly |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Hierarchy Proposal**: Merchandising proposes a change to the category tree (e.g., splitting "Tools" into "Hand Tools" and "Power Tools"). | Category Manager | — | 1 hour |
| 2 | **Impact Assessment**: BI Analyst assesses reporting impact and legacy mapping. Master Data Manager assesses reclassification effort for existing SKUs. | BI/Data Analyst | — | 2 hours |
| 3 | **Approval**: VP Merchandising approves the new multi-level category structure (MDM-007). | VP Merchandising | VP Merchandising | 15 min |
| 4 | **System Execution**: Master Data Analyst creates the new nodes (Department, Category, Sub-Category, Class), and executes a batch reclassification script for affected SKUs. | Master Data Analyst | Master Data Manager | 4 hours |
| 5 | **Downstream Sync**: The new hierarchy is synced to the Data Warehouse (for BI reporting) and Ecommerce (for website navigation). | System | — | Automated |

### System Touchpoints
- ERP Category Master
- BI/Data Warehouse
- Ecommerce PIM/Catalog

### Pain Points / Risks
- Broken historical reporting if legacy mapping is not maintained during tree reorganization.
- Orphaned SKUs lacking a valid category assignment.

### Staffing Implication
Significant manual effort during restructuring (up to 4 hours per node split) for reclassification. Handled by existing MDM team.

### Time Estimate
**Total**: ~1-2 days end-to-end for a minor reorganization.

---

## W291. Master Data Quality Monitoring & Reporting

| Field | Detail |
|---|---|
| **Trigger** | Monthly governance review and continuous automated profiling |
| **Frequency** | Automated daily profiling; Monthly governance review |
| **Owner** | Master Data Manager |
| **Participants** | Data Stewards (CRM, Vendor, Item), BI Analyst, Master Data Manager |
| **Volume** | Millions of records scanned daily against rule sets |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Automated Profiling**: System runs daily data quality (DQ) checks against predefined rules (e.g., % of Item Master missing dimensions, % of Customer Master missing email, suspected duplicate rates). | System | — | Automated |
| 2 | **Dashboard Generation**: BI platform aggregates DQ scores into a central MDM Governance Dashboard. | System | — | Automated |
| 3 | **Exception Routing**: High-priority exceptions (e.g., vendor missing TIN) automatically generate alert tickets routed to the respective Data Steward. | System | — | Automated |
| 4 | **Remediation**: Data Stewards execute bulk or single-record corrections based on the alerts. | Data Steward | — | 2 hours/week |
| 5 | **Data Archiving & Lifecycle Review**: System identifies obsolete records (e.g., zero transactions in 3 years, discontinued SKUs). Data Steward reviews and approves records for archival/soft-deletion to maintain system performance. | Data Steward | Master Data Manager | 2 hours/month |
| 6 | **Quarterly Data Governance Council Review**: Master Data Manager compiles the Enterprise Data Quality Scorecard and presents DQ trends, archiving metrics, and policy changes to the Enterprise Data Governance Council (W474) for ratification. | Master Data Manager | DGC Chair | 2 hours/quarter |

### System Touchpoints
- ERP / MDM Data Profiling Engine
- BI Dashboard (Data Governance)
- CRM & Vendor Portals (for missing data requests)
- Integration with W474 (Enterprise Data Governance Council for scorecard review)

### Pain Points / Risks
- Lack of executive visibility into how poor data quality drives downstream costs (e.g., slotting failures, duplicate payments).
- "Alert fatigue" if the profiling rules are too strict.
- System bloat causing slow queries if historical/obsolete data is not actively archived.

### Staffing Implication
Absorbed by existing MDM team and Data Stewards; shifts effort from reactive fixing to proactive monitoring.

### Time Estimate
**Total**: Continuous; ~2 hours monthly review.

---

## W292. Employee Master Data Governance & Cross-Entity Lifecycle

| Field | Detail |
|---|---|
| **Trigger** | New hire onboarding (W15), cross-entity transfer, position/department change, statutory ID update, or annual data verification |
| **Frequency** | Continuous (onboarding ~650 new hires/year); Quarterly bulk data verification |
| **Owner** | HR Data Steward |
| **Participants** | HR Specialist, Payroll Manager, IT ERP Administrator, Department Head |
| **Volume** | ~650 new employee records/year; ~200 cross-entity transfers/year; 6,715 records under governance |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Record Creation & Validation**: During onboarding (W15), HR Specialist enters employee master data. System enforces mandatory fields (full name, TIN, SSS, PhilHealth, Pag-IBIG, bank account, BIR tax status). System validates TIN format (XXX-XXX-XXX), SSS format, and checks for duplicate records using name + birthdate + TIN matching. | HR Specialist | HR Data Steward | 15 min |
| 2 | **Entity Assignment & Position Mapping**: System assigns the employee to the correct legal entity (5 entities). HR Specialist maps to department code, position code, and cost center (linked to W288 Financial Master). System validates that the cost center belongs to the assigned entity. | HR Specialist | — | 5 min |
| 3 | **Statutory ID Verification**: HR Data Steward verifies that all statutory IDs (TIN, SSS, PhilHealth, Pag-IBIG) are valid and unique. System flags employees with missing or duplicate statutory IDs for remediation before the next payroll run. | HR Data Steward | HR Manager | 10 min |
| 4 | **Cross-Entity Transfer Processing**: When an employee transfers between legal entities (e.g., BuildRight Depot, Inc. → BuildRight Logistics, Inc.), HR Specialist initiates a transfer request. System creates a separation record in the source entity and a new hire record in the target entity, linking them via a cross-reference ID for tenure continuity. Payroll Manager validates that YTD earnings, leave balances, and loan balances transfer correctly. | HR Specialist / Payroll Manager | HR Data Steward | 30 min |
| 5 | **Position & Department Change**: Department Head submits a position change request (promotion, lateral move, department reassignment). HR Data Steward updates the employee master, validates the new position code against the organizational hierarchy, and triggers downstream updates (access rights via W152, shift scheduling via W34, reporting line changes). | HR Data Steward | HR Manager | 10 min |
| 6 | **Quarterly Data Verification**: System generates a "Data Completeness Report" highlighting employees with missing fields (e.g., missing bank account, expired tax status, incomplete emergency contacts). HR Data Steward distributes reports to department heads for correction. | HR Data Steward | HR Manager | 4 hours/quarter |
| 7 | **Audit Trail & Change Logging**: All changes to employee master data (salary, department, entity, statutory IDs) are captured in an immutable audit log with timestamp, old value, new value, and changed-by user. | System | — | Automated |

### System Touchpoints
- ERP HR / Employee Master Module
- Payroll Module (for statutory ID and salary data)
- ERP Organizational Hierarchy (departments, positions, cost centers)
- IT Access Management (W152 — role-based access triggered by position changes)
- Biometric / Time & Attendance System (employee ID linkage)

### Pain Points / Risks
- Duplicate employee records (e.g., rehires creating a second profile instead of reactivating the original) causing fragmented YTD earnings and BIR reconciliation failures.
- Cross-entity transfers with incorrect YTD carryover causing over/under-taxation.
- Missing or invalid SSS/PhilHealth/Pag-IBIG numbers blocking statutory remittance filing.
- Stale position/department data causing incorrect cost center allocation in payroll GL postings.

### Staffing Implication
1 HR Data Steward FTE dedicated to employee master governance. Quarterly verification (~4 hours) absorbed by existing HR team. Cross-entity transfers require Payroll Manager coordination.

### Time Estimate
**Total**: ~15 minutes per new hire record; ~30 minutes per cross-entity transfer; ~4 hours quarterly verification.

---

## W293. Tax & Regulatory Master Data Governance

| Field | Detail |
|---|---|
| **Trigger** | BIR revenue regulation update, new tax code issuance, VAT/WHT rate change, LGU tax ordinance amendment, or annual tax table refresh |
| **Frequency** | As-needed (typically 2–4 BIR updates/year); Annual tax table refresh (January) |
| **Owner** | Tax Manager |
| **Participants** | Corporate Controller, Finance Controller, IT ERP Administrator, Master Data Analyst |
| **Volume** | ~2–4 regulatory updates/year; ~1 annual full refresh; ~200 ATC codes maintained |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Regulatory Change Monitoring**: Tax Manager monitors BIR Revenue Regulations, Revenue Memorandum Orders (RMOs), and LGU tax ordinances. When a change is identified, Tax Manager creates a Tax Master Change Request specifying the affected tax codes, rates, and effective dates. | Tax Manager | — | 30 min |
| 2 | **Impact Assessment**: Finance Controller assesses the impact on existing transactions — identifying open POs, pending invoices, and active promotional pricing affected by the rate change. Master Data Analyst identifies all vendor/customer records linked to the affected ATC codes. | Finance Controller / Master Data Analyst | Corporate Controller | 2 hours |
| 3 | **Tax Code Configuration**: IT ERP Administrator configures the new tax code or rate in the ERP Tax Master, specifying: effective date, tax type (VAT, EWT, percentage tax), rate, ATC code, BIR form mapping (2550M, 2550Q, 1601-E, 1601-C), and GL account for posting. System maintains both old and new rates with effective dating to handle transition-period transactions. | IT ERP Administrator | Tax Manager | 1 hour |
| 4 | **Validation & Testing**: Tax Manager runs test transactions (sample AP invoice, sample POS sale, sample payroll) using the new tax configuration to verify correct computation and GL posting. Corporate Controller reviews the test results. | Tax Manager | Corporate Controller | 1 hour |
| 5 | **Vendor/Customer Record Update**: Master Data Analyst bulk-updates vendor and customer records affected by the ATC code change. System generates a change log listing all records modified. | Master Data Analyst | Tax Manager | 2 hours |
| 6 | **Activation & Communication**: Tax Manager activates the new tax master configuration effective on the regulatory deadline. System notifies AP Clerks, Store Managers, and Payroll Officers of the change with a summary of affected codes. | Tax Manager | — | 30 min |
| 7 | **Post-Implementation Review**: Within the first month after activation, Tax Manager reviews a sample of transactions to verify correct tax application and BIR form generation. | Tax Manager | Corporate Controller | 2 hours |

### System Touchpoints
- ERP Tax Master / Configuration Module
- AP Module (EWT computation per vendor ATC)
- POS Module (VAT computation at checkout)
- Payroll Module (withholding tax on compensation)
- BIR eFPS Integration (W260 — tax filing)
- GL Module (tax posting accounts)

### Pain Points / Risks
- Incorrect effective dating causing transactions to apply the wrong tax rate during transition periods.
- Failure to update vendor ATC codes after a regulatory change, leading to BIR assessment penalties.
- LGU tax rate changes (e.g., local business tax, real property tax) not being updated on time, causing under/over-remittance.
- Misconfigured GL posting accounts causing tax balances to post to incorrect accounts, requiring manual journal adjustments during month-end close.

### Staffing Implication
Absorbed by existing Tax Manager and Finance team. Each regulatory update requires ~6–8 hours total effort across roles. Annual refresh ~4 hours.

### Time Estimate
**Total**: ~6–8 hours per regulatory update; ~4 hours annual refresh.

---

## W294. Unit of Measure (UOM) Master & Conversion Management

| Field | Detail |
|---|---|
| **Trigger** | Introduction of new UOM requirements (e.g., new product line sold by a different measure), conversion factor correction, or new supplier using a different purchasing UOM |
| **Frequency** | ~5–10 new UOM requests/month; ~2–3 conversion factor reviews/quarter |
| **Owner** | Master Data Manager |
| **Participants** | Category Manager, Supply Chain Planner, Pricing Analyst, Master Data Analyst |
| **Volume** | ~60 active UOM codes; ~150 conversion factors; ~5–10 new requests/month |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **UOM Request**: Category Manager or Supply Chain Planner requests a new UOM code or conversion factor (e.g., a new tile vendor sells by square meter but inventory is tracked by piece). Request specifies: base UOM, alternate UOM, conversion factor, and affected SKUs. | Category Manager / Supply Chain Planner | — | 10 min |
| 2 | **Conversion Validation**: Master Data Analyst validates the conversion factor mathematically and physically. For hardware retail, critical conversions include: board feet ↔ cubic meters, pieces ↔ square meters (tiles), meters ↔ feet (wire/pipes), kilograms ↔ pieces (nails/bolts). Analyst cross-references vendor packing lists and physical measurements. | Master Data Analyst | — | 15 min |
| 3 | **Impact Assessment**: System simulates the impact of the new/changed conversion factor on: (a) inventory valuation (WAC recalculation), (b) pricing (per-unit price consistency), and (c) replenishment (order quantity computation). Pricing Analyst reviews pricing impact. | Master Data Analyst / Pricing Analyst | — | 20 min |
| 4 | **Approval & Configuration**: Master Data Manager approves the UOM/conversion. IT ERP Administrator configures the UOM in the ERP, linking it to the relevant item records and ensuring catch-weight flags are set correctly (W5B.2, W3B.3). | Master Data Manager / IT ERP Administrator | Master Data Manager | 15 min |
| 5 | **Downstream Sync**: New UOM/conversion is synced to POS (for selling), WMS (for receiving/putaway), ecommerce (for online display), and procurement (for PO creation). | System | — | Automated |
| 6 | **Periodic Conversion Audit**: Quarterly, Master Data Analyst runs a conversion accuracy audit, comparing system conversion factors against actual physical measurements for high-volume catch-weight items (lumber, wire, tiles). Discrepancies trigger correction requests. | Master Data Analyst | Master Data Manager | 2 hours/quarter |

### System Touchpoints
- ERP UOM Master / Item Master Module
- POS (selling UOM and catch-weight)
- WMS (receiving and putaway UOM)
- Procurement (purchasing UOM vs. stocking UOM)
- Ecommerce (display UOM)
- Inventory Valuation (WAC per base UOM)

### Pain Points / Risks
- Incorrect conversion factors causing inventory valuation errors (e.g., if 1 board foot is configured as 0.00236 cubic meters instead of 0.00236, a small rounding error multiplied across thousands of transactions creates material valuation discrepancies).
- Catch-weight items sold at POS with wrong UOM conversion, causing customer over/under-charging.
- Vendor PO UOM not matching internal stocking UOM, leading to receiving discrepancies and 3-way match failures (FIN-004).
- Lack of periodic conversion audits allowing drift between system and physical reality.

### Staffing Implication
Absorbed by existing MDM team. ~5–10 requests/month × ~30 min each = ~2.5–5 hours/month. Quarterly audit ~2 hours.

### Time Estimate
**Total**: ~30 minutes per UOM/conversion request; ~2 hours quarterly audit.

---

## W295. Payment Terms & Settlement Rule Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New vendor/customer onboarding requiring payment terms, renegotiation of existing terms, or internal policy change to settlement rules |
| **Frequency** | ~20–30 new term assignments/month (linked to vendor/customer onboarding); ~2–3 policy changes/year |
| **Owner** | Finance Controller |
| **Participants** | AP Supervisor, AR Manager, Category Manager (for vendor terms), Sales Manager (for customer terms), Master Data Analyst |
| **Volume** | ~50 active payment term codes; ~1,000 vendor term assignments; ~600 B2B customer term assignments |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Terms Request**: During vendor onboarding (W36) or customer credit setup (W24), the requesting party proposes payment terms. Category Manager or Sales Manager submits the proposed terms with justification (e.g., "Net 60 requested by top-10 vendor due to 45-day manufacturing lead time"). | Category Manager / Sales Manager | — | 10 min |
| 2 | **Cash Flow Impact Analysis**: Finance Controller analyzes the proposed terms against current cash flow projections (W233). System calculates the projected DSO (Days Sales Outstanding) or DPO (Days Payable Outstanding) impact of the new terms. | Finance Controller | — | 15 min |
| 3 | **Approval**: Finance Controller approves standard terms (Net 30, Net 60, LC at Sight). Non-standard or extended terms (Net 90+, deferred payment) require CFO approval. | Finance Controller / CFO | CFO | 10 min |
| 4 | **System Configuration**: Master Data Analyst configures the payment term in the ERP, specifying: base term (days), discount structure (e.g., 2/10 Net 30 = 2% discount if paid within 10 days), settlement method (bank transfer, LC, check, e-wallet), and default GL cash discount account. Links the term to the vendor/customer master record. | Master Data Analyst | Finance Controller | 10 min |
| 5 | **Early Payment Discount Governance**: For terms with early payment discounts, AP Supervisor configures the discount capture rules in the AP module. System auto-calculates discount eligibility on the payment proposal run and flags invoices where paying early maximizes discount capture. | AP Supervisor | Finance Controller | 15 min |
| 6 | **Periodic Terms Review**: Annually, Finance Controller reviews all active payment terms against industry benchmarks and company working capital targets. Terms that deviate significantly (e.g., vendor on Net 90 when industry standard is Net 30) are flagged for renegotiation. | Finance Controller | CFO | 4 hours/year |
| 7 | **Audit Trail**: All changes to payment terms on vendor/customer records are logged with timestamp, old value, new value, and approver. Bank detail changes on vendor records trigger the 48-hour cooling-off period (W287 Step 5). | System | — | Automated |

### System Touchpoints
- ERP Payment Terms Master
- AP Module (vendor payment proposals, discount capture)
- AR Module (customer payment terms, dunning)
- Treasury Module (cash flow impact analysis)
- Vendor/Customer Master (term assignment)

### Pain Points / Risks
- Extended vendor terms (Net 90+) damaging supplier relationships if not negotiated transparently.
- Missed early payment discounts due to AP not running payment proposals within the discount window.
- Inconsistent customer terms causing disputes (e.g., corporate account expecting Net 45 but set up as Net 30).
- Manual override of system-calculated due dates bypassing governance controls.

### Staffing Implication
Absorbed by Finance Controller and AP team. Annual review ~4 hours. Per-term setup ~15 min.

### Time Estimate
**Total**: ~30 minutes per new term setup; ~4 hours annual review.

---

## W296. Service & Non-Stock Item Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Creation of a new service offering, modification of service pricing, or addition of a non-stock/special-order item template |
| **Frequency** | ~5–10 new service items/month; ~20–30 non-stock templates/month |
| **Owner** | Master Data Manager |
| **Participants** | Services Manager, Category Manager, Pricing Analyst, Master Data Analyst |
| **Volume** | ~200 active service items; ~500 non-stock item templates; growing with service expansion |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Service Item Request**: Services Manager or Category Manager requests creation of a new service item (e.g., "Aircon Installation — Split Type 1.5HP", "Bathroom Tile Laying — per sqm", "3D Kitchen Design Rendering — Standard"). Request specifies: service type (installation, rental, custom processing, consultancy, subscription), pricing model (fixed price, per-unit, hourly, tiered), and linked merchandise SKUs (if applicable, e.g., installation linked to appliance SKU). | Services Manager / Category Manager | — | 10 min |
| 2 | **Pricing & Margin Review**: Pricing Analyst reviews the proposed service pricing against cost inputs (labor rate, material cost, subcontractor rate, overhead allocation). System calculates the service margin and flags items below the target service margin threshold. | Pricing Analyst | — | 10 min |
| 3 | **Attribute Configuration**: Master Data Analyst configures service-specific attributes in the ERP: service duration estimate, scheduling rules, required certifications (e.g., licensed electrician for electrical installation), subcontractor assignment, warranty coverage, and revenue recognition method (point-in-time vs. over-time per PFRS 15). | Master Data Analyst | — | 15 min |
| 4 | **Non-Stock Item Template Creation**: For non-stock/special-order items (W38), Master Data Analyst creates item templates with: default vendor assignment, estimated lead time, special order flag (no inventory held), and auto-PO generation rules. Templates allow rapid creation of specific non-stock items against customer special orders while maintaining data consistency. | Master Data Analyst | Master Data Manager | 10 min |
| 5 | **POS & Channel Integration**: Service items are linked to POS quick-keys for in-store selling (W5B), ecommerce service booking pages, and the trade counter/pro desk (W112). Custom processing items (paint mixing W168, lumber cutting W169) are linked to the relevant POS workflow triggers. | Master Data Analyst | — | 10 min |
| 6 | **Approval & Activation**: Master Data Manager reviews the complete service/non-stock item setup, verifies all mandatory attributes are populated, and activates the item. System generates a cross-reference linking the service item to any related merchandise items for bundle/cross-sell reporting. | Master Data Manager | Master Data Manager | 5 min |
| 7 | **Periodic Service Catalog Review**: Quarterly, Services Manager and Master Data Manager review the active service catalog. Obsolete services (zero transactions in 6 months) are flagged for deactivation. Pricing is compared against subcontractor rate changes and competitor service pricing (W130). | Services Manager / Master Data Manager | VP Operations | 2 hours/quarter |

### System Touchpoints
- ERP Item Master (service item type distinct from merchandise)
- POS Module (service selling, custom processing triggers)
- Ecommerce Platform (service booking pages)
- Scheduling / Field Service Module (installation scheduling)
- Revenue Recognition Module (PFRS 15 compliance)
- Subcontractor / Partner Portal (work order dispatch)

### Pain Points / Risks
- Service items created as regular merchandise items, causing inventory valuation errors (services have no physical inventory).
- Incorrect revenue recognition (point-in-time vs. over-time) causing PFRS 15 compliance issues at audit.
- Service pricing not updated when subcontractor rates change, eroding margins.
- Non-stock item templates not linked to default vendors, causing delays in special-order PO generation.
- Missing certification requirements on service items leading to unqualified workers performing installations (safety/legal risk).

### Staffing Implication
Absorbed by existing MDM team and Services Manager. ~5–10 service items/month × ~30 min = ~2.5–5 hours/month. Quarterly review ~2 hours.

### Time Estimate
**Total**: ~30 minutes per service item setup; ~10 minutes per non-stock template; ~2 hours quarterly review.

---

## W297. Warehouse Location & Bin Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New DC zone/aisle/rack/bin creation, warehouse re-slotting, bin capacity change, or staging area reconfiguration |
| **Frequency** | During DC setup (4 DCs); ad-hoc re-slotting (~2–4 re-slot events/quarter per DC) |
| **Owner** | DC Operations Manager |
| **Participants** | WMS Administrator, Supply Chain Planner, DC Supervisor, Master Data Analyst |
| **Volume** | ~5,000–10,000 active bin locations per DC (~25,000–50,000 total); ~50–100 bin changes/quarter across all DCs |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Bin Request Initiation**: DC Supervisor or Supply Chain Planner requests a new bin/zone creation or re-slotting change. Request specifies: zone type (picking, reserve, staging, cross-dock, yard), aisle/rack/bin coordinates, storage capacity (weight, cubic volume, pallet positions), allowed item categories, and Hazmat segregation rules if applicable. | DC Supervisor / Supply Chain Planner | — | 15 min |
| 2 | **Slotting Analysis**: WMS Administrator runs a slotting analysis using velocity data (item pick frequency, cube-movement) to recommend optimal bin placement. Fast-moving A-items are assigned to ergonomic, ground-level, forward-pick locations; slow-moving C-items to reserve/upper rack positions. | WMS Administrator | — | 30 min |
| 3 | **Hazmat & Safety Compliance Check**: For zones storing chemicals, paint, or flammable materials, DC Operations Manager verifies bin placement against Hazmat segregation requirements (W236) and fire code regulations. Ensures incompatible chemicals are not stored adjacently. | DC Operations Manager | — | 15 min |
| 4 | **System Configuration**: WMS Administrator configures the bin in the WMS/ERP, specifying: location code (standardized format: DC-Zone-Aisle-Rack-Bin), bin type (pallet, carton, piece, bulk, yard), max weight/capacity, allowed UOM types, and replenishment-from link (for forward-pick bins linked to reserve bins). | WMS Administrator | DC Operations Manager | 20 min |
| 5 | **Validation & Testing**: Master Data Analyst validates the new bin configuration by running a test putaway and pick cycle. Confirms that RF-directed putaway routes correctly to the bin and pick paths are optimized. | Master Data Analyst | — | 15 min |
| 6 | **Periodic Re-Slotting Review**: Quarterly, DC Operations Manager reviews bin utilization reports (occupancy rate, pick frequency by zone, travel time analysis). Under-utilized or congested zones are flagged for re-slotting. Re-slotting plan is submitted for approval and executed during low-volume periods. | DC Operations Manager | VP Supply Chain | 4 hours/quarter |

### System Touchpoints
- WMS Location/Bin Master Module
- ERP Warehouse Setup (integration with W254 Location Master)
- Slotting Optimization Engine
- RF/Barcode System (location label printing and scanning)
- Hazmat Segregation Rules Engine (W236)

### Pain Points / Risks
- Incorrect bin capacity leading to overflow, safety hazards, or failed putaway.
- Poor slotting decisions causing excessive picker travel time and missed SLAs.
- Hazmat storage violations due to bin misassignment.
- Stale bin master data after re-slotting (RF gun directing to wrong locations).

### Staffing Implication
Absorbed by DC Operations team and WMS Administrator. ~2–4 re-slot events per quarter per DC × ~60 min each = ~8–16 hours/quarter. Initial DC setup: ~40 hours per DC for full bin master configuration.

### Time Estimate
**Total**: ~60 minutes per new bin/zone setup; ~4 hours quarterly re-slotting review per DC.

---

## W298. Product Attribute Template Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Introduction of a new product category, expansion of attribute requirements for existing categories, or data quality audit revealing missing attributes |
| **Frequency** | ~2–5 template changes/quarter; major template overhaul during category restructuring (W290) |
| **Owner** | Master Data Manager |
| **Participants** | Category Manager, Ecommerce Content Manager, BI/Data Analyst, Master Data Analyst |
| **Volume** | ~15 active category templates; ~200–300 total attribute definitions across all templates |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Template Change Request**: Category Manager or Ecommerce Content Manager requests a new attribute template or modification to an existing one. Request specifies: category affected, new attributes required (e.g., "Tile — Slip Rating (R9–R13)", "Lumber — Species (Tangile, Apitong, etc.)"), data type (text, numeric, dropdown, multi-select, Boolean), mandatory vs. optional, and attribute group (physical, commercial, logistical, compliance). | Category Manager / Ecommerce Content Manager | — | 20 min |
| 2 | **Impact Assessment**: BI Analyst assesses the downstream impact: (a) reporting — new attributes available for filtering and analysis; (b) ecommerce — new filter/facet on the website; (c) vendor portal — new mandatory fields for vendor item submissions; (d) existing items — backfill plan for items already in the category missing the new attribute. | BI/Data Analyst | — | 1 hour |
| 3 | **Template Design & Validation**: Master Data Analyst designs the attribute in the ERP/PIM: defines the attribute code, label, data type, allowed values (for dropdowns), default value, validation rules (min/max for numeric, regex for text), and units (mm, kg, watts). Cross-references with industry standards (e.g., GS1 GPC attributes for ecommerce feeds). | Master Data Analyst | — | 30 min |
| 4 | **Approval**: Master Data Manager reviews the template change, confirms alignment with the overall data model (no duplicate or redundant attributes), and approves. For mandatory attributes, confirms that a backfill plan exists for existing items. | Master Data Manager | Master Data Manager | 15 min |
| 5 | **System Configuration & Rollout**: Master Data Analyst configures the attribute in ERP and PIM. Links the attribute to the relevant category template. For ecommerce attributes, syncs to the ecommerce platform as a new facet/filter. Generates a data backfill task list for existing items missing the new mandatory attribute. | Master Data Analyst | — | 30 min |
| 6 | **Backfill Monitoring**: Master Data Analyst monitors completion of attribute backfill for existing items. System generates weekly completeness reports per category. Categories with < 95% mandatory attribute completion are escalated to the Category Manager. | Master Data Analyst | Master Data Manager | 2 hours/month |

### System Touchpoints
- ERP Item Attribute Module / PIM System
- Ecommerce Platform (facet/filter configuration)
- BI/Data Warehouse (attribute availability for reporting)
- Vendor Portal (attribute requirements for vendor item submissions)
- MDM Data Quality Dashboard (attribute completeness tracking — W291)

### Pain Points / Risks
- Proliferation of similar attributes across categories (e.g., "Width" in mm vs. "Width" in cm) causing data inconsistency.
- Mandatory attributes without a backfill plan, causing large volumes of incomplete item records.
- Dropdown value lists not maintained, leading to free-text entry and inconsistent data.
- Attribute definitions not aligned with GS1/industry standards, causing ecommerce catalog sync failures.

### Staffing Implication
Absorbed by existing MDM team and Category Managers. ~2–5 template changes/quarter × ~2 hours each = ~4–10 hours/quarter. Backfill monitoring ~2 hours/month.

### Time Estimate
**Total**: ~2 hours per template change; ~2 hours/month backfill monitoring.

---

## W299. Assortment & Store Cluster Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New store opening requiring cluster assignment, strategic assortment review, demographic shift in a store's trade area, or seasonal assortment reconfiguration |
| **Frequency** | Quarterly cluster reviews; ad-hoc for new store openings (~10–15/year) |
| **Owner** | VP Merchandising |
| **Participants** | Category Manager, Merchandise Planner, Store Operations Director, Master Data Analyst |
| **Volume** | ~200 store cluster assignments; ~10–15 active assortment matrices per category; ~10–15 new store cluster assignments/year |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Cluster Definition & Review**: Merchandise Planner proposes store cluster definitions based on: (a) geographic region (Mindanao, Visayas, Luzon, NCR), (b) store volume tier (high/medium/low revenue), (c) trade area demographics (residential vs. commercial vs. mixed), (d) store format/size (8,000 vs. 15,000 sqm). Each cluster has a descriptive name and defined criteria. | Merchandise Planner | — | 2 hours |
| 2 | **Cluster Assignment**: Master Data Analyst assigns each store (W254) to the appropriate cluster in the ERP/assortment planning system. System validates that all 200 stores are assigned to exactly one cluster. New stores receive a provisional cluster assignment at opening (W16) with review at the next quarterly cycle. | Master Data Analyst | — | 30 min |
| 3 | **Assortment Matrix Definition**: Category Manager defines the assortment matrix per cluster: which SKU groups (core, extended, seasonal, optional) are mandatory vs. optional for stores in each cluster. Core assortment items must be stocked at all stores in the cluster; optional items are at the Store Manager's discretion. Matrix specifies minimum facings and display requirements. | Category Manager | — | 4 hours/category |
| 4 | **System Configuration**: Master Data Analyst configures the assortment matrix in the ERP/planning system, linking each cluster to the relevant SKU list and planogram template. System validates that the matrix is internally consistent (no duplicate SKU assignments, no orphaned clusters). | Master Data Analyst | — | 1 hour |
| 5 | **Approval**: VP Merchandising approves the cluster definitions and assortment matrices. Confirms alignment with the overall merchandising strategy and budget. | VP Merchandising | VP Merchandising | 30 min |
| 6 | **Downstream Sync**: The assortment matrix is synced to: (a) replenishment engine — only matrix-assigned SKUs are auto-replenished to the store, (b) planogram system — correct template assigned per cluster, (c) ecommerce — store-level availability reflects the assortment matrix, (d) BI/reporting — store performance comparisons within clusters. | System | — | Automated |
| 7 | **Quarterly Cluster Performance Review**: Merchandise Planner reviews cluster-level performance metrics (revenue/sqm, assortment compliance, inventory turns, fill rate). Stores that have consistently outperformed or underperformed their cluster are flagged for reassignment. New demographic data (e.g., new subdivision construction near a store) is evaluated for cluster impact. | Merchandise Planner | VP Merchandising | 4 hours/quarter |

### System Touchpoints
- ERP Assortment Planning / Category Management Module
- Store Location Master (W254 — store attributes feed cluster assignment)
- Replenishment Engine (SCP-002 — assortment matrix filters auto-replenishment)
- Planogram System (cluster-linked templates)
- Ecommerce Platform (store-level assortment visibility)
- BI/Analytics (cluster-level reporting)

### Pain Points / Risks
- Misassigned stores in wrong clusters receiving inappropriate assortments (e.g., a small Visayas store receiving NCR-level assortment depth).
- Stale cluster definitions not reflecting demographic shifts, leading to over/under-stocking.
- Assortment matrix not synced to replenishment, causing auto-replenishment of items not in the store's assortment plan.
- New stores opened without a cluster assignment, receiving a default "all-items" replenishment plan.

### Staffing Implication
Absorbed by Merchandising team and MDM team. Quarterly cluster review ~4 hours. New store assignment ~30 min per store. Assortment matrix creation ~4 hours per category (one-time with quarterly updates).

### Time Estimate
**Total**: ~8 hours per cluster definition cycle (quarterly); ~30 minutes per new store assignment.

---

## W300. Promotional Rule & Campaign Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New promotional mechanic introduction, campaign rule change, seasonal promotion calendar update, or vendor-funded promotion agreement |
| **Frequency** | ~6 major sale events/year; ~12 monthly hot deals; ~50–100 promotional rule changes/month |
| **Owner** | VP Merchandising |
| **Participants** | Pricing Manager, Category Manager, Loyalty Manager, Marketing Campaign Manager, Master Data Analyst |
| **Volume** | ~200–300 active promotional rules at any time; ~50–100 new/modified rules/month |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Promotional Rule Request**: Category Manager or Marketing Campaign Manager submits a promotional rule creation request specifying: rule type (percentage discount, fixed amount off, BOGO, multi-buy/quantity break, bundle pricing, loyalty points multiplier, gift-with-purchase), applicable items (specific SKUs, categories, or brands), eligibility criteria (all customers, loyalty tiers, trade accounts only), date range, and channel applicability (POS, ecommerce, both). | Category Manager / Marketing Campaign Manager | — | 15 min |
| 2 | **Rule Configuration & Simulation**: Pricing Analyst configures the rule in the ERP Promotion Engine. For complex rules (e.g., "Buy 3 tiles, get 20% off + 2x loyalty points"), analyst specifies: trigger conditions, discount application sequence (largest discount first vs. stackable), maximum discount cap per transaction, and exclusions (clearance items, catch-weight items). System runs a sandbox simulation using 90-day historical basket data to project: (a) total promotional cost, (b) margin impact per item, (c) estimated sales uplift, (d) halo effect on related items. | Pricing Analyst | — | 30 min |
| 3 | **Vendor-Funded Promotion Linkage**: For vendor-funded promotions (co-op advertising, vendor rebates), Category Manager links the promotional rule to the vendor agreement (W27 rebate, W155 JBP). System validates that the vendor's contribution is documented and the net cost to BuildRight is within approved thresholds. | Category Manager | — | 10 min |
| 4 | **Loyalty Rule Review**: For promotions involving loyalty points (double points, bonus points), Loyalty Manager reviews the rule to verify: (a) points liability impact on the loyalty program financials (W104), (b) correct tier targeting, (c) consistency with the loyalty program terms and conditions. | Loyalty Manager | — | 10 min |
| 5 | **Approval**: VP Merchandising reviews the simulation output and approves the promotional rule. High-impact promotions (estimated margin erosion > PHP 500K) require CFO approval. VP Merchandising confirms the promotional calendar does not have overlapping or conflicting rules. | VP Merchandising / CFO | VP Merchandising | 15 min |
| 6 | **System Activation & Channel Push**: Master Data Analyst activates the rule with the specified effective dates. System pushes the promotional rule to: (a) POS terminals (auto-apply engine), (b) ecommerce platform (promo banner and pricing), (c) marketplace integrations (Lazada/Shopee promo sync), (d) mobile app (push notification trigger). | Master Data Analyst | — | 10 min |
| 7 | **Post-Promotion Deactivation & Analysis**: After the promotion ends, system auto-deactivates the rule. Pricing Analyst generates a post-promotion performance report: actual vs. projected sales uplift, margin impact, promotional cost, vendor contribution received, and loyalty points issued. Results feed into the next promotional planning cycle (W13). | Pricing Analyst / System | VP Merchandising | 1 hour/promotion |

### System Touchpoints
- ERP Promotion Engine / Rule Builder
- POS Auto-Apply Engine (POS-014)
- Ecommerce Promotion Module
- Marketplace Integration (W180 — promo sync)
- Loyalty Points Engine (CRM-001 — points multiplier rules)
- Vendor Rebate Module (W27 — vendor-funded promo linkage)
- Pricing Sandbox / Margin Simulation Engine
- Mobile App (push notification triggers)

### Pain Points / Risks
- Overlapping promotional rules causing unexpected stacking (e.g., percentage discount + loyalty discount + bundle price compounding to below-cost selling).
- Promotional rules not deactivating on schedule, causing customers to receive expired discounts.
- Vendor-funded promotions activated without documented vendor contribution, causing margin bleed.
- Mismatched promotional pricing between POS and ecommerce, causing customer complaints and price compliance violations.
- Complex multi-buy rules misconfigured at POS, causing incorrect checkout totals and cashier overrides.

### Staffing Implication
Absorbed by Pricing team, Merchandising, and MDM team. ~50–100 rule changes/month × ~30 min each = ~25–50 hours/month. Post-promotion analysis ~1 hour per major promotion (~6 hours/month).

### Time Estimate
**Total**: ~30 minutes per promotional rule configuration; ~1 hour post-promotion analysis per major event.

---

## W301. Reason Code & Disposition Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New operational exception type identified, audit finding requiring new tracking codes, or periodic code rationalization review |
| **Frequency** | ~5–10 new reason codes/year; annual rationalization review |
| **Owner** | Master Data Manager |
| **Participants** | Store Operations Director, DC Operations Manager, Finance Controller, AP Supervisor, Loss Prevention Officer, Master Data Analyst |
| **Volume** | ~100–150 active reason codes across all domains (inventory, returns, vendor, finance); ~15–20 disposition codes |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Code Request**: Operational stakeholder (Store Operations, DC, Finance, LP) requests a new reason code or disposition code. Request specifies: code domain (inventory adjustment, return, vendor dispute, AP hold, AR write-off, cycle count variance, damaged goods), code description, disposition action (return to stock, scrap, return to vendor, donate, quarantine, hold for investigation), and GL account mapping for financial impact posting. | Operational Stakeholder | — | 10 min |
| 2 | **Rationalization Review**: Master Data Analyst reviews existing codes in the same domain to check for duplication or overlap. If a similar code already exists, the request is redirected to use the existing code. If genuinely new, analyst confirms it fills a gap not covered by current codes. Target: no two codes with the same meaning in the same domain. | Master Data Analyst | — | 15 min |
| 3 | **Financial Impact Mapping**: Finance Controller reviews the GL account mapping for the new code. Ensures that: (a) the correct expense/revenue account is debited/credited, (b) the correct cost center bears the impact, (c) the code's financial treatment is consistent with PFRS and the company's accounting policies. | Finance Controller | — | 10 min |
| 4 | **System Configuration**: Master Data Analyst configures the reason/disposition code in the ERP, specifying: code value, description, domain, applicable modules (POS, WMS, AP, AR, Inventory), disposition action, GL mapping, and mandatory attachment requirement (e.g., "Damage" codes require photo evidence). | Master Data Analyst | — | 10 min |
| 5 | **Approval**: Master Data Manager approves the new code. Confirms alignment with the overall code structure and no redundancy. | Master Data Manager | Master Data Manager | 5 min |
| 6 | **Annual Rationalization**: Annually, Master Data Manager conducts a full rationalization review of all reason/disposition codes. Codes with zero usage in 12 months are flagged for deactivation. Codes that are frequently misused (identified by LP audit) are redesigned or merged. New codes proposed by operational teams are evaluated against the existing structure. | Master Data Manager | CFO / COO | 4 hours/year |

### System Touchpoints
- ERP Reason Code / Disposition Master
- Inventory Module (adjustment reason codes — W92)
- POS Module (return reason codes — W12A)
- AP Module (invoice hold/dispute reason codes — W244)
- WMS Module (receiving discrepancy codes — W3, damaged goods codes — W91)
- GL Module (account mapping for financial impact)
- MDM Data Quality Dashboard (code usage analytics — W291)

### Pain Points / Risks
- Proliferation of similar reason codes (e.g., "Damaged — Transit" vs. "Damaged — Handling" vs. "Damaged — Water") leading to inconsistent coding and unreliable analytics.
- Reason codes without GL mapping causing unposted financial impacts during month-end close.
- Disposition codes that don't enforce required evidence (photos, vendor authorization), enabling fraud or compliance gaps.
- Deprecated codes still selectable by users, causing reporting inconsistencies.
- "Other" or "Miscellaneous" codes being overused (top code by volume), masking the real reasons behind exceptions.

### Staffing Implication
Minimal ongoing effort. ~5–10 new codes/year × ~30 min each = ~2.5–5 hours/year. Annual rationalization ~4 hours.

### Time Estimate
**Total**: ~30 minutes per new code; ~4 hours annual rationalization.

---

## W302. Kit/BOM & Bundle Structure Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New kit/bundle product creation, BOM component change, costing method change, or seasonal kit refresh |
| **Frequency** | ~10–20 new kits/year; ~5–10 BOM changes/quarter; seasonal kit refresh 2x/year |
| **Owner** | Master Data Manager |
| **Participants** | Category Manager, Supply Chain Planner, Cost Accountant, Pricing Analyst, Master Data Analyst |
| **Volume** | ~200–300 active kit/bundle items; ~1,000–1,500 component line relationships |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Kit/BOM Request**: Category Manager requests creation of a new kit or modification to an existing BOM. Request specifies: kit parent item (already created per W252), component items with quantities, assembly instructions (if applicable), and target retail price. Example: "Bathroom Complete Set — Basic" containing 1 toilet (SKU-A), 1 lavatory (SKU-B), 2 angle valves (SKU-C), 2 flexible hoses (SKU-D), 1 installation hardware pack (SKU-E). | Category Manager | — | 15 min |
| 2 | **BOM Validation**: Master Data Analyst validates the BOM: (a) all component items exist in the item master (W252), (b) quantities are positive integers (or valid fractions for catch-weight), (c) no circular references (kit containing itself), (d) component items are not themselves kits with the same parent (max nesting depth = 1 to avoid costing complexity). | Master Data Analyst | — | 15 min |
| 3 | **Costing Analysis**: Cost Accountant calculates the kit cost by rolling up component costs (WAC × quantity per component). Compares the rolled-up cost to the target retail price to verify the kit margin meets the target threshold. If components include items with volatile costs (e.g., copper wire, steel), analyst runs a sensitivity analysis. | Cost Accountant | — | 20 min |
| 4 | **Supply Chain Feasibility**: Supply Chain Planner confirms that all components are available for kit assembly at the designated DC. Evaluates component lead times and identifies any sourcing constraints. For seasonal kits, confirms that component procurement aligns with the seasonal buy plan (W32). | Supply Chain Planner | — | 15 min |
| 5 | **System Configuration**: Master Data Analyst configures the BOM in the ERP, specifying: parent item, component items with quantities, assembly type (pre-built kit with physical inventory vs. virtual bundle assembled at POS), costing method (rolled-up WAC vs. manual cost), and disassembly rules (whether the kit can be broken back into components). | Master Data Analyst | — | 15 min |
| 6 | **Approval & Activation**: Master Data Manager approves the BOM. System validates the complete configuration. For pre-built kits, system creates a replenishment rule for the parent item and generates assembly orders at the DC (W46). For virtual bundles, system configures the POS promotion rule (W300) that applies the bundle discount when all components are scanned. | Master Data Manager | Master Data Manager | 10 min |
| 7 | **Periodic BOM Review**: Semi-annually, Category Manager and Cost Accountant review active kit BOMs. Kits with component cost changes > 10% since last review are flagged for repricing. Seasonal kits from the previous season are deactivated. Kit sales velocity is compared to plan; slow-moving kits are candidates for discontinuation (W68). | Category Manager / Cost Accountant | Master Data Manager | 4 hours/semi-annually |

### System Touchpoints
- ERP BOM / Kit Master Module
- Inventory Module (component reservation, kit stock tracking)
- Costing Module (rolled-up cost calculation, WAC impact)
- WMS Module (kit assembly orders — W46)
- POS Module (virtual bundle pricing)
- Replenishment Engine (kit-level demand signals)

### Pain Points / Risks
- Component cost increases eroding kit margins without triggering repricing (margin bleed).
- Component discontinuation (W68) without updating the BOM, causing assembly failures or phantom components.
- Incorrect BOM quantities causing assembly shortages or excess component consumption.
- Virtual bundles not correctly configured at POS, allowing customers to buy individual items without the bundle discount (or receiving the discount without all components).
- Multi-level BOMs (kits within kits) creating costing and inventory complexity beyond system capability.

### Staffing Implication
Absorbed by existing MDM team, Merchandising, and Finance. ~10–20 new kits/year × ~60 min each = ~10–20 hours/year. Semi-annual review ~4 hours.

### Time Estimate
**Total**: ~60 minutes per new kit/BOM; ~4 hours semi-annual review.

---

## W303. Manufacturer/Brand Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New brand/manufacturer onboarding, brand acquisition or licensing, private label brand creation (W129), or brand discontinuation |
| **Frequency** | ~10–20 new brands/year; ~5 brand changes/quarter; private label brand creation ~1–2/year |
| **Owner** | Master Data Manager |
| **Participants** | Category Manager, VP Merchandising, Legal Counsel, Master Data Analyst |
| **Volume** | ~500–800 active brands across all categories; ~300–500 active manufacturers; 2–3 private label brands |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|
| 1 | **Brand Request**: Category Manager requests creation of a new brand or manufacturer in the master. Request specifies: brand name, manufacturer/parent company, country of origin, associated vendors (one brand may be supplied by multiple vendors), product categories the brand covers, and any licensing/trademark considerations. | Category Manager | — | 10 min |
| 2 | **Deduplication Check**: Master Data Analyst checks for existing brand records using fuzzy matching (brand name similarity, parent company match). Common duplicates: "3M" vs. "3M Philippines" vs. "Minnesota Mining & Mfg"; "Bosch" vs. "Robert Bosch". If duplicate found, merges instead of creating new. | Master Data Analyst | — | 10 min |
| 3 | **Vendor-Brand Linkage**: Master Data Analyst links the brand to the authorized vendor(s) in the ERP. This establishes the many-to-many relationship: one brand can have multiple vendors (e.g., regional distributors for the same brand), and one vendor can carry multiple brands. Validates that linked vendors are active (W287). | Master Data Analyst | — | 10 min |
| 4 | **Private Label Governance**: For private label brands (W129), VP Merchandising and Legal Counsel review: (a) trademark registration status, (b) packaging compliance (FDA/DTI requirements where applicable), (c) approved factory list (W160 — social compliance audit required), and (d) brand positioning and margin targets. Private label brands require additional governance steps including quality testing (W150) and factory audit (W160). | VP Merchandising / Legal Counsel | — | 1 hour |
| 5 | **System Configuration**: Master Data Analyst configures the brand/manufacturer in the ERP, specifying: brand code, name, manufacturer, country of origin, active status, and linked categories. For private labels, adds the quality compliance flag (requiring factory audit certification before any SKU can be activated). | Master Data Analyst | Master Data Manager | 15 min |
| 6 | **Downstream Sync**: Brand master is synced to: (a) item master (W252 — brand assignment on each SKU), (b) ecommerce (brand filter/facet and brand landing pages), (c) BI/reporting (brand-level sales, margin, and market share analysis), (d) vendor portal (brand authorization for vendor item submissions). | System | — | Automated |
| 7 | **Annual Brand Performance Review**: Annually, Category Manager and Master Data Manager review all active brands. Brands with declining sales, quality issues, or vendor relationship changes are flagged. Inactive brands (zero sales in 12 months) are deactivated. Brand rationalization recommendations are submitted to VP Merchandising. | Category Manager / Master Data Manager | VP Merchandising | 4 hours/year |

### System Touchpoints
- ERP Brand / Manufacturer Master
- Item Master (W252 — brand assignment)
- Vendor Master (W287 — vendor-brand authorization)
- Ecommerce Platform (brand navigation)
- BI/Data Warehouse (brand-level analytics)
- Vendor Portal (brand-authorized vendor mapping)

### Pain Points / Risks
- Duplicate brand records causing fragmented brand-level sales reporting (e.g., "Dulux" and "Dulux Paint" reporting as two separate brands).
- Brand not linked to authorized vendors, allowing incorrect vendor-brand combinations in POs.
- Private label brands activated without factory audit certification, creating compliance and quality risks.
- Brand deactivation without checking for active SKUs, causing orphaned items.
- Brand name inconsistent between ERP and ecommerce, causing broken brand pages online.

### Staffing Implication
Absorbed by existing MDM team and Category Managers. ~10–20 new brands/year × ~30 min each = ~5–10 hours/year. Annual review ~4 hours.

### Time Estimate
**Total**: ~30 minutes per brand creation; ~1 hour for private label brands; ~4 hours annual review.

---

## W304. Routing, Carrier & Transit Time Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New store opening requiring route assignment, carrier contract change, new DC serving new regions, or quarterly route optimization review |
| **Frequency** | ~10–15 new route assignments/year (new stores); quarterly carrier/route review; ad-hoc for carrier changes |
| **Owner** | VP Supply Chain |
| **Participants** | Logistics Manager, DC Operations Manager, Fleet Manager, Master Data Analyst |
| **Volume** | ~200 store delivery routes; ~40 inter-island shipping routes; ~15 active carriers (owned fleet + 3PL); ~4 DCs as origin points |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Route Request**: Logistics Manager requests a new route or route modification. For new store openings (W16), request specifies: origin DC, destination store(s), recommended carrier (owned fleet or 3PL), estimated transit time, and delivery frequency (2–3x/week). For route modifications, specifies the reason (carrier performance issue, cost optimization, new road/bridge availability). | Logistics Manager | — | 15 min |
| 2 | **Transit Time Validation**: Logistics Manager validates the estimated transit time based on: (a) historical actual delivery data for similar routes, (b) inter-island ferry schedules (for Visayas/Mindanao routes), (c) known bottlenecks (port congestion, typhoon-season delays), and (d) carrier SLA commitments. System stores both standard transit time and peak-season buffer transit time. | Logistics Manager | — | 20 min |
| 3 | **Carrier Assignment & Rate Verification**: Fleet Manager assigns the carrier and verifies the contracted rate per trip/kg/cbm. For 3PL carriers, validates that the carrier contract (W62B) is active and rates are current. For owned fleet, confirms vehicle availability and driver assignment. System stores: carrier code, rate, rate type (per trip, per kg, per cbm, per km), and rate effective dates. | Fleet Manager | — | 15 min |
| 4 | **System Configuration**: Master Data Analyst configures the route in the ERP/transportation module, specifying: route code, origin DC (linked to W254), destination store(s), carrier assignment, standard transit time, peak buffer time, delivery schedule (day-of-week), vehicle type requirement, and special handling flags (Hazmat routing restrictions, oversized load permits). | Master Data Analyst | VP Supply Chain | 20 min |
| 5 | **Downstream Integration**: Route master is synced to: (a) replenishment engine — transit time feeds the lead time calculation for store replenishment (SCP-002), (b) WMS — route information drives load planning and dispatch (W106), (c) fleet telematics (W199) — route geofencing for GPS tracking, (d) ecommerce — transit time drives home delivery ETAs (W19). | System | — | Automated |
| 6 | **Quarterly Route Optimization Review**: Logistics Manager reviews route performance quarterly: on-time delivery %, actual vs. standard transit time, carrier cost per delivery, and route utilization (truck fill rate). Underperforming routes are flagged for carrier change or re-optimization (W196). New routes (e.g., from newly opened roads or ferry services) are evaluated for time/cost savings. | Logistics Manager | VP Supply Chain | 4 hours/quarter |

### System Touchpoints
- ERP Transportation / Route Master Module
- Replenishment Engine (SCP-002 — lead time = transit time + DC processing time)
- WMS Load Planning (W106 — route-based dispatch)
- Fleet Telematics (W199 — route geofencing and tracking)
- Ecommerce Platform (W19 — delivery ETA calculation)
- Carrier/3PL Integration (API-based rate and schedule sync)

### Pain Points / Risks
- Inaccurate transit times feeding wrong lead times into replenishment, causing stockouts or overstock.
- Carrier rate changes not updated in the route master, causing freight cost variance.
- Inter-island routes not accounting for ferry schedule seasonality, causing chronic late deliveries during peak season.
- Hazmat routing restrictions not configured, allowing illegal transport of hazardous materials through restricted tunnels or residential areas.
- New store openings without route assignment, causing delayed first delivery and empty shelves at opening.

### Staffing Implication
Absorbed by Supply Chain and Logistics team. ~10–15 new routes/year × ~60 min each = ~10–15 hours/year. Quarterly review ~4 hours.

### Time Estimate
**Total**: ~60 minutes per new route setup; ~4 hours quarterly route optimization review.

---

## W305. Intercompany Transfer Pricing Rule Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New IC service/goods flow establishment, annual transfer pricing review, regulatory rate change, or new legal entity creation |
| **Frequency** | Annual comprehensive review; ad-hoc for new IC flows (2–3/year) |
| **Owner** | Corporate Controller |
| **Participants** | CFO, VP Supply Chain, VP Operations, Tax Manager, IT ERP Administrator |
| **Volume** | ~15–20 active IC pricing rules across 5 entities and ~10 entity-pair transaction types |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|
|---|---|---|---|
| 1 | **IC Flow Identification**: Corporate Controller identifies a new intercompany service or goods flow requiring a transfer pricing rule. Current IC flows include: (a) BuildRight Depot → Property Management: store/DC lease payments, (b) Depot → Logistics: warehousing/distribution fees, (c) Depot → Digital Commerce: per-order ecommerce fulfillment fees, (d) Depot → Logistics: inter-DC freight charges, (e) Holdings → all entities: management fees. For each flow, specifies the pricing method (cost-plus, comparable uncontrolled price, transactional net margin method). | Corporate Controller | — | 30 min |
| 2 | **Arm's-Length Pricing Calculation**: Tax Manager calculates the arm's-length transfer price based on the selected method. For cost-plus: verifies the cost base (direct costs + allocated overhead) and applies the agreed markup percentage. For comparable uncontrolled price: benchmarks against market rates from third-party providers. Documents the calculation methodology and supporting data for BIR/transfer pricing documentation (W235). | Tax Manager | Corporate Controller | 2 hours |
| 3 | **System Configuration**: IT ERP Administrator configures the IC pricing rule in the ERP, specifying: (a) source entity, (b) target entity, (c) transaction type (lease fee, distribution fee, fulfillment fee, management fee, freight), (d) pricing method, (e) rate/amount (per sqm, per order, per pallet, per kg, percentage of revenue), (f) cost center allocations for both entities, (g) GL accounts for IC AP/AR, (h) effective date. System auto-generates IC invoices based on these rules (W14). | IT ERP Administrator | Corporate Controller | 1 hour |
| 4 | **Validation & Testing**: Corporate Controller runs test IC transactions to verify: (a) correct IC invoice generation, (b) correct GL posting in both entities, (c) correct elimination during consolidation (W234), (d) correct cost center allocation. Tax Manager reviews the test results for arm's-length compliance. | Corporate Controller / Tax Manager | CFO | 1 hour |
| 5 | **Approval**: CFO approves the IC pricing rule, confirming arm's-length compliance and alignment with the company's transfer pricing policy (W235). Rules above PHP 10M annual impact require Board approval. | CFO | Board (if > PHP 10M) | 30 min |
| 6 | **Annual Transfer Pricing Review**: Annually, Tax Manager and Corporate Controller review all active IC pricing rules: (a) verify rates against current market benchmarks, (b) update cost-plus calculations with current cost data, (c) confirm BIR compliance documentation is current, (d) assess whether any new IC flows need pricing rules. Updated rules are submitted for CFO approval. | Tax Manager / Corporate Controller | CFO | 8 hours/year |

### System Touchpoints
- ERP Intercompany Module (IC pricing rule engine)
- GL Module (IC AP/AR accounts, elimination entries)
- Cost Center Module (dual-entity cost allocation)
- Consolidation Module (IC elimination — W234)
- Tax Compliance Module (transfer pricing documentation — W235)
- AP/AR Module (auto-generated IC invoices — W14)

### Pain Points / Risks
- IC pricing rules not updated after cost structure changes, causing profit shifting to the wrong entity and BIR audit exposure.
- Missing IC pricing rules for new transaction types, causing unreconciled IC balances at month-end.
- Transfer pricing not at arm's length, triggering BIR assessment and penalties.
- IC invoice auto-generation configured with wrong rates, requiring manual correction during IC reconciliation (W14.4–5).
- Inconsistent markup percentages across similar IC flows, creating audit red flags.

### Staffing Implication
Absorbed by Finance and Tax teams. New IC rules ~4 hours each. Annual review ~8 hours across Tax Manager and Corporate Controller.

### Time Estimate
**Total**: ~5 hours per new IC pricing rule; ~8 hours annual comprehensive review.

---

## W306. Seasonal Calendar & Event Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Annual seasonal planning cycle, new event identification (e.g., government infrastructure stimulus drive), or promotional calendar change |
| **Frequency** | Annual comprehensive calendar setup; quarterly updates; ad-hoc for emerging events |
| **Owner** | VP Merchandising |
| **Participants** | Merchandise Planner, Marketing Campaign Manager, Supply Chain Planner, Category Manager, Master Data Analyst |
| **Volume** | ~12–15 seasonal periods/year; ~6 major sale events; ~12 monthly hot deal windows; ~10–15 regional events (fiestas, local construction booms) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Calendar Event Creation**: Merchandise Planner creates or updates a seasonal calendar event in the ERP. Each event specifies: event name (e.g., "Summer Dry Season 2027", "Ber-Months Home Improvement", "Typhoon Season Prep"), start/end dates, affected categories, geographic scope (national, regional, store-specific), expected demand multiplier (1.2x, 1.5x, 2.0x normal), and associated promotional campaigns (linked to W300). | Merchandise Planner | — | 15 min |
| 2 | **Historical Calibration**: Merchandise Planner calibrates the demand multiplier using historical sales data from the same event in previous years. System calculates: (a) actual vs. planned uplift, (b) category-level demand patterns, (c) regional variations, (d) out-of-stock incidents during the previous event. Calibration factors are stored with the event master for forecast model training (W31). | Merchandise Planner | — | 30 min |
| 3 | **Supply Chain Parameter Linkage**: Supply Chain Planner links the event to planning parameters: (a) pre-event stock build timeline (weeks of cover required), (b) safety stock multiplier during event, (c) supplier lead time adjustments (import PO cutoff dates), (d) DC capacity reservations (cross-dock space for seasonal surge). These parameters automatically adjust replenishment and demand forecast engines during the event window. | Supply Chain Planner | — | 20 min |
| 4 | **Promotional Calendar Sync**: Marketing Campaign Manager links the event to promotional campaigns (W83, W300). System validates that promotional rules are configured for the event window and that there are no gaps (event periods without active promotions) or overlaps (conflicting promotions in the same period for the same category). | Marketing Campaign Manager | — | 15 min |
| 5 | **Approval**: VP Merchandising approves the seasonal calendar, confirming completeness and alignment with the overall merchandising strategy. Supply Chain VP confirms that supply chain parameters are achievable given current supplier and DC capacity. | VP Merchandising / VP Supply Chain | VP Merchandising | 30 min |
| 6 | **System Activation**: Master Data Analyst activates the calendar. System automatically: (a) adjusts demand forecast multipliers (W31) for the event window, (b) triggers seasonal buy planning alerts (W32) at the pre-defined lead time before the event, (c) adjusts safety stock parameters in the replenishment engine (SCP-002), (d) schedules seasonal merchandise transition tasks (W264), (e) notifies Category Managers of upcoming seasonal shifts. | Master Data Analyst / System | — | 30 min |
| 7 | **Post-Event Review & Learning**: After each event, Merchandise Planner captures actual performance: actual vs. planned demand multiplier, category performance, stockout incidents, overstock carry-forward, and promotional ROI. These learnings are stored with the event master and used to calibrate the next year's event parameters. | Merchandise Planner | VP Merchandising | 2 hours/event |

### System Touchpoints
- ERP Seasonal Calendar / Event Master Module
- Demand Forecasting Engine (W31 — event-driven forecast adjustment)
- Seasonal Buy Planning (W32 — pre-event procurement triggers)
- Replenishment Engine (SCP-002 — safety stock adjustment)
- Promotional Rule Engine (W300 — event-linked promotions)
- Seasonal Merchandise Transition (W264 — display rotation triggers)
- BI/Analytics (event-level performance tracking)

### Pain Points / Risks
- Calendar events not linked to demand forecasting, causing the system to plan based on normal demand during peak periods.
- Demand multipliers based on gut feel rather than historical calibration, leading to over/under-buying.
- Seasonal stock build alerts triggered too late (after import PO cutoff dates), causing stockouts during the event.
- Post-event learnings not captured, causing the same forecasting errors to repeat year after year.
- Regional events (fiestas, local construction booms) not represented in the national calendar, causing localized stockouts.
- Event end dates not triggering seasonal markdown rules, leaving seasonal inventory unsold after the event window.

### Staffing Implication
Absorbed by Merchandising, Supply Chain, and Marketing teams. Annual calendar setup ~8 hours. Per-event calibration and review ~2.5 hours. Quarterly updates ~4 hours.

### Time Estimate
**Total**: ~8 hours annual calendar setup; ~2.5 hours per event calibration and review; ~4 hours quarterly updates.

---

## W307. Currency & Exchange Rate Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Daily exchange rate update cycle, new currency activation (e.g., new import sourcing country), central bank rate change, month-end rate lock for revaluation, or FX hedging rate recording |
| **Frequency** | Daily rate updates (automated + manual override); ~2–3 new currency activations/year; monthly rate review |
| **Owner** | Corporate Controller |
| **Participants** | Treasury Manager, Tax Manager, IT ERP Administrator, Master Data Analyst |
| **Volume** | ~15 active currencies; 1 daily rate update (PHP base); ~3–5 rate types per currency |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Daily Rate Import**: System automatically imports daily reference exchange rates from the BSP (Bangko Sentral ng Pilipmas) or a subscribed rate provider (e.g., Reuters, Bloomberg) via API integration. Rates are stored with: effective date, currency pair, rate type (spot, buying, selling, BSP reference), and source. If API fails, Master Data Analyst manually enters the BSP published rate before 10:00 AM. | System / Master Data Analyst | Corporate Controller | 5 min (manual fallback) |
| 2 | **Rate Type Governance**: For each currency, the ERP maintains multiple rate types: (a) **Spot rate** — for real-time transaction recording (import POs, vendor invoices), (b) **Monthly average rate** — for month-end WAC recalculation of imported inventory, (c) **Customs rate** — BOC-prescribed rate for duty/tax computation, (d) **Hedged/contract rate** — from FX forward contracts (W80), used for hedged payable settlement, (e) **Month-end closing rate** — for month-end FX revaluation (W9A.5a). IT ERP Administrator configures which rate type is used by each module (AP, Inventory, GL Revaluation, Treasury). | IT ERP Administrator | Corporate Controller | 30 min (one-time config) |
| 3 | **Rate Validation & Override**: Corporate Controller reviews the daily imported rates at 10:00 AM. If the system-imported rate deviates > 2% from the prior day's rate, an alert is triggered for manual verification (prevents erroneous API rates from posting). Controller may override the rate with a verified rate, which requires a justification note logged in the audit trail. | Corporate Controller | — | 10 min/day |
| 4 | **Month-End Rate Lock**: On the last business day of the month, Corporate Controller locks the month-end exchange rates in the ERP. This triggers: (a) FX revaluation of all open foreign-currency AP/AR balances (W9A.5a), (b) WAC recalculation for imported inventory using the monthly average rate, (c) Unrealized FX gain/loss posting to the GL. Locked rates cannot be changed for closed periods. | Corporate Controller | CFO | 15 min/month |
| 5 | **New Currency Activation**: When Procurement sources from a new country (e.g., sourcing from Vietnam in VND), Master Data Analyst requests activation of the new currency. IT ERP Administrator configures: currency code (ISO 4217), decimal precision, GL accounts for FX gains/losses, rounding rules, and linked bank account details. Tax Manager verifies that the BIR-required exchange rate source for the new currency is available. | Master Data Analyst / IT ERP Administrator | Corporate Controller | 30 min |
| 6 | **Hedged Rate Integration**: Treasury Manager records the contracted forward rate when an FX forward contract is executed (W80). System stores the hedged rate alongside the spot rate. AP module uses the hedged rate (not the spot rate) when settling import invoices covered by a forward contract, ensuring no FX variance on hedged payables. | Treasury Manager | — | 5 min/contract |
| 7 | **Quarterly Rate Audit**: Quarterly, Corporate Controller audits exchange rate accuracy: (a) compares ERP-stored rates against BSP published rates for each business day in the quarter, (b) verifies that the correct rate type was applied to each transaction category, (c) investigates any rate overrides and their justification, (d) confirms hedged rates match forward contract confirmations. Discrepancies are documented and corrected. | Corporate Controller | CFO | 2 hours/quarter |

### System Touchpoints
- ERP Currency Master / Exchange Rate Table
- AP Module (invoice rate at PO date vs. payment date)
- AR Module (customer invoice rate)
- Inventory Module (WAC recalculation for imported items)
- GL Module (FX revaluation, unrealized FX gain/loss posting)
- Treasury Module (cash position in multi-currency, W233)
- FX Hedging Module (W80 — forward rate storage)
- Import PO Module (W2B — PO rate, customs rate)
- BSP / Rate Provider API Integration

### Pain Points / Risks
- Wrong exchange rate applied to a large import PO (e.g., stale rate from prior week) causing material landed cost error and WAC distortion across thousands of units.
- API rate feed failure going unnoticed, causing zero or null rates to be used in transaction processing.
- Month-end rate lock not performed before FX revaluation run, causing the revaluation to use next-day rates.
- Hedged rates not linked to the correct AP invoices, causing FX gains/losses on hedged transactions (defeating the purpose of hedging).
- Rounding differences between customs-declared PHP amounts and ERP-converted PHP amounts, causing BIR reconciliation discrepancies.

### Staffing Implication
Daily rate review ~10 min by Corporate Controller. Monthly rate lock ~15 min. Quarterly audit ~2 hours. New currency activation ~30 min (rare). Absorbed by existing Finance team.

### Time Estimate
**Total**: ~10 min/day for rate review; ~15 min/month for rate lock; ~2 hours/quarter for audit; ~30 min per new currency activation.

---

## W308. Fiscal Calendar & Posting Period Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New fiscal year setup, new entity creation requiring fiscal calendar, BIR CAS registration requiring document numbering series, or period control policy change |
| **Frequency** | Annual fiscal year setup (December for following year); ad-hoc for new entities (~1/year during expansion phase) |
| **Owner** | Corporate Controller |
| **Participants** | Finance Controller, IT ERP Administrator, Tax Manager, Master Data Analyst |
| **Volume** | 5 entity fiscal calendars; 12 monthly posting periods + special periods (year-end adjustment, audit); ~50+ document numbering series per entity |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Fiscal Year Variant Definition**: IT ERP Administrator defines the fiscal year variant for each entity. All 5 entities use the calendar year (Jan–Dec) aligned with the BIR tax year (A5.5). The variant specifies: 12 regular posting periods, 2 special periods (Period 13: year-end adjustments; Period 14: audit adjustments), and the period-end close deadline (5 working days — A5.5). | IT ERP Administrator | Corporate Controller | 30 min/entity |
| 2 | **Posting Period Control Configuration**: Corporate Controller defines the period control policy: (a) which user roles can post to open periods (e.g., AP Clerks post to current period only; Finance Controllers can reopen prior periods with approval), (b) period opening/closing schedule (current month open, prior month closed after W9A completion, special periods open only during year-end close W9B), (c) document date vs. posting date rules (allow back-dating within the open period but not into closed periods). IT ERP Administrator configures these rules in the ERP. | Corporate Controller / IT ERP Administrator | CFO | 1 hour |
| 3 | **Document Numbering Series Setup**: For BIR CAS compliance (W54A, W216), IT ERP Administrator configures sequential document numbering series per entity per document type: (a) Sales Invoice / Official Receipt (per POS terminal per location — BIR requires no gaps), (b) Purchase Order, (c) AP Voucher / Payment, (d) Journal Entry (manual), (e) Debit Note / Credit Note, (f) Delivery Receipt. Each series specifies: prefix (entity code + document type + year), starting number, and reset rule (annual reset on Jan 1 per BIR requirements). System enforces strict sequential numbering — no gaps, no deletions (only reversals). | IT ERP Administrator | Corporate Controller | 2 hours/entity |
| 4 | **Intercompany Period Alignment**: Corporate Controller verifies that all 5 entities' posting periods are aligned. IC transactions (W14) require both source and target entities to have the same period open. If any entity's period is closed while another is open, IC auto-invoicing will fail. System is configured to prevent period closure if unreconciled IC transactions exist. | Corporate Controller | — | 15 min |
| 5 | **Year-End Period Transition**: During December, Corporate Controller prepares for the year-end transition: (a) confirms Period 13 (adjustments) and Period 14 (audit) are configured, (b) sets the prior-year period reopening policy (who can reopen and until when — typically until external audit completion in Q2), (c) archives completed fiscal year's period log, (d) resets annual document numbering series to start from 1 on January 1 per BIR requirements. | Corporate Controller | CFO | 1 hour/year |
| 6 | **New Entity Calendar Setup**: When a new legal entity is created (e.g., during corporate restructuring), Master Data Analyst sets up the fiscal calendar: fiscal year variant (aligned to group calendar), posting periods, document numbering series (registered with BIR — W54A), and period control rules (matching group policy). Tax Manager confirms BIR registration of the new numbering series before activation. | Master Data Analyst / Tax Manager | Corporate Controller | 2 hours/entity |
| 7 | **Period Control Audit**: Semi-annually, Internal Audit (W121) reviews period control compliance: (a) verify no postings to closed periods without proper approval, (b) verify document numbering sequences have no gaps (BIR compliance), (c) verify IC period alignment was maintained during all monthly closes, (d) verify special period access was restricted to authorized Finance Controllers. | Internal Auditor | Corporate Controller | 4 hours/semi-annually |

### System Touchpoints
- ERP Fiscal Calendar / Posting Period Module
- GL Module (period-based posting, year-end close — W9A, W9B)
- AP/AR Modules (document numbering, period-based processing)
- POS Module (sales invoice numbering — BIR CAS per location)
- Intercompany Module (IC period alignment — W14)
- Audit Trail Engine (period control change log)
- BIR CAS Compliance Module (W54A — sequential numbering verification)

### Pain Points / Risks
- Gaps in sales invoice numbering triggering BIR assessment during CAS audit (BIR requires continuous sequential numbering with no breaks).
- Entity period closed prematurely while IC auto-invoices are still generating, causing failed IC settlement and month-end reconciliation delays.
- Users posting to wrong periods (e.g., December transactions posted in January) causing tax period misalignment and BIR filing errors.
- Prior-year reopening without proper authorization, compromising audit integrity.
- Document numbering series not registered with BIR before first use, causing compliance violation.
- Annual numbering reset not executed on Jan 1, causing the new year to continue old numbering sequences (BIR requires new series per year).

### Staffing Implication
Annual fiscal year setup ~2 hours across 5 entities. Year-end transition ~1 hour. New entity setup ~2 hours. Absorbed by Corporate Controller and IT ERP Administrator.

### Time Estimate
**Total**: ~2 hours annual fiscal year setup; ~1 hour year-end transition; ~2 hours per new entity setup; ~4 hours semi-annual audit.

---

## W309. Bank & Banking Partner Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New bank account opening, new banking partner relationship, bank branch closure/merger, store opening requiring deposit account linkage, or e-wallet/digital payment partner onboarding |
| **Frequency** | ~5–10 bank account additions/year (new store openings); ~2–3 banking partner changes/year; ~50 store deposit account linkages/year during expansion |
| **Owner** | Treasury Manager |
| **Participants** | Finance Controller, AP Supervisor, Payroll Manager, IT ERP Administrator, Master Data Analyst |
| **Volume** | ~15–20 active bank accounts across 5 entities and 3 banking partners (BDO, BPI, Metrobank); ~200 store deposit points; ~5 e-wallet settlement accounts |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Bank Master Record Creation**: Treasury Manager requests creation of a new bank master record when a new banking relationship is established. Request specifies: bank name, SWIFT/BIC code, Philippine bank code (BRSTN — Bank Routing Symbol Transit Number), clearing code (PhilPaSS), and branch details. Master Data Analyst creates the bank master in the ERP. | Treasury Manager / Master Data Analyst | Finance Controller | 15 min |
| 2 | **Entity Bank Account Setup**: Treasury Manager requests creation of a new bank account in the ERP. Request specifies: entity (one of 5), bank, branch, account number, account type (operating, payroll, escrow, LC, float, deposit), currency (PHP/USD), GL account mapping (bank clearing account, bank sub-ledger), authorized signatories, and online banking access details. Finance Controller approves the GL mapping. IT ERP Administrator configures the bank account and links it to the relevant ERP modules (AP payment, payroll disbursement, treasury cash position, AR collection). | Treasury Manager / IT ERP Administrator | Finance Controller | 30 min |
| 3 | **Store Deposit Account Linkage**: For each of the 200 stores, Master Data Analyst links the store location (W254) to its designated bank deposit point. Configuration specifies: store code, nearest bank branch, deposit account number, deposit type (cash, check, e-wallet settlement), and CIT armored car deposit schedule (W174). This linkage drives the automatic store-level cash reconciliation in W5F and the bank deposit auto-matching in W30.4. | Master Data Analyst | Treasury Manager | 10 min/store |
| 4 | **E-Wallet & Digital Payment Partner Configuration**: For e-wallet settlement (GCash, Maya, GrabPay, ShopeePay — FIN-032), IT ERP Administrator configures: partner name, settlement account, settlement frequency (T+1, T+2), MDR rate per partner, reconciliation mapping (settlement file → POS transaction matching), and chargeback dispute workflow linkage. | IT ERP Administrator | Treasury Manager | 30 min/partner |
| 5 | **Payment File Format Configuration**: IT ERP Administrator configures the bank-specific payment file formats for AP disbursements (BDO, BPI, Metrobank — each uses different file layouts). Formats include: payroll bank credit file (HR-012), AP vendor payment file (W7), LC payment instruction (W232), and intercompany settlement file (W14). Treasury Manager validates the format by running a test payment file before go-live. | IT ERP Administrator / Treasury Manager | Finance Controller | 1 hour/bank |
| 6 | **Bank Detail Change Governance**: When a bank account needs to be modified (e.g., account closure, branch merger, signatory change), Treasury Manager initiates a change request. For entity-level bank accounts: Finance Controller approves. For vendor bank detail changes: the existing 48-hour cooling-off period (W287 Step 5) applies. All changes are logged in an immutable audit trail with old value, new value, approver, and effective date. | Treasury Manager | Finance Controller | 15 min |
| 7 | **Periodic Bank Master Review**: Annually, Treasury Manager reviews all bank master records: (a) verifies account status with actual bank statements, (b) confirms authorized signatories are current, (c) validates that e-wallet MDR rates match current contracts, (d) confirms payment file formats are compatible with any bank system updates, (e) deactivates closed/unused accounts. | Treasury Manager | Finance Controller | 4 hours/year |

### System Touchpoints
- ERP Bank Master Module
- Treasury Module (cash position, bank reconciliation — W89)
- AP Module (payment file generation — W7)
- Payroll Module (bank credit file — HR-012)
- AR Module (customer payment collection, e-wallet settlement — W261)
- CIT / Armored Car Module (store deposit scheduling — W174)
- Store EOD Module (cash reconciliation — W5F)
- Payment Gateway Integration (e-wallet settlement file import)

### Pain Points / Risks
- Incorrect GL account mapping on a new bank account causing AP payments to post to the wrong cash account, requiring manual journal corrections.
- Store deposit account linked to the wrong bank branch, causing deposit rejection and cash reconciliation failure.
- E-wallet settlement frequency misconfigured (T+1 instead of T+2), causing settlement matching failures and unreconciled e-wallet balances.
- Bank payment file format not updated after a bank system upgrade, causing bulk payment file rejection and delayed vendor payments.
- Unauthorized signatory changes on entity bank accounts creating internal control failures.
- Dormant bank accounts not deactivated, cluttering the cash position report and complicating bank reconciliation.

### Staffing Implication
Bank account setup ~30 min per account. Store deposit linkage ~10 min per store (batch during new store openings). E-wallet partner config ~30 min. Annual review ~4 hours. Absorbed by Treasury team and IT ERP Administrator.

### Time Estimate
**Total**: ~30 minutes per bank account setup; ~10 minutes per store deposit linkage; ~1 hour per bank payment format; ~4 hours annual review.

---

## W310. Address & Geographic Hierarchy Master Governance (Philippine-Specific)

| Field | Detail |
|---|---|
| **Trigger** | New Philippine geographic data release (PSA/Philippine Statistics Authority), new barangay/municipality creation by government, LGU tax rate change, store opening in a new location requiring full address hierarchy setup, or periodic data quality review |
| **Frequency** | ~20–30 geographic updates/year (new barangays, municipality conversions, LGU rate changes); quarterly data quality review; major update during census years (every 5 years) |
| **Owner** | Master Data Manager |
| **Participants** | Finance Controller, Tax Manager, Supply Chain Planner, IT ERP Administrator, Master Data Analyst |
| **Volume** | ~42,000+ barangays; ~1,500 municipalities/cities; ~82 provinces; 17 regions; 3 island groups (Luzon, Visayas, Mindanao); ~200 store-linked locations; ~4 DC-linked locations |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Hierarchy Structure Definition**: Master Data Analyst defines the Philippine geographic hierarchy in the ERP: Island Group → Region → Province → Municipality/City → Barangay. Each level has: official PSA code (Philippine Standard Geographic Code — PSGC), official name, parent relationship, and geographic coordinates (centroid for distance/routing calculations). The hierarchy is stored as a single tree structure used across all modules (store locations, customer addresses, vendor addresses, DC coverage areas, LGU tax jurisdictions). | Master Data Analyst | Master Data Manager | 8 hours (initial setup) |
| 2 | **LGU Tax Jurisdiction Mapping**: Tax Manager maps each municipality/city to its local business tax jurisdiction. Configuration specifies: LGU code, local business tax rate (percentage of gross receipts), tax filing frequency (annual, quarterly), and LGU contact details. This drives the per-location LBT computation in W9A and the real property tax computation in W119. For stores with locations spanning multiple barangays (e.g., large stores), the primary barangay is designated for tax purposes. | Tax Manager | Finance Controller | 20 min/LGU |
| 3 | **DC Coverage Area Assignment**: Supply Chain Planner defines the geographic coverage area for each of the 4 DCs. Each municipality/city is assigned to a primary DC (W254) based on: (a) road distance, (b) inter-island ferry route availability, (c) historical delivery time data. This drives replenishment lead time calculation (SCP-002) and delivery routing (W304). Coverage areas are reviewed when new DCs are opened or ferry routes change. | Supply Chain Planner | VP Supply Chain | 2 hours (initial); 30 min/update |
| 4 | **Geographic Data Update**: When PSA publishes new geographic data (new barangays created, municipality conversions, province reorganizations), Master Data Analyst updates the hierarchy: (a) adds new nodes with PSGC codes, (b) deactivates obsolete nodes (with address migration for affected records), (c) updates parent relationships for reorganized areas. System validates that no orphaned nodes exist after the update. | Master Data Analyst | Master Data Manager | 30 min/batch |
| 5 | **Customer/Vendor Address Standardization**: Master Data Analyst configures the ERP to enforce address standardization during data entry: (a) barangay, city/municipality, province, and region are selected from the geographic master (dropdown) rather than free-text, (b) system auto-populates the postal code (ZIP) based on the selected municipality/city, (c) system validates that the selected barangay belongs to the selected city, which belongs to the selected province. This applies to customer enrollment (W17, W253), vendor onboarding (W36, W287), and store/DC locations (W254). | Master Data Analyst | Master Data Manager | 4 hours (one-time config) |
| 6 | **BIR Registration Location Linkage**: Tax Manager links each geographic area to its corresponding BIR Revenue District Office (RDO). Each store location (W254) is assigned to an RDO, which determines the BIR filing jurisdiction for that location. This drives: BIR CAS registration per location (W54A), VAT return filing location, and withholding tax remittance jurisdiction. System validates that the RDO assignment is consistent with the province/region in the geographic hierarchy. | Tax Manager | Finance Controller | 10 min/location |
| 7 | **Quarterly Data Quality Review**: Master Data Analyst runs a quarterly geographic data quality check: (a) completeness — all stores, DCs, vendors, and customers have a valid full-address hierarchy (no missing barangay, city, or province), (b) consistency — no addresses with barangay/province mismatches, (c) currency — all PSGC codes match the latest PSA publication, (d) coverage — all municipalities with a BuildRight store have a DC coverage assignment. Exceptions are routed to the relevant Data Steward for remediation (W291). | Master Data Analyst | Master Data Manager | 2 hours/quarter |

### System Touchpoints
- ERP Geographic / Address Master Module
- Location Master (W254 — store/DC address linkage)
- Customer Master (W253 — customer address standardization)
- Vendor Master (W287 — vendor address standardization)
- Tax Module (LGU tax jurisdiction mapping — W119, W9A)
- BIR Compliance Module (RDO assignment — W54A, W260)
- Supply Chain Module (DC coverage area — SCP-002, W304)
- Ecommerce Platform (customer address validation at checkout)
- PSA / PSGC Data Integration

### Pain Points / Risks
- Free-text addresses without geographic hierarchy linkage causing undeliverable shipments, failed LGU tax computation, and fragmented customer analytics.
- New barangays created by government not added to the geographic master, causing customer/vendor address entry failures for affected areas.
- DC coverage areas not updated when new roads or ferry routes reduce delivery times, causing inflated lead times and overstock at stores.
- BIR RDO assignment missing for a store location, causing VAT returns to be filed in the wrong jurisdiction.
- Province/region mismatch on vendor addresses causing incorrect LGU tax withholding.
- Address standardization not enforced at POS (e.g., customer provides "Makati" but system needs the specific barangay), causing data quality degradation in the customer master.

### Staffing Implication
Initial hierarchy setup ~8 hours (one-time). Geographic updates ~30 min/batch, ~20–30 times/year. Quarterly quality review ~2 hours. Absorbed by existing MDM team with Tax and Supply Chain input.

### Time Estimate
**Total**: ~8 hours initial setup; ~30 minutes per geographic update batch; ~2 hours quarterly quality review.

---

## W311. Barcode, GTIN & Item Identification Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New SKU creation requiring barcode assignment, GS1 company prefix management, custom barcode generation (paint mixing, lumber cutting), vendor barcode registration, or periodic barcode quality audit |
| **Frequency** | Daily (~50–100 new SKU barcodes/week); ~5 custom barcode range extensions/year; annual GS1 registration renewal; quarterly barcode quality audit |
| **Owner** | Master Data Manager |
| **Participants** | Category Manager, IT ERP Administrator, POS Administrator, Master Data Analyst |
| **Volume** | ~35,000 active item barcodes; ~500–800 new barcodes/month; ~15,000 multi-barcode items (case, inner, unit); ~20 custom barcode ranges (paint, lumber, services) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **GS1 Company Prefix Management**: Master Data Manager manages the GS1 company prefix registration. BuildRight holds a GS1 prefix for its private label items (W129). Master Data Analyst maintains: prefix number, allocated capacity (number of available GTINs), annual renewal date, and GS1 Philippines membership status. When capacity is approaching exhaustion (> 80% used), Master Data Manager requests an additional prefix allocation from GS1. For vendor-assigned barcodes, the system stores the vendor's GS1 prefix as part of the vendor master (W287). | Master Data Analyst / Master Data Manager | — | 30 min/year |
| 2 | **Barcode Assignment at SKU Creation**: During item master creation (W252), Master Data Analyst assigns the primary barcode to each new SKU: (a) for vendor-branded items — the vendor's GTIN/EAN/UPC is recorded as-is (verified against the physical product packaging), (b) for private label items — a GTIN is generated from BuildRight's GS1 prefix, (c) for custom items (paint base + colorant combinations) — a custom barcode range is assigned. System validates: (i) no duplicate barcodes across the item master (including inactive items to prevent re-activation conflicts), (ii) check digit validation for EAN-13, UPC-A, and ITF-14 formats, (iii) barcode format consistency within the same category. | Master Data Analyst | — | 5 min/SKU |
| 3 | **Multi-Level Barcode Configuration**: For items sold in multiple packaging levels, Master Data Analyst configures the barcode hierarchy: (a) **Unit/EACH barcode** — the barcode scanned at POS for single-unit sale (EAN-13 or UPC-A), (b) **Inner pack barcode** — for items sold in inner packs (e.g., box of 10 screws), (c) **Case/pallet barcode** — for receiving and warehouse putaway (ITF-14 or GS1-128). System maps the hierarchy so that scanning a case barcode at receiving creates the correct unit quantity in inventory. This drives the UOM conversion (W294) and receiving workflow (W3). | Master Data Analyst | — | 10 min/item |
| 4 | **Custom Barcode Range Governance**: For custom-processing items that generate unique SKUs at POS, IT ERP Administrator manages dedicated barcode ranges: (a) **Paint mixing** — custom barcode prefix for tinted paint (links to base paint SKU + colorant formula per W168), (b) **Lumber cutting** — custom barcode for cut-to-size lumber (links to original SKU + cutting dimensions per W169), (c) **Service items** — barcode for service/rental items that don't have physical packaging. Each custom range has: prefix, next sequential number, format rules, and POS integration configuration. POS Administrator verifies that custom barcodes scan correctly at all POS terminals. | IT ERP Administrator / POS Administrator | Master Data Manager | 1 hour/range |
| 5 | **Vendor Barcode Registration & Verification**: When vendors submit new item requests via the Vendor Portal (W252 Step 1), system validates the vendor-provided GTIN: (a) checks that the GTIN prefix matches the vendor's registered GS1 prefix (from W287), (b) verifies the check digit, (c) cross-references the GS1 Global Product Database (if available) to confirm the item description matches the GTIN record. Invalid or unverifiable GTINs are flagged for manual review. | System / Master Data Analyst | — | 5 min/exception |
| 6 | **Barcode-to-Channel Sync**: Master Data Analyst ensures that barcodes are correctly synced to all downstream channels: (a) POS — all unit-level barcodes available for scanning at 1,000 terminals, (b) ecommerce — GTINs included in product catalog feeds for Google Shopping and marketplace integrations (W180), (c) WMS — case/pallet barcodes configured for RF scanning at 4 DCs, (d) vendor portal — vendor can view their assigned barcodes for item verification. IT ERP Administrator validates the sync by spot-checking barcode readability across channels after each major item master update. | Master Data Analyst / IT ERP Administrator | — | 1 hour/month |
| 7 | **Quarterly Barcode Quality Audit**: Master Data Analyst runs a quarterly barcode quality audit: (a) **Duplicate check** — scans for any duplicate barcodes across the item master (catching any missed during creation), (b) **Dead barcode cleanup** — identifies barcodes assigned to discontinued items (W68) that are inactive for > 12 months and flags them for reclamation (not reassignment to prevent confusion), (c) **Missing barcode report** — items without a primary barcode (blocking POS scanning), (d) **Physical verification** — samples 100 physical items in a DC and verifies that the barcode on the packaging matches the ERP record. Discrepancies are escalated for immediate correction. | Master Data Analyst | Master Data Manager | 4 hours/quarter |

### System Touchpoints
- ERP Item Master Module (barcode fields per SKU)
- GS1 Database Integration (vendor GTIN verification)
- POS Module (barcode scanning — POS-003)
- WMS Module (RF scanning — WMS-001)
- Ecommerce Platform (GTIN in product feeds — ECOM-009)
- Marketplace Integration (GTIN sync — W180)
- Vendor Portal (vendor barcode submission — W252)
- Custom Processing Modules (paint mixing W168, lumber cutting W169)
- Barcode Label Printing System (shelf labels, shipping labels — WMS-007)

### Pain Points / Risks
- Duplicate barcodes (two different items with the same GTIN) causing wrong items scanned at POS, incorrect inventory deduction, and customer complaints.
- Vendor GTIN not verified against the vendor's GS1 prefix, allowing fraudulent or incorrect barcodes to enter the system.
- Missing multi-level barcodes causing receiving staff to scan unit barcodes instead of case barcodes, resulting in incorrect receipt quantities and 3-way match failures.
- Custom barcode ranges running out of capacity during peak season, blocking paint mixing or lumber cutting operations at POS.
- Discontinued item barcodes reassigned to new items, causing phantom inventory transactions from old barcode labels still in circulation.
- Barcode format inconsistency (mixing EAN-13 and UPC-A within the same category) causing POS scanning failures for specific symbologies.
- Ecommerce catalog missing GTINs, causing Google Shopping feed rejection and marketplace listing failures.

### Staffing Implication
Barcode assignment is part of the SKU creation process (W252) — ~5 min per SKU handled by existing Master Data Analysts. Custom range management ~1 hour per range (rare). Quarterly audit ~4 hours. GS1 prefix management ~30 min/year.

### Time Estimate
**Total**: ~5 minutes per SKU barcode assignment (embedded in W252); ~1 hour per custom barcode range; ~4 hours quarterly quality audit.

---

## W312. Replenishment & Planning Parameter Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New SKU activation requiring planning parameters, seasonal parameter adjustment, new store opening requiring location-specific parameters, or periodic parameter review cycle |
| **Frequency** | Continuous (new SKU/store setup); Quarterly parameter review; Annual comprehensive calibration |
| **Owner** | VP Supply Chain |
| **Participants** | Supply Chain Planner, Category Manager, Master Data Analyst, Demand Planner |
| **Volume** | ~35,000 active SKUs × 204 locations = ~7.2M SKU-location parameter sets; ~500–800 new sets/month; ~5,000–10,000 parameter changes/quarter |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Parameter Request**: Supply Chain Planner or Demand Planner requests a new parameter set or modification. For new SKUs, request follows item master activation (W252). For new stores, follows location activation (W254). Request specifies: item, location, reorder point (ROP), safety stock (units and days of cover), economic order quantity (EOQ), lead time (vendor + transit), minimum order quantity, review cycle (continuous, weekly, bi-weekly), and ABC classification tier. | Supply Chain Planner | — | 10 min |
| 2 | **Parameter Calculation & Validation**: Demand Planner validates the proposed parameters using: (a) historical demand data (average daily sales, demand variability / coefficient of variation), (b) lead time variability (vendor on-time delivery % from W44, transit time variance from W304), (c) target service level by ABC tier (A-items: 98%, B-items: 95%, C-items: 90%). System calculates the recommended ROP = (average daily demand × lead time) + safety stock, where safety stock = Z-score × √(lead time × demand variance + demand² × lead time variance). Demand Planner reviews the system recommendation against the proposed values. | Demand Planner | — | 15 min |
| 3 | **Channel-Specific Parameter Override**: For items sold across multiple channels (POS, ecommerce, marketplace), Supply Chain Planner configures channel-specific allocation parameters: (a) reserved safety stock per channel (linked to W105 — multi-channel inventory allocation), (b) allocation priority (e.g., BOPIS orders take priority over marketplace), (c) reorder trigger split by channel demand ratio. For BOPIS items, planner sets the in-store reservation floor (minimum units to keep available for online pickup). | Supply Chain Planner | — | 10 min |
| 4 | **Seasonal & Event Parameter Adjustment**: For seasonal items or items linked to events (W306), Demand Planner sets time-bound parameter overrides: (a) pre-event safety stock multiplier (e.g., 2.0× for typhoon season prep items), (b) event window ROP adjustment, (c) post-event ramp-down rule (gradual return to normal parameters over 4 weeks). System stores the override with effective dates, automatically switching between normal and seasonal parameters. | Demand Planner | — | 10 min |
| 5 | **Approval**: For A-items (top 20% SKUs = 80% revenue), VP Supply Chain approves parameter changes exceeding ±20% from current values. For B/C-items, Supply Chain Planner has delegation authority within ±30%. Any parameter change that would increase total inventory investment by > PHP 5M requires CFO approval (linked to W26 — budget governance). | VP Supply Chain / CFO | VP Supply Chain | 10 min |
| 6 | **System Configuration**: Master Data Analyst configures the approved parameters in the ERP replenishment engine (SCP-002). System validates: (a) ROP > 0 and ≤ maximum shelf capacity at the location, (b) EOQ ≥ minimum order quantity from vendor (W287), (c) lead time ≥ transit time from route master (W304), (d) safety stock is consistent with ABC tier policy. Invalid parameters are rejected with a diagnostic message. | Master Data Analyst | VP Supply Chain | 10 min |
| 7 | **Exception Parameter Governance**: For items with non-standard replenishment rules, Master Data Analyst configures exceptions: (a) consignment items (W23) — no auto-replenishment, vendor-managed, (b) seasonal-only items — replenishment active only during event windows (W306), (c) direct-store-delivery (DSD) items (W18) — replenishment bypasses DC, linked to DSD vendor schedule, (d) non-stock/special-order items (W296) — no stocking parameters, PO-on-demand only. Exception rules are tagged in the system and excluded from standard parameter audit reports. | Master Data Analyst | — | 10 min |
| 8 | **Quarterly Parameter Review**: Quarterly, Demand Planner and Supply Chain Planner review planning parameters for the top 500 A-items (by revenue contribution): (a) compare actual vs. planned service level (fill rate, stockout frequency), (b) compare actual demand vs. forecast used for parameter calculation, (c) identify parameters that have drifted from optimal (service level below target or inventory turns below category benchmark), (d) flag locations with chronic overstock (inventory > 2× safety stock) or chronic stockout (> 3 stockout events in 90 days). Review generates a parameter change request list fed back to Step 2. | Demand Planner / Supply Chain Planner | VP Supply Chain | 8 hours/quarter |
| 9 | **Annual Comprehensive Calibration**: Annually, VP Supply Chain leads a full calibration review: (a) recalculate all 7.2M parameter sets using the latest 12-month demand history, (b) validate ABC classification tiers (W42 data feeds classification), (c) benchmark service level targets against industry standards, (d) review exception parameter rules for continued validity, (e) assess the impact of any new stores, DCs, or route changes on lead time parameters. Calibration results are submitted for CFO review (inventory investment impact) and approved by VP Supply Chain. | VP Supply Chain / Demand Planner | CFO | 40 hours/year |

### System Touchpoints
- ERP Replenishment Engine (SCP-002 — ROP/EOQ auto-trigger)
- Demand Forecasting Module (W31 — forecast feeds parameter calculation)
- ABC Classification Engine (INV-004 — tier feeds safety stock policy)
- Supply Chain Network (W254 — location master, W304 — transit time master)
- Multi-Channel Inventory Allocation (W105 — channel-specific parameters)
- Seasonal Calendar (W306 — event-driven parameter overrides)
- Vendor Performance Scorecard (W44 — lead time reliability data)
- Budget Module (W26 — inventory investment governance)

### Pain Points / Risks
- Stale parameters (not updated after demand pattern shifts) causing chronic stockouts on growing items or chronic overstock on declining items.
- Overly aggressive safety stock on C-items inflating total inventory investment by 15–20% without proportional service level improvement.
- ROP set above maximum shelf/bin capacity at small stores, triggering replenishment orders that cannot be physically received (W297 capacity conflict).
- Lead time parameters not updated after carrier route changes (W304), causing replenishment orders to arrive earlier/later than planned.
- Seasonal parameter overrides not deactivating after the event window, leaving inflated safety stock levels year-round.
- Channel allocation parameters not configured for BOPIS, causing online orders to consume store inventory needed for walk-in customers.
- Exception rules for consignment/VMI items not properly tagged, causing the system to generate auto-replenishment POs for vendor-managed stock.

### Staffing Implication
Absorbed by existing Supply Chain Planning team. New SKU/store setup ~10 min per parameter set (embedded in W252/W254 activation). Quarterly A-item review ~8 hours. Annual calibration ~40 hours (spread over 2 weeks).

### Time Estimate
**Total**: ~10 minutes per new parameter set; ~8 hours quarterly review (top 500 items); ~40 hours annual comprehensive calibration.

---

## W313. Loyalty Program Configuration & Rule Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Loyalty program redesign, new tier introduction, points earning rate change, redemption catalog update, tier qualification criteria modification, or partner co-earning rule establishment |
| **Frequency** | ~2–3 structural rule changes/year; ~10–20 redemption catalog updates/quarter; annual tier recalculation |
| **Owner** | VP Marketing (CMO) |
| **Participants** | Loyalty Manager, Finance Controller, Master Data Analyst, Marketing Campaign Manager, IT ERP Administrator |
| **Volume** | ~600,000 member accounts; 4 loyalty tiers; ~20 active earning rules; ~200 redemption SKUs/catalog items; ~5 partner co-earning agreements |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Tier Definition & Qualification Rule Governance**: Loyalty Manager defines or modifies loyalty tier structures. Each tier specifies: tier name (Bronze, Silver, Gold, Platinum), qualification criteria (minimum spend in trailing 12 months, e.g., Bronze: PHP 0, Silver: PHP 50K, Gold: PHP 150K, Platinum: PHP 500K), earning rate multiplier (e.g., Bronze: 1×, Silver: 1.5×, Gold: 2×, Platinum: 3× standard points per PHP 100), benefits (discount percentage, priority queue access, exclusive event invitations, free delivery), and downgrade grace period (months before tier is recalculated downward). Finance Controller reviews the financial impact of tier benefits on the loyalty liability (W104). | Loyalty Manager / Finance Controller | VP Marketing | 2 hours |
| 2 | **Points Earning Rule Configuration**: Loyalty Manager configures points earning rules in the ERP loyalty engine. Base rule: 1 point per PHP 100 spent. Additional rules specify: (a) category-specific earning rates (e.g., 2× points on paint category during promo), (b) channel-specific earning (in-store vs. ecommerce vs. marketplace — marketplaces may earn reduced points due to commission costs), (c) excluded items (gift cards, services, catch-weight items below minimum, employee purchases per W205), (d) bonus earning events (double-points weekends linked to W300 promotional rules), (e) partner co-earning (bank credit card partners per W149 — additional points on partner card transactions). Each rule has: earning rate, eligible SKUs/categories, eligible channels, effective dates, and maximum points per transaction cap. | Loyalty Manager | VP Marketing | 1 hour |
| 3 | **Redemption Catalog Governance**: Master Data Analyst maintains the points redemption catalog. Each catalog item specifies: redemption SKU (physical item, gift card, service voucher, partner offer), points required, cash equivalent value, redemption channel (in-store, online, both), stock availability (for physical items — linked to inventory ATP), and effective dates. Finance Controller validates that the redemption value (PHP 1.00 per point) is consistent across all catalog items and that the total redemption liability (outstanding points × redemption value) is within the accrued loyalty provision (W104). | Master Data Analyst / Finance Controller | Finance Controller | 2 hours/catalog update |
| 4 | **Tier Recalculation & Migration Rule Governance**: IT ERP Administrator configures the automatic tier recalculation engine. Rules specify: (a) recalculation frequency (monthly, based on trailing 12-month spend), (b) upgrade trigger (immediate tier upgrade when qualification threshold is crossed), (c) downgrade rule (grace period of 3 months — if spend falls below tier threshold, member retains current tier for 3 months before downgrade), (d) points expiration rule (points expire 24 months from earning date if account is inactive — no transaction in 12 months triggers expiration warning), (e) dormant account rule (W84 — accounts with no transaction in 6 months flagged for reactivation). Master Data Analyst validates the rule configuration against the loyalty program terms and conditions. | IT ERP Administrator / Master Data Analyst | Loyalty Manager | 1 hour |
| 5 | **Partner & Co-Branded Rule Integration**: Marketing Campaign Manager configures partner earning/redemption rules: (a) bank partners (W149) — additional points or cashback when using partner credit card, (b) marketplace partners (W180) — loyalty points earned on marketplace orders at reduced rate, (c) referral program (W189) — bonus points for referrer and referee on successful referral. Each partner rule has: partner code, earning/redemption rate, settlement method (points vs. cash reimbursement to partner), and reporting requirements. Loyalty Manager verifies that partner rules do not create circular earning (e.g., earning points on points redemption). | Marketing Campaign Manager / Loyalty Manager | VP Marketing | 30 min/partner |
| 6 | **Financial Liability Review**: Finance Controller reviews the loyalty program financial impact quarterly: (a) total outstanding points liability, (b) points earning rate trend (points issued per PHP 100 revenue), (c) redemption rate (% of earned points redeemed within 12 months), (d) breakage rate (% of points that expire unused — income recognition), (e) deferred revenue impact on the balance sheet. Controller recommends adjustments to earning rates or redemption values if the liability exceeds the accrued provision. | Finance Controller | CFO | 2 hours/quarter |
| 7 | **Approval & Activation**: VP Marketing approves all structural changes to loyalty rules (tier definitions, earning rate changes, new catalog items). Earning rate increases or redemption value increases require CFO approval (financial liability impact). IT ERP Administrator activates approved changes with specified effective dates. System generates a change log listing all modified rules, effective dates, and approvers. | VP Marketing / CFO | VP Marketing | 15 min |
| 8 | **Annual Program Review**: Annually, VP Marketing and Finance Controller conduct a comprehensive loyalty program review: (a) member engagement metrics (active rate, tier distribution, average points per member), (b) program ROI (incremental revenue from loyalty members vs. non-members, lift in visit frequency and basket size), (c) tier structure competitiveness (benchmarked against competitor programs), (d) financial sustainability (liability trend, breakage forecast), (e) partner program performance. Recommendations for program redesign are submitted to CEO/CFO for approval before the next calendar year. | VP Marketing / Finance Controller | CEO | 8 hours/year |

### System Touchpoints
- ERP Loyalty Points Engine (CRM-001 — earning, redemption, expiration)
- POS Module (POS-005 — loyalty scan, points earning, tier recognition)
- Ecommerce Platform (loyalty integration — online earning/redemption)
- Customer Master (W253 — member profile, tier status, points balance)
- CRM / Customer Data Platform (W156 — segmentation by tier)
- Finance Module (W104 — loyalty liability accrual, deferred revenue)
- Marketing Campaign Module (W83 — tier-targeted campaigns)
- Marketplace Integration (W180 — marketplace earning rules)
- Bank Partner Integration (W149 — co-branded earning rules)

### Pain Points / Risks
- Earning rate increase without corresponding redemption value or tier qualification adjustment, causing loyalty liability to grow faster than revenue.
- Redemption catalog items with incorrect points values (e.g., a PHP 5,000 item requiring only 500 points instead of 5,000), enabling rapid points arbitrage and financial loss.
- Tier downgrade rule too aggressive, alienating high-value customers who fall just below the threshold during a slow quarter.
- Points expiration triggering customer complaints and social media backlash if not communicated clearly (minimum 60-day warning per best practice).
- Partner co-earning rules creating double-dipping (e.g., earning partner card points AND loyalty points on the same transaction at a combined rate exceeding the margin on the purchased items).
- Redemption catalog out of sync with inventory (catalog item available for redemption but physical item out of stock at all locations), causing customer frustration.
- Tier qualification criteria not recalculating correctly after a system migration or upgrade, causing mass tier downgrades or upgrades.

### Staffing Implication
Absorbed by existing Loyalty team, Finance, and MDM team. Structural changes ~2–3/year × ~4 hours = ~8–12 hours/year. Catalog updates ~10–20/quarter × ~30 min = ~5–10 hours/quarter. Annual review ~8 hours.

### Time Estimate
**Total**: ~4 hours per structural rule change; ~30 minutes per catalog update; ~2 hours quarterly financial review; ~8 hours annual program review.

---

## W314. Planogram Template & Space Planning Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New category introduction, store format change, fixture type modification, assortment matrix update (W299), or periodic planogram template refresh cycle |
| **Frequency** | ~10–20 new/revised planogram templates/year; quarterly refresh cycle; major refresh during seasonal transitions (W264) |
| **Owner** | VP Merchandising |
| **Participants** | Category Manager, Store Operations Director, Visual Merchandising Manager, Master Data Analyst, Space Planning Analyst |
| **Volume** | ~15–20 active planogram templates per store format (small/large); ~200 store-specific planogram assignments; ~35,000 SKU-to-fixture position mappings |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Template Design Request**: Category Manager or Visual Merchandising Manager requests creation or modification of a planogram template. Request specifies: category/department affected, store format (8,000 sqm vs. 15,000 sqm), fixture types (gondola shelving, pegboard, pallet racking, bin display, endcap, power aisle stack, outdoor yard rack), target SKU count and facing requirements per SKU, and any category-specific display rules (e.g., heavy items on bottom shelves, paint mixing station adjacency to paint display, safety-compliant height limits for heavy materials). | Category Manager / Visual Merchandising Manager | — | 1 hour |
| 2 | **Space Allocation & Capacity Analysis**: Space Planning Analyst runs a space-to-sales analysis for the affected category: (a) current space allocation (% of total selling area), (b) space productivity (revenue per sqm by category), (c) optimal space allocation based on sales contribution and growth trajectory, (d) fixture capacity validation (linear meters of shelf space available vs. SKU count × facing depth). Analyst uses the assortment matrix (W299) to confirm that the template accommodates all mandatory assortment items for the relevant store cluster. | Space Planning Analyst | — | 2 hours |
| 3 | **SKU-to-Position Mapping**: Master Data Analyst maps each SKU in the assortment matrix to a specific fixture position in the planogram template. Each position specifies: fixture ID, shelf level (eye-level premium, waist-level standard, floor-level bulk), position number, number of facings, depth (units deep), and adjacent SKU placement rules (e.g., complementary items — tiles next to adhesives, paint next to brushes). System validates: (a) total SKU count matches the assortment matrix, (b) no duplicate positions, (c) facing count ≥ minimum defined in assortment matrix, (d) item dimensions (from W252) fit within fixture slot dimensions (from W297 bin master). | Master Data Analyst | — | 4 hours/template |
| 4 | **Store Cluster Template Assignment**: Master Data Analyst assigns each planogram template to the relevant store cluster (W299). Large-format stores (12,000–15,000 sqm) receive the full template; small-format stores (8,000–12,000 sqm) receive a condensed variant with reduced SKU count and facings. System validates that every store has a planogram assignment for every category (no uncovered categories). New stores receive a provisional planogram assignment at opening (W16) based on their cluster, with review at the next quarterly cycle. | Master Data Analyst | — | 30 min/cluster |
| 5 | **Fixture & Display Element Master**: Master Data Analyst maintains the fixture master data in the ERP/space planning system. Each fixture record specifies: fixture code, type (gondola, pegboard, pallet rack, endcap, island, wall unit, yard rack), dimensions (width, depth, height), shelf count, load capacity (kg per shelf), adjustable shelf flag, and compatible product categories. New fixture types require cataloging before they can be used in planogram templates. | Master Data Analyst | Master Data Manager | 15 min/fixture |
| 6 | **Approval**: VP Merchandising approves the planogram template, confirming alignment with merchandising strategy, assortment matrix (W299), and space productivity targets. Store Operations Director confirms operational feasibility (staffing for display maintenance, restock frequency, safety compliance). | VP Merchandising / Store Operations Director | VP Merchandising | 30 min |
| 7 | **Downstream Distribution**: Master Data Analyst distributes the approved planogram template to stores via the ERP/space planning system: (a) visual planogram image (PDF/digital) showing SKU placement and facing counts, (b) pick list for initial display build (list of SKUs with quantities needed to fill the planogram), (c) fixture setup instructions (assembly diagrams for new fixture types), (d) compliance photo upload requirement (W86 — stores photograph completed displays for compliance verification). Distribution triggers a task in the store's workflow queue with a completion deadline. | Master Data Analyst | — | 30 min |
| 8 | **Quarterly Planogram Performance Review**: Quarterly, Category Manager and Space Planning Analyst review planogram performance: (a) sales per linear meter by category vs. planogram target, (b) facing compliance rate (% of stores maintaining correct facings per W86), (c) out-of-shelf rate (SKUs with zero shelf stock despite backroom availability — indicating replenishment or facing issues), (d) dead space identification (positions consistently empty or filled with wrong items). Underperforming planograms are flagged for template revision. | Category Manager / Space Planning Analyst | VP Merchandising | 4 hours/quarter |

### System Touchpoints
- ERP Space Planning / Planogram Module
- Assortment Matrix (W299 — SKU list per cluster feeds planogram template)
- Item Master (W252 — item dimensions for fixture fit validation)
- Warehouse Bin Master (W297 — fixture capacity dimensions)
- Store Cluster Master (W299 — template-to-cluster assignment)
- Store Operations (W86 — planogram compliance verification)
- Visual Merchandising (W262 — promotional display setup brief)
- Seasonal Transition (W264 — seasonal planogram refresh)
- BI/Analytics (space productivity reports — revenue per sqm per category)

### Pain Points / Risks
- Planogram templates not aligned with the assortment matrix, causing stores to receive display instructions for items not in their assortment (or missing items that are in their assortment).
- SKU dimensions in the item master (W252) inaccurate, causing items to not physically fit in the planned fixture positions — discovered only during in-store setup.
- Small-format stores receiving large-format planogram templates, causing overcrowded displays and impossible facing requirements.
- Planogram compliance (W86) not linked to the template master, making it impossible to auto-detect which stores have outdated planograms.
- Fixture master data not maintained, causing planogram designers to specify fixtures that no longer exist in stores.
- Planogram templates not refreshed after SKU discontinuation (W68), leaving dead positions that stores fill with unauthorized items.
- No planogram assignment for new stores, causing ad-hoc display layouts that differ from the brand standard.

### Staffing Implication
Absorbed by Merchandising and MDM teams. ~10–20 new/revised templates/year × ~6 hours each = ~60–120 hours/year. Quarterly review ~4 hours. Fixture master maintenance ~15 min per new fixture type.

### Time Estimate
**Total**: ~6 hours per new planogram template; ~4 hours quarterly performance review; ~30 minutes per store cluster assignment.

---

## W315. Product Lifecycle Status & Transition Rule Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New product lifecycle stage definition, transition rule modification, status-dependent behavior change (e.g., replenishment rule for "End-of-Life" status), or periodic lifecycle status audit |
| **Frequency** | ~2–3 structural status/rule changes/year; ~500–800 lifecycle status transitions/month (driven by W252 creation, W68 discontinuation, W264 seasonal transition); annual lifecycle rule review |
| **Owner** | Master Data Manager |
| **Participants** | Category Manager, Supply Chain Planner, Pricing Analyst, Master Data Analyst, IT ERP Administrator |
| **Volume** | ~55,000 total SKU master records across ~6 lifecycle statuses; ~500–800 status changes/month; ~6 active transition rules |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Lifecycle Status Definition**: Master Data Analyst defines the valid lifecycle statuses in the ERP. The standard status set for BuildRight Depot includes: (a) **New/Introduction** — recently created SKU, not yet in active assortment, initial purchase order pending, (b) **Active** — in active assortment, auto-replenishment enabled, full channel availability (POS, ecommerce, marketplace), (c) **Seasonal** — available only during specific seasonal windows (linked to W306 event calendar), replenishment parameters activate/deactivate with the season, (d) **End-of-Life (EOL)** — vendor has communicated discontinuation or BuildRight has decided to discontinue, no new POs, sell through remaining stock, (e) **Discontinued/Inactive** — zero stock, no sales activity, retained in master for historical reporting and potential reactivation, (f) **Blocked/Hold** — quality issue, regulatory hold, or recall (W29) — no selling permitted, inventory quarantined (W219). Each status has a defined set of permitted downstream behaviors. | Master Data Analyst | Master Data Manager | 1 hour/status |
| 2 | **Status-Dependent Behavior Configuration**: IT ERP Administrator configures the behavior rules for each lifecycle status. These rules govern how the system treats an item based on its status: (a) **Replenishment** — Active: auto-replenishment enabled (SCP-002); Seasonal: replenishment enabled during event window only; EOL: no new POs, existing POs allowed to complete; Discontinued: no POs, no transfers; Blocked: no movement permitted. (b) **Pricing** — Active: standard pricing; Seasonal: seasonal pricing rules (W306); EOL: markdown pricing eligible (W93); Discontinued: not orderable. (c) **Channel Availability** — Active: all channels; Seasonal: channels per seasonal plan; EOL: POS and ecommerce only (remove from marketplace to avoid long-delivery commitments); Discontinued: no channel availability. (d) **Assortment** — Active: included in assortment matrix (W299); EOL: flagged for removal at next assortment review; Discontinued: removed from assortment matrix. (e) **Planogram** — Active: included in planogram templates (W314); EOL: flagged for position removal; Discontinued: position released for reassignment. | IT ERP Administrator | Master Data Manager | 2 hours/status |
| 3 | **Transition Rule Definition**: Master Data Analyst defines the valid transitions between statuses and the prerequisites for each transition: (a) **New → Active**: requires completed item master (W252), assigned vendor (W287), assigned category (W290), configured planning parameters (W312), and at least one PO received at a DC. (b) **Active → Seasonal**: requires linked seasonal event (W306) and seasonal-specific planning parameters. (c) **Active → EOL**: requires Category Manager approval, confirmation of no open POs or transfer orders, and markdown pricing plan (W93). (d) **Active → Blocked**: triggered by quality issue (W110), recall (W29), or compliance hold — requires documented reason code (W301). (e) **Blocked → Active**: requires quality clearance (W110 CAPA closure) or recall resolution. (f) **EOL → Discontinued**: requires zero on-hand inventory across all locations, zero open POs, zero open sales orders, and at least 90 days in EOL status. (g) **Discontinued → Active (Reactivation)**: requires Category Manager approval, new vendor assignment if original vendor is inactive, and updated planning parameters. System enforces these rules — transitions that don't meet prerequisites are blocked with a diagnostic message. | Master Data Analyst | Master Data Manager | 2 hours/transition rule |
| 4 | **Automated Status Transition Triggers**: IT ERP Administrator configures automated status transition triggers where appropriate: (a) **EOL auto-trigger**: when the last goods receipt for an EOL item is processed and on-hand reaches zero at all locations, system prompts the Discontinued transition (requires Master Data Analyst confirmation). (b) **Seasonal auto-activate/deactivate**: linked to the seasonal event calendar (W306) — items with "Seasonal" status automatically transition to "Active" at event start and back to "Seasonal" at event end. (c) **Blocked auto-trigger**: quality hold from W110 automatically sets status to Blocked with the quality case reference number. (d) **New → Active**: when the first goods receipt is processed against an item in New status, system prompts the Active transition. | IT ERP Administrator | Master Data Manager | 4 hours (one-time config) |
| 5 | **Status Change Execution**: When a lifecycle status change is needed, the responsible party initiates it: (a) Category Manager for assortment-driven changes (new product launches, discontinuations), (b) Supply Chain Planner for supply-driven changes (vendor discontinuation, sourcing change), (c) Quality team for compliance-driven changes (quality hold, recall). System validates prerequisites (Step 3) and either executes the transition or rejects it with a diagnostic. All status changes are logged in an immutable audit trail: timestamp, old status, new status, changed-by user, and approval reference. | Category Manager / Supply Chain Planner | Master Data Manager | 5 min |
| 6 | **Downstream Cascade**: Upon status change, system cascades the impact to all downstream modules: (a) replenishment engine — enable/disable auto-PO generation, (b) POS — enable/disable scanning and selling (blocked items trigger a "sale blocked" alert at POS), (c) ecommerce — add/remove from online catalog, (d) marketplace — add/remove from marketplace listings (W180), (e) planogram — flag for position removal/reassignment (W314), (f) assortment matrix — add/remove from store assortment lists (W299), (g) promotional rules — deactivate any active promotions on blocked/discontinued items (W300). Cascade execution is logged with timestamps for each downstream module. | System | — | Automated |
| 7 | **Quarterly Lifecycle Status Audit**: Quarterly, Master Data Analyst audits the lifecycle status distribution: (a) items in "New" status for > 60 days without activation (stuck in onboarding), (b) items in "EOL" status for > 180 days with remaining stock (stale EOL), (c) items in "Blocked" status for > 30 days without a linked quality case (orphaned blocks), (d) items in "Discontinued" status with non-zero inventory (data discrepancy), (e) items in "Active" status with zero sales in 12 months (candidates for EOL review). Exceptions are escalated to the Category Manager for action. | Master Data Analyst | Master Data Manager | 4 hours/quarter |
| 8 | **Annual Transition Rule Review**: Annually, Master Data Manager reviews all lifecycle statuses and transition rules: (a) validates that status-dependent behaviors are still aligned with operational policies, (b) reviews transition prerequisite rules for continued relevance (e.g., whether a new prerequisite should be added for the New→Active transition), (c) assesses the frequency of bypass overrides (transitions forced by Master Data Manager despite missing prerequisites) — high override rates indicate rules that are too strict, (d) benchmarks the average time-in-status for key transitions (New→Active target: < 30 days; EOL→Discontinued target: < 90 days after zero stock). | Master Data Manager | VP Merchandising | 4 hours/year |

### System Touchpoints
- ERP Item Master Module (lifecycle status field per SKU)
- Replenishment Engine (SCP-002 — status-driven PO generation control)
- POS Module (status-driven sale enable/disable)
- Ecommerce Platform (status-driven catalog visibility)
- Marketplace Integration (W180 — status-driven listing management)
- Promotional Rule Engine (W300 — status-driven promo eligibility)
- Assortment Matrix (W299 — status-driven assortment inclusion)
- Planogram Module (W314 — status-driven position management)
- Quality Module (W110 — quality-driven status blocking)
- Recall Module (W29 — recall-driven status blocking)
- Seasonal Calendar (W306 — seasonal status auto-transition)

### Pain Points / Risks
- Items stuck in "New" status blocking activation of the SKU for selling, causing revenue loss on launched products.
- EOL items not transitioning to Discontinued, remaining visible in ecommerce and marketplace with zero stock, causing customer orders that cannot be fulfilled.
- Blocked items not cascading to POS, allowing continued selling of quality-compromised or recalled products.
- Discontinued items not removed from planogram templates, leaving dead display positions in stores.
- Transition prerequisites too strict, causing frequent override requests that bypass governance controls.
- Seasonal status auto-transition not linked to the seasonal calendar, requiring manual status changes for hundreds of SKUs each season.
- Reactivated items (Discontinued→Active) carrying stale planning parameters and pricing from the original lifecycle, causing replenishment or pricing errors.

### Staffing Implication
Absorbed by existing MDM team. Status/rule changes ~2–3/year × ~2 hours = ~4–6 hours/year. Quarterly audit ~4 hours. Annual review ~4 hours. Status change execution ~5 min each × ~500–800/month, handled by Category Managers and Supply Chain Planners as part of routine operations.

### Time Estimate
**Total**: ~2 hours per structural status/rule change; ~5 minutes per status transition execution; ~4 hours quarterly audit; ~4 hours annual review.

---

## W316. Digital Asset & Product Content Master Governance

| Field | Detail |
|---|---|
| **Trigger** | New SKU creation requiring product content, seasonal content refresh, marketplace listing requirement, digital asset quality audit, or content format/channel requirement change |
| **Frequency** | ~500–800 new SKU content sets/month; ~2,000–3,000 content updates/month; quarterly quality audit; annual channel requirement review |
| **Owner** | Ecommerce Content Manager |
| **Participants** | Category Manager, Master Data Analyst, Marketing Designer, Ecommerce Platform Administrator |
| **Volume** | ~35,000 active SKUs requiring digital assets; ~6–10 asset types per SKU; ~5 channel-specific variants per asset type; ~200,000–350,000 total managed digital assets |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Asset Type & Standard Definition**: Ecommerce Content Manager defines the required digital asset types and quality standards per product category. Each asset type specifies: (a) **Hero image** — white background, minimum 2000×2000px, JPEG/PNG, no watermarks, (b) **Lifestyle image** — product in context (e.g., tiles in a bathroom mockup), minimum 1500×1500px, (c) **Dimensional diagram** — technical drawing showing product dimensions, standardized format per category, (d) **Product video** — optional for A-items, max 60 seconds, MP4, 1080p, (e) **Installation guide** — PDF, step-by-step for items requiring professional installation (linked to W138), (f) **Safety data sheet (SDS)** — mandatory for chemical/paint items, PDF format per DENR requirements, (g) **Specification sheet** — detailed technical specs, PDF. Each asset type has: naming convention (SKU_code_asset-type_channel_variant.extension), minimum resolution, maximum file size, required metadata fields (alt text, title, caption), and category-specific requirements (e.g., tiles require 360° room view, paint requires color accuracy calibration profile). | Ecommerce Content Manager | — | 4 hours (initial setup) |
| 2 | **Channel-Specific Variant Requirements**: Ecommerce Platform Administrator defines the required asset variants per channel: (a) **Own ecommerce** — full-resolution images, zoom capability, 360° view, embedded video, (b) **Lazada marketplace** — compliant image per Lazada specs (white background, no text overlay, max 5MB, watermarked brand logo allowed), (c) **Shopee marketplace** — compliant image per Shopee specs (similar but different dimension requirements), (d) **Google Shopping** — GTIN-linked feed image per Google Merchant Center requirements (linked to W311 barcode master), (e) **Social media** — optimized for Facebook/Instagram aspect ratios and file sizes (for W142 social media management), (f) **POS / In-store kiosk** — optimized for POS customer display and in-store digital signage resolution. Each channel variant is generated from the master asset using automated resizing/cropping rules configured in the PIM system (W50). | Ecommerce Platform Administrator | Ecommerce Content Manager | 2 hours/channel |
| 3 | **Asset Creation & Ingestion**: When a new SKU is created (W252) or a content refresh is needed, the asset creation process follows: (a) **Vendor-supplied assets** — vendor submits images and specs via the Vendor Portal (W252 Step 1). Master Data Analyst validates against quality standards (Step 1). Non-compliant assets are rejected with a checklist of required corrections. (b) **In-house produced assets** — Marketing Designer creates lifestyle images, dimensional diagrams, or videos. Designer follows the category-specific style guide and uploads to the PIM with completed metadata. (c) **Third-party sourced assets** — for private label items (W129), assets are sourced from the factory or produced by external photographers. Ecommerce Content Manager manages the production brief. | Master Data Analyst / Marketing Designer | Ecommerce Content Manager | 15 min/SKU |
| 4 | **Metadata & SEO Configuration**: Master Data Analyst configures product content metadata in the PIM: (a) **Product title** — follows naming convention: [Brand] [Product Name] [Key Spec] [Size/Color], max 150 characters, (b) **Product description** — structured: short description (max 300 chars for listing), long description (unlimited for detail page), bullet points (5–8 key features), (c) **SEO fields** — meta title, meta description, URL slug, keywords per category, (d) **Search facets** — material, finish, color, size, application (linked to W298 product attribute templates), (e) **Compliance declarations** — FDA registration number (if applicable), Hazmat classification (linked to W236), warranty terms, country of origin. System validates that all mandatory metadata fields are populated before the content set can be published. | Master Data Analyst | — | 10 min/SKU |
| 5 | **Quality Review & Approval**: Ecommerce Content Manager reviews the complete digital asset and content set for a SKU before publication: (a) image quality — correct resolution, proper lighting, no background clutter, accurate color representation (critical for tiles and paint), (b) content accuracy — specifications match the item master (W252) dimensions, weight, and material attributes, (c) SEO compliance — keyword density, meta description quality, (d) channel readiness — all required variants exist for each active channel. Non-compliant content is returned to the creator with specific feedback. | Ecommerce Content Manager | — | 5 min/SKU |
| 6 | **Publication & Channel Distribution**: Ecommerce Platform Administrator publishes the approved content set to all channels: (a) own ecommerce platform — full content set published, (b) marketplace integrations — channel-compliant variants pushed to Lazada/Shopee via API (W180), (c) Google Shopping feed — GTIN-linked content pushed via feed, (d) POS system — product image synced to POS terminals for customer-facing display, (e) print systems — image available for shelf labels (W181) and promotional flyers (W262). System tracks the publication status per channel and alerts if a channel sync fails. | System / Ecommerce Platform Administrator | — | 5 min/SKU |
| 7 | **Content Lifecycle Management**: Digital assets follow the product lifecycle (W315): (a) **Active items** — content reviewed quarterly for accuracy (price changes, spec updates, new lifestyle images), (b) **EOL items** — content remains published but flagged for removal at discontinuation, (c) **Discontinued items** — content unpublished from all channels, assets archived (not deleted — retained for potential reactivation), (d) **Seasonal refresh** — seasonal items receive updated lifestyle images and promotional banners at each seasonal transition (W264). Ecommerce Content Manager tracks content freshness: items with content older than 12 months are flagged for refresh. | Ecommerce Content Manager | — | 2 hours/month |
| 8 | **Quarterly Digital Asset Quality Audit**: Ecommerce Content Manager conducts a quarterly quality audit: (a) **Completeness** — % of active SKUs with all mandatory asset types populated (target: ≥ 98%), (b) **Channel compliance** — % of published content passing automated channel validation checks (Lazada/Shopee/Google feed rejection rates), (c) **Accuracy** — sample 100 SKUs and verify that product content (title, specs, images) matches the physical product and item master data, (d) **Freshness** — identify SKUs with content not updated in > 12 months, (e) **Orphaned assets** — digital assets not linked to any active SKU (data cleanup). Categories with < 95% completeness are escalated to the Category Manager for vendor follow-up (vendor-supplied content gaps). | Ecommerce Content Manager | Master Data Manager | 4 hours/quarter |
| 9 | **Annual Channel Requirement Update**: Annually, Ecommerce Platform Administrator reviews channel-specific requirements: (a) marketplace specification changes (Lazada/Shopee update their image requirements periodically), (b) Google Shopping feed specification updates, (c) new channel onboarding (e.g., TikTok Shop, future channels), (d) emerging content types (3D models, augmented reality views for tiles/furniture). Updated requirements are reflected in the asset type standards (Step 1) and channel variant rules (Step 2). Content that no longer meets updated standards is flagged for re-production. | Ecommerce Platform Administrator | Ecommerce Content Manager | 4 hours/year |

### System Touchpoints
- PIM (Product Information Management) System (W50 — central content repository)
- ERP Item Master (W252 — master data source for content validation)
- Product Attribute Templates (W298 — attribute-driven content metadata)
- Ecommerce Platform (catalog content publishing)
- Marketplace Integration (W180 — channel-specific content distribution)
- POS Module (product images on customer display)
- Google Shopping Feed (GTIN-linked product content)
- Vendor Portal (vendor-supplied digital assets)
- Digital Asset Management (DAM) System (asset storage, versioning, rights management)
- Barcode/GTIN Master (W311 — GTIN linkage for Google Shopping)

### Pain Points / Risks
- Vendor-supplied images with low resolution or watermarked with competitor branding, causing marketplace listing rejections and unprofessional appearance.
- Product specifications in digital content not matching item master data (e.g., wrong dimensions, outdated pricing in lifestyle images), causing customer complaints and returns.
- Missing Hazmat/SDS documentation for chemical products, causing regulatory non-compliance and marketplace listing removal.
- Color accuracy issues in tile/paint images (screen color ≠ actual product color), causing high return rates for ecommerce orders.
- Content not updated after product specification changes, causing inaccurate information to persist across all channels.
- Marketplace content feed failures going undetected, causing products to be listed without images or with outdated content.
- Orphaned digital assets (assets for discontinued items) consuming storage and cluttering the DAM system.
- Missing channel-specific variants causing products to appear with broken images or missing descriptions on specific channels.
- SEO metadata not configured, causing poor organic search ranking and lost ecommerce traffic.

### Staffing Implication
Absorbed by existing Ecommerce Content and MDM teams. ~500–800 new SKU content sets/month × ~30 min = ~250–400 hours/month (shared between Master Data Analysts, Marketing Designers, and Ecommerce Content Manager). Quarterly audit ~4 hours. Annual channel update ~4 hours. Content lifecycle management ~2 hours/month.

### Time Estimate
**Total**: ~30 minutes per new SKU content set; ~10 minutes per content update; ~2 hours/month lifecycle management; ~4 hours quarterly quality audit.

---

## W399. Fixed Asset Master Data Governance

| Field | Detail |
|---|---|
| **Trigger** | Introduction of new asset categories, updates to depreciation policies, or changes in useful life definitions |
| **Frequency** | Ad-hoc (typically annual review) |
| **Owner** | Corporate Controller |
| **Participants** | Fixed Asset Accountant, Tax Manager, IT ERP Administrator |
| **Volume** | ~20 active asset classes; ~50 depreciation keys |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Policy Definition**: Corporate Controller defines or updates an asset class (e.g., IT Equipment, Store Fixtures, Leasehold Improvements) including standard useful life, depreciation method (e.g., Straight Line), and salvage value policy. | Corporate Controller | CFO | 1 hour |
| 2 | **Tax Alignment**: Tax Manager reviews the depreciation keys against BIR regulations to ensure compliance for tax depreciation schedules. | Tax Manager | — | 30 min |
| 3 | **System Configuration**: IT ERP Administrator configures the new Asset Class and Depreciation Keys in the ERP, linking them to the appropriate GL accounts (Asset, Accumulated Depreciation, Depreciation Expense). | IT ERP Administrator | Corporate Controller | 30 min |
| 4 | **Mass Update Validation**: If a policy change affects existing assets (e.g., extending the useful life of POS terminals), Fixed Asset Accountant runs a simulation of the depreciation recalculation to review the P&L impact. | Fixed Asset Accountant | Corporate Controller | 2 hours |
| 5 | **Approval & Activation**: Corporate Controller approves the new master data and any mass updates. System applies the new rules for all future W21.7 capitalizations. | Corporate Controller | CFO | 15 min |

### System Touchpoints
- ERP Fixed Asset Module
- Finance / GL Configuration
- Tax Reporting Engine

### Pain Points / Risks
- Inconsistent useful life application across entities leading to audit adjustments.
- Disconnect between book depreciation and tax depreciation rules.

### Staffing Implication
Absorbed by existing Finance team. Handled centrally.

### Time Estimate
**Total**: ~4.5 hours per policy update.

---

## W400. Equipment & Asset Maintenance (EAM) Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Procurement of new store fixtures, material handling equipment (MHE), or HVAC systems requiring maintenance tracking |
| **Frequency** | Monthly (as new equipment types are acquired) |
| **Owner** | VP Engineering / Maintenance |
| **Participants** | Maintenance Manager, Master Data Analyst, Procurement Manager |
| **Volume** | ~5,000 trackable equipment records; ~200 maintenance plans |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Equipment Template Creation**: Procurement Manager provides specs for a new equipment model. Master Data Analyst creates the Equipment Master template, defining the manufacturer, model, warranty duration, and serial number tracking requirement. | Master Data Analyst | — | 15 min |
| 2 | **BOM Definition**: Maintenance Manager defines the equipment Bill of Materials (BOM), mapping standard spare parts (linked to Item Master W252) needed for repairs. | Maintenance Manager | — | 30 min |
| 3 | **Maintenance Plan Configuration**: Maintenance Manager establishes standard preventative maintenance (PM) schedules (e.g., 6-month HVAC servicing, 200-hour forklift check). | Maintenance Manager | VP Engineering | 20 min |
| 4 | **System Setup**: Master Data Analyst configures the PM schedules and ties them to the Equipment Master in the ERP/EAM module. | Master Data Analyst | — | 15 min |

### System Touchpoints
- ERP Enterprise Asset Management (EAM) / Plant Maintenance Module
- Item Master (for spare parts BOM)
- Procurement Module (warranty tracking)

### Pain Points / Risks
- Unplanned downtime due to missing preventative maintenance schedules.
- Overstocking or stockouts of spare parts because equipment BOMs are not linked to inventory.

### Staffing Implication
Absorbed by Engineering and MDM teams. ~1.5 hours per new equipment type.

### Time Estimate
**Total**: ~80 minutes per new equipment model setup.

---

## W401. Fleet & Vehicle Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Acquisition or leasing of new delivery trucks, vans, or corporate vehicles |
| **Frequency** | 1–2 times per quarter |
| **Owner** | Logistics Manager |
| **Participants** | Fleet Supervisor, Master Data Analyst, HR Manager |
| **Volume** | ~150 fleet vehicles |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Vehicle Master Creation**: Fleet Supervisor submits vehicle details (plate number, VIN, make/model, gross vehicle weight, cubic capacity). | Fleet Supervisor | — | 15 min |
| 2 | **Compliance Data Logging**: Master Data Analyst logs LTO registration expiration, insurance policy renewal dates, and emissions testing dates. System generates automated 30-day alerts prior to expiration. | Master Data Analyst | — | 10 min |
| 3 | **Routing & Capacity Setup**: Logistics Manager configures the vehicle in the transportation management system (TMS), defining its route restrictions (e.g., truck ban exemptions) and maximum payload (weight/volume) for load building (W197). | Logistics Manager | — | 20 min |
| 4 | **Driver Linkage**: HR Manager links the vehicle to the authorized driver pool (W292), ensuring only drivers with active professional licenses can be assigned. | HR Manager | — | 10 min |

### System Touchpoints
- ERP Fleet Management / TMS Module
- HR Employee Master (Driver linkage)
- Alerts & Notifications Engine

### Pain Points / Risks
- Delivery delays caused by operating vehicles with expired LTO registrations.
- Overloading trucks because GVW and cubic capacity master data are incorrect.

### Staffing Implication
Absorbed by Logistics team. ~1 hour per vehicle setup.

### Time Estimate
**Total**: ~55 minutes per vehicle.

---

## W402. Contract & Agreement Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Execution of a new vendor trade agreement, real estate lease, or corporate B2B sales contract |
| **Frequency** | ~10–20 new/renewed contracts per week |
| **Owner** | Legal Counsel / Contract Administrator |
| **Participants** | Category Manager, Procurement Manager, Finance Controller, Master Data Analyst |
| **Volume** | ~3,000 active contracts |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Contract Ingestion**: Contract Administrator scans and uploads the signed contract into the ERP Contract Management module, capturing metadata (parties, start/end dates, renewal terms, financial value). | Contract Administrator | — | 15 min |
| 2 | **Commercial Terms Mapping**: Category Manager extracts commercial terms (e.g., 2% volume rebate, marketing development funds) and inputs them into the Trade Spend / Rebate agreements master. | Category Manager | — | 20 min |
| 3 | **Lease Accounting Linkage**: For real estate contracts, Finance Controller maps the lease terms (monthly rent, escalation clauses) to the IFRS 16 / PFRS 16 lease accounting module (W275) to generate ROU asset schedules. | Finance Controller | — | 30 min |
| 4 | **Governance & Alerting**: System applies a master rule to send renewal/termination alerts 90 days prior to contract expiration to the respective business owner. | System | — | Automated |

### System Touchpoints
- ERP Contract Lifecycle Management (CLM) Module
- Rebate / Trade Spend Management Module
- IFRS 16 Lease Accounting Module

### Pain Points / Risks
- Missed vendor rebates due to untracked trade agreements.
- Unwanted auto-renewals of software or services due to lack of expiration alerts.

### Staffing Implication
Managed by Legal/Contract Admin and Finance.

### Time Estimate
**Total**: ~65 minutes per complex contract ingestion.

---

## W403. Competitor & Market Intelligence Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Identification of a new market competitor or competitive mapping requirement for price scraping |
| **Frequency** | Monthly review |
| **Owner** | Pricing Manager |
| **Participants** | Merchandising Analyst, Master Data Analyst |
| **Volume** | ~10–15 tracked competitors; ~5,000 mapped KVIs (Key Value Items) |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Competitor Setup**: Pricing Manager defines a new competitor profile, including their store locations (mapped to proximity of BuildRight stores) and ecommerce URLs. | Pricing Manager | — | 20 min |
| 2 | **KVI Mapping**: Merchandising Analyst maps BuildRight SKUs to the exact or comparable competitor SKUs (matching by GTIN, brand, or spec equivalence). | Merchandising Analyst | — | 5 min/SKU |
| 3 | **Scraping Configuration**: Master Data Analyst updates the competitive price scraping tool with the new URLs and CSS selectors if necessary. | Master Data Analyst | — | 30 min |
| 4 | **Index Governance**: Pricing Manager reviews the competitive index rules (e.g., "BuildRight price must be <= Competitor X for Category Y"). | Pricing Manager | VP Merchandising | 15 min |

### System Touchpoints
- Competitive Pricing & Scraping Tool
- ERP Pricing Rule Engine (W289)

### Pain Points / Risks
- Pricing algorithms lowering margins based on incorrect SKU matches (e.g., matching a 5L paint can against a competitor's 1L can).
- Scraping tools breaking when competitor websites change.

### Staffing Implication
Absorbed by Pricing team. Heavy upfront mapping effort for KVIs.

### Time Estimate
**Total**: ~65 minutes for competitor setup; ongoing KVI mapping effort.

---

## W404. Point-of-Sale (POS) System & Hardware Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Deployment of a new POS terminal, self-checkout kiosk, or updates to receipt templates and macro keys |
| **Frequency** | Weekly (for new registers or layout changes) |
| **Owner** | IT Store Operations Manager |
| **Participants** | Store Manager, Finance Controller, IT ERP Administrator |
| **Volume** | ~600 POS terminals across 200 stores |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Terminal Registration**: IT Store Ops Manager provisions a new POS terminal, assigning it a unique Terminal ID, linking it to the Store Location Master (W254), and defining its hardware profile (scanner, receipt printer, cash drawer). | IT Store Ops Mgr | — | 15 min |
| 2 | **Financial Mapping**: Finance Controller links the Terminal ID to the specific petty cash/till GL account and tax profile for correct VAT/LGU tax printing on receipts. | Finance Controller | — | 10 min |
| 3 | **UI & Macro Key Setup**: IT ERP Administrator pushes the standard UI profile to the terminal, containing the governed list of quick-keys (e.g., non-barcoded items, service fees, bag fees) ensuring consistency across all stores. | IT ERP Administrator | — | 10 min |
| 4 | **Offline DB Sync Rule**: System configures the terminal's offline database sync frequency and scope (downloading the Item Master and Pricing Master delta updates daily). | System | — | Automated |

### System Touchpoints
- POS Central Configuration Manager
- ERP GL & Tax Modules
- Store Location Master

### Pain Points / Risks
- Inconsistent tax rates printing on receipts if terminal tax profiles drift from the master.
- Rogue quick-keys created locally by Store Managers to bypass scanning.

### Staffing Implication
Absorbed by IT Operations.

### Time Estimate
**Total**: ~35 minutes per terminal configuration.

---

## W405. Data Privacy & Consent Preferences Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Customer opts in/out of marketing, submits a DSAR, or changes data privacy preferences |
| **Frequency** | Continuous |
| **Owner** | Data Protection Officer (DPO) |
| **Participants** | CRM Data Steward, IT ERP Administrator |
| **Volume** | ~600,000 customer records |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Consent Capture**: Customer updates preferences via the Ecommerce portal, mobile app, or in-store prompt. System logs the consent boolean (Email, SMS, Direct Mail, Data Sharing), the timestamp, and the IP/source of consent. | System / Customer | — | Automated |
| 2 | **Centralized Preference Master**: The consent data is immediately synced to the Central Consent Master, overriding any conflicting channel-specific preferences. | System | — | Automated |
| 3 | **Suppression List Generation**: CRM Data Steward ensures that marketing automation tools query the Consent Master daily to generate dynamic suppression lists, preventing unsolicited communications. | CRM Data Steward | DPO | 10 min/day |
| 4 | **Right-to-be-Forgotten Execution**: When a deletion request is approved (W271), IT Administrator executes a governed anonymization script that obfuscates PII in the Customer Master (W253) but retains transaction IDs for financial integrity. | IT ERP Administrator | DPO | 30 min |

### System Touchpoints
- Customer Data Platform (CDP) / Consent Master
- Marketing Automation Tools
- Ecommerce / POS (Consent capture forms)

### Pain Points / Risks
- National Privacy Commission (NPC) fines for sending marketing SMS to opted-out customers due to siloed consent data.
- Deleting financial transaction history accidentally when fulfilling a privacy deletion request.

### Staffing Implication
Automated system governance; DPO oversees compliance.

### Time Estimate
**Total**: Automated capture; ~30 minutes per complex deletion.

---

## W406. ESG & Sustainability Metrics Master Governance

| Field | Detail |
|---|---|
| **Trigger** | Changes in regulatory emission factors, new sustainability certification standards, or updates to vendor scoring rubrics |
| **Frequency** | Annually or upon regulatory update |
| **Owner** | Chief Sustainability Officer (CSO) |
| **Participants** | Master Data Analyst, Procurement Manager |
| **Volume** | ~100 emission factors; ~50 certification types |

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Factor Definition**: CSO defines or updates the standard greenhouse gas (GHG) emission factors (e.g., kg CO2e per kWh of electricity, or per liter of diesel) using updated government or international frameworks. | CSO | — | 1 hour |
| 2 | **Certification Master**: Master Data Analyst governs the list of recognized sustainability certifications (e.g., FSC certified wood, Energy Star) and links them to the Item Master attributes (W252/W298). | Master Data Analyst | CSO | 30 min |
| 3 | **Vendor Scoring Rubric**: Procurement Manager configures the weighting algorithms in the Vendor Master (W287) that calculate a vendor's Sustainability Score based on their certifications and audit results. | Procurement Manager | CSO | 1 hour |
| 4 | **Dashboard Sync**: System syncs these master factors to the ESG reporting dashboards (W192-W195) to ensure all calculated carbon footprints use the single source of truth. | System | — | Automated |

### System Touchpoints
- ERP ESG / Sustainability Module
- Vendor Master
- Item Attribute Templates

### Pain Points / Risks
- Inaccurate ESG reporting due to decentralized or outdated emission factor spreadsheets.
- Greenwashing risks from unverified or improperly mapped product certifications.

### Staffing Implication
Absorbed by the ESG and MDM teams.

### Time Estimate
**Total**: ~2.5 hours per annual metric update.
