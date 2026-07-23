sales=[25000,50000,73000,90000,45000,70000,89000]
days=len(sales)

def sale_total(sales,days):
    total=0
    i=1
    for sale in sales:
        total+=sale
        print(f"Day {i} : {sale}")
        i+=1
    average=total/days
    return total,average

total,average=sale_total(sales,days)
print("--week sales--")
print("Total sales  : ",total)
print(f"Avrage sales : {average:.2f}")
