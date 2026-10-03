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
            print("View Table Status")

        elif choice == "2":
            print("Create New Order")

        elif choice == "3":
            print("View / Modify Active Orders")

        elif choice == "4":
            print("Billing & Payment")

        elif choice == "5":
            print("Reservations")

        elif choice == "6":
            print("Staff logged out.")
            return

        else:
            print("Invalid choice.")