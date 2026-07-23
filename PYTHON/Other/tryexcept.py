try:
    balance = float(input("Enter Account Balance : "))
    withdraw = float(input("Enter Withdrawal Amount : "))

    if withdraw <= 0:
        raise ValueError("Withdrwal amount must be greter then 0.")
    
    if withdraw > balance :
        raise Exception("Insufficient Balance!")
    
    balance-=withdraw

    print("Withdrawal Successful")
    print("Remaning Balance = ",balance)

except ValueError as e:
    print("Input Error:",e)

except Exception as e:
    print("Transaction Failed:",e)

finally:
    print("Thanks for using DD Bank ATM.")