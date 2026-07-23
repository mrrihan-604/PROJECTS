# devlopa pgm that creates a class where it will check 
# wheter customer purches the product first time and wherhet he purchsed above 12000 give 35% descount
# wheter customer purches the product first time and wherhet he purchsed below 12000 give 5% descount
# if both conditions are false donnot provide discount

class check_discount:

    def cutomer_list(self,customer,bill,customers):
        if customer not in customers and bill >= 12000 :
            discount=bill*0.35
            total=bill-discount
            print("35% discount")

            return discount,total
        
        elif customer not in customers and bill < 12000 :
            discount=bill*0.05
            total=bill-discount
            print("5% discount")
            return discount,total
        
        else:
            discount=0
            return discount,bill
        
customers=["Rihan","Abdul"]
while True:
    customer=input("Enter customer name - ")
    bill=int(input("Enter bill amount - "))
    check=check_discount()
    discount,total=check.cutomer_list(customer,bill,customers)
    if customer not in customers:
        customers.append(customer)
    print(f"Discount = {discount:.2f}")
    print(f"Final Amount = {total:.2f}")
    print("\n")
        