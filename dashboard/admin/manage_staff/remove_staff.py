from utils.logger import log_info,log_warning
from auth.staff import load_staff, save_staff


def remove_staff():

    staff_list = load_staff()

    if len(staff_list) == 0:
        print("\nNo staff found.")
        return

    print("\n========== STAFF LIST ==========")

    for staff in staff_list:
        print(f"Staff ID : {staff['staff_id']}")
        print(f"Name     : {staff['name']}")
        print("-" * 30)

    staff_id = input("\nEnter Staff ID to remove: ").strip().upper()

    for staff in staff_list:

        if staff["staff_id"] == staff_id:
            staff_list.remove(staff)
            save_staff(staff_list)

            print("\nStaff removed successfully.")
            log_info(f"Staff removed: {staff_id}")
            return

    print("\nStaff ID not found.")
    log_warning(f"Invalid staff id removal attempt : {staff_id}")