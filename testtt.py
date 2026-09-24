# signup terminal
from pwinput import pwinput
from controller.signup_controller import signup_user
from utils.validator import (validate_name , validate_role , validate_phone , validate_user_id , validate_password)

def show_signup_screen():
    """Screen for takin signup input from user"""
    print("=====SIGNUP SCREEN======")

    while True:
        name = input("Please enter your name : ")
        is_valid,msg,cleaned_name = validate_name(name)
        if is_valid:
            name = cleaned_name
            break
        else:
            print(f"ERROR : {msg} Please Re-enter Name!")

    while True:
        role = input("Please enter your role(Admin/Staff) : ").strip()
        is_valid,msg,cleaned_role = validate_role(role)
        if is_valid:
            role = cleaned_role
            break
        else:
            print(f"ERROR : {msg} Please Re-enter Role!")

    while True:
        phone = input("Enter your phone number : ")
        is_valid,msg,cleaned_phone = validate_phone(phone)
        if is_valid:
            phone = cleaned_phone
            break
        else:
            print(f"ERROR : {msg} Please Re-enter phone number!")

    while True:
        user_id = input("Enter your Id : ")
        is_valid,msg,cleaned_id = validate_user_id(user_id)
        if is_valid:
            user_id = cleaned_id
            break
        else:
            print(f"ERROR : {msg} Please Re-enter user_id!")

    while True:
        password = pwinput("Please enter password : ", mask="*")
        is_valid,msg,cleaned_pass = validate_password(password)
        if is_valid:
            password = cleaned_pass
            break
        else:
            print(f"ERROR : {msg} Please Re-enter password!")

    success,message = signup_user(name,role,phone,user_id,password)

    print("--------------------------------------------\n")
    if success:
        print(f"SUCCESS : {message}")
    else:
        print(f"ERROR: {message}")
    print("--------------------------------------------")

    # signin_terminal.py

    from pwinput import pwinput
from utils.validator import validate_user_id, validate_password
from controller.signin_controller import signin_user
from dashboard.admin_dashboard import show_admin_dashboard
from dashboard.staff_dashboard import show_staff_dashboard

def show_signin_screen():
    """Screens for user signin inputs"""
    while True:
        user_id = input("Enter user id : ")
        is_valid,msg,cleaned_user_id = validate_user_id(user_id)
        if is_valid:
            user_id = cleaned_user_id
            break
        else:
            print(f"ERROR : {msg} Please Re-enter User Id")

    while True:
        password = pwinput("Enter password : ")
        is_valid,msg,cleaned_password = validate_password(password)
        if is_valid:
            password = cleaned_password
            break
        else:
            print(f"ERROR : {msg} Please Re-enter Password")

    print("Authenticating...Please wait...!!")

    success,msg,role,name = signin_user(user_id,password)

    if success:
        print(f"{msg}")
        if role.strip().capitalize() == "Admin":
            print("Admin dashboard redirecting...")
            show_admin_dashboard(name)
        elif role.strip().capitalize() == "Staff":
            print("Staff dashboard redirecting...")
            show_staff_dashboard(name)

    else:
        print(f"{msg}")

# signin_controller.py

from database.database_handler import read_users

def signin_user(user_id,password):
    user = next((u for u in read_users() if u.get("user_id") == user_id), None)

    if not user:
        return False, "ERROR ! User Id not found...Please check it or signup first" , None,None

    if user.get("password") != password:
        return False, "ERROR : Incorrect Password...Please try again...", None,None

    role = user.get("role")
    name = user.get("name",user_id)
    return True, f"SUCCESS : Welcome {user.get("name")}! Signed as {role}" , role,name

# signupcontroller

from database.database_handler import read_users, save_users
from utils.validator import validate_and_format_inputs

# inputs check and format
def signup_user(name,role,phone,user_id,password):
    """New users ko registered karne ka main controller"""
    is_valid,msg,cleaned_data = validate_and_format_inputs(name,role,phone,user_id,password)
    if not is_valid:
        return False, msg

    # old users read from database
    users = read_users()

    # duplicate id check
    for user in users:
        if user["user_id"] == cleaned_data["user_id"]:
            return False, "Duplicates ID's are not allowed...Please enter unique Id..."

    # limits count for admin and staff
    admin_count = sum(1 for u in users if u["role"] == "Admin")
    staff_count = sum(1 for u in users if u["role"] == "Staff")

    if cleaned_data["role"] == "Admin" and admin_count>=2:
        return False, "Limit full! There should be 2 Admins only"
    if cleaned_data["role"] == "Staff" and staff_count>=40:
        return False, "Limit full! There should be 40 staff only"

    # formatted data ko list me add karte hai
    users.append(cleaned_data)

    if save_users(users):
        return True, f"{cleaned_data["role"]} Signup Successfully!"
    return False, "Error created while saving new data..."


    
    

