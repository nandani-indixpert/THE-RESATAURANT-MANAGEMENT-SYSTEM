import json
import os
from datetime import datetime

FEEDBACK_FILE = "database/feedback.json"


def load_feedback():

    if not os.path.exists(FEEDBACK_FILE):
        return []

    with open(FEEDBACK_FILE, "r") as file:
        return json.load(file)


def save_feedback(feedback_list):

    with open(FEEDBACK_FILE, "w") as file:
        json.dump(feedback_list, file, indent=4)


def take_feedback(order_id, customer_name):

    choice = input(
        "\nWould you like to give feedback? (Yes/No): "
    ).strip().lower()

    if choice != "yes":
        print("\nFeedback skipped.")
        return

    print("\n========== CUSTOMER FEEDBACK ==========")

    rating = input(
        "Enter rating (1-5) (optional): "
    ).strip()

    if rating != "":
        if not rating.isdigit() or int(rating) < 1 or int(rating) > 5:
            print("\nInvalid rating.")
            return

        rating = int(rating)

    else:
        rating = ""

    feedback = input(
        "Enter your feedback (optional): "
    ).strip()

    feedback_list = load_feedback()

    feedback_id = f"F{len(feedback_list) + 1:03d}"

    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%I:%M %p")

    new_feedback = {
        "feedback_id": feedback_id,
        "order_id": order_id,
        "customer_name": customer_name,
        "rating": rating,
        "feedback": feedback,
        "date": current_date,
        "time": current_time
    }

    feedback_list.append(new_feedback)

    save_feedback(feedback_list)

    print("\nThank you for your feedback!")