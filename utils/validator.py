import re

def validate_name(name):
    name = name.strip().title()
    if len(name)<3:
        return False, "Name must contain at least 3 characters", None
    if not re.match(r"^[A-Za-z\s]+$", name):
        return False, "Only Alphabets and Spaces are allowed in Name", None
    return True, "Valid Name", name
    

def validate_role(role):
    role = role.strip().capitalize()
    if role not in ["Admin" , "Staff"]:
        return False, "Role should be admin or staff only" , None
    return True, "Valid Role", role

def validate_phone(phone):
    phone = phone.strip()
    if not phone.isdigit():
        return False, "Phone number should contain numbers only", None
    if len(phone) != 10:
        return False, "Phone number should be 10 characters long", None
    if phone[0] not in ['6','7','8','9']:
        return False, "Phone number should start with 6 or 7 or 8 or 9", None
    return True, "Valid Phone", phone

def validate_user_id(user_id):
    user_id = user_id.strip()
    if len(user_id) > 10 or len(user_id) == 0:
        return False, "User Id should be 1 to 10 characters long" , None
    if not user_id.isalnum():
        return False, "User Id should contain letters and numbers only" , None
    return True, "Valid User_Id", user_id

def validate_password(password):
    password = password.strip()
    if len(password) > 10 or len(password) == 0:
        return False, "Password should not be greater than 10 characters", None
    has_letter = re.search(r"[A-Za-z]" , password)
    has_digit = re.search(r"[0-9]", password)
    has_special = re.search(r"[^A-Za-z0-9\s]", password)
    if not (has_letter and has_digit and has_special):
        return False, "Password should contain letter , digits and special characters thrice", None
    return True, "Valid Password" , password 

def validate_and_format_inputs(name,role,phone,user_id,password):
    
    formatted_data = {
        "name" : name,
        "role" : role,
        "phone" : phone,
        "user_id" : user_id,
        "password" : password
    }
    return True, "Valid Inputs" , formatted_data