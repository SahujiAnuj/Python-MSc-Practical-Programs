# Program 02: Mutable and Immutable Objects in Python

print("=" * 60)
print("MUTABLE vs IMMUTABLE OBJECTS")
print("=" * 60)


# ---------- IMMUTABLE OBJECTS ----------
print("\n[Immutable Objects]\n")

# Integer
a = 10
print("Integer:")
print("Before →", a, "| ID:", id(a))
a = 20
print("After  →", a, "| ID:", id(a), "(new object)\n")

# String
s = "hello"
print("String:")
print("Before →", s, "| ID:", id(s))
s += " world"
print("After  →", s, "| ID:", id(s), "(new object)\n")

# Tuple
t = (1, 2, 3)
print("Tuple:")
print("Value  →", t, "| ID:", id(t))
try:
    t[0] = 99
except TypeError:
    print("Modification not allowed (immutable)\n")


# ---------- MUTABLE OBJECTS ----------
print("[Mutable Objects]\n")

# List
lst = [1, 2, 3]
print("List:")
print("Before →", lst, "| ID:", id(lst))
lst.append(4)
print("After  →", lst, "| ID:", id(lst), "(same object)\n")

# Dictionary
d = {"x": 1}
print("Dictionary:")
print("Before →", d, "| ID:", id(d))
d["y"] = 2
print("After  →", d, "| ID:", id(d), "(same object)\n")

# Set
st = {10, 20}
print("Set:")
print("Before →", st, "| ID:", id(st))
st.add(30)
print("After  →", st, "| ID:", id(st), "(same object)\n")


print("=" * 60)
print("Conclusion:")
print("Immutable → New object created on modification")
print("Mutable   → Same object modified in-place")
print("=" * 60)
