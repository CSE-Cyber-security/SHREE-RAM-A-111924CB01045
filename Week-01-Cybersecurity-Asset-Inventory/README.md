# Week 01 — Cybersecurity Asset Inventory System

## Problem Statement
An organization maintains several IT assets such as computers, servers, routers, switches, and
software applications. Managing these assets manually makes it difficult to identify the assets,
track their security status, and determine which assets require immediate attention.

This system allows a security administrator to **add, search, update, delete, and display**
information about the organization's IT assets, classifying each one by asset type and security
risk level.

## Features
- Add new assets with full input validation (Asset Type, Risk Level, Security Status must match
  a predefined set of allowed values)
- Display all assets in a formatted report, including a summary of:
  - Total assets
  - Critical / High / Medium risk asset counts
  - Vulnerable asset count
- Search for an asset by Asset ID
- Update any field of an existing asset (partial updates supported — leave blank to keep current value)
- Delete an asset (with confirmation prompt)
- Data is persisted to `data/assets.json` between runs

## Asset Fields
| Field | Description |
|---|---|
| Asset ID | Unique identifier |
| Asset Name | Descriptive name |
| Asset Type | Workstation / Server / Router / Switch / Application |
| IP Address | Network address |
| Operating System | OS running on the asset |
| Owner/Department | Responsible department |
| Risk Level | Low / Medium / High / Critical |
| Security Status | Secure / Warning / Vulnerable |

## How to Run
```bash
cd src
python asset_inventory.py
```

Requires Python 3.6+. No external dependencies.

## Project Structure
```
Week-01-Cybersecurity-Asset-Inventory/
├── src/
│   └── asset_inventory.py
├── data/
│   └── assets.json
├── tests/
│   └── test_cases.md
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
└── README.md
```

## Sample Output
```
=========================================
 CYBERSECURITY ASSET INVENTORY
=========================================
Asset ID    : A101
Asset Name  : HR-PC-01
Asset Type  : Workstation
IP Address  : 192.168.1.10
OS          : Windows 11
Department  : HR
Risk Level  : Medium
Status      : Secure
-----------------------------------------
Asset ID    : A102
Asset Name  : Web-Server
Asset Type  : Server
IP Address  : 192.168.1.20
OS          : Ubuntu
Department  : IT
Risk Level  : Critical
Status      : Vulnerable
-----------------------------------------
Asset ID    : A103
Asset Name  : Core-Router
Asset Type  : Router
IP Address  : 192.168.1.1
OS          : Cisco IOS
Department  : Network
Risk Level  : High
Status      : Warning
-----------------------------------------
=========================================
Total Assets       : 3
Critical Assets    : 1
High Risk Assets   : 1
Medium Risk Assets : 1
Vulnerable Assets  : 1
=========================================
```
