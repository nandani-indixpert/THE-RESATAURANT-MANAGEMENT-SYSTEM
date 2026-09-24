from auth.signup_terminal import show_signup_screen
from auth.signin_terminal import show_signin_screen

def show_main_menu():
    # Application with main menu screen
    while True:
        print("========================================================")
        print("======= RESTAURANT MANAGEMENT SYSTEM =======")
        print("========================================================")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit")
        choice = input("Please enter your choice = ").strip()
        if choice=="1":
            show_signup_screen()
        elif choice=="2":
            show_signin_screen()
        elif choice=="3":
            print("--------------------------------------------------------------------")
            print("Thank you so much for using Restaurant management system....GOODBYE!")
            print("--------------------------------------------------------------------")
            break
        else:
            print("\nPlease enter valid choice...")
