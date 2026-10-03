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


def update_food():

    food_list = load_food()

    if len(food_list) == 0:
        print("\nNo food found.")
        return

    print("\n========== FOOD MENU ==========")

    for food in food_list:
        print(f"{food['item_id']} - {food['name']}")

    item_id = input("\nEnter Item ID to update: ").strip().upper()

    for food in food_list:

        if food["item_id"].upper() == item_id:

            food["name"] = input("Enter new food name: ").strip()
            food["category"] = input("Enter new category: ").strip()
            food["price"] = input("Enter new price: ").strip()

            save_food(food_list)

            print("\nFood updated successfully.")
            return

    print("\nItem ID not found.")