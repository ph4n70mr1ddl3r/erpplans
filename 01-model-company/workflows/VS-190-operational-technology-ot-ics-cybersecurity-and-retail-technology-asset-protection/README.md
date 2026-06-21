# VS-190: Operational Technology (OT) / ICS Cybersecurity & Retail Technology Asset Protection

> **Technology & Data** · [Value Stream Index](../value-stream-index.md)

---

## Overview

Operational technology (OT) / industrial control systems (ICS) cybersecurity and retail technology
asset protection for BuildRight Depot Corp. — owning the **cross-domain security program for the
technology that physically runs stores, DCs, and energy/logistics assets**, distinct from the
corporate IT estate governed by VS-27. The program covers the OT/ICS asset inventory and risk
taxonomy across the built environment (BMS / building automation, fire detection & suppression
panels, access control & electric strikes, intrusion/CCTV via VS-23, HVAC & chiller PLCs, standby
generators & ATS, fuel/diesel storage monitoring, paint-mixing & cutting-station PLCs, lumber-yard
automation, SCADA on the rooftop-solar prosumer plant per VS-108, EV-charging controllers per
VS-163, smart-locker & self-checkout controllers per VS-164/VS-149, weighbridges & RF-directed WMS
infrastructure per VS-04, IoT flood/power/temp sensors, and the 600 POS terminal estate per VS-08);
IT/OT network segmentation and Purdue-model zone design; OT-specific monitoring, detection (OT-IDS),
and log correlation; OT vulnerability & patch management (the change-window / can't-just-patch
discipline that makes OT security structurally unlike IT security); OT incident response and
safety-of-life fail-secure procedures; OT-aware third-party / vendor remote-access governance; OT
cyber supply-chain risk; and IEC 62443 / NIST SP 800-82 alignment, BSP cyber-resilience
expectations for payment/cash infrastructure, NPC breach-notification linkage, and OT cyber
performance analytics.

BuildRight operates a very large and safety-coupled OT surface — ~205 sites running fire/life-safety
panels, access control, BMS, generators, fuel systems, and SCADA alongside 600 POS terminals and
~4 DCs of WMS/automation — where a compromised fire panel, suppressed alarm, locked-down BMS, or
POSe/SCO ransomware has direct **safety-of-life, store-closure, and cash/revenue** consequences that
corporate IT controls (VS-27.3) do not address, because OT cannot be patched on IT cadences,
cannot simply be taken offline, and is increasingly converged with the corporate network. This is
distinct from VS-27 (corporate IT operations & cybersecurity — this owns the **OT** layer beneath/
beside it), VS-138 (operates the BMS / building-automation — this **secures** it), VS-163/VS-164/
VS-149 (operate their respective connected-device channels — this owns the **cross-domain OT security
program**), VS-115 (calibrates measurement devices — this secures their connected/PLC layer),
VS-23 (operates CCTV/EAS as a loss-prevention tool — this defends the CCTV/EAS estate itself from
cyber compromise), VS-99 (hardware/software lifecycle — this owns its **cyber-hardening &
end-of-life security**), and VS-21.3 / VS-26 (audit and insure the risk — this operates the controls).
'Operational technology security', 'OT cybersecurity', 'ICS security', 'SCADA security', 'building
automation security', 'OT network segmentation', 'OT incident response', 'IEC 62443', and
'NIST SP 800-82' each appeared in **zero** PA files as dedicated workflow headers (the lone SCADA
reference is the *generation-operations* workflow W3457 in VS-108, not a security discipline) — no
value stream owned the **OT/ICS cybersecurity operating discipline**.

---

## Process Areas

| PA | Name | Workflows |
|---|---|---|
| [PA-190.1](PA-190.1-ot-asset-inventory-architecture-and-it-ot-segmentation-governance.md) | OT Asset Inventory, Architecture & IT/OT Segmentation Governance | 8 |
| [PA-190.2](PA-190.2-ot-threat-detection-vulnerability-and-incident-response-operations.md) | OT Threat Detection, Vulnerability & Incident Response Operations | 8 |
| [PA-190.3](PA-190.3-ot-compliance-third-party-access-and-cyber-resilience-analytics.md) | OT Compliance, Third-Party Access & Cyber Resilience Analytics | 8 |
| | **Total** | **24** |

---

*Back to [Value Stream Index](../value-stream-index.md)*
