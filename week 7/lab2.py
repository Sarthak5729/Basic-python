class MembershipRegistrationSystem:
    def __init__(self):
        self.registered_members = []
        self.withdrawn_members = 0

    def register_member(self, student_id, last_name, programme):
        if programme not in ["Diploma", "Bachelor"]:
            print("Invalid programme. Please enter 'Diploma' or 'Bachelor'.")
            return

        membership_id = len(self.registered_members) + 1
        self.registered_members.append({
            "Membership ID": membership_id,
            "Student ID": student_id,
            "Last Name": last_name,
            "Programme": programme
        })
        print(f"Member {last_name} registered successfully with Membership ID {membership_id}.")

    def withdraw_member(self, membership_id, last_name):
        for member in self.registered_members:
            if member["Membership ID"] == membership_id and member["Last Name"] == last_name:
                self.registered_members.remove(member)
                self.withdrawn_members += 1
                print(f"Membership ID {membership_id} withdrawn successfully.")
                return
        print("Membership ID not found or does not match with the last name.")

    def display_registered_members(self):
        diploma_students = len([member for member in self.registered_members if member["Programme"] == "Diploma"])
        bachelor_students = len([member for member in self.registered_members if member["Programme"] == "Bachelor"])
        print("Registered Members:")
        print(f"Total Registered Members: {len(self.registered_members)}")
        print(f"Diploma Students: {diploma_students}")
        print(f"Bachelor Students: {bachelor_students}")
        print(f"Withdrawn Members: {self.withdrawn_members}")

# Create an instance of the MembershipRegistrationSystem
system = MembershipRegistrationSystem()

while True:
    print("\nMembership Registration System")
    print("1. Register Member")
    print("2. Withdraw Member")
    print("3. Display Registered Members")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        last_name = input("Enter Last Name: ")
        programme = input("Enter Programme (Diploma or Bachelor): ")
        system.register_member(student_id, last_name, programme)
    elif choice == "2":
        membership_id = int(input("Enter Membership ID: "))
        last_name = input("Enter Last Name: ")
        system.withdraw_member(membership_id, last_name)
    elif choice == "3":
        system.display_registered_members()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")