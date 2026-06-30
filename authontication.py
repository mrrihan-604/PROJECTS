tpin = "1234"
attempt = 3
while attempt > 0:
    pin = input("Enter your pin : ")
    if pin == tpin:
        print("-----Welcome-----")
        break
    else:
        attempt -= 1
        if attempt > 0:
            print("Incorrect PIN. Try agoin......")
        else:
            print("Account blocked! Too many incorrect Pins.")