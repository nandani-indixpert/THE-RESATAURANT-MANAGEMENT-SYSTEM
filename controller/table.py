import json
import os

TABLE_FILE = "database/tables.json"


def load_tables():
    if not os.path.exists(TABLE_FILE):
        return []
    try:
        with open(TABLE_FILE, "r") as file:
            return json.load(file)
    except:
        return []



def save_tables(data):
    try:
        with open(TABLE_FILE, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except:
        return False


def add_table(table_no, capacity):
    tables = load_tables()

    for t in tables:
        if str(t["table_no"]) == str(table_no):
            return False, f"Table number {table_no} already exists"

    try:
        capacity = int(capacity)
    except:
        return False, "Capacity should be numerical"

    new_table = {
        "table_no": str(table_no),
        "capacity": capacity,
        "status": "Available",  
    }

    tables.append(new_table)

    if save_tables(tables):
        return True, f"Table No. {table_no} added successfully!"
    else:
        return False, "Error created during save"

def get_all_tables():
    return load_tables()

def update_table_status(table_no, new_status):
    tables = load_tables()

    for t in tables:
        if str(t["table_no"]) == str(table_no):
            t["status"] = new_status
            if save_tables(tables):
                return True, f"Table {table_no} status '{new_status}' "
            else:
                return False, "Status update not save"

    return False, "Table number not found"