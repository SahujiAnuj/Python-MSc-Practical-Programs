# Program 08: Palindrome Check (Using Slicing & Without Slicing)

def preprocess(text):
    """Convert to lowercase and remove non-alphanumeric characters."""
    return "".join(ch.lower() for ch in text if ch.isalnum())


# ----------- METHOD 1: USING SLICING -----------

def check_palindrome_slicing(text):
    s = preprocess(text)
    return s == s[::-1]


# ----------- METHOD 2: WITHOUT SLICING -----------

def check_palindrome_manual(text):
    s = preprocess(text)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# ---------------- MAIN PROGRAM ----------------

print("=" * 60)
print("PALINDROME CHECKER")
print("=" * 60)

test_strings = [
    "racecar",
    "hello",
    "Madam",
    "A man, a plan, a canal: Panama",
    "Python"
]

print("\n[Predefined Tests]\n")

for text in test_strings:
    result1 = check_palindrome_slicing(text)
    result2 = check_palindrome_manual(text)

    print(f"'{text}'")
    print("  Using Slicing   :", "Yes" if result1 else "No")
    print("  Without Slicing :", "Yes" if result2 else "No")
    print("-" * 50)


# ----------- USER INPUT -----------

user_input = input("\nEnter your own string: ")

if check_palindrome_slicing(user_input):
    print("Result: Palindrome ✓")
else:
    print("Result: Not a Palindrome ✗")

print("=" * 60)
