from utils.logger import log_info
import json
import os
import uuid


INVENTORY_FILE = "database/inventory.json"


def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return []

    with open(INVENTORY_FILE, "r") as file:
        return json.load(file)


def save_inventory(inventory_list):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory_list, file, indent=4)


def add_inventory():

    inventory_list = load_inventory()

    print("\n========== ADD INVENTORY ==========")

    inventory_id = "INV" + str(len(inventory_list) + 1)

    item_name = input("Enter item name: ").strip()
    quantity = input("Enter quantity: ").strip()
    unit = input("Enter unit (kg/litre/pcs): ").strip()

    inventory = {
        "id": str(uuid.uuid4())[:10],
        "inventory_id": inventory_id,
        "item_name": item_name,
        "quantity": quantity,
        "unit": unit,
        "status": "Available"
    }

    inventory_list.append(inventory)
    save_inventory(inventory_list)

    print("\nInventory added successfully.")
    log_info(f"Inventory added: {inventory_id}")
    print(f"Inventory ID: {inventory_id}")