# Program 22 (Continued): Using the Math Utilities Module

# Importing functions from our previous script
from q22_mathutils import factorial, is_prime, prime_factors

# 1. Using Factorial
num = int(input("Enter a number for factorial: "))
print("Factorial is:", factorial(num))

# 2. Using Prime Check
p_num = int(input("\nEnter a number to check prime: "))
if is_prime(p_num):
    print(p_num, "is a Prime Number")
else:
    print(p_num, "is not a Prime Number")

# 3. Using Prime Factors
f_num = int(input("\nEnter a number for prime factors: "))
print("Prime factors are:", prime_factors(f_num))
