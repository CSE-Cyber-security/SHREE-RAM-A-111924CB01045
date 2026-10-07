"""
Cybersecurity Asset Inventory System
--------------------------------------
A menu-driven CLI tool to add, search, update, delete, and display
an organization's IT assets, classified by type, risk level, and
security status.

Data is persisted to data/assets.json.
"""

import json
import os

# ---------------------------------------------------------
# Configuration / constants
# ---------------------------------------------------------

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "assets.json")

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


# ---------------------------------------------------------
# Data persistence
# ---------------------------------------------------------

def load_assets():
    """Load assets from the JSON data file. Returns an empty list if missing/corrupt."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_assets(assets):
    """Persist the current asset list to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=4)


# ---------------------------------------------------------
# Input helpers / validation
# ---------------------------------------------------------

def prompt_choice(label, choices):
    """Prompt the user until they enter a value from `choices` (case-insensitive)."""
    choices_display = "/".join(choices)
    while True:
        value = input(f"{label} ({choices_display}): ").strip()
        for c in choices:
            if value.lower() == c.lower():
                return c
        print(f"  Invalid value. Please enter one of: {choices_display}")


def prompt_nonempty(label):
    """Prompt the user until they enter a non-empty string."""
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print("  This field cannot be empty.")


def asset_id_exists(assets, asset_id):
    return any(a["asset_id"].lower() == asset_id.lower() for a in assets)


def find_asset_index(assets, asset_id):
    for i, a in enumerate(assets):
        if a["asset_id"].lower() == asset_id.lower():
            return i
    return -1


# ---------------------------------------------------------
# Core operations
# ---------------------------------------------------------

def add_asset(assets):
    print("\n--- Add New Asset ---")
    asset_id = prompt_nonempty("Asset ID")
    if asset_id_exists(assets, asset_id):
        print(f"  Asset ID '{asset_id}' already exists. Add cancelled.\n")
        return

    asset = {
        "asset_id": asset_id,
        "asset_name": prompt_nonempty("Asset Name"),
        "asset_type": prompt_choice("Asset Type", ASSET_TYPES),
        "ip_address": prompt_nonempty("IP Address"),
        "os": input("Operating System: ").strip() or "N/A",
        "department": prompt_nonempty("Owner/Department"),
        "risk_level": prompt_choice("Risk Level", RISK_LEVELS),
        "security_status": prompt_choice("Security Status", SECURITY_STATUSES),
    }

    assets.append(asset)
    save_assets(assets)
    print(f"  Asset '{asset_id}' added successfully.\n")


def display_assets(assets):
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    if not assets:
        print("No assets found.")
        print("=========================================\n")
        return

    for a in assets:
        print(f"Asset ID    : {a['asset_id']}")
        print(f"Asset Name  : {a['asset_name']}")
        print(f"Asset Type  : {a['asset_type']}")
        print(f"IP Address  : {a['ip_address']}")
        print(f"OS          : {a['os']}")
        print(f"Department  : {a['department']}")
        print(f"Risk Level  : {a['risk_level']}")
        print(f"Status      : {a['security_status']}")
        print("-----------------------------------------")

    print_summary(assets)


def print_summary(assets):
    total = len(assets)
    critical = sum(1 for a in assets if a["risk_level"] == "Critical")
    high = sum(1 for a in assets if a["risk_level"] == "High")
    medium = sum(1 for a in assets if a["risk_level"] == "Medium")
    vulnerable = sum(1 for a in assets if a["security_status"] == "Vulnerable")

    print("=========================================")
    print(f"Total Assets       : {total}")
    print(f"Critical Assets    : {critical}")
    print(f"High Risk Assets   : {high}")
    print(f"Medium Risk Assets : {medium}")
    print(f"Vulnerable Assets  : {vulnerable}")
    print("=========================================\n")


