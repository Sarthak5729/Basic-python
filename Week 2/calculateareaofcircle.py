"""
Author = Sarthak Modi
"""

cover_prize_book=24.95
total_copies=60
first_copy_shippingcost=3
other_copy_shippingcost =0.75
discount= cover_prize_book*0.40
cost_of_firstbook= first_copy_shippingcost+(cover_prize_book-discount)
cost_of_otherbooks=(other_copy_shippingcost*59)+(14.97*59)
wholesale= cost_of_firstbook + cost_of_otherbooks
print("discount:=",discount)
print("cost of firstbook:=",cost_of_firstbook)
print("cost of othertbooks:=",cost_of_otherbooks)
print("total wholesale cost:=",wholesale,sep="")
