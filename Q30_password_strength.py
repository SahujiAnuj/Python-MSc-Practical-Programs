# Program 30: Password Strength Checker using Regex

import re

def check_password(password):
    score = 0
    
    # 1. Length Check
    if len(password) >= 8:
        score += 1
    
    # 2. Uppercase Check
    if re.search(r'[A-Z]', password):
        score += 1
        
    # 3. Lowercase Check
    if re.search(r'[a-z]', password):
        score += 1
        
    # 4. Digit Check
    if re.search(r'\d', password):
        score += 1
        
    # 5. Special Character Check
    if re.search(r'[@#$%^&+=!]', password):
        score += 1
        
    # Determine Strength based on score
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Fair"
    else:
        return "Weak"

# --- Main Program ---
pwd = input("Enter password to check: ")
strength = check_password(pwd)

print(f"Password Strength: {strength}")
