
"""
description :- create a function which create generate unique id  for each user and store user information in a dictionary
Author Sarthak modi


"""
def  collect_user_information(id_counter):
    print("Enter User information")
    name  = input("Name: ")
    age  = input("Age: ")
    email  = input("Email: ")

    unique_id = id_counter + 1
    id_counter = unique_id
    print("User information")
    print("User name :", name)
    print("Useg  age :", age)
    print("User email :", email)
    print("User id :",unique_id)
def main():
    id_counter = 5000
    collect_user_information(id_counter)
main()



