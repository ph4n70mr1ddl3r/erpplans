# VS-163: Electric Vehicle (EV) Charging Station Host Network Operations

> **Asset & Infrastructure** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Electric Vehicle (EV) charging-station host-network workflows for BuildRight Depot Corp. — owning
the discipline by which BuildRight, as the **property host and network operator**, deploys and
operates EV charging infrastructure across its ~205 large, high-traffic, parking-rich sites
(200 stores at 8,000–15,000 sqm + 4 DCs + HQ), turning its real-estate + energy footprint into a
customer-traffic, basket-attach, and decarbonization asset as Philippine vehicle electrification
accelerates under the **Electric Vehicle Industry Development Act (RA 11697, 2022)** and its
implementing rules.

This matters for BuildRight specifically. The company **sells EV charging products as merchandise**
(in the Electrical category, profile §6.2), already owns an **on-site renewable / prosumer energy
program** with large solar-equipped rooftops and storage (VS-108), runs an **energy-efficiency and
RA 11285 compliance program** (VS-120), and operates a **"Home Building Partner" / sustainability
brand** (VS-25 ESG). Hosting EV charging at its own sites is the natural convergence: it (a)
captures the **dwell-time basket** (an EV driver charging 20–45 min is a high-intent shopper), (b)
monetizes BuildRight's own surplus solar/storage generation (VS-108) through EV energy sales, (c)
advances the decarbonization/ESG target (VS-25), and (d) future-proofs ~205 prime parking assets
against the EV transition (RA 11697 mandates a share of EVs in corporate and government fleets, and
 mandates charging infrastructure in certain new buildings/parking facilities). Across 200 stores,
 even a modest host footprint (2–6 charge points per site ≈ 400–1,200 ports group-wide) is a
 material energy/customer-experience asset.

Today this discipline is **unowned as a program**. The defining terms — "EV charging station host",
"EVSE host network", "charging network operator", "OCPI roaming", and "EV charge point operations" —
appear in **zero** PA files as dedicated workflow headers (the ~28 incidental "charging station" /
"EV charg" references are scattered, almost all about selling chargers as merchandise or generic
energy mentions). The capability is **not** covered by **VS-108 (On-Site Renewable Energy &
Prosumer Asset Operations)**, which generates clean energy for **BuildRight's own consumption**
(behind-the-meter, net-metering, REC) — this value stream operates charging infrastructure that
sells energy/services to **EV drivers** (a distinct customer-facing, public-facing, regulated-as-a-
service operation with roaming/billing/access). It is **not** covered by **VS-120 (Energy Efficiency
& RA 11285 Compliance)**, which manages BuildRight's own energy consumption/efficiency — this is an
energy **sales/service** operation. It is **not** covered by **VS-06 (Logistics & Fleet)** or
**VS-61 (Fuel & Fleet Cost)**, which fuel/maintain BuildRight's own (today diesel) delivery fleet —
though this value stream does own the **forward path for BuildRight's own EV-fleet charging**
(green-fleet transition) as a host-side capability. It is **not** covered by **VS-138 (Integrated
Facilities Management)**, which maintains buildings — charging-station operations is a specialized
high-voltage EVSE discipline. And it is **not** covered by **VS-14 (Marketing)** or **VS-25 (ESG)**
which consume the capability (drive-to-store traffic, decarbonization reporting) but do not operate
it.

This value stream owns the end-to-end host-network discipline: charging-network strategy & business
model (own-operate vs host-partner with a Charge Point Operator like EVgo/Petron EV/Meralco EV, site
selection, host-revenue/lease structure, customer-experience integration with loyalty VS-13 and the
app VS-75); station deployment, grid/utility coordination (with Meralco/electric cooperatives,
demand-charge management, integration with BuildRight's own solar/storage VS-108), and
billing/payment/roaming (OCPI/OCPP, RFID/app/QR access, acquirer settlement VS-80); and operations,
preventive/reactive EVSE maintenance (specialized high-voltage), accessibility (PWD-accessible
charge bays, RA 7277), safety/incident (PERA/DOLE/Energy Regulatory Board), regulatory compliance
(ERB, LGU, EMB), host-revenue settlement, and network uptime/analytics. It integrates tightly with
VS-108 (own generation/storage), VS-120 (energy), VS-138 (facility power infrastructure), VS-80
(payment/settlement), VS-13/VS-75 (loyalty/app), and VS-25 (decarbonization reporting).

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-163.1](PA-163.1-charging-network-strategy-siting-and-host-partnering.md) | Charging Network Strategy, Siting & Host Partnering | 8 |
| [PA-163.2](PA-163.2-station-deployment-energy-integration-and-roaming-payment.md) | Station Deployment, Energy Integration & Roaming/Payment | 8 |
| [PA-163.3](PA-163.3-operations-maintenance-compliance-and-network-analytics.md) | Operations, Maintenance, Compliance & Network Analytics | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
