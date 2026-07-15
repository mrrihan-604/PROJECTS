sales=[25000,50000,73000,90000,45000,70000,89000]
total=0
i=1
days=len(sales)
print("--week sales--")
for sale in sales:
    total+=sale
    print(f"Day {i} : {sale}")
    i+=1
average=total/days
print("Total sales  : ",total)
print(f"Avrage sales : {average:.2f}")
