# 1. Immutable Manager & Department Info (Tuple)
# Because managers change their minds, but they shouldn't change mid-report! 😉
report_meta = ("Sarah Jenkins", "Data Analytics & Training")

# 2. List of Tasks Completed
tasks_completed = [
    "Data Cleaning Script",
    "API Integration Blueprint",
    "SQL Query Optimization",
    "Dashboard Mockup Design",
    "Code Review Session"
]

# 3. Dictionary Mapping Tasks to Hours Spent
task_hours = {
    "Data Cleaning Script": 6.5,
    "API Integration Blueprint": 4.0,
    "SQL Query Optimization": 5.0,
    "Dashboard Mockup Design": 3.5,
    "Code Review Session": 2.0
}

# 4. Set of Unique Skills Practiced
# Sets are perfect here—no double-dipping on the same skill! 🎯
skills_practiced = {"Python", "SQL", "API Design", "Data Visualization", "Git"}

# 5. Function to Summarize the Week Using a Loop
def summarize_week(tasks, hours_dict):
    total_hours = 0.0
    for task in tasks:
        # Fetch hours from the dictionary; default to 0 if task isn't found
        total_hours += hours_dict.get(task, 0)
    return total_hours

# --- Execution & Reporting Logic ---

# Calculate total hours using our function
total_spent = summarize_week(tasks_completed, task_hours)

# Print the formal report output
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