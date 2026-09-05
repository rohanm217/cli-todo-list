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
        for index, item in enumerate(tasks, start=1):
            print(f"{index}. {item}")
        print("\n\n")
            
    elif choice == 3:

        tr = input("Which task would you like to remove?: ")


    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option pick again.")
