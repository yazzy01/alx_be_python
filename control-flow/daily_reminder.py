# Prompt for task, priority, and time sensitivity
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()  # .lower() to handle input variations
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case for priority
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Complete it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that still requires attention today.")
        else:
            print(f"Reminder: '{task}' is a low priority task. You can complete it when you have time.")
