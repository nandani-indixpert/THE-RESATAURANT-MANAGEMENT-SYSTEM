from utils.logger import log_info, log_warning
from dashboard.staff.billing_payment.feedback import take_feedback
from datetime import datetime
import json
import os

ORDER_FILE = "database/orders.json"


def load_orders():

    if not os.path.exists(ORDER_FILE):
        return []

    with open(ORDER_FILE, "r") as file:
        return json.load(file)


def save_orders(order_list):

    with open(ORDER_FILE, "w") as file:
        json.dump(order_list, file, indent=4)


def show_bill(order):

    customer_name = order.get("customer_name", "")
    order_id = order["order_id"]

    total = float(order["total"])
    discount = float(order.get("discount", 0))
    gst = float(order.get("gst", 0))
    final_amount = float(order.get("final_amount", total))

    date = order.get("date", "")
    time = order.get("time", "")

    print("\n")
    print("╔══════════════════════════════════════════════════╗")
    print("║                    BILL                          ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║ Customer Name : {customer_name:<31}║")
    print(f"║ Order ID      : {order_id:<31}║")
    print(f"║ Date          : {date:<31}║")
    print(f"║ Time          : {time:<31}║")
    print("╠══════════════════════════════════════════════════╣")
    print("║ ITEM NAME                 QTY           PRICE    ║")
    print("╠══════════════════════════════════════════════════╣")

    for item in order["items"]:

        food_name = item["food_name"]
        quantity = item["quantity"]
        item_total = item["total"]

        print(
            f"║ {food_name:<24} "
            f"{quantity:<10} "
            f"₹{item_total:<10} ║"
        )

    print("╠══════════════════════════════════════════════════╣")
    print(f"║ Food Total     : ₹{total:<30}║")
    print(f"║ Discount       : ₹{discount:<30}║")
    print(f"║ Subtotal       : ₹{total - discount:<30}║")
    print(f"║ GST (5%)       : ₹{gst:<30}║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║ Final Amount   : ₹{final_amount:<30}║")
    print("╚══════════════════════════════════════════════════╝")


def billing_payment():

    order_list = load_orders()

    if len(order_list) == 0:
        print("\nNo orders found.")
        return

    print("\n========== ORDERS ==========")

    for order in order_list:

        print(
            f"Order ID: {order['order_id']} "
            f"| Total: ₹{order['total']} "
            f"| Status: {order['status']}"
        )

    order_id = input("\nEnter Order ID: ").strip()

    for order in order_list:

        if order["order_id"] == order_id:

            # Check if payment is already completed

            if order.get("payment_status") == "Paid":

                show_bill(order)

                print(
                    f"\nPayment Method : "
                    f"{order.get('payment_method', '')}"
                )

                print("Payment Status : Paid")

                print(
                    "\nThis order has already been paid."
                )

                log_info(
                    f"Paid order viewed: {order_id}"
                )

                return

            # New payment

            customer_name = input(
                "\nEnter customer name (optional): "
            ).strip()

            total = float(order["total"])

            current_date = datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.now().strftime("%I:%M %p")

            # Bulk Purchase Discount

            if total >= 3000:

                discount = total * 15 / 100

            elif total >= 2000:

                discount = total * 10 / 100

            elif total >= 1000:

                discount = total * 5 / 100

            else:

                discount = 0

            subtotal = total - discount

            gst = subtotal * 5 / 100

            final_amount = subtotal + gst

            # Save billing details

            order["customer_name"] = customer_name
            order["discount"] = discount
            order["gst"] = gst
            order["final_amount"] = final_amount
            order["date"] = current_date
            order["time"] = current_time

            # Show Bill

            print("\n")
            print("╔══════════════════════════════════════════════════╗")
            print("║                    BILL                          ║")
            print("╠══════════════════════════════════════════════════╣")
            print(f"║ Customer Name : {customer_name:<31}║")
            print(f"║ Order ID      : {order['order_id']:<31}║")
            print(f"║ Date          : {current_date:<31}║")
            print(f"║ Time          : {current_time:<31}║")
            print("╠══════════════════════════════════════════════════╣")
            print("║ ITEM NAME                 QTY           PRICE    ║")
            print("╠══════════════════════════════════════════════════╣")

            for item in order["items"]:

                food_name = item["food_name"]
                quantity = item["quantity"]
                item_total = item["total"]

                print(
                    f"║ {food_name:<24} "
                    f"{quantity:<10} "
                    f"₹{item_total:<10} ║"
                )

            print("╠══════════════════════════════════════════════════╣")
            print(f"║ Food Total     : ₹{total:<30}║")
            print(f"║ Discount       : ₹{discount:<30}║")
            print(f"║ Subtotal       : ₹{subtotal:<30}║")
            print(f"║ GST (5%)       : ₹{gst:<30}║")
            print("╠══════════════════════════════════════════════════╣")
            print(f"║ Final Amount   : ₹{final_amount:<30}║")
            print("╚══════════════════════════════════════════════════╝")

            # Payment Method

            print("\nSelect Payment Method:")
            print("1. Cash")
            print("2. UPI")
            print("3. Card")

            while True:

                payment_choice = input(
                    "Enter your choice: "
                ).strip()

                if payment_choice == "1":

                    payment_method = "Cash"
                    break

                elif payment_choice == "2":

                    payment_method = "UPI"
                    break

                elif payment_choice == "3":

                    payment_method = "Card"
                    break

                else:

                    print(
                        "\nInvalid choice. "
                        "Please enter 1, 2 or 3."
                    )

            order["payment_method"] = payment_method
            order["payment_status"] = "Paid"

            save_orders(order_list)

            print("\n")
            print("╔══════════════════════════════════════════════════╗")
            print("║              PAYMENT SUCCESSFUL                 ║")
            print("╠══════════════════════════════════════════════════╣")
            print(f"║ Customer Name  : {customer_name:<30}║")
            print(f"║ Order ID       : {order['order_id']:<30}║")
            print(f"║ Date           : {current_date:<30}║")
            print(f"║ Time           : {current_time:<30}║")
            print(f"║ Food Total     : ₹{total:<29}║")
            print(f"║ Discount       : ₹{discount:<29}║")
            print(f"║ GST (5%)       : ₹{gst:<29}║")
            print(f"║ Final Amount   : ₹{final_amount:<29}║")
            print(f"║ Payment Method : {payment_method:<30}║")
            print("║ Payment Status : Paid                             ║")
            print("╚══════════════════════════════════════════════════╝")

            log_info(
                f"Payment completed for Order ID: {order_id}"
            )

            # Feedback

            take_feedback(order_id, customer_name)

            return

    print("\nOrder ID not found.")

    log_warning(
        f"Invalid billing attempt for Order ID: {order_id}"
    )