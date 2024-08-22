'''Q6. Make a password strength function. It will accept a string from user.
Return True if it is a strong password.
Strong password has these characteristics.
Minimum 8 character
Minimum 1 uppercase alphabet
Minimum 1 lowercase alphabet
Contains at least 1 special symbol (any symbol)
Minimum 1 digit'''

#  Imports the regular expression module (re) to help with pattern matching
import re


def is_strong_password(password):
    # Check for minimum length of 8 characters
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Check for at least one digit
    if not re.search(r"\d", password):
        return False

    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    # If all conditions are met, return True
    return True


# Take user input for the password
password = input("Enter your password: ")

# Check if the password is strong
if is_strong_password(password):
    print("Your password is strong.")
else:
    print("Your password is not strong enough.")


    

# another way
def is_strong_password(password):
    # Initialize flags for each requirement
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Check for minimum length
    if len(password) < 8:
        return False

    # Iterate through each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():  # Checks if the character is not alphanumeric, i.e., a special character
            has_special = True

    # Return True only if all conditions are met
    return has_upper and has_lower and has_digit and has_special


# Take user input for the password
user_password = input("Enter your password: ")

# Check if the password is strong
if is_strong_password(user_password):
    print("Your password is strong.")
else:
    print("Your password is not strong enough.")
