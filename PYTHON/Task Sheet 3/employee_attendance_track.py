i=1
present=0
absent=0
attendance={}
print("Enter 0 for present 1 for absent :")
while (i<=30):
    j=int(input(f"{i} : "))
    attendance[i]=j
    if j == 0:
        absent+=1
    else:
        present+=1
    i+=1

print("--Employee Attendance--")
percentage=(present/30)*100
print("Present    : ",present)
print("Absent     : ",absent)
print("Precentage : ",percentage)
if percentage == 100:
    status="Perfect"
elif percentage > 75:
    status="Good"
else:
    status="To Low"
print("Status     : ",status)