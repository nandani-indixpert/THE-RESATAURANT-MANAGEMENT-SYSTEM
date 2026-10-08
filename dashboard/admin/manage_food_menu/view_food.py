from utils.logger import log_info
import json
import os


FOOD_FILE = "database/food_menu.json"


def load_food():

    if not os.path.exists(FOOD_FILE):
        return []

    with open(FOOD_FILE, "r") as file:
        return json.load(file)


def print_category(category, food_list):

    items = []

    for food in food_list:
        if food["category"] == category:
            items.append(food)

    if len(items) == 0:
        return

    print()
    print("╔══════════════════════════════════════════════════╗")
    print(f"║{category.upper():^50}║")
    print("╠════════╦════════════════════════╦════════════════╣")
    print("║ ID     ║ ITEM NAME              ║ PRICE          ║")
    print("╠════════╬════════════════════════╬════════════════╣")

    for food in items:
        print(
            f"║ {food['item_id']:<6} "
            f"║ {food['name']:<22} "
            f"║ ₹{food['price']:<13} ║"
        )

    print("╚════════╩════════════════════════╩════════════════╝")


def view_food():

    food_list = load_food()

    if len(food_list) == 0:
        print("\nNo food found.")
        return

    categories = []

    for food in food_list:
        if food["category"] not in categories:
            categories.append(food["category"])

    for category in categories:
        print_category(category, food_list)

    log_info("Food menu viewed.")