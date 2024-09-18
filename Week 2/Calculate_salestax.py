"""
program wich calculate Grocerie bill
Author = Sarthak Modi
"""
item1=10
item2=20
item3=30

item1=float(input("Enter the price for item1:-"))
item2=float(input("Enter the price for item2:-"))
item3=float(input("Enter the price for item3:-"))
subtotal = item1 + item2 + item3
salestax= subtotal* 0.15
calculatetotal= subtotal + salestax

print("calculatestotal",calculatetotal)
