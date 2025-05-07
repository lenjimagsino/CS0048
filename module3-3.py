tasks = []

def menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting to-do list.")
            break
        else:
            print("Invalid choice.")

def add_task():
    task = input("Enter the task to add: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

def view_tasks():
    if tasks:
        print("Your Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    else:
        print("No tasks yet.")

menu()
