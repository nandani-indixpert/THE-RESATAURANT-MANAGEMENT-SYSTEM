import json
import os
import uuid
from datetime import datetime

RESERVATION_FILE = "database/reservations.json"
TABLE_FILE = "database/tables.json"


def load_reservations():

    if not os.path.exists(RESERVATION_FILE):
        return []

    with open(RESERVATION_FILE, "r") as file:
        return json.load(file)


def save_reservations(reservation_list):

    with open(RESERVATION_FILE, "w") as file:
        json.dump(reservation_list, file, indent=4)


def load_tables():

    if not os.path.exists(TABLE_FILE):
        return []

    with open(TABLE_FILE, "r") as file:
        return json.load(file)


def save_tables(table_list):

    with open(TABLE_FILE, "w") as file:
        json.dump(table_list, file, indent=4)


def create_reservation():

    reservation_list = load_reservations()
    table_list = load_tables()

    print("\n========== NEW RESERVATION ==========")

    # Show available tables
    available_tables = []

    for table in table_list:

        if table["status"] == "Available":
            available_tables.append(table)

    if len(available_tables) == 0:
        print("\nNo tables are available.")
        return

    print("\n========== AVAILABLE TABLES ==========")

    for table in available_tables:

        print(
            f"{table['table_id']} - "
            f"{table['table_type']} - "
            f"{table['seats']} seats"
        )

    # Select table
    while True:

        table_id = input(
            "\nEnter Table ID: "
        ).strip().upper()

        selected_table = None

        for table in available_tables:

            if table["table_id"] == table_id:
                selected_table = table
                break

        if selected_table is not None:
            break

        print("\nThis table is not available.")
        print("Please select an available table.")

    customer_name = input(
        "Enter customer name: "
    ).strip()

    phone = input(
        "Enter phone number: "
    ).strip()

    # Date validation
    while True:

        date = input(
            "Enter reservation date (YYYY-MM-DD): "
        ).strip()

        try:

            reservation_date = datetime.strptime(
                date, "%Y-%m-%d"
            ).date()

            today = datetime.now().date()

            if reservation_date < today:

                print(
                    "\nPast date reservation is not allowed."
                )

            else:
                break

        except ValueError:

            print(
                "\nInvalid date format. Use YYYY-MM-DD."
            )

    # Time validation
    while True:

        time = input(
            "Enter reservation time (HH:MM AM/PM): "
        ).strip()

        try:

            reservation_time = datetime.strptime(
                time, "%I:%M %p"
            ).time()

            now = datetime.now()

            if reservation_date == now.date():

                if reservation_time <= now.time():

                    print(
                        "\nPast time reservation is not allowed."
                    )

                else:
                    break

            else:
                break

        except ValueError:

            print(
                "\nInvalid time format. Use HH:MM AM/PM."
            )

    people = input(
        "Enter number of people: "
    ).strip()

    reservation_id = "R" + str(uuid.uuid4())[:8]

    new_reservation = {
        "reservation_id": reservation_id,
        "customer_name": customer_name,
        "phone": phone,
        "table_id": table_id,
        "date": date,
        "time": time,
        "people": people,
        "status": "Pending"
    }

    reservation_list.append(new_reservation)

    # Change table status
    for table in table_list:

        if table["table_id"] == table_id:

            table["status"] = "Reserved"
            break

    save_reservations(reservation_list)
    save_tables(table_list)

    print("\nReservation created successfully.")
    print("Reservation ID:", reservation_id)
    print("Table ID:", table_id)
    print("Status: Pending")
    print("Table Status: Reserved")


def view_reservations():

    reservation_list = load_reservations()

    if len(reservation_list) == 0:

        print("\nNo reservations found.")
        return

    print("\n========== RESERVATIONS ==========")

    for reservation in reservation_list:

        print(
            "\nReservation ID :",
            reservation["reservation_id"]
        )

        print(
            "Customer Name  :",
            reservation["customer_name"]
        )

        print(
            "Phone          :",
            reservation["phone"]
        )

        print(
            "Table ID       :",
            reservation["table_id"]
        )

        print(
            "Date           :",
            reservation["date"]
        )

        print(
            "Time           :",
            reservation["time"]
        )

        print(
            "People         :",
            reservation["people"]
        )

        print(
            "Status         :",
            reservation["status"]
        )


def update_reservation_status():

    reservation_list = load_reservations()

    if len(reservation_list) == 0:

        print("\nNo reservations found.")
        return

    reservation_id = input(
        "\nEnter Reservation ID: "
    ).strip()

    for reservation in reservation_list:

        if reservation["reservation_id"] == reservation_id:

            print("\nSelect New Status:")
            print("1. Pending")
            print("2. Confirmed")
            print("3. Cancelled")
            print("4. Completed")

            choice = input(
                "Enter your choice: "
            ).strip()

            if choice == "1":

                reservation["status"] = "Pending"

            elif choice == "2":

                reservation["status"] = "Confirmed"

            elif choice == "3":

                reservation["status"] = "Cancelled"

                # Free the table
                table_list = load_tables()

                for table in table_list:

                    if table["table_id"] == reservation["table_id"]:

                        table["status"] = "Available"
                        break

                save_tables(table_list)

            elif choice == "4":

                reservation["status"] = "Completed"

                # Free the table
                table_list = load_tables()

                for table in table_list:

                    if table["table_id"] == reservation["table_id"]:

                        table["status"] = "Available"
                        break

                save_tables(table_list)

            else:

                print("\nInvalid choice.")
                return

            save_reservations(reservation_list)

            print(
                "\nReservation status updated successfully."
            )

            print(
                "Reservation ID:",
                reservation_id
            )

            print(
                "New Status:",
                reservation["status"]
            )

            return

    print("\nReservation ID not found.")


def reservations():

    while True:

        print("\n========== RESERVATION ==========")
        print("1. Create New Reservation")
        print("2. View Reservations")
        print("3. Update Reservation Status")
        print("4. Back")

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            create_reservation()

        elif choice == "2":

            view_reservations()

        elif choice == "3":

            update_reservation_status()

        elif choice == "4":

            break

        else:

            print(
                "\nInvalid choice. Please try again."
            )