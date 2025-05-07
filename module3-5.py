scores = []

def menu():
    while True:
        print("\nGrade Calculator Menu:")
        print("1. Add Score")
        print("2. Calculate Average")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_score()
        elif choice == '2':
            calculate_average()
        elif choice == '3':
            print("Exiting grade calculator.")
            break
        else:
            print("Invalid choice.")

def add_score():
    subject = input("Enter subject name: ")
    score = input("Enter score: ")
    if score.replace('.', '', 1).isdigit():
        scores.append(float(score))
        print("Score added.")
    else:
        print("Invalid score.")

def calculate_average():
    if scores:
        avg = sum(scores) / len(scores)
        print(f"Average Score: {avg:.2f}")
    else:
        print("No scores added yet.")

menu()
