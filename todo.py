tasks = []

while True:


    print("TODO LIST")
    print()
    print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Edit task\n5. Quit")

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

        with open("task.txt", "w") as file:
            count = 1
            for line in lines:
                actual_num = line.split(". ")[0].strip()
                actual_word = line.split(". ")[-1].strip()

                if actual_num != removed_task:
                    file.write(f"{count}. {actual_word}\n")
                    count += 1


        print(f"Removed {removed_task} from the task list.")


    elif choice == 4:

        edited_num = input("Enter the number for the task that you would like to edit: ")

        try:
            with open("task.txt", "r") as file:
                edit_lines = file.readlines()
        except FileNotFoundError:
            print("The file doesn't exist yet")
            lines = []

        edited_task = input("Enter what you would like to change your task to?: ")





    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid option pick again.")
