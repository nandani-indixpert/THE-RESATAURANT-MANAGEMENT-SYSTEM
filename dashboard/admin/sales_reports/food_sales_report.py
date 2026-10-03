import json
import os


ORDER_FILE = "database/orders.json"


def load_orders():

    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, "r") as file:
        return json.load(file)


def food_sales_report():

    order_list = load_orders()

    if len(order_list) == 0:
        print("\nNo orders found.")
        return

    food_sales = {}

    for order in order_list:

        for item in order["items"]:

            food_name = item["food_name"]
            quantity = int(item["quantity"])

            if food_name in food_sales:
                food_sales[food_name] = food_sales[food_name] + quantity

            else:
                food_sales[food_name] = quantity

    print("\n========== FOOD SALES REPORT ==========")

    for food_name, quantity in food_sales.items():
        print(f"{food_name} : {quantity}")