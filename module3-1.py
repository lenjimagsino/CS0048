def menu():
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            calculator("add")
        elif choice == '2':
            calculator("subtract")
        elif choice == '3':
            calculator("multiply")
        elif choice == '4':
            calculator("divide")
        elif choice == '5':
            print("Exiting calculator.")
            break
        else:
            print("Invalid choice.")

def calculator(operation):
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
        a = float(a)
        b = float(b)
        if operation == "add":
            print("Result:", a + b)
        elif operation == "subtract":
            print("Result:", a - b)
        elif operation == "multiply":
            print("Result:", a * b)
        elif operation == "divide":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero.")
    else:
        print("Invalid input.")

menu()
