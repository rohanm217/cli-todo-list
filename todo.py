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
        print("Added to tasks!")

    elif choice == 2:
        for t in range(len(tasks)):
            print(f"{t+1}. {tasks[t]}")
        print("\n\n")
            
    elif choice == 3:
        try:
            for t in range(len(tasks)):
                print(f"{t+1}. {tasks[t]}")
            taskRem = int(input("Which task would you like to remove: "))
            if type(taskRem) == str:
                print("Pick a number!")
            else:
                tasks.pop(taskRem - 1)
            print("Task Removed!\nHere is the new List!")
            for t in range(len(tasks)):
                print(f"{t+1}. {tasks[t]}")
            taskRem = int(input("Which task would you like to remove: "))
        except IndexError:
            print("You haven't entered any tasks yet bitch")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option pick again.")
