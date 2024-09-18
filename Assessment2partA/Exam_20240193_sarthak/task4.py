"""
Description :- create a python function 
Author:- Sarthak
"""

def staff_info(id_counter):
    Date = input("Enter the date : ")
    Staff_id = input("Enter the staff id : ")
    Staff_name = input("Enter the staff name : ")
    unique_id = id_counter + 10000
    print("staff employee information")
    print("User name :", Staff_name)
    print("User id :", unique_id)
    print("Date :", Date)
    return {"Date": Date, "Staff_id": Staff_id, "Staff_name": Staff_name, "unique_id": unique_id}

def requisition_total(staff_info):
    total_amount = 0
    while True:
        item = input("Hello employee enter the name of the item (or type 'done' to finish) :")
        if item.lower() == 'done' :
            break
        try:
            price = float(input(f"Enter the price of '{item}': $"))
            total_amount += price
        except ValueError:
            print("Invalid price. Please enter a numeric value for the price.")
    return total_amount , staff_info
def requisition_approval(total_amount, staff_info):
    if total_amount < 500:
        status = "pending"
    else:
        status = "approved"
    print(f"Category: {status}")
    if status == "approved":
        approval_refrence_number = f"{staff_info['Staff_id']}{staff_info['unique_id'][-3:]}"
        return {"category": status, "approval_refrence_number": approval_refrence_number}
    else:
        return {"category": status}
def create_detailed_report(user_data, status, categorization):
    
    print("Detailed Report:")
    print("----------------")
    print(f"User's Name: {user_data['name']}")
    print(f"status : ${status:.2f}")
    print(f"Category: {categorization['category']}")
    print("----------------")
    return user_data,status
def  main_answer():
    id_counter = 10000
    staff_info = staff_info(id_counter)
    total_amount = requisition_total(staff_info)
    categorization = requisition_approval(total_amount, staff_info)
    print(categorization)
main_answer()




    
