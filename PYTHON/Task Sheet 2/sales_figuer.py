# Sales Figures sorting and reversing using sort() and reverse() methods
print("Sales Figures sorting and reversing")
# Original sales figures
sales=[12000,25000,34000,23000,19000,15000,64000]
print(f"Sales figures: {sales}")
# Sorting the sales figures in ascending order
sales.sort()    
print(f"Sorted sales figures: {sales}")
revsales=sales.copy()
# Reversing the sales figures
revsales.reverse()
print(f"Reversed sales figures: {revsales}")