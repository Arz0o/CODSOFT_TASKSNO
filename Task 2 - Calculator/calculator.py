def calculator():
    print("================================")
    print("          CALCULATOR")
    print("================================")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            result = num1 + num2
            print("\nResult:", result)

        elif choice == "2":
            result = num1 - num2
            print("\nResult:", result)

        elif choice == "3":
            result = num1 * num2
            print("\nResult:", result)

        elif choice == "4":
            if num2 == 0:
                print("\nError: Cannot divide by zero.")
            else:
                result = num1 / num2
                print("\nResult:", result)

        else:
            print("\nInvalid operation choice.")

    except ValueError:
        print("\nPlease enter valid numbers.")


while True:

    calculator()

    again = input("\nDo you want to perform another calculation? (y/n): ").lower()

    if again != "y":
        print("\nThank you for using the Calculator!")
        break