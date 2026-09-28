from controller.inventory import (
    add_inventory_item,
    check_low_stock,
    get_all_inventory,
    update_stock_quantity,
)


def inventory_management_menu():
    while True:
        print("\n=== INVENTORY MANAGEMENT ===")
        print("1. Add New Stock Item")
        print("2. View All Stock")
        print("3. Update/Restock Quantity")
        print("4. Check Low Stock Alerts")
        print("5. Back to Main Dashboard")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            print("\n--- Add New Stock Item ---")
            item_id = input("Enter Item ID (e.g. RAW101): ").strip()
            item_name = input(
                "Enter Item Name (e.g. Rice, Cooking Oil): "
            ).strip()
            quantity = input("Enter Initial Quantity: ").strip()
            unit = input("Enter Unit (kg, liters, pcs, packets): ").strip()
            min_limit = input("Enter Minimum Safety Limit (Alert Threshold): ").strip()

            status, msg = add_inventory_item(
                item_id, item_name, quantity, unit, min_limit
            )
            print(msg)

        elif choice == "2":
            print("\n--- CURRENT INVENTORY STOCK ---")
            inventory = get_all_inventory()
            if not inventory:
                print("Inventory abhi khali hai!")
            else:
                for item in inventory:
                    print(
                        f"ID: {item['item_id']} | Name: {item['item_name']} | Stock: {item['quantity']} {item['unit']} | Min Limit: {item['min_limit']}"
                    )

        elif choice == "3":
            print("\n--- Update / Restock Quantity ---")
            item_id = input("Enter Stock Item ID to Restock: ").strip()
            added_qty = input("Enter Quantity to Add: ").strip()

            status, msg = update_stock_quantity(item_id, added_qty)
            print(msg)

        elif choice == "4":
            print("\n--- LOW STOCK ALERTS ---")
            low_items = check_low_stock()
            if not low_items:
                print("✅ Sabhi items ka stock sufficient hai!")
            else:
                print("⚠️ WARNING: Ye items low stock me hain! Inhe kharido:")
                for item in low_items:
                    print(
                        f"⚠️ {item['item_name']} - Current Stock: {item['quantity']} {item['unit']} (Limit: {item['min_limit']})"
                    )

        elif choice == "5":
            break
        else:
            print("Invalid Choice! Try again.")