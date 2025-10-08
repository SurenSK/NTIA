![](\_page\_0\_Picture\_0.jpeg)

# \*\*O-RAN Working Group 8\*\*

\*\*Base Station O-DU and O-CU Software Architecture and APIs\*\*

Copyright © 2025 by the O-RAN ALLIANCE e.V.

O-RAN ALLIANCE e.V., Buschkauler Weg 27, 53347 Alfter, Germany

The copying or incorporation into any other work of part or all of the material available in this specification in any form without the prior written permission of O-RAN ALLIANCE e.V. is prohibited, save that you may print or download extracts of the material of this specification for your personal use, or copy the material of this specification for the purpose of sending to individual third parties for their information provided that you acknowledge O-RAN ALLIANCE as the source of the material and that you inform the third party that these conditions apply to them and that they must comply with them.

![](\_page\_2\_Picture\_0.jpeg)

# Contents

|  | Foreword                                                                   |  |  |
|--|----------------------------------------------------------------------------|--|--|
|  | -------------------------------------------------------------------- ----- |  |  |
|  | Modal verbs terminology                                                    |  |  |
|  | Scope<br>1.                                                                |  |  |
|  | 2.<br>References                                                           |  |  |
|  | 2.1 Normative references                                                   |  |  |
|  | Definitions of terms, symbols and abbreviations<br>3.                      |  |  |
|  | 3.1 Terms                                                                  |  |  |
|  | 3.2 Symbols                                                                |  |  |
|  | 3.3 Abbreviations                                                          |  |  |
|  | RAN Deployment Scenarios and Requirements<br>4.                            |  |  |
|  | 4.1 Deployment Scenario -<br>Example                                       |  |  |
|  | 4.2 Requirements                                                           |  |  |
|  | RAN Architecture<br>5.                                                     |  |  |
|  | 5.1 O-CU/O-DU Lower Layer Split Architecture                               |  |  |
|  | O-DU Software Architecture<br>6.                                           |  |  |
|  | 6.1 O1 Interface                                                           |  |  |
|  |                                                                            |  |  |
|  | O-DU L1 Functional Blocks<br>7.                                            |  |  |
|  | 7.1 Physical Uplink Shared Channel<br>7.2 Uplink Control Channels          |  |  |
|  | 7.3 Uplink Reference Signals                                               |  |  |

| 7.4 Physical Downlink Shared Channel                                                                               |     |  |
|--------------------------------------------------------------------------------------------------------------------|-----|--|
| 7.5 Physical Downlink Control Channel                                                                              |     |  |
| 7.6 Downlink Reference Signals                                                                                     |     |  |
| 7.7 Physical Broadcast Channel                                                                                     |     |  |
| 7.8 Physical Random Access Channel                                                                                 |     |  |
| 7.9 L1 Tasks Processing Flow                                                                                       |     |  |
| 7.10 Front Haul Module                                                                                             |     |  |
| 7.11 O-DU Timing Synchronization                                                                                   |     |  |
| 7.12 Accelerator Abstraction Layer (AAL)                                                                           |     |  |
| 7.13 AAL Lookaside Profile                                                                                         |     |  |
| 7.13.1 Lookaside FEC Profile                                                                                       |     |  |
| 7.13.2 FEC APIs.<br>                                                                                               | .24 |  |
| 7.14 Massive MIMO Optimization                                                                                     |     |  |
| 7.15 Fronthaul M-Plane Processing<br>7.16 Energy Saving Processing                                                 |     |  |
| 7.16.1 Energy Saving Feature Capability and Configuration                                                          |     |  |
| 7.16.2 Cell/Carrier Power Control                                                                                  |     |  |
| 7.16.3 RF Channel Reconfiguration                                                                                  |     |  |
| 7.16.4 Advanced Sleep Mode                                                                                         |     |  |
| 7.17 DMRS-BF                                                                                                       |     |  |
| 7.17.1 DMRS-BF Initialization                                                                                      |     |  |
| 7.17.2 DMRS-BF Operation                                                                                           |     |  |
| O-DU L2 Functional Blocks<br>8.                                                                                    |     |  |
| 8.1 L2 MAC Scheduler                                                                                               |     |  |
| 8.2 Supporting E2 service models                                                                                   |     |  |
| 8.3 O-DU Cloudification                                                                                            |     |  |
|                                                                                                                    |     |  |
|                                                                                                                    |     |  |
| #### O-RAN.WG8.AAD.0-R004-v14.00                                                                                   |     |  |
|                                                                                                                    |     |  |
| ![](_page_3_Picture_1.jpeg)                                                                                        |     |  |
|                                                                                                                    |     |  |
| 8.4 O-DU Security                                                                                                  |     |  |
| ------------------------------------------------------------------------ -- <br>  O-CU Software Architecture<br>9. |     |  |
| 9.1 O1 Interface                                                                                                   |     |  |
| 9.2 F1 Interface                                                                                                   |     |  |
| 9.3 E2 Interface                                                                                                   |     |  |
| 9.4 O-CU Cloudification Aspects                                                                                    |     |  |
| O-CU Functional Blocks                                                                                             |     |  |
|                                                                                                                    |     |  |
| 10.<br>10.1 O-CU-CP Functional Blocks                                                                              |     |  |
| 10.1.1 O-CU-CP-OAM-Agent                                                                                           |     |  |
| 10.1.2 gNB Procedure Management                                                                                    |     |  |
| 10.1.3 Cell Procedure Management                                                                                   |     |  |
| 10.1.4 UE Procedure Management                                                                                     |     |  |

| 10.1.5 RRC Encoder and Decoder | | | 10.1.6 NGAP Encoder and Decoder | | | 10.1.7 XnAP Encoder and Decoder | | | 10.1.8 F1AP Encoder and Decoder | | | 10.1.9 O-CU-UP Control | | | 10.2 Mobility | | | 10.2.1 Inter-O-CU Handover | | | 10.2.2 Inter-O-DU Handover within an O-CU | | | 10.3 O-CU-UP Functional Blocks | | | 10.3.1 O-CU-UP-OAM-Agent and data models | | | 10.3.2 eGTPu | | | 10.3.3 NR PDCP | | | 10.3.4 SDAP | | | | | | O-DU Interfaces<br>11. | | | 11.1 L1/L2 Interface | | | 11.2 L2 Interfaces | | | 11.2.1 O-DU-OAM-Agent -MAC Interface<br>11.2.1.1 NR Cell Configuration | | | 11.2.1.2 Slice Configuration | | | 11.2.2 MAC - O-DU-OAM-Agent Interface | | | 11.2.3 RLC-MAC Interface | | | 11.2.3.1 Data Transfer (DL) | | | 11.2.3.2 Data Transfer (UL) | | | 11.2.3.3 Schedule Result Reporting (DL) | | | 11.2.3.4 Buffer Status Report (DL) | | | 11.2.4 MAC – Scheduler Interface | | | 11.2.4.1 Common Information Elements in MAC-Scheduler APIs | | | 11.2.4.1.1 Air Interface Time | | | 11.2.4.1.2 (Debug) Timing Information | | | 11.2.4.2 MAC to Scheduler APIs | | | 11.2.4.2.1 Cell Configuration Request | | | 11.2.4.2.2 Cell Delete Request | | | 11.2.4.2.3 Slice Configuration Request | | | 11.2.4.2.4 Slice Reconfiguration Request | | | 11.2.4.2.5 Add UE Configuration Request | | | 11.2.4.2.6 Modify UE Reconfiguration Request | | | 11.2.4.2.7 Delete UE Request | | | 11.2.4.2.8 DL HARQ Indication | | | 11.2.4.2.9 UL HARQ (CRC) Indication | | | | |

## # O-RAN

| 11.2.4.2.11 DL Channel Quality Information | |

|--------------------------------------------------|--| | 11.2.4.2.12 RACH Indication Contents | | | 11.2.4.2.13 Paging Indication Contents | | | 11.2.4.2.14 RACH Resource Request | | | 11.2.4.2.15 RACH Resource Release | | | 11.2.4.2.16 DL RLC Buffer Status Information | | | 11.2.4.2.17 Scheduling Request Indication | | | 11.2.4.2.18 UL Buffer Status Report Indication | | | 11.2.4.2.19 Power Headroom Indication | | | 11.2.4.3 Scheduler to MAC APIs | | | 11.2.4.3.1 Cell Configuration Response | | | 11.2.4.3.2 Cell Deletion Response | | | 11.2.4.3.3 Slice Configuration Response | | | 11.2.4.3.4 Slice Reconfiguration Response | | | 11.2.4.3.5 UE Configuration Response | | | 11.2.4.3.6 UE Reconfiguration Response | | | 11.2.4.3.7 UE Deletion Response | | | 11.2.4.3.8 DL Scheduling Information | | | 11.2.4.3.9 UL Scheduling Information | | | 11.2.4.3.10 RAR Information | | | 11.2.4.3.11 Downlink Control Channel Information | | | 11.2.4.3.12 Downlink Broadcast Allocation | | | 11.2.4.3.13 Downlink Paging Allocation | | | 11.2.4.3.14 Downlink HARQ Release | | | 11.2.5 F1AP handler – MAC Interface | | | 11.2.5.1.1 Cell Start | | | 11.2.5.1.2 Cell Stop | | | 11.2.5.1.3 Cell Delete Request | | | 11.2.5.1.4 Cell Delete Response | | | 11.2.5.1.5 Slice Configuration Request | | | 11.2.5.1.6 Slice Configuration Response | | | 11.2.5.1.7 Slice ReConfiguration Request | | | 11.2.5.1.8 Slice ReConfiguration Response | | | 11.2.5.1.9 UE Create Request | | | 11.2.5.1.10 UE Create Response | | | 11.2.5.1.11 UE Reconfiguration Request | | | 11.2.5.1.12 UE Reconfiguration Response | | | 11.2.5.1.13 UE Delete Request | | | 11.2.5.1.14 UE Delete Response | | | 11.2.5.1.15 RACH Resource Request | | | 11.2.5.1.16 RACH Resource Response | | | 11.2.5.1.17 RACH Resource Release | | | 11.2.5.1.18 UE Reset Request | | | 11.2.5.1.19 UE Reset Response | |

| 11.2.5.1.20 UE Sync Status Indication | | | 11.2.5.1.21 UL CCCH Indication | | | 11.2.5.1.22 DL CCCH Indication | | | 11.2.5.1.23 DL PCCH Indication | | | 11.2.5.1.24 DL Broadcast Request | | | 11.2.6 F1AP Handler – RLC Interface | | | 11.2.6.1 UE Create | | | 11.2.6.2 UE Create Response | | | 11.2.6.3 UE Reconfiguration | | | | |

#### O-RAN.WG8.AAD.0-R004-v14.00

![](\_page\_5\_Picture\_1.jpeg)

| 11.2.6.4 UE Reconfiguration Response | | |-----------------------------------------------------|--| | 11.2.6.5 UE Delete | | | 11.2.6.6 UE Delete Response | | | 11.2.6.7 DL RRC Message Transfer | | | 11.2.6.8 DL RRC Message Response | | | 11.2.6.9 UL RRC Message Transfer | | | 11.2.6.10 UL RRC Message Delivery Report | | | 11.2.6.11 RLC Max Retransmission Reached | | | 11.2.6.12 UL RLC Re-establishment Request | | | 11.2.6.13 UE RLC Re-establishment Response | | | 11.2.6.14 UL User Data | | | 11.2.6.15 DL User Data | | | 11.2.7 RLC – O-DU-OAM-Agent Interface | | | 11.2.7.1 PM Slice throughput Event | | | 11.3 O1 Interface and data model | | | 11.4 E2 Interface | | | | | | O-CU Interface<br>12. | | | 12.1 RRC-SDAP Interface | | | 12.1.1 QoS Flow to DRB Mapping | | | 12.1.2 DRB Release | | | 12.2 SDAP-PDCP Interface | | | 12.2.1 Transfer Data PDU (DL) | | | 12.2.2 Transfer Data PDU (UL) | | | 12.2.3 End-marker Control PDU (DL) | | | 12.3 RRC-PDCP Interface | | | 12.3.1 PDCP Entity Establishment | | | 12.3.2 PDCP Entity Re-establishment | |

|  | 12.3.3 SRB Data Request                             |  |  |
|--|-----------------------------------------------------|--|--|
|  | 12.3.4 SRB Data Indication                          |  |  |
|  | 12.4 SDAP-eGTPU Interface                           |  |  |
|  | 12.4.1 Transfer Data SDAP SDU (UL)                  |  |  |
|  | 12.4.2 Transfer Data SDAP SDU (DL)                  |  |  |
|  | 12.4.3 PDCP-eGTPU Interface                         |  |  |
|  | 12.4.4 Transfer Data PDCP PDU (DL)                  |  |  |
|  | 12.4.5 Transfer Data PDCP PDU (UL)                  |  |  |
|  | 12.5 Ciphering and Integrity Protection             |  |  |
|  | 12.6 Header Compression                             |  |  |
|  |                                                     |  |  |
|  | Use-Cases Enhancements<br>13.                       |  |  |
|  | 13.1 Non-GoB mMIMO optimization                     |  |  |
|  | 13.2 Shared O-RU                                    |  |  |
|  | 13.3 RAN Analytics                                  |  |  |
|  | 13.4 RAN Slicing                                    |  |  |
|  | 13.5 Fronthaul M-Plane                              |  |  |
|  | 13.6 Network Energy Savings                         |  |  |
|  | 13.6.1 NES: RIC Control                             |  |  |
|  | 13.6.2 NES: PHY-MAC interactions                    |  |  |
|  | 13.7 O-CU/O-DU Energy Optimization                  |  |  |
|  | 13.7.1 O-CU/O-DU Power Management Architecture      |  |  |
|  | 13.7.2 O-CU/O-DU Demand Based Power Management Flow |  |  |
|  | 13.7.3 L1/L2 Collaboration on Power Management      |  |  |
|  | 13.8 DMRS Beamforming                               |  |  |

#### O-RAN.WG8.AAD.0-R004-v14.00

![](\_page\_6\_Picture\_1.jpeg)

|             | Annex A (Informative)                                                    |  |  |
|-------------|--------------------------------------------------------------------------|--|--|
| L1 APIs 162 | ------------- ------------------------------------------------------- -- |  |  |
|             | A.1.1 Scrambling procedure as defined in TS38.211 [4]                    |  |  |
|             | Call Flows                                                               |  |  |
|             | F1 Startup and Cells Activation                                          |  |  |
|             | UE registration                                                          |  |  |
|             | RACH procedure                                                           |  |  |
|             | SR procedure                                                             |  |  |
|             | UL Grant procedure                                                       |  |  |
|             | PDU Session Establishment                                                |  |  |
|             | Revision history                                                         |  |  |

![](\_page\_7\_Picture\_0.jpeg)

# <span id="page-7-0"></span>Foreword

This Technical Specification (TS) has been produced by O-RAN Alliance.

# <span id="page-7-1"></span>Modal verbs terminology

In the present document "\*\*shall\*\*", "\*\*shall not\*\*", "\*\*should\*\*", "\*\*should not\*\*", "\*\*may\*\*", "\*\*need not\*\*", "\*\*will\*\*", "\*\*will not\*\*", "\*\*can\*\*" and "\*\*cannot\*\*" are to be interpreted as described in clause 3.2 of the O-RAN Drafting Rules (Verbal forms for the expression of provisions).

"\*\*must\*\*" and "\*\*must not\*\*" are \*\*NOT\*\* allowed in O-RAN deliverables except when used in direct citation.

![](\_page\_8\_Picture\_1.jpeg)

# <span id="page-8-0"></span>1. Scope

This Technical Specification has been produced by the O-RAN Alliance.

The contents of the present document are subject to continuing work within O-RAN and may change following formal O-RAN approval. Should O-RAN modify the contents of the present document, it will be re-released by O-RAN with an identifying change of release date and an increase in version number as follows:

Version x.y.z

where:

- x the first digit is incremented for all changes of substance, i.e. technical enhancements, corrections, updates, etc. (the initial approved document will have x=01).

- y the second digit is incremented when editorial only changes have been incorporated in the document.

z the third digit included only in working versions of the document indicating incremental changes during the editing process.

This document contains RAN Requirements, reference O-CU and O-DU Software Architecture, Functional Blocks and API definitions. O-RU and Low-PHY references in this document are only informational to complete the architecture description. All hardware and/or software implementations of O-RU and Low-PHY are not in the scope of this document.

protocol specification". - <span id="page-8-14"></span>[8] 3GPP TR 38.322: "NR; Radio Link Control (RLC) protocol specification". - <span id="page-8-18"></span>[9] 3GPP TR 38.323: "NR; Packet Data Convergence Protocol (PDCP) specification". - <span id="page-8-19"></span>[10] 3GPP TR 37.324: "NR; Service Data Adaptation Protocol (SDAP) specification". - [11] 3GPP TS 38.331: "NR; Radio Resource Control (RRC) Protocol specification". - <span id="page-8-8"></span>[12] 3GPP TS 38.401: "NG-RAN; Architecture

<span id="page-8-2"></span>The following documents contain provisions which, through reference in this text, constitute provisions of the present document.

- <span id="page-8-3"></span>[1] 3GPP TR 21.905: Vocabulary for 3GPP

- <span id="page-8-12"></span>[2] 3GPP TS 29.281: "General Packet Radio System

- <span id="page-8-4"></span>[3] 3GPP TR 38.104: "NR; Base Station (BS) radio

- <span id="page-8-11"></span>[4] 3GPP TS 38.211: "NR; Physical channels and

- <span id="page-8-10"></span>[5] 3GPP TS 38.212: "NR; Multiplexing and channel

- <span id="page-8-9"></span>[6] 3GPP TR 38.300: "NR; NR and NG-RAN Overall

- <span id="page-8-15"></span>[7] 3GPP TR 38.321: "NR; Medium Access Control (MAC)

- <span id="page-8-16"></span>[13] 3GPP TS 38.413: "NG-RAN; NG Application - <span id="page-8-17"></span>[14] 3GPP TS 38.423: "NG-RAN; Xn Application - <span id="page-8-13"></span>[15] 3GPP TS 38.425: "NG-RAN; NR user plane

principles". (F1AP)".

- <span id="page-8-7"></span>[18] 3GPP TS 38.473: "NG-RAN; F1 Application Protocol

![](\_page\_9\_Picture\_1.jpeg)

- <span id="page-8-5"></span>[16] 3GPP TS 38.470: "NG-RAN; F1 general aspects and - <span id="page-8-6"></span>[17] 3GPP TS 38.472: "NG-RAN; F1 signaling transport".

# <span id="page-8-1"></span>2. References

(GPRS) Tunneling Protocol User Plane (GTPv1-U)".

### 2.1 Normative references

transmission and reception".

Specifications

modulation".

Description".

description".

Protocol (NGAP)".

Protocol (XnAP)".

protocol".

coding".

- <span id="page-9-13"></span>[19] 3GPP TS 38.474: "NG-RAN; F1 data transport".

- [20] 3GPP TS 28.541: "5G Network Resource Model (NRM)"

- [21] 3GPP TS 28.552: "Management and Orchestration, 5G Performance Management" - <span id="page-9-2"></span>[22] ORAN-WG4.CUS.0-R004-v16.00, Technical Specification, 'O-RAN Fronthaul Working Group Control, User and Synchronization Plane Specification'.

- <span id="page-9-15"></span>[23] O-RAN.WG4.MP.0-R004-v16.00, Technical Specification, 'O-RAN Fronthaul Working Group Management Plane Specification'.

- <span id="page-9-1"></span>[24] ORAN-WG1 Technical Specification, 'O-RAN Working Group 1 Architecture Description'

- <span id="page-9-0"></span>[25] ORAN-WG7-DSC.0-v01.00 Technical Specification, "Deployment Scenarios and Base Station Classes for White Box Hardware"

- <span id="page-9-8"></span>[26] O-RAN.WG5.O-DU-O1.0-v04.00 Technical Specification, "O1 Interface specification for O-DU"

- <span id="page-9-9"></span>[27] O-RAN.WG3.E2GAP-v01.01 Technical Specification, "Near-Real-time RAN Intelligent Controller Architecture & E2 General Aspects and Principles"

- <span id="page-9-10"></span>[28] O-RAN.WG3.E2AP-v01.01 Technical Specification, "Near-Real-time RAN Intelligent Controller E2 Application Protocol (E2AP)"

- <span id="page-9-3"></span>[29] SCF Release 10.0, Document 222.07.00, 5G FAPI: PHY API Specification, August 2023

- [30] SCF Release 1.0, Document SCF225.3.0, 5G nFAPI Specifications, July 2022 - [31] [O-RAN.WG1.Use-Cases-mMIMO-TR-

v00.11\\\_clean\\\_FixedNumbering.docx,](https://oranalliance.atlassian.net/wiki/d ownload/attachments/2221670469/O-RAN.WG1.Use-Cases-mMIMO-TR-

v00.11\_clean\_FixedNumbering.docx?api=v2) TR for Massive MIMO optimization usecases.

- [32] INT.AO-2021.12.09-WG3-WID-mMIMO\\_draft v06 , TR for WG3 WID to support Massive MIMO optimization feature.

- <span id="page-9-12"></span>[33] O-RAN.WG5.O-CU-O1.0-v03.00 Technical Specification, "O1 Interface specification for O-CU-UP and O-CU-CP"

- [34] O-RAN.WG6.AAL-GAnP.0-v03.00 Technical Specification, "O-RAN Acceleration Abstraction Layer General Aspects and Principles"

- [35] O-RAN.WG6.AAL Common API v02.00 Technical Specification, "Acceleration Abstraction Layer Common API"

- [36] O-RAN.WG6.AAL-FEC.0-v03.00 Technical Specification, "Acceleration Abstraction Layer FEC Profiles"

- [37] O-RAN.WG6.CAD.0-v04.00 Technical Report, "Cloud Architecture and Deployment Scenarios for O-RAN Virtualized RAN"

- <span id="page-9-5"></span>[38] O-RAN.WG6.O-Cloud Notification API -v02.01 Technical Specification, "O-Cloud Notification for Event Consumers"

- <span id="page-9-4"></span>[39] O-RAN.WG11.SecProtSpecs.O-R004-v10.00Technical Specification, "Security Protocols Specifications"

- <span id="page-9-14"></span>[40] O-RAN.WG1.Use-Cases-Detailed-Specification - R003-v14.00, "O-RAN Working Group 1 Use Cases Detailed Specification"

- [41] O-RAN.WG3.UCR-R003-v05.00, "O-RAN Working Group 3 Near-Real-time RAN Intelligent Controller Use Cases and Requirements"

- <span id="page-9-6"></span>[42] O-RAN.WG3.E2SM-KPM-R003-v05.00 . Technical Specification, "Near-Real-time RAN Intelligent Controller E2 Service Model (E2SM) KPM"

- <span id="page-9-7"></span>[43] O-RAN.WG3.E2SM-RC-R004v06.00.03. Technical Specification, "Near-Real-time RAN Intelligent Controller E2 Service Model (E2SM), RAN Control"

- <span id="page-9-11"></span>[44] O-RAN.WG3.E2SM-CCC-R003-v04.00, Technical Specification, " E2 Service Model (E2SM) Cell Configuration Control"

![](\_page\_10\_Picture\_1.jpeg)

# <span id="page-10-0"></span>3. Definitions of terms, symbols and abbreviations

### 3.1 Terms

<span id="page-10-1"></span>For the purposes of the present document, the terms and definitions given in 3GPP TR 21.905 [\[1\]](#page-8-3) and the following apply. A term defined in the present document takes precedence over the definition of the same term, if any, in 3GPP TR 21.905 [\[1\].](#page-8-3) For the base station classes of Pico, Micro and Macro, the definitions are given in 3GPP TR 38.104 [\[3\].](#page-8-4)

\*\*O-CU:\*\* O-RAN Control Unit – a logical node hosting PDCP, RRC, SDAP and other control functions.

\*\*O-DU:\*\* O-RAN Distributed Unit: a logical node hosting RLC, MAC, and High-PHY layers based on a lower layer functional split.

\*\*O-RU:\*\* O-RAN Radio Unit: a logical node hosting Low-PHY layer and RF processing based on a lower layer functional split.

\*\*E1 interface:\*\* The interface defined by 3GPP TS 38.460, 3GPP TS 38.462 and 3GPP TS 38.463 between CU control plane and CU user plane.

\*\*F1 interface:\*\* The interface defined by 3GPP TS 38.470 [\[16\],](#page-8-5) 3GPP TS 38.472 [\[17\]](#page-8-6) and 3GPP TS 38.473 [\[18\],](#page-8-7) to be further interpreted as per O-RAN WG5 specification for interoperability between O-CU and O-DU from different vendors.

<span id="page-10-2"></span>\*\*E2 interface:\*\* The interface is defined by O-RAN

WG3 Near RT-RIC Architecture & E2 General Aspects and Principles that is connecting the near RT-RIC and one or more O-CU-CPs, one or more O-DUs and one or more OeNBs.

### 3.2 Symbols

### 3.3 Abbreviations

<span id="page-10-3"></span>For the purposes of the present document, the abbreviations given in 3GPP TR 21.905 [\[1\]](#page-8-3) and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in 3GPP TR 21.905 [\[1\].](#page-8- 3)

| 3GPP | Third Generation Partnership Project<br>              |
|------|-------------------------------------------------------|
|      | --------- ------------------------------------------- |
| 5G   | Fifth-Generation Mobile Communications<br>            |
| AMC  | Adaptive Modulation and Coding<br>                    |
| BWP  | Bandwidth Part<br>                                    |
| CCCH | Common Control Channel<br>                            |
|      | CORESET   Control Resource Set<br>                    |
| CSI  | Channel State Information<br>                         |
| CU   | Centralized Unit as defined by 3GPP<br>               |
| DCI  | Downlink Control Information<br>                      |
| DPDK | Data Plane Development Kit<br>                        |
| DL   | Downlink<br>                                          |
| DRB  | Dedicated Radio Bearer<br>                            |
| DMRS | Demodulation Reference Signal<br>                     |
| DU   | Distributed Unit as defined by 3GPP<br>               |
| E1AP | E1 Application Protocol<br>                           |
| FAPI | Functional Application Platform Interface             |
| F1AP | F1 Application Protocol<br>                           |
| FDD  | Frequency Division Duplex<br>                         |

![](\_page\_11\_Picture\_1.jpeg)

| FFT  | Fast Fourier Transform<br>                                    |
|------|---------------------------------------------------------------|
|      | --------- --------------------------------------------------- |
| FSM  | Finite State Machine<br>                                      |
| GMC  | Grand Master Clock<br>                                        |
| HARQ | Hybrid Automatic Repeat Request<br>                           |
| IE   | Information Element<br>                                       |
| LCID | Logical Channel Identifier<br>                                |
| LDPC | Low Density Parity Check code<br>                             |

| PF | Proportional Fair (scheduling algorithm) | | PHC | PTP Hardware Clock | | PHR | Power Headroom Report | | PHY | Physical (L1) access layer of RAN | | PRACH | Physical Random Access Channel | | PRB | Physical Resource Block | | PUCCH | Physical Uplink Control Channel | | PUSCH | Physical Uplink Shared Channel | | PSS | Primary Synchronization Signal |

| LLR | Log Likelihood Ratio | | MAC | Medium Access Control protocol | | MAC CE | MAC Control Element | | MIMO | Multiple Input Multiple Output | | mMIMO | Massive MIMO | | MT | Mobile-Termination | | MU-MIMO | Multiple User MIMO | | NG-RAN | Next Generation Radio Access Network | | NIC | Network Interface Card | | nFAPI | Network Functional Application Platform Interface | | NGAP | NG Application Protocol | | NR | New Radio | | O-CU | O-RAN Centralized Unit as defined by O-RAN | | O-DU | O-RAN Distributed Unit as defined by O-RAN | | OFH | Open Front Haul protocol defined by O-RAN | | OFH-C | OFH Control plane | | OFH-U | OFH User plane | | O-RU | O-RAN Radio Unit as defined by O-RAN | | PBCH | Physical Broadcast Channel | | PDCCH | Physical Downlink Control Channel | | PDCP | Packet Data Control Protocol |

| QAM | Quadrature Amplitude Modulation | | QPSK | Quadrature (Quaternary) Phase Shift Keying | | QoS | Quality of Service |

| PTRS | Phase Tracking Reference Signal |

#### \*\*O-RAN.WG8.AAD.0-R004-v14.00\*\*

|---------|------------------------------------------------------------| | RAN | Radio Access Network | | Rel-x | Release number: where x is the actual release number | | RF | Radio Frequency |

![](\_page\_12\_Picture\_1.jpeg)

| RACH | Random Access Channel |

| RLC   | Radio Link Control protocol<br>                            |
|-------|------------------------------------------------------------|
| RRC   | Radio Resource Control protocol<br>                        |
| RU    | Radio Unit as defined by 3GPP<br>                          |
| Rx    | Receiver<br>                                               |
| SCS   | Sub-Carrier Spacing<br>                                    |
| SDAP  | Service Data Adaptation Protocol<br>                       |
| SDU   | Service Data Unit<br>                                      |
| SLA   | Slice Level Agreement<br>                                  |
| SRIOV | Single Root Input/Output Virtualization<br>                |
| SRB   | Signalling Radio Bearer<br>                                |
| SRS   | Sounding Reference Signal<br>                              |
| SSS   | Secondary Synchronization Signal<br>                       |
| SSB   | SS Block<br>                                               |
|       | SU-MIMO   Singer User MIMO<br>                             |
| TA    | Timing Advance<br>                                         |
| TB    | Transport Block<br>                                        |
| TDD   | Time Division Duplex<br>                                   |
| TS    | Technical Specification<br>                                |
| TTI   | Transmission Time Interval<br>                             |
| Tx    | Transmitter<br>                                            |
| UE    | User Equipment<br>                                         |
| UL    | Uplink<br>                                                 |
| URLLC | Ultra-Reliable Low Latency Communication<br>               |
| WG    | Working Group<br>                                          |
| FCAPS | Fault, Configuration, Accounting, Performance and Security |

```
# <span id="page-12-1"></span><span id="page-12-0"></span>4. RAN Deployment 
Scenarios and Requirements
```

### 4.1 Deployment Scenario - Example

The reference design of the O-CU and O-DU is specified in this document to support all deployment scenarios. In this version, the deployment scenario of indoor pico cell is used as an example.

## 4.2 Requirements

<span id="page-12-3"></span><span id="page-12-2"></span>[Table 4-1](#page-12-3) lists the features and requirements supported by the reference design based on the target release specification. Requirements marked "R1" and 'R2" are addressed in this release of the document. Requirements below are aligned to deployment requirements in [\[25\].](#page-9-0)

#### \*\*Table 4-1 Requirements\*\*

## ![](\_page\_13\_Picture\_1.jpeg)

| <br> <br>Feature                            | <br>Requirement                                                                                                                                                     |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WG8 Specification Re                        |                                                                                                                                                                     |
|                                             | ---- --------------------------- ----------------------------------------------<br>-------------------------------------------------------------------------------- |
|                                             | --------------------------------------------------------------------------------                                                                                    |
| --- ----------------------                  |                                                                                                                                                                     |
| <br>                                        |                                                                                                                                                                     |
| lease<br> <br> <br>L1<br> <br>Carrier<br>BW | <br>100MHz                                                                                                                                                          |
| R1<br>                                      |                                                                                                                                                                     |
| <br> <br>Subcarrier                         | Spacing<br> <br>30kHz,<br>120kHz                                                                                                                                    |
| R1<br>                                      |                                                                                                                                                                     |
| <br> <br>Number                             | of<br>carriers<br> <br>1                                                                                                                                            |
| R1<br> <br> <br> <br>Frame                  | structural<br>format<br> <br>Static<br>TDD                                                                                                                          |
| R1<br>                                      |                                                                                                                                                                     |
| <br>                                        | Number<br>of<br>spatial<br>streams<br> <br>2T2R                                                                                                                     |
| R1<br>                                      |                                                                                                                                                                     |
| <br> <br>(after                             | precoder)<br> <br>4T4R                                                                                                                                              |
| R1<br>                                      |                                                                                                                                                                     |
| <br> <br>  R1<br>                           | Numerology/BWP<br>number<br> <br>1                                                                                                                                  |
| <br>                                        | <br>4                                                                                                                                                               |
| R3<br>                                      |                                                                                                                                                                     |
| <br>                                        | RRC signaling                                                                                                                                                       |
| R3<br>                                      |                                                                                                                                                                     |
| <br> <br>BWP<br>change<br>  R3<br>          | <br>MAC<br>CE                                                                                                                                                       |
| <br>                                        | 30K<br>DL:2*2MIMO<br>UL:2*2MIMO                                                                                                                                     |
| R1<br>                                      |                                                                                                                                                                     |
| <br>  MIMO                                  | 30K DL:4*4MIMO<br>UL:2*2MIMO                                                                                                                                        |
| R1<br>                                      |                                                                                                                                                                     |
| <br>  Modulation<br>QPSK,                   | DL: QPSK,16QAM,64QAM,256QAM<br>UL: π/2-bpsk,<br>16QAM,<br>64QAM                                                                                                     |
| R1<br>                                      |                                                                                                                                                                     |
| <br>                                        | UL: 256QAM                                                                                                                                                          |
| R2<br>                                      |                                                                                                                                                                     |
| <br>  Capacity                              | Support at least 4 100MHz bandwidth 2T2R                                                                                                                            |
| TrxPs                                       |                                                                                                                                                                     |
| R1<br> <br> <br>                            | Support at least 2 100MHz bandwidth 4T4R                                                                                                                            |

| TrxPs                                                                            |                                          |
|----------------------------------------------------------------------------------|------------------------------------------|
| R3<br>                                                                           |                                          |
| <br>                                                                             | Support at least 8 100MHz bandwidth 2T2R |
| TrxPs                                                                            |                                          |
| R2<br>                                                                           |                                          |
| <br>                                                                             | Support at least 4 100MHz bandwidth 4T4R |
| TrxPs                                                                            |                                          |
| R3<br>                                                                           |                                          |
| <br>  Peak Data Throughput                                                       | With 100MHz bandwidth and TDD frames DL: |
| UL<br>(1:1), the DL peak throughput of one cell shall not be<br>lower than 750   |                                          |
| Mbps and the UL peak throughput of<br>one cell shall not be lower than 250 Mbps. |                                          |
| (2T2R)   R3<br>                                                                  |                                          |
| <br> <br>Data<br>Compression                                                     | <br>Support                              |
| R3<br>                                                                           |                                          |
| <br>                                                                             | Format<br>0                              |
| R1<br>                                                                           |                                          |
| <br> <br>PRACH<br>Format                                                         | <br>Format<br>B4                         |
| R1<br>                                                                           |                                          |
| <br>                                                                             | Format C2                                |
| R1<br>                                                                           |                                          |
| <br>                                                                             | <br>DCI<br>0-0                           |
| R1<br>                                                                           |                                          |
| <br>                                                                             | <br>DCI<br>0-1                           |
| R1<br>                                                                           |                                          |
| <br> <br>PDCCH<br>Format                                                         | <br>DCI<br>1-0                           |
| R1<br>                                                                           |                                          |
| <br>                                                                             | <br>DCI<br>1-1                           |
| R1<br>                                                                           |                                          |
| <br>                                                                             | <br>Format0                              |
| R1<br>                                                                           |                                          |
| <br> <br>PUCCH<br>Format                                                         | <br>Format1<br>+<br>Format2              |
| R1<br>                                                                           |                                          |
| <br>                                                                             | Format<br>3                              |
| R2<br>                                                                           |                                          |
| <br> <br>SCS<br>of<br>PBCH                                                       | <br>30<br>kHz                            |
| R1<br>                                                                           |                                          |
|                                                                                  |                                          |
| <br> <br>Power<br>control                                                        | <br>Enable                               |
| R2<br>                                                                           |                                          |
| <br>L2<br> <br>HARQ                                                              | <br>Enable                               |
| R1<br>                                                                           |                                          |

![](\_page\_14\_Picture\_1.jpeg)

| AMC |  |  | Enable | R1 |  |
|-----|--|--|--------|----|--|
|-----|--|--|--------|----|--|

|  |                        | ---- ---------------------- ---------------------------- ---- |    |  |
|--|------------------------|---------------------------------------------------------------|----|--|
|  | SRS                    | Enable                                                        | R2 |  |
|  |                        | Round Robin                                                   | R1 |  |
|  |                        | Scheduling algorithm   PF (Proportional Fair)                 | R1 |  |
|  |                        | Slice aware                                                   | R5 |  |
|  | Latency                | Control Plane: 10 ms                                          | R1 |  |
|  |                        | User Plane DL: 4 ms (eMBB)                                    |    |  |
|  | Inter-NR Handover      |                                                               | R3 |  |
|  | L3   Intra-NR Handover |                                                               | R5 |  |
|  | Paging                 |                                                               | R3 |  |
|  | F1AP                   |                                                               | R1 |  |
|  | E1AP                   |                                                               | R3 |  |

# <span id="page-14-0"></span>5. RAN Architecture

3GPP specifies the 5G RAN architecture and interfaces between the logical functional blocks. The following diagram presents the overall 5G network architecture [\[12\]](#page-8-8) as well as the logical partition of the main functions.

![](\_page\_14\_Figure\_5.jpeg)

#### \*\*Figure 5-1 3GPP RAN Architecture\*\*

<span id="page-14-1"></span>As specified by 3GPP in [\[12\]](#page-8-8) a gNB may consist of a gNB-CU-CP, multiple gNB-CU-UPs and multiple gNB-DUs. The gNB-CU-CP is connected to the gNB-DU through the F1-C interface. The gNB-CU-UP is connected to the gNB-DU through the F1-U interface. The gNB-CU-UP is connected to the gNB-CU-CP through the E1 interface. One gNB-DU is connected to only one gNB-CU-CP. One gNB-CU-UP is connected to only one gNB-CU-CP.

The following diagram represents the separation of the CU control plane and user plane.

![](\_page\_15\_Picture\_1.jpeg)

![](\_page\_15\_Figure\_2.jpeg)

\*\*Figure 5-2 Overall architecture for separation of gNB-CU-CP and gNB-CU-UP\*\*

As shown in [Figure 5-3](#page-15-1) [\[24\],](#page-9-1) O-RAN defines the RAN architecture with a focus on new, open interfaces between the logical nodes and physical partitions of the RAN functions.

![](\_page\_15\_Figure\_5.jpeg)

\*\*Figure 5-3 O-RAN Architecture and Interfaces\*\*

## <span id="page-15-1"></span>5.1 O-CU/O-DU Lower Layer Split Architecture

<span id="page-15-0"></span>In some RAN deployment scenarios, e.g., a microcell, the physical layer is split between the O-DU and O-RU. O-RAN WG4 defines the open front haul interface which is adopted in the split architecture as shown i[n Figure 5-4.](#page-16-2) The O-DU contains the higher physical layer High-PHY functions while the O-RU contains the lower physical layer Low-PHY functions as specified in [\[22\].](#page-9-2) The fronthaul software interface is discussed in section [7.10](#page-22-0) of this specification.

![](\_page\_16\_Picture\_1.jpeg)

![](\_page\_16\_Figure\_2.jpeg)

\*\*Figure 5-4 O-CU, O-DU and O-RU (Control and user plane)\*\*

# SPEC 001: 6. O-DU Software Architecture

#####################################SPEC NODE START############################ # <span id="page-16-2"></span><span id="page-16-0"></span>6. O-DU Software Architecture

The O-DU software architecture is illustrated in [Figure 5-1.](#page-14-1) The O-DU is composed of L1 and L2 functional blocks which interface through the FAPI interface [\[29\].](#page-9-3) The functional blocks are further described in the following sections.

```
![](_page_16_Figure_6.jpeg)
```

\*\*Figure 6-1 O-DU functional blocks\*\*

### 6.1 O1 Interface

<span id="page-16-1"></span>The O-DU O1 interface supports the following management capabilities:

- Transport establishment, startup sequence and heartbeat management

- Software management

- Performance (KPIs) management

![](\_page\_17\_Picture\_1.jpeg)

- Fault management
- File management
- Provisioning management
- Synchronization
- Fronthaul delay management

The protocol stack for this interface is shown in [Figure 6-2](#page-17-2)

![](\_page\_17\_Figure\_8.jpeg)

\*\*Figure 6-2 O1 interface protocol stack\*\*

<span id="page-17-2"></span>The O1 interface needs to be secured as specified in [\[39\].](#page-9-4)

#####################################SPEC NODE END############################ # SPEC 002: 7. O-DU L1 Functional Blocks #####################################SPEC NODE START############################ # <span id="page-17-0"></span>7. O-DU L1 Functional Blocks

In O-RAN architecture (refer to [Figure 5-3\)](#page-15-1), PHY layer functionality is realized as High-PHY in O-DU and Low-PHY in O-RU. Some of the PHY functionalities may be realized using hardware acceleration.

Below is a list of PHY related functional blocks.

- PUSCH, PUCCH, PRACH
- PDSCH, PDCCH, PBCH
- UL/DL Reference Signals (DMRS, PTRS, SRS, PSS, SSS)
- Fronthaul handler
- FAPI handler
- Hardware accelerator handler
- Timing sync
- L1 Task Control Module

<span id="page-17-1"></span>In the following sections, the functional blocks are described in detail.

### 7.1 Physical Uplink Shared Channel

The uplink physical layer processing of transport channels consists of the following steps as described in [\[6\]:](#page-8-9)

- Transport Block CRC attachment

- Code Block segmentation and Code Block CRC attachment

- Channel coding: LDPC coding

- Physical layer hybrid-ARQ processing

- Rate matching

- Scrambling

- Modulation: π/2 BPSK (with transform precoding only), QPSK, 16QAM, 64QAM and 256QAM

- Layer mapping, transform precoding (enabled/disabled by configuration), and precoding

- Mapping to assigned resources and antenna ports

![](\_page\_18\_Picture\_1.jpeg)

The frequency domain IQ data received by the fronthaul module are sent to the L1 PUSCH processing functions and the output of the PUSCH is the user bit stream. Figure 7-1 illustrates the PUSCH functional blocks.

![](\_page\_18\_Figure\_3.jpeg)

#### Figure 7-1 PUSCH functional blocks

<span id="page-18-3"></span>\*\*Resource Element (RE) Demapper:\*\* The RE Demapper function separates the DMRS REs and the user data REs. The DMRS REs are provided to the channel estimation function.

\*\*Channel Estimation:\*\* The channel estimation functional block provides a channel estimate based on the DMRS of resource elements of the user data.

\*\*MIMO Equalizer:\*\* The MIMO equalizer function processes the received IQ data signals to reverse the distortion incurred during the signal transmission over the air. Using the channel information acquired via the channel estimation, the equalizer tries to restore the IQ symbol sent by the transmitter. The symbols may be conveyed as log-likelihood ratios (LLRs) for use by the LDPC decoder.

\*\*Rate Dematching:\*\* The rate dematching function performs the reverse operation steps of rate matching for LDPC code in clause 5.4.2 in 3GPP TS38.212 [5].

LDPC Decoder: The LDPC decoder function uses received log-likelihood ratios (LLRs) to compute the data bits based on selected decoder algorithm. The selection of the decoder algorithm is out of scope of this specification.

\*\*CRC Check:\*\* The CRC function block checks the parity bits using the generator polynomials in Subclause 5.1 of 3GPP TS38.212 [5]. Refer to the 3GPP specification for details.

### 7.2 Uplink Control Channels

<span id="page-18-0"></span>Physical Uplink Control Channel (PUCCH) conveys Uplink Control Information (UCI) and supports all the formats defined in clause 6.3.2 of 3GPP TS38.211 specification [4]. Refer to this specification for details of the formats as well as the control message including:

- HARQ-ACK (Hybrid Automated Repeat Request Acknowledgement).
- Scheduling Request (SR)
- <span id="page-18-1"></span>Channel State Information (CSI) ٠

### 7.3 Uplink Reference Signals

5G NR introduces the following reference signals.

- Demodulation Reference Signal (DMRS) for PUSCH and PUCCH .
- Phase Tracking Reference Signal (PTRS) ٠
- Sounding Reference Signal (SRS)

<span id="page-18-2"></span>Refer to clause 6.4.1 in 3GPP TS38.211 specification [4] for more details of the reference signals.

### 7.4 Physical Downlink Shared Channel

The downlink physical layer processing of transport channels consists of the following steps as described in [6]:

- Transport Block CRC attachment .
- Code Block segmentation and Code Block CRC attachment .
- Channel coding: LDPC coding .
- Physical-layer hybrid-ARQ processing

![](\_page\_19\_Picture\_1.jpeg)

- Rate matching
- Scrambling
- Modulation: QPSK, 16QAM, 64QAM and 256QAM
- Layer mapping .
- Mapping to assigned resources and antenna ports .

Figure 7-2 illustrates the functional blocks of the PDSCH for Category A and Category B radio.

In Category A radio, the precoder function is located in O-DU; In Category B radio, the precoder function is located in O-RU.

![](\_page\_19\_Figure\_9.jpeg)

#### Figure 7-2 PDSCH Functional Blocks

<span id="page-19-2"></span>\*\*Cyclic Redundancy Check Generation:\*\* The CRC function block computes the parity bits using the generator polynomials in Subclause 5.1 of 3GPP TS38.212 [5]. Refer to the 3GPP specification for details.

\*\*Segmentation\*\*: The transport block is segmented when it exceeds the code block size specified by 3GPP TS38.212 [5]. Refer to Subclause 7.2.3 for details.

\*\*LDPC Encoder\*\*: Refer to Subclause 5.3.2 in 3GPP TS38.212 [5] for details.

\*\*Rate Matching\*\*: Refer to Subclause 5.4.2 in 3GPP TS38.212 [5] for details.

\*\*Scrambler\*\*: Refer to Subclause 7.3.1.1 in 3GPP TS38.211 [4] for details.

\*\*Modulation Mapper\*\*: Refer to Subclause 7.3.1.2 in 3GPP TS38.211 [4] for details.

\*\*Layer Mapper:\*\* Refer to Subclause 7.3.1.3 in 3GPP TS38.211 [4] for details.

<span id="page-19-0"></span>\*\*RE Mapper\*\*: Refer to Subclause 7.3.1.5 and Subclause 7.3.1.6 in 3GPP TS38.211 [4] for details.

### 7.5 Physical Downlink Control Channel

A Physical Downlink Control Channel (PDCCH) carries control information (DCI) such as scheduling information and resource grant to UEs. The PDCCH includes one or more Control Channel Elements (CCE, consists of 6 resource element group) based on the aggregation level defined by 3GPP specification [4]. The PDCCH processing flow is similar to the PDSCH. The PDCCH uses a polar code instead of LDPC. QPSK modulation is the designated modulation scheme for the PDCCH bits block.

## ### 7.6 Downlink Reference Signals

<span id="page-19-1"></span>The Downlink Reference Signals include:

- Demodulation Reference Signal (DMRS) for PDSCH, PDCCH and PBCH.
- Phase Tracking Reference Signal (PTRS) .
- Channel State Information Reference Signal (CSI-RS) .
- Primary Synchronization Signal (PSS) .

![](\_page\_20\_Picture\_1.jpeg)

Secondary Synchronization Signal (SSS)

Refers to clause 7.4.1 in 3GPP TS38.211 specification [4] for more details related to the reference signals. The PSS and SSS combined with PBCH is known as SS/PBCH block, which consists of:

<span id="page-20-0"></span>1 symbol PSS, 1 symbol SSS and 2 symbol PBCH.

### 7.7 Physical Broadcast Channel

PBCH carries 5G NR system information for UEs. UEs need to decode the PBCH information in order to access the 5G cell. PBCH information includes: downlink bandwidth, SFN, timing information in radio frame and SS burst periodicity. Polar codes are used as error correcting code for PBCH.

![](\_page\_20\_Figure\_7.jpeg)

Figure 7-3: PBCH processing flow diagram

\*\*PBCH Payload Generation:\*\* Creates the PBCH payload message, Refer to Subclause 7.1.1 in 3GPP TS38.212 [5] for details.

\*\*Scrambling\*\*: Refer to Subclause 7.1.2 in 3GPP TS38.212 [5] for details.

\*\*CRC attachment\*\*: Refer to Subclause 7.1.3 in 3GPP TS38.212 [5] for details.

\*\*Channel Encoding\*\*: Refer to Subclause 7.1.4 in 3GPP TS38.212 [5] for details.

\*\*Rate Matching\*\*: Refer to Subclause 7.1.5 in 3GPP TS38.212 [5] for details.

\*\*Data Scrambling\*\*: Refer to Subclause 7.3.1.3 in 3GPP TS38.211 [4] for details.

\*\*Data Modulation:\*\* Refer to Subclause 7.3.3.2 in 3GPP TS38.211 [4] for details.

\*\*Resource Element Mapping:\*\* Refer to Subclause 7.3.3.3 in 3GPP TS38.211 [4] for details.

\*\*DMRS Sequence Generation\*\*: Refer to Subclause 7.4.1.4 in 3GPP TS38.211 [4] for details.

\*\*DMRS Scrambling\*\*: Refer to Subclause 7.4.1.4 in 3GPP TS38.211 [4] for details.

<span id="page-20-1"></span>\*\*DMRS Modulation\*\*: Refer to Subclause 7.3.3.2 in 3GPP TS38.211 [4] for details.

### 7.8 Physical Random Access Channel

Physical Random Access Channel (PRACH) is used to carry preamble from UE to gNB. Based on PRACH, gNB is able to calculate the timing advance of each UE and make adjustments on Rx timing for all UEs. PRACH adopts ZC (Zero Correlation) sequences as preamble. It supports two sequence lengths (139 and 839) with various formats targeted for different deployment scenarios. As O-RAN fronthaul separates the PRACH processing into two parts, the CP removal, frequency shift, samples decimation/filter, FFT and de-mapping function are handled by O-RU; the O-DU PRACH processing flow is shown in Figure 7-4.

![](\_page\_21\_Picture\_1.jpeg)

![](\_page\_21\_Figure\_2.jpeg)

\*\*Figure 7-4: PRACH processing flow diagram\*\*

<span id="page-21-1"></span>Each O-DU PRACH processing function blocks are described below. The details of the PRACH signal generation, formats are described in 3GPP specifications.

\*\*Root Sequence Generation\*\*: Refer to Subclause 6.3.3.1 in 3GPP TS38.211 [4] for details.

\*\*Correlation\*\*: Perform correlation operation between root sequence and received signals.

\*\*iFFT\*\*: Perform the iFFT operation of received signals.

\*\*Antenna Combination\*\*: Combine the received signals from all the antennas.

\*\*Noise Estimation\*\*: Perform the noise estimation operation

\*\*Peak Search\*\*: Detect the peak for different root sequences.

\*\*Preamble Detection and Timing Advance (TA) Estimation\*\*: Determine the preamble sequence and timing advance estimation.

#####################################SPEC NODE END############################ # SPEC 003: 7.9 L1 Tasks Processing Flow

#####################################SPEC NODE START############################ ## 7.9 L1 Tasks Processing Flow

<span id="page-21-0"></span>The L1 function processes are described in previous sections. Those processing blocks focus on specific task that needs to be completed in a timely fashion. [Figure 7-5](#page-21-2) shows the L1 related task processing blocks.

![](\_page\_21\_Figure\_14.jpeg)

<span id="page-21-2"></span>\*\*Figure 7-5: L1 tasks processing diagram\*\*

![](\_page\_22\_Picture\_1.jpeg)

\*\*L2 FAPI processing:\*\* Handle L2 interface request/response based on FAPI protocol. And triggers additional processing task if required.

\*\*Timing events processing:\*\* Handle timing related operations and triggers any prescheduled periodic tasks.

\*\*FEC acceleration processing:\*\* Handle FEC related operations and passes the FEC request to hardware and invokes call back function when the acceleration processing is completed.

\*\*Front haul processing:\*\* Handle all the front haul related Tx/Rx operations, and queue task if further processing is needed.

\*\*UL task scheduling:\*\* Manage all queued UL tasks and starts the processing operation accordingly.

\*\*DL task scheduling:\*\* Manage all queued DL tasks and starts the processing operation accordingly.

\*\*PUSCH processing:\*\* Process the PUSCH related tasks, refer to section 7.1 for details of processing requirements.

\*\*PUCCH processing:\*\* Process the PUCCH related tasks, refer to section 7.2 错误! 未找到引用源。 for details of processing requirements.

\*\*PRACH processing:\*\* Process the PRACH related tasks, refer to section 7.8 for details of processing requirements.

\*\*PDSCH processing:\*\* Process the PDSCH related tasks, refer to section 7.4 for details of processing requirements.

\*\*PDCCH processing:\*\* Process the PDCCH related tasks, refer to section 7.5 错误! 未找到引用源。 for details of processing requirements.

\*\*PBCH processing:\*\* Process the PBCH related tasks, refer to section 7.7 for details of processing requirements.

M-Plane processing: Process the fronthaul M-plane related task for O-RU configuration, management, and operation control.

\*\*Energy Saving processing:\*\* Process the O-RAN energy saving related power capability configuration and power control using M-plane and CUS-plane messages.

### 7.10 Front Haul Module

<span id="page-22-0"></span>The fronthaul module supports the open fronthaul interface specified by O-RAN Fronthaul Specification [22] lower level split distributed gNB architecture [22]. The detailed requirements and control and data plane protocols are described in O-RAN Fronthaul CUS-plane specification. The module is responsible for communication between the O-DU and O-RU. The fronthaul module processes incoming O-RAN Fronthaul CUS-plane packets and constructs outgoing CUS-plane packets. Figure 7-6 illustrates an example implementation of hardware accelerated packet processing related to the fronthaul interface.

![](\_page\_22\_Figure\_18.jpeg)

Figure 7-6: Fronthaul library and interfaces

<span id="page-22-1"></span>The FH library APIs are listed in the following table.

![](\_page\_23\_Picture\_1.jpeg)

|    | API Name            | Parameters                                                                      | Description               |
|----|---------------------|---------------------------------------------------------------------------------|---------------------------|
|    |                     |                                                                                 |                           |
|    |                     | --------------- ------------------------------------ -------------------------- |                           |
|    |                     | ----------------------------                                                    |                           |
|    | FH Init             | Returns handle which is used later   Instantiate the lib memory                 |                           |
|    | model and<br>thread |                                                                                 |                           |
|    | FH start            | FH handle                                                                       | Start processing front    |
|    |                     | haul packets<br>for DL and UL                                                   |                           |
|    | FH stop             | FH handle                                                                       | Stop processing of DL and |
| UL |                     |                                                                                 |                           |
|    | FH close            | FH handle                                                                       | Remove usage of front     |
|    | haul re<br>sources  |                                                                                 |                           |

| FH mm destroy | FH handle | Destroy memory structure |

## #### \*\*Table 7-1 Fronthaul library APIs\*\*

### 7.11 O-DU Timing Synchronization

<span id="page-23-0"></span>In order to meet the timing accuracy in microsecond to sub-microsecond precision requirement over the air interface, O-DU clock needs to synchronize with the Grand Master Clock (GMC). The location of GMC and its connectivity to DU is out of scope of this specification. Please refer to Chapter 9 of [\[22\]](#page-9-2) for details of S-plane (synchronization) aspects.

O-RAN fronthaul defines several timing distribution network topologies. IEEE1588 is used for O-RAN nodes timing synchronization protocol. GNSS based timing synchronization is another option for O-DU acquiring high accuracy timing. With GNSS based timing synchronization, first, the satellite timing messages are decoded by GNSS receiver, then the 1PPS output signal is generated. As described in O-RAN white box hardware reference specification, the 1PPS signal is connected with the PHC on fronthaul NIC. The O-DU is able to choose either IEEE1588 or GNSS synchronization method. Or it can use either one as primary timing synchronization source while keeping the other one as the backup. Here, a LinuxPTP based timing synchronization method is shown as an example. It may be used for O-DU to synchronize with GMC and distribute the clock to O-RU.

![](\_page\_23\_Figure\_7.jpeg)

\*\*Figure 7-7: O-DU Timing Synchronization\*\*

<span id="page-23-1"></span>In [Figure 7-7,](#page-23-1) first, O-DU syncs up backhaul NIC PHC with GMC; second, the system clock syncs up with backhaul PHC using PHC2Sys; then the O-DU software (fronthaul library) gets the system clock using Linux kernel function call. The fronthaul NIC PHC syncs up with system clock through PTP4L. The O-DU becomes boundary clock and is able to distribute the clock through front haul network to O-RU.

In case of loss of PTP sync in a vO-DU (Cloudified O-DU), the O-Cloud is notified using an event trigger as described in 7.2.3 of [\[38\].](#page-9-5)

![](\_page\_24\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 004: 7.12 Accelerator Abstraction Layer (AAL) #####################################SPEC NODE START############################

### ## 7.12 Accelerator Abstraction Layer (AAL)

<span id="page-24-0"></span>In previous sections, the focus is on running a complete L1 layer data on general purpose processor. In certain use cases, a dedicated hardware is used along with host processor to fulfil specific requirements on latency, power efficiency, etc. The hardware accelerator can be implemented on many types of devices such as GPU, FPGA, or ASIC. The accelerator hardware is implementation dependent and is out of scope of this specification. Even so, it is necessary to define a standardized interface to hardware accelerator, which will make the software stack portable with different hardware platform. Based on the data processing flow, the hardware accelerators are categorized into two models: lookaside and inline. In the lookaside model, an accelerator is invoked by the L1 host application to offload designated functions; when acceleration functions are completed, the results are sent back to the host application. With the inline acceleration model, the host processor invokes the accelerator to offload the data processing work, however the result is not sent back to the host. The following figures illustrates L1 processing flow based on these two types of hardware acceleration models.

1. Lookaside accelerator processing flow

![](\_page\_24\_Figure\_5.jpeg)

Figure 7-8: Lookaside Accelerator Model

2. Inline accelerator processing flow

![](\_page\_24\_Figure\_8.jpeg)

![](\_page\_24\_Figure\_9.jpeg)

Figure 5.8 shows the lookaside acceleration model. For the uplink data processing, the host receives the data from O-RAN via fronthaul interface; for the downlink processing, the host processor receives the data from L2 via L1/L2 interface. When either uplink or downlink data needs to be processed by accelerator, the host processor handovers the workload to the accelerator; after the data processing is completed, the results are turn over to the host. Figure 5-9 shows the inline accelerator model. In this case, the accelerator directly receives the uplink data from O-RU via front haul interface. When the L1 process is completed, the result is sent to the host via AAL in order to continue the L2 processing. For the downlink process, the finished L2 data is sent to the accelerator via AAL for L1 processing. When the L1 downlink is completed, the results are sent to O-RU.

### ![](\_page\_25\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 005: 7.13 AAL Lookaside Profile / 7.13.2 FEC APIs #####################################SPEC NODE START############################

## 7.13 AAL Lookaside Profile

### <span id="page-25-1"></span><span id="page-25-0"></span>7.13.1 Lookaside FEC Profile

In general, any combination of L1 functions can be offload to the accelerator. In real deployment, only those functions take more computing power will be offloaded to the accelerator. The accelerator design is implementation specific. To better represent accelerator's functional capabilities, AAL profile is used to differentiate the combination of accelerator architecture and functions. AAL lookaside profile indicates the accelerator adopted the lookaside processing model. The AAL lookaside processing flows are explained in the early section. During the L1 process, the host application initiates the offload work to accelerator, meanwhile the host may perform other work in parallel, it retrieves the result once the work is complete. The AAL FEC Profile includes both uplink and downlink function of PDSCH and PUSCH. The downlink functions are CRC Generation, LDPC Encoding, Rate Matching. The uplink functions are Rate De-matching, LDPC Decoder, CRC Check. These functions can be invoked sequentially or individually.

![](\_page\_25\_Figure\_5.jpeg)

\*\*Figure 7-10: Lookaside FEC Accelerator\*\*

## <span id="page-25-2"></span>7.13.2 FEC APIs

Refer to the O-RAN OSC for FEC APIs details.

### 7.14 Massive MIMO Optimization

<span id="page-25-3"></span>The Massive MIMO (mMIMO) technology is adopted to improve the wireless performance, coverage and the QoS. The beamforming method is the essential element of mMIMO which greatly affects the throughput of wireless network. To optimize the mMIMO beamforming, the non-RT and near-RT RIC utilize the UE/BS channel condition, mobility, and measured performance data to assisted beamforming mode selection. The Grid-of-Beam (GoB) [40] and non-Grid-of-Beam (non-GoB) [41] are two different approaches of beamforming methods that can be used in the O-RAN system [40]. In case of non-GoB, the beamforming weights are generated dynamically in real time instead of using predefined beam set. As O-RAN does not standardize the beamforming algorithm, there are many algorithms that vendors can chose for non-GoB BF weight calculate. The SRS based dynamic BF weight generation is commonly used for non-GoB beamforming weight calculation. There are many factors (SRS periodicity, channel estimation and BF weight calculation algorithms) will affect the effectiveness of non-GoB performance, and the combination of these factors corresponding a BF mode. Various non-GoB modes can be designed to meet the requirements of different UE locations and channel situations [42]. Figure 7- 11 diagram describes the SRS based non-GoB operation flow.

![](\_page\_26\_Picture\_1.jpeg)

![](\_page\_26\_Figure\_2.jpeg)

\*\*Figure 7-11 Non-GoB mMIMO operation flow\*\*

When non-GoB is used, the L1 and L2 need to share the information entities such as BF mode configuration, UE performance measurement KPIs to facilitate the AI/ML model training and inference operations . The following information listed in the Table 7-2.

| <br>Info<br>Name                                                                         |
|------------------------------------------------------------------------------------------|
| <br>Info<br>type                                                                         |
| <br>Description/Notes                                                                    |
|                                                                                          |
| -------------------------------------------------------------------------------          |
| ----------------- --------------------------------------------------------------         |
| ------------------------ -------------------------------------------------------         |
| --------------------------------------------------------------------------------         |
| ---------------                                                                          |
| <br>Supported<br>Non-GoB<br>Beamforming<br>Modes<br>[42]                                 |
| Number of BF mode > 1<br>(Numeric number)<br>Optional BF mode Index<br>&                 |
| description   L1 reports supported beamforming configura<br>tions modes and              |
| related<br>info<br>when<br>requested<br>via<br>O1<br>interface                           |
|                                                                                          |
| <br>DL<br>Synchronization<br>Signal<br>based<br>Reference<br>Signal<br>Received<br>Power |
| (SS<br>RSRP)<br>[42]<br>                                                                 |
| Reports the linear average of the DL SS-RSRP<br>(in [W]) from UEs in the cell            |
| when SS-RSRP<br>is used<br>                                                              |
| DL Synchronization Signal<br>based Signal to Noise and<br>Interference Ratio             |
| (SS<br>SINR)<br>[42]<br>                                                                 |
|                                                                                          |
| Reports the linear average of the DL SS-SINR<br>(in [W]) from UEs in the cell            |
|                                                                                          |
| <br>UL<br>Sounding<br>Reference<br>Signal<br>based<br>Reference<br>Signal<br>Received    |
| Power<br>(SRS-RSRP)<br>[42]<br>                                                          |

| Reports the linear average of the UL SRS<br>RSRP (in [W]) measured for UEs in the cell. |

| Non-GoB BF Mode<br>Configuration [43] | BF mode index (Numeric<br>number) | Index represents a vendor defined proprietary<br>Non-GoB BF algorithm. This index is within<br>the range of Supported Non-GoB Beamform<br>ing Modes. |

\*\*Table 7-2 L1/L2 Information Entities List\*\*

#####################################SPEC NODE END############################ # SPEC 006: 7.15 Fronthaul M-Plane Processing #####################################SPEC NODE START############################ ## 7.15 Fronthaul M-Plane Processing

<span id="page-26-0"></span>The fronthaul M-plane is responsible for O-RU configuration management, performance management, software/file management, and fault management. NETCONF/Yang model is used for the fronthaul M-plane protocol. Refer to the WG4 Management Plane Specification for details.

![](\_page\_27\_Picture\_1.jpeg)

![](\_page\_27\_Figure\_2.jpeg)

\*\*Figure 7-12 Fronthaul M-Plane Processing\*\*

<span id="page-27-3"></span>\*\*[Figure 7-12](#page-27-3)\*\* shows the fronthaul Mplane processing flow which includes the protocol processing, message parsing and preparation, and the M-plane message execution operation.

#####################################SPEC NODE END############################ # SPEC 007: 7.16 Energy Saving Processing / 7.16.1 Energy Saving Feature Capability and Configuration / 7.16.2 Cell/Carrier Power Control #####################################SPEC NODE START############################ ## <span id="page-27-0"></span>7.16 Energy Saving Processing

Energy saving (ES) is one of the key features of sustainable mobile network. The O-RAN energy saving function is achieved by utilizing the AI/ML technology to facilitate the ES operation. To optimize decision making, AI/ML model within Non-RT RIC/ Near-RT RIC predicts traffic, user mobility, and resource usage based on the RAN network status info and AI model. The non-RT RIC and near-RT RIC energy saving application determine the proper time to put the RAN operation in different energy saving modes and resume the normal operation when needed. The following sections describes energy saving operations to fulfill different use case scenarios.

## <span id="page-27-1"></span>7.16.1 Energy Saving Feature Capability and Configuration

The O-RU reports energy saving capability, configurations to O-DU via M-plane during initialization. The capabilities include carrier deactivation for energy saving, TRX control module capabilities, ASM module capabilities, and energy saving capability common information. This information will be used by O-DU to setup the O-RU into proper energy saving state when it is required. The details of ES capabilities are described in the O-RAN fronthaul M-plane specification.

## <span id="page-27-2"></span>7.16.2 Cell/Carrier Power Control

When the mobile network traffic volume is low, it is possible for RAN to get into save energy mode by switching off carrier(s) or entire cell without impairing the user experience. The handover may be required before bringing down carrier or cell.

The cell/carrier power control is done via M-plane message and operation procedure is provided below.

Power Off Cell/Carrier:

- The L1 function set the parameters energy-saving-enabled to "TRUE" and send Mplane message to O-RU

- L1 receives Cell/Carrier power off command from L2

- L1 set parameter [tr]x-array-carrier::deactive for correspond cell or carrier, and send the M-plane message to O-RU.

# \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_

• If the O-RU fails to change the cell/carriers power state, an error message is sent to O-DU by O-RU

![](\_page\_28\_Picture\_1.jpeg)

Power On Cell/Carrier:

- The L1 function set the parameters energy-saving-enabled to "TRUE" and send Mplane message to O-RU

- L1 receives Cell/Carrier power off command from L2

- L1 set parameter [tr]x-array-carrier:: active for correspond cell or carrier,

and send the M-plane message to O-RU. - If the O-RU fails to power on the cell/carriers power state, an error message is sent to O-DU by O-RU

#####################################SPEC NODE END############################ # SPEC 008: 7.16.3 RF Channel Reconfiguration #####################################SPEC NODE START############################ # <span id="page-28-0"></span>7.16.3 RF Channel Reconfiguration

In 5G mobile networks, when mMIMO is used to enhance the network performance on capacity, it requires more power for the RF channels. To create a green mobile network, during a low network traffic period, the O-RU can reduce the power consumption by switching off some Tx/Rx arrays. The RF Channel Reconfiguration operation procedure can be triggered by RIC xApp.

Before the RF Channel Reconfiguration can be performed, the O-DU gathers the O-RU supported antenna pattern via M-plane message, then the O-DU will send the TRX\\_CONTROL command to the O-RU to disable a set of the antenna arrays.

![](\_page\_28\_Figure\_10.jpeg)

\*\*Figure 7-13 RF channel reconfiguration Processing\*\*

RF Reconfiguration Operation flow:

1. Receives RF reconfiguration from RIC energy saving application.

2. O-DU sends TRX control C-plane message with new antenna carrier pattern to O-RU.

3. Case 1, step1: For defined sleep period case, the O-RU configures the antennas and disable certain designated antennas and set sleep timer for specified period time at sleep start time.

4. Case 1, step2: O-RU will wake up and resume to normal operation state after sleep period.

5. Case 1, step3: O-RU may send Ack/Nack message to O-DU if the TRX message includes request for Ack/Nack.

6. Case 2, step1: For undefined sleep period case, the O-RU configures the antennas and disable certain designated antennas and enter sleep state at sleep start time.

![](\_page\_29\_Picture\_1.jpeg)

- 7. Case 2, step2: O-RU receives second TRX control C-plane message with a set of antennas pattern.

- 8. Case 2, step3: O-RU set the antenna pattern and enable specified antennas.

### <span id="page-29-0"></span>7.16.4 Advanced Sleep Mode

This energy saving feature is based on the capability of the O-RU. During system initialization phase, the O-RU reports its capable of supporting the ASM feature, which includes the number of sleep modes. Based on the policy and trained model, when the network traffic is low, RIC ES app can put the RAN into different level of sleep mode. The O-DU will take action to put the O-RU into sleep mode after receiving instruction from Near-RT RIC xApp.

the Advanced Sleep Mode operation processing flow show in \*\*[Figure 7-14](#page-29-1)\*\*.

![](\_page\_29\_Figure\_7.jpeg)

\*\*Figure 7-14 Advanced sleep mode Processing\*\*

<span id="page-29-1"></span>Advanced Sleep Mode Operation flow:

- 1. Receives Advanced Sleep Mode request from RIC energy saving application. - 2. O-DU sends ASM C-plane message to O-RU.

3. Case 1, step1: For defined sleep period case, the O-RU enters the sleep state for specified period time at sleep start time.

- 4. Case 1, step 2: O-RU will wake up and resume to normal operation state after sleep timer expired.

- 5. Case 1, step 3: O-RU may send Ack/Nack message to O-DU if the ASM message includes request for Ack/Nack.

- 6. Case 2, step 1: For undefined sleep period case, the O-RU enters the sleep state at sleep start time.

- 7. Case 2, step 2: O-RU receives second ASM control C-plane message to wake up O-RU.

- 8. Case 2, step 3: O-RU wake up.

![](\_page\_30\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 009: 7.17 DMRS-BF

#####################################SPEC NODE START############################

# <span id="page-30-0"></span>7.17 DMRS-BF

DMRS-based beamforming uses DMRS to calculate beamforming weights in the O-RU. The O-DU provides DMRS configurations of UEs/UE group to the O-RU. Upon receiving I/Q data via air interface, the O-RU uses DMRS for channel estimation, computes beamforming weights, and applies them to both PUSCH and DMRS data. This technique dynamically adjusts beam direction based on frequent DMRS updates, making it ideal for high mobility environments. It may also complete the equalization process within O-RU.

This method excels in tracking fast-moving UEs, ensuring stable, high-quality connections. By focusing energy on the UE, it improves signal quality, reduces interference, increases system capacity, and optimizes energy use. Thus, DMRSbased beamforming enhances network performance, supports high mobility, and optimizes signal direction for better efficiency and connectivity.

```
### <span id="page-30-1"></span>7.17.1 DMRS-BF Initialization
```

The initialization process for DMRS-based beamforming begins by obtaining the DMRS-BF configuration information via the M-plane. Once the configuration is retrieved, the system checks whether DMRS-BF-EQ or DMRS-BF-NEQ is supported by both the O-DU and O-RU. If any one type of DMRS-BF is supported, the O-DU and O-RU are initialized accordingly, enabling channel estimation and beamforming based on the DMRS data. However, if DMRS-BF is not supported by either unit, the system automatically configures an alternative beamforming method, such as SRS-based or codebook-based beamforming, provided those methods are supported. This ensures that even in the absence of DMRS-BF capabilities, the system can still achieve optimized beamforming through other available techniques.

![](\_page\_30\_Figure\_7.jpeg)

\*\*Figure 7-15\*\* DMRS-BF Initialization Process

![](\_page\_31\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 010: 7.17.2 DMRS-BF Operation #####################################SPEC NODE START############################ ## <span id="page-31-0"></span>7.17.2 DMRS-BF Operation

In \*\*DMRS-based beamforming\*\*, the O-RU begins by collecting I/Q data from the antennas, which records both the amplitude and phase of the signal. The \*\*DMRS\*\* is then used to estimate channel conditions using various techniques and calculate beamforming weights. The details of techniques used in channel estimation and weights calculation are beyond the scope of this specification. These weights are applied to the I/Q data to improve signal quality by enhancing its directionality and reducing interference. This involves adjusting the phase and amplitude of signals from each antenna for optimal beamforming.

In the follow-on processing of O-DU, it may be desired to receive certain symbols first, so I would better process the data, e.g., receiving the DMRS signal for channel estimation. If necessary, the O-RU reorders the beamformed data to match the O-DU's data transmission requirements, as defined during initialization, ensuring seamless data handling. The processed PUSCH data is then transmitted to the O-DU over the fronthaul interface.

When the O-DU receives the data, it reassembles it if it had been reordered by the O-RU. Using the DMRS data, the O-DU performs channel estimation, determining how the channel has affected the signal. Equalization weights are then calculated and applied to the PUSCH data to correct any signal distortions caused by the channel.

After applying these equalization adjustments, the PUSCH data moves through further processing stages like decoding and error correction, ensuring the accuracy and reliability of the uplink transmission.

![](\_page\_31\_Figure\_7.jpeg)

Figure 7-16 PUSCH DMRS-BF Processing

![](\_page\_32\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 011: 8. O-DU L2 Functional Blocks #####################################SPEC NODE START############################ # <span id="page-32-0"></span>8. O-DU L2 Functional Blocks

[Figure 8-1](#page-32-1) illustrates the L2 functional blocks of O-DU as a reference design. An implementation may specify the modules differently.

![](\_page\_32\_Figure\_4.jpeg)

#### \*\*Figure 8-1 O-DU L2 functional blocks\*\*

<span id="page-32-1"></span>\*\*O-DU-OAM-Agent\*\*: This module terminates O1 interface from the SMO or the management system. The OAM agent module:

- performs startup and registration procedure with SMO

- establishes and maintains transport and NETCONF connections
- handles configuration and reconfiguration messages on O1
- stores the latest configuration
- relays configuration parameters to appropriate L1 (High-PHY) and L2 modules
- receives and relays notifications over O1
- handles software management for O-DU and O-RU
- collects and send performance data files for O-DU and O-RU performance counters

The procedures and call flows for the above operations are described in [\[26\].](#page-9-8) The management plane for fronthaul supports only hierarchical mode as defined currently in [\[26\].](#page-9-8)

\*\*E2 handler\*\*: This module terminates E2 interface from near real-time RIC. This module handles the following:

- E2/SCTP interface termination
- E2AP protocol message send/receive
- Configure appropriate KPI measurements in L2 and L1 modules
- Report metrics over E2
- Actions to be relayed to other modules (based on E2 messages)
- Relaying response over E2

The E2 global procedures and functional procedures are defines in [\[27\]](#page-9-9) and [\[28\]](#page-9-10) respectively. The E2 service models for different use case implemented by following the generic design described in [8.2.](#page-35-0)

![](\_page\_33\_Picture\_1.jpeg)

\*\*F1 Control Plane interface handling modules (F1AP handler)\*\*: It consists of tasks related to cell management, UE management and semi-static Air Interface Resource Management at the cell level. It does tasks defined in 3GPP TS 38.473 [\[18\].](#page-8-7)

- 1. Cell State Manager: It handles all the tasks related to the handling of cells at O-DU Cell Start, Cell Stop, etc. It also manages a Finite State Machine (FSM) for handling cell specific procedures. This includes maintaining the cell broadcast information. There would be per cell FSM which would run independently of another cell's FSM.

- 2. UE State Manager: It handles the procedures related to a UE, e.g., SRB packet transfer, UE Context Setup, Release procedure, UE Context Modification procedure, etc. It also manages an internal state machine for handling UE specific procedures. It interacts with other layers like RLC/MAC/F1U for UE level interactions and signaling.

- 3. F1AP Interface Manager: This interacts with the O-CU-CP (Control Unit) to control communication setup, and it exchanges F1AP messages over SCTP interface. It also decodes/encodes the messages and exchanges the same messages with other tasks.

- 4. Resource Manager: This block performs tasks like Admission Control, Bearer Control, etc. It also takes care of managing all the air interface resources for a UE, e.g., physical level resource allocation (SR, CSI resources), etc.

\*\*F1 User Plane interface handling modules\*\*: It consists of tasks related to Tunnel management, DL and UL Data and Downlink flow control. It does tasks defined in 3GPP TS 29.281 [\[2\]](#page-8-12) and TS 38.425 [\[15\].](#page-8-13)

- 1. Data Plane Application: Handles DL Data packets received within 3GPP TS 29.281 [\[2\]](#page-8-12) defined NR RAN Container and performs UL Data packet transmission for packets received from RLC. This Application invokes eGTPU encapsulation/decapsulation functionality for eGTPU header processing.

- 2. eGTPU encaps/decaps: This functional block performs eGTPU header decapsulation and processing in DL and eGTPU header encapsulation for the UL packets at F1-U.

- 3. Downlink Flow Control: Downlink Data Delivery Status generation with feedback received from RLC.

\*\*RLC Protocol modules\*\*: These modules handle processing related to SRB and DRB plane. It does tasks defined in 3GPP TS 38.322 [\[8\].](#page-8-14) RLC uses the logical channel for data transfer. MAC layer indicates the downlink data notification request for a logical channel along with the desired RLC PDU size. RLC segments (optionally) the SDUs depending upon the size requested from MAC and sends the RLC PDUs to MAC. MAC layer also indicates uplink data by sending RLC PDUs. RLC layer forms SDUs by reassembling the received PDUs and transmits SDUs to upper Layer via F1 interface. It does tasks defined in 3GPP TS 38.322 [8].

- 1. UE and Bearer Context management
- 2. RLC Mode Receiver and Transmitter
- a. TM Mode
- b. UM Mode
- c. AM Mode

\*\*MAC Protocol modules\*\*: MAC modules include RACH management, HARQ Management, DL and UL Data, BCCH/PCCH/CCCH processing, MAC Transport Block formation, etc. It does tasks defined in 3GPP TS 38.321 [\[7\].](#page-8-15)

- 1. UE and Bearer Context Management: Stores the semi-static information on air interface resources for the UE. It keeps the QoS related information for the scheduler.

- 2. HARQ Management: Performs DL and UL HARQ management by keeping track of HARQ feedback, HARQ timer and providing free HARQ processes information to the scheduler.

- 3. RACH Manager: RACH (Preamble) resource management, CRNTI Assignment, Message-2,3,4 resource allocation and handling.

- 4. CCCH Manager: Handles the DL and UL CCCH message and corresponding HARQ.

- 5. Resource Assign: PDCCH, PDSCH, PUCCH and PUSCH Resource Assignment based on resource allocation schedule from the scheduler.

### ![](\_page\_34\_Picture\_1.jpeg)

- 6. MAC Encoder: It creates MAC Transport block based on input from the scheduler. It interfaces with RLC to get RLC PDUs.

- 7. Demultiplexer: Demultiplexing UL Transport block containing MAC CE and RLC PDUs and sends it to respective tasks.

- 8. CSI Manager: Configuration of "Channel State Information" and informing the CSI feedback from UE to the scheduler.

- 9. PHY-MAC Interface: Receive and transmit the L1-L2 interface messages.

- 10. Beam Failure Detection and Recovery: Beam failure detection in the UE based on the configured beam failure detection reference signal by the gNB and beam failure recovery by performing contention free RACH procedure to the suitable candidate beam.

### 8.1 L2 MAC Scheduler

<span id="page-34-0"></span>[Figure 8-2](#page-34-1) illustrates the MAC scheduler components present in O-DU architecture. It is assumed that the DU includes complete MAC and scheduler functions implemented in the same physical platform.

![](\_page\_34\_Figure\_9.jpeg)

#### \*\*Figure 8-2 L2 MAC scheduler components\*\*

<span id="page-34-1"></span>NR Scheduler functional block has been further expanded into indicative smaller functional sub-blocks to capture the scheduler functionality.

Note: An actual implementation may divide the scheduler into functional sub-blocks differently.

DL/UL Resource Scheduler: This corresponds to functionality of time-domain and frequency domain scheduling in DL and UL, respectively. Resource scheduling is performed per scheduling period and may be performed for a single slot or multiple slots. Massive MIMO focuses on beamforming for capacity enhancement with full digital array structure for frequency<6GHz and hybrid/analog architecture for frequency >6GHz. It is also feasible to have single beam approach for low carrier frequency, however multi-beam approach is desirable for higher carrier frequency. It may include functions such as beam selection, selecting of UEs and associated bearers per scheduling period, allocation of radio resources for PDCCH, PUSCH, PDSCH and associated

![](\_page\_35\_Picture\_1.jpeg)

channels like DMRS. The beam selection is based on various beamforming method supported in the gNB system. In the case of predefined beamforming method, an index called "beamId" indicates the specific beam predefined in the O-RU to use in case of hybrid architecture. However, in case of Hierarchical architecture, the beam indices are pre-defined in the O-DU as defined by O-RAN Fronthaul M-Plane specification [21]. The beam selection function selects beam indices "beamId" that is applied to DL or UL data. In the case of dynamic beamforming, the beamforming weights are given to be applied as defined in the O-RAN Fronthaul CUS Plane specification [20]. It may also include functions/algorithm to support slice differentiation as specified by RRMpolicy for the resource type (PRB) so as to meet the specific SLA. It may also include the slice metric so as to prioritize the specific slice scheduling in a particular TTI that enables the gNB DU system to meet the slice level agreement.

- DL/UL Link Adaptation (LA): This functionality performs per UE Link Adaptation in DL and UL, respectively. Link Adaptation may be performed based on channel quality reported by UE or estimated at gNB corrected by BLER. LA would return effective MCS to be used for channel allocation to the UE.

- UL Tx Power Control: Performs Closed loop UL power control for PUSCH, SRS and PUCCH. It may estimate the UL Tx power based on UE feedback (e.g.: Power Headroom Report) or measured UL channels.

- DL/UL MIMO Mode Control: Determines per UE the MIMO mode, in DL and UL, respectively, to be used along with the corresponding precoding matrix.

- TA Manager: Estimating the TA Command for UE based on feedback from L1 using PUSCH, PUCCH and SRS.

Performance metrics (Capacity, throughput etc.) will be dependent on software implementation and underlying hardware.

### 8.2 Supporting E2 service models

<span id="page-35-0"></span>E2 service models are supported as per call flows as per specifications from O-RAN WG5. Each service model enables a use case across O-RAN nodes. The following generic design in O-DU and O-CU supports any service model with report/insert/control/policy services with the neat real-time RIC.

![](\_page\_35\_Figure\_10.jpeg)

#### \*\*Figure 8-3 E2 service model support in O-DU\*\*

When an E2 message is received at O-DU, the E2 handler module interacts with SM (Service Model) Fanout module to deliver the messages to internal module related to the service model. The SM fanout module consults the SM catalog module and finds the SM specific modules and APIs to be invoked the SM-Service-API-Table module contains maps the following:

- SM service, E2 messages corresponding
- Receiver module(s) for each E2 message and the message contents to be relayed

![](\_page\_36\_Picture\_1.jpeg)

When the O-DU sends an E2 message, it is sent through the E2 Sender module which consults SM Catalog module and maps the respective E2 message API. The E2 sender uses KPIs in KPI module when KPIs are reported in an E2 message.

O-DU handles E2 messages and performs control or reporting actions as per he service models defined by O-RAN WG3. The following service modules are currently defined

E2SM-KPM: Refer to [\[42\]](#page-9-6)

E2SM-RC: Refer to [\[43\]](#page-9-7)

<span id="page-36-0"></span>E2SM-CCC: Refer to [\[44\]](#page-9-11)

### 8.3 O-DU Cloudification

Please refer to O-RAN WG6 specifications for cloud deployment of O-DU. The network functions need to be secured with cryptographic protection as specified in [\[39\].](#page-9-4)

### 8.4 O-DU Security

<span id="page-36-1"></span>All the O-DU interfaces need to be secured as specified in [\[39\].](#page-9-4)

#####################################SPEC NODE END############################ # SPEC 012: 9. O-CU Software Architecture

#####################################SPEC NODE START############################ # <span id="page-36-2"></span>9. O-CU Software Architecture

O-CU node interacts with one or more O-DU nodes through F1 interface.

![](\_page\_37\_Picture\_1.jpeg)

![](\_page\_37\_Figure\_2.jpeg)

#### \*\*Figure 9-1 O-CU interfaces\*\*

### 9.1 O1 Interface

<span id="page-37-0"></span>O1 interface is an interface between management entities in Service Management and Orchestration Framework and O-CU. It is used for operation and management, by which FCAPS management, Software management, File management is achieved.

### 9.2 F1 Interface

<span id="page-37-1"></span>F1 interface supports control plane and user plane separation. The following describe the functions supported over F1-C and F1-U.

The main services and functions of F1-C:

- F1 interface management function

- System Information management function
- F1 UE context management function
- RRC message transfer function
- Paging function

![](\_page\_38\_Picture\_1.jpeg)

Warning messages information transfer function

The main services and functions of F1-U:

- Transfer of user data

- Flow control function

### 9.3 E2 Interface

<span id="page-38-1"></span><span id="page-38-0"></span>A near real-time RIC can configure and control an O-CU via the E2 interface, based on the service models defined. The service models and E2 messages are defined in O-RAN WG3 specifications.

### 9.4 O-CU Cloudification Aspects

Please refer to O-RAN WG6 specifications for cloud deployment of O-CU.

#####################################SPEC NODE END############################ # SPEC 013: 10. O-CU Functional Blocks / 10.1 O-CU-CP Functional Blocks #####################################SPEC NODE START############################ # <span id="page-38-2"></span>10. O-CU Functional Blocks

[Figure 10-1](#page-38-5) below outlines the O-CU functional blocks. An implementation may specify the modules differently.

![](\_page\_38\_Figure\_12.jpeg)

#### \*\*Figure 10-1 O-CU Functional Blocks\*\*

<span id="page-38-5"></span><span id="page-38-3"></span>The O-CU comprises of O-CU-CP and O-CU-UP.

## 10.1 O-CU-CP Functional Blocks

O-CU-CP handles the control plane functionality of O-CU.

### <span id="page-38-4"></span>10.1.1 O-CU-CP-OAM-Agent

O-CU-CP-OAM-Agent manages following services of O-CU-CP:

- Configuration and Control Management
- Performance Counter Management
- Fault Management

O-CU-CP-OAM receives the configuration for O-CU-CP and configures all the modules of O-CU-CP. It may perform operations like spawning of O-CU-CP modules, and software downloading for O-CU-CP.

O-CU-CP-OAM collects the performance counters of O-CU-CP and reports it to performance management entity present in the network.

O-CU-CP-OAM manages the faults and alarms raised at O-CU-CP and reports it to fault management entity present in the network.

![](\_page\_39\_Picture\_1.jpeg)

### <span id="page-39-0"></span>10.1.2 gNB Procedure Management

[Figure 10-2](#page-39-3) shows the detailed view of gNB Procedure Management functional block. gNB Procedure Management manages the non-UE associated NGAP and XnAP procedures like NG/Xn Interface Management and Configuration Transfer procedures as defined in 3GPP TS 38.413 [\[13\],](#page-8-16) TS 38.423 [\[14\]](#page-8-17) and TS 38.473 [\[18\].](#page-8-7) The functional sub-blocks shown in figure below are indicatively used to capture the functionality of gNB Procedure Management functional block and could be realized differently.

![](\_page\_39\_Figure\_4.jpeg)

#### \*\*Figure 10-2 gNB Procedure Management Functional Blocks\*\*

<span id="page-39-3"></span>\*\*Procedure Management\*\*: This functionality handles procedures and business logic involving application of the procedure across multiple cells of the gNB. For example, reset triggered due to NGAP link down involving coordination among multiple cells and UE specific paging as described in 3GPP TS 38.413 [12].

\*\*NGAP Interface Management\*\*: This functionality manages Interface Management procedures, Configuration Transfer procedures, and Warning Message Transmission Procedures over NGAP interface with AMFs as described in 3GPP TS 38.413 [12]. It establishes the association with AMFs. It monitors the association with AMFs. It also maintains context for each AMF with which O-CU is connected and stores information like link status with AMF.

\*\*XnAP Interface Management\*\*: This functionality manages the Global procedures over XnAP interface with peer O-CUs as described in 3GPP TS 38.423 [13]. It establishes the association with peer O-CUs and also accepts association requests from peer O-CUs based on configuration provided by higher layers. It monitors the association with peer O-CUs. It also maintains context for each peer O-CU with which O-CU is connected and stores information like link status with peer O-CU.

\*\*F1AP Interface Procedure Management\*\*: This functionality manages Interface Management procedures over F1AP interface with O-DUs as described in 3GPP TS 38.470 [\[16\]](#page-8-5) and 38.473 [\[18\].](#page-8-7) It establishes the association with O-DUs and also accepts association requests from O-DUs based on configuration provided by higher layers. It monitors the association with O-DUs. It also maintains context for each O-DU with which O-CU is connected and stores information like link status with O-DU.

#####################################SPEC NODE END############################

# SPEC 014: 10.1.3 Cell Procedure Management / 10.1.4 UE Procedure Management #####################################SPEC NODE START############################ ## <span id="page-39-1"></span>10.1.3 Cell Procedure Management

Cell Procedure Management manages the cell level procedures at O-CU like system information management described in 3GPP TS 38.331, procedures for dual connectivity, global procedures like Cell Activation described in 3GPP TS 38.423 [13], Warning Message Transmission procedures, and System Information Procedures described in 3GPP TS 38.473 [\[18\].](#page-8-7)

It maintains multiple state machines to handle various cell level procedures. It may have separate state machines for various cell procedures like Cell Setup, Cell Delete, Cell Start, Cell Stop, and Cell Reconfiguration. It also maintains context of each cell to store information like cell state, number of UEs served by the cell, and cell broadcast information.

It manages the cell level performance counters and provides this information to O-CU-CP-OAM.

## <span id="page-39-2"></span>10.1.4 UE Procedure Management

UE Procedure Management manages the UE Access Control and signalling procedures at O-CU by binding together UE associated RRC, NGAP, XnAP, and F1AP signalling transactions into end-to-end procedures.

This functionality binds together the following signalling procedures on different 3GPP interfaces:

3GPP TS 38.331 defined procedures like RRC Connection Control, Inter-RAT mobility, Measurements, UE capabilities and other UE associated procedures.

# \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_

3GPP TS 38.413 [12] defined procedures like UE Context Management procedures, UE Mobility Management procedures, PDU Session Management procedures, Transport of NAS Messages procedures, Trace Procedures,

![](\_page\_40\_Picture\_1.jpeg)

Location Reporting procedures, UE Radio Capability Management procedures, and Data Usage Reporting Procedures.

- 3GPP TS 38.423 [13] defined inter-gNB procedures for Basic mobility and for gNB-gNB Dual Connectivity.

- 3GPP TS 38.47[3 \[18\]](#page-8-7) defined procedures like UE Context Management procedures, and RRC Message Transfer procedures.

This functionality maintains multiple state machines to handle various UE associated procedures. It may have separate state machines for different UE procedures like UE attach, UE handover, UE context modification, and UE measurement. The single FSM handles NGAP and RRC messages involved in a UE associated procedure, coordinating among AMF, UE, O-DU and other modules of O-CU. It also maintains context of each UE to store information like UE state, various UE AP Ids, and ongoing procedure related information.

### <span id="page-40-0"></span>10.1.5 RRC Encoder and Decoder

RRC Encoder and Decoder encodes and decodes all RRC ASN content as described in 3GPP TS 38.331. RRC ASN encoding is performed for sending message to UE and for preparing containers to be exchanged during handover, etc. RRC ASN decoding is performed on receiving messages from UE and on receiving containers exchanged during handover, etc. RRC Encoder and Decoder is accessed by Cell Procedure Management and UE Procedure Management functional blocks. Cell Procedure Management accesses it for RRC ASN encoding of broadcast messages and paging message. UE Procedure Management accesses it for encoding and decoding of all the messages exchanged with UE and for populating the RRC ASN content in handover containers.

### <span id="page-40-1"></span>10.1.6 NGAP Encoder and Decoder

NGAP Encoder and Decoder encodes and decodes all NGAP ASN message as described in 3GPP TS 38.413 [12]. NGAP ASN encoding is be performed for sending message to AMF. NGAP ASN decoding is performed on receiving messages from AMF. NGAP Encoder and Decoder is accessed by gNB Procedure Management and UE Procedure Management functional blocks. gNB Procedure Management accesses it for non-UE associated procedures between O-CU and AMF. UE Procedure Management accesses it for encoding and decoding of all the UE associated messages exchanged with AMF.

#####################################SPEC NODE END############################ # SPEC 015: 10.1.7 XnAP Encoder and Decoder #####################################SPEC NODE START############################ ## <span id="page-40-2"></span>10.1.7 XnAP Encoder and Decoder

XnAP Encoder and Decoder encodes and decodes all XnAP ASN message as described in 3GPP TS 38.423 [13]. XnAP ASN encoding is performed for sending message to peer O-CU. XnAP ASN decoding is performed on receiving messages from peer O-CU. XnAP Encoder and Decoder is accessed by gNB Procedure Management and UE Procedure Management functional blocks. gNB Procedure Management accesses to perform non-UE associated procedures with peer O-CU. UE Procedure Management accesses it for encoding and decoding of all the UE associated messages exchanged with peer O-CU.

### <span id="page-40-3"></span>10.1.8 F1AP Encoder and Decoder

F1AP Encoder and Decoder encodes and decodes all F1AP ASN content at O-CU as described in 3GPP TS 38.473 [\[18\].](#page-8-7) F1AP ASN encoding is performed for sending message to O-DU. F1AP ASN decoding is performed on receiving messages from O-DU. F1AP Encoder and Decoder is accessed by gNB Procedure Management and UE Procedure Management functional blocks. gNB Procedure Management accesses it to perform non-UE associated procedures with O-DU. UE Procedure Management accesses it for encoding and decoding of all the UE associated messages exchanged with O-DU.

```
### <span id="page-40-4"></span>10.1.9 O-CU-UP Control
```

O-CU-UP Control function configures and controls the CU User Plane entities as per the E1 interface defined by 3GPP. This function is invoked primarily by the UE Procedure Management functionality though the non-UE associated procedures would be invoked by the gNB and Cell Procedure Management functionality.

\*\*O-RAN.WG8.AAD.0-R004-v14.00\*\*

![](\_page\_41\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 016: 10.2 Mobility #####################################SPEC NODE START############################ ## 10.2 Mobility

### <span id="page-41-1"></span><span id="page-41-0"></span>10.2.1 Inter-O-CU Handover

Handover between O-CUs is described in the call flow below.

![](\_page\_42\_Picture\_1.jpeg)

![](\_page\_42\_Figure\_2.jpeg)

Figure 10-3 Inter NG-RAN NG based handover (C-Plane Handling)

![](\_page\_43\_Picture\_1.jpeg)

- 1. The source gNB RRC decides for handover.

- 2. Source gNB RRC requests PDCP to provide HO preparation info by sending message \*HO Preparation Info Request\*. In this message, RRC provides target Cell Id and may provide list of cells under control of target gNB, required for potential re-establishment by the UE in these cells to succeed.

- 3. PDCP sends \*HO Preparation Info Response\* to RRC containing list of ShortMAC-I prepared for the cell list received in \*HO Preparation Info Request\*. PDCP may also report ue-InactiveTime.

- 4. RRC sends \*UE Context Modification Request\* to GNB CU F1AP to query gNB DU configuration.

- 5. GNB CU F1AP sends \*UE Context Modification Request\* to DU to query gNB DU configuration by setting GNB-DU Configuration Query to TRUE.

- 6. gNB DU provides CellGroupConfig in DU to CU RRC Information IE in \*UE Context Modification Response\* to gNB CU F1AP.

- 7. gNB CU F1AP provides the information received from DU to RRC in \*UE Context Modification Response\*.

Note: If RRC maintains the DU CellGroupConfig then steps 4 to 7 are not required.

- 8. Starts TNGRELOCprep timer.

- 9. Source gNB RRC sends \*Handover Required\* message to the AMF.

- 10. Target gNB RRC receives \*Handover Request\* from AMF.

- 11. RRC performs UE admission control and allocates resources for the UE.

- 12. RRC creates UE entity at PDCP by sending message \*PDCP Entity Establishment Request\*.

- 13. After creating UE entity, PDCP sends response message \*PDCP Entity Establishment Response\* to RRC.

- 14. RRC creates UE entity at F1U by sending message \*F1U Entity Establishment Request\*.

- 15. After creating UE entity, F1U sends response message \*F1U Entity Establishment Response\* to RRC. This message includes UL tunnel information for each DRB to be shared with DU to receive uplink data from DU.

- 16. RRC sends \*UE Context Setup Request\* message to F1AP to create UE entity at DU.

- 17. F1AP sends \*UE Context Setup Request\* message to DU to create UE entity at DU.

- 18. After creating UE entity at DU, sends \*UE Context Setup Response\* message to F1AP. This message includes DL tunnel information for each DRB to be shared with gNB CU F1U to receive downlink data from CU.

- 19. F1AP sends \*UE Context Setup Response\* message to RRC.

- 20. RRC reconfigures UE entity at F1U by sending message \*F1U Entity Reconfigure Request\*. In this, RRC provides the DL tunnel information received from DU.

- 21. After reconfiguring UE entity, F1U sends response message \*F1U Entity

Reconfigure Response\* to RRC.

- 22. RRC creates UE entity at NGU by sending message \*NGU Entity Establishment Request\*. RRC will also provide forwarding tunnels configuration to NGU, if required.

- 23. After creating UE entity, NGU sends response message \*NGU Entity Establishment Response\* to RRC.

- 24. After preparing the target gNB for UE, RRC sends \*Handover Request Acknowledge\* message to AMF. This message also contains HandoverCommand IE for UE.

- 25. Source gNB RRC receives \*Handover Command\* message from target gNB.

- 26. Source gNB RRC stops TNGRELOCprep timer and start TNGRELOCOverall timer.

- 27. RRC sends \*PDCP Entity Suspend Request\* to suspend data in downlink for the UE.

- 28. After suspending the data, PDCP sends \*PDCP Entity Suspend Response\* to RRC. - 29. RRC reconfigures NGU with message \*NGU Entity Reconfiguration Request\* to configure forwarding tunnels for DRBs for which target gNB has provided DL Forwarding UP TNL Information or UL Forwarding UP TNL Information or both.

- 30. NGU sends \*NGU Entity Reconfiguration Response\* after configuring the forwarding tunnels. After this, source gNB will start forwarding data to target gNB.

Note: If target gNB does not provide DL Forwarding UP TNL Information or UL Forwarding UP TNL Information, data forwarding will not be configured. In that case, step 29 and step 30 is not be performed.

- 31. RRC sends \*UE Context Modification Request\* to GNB CU F1AP to stop DL data transmission.

- 32. gNB CU F1AP sends \*UE Context Modification Request\* to DU which includes RRCReconfiguration message and indicates to stop the data transmission for the UE.

# \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_

33. DU may indicate RRCReconfiguration message delivery to UE status to gNB CU F1AP.

![](\_page\_44\_Picture\_1.jpeg)

- 34. DU responds with \*UE Context Modification Response\* to gNB CU F1AP.

- 35. gNB CU F1AP responds with \*UE Context Modification Response\* to RRC.

- 36. RRC requests PDCP to provide uplink PDCP-SN and HFN receiver status and the downlink PDCP SN and HFN transmitter status of RLC AM DRBs for which PDCP status preservation applies in message \*RAN Status Transfer Request\* so that same can be provided to target gNB.

- 37. PDCP reports uplink PDCP-SN and HFN receiver status and the downlink PDCP SN and HFN transmitter status of RLC AM DRBs in \*RAN Status Transfer Request\* message.

- 38. RRC provides uplink PDCP-SN and HFN receiver status and the downlink PDCP SN and HFN transmitter status of RLC AM DRBs to target gNB in \*Uplink RAN Status Transfer\* message. After sending this, source gNB RRC waits for \*UE Context Release Command\* message from AMF.

- 39. Target gNB receives source gNB \*Downlink RAN Status Transfer\* for RLC AM DRBs on which PDCP status preservation applies.

- 40. RRC sends RAN Status Transfer Indication to PDCP to provide uplink PDCP-SN and HFN receiver status and the downlink PDCP SN and HFN transmitter status of RLC AM DRBs received from source gNB via AMF.

Note: If RLC AM DRB is not configured, steps 36 to 40 is not be performed. In that case, source gNB RRC can receive UE Context Release Command from AMF any time after performing step 32.

- 41. After handover execution at source gNB, UE sends RRCReconfigurationComplete to target gNB DU which target gNB DU sends to target gNB CU F1AP in \*UL RRC Message Transfer\* message.

- 42. gNB CU F1AP sends the received RRCReconfigurationComplete message to PDCP in \*UL RRC Message Transfer\* message for decryption and deciphering.

- 43. PDPC decrypt and decipher RRCReconfigurationComplete and sends it to RRC as payload in \*SRB Data Request\* message.

- 44. On receiving RRCReconfigurationComplete, RRC sends \*Data Buffer Stop Indication\* to PDCP so that PDCP can process the buffered data and resume the data at target gNB.

- 45. Target gNB RRC sends \*Handover Notify\* to AMF to indicate successful completion of handover procedure at target gNB.

- 46. After successful handover of UE at target gNB, AMF sends \*UE Context Release Command\* to source gNB which is handled by source gNB RRC.

- 47. Source gNB initiates local UE release procedure.

- 48. After completion of UE release, source gNB RRC sends \*UE Context Release Complete\* message to AMF.

### <span id="page-44-0"></span>10.2.2 Inter-O-DU Handover within an O-CU

This procedure is defined for the use case when UE moves from one gNB-DU to another gNB-DU within the same gNB-CU during NR operation.

This message descriptions are captured high level with the intend to specify the inter-layer messages interaction on top of 3gpp messages. FAPI messages are not detailed here (Reference for FAPI specification [29], [30]).

#### \*\*O-RAN.WG8.AAD.0-R004-v14.00\*\*

![](\_page\_45\_Picture\_1.jpeg)

![](\_page\_45\_Figure\_2.jpeg)

![](\_page\_46\_Picture\_1.jpeg)

![](\_page\_46\_Figure\_2.jpeg)

#### \*\*Figure 10-4 Inter NG-RAN NG based handover (C-Plane Handling)\*\*

#### \*\*Assumption: UE is RRC connected with gNB and PDU data session is active.\*\*

- The UE sends Measurement Report message to the source gNB-DU. gNB-DU receives the UL Information Transfer message and it send the PUSCH message to the MAC/RLC layer.

- The UL RRC message transfer message is sent by RLC to F1AP over RLC-F1AP interface, later O-DU/F1AP layer sends the UL RRC Message Transfer to F1AP layer at O-CU to convey the UE Measurement Report message.

- F1AP later at O-CU sends the UL RRC Message Transfer message to RRC layer via PDCP interface.

- The gNB-CU makes an handover decision to the another cell belonging to the target gNB-DU.

- Optionally the gNB-CU may send an UE CONTEXT MODIFICATION REQUEST message to the source gNB-DU to query the latest configuration. Optionally the source gNB-DU sends the UE Reconfiguration Request to MAC/RLC layer and get the UE Reconfiguration Response from the respective protocol layers in case gNB-DU application does not store the latest configuration.

- The source gNB-DU responds with an UE CONTEXT MODIFICATION RESPONSE message that includes latest full configuration information.

- The gNB-CU sends an UE CONTEXT SETUP REQUEST message to the target gNB-DU to create an UE context and setup one or more data bearers. The UE CONTEXT SETUP REQUEST message includes HandoverPreparationInformation. The target gNB-DU sends the UE Create Request to the MAC and RLC layer to create the UE context with radio resources and receives UE Create Response from the respective protocol layers.

- The target gNB-DU responds with an UE CONTEXT SETUP RESPONSE message if the target gNB-DU can admit resources for the handover.

- The gNB-CU sends an UE CONTEXT MODIFICATION REQUEST message to the source gNB-DU, which includes RRCReconfiguration message towards the UE. The gNB-CU also indicates the source gNB-DU to stop the data transmission for the UE.

- The source gNB-DU sends the UE Reconfiguration Request to MAC/Scheduler and RLC

layer and get the UE Reconfiguration Response from the respective protocol layers.

![](\_page\_47\_Picture\_1.jpeg)

- The source gNB-DU optionally sends a Downlink Data Delivery Status frame to inform the gNB-CU about the downlink data PDUs that could not be successfully transmitted to the UE.

- The source gNB-DU forwards the received RRCReconfiguration message to the UE.

- The source gNB-DU responds to the gNB-CU with UE CONTEXT MODIFICATION RESPONSE message.

- UE triggers Random Access procedure at the target gNB-DU.

- Optionally the target gNB-DU sends Downlink Data Delivery Status frame to the gNB-CU.

- The gNB-CU sends the target gNB-DU with the PDCP PDUs that are not successfully transmitted in the source gNB-DU.

- The UE responds to the target gNB-DU with an RRCReconfigurationComplete message.

- The target gNB-DU sends UL RRC MESSAGE TRANSFER message to the gNB-CU to convey the received RRCReconfigurationComplete message.

- The downlink and uplink data packets are sent to/from the UE through the target gNB-DU.

- The gNB-CU sends an UE CONTEXT RELEASE COMMAND message to the source gNB-DU.

- The source gNB-DU sends UE DELETE REQUEST to MAC/RLC layer to release the UE context in the respective protocol layer and receives UE DELETE RESPONSE message. - The source gNB-DU responds the gNB-CU with an UE CONTEXT RELEASE COMPLETE message.

### 10.3 O-CU-UP Functional Blocks

<span id="page-47-0"></span>O-CU-UP handles the user plane functionality at O-CU.

### <span id="page-47-1"></span>10.3.1 O-CU-UP-OAM-Agent and data models

O-CU-UP-OAM-Agent manages following services of O-CU-UP:

- Configuration and Control Management

- Performance Counter Management

- Fault Management

O-CU-UP-OAM receives the configuration for O-CU-UP and configures all the modules of O-CU-UP. It may perform operations like spawning of O-CU-UP modules and software downloading for O-CU-UP.

O-CU-UP-OAM collects the performance counters of O-CU-UP and reports it to performance management entity present in the network.

O-CU-UP-OAM manages the faults and alarms raised at O-CU-UP and reports it to fault management entity present in the network.

For O-CU data models, please refer to O-RAN WG5 data models [\[33\].](#page-9-12)

### <span id="page-47-2"></span>10.3.2 eGTPu

[Figure 10-5](#page-47-3) shows the detailed view of eGTPu functional block.

![](\_page\_47\_Figure\_27.jpeg)

\*\*Figure 10-5 eGTPu Functional Blocks\*\*

<span id="page-47-3"></span>\*\*eGTPu encaps and decaps\*\*: It handles the eGTPu protocol stack. It performs eGTPu encapsulation and decapsulation as described in 3GPP TS 29.281 [\[2\]](#page-8-12) and TS 38.425 [\[15\].](#page-8-13)

![](\_page\_48\_Picture\_1.jpeg)

\*\*Data Application\*\*: This function receives the data packet from UPF, peer O-CU and O-DU over eGTPu interface. It calls eGTPu encaps and decaps to remove the eGTPu header. It identifies the corresponding UE and DRB Id based on mapping of TEID and IP address maintained at eGTPu. It then forwards the data packet to SDAP, which maps the PDU Session to appropriate DRB and passes data to NR PDCP along with information of UE and DRB Id. While sending packet to NR PDCP, it also indicates from which interface this packet has been received, i.e., from UPF or from peer O-CU or from O-DU.

Data Application also processes the data packets received from SDAP. On receiving data packet, it adds the eGTPu header by calling eGTPu encaps and decaps. On the basis of destination, UE and DRB Id received from NR PDCP, packet relay fetches the TEID and IP address from the mapping maintained at eGTPu and sends the data packet to the destination provided by NR PDCP.

\*\*NGU\*\*: It exchanges ECHO request and response over NGU interface. It takes care of the error handling on NGU interface.

\*\*XnU\*\*: It exchanges ECHO request and response over XnU interface. It takes care of the error handling on XnU interface. It also takes care of data flow control on XnU interface.

\*\*F1U\*\*: It exchanges ECHO request and response over F1U interface defined in [\[19\].](#page-9-13) It takes care of the error handling on F1U interface. It also takes care of data flow control on F1U interface.

### <span id="page-48-0"></span>10.3.3 NR PDCP

NR PDCP transfers user plane and control plane data. It maintains PDCP SNs of 12 bits or 18 bits for DRBs and 12 bits for SRBs. It performs header compression and decompression, integrity protection and verification, ciphering and deciphering, timer based SDU discard, routing for split bearers, duplication, reordering and in-order delivery, out of order delivery, and duplicate discarding as described in 3GPP TS 38.323 [\[9\].](#page-8-18)

![](\_page\_48\_Figure\_9.jpeg)

#### \*\*Figure 10-6 PDCP Functional Blocks\*\*

The PDCP layer provides its services to the RRC or SDAP layers. The following services are provided by PDCP to upper layers:

- Transfer of user plane data
- Transfer of control plane data
- Header compression
- Ciphering
- Integrity protection.

![](\_page\_49\_Picture\_1.jpeg)

A PDCP entity expects the following services from lower layers per RLC entity:

- Acknowledged data transfer service, including indication of successful delivery of PDCP PDUs

- Unacknowledged data transfer service.

```
#####################################SPEC NODE END############################
# SPEC 017: 10.3.4 SDAP
#####################################SPEC NODE START############################
```

## <span id="page-49-0"></span>10.3.4 SDAP

It performs QoS flow to DRB mapping and implements the procedure described in 3GPP TS 37.324 [\[10\].](#page-8-19) In case of a DRB where SDAP header to/from UE is not configured, SDAP entity may not be present.

```
![](_page_49_Figure_7.jpeg)
```

\*\*Figure 10-7 SDAP Functional Blocks\*\*

The following services are provided by SDAP to upper layers:

Transfer of user plane data

An SDAP entity expects the following services from lower layers:

- User plane data transfer service

- In-order delivery except when out of order delivery is configured by RRC

#####################################SPEC NODE END############################ # SPEC 018: 11. O-DU Interfaces

#####################################SPEC NODE START############################ # <span id="page-49-2"></span><span id="page-49-1"></span>11. O-DU Interfaces

### 11.1 L1/L2 Interface

MAC and Scheduler in Layer 2 (L2) and High-PHY (L1) in O-DU use the APIs defined SCF 5G FAPI specifications [\[29\].](#page-9-3) In implementations where L2 and L1 of O-DU are on different hosts, a network FAPI (nFAPI) interface is used.

SCF FAPI includes the following interfaces:

- P5: PHY control interface - P7: Main data path interface

![](\_page\_50\_Picture\_1.jpeg)

Please refer to SCF specifications for implementation details of FAPI and nFAPI messages. Some of the FAPI messages are illustrated in the call flows for [UE registration](#page-165-2) in Annex A.

#####################################SPEC NODE END############################ # SPEC 019: 11.2 L2 Interfaces / 11.2.1 O-DU-OAM-Agent -MAC Interface #####################################SPEC NODE START############################

## 11.2 L2 Interfaces

<span id="page-50-0"></span>It is expected that the software implementation of the APIs defined in this section will be in conformance with the API message definition and the fields or message elements. Data types and encoding/decoding of the message contents will be implementation dependent. Message elements (IEs) referring to definitions in 3GPP specifications are italicized for ease of reference.

# <span id="page-50-1"></span>11.2.1 O-DU-OAM-Agent -MAC Interface

### <span id="page-50-2"></span>11.2.1.1 NR Cell Configuration

The following table details the configurations between O-DU-OAM-Agent and MAC for config parameter exchanges.

| Carrier Configuration | struct | Configuration of each transmission<br>point associated to the corresponding<br>cell(s). This includes different physi<br>cal antennas, different frequencies,<br>bandwidths. The NR sector-carrier<br>can have downlink, uplink or both as<br>specified by txDirection. It also ap<br>plies the carrier configurations like<br>numTxAnt , numRxAnt, sdlFre<br>quency, uplinkFrequency, dlBand<br>width<br>or uplinkBandwidth. |

|---------------------------|--------|------------------------------------------ -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -----------------------------------------------------|

| Cell Configuration | struct | This contains the configuration pa<br>rameters relating cell configuration.<br>This also contains the list of slices to<br>be supported in the Tracking area per<br>PLMN. |

| SSB Configuration | struct | This contains the configuration pa<br>rameters relating SSB/PBCH config<br>uration as defined in 38.331 CSI<br>MeasConfig.

| | CSI-RS Configuration | struct | This contains the configuration pa<br>rameters relating CSI-RS configura<br>tion. |

| PRACH Configuration | struct | This contains the configuration pa<br>rameters relating to RACH.s |

| TDD Configuration | | This contains the TDD pattern spe<br>cific information along with TDD<br>periodicity. |

| Precoding Configuration | struct | This contains the configuration pa<br>rameters used for storing a TDD pat<br>tern (up to 63 SSB) |

| Beamforming Configuration | struct | This contains beamforming parame<br>ters. |

![](\_page\_51\_Picture\_1.jpeg)

| carrier-bandwidth | uint16\_t | Carrier bandwidth for DL in MHz<br>[38.104, sec 5.3.2] Values: 5, 10, 15,<br>20, 25, 30, 40,50, 60, 70,<br>80,90,100,200,400<br>Width of this carrier in number of<br>PRBs (using the subcarrierSpacing<br>defined for this carrier) (see TS<br>38.211 [16], clause 4.4.2) |

```
|-------------------|----------|------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
------------------------------------------------------------|
```

| arfcnDL | uint32\_t | NR Absolute Radio Frequency<br>Channel Number (NR-ARFCN)<br>point A in kHz for downlink<br>([38.104, sec5.4.2 and 38.211 sec<br>4.4.4.2] Value: 82000 -> 2489166) | | bSChannelBwUL | uint32\_t | Base station channel bandwidth for<br>UL in MHz [38.104, sec 5.3.2] Val<br>ues: 5, 10, 15, 20, 25, 30, 40,50, 60,<br>70, 80,90,100,200,400 | | arfcnUL | uint32\_t | NR Absolute Radio Frequency<br>Channel Number (NR-ARFCN)<br>point A in kHz for uplink ([38.104,<br>sec5.2 and 38.211 sec 4.4.4.2]<br>Value: 82000 -> 2489166) | | numTxAnt | uint16\_t | Number of Tx antennas Value: 0<br>->65355 |

| numRxAnt | uint16\_t | Number of Rx antennas Value: 0<br>->65355 |

#### \*\*Table 11-1 Carrier Configuration Table\*\*

#### \*\*Table 11-2 Cell Configuration Table\*\*

| operationalState | uint8\_t | Operational state of the cell [Value:<br>ENABLED, DISABLED]<br>It indicates the operational state of<br>the NRCellDU instance. It describes<br>whether the resource is installed and<br>partially or fully operable (Enabled)<br>or the resource is not installed or not<br>operable (Disabled) |

|---------------------|---------|----------------------------------------------- --------------------------------------------------------------------------------

-------------------------------------------------------------------------------- --------------------------------------------------------------------------------

--|

| administrativeState | uint8\_t | Administrative state of the cell<br>[Value: LOCKED, SHUTTING<br>DOWN, UNLOCKED]<br>It indicates the administrative state<br>of the NRCellDU. It describes the |

![](\_page\_52\_Picture\_1.jpeg)

| | | permission to use or prohibition | |---------------|-------------------|------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ------------| | | | against using the cell, imposed | | | | through the OAM services | | | | | | cellState | uint16\_t | Usage state of the cell [Value: IDLE,<br>INACTIVE, ACTIVE] | | | | It indicates the usage state of the | | | | NRCellDU instance. It describes | | | | whether the cell is not currently in | | | | use (Idle), or currently in use but not | | | | configured to carry traffic (Inactive) | | | | or is currently in use and is config | | | | ured to carry traffic (Active) | | | | | | pLMNInfoList | uint64\_t | The list of PLMNs that can be served<br>by the cell, and which S-NSSAs can<br>be supported by the NR cell for cor<br>responding PLMN in case of network<br>slicing feature is supported. The<br>pLMNId of the first entry of the list is<br>the PLMNId used to construct the<br>nCGI for the NR cell. | | >> pLMNId | | This represent the PLMN Identity. | | >> sNSSAIList | | This represent the list of S-NSSAI<br>supported in the PLMN. This is a<br>conditional mandatory parameter if<br>network slicing feature is supported. | | nRPCI | uint16\_t | Physical Cell ID, [38.211,<br>sec 7.4.2.1] Value: 0 ->1007 | | | | It uniquely identifies a NR cell<br>within a PLMN | | nRTAC | uint64\_t / string | This information element is used to<br>identify a configured EPS Tracking<br>Area Code in order to enable appli<br>cation of Roaming and Access Re<br>strictions for EN-DC as specified in<br>TS 37.340 [7]. This IE is configured<br>for the cell, but not broadcast | | ssbFrequency | uint32\_t | Indicates cell defining SSB fre<br>quency domain position | | | | | | | | Frequency of the cell defining SSB<br>transmission. The frequency pro<br>vided in this attribute identifies the<br>position of resource element RE=#0 | | | | (subcarrier #0) of resource block | ![](\_page\_53\_Picture\_1.jpeg) | | | RB#10 of the SS block. The fre<br>quency must be positioned on the<br>NR global frequency raster, as de<br>fined in TS 38.101-1 [42] subclause<br>5.4.2. and within bSChannelBwDL.<br>Values: 0->3279165 | |---------------------------------|----------|---------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -----------------| | Subcarrier-spacing | uint16\_t | This is used for SSB synchroniza<br>tion. See subclause 5 in TS 38.104<br>[12]. Its units are in kHz. | | | | Values: {15, 30, 120, 240}. | | | | Note that the allowed values of SSB<br>used for representing data, by e.g. a<br>BWP, are: 15, 30, 60 and 120 in<br>units of kHz. |

| | | Subcarrier spacing of this carrier. It<br>is used to convert the offsetToCarrier<br>into an actual frequency. Only the<br>values 15 kHz, 30 kHz or 60 kHz<br>(FR1), and 60 kHz or 120 kHz (FR2)<br>are applicable | | | | | | DuplexType | uint8\_t | Frame duplex type | | | | Value:0 = FDD | | | | 1 = TDD | | Sib1CfgAndInfo | | | | > PdcchCfgSib1 | | | | {CoresetZeroIndex, | | | | SearchSpaceZroIndex} | | | | > \*sib1Pdu | uint8\*t | | | | | | | > Sib1PduLen | uint16\_t | | | > pagingCfg | | | | { numPO/ Ns, | | | | poPresent, | | | | pagingOcc[MAX\_PO\_PER\_PF<br>= 4] | | | | Initial DL BWP | struct | Spec 38.331 DownlinkConfigCom | | | | monSIB |

## ![](\_page\_54\_Picture\_1.jpeg)

|  |  |  | Initial UL Bwp   struct   Spec 38.331 UplinkConfigCom<br>monSIB   |  |
|--|--|--|-------------------------------------------------------------------|--|
|  |  |  | ---------------- -------- --------------------------------------- |  |
|  |  |  |                                                                   |  |

### #### \*\*Table 11-3 SSB Configuration Table\*\*

| ssPbchPower                                                                                                                                                                                                                                                                                                                                                                                                         | uint32_t                                                         |                                  |                                  | SSB Block Power Value: s (-6050<br>dBm)                                                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|----------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <br> ----------------------- ------------- -----------------------------------------                                                                                                                                                                                                                                                                                                                                |                                                                  |                                  |                                  |                                                                                                                                             |
| --------------------------------------------------------------------------------<br>--------------------------------------------------------------------------------                                                                                                                                                                                                                                                |                                                                  |                                  |                                  |                                                                                                                                             |
| --------------------------------------------------------------------------------                                                                                                                                                                                                                                                                                                                                    |                                                                  |                                  |                                  |                                                                                                                                             |
| --------------------------------------------------------------------------------<br>--------------------------------------------------------------------------------                                                                                                                                                                                                                                                |                                                                  |                                  |                                  |                                                                                                                                             |
| ------                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                  |                                  |                                  |                                                                                                                                             |
| subcarrier-spacing<br>initial<br>access<br>and<br>Value:0->3<br>Subcarrier spacing of this carrier. It<br>is used to convert the<br>offsetToCarrier<br>into an actual frequency. Only the<br>values 15 kHz, 30 kHz or<br>60<br>kHz<br>(FR1),<br>and<br>                                                                                                                                                             | uint8_t<br>broadcast<br>60<br>kHz                                | mes<br>sage.<br>or<br>120<br>kHz | [38.211<br>(FR2)<br>are          | subcarrierSpacing for common, used<br>for<br>sec<br>4.2]<br>applicable                                                                      |
| offset-to-carrier<br>lowest<br>resource block used for SS/PBCH<br>block. Given in PRB [38.211,<br>sec<br>tion<br>4.4.4.2]<br>between<br>Point A (lowest subcarrier of com<br>mon RB 0) and the lowest<br>usable<br>subcarrier<br>on<br>subcarrierSpac<br>ing defined for this carrier). The<br>maximum value corresponds<br>to<br>275*8-1. See TS 38.211 [16], clause<br>4.4.2  <br>  SsbPeriod<br>1:<br>ms10<br>2: | uint16_t<br>Value:<br>this<br>carrier<br>  uint8_t<br>ms20<br>3: | 0->2199<br>Offset<br>in<br>ms40  | in<br>number<br>of<br>4:<br>ms80 | Offset of lowest subcarrier of<br>frequency<br>domain<br>PRBs<br>(using<br>the<br>  SSB periodicity in msec Value: 0:<br>ms5<br>5:<br>ms160 |
| <br>  SsbSubcarrierOffset<br>section                                                                                                                                                                                                                                                                                                                                                                                | uint8_t<br>7.4.3.1)                                              |                                  |                                  | ssbSubcarrierOffset or 𝑘𝑆𝑆𝐵<br>(38.211,<br>Value:<br>0->31                                                                                  |
| <br>  SsbMask[SSB_MAX_SIZE]   uint32_t[2]   Bitmap for actually transmitted SSB.<br>As<br>per Spec SCF222, Table 3–46<br>'SSB_resource Configuration', This<br>is the array<br>of size<br>SSB_MAX_SIZE=2<br>MSB->LSB of first 32 bit number<br>corresponds to<br>SSB<br>0<br>                                                                                                                                       |                                                                  | to                               | SSB                              | 31                                                                                                                                          |
| ![](_page_55_Picture_1.jpeg)                                                                                                                                                                                                                                                                                                                                                                                        |                                                                  |                                  |                                  |                                                                                                                                             |
| <br> <br>SSB<br>32<br>to<br>SSB                                                                                                                                                                                                                                                                                                                                                                                     | 63<br>Value<br>for                                               | each                             | bit:<br>•<br>0:                  | MSB->LSB of second 32 bit number<br>corresponds to<br>not<br>transmitted                                                                    |
| <br> ---------------- --------- ----------------------------------------------------<br>--------------------------------------------------------------------------------                                                                                                                                                                                                                                            |                                                                  |                                  |                                  |                                                                                                                                             |

---------------------------------------| | | | • 1: transmitted | | BeamId [64] | uint8\_t | BeamID for each SSB in SsbMask.<br>For example, if SSB mask bit 26 is<br>set to 1, then BeamId [26] will be<br>used to indicate beam ID of SSB 26.<br>Value: from 0 to 63 | | betaPss | uint8\_t | PSS EPRE to SSS EPRE in a<br>SS/PBCH block [38.213, sec 4.1]<br>Values: 0 = 0dB 1 = 3dB | | bchPayloadFlag | uint8\_t | bchPayload to determine how it its<br>generated, req by FAPI | | | | 0: MAC generates the full PBCH<br>payload | | | | 1: PHY generates the timing PBCH<br>bits | | | | 2: PHY generates the full PBCH<br>payload | | bchPayload | uint8\_t | | | dmrsTypeAPos | uint8\_t | The position of the first DM-RS for<br>downlink and uplink. Value: 0 -> 1 |

## #### \*\*Table 11-4 PRACH Configuration\*\*

| prachSequenceLength | uint8\_t | RACH sequence length. Long or<br>Short sequence length. Only short<br>sequence length is supported for<br>FR2. [38.211, sec 6.3.3.1]<br>Value: 0 = Long sequence 1 =<br>Short sequence | |---------------------|---------|-----------------------------------------------

---------------------------------------------------------|

| prachSubCSpacing | uint8\_t | Subcarrier spacing of PRACH.<br>[38.211 sec 4.2Tables 6.3.3.1-2<br>and 6.3.3.1-7]<br>Value:0->34 |

--------------------------------------------------------------------------------

| numPrachFdOccasions | uint8\_t | Number of RACH frequency do<br>main occasions. Corresponds to the<br>parameter in [38.211, sec<br>6.3.3.2] which equals the higher<br>layer parameter msg1FDM<br>Value: 1,2,4,8 |

![](\_page\_56\_Picture\_1.jpeg)

|  | prachConfigIndex[]                                                              |  | uint8_t |  | PRACH | configuration | index. |
|--|---------------------------------------------------------------------------------|--|---------|--|-------|---------------|--------|
|  |                                                                                 |  |         |  |       |               |        |
|  | ------------------------- ---------- ------------------------------------------ |  |         |  |       |               |        |

-------------------------------------------------------------------------------- -------------------------------------| | | | Following parameters will be hav<br>ing unique values for each in<br>stances of PRACH Frequency oc<br>casion. The array size will be<br>'numPrachFdOccasions' | | | | MAX size of array is 8. | | | | Value: from 0 to 255 | | >prachRootSequenceIndex | uint16\_t | Starting logical root sequence in<br>dex, , equivalent to higher layer<br>parameter prach-RootSequenceIn<br>dex [38.211, sec 6.3.3.1] | | | | Value: 0 -> 837 | | >numRootSequences | uint8\_t | Number of root sequences for a<br>particular FD occasion that are re<br>quired to generate the necessary<br>number of preambles | | >k1 | uint16\_t | Frequency offset (from UL band<br>width part) for each FD. [38.211,<br>sec 6.3.3.2] | | | | Value: from 0 to 272 | | >prachZeroCorrConf | uint8\_t | PRACH Zero CorrelationZone<br>Config which is used to derive <br>[38.211, sec 6.3.3.1] | | | | Value: from 0 to 15 | | restrictedSetConfig | uint8\_t | PRACH restricted set config | | | | Value: | | | | 0: unrestricted | | | | 1: restricted set type A | | | | 2: restricted set type B | | ssbPerRach | uint8\_t | SSB-per-RACH-occasion Value:<br>0: 1/8 | | | | 1:1/4, | | | | 2:1/2 | | | | 3:1

|  |  | 4:2  |
|--|--|------|
|  |  |      |
|  |  | 5:4, |
|  |  |      |
|  |  | 6:8  |
|  |  |      |
|  |  | 7:16 |

## ![](\_page\_57\_Picture\_1.jpeg)

|  | numCbPreamblePerSsb                                                                                                                                |  | uint8_t |  | Number | of | CBRA | preamble | per<br>SSB |
|--|----------------------------------------------------------------------------------------------------------------------------------------------------|--|---------|--|--------|----|------|----------|------------|
|  | --------------------- --------- -----------------------------------------------                                                                    |  |         |  |        |    |      |          |            |
|  | --------------------------------------------------------------------------------                                                                   |  |         |  |        |    |      |          |            |
|  | --------------------------------------------------------------------------------<br>-------------------------------------------------------------- |  |         |  |        |    |      |          |            |
|  |                                                                                                                                                    |  |         |  |        |    |      |          |            |

| raRspWReqindow | uint8\_t | RA response window<br>Msg2 (RAR) window length in<br>number of slots. |

| Msg1FreqStart | uint8\_t | Offset of lowest PRACH transmis<br>sion occasion in frequency domain<br>with respective to PRB 0. The<br>value is configured so that the cor<br>responding RACH resource is en<br>tirely<br>within the bandwidth of the UL<br>BWP. (see TS 38.211 [16], clause<br>6.3.3.2). |

| totalNumRaPreamble | uint8\_t | Total number of preambles used<br>for contention based and conten<br>tion free 4-step or 2-step random<br>access in the RACH resources

|

|

## #### \*\*Table 11-5 TDD Configuration\*\*

| dl-ul-transmission-periodicity | uint8\_t<br>/enumeration | "Periodicity of the DL-UL pattern,<br>see TS 38.213 [13], clause 11.1. If<br>the dl-UL-TransmissionPeriodicity<br>v1530 is signalled, UE ignores the<br>dl-UL-TransmissionPeriodicity<br>(without suffix).". |

| -------------------------------- ------------------------- --------------------  |    |  |             |                    |
|----------------------------------------------------------------------------------|----|--|-------------|--------------------|
| -------------------------------------------------------------------------------- |    |  |             |                    |
| -------------------------------------------------------------------------------- |    |  |             |                    |
| --------------------------                                                       |    |  |             |                    |
|                                                                                  |    |  |             | DL UL Transmission |
| Periodicity<br>Value:                                                            | 0: |  | ms0p5<br>1: | ms0p625            |
|                                                                                  |    |  |             |                    |
|                                                                                  |    |  |             | 2: ms1             |

| | | | 3: ms1p25 | | | | 4: ms2 | | | | 5: ms2p5 | | | | 6: ms5 | | | | s7: ms10 | | nr-of-downlink-slots | uint16\_t | Number of consecutive full DL slots<br>at the beginning of each DL-UL pat<br>tern, see TS 38.213 [13], clause 11.1.<br>In this release, the maximum value<br>for this field is 80. | ![](\_page\_58\_Picture\_1.jpeg) | nr-of-downlink-symbols | uint8\_t | Number of consecutive DL symbols<br>in the beginning of the slot following<br>the last full DL slot (as derived from<br>nrofDownlinkSlots). The value 0 in<br>dicates that there is no partialdown<br>link slot. (see TS 38.213 [13], clause<br>11.1) | |------------------------|----------|------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ---------------------------------------------| | nr-of-uplink-slots | uint16\_t | Number of consecutive full UL slots<br>at the end of each DL-UL pattern,<br>see TS 38.213 [13], clause 11.1. In<br>this release, the maximum value for<br>this field is 80 | | nr-of-uplink-symbols | uint8\_t | Number of consecutive UL symbols<br>in the end of the slot preceding the<br>first full UL slot (as derived from<br>nrofUplinkSlots). The value 0 indi<br>cates that there is no partialuplink<br>slot. (see TS 38.213 [13], clause<br>11.1) | | SlotConfig | uint8\_t | For each symbol in each slot within<br>max

TDD periodicity a uint8\_t value<br>is provided indicating: 0: DL slot<br>1: UL slot<br>2: Guard slot

|

#### \*\*Table 11-6 Precoding Configuration\*\*

|  | numLayers                                                                       |  |  |  |  | uint16_t   Number of ports at the precoder in<br>put |
|--|---------------------------------------------------------------------------------|--|--|--|--|------------------------------------------------------|
|  |                                                                                 |  |  |  |  |                                                      |
|  | ------------- ---------- ------------------------------------------------------ |  |  |  |  |                                                      |

-------| | | | Value: 0->8 | | numAntPorts | uint16\_t | Number of ports at the precoder out<br>put<br>sValue: 0->64 |

#### \*\*Table 11-7 Beamforming Configuration (Reference: TS 28.541 NRM section 4.3.40)\*\*

|  | numofBeams   uint16_t   Number of beams   |                            |              |  |
|--|-------------------------------------------|----------------------------|--------------|--|
|  | ------------ ---------- ----------------- |                            |              |  |
|  |                                           |                            | Value: 0->64 |  |
|  | numTXRUs                                  | uint16_t   Number of ports |              |  |
|  |                                           |                            | Value: 0->64 |  |

## ![](\_page\_59\_Picture\_1.jpeg)

| <br>beamIndex                                                                                                                                                       |  |  | uint16_t                                       |  | For     | each                  | beam       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|------------------------------------------------|--|---------|-----------------------|------------|
|                                                                                                                                                                     |  |  |                                                |  |         |                       |            |
| ---------------- ---------- ---------------------------------------------------<br>-------------------------------------------------------------------------------- |  |  |                                                |  |         |                       |            |
| --------------------------------------------------------------------------------                                                                                    |  |  |                                                |  |         |                       |            |
| --------------------------------------------------------------------------------                                                                                    |  |  |                                                |  |         |                       |            |
| --------------------------------------------------------------------------------                                                                                    |  |  |                                                |  |         |                       |            |
| --------------------------------------------------------------------------------                                                                                    |  |  |                                                |  |         |                       |            |
| --------------------------------------------------------------------------------<br>--------------------------------------------------------                        |  |  |                                                |  |         |                       |            |
| <br>                                                                                                                                                                |  |  | Identifying number for the beam in<br>dex      |  |         |                       |            |
|                                                                                                                                                                     |  |  |                                                |  |         | Value:                | 0->64      |
| <br> <br>beamType                                                                                                                                                   |  |  | uint16_t                                       |  | For     | each                  | beam       |
| <br>                                                                                                                                                                |  |  |                                                |  |         | The type of the beam. |            |
| <br>                                                                                                                                                                |  |  |                                                |  | Values: |                       | "SSB-BEAM" |
| <br> <br>beamAzimuth                                                                                                                                                |  |  | uint32_t                                       |  | For     | each                  | beam       |
| <br>                                                                                                                                                                |  |  | sThe azimuth of a beam transmis<br>sion, which |  |         |                       |            |
| means the horizontal<br>beamforming pointing angle (beam<br>peak direction) in                                                                                      |  |  |                                                |  |         |                       |            |
| the (Phi) φ-axis in<br>1/10th degree resolution. See sub<br>clauses 3.2 in TS                                                                                       |  |  |                                                |  |         |                       |            |
| 38.104 [12] and 7.3<br>in TS 38.901 [53] as well as TS<br>28.662 [11]. The pointing                                                                                 |  |  |                                                |  |         |                       |            |

angle is<br>the direction equal to the geometric<br>center of the half-power

contour of<br>the beam relative to the reference<br>plane. Zero degree implies explicit<br>antenna bearing (boresight). Positive<br>angle implies clockwise from the an<br>tenna bearing.<br>Values: [-1800 1800] 0.1 degree |

| beamTilt | uint32\_t | For each beam | | | | The tilt of a beam transmission,<br>which means the vertical beamform<br>ing pointing angle (beam peak direc<br>tion) in the (Theta) θ-axis in 1/10th<br>degree resolution. See subclauses<br>3.2 in TS 38.104 [12] and 7.3 in TS<br>38.901 [53] as well as TS 28.662<br>[11]. The pointing angle is the direc<br>tion equal to the geometric center of<br>the half-power contour of the beam<br>relative to the reference plane. Posi<br>tive value implies downtilt.<br>Values: [-900900] 0.1 degree |

| beamHorizWidth | uint32\_t | For each beam |

![](\_page\_60\_Picture\_1.jpeg)

| | | The Horizontal beamWidth of a<br>beam transmission, which means the<br>horizontal beamforming half-power<br>(3dB down) beamwidth in the (Phi)<br>φ-axis in 1/10th degree resolution.<br>See subclauses 3.2 in TS 38.104 [12]<br>and 7.3 in TS 38.901 [53].<br>Values: [03599] 0.1 degree | |----------------|----------|--------------------------------------------------- -------------------------------------------------------------------------------- --------------------------------------------------------------------------------

--------------------------------------------------------------------------------

-------------------------------------------------------------------------------- --------------------------------|

|

| beamVertWidth | uint32\_t | For each beam<br>The Vertical beamWidth of a beam<br>transmission, which means the verti<br>cal beamforming half-power (3dB<br>down) beamwidth in the (Theta) θ<br>axis in 1/10th degree resolution. See<br>subclauses 3.2 in TS 38.104 [12] and<br>7.3 in TS 38.901 [53].<br>Values: [01800] 0.1 degree

| coverageShape | uint32\_t | Identifies the sector carrier coverage<br>shape described by the envelope of<br>the contained SSB beams. The cov<br>erage shape is implementation de<br>pendent.<br>Values: 0: 65535 |

| digitalTilt | uint32\_t | Digitally controlled tilt through<br>beamforming. It represents the verti<br>cal pointing direction of the antenna<br>relative to the antenna bore sight,<br>representing the total non-mechani<br>cal vertical tilt of the selected cover<br>ageShape. Positive value gives<br>downwards tilt and negative value<br>gives upwards tilt.<br>Values: [-900900] 0.1 degree | | digitalAzimuth | uint32\_t | Digitally controlled azimuth through<br>beamforming. It represents the hori<br>zontal pointing direction of the an<br>tenna relative to the antenna bore<br>sight, representing the total non-me<br>chanical horizontal pan of the se<br>lected coverageShape. Positive value<br>gives azimuth to the right and nega<br>tive value gives an azimuth to the<br>left.<br>allowed Values: [-1800 1800] 0.1<br>degree |

![](\_page\_61\_Picture\_0.jpeg)

![](\_page\_61\_Picture\_1.jpeg)

In case of hierarchical architecture, O-DU receives the aggregated RU configuration, disaggregate the RU configuration per each RU instance and send the specific configurations towards O-RU. The below table captures the beam forming configuration towards O-RU applicable for hierarchical approach.

Beamforming configuration as per O-RAN Fronthaul M-plane specification [21]

| per-band-config                                                                          |    |               |             |
|------------------------------------------------------------------------------------------|----|---------------|-------------|
| <br> -------------------------------------------------- ------------- --------------     |    |               |             |
| --------------------------------------------------------------------------------<br>---- |    |               |             |
| > band-number                                                                            |    | uint16        | Band number |
| supported                                                                                | at |               | O-RU        |
| <br>  > tx-array<br>                                                                     |    | uint16        | Tx path     |
| > rx-array<br>                                                                           |    | uint16        | Rx path     |
| > static-properties<br>                                                                  |    |               |             |
| >> rt-bf-weights-update-support                                                          |    | boolean       | Real time   |
| beam forming weight up<br>date if supported at O-RU in case of<br>digital                |    |               |             |
| beamforming.                                                                             |    |               |             |
| >> beamforming-type                                                                      |    |               |             |
| <br>  >>> frequency                                                                      |    |               | if the beam |
| forming<br>type                                                                          | is | fre<br>quency | domain      |
| <br>  >>>> frequency-domain<br>beams<br>                                                 |    |               |             |
| >>>> max-number-of<br>beam-ids                                                           |    | uint16        | Maximum     |

| number   | of                             | beams | sup<br>ported                                    | in     | frequency | domain                    |
|----------|--------------------------------|-------|--------------------------------------------------|--------|-----------|---------------------------|
| <br>     | >>>> initial-beam-id           |       |                                                  | uint16 |           | Beam index                |
|          | >>>> iq-bitwidth               |       |                                                  |        | uint8     |                           |
|          | >>>> compression-type          |       |                                                  |        |           | enumeration               |
|          | >>>> bitwidth                  |       |                                                  |        | uint8     |                           |
|          | >>>> compression-format        |       |                                                  |        |           |                           |
|          |                                |       | >>>> additional-compres<br>sion-method-supported |        |           |                           |
| >>> time |                                |       |                                                  |        |           |                           |
|          |                                |       |                                                  |        |           |                           |
|          | >>>> time-domain-beams         |       |                                                  |        |           |                           |
| forming  |                                | type  | is                                               | time   |           | if the beam<br>do<br>main |
|          | >>>> max-number-of-beam<br>ids |       |                                                  |        | uint16    | Maximum                   |
| number   | of                             | beams | sup<br>ported                                    | in     | time      |                           |
|          | >>>> initial-beam-id           |       |                                                  |        | uint16    | domain<br>                |
|          | >>>> frequency-granularity     |       |                                                  |        |           | enumeration               |
|          | >>>> time-granularity          |       |                                                  |        |           | enumeration               |
| <br>     | >>>> iq-bitwidth               |       |                                                  |        | uint8     |                           |

## ![](\_page\_62\_Picture\_1.jpeg)

| >>>> bitwidth                                                                        |  | uint8<br> |
|--------------------------------------------------------------------------------------|--|-----------|
| <br> ----------------------------------------------------- ------------- ----------- |  |           |
| ------------------------------------------------- <br>  >>>> compression-format      |  |           |
| <br>  >>>> additional-compres<br>sion-method-supported                               |  |           |
| <br>  >>> hybrid                                                                     |  | Hybrid    |

```
architecture is preferred for<br>frequencies > 6GHz |
| >>>> hybrid-beams | | if the 
beam forming type is hybrid<br>domain |
| >>>> max-number-of-beam<br>ids | uint16 | Maximum 
number of beams sup<br>ported in hybrid domain |
| >>>> initial-beam-id | uint16 | 
|
| >>>> frequency-granularity | enumeration | 
|
| >>>> time-granularity | enumeration | 
|
| >>>> iq-bitwidth | uint8 | 
|
| >>>> compression-type | enumeration | 
|
| >>>> bitwidth | uint8 | 
|
| >>>> compression-format | | 
|
| >> number-of-beams | uint16 | Number of 
beams supported in the<br>O-RU |
| > beam-information | | 
|
| >> number-of-beamforming<br>properties | uint16 | Beam 
forming properties for each<br>beam |
| >> beamforming-properties | | 
|
| >>> beam-id | uint16 | 
|
| >>> beamforming-property | | 
|
| >>>> beam-type | enumeration | 
|
| >>>> beam-group-id | uint16 | 
|
| >>>> coarse-fine-beam-rela<br>tion | | 
|
| >>>> neighbor-beams | | 
|
| >>>> coarse-fine-beam-capa<br>bility-based-relation | | 
|
| >>>> neighbor-beams-capabil<br>ity-based | | 
|
| capabilities-group | uint16 |
```

```
|
```

|

## ![](\_page\_63\_Picture\_0.jpeg)

| > tx-array                                                                           | uint16<br>  |
|--------------------------------------------------------------------------------------|-------------|
| -------------------------------------------------- ------------- -- <br>  > rx-array | uint16<br>  |
| > static-properties                                                                  | <br>        |
| >> rt-bf-weights-update-support                                                      | boolean<br> |
| >> beamforming-type                                                                  | <br>        |
| >>> frequency                                                                        | <br>        |
| >>>> frequency-domain-beams                                                          | <br>        |
| >>>> max-number-of-beam-ids                                                          | uint16<br>  |
| >>>> initial-beam-id                                                                 | uint16<br>  |
| >>>> iq-bitwidth                                                                     | uint8<br>   |
| >>>> compression-type                                                                | enumeration |
| >>>> bitwidth                                                                        | uint8<br>   |
| >>>> compression-format                                                              | <br>        |
| >>>> additional-compression<br>method-supported                                      |             |
| >>> time                                                                             | <br>        |
| >>>> time-domain-beams                                                               | <br>        |
| >>>> max-number-of-beam-ids                                                          | uint16<br>  |
| >>>> initial-beam-id                                                                 | uint16<br>  |
| >>>> frequency-granularity                                                           | enumeration |
| >>>> time-granularity                                                                | enumeration |
| >>>> iq-bitwidth                                                                     | uint8<br>   |
| >>>> compression-type                                                                | enumeration |
| >>>> bitwidth                                                                        | uint8<br>   |
| >>>> compression-format                                                              | <br>        |
| >>>> additional-compression<br>method-supported*                                     |             |
| >>> hybrid                                                                           | <br>        |
| >>>> hybrid-beams                                                                    | <br>        |
| >>>> max-number-of-beam-ids                                                          | uint16<br>  |
| >>>> initial-beam-id                                                                 | uint16<br>  |
| >>>> frequency-granularity                                                           | enumeration |
| >>>> time-granularity                                                                | enumeration |

## ![](\_page\_64\_Picture\_0.jpeg)

| >>>> iq-bitwidth                                                     | uint8       |  |  |
|----------------------------------------------------------------------|-------------|--|--|
| --------------------------------------------------- ------------- -- |             |  |  |
| >>>> compression-type                                                | enumeration |  |  |

| >>>> bitwidth                                               | uint8<br>   |  |
|-------------------------------------------------------------|-------------|--|
| >>>> compression-format                                     | <br>        |  |
| >>>> additional-compression<br>method-supported             | <br>        |  |
| >> number-of-beams                                          | uint16<br>  |  |
| > beam-information                                          | <br>        |  |
| >> number-of-beamforming-prop<br>erties                     | uint16<br>  |  |
| >> beamforming-properties                                   | <br>        |  |
| >>> beam-id                                                 | <br>        |  |
| >>> beamforming-property                                    | <br>        |  |
| >>>> beam-type                                              | enumeration |  |
| >>>> beam-group-id                                          | uint16<br>  |  |
| >>>> coarse-fine-beam-relation                              | <br>        |  |
| >>>> neighbor-beams                                         | <br>        |  |
| > ue-specific-beamforming                                   | <br>        |  |
| >> max-number-of-ues                                        | uint8<br>   |  |
| > operational-properties                                    | <br>        |  |
| >> number-of-writeable-beam<br>forming-files                | uint8<br>   |  |
| >> update-bf-non-delete                                     | boolean<br> |  |
| >> persistent-bf-files                                      | boolean<br> |  |
| > beamforming-trough-attributes<br>supported                | boolean<br> |  |
| > beamforming-trough-ue-channel<br>info-supported   boolean |             |  |
| > beam-tilt                                                 | <br>        |  |
| >> predefined-beam-tilt-offset-in<br>formation              | <br>        |  |
| >>> band-number                                             | <br>        |  |
| >>> elevation-tilt-granularity                              | uint8<br>   |  |
| >>> azimuth-tilt-granularity                                | uint8<br>   |  |

![](\_page\_65\_Picture\_1.jpeg)

| >>> minimum-supported-eleva<br>tion-tilt   int16                                |         |  |                     |
|---------------------------------------------------------------------------------|---------|--|---------------------|
| ------------------------------------------ --------- --                         |         |  |                     |
| >>> maximum-supported-eleva<br>tion-tilt   int16                                |         |  |                     |
| >>> minimum-supported-azimuth<br>tilt                                           | int16   |  |                     |
| >>> maximum-supported-azimuth<br>tilt                                           | int16   |  |                     |
| >>> run-time-tilt-offset-supported                                              | boolean |  |                     |
| >> predefined-beam-tilt-state                                                   |         |  |                     |
| >>> band-number                                                                 | int16   |  |                     |
| >>> offset-elevation-tilt-angle                                                 | int16   |  |                     |
| >>> offset-azimuth-tilt-angle                                                   | int16   |  |                     |
| > activate-beamforming-config<br>configuration<br>if supported at O-RU          | rpcs    |  | Modify beam forming |
| -------------------------------------- --------------- ------------------------ |         |  |                     |
| -----------------------------------                                             |         |  |                     |

| > beamforming-information-up<br>date | notifications | Notify beam forming information<br>update |

| <br>csirsfrequencyDomainAllocation<br>{                                   | <br>BIT<br>STRING<br> <br>CHOICE<br>                                            |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| -------------                                                             | ----------------------------------- ------------ ------------------------------ |
| <br>(4)),<br>                                                             | <br>  row1<br>BIT STRING (SIZE                                                  |
|                                                                           | <br>  row2<br>BIT STRING (SIZE                                                  |
| (12)),<br> <br>                                                           | <br>  row4<br>BIT STRING (SIZE                                                  |
| (3)),<br> <br>                                                            | <br>  other BIT STRING (SIZE (6))                                               |
| <br>                                                                      | <br>  },                                                                        |
| <br>  csirsnrofPorts                                                      | uint8_t<br>  ENUMERATED                                                         |
| {p1,p2,p4,p8,p12,p16,p24,p32},  <br> <br>csirsfirstOFDMSymbolInTimeDomain | <br>uint8_t<br> <br>INTEGER<br>(013),                                           |
| <br>                                                                      | <br>                                                                            |
| <br> <br>csirsfirstOFDMSymbolInTimeDomain2                                | <br>uint8_t<br> <br>INTEGER<br>(212)                                            |
| <br>  csirscdm-Type                                                       | uint8_t<br>  ENUMERATED {noCDM, fd-CDM2,                                        |
| cdm4-FD2-<br> <br>                                                        | <br>  TD2, cdm8-FD2-TD4}                                                        |
| <br>  Csirsdensity                                                        | uint8_t<br>  CHOICE                                                             |
| {<br>                                                                     | <br> <br>  dot5<br>ENUMERATED {evenPRBs,                                        |
| oddPRBs},<br> <br>                                                        | <br>  one<br>NULL,                                                              |
| <br>                                                                      | <br>  three<br>NULL,                                                            |
| <br>                                                                      | <br>  spare<br>NULL                                                             |
| <br>                                                                      | <br>  },                                                                        |
| <br>  csirsdensitydot5                                                    | uint8_t<br>  ENUMERATED {evenPRBs,                                              |

#### \*\*Table 11-8 CSI-RS Configuration (Reference: 38.331 CSI-MeasConfig.)\*\*

```
oddPRBs}, |
| | | 
|
| powerControlOffset | uint8_t | INTEGER (-815) 
|
| powerControlOffsetSS | uint8_t | ENUMERATED{db-3, db0, db3, 
db6} |
| | | 
|
```

```
#### **O-RAN.WG8.AAD.0-R004-v14.00**
```

![](\_page\_66\_Picture\_1.jpeg)

| periodicityAndOffset   uint16_t   slots4 INTEGER (03), |  |                                                              |
|--------------------------------------------------------|--|--------------------------------------------------------------|
|                                                        |  | ---------------------- ---------- -------------------------- |
|                                                        |  | slots5 INTEGER (04),<br>                                     |
|                                                        |  | slots8 INTEGER (07),<br>                                     |
|                                                        |  | slots10 INTEGER (09),<br>                                    |
|                                                        |  | slots16 INTEGER (015),<br>                                   |
|                                                        |  | slots20 INTEGER (019),<br>                                   |
|                                                        |  | slots32 INTEGER (031),<br>                                   |
|                                                        |  | slots40 INTEGER (039),<br>                                   |
|                                                        |  | slots64 INTEGER (063),<br>                                   |
|                                                        |  | slots80 INTEGER (079),<br>                                   |
|                                                        |  | slots160 INTEGER (0159),                                     |
|                                                        |  | slots320 INTEGER (0319),                                     |
|                                                        |  | slots640 INTEGER (0639)                                      |
|                                                        |  | <br>                                                         |

#### \*\*Table 11-9 SRS Configuration\*\*

| nrofSymbols  | uint8_t   ENUMERATED {n1, n2, n4},                                           |  |
|--------------|------------------------------------------------------------------------------|--|
|              | ------------------ --------- ----------------------------------------------- |  |
| resourceType | uint8_t   CHOICE {aperiodic, semi-persistent, periodic}                      |  |
|              | transmissionComb   uint8_t   CHOICE { n2, n4 }                               |  |
| p0           | int32_t   INTEGER (-20224)                                                   |  |

### <span id="page-66-0"></span>11.2.1.2 Slice Configuration

#### \*\*Table 11-10 Slice Configuration\*\*

| RRMPolicyList | | List of RRM policy in case of multi<br>ple dedicated slices | |-----------------------|----------|-------------------------------------------- --------------------------------------------------------------------------------

-------------------------------------------------------------|

| > resourceType | uint16\_t | This defines type of resource (PRB,<br>RRC connected users, DRB usage)<br>that is subject to policy. Valid values<br>are 'PRB', 'RRC' or 'DRB' | | > rRMPolicyMemberList | | It represents the list of RRMPolicy<br>Member(s) that include the PLMNId<br>and S-NSSAI | | >> RRMPolicyMember | | | | >>> pLMNId | uint16\_t | It defines the PLMN identifier. | | >>> sNSSAI | uint32\_t | This constitute of SST and SD value. | | > RRMPolicyRatio | | | | >> rRMPolicyMaxRatio | uint8\_t | This attribute specifies the

maximum<br>percentage of radio resource that can<br>be used by the associated rRMPoli<br>cyMemberList/SNSSAI. The maxi<br>mum percentage of radio resource |

![](\_page\_67\_Picture\_1.jpeg)

----------|

| | | include at least one of the shared re<br>sources, prioritized resources and<br>dedicated resources. The sum of the<br>rRMPolicyMaxRatio values assigned<br>to all slices can be greater than 100.

| |----------------------------|---------|---------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- --------------------------------------------------------------------------------

| >> rRMPolicyMinRatio | uint8\_t | This attribute specifies the minimum<br>percentage of radio resources that<br>can be used by the associated rRM<br>PolicyMemberList/sNSSAI. The<br>minimum percentage of radio re<br>sources including at least one of pri<br>oritized resources and dedicated re<br>sources. The sum of the rRMPoli<br>cyMinRatio values assigned to all<br>slices be less than or equal to100. |

| >> rRMPolicyDedicatedRatio | uint8\_t | This attribute specifies the percent<br>age of radio resource that dedicat<br>edly used by the associated rRMPoli<br>cyMemberList/sNSSAI. The sum of<br>the rRMPolicyDeidctaedRatio values<br>assigned to all slices be less than or<br>equal to100. ### <span id="page-67-0"></span>11.2.2 MAC - O-DU-OAM-Agent Interface

The following table details the performance statistics for various features to be reported from MAC layer towards the O-DU OAM agent. The cell specific measurements or the distribution of UE statistics received by the gNB from UEs in that cell (Reference [21] and reference [26] ) are reported in these interface functions.

The below MU-MIMO feature related statistics helps to fix and improve the MU-MIMO algorithms in the Non RT-RIC/rAPPs which is AI/ML driven and optimize the specific MU-MIMO configuration towards the gNB system.

| Direction<br>  Message/API                                                       |              |
|----------------------------------------------------------------------------------|--------------|
| Description                                                                      |              |
|                                                                                  |              |
| -------------------------- ---------------------------------------------- -----  |              |
| -------------------------------------------------------------------------------- |              |
| -------------------------------------------------------------------------------- |              |
| ------------------                                                               |              |
| MAC to O-DU-OAM<br>Agent   RSRP/RSRQ/SINR measure<br>ments                       | API          |
| to transfer the performance metric for the SS<br>RSRP distribution per SSB, SS   |              |
| RSRQ distribution<br>per SSB and SS-SINR distribution per SSB in the<br>cell for |              |
| the GoB use case.                                                                |              |
| MAC to O-DU-OAM<br>Agent   Measurement for the SSB beam<br>switch                | API          |
| to transfer the performance metrics for Beam<br>switching and beam switching     |              |
| interval<br>per<br>cell<br>for<br>the<br>GoB                                     | use<br>case. |
|                                                                                  |              |
| MAC to O-DU-OAM<br>Agent   Beam Failure statistics per cell<br>per beam   API    |              |
| to transfer the performance metrics for beam<br>failure statistics per cell per  |              |
| beam<br>for<br>the<br>GoB                                                        | use<br>case. |
|                                                                                  |              |
| MAC to O-DU-OAM<br>Agent   UL SRS RSRP measurement                               | API          |
| to transfer the performance metrics for SRS<br>RSRP in the UL for non GoB use    |              |
| case.                                                                            |              |
|                                                                                  |              |

### <span id="page-67-1"></span>11.2.3 RLC-MAC Interface

The following table details the interactions between RLC and MAC for data transfer and reporting operations.

![](\_page\_68\_Picture\_1.jpeg)

|

#### #### \*\*Table 11-11 RLC-MAC Interface\*\*

| Direction | Message/API | Description | |------------|--------------------------------|--------------------------------- ----| | RLC to MAC | Data transfer (DL) | API to transfer downlink data | | MAC to RLC | Data transfer (UL) | API to transfer uplink data | | MAC to RLC | Schedule result reporting (DL) | DL schedule result Reporting to RLC | | RLC to MAC | Buffer status reporting (DL) | DL data volume in the RLC entity | Note: DL: - 1. RLC -> MAC: The Buffer status in RLC - 2. MAC -> RLC: the schedule result Reporting to RLC, then RLC decide how to implement the RLC segment. - 3. RLC->MAC: DL data UL: 1. MAC-> RLC: UL data ### <span id="page-68-0"></span>11.2.3.1 Data Transfer (DL) #### \*\*Table 11-12 RLC-MAC Data transfer (DL) message contents\*\* | Element | Presence | Description | |---------------------------------------------------|----------|---------------- -------------------------------------------------------------------------------- -----------------| | Frame Number | M | Air interface time | | Slot Number | M | Air interface time | | Cell Index | M | Identification of the Cell |

| UE Index | M | Identification of the UE | | Number of RLC PDUs | M | Number of RLC PDUs to be sent | | RLC PDU info (RB Type, LCID, PDU<br>LEN, RLC PDU) | M | Radio Bearer type, LCID and length<br>for the RLC PDU, RLC PDU data | | numLC | M | | | Buffer Occupancy[numLC] | M | This is the buffer occupancy infor<br>mation for the logical channel that<br>needs to be informed to scheduler. |

#####################################SPEC NODE END############################ # SPEC 020: 11.2.3.2 Data Transfer (UL) #####################################SPEC NODE START############################ ## <span id="page-68-1"></span>11.2.3.2 Data Transfer (UL)

#### \*\*Table 11-13 RLC-MAC Data transfer (UL) message contents\*\*

| Element                |   | Presence   Description<br>                                               |  |
|------------------------|---|--------------------------------------------------------------------------|--|
|                        |   | -------------------- ---------- ---------------------------------------- |  |
| Frame Number           | M | Air interface time<br>                                                   |  |
| Slot Number            | M | Air interface time<br>                                                   |  |
| Cell Index             | M | Identification of the Cell<br>                                           |  |
| UE Index               | M | Identification of the UE<br>                                             |  |
| Number of RLC PDUs   M |   | Number of RLC PDUs receive from<br>MAC                                   |  |

![](\_page\_69\_Picture\_1.jpeg)

|                   |  | RLC PDU info (RB Type, RB id,   M   Radio Bearer type, Radio Bearer ID,   |
|-------------------|--|---------------------------------------------------------------------------|
|                   |  | ------------------------------- --- ------------------------------------- |
| PDU LEN, RLC PDU) |  | LCID and length for the RLC PDU,<br>                                      |
|                   |  | RLC PDU data<br>                                                          |
|                   |  | <br>                                                                      |

#####################################SPEC NODE END############################ # SPEC 021: 11.2.3.3 Schedule Result Reporting (DL) #####################################SPEC NODE START############################ # <span id="page-69-0"></span>11.2.3.3 Schedule Result Reporting (DL)

#### \*\*Table 11-14 RLC-MAC Schedule result reporting (DL) message contents\*\*

| Element | Presence | Description | |-----------------------------------------------------|----------|-------------- ----------------------------------| | Frame Number | M | Air interface time | | Slot Number | M | Air interface time | | Cell Index | M | Identification of the Cell | | UE Index | M | Identification of the UE | | Number of RB | M | Number of RBs to send | | RLC PDU info (RB id, overall length<br>for each RB) | M | RB id and length overall length for<br>each RB |

#####################################SPEC NODE END############################ # SPEC 022: 11.2.3.4 Buffer Status Report (DL) #####################################SPEC NODE START############################ # <span id="page-69-1"></span>11.2.3.4 Buffer Status Report (DL)

#### \*\*Table 11-15 RLC-MAC Buffer Status reporting (DL) message contents\*\*

| Element                           |   | Presence   Description<br>                                                     |
|-----------------------------------|---|--------------------------------------------------------------------------------|
|                                   |   | ------------------------------- ---------- ----------------------------------- |
| Cell Index                        | M | Identification of the Cell<br>                                                 |
| UE Index                          | M | Identification of the UE<br>                                                   |
| Number of RLC PDU                 | M | Number of RLC PDU in RLC buffer<br>                                            |
| RLC PDU info (RB id, PDU LEN)   M |   | LCID and length for each RLC PDU.                                              |

### <span id="page-69-2"></span>11.2.4 MAC – Scheduler Interface

5G NR MAC and scheduler modules interact via well-defined APIs. The APIs ensure any scheduler implementation interworks with MAC. This ensures the freedom of choice for OEMs and operators to plug in a scheduler implementation of choice from a third-party vendor in O-DU.

The functionalities of the scheduler module are restricted to optimal allocation of radio resources at every TTI while catering to the need of gNB for transmission of:

- UE specific UL/DL data and signalling messages and

- broadcast messages

To achieve the above objective, the APIs defined below abstract the scheduler of any protocol specific operations like handling payloads. The interfaces shown below and the APIs may evolve/change further in future releases of this document to achieve a more optimized scheduler implementation.

![](\_page\_70\_Picture\_1.jpeg)

![](\_page\_70\_Figure\_2.jpeg)

#### \*\*Figure 11-13 MAC-Scheduler interface\*\*

The MAC-Scheduler interface includes the slice related information (sNSSAI) associated with the logical channel, that helps the scheduler in multiplexing of MAC SDUs from one or different logical channel onto transport blocks (TB) to be delivered to the physical layer on transport channels. The slice id/sNSSAI associated with the logical channel and its slice priority (defined by the operator) derives a slice metric in the PF scheduler to do logical channel prioritization and radio resource selection so as to meet the slice SLA.

The following tables detail the interactions between MAC and scheduler both for configuration and data transfer operations.

| Direction | Message/API | Description | |------------|-------------------------------------|---------------------------- -------------------------------------------------------------------------------- ---------------------------------| | MAC to SCH | Cell configuration Re<br>quest | MAC provides SCH the cell configuration | | MAC to SCH | Cell Delete Request | MAC initiates deletion of a cell at SCH | | MAC to SCH | Add UE configuration<br>Request | MAC provides SCH the configuration/capabilities of a UE | | MAC to SCH | Modify UE configura<br>tion Request | MAC provides SCH the reconfiguration of UE, also used to add/re<br>lease/modify existing bearers | | MAC to SCH | Delete UE Request | MAC initiates deletion of a UE at SCH |

| MAC to SCH | DL HARQ Indication | Contains the list of UEs for which DL HARQ ACK / NACK received<br>from UE in a given TTI. | | | | Note: It is the responsibility of the SCH to associate the DL HARQ<br>ACK/NACKs received in a TTI to the corresponding HARQ process<br>Ids. | | Table 11-16 MAC to Scheduler APIs | | | | |-----------------------------------|--|--|--| |-----------------------------------|--|--|--| ![](\_page\_71\_Picture\_1.jpeg) | MAC to SCH | UL HARQ Indication | Contains the list of UEs for which UL Data on PUSCH was received.<br>Per UE, indication of CRC check success or failure is sent by MAC to<br>SCH based on CRC Indication received from L1. | |------------|------------------------------------------|----------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -----| | | | Note: It is the responsibility of the SCH to associate the UL HARQ In<br>dication received in a TTI to the corresponding HARQ process Ids. | | MAC to SCH | Uplink channel quality<br>information | MAC provides SCH channel condition (including RI, PMI, CQI) infor<br>mation for UEs for scheduling UL | | MAC to SCH | Downlink channel qual<br>ity information | MAC provides SCH channel condition (including RI, PMI, CQI) infor<br>mation for UEs for scheduling DL | | MAC to SCH | RACH Indication Con<br>tents | MAC receives the RACH Indication and shares the contents with SCH | | MAC to SCH | Paging Indication Con<br>tents | MAC indicates Paging message (F1AP Paging) contents to scheduler | | MAC to SCH | RACH Resource Re<br>quest | This API is used to get CRNTI, preamble information from MAC for<br>Contention Free Random Access | | MAC to SCH | RACH Resource Release | This API is used to release the Contention Free RACH Resources at<br>MAC | | MAC to SCH | RLC Buffer Status Info | DL data volume in the RLC entity | | MAC to SCH | Scheduling request indi<br>cation | MAC provides SCH scheduling request information for UL | | MAC to SCH | UL Buffer status report<br>indication | MAC provides SCH buffer status report for UL scheduling | | MAC to SCH | UL Power headroom in<br>dication | MAC provides SCH power headroom for UL scheduling |

#### \*\*Table 11-17 Scheduler to MAC APIs\*\*

| Direction | Message/API | Description | |------------|---------------------------------|-------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -----------------------------------------------------------------|

| SCH to MAC | UE configuration Re<br>sponse | SCH provides response to MAC for a UE configuration Request | | SCH to MAC | UE Reconfiguration<br>Response | SCH provides response to MAC for a UE Reconfiguration Request | | SCH to MAC | Cell configuration Re<br>sponse | SCH provides response to MAC for a Cell configuration Request | | SCH to MAC | Cell Deletion Re<br>sponse | SCH provides response to MAC for a Cell Deletion Request | | SCH to MAC | UE Deletion Response | SCH provides response to MAC for a UE Deletion Request |

| SCH to MAC | DL Scheduling Infor<br>mation | SCH provides scheduling information for a given TTI for scheduling DL<br>data. The scheduling information provides time and frequency domain re<br>sources to be scheduled with a list of Logical Channels (LC) and transport<br>block size opportunity per LC. |

| SCH to MAC | UL Scheduling Infor<br>mation | SCH provides scheduling information for a given TTI for scheduling UL<br>data. The scheduling information provides time and frequency domain re<br>sources to be scheduled based on the LC Group (LCG) buffer status or<br>Scheduling Request from UE. |

| SCH to MAC | RAR Information | SCH shares the RAR and uplink

scheduling and Msg3 scheduling infor<br>mation with MAC |

![](\_page\_72\_Picture\_1.jpeg)

| SCH to MAC | Downlink control<br>channel information | SCH provides to MAC information for DCI scheduling on PDCCH | |------------|-----------------------------------------|------------------------ -------------------------------------------------------| | SCH to MAC | Downlink Broadcast<br>Allocation | Scheduling information for broadcasting SIB1 and other system infor<br>mation | | SCH to MAC | Downlink Paging Al<br>location | Scheduling information for paging message on a paging channel |

#####################################SPEC NODE END############################ # SPEC 023: 11.2.4.1 Common Information Elements in MAC-Scheduler APIs / 11.2.4.1.1 Air Interface Time #####################################SPEC NODE START############################

# <span id="page-72-0"></span>11.2.4.1 Common Information Elements in MAC-Scheduler APIs

## <span id="page-72-1"></span>11.2.4.1.1 Air Interface Time

This is the timing information over the air interface in terms of system frame number and slot.

|                                                                                                                  | Presence                                                            |      |        |            |                | Description |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|------|--------|------------|----------------|-------------|
| <br> ---------- --------------------------------------------------------------------                             |                                                                     |      |        |            |                |             |
| --------------------------------------------------------------------------------                                 |                                                                     |      |        |            |                |             |
| --------------------------------------------------------------------------------<br>---------------------------- |                                                                     |      |        |            |                |             |
| <br>M<br>                                                                                                        |                                                                     |      | System | Frame      | number         | {0…1023}    |
| M                                                                                                                | Slot number {0…319} per 38.211 and FAPI specification<br>This value |      |        |            |                |             |
| wraps<br>around<br>in                                                                                            | accordance                                                          | with | the    | configured | nu<br>merology | in          |
| use<br>e.g.<br>for                                                                                               | = 3 the wrap around would be mod 80<br>** 80 is the number          |      |        |            |                |             |
| of slots per system frame for 120 kHz SCS  <br>                                                                  |                                                                     |      |        |            |                |             |
|                                                                                                                  |                                                                     |      |        |            |                |             |

#####################################SPEC NODE END############################ # SPEC 024: 11.2.4.1.2 (Debug) Timing Information #####################################SPEC NODE START############################

## # <span id="page-72-2"></span>11.2.4.1.2 (Debug) Timing Information

Additional timing information might be present in the APIs between MAC and scheduler to help troubleshoot issues. This is an optional information element in the APIs below. This timing information is defined below.

| Element | Presence | Description | |-------------------|----------|------------------------------------------------ ---------------------------------------| | SFN | M | System Frame number {0…1023} | | Slot | M | Slot number {0…319} per 38.211 and FAPI specification | | | | This value wraps around in accordance with the configured nu<br>merology in use | | | | e.g. | | | | for = 3 the wrap around would be mod 80 | | | | \*\* 80 is the number of slots per system frame for 120 kHz SCS | | System Time Stamp | M | Time Stamp of the system; equivalent to Linux timeval struc<br>ture (tv\_sec, tv\_usec) |

| | | Table 11-19 Debug timing information | |--|--|--------------------------------------| | | | |

#####################################SPEC NODE END############################ # SPEC 025: 11.2.4.2 MAC to Scheduler APIs #####################################SPEC NODE START############################ # <span id="page-73-0"></span>11.2.4.2 MAC to Scheduler APIs

### <span id="page-73-1"></span>11.2.4.2.1 Cell Configuration Request

When MAC layer receives configuration to create a new cell, this API is invoked.

| <br>Element                                                                      |  | Presence |  | Description |
|----------------------------------------------------------------------------------|--|----------|--|-------------|
|                                                                                  |  |          |  |             |
| ------------------------ ---------- -------------------------------------------  |  |          |  |             |
| -------------------------------------------------------------------------------- |  |          |  |             |

<sup>![](</sup>\_page\_73\_Picture\_1.jpeg)

-------------------------------------------------------------------------------- ---------------| | Debug Time Info | O | This is an optional IE and may be provided on availa<br>bility | | Cell Index | M | Identification of the Cell. 2-byte integer allocated by<br>DU | | numOfBeams | M | Number of beams | | | | Value: 0->64 | | numLayers | M | Number of layers | | | | Value: 0->8 | | numAntPorts | M | Number of Antennae ports | | | | Value: 0->64 | | Physical Cell Identity | M | PCI per TS 38.331 | | PLMN Information List | M | It defines which PLMNs that can be served by the NR<br>cell, and which S-NSSAIs can be supported by the NR<br>cell for corresponding PLMN in case of network slic<br>ing feature is supported. The pLMNId of the first entry<br>of the list is the PLMNId used to construct the nCGI<br>for the NR cell. | | >PLMNid | M | PLMN identifier served by the cell | | >S-NSSAIlist | CM | List of S-NSSAIs supported in the cell corresponding<br>to the PLMN. | | Duplex Mode | M | FDD or TDD mode of operation for the cell | | DL Cell Bandwidth | M | Total DL Cell Bandwidth | | UL Cell Bandwidth | M | Total UL Cell Bandwidth | | downlinkConfigCommon | M | See TS 38.331 DownlinkConfigCommonSIB | | >frequencyInfoDL | M | See TS 38.331 FrequencyInfoDL-SIB | | >initialDownlinkBWP | M | See TS 38.331 BWP-DownlinkCommon

--------------------------------------------------------------------------------

| | >BCCH-Config | M | See TS 38.331 BCCH-Config | | >PCCH-Config | M | See TS 38.331 PCCH-Config | ![](\_page\_74\_Picture\_1.jpeg) | uplinkConfigCommon | M | See TS 38.331 UplinkConfigCommonSIB | |-------------------------------|---|------------------------------------------- ----------------| | | | | | tdd-UL-DL-ConfigurationCommon | M | See TS 38.331 TDD-UL-DL-ConfigCommon | | >initialUplinkBWP | M | See TS 38.331 UplinkConfigCommonSIB | | SSB PositionsInBurst | M | See TS 38.331 ssb-PositionsInBurst | | SSB periodicityServingCell | M | See TS 38.331 ssb-periodicityServingCell | | DMRS TypeA Position | M | See TS 38.331 dmrs-TypeA-Position | | SSB Subcarrier Spacing | M | See TS 38.331 ssbSubcarrierSpacing | | PDCCH Config SIB1 | M | See TS 38.331 pdcch-ConfigSIB1 | | SS PBCH BlockPower | M | See TS 38.331 ss-PBCH-BlockPower | | SSB Frequency | M | Indicates cell defining SSB frequency domain position | | | | Frequency of the cell defining SSB transmission in<br>kHz | | | | | | ssbSubOffset | M | See TS 38.331 ssb-SubcarrierOffset | | Sib1PduLen | M | |

#####################################SPEC NODE END############################ # SPEC 026: 11.2.4.2.2 Cell Delete Request #####################################SPEC NODE START############################ ## <span id="page-74-0"></span>11.2.4.2.2 Cell Delete Request

When MAC layer receives configuration to create a new cell, this API is invoked. #### \*\*Table 11-21 Cell Delete Request\*\*

| Element | Presence | Description | |-----------------|----------|-------------------------------------------------- ----------| | Debug Time Info | O | This is an optional IE and may be provided on

availability | | Cell Index | M | Identification of the Cell. 2-byte integer allocated by DU |

### <span id="page-74-1"></span>11.2.4.2.3 Slice Configuration Request

Slice Configuration Request is sent to configure the MAC/Scheduler with the rRMPolicyRatio for each of the slices supported in the cell.

| Table 11-22 Slice Configuration Request         |  |
|-------------------------------------------------|--|
| -- ----------------------------------------- -- |  |
|                                                 |  |

| Element | Presence | Description | |------------------|----------|------------------------------------------------- --------------------------------------------------------------------------------

| S-NSSAI List | | This defines the list of S-NSSAIs<br>supported in the PLMN belonging to<br>the cell. This is to be included if net<br>work slicing is supported. |

| > S-NSSAI | M | Identification of the slice. |

| > RRMPolicyRatio | M | rRMPolicy for the slice if network<br>slicing feature is supported. This pol<br>icy is for the resource type "PRB"<br>and applicable to gNB-DU. The |

![](\_page\_75\_Picture\_1.jpeg)

--------------------|

|                                                                                 |     |            | other resource type " DRB" |
|---------------------------------------------------------------------------------|-----|------------|----------------------------|
| and<br>"RRCConnected"                                                           | are | applicable | to<br>gNB-CU.              |
|                                                                                 |     |            |                            |
| ----------------------------- --------- --------------------------------------- |     |            |                            |

![](_page_86_Figure_0.jpeg)

| >> rRMPolicyMaxRatio | uint8\_t | This attribute specifies the maximum<br>percentage of radio resource that can<br>be used by the associated rRMPoli<br>cyMemberList/SNSSAI. The maxi<br>mum percentage of radio resource<br>include at least one of the shared re<br>sources, prioritized resources and<br>dedicated resources. The sum of the<br>rRMPolicyMaxRatio values assigned<br>to all slices can be greater than 100. |

| >> rRMPolicyMinRatio | uint8\_t | This attribute specifies the minimum<br>percentage of radio resources that<br>can be used by the associated rRM<br>PolicyMemberList/sNSSAI. The<br>minimum percentage of radio re<br>sources including at least one of pri<br>oritized resources and dedicated re<br>sources. The sum of the rRMPoli<br>cyMinRatio values assigned to all<br>slices be less than or equal to100. |

| >>s rRMPolicyDedicatedRatio | uint8\_t | This attribute specifies the percent<br>age of radio resource that dedicat<br>edly used by the associated rRMPoli<br>cyMemberList/sNSSAI. The sum of<br>the rRMPolicyDeidctaedRatio values<br>assigned to all slices be less than or<br>equal to100. |

#####################################SPEC NODE END############################ # SPEC 027: 11.2.4.2.4 Slice Reconfiguration Request #####################################SPEC NODE START############################

## <span id="page-75-0"></span>11.2.4.2.4 Slice Reconfiguration Request

Slice Reconfiguration Request is sent to re-configure the MAC/Scheduler with the rRMPolicyRatio for the slices for which the rRMPolicy is updated/modified over O1 interface.

| <br>Element                                                                      |   |    | Presence | <br>Description                                |
|----------------------------------------------------------------------------------|---|----|----------|------------------------------------------------|
|                                                                                  |   |    |          |                                                |
| ------------------ ---------- -------------------------------------------------  |   |    |          |                                                |
| -------------------------------------------------------------------------------- |   |    |          |                                                |
| -------------------------------------------------------------------------------- |   |    |          |                                                |
| ---------------------                                                            |   |    |          |                                                |
| S-NSSAI List<br>                                                                 |   |    |          | This defines the list of S-NSSAIs<br>supported |
| in the PLMN belonging to<br>the cell. This is to be included if net<br>work      |   |    |          |                                                |
| slicing                                                                          |   | is |          | supported.                                     |
|                                                                                  |   |    |          |                                                |
| > S-NSSAI                                                                        | M |    |          | Identification of the slice.                   |

|

| > RRMPolicyRatio | M | rRMPolicy for the slice if network<br>slicing feature is supported. This pol<br>icy is for the resource type "PRB"<br>and applicable to gNB-DU. The<br>other resource type " DRB" and<br>"RRCConnected" are applicable to<br>gNB-CU. |

| | Table 11-23 Slice Reconfiguration Request | | |--|-------------------------------------------|--| | | | |

## ![](\_page\_76\_Picture\_1.jpeg)

| >> rRMPolicyMaxRatio | uint8\_t | This attribute specifies the maximum<br>percentage of radio resource that can<br>be used by the associated rRMPoli<br>cyMemberList/SNSSAI. The maxi<br>mum percentage of radio resource<br>include at least one of the shared re<br>sources, prioritized resources and<br>dedicated resources. The sum of the<br>rRMPolicyMaxRatio values assigned<br>to all slices can be greater than 100. |

|-----------------------------|---------|--------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -----------------------|

| >> rRMPolicyMinRatio | uint8\_t | This attribute specifies the minimum<br>percentage of radio resources that<br>can be used by the associated rRM<br>PolicyMemberList/sNSSAI. The<br>minimum percentage of radio re<br>sources including at least one of pri<br>oritized resources and dedicated re<br>sources. The sum of the rRMPoli<br>cyMinRatio values assigned to all<br>slices be less than or equal to100. |

| >>s rRMPolicyDedicatedRatio | uint8\_t | This attribute specifies the percent<br>age of radio resource that dedicat<br>edly used by the associated rRMPoli<br>cyMemberList/sNSSAI. The sum of<br>the rRMPolicyDeidctaedRatio values<br>assigned to all slices be less than or<br>equal to100. |

#####################################SPEC NODE END############################ # SPEC 028: 11.2.4.2.5 Add UE Configuration Request #####################################SPEC NODE START############################ # <span id="page-76-0"></span>11.2.4.2.5 Add UE Configuration Request

This API is invoked by MAC layer to create a new UE in the scheduler, including the details of logical channels associated with the UE.

| Element | Pres<br>ence | Description

| |--------------------|--------------|------------------------------------------- -------------------------------------------------------------------------------- ---------------------------------------| | Debug Time<br>Info | O | This is an optional IE and may be provided on availability | | Cell Index | M | Identification of the Cell. 2-byte integer allocated by DU | | beamIndex | M | Index of the beam.<br>For example, please see subclause 6.6.2 of TS 38.331 [54] where the ssb-Index in the<br>rsIndexResults element of MeasResultNR is defined. | | CRNTI | M | See TS 38.331 RNTI-Value. Allocated by MAC.<br>CRNTI shall be included only in case of SA | ![](\_page\_77\_Picture\_1.jpeg) | mac-CellGroup<br>Config (sched<br>ulingRe<br>questConfig,<br>tag-Config, phr<br>Config,DRX<br>Config) | M | See TS 38.331 MAC-CellGroupConfig | |------------------------------------------------------------------------------- ------------------------|---|--------------------------------------------------- -------------------------------------------------------------------------------- ----------------------------------| | physical<br>CellGroupCon<br>fig (pdsch<br>HARQ-ACK<br>Codebook, p<br>NR-FR1) | M | See TS 38.331 PhysicalCellGroupConfig | | spCellConfig | M | See TS 38.331 SpCellConfig | | >servCel<br>lIndex | M | See TS 38.331 ServCellIndex | | >Serv<br>ingCell<br>ConfigInfo | M | See TS 38.331 ServingCellConfig | | >>ini<br>tialDown<br>linkBWP<br>(pdcch<br>Config,<br>pdsch<br>Config) | M | See TS 38.331 BWP-DownlinkDedicated in ServingCellConfig. | | >>><br>radi<br>oLink<br>Monitor<br>ingCon<br>fig | M | RadioLinkMonitoringConfig is used to configure radio link monitoring for

detection of<br>beam- and/or cell radio link failure. See also TS 38.321 [3],

clause 5.1.1 | | >>Num<br>ber of<br>DL BWP<br>To Add | M | The number of dedicated DL BWP To Add | | >>down<br>link<br>BWP<br>ToAdd<br>ModList<br>(bwp-Id,<br>bwp<br>Com<br>mon,<br>bwp<br>Dedi<br>cated) | M | See TS 38.331 BWP-Downlink in ServingCellConfig | | >>firstA<br>ctive<br>Down<br>link<br>BWP-Id | M | See TS 38.331 ServingCellConfig |

## ![](\_page\_78\_Picture\_1.jpeg)

|

| >>de<br>fault<br>Down | M | See TS 38.331 ServingCellConfig | |-----------------------|---|--------------------------------------------------- ----------------------------------------| | link<br>BWP-Id | | | | >>bwp | M | See TS 38.331 ServingCellConfig | | Inactivi | | | | tyTimer | | | | >>>pdsc | M | See TS 38.331 PDSCH-ServingCellConfig in ServingCellConfig | | h-Serv | | | | ingCell | | | | Config | | | | (max | | | | MIMO | | | | Layers, | | | | nrof | | | | HARQ | | | Process<br>esForPD | | | | SCH, | | | | codeBloc | | | | kGroup | | | | Trans | | | | mission, | | | | xOver | | | | head) | | | | >>ini | M | See TS 38.331 BWP-UplinkDedicated in ServingCellConfig | | tialUplin | | | | kBWP | | | | (pucch | | | | Config, | | | | pusch<br>Config) | | | | >>>bea | M | The IE BeamFailureRecoveryConfig is used to configure the UE with RACH resources | | mFailure | | and candidate beams for beam failure recovery in case of beam failure detection. See also | | Recov | | TS 38.321 [3], clause 5.1.1 | | eryCon | | | | fig | | | | >>Num | M | The number of UL BWP To Add | | ber of | | | | UL BWP | | |

| To Add | | | | >>up<br>link | M | See TS 38.331 BWP-Uplink in ServingCellConfig | | BWP | | | | ToAdd | | | | ModList | | | | (bwp-Id, | | | | bwp | | | | Com | | | | mon, | | | | bwp | | | | Dedi | | | | cated) | | | | >>firstA | M | See TS 38.331 ServingCellConfig | | ctiveUpli<br>nkBWP | | | | Id | | | ![](\_page\_79\_Picture\_1.jpeg) | UE Aggre<br>gate Maxim-um<br>Bit Rate Uplink | | MSee TS 38.473 gNB-DU UE Aggregate Maximum Bit Rate Uplink | |------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -----------------------------------------------|--------|----------------------- ------------------------------------------------------------------| | dlModInfo {mo<br>dOrder, mcsIn<br>dex , mcsTa<br>ble} | M | |

| ulModInfo<br>{modOrder,<br>mcsIndex,<br>mcsTable}

M LC<br>To Number of Add The M  $number$ of Logical Channel To Add >logical<br>ChannelI<br>dentity TS 38.331 logicalChannelIdentity M See Qos (5Qi, <br>GBR Qos<br>Info. NG<br/>NG Allo<br>cation and<br>Retention<br>Priority,<br>GBR QoS<br>Flow Infor<br>mation,<br>PDU Ses<br>sion ID, UL<br>PDU Ses<br>sion Aggre<br>gate Maxi<br>mum Bit<br>Rate) | M See TS 38.473 DRB QoS UE CONTEXT MODIFICATION REQUEST in  $>S-NSSAI < br > DL$ Logi M<br>M | See TS 38.473 Section 9.2.2.1 DRB Information<br>See TS 38.321 Logical channel priority calChannel<br>Config (Lc<br>priority) >UL Logi<br>calChannel<br>Config (pri<br>ority, logi<br>calChan<br>nelGroup,<br>schedul<br>ingReques<br>tID, priori<br>tisedBitRate,<br>bucketSize<br>Duration) M See 38.331 LogicalChannelConfig

![]( page 80 Picture 1. jpeg)

############################SPEC NODE END################################## # SPEC 029: 11.2.4.2.6 Modify UE Reconfiguration Request ################################SPEC NODE START################################## ## <span id="page-80-0"></span>11.2.4.2.6 Modify UE Reconfiguration Request

MAC layer invokes this API to modify an existing UE context also to add/release/modify existing logical channels.

|          |                                                            | Element     |
|----------|------------------------------------------------------------|-------------|
| Presence |                                                            | Description |
|          |                                                            |             |
|          |                                                            |             |
|          |                                                            |             |
|          |                                                            |             |
|          |                                                            |             |
| Debug    | Time                                                       | Info        |
|          | This is an optional IE and may be provided on availability |             |

| | Cell Index | M | Identification of the Cell | | beamIndex | M | Index of the beam. | | | | For example, please see subclause 6.6.2 of TS 38.331 [54] where the ssb-In<br>dex in the rsIndexResults element of MeasResultNR is defined. | | CRNTI | M | See TS 38.331 RNTI-Value | | mac-CellGroup-Recon<br>fig (schedulingRequest<br>Reconfig, tag-Recon<br>fig) | M | See TS 38.331 MAC-CellGroupConfig | | physicalCellGroup-Re<br>config (pdsch-HARQ<br>ACK-Codebook, p-NR<br>FR1) | M | See TS 38.331 PhysicalCellGroupConfig | | spCell-Reconfig | M | See TS 38.331 SpCellConfig | | >servCellIndex | M | See TS 38.331 ServCellIndex | | >ServingCell-Re<br>configInfo | M | See TS 38.331 ServingCellConfig | | >>initialDown<br>linkBWP-Re<br>config (pdcch<br>Config, pdsch<br>Config) | M | See TS 38.331 BWP-DownlinkDedicated in ServingCellConfig | | >>> radi<br>oLinkMonitor<br>ingConfig | M | RadioLinkMonitoringConfig is used to configure radio link monitoring for<br>detection of beam- and/or cell radio link failure. See also TS 38.321 [3],<br>clause 5.1.1 | | >>Number of<br>DL BWP To<br>Add or Modify | M | The number of dedicated DL BWP To Add or Modify | | >>downlink<br>BWP<br>ToAddModList<br>(bwp-Id, bwp<br>Common, bwp<br>Dedicated) | M | See TS 38.331 BWP-Downlink in ServingCellConfig | | >>Number of<br>DL BWP To Re<br>lease | M | The number of dedicated DL BWP to remove | | >>downlink<br>BWP<br>ToReleaseList<br>(bwp-Id) | M | See TS 38.331 downlinkBWP-ToReleaseList in ServingCellConfig |

## ![](\_page\_81\_Picture\_1.jpeg)

|

| >>firstActive<br>DownlinkBWP<br>Id | M | See TS 38.331 ServingCellConfig | |------------------------------------|---|--------------------------------------

--------------------------------------------------------------------------------

------------------------| | >>defaultDown<br>linkBWP-Id | M | See TS 38.331 ServingCellConfig | | >>bwp-Inactivi<br>tyTimer | M | See TS 38.331 ServingCellConfig | | >>pdsch-Serv<br>ingCell-Recon | M | See TS 38.331 PDSCH-ServingCellConfig | | fig (maxMIMO<br>Layers, nrof | | | | HARQ | | | | Process<br>esForPDSCH, | | | | codeBlock<br>GroupTransmis | | | | sion, xOver | | | | head)<br>>>initialUplink | M | See TS 38.331 BWP-UplinkDedicated in ServingCellConfig | | BWP-Reconfig<br>(pucch-Config, | | | | pusch-Config) | |

| >>>beam<br>FailureRecov | M | The IE BeamFailureRecoveryConfig is used to configure the UE with<br>RACH resources and candidate beams for beam failure recovery in case of | | eryConfig | | beam failure detection. See also TS 38.321 [3], clause 5.1.1 | | >>Number of | M | The number of dedicated UL BWP To Add or Modify |

```
| UL BWP To<br>Add or Modify | | 
|
| >>uplinkBWP | M | See TS 38.331 BWP-Uplink in 
ServingCellConfig 
|
| ToAddModList | | 
|
| (bwp-Id, bwp<br>Common, bwp | | 
|
| Dedicated) | | 
|
| >>Number of | M | The number of dedicated UL BWP to 
remove 
|
| UL BWP To Re<br>lease | | 
|
| >>uplinkBWP | M | See TS 38.331 uplinkBWP-ToReleaseList 
in ServingCellConfig 
|
| ToReleaseList<br>(bwp-Id) | | 
|
| >>firstAc | M | See TS 38.331 ServingCellConfig 
|
| tiveUplinkBWP | | 
|
| Id<br>UE Aggregate | M | See TS 38.473 gNB-DU UE Aggregate 
Maximum Bit Rate Uplink 
|
| Maximum Bit | | 
|
| Rate Uplink | | 
|
| dlModInfo {mo<br>dOrder, mcsIn | M | 
|
| dex , mcsTable} | | 
|
| ulModInfo | M | 
|
| {modOrder, | | 
|
| mcsIndex,<br>mcsTable} | | 
|
| Number of LC To Add | M | The number of Logical Channel to Add
```

|

```
| logicalChannelI | M | See TS 38.331 logicalChannelIdentity 
|
| dentity | | 
|
```

```
![](_page_82_Picture_1.jpeg)
```

| Qos (5Qi, GBR Qos | M | See TS 38.473 DRB QoS in UE CONTEXT MODIFICATION REQUEST |

| ---------------------- --- ---------------------------------------------------- |                                                      |        |                      |
|---------------------------------------------------------------------------------|------------------------------------------------------|--------|----------------------|
| -------------------- <br> <br>Info,<br>NG-RAN<br>Al<br>                         |                                                      |        |                      |
| <br>                                                                            |                                                      |        | <br>                 |
| <br>location<br>and<br>                                                         | Reten                                                |        |                      |
| <br>tion<br>Priority,                                                           | GBR                                                  |        |                      |
| <br> <br>QoS<br>Flow<br>Infor                                                   |                                                      |        |                      |
| <br> <br>mation,<br>PDU<br>Ses                                                  |                                                      |        |                      |
| <br>                                                                            |                                                      |        | <br>                 |
| <br> <br>sion<br>ID,<br>UL<br>PDU                                               |                                                      |        |                      |
| <br> <br>Session<br>Aggregate                                                   |                                                      |        |                      |
| <br> <br>Maximum<br>Bit<br>Rate)                                                |                                                      |        |                      |
|                                                                                 |                                                      |        |                      |
| <br>                                                                            |                                                      |        | <br>                 |
| S-NSSAI<br>REQUEST<br>                                                          | M   See TS 38.473 S-NSSAI in UE CONTEXT MODIFICATION |        |                      |
| DL LogicalChan<br>                                                              | M   See TS 38.321 Logical channel priority           |        |                      |
| <br>                                                                            |                                                      |        | <br>                 |
| <br>nelConfig<br>(Lc                                                            | prior                                                |        |                      |
| <br> <br>ity)                                                                   |                                                      |        | <br>                 |
| <br> <br>UL<br>LogicalChan                                                      | <br>M<br> <br>See                                    | 38.331 | LogicalChannelConfig |

| <br> <br>nelConfig           | (priority,                                    |              |                        |  |
|------------------------------|-----------------------------------------------|--------------|------------------------|--|
| <br>                         |                                               |              |                        |  |
| <br> <br>logicalChan         |                                               |              |                        |  |
| <br> <br>nelGroup,           | schedul                                       |              |                        |  |
| <br> <br>ingRequestID,       | pri                                           |              |                        |  |
| <br>                         |                                               |              |                        |  |
| <br> <br>oritisedBitRate,    |                                               |              |                        |  |
| <br> <br>bucketSize          |                                               |              |                        |  |
| <br> <br>Duration)           |                                               |              |                        |  |
| <br>                         |                                               |              |                        |  |
| <br>  Number of LC To De     | M   The number of Logical Channel to Delete   |              |                        |  |
| <br> <br>lete                |                                               |              |                        |  |
| <br>                         |                                               |              |                        |  |
| <br> <br>>logicalChannelI    | <br>M<br> <br>See                             | TS<br>38.331 | logicalChannelIdentity |  |
| <br> <br>dentity             |                                               |              |                        |  |
| <br>                         |                                               |              |                        |  |
| <br>  >Number of LC To       | M   The number of Logical Channel To Modified |              |                        |  |
| <br> <br>Modified            |                                               |              |                        |  |
| <br>                         |                                               |              |                        |  |
| <br>                         |                                               |              |                        |  |
| <br>                         |                                               |              |                        |  |
| <br> <br>>Logical<br>Channel | <br>M<br> <br>See                             | TS<br>38.331 | logicalChannelIdentity |  |

| <br>Identity<br>          |             |              |     |  |   |  |     |        |  |  |  |                                                      |
|---------------------------|-------------|--------------|-----|--|---|--|-----|--------|--|--|--|------------------------------------------------------|
| >Qos(5Qi , GBR<br>REQUEST |             |              |     |  |   |  |     |        |  |  |  | M   See TS 38.473 DRB QoS in UE CONTEXT MODIFICATION |
| <br>                      |             |              |     |  |   |  |     |        |  |  |  |                                                      |
| <br>Qos<br>               | Info,       | NG           |     |  |   |  |     |        |  |  |  |                                                      |
| <br>RAN                   | Allocation  |              |     |  |   |  |     |        |  |  |  |                                                      |
| <br> <br>and              |             | Retention    | Pri |  |   |  |     |        |  |  |  |                                                      |
| <br>                      |             |              |     |  |   |  |     |        |  |  |  |                                                      |
| <br> <br>ority,           | GBR         | QoS          |     |  |   |  |     |        |  |  |  |                                                      |
| <br> <br>Flow             |             | Information, |     |  |   |  |     |        |  |  |  |                                                      |
| <br> <br>PDU              | Session     | ID,          |     |  |   |  |     |        |  |  |  |                                                      |
| <br> <br>UL               | PDU         | Session      |     |  |   |  |     |        |  |  |  |                                                      |
| <br>                      |             |              |     |  |   |  |     |        |  |  |  |                                                      |
| <br> <br>Aggregate        |             | Maxi         |     |  |   |  |     |        |  |  |  |                                                      |
| <br> <br>mum              | Bit         | Rate)        |     |  |   |  |     |        |  |  |  |                                                      |
| <br>  >S-NSSAI            |             |              |     |  |   |  |     |        |  |  |  | M   See TS 38.473 S-NSSAI in UE CONTEXT MODIFICATION |
| REQUEST<br>               |             |              |     |  |   |  |     |        |  |  |  |                                                      |
| <br>  >DL LogicalChan     |             |              |     |  |   |  |     |        |  |  |  | M   See TS 38.321 Logical channel priority           |
| <br>                      |             |              |     |  |   |  |     |        |  |  |  |                                                      |
| <br> <br>nelConfig        |             | (Lc          | pri |  |   |  |     |        |  |  |  |                                                      |
| <br> <br>ority)           |             |              |     |  |   |  |     |        |  |  |  |                                                      |
|                           |             |              |     |  |   |  |     |        |  |  |  |                                                      |
| <br>>UL<br>               | LogicalChan |              |     |  | M |  | See | 38.331 |  |  |  | LogicalChannelConfig                                 |
|                           |             |              |     |  |   |  |     |        |  |  |  |                                                      |

| | nelConfig (priority, | | | | logicalChan | | | | nelGroup, schedul | | | | ingRequestID, pri | | | | | | | | oritisedBitRate, | | | | bucketSize | | | | Duration) | | | | | | | | drxConfigIndict | M | As per Spec 38.473, CU sends this parameter in 'UE Context Mod req' to | | orRelease | | indicate whether to release UE or not | | | | | | | | Value: ENUM(release,)

![](\_page\_83\_Picture\_1.jpeg)

|

### <span id="page-83-0"></span>11.2.4.2.7 Delete UE Request

MAC indicates to Scheduler to Delete an existing UE using this API.

| Table 11-26 Delete UE Request | | |-------------------------------|--| |-------------------------------|--| | Element | Presence | Description | |-----------------|----------|-------------------------------------------------- ----------|

| Debug Time Info | O | This is an optional IE and may be provided on availability |

```
| Cell Index | M | Identification of the Cell. 2-byte integer 
allocated by DU |
| CRNTI | M | See TS 38.331 RNTI-Value 
|
```

### <span id="page-83-1"></span>11.2.4.2.8 DL HARQ Indication

MAC informs Scheduler on reception and Decoding of received DL HARQ feedback from the UE. Feedback itself might have been received either on PUSCH or PUCCH, decoding of feedback is done at MAC/L1.

| Element<br>                                                                                                       |   | Presence   Description       |
|-------------------------------------------------------------------------------------------------------------------|---|------------------------------|
| ------------------------------------- ---------- ------------------------------<br>------------------------------ |   |                              |
| Cell Index                                                                                                        | M | Identification of the Cell.  |
| 2-byte integer allocated by DU                                                                                    |   |                              |
| CRNTI<br>                                                                                                         | M | See TS 38.331 RNTI-Value     |
| Timing Information                                                                                                | M | Timing information for this  |
| message.<br>                                                                                                      |   |                              |
| Number of HARQ feedback<br>Reported   M                                                                           |   | Number of HARQ feedback bits |
| reported<br>                                                                                                      |   |                              |
| >harq payload bits                                                                                                | M | Bitmap of length =           |
| MAX_HARQ_BITS per 38.213                                                                                          |   |                              |
| #### **Table 11-27 DL HARQ Indication**<br>### <span id="page-83-2"></span> 11.2.4.2.9 UL HARQ (CRC) Indication   |   |                              |
| This API is invoked by MAC to inform Scheduler the CRC decode results of PUSCH.                                   |   |                              |
| **Table 11-28 UL HARQ (CRC) Indication**                                                                          |   |                              |
| Element                                                                                                           |   | Presence   Description       |
|                                                                                                                   |   |                              |
| -------------------------------------- ---------- -----------------------------                                   |   |                              |
| -------------------------------------------                                                                       |   |                              |
| Cell Index                                                                                                        | M | Identification of the Cell.  |
| 2-byte integer allocated by DU                                                                                    |   |                              |
| CRNTI<br>                                                                                                         | M | See TS 38.331 RNTI-Value     |
| Timing Information                                                                                                | M | Timing information for this  |
| message.                                                                                                          |   |                              |

| Number of CRC Indication<br>Reported | M | Number of CRC Indication reported | | >CRC Indication | M | {0MAX\_NUMBER\_OF\_CRC\_IND\_BITS} for UL SISO<br>there would be just 1 bit | | | | 0: PASS |

![](\_page\_84\_Picture\_1.jpeg)

|  |  | 1: FAILURE |  |  |  |  |  |                                                                         |  |
|--|--|------------|--|--|--|--|--|-------------------------------------------------------------------------|--|
|  |  |            |  |  |  |  |  | -- -------------------------------------------------------------------- |  |
|  |  |            |  |  |  |  |  | For the case of UL MIMO 1 bit per TB would convey the feed<br>back      |  |

#####################################SPEC NODE END############################ # SPEC 030: 11.2.4.2.10 UL Channel Quality Information #####################################SPEC NODE START############################ ## <span id="page-84-0"></span>11.2.4.2.10 UL Channel Quality Information

MAC informs Scheduler using this API the UL Channel Quality Indication of PUSCH/PUCCH

| Element                                                                                                                |  |   |   | Presence   Description   |
|------------------------------------------------------------------------------------------------------------------------|--|---|---|--------------------------|
|                                                                                                                        |  |   |   |                          |
| ------------------------------------------ ---------- -------------------------<br>----------------------------------- |  |   |   |                          |
| Cell Index                                                                                                             |  | M |   | Identification of the    |
| Cell. 2-byte integer allocated by DU                                                                                   |  |   |   |                          |
| CRNTI                                                                                                                  |  | M |   | See TS 38.331 RNTI-Value |
|                                                                                                                        |  |   |   |                          |
| Timing Information                                                                                                     |  | M |   | Timing information for   |
| this message.                                                                                                          |  |   |   |                          |
| Number of UL CQI Indica<br>tion Reported   M                                                                           |  |   |   | Number of UL CQI         |
| Indication reported                                                                                                    |  |   |   |                          |
| >Type of Report                                                                                                        |  |   | M | {PUCCH, PUSCH}           |
|                                                                                                                        |  |   |   |                          |
| >UL_CQI                                                                                                                |  | M |   | 0-255 in steps of 0.5 dB |
| {-64 dB, … 63 dB}                                                                                                      |  |   |   |                          |
| >Timing Advance                                                                                                        |  | M |   | TA measured for 38.213   |
| section 4.2                                                                                                            |  |   |   |                          |

#### \*\*Table 11-29 UL Channel Quality Information\*\*

#####################################SPEC NODE END############################ # SPEC 031: 11.2.4.2.11 DL Channel Quality Information

#####################################SPEC NODE START############################ # <span id="page-84-1"></span>11.2.4.2.11 DL Channel Quality Information

This API is invoked by MAC to report to Scheduler the DL Channel Quality delivered on PUSCH/PUCCH

| Element                                                                              |   |   | Presence   Description   |
|--------------------------------------------------------------------------------------|---|---|--------------------------|
| <br> ------------------------------------------ ---------- ------------------------- |   |   |                          |
| -----------------------------------                                                  |   |   |                          |
| Cell Index                                                                           | M |   | Identification of the    |
| Cell. 2-byte integer allocated by DU                                                 |   |   |                          |
| CRNTI                                                                                | M |   | See TS 38.331 RNTI-Value |
|                                                                                      |   |   |                          |
| Timing Information                                                                   | M |   | Timing information for   |
| this message.                                                                        |   |   |                          |
| Number of DL CQI Indica<br>tion Reported   M                                         |   |   | Number of UL CQI         |
| Indication reported                                                                  |   |   |                          |
| >Type of Report                                                                      | M |   | Bitmap for CQI, PMI, RI, |
| CRI report<br>                                                                       |   |   |                          |
| > CQI                                                                                |   | O | CQI report on            |
| PUCCH/PUSCH                                                                          |   |   |                          |
| >PMI                                                                                 |   | O | PMI report on            |
| PUCCH/PUSCH                                                                          |   |   |                          |
| >CRI                                                                                 |   | O | CQI report on            |
| PUCCH/PUSCH                                                                          |   |   |                          |
| >RI                                                                                  | O |   | RI report on PUCCH/PUSCH |
|                                                                                      |   |   |                          |

#### \*\*Table 11-30 DL Channel Quality Information\*\*

![](\_page\_85\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 032: 11.2.4.2.12 RACH Indication Contents #####################################SPEC NODE START############################ ## <span id="page-85-0"></span>11.2.4.2.12 RACH Indication Contents

MAC receives the RACH Indication and shares the contents with the scheduler.

| <br>Element                                                                     |  | Presence |  | Description |
|---------------------------------------------------------------------------------|--|----------|--|-------------|
|                                                                                 |  |          |  |             |
| -------------------- ---------- ----------------------------------------------- |  |          |  |             |
| -------------                                                                   |  |          |  |             |

| Cell Index | M | Identification of the Cell. 2-byte integer allocated by DU | | CRNTI | M | See TS 38.331 RNTI-Value | | Timing Information | M | Timing information for this message. | | Slot Index | M | Index of the First Slot where RACH was detected | | Symbol Index | M | Index of the first OFDM Symbol where RACH was detected | | Frequency Index | M | Index of the Frequency where RACH was detected. 38.211 | | Preamble ID | M | Preamble ID that was detected | | Timing Advance | M | Timing Advance that was detected and reported to MAC |

#### \*\*Table 11-31 RACH Indication Contents\*\*

#####################################SPEC NODE END############################ # SPEC 033: 11.2.4.2.13 Paging Indication Contents #####################################SPEC NODE START############################ # <span id="page-85-1"></span>11.2.4.2.13 Paging Indication Contents

MAC indicates Paging message (F1AP Paging) contents to scheduler.

\*\*Table 11-32 Paging Indication Contents\*\*

![](_page_103_Figure_5.jpeg)

| to<br>Scheduler. |   |                                     |
|------------------|---|-------------------------------------|
| Paging message   | M | Bit string. Paging messages need to |
| transfer         |   |                                     |
|                  |   |                                     |

### <span id="page-85-2"></span>11.2.4.2.14 RACH Resource Request

When contention free random access is initiated by a UE, MAC shares the CRNTI and SSB resource allocation information with the scheduler through this API.

| Table 11-33 RACH Resource Request | | | | |-----------------------------------|--|--|--| |-----------------------------------|--|--|--|

| Element          | Presence   Description<br>                  |
|------------------|---------------------------------------------|
|                  | -------------- ---------- ----------------- |
| Frame Number   M | Time indication                             |
| Slot Number   M  | Time indication                             |

![](\_page\_86\_Picture\_1.jpeg)

| <br>Cell     | Index                                                                           |  | M |       |  | Identification |    | of     | the                                          | Cell |
|--------------|---------------------------------------------------------------------------------|--|---|-------|--|----------------|----|--------|----------------------------------------------|------|
|              |                                                                                 |  |   |       |  |                |    |        |                                              |      |
|              | --------------- --- ----------------------------------------------------------- |  |   |       |  |                |    |        |                                              |      |
| ------------ |                                                                                 |  |   |       |  |                |    |        |                                              |      |
| CRNTI        |                                                                                 |  |   |       |  |                |    |        | M   The CRNTI allocated by MAC for the<br>UE |      |
|              |                                                                                 |  |   |       |  |                |    |        |                                              |      |
|              | Number of SSB   M   The number of ssb for which CFRA<br>resource allocation is  |  |   |       |  |                |    |        |                                              |      |
| requested.   |                                                                                 |  |   |       |  |                |    |        |                                              |      |
| <br>>ssb     |                                                                                 |  |   | <br>M |  | See            | TS | 38.331 | SSB-Index                                    |      |
|              |                                                                                 |  |   |       |  |                |    |        |                                              |      |

### <span id="page-86-0"></span>11.2.4.2.15 RACH Resource Release

MAC indicates to scheduler through this API when RACH resources associated with a UE have to be released.

|  | Element                                                                         |       |  | Presence |      | Description |
|--|---------------------------------------------------------------------------------|-------|--|----------|------|-------------|
|  |                                                                                 |       |  |          |      |             |
|  | -------------------- ---------- ----------------------------------------------- |       |  |          |      |             |
|  | ---------------------------------------                                         |       |  |          |      |             |
|  | Frame<br>Number                                                                 | <br>M |  |          | Time | indication  |
|  |                                                                                 |       |  |          |      |             |
|  | Slot<br>Number                                                                  | <br>M |  |          | Time | indication  |

| | Cell Index | M | Identification of the Cell | | CRNTI | M | The CRNTI allocated by MAC for the<br>UE | | CFRA-SSB-Resource | M | See TS 38.331 CFRA-SSB-Resource | | >Ssb index | M | See TS 38.331 SSB-Index | | >ra preamble index | M | The RA preamble index to be used in<br>the RA occasions associated with this<br>SSB. |

| | Table 11-34 RACH Resource Release | | |--|-----------------------------------|--| | | | |

#####################################SPEC NODE END############################ # SPEC 034: 11.2.4.2.16 DL RLC Buffer Status Information #####################################SPEC NODE START############################ ## <span id="page-86-1"></span>11.2.4.2.16 DL RLC Buffer Status Information

This API is used by RLC for reporting data volume per UE for multiple LCs. This can be used in two different ways depending on the QoS/latency requirements.

- 1. Data Volume reports are aggregated per UE (at an aggregation point such as slot indication)

- a. This adds latency however it reduces message exchange traffic between SCHED and MAC 2. Data Volume is reported per LC as soon as it is received at MAC

 - a. This adds to the message exchange traffic however it would be perfect for Low Latency Usecases

Implementor of this API can choose either one of the above approaches.

| Element                                                                         |   | Presence   Description      |
|---------------------------------------------------------------------------------|---|-----------------------------|
|                                                                                 |   |                             |
| ------------------------------------- ---------- ------------------------------ |   |                             |
| -----------------------------------------------                                 |   |                             |
| Debug Time Info                                                                 | O | This is an optional IE and  |
| may be provided on availability                                                 |   |                             |
| Cell Index                                                                      | M | Identification of the Cell. |
| 2-byte integer allocated by DU                                                  |   |                             |
| CRNTI                                                                           | M | See TS 38.331 RNTI-Value    |
|                                                                                 |   |                             |
| Number of DL LCs to be Re<br>ported   M                                         |   | Number of LC for which DL   |

Buffer Occupancy/Data Volume<br>is being reported |

| | | | | | | Table 11-35 DL RLC Buffer Status Information | |--|--|--|--|--|--|----------------------------------------------| |--|--|--|--|--|--|----------------------------------------------|

![](\_page\_87\_Picture\_1.jpeg)

| >logicalChannelIdentity | M | {132} SRB/DRB logical channel identity | |-------------------------|---|------------------------------------------------- ----------------------------| | >> S-NSSAI | M | Slice identifier associated to the logical channel | | >> dataVolume | M | Integer representing number of Cumulative Bytes for the logi<br>cal channel |

### <span id="page-87-0"></span>11.2.4.2.17 Scheduling Request Indication

MAC indicates to scheduler through this API when UE has to be scheduled for uplink grant.

| Element | Presence | Description | |------------------------|----------|------------------------------------------- -----------------------| | Cell Index | M | Identification of the Cell.<br>2-byte integer allocated by<br>DU | | CRNTI | M | See TS 38.331 RNTI-Value | | Timing Infor<br>mation | M | Timing information for this<br>particular message. | | Number of SR<br>Bits | M | {07} number of SR bits<br>reported | | SR Payload | M | Bitmap equal to the<br>MAX\_SR\_BIT |

#### \*\*Table 11-36 Scheduling Request Indication\*\*

### <span id="page-87-1"></span>11.2.4.2.18 UL Buffer Status Report Indication This API is invoked by MAC on reception and Decoding of received BSR from the UE.

| Element | Presence | Description

|--------------------------------|----------|----------------------------------- -----------------------------------------------| | Cell Index | M | Identification of the Cell. 2-byte integer allocated by DU | | CRNTI | M | See TS 38.331 RNTI-Value | | BSR Type | M | Enumeration of {SHORT\_BSR, LONG\_BSR,<br>SHORT\_TRUNCATED\_BSR, LONG\_TRUNCATED\_BSR} | | Number of UL LCGs Re<br>ported | M | Number of UL LCGs carried in the BSR | | >logicalChannelGroupId | M | {07} logical channel Group identity | | >> dataVolume | M | Integer representing number of reported Bytes |

#### \*\*Table 11-37 Buffer Status Report Indication\*\*

#####################################SPEC NODE END############################ # SPEC 035: 11.2.4.2.19 Power Headroom Indication #####################################SPEC NODE START############################ ## <span id="page-87-2"></span>11.2.4.2.19 Power Headroom Indication

MAC invokes this API to inform Scheduler on reception and decoding of received PHR from the UE.

| Element | Presence | Description | |-----------------------|----------|-------------------------------------------- -------------------------------------------------------------------------| | Cell Index | M | Identification of the Cell. 2-byte integer allocated by DU | | CRNTI | M | See TS 38.331 RNTI-Value | | PHR Type | M | Enumeration of {SINGLE\_ENTRY\_PHR,<br>MULTIPLE\_ENTRY\_PHR} | | >Single Entry PHR | O | Present if the PHR Type == SINGLE\_ENTRY\_PHR | | >>Power Head Room | M | 1 Byte – Reported Power Head Room as per 38.321 Section<br>6.1.3.8 | | >> PCMAX, f, c | M | This field indicates the PCMAX, f, c (as

![](\_page\_88\_Picture\_1.jpeg)

|

```
specified in TS<br>38.213) used for calculation of the preceding PH field. |
| >Multiple Entry PHR | O | Present if PHR Type == MULTIPLE_ENTRY_PHR 
|
| >>Number of Reports | M | Number of PHRs reported in this instance. 
Range as specified<br>in TS 38.321 |
| >>PH Type | M | Enumeration {PH_TYPE_1, PH_TYPE_2} 
|
| >>>Power Head<br>Room | M | 1 Byte – Reported Power Head Room as per 
38.321 Section<br>6.1.3.8 |
| >>> PCMAX, f, c | M | This field indicates the PCMAX, f, c (as 
specified in TS<br>38.213) used for calculation of the preceding PH field. |
```

#### \*\*Table 11-38 Power Headroom Indication\*\*

```
#####################################SPEC NODE END############################
# SPEC 036: 11.2.4.3 Scheduler to MAC APIs
#####################################SPEC NODE START############################
## <span id="page-88-0"></span>11.2.4.3 Scheduler to MAC APIs
```

### <span id="page-88-1"></span>11.2.4.3.1 Cell Configuration Response

This API is invoked by scheduler to respond to a Cell configuration request.

| <br>Element                                                                          |                                                      | Presence | <br>Description                                |
|--------------------------------------------------------------------------------------|------------------------------------------------------|----------|------------------------------------------------|
| <br> ------------- ---------- ------------------------------------------------------ |                                                      |          |                                                |
| ------ <br>  Cell Index   M<br>by DU                                                 | Identification of the Cell. 2-byte integer allocated |          |                                                |
| Response<br>  M                                                                      | Response that maybe used to identify failure/success |          |                                                |
| <br> <br>                                                                            |                                                      |          | OK<br>–<br>Success                             |
| <br>                                                                                 |                                                      |          | NOK<br>–<br>Failure                            |
| <br>Error<br>Cause<br>                                                               | O                                                    | <br>If   | Response<br>==<br>NOK                          |
| <br> <br> <br>                                                                       |                                                      |          | This field describes the cause of the failure. |

#####################################SPEC NODE END############################ # SPEC 037: 11.2.4.3.2 Cell Deletion Response #####################################SPEC NODE START############################ ## <span id="page-88-2"></span>11.2.4.3.2 Cell Deletion Response

This API is invoked by scheduler to respond to a Cell Deletion request.

![](\_page\_89\_Picture\_1.jpeg)

| Element | Presence | Description | |-------------|----------|------------------------------------------------------ ---------------------------------| | Cell Index | M | Identification of the Cell. 2-byte integer allocated by DU | | Response | M | Response that maybe used to identify failure/success<br>OK – Success<br>NOK – Failure | | Error Cause | O | If Response == NOK<br>This field describes the cause of the failure. |

#### \*\*Table 11-40 Cell Deletion Response\*\*

### <span id="page-89-0"></span>11.2.4.3.3 Slice Configuration Response

This API is invoked by scheduler to respond to a Slice Configuration request.

| <br>Element                                                                                                                                                         |           |    | Presence<br> | Description                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----|--------------|------------------------------------------------------|
|                                                                                                                                                                     |           |    |              |                                                      |
| ------------- ---------- ------------------------------------------------------<br>-------------------------------------------------------------------------------- |           |    |              |                                                      |
| ------------------                                                                                                                                                  |           |    |              |                                                      |
| Slice Index   M                                                                                                                                                     |           |    |              | Identification of the Slice. This constitute of SST  |
| of<br>8-bit                                                                                                                                                         | and<br>SD | of | 24-bit       | value.                                               |
|                                                                                                                                                                     |           |    |              |                                                      |
| Response<br>  M                                                                                                                                                     |           |    |              | Response that maybe used to identify failure/success |
| in case<br>the slice configuration is accepted by the scheduler.<br>OK –                                                                                            |           |    |              |                                                      |
| Success<br>NOK –<br>Failure                                                                                                                                         |           |    |              |                                                      |
| Error Cause   O                                                                                                                                                     |           |    |              | If Response == NOK<br>This field describes the cause |
| of the failure. The cause can be<br>specific to Vendor's implementation.                                                                                            |           |    |              |                                                      |
|                                                                                                                                                                     |           |    |              |                                                      |

#### \*\*Table 11-41 Slice Configuration Response\*\*

### <span id="page-89-1"></span>11.2.4.3.4 Slice Reconfiguration Response

This API is invoked by scheduler to respond to a Slice Reconfiguration request.

| Element | Presence | Description |
|---------|----------|-------------|

| ------------- ---------- ------------------------------------------------------                                  |           |                                                      |        |          |    |        |
|------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------------------------|--------|----------|----|--------|
| --------------------------------------------------------------------------------<br>---------------------------- |           |                                                      |        |          |    |        |
| Slice Index   M                                                                                                  |           | Identification of the Slice. This constitute of SST  |        |          |    |        |
| of<br>8-bit                                                                                                      | and<br>SD | of                                                   |        | 24-bit   |    | value. |
|                                                                                                                  |           |                                                      |        |          |    |        |
| Response<br>  M                                                                                                  |           | Response that maybe used to identify failure/success |        |          |    |        |
| in case<br>the slice reconfiguration request is accepted by the scheduler.<br>OK                                 |           |                                                      |        |          |    |        |
| –<br>Success<br>NOK –                                                                                            | Failure   |                                                      |        |          |    |        |
| <br>Error<br>Cause<br>                                                                                           | O         |                                                      | <br>If | Response | == | NOK    |
|                                                                                                                  |           |                                                      |        |          |    |        |
|                                                                                                                  |           |                                                      |        |          |    |        |
| **Table 11-42 Slice Reconfiguration Response**                                                                   |           |                                                      |        |          |    |        |

![](\_page\_90\_Picture\_1.jpeg)

-------------------------------|

|

| | This field describes the cause of the failure. The cause can be<br>specific to Vendor's implementation. |

|  |                               | -- ---------------------------------------------------------------------------- |
|--|-------------------------------|---------------------------------------------------------------------------------|
|  | ----------------------------- |                                                                                 |
|  |                               | -- ---------------------------------------------------------------------------- |
|  | ----------------------------- |                                                                                 |

#####################################SPEC NODE END############################ # SPEC 038: 11.2.4.3.5 UE Configuration Response

#####################################SPEC NODE START############################ ## <span id="page-90-0"></span>11.2.4.3.5 UE Configuration Response

This response API is used by scheduler to respond to a UE configuration request from MAC.

|  | Element |                                                                                  |  | Presence |  | Description |
|--|---------|----------------------------------------------------------------------------------|--|----------|--|-------------|
|  |         |                                                                                  |  |          |  |             |
|  |         | ------------- ---------- ------------------------------------------------------  |  |          |  |             |
|  |         | -------------------------------------------------------------------------------- |  |          |  |             |

| Cell Index | M | Identification of the Cell. 2-byte integer allocated by<br>DU

| beamIndex | M | Index of the beam.<br>For example, please see subclause 6.6.2 of TS 38.331<br>[54] where the ssb-Index in the rsIndexResults element<br>of MeasResultNR is defined. | | CRNTI | M | See TS 38.331 RNTI-Value

```
|
| Response | M | Response that maybe used to identify 
failure/success<br>OK – Success<br>NOK – Failure 
|
| Error Cause | O | If Response == NOK<br>This field describes the cause 
of the failure. 
|
```

#### \*\*Table 11-43 UE Configuration Response\*\*

### <span id="page-90-1"></span>11.2.4.3.6 UE Reconfiguration Response

This response API is used by scheduler to respond to a UE reconfiguration request from MAC.

#### \*\*Table 11-44 UE Reconfiguration Response\*\*

| Element | Presence | Description | |------------|----------|------------------------------------------------------- --------| | Cell Index | M | Identification of the Cell. 2-byte integer allocated by<br>DU |

## ![](\_page\_91\_Picture\_1.jpeg)

| <br>beamIndex                                                                                                                                                                      |  |                                                              | M |       | Index |    | of     | the | beam.      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--------------------------------------------------------------|---|-------|-------|----|--------|-----|------------|
| <br> ------------- --- -------------------------------------------------------------                                                                                               |  |                                                              |   |       |       |    |        |     |            |
| --------------------------------------------------------------------------------<br>--- <br> <br>where the ssb-Index in the rsIndexResults ele<br>ment of MeasResultNR is defined. |  | For example, please see subclause 6.6.2 of TS 38.331<br>[54] |   |       |       |    |        |     |            |
| <br> <br>CRNTI<br>                                                                                                                                                                 |  |                                                              |   | M<br> | See   | TS | 38.331 |     | RNTI-Value |
| Response                                                                                                                                                                           |  | M   Response that maybe used to identify failure/success     |   |       |       |    |        |     |            |
| <br>                                                                                                                                                                               |  |                                                              |   |       |       |    | OK     | –   | Success    |
| <br>                                                                                                                                                                               |  |                                                              |   |       |       |    | NOK    | –   | Failure    |
| <br> <br>                                                                                                                                                                          |  |                                                              |   |       |       |    |        |     |            |

```
| Error Cause | O | If Response == NOK 
|
| | | This field describes the cause of the failure. 
|
| | | 
|
```

#####################################SPEC NODE END############################ # SPEC 039: 11.2.4.3.7 UE Deletion Response #####################################SPEC NODE START############################ # <span id="page-91-0"></span>11.2.4.3.7 UE Deletion Response

Scheduler responds with this API to a UE deletion request from MAC.

\*\*Table 11-45 UE Deletion Response\*\*

| <br>Element                       | <br>Presence<br> <br>Description                                                |
|-----------------------------------|---------------------------------------------------------------------------------|
|                                   | ------------- ---------- ------------------------------------------------------ |
| --------------------------------- |                                                                                 |
| Cell Index   M                    | Identification of the Cell. 2-byte integer allocated                            |
| by DU                             |                                                                                 |
| <br>CRNTI                         | <br>M<br> <br>See<br>TS<br>38.331<br>RNTI-Value                                 |
|                                   |                                                                                 |
| Response<br>  M                   | Response that maybe used to identify                                            |
| failure/success<br>OK –           | Success<br>NOK –<br>Failure                                                     |
| Error Cause   O                   | If Response == NOK<br>This field describes the cause                            |
| of the failure.                   |                                                                                 |

#####################################SPEC NODE END############################ # SPEC 040: 11.2.4.3.8 DL Scheduling Information #####################################SPEC NODE START############################ ## <span id="page-91-1"></span>11.2.4.3.8 DL Scheduling Information

Scheduler provides scheduling information for a given TTI for downlink data. Downlink data can either be a Broadcast message or RAR or MSG4 or Grant for the BSR response or a Dedicated downlink message. Scheduling information contains timing information, time and frequency domain resources to be scheduled with a list of logical channels and TBS opportunity per LC, BWP information along with PDCCH and PDSCH configuration. Additionally, SCH also provides a list of MAC CEs that are scheduled for a specific transmission opportunity. MAC is supposed to encode these CEs into the MAC PDU.

#### \*\*Table 11-46 DL Scheduling Information\*\*

| Element | Presence | Description | |---------|----------|-------------| |---------|----------|-------------|

![](\_page\_92\_Picture\_1.jpeg)

| Cell Index | M | Identification of the Cell. 2-byte integer allocated by DU | |------------------------------------|---|-------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ----------------------------------------------------------| | Timing Information | M | Timing information for this message (SFN/Slot). | | CRNTI | M | See TS 38.331 RNTI-Value. This may be SI-RNTI or C<br>RNTI or RA-RNTI. | | Broadcast Presence | M | If DL scheduling is for broadcast message | | Downlink Broad<br>cast Allocation | O | DL Resource allocation for Broadcast message conditionally<br>present when Broadcast Presence is true. | | >SSB Transmission | M | SSB Transmission mode as follows: | | Mode | | { \* 0 : No transmission | | | | \* 1 : SSB Transmission | | | | \* 2 : SSB Repetition } | | >Supported SSB In | M | Supported SSB Index | | dex | | | | >SSB Information | M | SSB Resource information | | >>SSB Index | M | SS/PBCH block index within an SSB burst set [TS38.211,<br>section 7.3.3.1]. Required for PBCH DMRS scrambling.<br>Value: 0->63 (Lmax) |

| >>TimeDo<br>mainAllocation | M | Time Domain resources allocation [TS38.211 section<br>7.4.3.1] | | >>>StartSym<br>bolNumber | M | OFDM symbol number | | >>>Number of<br>Symbols | M | Number of Symbols | | >>FrequencyDo<br>mainAllocation | M | Frequency Domain resources allocation [TS38.211 section<br>7.4.3.1] | | >>>StartPRB | M | PRB start number | | >>>NoOfPRBs | M | Number of PRBs | | > System infor<br>mation indicator | M | {0 – 1}. Specifies SIB1 or SI message; as defined in 38.212<br>Table 7.3.1.2.1-2 | | > SI Content | M | Byte Array [MAX\_BYTES\_FOR\_SI]; this carries the ASN.1<br>encoded System Information Messages that Scheduler wants<br>to transmit to the UE; as defined in 38.331 SIB1 or SystemIn<br>formation. Maximum TB size is 2976 bytes as per 38.214<br>section 5.1.3.2 | | > SIB1 Transmis<br>sion Mode | M | SIB1 transmission mode | | > SIB1 Allocation<br>Information | O | SIB1 Resource Allocation Information | ![](\_page\_93\_Picture\_1.jpeg) | >> BWP Config<br>uration | M | Specifies the BWP information for Scheduling Broadcast<br>data, Refer Table 9-34 BWP Configuration | |---------------------------------------|---|----------------------------------- -----------------------------------------------------------------------------| | >> PDCCH<br>Configuration | M | Specifies the CORESET and DL DCI(s) information. | | >>><br>CORESET Configu<br>ration | M | CORESET Configuration. Refer Table 9-35 CORESET Con<br>figuration. | | >>> Num<br>berOfDLDCI | M | Number of DL DCIs | | >>> DLDCI | O | DL DCI Information, Refer Table 9- 39 DL DCI Configura<br>tion | | Random Access Re<br>sponse Allocation | O | DL Resource allocation for Random Access Response mes<br>sage conditionally present when RAR Presence is true. | | > RAR Infor<br>mation | | |

| >>RAPID | M | | | >>TA | M | timing advance command [11, TS 38.321],<br>. Refer TS<br>TA<br>38.321 section 4.2 | | >>msg3FreqAlloc | M | Frequency Domain resource allocation for msg3 | | >>>StartPRB | M | BWPStart: bandwidth part start RB index from reference<br>CRB [TS38.213 sec 12] Value: 0->274 | | >>>NoOfPRBs | M | BWPSize: Bandwidth part size [TS38.213 sec12]. Number of<br>contiguous PRBs allocated to the BWP Value: 1->275 | | >>TC\_RNTI | M | See TS 38.331 RNTI-Value | | >>rarPDULen | M | RAR PDU Length | | >>rarPDU | M | RAR PDU | | > BWP Configura<br>tion | M | Specifies the BWP information for Scheduling Random Ac<br>cess Response. Refer Table 9-34 BWP Configuration. | | > PDCCH Config<br>uration | M | Specifies the CORESET and DL DCI(s) information. | | >> CORESET<br>Configuration | M | CORESET Configuration. Refer Table 9-35 CORESET Con<br>figuration. | | >> Number<br>OfDLDCI | M | Number of DL DCIs | | >> DLDCI | M | DL DCI and DL SCH Information. Refer Table 9-39 DL<br>DCI Configuration. | | DCI Information | O | Downlink Control Information for UL grant | | > BWP Configura<br>tion | M | Specifies the BWP information for Downlink control data.<br>Refer Table 9-34 BWP Configuration. | ![](\_page\_94\_Picture\_1.jpeg) | > CORESET Con<br>figuration | M | CORESET Configuration . Refer Table 9-35 CORESET<br>Configuration. | |-------------------------------------------------|---|------------------------- -------------------------------------------------------------------------------- -----------------| | > DCI Format<br>Type | M | DCI Format as defined in TS 38.212 section 7.3.1 |

```
| >> Format 0_0 | | DCI format for 
scheduling PUSCH in one cell, Refer Table<br>9-36 DCI Format 0_0 Configuration. 
|
| >> Format 0_1 | | DCI format for 
scheduling one or multiple PUSCH in one<br>cell, Refer Table 9-37 DCI Format 0_0 
Configuration. |
| > DLDCI | M | DL DCI and DL SCH 
Information 
|
| Downlink Message<br>Allocation | O | DL data Allocation 
|
| > DCIFormatID | M | Value: 1 bit, the value 
of this bit field is always set to 1, indi<br>cating a DL DCI format 
|
| > harqProcessID | M | HARQ process number 4 
bits [TS38.212, sec 7.3.1.2], it<br>should match value sent in DCI Value: 0 ->15 
|
| > VRB<br>PRBMapping | M | Value: 1, According to 
38.212 Table 7.3.1.1.2-33<br>0: Non-Interleaved<br>1: Interleaved 
|
| > DownlinkAssign<br>mentIndex | M | Value:2 bits [TS38.214, 
sec 7.3.1.1.2] 
|
| > tpcCommand | O | TPC command for 
scheduled PUSCH, TS 38.213-table 7.1.1-<br>1 
|
| > PUCCHRe<br>sourceIndicator | M | Given by higher layer 
parameter PUCCHResourceSet de<br>fined in PUCCH-Config, else as defined in TS 
38.213 table -<br>1. |
| > PDSCH-to<br>HARQ_feedback<br>timing indicator | O | Value: 3 bits. maps to 
maps to k1= {1,2,3,4,5,6,7,8}. 
|
| >>dlMsgPDU | M | DL Message PDU 
|
| >>dlMsgPDULen | M | DL Msg PDU Length 
|
| Frequency Domain<br>Allocation | M | Frequency Domain resource 
assignment; as defined in<br>38.214 
|
| >resource allocation<br>type | M | {Type-0, Type-1} from 
38.214 
|
| >resourceAlloca<br>tionType-0 | O | Conditional presence on 
the resource allocation type value
```

```
|
| >>rbBitMap | M | Resource allocation 
Type-0 bit map 
|
| >resourceAlloca<br>tionType-1 | O | Conditional presence on 
the resource allocation type value 
|
| >>Start RB | M | Starting Resource Block 
for the allocation 
|
![](_page_95_Picture_1.jpeg)
| >>Number of RBs | M | Number of allocated Resource Blocks 
|
|-----------------------------------|---|---------------------------------------
--------------------------------------------------------------------------------
-----------------------------------------------------------------------------|
| Time Domain Allo<br>cation | M | Specifies the time domain allocation 
for this transmission 
|
| >Start Symbol In<br>dex | M | Specifies the index of the starting 
symbol of the allocation<br>{0…13} 
|
| >Number of Sym<br>bols | M | Specifies the number of contiguous 
symbols allocated for<br>this transmission<br>{1…14} 
|
| Number of TBs | M | Number of scheduled Transportblocks 
|
| TB1 | M | Transport Block#1 
|
| >MCS | M | {0…31} per 38.214 
|
| >NDI | M | New Data Indicator (toggled if a new 
transmission) 
|
| >RV | M | Redundancy Version {0, 2, 3, 1} per 
38.212 
|
| >TB Size | M | Transport Block Size in Bytes 
{0…65535} 
|
| >Number of DL<br>CEs Scheduled | M | Number of DL CEs Scheduled {0…32} 
|
```

```
| >>CE Content | M | Information for the CE carried in non-
encoded format.<br>Refer the table below for details 
|
| >Number of DL<br>LCs Scheduled | M | Number of DL LCs Scheduled {0…32}; 
includes both SRBs<br>and DRBs 
|
| >>DL LCID | M | DL LCs ID {0…32} 
|
| >>Number of<br>Scheduled<br>Bytes | M | Number of Scheduled Bytes for this 
specific Logical Channel<br>{0…65535} 
|
| TB2 | O | Transport Block # 2 
|
| >MCS | M | {0…31} per 38.214 
|
| >NDI | M | New Data Indicator (toggled if a new 
transmission) 
|
| >RV | M | Redundancy Version {0, 2, 3, 1} per 
38.212 
|
| >TB Size | M | Transport Block Size in Bytes 
{0…65535} 
|
| >Number of DL<br>CEs Scheduled | M | Number of DL CEs Scheduled {0…32} 
|
| >>CE LCID | M | Corresponds to CEs LCID as per 38.321 
|
| >>CE Content | M | Byte Array [MAX_BYTES_PER_CE]; this 
carries the CE<br>content (not encoded) that Scheduler wants to transmit to 
the<br>UE. MAC takes this content and encode per the formats de<br>fined in 38.321 
|
![](_page_96_Picture_1.jpeg)
| >Number of DL<br>LCs Scheduled | M | Number of DL LCs Scheduled {0…32}; 
includes both SRBs<br>and DRBs |
|-----------------------------------|---|---------------------------------------
----------------------------------------------------------|
| >>DL LCID | M | DL LCs ID {0…32} 
|
| | M | Number of Scheduled Bytes for this 
specific Logical Channel |
```

| >>Number of<br>Scheduled<br>Bytes | | {0…65535}

| | > BWP Configura<br>tion | M | Specifies the BWP information for Downlink control data.<br>Refer Table 9-34 BWP Configuration. | | > PDCCH Config<br>uration | M | Specifies the CORESET and DL DCI(s) information. | | >> CORESET<br>Configuration | M | CORESET Configuration, Refer Table 9- 35 CORESET Con<br>figuration. | | >> Number<br>OfDLDCI | M | Number of DL DCIs | | >> DLDCI | M | DL DCI and DL SCH Information. Refer Table 9-39 DL DCI<br>Configuration. | #### \*\*Table 11-47 MAC CE Information\*\* | Element | Presence | Description | |---------------------------------------------|----------|----------------------

----------------------------------------------------------| | CE LC\_ID | M | Corresponds to CEs LCID as per 38.321 |

--------------------------------------------------------------------------------

| Contention Resolution Identity<br>CE | O | If LC\_ID corresponds to UE Contention Resolution Identity<br>CE. No content is sent from Scheduler to MAC as the contents<br>of Msg3 are to be buffered at MAC |

| Timing Advance Command<br>CE | O | If LC\_ID corresponds to Timing Advance Command CE | | >TAG ID | M | Timing Advance Group ID as per 38.321 |

| >Timing Advance | M | Index value of TA per 38.321 and 38.213 |

| SCell Activation/Deactivation<br>CE | O | If LC\_ID Corresponds to SCell Activation/Deactivation CE |

| >Number of SCells | M | Number of SCells being addressed in this IE | | >act\_deact\_val<br>[MAX\_NUMBER<br>OF\_SCELLS] | M | An Array of values

corresponding to the index of the SCell as<br>configured per 38.331.

|

| | | Value at each index i

corresponds to | | | | 0 – Deactivation | | | | 1 – Activation | | | | MAX\_NUMBER\_OF\_SCELL = 31 per 38.321 current specifi<br>cation, subject to change with newer specification versions. |

![](\_page\_97\_Picture\_1.jpeg)

| BFR MAC CE | O | | |-------------------|---|------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ---------------------------------------------------| | >SP | M | Beam failure detection for the SpCell of this MAC entity as per<br>TS 38.321 section 6.1.3. |

| > Ci | M | Beam failure detection (as specified in TS 38.321 clause 5.17)<br>and the presence of an octet containing the AC field for the<br>SCell with ServCellIndex i as specified in TS 38.331. |

| > AC | M | Indicates the presence of the Candidate RS ID field in this oc<br>tet as per TS 38.321 section 6.1.3. |

| > Candidate RS ID | M | Index of an SSB with SS-RSRP above rsrp-ThresholdBFR<br>amongst the SSBs in candidateBeamRSSCellList or to the in<br>dex of a CSI-RS with CSI-RSRP above rsrp-ThresholdBFR<br>amongst the CSI-RSs in candidateBeamRSSCellList. Index of<br>an SSB or CSI-RS is the index of an entry in candidate<br>BeamRSSCellList corresponding to the SSB or CSI-RS. | | >R | M | Reserved bit, set to 0.

|

#### \*\*Table 11-48 BWP Information\*\*

|  | Element                                                                         |  | Presence |  | Description |
|--|---------------------------------------------------------------------------------|--|----------|--|-------------|
|  |                                                                                 |  |          |  |             |
|  | ---------------------- ---------- --------------------------------------------- |  |          |  |             |
|  | -----------------                                                               |  |          |  |             |
|  |                                                                                 |  |          |  |             |

| | BWP | M | Specifies the DL DCI Coreset and Search Space for Schedul | | | | ing DCI for Broadcast data. | | >Subcarrierspacing | M | subcarrierSpacing [TS38.211 sec 4.2] Value:0->4 | | >CyclicPrefix | M | Cyclic prefix type [TS38.211 sec 4.2] 0: Normal; 1: Extended | | >Frequency Domain Re | M | Frequency Domain resources allocation | | sources | | | | >>StartPRB | M | BWPStart: bandwidth part start RB index from reference CRB | | | | [TS38.213 sec 12] Value: 0->274 | | >>NoOfPRBs | M | BWPSize: Bandwidth part size [TS38.213 sec12]. Number of | | | | contiguous PRBs allocated to the BWP Value: 1->275 |

#### \*\*Table 11-49 CORESET Configuration\*\*

| Element | Presence | Description | |---------------------------|----------|---------------------------------------- -------------------------------------------------------------------------------- ----------------------------| | CORESET | M | Specifies the CORESET Information. Refer [TS38.211 sec<br>7.3.2.2] | | > CORESET Size | M | Coreset size, {One CORESET, Two CORESET ,} | | > StartSymbolIndex | M | Starting OFDM symbol for the CORESET Value: 0->13 | | > DurationSymbols | M | Contiguous time duration of the CORESET in number of sym<br>bols. Corresponds to L1 parameter <br>[TS38.211 sec 7.3.2.2] Value: 1,2,3 | | > FrequencyDomainResource | M | Resource location in frequency domain. This IE is a bitmap,<br>similar to Type1 frequency domain allocation. |

## ![](\_page\_98\_Picture\_1.jpeg)

| > CceRegMappingType | M | CORESET-CCE-to-REG-mapping-type [TS38.211 sec 7.3.2.2]<br>0: non-interleaved 1: interleaved | |-----------------------|---|--------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ----------------------------------------------------------| | >> RegBundleSize | M | The number of REGs in a bundle. Must be 6 for cceRegMap<br>pingType = nonInterleaved. For cceRegMappingType = inter<br>leaved, must belong to {2,6} if duration = 1,2 and must belong<br>to {3,6} if duration = 3. Corresponds to parameter L.<br>[TS38.211 sec 7.3.2.2] Value: 2,3,6 | | >>InterleaverSize | M | The interleaver size. For interleaved mapping belongs to<br>{2,3,6} and for non-interleaved mapping is NA. Corresponds<br>to parameter R. [TS38.211 sec 7.3.2.2] Value: 2,3,6 | | >>ShiftIndex | M | [TS38.211 sec 7.3.2.2] Not applicable for noninterleaved<br>mapping. For interleaved mapping and a PDCCH transmitted<br>in a CORESET configured by the PBCH or SIB1 this should<br>be set to phy cell ID. Value: 10 bits Otherwise, for interleaved<br>mapping this is set to 0-> max num of PRBs. Value 0-> 275 | | > CORESETType | M | [TS38.211 sec 7.3.2.2 and sec 7.4.1.3.2] 0: CORESET is con<br>figured by the PBCH or SIB1 (subcarrier 0 of CRB0 for<br>DMRS mapping) 1: otherwise (subcarrier 0 of CORESET) | | > CoresetPoolIndex | O | The index of the CORESET pool for this CORESET as speci<br>fied in TS 38.213 [13] (clauses 9 and 10) and TS 38.214 [19]<br>(clauses 5.1 and 6.1). | | | | With two different values of CORESETPoolIndex in Con<br>trolResourceSet, the UE may expect to receive multiple<br>PDCCHs scheduling fully/partially/non-overlapped PDSCHs<br>in time and frequency domain. The UE may expect the recep<br>tion of full/partially-overlapped PDSCHs in time only when<br>PDCCHs that schedule two PDSCHs are associated to different<br>ControlResourceSets having different values of CORESET<br>PoolIndex. | | > PrecoderGranularity | M | Granularity of precoding [TS38.211 sec 7.3.2.2] 0:<br>sameAsRegBundle 1: allContiguousRBs

```
|
| > CCEIndex | M | CCE start Index used to send the DCI Value: 0->135 
|
| > AggregationLevel | M | Aggregation level used [TS38.211, sec 7.3.2.1] 
Value:<br>1,2,4,8,16 
|
| Element | Presence | Description 
|
|-----------------------------------|----------|--------------------------------
-----------------------------------------|
| FORMAT0_0 | M | Specifies the DCI format 0_0 
[TS38.212 sec 7.3.1.1.1] |
| > resourceAlloc | M | Resource Allocation Type 
[TS38.214, sec 6.1.2.2] 0: Type 0 1:<br>Type 1 |
| > Frequency Domain Alloca<br>tion | M | Frequency Domain resources 
allocation |
| >>resource allocation type | M | {Type-0, Type-1} from 38.214 
|
| >>resourceAllocationType-0 | O | Conditional presence on the 
resource allocation type value |
#### **Table 11-50 DCI Format0\_0 Configuration**
![](_page_99_Picture_1.jpeg)
| >>>rbBitMap | M | Resource allocation Type-0 bit map 
|
|-----------------------------|---|---------------------------------------------
--------------------------------------------------------------------------------
```

----------------------| | > >resourceAllocationType-1 | O | Conditional presence on the resource allocation type value | | >>> StartPRB | M | BWPStart: bandwidth part start RB index from reference CRB<br>[TS38.213 sec 12] Value: 0->274 | | >>> NoOfPRBs | M | BWPSize: Bandwidth part size [TS38.213 sec12]. Number of<br>contiguous PRBs allocated to the BWP Value: 1->275 | | >TimeDomainAllocation | M | 4 bits as defined in Clause 6.1.2.1 of [6, TS 38.214] | | >> StartSymbolNumber | M | OFDM symbol number | | >> Number of Symbols | M | Number of Symbols | | > Row | M | Row entry to pusch-AllocationList, Time Domain resource al<br>location for PUSCH based on 38.214 - 6.1.2.1 Resource alloca<br>tion in time domain | | > mcs | M | mcsIndex uint8\_t MCS index [TS38.214, sec 6.1.4, & 5.1.3.1],<br>Value: 0->31 | | > harqProcessID | M | HARQ process number [TS38.212, sec 7.3.1.1], it should<br>match value sent in DCI Value: 0 ->15 | | > FrequencyHopping | M | For resource allocation type 1. [TS38.212, sec 7.3.1.1]<br>[TS38.214, sec 6.3] Indicates if frequency hopping is enabled<br>Value: 0: disabled | | > newDataIndicator | M | Indicates if this new data or a retransmission [TS38.212, sec<br>7.3.1.1]<br>Value: 0: retransmission 1: new data | | > rvIndex | M | Redundancy version index [TS38.214, sec 6.1.4], it should<br>match value sent in DCI Value: 0->3 | | > tpcCommand | M | TPC command for scheduled PUSCH, TS 38.213 table 7.1.1-1 | | > SULIndicator | M | SUL Configuration, | | | | 0 bit: SUL not figured | | | | 1 bit: SUL configured | | | | |

## #### \*\*Table 11-51 DCI Format0\\_1 Configuration\*\*

| Element | Presence | Description | |--------------------|----------|----------------------------------------------- ---------------------------------------| | FORMAT0\_1 | M | Specifies the DCI format 0\_1 [TS38.212 sec 7.3.1.1.2] | | > carrierIndicator | M | Indicator to the carrier, 0 or 3 bits, as defined in Clause 10.1 of<br>[5, TS38.213] | | > SULIndicator | M | SUL Configuration,

```
![](_page_100_Picture_1.jpeg)
| | | 0 bit: SUL not figured 
|
|-----------------------------------|---|---------------------------------------
--------------------------------------------------------------------------------
----------------------------|
| | | 1 bit: SUL configured 
|
| | | 
|
| | | 
|
| > BWPIndicator | M | Bits-0,1,2. Determined by 
BandwidthPart-Config in higher<br>layer message and 38.212 - Table 7.3.1.1.2-1 
|
| > resourceAlloc | M | Resource Allocation Type [TS38.214, 
sec 6.1.2.2] 0: Type 0 1:<br>Type 1 
|
| > Frequency Domain Alloca<br>tion | M | Frequency Domain resources allocation 
|
| >> StartPRB | M | BWPStart: bandwidth part start RB 
index from reference CRB<br>[TS38.213 sec 12] Value: 0->274 
|
| >> NoOfPRBs | M | BWPSize: Bandwidth part size [TS38.213 
sec12]. Number of<br>contiguous PRBs allocated to the BWP Value: 1->275 
|
| >TimeDomainAllocation | M | 4 bits as defined in Clause 6.1.2.1 of 
[6, TS 38.214] 
|
| >> StartSymbolNumber | M | OFDM symbol number 
|
| >> Number of Symbols | M | Number of Symbols 
|
| > Row | M | Row entry to pusch-AllocationList, 
Time Domain resource al<br>location for PUSCH based on 38.214 - 6.1.2.1 Resource 
alloca<br>tion in time domain |
| > mcs | M | mcsIndex uint8_t MCS index [TS38.214, 
sec 6.1.4, & 5.1.3.1],<br>Value: 0->31 
|
| > harqProcessID | M | HARQ process number [TS38.212, sec 
7.3.1.1], it should<br>match value sent in DCI Value: 0 ->15
```

|

|

| > FrequencyHopping | M | For resource allocation type 1. [TS38.212, sec 7.3.1.1]<br>[TS38.214, sec 6.3] Indicates if frequency hopping is enabled<br>Value: 0: disabled | | > newDataIndicator | M | Indicates if this new data or a retransmission [TS38.212, sec<br>7.3.1.1] | | | | Value: 0: retransmission 1: new data | | > rvIndex | M | Redundancy version index [TS38.214, sec 6.1.4], it should<br>match value sent in DCI Value: 0->3 | | > 1stDownlinkAssignmentIn<br>dex | M | Value:1, 2 or 4 bits [TS38.214, sec 7.3.1.1.2] | | > 2ndDownlinkAssignmentIn<br>dex | M | Value:0, 2 or 4 bits [TS38.214, sec 7.3.1.1.2] | | > tpcCommand | M | TPC command for scheduled PUSCH, TS 38.213-table 7.1.1-1 | | >SRSResourceSetIndicator | M | 0 or 2 bits, 2 bits according to Table 7.3.1.1.2-36 in TS 38.212<br>0 bit otherwise. | ![](\_page\_101\_Picture\_1.jpeg)

| | | The SRS resource set applicability is configured by the higher<br>layer parameter usage in SRS-ResourceSet. When the higher<br>layer parameter usage is set to 'beamManagement', only one<br>SRS resource in each of multiple SRS sets may be transmitted<br>at a given time instant, but the SRS resources in different SRS<br>resource sets with the same time domain behaviour in the same<br>BWP may be transmitted simultaneously. | |--------------------------------|---|------------------------------------------ -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ---------------------------------------------------------------| | > SRSResourceIndicator | | Given by higher layer parameter srs-ResourceSetToAdd<br>ModList | | > TPMI | O | Value: 0,2,3,4,5,6. Determined by ulTxConfig, Number of An<br>tenna ports, PUSCH-tp, ULmaxRank

```
|
| > AntennaPorts | M | Value: 2,3,4,5. Determined by PUSCH-tp, 
DL-DMRS-config<br>type, DL-DMRS-config-max-len, Rank 
|
| > SRS Request | O | SRS Request Field, TS 38.212 Table 
7.3.1.1.2-24 
|
| > CSI Request | O | Value: 0,1,2,3,4,5,6, Determined by 
ReportTriggerSize in<br>RRC message.See Configure Aperiodic Trigger section for 
the<br>details. 
|
| > CBG Transmission Information | O | Value: 0, 2,4, 6,8. Determined by 
maxCodeBlockGroupPer<br>Transportblock in RRC message, 
|
| > PTRS-DMRS | O | Value: 0,2. Determined by UL-PTRS-present, 
PUSCH-tp in<br>RRC Message 
|
| > beta-offsetIndicator | O | Value: 0,2. 0 - if uci-on-PUSCH.dynamic = 
Not Configured<br>2 - otherwise 
|
| > DMRS Sequence Initialization | O | Value: 0,1. 0 - if PUSCH-tp=Disabled<br>1 
- if PUSCH-tp=Enabled 
|
| > UL-SCH Indicator | O | Value: 0, 1. 0 - UL-SCH is not transmitted 
on the PUSCH<br>1 - UL-SCH is transmitted on the PUSCH 
|
```

#### \*\*Table 11-52 DCI Format1\\_0 Configuration\*\*

![](_page_127_Figure_2.jpeg)

| | | | | | tion | | | | | | | | | | | | >> StartPRB | M | BWPStart: bandwidth part start RB index from reference CRB | | | | | | | | [TS38.213 sec 12] Value: 0->274 | | | | | | | | | | >> NoOfPRBs | M | BWPSize: Bandwidth part size [TS38.213 sec12]. Number of | | | | contiguous PRBs allocated to the BWP Value: 1->275 | | | | | | | | | ![](\_page\_102\_Picture\_1.jpeg) | >TimeDomainAllocation | M | 4 bits as defined in Clause 6.1.2.1 of [6, TS 38.214] | |--------------------------------------------------|---|------------------------ -------------------------------------------------------------------------------- -----------------| | >> StartSymbolNumber | M | OFDM symbol number | | >> Number of Symbols | M | Number of Symbols | | > VRB-PRBMapping | M | Value: 1, According to 38.212 Table 7.3.1.1.2-33<br>0: Non-Interleaved<br>1: Interleaved | | > mcs | M | mcsIndex uint8\_t MCS index [TS38.214, sec 6.1.4, & 5.1.3.1],<br>Value: 0->31 | | > harqProcessID | M | HARQ process number [TS38.212, sec 7.3.1.1], it should<br>match value sent in DCI Value: 0 ->15 | | > newDataIndicator | M | Indicates if this new data or a retransmission [TS38.212, sec<br>7.3.1.1]<br>Value: 0: retransmission 1: new data | | > rvIndex | M | Redundancy version index [TS38.214, sec 6.1.4], it should<br>match value sent in DCI Value: 0->3 | | > DownlinkAssignmentIndex | M | Value:2 bits [TS38.214, sec 7.3.1.1.2] | | > tpcCommand | M | TPC command for scheduled PUSCH, TS 38.213-table 7.1.1-1 | | > PUCCHResourceIndicator | M | Given by higher layer parameter PUCCHResourceSet de<br>fined in PUCCH-Config, else as defined in TS<br>38.213 table -1. | | > PDSCH-to<br>HARQ\_feedback timing indi<br>cator | O | Value: 3 bits. maps to maps to k1= {1,2,3,4,5,6,7,8}. |

#### \*\*Table 11-53 DCI Format1\\_1 Configuration\*\*

| Element | Presence | Description | |---------------------------|----------|---------------------------------------- -----------------------------| | | | | | FORMAT1\_1 | M | Specifies the DCI format 1\_1 [TS38.212 sec 7.3.1.2.2] | | | | | | > carrierIndicator | M | Indicator to the carrier, 0 or 3 bits, as defined in Clause 10.1 of | | | | [5, TS38.213] | | | | | | > BWPIndicator | M | Bits-0,1,2. Determined by BandwidthPart-Config in higher |

| | | layer message and 38.212 - Table 7.3.1.1.2-1 | | | | | | > resourceAlloc | M | Resource Allocation Type [TS38.214, sec 6.1.2.2] 0: Type 0 1: | | | | | | | | Type 1 | | | | | | > Frequency Domain Alloca | M | Frequency Domain resources allocation | | tion | | | | | | | | >> StartPRB | M | BWPStart: bandwidth part start RB index from reference CRB | | | | [TS38.213 sec 12] Value: 0->274 | | | | | ![](\_page\_103\_Picture\_1.jpeg) | >> NoOfPRBs | M | BWPSize: Bandwidth part size [TS38.213 sec12]. Number of<br>contiguous PRBs allocated to the BWP Value: 1->275 | |----------------------------------------------|---|---------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ------------------------------------------------| | >TimeDomainAllocation | M | 4 bits as defined in Clause 6.1.2.1 of [6, TS 38.214] | | >> StartSymbolNumber | M | OFDM symbol number | | >> Number of Symbols | M | Number of Symbols |

| > VRB-PRBMapping | M | Value: 1, According to 38.212 Table 7.3.1.1.2-33<br>0: Non-Interleaved<br>1: Interleaved | | > mcs | M | mcsIndex uint8\_t MCS index [TS38.214, sec 6.1.4, & 5.1.3.1],<br>Value: 0->31, Applicable for transport block#1 and transport<br>block#2 | | > harqProcessID | M | HARQ process number [TS38.212, sec 7.3.1.1], it should<br>match value sent in DCI Value: 0 ->15 | | > newDataIndicator | M | Indicates if this new data or a retransmission [TS38.212, sec<br>7.3.1.1] . Applicable for transport block#1 and transport<br>block#2 | | | | Value: 0: retransmission 1: new data | | > rvIndex | M | Redundancy version index [TS38.214, sec 6.1.4], it should<br>match value sent in DCI Value: 0->3. Applicable for transport<br>block#1 and transport block#2 | | > DownlinkAssignmentIndex | M | Value:2 bits [TS38.214, sec 7.3.1.1.2] | | > tpcCommand | M | TPC command for scheduled PUSCH, TS 38.213-table 7.1.1-1 | | >SecondtpcComand | O | 2 bits as defined in Clause 7.2.1 of [5, TS 38.213] if higher<br>layer parameter SecondTPCFieldDCI-1-1 is configured; 0 bit<br>otherwise | | > PUCCHResourceIndicator | M | Given by higher layer parameter PUCCHResourceSet de<br>fined in PUCCH-Config, else as defined in TS<br>38.213 table -1. | | > PDSCH-to-HARQ\_feedback<br>timing indicator | O | Value: 3 bits. maps to maps to k1= {1,2,3,4,5,6,7,8}. | | > AntennaPorts | M | 4, 5, or 6 bits as defined by Tables 7.3.1.2.2-1/2/3/4 and Tables<br>7.3.1.2.2-1A/2A/3A/4A in TS 38.312. | | > TransmissionConfigurationIndi<br>cation | O | 0 bit if higher layer parameter tci-PresentInDCI is not enabled;<br>otherwise 3 bits as defined in

Clause 5.1.5 of [6, TS38.214].<br>The UE may expect to be indicated with one or

two TCI states<br>in a codepoint of the DCI field 'Transmission Configuration<br>Indication' together with the DCI field "Time domain resource<br>assignment' indicating an entry in pdsch-TimeDomainAlloca<br>tionList |

| Element | Presence | Description | |----------------------------|----------|---------------------------------------

--------------------------------------------------------------------------------

-------------------------------------------------------------------------------- ---------------------------------------| | DL DCI | M | Specifies the DL DCI Coreset and Search Space for Schedul<br>ing DCI for Broadcast data. | | > C-RNTI | M | The RNTI used for identifying the UE when receiving the PDU<br>Value: 1 -> 65535 | | > ScramblingID | M | For a UE-specific search space it equals the higherlayer param<br>eter PDCCH-DMRS-Scrambling-ID if configured, otherwise it<br>should be set to the phy cell ID. [TS38.211, sec 7.3.2.3] Value:<br>0->65535 | | > ScramblingRNTI | M | For a UE-specific search space where PDCCH<br>DMRSScrambling-ID is configured This param equals the<br>CRNTI. Otherwise, it should be set to 0. [TS38.211, sec<br>7.3.2.3] Value: 0 -> 65535 | | > CCEIndex | M | CCE start Index used to send the DCI Value: 0->135 | | > AggregationLevel | M | Aggregation level used [TS38.211, sec 7.3.2.1] Value:<br>1,2,4,8,16 | | > BeamformingInfo | O | | | >> numPRGs | M | Number of PRGs spanning this allocation. Value: 1->275 | | >> prgSize | M | Size in RBs of a precoding resource block group (PRG) – to<br>which same precoding and digital beamforming gets applied.<br>Value: 1->275 | | >> digBFInterfaces | M | Number of STD ant ports (parallel streams) feeding into the<br>digBF Value: 0->255

```
| >> PRGInfo | O |
```

|

| | >>> PMidx | M | Index to precoding matrix (PM) prestored at cell configura<br>tion. Note: If precoding is not used this parameter should be set<br>to 0. Value: 0->65535. | | >>> beamIdx | M | For each digBFInterface, Index of the digital beam weight vec<br>tor pre-stored at cell configuration. The vector maps this input<br>port to output TXRUs. Value: 0->65535 | | > TxPowerPDCCHInfo | | | | >> beta\_PDCCH\_1\_0 | M | PDCCH power value used for PDCCH Format 1\_0 with CRC<br>scrambled by SI-RNTI, PI-RNTI or RA-RNTI. This is ratio of<br>SSB/PBCH EPRE to PDCCH and PDCCH DMRS EPRE<br>[TS38.213, sec 4.1] Value :0->17 representing -8 to 8 dB in<br>1dB steps | | >>PowerCon<br>trolOffsetSS | M | PDCCH power value used for all other PDCCH Formats. This<br>is ratio of SSB/PBCH block EPRE to PDCCH and PDCCH<br>DMRS EPRE [TS38.214, sec 4.1] Values: 0: -3dB, 1: 0dB, 2:<br>3dB, 3: 6dB | #### \*\*Table 11-54 DL-DCI Configuration\*\* ![](\_page\_105\_Picture\_1.jpeg)

| > PDSCH Configuration | PDSCH configuration for DL SCH data. Refer Table 9-40 DL | |-----------------------|------------------------------------------------------- ---| | | SCH Configuration. | | | | | Element | Presence | Description | |----------------------|----------|--------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- --------------------------------------------------------------| | DL SCH | O | Conditional presence on Short Message Indicator value for<br>broadcasting data. Present in case Short Message Indicator is 1<br>or 3; as defined in 38.212 Table 7.3.1.2.1-1. Mandatory for<br>other DL

| > pduBitmap | O | Bitmap indicating presence of optional PDUs

data. |

```
Bit 0: pdschPtrs -<br>Indicates PTRS included (FR2) Bit 1: cbgRetxCtrl 
(Present<br>when CBG based retransmit is used) All other bits reserved 
|
| > C-RNTI | M | The RNTI used for identifying the UE when 
receiving the PDU<br>Value: 1 -> 65535 
|
| > pduIndex | M | PDU index incremented for each PDSCH PDU 
sent in TX con<br>trol message. This is used to associate control information 
to<br>data and is reset every slot. Value: 0 -> 65535 
|
| > NrOfCodewords | M | Number of code words for this RNTI (UE) 
Value: 1 -> 2 
|
| > CodewordInfo | M | For each codeword 
|
| >> targetCodeRate | M | Target coding rate [TS38.212 sec 5.4.2.1 and 
38.214 sec<br>5.1.3.1]. This is the number of information bits per 1024 
coded<br>bits expressed in 0.1-bit units 
|
| >>qamModOrder | M | QAM modulation [TS38.212 sec 5.4.2.1 and 
38.214 sec<br>5.1.3.1] Value: 2,4,6,8 
|
| >>mcsIndex | M | MCS index [TS38.214, sec 5.1.3.1], should 
match value sent in<br>DCI Value: 0->31 
|
| >> mcsTable | M | MCS-Table-PDSCH [TS38.214, sec 5.1.3.1] 0: 
notqam256 1:<br>qam256 2: qam64LowSE 
|
| >> rvIndex | M | Redundancy version index [TS38.212, Table 
5.4.2.1-2 and<br>38.214, Table 5.1.2.1-2], should match value sent in DCI<br>Value: 
0->3 
|
| >> TBSize | M | Transmit block size (in bytes) [TS38.214 sec 
5.1.3.2] Value:<br>0->65535 
|
| > dataScramblingId | O | dataScramblingIdentityPdsch [TS38.211, sec 
7.3.1.1] It equals<br>the higher-layer parameter dataScramblingIdentityPDSCH 
[TS<br>38.331 PDSCH-Config] if configured and the RNTI equals the<br>C-RNTI, 
otherwise L2 needs to set it to physical cell id. Value:<br>0->65535 |
| > nrOfLayers | M | Number of layers [TS38.211, sec 7.3.1.3] 
Value: 1->8 
|
| > transmissionScheme | M | PDSCH transmission schemes [TS38.214, sec 
5.1.1] only one<br>transmission scheme (transmission scheme 1) for 0: Up to
```

## #### \*\*Table 11-55 PDSCH Configuration\*\*

![](\_page\_106\_Picture\_1.jpeg)

| > refPoint | M | Reference point for PDSCH DMRS "k" - used for tone map<br>ping [TS38.211, sec 7.4.1.1.2] Resource block bundles<br>[TS38.211, sec 7.3.1.6]. Value: 0 -> 1 If 0, the 0-reference<br>point for PDSCH DMRS is at Point A [TS38.211 sec 4.4.4.2].<br>Resource block bundles generated per subbullets 2 and 3 in<br>[TS38.211, sec 7.3.1.6]. For sub-bullet 2, the start of band<br>width part must be set to the start of actual bandwidth part<br>+NstartCORESET and the bandwidth of the bandwidth part<br>must be set to the bandwidth of the initial bandwidth part. If 1,<br>the DMRS reference point is at the lowest VRB/PRB of the al<br>location. Resource block bundles generated per sub-bullets 1<br>[TS38.211, sec 7.3.1.6] |

|-----------------------------|---|--------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- --------------------------| | > DMRS | M | | | >> dlDmrsSymbPos | M | DMRS symbol positions [TS38.211, sec 7.4.1.1.2 and Tables<br>7.4.1.1.2-3 and 7.4.1.1.2-4] Bitmap occupying the 14 LSBs<br>with:<br>bit 0: first symbol | | | | and for each bit | | | | 0: no DMRS 1: DMRS | | | | | | >> dmrsConfigType | O | DL DMRS config type [TS38.211, sec 7.4.1.1.2] given by the<br>higher-layer parameter [TS 38.331 DMRS-DownlinkConfig:<br>dmrs-Type] | | | | 0: type 1 1: type 2 | | >> dlDmrsScramblingId | O | DL-DMRS-Scrambling-ID [TS38.211, sec 7.4.1.1.2 ] If pro<br>vided by the higher-layer [ TS 38.331, DMRS<br>DownlinkConfig: scramblingID0, scramblingID1] and the<br>PDSCH is scheduled by PDCCH with CRC scrambled by C<br>RNTI or CS-RNTI, otherwise, L2 should set this to physical<br>cell id. Value: 0->65535 | | >> SCID | M | DMRS sequence initialization [TS38.211, sec 7.4.1.1.2].<br>Should match what is sent in DCI 1\_1, otherwise set to 0.<br>Value: 0->1 | | >> numDmrsCdmGrps<br>NoData | O | Number of DM-RS CDM groups without data [TS38.212 sec<br>7.3.1.2.2] [TS38.214 Table 4.1-1] it determines the ratio of<br>PDSCH EPRE to DM-RS EPRE. Value: 1->3 | | >> dmrsPorts | M | DMRS ports. [TS38.212 7.3.1.2.2] provides description be<br>tween DCI 1-1 content and DMRS ports. Bitmap occupying<br>the 11 LSBs with: bit 0: antenna port 1000 bit 11: antenna port<br>1011 and for each bit<br>0: DMRS port not used 1: DMRS port used | | | | | | >> MappingType | M | Selection of the DMRS type to be used for DL. Configuration<br>type 1 or configuration type 2 as given by the higher-layer pa<br>rameter dmrs-Type. | | >> NumberOfDMRSSymbols | O | The maximum number of OFDM symbols for DL front loaded<br>DMRS data [TS38.212 sec 7.4.1.1.2], provided by higherlayer<br>[TS 38.331 DMRS-DownlinkConfig: maxLength] len1 corre<br>sponds to value 1. len2 corresponds to value 2. If the field is | ![](\_page\_107\_Picture\_1.jpeg) | | | absent, the UE applies value len1. If set to len2, the UE deter<br>mines the actual number of DM-RS symbols by the associated<br>DCI. | |---------------------------|---|----------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ---------------------------| | >> DMRSAddPostion | O | Position for additional DM-RS in DL, see Tables 7.4.1.1.2-3<br>and 7.4.1.1.2-4 in TS 38.211 [16].

```
| >PDSCHFrequencyAllocation | M | PDSCH resource allocation in frequency domain 
[TS38.214,<br>sec 5.1.2.2] 
|
| >> resourceAlloc | M | Resource Allocation Type [TS38.214, sec 
5.1.2.2]<br>0: Type 0 1: Type 1 
|
| >> rbBitmap | O | Conditionally included for resource alloc type 
0. TS 38.212<br>V15.0.x, 7.3.1.2.2 bitmap of RBs, 273 rounded up to multiple<br>of 
32. This bitmap is in units of VRBs. LSB of byte 0 of the<br>bitmap represents 
the first RB of the bwp |
| >> rbStart | O | Conditionally included for resource allocation 
type 1.<br>[TS38.214, sec 5.1.2.2.2] The number of resource block within<br>for 
this PDSCH.<br>Value: 1->275 
|
| >> rbSize | O | Conditionally included for resource allocation 
type 1.<br>[TS38.214, sec 5.1.2.2.2] The number of resource block within<br>for 
this PDSCH. Value: 1->275 
|
| >> VRBtoPRBMapping | O | VRB-to-PRB-mapping [TS38.211, sec 7.3.1.6] 0: 
non-inter<br>leaved 1: interleaved with RB size 2 2: Interleaved with RB<br>size 
4 
|
| > PDSCHTimeAllocation | M | Resource Allocation in time domain [TS38.214, 
sec 5.1.2.1] 
|
| >> StartSymbolIndex | M | Start symbol index of PDSCH mapping from the 
start of the<br>slot, S. [TS38.214, Table 5.1.2.1-1]<br>Value: 0->13 
|
| >> NrOfSymbols | M | PDSCH duration in symbols, L [TS38.214, Table 
5.1.2.1-1]<br>Value: 1->14 
|
| > beamPDSCHInfo | O | Beamforming information in PDSCH 
|
| >> numPRGs | O | Number of PRGs spanning this allocation. Value: 
1->275 
|
| >> prgSize | O | Size in RBs of a precoding resource block group 
(PRG) – to<br>which same precoding and digital beamforming gets applied.<br>Value: 
1->275 
|
| >> digBFInterfaces | O | Number of STD ant ports (parallel streams) 
feeding into the<br>digBF Value: 0->255 
|
```

|

| >> prgInfo | O | For number of PRGs | | >>> PMidx | O | Index to precoding matrix (PM) pre-stored at cell configura<br>tion. Note: If precoding is not used this parameter should be set<br>to 0. Value: 0->65535. | | >>>> beamIdx | O | For each digBFInterface, |

## ![](\_page\_108\_Picture\_1.jpeg)

|

| | | Index of the digital beam weight vector prestored at cell con<br>figuration. The vector maps this input port to output TXRUs.<br>Value: 0->65535

|-------------------------|---|------------------------------------------------- -------------------------------------------------------------------------------- -----------------------------------------------------------------------------| | > TxPDSCHPower | M | Tx Power info |

| >> powerControlOffset | M | Ratio of PDSCH EPRE to NZP CSI-RSEPRE [TS38.214, sec<br>5.2.2.3.1] Value :0->23 representing -8 to 15 dB in 1dB steps,<br>as given by higher layer [TS 38.331, NZP-CSI-RS-Resource:<br>powerControlOffset] | | >> powerControlOffsetSS | O | Ratio of SSB/PBCH block EPRE to NZP CSI-RS EPRES<br>[TS38.214, sec 5.2.2.3.1] Values: 0: -3dB, 1: 0dB, 2: 3dB, 3:<br>6dB as

given by higher layer [TS 38.331, NZP-CSI-RS<br>Resource: powerControlOffsetSS ] |

#### \*\*Table 9-44 DL-SCH Configuration\*\*

### <span id="page-108-0"></span>11.2.4.3.9 UL Scheduling Information

Scheduler provides Scheduled information to MAC to enable MAC to form the UL\\_TTI.request towards L1. This is akin to a reception request towards L1 to allow L1 to receive scheduled PUSCH, PUCCH, and SRS data for a specific UE.

| Element | Presence | Description | |----------------------------------|----------|--------------------------------- -----------------------------------------| | Cell Index | M | Identification of the Cell. 2 byte integer allocated by DU | | CRNTI | M | See TS 38.331 RNTI-Value |

| Timing Information | M | Timing information for this particular message. | | Data Type | M | {PUSCH, PUSCH\_UCI, UCI, SRS, PRACH} | | PUSCH Information | O | Present if Data Type == PUSCH | | >HARQ Process ID | M | 4 bits; identifies the HARQ Process being used for this trans<br>mission | | >Frequency Domain Alloca<br>tion | M | Frequency Domain resource assignment; as defined in 38.214 | | >>resource allocation type | M | {Type-0, Type-1} from 38.214 | | >>resourceAllocationType-0 | O | Conditional presence on the resource allocation type value | | >>>rbBitMap | M | Resource allocation Type-0-bit map | | >>resourceAllocationType-1 | O | Conditional presence on the resource allocation type value | | >>>Start RB | M | Starting Resource Block for the allocation | | >>>Number of RBs | M | Number of allocated Resource Blocks | | >Time Domain Allocation | M | Specifies the time domain allocation for this transmission | | >>Start Symbol Index | M | Specifies the index of the starting symbol of the allocation | #### \*\*Table 11-56 UL Scheduling Information\*\* ![](\_page\_109\_Picture\_1.jpeg) | | | {0…13} | |----------------------------------|---|---------------------------------------- ---------------------------------------| | >>Number of Symbols | M | Specifies the number of contiguous symbols allocated for this<br>transmission | | | | {1…14} | | >TB | M | Transport Block # 1 | | >>MCS | M | {0…31} per 38.214 | | >>NDI | M | Set if New Transmission

```
|
| >>RV | M | Redundancy Version {0, 2, 3, 1} per 
38.212 |
| >>TB Size | M | Transport Block Size in Bytes {0…65535} 
|
| PUSCH_UCI | O | Present if Data Type == PUSCH_UCI 
|
| >HARQ Process ID | M | 4 bits; identifies the HARQ Process 
being used for this trans<br>mission |
| >Frequency Domain Alloca<br>tion | M | Frequency Domain resource assignment; as 
defined in 38.214 |
| >>resource allocation type | M | {Type-0, Type-1} 38.214 
|
| >>resourceAllocationType<br>0 | O | Conditional presence on the resource 
allocation type value |
| >>>rbBitMap | M | Resource allocation Type-0-bit map 
|
| >>resourceAllocationType<br>1 | O | Conditional presence on the resource 
allocation type value |
| >>>Start RB | M | Starting Resource Block for the 
allocation |
| >>>Number of RBs | M | Number of allocated Resource Blocks 
|
| >Time Domain Allocation | M | Specifies the time domain allocation 
for this transmission |
| >>Start Symbol Index | M | Specifies the index of the starting 
symbol of the allocation |
| | | {0…13} 
|
| >>Number of Symbols | M | Specifies the number of contiguous 
symbols allocated for this<br>transmission |
| | | {1…14} 
|
| >TB | M | Transport Block # 1 
|
| >>MCS | M | {0…31} per 38.214 
|
| >>NDI | M | Set if New Transmission 
|
| >>RV | M | Redundancy Version {0, 2, 3, 1} per 
38.212 |
| >>TB Size | M | Transport Block Size in Bytes {0…65535} 
|
| >HARQ_INFO | O | Present if HARQ feedback is expected
```

and is multiplexed<br>along with PUSCH |

![](\_page\_110\_Picture\_1.jpeg)

| >>HARQ\_Bits | M | Number of HARQ ACK Bits expected | |----------------------------------|---|---------------------------------------- -------------------------------------------------------------------------------- ------------------------------------| | >>betaOffsetHarqACK | M | Beta Offset for HARQ-ACK per 38.212 | | >CSI\_INFO | O | Present if CSI feedback is expected and is multiplexed along<br>with PUSCH | | >>csiBits | M | Number of CSI bits | | >>betaOffsetCSI | M | Beta Offset for CSI per 38.212 | | UCI | O | Present if Data Type == UCI | | >Frequency Domain alloca<br>tion | M | Frequency domain location of PUCCH | | >>Start RB | M | Starting Resource Block for the allocation | | >>Number of RBs | M | Number of allocated Resource Blocks | | >Time Domain Allocation | M | Specifies the time domain allocation for this transmission | | >>Start Symbol Index | M | Specifies the index of the starting symbol of the allocation | | | | {0…13} | | >>Number of Symbols | M | Specifies the number of contiguous symbols allocated for this<br>transmission | | | | {1…2} for format 0, 2 | | | | {4…14} for format 1, 3, 4 | | >SR Flag | O | Set if SR is expected in the scheduled slot

```
|
| >HARQ_INFO | O | Present if HARQ feedback is expected 
and is multiplexed<br>along with PUSCH 
|
| >>HARQ_Bits | M | Number of HARQ ACK Bits expected 
|
| >CSI_INFO | O | Present if CSI feedback is expected and 
is multiplexed along<br>with PUSCH 
|
| >>csiBits | M | Number of CSI bits 
|
| > beamPUSCHInfo | O | Beamforming information in PUSCH 
|
| >> numPRGs | O | Number of PRGs spanning this allocation. 
Value: 1->275 
|
| >> prgSize | O | Size in RBs of a precoding resource 
block group (PRG) – to<br>which same precoding and digital beamforming gets 
applied.<br>Value: 1->275 |
| >> digBFInterfaces | O | Number of STD ant ports (parallel 
streams) feeding into the<br>digBF Value: 0->255 
|
| >> prgInfo | O | For number of PRGs 
|
| >>> PMidx | O | Index to precoding matrix (PM) pre-
stored at cell configura<br>tion. Note: If precoding is not used this parameter 
should be<br>set to 0. Value: 0->65535. |
| >>>> beamIdx | O | For each digBFInterface, 
|
```

```
![](_page_111_Picture_1.jpeg)
```

|        | >pucchFormat<br>M<br>PUCCH                                                      | format<br>Value: | 0 | -> | 2       |
|--------|---------------------------------------------------------------------------------|------------------|---|----|---------|
|        | ------------------------------------------------------------------------------- |                  |   |    |         |
| --- -- |                                                                                 |                  |   |    |         |
|        |                                                                                 |                  |   |    |         |
| <br>   |                                                                                 |                  |   |    |         |
|        |                                                                                 |                  |   |    |         |
| <br>   | 0:                                                                              | PUCCH            |   |    | Format2 |
|        | 1:                                                                              | PUCCH            |   |    | Format3 |
|        |                                                                                 |                  |   |    |         |

| 2: PUCCH Format4 | | | M<br>Frequency hopping for a PUCCH resource [38.211,<br>>intraFreqHop<br>Sec | | | 6.3.2.2.1]. Valid for all formats | | | Value: | | | 0: disabled | | | 1: enabled | | | M<br>Index of the first PRB after frequency hopping.<br>>secondPrbHop | | | Valid for all formats. | | | Value:0->274 | | | >initialCyclicShift<br>M<br>Initial cyclic shift (M0) used as part of frequency. | | | hopping. [38.213, sec 9.2.1 and 38.211, sec | | | 6.3.2.2.2]. | | | Valid for formats 0, 1, 3 and 4 | | | Value: 0->11 | | | >occLen<br>M<br>The length of an orthogonal cover code. [38.211, sec | | | 6.3.2.6.3]. | | | Valid for format 4. | | | Value: 2 or 4 | | | >occIdx<br>M<br>An index of an orthogonal cover code. [38.211, sec | | | 6.3.2.6.3]. | | | Valid for format 4. | | | Value: 0->3 | |

| >timeDomOCC<br>M<br>An index of an orthogonal cover code [38.211, sec | | | 6.3.2.4.1]. | | | Valid for format 1. | | | | |

## ![](\_page\_112\_Picture\_1.jpeg)

| >addDmrsFlag | M | Flag for additional DMRS. [38.213, sec 9.2.2]. | |-------------------|---|------------------------------------------------------- ----| | | | | | | | Valid for formats 3 and 4. | | | | Value: | | | | 0 = disabled | | | | 1 = enabled | | > pi2BPSK | M | When enabled, indicates that the UE uses pi/2 BPSK<br>for | | | | UCI symbols instead of QPSK for PUCCH. | | | | [TS 38.213, sec 9.2.5] | | | | Value: 0: disabled, 1: enabled | | PRACH Information | M | Present if Data Type == PRACH | | >numPrachOcas | M | | | | | | | >prachFormat | M | | | >numRa | M | | | >prachStartSymb | M | #####################################SPEC NODE END############################ # SPEC 041: 11.2.4.3.10 RAR Information #####################################SPEC NODE START############################

## <span id="page-112-0"></span>11.2.4.3.10 RAR Information

This API is invoked by scheduler to inform MAC of uplink scheduling and Msg3 scheduling information.

| <br>Element                                                           | <br>Presence<br> <br>Description                                                |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------|
|                                                                       | ----------------------- ---------- -------------------------------------------- |
| ---------------------- <br>  Cell Index<br>  M<br>allocated by DU<br> | Identification of the Cell. 2-byte integer                                      |
| Timing Information<br>  M                                             | Timing information for this message.                                            |
| <br>  RA_RNTI<br>  M<br>                                              | RA_RNTI corresponding to the received RACH                                      |
| Number of Preambles<br>  M                                            | Number of Preambles that were received for                                      |
| the RA_RNTI<br>                                                       |                                                                                 |
| <br>>RAPID                                                            | <br>M<br> <br>Preamble<br>ID                                                    |
| <br> <br>>Timing<br>Advance<br>Value<br> <br>M<br>                    | <br>Initial<br>Timing<br>Advance                                                |
| >Start RB<br>  M                                                      | Starting Resource Block for the PUSCH                                           |
| Allocation<br>                                                        |                                                                                 |
| >Number of RBs<br>  M                                                 | Number of allocated Resource Blocks for the                                     |
| PUSCH Alloca<br>tion                                                  |                                                                                 |
| >Temporary CRNTI<br>  M                                               | Temporary CRNTI allocated by Scheduler                                          |
|                                                                       |                                                                                 |

#### \*\*Table 11-57 RAR Information\*\*

![](\_page\_113\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 042: 11.2.4.3.11 Downlink Control Channel Information #####################################SPEC NODE START############################ # <span id="page-113-0"></span>11.2.4.3.11 Downlink Control Channel Information

Scheduler provides DCI scheduling information for a given TTI on PDCCH. Scheduling information contains Coreset and Search Space resource allocation. MAC is supposed

|

| Element | Presence | Description | |----------------------------|----------|--------------------------------------- -------------------------------------------------------------------| | Frame Number | M | Time indication. Frame Number where DCI is scheduled | | Slot Number | M | Time indication. Slot Number where DCI is scheduled | | Cell Index | M | Identification of the Cell. 2-byte integer allocated by DU | | CRNTI | M | See TS 38.331 RNTI-Value | | Frequency Domain Resources | M | Frequency domain resources for the CORESET as defined in<br>38.211 section 7.3.2.2 | | Duration | M | time duration of the CORESET in number of symbols as de<br>fined in 38.211 section 7.3.2.2 | | CCE REG Mapping type | M | {interleaved, nonInterleaved}. as defined in 38.211 section<br>7.3.2.2 | | >interleaved | O | Conditional presence on the CCE REG Mapping type value | | >> reg Bundle Size | M | {2, 3, 6}. Size of REG Bundles as defined in 38.211 section<br>7.3.2.2 | | >>interleaver Size | M | {2, 3, 6}. Interleaver Size as defined in 38.211 section 7.3.2.2 | | >>shift Index | M | shiftIndex or Physical Cell Id as defined in 38.211 section<br>7.3.2.2 | | Search Space Start Symbol | M | first symbol for PDCCH monitoring in the slot; as defined in<br>38.213 section 10.1. | | CCE Index | M | First CCE index in the aggregation level as defined in 38.211<br>section 7.3.2.2 | | Aggregation Level | M | {1,2,4,8,16}. as defined in 38.213 Table 10.1-1 | | Precoder Granularity | M | {sameAsRegBundle, allContigousRBs}; as defined in 38.211<br>section 7.3.2.2 | | PDCCH Power Offset | M | -8 to 8 dB in 1dB steps. SSB/PBCH EPRE to PDCCH and<br>PDCCH DMRS EPRE; as defined in 38.213 section 4.1 | | DCI Format type | M | {format\_0\_0, format\_0\_1, format\_1\_0, format\_1\_1}; as de<br>fined in 38.212 section 7.3.1 | | > Format\_1\_0 | O | Conditional presence on the DCI Format type value | | >>VRB to PRB Map<br>ping | M | Physical resource block Bundling as

to prepare the DCI payload with the Downlink control channel information and DL/UL Scheduling Information Frequency and Time Domain allocation for the UE.

defined in 38.214 section<br>5.1.2.3 | | >>DAI | M | Downlink Assignment Index as defined in as defined in 38.213<br>section 9.1.2 | | >> TPC Command | M | PUCCH TPC as defined in 38.213 section 7.2.1 |

#### \*\*Table 11-58 Downlink Control Channel Information\*\*

### ![](\_page\_114\_Picture\_1.jpeg)

| >>PUCCH Resource In<br>dicator | M | Resource for reporting HARQ-ACK as defined in 38.213 sec<br>tion 9.2.3 | |---------------------------------------------------|---|----------------------- -------------------------------------------------------------------------------- --------------------------------------------------------| | >> PDSCH to Harq<br>Feedback Timing In<br>dicaor | M | Timing for reporting HARQ-ACK as defined in 38.213 section<br>9.2.3 | | > Format\_1\_1 | O | Conditional presence on the DCI Format type value | | >>Carrier Indicator | O | Conditional presence on CrossCarrierSchedulingConfig sup<br>port; as defined in 38.213 section 10.1 | | >>BWP Indicator | O | Conditional presence on dedicated DL BWP Config; as defined<br>in 38.213 section 12 | | >>VRB to PRB Map<br>ping | O | Conditional presence on RAT type and interleaved VRB-to<br>PRB mapping configuration.Physical resource block Bundling<br>as defined in 38.214 section 5.1.2.3 | | >>PRB bundling size<br>indicator | O | Conditional presence on prb-BundlingType; as defined in<br>38.214 section 5.1.2.3 | | >> Rate Matching Indi<br>cator | O | Conditional presence on rateMatchPatternGroup Config; as de<br>fined in 38.214 section 5.1.4.1 | | >>ZP CSI-RS trigger | O | Conditional presence on zp-CSI-RS-Resource Config; as de<br>fined in 38.214 section 5.1.4.2 | | >>DAI | O | Downlink Assignment Index as defined in as defined in 38.213<br>section 9.1.2 | | >> TPC Command | M | PUCCH TPC as defined in 38.213 section 7.2.1 | | >>PUCCH Resource In<br>dicator | M | Resource for reporting HARQ-ACK as defined in 38.213 sec<br>tion 9.2.3 | | >> PDSCH to HARQ<br>Feedback Timing Indi<br>cator | O | Timing for reporting HARQ-ACK as defined in 38.213 section<br>9.2.3 | | >> Transmission config<br>uration indication | O | Conditional presence on tci-PresentInDCI Config as defined in<br>38.214 section 5.1.5 | | >> SRS Request | M | Request for SRS Reporting as defined in 38.212 Table<br>7.3.1.1.2-24 | | >>CBG transmission in<br>formation | O | Conditional presence on Max CBG per TB config as defined in<br>38.214 section 5.1.7 | | >>CBG flushing out in<br>formation | O | Conditional presence on CBG Flush Indicator config as de<br>fined in 38.214 section 5.1.7 | | >>DMRS sequence ini<br>tialization | M | DM-RS sequence initialization field as defined in 38.211 sec<br>tion 7.4.1.1.1 | | > Format\_0\_0 | O | Conditional presence on the DCI Format type value | | >>PUSCH Hopping | O | Conditional presence on Frequency Hopping offset Config; as<br>defined in 38.214 section 6.3 | ![](\_page\_115\_Picture\_1.jpeg) | >>Frequency Hopping<br>Flag | M | PUSCH Frequency Hopping as defined in 38.214 section 6.3 | |-----------------------------------------------------|---|--------------------- -------------------------------------------------------------------------------- ----------------------------------------------------| | >>TPC Command | M | PUSCH TPC value as defined in 38.213 section 7.1 | | >>UL/SUL Indicator | O | Conditional Presence based on supplementaryUplink; as de<br>fined in 38.331 ServingCellConfig |

| > Format\_0\_1 | O | Conditional presence on the DCI Format type value | | >>Carrier Indicator | O | Conditional presence on Cross Carrier Scheduling Config sup<br>port; as defined in 38.213 section 10.1 | | >>UL/SUL Indicator | O | Conditional Presence based on supplementaryUplink; as de<br>fined in 38.331 ServingCellConfig | | >>BWP Indicator | O | Conditional presence on dedicated UL BWP Config; as defined<br>in 38.213 section 12 | | >>PUSCH Hopping | O | Conditional presence for RAT1 on Frequency Hopping offset<br>Config; as defined in 38.214 section 6.3 | | >>Frequency Hopping<br>Flag | O | Conditional presence for RAT1 as defined in 38.214 section<br>6.3 | | >>TPC Command | M | PUSCH TPC value as defined in 38.213 section 7.1 | | >>SRS Resource Indi<br>cator | O | Conditional presence on SRS Resource Config; as defined in<br>38.331 PUSCH-Config and 38.212 Table 7.3.1.1.2- 28 to<br>7.3.1.1.2-32 | | >>Precoding Infor<br>mation and Number of<br>Layers | O | Conditional presence on txConfig and antenna ports configura<br>tion; as defined in 38.331 PUSCH-Config and 38.212 Table<br>7.3.1.1.2- 2 to 7.3.1.1.2-5 | | >> SRS Request | M | Request for SRS Reporting as defined in 38.212 Table<br>7.3.1.1.2-24 | | >>CSI request | O | Conditional presence on report Trigger Size configuration as<br>defined in 38.331 CSI-MeasConfig | | >>CBG transmission in<br>formation | O | Conditional presence on Max CBG per TB config as defined in<br>38.214 section 5.1.7 | | >>Beta Offset Indicator | O | Conditional presence on betaOffsets configuration as defined<br>in 38.213 | | >>DMRS Sequence Ini<br>tialization | O | Conditional presence on transform Precoding; as defined in<br>38.211 section 6.4.1.1.1 | | >>UL SCH Indicator | M | UL SCH transmitted on PUSCH or not. ### <span id="page-115-0"></span>11.2.4.3.12 Downlink Broadcast Allocation

Scheduler provides DCI and DL data scheduling information for SSB and System Information Block1 and Other System Information for a given TTI for Broadcast Channel. MAC forms the SSB and SI payload.

#### \*\*Table 11-59 Downlink Broadcast Allocation\*\*

| Element<br>Presence   Description   |  |
|-------------------------------------|--|
| --------------------- ------------- |  |
| --------------------- ------------- |  |

![](\_page\_116\_Picture\_1.jpeg)

| Cell Index | M | Identification of the Cell. 2-byte integer allocated by DU | | |-----------------------------------|---|--------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ---------------------------------------------------------|--| | Frame Number | M | Time indication. Frame Number where Broadcast data is<br>scheduled | | | Slot Number | M | Time indication. Slot Number where Broadcast data is sched<br>uled | | | SSB Index | M | Index of SSB corresponding to the Broadcast data; For SIB1 as<br>defined in 38.213 section 13. For other SI as defined in 38.331<br>section 5.2.2.3.2 | | | DL DCI | O | Specifies the DL DCI Coreset and Search Space for Schedul<br>ing DCI for Broadcast data. | | | DL SCH | O | Specifies the DL PDSCH for Broadcast data. | | | >System information indi<br>cator | M | {0 – 1}. Specifies SIB1 or SI message; as defined in 38.212<br>Table 7.3.1.2.1-2 | | | >SI Content | M | Byte Array [MAX\_BYTES\_FOR\_SI]; this carries the ASN.1<br>encoded System Information Messages that Scheduler wants

|

```
to<br>transmit to the UE; as defined in 38.331 SIB1 or SystemInfor<br>mation. 
Maximum TB size is 2976 bytes as per 38.214 section<br>5.1.3.2 | |
| SSB Information | O | Carries the SSB Information 
| |
| >ssbSubcarrierOffset | M | kssb<br>as per 38.211 
| |
| >ssbOffsetPointA | M | Offset of the lowest RB per 38.211 
| |
```

## #### \*\*Table 11-60 DL DCI Information\*\*

```
| Element | Presence | Description 
| |
|---------------------------------|----------|----------------------------------
--------------------------------------------------------------------------------
------------|--|
| DL DCI | M | Specifies the DL DCI Coreset and 
Search Space for Schedul<br>ing DCI for Broadcast data. 
| |
| >Frequency Domain Re<br>sources | M | Frequency domain resources for 
the CORESET as defined in<br>38.211 section 7.3.2.2 
| |
| >duration | M | time duration of the CORESET in 
number of symbols as de<br>fined in 38.211 section 7.3.2.2 
| |
| >CCE REG Mapping type | M | {interleaved, nonInterleaved}. 
For SIB1 only interleaved map<br>ping type is applicable as defined in 38.211 
section 7.3.2.2 | |
| >>interleaved | O | Conditional presence on the CCE 
REG Mapping type value 
| |
| >>> reg Bundle Size | M | {2, 3, 6}. Size of REG Bundles as 
defined in 38.211 section<br>7.3.2.2 
| |
| >>>interleaver Size | M | {2, 3, 6}. Interleaver Size as 
defined in 38.211 section 7.3.2.2 
| |
| >>>shift Index | M | shiftIndex or Physical Cell Id as 
defined in 38.211 section<br>7.3.2.2 
| |
| >Search Space Start Sym<br>bol | M | monitoringSymbolsWithinSlot. For 
SIB1 as defined in 38.213<br>section 13. For other SI as defined in 38.213 section 
10.1. | |
```

![](\_page\_117\_Picture\_1.jpeg)

| > CCE Index | M | First CCE index in the aggregation level as defined in 38.211<br>section 7.3.2.2 | |------------------------|---|-------------------------------------------------- --------------------------------------------------------| | >Aggregation Level | M | {4,8,16}. as defined in 38.213 Table 10.1-1 | | > Precoder Granularity | M | {sameAsRegBundle, allContigousRBs} as defined in 38.211<br>section 7.3.2.2 | | >pdcch Power Offset | M | -8 to 8 dB in 1dB steps. SSB/PBCH EPRE to PDCCH and<br>PDCCH DMRS EPRE; as defined in 38.213 section 4.1 | #### \*\*Table 11-61 DL SCH Information\*\* | Element | Presence | Description | | |----------------------------------|----------|--------------------------------- -------------------------------------------------------------------------------- ----------------------------------------|--| | DL SCH | O | Conditional presence on Short Message Indicator value. Pre<br>sent in case Short Message Indicator is 1 or 3; as defined in<br>38.212 Table 7.3.1.2.1-1 | | | >Frequency Domain Allo<br>cation | M | RAT1 Frequency Domain resource assignment; as defined in<br>38.214 section 5.1.2.2.2 | | | >>Start RB | M | Starting Resource Block for the allocation | | | >>Number of RBs | M | Number of allocated Resource Blocks | | | >Time Domain Allocation | M | Specifies the time domain allocation for this transmission; as<br>defined in 38.214 section 5.1.2.1 | | | >>Mapping Type | M | {typeA, typeB} | | | >>Start Symbol Index | M | Specifies the index of the starting symbol of the allocation | | | | | {0…13} | | | >>Number of Symbols | M | Specifies the number of contiguous symbols allocated for this<br>transmission | | | | | {1…14} | | | >DMRS Config | M | Specifies downlink demodulation reference signals for<br>PDSCH; as defined in 38.214 section 5.1.6.2 | | | >>DMRS Type | M | DMRS type to be used for DL | | | >>DMRS Additional<br>Pos | M | Position for additional DM-RS in DL | | | >>Max Length | M | The maximum number of OFDM symbols for DL front loaded<br>DMRS | | | >VRB-to-PRB mapping | M | Specifies Non-Interleaved or Interleaved VRB-to-PRB map<br>ping; as defined in 38.214 section 5.1.2.3. | | | >TB | M | Transport Block as defined in 38.214 section 5.1.3. | | | >>MCS | M | {0…9} | | | >>TB Size | M | Transport Block Size in Bytes | |

![](\_page\_118\_Picture\_1.jpeg)

| >TB Scaling | M | Scaling factor {0 – 2} as defined in 38.214 section 5.1.3.2. | |-------------|---|------------------------------------------------------------- -| | | | |

### <span id="page-118-0"></span>11.2.4.3.13 Downlink Paging Allocation

Scheduler provides DCI and optionally DL data scheduling information for Paging Message for given TTI for Paging Channel.

| Element | Presence | Description | | |---------------------------------|----------|---------------------------------- ------------------------------------------------------------------|--| | Cell Index | M | Identification of the Cell. 2byte integer allocated by DU | | | Frame Number | M | Time indication. Frame Number where Paging data is sched<br>uled | | | Slot Number | M | Time indication. Slot Number where Paging data is scheduled | | | SSB Index | M | Index of SSB corresponding to the Paging data; as defined in<br>38.304 section 7.1 | | | Short Message Indicator | M | {0-3}; as defined in 38.212 Table 7.3.1.2.1-1: Short Message<br>indicator | | | Short Message | O | 8 bits; as defined in 38.331 section 6.5. Conditional presence<br>on Short Message Indicator value | | | DL DCI | M | Specifies the DL DCI Coreset and Search Space for Schedul<br>ing DCI for Paging data. | | | >Frequency Domain Re<br>sources | M | Frequency domain resources for the CORESET as defined in<br>38.211 section 7.3.2.2 | | | >Duration | M | time duration of the CORESET in number of symbols as de<br>fined in 38.211 section 7.3.2.2 | | | >CCE REG Mapping type | M | {interleaved, nonInterleaved}; as defined in 38.211 section<br>7.3.2.2 | | | >>interleaved | O | Conditional presence on the CCE REG Mapping type value | | | >>> reg Bundle Size | M | {2, 3, 6}. Size of REG Bundles as defined in 38.211 section<br>7.3.2.2 | | | >>>interleaver Size | M | {2, 3, 6}. Interleaver Size as defined in 38.211 section 7.3.2.2 | | | >>>shift Index | M | shiftIndex or Physical Cell Id as defined in 38.211 section<br>7.3.2.2 | | | >Search Space Start Sym<br>bol | M | monitoringSymbolsWithinSlot as defined in 38.213 section<br>10.1. | | | > CCE Index | M | First CCE index in the aggregation level as defined in 38.211<br>section 7.3.2.2 | | | >Aggregation Level | M | {4,8,16}. as defined in 38.213 Table 10.1-1 | |

\*\*Table 11-62 Downlink Paging Allocation\*\*

![](\_page\_119\_Picture\_1.jpeg)

| > Precoder Granularity |                                                                                  |  |                   | M   {sameAsRegBundle, allContigousRBs} as |         |  |
|------------------------|----------------------------------------------------------------------------------|--|-------------------|-------------------------------------------|---------|--|
| defined                | in                                                                               |  | 38.211<br>section |                                           | 7.3.2.2 |  |
|                        |                                                                                  |  |                   |                                           |         |  |
|                        | ---------------------------------- --- ----------------------------------------  |  |                   |                                           |         |  |
|                        | -------------------------------------------------------------------------------- |  |                   |                                           |         |  |
|                        | ------------------------------------------ --                                    |  |                   |                                           |         |  |

```
| >PDCCH Power Offset | M | -8 to 8 dB in 1dB steps. SSB/PBCH EPRE 
to PDCCH and<br>PDCCH DMRS EPRE; as defined in 38.213 section 4.1 
| |
| DL SCH | O | Conditional presence on Short Message 
Indicator value. Pre<br>sent in case Short Message Indicator is 1 or 3; as defined 
in<br>38.212 Table 7.3.1.2.1-1 | |
| >Frequency Domain Allo<br>cation | M | RAT1 Frequency Domain resource assignment; 
as defined in<br>38.214 section 5.1.2.2.2 
| |
| >>Start RB | M | Starting Resource Block for the 
allocation 
| |
| >>Number of RBs | M | Number of allocated Resource Blocks 
| |
| >Time Domain Allocation | M | Specifies the time domain allocation 
for this transmission; as<br>defined in 38.214 section 5.1.2.1 
| |
| >>Mapping Type | M | {typeA, typeB} 
| |
| >>Start Symbol Index | M | Specifies the index of the starting 
symbol of the allocation 
| |
| | | {0…13} 
| |
| >>Number of Symbols | M | Specifies the number of contiguous 
symbols allocated for this<br>transmission 
| |
| | | {1…14} 
| |
| >DMRS Config | M | Specifies downlink demodulation 
reference signals for<br>PDSCH; as defined in 38.214 section 5.1.6.2 
| |
| >>DMRS Type | M | DMRS type to be used for DL 
| |
| >>DMRS Additional<br>Pos | M | Position for additional DM-RS in DL 
| |
| >>Max Length | M | The maximum number of OFDM symbols for 
DL front loaded<br>DMRS 
| |
| >VRB-to-PRB mapping | M | Specifies Non-Interleaved or Interleaved 
VRB-to-PRB map<br>ping; as defined in 38.214 section 5.1.2.3. 
| |
| >TB | M | Transport Block as defined in 38.214 
section 5.1.3.
```

```
| |
| >>MCS | M | {0…9} 
| |
| >>TB Size | M | Transport Block Size in Bytes 
| |
| >TB Scaling | M | Scaling factor {0 – 2} as defined in 
38.214 section 5.1.3.2. 
| |
| >Paging Content | M | Byte Array [MAX_BYTES_FOR_PAGING]; this 
carries the<br>ASN.1 encoded Paging Messages that Scheduler wants to<br>transmit
```

to the UE's as defined in 38.331 Paging | |

#####################################SPEC NODE END############################ # SPEC 043: 11.2.4.3.14 Downlink HARQ Release #####################################SPEC NODE START############################

# <span id="page-119-0"></span>11.2.4.3.14 Downlink HARQ Release

Scheduler informs MAC to release the HARQ process when HARQ feedback is failure and max transmission Per Haq has reached.

![](\_page\_120\_Picture\_1.jpeg)

| <br>Element<br>                                                                 |         |        |   | Presence |        | Description                                |
|---------------------------------------------------------------------------------|---------|--------|---|----------|--------|--------------------------------------------|
| ------------------- ---------- ------------------------------------------------ |         |        |   |          |        |                                            |
| ------------                                                                    |         |        |   |          |        |                                            |
| Cell Index                                                                      | M       |        |   |          |        | Identification of the Cell. 2-byte integer |
| allocated by DU                                                                 |         |        |   |          |        |                                            |
| Num of UEs                                                                      | M       |        |   |          |        | Number of UEs whose Harq processes must be |
| released<br>                                                                    |         |        |   |          |        |                                            |
| <br>Ue<br>HarqInfo                                                              |         |        |   |          |        |                                            |
|                                                                                 |         |        |   |          |        |                                            |
| <br>><br>CRNTI                                                                  |         |        | M |          | <br>UE | Identifier                                 |
|                                                                                 |         |        |   |          |        |                                            |
| <br>><br>Harq<br>                                                               | Process | ID<br> | M |          |        |                                            |
|                                                                                 |         |        |   |          |        |                                            |

#### \*\*Table 11-63 Downlink HARQ Release\*\*

#####################################SPEC NODE END############################ # SPEC 044: 11.2.5 F1AP handler – MAC Interface #####################################SPEC NODE START############################ ## <span id="page-120-0"></span>11.2.5 F1AP handler – MAC Interface

The following section captures the interface APIs between F1AP handler and MAC:

#### \*\*Table 11-64 F1AP handler –MAC Cell Specific API\*\*

\*\*Note:\*\* Cell State Manager in the F1AP module interfacing with MAC

| <br>Direction<br>                                                                                                                                                   |  | Message/API |  | Description |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|-------------|--|-------------|
| --------------------- ------------- -------------------------------------------<br>-------------------------------------------------------------------------------- |  |             |  |             |
| --------------------------------------------------------------------------------                                                                                    |  |             |  |             |
| --------------------------------------------------------------------------------<br>----------------------------------------------------------------                |  |             |  |             |

| F1AP handler to MAC | Cell Start | This API is used to start the Cell at MAC, i.e., to start<br>broadcasting the system information. MAC starts the cell<br>at L1 before sending the confirmation to the F1AP han<br>dler. |

| F1AP handler to MAC | Cell Stop | This API is used to stop the broadcast at MAC, i.e., to<br>stop broadcasting the system information. MAC stops the<br>cell at L1 before sending the confirmation to the F1AP<br>handler. MAC may also delete the cell configuration at<br>SCH in which case it needs to configure the SCH with<br>stored cell configuration before the start of the cell. |

#### \*\*Table 11-65 F1AP handler –MAC UE Specific API\*\*

Note: UE State Manager in the F1AP module interfacing with MAC will be the module interacting with MAC for the following APIs.

| Direction    |               | Message/API                              |                                                                                    |                     | Description          |
|--------------|---------------|------------------------------------------|------------------------------------------------------------------------------------|---------------------|----------------------|
|              |               |                                          |                                                                                    |                     |                      |
|              |               |                                          | --------------------- --------------------------------- -----------------------    |                     |                      |
|              |               |                                          | --------------------------------------------------------------------------------   |                     |                      |
|              |               |                                          | --------------------------------------------------------------------------         |                     |                      |
|              |               | F1AP handler to MAC   UE Create Request  |                                                                                    |                     | This API adds the UE |
| information, | such<br>as,   | BWP,<br>chan<br>nel                      | information,                                                                       | etc,                | at<br>MAC.           |
|              |               |                                          |                                                                                    |                     |                      |
|              |               | MAC to F1AP handler   UE Create Response |                                                                                    |                     | This API is used to  |
| acknowledge  | the           | status<br>of                             | the                                                                                | UE<br>Create        | Request.             |
|              |               |                                          |                                                                                    |                     |                      |
|              |               |                                          | F1AP handler to MAC   UE Reconfiguration Re<br>quest                               |                     | This API is used to  |
|              |               |                                          | reconfigure the UE information, such<br>as, BWP, channel information, etc, at MAC. |                     |                      |
|              |               |                                          | MAC re<br>turns an error if the UE has not been already added at<br>MAC.           |                     |                      |
|              |               |                                          | MAC to F1AP handler   UE Reconfiguration Re<br>sponse   This API is used to        |                     |                      |
| acknowledge  | the<br>status | of<br>the                                | UE                                                                                 | Re<br>configuration | Response.            |

|

![](\_page\_121\_Picture\_1.jpeg)

| F1AP handler to MAC | UE Delete Request | This API is used to delete the dedicated UE information<br>at MAC | |---------------------|---------------------------|----------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ---------------------------------------------------------------| | MAC to F1AP handler | UE Delete Response | This API is used to acknowledge the status of the UE De<br>lete Request. | | F1AP handler to MAC | RACH Resource Request | This API is used to get the CRNTI, preamble information<br>from MAC for Contention Free Random Access | | F1AP handler to MAC | RACH Resource Release | This API is used to release the Contention Free RACH<br>Resources at MAC | | F1AP handler to MAC | UE Reset Request | This API is used to reset the UE associated dynamic in<br>formation (eg: HARQ processes) and release the UL<br>Control channels (PUCCH, SRS) at MAC. MAC may<br>use invoke the API at SCH to release the UE associated<br>resources, as above, at the SCH. | | MAC to F1AP handler | UE Reset Response | This API is used to ack the UE context reset. | | MAC to F1AP handler | UE Sync Status Indication | This API is sent from MAC to F1AP to inform the sync<br>status of UE at MAC. | #### \*\*Table 11-66 F1AP handler –MAC Channels Specific API\*\* Note: UE State Manager in the F1AP module interfacing with MAC | Direction | Message/API | Description | |---------------------|----------------------|---------------------------------- -------------------------------------------------------------------------------- ----------------------------------------------------------------------| | MAC to F1AP handler | UL CCCH Indication | This API is sent from MAC to F1AP

to pass the UL<br>CCCH message received from UE. Cell id where CCCH<br>message is received is sent to F1AP. This API is required<br>for SA mode only | | F1AP handler to MAC | DL CCCH Indication | This API is sent from F1AP to MAC to send the DL<br>CCCH message to UE with Cell id on which the message<br>is to be transmitted. This API is required for SA mode<br>only. | | F1AP handler to MAC | DL PCCH Indication | This API is sent from F1AP to MAC to broadcast the DL<br>PCCH message in the cell. This API is required for SA<br>mode only. | | F1AP handler to MAC | DL Broadcast Request | This API is sent from F1AP to MAC the SIB messages in<br>the cell. |

The detailed description of the APIs is below:

### <span id="page-121-0"></span>11.2.5.1.1 Cell Start

#### \*\*Table 11-67 F1AP handler –MAC Cell Start message contents\*\*

| Element          |   | Presence   Description<br>                             |
|------------------|---|--------------------------------------------------------|
|                  |   | -------------- ---------- ---------------------------- |
| Cell Index       | M | Identification of the Cell                             |
| Frame Number   O |   | Start time<br>                                         |

![](\_page\_122\_Picture\_1.jpeg)

|  | Slot Number   O   Start time   |  |  |
|--|--------------------------------|--|--|
|  | ------------- --- ------------ |  |  |

### <span id="page-122-0"></span>11.2.5.1.2 Cell Stop

#### \*\*Table 11-68 F1AP handler –MAC Cell Stop message contents\*\*

| Element          |   | Presence   Description<br>                             |  |
|------------------|---|--------------------------------------------------------|--|
|                  |   | -------------- ---------- ---------------------------- |  |
| Cell Index       | M | Identification of the Cell                             |  |
| Frame Number   O |   | Stop time<br>                                          |  |
| Slot Number   O  |   | Stop time<br>                                          |  |

### <span id="page-122-1"></span>11.2.5.1.3 Cell Delete Request

DUAPP send this to MAC to delete a cell, this API is invoked.

#### \*\*Table 11-69 Cell Start Delete Request\*\*

|  | Element |                                                                                 | Presence<br> <br>Description |  |
|--|---------|---------------------------------------------------------------------------------|------------------------------|--|
|  |         |                                                                                 |                              |  |
|  |         | ----------------- ---------- -------------------------------------------------- |                              |  |

----------| | Debug Time Info | O | This is an optional IE and may be provided on availability | | Cell Index | M | Identification of the Cell. 2-byte integer allocated by DU |

### <span id="page-122-2"></span>11.2.5.1.4 Cell Delete Response

This API is invoked by scheduler to respond to a Cell Deletion request.

#### \*\*Table 11-70 Cell Delete Response\*\*

| <br>Element                                                                          |   |                                                      |                                                | Presence                     |            | Description |
|--------------------------------------------------------------------------------------|---|------------------------------------------------------|------------------------------------------------|------------------------------|------------|-------------|
| <br> ------------- ---------- ------------------------------------------------------ |   |                                                      |                                                |                              |            |             |
| -------------- <br>  Cell Index   M                                                  |   | Identification of the Cell. 2-byte integer allocated |                                                |                              |            |             |
| by DU<br> <br>  Response                                                             | M | Response that maybe used to identify failure/success |                                                |                              |            |             |
|                                                                                      |   |                                                      |                                                |                              |            |             |
|                                                                                      |   |                                                      |                                                |                              | OK<br>–    | Success     |
| <br> <br>                                                                            |   |                                                      |                                                |                              | NOK<br>–   | Failure     |
| <br>Error<br>Cause<br> <br>O<br> <br>If<br>Response<br>==<br>                        |   |                                                      |                                                | NOK                          |            |             |
|                                                                                      |   |                                                      | This field describes the cause of the failure. |                              |            |             |
| <br> <br>                                                                            |   |                                                      |                                                |                              | <br>Value: | ENUM        |
| <br>UEID_INVALID,<br>RESOURCE_UNAVAILABLE                                            |   |                                                      |                                                | {SUCCESSFUL, CELLID_INVALID, |            |             |

#####################################SPEC NODE END############################ # SPEC 045: 11.2.5.1.5 Slice Configuration Request #####################################SPEC NODE START############################ ## <span id="page-122-3"></span>11.2.5.1.5 Slice Configuration Request

Slice Configuration Request is sent to configure the MAC/Scheduler with the rRMPolicyRatio for each of the slices supported in the cell.

![](\_page\_123\_Picture\_1.jpeg)

| Element | Presence | Description

| |--------------------------------|----------|----------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ------------| | RRMPolicyList | | List of RRM policies received from O1. | | ResourceType | | For ODU, only PRB will be relevant resource to apply RRM policy on. | | | | Value: PRB, DRB, RRC\_CONNECTED\_USERS. | | RRMPolicyMemberList | | This defines the list of S-NSSAIs and PLMN belonging to the cell.<br>This is to be included if network slicing is supported. | | > S-NSSAI | M | Identification of the slice. | | >PLMN | M | |

| RRMPolicyRatio | M | rRMPolicy for the slice if network slicing feature is supported. This<br>policy is for the resource type "PRB" and applicable to gNB-DU. The<br>other resource type " DRB" and "RRCConnected" are applicable to<br>gNB-CU.

|

| >> rRMPolicyMaxRatio | uint8\_t | This attribute specifies the maximum percentage of radio resource that<br>can be used by the associated rRMPolicyMemberList/SNSSAI. The<br>maximum percentage of radio resource include at least one of the<br>shared resources, prioritized resources and dedicated resources. The<br>sum of the rRMPolicyMaxRatio values assigned to all slices can be<br>greater than 100. |

| >> rRMPolicyMinRatio | uint8\_t | This attribute specifies the minimum percentage of radio resources that<br>can be used by the associated rRMPolicyMemberList/sNSSAI. The<br>minimum percentage of radio resources including at least one of priori<br>tized resources and dedicated resources. The sum of the rRMPoli<br>cyMinRatio values assigned to all slices be less than or equal to100. |

| >> rRMPolicyDedicat<br>edRatio | uint8\_t | This attribute specifies the percentage of radio resource that dedicat<br>edly used by the associated rRMPolicyMemberList/sNSSAI. The sum<br>of the rRMPolicyDeidctaedRatio values assigned to all slices be less<br>than or equal to100. |

#### \*\*Table 11-71 Slice Configuration Request\*\*

### <span id="page-123-0"></span>11.2.5.1.6 Slice Configuration Response

This Status is sent for each SNSSAI whether the policy sent via Slice Configuration Request has been applied or not.

#### \*\*Table 11-72 Slice Configuration Response\*\*

![](_page_162_Figure_5.jpeg)

![](\_page\_124\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 046: 11.2.5.1.7 Slice ReConfiguration Request #####################################SPEC NODE START############################ ## <span id="page-124-0"></span>11.2.5.1.7 Slice ReConfiguration Request

Slice Configuration Request is sent to configure the MAC/Scheduler with the rRMPolicyRatio for each of the slices supported in the cell.

| Element       |  | Presence   Description                                                                                                                                               |
|---------------|--|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               |  |                                                                                                                                                                      |
|               |  | -------------------------------- ---------- -----------------------------------                                                                                      |
|               |  | --------------------------------------------------------------------------------                                                                                     |
|               |  | --------------------------------------------------------------------------------<br>-------------------------------------------------------------------------------- |
|               |  | --------------------------------------------------------------------------------                                                                                     |
| ------------  |  |                                                                                                                                                                      |
| RRMPolicyList |  | List of RRM policies received from                                                                                                                                   |
| O1.           |  |                                                                                                                                                                      |
|               |  |                                                                                                                                                                      |

| ResouceType | | For ODU, only PRB will be relevant resource to apply RRM policy on. | | | | Value: PRB, DRB, RRC\_CONNECTED\_USERS. | | RRMPolicyMemberList | | This defines the list of S-NSSAIs and PLMN belonging to the cell.<br>This is to be included if network slicing is supported. | | > S-NSSAI | M | Identification of the slice. |

| >PLMN | M |

| RRMPolicyRatio | M | rRMPolicy for the slice if network slicing feature is supported. This<br>policy is for the resource type "PRB" and applicable to gNB-DU. The<br>other resource type " DRB" and "RRCConnected" are applicable to<br>gNB-CU.

| >> rRMPolicyMaxRatio | uint8\_t | This attribute specifies the maximum percentage of radio resource that<br>can be used by the associated rRMPolicyMemberList/SNSSAI. The<br>maximum percentage of radio resource include at least one of the<br>shared resources, prioritized resources and dedicated resources. The<br>sum of the rRMPolicyMaxRatio values assigned to all slices can be<br>greater than 100. |

| >> rRMPolicyMinRatio | uint8\_t | This attribute specifies the minimum percentage of radio resources that<br>can be used by the associated rRMPolicyMemberList/sNSSAI. The<br>minimum percentage of radio resources including at least one of priori<br>tized resources and dedicated resources. The sum of the rRMPoli<br>cyMinRatio values assigned to all slices be less than or equal to100. |

| >> rRMPolicyDedicat<br>edRatio | uint8\_t | This attribute specifies the percentage of radio resource that dedicat<br>edly used by the associated rRMPolicyMemberList/sNSSAI. The sum<br>of the rRMPolicyDeidctaedRatio values assigned to all slices be less<br>than or equal to100. |

#### \*\*Table 11-73 Slice Reconfiguration Request\*\*

|

|

### <span id="page-124-1"></span>11.2.5.1.8 Slice ReConfiguration Response

This Status is sent for each SNSSAI whether the policy sent via Slice ReConfiguration Request has been applied or not.

| Element | Presence | Description | |---------|----------|---------------------------------------------------------- -------------| | SNSSAI | | | | Status | M | Value: OK, FAILURE | | Cause | M | Value: Cell\_id, ueId\_value, Re<br>source\_unavilable, Slice\_not\_found. |

\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_

#### \*\*Table 11-74 Slice Reconfiguration Response\*\*

![](\_page\_125\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 047: 11.2.5.1.9 UE Create Request #####################################SPEC NODE START############################ ## <span id="page-125-0"></span>11.2.5.1.9 UE Create Request

#### \*\*Table 11-75 F1AP handler - MAC UE Create Request message contents\*\*

|   |                                                                                                                                                                     |      | Element       |
|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|---------------|
|   | Presence   Description                                                                                                                                              |      |               |
|   | -------------------------------------------------------------------------------<br>-------------------------------------------- ---------- ------------------------ |      |               |
|   | -------------------------------------------                                                                                                                         |      |               |
|   | Debug                                                                                                                                                               | Time | Info          |
| O | This is an optional IE and may be<br>provided on availability                                                                                                       |      |               |
|   | Cell                                                                                                                                                                |      | Index         |
| M | Identification of the Cell. 2-byte in<br>teger allocated by F1AP                                                                                                    |      |               |
|   | UE                                                                                                                                                                  |      | Index         |
| M | Identification of the UE. 2-byte in<br>teger allocated by F1AP                                                                                                      |      |               |
|   |                                                                                                                                                                     |      | CRNTI         |
| M | See TS 38.331 RNTI-Value. Allo<br>cated by MAC.                                                                                                                     |      |               |
|   |                                                                                                                                                                     |      |               |
|   | CRNTI is included only in case of<br>SA                                                                                                                             |      |               |
|   | mac-CellGroupConfig (schedulingRequestCon<br>fig, tag-Config, phr-Config,bsr                                                                                        |      |               |
|   | config, drx-con<br>fig)                                                                                                                                             | M    | See TS 38.331 |
|   | MAC<br>CellGroupConfig                                                                                                                                              |      |               |

| physicalCellGroupConfig (pdsch-HARQ-ACK<br>Codebook, p-NR-FR1) | M | See TS 38.331 PhysicalCellGroup<br>Config | | spCellConfig | M | See TS 38.331 SpCellConfig | | >servCellIndex | M | See TS 38.331 ServCellIndex | | >ServingCellConfigInfo | M | See TS 38.331 ServingCellConfig | | >>initialDownlinkBWP (pdcch-Config,<br>pdsch-Config) | M | See TS 38.331 BWP<br>DownlinkDedicated in ServingCell<br>Config. | | >>Number of DL BWP To Add | M | The number of dedicated DL BWP<br>To Add | | >>DownlinkBWP-ToAddModList (bwp<br>Id, bwp-Common, bwp-Dedicated) | M | See TS 38.331 BWP-Downlink in<br>ServingCellConfig | | >>firstActiveDownlinkBWP-Id | M | See TS 38.331 ServingCellConfig | | >>defaultDownlinkBWP-Id | M | See TS 38.331 ServingCellConfig | | >>bwp-InactivityTimer | M | See TS 38.331 ServingCellConfig | | >>PDSCH-ServingCellConfig (max<br>MIMO-Layers, nrofHARQ-Process<br>esForPDSCH, codeBlockGroupTransmis<br>sion, xOverhead) | M | See TS 38.331 PDSCH<br>ServingCellConfig in ServingCell<br>Config | | >>initialUplinkBWP (pucch-Config,<br>pusch-Config) | M | See TS 38.331 BWP<br>UplinkDedicated in ServingCell<br>Config | | >>Number of UL BWP To Add | M | The number of UL BWP To Add |

| >>uplinkBWP-ToAddModList (bwp-Id,<br>M<br>See TS 38.331 BWP-Uplink in<br>bwp-Common, bwp-Dedicated)<br>ServingCellConfig<br>>>firstActiveUplinkBWP-Id<br>M<br>See TS 38.331 ServingCellConfig<br>UE Aggregate Maximum Bit Rate Uplink<br>M<br>See TS 38.473 gNB-DU UE<br>Aggregate Maximum Bit Rate Uplink<br>dlModInfo<br>M<br>{modOrder,<br>mcsIndex , mcsTable}<br>ulModInfo<br>M<br>{modOrder,<br>mcsIndex,<br>mcsTable}<br>Number of LC To Add<br>M<br>The number of Logical Channel To<br>Add<br>>logicalChannelIdentity<br>M<br>See TS 38.331 logicalChannelI<br>dentity<br>>Qos(5Qi , GBR Qos Info, NG-RAN Alloca<br>M<br>See TS 38.473 DRB QoS in UE<br>tion and Retention Priority, GBR QoS Flow<br>CONTEXT MODIFICATION<br>Information, PDU Session ID, UL PDU Ses<br>REQUEST | | | |-------------------------------------------------------------------------------

--------------------------------------------------------------------------------

<sup>![](</sup>\_page\_126\_Picture\_1.jpeg)

| $\mid$            |  |  |  |  |
|-------------------|--|--|--|--|
|                   |  |  |  |  |
|                   |  |  |  |  |
| $\mathbf{1}$      |  |  |  |  |
|                   |  |  |  |  |
| $\mid \cdot \mid$ |  |  |  |  |
|                   |  |  |  |  |

| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | sion Aggregate Maximum Bit Rate) | | | >S-NSSAI<br>M<br>See TS 38.473 UE Context Cre | | | | ate/Modification Request: DRB In | | | | formation | | | | | | | | >DL LogicalChannelConfig (Lc priority)<br>M<br>See TS 38.321 Logical channel pri | | | | ority | | | | | | | | >UL LogicalChannelConfig (priority, logi<br>M<br>See 38.331 LogicalChannelConfig | | | | calChannelGroup, schedulingRequestID, pri | | | | oritisedBitRate, bucketSizeDuration) | | |

### <span id="page-126-0"></span>11.2.5.1.10 UE Create Response

#### \*\*Table 11-76 F1AP handler - MAC UE Create Response message contents\*\*

| Element | Presence | Description | |-----------------|----------|-------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -----------------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | | Cell Index | M | Identification of the Cell | | UE index | M | Identification of the UE | | Result | M | <br>Failure – if API parsing error<br>or semantic error (e.g. incorrect<br>state or invalid CRNTI, Cell<br>Index) or even a single Radio<br>Bearer (SRB/DRB) fails to be<br>established<br> <br>Success – in all the other cases | ![](\_page\_127\_Picture\_1.jpeg) | SRB failed to setup list | M | See TS 38.473 SRB Failed to Setup List<br>in UE CONTEXT SETUP RESPONSE | |----------------------------|---|---------------------------------------------- -------------------------------| | DRB failed to setup list | M | See TS 38.473 DRB Failed to Setup List<br>in UE CONTEXT SETUP RESPONSE | | Scell failed to setup list | M | See TS 38.473 SCell Failed To Setup<br>List in UE CONTEXT SETUP<br>RESPONSE | #####################################SPEC NODE END############################ # SPEC 048: 11.2.5.1.11 UE Reconfiguration Request #####################################SPEC NODE START############################ # <span id="page-127-0"></span>11.2.5.1.11 UE Reconfiguration Request #### \*\*Table 11-77 F1AP handler - MAC UE Reconfiguration Request message contents\*\* | Element | Presence | Description

|------------------------------------------------------------------------------- --------------------|----------|------------------------------------------------

|

-------------------------------------------------------------------------------- -----------------------------------------------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | | Cell Index | M | Identification of the Cell | | UE index | M | Identification of the UE | | CRNTI | M | See TS 38.331 RNTI-Value | | | | CRNTI is included only in case of<br>reestablishment procedure in SA | | mac-CellGroup-Reconfig (schedulingRe<br>quest-Reconfig, tag-Reconfig, ,bsrcon<br>fig,drx-config) | M | See TS 38.331 MAC-CellGroupConfig | | physicalCellGroup-Reconfig (pdsch-HARQ<br>ACK-Codebook, p-NR-FR1) | M | See TS 38.331 PhysicalCellGroupCon<br>fig | | spCell-Reconfig | M | See TS 38.331 SpCellConfig | | >servCellIndex | M | See TS 38.331 ServCellIndex | | >ServingCell-ReconfigInfo | M | See TS 38.331 ServingCellConfig | | >initialDownlinkBWP-Reconfig<br>(pdcch-Config, pdsch-Config) | M | See TS 38.331 BWP<br>DownlinkDedicated in ServingCell<br>Config | | >> radioLinkMonitoringConfig | M | RadioLinkMonitoringConfig is used to<br>configure radio link monitoring for de<br>tection of beam- and/or cell radio link<br>failure. See also TS 38.321 [3], clause<br>5.1.1 | | >Number of DL BWP To Add or<br>Modify | M | The number of dedicated DL BWP To<br>Add or Modify | | >DownlinkBWP-ToAddModList<br>(bwp-Id, bwp-Common, bwp-Dedi<br>cated)

|  | M |         |  | See | TS  | 38.331 |    | BWP-Downlink |    |     | in<br>ServingCellConfig |
|--|---|---------|--|-----|-----|--------|----|--------------|----|-----|-------------------------|
|  |   |         |  |     |     |        |    |              |    |     |                         |
|  |   | >Number |  | of  |     | DL     |    | BWP          |    | To  | Release                 |
|  | M |         |  |     | The | number | of | dedicated    | DL | BWP | To<br>remove            |
|  |   |         |  |     |     |        |    |              |    |     |                         |

## ![](\_page\_128\_Picture\_1.jpeg)

| <br> <br>M<br>           |                                 | See                                                    | TS          | 38.331                                                                     | >DownlinkBWP-ToReleaseList<br>downlinkBWP-ToRe<br> -------------------------------------------------------------------------------                                   |
|--------------------------|---------------------------------|--------------------------------------------------------|-------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                          |                                 |                                                        |             |                                                                            | --------------------------------------------------------------------------------<br>------- --- -------------------------------------------------------------------- |
|                          |                                 |                                                        |             | -------------------------------------------------------------------        | --------------------------------------------------------------------------------                                                                                     |
|                          |                                 |                                                        |             |                                                                            | (bwp-Id)                                                                                                                                                             |
|                          |                                 |                                                        | leaseList   | in                                                                         | ServingCellConfig                                                                                                                                                    |
| <br>                     |                                 |                                                        |             |                                                                            | >firstActiveDownlinkBWP-Id                                                                                                                                           |
| <br>M                    |                                 | See                                                    | TS          | 38.331                                                                     | ServingCellConfig                                                                                                                                                    |
| <br>                     |                                 |                                                        |             |                                                                            | >DefaultDownlinkBWP-Id                                                                                                                                               |
| <br>M                    |                                 | See                                                    | TS          | 38.331                                                                     | ServingCellConfig                                                                                                                                                    |
|                          |                                 |                                                        |             |                                                                            |                                                                                                                                                                      |
|                          |                                 |                                                        |             |                                                                            | >bwp-InactivityTimer                                                                                                                                                 |
| <br>M<br>                |                                 | See                                                    | TS          | 38.331                                                                     | ServingCellConfig                                                                                                                                                    |
|                          |                                 |                                                        |             |                                                                            | >PDSCH-ServingCell-Reconfig<br>(maxMIMO-Layers, nrofHARQ-Pro<br>cessesForPDSCH,                                                                                      |
|                          | codeBlockGroup<br>Transmission, |                                                        |             |                                                                            | xOverhead)                                                                                                                                                           |
| <br>M                    |                                 | See<br>TS                                              | 38.331      |                                                                            | PDSCH<br>ServingCellConfig                                                                                                                                           |
| <br> <br> <br>M<br> <br> | See<br>TS                       | >InitialUplinkBWP-Reconfig<br>(pucch-Config,<br>38.331 |             | BWP-UplinkDedicated<br>in                                                  | pusch-Config)<br>ServingCellConfig                                                                                                                                   |
|                          |                                 |                                                        |             |                                                                            | >>beamFailureRecoveryConfig                                                                                                                                          |
|                          |                                 |                                                        |             |                                                                            | M   The IE BeamFailureRecoveryConfig is<br>used to configure the UE with                                                                                             |
|                          |                                 |                                                        |             |                                                                            | RACH<br>resources and candidate beams for<br>beam failure recovery in case of                                                                                        |
|                          | >Number<br>of                   | UL                                                     | BWP         | beam<br>failure detection. See also TS 38.321<br>[3], clause 5.1.1  <br>To | Add<br>or<br>Modify                                                                                                                                                  |
| <br>M<br>                | The<br>number                   | of                                                     | dedicated   | UL<br>BWP                                                                  | To<br>Add<br>or<br>Modify                                                                                                                                            |
|                          |                                 |                                                        |             |                                                                            |                                                                                                                                                                      |
|                          | >UplinkBWP-ToAddModList         |                                                        | (bwp<br>Id, | bwp-Common,                                                                | bwp-Dedicated)                                                                                                                                                       |
| <br>M                    | <br>See                         | TS<br>38.331                                           | BWP-Uplink  | in                                                                         | Serv<br>ingCellConfig                                                                                                                                                |

| | >Number of UL BWP To Release | M | The number of dedicated UL BWP To<br>remove | | >uplinkBWP-ToReleaseList (bwp<br>Id) | M | See TS 38.331 uplinkBWP-ToRe<br>leaseList in ServingCellConfig | | >firstActiveUplinkBWP-Id | M | See TS 38.331 ServingCellConfig | | UE Aggregate Maximum Bit Rate Uplink | M | See TS 38.473 gNB-DU UE Aggregate<br>Maximum Bit Rate Uplink | | dlModInfo<br>{modOrder,<br>mcsIndex ,<br>mcsTable} | M | | | ulModInfo<br>{modOrder,<br>mcsIndex,<br>mcsTable} | M | | | Number of LC To Add | M | The number of Logical Channel to<br>Add | | >logicalChannelIdentity | M | See TS 38.331 logicalChannelIdentity | | >Qos(5Qi , GBR Qos Info, NG-RAN Al<br>location and Retention Priority, GBR<br>QoS Flow Information, PDU Session ID,<br>UL PDU Session Aggregate Maximum<br>Bit Rate) | M | See TS 38.473 DRB QoS in UE<br>CONTEXT MODIFICATION<br>REQUEST | ![](\_page\_129\_Picture\_1.jpeg) | >S-NSSAI | M | See TS 38.473 S-NSSAI in UE<br>CONTEXT MODIFICATION<br>REQUEST | |------------------------------------------------------------------------------- -------------------------------------------------------------------------------- -------|---|----------------------------------------------------------------| | >DL LogicalChannelConfig (Lc priority) | M | See TS 38.321 Logical channel prior<br>ity | | >UL LogicalChannelConfig (priority,<br>logicalChannelGroup, schedulingRe<br>questID, prioritisedBitRate, bucketSize<br>Duration) | M | See 38.331 LogicalChannelConfig | | Number of LC To Delete | M | The number of Logical Channel to De<br>lete | | >logicalChannelIdentity | M | See TS 38.331 logicalChannelIdentity | | Number of LC To Modified | M | The number of Logical Channel To<br>Modified | | >Logical Channel Identity | M | See TS 38.331 logicalChannelIdentity | | >Qos(5Qi , GBR Qos Info, NG-RAN Al<br>location and Retention Priority, GBR<br>QoS Flow Information, PDU Session ID,<br>UL PDU Session Aggregate Maximum<br>Bit Rate) | M | See TS 38.473 DRB QoS in UE<br>CONTEXT MODIFICATION<br>REQUEST | | >S-NSSAI | M | See TS 38.473 S-NSSAI in UE<br>CONTEXT MODIFICATION<br>REQUEST | | >DL LogicalChannelConfig (Lc priority) | M | See TS 38.321 Logical channel prior<br>ity | | >UL LogicalChannelConfig (priority,<br>logicalChannelGroup, schedulingRe<br>questID, prioritisedBitRate, bucketSize<br>Duration) | M | See 38.331 LogicalChannelConfig | ### <span id="page-129-0"></span>11.2.5.1.12 UE Reconfiguration Response #### \*\*Table 11-78 F1AP handler - MAC UE Reconfiguration Response message contents\*\* | Element | Presence | Description | |-----------------|----------|-------------------------------------------------- -------------------------------------------------------------------------------- -------------------------------------------------------------------------------- ---------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability

| Cell Index | M | Identification of the Cell | | UE Index | M | Identification of the UE |

| Result | M | <br>Failure – if API parsing error or<br>semantic error (e.g. invalid UE<br>Index, Cell Index) or none of<br>the requested reconfigurations /<br>modifications could be applied<br> <br>Success – in all the other cases |

![](\_page\_130\_Picture\_1.jpeg)

|

| SRB failed to setup list | M | See TS 38.473 SRB Failed to Setup List<br>in UE CONTEXT MODIFICATION<br>RESPONSE |

|----------------------------|---|---------------------------------------------- -------------------------------------------|

| DRB failed to setup list | M | See TS 38.473 DRB Failed to Setup List<br>in UE CONTEXT MODIFICATION<br>RESPONSE |

| Scell failed to setup list | M | See TS 38.473 SCell Failed To Setup<br>List in UE CONTEXT<br>MODIFICATION RESPONSE |

| DRB Failed to Modify List | M | See TS 38.473 DRB Failed to be Modi<br>fied List in UE CONTEXT<br>MODIFICATION RESPONSE |

### <span id="page-130-0"></span>11.2.5.1.13 UE Delete Request

#### \*\*Table 11-79 F1AP handler - MAC UE Delete Request message contents\*\*

| Element | Presence | Description | |-----------------|----------|-------------------------------------------------- -------------------------------------------------------------------------------- --------------------------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | | Cell Index | M | Identification of the Cell | | UE Index | M | Identification of the UE<br>is present if UE has been previously<br>successfully created at MAC. | | CRNTI | M | Identification of the UE.<br>CRNTI presence is optional.<br>CRNTI is present if UE is being de<br>leted without UE have been created<br>previously at MAC. | ### <span id="page-130-1"></span>11.2.5.1.14 UE Delete Response #### \*\*Table 11-80 F1AP handler - MAC UE Delete Response message contents\*\* | Element | Presence | Description | |-----------------|----------|-------------------------------------------------- -----------------------------------------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability |

| Cell Index | M | Identification of the Cell

|

| UE Index | M | Identification of the UE | | Status | M | <br>Failure – Invalid Cell Index or<br>UE Index<br> <br>Success – in all the other cases |

![](\_page\_131\_Picture\_1.jpeg)

### <span id="page-131-0"></span>11.2.5.1.15 RACH Resource Request

#### \*\*Table 11-81 F1AP handler - MAC RACH Resource Request message contents\*\*

| Element | Presence | Description | |-----------------|----------|-------------------------------------------------- ---------------------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | | Cell Index | M | Identification of the Cell | | UE Index | M | Identification of the UE | | Number of SSB | M | The number of ssb for which CFRA<br>resource allocation is requested. | | <br>ssb | M | See TS 38.331 SSB-Index | ### <span id="page-131-1"></span>11.2.5.1.16 RACH Resource Response #### \*\*Table 11-82 F1AP handler - MAC RACH Resource Response message contents\*\*

| Element | Presence | Description | |-------------------|----------|------------------------------------------------ --------------------------------------------------------------------------------

-----------------------------------------------------------------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | | Cell Index | M | Identification of the Cell | | UE Index | M | Identification of the UE | | Result | M | <br>Failure – if API parsing error<br>or semantic error (e.g. invalid<br>Cell Index) or unable to allo<br>cate any CFRA

```
Resource on<br>any of the SSB<br> <br>Success – in all the other cases |
| newUE-Identity | M | See TS 38.331 newUE-Identity 
|
| CFRA-SSB-Resource | M | See TS 38.331 CFRA-SSB-Resource 
|
```

```
### <span id="page-131-2"></span>11.2.5.1.17 RACH Resource Release
```

#### \*\*Table 11-83 F1AP handler - MAC RACH Resource Release message contents\*\*

| Element | Presence | Description | |-----------------|----------|-------------------------------------------------- --------------------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | | Cell Index | M | Identification of the Cell | | UE Index | M | Identification of the UE | | | | is present if UE has been previously<br>successfully created at MAC. | | CRNTI | M | Identification of the UE. | ![](\_page\_132\_Picture\_1.jpeg) | CRNTI presence is optional. | | |------------------------------------------------------------------------------- -----------------|--| | CRNTI is present if UE is being de<br>leted without UE have been created<br>previously at MAC. | |

### <span id="page-132-0"></span>11.2.5.1.18 UE Reset Request

#### \*\*Table 11-84 F1AP handler - MAC UE Reset Request message contents\*\*

|  | Element                                                                         |  | Presence |  | Description |
|--|---------------------------------------------------------------------------------|--|----------|--|-------------|
|  |                                                                                 |  |          |  |             |
|  | ----------------- ---------- -------------------------------------------------- |  |          |  |             |
|  | --------------                                                                  |  |          |  |             |

| Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability |

```
| Cell Index | M | Identification of the Cell 
|
| UE Index | M | Identification of the UE 
|
```

### <span id="page-132-1"></span>11.2.5.1.19 UE Reset Response

#### \*\*Table 11-85 F1AP handler - MAC UE Reset Response message contents\*\*

| Element | Presence | Description | |-----------------|----------|-------------------------------------------------- -------------------------------------------------------------------------------- --------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | | Cell Index | M | Identification of the Cell | | UE Index | M | Identification of the UE | | Status | M | <br>Failure – if API parsing error<br>or semantic error (e.g. invalid<br>UE Index, Cell Index)<br> <br>Success – in all the other cases | ### <span id="page-132-2"></span>11.2.5.1.20 UE Sync Status Indication #### \*\*Table 11-86 F1AP handler - MAC UE Sync Status message contents\*\* | Element | Presence | Description | |-----------------|----------|-------------------------------------------------- ------------------------------| | Debug Time Info | O | This is an optional IE and may be provided<br>on availability | | Cell Index | M | Identification of the Cell | | UE Index | M | Identification of the UE | | Sync Status | M | <br>The sync status is 'inSync', 'Ou<br>tOfSync' and OutOfSyncMaxRe<br>triess |

![](\_page\_133\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 049: 11.2.5.1.21 UL CCCH Indication #####################################SPEC NODE START############################

## <span id="page-133-0"></span>11.2.5.1.21 UL CCCH Indication

#### \*\*Table 11-87 F1AP handler - MAC UL CCCH Indication message contents\*\*

| Element | Presence | Description | |-----------------|----------|-------------------------------------------------- --------------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | | Cell Index | M | Identification of the Cell | | CRNTI | M | See TS 38.331 RNTI-Value | | UL-CCCH-Message | M | See TS 38.331 UL-CCCH-Message |

### <span id="page-133-1"></span>11.2.5.1.22 DL CCCH Indication

#### \*\*Table 11-88 F1AP handler - MAC DL CCCH Indication message contents\*\*

| Element | Presence | Description | |-----------------|----------|-------------------------------------------------- --------------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | | Cell Index | M | Identification of the Cell | | CRNTI | M | See TS 38.331 RNTI-Value | | Message Type | M | See TS 38.331 DL-CCCH-Message<br>Type | | DL-CCCH-Message | M | See TS 38.331 DL-CCCH-Message |

### <span id="page-133-2"></span>11.2.5.1.23 DL PCCH Indication

#### \*\*Table 11-89 F1AP handler - MAC DL CCCH Indication message contents\*\*

| Element | Presence | Description | |-----------------|----------|-------------------------------------------------- --------------| | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | | Cell Index | M | Identification of the Cell | | Paging Frame | M | See TS 38.304 PF | | Paging Occasion | M | See TS 38.304 PO | | Short-Message | M | See TS 38.331 Short Message | | PCCH-Message | M | See TS 38.331 PCCH-Message | ### <span id="page-133-3"></span>11.2.5.1.24 DL Broadcast Request #### \*\*Table 11-90 F1AP handler - MAC DL Broadcast Request message contents\*\* | Element | Presence | Description | |---------|----------|-------------| ![](\_page\_134\_Picture\_1.jpeg) | Debug Time Info | O | This is an optional IE and may be pro<br>vided on availability | |---------------------------------------------------|---|----------------------- -----------------------------------------| | Cell Index | M | Identification of the Cell | | Number of SI blocks | M | The number of SI | | SI Message (SI type, scheduling Info<br>and Data) | M | See TS 38.331 SI-SchedulingInfo | #####################################SPEC NODE END############################ # SPEC 050: 11.2.6 F1AP Handler – RLC Interface #####################################SPEC NODE START############################ ## <span id="page-134-0"></span>11.2.6 F1AP Handler – RLC Interface

The following section captures the interface APIs between F1AP and RLC:

| Direction                                                                                                                 | Message/API                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                            |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
|                                                                                                                           | ------------------------ --------------------------------- --------------------                                                                                                                                                                                                                                                                                                                                                                         |                                                                                        |
|                                                                                                                           | --------------------------------------------------------------------------------<br>--------------------------------------------------------------------------------<br>--------------------------------------------------------------------------------                                                                                                                                                                                                |                                                                                        |
| F1AP handler<br>to RLC   UE Create<br>ack<br>                                                                             | -------------------------------------------------------- <br>add the<br>UE associated RLC entity<br>and related information (e.g.:<br>sn field<br>length, t reassembly<br>timer etc.). Refer to sub<br>clause 8.3 in 3GPP<br>TS<br>38.473 for details of related<br>F1 procedure [18].<br>Note: One or more<br>RLC enti<br>ties of the UE may be created<br>in the same API.  <br>  RLC to F1AP<br>Handler   UE Create Re<br>sponse<br>for<br>the<br>UE | This API is used to<br>  This API is used to<br>context<br>creation.                   |
| to<br>subclause<br>con<br>figured in the same API.<br>ack<br>for<br>the<br>                                               | F1AP handler<br>to RLC   UE Reconfigura<br>tion<br>reconfig<br>ure the UE associated RLC<br>entity previously added at<br>RLC. Refer<br>8.3<br>in<br>3GPP<br>TS<br>38.473<br>for<br>procedure<br>[18].<br>Note: One or more RLC enti<br>ties of the UE may be re<br>  RLC to F1AP<br>Handler   UE Reconfigura<br>tion Response   This API is used to<br>UE<br>context                                                                                   | This API is used to<br>de<br>tails<br>of<br>related<br>F1<br> <br>reconfigura<br>tion. |
| 8.3<br>in<br>3GPP<br>                                                                                                     | F1AP handler<br>to RLC   UE Delete Request<br>delete the<br>UE and associated RLC enti<br>ties at RLC. Refer to sub<br>clause<br>TS<br>38.473<br>for<br>details<br>of                                                                                                                                                                                                                                                                                   | This API is used to<br>related<br>F1<br>procedure<br>[18].                             |
| #### **Table 11-91 F1AP handler -                                                                                         | RLC Specific APIs**                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                        |
| ![](_page_135_Picture_1.jpeg)                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                        |
| <br>                                                                                                                      | Note: One or more RLC enti<br>ties of the UE may be deleted<br>in the same API.<br> -------------------------------------------------- ----------------------------<br>-------- -----------------------------------------------------------------------                                                                                                                                                                                                 |                                                                                        |
| ---------------------------- <br>  RLC to F1AP<br>Handler<br> <br>This<br>API<br> <br>  F1AP handler<br>to RLC<br>Request | --------------------------------------------------------------------------------<br>is<br>used<br>to<br>ack<br>for<br>the<br>  This API is used to re-estab<br>lish all the RLC entities                                                                                                                                                                                                                                                                | UE Delete Re<br>sponse<br>UE<br>context<br>deletion.<br>  UE RLC Re-estab<br>lish      |

asso<br>ciated with the UE. Refer to<br>subclause 8.3 in 3GPP TS<br>38.473 for details of related<br>F1 procedure [18]. | | RLC to F1AP<br>Handler | UE RLC Re-estab<br>lish Response | This API is used to ack for<br>the RLC reestablishment<br>with the UE . | | F1AP handler<br>(UE State<br>Manager) | DL RRC Message<br>Transfer | This API is used to request<br>RLC to deliver RRC mes<br>sage from CU (RRC) to the<br>UE. | | F1AP handler<br>(UE State<br>Manager) | UL RRC Message<br>Transfer | This API is used to deliver<br>RRC message from UE to<br>the CU (RRC) | | RLC to F1AP<br>Handler (UE<br>State Man<br>ager) | RLC Max Retrans<br>mission Reached | This API is used to inform<br>the higher layers once maxi<br>mum number of Retransmis<br>sions are hit. | | RLC to F1AP<br>Handler (UE<br>State Man<br>ager) | RRC Message De<br>livery Report | This API is used by RLC to<br>inform higher layers on suc<br>cessful/failed delivery of a<br>DL RRC Message |

The detailed description of APIs is below.

### <span id="page-135-0"></span>11.2.6.1 UE Create

Please note that UL configuration below applies to the DL AM/UM entity locally on the O-DU. Correspondingly DL Configuration below applies to UL AM/UM entity locally on the O-DU.

| <br>Element                           |   | <br>Presence<br> <br>Description                                                |
|---------------------------------------|---|---------------------------------------------------------------------------------|
|                                       |   |                                                                                 |
|                                       |   | --------------------------- ---------- ---------------------------------------- |
| ---------------------------           |   |                                                                                 |
| Cell Index                            | M | Identification of the Cell. 2-byte                                              |
| integer allocated by F1AP             |   |                                                                                 |
| UE Index                              | M | Identification of the UE. 2-byte                                                |
| integer allocated by F1AP             |   |                                                                                 |
| Number of LCs to be Setup   M         |   | Number of LC to be added as part of UE                                          |
| Creation<br>                          |   |                                                                                 |
| >logicalChannelIdentity               | M | {132} SRB/DRB logical channel identity                                          |
|                                       |   |                                                                                 |
| >S-NSSAI                              | M | See TS 38.473 S-NSSAI in UE                                                     |
| CONTEXT<br>SETUP/MODIFICATION REQUEST |   |                                                                                 |

\*\*Table 11-92 F1AP handler - RLC UE Create message contents\*\*

![](\_page\_136\_Picture\_1.jpeg)

| >RlcMode                                                 | M | Mode of operation of this                                                       |
|----------------------------------------------------------|---|---------------------------------------------------------------------------------|
| logical channel                                          |   |                                                                                 |
|                                                          |   | --------------------------------- ----------- --------------------------------- |
| -------------------------------------------------------- |   |                                                                                 |
|                                                          |   | {RLC-AM, RLC-UM-Bidirectional,                                                  |
| RLC-UM-Unidirectional<br>UL, RLC-UM-Unidirectional-DL, ) |   |                                                                                 |
|                                                          |   | Range is same as defined in                                                     |
| 38.331<br>  > AM Bearer Config                           |   | <br>  O (if AM)   Present if the RLC Mode is AM                                 |
|                                                          |   |                                                                                 |
| >> UL AM Config<br>                                      |   | M<br>                                                                           |
| >>> snFieldLength<br>                                    |   | M<br>  {size12, size18}                                                         |
|                                                          |   | Range is same as defined in                                                     |
| 38.331                                                   |   |                                                                                 |
| >>> t-PollRetrans<br>mit                                 | M | Range same as 38.331 defined                                                    |
| range for T-PollRetransmit                               |   |                                                                                 |
| >>> pollPDU                                              | M | Range same as defined in 38.331                                                 |
| range for PollPDU                                        |   |                                                                                 |
| >>> pollByte                                             | M | Range same as defined in 38.331                                                 |
| range for PollByte                                       |   |                                                                                 |
| >>>                                                      | M | Range same as defined in 38.331                                                 |
| range for maxRetxThreshold                               |   |                                                                                 |
| maxRetxThreshold                                         |   | {t1, t2, t3, t4, t6, t8, t16,                                                   |
| t32}                                                     |   |                                                                                 |
| >> DL AM Config<br>                                      |   | M<br>                                                                           |
| >>> snFieldLength                                        | M | Range same as defined in 38.331                                                 |
| range for SN<br>FieldLengthAM                            |   |                                                                                 |
| >>> t-Reassembly                                         | M | Range same as defined in 38.331                                                 |
| range for T-Reassembly                                   |   |                                                                                 |
| >>> t-statusProhibit                                     | M | Range same as defined in 38.331                                                 |
| range for T-StatusProhibit                               |   |                                                                                 |
| >UM-Bi<br>DirectionalConfig                              | O | Present if RLC Mode = RLC-UM                                                    |
| Bidirectional                                            |   |                                                                                 |
| <br>>><br>UL-UM-Config<br>                               |   | <br>M<br>                                                                       |
| >>> snFieldLength                                        | M | Range same as defined in 38.331                                                 |

| range for SN<br>FieldLengthUM<br> <br>>><br>DL-UM-Config                                                                                                               |               | <br>                                                     | M |                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|----------------------------------------------------------|---|---------------------------------|
| <br>  >>> snFieldLength<br>range for SN<br>FieldLengthUM                                                                                                               | M             |                                                          |   | Range same as defined in 38.331 |
| >>> t-Reassembly<br>range for T-Reassembly                                                                                                                             | M             |                                                          |   | Range same as defined in 38.331 |
| >UM-Uni<br>DirectionalConfig-UL   O<br>Unidirectional-UL                                                                                                               |               |                                                          |   | Present if RLC-Mode = RLC-UM    |
| >> snFieldLength<br>range for SN<br>FieldLengthUM                                                                                                                      | M             |                                                          |   | Range same as defined in 38.331 |
| >UM-Uni<br>DirectionalConfig-DL   O<br>Unidirectional-DL                                                                                                               |               |                                                          |   | Present if RLC-Mode = RLC-UM    |
| <br>>><br>DL-UM-Config<br>                                                                                                                                             |               |                                                          | M |                                 |
| >>> snFieldLength<br>range for SN<br>FieldLengthUM                                                                                                                     | M             |                                                          |   | Range same as defined in 38.331 |
| ![](_page_137_Picture_1.jpeg)                                                                                                                                          |               |                                                          |   |                                 |
| >>> t-Reassembly   M   Range same as defined in 38.331 range for T-Reassembly<br> <br> ------------------ --- -------------------------------------------------------- |               |                                                          |   |                                 |
| <br> <br>                                                                                                                                                              |               |                                                          |   | <br>                            |
| ### <span id="page-137-0"></span> 11.2.6.2 UE Create Response                                                                                                          |               |                                                          |   |                                 |
| #### **Table 11-93 F1AP handler -                                                                                                                                      |               | RLC UE Create Response message contents**                |   |                                 |
| <br>Element<br>                                                                                                                                                        |               | Presence                                                 |   | Description                     |
| ------------ ---------- -------------------------------------------------------<br>--------------------------------------------------------------------------------    |               |                                                          |   |                                 |
| ------------------------------------------------------------------ <br>  Cell Index   M<br>by                                                                          |               | Identification of the Cell. 2-byte in<br>teger allocated |   | F1AP                            |
| <br>  UE Index<br>  M<br>by<br>                                                                                                                                        |               | Identification of the UE. 2-byte inte<br>ger allocated   |   | F1AP                            |
| Result<br>  M<br> <br>error (e.g.<br>incorrect state or invalid UE<br>Index, Cell Index). Refer<br>TS                                                                  | <br>Failure – | if API parsing er<br>ror or semantic                     |   |                                 |

38.473 section 9.3.1.2<br>Cause<br>Success – in all the other cases |

#####################################SPEC NODE END############################ # SPEC 051: 11.2.6.3 UE Reconfiguration

#####################################SPEC NODE START############################ ## <span id="page-137-1"></span>11.2.6.3 UE Reconfiguration

Please note that UL configuration below applies to the DL AM/UM entity locally on the gNB. Correspondingly DL Configuration below applies to UL AM/UM entity locally on the gNB.

| Element | Presence | Description | |--------------------------|-----------|---------------------------------------- -------------------------------------------------------------------------------- -----------------------------------------------------| | Cell Index | M | Identification of the Cell. 2-byte integer allocated by F1AP | | UE Index | M | Identification of the UE. 2-byte integer allocated by F1AP | | Number of LCs to Add/Mod | M | Number of LC to be added | | >logicalChannelIdentity | M | {132} SRB/DRB logical channel identity | | >S-NSSAI | M | See TS 38.473 S-NSSAI in UE CONTEXT MODIFICATION<br>REQUEST | | >RlcMode | M | Mode of operation of this logical channel<br>{RLC-AM, RLC-UM-Bidirectional, RLC-UM-Unidirectional<br>UL, RLC-UM-Unidirectionall-DL, )<br>Range is same as defined in 38.331 | | > AM Bearer Config | O (if AM) | Present if the RLC Mode is AM | | >> UL AM Config | M | |

\*\*Table 11-94 F1AP handler - RLC UE Reconfiguration message contents\*\*

![](\_page\_138\_Picture\_1.jpeg)

| >>> | M | {size12, size18} | |---------------------------------|---|-----------------------------------------

----------------------| | snFieldLength | | | | | | Range is same as defined in 38.331 | | >>> t-PollRetrans | M | Range same as 38.331 defined range for T-PollRetransmit | | mit | | | | >>> pollPDU | M | Range same as defined in 38.331 range for PollPDU | | >>> pollByte | M | Range same as defined in 38.331 range for PollByte | | >>> | M | Range same as defined in 38.331 range for maxRetxThreshold | | maxRetxThreshold | | {t1, t2, t3, t4, t6, t8, t16, t32} | | | | | | >> DL AM Config | M | | | >>> snFieldLength | M | Range same as defined in 38.331 range for SN<br>FieldLengthAM | | >>> t-Reassembly | M | Range same as defined in 38.331 range for T-Reassembly | | >>> t-statusProhibit | M | Range same as defined in 38.331 range for T-StatusProhibit | | >UM-Bi-DirectionalConfig | O | Present if RLC Mode = RLC-UM-Bidirectional | | >> UL-UM-Config | M | | | >>> snFieldLength | M | Range same as defined in 38.331 range for SN<br>FieldLengthUM | | >> DL-UM-Config | M | | | >>> snFieldLength | M | Range same as defined in 38.331 range for SN<br>FieldLengthUM | | >>> t-Reassembly | M | Range same as defined in 38.331 range for T-Reassembly | | >UM-Uni<br>DirectionalConfig-UL | O | Present if RLC-Mode = RLC-UM-Unidirectional-UL | | >> snFieldLength | M | Range same as defined in 38.331 range for SN<br>FieldLengthUM | | >UM-Uni<br>DirectionalConfig-DL | O | Present if RLC-Mode = RLC-UM-

```
Unidirectional-DL |
| >> DL-UM-Config | M | 
|
| >>> snFieldLength | M | Range same as defined in 38.331 range 
for SN<br>FieldLengthUM |
| >>> t-Reassembly | M | Range same as defined in 38.331 range 
for T-Reassembly |
| Number of LCs to be Released | M | Number of LC to be released 
|
| >logicalChannelIdentity | M | {132} SRB/DRB logical channel identity 
|
```

![](\_page\_139\_Picture\_1.jpeg)

-------|

### <span id="page-139-0"></span>11.2.6.4 UE Reconfiguration Response

#### \*\*Table 11-95 F1AP handler - RLC UE Reconfiguration Response message contents\*\*

| <br>Element                                                                                                                                                         |                   | Presence                         |                                                          |  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|----------------------------------|----------------------------------------------------------|--|
|                                                                                                                                                                     |                   |                                  |                                                          |  |
| ------------ ---------- -------------------------------------------------------<br>-------------------------------------------------------------------------------- |                   |                                  |                                                          |  |
| ----------------------------------------------------------                                                                                                          |                   |                                  |                                                          |  |
| Cell Index   M                                                                                                                                                      |                   |                                  | Identification of the Cell. 2-byte in<br>teger allocated |  |
| by                                                                                                                                                                  |                   |                                  | F1AP                                                     |  |
|                                                                                                                                                                     |                   |                                  |                                                          |  |
| UE Index<br>  M                                                                                                                                                     |                   |                                  | Identification of the UE. 2-byte inte<br>ger allocated   |  |
| by<br>                                                                                                                                                              |                   |                                  | F1AP                                                     |  |
| Result<br>  M                                                                                                                                                       | <br><br>Failure – |                                  | if API parsing er<br>ror or semantic                     |  |
| error (e.g.<br>incorrect state or invalid UE<br>Index, Cell Index). Refer<br>TS                                                                                     |                   |                                  |                                                          |  |
| 38.473 section 9.3.1.2.<br>Success –                                                                                                                                |                   | in all the other cases           |                                                          |  |
|                                                                                                                                                                     |                   |                                  |                                                          |  |
| ### <span id="page-139-1"></span> 11.2.6.5 UE Delete                                                                                                                |                   |                                  |                                                          |  |
| #### **Table 11-96 F1AP handler -                                                                                                                                   |                   | RLC UE Delete message contents** |                                                          |  |
| <br>Element<br>                                                                                                                                                     |                   | Presence                         | <br>Description                                          |  |
| ------------ ---------- -------------------------------------------------------                                                                                     |                   |                                  |                                                          |  |

| Cell Index | M | Identification of the Cell. 2-byte integer allocated by F1AP |

| UE Index | M | Identification of the UE. 2-byte integer allocated by F1AP |

### <span id="page-139-2"></span>11.2.6.6 UE Delete Response

#### \*\*Table 11-97 F1AP handler - RLC UE Delete Response message contents\*\*

| <br>Element | <br>Presence                                                                                                                                                        | <br>Description |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
|             |                                                                                                                                                                     |                 |
|             | ------------ ---------- -------------------------------------------------------<br>-------------------------------------------------------------------------------- |                 |

---------------------------------------------------|

| Cell Index | M | Identification of the Cell. 2-byte integer allocated by F1AP |

| Result | M | <br>Failure – if API parsing error or semantic error (e.g.<br>incorrect state or invalid UE Index, Cell Index). Refer<br>TS 38.473 section 9.3.1.2.<br>Success – in all the other cases |

#####################################SPEC NODE END############################ # SPEC 052: 11.2.6.7 DL RRC Message Transfer #####################################SPEC NODE START############################ ## <span id="page-139-3"></span>11.2.6.7 DL RRC Message Transfer

#### \*\*Table 11-98 F1AP handler - RLC DL RRC Message Transfer message contents\*\*

| <br>Element                                                                          |   |           |  | Presence | <br>Description                                   |
|--------------------------------------------------------------------------------------|---|-----------|--|----------|---------------------------------------------------|
| <br> ------------------------ ---------- ------------------------------------------- |   |           |  |          |                                                   |
| -------------------                                                                  |   |           |  |          |                                                   |
| Cell Index                                                                           | M |           |  |          | Identification of the Cell. 2-byte integer        |
| allocated by F1AP                                                                    |   |           |  |          |                                                   |
| UE Index                                                                             | M |           |  |          | Identification of the UE. 2-byte integer          |
| allocated by F1AP<br>                                                                |   |           |  |          |                                                   |
| logicalChannelIdentity   M                                                           |   |           |  |          | {13} SRB logical channel identity                 |
|                                                                                      |   |           |  |          |                                                   |
|                                                                                      |   |           |  |          |                                                   |
| ![](_page_140_Picture_1.jpeg)                                                        |   |           |  |          |                                                   |
|                                                                                      |   |           |  |          |                                                   |
| ExecuteDuplication                                                                   |   |           |  |          | O   {true, false} if present it implies RLC needs |
| to                                                                                   |   | duplicate |  |          | via<br>CA                                         |
|                                                                                      |   |           |  |          |                                                   |
| --------------------------- --- -----------------------------------------------      |   |           |  |          |                                                   |
| --------------------------------------------------------------------------------     |   |           |  |          |                                                   |

| | RRCDeliveryStatusRequired | O | {true, false} if present it implies that RLC must report delivery<br>to F1AP (UE State Manager) on successful/failed delivery | | RRC-Message | M | DL-DCCH-Message as specified in 38.331 | | RRC-Message-Length | M | Length of DL-DCCH message |

### <span id="page-140-0"></span>11.2.6.8 DL RRC Message Response

RLC sends the status of RRC message sent by DUAPP so that DUAPP can further carry on with the remaining UE related procedures such as UE Context Setup/Modification or release accordingly.

| Table 11-99 F1AP handler - RLC DL RRC Message Transfer response | | |-----------------------------------------------------------------|--| |-----------------------------------------------------------------|--| | Element | Presence | Description | |------------|----------|------------------------------------------------------- ------------------------------------| | Cell Index | M | Identification of the Cell. 2-byte inte<br>ger allocated by F1AP | | UE Index | M | Identification of the UE. 2-byte inte<br>ger allocated by F1AP | | DLMsgState | M | Provides the feedback of the pro<br>cessing state of RRC message sent<br>by DUAPP to RLC. | | | | Values: | | | | ENUM { | | | | TRANSMISSION\_IN\_PROGRESS, | | | | TRANSMISSION\_COMPLETE, | | | | TRANSMISSIN\_FAILED} |

### <span id="page-140-1"></span>11.2.6.9 UL RRC Message Transfer #### \*\*Table 11-100 F1AP handler - RLC UL RRC Message Transfer\*\*

| Element | Presence | Description | |------------------------|----------|------------------------------------------- -------------------| | Cell Index | M | Identification of the Cell. 2-byte integer allocated by F1AP | | UE Index | M | Identification of the UE. 2-byte integer allocated by F1AP | | logicalChannelIdentity | M | {13} SRB logical channel identity | | RRC-Message | M | UL-DCCH-Message as specified in 38.331 | | RRC-Message-Length | M | Length of UL-DCCH message | ![](\_page\_141\_Picture\_1.jpeg) ### <span id="page-141-0"></span>11.2.6.10 UL RRC Message Delivery Report #### \*\*Table 11-101 F1AP handler - RLC UL RRC Message Delivery Report\*\* | Element | Presence | Description | |------------------------|----------|------------------------------------------- -------------------| | Cell Index | M | Identification of the Cell. 2-byte integer allocated by F1AP | | UE Index | M | Identification of the UE. 2-byte integer allocated by F1AP | | logicalChannelIdentity | M | {13} SRB logical channel identity | | RRC Delivery Status | M | RRC Delivery Status as defined in 38.473 | ### <span id="page-141-1"></span>11.2.6.11 RLC Max Retransmission Reached #### \*\*Table 11-102 F1AP handler - RLC Max Retransmission Reached message contents\*\* | Element | Presence | Description | |------------------------|----------|------------------------------------------- ------------------------------------------|

| Cell Index | M | Identification of the Cell. 2-byte integer allocated by F1AP | | UE Index | M | Identification of the UE. 2-byte integer allocated by F1AP | | SRB/DRB | M | Identification of SRB (0) or DRB (1) | | logicalChannelIdentity | M | {132} SRB/DRB logical channel identity that experienced<br>MAX RETRANSMISSION EVENT |

### <span id="page-141-2"></span>11.2.6.12 UL RLC Re-establishment Request

#### \*\*Table 11-103 F1AP handler - RLC UL RLC Reestablishment Request message contents\*\*

| Element | Presence | Description | |-------------------------|----------|------------------------------------------ --------------------| | Cell Index | M | Identification of the Cell. 2-byte integer allocated by F1AP | | UE Index | M | Identification of the UE. 2-byte integer allocated by F1AP | | numberOfLc | M | Number of Logical Channels that have to be re-established | | >logicalChannelIdentity | M | {132} SRB/DRB logical channel identity |

### <span id="page-141-3"></span>11.2.6.13 UE RLC Re-establishment Response

#### \*\*Table 11-104 F1AP handler - RLC UE RLC Reestablishment Response message contents\*\*

| <br>Element     |                                                                                 | Presence |  | Description                                              |
|-----------------|---------------------------------------------------------------------------------|----------|--|----------------------------------------------------------|
|                 |                                                                                 |          |  |                                                          |
|                 | ------------ ---------- ------------------------------------------------------- |          |  |                                                          |
|                 | -------------------------------------------                                     |          |  |                                                          |
| Cell Index   M  |                                                                                 |          |  | Identification of the Cell. 2-byte in<br>teger allocated |
| by F1AP         |                                                                                 |          |  |                                                          |
| UE Index<br>  M |                                                                                 |          |  | Identification of the UE. 2-byte inte<br>ger allocated   |
| by F1AP         |                                                                                 |          |  |                                                          |
| Result<br>  M   | <br><br>Failure –                                                               |          |  | if API parsing er<br>ror or semantic                     |
|                 | error (e.g.<br>incorrect state or invalid UE                                    |          |  |                                                          |

![](\_page\_142\_Picture\_1.jpeg)

```
| | Index, Cell Index). Refer<br>TS 38.473 section 9.3.1.2. |
|--|---------------------------------------------------------|
| | Success – in all the other cases |
```

#####################################SPEC NODE END############################ # SPEC 053: 11.2.6.14 UL User Data #####################################SPEC NODE START############################ ## <span id="page-142-0"></span>11.2.6.14 UL User Data

#### \*\*Table 11-105 RLC - F1AP handler UL User Data\*\*

```
| Element | Presence | Description 
|
|------------------------|----------|-------------------------------------------
-------------------|
| Cell Index | M | Identification of the Cell. 2-byte integer 
allocated by F1AP |
| UE Index | M | Identification of the UE. 2-byte integer 
allocated by F1AP |
| logicalChannelIdentity | M | {132} SRB/DRB logical channel identity 
|
| MsgLength | M | Length of the User data in uplink 
|
| User Data | M | 
|
```

#####################################SPEC NODE END############################ # SPEC 054: 11.2.6.15 DL User Data #####################################SPEC NODE START############################ # <span id="page-142-1"></span>11.2.6.15 DL User Data

\*\*Table 11-106 RLC - F1AP handler DL User Data\*\*

```
| Element | Presence | Description 
|
|------------------------|----------|-------------------------------------------
-------------------|
| Cell Index | M | Identification of the Cell. 2-byte integer 
allocated by F1AP |
| UE Index | M | Identification of the UE. 2-byte integer 
allocated by F1AP |
| logicalChannelIdentity | M | {132} SRB/DRB logical channel identity 
|
```

```
| MsgLength | M | Length of the User data in Downlink 
|
| User Data | M | 
|
```

```
#####################################SPEC NODE END############################
# SPEC 055: 11.2.7 RLC – O-DU-OAM-Agent Interface / 11.2.7.1 PM Slice throughput 
Event
```

```
#####################################SPEC NODE START############################
# <span id="page-142-2"></span>11.2.7 RLC – O-DU-OAM-Agent Interface
```

```
## <span id="page-142-3"></span>11.2.7.1 PM Slice throughput Event
```

This is PM event to notify the slice specific throughput towards OAM agent that are sent at every reporting interval (1 minutes).

```
| Element | Presence | Description 
|
|-------------------------------|----------|------------------------------------
-----------------|
| Num of Slices | M | Number of slices which have 
active<br>Data sessions |
| <br>Network Slice Identifier | M | 32Bit Integer; 24Bits SD and 8 
bits<br>SST |
| <br>Throughput DL | M | DL throughput of this SNSSAI 
|
```

```
**Table 11-107 RLC – O-DU-OAM-Agent PM Slice Throughput Event**
```

```
![](_page_143_Picture_1.jpeg)
```

| | Throughput UL | M | UL throughput of this SNSSAI | |---|---------------|---|------------------------------|

### 11.3 O1 Interface and data model

<span id="page-143-0"></span>The O1 interface performs FCAPS management for the O-DU.

- The O1 interface is terminated at the O-DU-OAM-Agent module of O-DU to handle all configurations of L1 and L2 layers.

- The interface includes cell configuration towards MAC/SCH and RLC layer.

 - o The interface includes slice specific configuration to support RAN slicing SLA assurance.

 - o The interface includes Beam forming and MIMO configurations and additionally configuration related to supported SSB and CSI-RS TRS per cell, supported beam forming modes, SRS configuration periodicity to support massive MIMO optimization use cases like non-GoB ,GoB beamforming, L1/L2 beam management as reference in O-RAN.WG1.Use-Cases-mMIMO-TR[31].

- o to support Massive MIMO optimization feature.

- The O1 interface for the O-DU details the data model at cell level, beam level and slice level configurations at stated in reference [26].

- O1 interface supports the performance management/KPI management. O-DU-OAM - Agent collects the performance counters at the cell level, beam level and slice level as required to support various feature optimization and reports to the performance management entity of the SMO.

- The optimized DU configuration for the features e.g. Massive MIMO optimization is notified by the SMO to O-DU-OAM-Agent over file ready notification and the same can be downloaded at O-DU-OAM-Agent module upon accepting the file download request from O-DU system. If required, the O-DU system notifies the new configuration to the O-RU over Fronthaul M-plane interface as reference in [23]. The optimized DU configuration is achieved by the AI/ML driven rAPP application hosted at the Non RT-RIC performs or by xApp application hosted at the Near RT-RIC underlying ML model trained on the historical data collected from a cell or a cluster of cells .The input data for this optimization training and interference can be comprised of several performance statistics and the output of the inference is the optimized configuration sent towards O-DU over the O1 interface.

For data models, please refer to O-RAN WG5 data models for O-D[U \[26\].](#page-9-8)

### <span id="page-143-1"></span>11.4 E2 Interface

The E2 service models is extended to support the use cases e.g. RAN slicing SLA assurance and Massive MIMO Optimization.

o The enhancement in the O-RAN interfaces and data models of the E2 interface to enable the Near RT RIC to support Massive MIMO sub-features for AI/ML based mMIMO BF optimization, also enhancements to Near-RT RIC architecture if there is any is detailed in reference [32]

#####################################SPEC NODE END############################ # SPEC 056: 12. O-CU Interface #####################################SPEC NODE START############################ # <span id="page-143-2"></span>12. O-CU Interface

APIs between the following layers of O-CU are described in this section.

- RRC-SDAP - RRC-PDCP - SDAP- PDCP

It is expected that the software implementation of the APIs defined in this section will be in conformance with the API message definition and the fields or message elements. Data types and encoding/decoding of the message contents will be implementation dependent. Message elements (IEs) referring to definitions in 3GPP specifications are italicized for ease of reference.

![](\_page\_144\_Picture\_1.jpeg)

### <span id="page-144-0"></span>12.1 RRC-SDAP Interface

#### \*\*Table 12-1 RRC-SDAP APIs\*\*

| <br>Direction | <br>Message/API                                              | <br>Description                                                                 |
|---------------|--------------------------------------------------------------|---------------------------------------------------------------------------------|
|               |                                                              |                                                                                 |
|               | ------------------------------------------------------------ | ------------- ------------------------- --------------------------------------- |

| RRC to SDAP | QoS flow to DRB mapping | QoS mapping when a DRB is added/modified. RRC indicates<br>in this API if reflective QoS is used. | | RRC to SDAP | DRB release | To remove all QoS flow to DRB mappings |

The detailed description of RRC-SDAP APIs is below.

#####################################SPEC NODE END############################ # SPEC 057: 12.1.1 QoS Flow to DRB Mapping #####################################SPEC NODE START############################ # <span id="page-144-1"></span>12.1.1 QoS Flow to DRB Mapping

#### \*\*Table 12-2 RRC-SDAP QoS flow to DRB mapping message contents\*\*

|      | Element                                                                         |  |   |  |   | <br>Presence<br>           | Description |      |
|------|---------------------------------------------------------------------------------|--|---|--|---|----------------------------|-------------|------|
|      | -------------------------- ---------- ----------------------------------------- |  |   |  |   |                            |             |      |
|      | ---------------                                                                 |  |   |  |   |                            |             |      |
| <br> | Frame<br>Number                                                                 |  |   |  | M |                            | Start       | time |
|      | Slot Number                                                                     |  |   |  | M |                            | Start time  |      |
|      | Cell Index                                                                      |  | M |  |   | Identification of the Cell |             |      |

| UE index | M | Identification of the UE | | Mapping list number | M | The number of mapping list | | Mapping list(QFI, RB id) | M | Identification of the mapping between<br>QFI and RB id |

### <span id="page-144-2"></span>12.1.2 DRB Release

#### \*\*Table 12-3 RRC-SDAP DRB release message contents\*\*

| Element          |   | Presence   Description                                         |  |
|------------------|---|----------------------------------------------------------------|--|
|                  |   | -------------- ---------- ------------------------------------ |  |
| Frame Number   M |   | Start time                                                     |  |
| Slot Number   M  |   | Start time                                                     |  |
| Cell Index       | M | Identification of the Cell                                     |  |
| UE index         | M | Identification of the UE                                       |  |
| DRB id           | M | Identification of the Released DRB                             |  |

### <span id="page-144-3"></span>12.2 SDAP-PDCP Interface

#### \*\*Table 12-4 SDAP-PDCP Interface\*\*

| Direction                                                                       | Message/API |  |                               |  | Description |  |
|---------------------------------------------------------------------------------|-------------|--|-------------------------------|--|-------------|--|
|                                                                                 |             |  |                               |  |             |  |
| -------------- ----------------------------- ---------------------------------- |             |  |                               |  |             |  |
| -------------------------------------------                                     |             |  |                               |  |             |  |
| SDAP to PDCP   Transfer data PDU (DL)                                           |             |  | Transfer of SDAP PDU (with or |  |             |  |
| without SDAP header) in<br>downlink direction                                   |             |  |                               |  |             |  |
| PDCP to SDAP   Transfer data PDU (UL)                                           |             |  | Transfer of SDAP PDU (with or |  |             |  |
| without SDAP header) in up<br>link direction                                    |             |  |                               |  |             |  |
| SDAP to PDCP   End-marker control PDU (DL)   Control PDU (only SDAP header) to  |             |  |                               |  |             |  |
| indicate end of mapping of<br>QoS flow                                          |             |  |                               |  |             |  |

![](\_page\_145\_Picture\_1.jpeg)

The detailed description of SDAP-PDCP APIs is below:

#####################################SPEC NODE END############################ # SPEC 058: 12.2.1 Transfer Data PDU (DL) #####################################SPEC NODE START############################ ## <span id="page-145-0"></span>12.2.1 Transfer Data PDU (DL)

#### \*\*Table 12-5 SDAP-PDCP Transfer Data PDU (DL) message contents\*\*

| Element                                                                          |  |   |   | Presence |
|----------------------------------------------------------------------------------|--|---|---|----------|
| Description                                                                      |  |   |   |          |
| ----------------------------------------------------------- ---------- --------  |  |   |   |          |
| --------------------------------------------------- <br>  Frame Number           |  | M |   | Start    |
| time                                                                             |  |   |   |          |
| Slot Number                                                                      |  | M |   | Start    |
| time                                                                             |  |   |   |          |
| Cell Index                                                                       |  |   | M |          |
| Identification of the Cell                                                       |  |   |   |          |
| SDAP PDU number                                                                  |  | M |   | PDU      |
| number                                                                           |  |   |   |          |
| SDAP PDU info (UE index, DRB id,<br>PDU length, PDU data)   M                    |  |   |   |          |
| Identification of the UE, PDU length<br>and SDAP PDU data                        |  |   |   |          |
| ### <span id="page-145-1"></span> 12.2.2 Transfer Data PDU (UL)                  |  |   |   |          |
| #### **Table 12-6 SDAP-PDCP Transfer Data PDU (UL) message contents**            |  |   |   |          |
| Element                                                                          |  |   |   | Presence |
| Description                                                                      |  |   |   |          |
| ----------------------------------------------------------- ---------- --------  |  |   |   |          |
| ---------------------------------------------------                              |  |   |   |          |
| Frame Number                                                                     |  | M |   | Start    |
| time                                                                             |  |   |   |          |
| Slot Number                                                                      |  | M |   | Start    |
| time                                                                             |  |   |   |          |
| Cell Index                                                                       |  |   | M |          |
| Identification of the Cell                                                       |  |   |   |          |
| SDAP PDU number                                                                  |  | M |   | PDU      |
| number                                                                           |  |   |   |          |
| SDAP PDU info (UE index, DRB id,<br>PDU length, PDU data)   M                    |  |   |   |          |
|                                                                                  |  |   |   |          |
| Identification of the UE, PDU length<br>and SDAP PDU data                        |  |   |   |          |
|                                                                                  |  |   |   |          |
| #####################################SPEC NODE END############################   |  |   |   |          |
| # SPEC 059: 12.2.3 End-marker Control PDU (DL)                                   |  |   |   |          |
| #####################################SPEC NODE START############################ |  |   |   |          |
| ## <span id="page-145-2"></span> 12.2.3 End-marker Control PDU (DL)              |  |   |   |          |
| #### **Table 12-7 SDAP-PDCP End-marker control PDU (UL) message contents**       |  |   |   |          |
|                                                                                  |  |   |   |          |

|--------------|----------|---------------------------------|

```
| Frame Number | M | Start time |
| Slot Number | M | Start time |
| Cell Index | M | Identification of the Cell |
| UE index | M | Identification of the UE |
| DRB id | M | Identification of the DRB |
| EndMarker | M | End of the QoS flow-DRB mapping |
```

```
![](_page_146_Picture_1.jpeg)
```

### <span id="page-146-0"></span>12.3 RRC-PDCP Interface

#### \*\*Table 12-8 RRC-PDCP Interface\*\*

```
| Direction | Message/API | Description 
|
|-------------|------------------------------|----------------------------------
------------|
| RRC to PDCP | PDCP entity establishment | To establish a PDCP entity for 
radio bearers |
| RRC to PDCP | PDCP entity re-establishment | To re-establish PDCP entity 
|
| RRC to PDCP | PDCP entity release | To release PDCP entity 
|
| RRC to PDCP | SRB Data Request | To Deliver SRB(s) Data from RRC 
to PDCP (DL) |
| PDCP to RRC | SRB Data Indication | To Deliver SRB(s) Data from PDCH 
to RRC (UL) |
```

The detailed description of RRC-PDCP APIs is below:

### <span id="page-146-1"></span>12.3.1 PDCP Entity Establishment

#### \*\*Table 12-9 RRC-PDCP PDCP entity establishment\*\*

|   |                                                                                                            |  | Element |
|---|------------------------------------------------------------------------------------------------------------|--|---------|
|   | Presence   Description<br> ------------------------------------------------------------------------------- |  |         |
|   | ------------------------------------------------------------------ ---------- --                           |  |         |
|   | -----------------------------------------------                                                            |  |         |
|   | Cell                                                                                                       |  | Index   |
| M | Identification of the Cell                                                                                 |  |         |
|   | UE                                                                                                         |  | index   |
| M | Identification of the UE                                                                                   |  |         |
|   | Frame                                                                                                      |  | Number  |

| M | Start time | | Slot Number | M | Start time | | RB number | M | The number of RB | | RB information list (Rb Id, logical<br>ChannelIdentity, RB type, discard<br>Timer, t-Reordering, SN Bit, header<br>Compression, securityConfig) | M | See RadioBearerConfig, PDCP-Config<br>in 38.331 |

#####################################SPEC NODE END############################ # SPEC 060: 12.3.2 PDCP Entity Re-establishment #####################################SPEC NODE START############################ # <span id="page-146-2"></span>12.3.2 PDCP Entity Re-establishment

#### \*\*Table 12-10 RRC-PDCP PDCP entity release\*\*

| Element          |   | Presence   Description                                 |  |  |  |  |  |
|------------------|---|--------------------------------------------------------|--|--|--|--|--|
|                  |   | -------------- ---------- ---------------------------- |  |  |  |  |  |
| Cell Index       | M | Identification of the Cell                             |  |  |  |  |  |
| UE index         | M | Identification of the UE                               |  |  |  |  |  |
| Frame Number   M |   | Start time                                             |  |  |  |  |  |
| Slot Number   M  |   | Start time                                             |  |  |  |  |  |

### <span id="page-146-3"></span>12.3.3 SRB Data Request

#### \*\*Table 12-11 RRC-PDCP SRB Data Request\*\*

| Element        | Presence   Description<br>                           |
|----------------|------------------------------------------------------|
|                | ------------ ---------- ---------------------------- |
| Cell Index   M | Identification of the Cell                           |

![](\_page\_147\_Picture\_1.jpeg)

| UE index | M | Identification of the UE | |----------------------------------------------------|---|---------------------- ----| | Frame Number | M | Start time | | Slot Number | M | Start time | | SRB PDU Number | M | The number of RB | | SRB PDU info(SRB id, data length,<br>SRB PDU data) | M | |

#####################################SPEC NODE END############################ # SPEC 061: 12.3.4 SRB Data Indication #####################################SPEC NODE START############################ # <span id="page-147-0"></span>12.3.4 SRB Data Indication

# | Element | Presence | Description | |----------------------------------------------------|----------|--------------- -------------| | Cell Index | M | Identification of the Cell | | UE index | M | Identification of the UE | | Frame Number | M | Start time | | Slot Number | M | Start time | | SRB PDU Number | M | The number of RB | | SRB PDU info(SRB id, data length,<br>SRB PDU data) | M | |

## #### \*\*Table 12-12 RRC-PDCP SRB Data Indication\*\*

```
### <span id="page-147-1"></span>12.4 SDAP-eGTPU Interface
```

## #### \*\*Table 12-13 SDAP-eGTPU APIs\*\*

| Direction | Message/API | Description | |------------------|-------------------------------|---------------------------- ----------------| | SDAP to<br>eGTPU | Transfer Data SDAP<br>SDU(UL) | Transfer of SDAP SDU in uplink direction | | eGTPU to<br>SDAP | Transfer Data SDAP<br>SDU(DL) | Transfer of SDAP SDU in downlink direction |

#####################################SPEC NODE END############################ # SPEC 062: 12.4.1 Transfer Data SDAP SDU (UL) #####################################SPEC NODE START############################ # <span id="page-147-2"></span>12.4.1 Transfer Data SDAP SDU (UL)

This message is sent by SDAP to transfer uplink data to eGTPU.

#### \*\*Table 12-14 SDAP-eGTPU Transfer Data SDAP SDU (UL) message contents\*\*

| Element            |   | Presence   Description                                          |  |
|--------------------|---|-----------------------------------------------------------------|--|
|                    |   | ---------------- ---------- ----------------------------------- |  |
| Cell index         | M | Identification of the Cell                                      |  |
| UE index           | M | Identification of the UE                                        |  |
| PDU Session id   M |   | Identification of the PDU Session                               |  |
| QFI                | M | QoS Flow Identifier                                             |  |

![](\_page\_148\_Picture\_1.jpeg)

|  | SDAP SDU data                           | M   SDAP SDU data |  |  |
|--|-----------------------------------------|-------------------|--|--|
|  | ----------------- --- ----------------- |                   |  |  |
|  | SDAP SDU length   M   SDAP SDU length   |                   |  |  |

#####################################SPEC NODE END############################ # SPEC 063: 12.4.2 Transfer Data SDAP SDU (DL) #####################################SPEC NODE START############################ # <span id="page-148-0"></span>12.4.2 Transfer Data SDAP SDU (DL)

This message is sent by eGTPU to transfer downlink data to SDAP.

#### \*\*Table 12-15 SDAP-eGTPU Transfer Data SDAP SDU (DL) message contents\*\*

| Element             |   | Presence   Description<br>                                       |
|---------------------|---|------------------------------------------------------------------|
|                     |   | ----------------- ---------- ----------------------------------- |
| Cell index          | M | Identification of the Cell<br>                                   |
| UE index            | M | Identification of the UE<br>                                     |
| PDU Session id   M  |   | Identification of the PDU Session                                |
| QFI                 | M | QoS Flow Identifier<br>                                          |
| SDAP SDU data       | M | SDAP SDU data<br>                                                |
| SDAP SDU length   M |   | SDAP SDU length<br>                                              |

### <span id="page-148-1"></span>12.4.3 PDCP-eGTPU Interface

#### #### \*\*Table 12-16 PDCP-eGTPU APIs\*\*

|  | Direction                                                                       | Message/API |  |  | Description |  |
|--|---------------------------------------------------------------------------------|-------------|--|--|-------------|--|
|  |                                                                                 |             |  |  |             |  |
|  | ------------------ ------------------------------- ---------------------------- |             |  |  |             |  |
|  | -----------------                                                               |             |  |  |             |  |
|  | PDCP to<br>eGTPU   Transfer Data PDCP<br>PDU(DL)   Transfer of PDCP PDU in      |             |  |  |             |  |

downlink direction. | | eGTPU to<br>PDCP | Transfer Data PDCP<br>PDU(UL) | Transfer of PDCP PDU in uplink direction |

#####################################SPEC NODE END############################ # SPEC 064: 12.4.4 Transfer Data PDCP PDU (DL) #####################################SPEC NODE START############################ ## <span id="page-148-2"></span>12.4.4 Transfer Data PDCP PDU (DL)

This message is sent by PDCP to eGTPU to transfer packets in downlink direction.

#### \*\*Table 12-17 PDCP-eGTPU Transfer Data PDCP PDU (DL) message contents\*\*

| Element             |   | Presence   Description                                    |  |
|---------------------|---|-----------------------------------------------------------|--|
|                     |   | ----------------- ---------- ---------------------------- |  |
| Cell index          | M | Identification of the Cell                                |  |
| UE index            | M | Identification of the UE                                  |  |
| DRB id              | M | Identification of the DRB                                 |  |
| PDCP PDU data       | M | PDCP PDU data                                             |  |
| PDCP PDU length   M |   | PDCP PDU length                                           |  |

![](\_page\_149\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 065: 12.4.5 Transfer Data PDCP PDU (UL) #####################################SPEC NODE START############################ # <span id="page-149-0"></span>12.4.5 Transfer Data PDCP PDU (UL)

This message is sent by eGTPU to PDPCP to transfer packets in uplink direction.

#### \*\*Table 12-18 eGTPU to PDCP Transfer Data PDCP PDU (UL) message contents\*\*

| Element             |   | Presence   Description                                    |  |
|---------------------|---|-----------------------------------------------------------|--|
|                     |   | ----------------- ---------- ---------------------------- |  |
| Cell index          | M | Identification of the Cell                                |  |
| UE index            | M | Identification of the UE                                  |  |
| DRB id              | M | Identification of the DRB                                 |  |
| PDCP PDU data       | M | PDCP PDU data                                             |  |
| PDCP PDU length   M |   | PDCP PDU length                                           |  |

### 12.5 Ciphering and Integrity Protection

<span id="page-149-1"></span>O-CU implements ciphering and integrity algorithms specified i[n \[9\]](#page-8-18) for signalling and data bearers. This may be implemented in software or in hardware for acceleration.

### 12.6 Header Compression

<span id="page-149-2"></span>The header compression protocol is based on the Robust Header Compression (ROHC) framework defined in RFC 5795. As specified i[n \[9\]](#page-8-18) the following profiles are supported.

| Profile Identifier   Usage |                           | Reference<br>                                              |
|----------------------------|---------------------------|------------------------------------------------------------|
|                            |                           | -------------------- ---------------- -------------------- |
| 0x0000                     | No compression   RFC 5795 |                                                            |
| 0x0001                     | RTP/UDP/IP                | RFC 3095, RFC 4815                                         |
| 0x0002                     | UDP/IP                    | RFC 3095, RFC 4815                                         |
| 0x0003                     | ESP/IP                    | RFC 3095, RFC 4815                                         |
| 0x0004                     | IP                        | RFC 3843, RFC 4815                                         |
| 0x0006                     | TCP/IP                    | RFC 6846<br>                                               |
| 0x0101                     | RTP/UDP/IP                | RFC 5225<br>                                               |
| 0x0102                     | UDP/IP                    | RFC 5225<br>                                               |
| 0x0103                     | ESP/IP                    | RFC 5225<br>                                               |
| 0x0104                     | IP                        | RFC 5225<br>                                               |

#### \*\*Table 12-19 Header compression profiles\*\*

#####################################SPEC NODE END############################ # SPEC 066: 13. Use-Cases Enhancements

#####################################SPEC NODE START############################ # <span id="page-149-3"></span>13. Use-Cases Enhancements

<span id="page-149-4"></span>Below section has been added to define few of the enhancements corresponding to the ORAN use cases document.

### 13.1 Non-GoB mMIMO optimization

This section details the \*Use case 6: Massive MIMO Beamforming Optimization\* as defined in [\[40\].](#page-9-14) This use case allows the operator to flexibly configure Massive MIMO system parameters by means of policies, configuration, or machine learning techniques to improve the wireless performance, coverage and the QoS.

In this method, the non-RT and near-RT RIC utilize the UE/BS channel condition, mobility, and measured performance data to assist in beamforming mode selection and dynamically generate the beamforming weights.

![](\_page\_150\_Picture\_1.jpeg)

Below diagram captures the flow of information between the PHY, L2 and near RT-RIC. Functionality such as ML training and application have not been captured in this document and is out of scope.

![](\_page\_150\_Figure\_3.jpeg)

#### \*\*Figure 13-1 Non-GoB mMIMO\*\*

Following RAN information data is identified to be shared with RIC/rApps for ML training and application.

- DL Synchronization Signal based Reference Signal Received Power (SS-RSRP)

- DL Synchronization Signal based Signal to Noise and Interference Ratio (SS-SINR)

- UL Sounding Reference Signal based Reference Signal Received Power (SRS-RSRP)

- Supported Non-GoB Beamforming Modes

No New API is to be defined for this. O1 parameters and KPIs used are detailed in section [11.2.1.](#page-50-1)

Communication with RIC/rApps over the E2 interface are defined in the service models and E2 interface specifications. Please refer to [\[42\]](#page-9-6) and [\[43\]](#page-9-7) more details.

[E2 Interface](#page-143-1) can be referred for more details. O-RAN.WG3.E2SM-KPM [40) and O-RAN.WG3.E2SM-RC [41] documents can be referred to for more details on the E2 service models used.

### 13.2 Shared O-RU

<span id="page-150-0"></span>This section details the \*Use case 20: Shared O-RU\* as defined in [\[40\].](#page-9-14) It allows deploying O-RU where below objectives could be achieved.

- 1. Enhanced scalability and/or enhance availability and/or enable accessspecific node deployments in fronthaul systems, where multiple O-DU nodes are deployed by a single operator and connected to a shared O-RU.

- 2. Enhanced sharing capabilities where multiple O-DU nodes are deployed by different operators and connected to a shared O-RU.

Proposed Use Cases:

- Single MNO, Hierarchical mode

- Single MNO, Hybrid mode

- Multiple MNO, Hierarchical mode
- Multiple MNO, Hybrid Mode
- Multiple MNO, Neutral Host

![](\_page\_151\_Picture\_1.jpeg)

Single MNO use cases may cover load-sharing or redundant-O-DU use cases, or multiple RAN types e.g., 4G + 5G. Multiple MNO use cases may cover O-RU sharing between two or more RAN operators.

- ![](\_page\_151\_Figure\_3.jpeg)
- \*\*Figure 13-2 Single MNO, Hierarchical mode\*\*
- ![](\_page\_151\_Figure\_5.jpeg)

\*\*Figure 13-3 Single MNO, Hybrid mode\*\*

![](\_page\_152\_Picture\_1.jpeg)

- ![](\_page\_152\_Figure\_2.jpeg)
- ![](\_page\_152\_Figure\_3.jpeg)
- ![](\_page\_152\_Figure\_4.jpeg)

\*\*Figure 13-5 Multiple MNO, Hybrid mode\*\*

![](\_page\_152\_Figure\_6.jpeg)

\*\*Figure 13-6 Multiple MNO, Neutral Host\*\*

![](\_page\_153\_Picture\_1.jpeg)

Static allocation of resources between O-DU nodes

- 1. Single Operator Use Case

- Active/Standby operation

- o Identical carrier configurations on separate O-DU nodes.

 - o The operation of the stand-by O-DU node is enhanced such that carrier configuration of the O-RU is omitted, which is instead performed only by the active O-DU node.

 - o The stand-by O-DU node subscribes to receive supervision notifications from the O-RU

- Scale in/Scale out operation

 - o SMO statically partitions O-RU resources between a set of candidate O-DU nodes.

 - o The SMO uses the O1 interface to either i) activate and configure or ii) de-activate.

- Access-centric configuration

 - o The SMO statically partitions O-RU resources between LTE and NR carriers. - 2. Multi-Operator Use Case

 - Shared Resource Operator (SRO)-H enters into an agreement with one or more SRO-Ts to offer access to the resources of a shared O-RU

Dynamic allocation of resources between O-DU nodes

- 1. Single Operator Use Case

 - Co-ordination of O-RU resources is performed by the Near RT-RIC or M-plane based on demand and performance for slices.

- 2. Multi-Operator Use Case

- FFS

#### O-DU Changes:

- 1. Configuration Impact

 - No additional O1 interface changes required as NRCellDU operationalState/administrativeState can be used to define ODU node in active or standby mode.

- 2. Functional Impact

 - Existing Netconf session can be used for supervision notifications and to determine the operational state of ODU nodes.

 - Standby ODU storing of the configuration and applying it once the state changes from standby to active.

- 3. Impact on S-Plane

- The requirements for S-Plane in the Shared O-RU application are unchanged.

### 13.3 RAN Analytics

<span id="page-153-0"></span>This section details the use case as defined in https://oranalliance.atlassian.net/wiki/spaces/MVPC/pages/2214658090/MVP-C+RAN+analytics+information+exposure+-+Phase+1+Approved

Purpose of the feature is to expose RAN analytics information to external applications or MEC.

![](\_page\_154\_Picture\_1.jpeg)

|

|

|

|

|

|

|

|

---|

| O-RAN | | External |---------------------------------------------|-----------|--------------------- | Near-RT RIC | O-CU/O-DU | Application Server/MEC | | RAN analytics information Request/Subscribe | | | <e2>&gt; RIC Subscription Request</e2> | | | <e2>&gt; RIC Subscription Response</e2> | | | <e2>&gt; RIC Indication</e2> | | | Data analysis | | | ML model inference | | | RAN analytics information Response/Notify | | | Near-RT RIC | O-CU/O-DU | Application Server/MEC |

```
| | | 
|
```

\*\*Figure 13-7 RAN performance Analytics Flow Diagram\*\*

Data expected to be retrieved by non-RT RIC

- Network level measurement

 - UE level radio channel information, mobility related metrics, e.g., CQI, SINR, MCS

 - L2 measurement report related to traffic patterns, e.g., throughput, latency, packets per-second, inter frame arrival time.

- RAN protocol stack status: e.g., PDCP buffer status.

- Cell level information: e.g., DL/UL PRB occupation rate

- QoE related measurement metrics collected from SMO.

- User traffic data
- Currently out of the scope of A1 or E2
- Data exposed by Near-RT RIC to application server.
- UE level information
- e.g., Predicted RAN performance or related information,
- Cell level information
- More information as needed.

### 13.4 RAN Slicing

<span id="page-154-0"></span>RAN Slicing allows a network operator to provide services tailored to customers' requirements. Network slice is defined as a logical network with a bundle of specified network services over a common network infrastructure. A single physical network is sliced into multiple virtual networks that can support different service types over a single RAN.

O-RAN defines multiple slicing use case:

Use Case 1: RAN Slice SLA Assurance

Use Case 2: Multi-vendor Slice

Use Case 3: NSSI Resource Allocation Optimization

![](\_page\_155\_Picture\_1.jpeg)

![](\_page\_155\_Figure\_2.jpeg)

\*\*Figure 13-8 O-RAN Reference Slicing Architecture\*\*

O-RAN reference slicing architecture includes slice management functions along with O-RAN architectural components.

<span id="page-155-0"></span>ODU configuration is defined in the document under respective sections including [11.2.4.2.3](#page-74-1) and [11.2.4.2.4.](#page-75-0)

### 13.5 Fronthaul M-Plane

The Lower-Layer Split M-plane(LLS-M) as defined by O-RAN FH specification, facilitates the initialization, configuration and management of the O-RU to support the stated functional split.

A NETCONF/YANG based M-Plane is used for supporting the management features including "start up" installation, software management, configuration management, performance management, fault management and file management towards the O-RU.

The M-Plane supports two architectural models:

Hierarchical model:

The O-RU is managed entirely by one or more O-DU(s) using a NETCONF based M-Plane interface.

Hybrid model:

The hybrid architecture enables one or more direct logical interface(s) between management system(s) and O-RU in addition to a logical interface between O-DU and the O-RU.

![](\_page\_156\_Picture\_1.jpeg)

![](\_page\_156\_Figure\_2.jpeg)

#### \*\*Figure 13-9 M-Plane Architecture\*\*

The M-Plane provides the following major functionalities to the O-RU. These features are implemented using the NETCONF provided functions.

- "Start-up" installation
- SW management
- Configuration management
- Performance management
- Fault Management
- File Management

### 13.6 Network Energy Savings

<span id="page-156-0"></span>The Network Energy Saving feature involves many RAN nodes in collecting RAN configuration and network performance data, controlling energy operation policy and energy saving action. NES AI/ML based rApp/xApp handles model training and inference operation. The O-DU interacts with OAM, Non-RT/Near-RT RIC and O-RU through O1, E2, and FH CUS-plane/M-Plane interface respectively.

![](\_page\_157\_Picture\_1.jpeg)

#####################################SPEC NODE END############################ # SPEC 067: 13.6.1 NES: RIC Control #####################################SPEC NODE START############################ ## <span id="page-157-0"></span>13.6.1 NES: RIC Control

The Near RT RIC configures and controls network energy savings on O-CU and O-DU using CCC (Cell Configuration and Control) service model, as described i[n \[44\].](#page-9-11) The O-NESPolicy RAN configuration structure contains the

following attributes

| <br>Information         | Element                                                                         |                    | Description                           |
|-------------------------|---------------------------------------------------------------------------------|--------------------|---------------------------------------|
|                         | --------------------- --------------------------------------------------------- |                    |                                       |
| ---                     |                                                                                 |                    |                                       |
| <br>policyType<br>      | <br>Policy                                                                      | indicates<br>ASM   | or<br>TRX<br>control                  |
| <br>antennaMaskName<br> | <br>Name<br>indicating                                                          | supported          | TX<br>control<br>mask                 |
| antennaMask<br>         | Antenna mask indicating on/off of antenna element                               |                    |                                       |
| sleepMode<br>           |                                                                                 |                    | ASM sleep mode type as defined by WG4 |
| <br>dataDir<br>         |                                                                                 | Applied<br>data    | direction:<br>DL/UL                   |
| symbolMask<br>applied   | Indicates OFDM symbols for which the sleep mode is                              |                    |                                       |
| slotMask<br>            | Indicates slots for which the sleep mode is applied                             |                    |                                       |
| <br>validDuration<br>   | <br>Indicates                                                                   | duration           | in<br>10<br>ms<br>units               |
| <br>esObjective<br>     |                                                                                 | Expected<br>energy | savings<br>target                     |

For the full description of energy savings using ASM or TRX control, please refer to [\[22\].](#page-9-2)

### <span id="page-157-1"></span>13.6.2 NES: PHY-MAC interactions

Within O-DU, the NES related information needs to be shared among L1 processing, L2 processing, and various interface processing functional blocks. The NES interface related information is divided into four categories: NES Configuration and Capability Information, NES RAN Performance Data, NES Operation Control, and NES Operation Status Info. The details of NES information are described in the following tables.

| Message Type                                                  | Parameters                                                                      |  |
|---------------------------------------------------------------|---------------------------------------------------------------------------------|--|
| Description                                                   | Notes<br>                                                                       |  |
|                                                               | --------------------------------- ----------------------------------------- --- |  |
| -------------------------------- ----------------------       |                                                                                 |  |
| energy-saving<br>capability-com   ST8-ready-message-supported |                                                                                 |  |
| Section Type 8, Ack/Nack support   O-RU->O<br>DU via FH       |                                                                                 |  |
| mon-info                                                      | sleep-duration-extension-supported                                              |  |

| L1->L2<br>                                                        |
|-------------------------------------------------------------------|
| emergency-wake-up-command-sup<br>ported                           |
| Support emergency M-plane wake up  <br>                           |
| trx-control-ca<br>pability-info   supported-trx-control-masks<br> |
| O-RU->O<br>DU via FH                                              |
| sleep-mode-type<br>                                               |
| L1->L2<br>                                                        |
| wake-up-duration<br>                                              |
| <br>                                                              |
| wake-up-duration-guaranteed<br>                                   |
| <br>                                                              |
| defined-duration-sleep-supported<br>                              |
| <br>                                                              |
| undefined-duration-sleep-supported<br>                            |
| <br>                                                              |
| sleep-mode-type<br>                                               |
| O-RU->O<br>DU via FH                                              |
| wake-up-duration<br>                                              |
| <br>                                                              |
|                                                                   |

\*\*Table 13-1 NES Configuration and Capability Info\*\*

![](\_page\_158\_Picture\_1.jpeg)

| wake-up-duration-guaranteed                                                    | Guaranteed wake up period    |  | L1->L2 |
|--------------------------------------------------------------------------------|------------------------------|--|--------|
| ------------------------------------ -------------------------------- -------- |                              |  |        |
| defined-duration-sleep-supported                                               | Support defined sleep period |  |        |
| undefined-duration-sleep-supported   Support undefined sleep period            |                              |  |        |

#### \*\*Table 13-2 NES RAN Performance Data\*\*

| <br>Message<br>Type                  |    | <br>Parameters<br> <br>Description                                               |
|--------------------------------------|----|----------------------------------------------------------------------------------|
| Notes                                |    |                                                                                  |
|                                      |    | ----------------------- ------------ ------------------------------------------  |
| -----------                          |    | ---------------------------------------------------------- --------------------- |
| RSRP measure<br>ments   RSRP         |    | Reference Signals spread over the full                                           |
| bandwidth;<br>RSRP<br>is<br>measured | in | decibels-milliwatts<br>(dBm)<br> <br>O-RU->O-DU                                  |
| via<br>FH<br>L1->L2                  |    |                                                                                  |
| RSRQ measure<br>ments   RSRQ         |    | RSRQ are indications of your signal                                              |
| performance                          |    | O-RU->O-DU                                                                       |
| via<br>FH<br>L1->L2                  |    |                                                                                  |
| SINR measure<br>ments                |    | Uses to give theoretical upper bounds on                                         |
| channel<br>cap                       |    | O-RU->O-DU                                                                       |

| via<br>FH<br>L1->L2 |     |     |                                            |
|---------------------|-----|-----|--------------------------------------------|
| CQI measure<br>ment | CQI |     | An indicator to reflect RF channel quality |
| L1->L2              |     |     |                                            |
| MCS Index           |     | MCS | Modulation and coding scheme               |
| L1 -> L2            |     |     |                                            |

#### \*\*Table 13-3 NES Operation Control\*\*

| Message Type | Parameters | Description | Notes | |--------------------------------|-----------------------|---------------------- -------|----------------------| | Cell/Carrier<br>Power Control | On/ Off | | O-DU->O<br>RU via FH | | | Pwr Off Start | Frame/sub frame/slot number | | | RF Channel Re<br>configuration | Enable/Disable | M0-M3 | O-DU->O<br>RU via FH | | | Activation Start Slot | Frame/sub frame/slot number | | | | Period | Number of slots | | | | Acknowledgement | | | | Advanced Sleep<br>Modes | On/Off | | O-DU->O<br>RU via FH | | | Sleep State | M0-M3 | | | | Sleep Start Slot | Frame/sub frame/slot number | | | | Sleep Period | Number of slots | | | | Acknowledgement | | |

#### \*\*Table 13-4 NES Operation Status Information\*\*

| Message Type   Parameters   Description |          |                                                                          | Notes |
|-----------------------------------------|----------|--------------------------------------------------------------------------|-------|
|                                         |          | -------------- ------------ ------------------------------------ ------- |       |
|                                         | NES Mode | Cell/Carrier Off, RF Channels; ASM                                       |       |

![](\_page\_159\_Picture\_1.jpeg)

| O-RU NES Sta | Sleep State | M0-M3 | |

| -------------- ------------- ------- -- |  |  |  |
|-----------------------------------------|--|--|--|
| tus                                     |  |  |  |
|                                         |  |  |  |

#####################################SPEC NODE END############################ # SPEC 068: 13.7 O-CU/O-DU Energy Optimization #####################################SPEC NODE START############################ # 13.7 O-CU/O-DU Energy Optimization

<span id="page-159-0"></span>In the early discussion, most of the energy saving measurements focused on the radio related operation which is the major energy consumption unit. To further achieve the green network goal, more measures can be taken on O-CU aand O-DU to reduce a significant portion of RAN energy cost while maintaining the wireless network performance. Efficient power management in O-CU/O-DU systems is essential for cost reduction and environmental sustainability. The following approaches are considered to optimize RAN system power utilization:

- 1. For CPU power management, Dynamic Voltage and Frequency Scaling (DVFS) is a technique to adjust CPU voltage and clock frequency dynamically based on workload. Lower frequencies during idle periods save power with optimal task allocation to cores, minimizing context switches and maximizing CPU utilization.

- 2. On Memory Power Optimization, adjusting memory clock speeds based on workload, results in power savins. It is also possible to limit memory bandwidth during low-demand periods to reduce power consumption.

- 3. For the system thermal control, adjusting fan speed based on system (include CPU and memory) temperatures. Overcooling wastes energy if it is not based on thermals condition. Turning off or reducing fan speed during low-load periods save energy.

In summary, a holistic approach that combines CPU power management, memory optimization, and intelligent fan control ensures energy-efficient O-CU/O-DU systems while maintaining performance and reliability.

#####################################SPEC NODE END############################ # SPEC 069: 13.7.1 O-CU/O-DU Power Management Architecture #####################################SPEC NODE START############################ ## <span id="page-159-1"></span>13.7.1 O-CU/O-DU Power Management Architecture

O-CU/O-DU power management architecture can be significantly enhanced by employing a centralized power manager that makes dynamic decisions based on power-saving policies, workload demands, and CPU utilization. This intelligent power manager continuously monitors the server's performance metrics and adjusts the operational states of the CPU and its cores accordingly, scaling down during low demand periods to conserve energy or ramping up during peak times to ensure performance. By applying power-saving policies, it can selectively idle or shut down underutilized cores, thus optimizing CPU power usage. Additionally, the power manager oversees memory power consumption by regulating memory frequency and voltage based on current workload requirements, ensuring that energy is not wasted on idle memory resources. Cooling fans are also controlled adaptively; their speeds are adjusted in real-time according to the thermal conditions, preventing unnecessary energy expenditure while maintaining optimal cooling. This power management architecture not only improves energy efficiency but also maintains the balance between performance and power consumption, leading to cost savings and a reduced environmental footprint for overall RAN system. The O-CU/O-DU power management architecture is described in [Figure 13-10.](#page-160-1) The architecture leverages the commercial off the shelf processor and memory devices to achieve the best performance with lower power consumption.

![](\_page\_160\_Picture\_1.jpeg)

![](\_page\_160\_Figure\_2.jpeg)

\*\*Figure 13-10 O-CU/O-DU Power Control Architecture\*\*

#####################################SPEC NODE END############################ # SPEC 070: 13.7.2 O-CU/O-DU Demand Based Power Management Flow #####################################SPEC NODE START############################ ## <span id="page-160-1"></span><span id="page-160-0"></span>13.7.2 O-CU/O-DU Demand Based Power Management Flow

Demand-based power management flow involves a continuous assessment of the O-CU/O-DU's workload and CPU utilization to dynamically adjust power usage for optimal efficiency. The process begins with real-time monitoring of workload demands and CPU activity levels. When the workload is low or CPU utilization drops, the power management system triggers adjustments to the Voltage Regulator Module (VRM) voltage, lowering it to decrease power consumption. In tandem, the CPU clock speed may be reduced to further conserve energy, aligning processing power with the current demand. This dual adjustment not only minimizes unnecessary power usage but also reduces heat generation, alleviating the load on cooling systems and contributing to overall energy savings. By fine-tuning these parameters on-the-fly, the RAN system can achieve a balance between maintaining performance standards and reducing power consumption, thereby enhancing operational efficiency and prolonging hardware lifespan.

[Figure 13-11](#page-161-1) shows the demand-based power management flow. the power control software may adjust CPU voltage and clock frequency dynamically based on workload.

![](\_page\_161\_Picture\_1.jpeg)

![](\_page\_161\_Figure\_2.jpeg)

Figure 13-11 Demand Based Power Management Flow

<span id="page-161-1"></span>CPU Turbo Mode is a feature found in modern processors that dynamically adjusts the clock speed of individual cores to enhance performance. It allows a processor core to temporarily exceed its base clock frequency when certain conditions are met (such as power and thermal headroom). When using turbo mode, the intention is fine-tuning for specific applications that benefit from higher clock speeds on certain cores; it can improve performance in workloads that don't utilize all cores equally.

Utilizing CPU C-states for power saving involves strategically transitioning the CPU into various low-power idle states when full performance is not needed. Each C-state represents a deeper level of power reduction, with C0 being the fully operational state and deeper states ( \$C1\$ , \$C2\$ , \$C3\$ , etc.) progressively reducing power consumption by shutting down more components. The transition into these states is based on workload conditions and CPU activity; when the CPU is idle, it can enter a deeper C-state to save energy. However, there are conditions and restrictions to consider, such as the wakeup time, which is the time required for the CPU to return to an active state (C0) from a deeper C-state. Deeper Cstates save more power but have longer wake-up times, which can affect performance if the CPU needs to quickly resume full activity. Thus, the power management system must balance the energy savings with the potential impact on responsiveness, ensuring that deeper C-states are used during extended idle periods while lighter states are used for shorter idles to maintain a responsive system. This careful management helps maximize power efficiency without compromising the performance demands of active workloads.

### <span id="page-161-0"></span>13.7.3 L1/L2 Collaboration on Power Management

In a RAN network, the interaction between the physical layer (L1) and the medium access control layer (L2) plays a crucial role in power saving strategies, especially based on varying workloads such as user numbers and time of day. The physical layer is responsible for the actual transmission and reception of data over the air interface, while the MAC layer handles the scheduling and management of these transmissions.

Interaction between L1 and L2 for Power Saving

![](\_page\_162\_Picture\_1.jpeg)

1. Monitoring and Reporting: The physical layer continuously monitors real-time network conditions, including the channel condition, reference signal quality. This information is periodically reported to the MAC layer.

2. Dynamic Scheduling: The MAC layer, using the data from L1, dynamically schedules resource allocation. During periods of low demand (e.g., fewer users or off-peak hours), the MAC layer can reduce the number of active physical resource blocks (PRBs), thereby instructing L1 to lower transmission power or deactivate certain components temporarily.

3. Sleep Modes and Deactivation: The MAC layer can instruct the physical layer to enter various sleep modes during periods of inactivity. For example, during nighttime or off-peak hours, the MAC scheduler can consolidate traffic to fewer base stations, allowing other base stations to enter deep sleep states, significantly saving power.

5. Wake-Up Mechanisms: To ensure a balance between power saving and performance, the physical layer must be equipped with fast wake-up mechanisms. The predictive algorithms to anticipate traffic surges based on historical data (e.g., increased user activity during specific times of the day) and can pre-emptively bring components out of sleep modes in preparation for higher loads.

6. Load Balancing: The MAC layer also performs load balancing by reallocating resources among cells based on realtime demand. By shifting the load to cells with more efficient power states or less congestion, the MAC layer can optimize overall power usage across the network.

By closely coordinating the activities between L1 and L2 based on real-time workload and user activity patterns, 5G networks can achieve significant power savings while maintaining the necessary quality of service. This dynamic and adaptive approach ensures that power usage is minimized during low-demand periods without compromising performance during high-demand times.

### ### 13.8 DMRS Beamforming

<span id="page-162-0"></span>The O-DU performs configuration of O-RU if DMRS beamforming is supported by O-DU and O-RU. The configuration parameters are described in [\[23\].](#page-9-15) In addition the O\\_DU processes the RRM and SINR measurements sent by O-RU. The processing of these measurement in O-DU MAC and scheduler and any algorithms used are implementation dependent.

```
![](_page_163_Picture_1.jpeg)
```

# <span id="page-163-0"></span>Annex A (Informative)

# <span id="page-163-1"></span>L1 APIs

| API | Description | |--------------------|---------------------------------------------------------- -------------------------------------------------------------------------------- ------| | FFT | Perform the FFT operation | | Layer demapping | Layer De-mapping for 5GNR providing support for a<br>single code word. The algorithm is defined in section<br>7.3.1.3 in TS38.211 [4] | | Channel estimation | Performance channel estimation based on the DMRS<br>symbols | | MIMO equalizer | 5G NR MIMO equalization algorithm | | Demodulation | Modulation demapper for 5GNR that conforms to sec<br>tion 5.1 in 3GPP TS38.211 [4] | | Descrambler | Descrambling procedure as defined in TS38.211 [4],<br>which takes a sequence of LLRs and descrambles them<br>based on a scramble code sequence | | Rate Dematching | LDPC rate dematching operation | | Polar Decoder | Polar Decoder 5G NR function | | LDPC Decoder | LDPC Decoder 5G NR function | | CRC Check | The CRC validate function. It calculates a CRC value<br>and then compares that value to the one at the end of the<br>data | | Beamforming | Perform the spatial combining of the data from antennas<br>to reduce the number of radio data streams | #### \*\*Table A-1 Uplink Module APIs\*\*

#### \*\*Table A-2 Layer Demapping Parameters\*\*

| Parameter Fields   Description |                                                 |
|--------------------------------|-------------------------------------------------|
|                                | ------------------ ---------------------------- |
|                                | Layer data size   The layer data length<br>     |
| Number of layers   Layer count |                                                 |

| Input Data | Layer demapping input data |

#### \*\*Table A-3 Channel Estimation API Parameters\*\*

| Parameter Fields   Description |                                         |
|--------------------------------|-----------------------------------------|
|                                | ------------------ -------------------- |
| Start PRB                      | PRB start position                      |
| Number of PRB                  | PRB counts<br>                          |

![](\_page\_164\_Picture\_1.jpeg)

|

| Start Rx Antenna | Start antenna number of contiguous antenna numbers | |-----------------------------|-------------------------------------------------

```
---|
| Number of Rx Antenna | Rx antenna count 
|
| Number of Layers | Layer count 
|
| Number of DMRS | Number of DMRS symbols per TTI 
|
| DMRS configuration type | DMRS configuration type 
|
| DMRS in slot | Slot contains the DMRS 
|
| First DMRS in Slot Position | Position in the slot of the first DMRS symbol 
|
| PUSCH symbols in TTI | Number of PUSCH symbols in the TTI 
|
| Received Data | Received DMRS Data from antennas 
|
| Reference DMRS | Reference DMRS used
```

#### <span id="page-164-0"></span>\*\*Table A-4 Downlink Module APIs\*\*

| API | Description | |----------------|-------------------------------------------------------------- ----------------------------------------------------------------------|

| Layer mapping | Layer mapping for 5GNR providing support for a single<br>code word. The algorithm is defined in section 7.3.1.3 in<br>TS38.211 [4] | | Demodulation | Modulation mapper for 5GNR that conforms to section<br>5.1 in 3GPP TS38.211 [4] |

| Scrambler | A.1.1 Scrambling procedure as defined in TS38.211 [4] | | Rate matching | LDPC rate dematching operation | | Polar Encoder | Polar Encoder 5G NR function | | LDPC Encoder | LDPC Encoder 5G NR function | | CRC Generation | The CRC generation function. It calculates a CRC value | | Beam Forming | Performs Beamforming function based on the selected<br>algorithm.

| Precoder | Precoder combines the information from beamforming<br>with several layers of subcarriers to create a set of an<br>tenna outputs. |

#### \*\*Table A-5 PRACH Module APIs\*\*

|

| API | Description | |-----------------|------------------------------------------------------------- ---------------------------------------------|

| PRACH ZC Gen | Generate root ZC sequence used in PRACH. The algo<br>rithm is defined in section 7.3.1.3 in TS38.211 [4] | | PRACH Detection | PRACH preamble detection and power spectrum |

![](\_page\_165\_Picture\_1.jpeg)

#### \*\*Table A-6 PBCH Module APIs\*\*

| API<br>  Description |                                                      |  |
|----------------------|------------------------------------------------------|--|
|                      | --------------- ------------------------------------ |  |
|                      | PBCH DMRS Gen   Generate the DMRS For PBCH message   |  |
| PBCH Gen             | Create Complete PBCH message                         |  |

# <span id="page-165-0"></span>Call Flows

### <span id="page-165-1"></span>F1 Startup and Cells Activation

Figure below describes F1 interface setup and cell enabling across O-CU and O-DU as specified in subclause 8.5 of 3GPP TS 38.401 [\[12\]](#page-8-8) when O-CU and O-DU nodes are brought up. The O-DU and its cells are configured by OAM in the pre-operational state.

![](\_page\_165\_Figure\_7.jpeg)

\*\*Figure A-1 F1 interface setup and cell enabling across O-CU and O-DU\*\*

### <span id="page-165-2"></span>UE registration

The following call flow depicts all the messages across interfaces and internal APIs for UE registration in 5G SA.

![](\_page\_166\_Picture\_1.jpeg)

| | O-DU | | O-CU | | NG-C | |-------------------------------------------|----------------------------------- ---------------------------------------------------------------------------|---- ---------------------------------------------------|---------------------------- ------------------------------------------------------------------|------------- ------------------------------------|------------------------------------------- ------------------| | UE<br>O-RU | PHY<br>MAC<br>SCH | RLC<br>F1AP | F1AP<br>PDCP | SDAP<br>RRC | AMF | | | <b>RACH Procedure</b> | | F1 Setup Procedure | | NG Setup Procedure | | 1.RRCSetup Request | 2. RX\_Data.indication (PUSCH)<br>3.UL HARQ Indication<br>4. UL CCCH Indication<br>7. UE Create Request (SRB) | 5. UE Create (SRB)<br>UE Create Response (SRB) | | | | | | 8.Add UE configuration Request<br>UE configuration Response (SRB)<br>UE Create Response (SRB) | | 11. INITIAL UL RRC MESSAGE TRANSFER<br>UL RRC MESSAGE TRANSFER<br>14.DL RRC MESSAGE TRANSFER | PDCP entity establishment (SRB) | | | 19.RRCSetup | 16.DL CCCH Request<br>DL\_TTI.request(DCI)<br>18.Tx\_Data.request(PDSCH) | | 15. DL RRC MESSAGE

TRANSFER | | | | | UL Grant / SR Procedure | | | | | | UE<br>O-RU<br>20. RRCSetup Complete (SRB) | O-DU<br>PHY<br>MAC<br>SCH | RLC<br>F1AP | O-CU<br>F1AP<br>PDCP | SDAP<br>RRC | NG-C<br>AMF | | | 21. RX\_Data.indication(PUSCH)<br>22.UL HARQ Indication<br>23. Data transfer (UL) | 24.UL RRC Message Transfer | 25.UL RRC MESSAGE TRANSFER<br>26.UL RRC Message Transfer | | | | | | | | 27. SRB Data Indication<br>30. SRB Data Request | 28. INITIAL UE MESSAGE<br>29. INITIAL CONNTEXT SETUP REQUES | | | UE Reconfiguration Request | 33. UE Reconfiguration<br>UE Reconfiguration Complete | 31. UE CONTEXT SETUP REQUEST<br>32. UE CONTEXT SETUP REQUEST | | | | | 36. Modify UE configuration Request<br>37.UE Reconfiguration Response<br>UE Reconfiguration Response | | | | | | | 42. Buffer status reporting (DL) | 39.DL RRC Message Transfer | 40. UE CONTEXT SETUP RESPONSE | | | ![](\_page\_167\_Picture\_1.jpeg) | | O-DU | | | | | | o-cu | | | | NG-C | |---|---------------------------------|--------------------------------|-------- ----------------------------|-----|---------------------------------|----------- -----------------|----------------------------|-------------------------------|- -----------------------------|----------------------------|------| | ш | O-RU | PHY | MAC | SCH | RLC | F1AP | F1AP | PDCP | SDAP | RRC | AMF | | | | | 42.RLC Buffer Status Info | | | | | | | | | | | | | \$\rightarrow\$ | | | | | 41. UE CONTEXT SETUP RESPONSE | | | | | | | | 43.BL Scheduling Information | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | 44. Schedule result reporting (DL) | | | | | | | | | | | | | | | | | | | | | | | | | | 45.Data transfer (DL) | | | | | | | | | | | | 46. DL\_TTI.request(DCI) | | | | | | | | | | | | | | | | | | | | | | | | | 48.SecurityModeCommand | 47. Tx\_Data.request(PDSCH) | | | | | | | | | | | | | 49. UCI.indication | | | | | | | | | | | | | | 50. DL HARQ Indication | | | | | | | | | | | | | | | | | | | | | | | | UL Grant / SR Procedure | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | 56.SecurityModeCommand Complete | | | | | | | | | | | | | | 57. RX\_Data.indication (PUSCH) | | | | | | | | | | | | | | 58.UL HARQ Indication | | | | | | | | | | | | | | | 59. RRC Message Delivery Report | | | | | | | | | | | 61. Data transfer (UL) | | | 60. RRC Delivery Report | | | | | | | | | | | | 62.UL RRC Message Transfer | | | | | | | | | | | | | | 53.UL RRC Message Transfer | | | | | | | | | | | | | | 64.UL RRC Message Fransfer | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | 65.SRB Data Indication | | | | | | | | | | | | | 66.PDCP entity establishment | | | | | | | | | | | | | | 67.QoS flow to DRB mapping | | | | | | | | | | | | \$\leftarrow\$ | | | | | | |

![](_page_223_Figure_0.jpeg)

| | | | | | | | 85. Data transfer (UL) | | | | | | | | | | | | | | | 86. RRC Message Delivery Report<br>87.UL RRC Message Transfer | | 88. RRC Delivery Report | | | | | | | | | | | | 89. UL RRC Message Transfer | | | | | | | | | | | | | | 90.UL RRC Message Transfer | | | | | | | | | | | | | | 91. SRB Data Indication | | | | | | | | | | | | | | | | 92. INITIAL CONNTEXT SETUP RESPONSE |

```
![](_page_168_Picture_1.jpeg)
```

#### \*\*Figure A-2 UE registration\*\*

## <span id="page-168-0"></span>RACH procedure

Figure [0](#page-168-0) shows the RACH procedure in UE registration call flow described in the previous section.

![](\_page\_168\_Figure\_5.jpeg)

\*\*Figure A-3 RACH procedure\*\*

### <span id="page-168-1"></span>SR procedure

The SR procedure call flow is depicted in Figure [0](#page-168-1)

- ![](\_page\_169\_Picture\_1.jpeg)
- ![](\_page\_169\_Figure\_2.jpeg)
- \*\*Figure A-4 SR procedure\*\*
- ## <span id="page-169-0"></span>UL Grant procedure

The UL Grant procedure call flow is depicted in Figure [0](#page-169-0)

- ![](\_page\_169\_Figure\_6.jpeg)
- \*\*Figure A-5 UL Grant Procedure\*\*
- ## <span id="page-169-1"></span>PDU Session Establishment
- PDU session establishment call flows are as shown in Figur[e 0](#page-169-1)
- ![](\_page\_170\_Picture\_1.jpeg)
- ![](\_page\_170\_Figure\_2.jpeg)
- ![](\_page\_170\_Figure\_3.jpeg)
- ![](\_page\_171\_Picture\_1.jpeg)
- # <span id="page-171-0"></span>Revision history

| <br>Date                                                                                       |                                                       |          | Revision |  | Description                                  |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------|----------|----------|--|----------------------------------------------|
|                                                                                                |                                                       |          |          |  |                                              |
| ------------ ---------- -------------------------------------------------------                |                                                       |          |          |  |                                              |
| --------------------------------------------------------------------------------<br>---------- |                                                       |          |          |  |                                              |
| 08/09/2019   v01.0.0   First published version for Base Station O-DU and O-CU                  |                                                       |          |          |  |                                              |
| Software                                                                                       | Architecture                                          |          |          |  | and<br>APIs                                  |
|                                                                                                |                                                       |          |          |  |                                              |
| 02/14/2020   v02.0.0                                                                           | <br>Added Physical Broadcast Channel, Physical Random |          |          |  |                                              |
| Access                                                                                         |                                                       | Channel, |          |  | L1                                           |
| <br> <br>                                                                                      | Tasks Processing Flow, Front Haul Module, O-DU Timing |          |          |  |                                              |
| Synchronization                                                                                |                                                       |          |          |  |                                              |
| <br> <br>                                                                                      |                                                       |          |          |  | <br>L2 and L3 APIs: Corrections and new APIs |
|                                                                                                |                                                       |          |          |  |                                              |

| | | MAC-Scheduler APIs: New APIs added to list. All APIs defined fully in this release. | | 11/09/2020 | v03.0.0 | L2/L3 API updates | | | | O1 interface and E2 interface description | | 08/07/2021 | v04.0.0 | <br>L2 APIs: Corrections and new APIs | | | | <br>MAC-Scheduler single API for DL scheduling information and L2 APIs correc<br>tion. | | | | <br>mMIMO configuration/functionalities added | | | | <br>Beamforming configuration updated in O1 and scheduling information | | | | <br>Added Cat A radio flow | | 11/08/2021 | v05.0.0 | <br>RAN slicing feature configuration/functionalities | | | | <br>Updated mobility section 8.2.2 Inter O-DU Handover within an O-CU. | | | | <br>Added Sections 5.11 O-DU Timing Synchronization and 5.12 Accelerator Ab<br>straction Layer (AAL) | | 23/03/2021 | V06.0.0 | <br>Rel-16 3gpp functionalities to support Massive MIMO feature. | | | | <br>Massive MIMO optimization feature configuration/functionalities (MPV-C). | | 7/18/2022 | 06.00.01 | Updated as per new TS template | | 7/20/2022 | 06.00.02 | Further cleanup as per template. Renumbered sections, tables and figures. | | 7/25/2022 | 06.00.03 | Final updates to sections: References, O-DU and O-CU interfaces | | 11/14/2022 | 08.00.01 | Final updates for November release. Added references to WG6 and WG11 specifications. |

| 03/22/2023 | 09.00.00 | Final updates for Mar 2023 Train. Incorporated contributions from TG1 and TG2 on mas<br>sive MIMO optimization. Fixed section numbering issues. | | 07/21/2023 | 10.00 | Final updates for Jul 2023 release. Incorporated TG1 and TG2 contributions. | | 11/20/2023 | 11.00 | Final update and WG voting revision for Nov 2023 release. Includes TG1 and TG2 contri | | | | butions. | | 03/21/2024 | 12.00 | Final update for Mar 2024 release. TG1 and TG2 contributions – updates to O-CU section | | | | and addition of section on network energy savings. Minor corrections in other sections. | | 07/18/2024 | 13.00 | Updates for July 2024 release. Updates to O-CU and O-DU power savings and NES sec<br>tions. | | 11/22/2024 | 14.00 | Updates for Nov 2024 release. Included DMRS beamforming description. Added latest<br>references to WG3 service models. | #####################################SPEC NODE END############################