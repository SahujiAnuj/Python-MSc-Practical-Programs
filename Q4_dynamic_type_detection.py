# Program 04: Dynamic Data Type Detection and Conversion

def detect_type(value):
    """
    Detect and convert input into the most suitable Python type.
    Priority: bool → int → float → complex → string
    """

    val = value.strip()

    # Boolean check
    if val.lower() in ["true", "false"]:
        return val.lower() == "true", "Boolean"

    # Integer check
    try:
        return int(val), "Integer"
    except ValueError:
        pass

    # Float check
    try:
        return float(val), "Float"
    except ValueError:
        pass

    # Complex check
    try:
        return complex(val), "Complex"
    except ValueError:
        pass

    # Default → String
    return val, "String"


def show_possible_conversions(value):
    print("\n[Possible Conversions]")

    conversions = {
        "Integer": lambda v: int(float(v)),
        "Float": float,
        "Complex": complex,
        "String": str,
        "Boolean": bool
    }

    for name, func in conversions.items():
        try:
            print(f"{name:<10} → {func(value)}")
        except:
            print(f"{name:<10} → Not possible")


# ---------------- MAIN PROGRAM ----------------

print("=" * 60)
print("DYNAMIC DATA TYPE DETECTOR")
print("=" * 60)

user_input = input("Enter a value: ")

converted_value, detected_type = detect_type(user_input)

print("\n[Result]")
print("Input Value   :", user_input)
print("Detected Type :", detected_type)
print("Converted To  :", type(converted_value))
print("Final Value   :", converted_value)

show_possible_conversions(user_input)

print("=" * 60)
