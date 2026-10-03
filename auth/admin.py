import json
import os


ADMIN_FILE = "database/admin.json"


def load_admin():
    if not os.path.exists(ADMIN_FILE):
        return []

    with open(ADMIN_FILE, "r") as file:
        return json.load(file)


def save_admin(admin):
    with open(ADMIN_FILE, "w") as file:
        json.dump(admin, file, indent=4)