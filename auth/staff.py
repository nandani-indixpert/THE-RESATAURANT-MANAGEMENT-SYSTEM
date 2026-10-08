import json
import os


STAFF_FILE = "database/staff.json"


def load_staff():
    if not os.path.exists(STAFF_FILE):
        return []

    with open(STAFF_FILE, "r") as file:
        return json.load(file)


def save_staff(staff):
    with open(STAFF_FILE, "w") as file:
        json.dump(staff, file, indent=4)