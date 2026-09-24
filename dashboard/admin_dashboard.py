from dashboard.food_menu_dashboard import menu_management
def show_admin_dashboard(user_name):
    """Admin dashboard---Menu Screen"""

    while True:
        print("========================================================")
        print("            ADMIN DASHBOARD --  Welcome {user_name}")
        print("========================================================" )
        print("Enter 1 for Manage Food Menu (Add / View / Update / Remove Items)")
        print("Enter 2 for Table Management")
        print("Enter 3 for Manage Staff")
        print("Enter 4 for View Sales Reports")
        print("Ente 5 for View Order History")
        print("Enter 6 for Manage Discounts (Coupons & Offers)")
        print("Enter 7 for Check Inventory Stock")
        print("Enter 8 for Manage Tables Reservations And Advance Bookings")
        print("Enter 9 for Manage Payment Gateways & Tax Settings (GST)")
        print("Enter 10 for Customer Feedbacks & Ratings")
        print("Enter 11 for System Backup & Data Restore")
        print("Enter 12 for Logout")
        print("========================================================")

        choice = input("Enter your choice (1-12): ").strip()

        if choice == "1":
            print("\nFood Menu Management]")
            menu_management()
        elif choice == "2":
            print("\nTable Management]")
        elif choice == "3":
            print("\nStaff Management]")
        elif choice == "4":
            print("\nSales Analytics]")
        elif choice == "5":
            print("\nOrder History]")
        elif choice == "6":
            print("\nDiscounts & Offers]")
        elif choice == "7":
            print("\nInventory Management]")
        elif choice == "8":
            print("\nAdvance Reservations]" )
        elif choice == "9":
            print("\nPayments & Tax Settings]")
        elif choice == "10":
            print("\nCustomer Feedback]" )
        elif choice == "11":
            print("\nSystem Backup]" )
        elif choice == "12":
            print(f"\nLogging out.....Good bye, {user_name}" )
            break
        else:
            print("\nInvalid Choice! Please enter a number between 1 and 12." )