import json

MENU_FILE = "database/menu.json"


# File se data load karne ke liye
def load_menu():
    try:
        with open(MENU_FILE, "r") as file:
            return json.load(file)
    except:
        return []


# File me data save karne ke liye
def save_menu(data):
    try:
        with open(MENU_FILE, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except:
        return False


# 1. Add New Item
def add_menu_item(item_id, name, category, price):
    menu = load_menu()

    # Check ID match
    for item in menu:
        if item["item_id"] == item_id:
            return False, "Item ID already exists!"

    try:
        price = float(price)
    except:
        return False, "Price must be a number!"

    new_item = {
        "item_id": item_id,
        "name": name,
        "category": category,
        "price": price,
    }

    menu.append(new_item)

    if save_menu(menu):
        return True, "Item added successfully!"
    else:
        return False, "Failed to save item!"


# 2. Get All Items
def get_all_menu_items():
    return load_menu()


# 3. Update Item
def update_menu_item(item_id, name, category, price):
    menu = load_menu()

    try:
        price = float(price)
    except:
        return False, "Price must be a number!"

    for item in menu:
        if item["item_id"] == item_id:
            item["name"] = name
            item["category"] = category
            item["price"] = price

            if save_menu(menu):
                return True, "Item updated successfully!"
            else:
                return False, "Failed to update item!"

    return False, "Item not found!"


# 4. Delete Item
def delete_menu_item(item_id):
    menu = load_menu()

    for item in menu:
        if item["item_id"] == item_id:
            menu.remove(item)

            if save_menu(menu):
                return True, "Item deleted successfully!"
            else:
                return False, "Failed to delete item!"

    return False, "Item not found!"