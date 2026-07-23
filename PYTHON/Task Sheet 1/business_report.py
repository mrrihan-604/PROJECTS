# This is a simple business report generator
print("     Digital Dreams LTD")

# Take monthly income and expenses input from user
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))

# Calculate profit by subtracting expenses from income
profit = income - expenses
print("-" * 30)
print("Business Report")
print("-" * 30)
print(f"Monthly Income   : {income:.2f}/-")
print(f"Monthly Expenses : {expenses:.2f}/-")

# Check company status based on profit/loss condition
if income == 0:
    print("-" * 30)
    print("Company is broke.")
elif income > expenses:
    print(f"Your monthly profit is: {profit:.2f}/-")
    print("-" * 30)
    print("Company is making a profit.")
elif income < expenses:
    print(f"Your monthly loss is: {abs(profit):.2f}/-")
    print("-" * 30)
    print("Company is running at a loss.")
else:
    print("-" * 30)
    print("Company is not making any profit or loss.")
print("\n")