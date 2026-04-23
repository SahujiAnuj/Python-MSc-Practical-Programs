# Program 06: Arithmetic Operations on Complex Numbers

import cmath

def show_details(name, z):
    """Display complex number with magnitude and phase."""
    print(f"{name:<12}: {z}")
    print(f"{'':12}  Magnitude = {abs(z):.2f}")
    print(f"{'':12}  Phase     = {cmath.phase(z):.2f} radians\n")


# ----------- INPUT VALUES -----------

z1 = complex(4, 3)   # 4 + 3j
z2 = complex(1, -2)  # 1 - 2j

print("=" * 60)
print("COMPLEX NUMBER OPERATIONS")
print("=" * 60)

# Display original numbers
print("\n[Input Values]\n")
show_details("z1", z1)
show_details("z2", z2)


# ----------- ARITHMETIC OPERATIONS -----------

print("[Arithmetic Results]\n")

show_details("z1 + z2", z1 + z2)
show_details("z1 - z2", z1 - z2)
show_details("z1 * z2", z1 * z2)
show_details("z1 / z2", z1 / z2)


# ----------- ADDITIONAL PROPERTIES -----------

print("[Additional Properties]\n")

print("Real Part       :", z1.real)
print("Imaginary Part  :", z1.imag)
print("Conjugate       :", z1.conjugate())
print("Square Root     :", cmath.sqrt(z1))
print("Exponential     :", cmath.exp(z1))
print("Logarithm       :", cmath.log(z1))

# Polar form
r, theta = cmath.polar(z1)
print("Polar Form      :", (r, theta))

# Rectangular conversion
print("Back to Rect    :", cmath.rect(r, theta))

print("=" * 60)
