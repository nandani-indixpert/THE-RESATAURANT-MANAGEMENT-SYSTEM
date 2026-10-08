import json
import os

ORDER_FILE = "database/orders.json"
TABLE_FILE = "database/tables.json"


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


def view_active_orders():

    order_list = load_orders()

    if len(order_list) == 0:
        print("\nNo orders found.")
        return

    print("\n========== ACTIVE ORDERS ==========")

    for order in order_list:

        print("\nOrder ID   :", order["order_id"])
        print("Order Type :", order["order_type"])

        if order["order_type"] == "Dine-In":
            print("Table ID   :", order["table_id"])
        else:
            print("Table ID   : -")

        print("Status     :", order["status"])

        print("Items:")

        for item in order["items"]:
            print(
                f"  {item['food_name']} x {item['quantity']} "
                f"= ₹{item['total']}"
            )

        print("Total      : ₹", order["total"])
        print("-" * 40)


def update_active_order():

    order_list = load_orders()

    if len(order_list) == 0:
        print("\nNo orders found.")
        return

    print("\n========== ORDERS ==========")

    for order in order_list:
        print(
            f"{order['order_id']} - "
            f"{order['order_type']} - "
            f"{order['status']}"
        )

    order_id = input("\nEnter Order ID: ").strip()

    for order in order_list:

        if order["order_id"] == order_id:

            print("\n1. Update Status")
            print("2. Update Quantity")

            choice = input("Enter your choice: ").strip()

            if choice == "1":

                print("\n1. Pending")
                print("2. Preparing")
                print("3. Completed")
                print("4. Cancelled")

                status_choice = input("Enter your choice: ").strip()

                if status_choice == "1":
                    order["status"] = "Pending"

                elif status_choice == "2":
                    order["status"] = "Preparing"

                elif status_choice == "3":
                    order["status"] = "Completed"

                elif status_choice == "4":
                    order["status"] = "Cancelled"

                else:
                    print("\nInvalid choice.")
                    return

                # Free table after order completion/cancellation
                if (
                    order["order_type"] == "Dine-In"
                    and order["status"] in ["Completed", "Cancelled"]
                ):

                    table_list = load_tables()

                    for table in table_list:
                        if table["table_id"] == order["table_id"]:
                            table["status"] = "Available"
                            break

                    save_tables(table_list)

            elif choice == "2":

                for item in order["items"]:
                    print(
                        f"{item['item_id']} - "
                        f"{item['food_name']} x {item['quantity']}"
                    )

                item_id = input("\nEnter Item ID: ").strip().upper()

                for item in order["items"]:

                    if item["item_id"].upper() == item_id:

                        try:
                            quantity = int(
                                input("Enter new quantity: ")
                            )

                            if quantity <= 0:
                                print("\nQuantity must be greater than 0.")
                                return

                        except ValueError:
                            print("\nPlease enter a valid quantity.")
                            return

                        item["quantity"] = quantity
                        item["total"] = float(item["price"]) * quantity

                        order["total"] = sum(
                            item["total"]
                            for item in order["items"]
                        )

                        break

                else:
                    print("\nItem ID not found.")
                    return

            else:
                print("\nInvalid choice.")
                return

            save_orders(order_list)

            print("\nOrder updated successfully.")
            return

    print("\nOrder ID not found.")


def active_orders():

    while True:

        print("\n========== ACTIVE ORDERS ==========")
        print("1. View Active Orders")
        print("2. Modify Order")
        print("3. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_active_orders()

        elif choice == "2":
            update_active_order()

        elif choice == "3":
            break

        else:
            print("\nInvalid choice.")