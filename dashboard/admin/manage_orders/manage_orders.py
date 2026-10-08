from dashboard.admin.manage_orders.create_order import create_order
from dashboard.admin.manage_orders.view_order import view_orders
from dashboard.admin.manage_orders.update_order import update_order
from dashboard.admin.manage_orders.delete_order import delete_order
def manage_orders():

    while True:

        print("\n========== MANAGE ORDERS ==========")
        print("1. Create Order")
        print("2. View Orders")
        print("3. Update Order")
        print("4. Delete Order")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_order()

        elif choice == "2":
            view_orders()

        elif choice == "3":
            update_order()

        elif choice == "4":
            delete_order()

        elif choice == "5":
            return

        else:
            print("Invalid choice.")