def show_staff_dashboard(user_name):
    """Staff Dashboard: Menu Screen"""
    while True:
        print("========================================================")
        print(f"             STAFF DASHBOARD --  Welcome {user_name}")
        print("========================================================")
        print("Enter 1 for View Table Status")
        print("Enter 2 for Take New Order (Assign Table & Items)")
        print("Enter 3 for View Active Orders")
        print("Enter 4 for Modify / Update Active Order")
        print("Enter 5 for Billing and Payment")
        print("Enter 6 for Table Reservations")
        print("Enter 7 for View Today Sales Summary")
        print("Enter 8 for Logout")
        print("========================================================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            print("\n[Table Status & Seating]")
        elif choice == "2":
            print("\n[Take New Order]")
        elif choice == "3":
            print("\n[Kitchen Order Ticket (KOT) Tracker]")
        elif choice == "4":
            print("\n[Modify Active Order]")
        elif choice == "5":
            print("\n[Billing & Payment]" )
        elif choice == "6":
            print("\n[Table Reservations]")
        elif choice == "7":
            print("\n[Shift Sales & Summary]")
        elif choice == "8":
            print(f"\nLogging out....Good bye {user_name}")
            break
        else:
            print("\nInvalid Choice! Please enter a number between 1 and 8.") 
        





