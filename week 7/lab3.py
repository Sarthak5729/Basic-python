class RequestSystem:
    def __init__(self):
        self.request_id_counter = 1
        self.requests = []

    def user_info(self, name, age, email):
        user_details = {
            "name": name,
            "age": age,
            "email": email
        }
        return user_details

    def request_details(self, items):
        total_amount = 0
        request_items = []
        for item in items:
            total_amount += item["cost"]
            request_items.append(item)
        return total_amount, request_items

    def request_approval(self, total_amount):
        if total_amount < 150:
            return "approved"
        else:
            return "pending"

    def respond_request(self, request_id, status):
        for request in self.requests:
            if request["id"] == request_id:
                request["status"] = status
                break

    def display_request(self):
        for request in self.requests:
            print(f"Request ID: {request['id']}")
            print(f"Name: {request['user_details']['name']}")
            print(f"Total: ${request['total_amount']:.2f}")
            print(f"Status: {request['status']}")
            print("")

    def request_statistic(self):
        total_requests = len(self.requests)
        approved_requests = len([request for request in self.requests if request["status"] == "approved"])
        pending_requests = len([request for request in self.requests if request["status"] == "pending"])
        not_approved_requests = len([request for request in self.requests if request["status"] == "not approved"])
        print(f"Total number of requests submitted: {total_requests}")
        print(f"Total number of approved requests: {approved_requests}")
        print(f"Total number of pending requests: {pending_requests}")
        print(f"Total number of not approved requests: {not_approved_requests}")

    def submit_request(self, user_details, items):
        total_amount, request_items = self.request_details(items)
        status = self.request_approval(total_amount)
        request = {
            "id": self.request_id_counter,
            "user_details": user_details,
            "items": request_items,
            "total_amount": total_amount,
            "status": status
        }
        self.requests.append(request)
        self.request_id_counter += 1

    def main(self):
        while True:
            print("1. Submit Request")
            print("2. Respond to Request")
            print("3. Display Requests")
            print("4. Request Statistics")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                email = input("Enter your email: ")
                user_details = self.user_info(name, age, email)
                num_items = int(input("Enter the number of items: "))
                items = []
                for i in range(num_items):
                    item_name = input(f"Enter item {i+1} name: ")
                    item_cost = float(input(f"Enter item {i+1} cost: "))
                    item = {"name": item_name, "cost": item_cost}
                    items.append(item)
                self.submit_request(user_details, items)
            elif choice == "2":
                request_id = int(input("Enter the request ID: "))
                status = input("Enter the status (Approved/Not Approved): ")
                self.respond_request(request_id, status)
            elif choice == "3":
                self.display_request()
            elif choice == "4":
                self.request_statistic()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    request_system = RequestSystem()
    request_system.main()

    