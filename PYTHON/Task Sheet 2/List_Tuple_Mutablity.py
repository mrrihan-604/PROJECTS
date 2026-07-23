# The program helps to represent list is mutable and tuple is immutable
# Initalixig tasks list
task_queue = ["Review PR #102", "Fix login bug", "Update documentation"]

# List is mutable so it can be modified
# Modifying tasks list using append and pop
task_queue.append("Prepare for sprint planning") 
completed_task = task_queue.pop(0)                

print(f"Remaining Task Queue: {task_queue}")

office_branches_logs = [
    (12.9716, 77.5946),  # Bengaluru Office 
    (13.0827, 80.2707),  # Chennai Hub 
]

print(f"Office Locations Coordinates: {office_branches_logs}")

# Tring to modify Tuple but tuple is immutabe so it cannot be modified so it will throw exception
try:
    office_branches_logs[0]=(14.8965, 82.7554)
except TypeError as error:
    print(error)