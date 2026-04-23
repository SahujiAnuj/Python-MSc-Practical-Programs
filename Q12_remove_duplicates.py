# Program 12: Remove Duplicates from a List (Maintain Order)

def remove_duplicates(lst):
    """Remove duplicates while preserving order."""
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


# ---------------- MAIN PROGRAM ----------------

print("=" * 60)
print("REMOVE DUPLICATES FROM LIST")
print("=" * 60)

# User input
items = input("Enter elements (space-separated): ").split()

# Process
unique_items = remove_duplicates(items)

# Output
print("\nOriginal List :", items)
print("Without Duplicates :", unique_items)

print("=" * 60)
