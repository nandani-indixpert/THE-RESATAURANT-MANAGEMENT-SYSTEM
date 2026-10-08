from dashboard.admin.inventory.add_inventory import add_inventory
from dashboard.admin.inventory.view_inventory import view_inventory
from dashboard.admin.inventory.update_inventory import update_inventory
from dashboard.admin.inventory.delete_inventory import delete_inventory


def inventory():

    while True:

        print("\n========== INVENTORY MANAGEMENT ==========")
        print("1. Add Inventory")
        print("2. View Inventory")
        print("3. Update Inventory")
        print("4. Delete Inventory")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_inventory()

        elif choice == "2":
            view_inventory()

        elif choice == "3":
            update_inventory()

        elif choice == "4":
            delete_inventory()

        elif choice == "5":
            return

        else:
            print("Invalid choice.")