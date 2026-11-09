goals = []

while True:
    print("\n===== STUDY PLANNER =====")
    print("1. Add a study goal")
    print("2. View my goals")
    print("3. Delete a goal")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        goal = input("Enter your goal: ")
        goals.append(goal)
        print("Goal added successfully!")

    elif choice == "2":
        if not goals:
            print("No goals yet.")
        else:
            for number, goal in enumerate(goals, 1):
                print(f"{number}. {goal}")

    elif choice == "3":
        for number, goal in enumerate(goals, 1):
            print(f"{number}. {goal}")

        if goals:
            number = int(input("Enter goal number to delete: "))
            if 1 <= number <= len(goals):
                goals.pop(number - 1)
                print("Goal deleted!")

    elif choice == "4":
        print("Good luck with your studies!")
        break

    else:
        print("Invalid choice. Try again.")
