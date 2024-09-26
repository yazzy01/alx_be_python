# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Match case for the priority
match priority.lower():
    case 'high':
        reminder = f"Reminder: '{task}' is a high priority task"
    case 'medium':
        reminder = f"Reminder: '{task}' is a medium priority task"
    case 'low':
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

# Check if the task is time-bound
if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Output the customized reminder
print(reminder)
