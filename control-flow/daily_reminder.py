task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print("You have no pending task!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print("You have no pending task!")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print("You have no pending task!")
    case _:
        print("Please add a valid task")