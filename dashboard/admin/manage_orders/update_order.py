from utils.logger import log_info,log_warning
import json
import os


ORDER_FILE = "database/orders.json"


def load_orders():

    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, "r") as file:
        return json.load(file)


def save_orders(order_list):

    with open(ORDER_FILE, "w") as file:
        json.dump(order_list, file, indent=4)


def update_order():

    order_list = load_orders()

    if len(order_list) == 0:
        print("\nNo orders found.")
        log_warning(f"Invalid order update attempt: {order_id}")
        return

    print("\n========== ORDERS ==========")

    for order in order_list:
        print(f"Order ID: {order['order_id']}")
        print(f"Status  : {order['status']}")
        print("-" * 30)

    order_id = input("\nEnter Order ID to update: ").strip()

    for order in order_list:

        if order["order_id"] == order_id:

            print("\n1. Update Status")
            print("2. Update Quantity")

            choice = input("Enter your choice: ")

            if choice == "1":

                status = input("Enter new status: ").strip()
                order["status"] = status

            elif choice == "2":

                for item in order["items"]:
                    print(
                        f"{item['item_id']} - "
                        f"{item['food_name']} x {item['quantity']}"
                    )

                item_id = input("Enter Item ID: ").strip().upper()

                for item in order["items"]:

                    if item["item_id"].upper() == item_id:

                        quantity = int(input("Enter new quantity: "))

                        item["quantity"] = quantity
                        item["total"] = float(item["price"]) * quantity

                        order["total"] = sum(
                            item["total"] for item in order["items"]
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
            log_info(f"Order updated: {order_id}")
            return

    print("\nOrder ID not found.")