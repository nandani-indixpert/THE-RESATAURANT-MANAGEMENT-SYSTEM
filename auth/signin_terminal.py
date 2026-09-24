from pwinput import pwinput
from controller.signin_controller import signin_user
from dashboard.admin_dashboard import show_admin_dashboard
from dashboard.staff_dashboard import show_staff_dashboard
from utils.validator import validate_password, validate_user_id


def show_signin_screen():
    print("================ SIGNIN SCREEN ================")

    # User ID input
    while True:
        user_id = input("Enter user id : ")
        is_valid, msg, _ = validate_user_id(user_id)
        if is_valid == True:
            break
        print("ERROR:", msg)

    # Password input
    while True:
        password = pwinput("Enter password : ")
        is_valid, msg, _ = validate_password(password)
        if is_valid == True:
            break
        print("ERROR:", msg)

    print("Authenticating...")

    # Signin controller call
    success, msg, role, name = signin_user(user_id, password)

    if success == True:
        print("Login Successful!")
        if role == "Admin":
            show_admin_dashboard(name)
        else:
            show_staff_dashboard(name)
    else:
        print("ERROR:", msg)