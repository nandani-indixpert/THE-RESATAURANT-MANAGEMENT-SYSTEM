from controller.menu import (
    add_menu_item,
    get_all_menu_items,
    update_menu_item,
    delete_menu_item,
)


def menu_management():
    while True:
        print("\n--- MENU MANAGEMENT ---")
        print("1. Add Food Item")
        print("2. View All Items")
        print("3. Update Food Item")
        print("4. Delete Food Item")
        print("5. Back to Main Dashboard")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            print("\n--- Add Food Item ---")
            item_id = input("Enter Item ID: ")
            name = input("Enter Item Name: ")
            category = input("Enter Category (e.g. Veg, Italian, Chinese): ")
            price = input("Enter Price: ")

            status, msg = add_menu_item(item_id, name, category, price)
            print(msg)

        elif choice == "2":
            print("\n--- RESTAURANT MENU ---")
            items = get_all_menu_items()

            if not items:
                print("Menu is empty!")
            else:
                for item in items:
                    print(
                        f"ID: {item['item_id']} | Name: {item['name']} | Category: {item['category']} | Price: Rs.{item['price']}"
                    )

        elif choice == "3":
            print("\n--- Update Food Item ---")
            item_id = input("Enter Item ID to update: ")
            name = input("Enter New Name: ")
            category = input("Enter New Category: ")
            price = input("Enter New Price: ")

            status, msg = update_menu_item(item_id, name, category, price)
            print(msg)

        elif choice == "4":
            print("\n--- Delete Food Item ---")
            item_id = input("Enter Item ID to delete: ")

            status, msg = delete_menu_item(item_id)
            print(msg)

        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")