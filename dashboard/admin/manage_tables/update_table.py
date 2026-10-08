from utils.logger import log_info, log_warning
import json
import os


TABLE_FILE = "database/tables.json"


def load_tables():

    if not os.path.exists(TABLE_FILE):
        return []

    with open(TABLE_FILE, "r") as file:
        return json.load(file)


def save_tables(table_list):

    with open(TABLE_FILE, "w") as file:
        json.dump(table_list, file, indent=4)


def update_table():

    table_list = load_tables()

    if len(table_list) == 0:
        print("\nNo tables found.")
        
        return

    print("\n========== TABLE LIST ==========")

    for table in table_list:
        print(f"{table['table_id']} - {table['table_type']} - {table['seats']} seats")

    table_id = input("\nEnter Table ID to update: ").strip().upper()

    for table in table_list:

        if table["table_id"].upper() == table_id:

            table["table_type"] = input("Enter new table type: ").strip()
            table["seats"] = input("Enter new number of seats: ").strip()

            save_tables(table_list)

            print("\nTable updated successfully.")
            log_info(f"Table updated: {table_id}")
            return

    print("\nTable ID not found.")
    log_warning(f"Invalid table update attempt: {table_id}")