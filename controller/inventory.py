import json
import os

INVENTORY_FILE = "database/inventory.json"


# File se inventory load karne ke liye
def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return []
    try:
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    except:
        return []


# File me inventory save karne ke liye
def save_inventory(data):
    try:
        with open(INVENTORY_FILE, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except:
        return False


# 1. Naya Stock Item Add Karna
def add_inventory_item(item_id, item_name, quantity, unit, min_limit):
    inventory = load_inventory()

    # ID Check
    for item in inventory:
        if item["item_id"] == item_id:
            return False, "Item ID pehle se exist karti hai!"

    try:
        quantity = float(quantity)
        min_limit = float(min_limit)
    except:
        return False, "Quantity aur Min Limit numbers hone chahiye!"

    new_item = {
        "item_id": item_id,
        "item_name": item_name,
        "quantity": quantity,
        "unit": unit,  # e.g. kg, liter, packets, pcs
        "min_limit": min_limit,  # Kitne se kam hone par alert aaye
    }

    inventory.append(new_item)

    if save_inventory(inventory):
        return True, f"'{item_name}' inventory me successfully add ho gaya!"
    else:
        return False, "Save karne me error aaya!"


# 2. View All Stock
def get_all_inventory():
    return load_inventory()


# 3. Stock Quantity Update Karna (Restock / Add Quantity)
def update_stock_quantity(item_id, added_qty):
    inventory = load_inventory()

    try:
        added_qty = float(added_qty)
    except:
        return False, "Quantity valid number honi chahiye!"

    for item in inventory:
        if item["item_id"] == item_id:
            item["quantity"] += added_qty
            if save_inventory(inventory):
                return (
                    True,
                    f"Stock updated! Naya stock: {item['quantity']} {item['unit']}",
                )
            else:
                return False, "Save karne me fail ho gaya!"

    return False, "Item ID nahi mili!"


# 4. Low Stock Check Alert
def check_low_stock():
    inventory = load_inventory()
    low_stock_items = []

    for item in inventory:
        if item["quantity"] <= item["min_limit"]:
            low_stock_items.append(item)

    return low_stock_items