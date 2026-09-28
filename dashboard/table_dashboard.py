from controller.table import add_table, get_all_tables, update_table_status


def table_management_menu():
    while True:
        print("\n--- TABLE MANAGEMENT ---")
        print("1. Add New Table")
        print("2. View All Tables")
        print("3. Update Table Status")
        print("4. Back to Admin Dashboard")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            print("\n--- Add New Table ---")
            table_no = input("Enter Table Number (e.g., T1, T2): ").strip()
            capacity = input("Enter Seating Capacity (e.g., 2, 4, 6): ").strip()

            status, msg = add_table(table_no, capacity)
            print(msg)

        elif choice == "2":
            print("\n--- ALL TABLES STATUS ---")
            tables = get_all_tables()
            if not tables:
                print("Koi table add nahi ki gayi hai!")
            else:
                for t in tables:
                    print(
                        f"Table No: {t['table_no']} | Capacity: {t['capacity']} Seats | Status: {t['status']}"
                    )

        elif choice == "3":
            print("\n--- Update Table Status ---")
            table_no = input("Enter Table Number: ").strip()
            print("Select Status: 1. Available | 2. Occupied | 3. Reserved")
            st_choice = input("Enter choice (1-3): ").strip()

            status_map = {"1": "Available", "2": "Occupied", "3": "Reserved"}
            if st_choice in status_map:
                status, msg = update_table_status(table_no, status_map[st_choice])
                print(msg)
            else:
                print("Invalid status choice!")

        elif choice == "4":
            break
        else:
            print("Invalid choice! Try again.")