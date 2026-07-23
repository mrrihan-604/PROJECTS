# Project Office Management System

tasks_to_do = ["Prepare meeting agenda", "Send out invites", "Book conference room"]
print("Initial tasks to do:", tasks_to_do)

# 1. Using append() to add a new task at the very end
print("Poping first task from the list:", tasks_to_do.pop(0))
print("Tasks to do after popping:", tasks_to_do)

# 2. Using extend() to add multiple tasks at once
client_tasks = ["Prepare client presentation", "Send proposal", "Follow up on feedback"]
print("Initial client tasks:", client_tasks)
tasks_to_do.extend(client_tasks)
print("Tasks to do after extending with client tasks:", tasks_to_do)