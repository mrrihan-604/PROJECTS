# Mobile Bill Generator
device_name = input("Enter your device name  : ")
price=float(input("Enter your device price : "))
quantity=int(input("Enter device quantity   : "))
total_price=price*quantity
print("--------Bill Details--------")
print("Device Name     :", device_name)
print("Device Price    :", price)
print("Device Quantity :", quantity)
print("Total Price     :", total_price)