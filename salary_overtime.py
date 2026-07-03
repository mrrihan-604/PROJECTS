# Given hours_worked and standard working_hours = 8, calculate overtime_hours (if any) and overtime_pay at 1.5x the hourly rate.

standard_working_hours = 8
hourly_rate = 1.5
standard_salary = float(input("Enter standard salary: "))
worked_hours = float(input("Enter total hours worked: "))
overtime_hours =worked_hours-standard_working_hours 
overtime_pay = standard_salary * hourly_rate * overtime_hours / standard_working_hours
salry = standard_salary + overtime_pay

if worked_hours > standard_working_hours:
    print(f"Overtime hours: {overtime_hours}")
    print(f"Total salary including overtime pay: {salry:.2f}")
else:
    print(f"No overtime hours. salary: {standard_salary:.2f}")
