from database.database_handler import read_users, save_users


def signup_user(name, role, phone, user_id, password):
    users = read_users()

    # 1. Check if User ID already exists
    for user in users:
        if user["user_id"] == user_id:
            return False, "User ID already exists!"

    # 2. Count current Admins and Staff
    admin_count = 0
    staff_count = 0
    for user in users:
        if user["role"] == "Admin":
            admin_count = admin_count + 1
        if user["role"] == "Staff":
            staff_count = staff_count + 1

    # 3. Check limits
    if role == "Admin" and admin_count >= 2:
        return False, "Only 2 Admins allowed!"

    if role == "Staff" and staff_count >= 40:
        return False, "Only 40 Staff allowed!"

    # 4. Add new user to list
    new_user = {
        "name": name,
        "role": role,
        "phone": phone,
        "user_id": user_id,
        "password": password,
    }

    users.append(new_user)

    # 5. Save data
    if save_users(users):
        return True, "Signup successful!"
    else:
        return False, "Failed to save data!"