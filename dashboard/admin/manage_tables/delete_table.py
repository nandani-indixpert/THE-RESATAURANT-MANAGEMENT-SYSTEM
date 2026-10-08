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


def delete_table():

    table_list = load_tables()

    if len(table_list) == 0:
        print("\nNo tables found.")
        log_warning(f"Invalid table delete attempt: {table_id}")
        return

    print("\n========== TABLE LIST ==========")

    for table in table_list:
        print(f"{table['table_id']} - {table['table_type']} - {table['seats']} seats")

    table_id = input("\nEnter Table ID to delete: ").strip().upper()

    for table in table_list:

        if table["table_id"].upper() == table_id:

            table_list.remove(table)
            save_tables(table_list)

            print("\nTable deleted successfully.")
            log_info(f"Table deleted: {table_id}")
            return

    print("\nTable ID not found.")