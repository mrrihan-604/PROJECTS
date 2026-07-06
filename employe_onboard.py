# Initial onboarding checklist for DDI new hires
print("...Welcome to the DDI Employee Onboarding Checklist Program...")
print("-" * 40)

onboarding_checklist = ["Laptop issued", "ID card created"]
print(f"Initial Checklist: {onboarding_checklist}")
print("-" * 40)

# 1. Using append() to add a new task at the very end
task=input("Enter a new onboarding task to append: ")
onboarding_checklist.append(task)
print(f"After appending a new task: {onboarding_checklist}")
print("-" * 40)

# 2. Using insert() to push an urgent task to position 0 (the absolute front)
task=input("Enter an urgent onboarding task to insert at the beginning: ")
onboarding_checklist.insert(0, task)
print(f"After inserting an urgent task at position 0: {onboarding_checklist}")