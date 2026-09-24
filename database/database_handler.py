import json
import os

USERS_FILE = "database/users.json"

def read_users():
    """Read user data from json file"""
    if not os.path.exists(USERS_FILE):
        return []
    try:
        with open(USERS_FILE , 'r' , encoding = "utf-8") as file:
            return json.load(file)
    except:
        return []

def save_users(users_data):
    """Saved updated users list to json file"""
    try:
        with open(USERS_FILE , 'w' , encoding = "utf-8") as file:
            json.dump(users_data , file , indent=4)
            return True
    except:
        return False