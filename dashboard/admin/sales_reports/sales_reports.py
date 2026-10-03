from dashboard.admin.sales_reports.today_sales import today_sales
from dashboard.admin.sales_reports.total_sales import total_sales
from dashboard.admin.sales_reports.order_report import order_report
from dashboard.admin.sales_reports.food_sales_report import food_sales_report


def sales_reports():

    while True:

        print("\n========== SALES & REPORTS ==========")
        print("1. Today's Sales")
        print("2. Total Sales")
        print("3. Order Report")
        print("4. Food Sales Report")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            today_sales()

        elif choice == "2":
            total_sales()

        elif choice == "3":
            order_report()

        elif choice == "4":
            food_sales_report()

        elif choice == "5":
            return

        else:
            print("Invalid choice.")