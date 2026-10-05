from utils.logger import log_info,log_warning
import json
import os
import uuid


FOOD_FILE = "database/food_menu.json"


def load_food():
    if not os.path.exists(FOOD_FILE):
        return []

    with open(FOOD_FILE, "r") as file:
        return json.load(file)


def save_food(food_list):
    with open(FOOD_FILE, "w") as file:
        json.dump(food_list, file, indent=4)


def add_food():

    food_list = load_food()

    print("\n========== ADD FOOD ==========")

    item_id = f"I{len(food_list) + 1:03d}"

    name = input("Enter food name: ").strip()
    if name == "":
        print("\nFood name cannot be empty.")
        log_warning("Attempt to add food with empty name.")
        return
    
    category = input("Enter category: ").strip()
    price = input("Enter food price: ").strip()

    food = {
        "id": str(uuid.uuid4())[:10],
        "item_id": item_id,
        "name": name,
        "category": category,
        "price": price
    }

    food_list.append(food)
    save_food(food_list)

    print("\nFood added successfully.")
    print(f"Item ID: {item_id}")
    log_info(f"Food added : {item_id} - {name}")

