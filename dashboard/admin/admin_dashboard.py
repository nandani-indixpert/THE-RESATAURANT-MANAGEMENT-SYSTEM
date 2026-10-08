from dashboard.admin.manage_food_menu.manage_food_menu import manage_food_menu
from dashboard.admin.manage_tables.manage_tables import manage_tables
from dashboard.admin.manage_staff.manage_staff import manage_staff
from dashboard.admin.manage_orders.manage_orders import manage_orders
from dashboard.admin.inventory.inventory import inventory
from dashboard.admin.view_logs import view_logs
def admin_dashboard():

    while True:

        print("\n========== ADMIN DASHBOARD ==========")
        print("1. Manage Food Menu")
        print("2. Manage Tables")
        print("3. Manage Staff")
        print("4. Manage Orders")
        print("5. Inventory Management")
        print("6. View Logs")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            manage_food_menu()

        elif choice == "2":
            manage_tables()

        elif choice == "3":
            manage_staff()

        elif choice == "4":
            manage_orders()

        elif choice == "5":
            inventory()

        elif choice == "6":
            view_logs()

        elif choice == "7":
            print("Admin logged out.")
            return

        else:
            print("Invalid choice.")