from dashboard.admin.manage_staff.add_staff import add_staff
from dashboard.admin.manage_staff.view_staff import view_staff
from dashboard.admin.manage_staff.remove_staff import remove_staff


def manage_staff():

    while True:

        print("\n========== MANAGE STAFF ==========")
        print("1. Add Staff")
        print("2. View Staff")
        print("3. Remove Staff")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_staff()

        elif choice == "2":
            view_staff()

        elif choice == "3":
            remove_staff()

        elif choice == "4":
            return

        else:
            print("Invalid choice.")