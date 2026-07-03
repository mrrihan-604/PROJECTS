# This program checks the current stock level in a warehouse.
print("\n")
Current_Stock=int(input("Enter your current stock:"))
Minimum_Threshold=50
Maximum_Capacity=200
print("-"*50)
if Current_Stock < Minimum_Threshold or Current_Stock == Minimum_Threshold:
    if Current_Stock < Minimum_Threshold:
        print("Stock in warehouse is LOW!!!!")
    else:
        print("Stock in warehouse is optimal!!")
else:
    if Current_Stock < Maximum_Capacity and Current_Stock > Minimum_Threshold:
        print("Your stock in warehouse is correct!! ")
    else:
        print("Your Stock is overloaded!!")