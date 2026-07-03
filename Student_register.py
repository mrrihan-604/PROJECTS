# Take student information and course details as input
student_name=input("Enter Student Name:")
student_id=input("Enter Student ID:")
course_name=input("Enter Course Name:")
duration=input("Enter Duration:")
email=input("Enter Email:")
mobile=input("Enter Mobile Number:")
course_fee=float(input("Enter Course Fee:"))
registration_fee=float(input("Enter Registration Fee:"))

# Calculate remaining fee after deducting registration fee
remaining_fee=course_fee-registration_fee

# Display registration slip header and student details
print("\n")
print("  DIGITAL DREAMS INTERNSHIP ")
print("    ---------------------   ")
print("      Registration Slip     ")
print("-"*50)
print(f"Student Name     : {student_name}")
print(f"Student ID       : {student_id}")
print(f"Course Name      : {course_name}")
print(f"Duration         : {duration}")
print(f"Email            : {email}")
print(f"Mobile Number    : {mobile}")
print(f"Course Fee       : {course_fee}")
print(f"Registration Fee : {registration_fee}")
print("-"*50)
# Display fee summary
print(f"Remaining Fee    : {remaining_fee}")
print("\n")
print("Welcome to Digital Dreams Internship! ")