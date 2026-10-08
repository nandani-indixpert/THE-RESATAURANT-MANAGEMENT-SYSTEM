from utils.logger import log_info, log_warning
import pwinput

from auth.admin import load_admin


def admin_signin():

    admins = load_admin()

    if len(admins) == 0:
        print("\nNo admin found. Please sign up first.")
        return None

    print("\n========== ADMIN SIGN IN ==========")

    email_or_phone = input("Enter email or phone: ")
    password = pwinput.pwinput("Enter password: ")

    admin = admins[0]

    if (
        (email_or_phone == admin["email"] or
         email_or_phone == admin["phone"])
        and password == admin["password"]
    ):
        print(f"\nWelcome, {admin['name']}!")
        log_info(f"Admin logged in: {admin['name']}")
        return admin

    print("\nInvalid email/phone or password.")
    log_warning("Invalid admin login attempt.")
    return None