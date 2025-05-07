#Temperature Converter

def temperature_converter():
    while True:
        print("\nTemperature Converter Menu:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '3':
            print("Exiting temperature converter. Goodbye!")
            break

        temp = input("Enter temperature: ")

        if temp.replace('.', '', 1).isdigit() or (temp.startswith('-') and temp[1:].replace('.', '', 1).isdigit()):
            t = float(temp)
            if choice == '1':
                print("Temperature in Fahrenheit:", (t * 9 / 5) + 32)
            elif choice == '2':
                print("Temperature in Celsius:", (t - 32) * 5 / 9)
            else:
                print("Invalid choice.")
        else:
            print("Please enter a valid number.")
            
temperature_converter()
