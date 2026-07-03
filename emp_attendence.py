# Employee Attendance Management System
print("\n")
total_working_days = 30
employee_name = input("Enter employee name: ")
attendance_days = int(input("Enter number of days attended: "))

attendance_percentage = (attendance_days / total_working_days) * 100
print("\n")
print("          Employee Attendance Report         ")
print("-" * 50)
print(f"Employee Name           : {employee_name}")
print(f"Total Working Days      : {total_working_days}")
print(f"Days Attended           : {attendance_days}")
print(f"Attendance Percentage   : {attendance_percentage:.2f}%")

if attendance_percentage >= 95:
    print("Status               : Excellent Attendance Elegible for Bonus")
elif attendance_percentage < 95 and attendance_percentage >= 75:
    print("Status               : Good Attendance normal salary ")
else:   
    print("Status               : Poor Attendance, cutoff in salary.")
print("\n")