# Program 11: Tuple Packing and Unpacking (including nested tuples)

print("=" * 60)
print("TUPLE PACKING & UNPACKING")
print("=" * 60)


# ----------- PACKING -----------

student = ("Alice", 21, "CS", 9.1)
print("\nPacked Tuple:", student)


# ----------- BASIC UNPACKING -----------

name, age, branch, cgpa = student
print("\nUnpacked Values:")
print("Name  :", name)
print("Age   :", age)
print("Branch:", branch)
print("CGPA  :", cgpa)


# ----------- EXTENDED UNPACKING -----------

nums = (10, 20, 30, 40, 50)
first, *middle, last = nums

print("\nExtended Unpacking:")
print("First :", first)
print("Middle:", middle)
print("Last  :", last)


# ----------- SWAPPING -----------

x, y = 100, 200
x, y = y, x

print("\nAfter Swapping:")
print("x =", x, ", y =", y)


# ----------- NESTED TUPLE -----------

person = ("Bob", 25, ("Mumbai", "MH", 400001))
name, age, (city, state, pin) = person

print("\nNested Tuple Unpacking:")
print("Name :", name)
print("City :", city)
print("State:", state)


# ----------- FUNCTION RETURN -----------

def get_values(lst):
    return min(lst), max(lst)

data = [4, 7, 2, 9]
mn, mx = get_values(data)

print("\nFunction Return (Tuple):")
print("Min:", mn, "Max:", mx)

print("=" * 60)
