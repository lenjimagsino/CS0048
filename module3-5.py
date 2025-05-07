#Student Grade Calculator

def student_grade_calculator():
    scores = []
    while True:
        print("\nStudent Grade Calculator Menu:")
        print("1. Add Score")
        print("2. Calculate Average")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '3':
            print("Exiting grade calculator. Goodbye!")
            break
        elif choice == '1':
            subject = input("Enter the subject: ")
            score = input("Enter the score: ")
            if score.replace('.', '', 1).isdigit():
                scores.append(float(score))
                print("Score added.")
            else:
                print("Please enter a valid numeric score.")
        elif choice == '2':
            if scores:
                average = sum(scores) / len(scores)
                print(f"Average Grade: {average:.2f}")
            else:
                print("No scores available to calculate average.")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
student_grade_calculator()