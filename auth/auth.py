from auth.admin import load_admin
from auth.admin_signup import admin_signup
from auth.admin_signin import admin_signin
from auth.staff_signin import staff_signin
from dashboard.admin.admin_dashboard import admin_dashboard
from dashboard.staff.staff_dashboard import staff_dashboard


def authentication():

    admins = load_admin()

    if len(admins) == 0:

        while True:
            print("\n========== RESTAURANT MANAGEMENT SYSTEM ==========")
            print("1. Admin Sign Up")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                admin_signup()
                break

            elif choice == "2":
                print("Thank you!")
                return

            else:
                print("Invalid choice.")

    while True:
        print("\n========== LOGIN ==========")
        print("1. Admin Sign In")
        print("2. Staff Sign In")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin = admin_signin()

            if admin:
                admin_dashboard()

        elif choice == "2":
            staff = staff_signin()
            if staff:
                staff_dashboard()

        elif choice == "3":
            print("===============================================================")
            print("Thank you so much for using Restaurant Management System.....")
            print("===============================================================")
            return

        else:
            print("Invalid choice.")