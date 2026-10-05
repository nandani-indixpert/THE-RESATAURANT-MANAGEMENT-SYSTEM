from utils.logger import log_info
import json
import os


ORDER_FILE = "database/orders.json"


def load_orders():

    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, "r") as file:
        return json.load(file)


def view_orders():

    order_list = load_orders()

    if len(order_list) == 0:
        print("\nNo orders found.")
        return

    print("\n========== ALL ORDERS ==========")

    for order in order_list:

        print(f"\nOrder ID : {order['order_id']}")
        print(f"Status   : {order['status']}")

        print("Items:")

        for item in order["items"]:
            print(
                f"  {item['food_name']} x {item['quantity']} "
                f"= ₹{item['total']}"
            )

        print(f"Total    : ₹{order['total']}")
        print("-" * 40)

    log_info("Order list viewed")