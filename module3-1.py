#Simple Calculator

def simple_calculator():
    while True:
        print("\nSimple Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
            a = float(num1)
            b = float(num2)

            if choice == '1':
                print("Result:", a + b)
            elif choice == '2':
                print("Result:", a - b)
            elif choice == '3':
                print("Result:", a * b)
            elif choice == '4':
                if b != 0:
                    print("Result:", a / b)
                else:
                    print("Cannot divide by zero.")
            else:
                print("Invalid operation choice.")
        else:
            print("Please enter valid numbers.")

# Call the function
simple_calculator()