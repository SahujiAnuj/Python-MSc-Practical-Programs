# --- Program 1: Python Built-in Data Types Exploration ---

import sys

def display_info(label, value):
    print("-" * 60)
    print(f"{label:<12} : {value}")
    print(f"Data Type   : {type(value)}")
    print(f"Memory ID   : {id(value)}")
    print(f"Size        : {sys.getsizeof(value)} bytes")


# Sample Data
num_int = 42
num_float = 3.14159
num_complex = 2 + 3j
flag = True
text = "Hello, Python!"
my_list = [1, "two", 3.0, True]
my_tuple = (10, 20, 30)
my_set = {1, 2, 3, 4, 5}
my_dict = {"name": "Alice", "age": 22}
nothing = None

print("=" * 60)
print("DATA TYPE ANALYSIS IN PYTHON")
print("=" * 60)

display_info("Integer", num_int)
display_info("Float", num_float)
display_info("Complex", num_complex)
display_info("Boolean", flag)
display_info("String", text)
display_info("List", my_list)
display_info("Tuple", my_tuple)
display_info("Set", my_set)
display_info("Dictionary", my_dict)
display_info("NoneType", nothing)

print("-" * 60)
