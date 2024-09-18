def function1(n1,n2,n3):
    sum = n1+n2+n3
    minimum = min(n1,n2,n3)
    return  sum-minimum

n1 = int(input("enter n1:-"))
n2 = int(input("enter n2:-"))
n3 = int(input("enter n3:-"))
print(function1(n1,n2,n3))
