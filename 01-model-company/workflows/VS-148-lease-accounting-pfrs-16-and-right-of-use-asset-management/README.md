# VS-148: Lease Accounting (PFRS 16/IFRS 16) & Right-of-Use Asset Management

> **Finance** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Lease Accounting (PFRS 16/IFRS 16) & Right-of-Use (ROU) Asset Management workflows for
BuildRight Depot Corp. — owning the **lease-accounting discipline** across the 5-entity group's
extensive lease portfolio. BuildRight operates ~205 sites (200 stores + 4 DCs + HQ + regional
offices), most **leased** from third-party landlords or, for the ~205 store/DC/office sites, from
its own **BuildRight Property Management, Inc.** (intercompany lessor, profile §2). Beyond real
estate, the group leases forklifts/reach trucks, fleet (80% third-party trucks), IT/POS hardware,
store fixtures, and equipment — a large, heterogeneous lease portfolio recognized under **PFRS 16
(the Philippine equivalent of IFRS 16)** which, since 2019, brings almost all leases onto the
balance sheet as a **right-of-use asset** and a **lease liability**.

Today this discipline is **unowned as a program**. "right-of-use", "lease liability", "ROU asset",
and "PFRS 16" appear in **zero** PA files as dedicated workflow headers (only scattered single-step
mentions). The capability is sprinkled inside VS-42 (Property & Lease Administration — owns the
*lessee commercial administration*: rent payment, rent review, lease *negotiation*, not the
*accounting recognition*), VS-17.3 (Tax & Statutory — touches the *deduction* side), VS-18
(Treasury — touches *cash* impact), VS-20.1 (Real Estate — site selection/lease *intake*), VS-35
(Fixed Asset — *owned* assets, not ROU), and VS-29 (Master Data — *contract* records). No value
stream owns the end-to-end PFRS 16 lease-accounting program: portfolio discovery & identification,
contract abstracting, discount-rate/term/payment determination, classification & exemption,
initial recognition (ROU asset + lease liability), transition, subsequent measurement
(depreciation, interest, payment unwind), modification/reassessment/renewal/termination, sublease
& lease-back, short-term/low-value exemption, intercompany/consolidation elimination, period-end
close & disclosure, system configuration, audit/control, and tax handling.

This is distinct from **VS-42 (Property & Lease Administration)** which owns the *commercial*
lease administration (negotiate, pay, administer) — this value stream owns the *accounting
recognition & measurement* of those leases. It is distinct from **VS-35 (Fixed Asset Management)**
which owns *owned* fixed assets — this value stream owns the *right-of-use* asset (a separate
PFRS 16 asset class). It is distinct from **VS-97 (Corporate Real Estate / Property Portfolio)**
which owns BuildRight as **lessor/property-owner/investor** — this value stream owns BuildRight as
**lessee** (and the lessor-side sublease accounting that flows back, W4421). It is distinct from
**VS-17.3 (Tax)** which handles tax *deductions* — this value stream handles the PFRS 16
*recognition/measurement* that drives the numbers. It is distinct from **VS-72 (Intercompany)** at
the *settlement* level — this value stream handles the *consolidation elimination* of intercompany
leases.

BuildRight's exposure is structural: at ~205 sites and a multi-entity structure with substantial
real-estate and equipment leasing, the ROU asset and lease liability are material balance-sheet
items; mis-recognition (missed leases, wrong discount rate, missed modifications, mishandled
intercompany) distorts EBITDA/EBIT, leverage covenants, and the audited PFRS financials, and
creates SEC/BIR/auditor findings. PFRS 16 also carries heavy disclosure and judgment areas
(discount rate, lease term, renewal options, variable payments) that require a dedicated program.

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-148.1](PA-148.1-lease-portfolio-identification-recognition-and-pfrs-16-transition.md) | Lease Portfolio Identification, Recognition & PFRS 16 Transition | 8 |
| [PA-148.2](PA-148.2-rou-asset-and-lease-liability-measurement-modification-and-reporting.md) | ROU Asset & Lease Liability Measurement, Modification & Reporting | 8 |
| [PA-148.3](PA-148.3-lease-administration-compliance-and-optimization-analytics.md) | Lease Administration, Compliance & Optimization Analytics | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
