def student_info() :

 id = input("Enter your student ID: ")
 student_first_Name = input( "Enter your first name: ")
 student_last_Name = input ("Enter your last name:")
 university = input("Which university do you attend?: ").Lower()

 if "whitecliffe" in university and "college" in university:
      username = id[:2] + student_last_Name[ :3]
      print("Welcome to Whitecliffe Collegel Your username is", username)
 else:
    print("Please have your university generate your username.")
def main() :
    student_info()
main()