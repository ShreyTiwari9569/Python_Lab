tasks = []

while True:
    print("\n1. Add Task")
    print("2. Run Tasks")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        condition = input("Is condition true? (yes/no): ")
        tasks.append((task, condition == "yes"))
        print("Task added.")

    elif choice == "2":
        if tasks:
            for task, condition in tasks:
                if condition and task:
                    print("Executing:", task)
                elif not condition:
                    print("Condition false:", task)
                else:
                    print("Invalid task.")
            tasks.clear()
        else:
            print("No tasks available.")

    elif choice == "3":
        if tasks:
            print("Scheduled Tasks:")
            for task, condition in tasks:
                print(task, "->", condition)
        else:
            print("No tasks available.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")