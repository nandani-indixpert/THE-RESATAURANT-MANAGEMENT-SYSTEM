from utils.logger import log_info
import json
import os


INVENTORY_FILE = "database/inventory.json"


def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return []

    with open(INVENTORY_FILE, "r") as file:
        return json.load(file)


def view_inventory():

    inventory_list = load_inventory()

    if len(inventory_list) == 0:
        print("\nNo inventory found.")
        return

    print("\n")
    print("╔══════════════╦══════════════════╦══════════╦══════════╦══════════════╗")
    print("║ INVENTORY ID ║ ITEM NAME        ║ QUANTITY ║ UNIT     ║ STATUS       ║")
    print("╠══════════════╬══════════════════╬══════════╬══════════╬══════════════╣")

    for item in inventory_list:
        print(
            f"║ {item['inventory_id']:<12} "
            f"║ {item['item_name']:<16} "
            f"║ {item['quantity']:<8} "
            f"║ {item['unit']:<8} "
            f"║ {item['status']:<12} ║"
        )

    print("╚══════════════╩══════════════════╩══════════╩══════════╩══════════════╝")

    log_info("Inventory list viewed.")