def search_asset(assets):
    print("\n--- Search Asset ---")
    asset_id = prompt_nonempty("Enter Asset ID to search")
    idx = find_asset_index(assets, asset_id)

    if idx == -1:
        print(f"  No asset found with ID '{asset_id}'.\n")
        return

    a = assets[idx]
    print("\n-----------------------------------------")
    print(f"Asset ID    : {a['asset_id']}")
    print(f"Asset Name  : {a['asset_name']}")
    print(f"Asset Type  : {a['asset_type']}")
    print(f"IP Address  : {a['ip_address']}")
    print(f"OS          : {a['os']}")
    print(f"Department  : {a['department']}")
    print(f"Risk Level  : {a['risk_level']}")
    print(f"Status      : {a['security_status']}")
    print("-----------------------------------------\n")


def update_asset(assets):
    print("\n--- Update Asset ---")
    asset_id = prompt_nonempty("Enter Asset ID to update")
    idx = find_asset_index(assets, asset_id)

    if idx == -1:
        print(f"  No asset found with ID '{asset_id}'.\n")
        return

    a = assets[idx]
    print("Leave a field blank to keep its current value.")

    name = input(f"Asset Name [{a['asset_name']}]: ").strip()
    if name:
        a["asset_name"] = name

    atype = input(f"Asset Type [{a['asset_type']}] ({'/'.join(ASSET_TYPES)}): ").strip()
    if atype:
        for c in ASSET_TYPES:
            if atype.lower() == c.lower():
                a["asset_type"] = c
                break
        else:
            print("  Invalid asset type — keeping previous value.")

    ip = input(f"IP Address [{a['ip_address']}]: ").strip()
    if ip:
        a["ip_address"] = ip

    os_val = input(f"Operating System [{a['os']}]: ").strip()
    if os_val:
        a["os"] = os_val

    dept = input(f"Department [{a['department']}]: ").strip()
    if dept:
        a["department"] = dept

    risk = input(f"Risk Level [{a['risk_level']}] ({'/'.join(RISK_LEVELS)}): ").strip()
    if risk:
        for c in RISK_LEVELS:
            if risk.lower() == c.lower():
                a["risk_level"] = c
                break
        else:
            print("  Invalid risk level — keeping previous value.")

    status = input(f"Security Status [{a['security_status']}] ({'/'.join(SECURITY_STATUSES)}): ").strip()
    if status:
        for c in SECURITY_STATUSES:
            if status.lower() == c.lower():
                a["security_status"] = c
                break
        else:
            print("  Invalid security status — keeping previous value.")

    save_assets(assets)
    print(f"  Asset '{asset_id}' updated successfully.\n")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    asset_id = prompt_nonempty("Enter Asset ID to delete")
    idx = find_asset_index(assets, asset_id)

    if idx == -1:
        print(f"  No asset found with ID '{asset_id}'.\n")
        return

    confirm = input(f"Are you sure you want to delete '{asset_id}'? (y/n): ").strip().lower()
    if confirm == "y":
        del assets[idx]
        save_assets(assets)
        print(f"  Asset '{asset_id}' deleted successfully.\n")
    else:
        print("  Delete cancelled.\n")


# ---------------------------------------------------------
# Menu / main loop
# ---------------------------------------------------------

def print_menu():
    print("=========================================")
    print(" CYBERSECURITY ASSET INVENTORY SYSTEM")
    print("=========================================")
    print("1. Add Asset")
    print("2. Display All Assets")
    print("3. Search Asset")
    print("4. Update Asset")
    print("5. Delete Asset")
    print("6. Exit")
    print("=========================================")


def main():
    assets = load_assets()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            display_assets(assets)
        elif choice == "3":
            search_asset(assets)
        elif choice == "4":
            update_asset(assets)
        elif choice == "5":
            delete_asset(assets)
        elif choice == "6":
            print("Exiting Cybersecurity Asset Inventory System. Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter a number from 1 to 6.\n")


if __name__ == "__main__":
    main()
