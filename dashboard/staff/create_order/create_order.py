import json
import os
import uuid

FOOD_FILE = "database/food_menu.json"
ORDER_FILE = "database/orders.json"
TABLE_FILE = "database/tables.json"


def load_food():
    if not os.path.exists(FOOD_FILE):
        return []

    with open(FOOD_FILE, "r") as file:
        return json.load(file)


def load_orders():
    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, "r") as file:
        return json.load(file)


def save_orders(order_list):
    with open(ORDER_FILE, "w") as file:
        json.dump(order_list, file, indent=4)


def load_tables():
    if not os.path.exists(TABLE_FILE):
        return []

    with open(TABLE_FILE, "r") as file:
        return json.load(file)


def save_tables(table_list):
    with open(TABLE_FILE, "w") as file:
        json.dump(table_list, file, indent=4)


def create_order():

    food_list = load_food()
    order_list = load_orders()

    if len(food_list) == 0:
        print("\nNo food items found.")
        return

    print("\n========== CREATE NEW ORDER ==========")

    # Select order type
    while True:
        print("\n1. Dine-In")
        print("2. Takeaway")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            order_type = "Dine-In"
            break

        elif choice == "2":
            order_type = "Takeaway"
            break

        else:
            print("\nInvalid choice. Please try again.")

    table_id = None

    # Table selection for Dine-In
    if order_type == "Dine-In":

        table_list = load_tables()
        available_tables = []

        for table in table_list:
            if table["status"] == "Available":
                available_tables.append(table)

        if len(available_tables) == 0:
            print("\nNo tables are available.")
            return

        print("\n========== AVAILABLE TABLES ==========")

        for table in available_tables:
            print(
                f"{table['table_id']} - "
                f"{table['table_type']} - "
                f"{table['seats']} seats"
            )

        while True:
            table_id = input("\nEnter Table ID: ").strip().upper()

            found = False

            for table in available_tables:
                if table["table_id"] == table_id:
                    found = True
                    break

            if found:
                break

            print("\nThis table is not available.")

    # Show food menu
    print("\n========== FOOD MENU ==========")

    for food in food_list:
        print(
            f"{food['item_id']} - "
            f"{food['name']} - "
            f"₹{food['price']}"
        )

    # Select food
    item_id = input("\nEnter Food Item ID: ").strip().upper()

    selected_food = None

    for food in food_list:
        if food["item_id"] == item_id:
            selected_food = food
            break

    if selected_food is None:
        print("\nFood item not found.")
        return

    # Quantity
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("\nQuantity must be greater than 0.")
            else:
                break

        except ValueError:
            print("\nPlease enter a valid quantity.")

    price = float(selected_food["price"])
    total = price * quantity

    order_id = str(uuid.uuid4())[:10]

    new_order = {
    "order_id": order_id,
    "order_type": order_type,
    "table_id": table_id,
    "items": [
        {
            "item_id": selected_food["item_id"],
            "food_name": selected_food["name"],
            "quantity": quantity,
            "price": price,
            "total": total
        }
    ],
    "total": total,
    "status": "Pending"
}
    order_list.append(new_order)
    save_orders(order_list)

    # Book table for Dine-In
    if order_type == "Dine-In":

        table_list = load_tables()

        for table in table_list:
            if table["table_id"] == table_id:
                table["status"] = "Occupied"
                break

        save_tables(table_list)

    # Order confirmation
    print("\n========== ORDER CREATED ==========")
    print("Order ID   :", order_id)
    print("Order Type :", order_type)

    if order_type == "Dine-In":
        print("Table ID   :", table_id)

    print("Food       :", selected_food["name"])
    print("Quantity   :", quantity)
    print("Total      : ₹", total)
    print("Status     : Pending")

    if order_type == "Dine-In":
        print("Table Status: Occupied")