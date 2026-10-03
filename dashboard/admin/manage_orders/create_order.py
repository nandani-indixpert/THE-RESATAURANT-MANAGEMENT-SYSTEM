import json
import os
import uuid
import datetime


FOOD_FILE = "database/food_menu.json"
ORDER_FILE = "database/orders.json"


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


def create_order():

    food_list = load_food()

    if len(food_list) == 0:
        print("\nNo food found. Please add food first.")
        return

    print("\n========== FOOD MENU ==========")

    for food in food_list:
        print(
            f"{food['item_id']} - "
            f"{food['name']} - "
            f"₹{food['price']}"
        )

    items = []
    total = 0

    while True:

        item_id = input("\nEnter Item ID: ").strip().upper()

        selected_food = None

        for food in food_list:
            if food["item_id"].upper() == item_id:
                selected_food = food
                break

        if selected_food is None:
            print("\nItem ID not found.")
            continue

        quantity = int(input("Enter quantity: "))

        item_total = float(selected_food["price"]) * quantity

        item = {
            "item_id": selected_food["item_id"],
            "food_name": selected_food["name"],
            "quantity": quantity,
            "price": selected_food["price"],
            "total": item_total
        }

        items.append(item)

        total = total + item_total

        print(f"\n{selected_food['name']} added to order.")
        print(f"Current Total: ₹{total}")

        more = input("\nAdd another food? (y/n): ").strip().lower()

        if more != "y":
            break

    order = {
    "order_id": str(uuid.uuid4())[:10],
    "items": items,
    "total": total,
    "status": "Pending",
    "date": str(datetime.date.today())
}

    order_list = load_orders()
    order_list.append(order)
    save_orders(order_list)

    print("\n========== ORDER CREATED ==========")
    print(f"Order ID: {order['order_id']}")

    for item in items:
        print(
            f"{item['food_name']} x {item['quantity']} "
            f"= ₹{item['total']}"
        )

    print(f"Total: ₹{total}")