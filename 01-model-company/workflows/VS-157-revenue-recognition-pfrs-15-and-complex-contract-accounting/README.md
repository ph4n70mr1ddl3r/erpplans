# VS-157: Revenue Recognition (PFRS 15) & Complex Contract Accounting

> **Finance** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Revenue Recognition (PFRS 15) & Complex Contract Accounting workflows for BuildRight Depot Corp. —
owning the enterprise **revenue-accounting discipline** by which BuildRight applies the PFRS 15
(*Revenue from Contracts with Customers*) five-step model — and its companions PAS 18 (contract
costs) and PAS 37 (contract liabilities) — across the full spectrum of non-straightforward
revenue arrangements that a PHP 62.3B, 5-entity, omnichannel hardware retailer now operates:
loyalty-points earning (600K members), gift cards & stored value, layaway & customer deposits,
product + installation bundles, consignment / VMI sell-through, subscription & recurring services,
extended warranty, project/contractor over-time billing, retail-media (agency vs. principal),
marketplace operator commissions, cash-on-delivery, in-store value-added/financial-agency
services, trade-in/buy-back, and captive/construction-finance referral flows.

Today this discipline is **unowned as a program**. The single workflow **W487 ("Revenue
Recognition Review — PFRS 15 Complex Scenarios")** sits inside VS-15.1 (Invoice Processing &
Matching — an operationally inappropriate home), is referenced across 12 PA files, and explicitly
acknowledges it is over-stuffed: it lists eleven revenue streams requiring assessment and states
"Existing workflows cover the operational execution of these revenue streams but not the PFRS 15
accounting assessment." Each revenue channel carries its own one-off recognition workflow in its
operational value stream (W2014 retail media, W1971 government, W1992 subscription, W4618 VAS,
W1771 installment, W1017 scrap/recyclables) and the deferred-revenue / SSP / breakage accounting is
sprinkled across VS-13 (loyalty W104), VS-54 (gift card W28), VS-17.4 (FP&A), and VS-15.1 (W487) —
but no value stream owns the **end-to-end contract-accounting discipline**: contract
identification/combination/modification, performance-obligigation analysis, principal-vs-agent
(gross-vs-net) determination, standalone-selling-price methodology, transaction-price allocation,
variable-consideration constraint, deferred-revenue measurement, contract-cost capitalization,
period close & journal-entry cycle, AFS disclosure-schedule preparation, and external-audit
coordination.

This is distinct from **VS-118 (Revenue Assurance, Pricing Integrity & Leakage Management)** which
protects revenue from **pricing/promo/refund leakage at the transaction** — this value stream owns
the **PFRS 15 accounting of revenue already booked** (when, how much, in which entity, gross or
net, current or deferred). It is distinct from **VS-17.4 (FP&A)** which plans and reports — this
value stream executes the recognition accounting. It is distinct from each **channel value stream**
(VS-10/VS-11/VS-13/VS-45/VS-47/VS-48/VS-53/VS-54/VS-92/VS-95/VS-142/VS-154/VS-155/VS-156) which
operates the channel — this value stream owns the accounting consequence.

BuildRight's exposure is structural: at ~PHP 62.3B revenue with a fast-expanding multi-element
arrangement portfolio (loyalty points liability on every one of 2.8M monthly POS transactions,
gift-card breakage, ~515K ecommerce orders/yr with mixed-basket multi-origin fulfillment, growing
retail-media and marketplace commission flows, and new captive/construction-finance/trade-in
services from Pass 17), mis-recognition distorts EBITDA, deferred-revenue balances, the audited
PFRS financials, and the 5-entity consolidation — and external-audit scrutiny of PFRS 15 is among
the highest-judgment areas in the annual audit.

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-157.1](PA-157.1-multi-element-arrangement-identification-and-performance-obligation-assessment.md) | Multi-Element Arrangement Identification & Performance Obligation Assessment | 8 |
| [PA-157.2](PA-157.2-standalone-selling-price-allocation-and-deferred-revenue-measurement.md) | Standalone Selling Price, Allocation & Deferred-Revenue Measurement | 8 |
| [PA-157.3](PA-157.3-period-close-disclosure-audit-and-new-revenue-stream-onboarding.md) | Period Close, Disclosure, Audit & New-Revenue-Stream Onboarding | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
