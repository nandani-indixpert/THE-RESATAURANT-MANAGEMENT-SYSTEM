from utils.logger import log_info
import json
import os


TABLE_FILE = "database/tables.json"


def load_tables():

    if not os.path.exists(TABLE_FILE):
        return []

    with open(TABLE_FILE, "r") as file:
        return json.load(file)


def view_table():

    table_list = load_tables()

    if len(table_list) == 0:
        print("\nNo tables found.")
        return

    print("\n")
    print("╔══════════╦══════════════╦══════════╦═══════════════╗")
    print("║ TABLE ID ║ TABLE TYPE   ║ CAPACITY ║ STATUS        ║")
    print("╠══════════╬══════════════╬══════════╬═══════════════╣")

    for table in table_list:
        print(
            f"║ {table['table_id']:<8} "
            f"║ {table['table_type']:<12} "
            f"║ {table['seats']:<8} "
            f"║ {table['status']:<13} ║"
        )

    print("╚══════════╩══════════════╩══════════╩═══════════════╝")

    log_info("Table list viewed.")