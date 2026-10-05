from utils.logger import log_info, log_warning
import uuid
import pwinput

from auth.admin import load_admin, save_admin
from auth.validation import (
    validate_name,
    validate_email,
    validate_phone,
    validate_password
)


def admin_signup():

    admins = load_admin()

    if len(admins) > 0:
        print("\nAdmin already exists.")
        return

    print("\n========== ADMIN SIGN UP ==========")

    name = input("Enter name: ")

    valid, message = validate_name(name)
    if not valid:
        print("ERROR:", message)
        log_warning("Invalid admin name.")
        return

    email = input("Enter email: ")

    valid, message = validate_email(email)
    if not valid:
        print("ERROR:", message)
        log_warning("Invalid admin email.")
        return

    phone = input("Enter phone: ")

    valid, message = validate_phone(phone)
    if not valid:
        print("ERROR:", message)
        log_warning("Invalid admin phone")
        return

    password = pwinput.pwinput("Enter password: ")

    valid, message = validate_password(password)
    if not valid:
        print("ERROR:", message)
        log_warning("Invalid admin passsword")
        return

    admin = {
        "id": str(uuid.uuid4())[:10],
        "name": name,
        "email": email,
        "phone": phone,
        "password": password
    }

    admins.append(admin)
    save_admin(admins)

    print("\nAdmin account created successfully.")
    log_info(f"Admin account created: {name}")