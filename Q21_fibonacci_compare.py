# Program 21: Fibonacci Series - Recursive vs Iterative

import time

# 1. Recursive Function
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# 2. Iterative Function
def fib_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# --- Performance Comparison ---
n = 30  # Try a larger number like 40 to see a big difference

# Timing Recursive
start = time.time()
res_r = fib_recursive(n)
end = time.time()
print(f"Recursive Result: {res_r} | Time: {end - start:.5f} seconds")

# Timing Iterative
start = time.time()
res_i = fib_iterative(n)
end = time.time()
print(f"Iterative Result: {res_i} | Time: {end - start:.5f} seconds")
