# Emp Directory
def print_employee_name(emp):
    i=1
    print("--Employee Names--")
    for empname in emp:
        print(i," : ",empname)
        i+=1
        
emp=["Kido","Rihan","Aditya","Rakshita","Abdul","Sammad","Sanjana"]
print_employee_name(emp)