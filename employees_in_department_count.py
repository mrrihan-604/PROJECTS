# The PMO task list (using a list of dictionaries for clean data mapping)
departments = {"Developer":8 ,"Debugger":8 ,"Tester":2 ,"Hr":5}

# Loop through the task list
for department in departments:
    dep=department
    emp=departments[department]
    print(f" department : {dep}   \n emmployess : {emp}  \n")
    