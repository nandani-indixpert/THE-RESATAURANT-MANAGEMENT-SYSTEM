from auth.staff import load_staff


def view_staff():

    staff_list = load_staff()

    if len(staff_list) == 0:
        print("\nNo staff found.")
        return

    print("\n========== STAFF LIST ==========")

    for staff in staff_list:
        print(f"Staff ID : {staff['staff_id']}")
        print(f"Name     : {staff['name']}")
        print(f"Email    : {staff['email']}")
        print(f"Phone    : {staff['phone']}")
        print("-" * 40)