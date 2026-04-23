# Program 22: Math Utilities Module (Factorial, Prime, Factors)

def factorial(n):
    """Returns the factorial of n"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def is_prime(n):
    """Returns True if n is prime, else False"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    """Returns a list of prime factors of n"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# --- Self-Test Section ---
if __name__ == "__main__":
    num = 36
    print(f"Number: {num}")
    print(f"Factorial     : {factorial(5)}") # Testing with 5
    print(f"Is Prime?     : {is_prime(num)}")
    print(f"Prime Factors : {prime_factors(num)}")
