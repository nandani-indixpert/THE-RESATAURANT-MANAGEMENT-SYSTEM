from utils.logger import log_info, log_warning
import pwinput

from auth.staff import load_staff


def staff_signin():

    staff_list = load_staff()

    if len(staff_list) == 0:
        print("\nNo staff found. Please add staff first.")
        log_warning("Staff sign-in attempted but no staff found.")
        return None

    print("\n========== STAFF SIGN IN ==========")

    email_or_phone = input("Enter email or phone: ")
    password = pwinput.pwinput("Enter password: ")

    for staff in staff_list:

        if (
            (email_or_phone == staff["email"] or
             email_or_phone == staff["phone"])
            and password == staff["password"]
        ):
            print(f"\nWelcome, {staff['name']}!")
            log_info(f"Staff logged in: {staff['name']}")
            return staff

    print("\nInvalid email/phone or password.")
    log_warning("Invalid staff login attempt.")
    return None