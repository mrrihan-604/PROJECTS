def bonus_eligible(rating,experience):
    if experience > 2 and rating >= 8 :
        return "Eligible for Bonus..."
    else:
        return "Not Eligible for Bonus..."

print("Enter employee detals---")
emp_details=[]
emp_count=int(input("Enter number of employes : "))
for i in range(emp_count):
    emp_name=input("Enter empolyee name : ")
    exprence=int(input("Enter emplyee exprence : "))
    rating=int(input("Enter employee rating : "))
    bonus=bonus_eligible(rating,exprence)
    emp_details.append([emp_name,exprence,rating,bonus])

for emp in emp_details :
    print(f"{emp[0]} : {emp[3]}")