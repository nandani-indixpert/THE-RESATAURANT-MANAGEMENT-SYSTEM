from utils.logger import log_info, log_warning
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

            total = float(order["total"])

            print("\n========== BILL ==========")

            for item in order["items"]:
                print(
                    f"{item['food_name']} x {item['quantity']} "
                    f"= ₹{item['total']}"
                )

            print("-" * 35)
            print(f"Food Total     : ₹{total}")

            # Coupon
            coupon = input(
                "Enter coupon code (or press Enter to skip): "
            ).strip().upper()

            discount = 0

            if coupon == "SAVE10":
                discount = total * 10 / 100

            elif coupon == "SAVE20":
                discount = total * 20 / 100

            elif coupon == "WELCOME5":
                discount = total * 5 / 100

            elif coupon == "":
                discount = 0

            else:
                print("Invalid coupon.")
                coupon = "NOCOUPON"

            subtotal = total - discount

            # 5% GST
            gst = subtotal * 5 / 100

            final_amount = subtotal + gst

            print(f"Coupon Discount: ₹{discount}")
            print(f"Subtotal       : ₹{subtotal}")
            print(f"GST (5%)       : ₹{gst}")
            print("-" * 35)
            print(f"Final Amount   : ₹{final_amount}")

            # Payment
            payment_method = input(
                "\nEnter payment method (Cash/UPI/Card): "
            ).strip().title()

            order["coupon"] = coupon
            order["discount"] = discount
            order["gst"] = gst
            order["final_amount"] = final_amount
            order["payment_method"] = payment_method
            order["payment_status"] = "Paid"

            save_orders(order_list)

            print("\n========== PAYMENT SUCCESSFUL ==========")
            print(f"Order ID       : {order['order_id']}")
            print(f"Food Total     : ₹{total}")
            print(f"Discount       : ₹{discount}")
            print(f"GST (5%)       : ₹{gst}")
            print(f"Final Amount   : ₹{final_amount}")
            print(f"Payment Method : {payment_method}")
            print("Payment Status : Paid")
            log_info(f"Payment completed for Order ID: {order_id}")

            return

    print("\nOrder ID not found.")
    log_warning(f"Invalid billing attempt for Order ID: {order_id}")