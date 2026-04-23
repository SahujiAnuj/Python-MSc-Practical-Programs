# Program 03: Comprehensive Demonstration of Python Operators

a, b = 15, 4

print("=" * 60)
print("PYTHON OPERATORS SHOWCASE")
print("=" * 60)


# ---------- ARITHMETIC OPERATORS ----------
print("\n[Arithmetic Operators]")
print(f"a = {a}, b = {b}")
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Exponentiation :", a ** b)


# ---------- RELATIONAL OPERATORS ----------
print("\n[Relational Operators]")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)


# ---------- LOGICAL OPERATORS ----------
print("\n[Logical Operators]")
x, y = True, False
print(f"x = {x}, y = {y}")
print("x AND y :", x and y)
print("x OR y  :", x or y)
print("NOT x   :", not x)


# ---------- BITWISE OPERATORS ----------
print("\n[Bitwise Operators]")
print(f"a = {a} ({bin(a)}), b = {b} ({bin(b)})")
print("AND  (&) :", a & b)
print("OR   (|) :", a | b)
print("XOR  (^) :", a ^ b)
print("NOT  (~a):", ~a)
print("Left Shift  (a << 1):", a << 1)
print("Right Shift (a >> 1):", a >> 1)


# ---------- ASSIGNMENT OPERATORS ----------
print("\n[Assignment Operators]")
n = 10
print("Initial n =", n)

n += 5
print("n += 5  →", n)

n -= 3
print("n -= 3  →", n)

n *= 2
print("n *= 2  →", n)

n //= 4
print("n //= 4 →", n)

n **= 2
print("n **= 2 →", n)


# ---------- MEMBERSHIP & IDENTITY ----------
print("\n[Membership & Identity Operators]")
lst = [1, 2, 3]

print("1 in list     :", 1 in lst)
print("5 not in list :", 5 not in lst)

p = q = [1, 2]
r = [1, 2]

print("p is q :", p is q)
print("p is r :", p is r)

print("=" * 60)
