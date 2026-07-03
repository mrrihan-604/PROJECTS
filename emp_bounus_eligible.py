# Program to check employee bonus eligibility based on experience and performance rating
print("\n")
print("Enter Empolyee Details")
print("-"*50)

# Take employee information as input
emp_name=input("Enter Employee Name:")  
emp_experience=int(input("Enter Employee years of Experience:"))
emp_rating=float(input("Enter Employee Rating (1 to 10):"))
print("\n")

# Check bonus eligibility: minimum 2 years experience and rating >= 8
if emp_experience >= 2 and emp_rating >=8:
    # Display eligibility message if conditions are met
    print(f"Employee {emp_name} is eligible for bonus.")
else:
    # Display ineligibility message if conditions are not met
    print(f"Employee {emp_name} is not eligible for bonus.")
print