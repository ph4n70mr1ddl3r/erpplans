# Technical Implementation Guidelines

> This document provides technical guidelines and reference specifications for BuildRight Depot Corp.'s unified cloud ERP system architecture. The POS architecture is designed for **real-time/near-real-time operation** with **offline resilience** and **multi-origin fulfillment** capability.

---

## 1. POS Hardware Reference Specification

The following is the POS hardware specification that meets the business requirements
(offline capability, barcode scanning, multi-tender, receipt printing).

| Component | Reference Spec |
|---|---|
| **Terminal Type** | All-in-one POS terminal (touchscreen) |
| **Screen Size** | 15" touchscreen (cashier) + customer-facing display |
| **Barcode Scanner** | Integrated 2D imager (1D + 2D: QR, DataMatrix) + handheld scanner |
| **Receipt Printer** | 80mm thermal printer (BIR-registered format) |
| **Cash Drawer** | Triggered by POS; 4-bill / 8-coin compartments |
| **Payment Device** | PIN pad for card (EMV/chip & contactless); e-wallet QR support |
| **Offline Storage** | Must store ≥ 8 hours of transactions locally (~1,000 txns per store per day at peak, buffered to ~1,500 capacity for safety margin) |
| **Local Data Store** | Embedded local database on each terminal containing: active SKU catalog (barcode, description, price, UOM, promo rules, flags), cached customer records (loyalty members + trade accounts), terminal configuration; enables full offline selling with accurate pricing and customer recognition |
| **Connectivity** | Primary link + failover connectivity; POS operates offline with full capability during WAN outage; store LAN enables terminal-to-terminal sync when WAN is down |
| **Central Management** | Centrally managed (MDM or equivalent); OTA updates across 600 terminals |

### POS Cost Estimate (Reference)

| Item | Unit Cost (PHP) | Qty | Total (PHP) |
|---|---|---|---|
| POS Terminal (all-in-one) | ~20,000 | 600 | 12,000,000 |
| Barcode Scanner (handheld) | ~5,000 | 600 | 3,000,000 |
| Receipt Printer | ~8,000 | 600 | 4,800,000 |
| Cash Drawer | ~5,000 | 600 | 3,000,000 |
| Payment PIN Pad | ~15,000 | 600 | 9,000,000 |
| **Per-Store Total (3 terminals)** | | | **~PHP 159,000** |
| **All 200 Stores** | | | **~PHP 31,800,000** |

> Note: POS hardware costs are standardized across all locations.

### POS Architecture Principles

The POS system architecture follows three core principles:

#### 1. Real-Time / Near-Real-Time Event-Driven Architecture

| Principle | Implementation |
|---|---|
| **Event streaming** | Each POS transaction (sale, void, return, refund) is published as a discrete event to the ERP message bus within 30 seconds of occurrence |
| **Decoupled processing** | POS terminals operate independently of downstream processing latency; events are queued locally and transmitted asynchronously |
| **Guaranteed delivery** | At-least-once delivery semantics with idempotent event processing and deduplication at ERP; zero data loss tolerance |
| **Event replay** | On reconnection after offline period, events are replayed from last-acknowledged sequence number |
| **Multi-consumer** | Downstream systems (inventory, GL, loyalty, ecommerce ATP, BI dashboards) subscribe to events independently and process at their own pace |
| **Continuous price push** | ERP pushes price changes, new items, discontinued flags, and promotional rules to terminals continuously throughout the day (not nightly batch only); price updates applied within 60 seconds of central activation |

#### 2. Multi-Origin / Mixed Fulfillment

| Principle | Implementation |
|---|---|
| **Unified order management** | Centralized order engine accepts orders from all channels (POS, ecommerce, marketplace, mobile app, trade counter) |
| **Mixed-basket support** | A single POS transaction can contain items fulfilled from different origins: in-store, another store (inter-store transfer), DC home delivery, drop-ship vendor, or endless aisle special order |
| **Fulfillment routing** | Intelligent routing engine evaluates ATP across all locations and fulfillment sources to determine optimal origin per line item |
| **Split fulfillment** | System creates separate fulfillment orders per origin while linking to a single sales order for unified financial posting |
| **Cross-channel returns** | Buy online return in-store, buy in-store return online, with unified credit/refund processing |

#### 3. Offline Resilience

| Principle | Implementation |
|---|---|
| **Full offline selling** | POS terminals continue complete selling operations during network outage for ≥ 8 hours with local embedded data store |
| **Local data scope** | Active SKU catalog, price file, promotional rules, cached customer records (loyalty + trade), terminal configuration stored locally |
| **Terminal-to-terminal LAN sync** | When WAN is down but store LAN is operational, terminals synchronize transactions and inventory deductions peer-to-peer, preventing overselling |
| **Offline capability matrix** | Configurable per-store: full capability (scanning, pricing, cash, offline card, receipts, voids), degraded capability (loyalty queued, trade account floor limit), unavailable functions (e-wallet, digital receipts, new enrollment) |
| **Automatic reconciliation** | On reconnection: encrypted offline transactions uploaded, inventory conflicts resolved, GL posted, loyalty reconciled, stale price flagged — all automatically with Store Manager exception review only |

---

## 2. Infrastructure & Deployment Reference

The following is the infrastructure topology that satisfies the NFRs in [erp-requirements.md](../01-model-company/erp-requirements.md).

### 2.1 Deployment Model Considerations

