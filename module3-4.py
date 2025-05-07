import random

def menu():
    while True:
        print("\nNumber Guessing Game Menu:")
        print("1. Play")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            play_game()
        elif choice == '2':
            print("Exiting game.")
            break
        else:
            print("Invalid choice.")

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("Guess a number between 1 and 100.")

    while True:
        guess = input("Your guess: ")
        if guess.isdigit():
            guess = int(guess)
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        else:
            print("Please enter a valid number.")

menu()
