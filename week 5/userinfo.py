def collect_user_data(id_counter):
 
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    user_email = input("Enter your email: ")

    id_counter += 1
    user_id = id_counter

    user_data = {
        "name": user_name,
        "age": user_age,
        "email": user_email,
        "id": user_id
    }

    print("User Information:")
    print("----------------")
    print(f"Name: {user_name}")
    print(f"Age: {user_age}")
    print(f"Email: {user_email}")
    print(f"ID: {user_id}")
    print("----------------")

    return id_counter, user_id, user_data

def calculate_total_amount():
    
    total_amount = 0
    while True:
        price = input("Enter the price of an item (or 'finish' to stop): ")
        if price.lower() == "finish":
            break
        total_amount += float(price)

    print(f"Total Amount: ${total_amount:.2f}")

    return total_amount

def categorize_request(total_amount):
    
    if total_amount < 150:
        category = "Low"
        recommendation = "Proceed with standard processing."
    else:
        category = "High"
        recommendation = "Review for potential discounts."

    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")

    return {"category": category, "recommendation": recommendation}

def create_detailed_report(user_data, total_amount, categorization):
    
    print("Detailed Report:")
    print("----------------")
    print(f"User's Name: {user_data['name']}")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Category: {categorization['category']}")
    print(f"Recommendation: {categorization['recommendation']}")
    print("----------------")

def main_lab1():
    id_counter = 5000
    id_counter, user_id, user_data = collect_user_data(id_counter)

def main_lab2():
    total_amount = calculate_total_amount()

def main_lab3():
    total_amount = calculate_total_amount()
    categorization = categorize_request(total_amount)

def main_lab4():
    id_counter = 5000
    id_counter, user_id, user_data = collect_user_data(id_counter)
    total_amount = calculate_total_amount()
    categorization = categorize_request(total_amount)
    create_detailed_report(user_data, total_amount, categorization)

if __name__ == "__main__":
    main_lab1()
    main_lab2()
    main_lab3()
    main_lab4()