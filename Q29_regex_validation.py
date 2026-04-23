# Program 29: Validate Email and Phone Number using Regex

import re

# 1. Email Validation Function
def is_valid_email(email):
    # Simple pattern: letters/numbers + @ + letters + . + 2-3 letters
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

# 2. Phone Validation Function (Indian Standard)
def is_valid_phone(phone):
    # Pattern: Starts with 6-9 and has exactly 10 digits
    pattern = r'^[6-9]\d{9}$'
    if re.match(pattern, phone):
        return True
    return False

# --- Main Program ---
print("--- Validator ---")

# Test Email
user_email = input("Enter Email: ").strip()
if is_valid_email(user_email):
    print("✓ Valid Email")
else:
    print("✗ Invalid Email")

# Test Phone
user_phone = input("Enter Phone (10 digits): ").strip()
if is_valid_phone(user_phone):
    print("✓ Valid Phone")
else:
    print("✗ Invalid Phone")
