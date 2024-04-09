import re

def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"
    
    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter"
    
    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit"
    
    # Check if the password contains at least one special character
    special_characters = r'[!@#$%^&*()_+}{":?><,./;\'[\]\\=-`~|]'
    if not re.search(special_characters, password):
        return False, "Password must contain at least one special character"
    
    # Password meets all criteria
    return True, "Password is valid"

# Example usage:
password = "StrongPassword123!"
is_valid, message = validate_password(password)
print(message)

"""
Rejects in Python

In Python, "reject" isn't a built-in concept. However, you can achieve rejection-like behavior using various methods:

Exceptions: You can raise exceptions to signal errors or invalid data. For example, 
if a function receives a string that doesn't meet password criteria, you can raise a ValueError.

Return values: Functions can return specific values to indicate rejection. 
You could return False or None if the password doesn't pass validation.

assert statements: While not strictly for rejection, assert statements can help catch invalid conditions during development. 
They raise AssertionError if a condition is not met.

"""