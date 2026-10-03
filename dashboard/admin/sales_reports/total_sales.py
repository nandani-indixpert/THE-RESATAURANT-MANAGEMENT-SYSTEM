import json
import os


ORDER_FILE = "database/orders.json"


def load_orders():

    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, "r") as file:
        return json.load(file)


def total_sales():

    order_list = load_orders()

    if len(order_list) == 0:
        print("\nNo orders found.")
        return

    total_sales = 0
    total_orders = 0

    for order in order_list:

        total_sales = total_sales + float(order["total"])
        total_orders = total_orders + 1

    print("\n========== TOTAL SALES ==========")
    print(f"Total Orders : {total_orders}")
    print(f"Total Sales  : ₹{total_sales}")