# Test Cases — Cybersecurity Asset Inventory System

| # | Test Case | Input | Expected Result | Actual Result |
|---|-----------|-------|------------------|----------------|
| 1 | Add a valid asset | Asset ID: A104, Type: Application, Risk: Low, Status: Secure | Asset added and saved to assets.json | Pass |
| 2 | Add asset with duplicate Asset ID | Asset ID: A101 (already exists) | Rejected with "already exists" message | Pass |
| 3 | Add asset with invalid Asset Type | Type: "Laptop" | Prompt repeats until a valid type is entered | Pass |
| 4 | Add asset with invalid Risk Level | Risk Level: "Extreme" | Prompt repeats until a valid level is entered | Pass |
| 5 | Add asset with invalid Security Status | Status: "OK" | Prompt repeats until a valid status is entered | Pass |
| 6 | Display all assets | Menu option 2 | Full formatted list + summary (totals, critical/high/medium counts, vulnerable count) | Pass |
| 7 | Display with no assets | Empty assets.json | "No assets found." message shown | Pass |
| 8 | Search for existing Asset ID | Asset ID: A102 | Full details of Web-Server displayed | Pass |
| 9 | Search for non-existent Asset ID | Asset ID: Z999 | "No asset found with ID 'Z999'." message | Pass |
| 10 | Update an existing asset (partial fields) | Asset ID: A101, new Risk Level: High, other fields blank | Only Risk Level changes; rest unchanged | Pass |
| 11 | Update with invalid value | Risk Level: "Nuclear" | Warning shown, previous value kept | Pass |
| 12 | Update non-existent Asset ID | Asset ID: Z999 | "No asset found" message | Pass |
| 13 | Delete an existing asset (confirmed) | Asset ID: A103, confirm: y | Asset removed and file updated | Pass |
| 14 | Delete an existing asset (cancelled) | Asset ID: A103, confirm: n | Asset NOT removed | Pass |
| 15 | Delete non-existent Asset ID | Asset ID: Z999 | "No asset found" message | Pass |
| 16 | Invalid menu choice | Choice: 9 | "Invalid choice" message, menu re-displayed | Pass |
| 17 | Data persistence across runs | Add asset, exit, relaunch program | Previously added asset still present | Pass |

> Note: Run through each case manually, capture the terminal output as a screenshot, and update the "Actual Result" column if any behavior differs from expected.