| Consideration | Notes |
|---|---|
| 200 store locations with POS | Requires reliable connectivity or robust offline mode |
| 4 DCs with WMS/RF guns | Low-latency connection needed for real-time pick/ship |
| 600 POS terminals | Centralized management is essential |
| 6,715 employees | HR/payroll can be cloud-hosted |
| Philippine regulatory filing | BIR, SSS, PhilHealth, Pag-IBIG file generation |
| Data residency | No strict PH data residency requirement, but Asia-Pacific hosting recommended for latency |

### 2.2 Network Bandwidth Reference Estimates

These are estimates based on transaction volumes. Actual bandwidth depends on the chosen
ERP's data sync requirements.

| Site Type | Count | Reference Bandwidth | Rationale |
|---|---|---|---|
| Store | 200 | ≥ 2 Mbps stable + failover link | POS sync, price updates, inventory updates |
| DC | 4 | ≥ 10 Mbps stable, redundant | WMS real-time operations, ~80 RF guns per DC |
| HQ | 1 | ≥ 100 Mbps | 300 users, reporting, batch processing |
| **Total WAN** | **205** | **~540 Mbps aggregate** | |

### 2.3 DR & Business Continuity Reference

| Parameter | Target | Notes |
|---|---|---|
| RPO (back-office) | ≤ 1 hour | Financial data, inventory |
| RTO (back-office) | ≤ 4 hours | Core ERP functions |
| POS offline endurance | ≥ 8 hours | Must continue selling without connectivity |
| POS sync on reconnection | Automatic | No manual intervention; reconcile all offline transactions |
| Data backup | Daily | 30-day rolling + 7-year archive |
| Data retention | 7 years | BIR requirement |

---

## 3. Integration Architecture Reference

### 3.1 Integration Methods by Touchpoint

The model company's [integration touchpoints](../01-model-company/model-company-profile.md#143-integration-touchpoints)
define what connects. The table below details how these systems are integrated.

| Touchpoint | Suggested Method | Notes |
|---|---|---|
| POS ↔ ERP | Event-driven API (near-real-time, < 30 sec latency) | POS publishes transaction events continuously; nightly reconciliation batch validates completeness; offline events queued locally and replayed on reconnection |
| Ecommerce ↔ ERP | REST API | Real-time for orders; near-real-time for inventory |
| Payment Gateway → ERP | Webhook / API | Real-time payment confirmation |
| Bank ↔ ERP | File-based (CSV/XML) or API | Bank-specific formats (BDO, BPI, Metrobank) |
| BIR eFPS ← ERP | File export | BIR-formatted tax return files |
| SSS / PhilHealth / Pag-IBIG ← ERP | File export | Monthly contribution files with PRN |
| Delivery Partners ↔ ERP | API | Real-time order dispatch and status tracking |
| Loyalty Engine ↔ ERP | API | Real-time points earn/redeem |
| WMS ↔ ERP | API or middleware | Real-time for pick/ship confirmations |
| Supplier Portal ↔ ERP | Web portal / EDI | PO viewing, ASN, invoice submission |

### 3.2 Integration Architecture Diagram (Reference)

> The canonical integration architecture diagram is maintained in [data-volumes-and-integrations.md](../01-model-company/data-volumes-and-integrations.md). The diagram below is a duplicate for convenience; if updates are needed, update the canonical version first.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        BUILDRIGHT DEPOT CORP                        │
│                      INTEGRATION TOUCHPOINTS                        │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │ 600 POS  │  │ 4 WMS    │  │ Ecommerce │  │ Loyalty Engine   │   │
│  │Terminals │  │Systems   │  │ Platform │  │ (CRM)            │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────────┬─────────┘   │
│       │              │              │                  │             │
│       └──────────────┴──────┬───────┴──────────────────┘             │
│                             │                                        │
│                    ┌────────▼────────┐                               │
│                    │   ERP SYSTEM    │                               │
│                    │   (Core Hub)    │                               │
│                    └────────┬────────┘                               │
│                             │                                        │
│       ┌─────────────┬──────┴──────┬──────────────┐                  │
│       │             │             │              │                   │
│  ┌────▼─────┐ ┌────▼─────┐ ┌────▼─────┐  ┌────▼──────┐            │
│  │   Banks   │ │ BIR/eFPS │ │ SSS/PH/  │  │ Delivery  │            │
│  │(BDO,BPI,  │ │ (Tax     │ │ Pag-IBIG │  │ Partners  │            │
│  │  MB)      │ │ filing)  │ │ (Stat.)  │  │(Lalamove, │            │
│  └──────────┘ └──────────┘ └──────────┘  │ Transp.)  │            │
│                                           └───────────┘            │
│       ┌─────────────┐         ┌─────────────────┐                  │
│       │  Payment     │         │   Supplier       │                 │
│       │  Gateways    │         │   Portal         │                 │
│       │(PayMongo,   │         │                   │                 │
│       │ Dragonpay)  │         └─────────────────┘                  │
│       └─────────────┘                                               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Security Reference Requirements

These are the active security controls implemented across the unified cloud ERP platform.

| Area | Expectation |
|---|---|
| **Access Control** | Role-based access control (RBAC) with per-entity, per-location, per-function permissions |
| **Audit Trail** | All financial and inventory transactions must have immutable audit logs |
| **Data Encryption** | Encryption at rest and in transit for all sensitive data |
| **POS Security** | Endpoint protection on all POS devices; tamper-resistant payment processing; BIR CAS registration per location |
| **Customer Data** | RA 10173 (Data Privacy Act) compliance; consent management; data subject access requests |
| **Vulnerability Management** | Regular patching; annual penetration testing |
| **Compliance** | SOC 2 Type II or ISO 27001 certification target for ERP provider |

---

*Document Version: 2.1 | Date: 2026-06-09 | Integration diagram canonical reference updated; counts reconciled with README.md*
