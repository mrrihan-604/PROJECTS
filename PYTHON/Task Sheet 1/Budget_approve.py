# Gather user inputs for the budget allocation check
allocated_budget = float(input("Enter the total allocated budget: "))
budget_amount = float(input("Enter the requested budget amount: "))
department_performance_score = float(input("Enter the department performance score (0-10): "))

# Check if the requested budget is within the allowed limits
budget_ok = budget_amount <= allocated_budget

# Check if the department meets the performance threshold
performance_ok = department_performance_score >= 7

# Use a logical AND operator to evaluate the final approval status
is_approved = budget_ok and performance_ok

# Output the evaluation result directly to the console
print("Budget Approval Status:", is_approved)