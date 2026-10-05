from utils.logger import log_info
import json
import os


TABLE_FILE = "database/tables.json"


def load_tables():

    if not os.path.exists(TABLE_FILE):
        return []

    with open(TABLE_FILE, "r") as file:
        return json.load(file)


def view_table_status():

    table_list = load_tables()

    if len(table_list) == 0:
        print("\nNo tables found.")
        return

    print("\n========== TABLE STATUS ==========")

    for table in table_list:

        print(f"Table ID : {table['table_id']}")
        print(f"Type     : {table['table_type']}")
        print(f"Seats    : {table['seats']}")
        print(f"Status   : {table['status']}")
        print("-" * 35)

    log_info("Staff viewed table status.")