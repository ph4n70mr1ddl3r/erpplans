# VS-125: Cross-Channel Fraud Management & Payment Fraud Protection

> **Finance** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Cross-Channel Fraud Management & Payment Fraud Protection workflows for BuildRight Depot Corp. —
owning the **enterprise fraud program** that protects ~PHP 62.3B annual revenue across 2.8M monthly
POS transactions (600 terminals), ~42,900 ecommerce orders/month, COD, ~600K loyalty members, gift
cards/stored value, coupon/promo, returns/refunds, trade/B2B accounts, and ~PHP 5.19B monthly
payments flowing through cash, card, e-wallet (GCash/Maya), and bank channels. Retail fraud
benchmarks of 0.5–1.5% of gross revenue put **PHP 0.3B–0.9B/yr** at risk across payment fraud,
return/refund abuse, promo/coupon/loyalty abuse, gift-card fraud, account takeover, first-party/
friendly fraud, chargebacks, employee/internal collusion, and trade-account/application fraud.

Today this discipline is **unowned as a program**: fraud detection is referenced across ~17 PA
files and specific fraud types are handled as single steps within adjacent value streams — return
fraud as a step in VS-32.1 (W returns processing), coupon fraud as a single workflow in VS-58.2
(coupon-redemption fraud), payment/chargeback fraud as steps in VS-80 (payment operations), loyalty
fraud as a step in VS-13.2 (loyalty operations), promo abuse in VS-14/VS-58, account takeover in
VS-10/VS-91, physical shrink in VS-23 (loss prevention), pricing/promo leakage in VS-118 (revenue
assurance), and AML/KYC/sanctions in VS-86 — but no value stream owns the **cross-channel fraud
program**: detection rules and ML models, fraud orchestration, case management, investigations,
recovery/restitution, chargeback representment, internal/employee fraud, regulatory/law-enforcement
coordination, and fraud analytics/loss-rate reporting. 'fraud orchestration' appears in **zero** PA
files, 'fraud management' in one, and 'first-party fraud'/'chargeback fraud' in one each.

This is distinct from **VS-23 (Loss Prevention & Asset Protection)** which owns physical shrink,
theft, and in-store security (this value stream owns *transactional and financial fraud* across
channels). It is distinct from **VS-118 (Revenue Assurance)** which owns pricing/promo/tax/refund
*leakage* from process or configuration error (this value stream owns *intentional fraud* by
customers, employees, or third parties). It is distinct from **VS-80 (Payment Operations)** which
operates the acquirer/settlement plumbing (this value stream owns the *fraud controls* layered on
top of payments). It is distinct from **VS-86 (Anti-Financial Crime)** which owns AML/KYC/sanctions/
anti-corruption compliance (this value stream owns *retail/commercial fraud*, not money-laundering
compliance). It is distinct from **VS-91 (Consumer Data Privacy)** which owns personal-data
protection (this value stream owns *account-takeover and identity-fraud prevention* as a fraud
control, working alongside privacy). Cross-channel fraud management is the *enterprise fraud-risk*
discipline — distinct from physical loss prevention, revenue-leakage assurance, payment operations,
AML, and data privacy.

BuildRight's exposure is structural: high-volume low-margin retail (2.8M POS txns/month at PHP 1,800
ATV, ~12–14% EBITDA) where a small fraud-loss rate moves millions of pesos, COD and e-wallet
tenders that are reversible and identity-light, a fast-growing ecommerce channel (~515K orders/yr)
with card-not-present exposure, ~600K loyalty members and gift-card balances that are monetizable
fraud targets, and ~5,200 trade accounts with credit exposure. Without a dedicated owner, BuildRight
risks siloed per-channel fraud controls, no cross-channel identity linking, no enterprise fraud
case management, inconsistent chargeback representment, and no consolidated fraud loss-rate
visibility — risks that no existing value stream owns end-to-end.

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-125.1](PA-125.1-fraud-strategy-governance-detection-platform.md) | Fraud Strategy, Governance & Detection Platform | 8 |
| [PA-125.2](PA-125.2-channel-fraud-prevention-detection.md) | Channel-Specific Fraud Prevention & Detection | 8 |
| [PA-125.3](PA-125.3-investigation-recovery-compliance-analytics.md) | Investigation, Recovery, Compliance & Analytics | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
