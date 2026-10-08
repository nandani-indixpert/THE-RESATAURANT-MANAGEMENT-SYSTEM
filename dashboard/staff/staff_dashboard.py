from dashboard.staff.view_table_status.view_table_status import view_table_status
from dashboard.staff.create_order.create_order import create_order
from dashboard.staff.active_orders.active_orders import active_orders
from dashboard.staff.billing_payment.billing_payment import billing_payment
from dashboard.staff.reservations.reservations import reservations
def staff_dashboard():

    while True:

        print("\n========== STAFF DASHBOARD ==========")
        print("1. View Table Status")
        print("2. Create New Order")
        print("3. View / Modify Active Orders")
        print("4. Billing & Payment")
        print("5. Reservations")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_table_status()

        elif choice == "2":
            create_order()

        elif choice == "3":
            active_orders()

        elif choice == "4":
            billing_payment()

        elif choice == "5":
            reservations()

        elif choice == "6":
            print("Staff logged out.")
            return

        else:
            print("Invalid choice.")