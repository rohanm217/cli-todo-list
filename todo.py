tasks = []


while True:

    print("TODO LIST")
    print()
    print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Quit")

    choice = int(input("What would you like to pick?: "))
    print()

    if choice == 1:
        task = input("Name a task you have for the today!: ")
        tasks.append(task)

        with open("task.txt", "w") as file:
            for count, item in enumerate(tasks, start=1):
                file.write(f"{count}. {item}\n")

        print("Added to tasks!")

    elif choice == 2:
        with open("task.txt", "r") as file:
            taskContent = file.read()
            print("--- To-Do List ---")
            print(taskContent)

    elif choice == 3:

        removed_task = input("Enter the number of the task that you want to remove: ")

        try:
            with open("task.txt", "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            print("The file doesn't exist yet")
            lines = []

        new_lines = []
        for line in lines:
            if removed_task not in line:
                new_lines.append(line)

        with open("task.txt", "w") as file:
            file.writelines(new_lines)

        print(f"Removed {removed_task} from the task list.")


        # for index, item in enumerate(tasks, start=1):
        #     print(f"{index}. {item}")
        # tr = input("Which task would you like to remove?: ")
        # if tasks[int(tr)-1] not in tasks:
        #     print("Not in To-Do List")
        # tasks.pop(int(tr)-1)
        # print("Task Removed")


    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option pick again.")
