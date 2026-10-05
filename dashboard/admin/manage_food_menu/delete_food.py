from utils.logger import log_info,log_warning
import json
import os


FOOD_FILE = "database/food_menu.json"


def load_food():
    if not os.path.exists(FOOD_FILE):
        return []

    with open(FOOD_FILE, "r") as file:
        return json.load(file)


def save_food(food_list):
    with open(FOOD_FILE, "w") as file:
        json.dump(food_list, file, indent=4)


def delete_food():

    food_list = load_food()

    if len(food_list) == 0:
        print("\nNo food found.")
        return

    print("\n========== FOOD MENU ==========")

    for food in food_list:
        print(f"{food['item_id']} - {food['name']}")

    item_id = input("\nEnter Item ID to delete: ").strip().upper()

    for food in food_list:

        if food["item_id"].upper() == item_id:

            food_list.remove(food)
            save_food(food_list)

            print("\nFood deleted successfully.")
            log_info(f"Food deleted : {item_id}")
            return

    print("\nItem ID not found.")
    log_warning(f"Invalid food delete attempt : {item_id}")