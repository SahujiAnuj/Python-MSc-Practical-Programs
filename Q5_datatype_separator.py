# Program 05: Separate Elements of a Mixed List by Data Type

# Sample mixed list
mixed_list = [
    42, 3.14, "hello", True, None, 2+3j,
    "world", 100, 0.001, False,
    [1, 2], {"key": "val"}, (7, 8), {9, 10}
]

# Dictionary to store separated data
type_groups = {}

# Group elements by datatype
for item in mixed_list:
    type_name = type(item).__name__
    
    if type_name not in type_groups:
        type_groups[type_name] = []
    
    type_groups[type_name].append(item)


# ----------- OUTPUT SECTION -----------

print("=" * 60)
print("MIXED LIST DATA TYPE SEPARATION")
print("=" * 60)

print("\nOriginal List:")
print(mixed_list)

print("\nGrouped Elements:\n")

for dtype, values in type_groups.items():
    print(f"{dtype} ({len(values)} items):")
    for v in values:
        print("  →", repr(v))
    print()

# ----------- SUMMARY -----------

print("-" * 60)
print("Summary:")
print("Total Elements :", len(mixed_list))
print("Total Types    :", len(type_groups))

for dtype, values in type_groups.items():
    print(f"{dtype:<10} : {len(values)}")

print("=" * 60)
