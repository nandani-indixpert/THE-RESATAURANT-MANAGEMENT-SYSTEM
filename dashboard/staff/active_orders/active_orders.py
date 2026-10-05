from utils.logger import log_info
from dashboard.admin.manage_orders.view_order import view_orders
from dashboard.admin.manage_orders.update_order import update_order


def active_orders():

    while True:

        print("\n========== ACTIVE ORDERS ==========")
        print("1. View Active Orders")
        print("2. Modify Order")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_orders()
            log_info("Staff viewed active orders.")

        elif choice == "2":
            update_order()
            log_info("Staff modified an order.")

        elif choice == "3":
            return

        else:
            print("Invalid choice.")