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


def delete_order():

    order_list = load_orders()

    if len(order_list) == 0:
        print("\nNo orders found.")
        return

    print("\n========== ORDERS ==========")

    for order in order_list:
        print(f"Order ID: {order['order_id']}")
        print(f"Status  : {order['status']}")
        print("-" * 30)

    order_id = input("\nEnter Order ID to delete: ").strip()

    for order in order_list:

        if order["order_id"] == order_id:

            order_list.remove(order)
            save_orders(order_list)

            print("\nOrder deleted successfully.")
            return

    print("\nOrder ID not found.")