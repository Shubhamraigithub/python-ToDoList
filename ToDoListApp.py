def main():
    tasks = []  # Create an empty list to store tasks

    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            print("Thank you for using the To-Do List program!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_task(tasks):
    task = input("Enter the task description: ")
    tasks.append(task)
    print("Task added successfully.")

def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    main()
