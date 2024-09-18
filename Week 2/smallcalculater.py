"""
program wich calculate the area of circle 
Author = Sarthak Modi
"""
print('''
+ Add
- Subtract
* Multiply
/ Divide
''')
A=int(input("Enter the value1:-"))
B=int(input("Enter the value2:-"))
opr=input("Enter The oper..")
if opr=="+":
	print(A+B)
elif opr=="-":
	print(A+B)
elif opr=="*":
	print(A*B)
elif opr=="/":
 	print(A/B)
elif opr=="//":
	print(A//B)
elif opr=="%":
    print(A%B)
else:
    print("invalide oper....") 
