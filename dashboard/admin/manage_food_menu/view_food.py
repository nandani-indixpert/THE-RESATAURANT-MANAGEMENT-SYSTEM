from utils.logger import log_info,log_warning
import json
import os


FOOD_FILE = "database/food_menu.json"


def load_food():
    if not os.path.exists(FOOD_FILE):
        return []

    with open(FOOD_FILE, "r") as file:
        return json.load(file)


def view_food():

    food_list = load_food()

    if len(food_list) == 0:
        print("\nNo food found.")
        return

    print("\n========== FOOD MENU ==========")

    for food in food_list:
        print(f"Item ID  : {food['item_id']}")
        print(f"Name     : {food['name']}")
        print(f"Category : {food['category']}")
        print(f"Price    : ₹{food['price']}")
        print("-" * 40)

    log_info("Food menu viewed.")