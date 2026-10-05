from utils.logger import log_info,log_warning
import json
import os
import uuid


TABLE_FILE = "database/tables.json"


def load_tables():
    if not os.path.exists(TABLE_FILE):
        return []

    with open(TABLE_FILE, "r") as file:
        return json.load(file)


def save_tables(table_list):
    with open(TABLE_FILE, "w") as file:
        json.dump(table_list, file, indent=4)


def add_table():

    table_list = load_tables()

    print("\n========== ADD TABLE ==========")

    table_id = "T" + str(len(table_list) + 1)

    table_type = input("Enter table type: ").strip()
    seats = input("Enter number of seats: ").strip()

    table = {
        "id": str(uuid.uuid4())[:10],
        "table_id": table_id,
        "table_type": table_type,
        "seats": seats,
        "status": "Available"
    }

    table_list.append(table)
    save_tables(table_list)

    print("\nTable added successfully.")
    log_info(f"Table added : {table_id}")
    print(f"Table ID: {table_id}")