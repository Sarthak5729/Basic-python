"""
program wich calculate interest 
Author = Sarthak Modi
"""
Principal = 100
years = 15
interest = 10

final_amount = Principal *(1+interest/100) ** years

print("Principal is $", Principal,sep="")
print("final amount" , final_amount,sep="")
