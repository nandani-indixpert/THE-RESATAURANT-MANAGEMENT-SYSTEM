from pwinput import pwinput
from controller.signup_controller import signup_user
from utils.validator import (
    validate_name,
    validate_password,
    validate_phone,
    validate_role,
    validate_user_id,
)


def show_signup_screen():
    print("================ SIGNUP SCREEN ================")

    # Name Input
    while True:
        name = input("Enter your name: ")
        is_valid, msg, _ = validate_name(name)
        if is_valid == True:
            break
        print("ERROR:", msg)

    # Role Input
    while True:
        role = input("Enter your role (Admin/Staff): ").strip()
        is_valid, msg, _ = validate_role(role)
        if is_valid == True:
            break
        print("ERROR:", msg)

    # Phone Input
    while True:
        phone = input("Enter your phone number: ")
        is_valid, msg, _ = validate_phone(phone)
        if is_valid == True:
            break
        print("ERROR:", msg)

    # User ID Input
    while True:
        user_id = input("Enter your ID: ")
        is_valid, msg, _ = validate_user_id(user_id)
        if is_valid == True:
            break
        print("ERROR:", msg)

    # Password Input
    while True:
        password = pwinput("Enter password: ")
        is_valid, msg, _ = validate_password(password)
        if is_valid == True:
            break
        print("ERROR:", msg)

    # Signup Process
    success, message = signup_user(name, role, phone, user_id, password)

    print("--------------------------------------------------\n")
    if success == True:
        print("SUCCESS:", message)
    else:
        print("ERROR:", message)