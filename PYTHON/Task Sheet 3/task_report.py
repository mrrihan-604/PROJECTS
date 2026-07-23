
report_meta = ("Sarah Jenkins", "Data Analytics & Training")

tasks_completed = [
    "Data Cleaning Script",
    "API Integration Blueprint",
    "SQL Query Optimization",
    "Dashboard Mockup Design",
    "Code Review Session"
]

task_hours = {
    "Data Cleaning Script": 6.5,
    "API Integration Blueprint": 4.0,
    "SQL Query Optimization": 5.0,
    "Dashboard Mockup Design": 3.5,
    "Code Review Session": 2.0
}

skills_practiced = {"Python", "SQL", "API Design", "Data Visualization", "Git"}

# 5. Function to Summarize the Week Using a Loop
def summarize_week(tasks, hours_dict):
    total_hours = 0.0
    for task in tasks:
        # Fetch hours from the dictionary; default to 0 if task isn't found
        total_hours += hours_dict[task]
    return total_hours

# --- Execution & Reporting Logic ---

total_spent = summarize_week(tasks_completed, task_hours)

print("=" * 40)
print(f"WEEKLY PERFORMANCE REPORT")
print("=" * 40)
print(f"Manager: {report_meta[0]}")
print(f"Department: {report_meta[1]}")
print("-" * 40)
print(f"Tasks Completed: {len(tasks_completed)}")
print(f"Skills Sharpened: {', '.join(skills_practiced)}")
print(f"Total Hours Invested: {total_spent} hours")
print("-" * 40)

# 6. Conditional Status Check
if total_spent >= 20:
    print("Status: On Track ")
else:
    print("Status: Needs Catch-up ")
print("=" * 40)