
"""
Desccriptin :- This the function to get the information of a staff employee
Author :- Sarthak modi
"""
def staff_info(id_counter):
    print("Enter Staff Information")
    Date = input("Date :")
    Staff_id =input("Staff Id:")
    Staff_name = input("Staff name")

    unique_id = id_counter + 1 
    id_counter = unique_id

    print("staff employee information")
    print("User name :", Staff_name)    
    print("User id :", unique_id)
    print("Date :", Date)

def main():
    id_counter = 10000
    
    staff_info (id_counter)
main()
