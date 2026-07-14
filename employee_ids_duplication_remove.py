employee_ids=["Ak47","Ak97","Ak40","Ak97","Ak47","Ak35","Ak40","Ak20","Ak24"]
duplicate_count=len(employee_ids)
employee_ids=set(employee_ids)
unique_count=len(employee_ids)
count=duplicate_count-unique_count
print("Duplicates ids count : ",count)
