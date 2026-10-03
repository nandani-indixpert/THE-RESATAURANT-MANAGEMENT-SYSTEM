import json
import os


ORDER_FILE = "database/orders.json"


def load_orders():

    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, "r") as file:
        return json.load(file)


def order_report():

    order_list = load_orders()

    if len(order_list) == 0:
        print("\nNo orders found.")
        return

    pending = 0
    completed = 0
    cancelled = 0

    for order in order_list:

        status = order["status"].lower()

        if status == "pending":
            pending = pending + 1

        elif status == "completed":
            completed = completed + 1

        elif status == "cancelled":
            cancelled = cancelled + 1

    print("\n========== ORDER REPORT ==========")
    print(f"Pending Orders   : {pending}")
    print(f"Completed Orders : {completed}")
    print(f"Cancelled Orders : {cancelled}")
    print(f"Total Orders     : {len(order_list)}")