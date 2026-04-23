# Program 18: Command-Line Arguments for Arithmetic Operations

import sys

# Check if correct number of arguments are provided
# sys.argv[0] is script name, [1] is first number, [2] is second number
if len(sys.argv) < 3:
    print("Usage: python script.py <num1> <num2>")
else:
    # Convert arguments from string to float
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    # Perform and display operations
    print("\nArithmetic Results:")
    print("-------------------")
    print("Addition       :", num1 + num2)
    print("Subtraction    :", num1 - num2)
    print("Multiplication :", num1 * num2)

    if num2 != 0:
        print("Division       :", num1 / num2)
    else:
        print("Division       : Error (Division by zero)")
