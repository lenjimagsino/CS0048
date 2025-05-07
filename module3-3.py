#To-Do List

def todo_list():
    tasks = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '4':
            print("Exiting to-do list. Goodbye!")
            break
        elif choice == '1':
            task = input("Enter the task to add: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("Task removed.")
            else:
                print("Task not found.")
        elif choice == '3':
            print("Current Tasks:")
            if tasks:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
            else:
                print("No tasks added.")
        else:
            print("Invalid choice. Please select from 1 to 4.")
        
todo_list()