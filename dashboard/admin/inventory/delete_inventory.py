import json
import os


INVENTORY_FILE = "database/inventory.json"


def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return []

    with open(INVENTORY_FILE, "r") as file:
        return json.load(file)


def save_inventory(inventory_list):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory_list, file, indent=4)


def delete_inventory():

    inventory_list = load_inventory()

    if len(inventory_list) == 0:
        print("\nNo inventory found.")
        return

    print("\n========== INVENTORY LIST ==========")

    for item in inventory_list:
        print(
            f"{item['inventory_id']} - "
            f"{item['item_name']} - "
            f"{item['quantity']} {item['unit']}"
        )

    inventory_id = input(
        "\nEnter Inventory ID to delete: "
    ).strip().upper()

    for item in inventory_list:

        if item["inventory_id"].upper() == inventory_id:

            inventory_list.remove(item)
            save_inventory(inventory_list)

            print("\nInventory deleted successfully.")
            return

    print("\nInventory ID not found.")