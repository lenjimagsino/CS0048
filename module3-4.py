#Number Guessing Game

import random

def number_guessing_game():
    while True:
        print("\nNumber Guessing Game Menu:")
        print("1. Play Number Guessing Game")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '2':
            print("Exiting game. Goodbye!")
            break
        elif choice == '1':
            number = random.randint(1, 100)
            attempts = 0
            print("Guess a number between 1 and 100.")
            while True:
                guess = input("Guess the number: ")
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
        else:
            print("Invalid choice. Please enter 1 or 2.")

number_guessing_game()