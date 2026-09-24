from database.database_handler import read_users


def signin_user(user_id, password):
    users = read_users()

    # Find user and match
    for user in users:
        if user["user_id"] == user_id:
            if user["password"] == password:
                return (
                    True,
                    "Login Successful!",
                    user["role"],
                    user["name"],
                )
            else:
                return False, "Wrong password!", None, None

    # If loop finishes, user was not found
    return False, "User ID not found!", None, None