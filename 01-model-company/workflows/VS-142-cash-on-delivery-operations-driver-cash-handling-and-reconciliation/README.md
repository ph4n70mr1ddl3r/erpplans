# VS-142: Cash-on-Delivery (COD) Operations, Driver Cash Handling & Reconciliation

> **Finance** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Cash-on-Delivery (COD) Operations, Driver Cash Handling & Reconciliation workflows for BuildRight
Depot Corp. — owning the enterprise **COD cash-chain discipline** for ecommerce and B2B/micro-
wholesale orders where the customer pays **cash at the doorstep** rather than online. The
Philippines is a COD-dominant ecommerce market, and BuildRight accepts COD explicitly
(model-company-profile §8.1). With ~42,900 ecommerce orders/month plus sari-sari/MSME micro-
wholesale (VS-82) and trade deliveries (VS-74), a large share of orders settle as cash collected
by a third-party last-mile driver or BuildRight's own crew — a multi-party physical-cash chain
(driver → 3PL/branch → BuildRight → bank) that runs entirely outside the card/acquirer settlement
rail (VS-80) and is reconcilable only with a dedicated program.

Today this discipline is **unowned as a program**. Only two COD-adjacent workflows exist —
**W2837 (MSME Cash-on-Delivery)** inside VS-82 (sari-sari/MSME micro-wholesale) and
**W1202 (Store Daily Cash Collection)** in VS-07 — neither owns the **consumer/B2B ecommerce
COD operating model**. The defining terms — "COD operations", "driver cash handling", "COD
reconciliation", "cash-on-delivery settlement" — appear in **zero** PA files as dedicated workflow
headers. COD touches are scattered as single steps inside VS-06.3 (last-mile delivery), VS-08.2
(cash management), VS-10.2 (ecommerce fulfillment), VS-16.3 (customer payment), VS-80 (payment
ops), and VS-56 (3PL partners) — but no value stream owns the end-to-end **COD program**: COD
policy & risk framework, order eligibility/limits, cash collection & custody at the doorstep, the
driver/3PL cash remittance chain, daily reconciliation of cash collected against thousands of
orders, COD refusal/return handling, COD fraud (phantom orders, driver theft, refund/short-pay
abuse), COD float/working-capital impact, COD insurance/bonding, and COD settlement to the bank
and the GL.

This is distinct from **VS-80 (Payment Operations, Acquirer & Settlement)** which owns the
**electronic** payment rail (card/e-wallet/acquirer/settlement/chargeback) — this value stream
owns the **physical-cash** rail collected in the field by drivers. It is distinct from **VS-06.3
(Last-Mile & Delivery Partners)** which **delivers** the parcel — this value stream owns the
**cash** collected at that delivery. It is distinct from **VS-08.2 (Payment & Cash Management)**
which owns **in-store** cash at the POS — this value stream owns cash collected **off-site, in the
field**. It is distinct from **VS-81 (Cash-in-Transit/Vault)** which moves **BuildRight's own**
banked cash under armed escort — this value stream governs **customer** cash flowing *inward*
from the doorstep. It is distinct from **VS-82 (Sari-Sari/MSME)** whose single W2837 handles
MSME-segment COD — this value stream owns the **enterprise COD program** across consumer ecommerce,
trade, and MSME. COD is the **physical-cash-on-delivery** discipline — distinct from electronic
payments, delivery execution, in-store cash, armored inbound, and the MSME segment.

BuildRight's exposure is structural: COD is the single largest reconciliation, working-capital,
and fraud vector in a COD-heavy market — at ~42,900 ecommerce orders/month, even a 30–50% COD
share means **~13,000–21,000 COD orders/month** (~150,000–250,000/yr), each carrying physical cash
through a 3- or 4-party chain with float (inventory and cash in motion until collected),
short-pay/refusal risk, and theft/fraud exposure; unreconciled COD cash directly distorts revenue
(VS-17.4), inventory (VS-05), and AR (VS-16), and a weak COD program is a top source of leakage
benchmarked at 0.3–1.0% of COD GMV.

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-142.1](PA-142.1-cod-program-design-policy-and-risk-framework.md) | COD Program Design, Policy & Risk Framework | 8 |
| [PA-142.2](PA-142.2-cod-cash-collection-custody-and-driver-3pl-reconciliation.md) | COD Cash Collection, Custody & Driver/3PL Reconciliation | 8 |
| [PA-142.3](PA-142.3-cod-settlement-working-capital-fraud-and-analytics.md) | COD Settlement, Working-Capital, Fraud & Analytics | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
