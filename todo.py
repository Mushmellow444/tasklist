tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    # VIEW TASKS
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # ADD TASK
    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    # REMOVE TASK
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")

    # EXIT
    elif choice == "4":
        print("Goodbye!")
        break

    # INVALID INPUT
    else:
        print("Invalid choice. Please select 1-4.")
