# This program generates a badge ID by combining department code, joining year, and employee number
print("\n")
print("Badge Generator")
print("-"*50)

# Take input for badge components from user
departmant_code=input("Enter your departmant code:")
joining_year=input("Enter your joining year:")
emp_number=input("Enter your employee number:")

# Generate badge ID by concatenating all three components and display it
id=departmant_code+joining_year+emp_number
print("Badge ID is:",id)
print("\n")