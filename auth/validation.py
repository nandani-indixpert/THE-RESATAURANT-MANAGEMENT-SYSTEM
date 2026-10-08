import re


def validate_name(name):
    if len(name.strip()) < 3:
        return False, "Name must contain at least 3 characters."

    if not name.replace(" ", "").isalpha():
        return False, "Name can contain only letters."

    return True, "Valid name."


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"

    if not re.match(pattern, email):
        return False, "Enter a valid Gmail address."

    return True, "Valid email."


def validate_phone(phone):
    if not phone.isdigit():
        return False, "Phone number must contain only digits."

    if len(phone) != 10:
        return False, "Phone number must contain exactly 10 digits."

    if phone[0] not in "6789":
        return False, "Phone number must start with 6, 7, 8 or 9."

    return True, "Valid phone number."


def validate_password(password):

    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    if len(password) > 20:
        return False, "Password cannot contain more than 20 characters."

    return True, "Valid password."