# VS-118: Revenue Assurance, Pricing Integrity & Leakage Management

> **Finance** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Revenue Assurance, Pricing Integrity & Leakage Management workflows for BuildRight Depot Corp. —
governing the **revenue-assurance program** that detects, quantifies, prevents, and recovers
revenue **leakage** across every monetization channel. At ~PHP 62.3B annual revenue, the company
processes ~2.8M POS transactions/month across 600 terminals (profile §5), ~42,900 ecommerce
orders/month (profile §8.5), ~3,500 AR invoices/month across ~5,400 trade/corporate accounts
(profile §10.3), ~515K ecommerce orders/year, a ~600K-member loyalty program, gift-card and
stored-value programs, marketplace (3P seller) and retail-media revenue, catch-weight and
cut-length selling (lumber/board-foot, wire/meter, nails bulk), and a complex promotional /
mandatory-discount / tax-exempt pricing landscape. Industry benchmarks place retail revenue
leakage at **1–3% of gross revenue** — for BuildRight that is **PHP 0.6B–1.9B per year** at risk
from pricing errors, promo/loyalty/gift-card mis-application, refund and reversal fraud,
catch-weight/weighing inaccuracies, discount-stacking abuse, VAT/tax mis-calculation, payment
and settlement discrepancies (MDR/fees), ecommerce/marketplace settlement gaps, and POS-to-GL
data-integrity failures.

Today the program is reduced to a single monthly-audit workflow — **W348 (Revenue Assurance &
Payment Gateway Audit)** in VS-21.3 (specialized audit domains) — which performs a backward-
looking monthly reconciliation of POS-to-bank deposits, MDR verification, override review,
loyalty/gift-card audit, and a POS-to-GL data-integrity test. The full revenue-assurance program
is unowned: a continuous leak-detection framework spanning all channels and revenue waterfalls;
pricing/promo/loyalty/gift-card/mandatory-discount/tax-exempt integrity monitoring in near-real-
time; catch-weight/cut-length measurement-based revenue assurance; ecommerce/marketplace/3P
settlement assurance; refund/reversal leakage; leakage quantification, root-cause, recovery and
corrective action; fraud/collusion/abuse revenue-loss investigation; revenue-assurance technology
and automation; and multi-entity (5 legal entities) consolidated revenue assurance. This value
stream consolidates the discipline: strategy/governance/leak-detection framework; pricing/
promotion/loyalty/payment integrity monitoring across all channels; and leakage recovery,
analytics and continuous assurance.

This is distinct from **VS-21.3 (Internal Audit – Specialized Domains)** which performs the
*periodic audit* of revenue (this value stream owns the *continuous, operational* revenue-
assurance program — of which the W348 audit becomes one backward-looking control). It is distinct
from **VS-23 (Loss Prevention)** which addresses *inventory shrink and theft* (this value stream
addresses *revenue leakage* — the failure to capture revenue that should have been earned, a
different loss vector from physical shrink). It is distinct from **VS-08 (POS/Checkout)** which
*executes* the transaction (this value stream *assures* the transaction captured the correct
revenue). It is distinct from **VS-17.4 (FP&A)** which *reports* revenue (this value stream
*protects* revenue before it is reported). It is distinct from **VS-13 (Loyalty) / VS-54 (Gift
Card) / VS-58 (Promotions) / VS-85 (Mandatory Discount)** which *operate* those programs (this
value stream *assures* their financial integrity — that points/gift-card value/discounts were
correctly applied and not abused). It is distinct from **VS-80 (Payment Operations)** which
*operates* the payment/acquirer relationship (this value stream *assures* that payment and
settlement amounts reconcile to revenue). Revenue assurance is the *revenue-protection and
leakage-management* discipline — distinct from audit, loss prevention, POS execution, FP&A, the
loyalty/gift-card/promo/discount programs, and payment operations.

BuildRight's exposure is structural: high transaction volume, many monetization mechanisms, a
complex Philippine pricing/tax/discount landscape, and 5 legal entities. Without a dedicated
owner, BuildRight risks persistent, undetected revenue leakage (each 0.5% = ~PHP 311M/year),
audit findings, and compounding loss — risks that no existing value stream owns end-to-end.

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-118.1](PA-118.1-revenue-assurance-strategy-governance-and-leak-detection-framework.md) | Revenue Assurance Strategy, Governance & Leak Detection Framework | 8 |
| [PA-118.2](PA-118.2-pricing-promotion-loyalty-and-payment-integrity-monitoring.md) | Pricing, Promotion, Loyalty & Payment Integrity Monitoring | 8 |
| [PA-118.3](PA-118.3-leakage-recovery-revenue-analytics-and-continuous-assurance.md) | Leakage Recovery, Revenue Analytics & Continuous Assurance | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
