import os

LOG_FILE = "logs/restaurant.log"


def view_logs():

    if not os.path.exists(LOG_FILE):
        print("\nNo logs found.")
        return

    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    if len(logs) == 0:
        print("\nNo logs found.")
        return

    print("\n========== SYSTEM LOGS ==========")

    for log in logs:
        print(log.strip())