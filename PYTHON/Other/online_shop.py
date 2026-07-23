try:
    order_amount=float(input("Enter the order amount: "))
    payment=float(input("Enter the payment amount: "))

    if payment<=0:
        raise ValueError("Payment must be greater than 0")
    if payment<order_amount or payment>order_amount:
        raise Exception("Entered Amount is incorrect Recheck Entered Amount")

    if payment==order_amount: 
        print("Order Placed Successfully")

except ValueError as e:
    print("Input Error:",e)
except Exception as e:
    print("Transaction failed:",e)
finally:
    print("THANKYOU FOR SHOPPING!")