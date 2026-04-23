# Program 07: Count vowels, consonants, digits, and special characters in a string.

def analyze_text(text):
    vowels_set = "aeiouAEIOU"

    vowels = consonants = digits = spaces = special = 0

    for ch in text:
        if ch in vowels_set:
            vowels += 1
        elif ch.isalpha():
            consonants += 1
        elif ch.isdigit():
            digits += 1
        elif ch.isspace():
            spaces += 1
        else:
            special += 1

    return vowels, consonants, digits, spaces, special


# ---------------- MAIN PROGRAM ----------------

print("=" * 60)
print("STRING CHARACTER ANALYZER")
print("=" * 60)

text = input("Enter a string: ")

v, c, d, s, sp = analyze_text(text)

print("\n[Analysis Result]")
print("Input String :", text)
print("Length       :", len(text))

print("-" * 60)
print(f"Vowels        : {v}")
print(f"Consonants    : {c}")
print(f"Digits        : {d}")
print(f"Spaces        : {s}")
print(f"Special Chars : {sp}")
print("-" * 60)

total = v + c + d + s + sp
print("Total Counted :", total)

print("=" * 60)
