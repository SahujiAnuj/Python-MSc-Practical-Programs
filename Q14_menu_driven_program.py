# Program 14: Menu-Driven Program using if-elif and loop

while True:
    print("\n" + "=" * 50)
    print("        SIMPLE CALCULATOR MENU")
    print("=" * 50)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Exit condition
    if choice == "5":
        print("Exiting program...")
        break

    # Input numbers
    if choice in ["1", "2", "3", "4"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue

    # Operations using if-elif
    if choice == "1":
        print("Result:", a + b)

    elif choice == "2":
        print("Result:", a - b)

    elif choice == "3":
        print("Result:", a * b)

    elif choice == "4":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid choice! Please select 1-5.")
