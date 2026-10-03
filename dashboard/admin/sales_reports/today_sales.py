import json
import os
import datetime


ORDER_FILE = "database/orders.json"


def load_orders():

    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, "r") as file:
        return json.load(file)


def today_sales():

    order_list = load_orders()

    if len(order_list) == 0:
        print("\nNo orders found.")
        return

    today = str(datetime.date.today())

    total_sales = 0
    total_orders = 0

    for order in order_list:

        if order["date"] == today:
            total_sales = total_sales + float(order["total"])
            total_orders = total_orders + 1

    print("\n========== TODAY'S SALES ==========")
    print(f"Date         : {today}")
    print(f"Total Orders : {total_orders}")
    print(f"Total Sales  : ₹{total_sales}")