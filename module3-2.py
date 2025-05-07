def menu():
    while True:
        print("\nTemperature Converter Menu:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            convert_c_to_f()
        elif choice == '2':
            convert_f_to_c()
        elif choice == '3':
            print("Exiting temperature converter.")
            break
        else:
            print("Invalid choice.")

def convert_c_to_f():
    temp = input("Enter temperature in Celsius: ")
    if is_number(temp):
        c = float(temp)
        f = (c * 9 / 5) + 32
        print("Fahrenheit:", f)
    else:
        print("Invalid number.")

def convert_f_to_c():
    temp = input("Enter temperature in Fahrenheit: ")
    if is_number(temp):
        f = float(temp)
        c = (f - 32) * 5 / 9
        print("Celsius:", c)
    else:
        print("Invalid number.")

def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

menu()
