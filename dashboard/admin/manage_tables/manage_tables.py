from dashboard.admin.manage_tables.add_table import add_table
from dashboard.admin.manage_tables.view_table import view_table
from dashboard.admin.manage_tables.update_table import update_table
from dashboard.admin.manage_tables.delete_table import delete_table

def manage_tables():

    while True:

        print("\n========== MANAGE TABLES ==========")
        print("1. Add Table")
        print("2. View Table")
        print("3. Update Table")
        print("4. Delete Table")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_table()

        elif choice == "2":
            view_table()

        elif choice == "3":
            update_table()

        elif choice == "4":
            delete_table()

        elif choice == "5":
            return

        else:
            print("Invalid choice.")