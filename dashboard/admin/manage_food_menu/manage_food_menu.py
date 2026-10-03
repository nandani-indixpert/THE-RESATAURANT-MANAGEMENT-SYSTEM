from dashboard.admin.manage_food_menu.add_food import add_food
from dashboard.admin.manage_food_menu.view_food import view_food
from dashboard.admin.manage_food_menu.update_food import update_food
from dashboard.admin.manage_food_menu.delete_food import delete_food
def manage_food_menu():
    while True:

        print("\n========== MANAGE FOOD MENU ==========")
        print("1. Add Food")
        print("2. View Food")
        print("3. Update Food")
        print("4. Delete Food")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_food()

        elif choice == "2":
            view_food()

        elif choice == "3":
            update_food()

        elif choice == "4":
            delete_food()

        elif choice == "5":
            return

        else:
            print("Invalid choice.")