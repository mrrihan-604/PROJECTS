# Empoly bonus eligibility base on experience and rating
print("\n")
print("Enter Empolyee Details")
print("-"*50)
emp_name=input("Enter Employee Name:")  
emp_experience=int(input("Enter Employee years of Experience:"))
emp_rating=float(input("Enter Employee Rating (1 to 10):"))
print("\n")

if emp_experience >= 2 and emp_rating >=8:
    print(f"Employee {emp_name} is eligible for bonus.")
else:
    print(f"Employee {emp_name} is not eligible for bonus.")
print