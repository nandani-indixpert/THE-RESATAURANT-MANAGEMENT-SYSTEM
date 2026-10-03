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

    print("\n========== INVENTORY LIST ==========")

    for item in inventory_list:
        print(f"Inventory ID : {item['inventory_id']}")
        print(f"Item Name    : {item['item_name']}")
        print(f"Quantity     : {item['quantity']}")
        print(f"Unit         : {item['unit']}")
        print(f"Status       : {item['status']}")
        print("-" * 40)