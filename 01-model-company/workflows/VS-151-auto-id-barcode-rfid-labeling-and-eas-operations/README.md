# VS-151: Auto-ID, Barcode, RFID, Price-Tag Labeling & EAS Operations

> **Technology & Data** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Auto-ID, Barcode, RFID, Price-Tag Labeling & Electronic Article Surveillance (EAS) Operations
workflows for BuildRight Depot Corp. — owning the enterprise **physical item-identification and
labeling infrastructure** that makes 35,000 active SKUs scannable, correctly priced, loss-protected,
and traceable across 600 POS terminals, 200 stores, 4 DCs, and the ecommerce/last-mile chain.

Today this discipline is **unowned as a program**. The defining terms — "auto-ID", "barcode
governance", "RFID", "price-tag labeling", "EAS operations", "label production" — appear in
**zero** PA files as dedicated workflow headers and in **zero** value-stream directory names.
Auto-ID touches are scattered across VS-29 (W1345 barcode/GS1 master data), VS-71
(anti-counterfeit authentication tags), VS-08 (POS barcode scan, age-restricted prompt), VS-23
(EAS tag, exception reporting), VS-04/VS-05 (RF-directed bin, lot/serial tracking), VS-115
(calibration of the barcode/scan chain), VS-111 (transport packaging labeling, ISPM-15) — but no
value stream owns the end-to-end **labeling & auto-ID operating discipline**: GS1/item-identification
governance and the GTIN/serial/lot/barcode data model, label & price-tag specification and artwork,
the label-production/printing fleet at HQ and stores, in-store price-tag & shelf-label application
(including the **Consumer Act RA 7394** price-tag requirement and price-override integrity),
source-tagging and EAS/RFID tag application, EAS system operations (gate/deactivator/exception),
RFID infrastructure for cycle-count/smart-shelf/real-time visibility, label/tag reconciliation and
shrink analytics, and the print/label hardware lifecycle.

This is distinct from **VS-29 (Master Data Management)** which owns the *data record* (the item
master, the GTIN field) — this value stream owns the *physical identifier and label applied to the
good*. It is distinct from **VS-115 (Calibration/Metrology)** which owns measurement *accuracy* of
scales — this value stream owns *read accuracy* of the scan/RFID chain. It is distinct from
**VS-23 (Loss Prevention)** which investigates shrink — this value stream owns the *EAS/RFID
detection infrastructure* that surfaces it. It is distinct from **VS-71 (Anti-Counterfeit)** which
authenticates genuine product — this value stream owns the *generic item-identification labeling*
every SKU carries. It is distinct from **VS-01.2 (Pricing)** which sets the price — this value
stream owns *physically printing and applying the price tag* and the RA 7394 price-tag compliance.

BuildRight's exposure is structural: at 134.4M annual POS line items, every scan failure, misprice,
missing price tag, or EAS miss is multiplied 134.4M-fold; RA 7394 makes a **missing or wrong price
tag** a direct consumer-protection violation per SKU per store; EAS/RFID is the frontline defense
against the < 1.5% shrinkage target (≈ PHP 0.9B/yr); and the omnichannel/real-time-inventory
ambition (profile §8.4, §15.3) is impossible without reliable auto-ID. A 1% scan-fail or misprice
rate across 134.4M lines is ~1.3M failure events/yr — checkout friction, revenue leakage (links to
VS-118), and compliance exposure.

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-151.1](PA-151.1-auto-id-standards-gs1-governance-and-label-tag-specification.md) | Auto-ID Standards, GS1 Governance & Label/Tag Specification | 8 |
| [PA-151.2](PA-151.2-label-and-price-tag-production-printing-and-application.md) | Label & Price-Tag Production, Printing & In-Store Application | 8 |
| [PA-151.3](PA-151.3-eas-rfid-tagging-source-tagging-and-loss-prevention-integration.md) | EAS/RFID Tagging, Source-Tagging & Loss-Prevention Integration | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
