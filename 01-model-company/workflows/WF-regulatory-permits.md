# Regulatory Permits & Local Government Compliance Workflows

> Management of product certifications, local government health/sanitary permits, and other recurring regulatory requirements.
>
> Back to [Workflow Index](README.md)

---

## Workflows in This Domain

- [W447. DTI-BPS Mandatory Product Certification (ICC/SOC)](#w447-dti-bps-mandatory-product-certification-iccsoc)
- [W448. LGU Sanitary & Health Permit Management](#w448-lgu-sanitary--health-permit-management)
- [W467. Specialized Hardware Permits (DENR, FPA)](#w467-specialized-hardware-permits-denr-fpa)
- [W476. LGU / BFP Fire Safety Inspection Certificate (FSIC) Management](#w476-lgu--bfp-fire-safety-inspection-certificate-fsic-management)
- [W477. DENR Permit to Operate (PTO) & Wastewater Discharge Permit (WDP) Compliance](#w477-denr-permit-to-operate-pto--wastewater-discharge-permit-wdp-compliance)
- [W479. FDA License to Operate (LTO) for Household Hazardous Substances Compliance](#w479-fda-license-to-operate-lto-for-household-hazardous-substances-compliance)
- [W480. CAAP Height Clearance Permit Compliance](#w480-caap-height-clearance-permit-compliance)
- [W802. LGU Local Business Tax Computation, Payment & Receipt Management](#w802-lgu-local-business-tax-computation-payment--receipt-management)

---

## W447. DTI-BPS Mandatory Product Certification (ICC/SOC)

| Field | Detail |
|---|---|
| **Trigger** | Import Purchase Order (W2B) created for regulated construction materials |
| **Frequency** | Per import shipment of regulated goods (e.g., steel, cement, electrical) |
| **Volume** | ~10–15 shipments/month |
| **Owner** | Import Coordinator |
| **Participants** | Buyer, Customs Broker, DTI-BPS Officer, Third-Party Testing Lab |

### Background

Under Philippine law, certain products (deformed steel bars, cement, PVC pipes, etc.) must undergo mandatory certification by the Department of Trade and Industry - Bureau of Product Standards (DTI-BPS). Imported goods require either an **Import Commodity Clearance (ICC)** or a **Statement of Confirmation (SOC)** for products with a valid PS (Product Standard) license.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Application**: Import Coordinator files ICC/SOC application via DTI's I-SEAL portal upon shipment departure from origin | Import Coordinator | Category Mgr | 1 hour |
| 2 | **Documentary Review**: DTI-BPS reviews Bill of Lading, Packing List, and Commercial Invoice | DTI-BPS | — | 1–3 days |
| 3 | **Inspection & Sampling**: Upon arrival at Port/DC, DTI inspector performs physical inspection and draws random samples | DTI Inspector | Import Coordinator | 4 hours |
| 4 | **Testing**: Samples sent to DTI-accredited laboratory for testing (e.g., tensile strength for steel, compression for cement) | Lab Tech | — | 5–10 days |
| 5 | **Certificate Issuance**: If tests pass, DTI issues ICC/SOC certificate and ICC stickers for each unit/package | DTI-BPS | — | 2 days |
| 6 | **Release**: Customs Broker uses the certificate to finalize customs clearance; goods released to DC | Customs Broker | — | 1 day |
| 7 | **Sticker Application**: DC staff apply ICC stickers to individual items before putaway or dispatch to stores | DC Team | DC Manager | Varies |

### System Touchpoints
- Import Tracker (link to ICC/SOC application status)
- Document storage for DTI certificates
- Cost component: DTI fees and testing charges allocated to Landed Cost (W144)

### Pain Points / Risks
- **Testing delays**: Lead times for accredited labs can exceed 2 weeks, triggering port demurrage (W249)
- **Sample failure**: If samples fail, the entire shipment must be re-exported or destroyed under DTI supervision
- **ICC sticker inventory**: Managing physical stickers for thousands of units is a manual bottleneck

### Time Estimate
- Total cycle time: 14–21 days from port arrival to release

---

## W448. LGU Sanitary & Health Permit Management

| Field | Detail |
|---|---|
| **Trigger** | Annual LGU Business Permit renewal cycle (January) or new hire onboarding |
| **Frequency** | Annual for all staff; per-hire for new employees |
| **Volume** | ~6,715 employees across 200 stores |
| **Owner** | Store Manager |
| **Participants** | HR Assistant, Store Staff, LGU Health Office, Accredited Clinic |

### Background

Every retail establishment in the Philippines must secure an annual **Sanitary Permit**. Additionally, every employee is required to hold a valid **Health Certificate** (Health Card) issued by the local health office, usually requiring medical clearance (X-ray, stool test, drug test).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Medical Screening**: Store staff undergo annual medical exam (X-ray, stool/drug test) at accredited clinic | Employee | HR Assistant | 2 hours |
| 2 | **Application**: HR Assistant compiles medical results and submits application to LGU Health Office | HR Assistant | Store Manager | 30 min |
| 3 | **Payment & Issuance**: Pay LGU fees; Health Office issues individual Health Cards and the Store Sanitary Permit | HR Assistant | — | 1 day |
| 4 | **Compliance Display**: Store Manager displays Sanitary Permit in the customer area; Health Cards kept in store files for inspection | Store Manager | — | 10 min |
| 5 | **Inspection**: LGU Health Inspector conducts unannounced visit to check facility sanitation and staff health cards | LGU Inspector | Store Manager | 1 hour |

### System Touchpoints
- HRIS: Tracking medical expiry dates per employee
- Document Storage: Scanned copies of Sanitary Permits and Health Cards
- Expense: LGU fees and medical exam costs (W7)

### Pain Points / Risks
- **Mass scheduling**: Coordinating exams for 30+ staff per store without disrupting operations
- **LGU variations**: Each of the ~100 LGUs has slightly different requirements and accredited clinics
- **Compliance gaps**: Employees missing cards during inspections can lead to "Notice of Violation" or closure

### Time Estimate
- Medical exam: 2 hours/employee
- Permit processing: 2–5 business days

---

## W467. Specialized Hardware Permits (DENR, FPA)

| Field | Detail |
|---|---|
| **Trigger** | Initial store setup or annual permit expiry |
| **Frequency** | Annual |
| **Volume** | All stores selling Lumber (DENR) or Fertilizer (FPA) |
| **Owner** | Store Manager |
| **Participants** | Category Manager (Merch), Legal, DENR, FPA |

### Background

Big-box hardware retailers in the Philippines must comply with specific environmental and agricultural regulations. Selling lumber requires a **DENR Wood Processing Plant / Lumber Dealer’s Permit**. Selling garden fertilizers and pesticides requires an **FPA License to Operate as Dealer**.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Application**: Store Manager compiles proof of legitimate wood sourcing (for DENR) or accredited handler training (for FPA) | Store Manager | — | 1 day |
| 2 | **Submission**: File application with the regional DENR or FPA office | Store Manager | Legal | 2 hours |
| 3 | **Inspection**: Regional officers inspect the store storage area for compliant ventilation, signage, and safety | Inspector | Store Manager | 4 hours |
| 4 | **Issuance**: Pay fees; Receive permit/license | Store Manager | — | 1-2 weeks |
| 5 | **Display**: Post permit in a conspicuous location near the lumber yard or garden center | Store Manager | — | 5 min |

### System Touchpoints
- Document Management (W255) for permit storage
- Compliance Calendar for renewal alerts
- Vendor Master: Linking wood suppliers to their DENR Sustainable Sourcing certificates

### Pain Points / Risks
- **Illegal Sourcing**: If lumber vendors lose their DENR accreditation, BuildRight's dealer permit may be revoked.
- **Handling Safety**: Improper storage of FPA-regulated chemicals leading to fines or environmental incidents.

---

## W476. LGU / BFP Fire Safety Inspection Certificate (FSIC) Management

| Field | Detail |
|---|---|
| **Trigger** | Upcoming annual FSIC expiration (tracked in Compliance Calendar) or LGU Business Permit renewal cycle (January) |
| **Frequency** | Annual per location |
| **Volume** | 205 locations (200 stores, 4 DCs, 1 Corporate HQ) |
| **Owner** | Store Manager (Stores) / DC Manager (DCs) / Facilities Manager (HQ) |
| **Participants** | Safety Officer, BFP Inspectors, Certified Fire Protection Contractor, Regulatory Officer, Legal |

### Background

Under the Fire Code of the Philippines (RA 9514), all business establishments must obtain an annual Fire Safety Inspection Certificate (FSIC) from the Bureau of Fire Protection (BFP). The FSIC is a mandatory prerequisite for renewing the local government (LGU) Business Permit (W54). Securing it requires building inspection, fire drill execution, and third-party certification of active firefighting systems (sprinklers, fire hydrants, emergency alarms, extinguishers).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Pre-Inspection System Testing**: 60 days before FSIC expiry, Safety Officer hires a certified third-party contractor to test the facility's fire systems: water pressure testing for sprinklers/hydrants, smoke detector functionality, emergency light backups, and fire extinguisher weight checks; contractor issues a Certificate of Testing/Compliance. | Safety Officer | Store/DC Manager | 2 days |
| 2 | **Employee Fire Drill**: Safety Officer conducts the mandatory annual fire evacuation drill for all store/DC personnel, documents it with photographs and attendance sheets, and files the report. | Safety Officer | Store/DC Manager | 2 hours |
| 3 | **Documentary Package Compilation**: Safety Officer compiles the FSIC renewal packet: (a) Prior year FSIC copy, (b) Real property tax receipt (W119) or lease contract, (c) Fire system test certificates, (d) Fire drill report, (e) Occupancy permit, (f) Comprehensive general liability insurance policy (W59). | Safety Officer | Store/DC Manager | 3 hours |
| 4 | **Application & Fee Payment**: Store Manager submits the packet to the local BFP station or via the online BFP portal (eBFP); pays the Fire Code Fees; system records the payment and uploads the BFP receipt. | Store Manager | Regulatory Officer | 1 hour |
| 5 | **BFP On-Site Inspection**: BFP Fire Inspectors conduct a scheduled on-site inspection: verify fire exits are clear, test the emergency alarm system, check sprinkler valves, inspect fire hose cabinets, and verify employee safety training. | BFP Inspectors / Safety Officer | Store/DC Manager | 3 hours |
| 6 | **Deficiency Resolution (If Applicable)**: If BFP identifies deficiencies: (a) BFP issues a Notice of Discrepancy, (b) Safety Officer creates urgent maintenance tickets (W47/W240) to resolve findings (e.g. repairing exit signs, clearing aisles), (c) schedules re-inspection within 15 days. | Safety Officer / Maintenance Team | Store/DC Manager | Varies (1-5 days) |
| 7 | **FSIC Issuance & Posting**: Upon passing inspection, BFP issues the FSIC. Store Manager posts the original certificate in a conspicuous public place; uploads a scanned copy to the ERP Document Management System (W255) and updates the Compliance Calendar. | Store Manager | — | 15 min |

### System Touchpoints
- ERP Compliance Calendar (Expiry alerts at 90/60/30 days)
- Document Management System (W255) for FSIC copies and inspection logs
- Fixed Asset / EAM Module (W240) to trigger fire system maintenance tickets
- Integration with W54 (LGU business permit renewal), W59 (Insurance lifecycle), W47 (Store facility maintenance), W240 (DC maintenance)

### Pain Points / Risks
- **Operational Shutdown**: BFP has the authority to padlock stores/DCs immediately for critical fire hazards (e.g. failed sprinkler pump), causing severe operational disruption.
- **Bribery & Extortion Risks**: Inconsistent enforcement across LGUs creates corruption risks during inspections; strictly monitored under W159 (Anti-Bribery compliance).
- **Exit Obstructions**: Hardware retail environments are prone to blocking emergency exit paths with bulk product displays (lumber pallets, rebar stacks), leading to failed inspections.

### Staffing Implication
- **Safety Officer**: Responsible for testing coordination, drill documentation, and document submission. ~16 hours/year per store/DC.
- **Store / DC Manager**: Accountable for BFP inspection coordination and deficiency resolution. ~8 hours/year per store/DC.

---

## W477. DENR Permit to Operate (PTO) & Wastewater Discharge Permit (WDP) Compliance

| Field | Detail |
|---|---|
| **Trigger** | Installation of a new standby generator/STP, or upcoming permit expiry (tracked in Compliance Calendar) |
| **Frequency** | Renewed every 1 to 5 years (depending on generator capacity and discharge volume) |
| **Volume** | ~204 locations (stores, DCs) with standby generators and STPs/septic systems |
| **Owner** | Pollution Control Officer (PCO) |
| **Participants** | Store Manager, DC Manager, DENR-EMB Inspectors, Accredited Stack Testing Firm, Third-Party Water Lab |

### Background

Under Philippine Environmental Laws, big-box hardware operations must secure:
1. **Permit to Operate (PTO)** for Air Emissions (RA 8749 - Clean Air Act) for standby generator sets used during power outages.
2. **Wastewater Discharge Permit (WDP)** (RA 9275 - Clean Water Act) for discharging domestic wastewater through Sewage Treatment Plants (STPs) or septic systems.
Securing these permits requires certified engineering plans, laboratory tests of wastewater, stack emission tests for generators, and an accredited Pollution Control Officer (PCO) to manage the submission via the DENR Environmental Management Bureau (EMB) Online Permitting and Monitoring System (OPMS).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Testing Coordination**: 90 days before permit expiry, PCO schedules mandatory environmental testing: (a) accredited laboratory draws effluent samples from the STP/septic system for biochemical analysis (BOD, COD, TSS), (b) accredited stack testing firm performs source emission testing (particulate matter, NOx, SOx) on standby generator exhausts. | Pollution Control Officer | VP Legal & Compliance | 2 days |
| 2 | **Lab Results Analysis**: PCO receives lab/stack test reports: (a) If compliant: moves to application; (b) If non-compliant: raises urgent EAM repair tickets (W47/W240) to service the STP (bacterial dosing, filter replacement) or tune the generator, then schedules re-testing. | Pollution Control Officer | Store/DC Manager | 1 day |
| 3 | **Documentary Package Compilation**: PCO compiles renewal documents: (a) Prior year PTO and WDP copies, (b) Water and air test certificates, (c) Water billing records (to calculate discharge fees), (d) Generator technical specifications, (e) PCO Accreditation Certificate. | Pollution Control Officer | — | 4 hours |
| 4 | **Online Application Submission**: PCO uploads documents and files renewal application in the DENR-EMB OPMS portal; generates payment voucher for regulatory fees. | Pollution Control Officer | — | 2 hours |
| 5 | **Fee Settlement**: Finance processes the payment voucher (W7); PCO uploads the proof of payment to the EMB portal. | Finance / PCO | PCO | 1 day |
| 6 | **EMB Inspection**: Regional DENR-EMB inspectors conduct on-site audits of the store/DC: verify the generator's exhaust stack height complies with the 5-meter rule, inspect the STP aeration tanks, and review onsite chemical storage. | EMB Inspectors / PCO | Store/DC Manager | 4 hours |
| 7 | **Permit Issuance & System Update**: Upon approval, EMB issues the digital PTO and WDP. PCO uploads the permits to the ERP Document Registry (W255), updates the Compliance Calendar, and updates the permit databases used for SMR/CMR reporting (W433). | Pollution Control Officer | VP Legal & Compliance | 30 min |

### System Touchpoints
- ERP Compliance Calendar (Expiry alerts at 120/90/60 days)
- Document Registry (W255) for digital permits and lab test records
- WMS / Fixed Asset register for tracking generator serials and capacities
- Integration with W433 (DENR SMR/CMR reporting), W47 (Store maintenance), W240 (DC maintenance), W7 (Accounts Payable - fee payments)

### Pain Points / Risks
- **Testing Lead Times**: Stack testing and wastewater analysis labs have long turnaround times (up to 3 weeks), which can cause permit lapse if not scheduled early.
- **Strict Effluent Standards**: DENR Administrative Order (DAO) 2016-08 enforces strict limits on phosphate, ammonia, and fecal coliform; failing water tests requires costly STP modifications.
- **Daily Non-Compliance Fines**: Operating a generator or STP without active permits carries statutory fines ranging from PHP 10,000 to PHP 200,000 per day of undocumented operation.

### Staffing Implication
- **Pollution Control Officer (PCO)**: Accountable for scheduling stack/effluent testing, document preparation, and EMB online portal management. Requires ~12 hours/year per store/DC.
- **Store / DC Manager**: Responsible for supporting EMB inspections and managing local STP/genset maintenance. ~4 hours/year per store/DC.

---

## W479. FDA License to Operate (LTO) for Household Hazardous Substances Compliance

| Field | Detail |
|---|---|
| **Trigger** | Annual license renewal cycle, or introduction of new regulated paints, thinners, varnishes, or solvent-based adhesives |
| **Frequency** | Renewed every 1 to 3 years depending on license validity period selected |
| **Volume** | Store-wide compliance across 200 retail stores selling chemical-based DIY goods, plus 4 DCs |
| **Owner** | Regulatory Compliance Manager |
| **Participants** | Qualified Person (technical representative), Category Managers, Store Managers, DC Managers, FDA Inspectors |

### Background

Under Republic Act No. 9711 (FDA Act of 2009) and FDA Circular 2020-025, establishments engaged in the manufacture, distribution, import, or retail sale of Household Hazardous Substances (HHS) must secure a valid License to Operate (LTO) from the Food and Drug Administration (FDA) of the Philippines. Regulated HHS products common in DIY hardware retail include solvent-based paints, varnishes, paint thinners, wood preservatives, chemical adhesives (like epoxy or contact cement), and household aerosol insecticides. Selling these products without an active LTO or distributing brands that lack a valid Certificate of Product Registration (CPR) results in immediate confiscation of stock, massive operational fines, and temporary store closure.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **SKU Compliance Screening**: Category Managers flag chemical, paint, and adhesive items in the SKU registry. Regulatory Compliance Manager cross-references each vendor's Certificate of Product Registration (CPR) against the FDA database to ensure all stock is legally registered. | Category Manager / Regulatory Compliance Manager | Regulatory Compliance Manager | 4 hours/quarter |
| 2 | **Technical Representative Assignment**: Regulatory Compliance Manager maintains the registered credentials of the designated "Qualified Person" (e.g. licensed pharmacist or chemist) required by the FDA to oversee chemical safety reporting. | Regulatory Compliance Manager | VP Legal & Compliance | Ongoing |
| 3 | **Site Inspection Audit**: Store and DC Managers inspect paint-mixing machines (W168) and hazardous chemical storage areas (W236) to verify compliance with FDA Good Distribution and Storage Practices (GDSP) guidelines (ventilation, warning signs, spill kits). | Store Manager / DC Manager | Regulatory Compliance Manager | 2 hours/store |
| 4 | **Documentation Package Compilation**: Qualified Person compiles application requirements: (a) Business permit, (b) Lease contract, (c) Location and floor plans showing hazmat storage layout, (d) Notarized Qualified Person affidavit, (e) List of products to be distributed. | Qualified Person | Regulatory Compliance Manager | 4 hours |
| 5 | **FDA Portal Submission**: Qualified Person uploads documents and submits the LTO renewal/initial application on the FDA ePortal; generates the electronic payment voucher. | Qualified Person | Regulatory Compliance Manager | 1 hour |
| 6 | **Application Fee Settlement**: Finance processes the FDA payment voucher (W7). Qualified Person uploads the official receipt to the portal to activate the application evaluation queue. | Finance / Qualified Person | Qualified Person | 1 day |
| 7 | **On-Site FDA Audit**: FDA inspectors conduct physical or virtual inspection of stores/DCs to verify proper storage segregation, emergency procedures, and technical documentation. | FDA Inspectors / Store Manager | DC Manager (for DCs) / Store Manager (for stores) | 4 hours |
| 8 | **LTO Issuance & ERP Release**: FDA issues the digital LTO. Regulatory Compliance Manager uploads the permit to the Document Registry (W255), updates the Compliance Calendar, and updates the SKU master regulatory flag, authorizing procurement (W2) and sales. | Regulatory Compliance Manager | — | 30 min |

### System Touchpoints
- Item Master (SKU regulatory flag, vendor CPR attachment)
- ERP Compliance Calendar (Expiry alerts at 180/120/90 days)
- Document Management System (W255) for archiving LTO files and inspection reports
- Integration with W168 (Custom Paint Mixing), W236 (Hazmat Storage), W237 (Hazmat Handling), W287 (Vendor Master), W2 (Procurement PO execution)

### Pain Points / Risks
- **Sales Freeze**: Expiration of the LTO halts all sales of high-margin paint, varnish, and chemical products across the network, leading to massive revenue loss.
- **Staffing Bottlenecks**: The FDA LTO is legally tied to the technical representative's license; if the technical representative resigns, the company has only 10 days to replace them or the LTO is suspended.
- **Vendor Certificate Expiry**: Hardware store vendors often fail to renew their individual product CPRs on time, creating regulatory liabilities for the retailer.

### Staffing Implication
- **Regulatory Compliance Manager**: Accountable for overall application strategy, vendor compliance audits, and FDA inspector coordination. ~30 hours/year.
- **Qualified Person**: Responsible for ePortal filings, product lists, and compliance reviews. Retainer/Full-time.
- **Store / DC Manager**: Supporting physical audits and onsite safety compliance. ~4 hours/year per store/DC.

---

## W480. CAAP Height Clearance Permit Compliance

| Field | Detail |
|---|---|
| **Trigger** | Construction of a new store/DC, major renovation, or installation of tall outdoor signage structures (pylon signs, cellular/radio antennas) near aerodromes |
| **Frequency** | Per construction project, or upon modification of tall structures in airport buffer zones |
| **Volume** | Relates to store/DC development projects located within 15 kilometers of airports |
| **Owner** | Engineering & Construction Director |
| **Participants** | Project Manager, Store Design Architect, CAAP Aeronautical Engineers, Geodetic Engineer, LGU Building Official |

### Background

Under Civil Aviation Authority of the Philippines (CAAP) regulations, any construction, structure, sign pylon, or antenna that may penetrate the Obstacle Limitation Surfaces (OLS) of aerodromes must obtain a Height Clearance Permit (HCP) (Height Clearance Certificate). The local government unit (LGU) Building Official will refuse to issue building permits (W54/W225) or occupancy permits (W227) without a valid CAAP clearance. Securing this permit requires certified geodetic surveys showing coordinates and elevations above mean sea level, aeronautical analysis by CAAP, and adherence to paint/lighting specifications (e.g. aviation warning lights).

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Flight Path Proximity Check**: During site feasibility (W116), Store Design Architect uses geographical coordinates (W310) to assess proximity to airport runways and determine if CAAP buffer zones apply. | Store Design Architect | Engineering & Construction Director | 2 hours |
| 2 | **Geodetic & Topographic Survey**: If the site is within CAAP buffer zones, Project Manager hires a CAAP-deputized Geodetic Engineer to perform an elevation survey and prepare a certified Geodetic Report detailing elevation and height. | Geodetic Engineer | Project Manager | 3 days |
| 3 | **Documentary Package Compilation**: Project Manager compiles the HCP application: (a) Certified Geodetic Report, (b) Site plans, (c) Elevation drawings showing highest point of structure/pylon sign, (d) Certified coordinate list. | Project Manager | Engineering & Construction Director | 4 hours |
| 4 | **CAAP Submission**: Project Manager submits the application to the CAAP Aerodrome Development and Management Service (ADMS) at the CAAP Main Office or regional office. | Project Manager | — | 2 hours |
| 5 | **Aeronautical Technical Study**: CAAP Aeronautical Engineers evaluate the proposed structure height against flight path models and airport radar lines of sight. | CAAP Engineers | — | 15–45 days |
| 6 | **Fee Settlement & Lighting Requirements**: Finance processes the CAAP study fees (W7). CAAP issues structural specifications (e.g. painting sign towers in aviation orange/white, installing warning lights (W173)). | Finance / Project Manager | Project Manager | 2 days |
| 7 | **HCP Certificate Issuance**: CAAP issues the final Height Clearance Permit specifying the maximum allowable height. | CAAP | — | 5 days |
| 8 | **LGU Permit Release & Archiving**: Project Manager submits the CAAP HCP to the LGU Building Official to secure the building permit (W54/W225); uploads the digital HCP copy to the Document Registry (W255). | Project Manager | Engineering & Construction Director | 1 day |

### System Touchpoints
- ERP Project Management Module (Store Construction W225 tasks, project budget)
- Location Master (Store coordinates W310, elevation data)
- Document Registry (W255) for HCP documents
- Integration with W116 (Site Selection), W223 (Store Design), W225 (Store Construction), W54 (LGU permits)

### Pain Points / Risks
- **Severe Project Delays**: CAAP's aeronautical evaluation can take 2 to 3 months; if not initiated early, it delays LGU building permit approval, pushing back store opening dates.
- **Signage Height Reduction**: If CAAP denies the original height proposal, store pylon signs must be shortened, reducing store visibility from major roads and highways, impacting initial marketing performance.
- **Operational Penalties**: Operating a structure without CAAP height clearance can result in legal injunctions, fines, and local government orders to demolish the non-compliant structure.

### Staffing Implication
- **Project Manager**: Responsible for hiring geodetic engineers, compiling files, and submitting CAAP documents. ~20 hours per construction project.
- **Store Design Architect**: Responsible for adjusting elevations and coordinate checking. ~8 hours per project.

---

## W485. BIR Branch Registration & RDO Transfer Management

| Field | Detail |
|---|---|
| **Trigger** | New store opening (W16); store relocation (W45); BIR Revenue District Office (RDO) boundary realignment; entity-level restructuring |
| **Frequency** | Event-driven (~10–15 new stores/year per growth plan; occasional relocations and RDO boundary changes) |
| **Volume** | 10–15 new registrations/year; 2–5 RDO transfers/year; 200+ active BIR-registered locations |
| **Owner** | Tax Accountant |
| **Participants** | Store Manager, Legal Head, Regulatory Officer, BIR RDO, Finance |

### Background

Every BuildRight Depot store and DC must be registered with the Bureau of Internal Revenue (BIR) as a branch of its respective legal entity. This registration includes: (a) securing a BIR Certificate of Registration (COR) per branch/location; (b) registering books of accounts and accounting systems (W54A — CAS registration); (c) obtaining Authority to Print (ATP) receipts and invoices; (d) registering point-of-sale systems and cash registers. When a store relocates to a new address or when the BIR reorganizes Revenue District Office (RDO) boundaries, the registration must be transferred to the correct RDO. With 200+ locations across the Philippines and ongoing expansion (~10–15 new stores/year), BIR branch registration is a continuous compliance workflow. W54A covers CAS registration specifically, but the broader branch registration and RDO transfer lifecycle is not covered by any existing workflow.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **Registration Requirements Gathering**: Tax Accountant prepares BIR branch registration requirements: (a) SEC Certificate of Incorporation or Certificate of Filing of Amended Articles (for the parent entity); (b) Mayor's Permit / Business Permit from LGU (W54); (c) lease contract or proof of business location (W117); (d) Bureau of Internal Revenue Form 1901 (Application for Registration); (e) valid IDs of authorized representative; (f) BIR Form 1905 (Application for Registration Information Update) for RDO transfers | Tax Accountant | Controller | 1–2 days/location |
| 2 | **BIR RDO Submission**: Tax Accountant or authorized representative submits registration application to the BIR Revenue District Office (RDO) having jurisdiction over the store location: (a) determine correct RDO using BIR RDO finder tool and the Address & Geographic Hierarchy Master (W310 — RDO mapping per municipality/city); (b) submit complete documentary requirements; (c) attend any BIR interview or verification as required | Tax Accountant | — | 1–2 days/RDO visit |
| 3 | **Certificate of Registration (COR) Issuance**: BIR issues the Certificate of Registration for the branch: (a) COR includes: TIN of parent entity, branch name, registered address, registered activities (retail sales), tax types (VAT, percentage tax, withholding tax); (b) BIR issues registered books of accounts; (c) BIR issues Authority to Print (ATP) for receipts and invoices | BIR RDO | — | 5–10 working days |
| 4 | **Books of Accounts & Receipt Registration**: Tax Accountant coordinates the registration of books and receipts: (a) register manual books of accounts (if applicable) or obtain authority for computerized books (linked to W54A — CAS registration); (b) register invoice/receipt format with BIR (must comply with BIR revenue regulations on registered sales invoices per POS-012); (c) obtain ATP for printed receipts; (d) update POS system with BIR-registered receipt format and serial number range per location | Tax Accountant / IT | Controller | 3–5 days |
| 5 | **System Configuration Update**: IT configures the ERP/POS for the new branch: (a) create new location in Location Master (W254) with BIR registration details (TIN, RDO code, COR number, ATP details); (b) configure BIR-sequential document numbering series per entity per document type (per MDM-017); (c) configure tax parameters for the new location in Tax Master (W293); (d) activate POS terminals at new store with registered receipt format; (e) enable BIR EIS API transmission for the new location (W473) | IT / Tax Accountant | CIO | 2–3 days |
| 6 | **RDO Transfer (Relocation)**: When a store relocates or RDO boundaries change: (a) Tax Accountant files BIR Form 1905 (Application for Registration Information Update) with the old RDO; (b) old RDO processes the transfer and forwards records to the new RDO; (c) new RDO issues updated COR with new RDO code; (d) Tax Accountant updates Location Master (W254) and Tax Master (W293) with new RDO code; (e) POS receipt format and serial numbers are updated if required by new RDO; (f) all open tax filings for the location are settled with the old RDO before transfer | Tax Accountant | Controller | 15–30 days (BIR processing time) |
| 7 | **Compliance Tracking & Calendar Update**: Tax Accountant updates the BIR compliance calendar: (a) register new location in BIR filing calendar with applicable tax types and filing deadlines; (b) update eFPS enrollment (W260) for the new location; (c) update BIR EIS API transmission enrollment (W473) for the new location; (d) update monthly tax filing (W90) with new location's tax obligations; (e) archive COR and ATP in document management system (W255) | Tax Accountant | Controller | 2–4 hours/location |
| 8 | **Annual Compliance Verification**: Tax Accountant performs annual verification of all 200+ BIR registrations: (a) confirm all locations have valid COR; (b) confirm ATP is not expired (typically valid for 5 years); (c) confirm RDO assignments are correct (especially after BIR reorganizations); (d) identify any locations with pending registration issues; (e) resolve discrepancies before annual tax filing season | Tax Accountant | Controller | 1–2 weeks/annual |

### System Touchpoints
- Location Master (W254): BIR registration status, COR number, RDO code, ATP details per location
- Tax & Regulatory Master (W293): tax code configuration per RDO
- Address & Geographic Hierarchy Master (W310): RDO-to-municipality mapping
- Fiscal Calendar & Posting Period Master (W308): BIR sequential numbering series per location
- BIR eFPS Portal (W260): location enrollment for electronic filing
- BIR EIS Portal (W473): location enrollment for e-invoicing transmission
- Document Management (W255): COR, ATP, and registration document archival
- POS Configuration: receipt format and serial number management per location
- Integration with W16 (new store opening), W45 (store closure/relocation), W54A (CAS registration), W54 (LGU permits), W254 (location master), W260 (eFPS filing), W473 (EIS transmission)

### Pain Points / Risks
- **BIR processing delays**: BIR RDO offices may take 5–30 working days to process branch registrations, especially in provincial RDOs with limited staff; this can delay new store openings (W16) if not initiated early enough
- **RDO jurisdiction confusion**: BIR RDO boundaries do not always align with LGU boundaries (municipality/city); a store in a border area may be misassigned to the wrong RDO, leading to tax filing rejections and penalties
- **ATP expiry**: Authority to Print receipts expires after 5 years; with 200+ locations, tracking ATP expiry dates and initiating renewals on time requires a robust calendar system; operating with an expired ATP risks BIR penalties
- **RDO transfer disruption**: During RDO transfer (store relocation), tax filing obligations may fall through the gap between old and new RDO; BuildRight must continue filing with the old RDO until the transfer is officially processed
- **Sequential numbering compliance**: BIR requires strict sequential numbering of invoices and receipts per location per document type; any gap in numbering can trigger a BIR audit (W77); adding new locations requires careful numbering series configuration to avoid conflicts

### Time Estimate
- New branch registration: 3–5 days elapsed (1–2 days Tax Accountant effort)
- RDO transfer: 15–30 days elapsed (2–3 days Tax Accountant effort)
- System configuration: 2–3 days per location
- Annual compliance verification: 1–2 weeks across all locations
- **Total annual effort**: ~60–80 hours/year for Tax Accountant across ~15–20 registration events and annual verification

### Staffing Implication
- **Tax Accountant**: ~60–80 hours/year for BIR branch registration management. Absorbed within existing Tax Accountant role.
- **IT**: ~2–3 days per new location for system configuration. Absorbed within existing IT provisioning duties (W152).
- **Store Manager**: Provides location-specific documents and facilitates BIR visits. ~2–4 hours/event. Absorbed.

---

## W802. LGU Local Business Tax Computation, Payment & Receipt Management

| Field | Detail |
|---|---|
| **Trigger** | Annual LGU Business Permit renewal per W54; quarterly local business tax payment schedule; new store opening per W16 |
| **Frequency** | Annual for permit renewal; quarterly for tax payment; per new store opening |
| **Volume** | 200 stores + 4 DCs + HQ = 205 locations across 100+ LGU jurisdictions; ~820 quarterly tax payments/year |
| **Owner** | Tax Manager |
| **Participants** | Finance, Store Managers, DC Managers, Legal, LGU Business Permit and Licensing Office (BPLO) |

### Background

Philippine Local Government Units (LGUs) impose Local Business Tax (LBT) on businesses operating within their jurisdiction under the Local Government Code (RA 7160). LBT is computed based on gross receipts or gross sales of the preceding year, with rates varying by LGU ordinance and business classification (retail, wholesale, services). For BuildRight's 200 stores across 100+ LGU jurisdictions, each LGU has its own tax ordinance, computation method, payment schedule, and receipt format. Failure to pay LBT results in surcharges (25% of tax due) and may prevent Business Permit renewal per W54. This workflow manages the computation, payment, and documentation of LBT across all BuildRight locations.

### Steps

| # | Activity | Role (R) | Role (A) | Duration |
|---|---|---|---|---|
| 1 | **LGU Tax Ordinance Maintenance**: Tax Manager maintains database of LGU tax ordinances: (a) for each LGU where BuildRight operates: tax rate, computation basis (gross receipts vs. gross sales), business classification, payment schedule (annual, quarterly), payment method (cash, check, online), required forms; (b) monitor LGU ordinance amendments that change tax rates or computation methods; (c) system stores LGU tax parameters linked to Location Master per W254 and Tax Master per W293 | Tax Manager | Finance Controller | 2-3 days/year maintenance |
| 2 | **Annual Tax Computation**: During W54 Business Permit renewal period (typically January): (a) system extracts prior-year gross receipts per location from Financial module per W9; (b) system applies LGU-specific tax rate and computation method; (c) Tax Manager reviews computed tax per location for accuracy; (d) compare to prior year: flag locations with >20% tax increase for review; (e) identify any LGU ordinance changes that affect computation; (f) produce LBT computation schedule for all 205 locations | Tax Manager / System | Finance Controller | 1-2 weeks |
| 3 | **Tax Payment Execution**: Per LGU payment schedule: (a) prepare payment documents per LGU requirements: tax computation form, declaration of gross receipts, supporting schedules; (b) execute payment: cash or manager's check per LGU acceptance; some LGUs now accept online payment via LGU portal; (c) obtain Official Receipt from LGU; (d) record payment in AP module per W7; (e) file LGU Official Receipt in Document Management System per W255; (f) system tracks payment status: paid, pending, overdue with escalation alerts | Tax Admin / Store Manager | Tax Manager | 1-2 days per payment cycle |
| 4 | **New Store Tax Registration**: When new store opens per W16: (a) Tax Manager determines applicable LGU tax classification for the new location; (b) compute first-year estimated LBT based on projected gross receipts; (c) include LBT in store opening budget per W21; (d) register for LBT payment with LGU BPLO as part of Business Permit application per W54; (e) add LGU tax parameters to system per Step 1 | Tax Manager | Finance Controller | 1-2 days per new store |
| 5 | **Quarterly Reconciliation**: Quarterly, Tax Manager reconciles: (a) actual quarterly payments vs. annual computation (are we on track); (b) any mid-year LGU ordinance amendments that change rates; (c) any locations with overdue payments and surcharges; (d) update system with actual payment data for full-year reconciliation; (e) flag any LGU audit notifications for VP Legal review | Tax Manager | Finance Controller | 2-3 days/quarter |
| 6 | **Annual Reconciliation & Provision**: At year-end per W9B: (a) reconcile total LBT paid vs. actual tax liability based on final gross receipts; (b) if underpaid: settle balance before Business Permit renewal per W54; (c) if overpaid: determine if LGU allows credit against next year's tax; (d) compute next-year LBT provision for budgeting per W26; (e) record LBT expense in correct GL account per LGU per W9 | Tax Manager / Finance Controller | CFO | 3-5 days |

### System Touchpoints

- LGU Tax Parameter Master linked to Location Master per W254
- Financial module for gross receipts extraction per location
- Tax computation engine with LGU-specific rate tables
- AP module per W7 for payment processing
- Document Management System per W255 for Official Receipt filing
- Compliance calendar per W506 for payment deadline tracking
- Budget module per W26 for annual LBT provision
- New store opening integration per W16 for initial tax registration

### Pain Points / Risks

- **100+ LGU jurisdictions with different rules**: no two LGUs have identical tax ordinances; maintaining accurate tax parameters for 205 locations across 100+ LGUs is complex and error-prone
- **LGU ordinance amendments without notice**: LGUs may amend tax ordinances mid-year without proactive notification to taxpayers; BuildRight may underpay and face surcharges
- **Gross receipts definition varies by LGU**: some LGUs define gross receipts as total revenue, others exclude VAT, others exclude intercompany revenue; incorrect interpretation leads to underpayment or overpayment
- **Manual payment processes**: many LGUs still require in-person payment with manager's check; 205 locations x 4 quarterly payments = 820 payment transactions, many requiring physical presence
- **Surcharges for late payment**: 25% surcharge on unpaid tax plus 2% monthly interest; a PHP 500K annual LBT paid 1 month late incurs PHP 125K surcharge + PHP 10K interest
- **LGU audit risk**: LGUs may conduct tax audits comparing BuildRight's declared gross receipts against other data sources (BIR filings, SEC reports); discrepancies create audit exposure

### Staffing Implication

- **Tax Manager**: ~4-6 hours/month on LBT management; absorbed by existing role
- **Tax Admin**: ~2-3 days/quarter on payment processing and receipt management; absorbed by existing admin role
- **Store Managers**: ~30 min/quarter per store on local payment facilitation; absorbed by existing role
- **No incremental headcount**.

### Time Estimate

- LGU ordinance maintenance: 2-3 days/year
- Annual tax computation: 1-2 weeks
- Quarterly payment processing: 1-2 days per cycle
- Quarterly reconciliation: 2-3 days
- Annual reconciliation: 3-5 days
- **Total annual LBT management effort**: ~30-40 person-days
