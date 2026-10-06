from utils.logger import log_info, log_warning
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

    item_number = 1

    while True:

        new_id = f"I{item_number:03d}"

        found = False

        for food in food_list:
            if food["item_id"] == new_id:
                found = True
                break

        if found == False:
            item_id = new_id
            break

        item_number += 1

    name = input("Enter food name: ").strip()

    if name == "":
        print("\nFood name cannot be empty.")
        log_warning("Attempt to add food with empty name.")
        return

    for food in food_list:

        if food["name"].strip().lower() == name.lower():
            print("\nThis food item already exists.")
            log_warning(f"Duplicate food attempt: {name}")
            return

    print("\nSelect Category:")
    print("1. Indian Classics")
    print("2. Tandoor & Kebabs")
    print("3. Chinese & Asian")
    print("4. Biryani & Rice")
    print("5. Vegetarian Delights")
    print("6. Non-Vegetarian Delights")
    print("7. Sweet Temptations")
    print("8. Refreshments")
    print("9. Chef's Combos")
    print("10. Starters & Soups")
    print("11. Add New Category")

    choice = input("Enter your choice: ").strip()

    categories = [
        "Indian Classics",
        "Tandoor & Kebabs",
        "Chinese & Asian",
        "Biryani & Rice",
        "Vegetarian Delights",
        "Non-Vegetarian Delights",
        "Sweet Temptations",
        "Refreshments",
        "Chef's Combos",
        "Starters & Soups"
    ]

    if choice.isdigit() and 1 <= int(choice) <= 10:

        category = categories[int(choice) - 1]

    elif choice == "11":

        category = input("Enter new category: ").strip()

        if category == "":
            print("\nCategory cannot be empty.")
            log_warning("Attempt to add food with empty category.")
            return

    else:

        print("\nInvalid category choice.")
        log_warning("Invalid food category choice.")
        return

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