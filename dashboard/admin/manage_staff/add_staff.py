import uuid
import pwinput

from auth.staff import load_staff, save_staff
from auth.validation import (
    validate_name,
    validate_email,
    validate_phone,
    validate_password
)


def add_staff():

    staff_list = load_staff()

    if len(staff_list) >= 40:
        print("\nMaximum 40 staff members are allowed.")
        return

    print("\n========== ADD STAFF ==========")

    name = input("Enter name: ")

    valid, message = validate_name(name)
    if not valid:
        print("ERROR:", message)
        return

    email = input("Enter email: ")

    valid, message = validate_email(email)
    if not valid:
        print("ERROR:", message)
        return

    phone = input("Enter phone: ")

    valid, message = validate_phone(phone)
    if not valid:
        print("ERROR:", message)
        return

    password = pwinput.pwinput("Enter password: ")

    valid, message = validate_password(password)
    if not valid:
        print("ERROR:", message)
        return

    staff_id = f"S{len(staff_list) + 1:03d}"

    staff = {
        "id": str(uuid.uuid4())[:10],
        "staff_id": staff_id,
        "name": name,
        "email": email,
        "phone": phone,
        "password": password
    }

    staff_list.append(staff)
    save_staff(staff_list)

    print(f"\nStaff added successfully.")
    print(f"Staff ID: {staff_id}")