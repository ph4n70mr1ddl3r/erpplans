# VS-162: Customer Pickup Truck & Cargo Van Rental (Self-Haul) Operations

> **Sell & Serve** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Customer self-haul vehicle-rental workflows for BuildRight Depot Corp. — owning the **"rent-a-truck"
in-store service** by which a customer who has just bought bulky/large merchandise (lumber packs,
cement/tile pallets, appliances, sheet goods, fencing, plumbing/fixtures) but arrived without a
suitable vehicle rents a **BuildRight-owned pickup truck or cargo van** for a short window (typically
75 minutes flat-rate, then an hourly/mileage rate) to take the purchase home or to the jobsite the
same day — the well-known "Load N Go" / "make it fit" capability operated by every major big-box
home-improvement retailer (Home Depot, Lowe's, Menards, Leroy Merlin) but **genuinely uncovered in
BuildRight's workflow inventory**.

This matters at BuildRight's scale and format. **55% of revenue is B2C walk-in** (profile §9.1) and
the big-box format sells **bulky, heavy, jobsite-bound merchandise** — lumber & building materials
(14% of SKUs), tiles & flooring (12%), appliances (5%), and furniture (5%) — much of it too large
for a typical sedan/UV and uneconomical to pay a last-mile delivery fee (VS-06.3 charges
weight/distance, free only above PHP 5,000) for a single trip. A store-level self-haul fleet converts
the otherwise-lost "I can't get it home" sale (a documented basket-abandonment driver in big-box
retail) into a completed, same-day transaction, and earns incremental **rental revenue + fuel
recovery + insurance waiver income** on top of the merchandise sale. Across 200 stores, even a small
fleet (2–3 trucks + 1 cargo van per store ≈ 600–800 vehicles group-wide) materially lifts
large-item attach and customer convenience. The same fleet is the cleanest substitute for the
~500–600 DSD bulky receipts/month (profile §7.1) when a vendor's own delivery falls through.

Today this discipline is **unowned as a program**. The defining terms — "pickup truck rental",
"cargo van rental", "self-haul rental", "rent-a-truck", and "customer vehicle rental" — appear in
**zero** PA files as dedicated workflow headers. The capability is **not** covered by **VS-06
(Logistics & Fleet)**, which moves BuildRight's *goods* in BuildRight's delivery trucks with
BuildRight drivers (W196/W197/W199/W653) and is governed by LTFRB cargo-freight licensing — this
value stream rents a *vehicle to the customer* for the customer to self-drive, under a passenger-
/for-hire-style rental contract, a fundamentally different operating model, risk profile, and
regulatory regime. It is **not** covered by **VS-12.2 (Tool & Equipment Rental)**, which rents
*items* (jackhammers, tile cutters, generators per W139) under a deposit-and-return merchandise-
rental model — this rents *titled, registered motor vehicles* requiring LTO registration, compulsory
motor-vehicle insurance, driver-license verification, and motor-vehicle-liability law. It is **not**
covered by **VS-74 (Contractor Jobsite Delivery)** or **VS-56 (Third-Party Delivery Partner)**, which
are *delivery services* (BuildRight or a 3PL delivers) — this is *customer self-haul*. And it is
**not** covered by **VS-141 (Employee Transport)**, which moves *BuildRight employees* — this moves
*customers in rented vehicles*. The closest existing touchpoint is the lumber-yard "customer load"
assistance (W438 Yard Dispatch & Loading, W1281 Lumber Yard Operations in VS-07.1) which *helps the
customer load their own vehicle* but does not *provide the vehicle*.

This value stream owns the end-to-end self-haul rental discipline: fleet strategy/sizing/acquisition
and lifecycle (procurement, LTO registration, MVIR, compulsory CTPL + comprehensive motor-vehicle
insurance, telematics/GPS, preventive maintenance, remarketing); the rental transaction at the
rental desk / Pro Desk (driver-license verification, age/eligibility, liability waiver & damage
waiver upsell, security deposit/hold, time-and-mileage capture, return inspection, fuel/cleaning
policy, billing/settlement); and incident/damage/traffic-violation/insurance-claim handling, theft/
non-return recovery, DOLE/LTO/LTFRB regulatory compliance, and rental revenue/utilization analytics.
It is designed to integrate tightly with VS-07.1 (yard dispatch & loading of the rented vehicle),
VS-08 (rental agreement & deposit capture at POS, W139 pattern extended to vehicles), VS-12.2
(rental-operations playbook), VS-06 (fleet maintenance shared standards), and VS-23 (vehicle theft/
non-return).

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-162.1](PA-162.1-rental-fleet-strategy-acquisition-and-lifecycle-management.md) | Rental Fleet Strategy, Acquisition & Lifecycle Management | 8 |
| [PA-162.2](PA-162.2-rental-transaction-counter-operations-and-customer-onboarding.md) | Rental Transaction, Counter Operations & Customer Onboarding | 8 |
| [PA-162.3](PA-162.3-incident-damage-compliance-and-rental-analytics.md) | Incident, Damage, Compliance & Rental Analytics | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
