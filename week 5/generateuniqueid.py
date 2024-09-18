# Lab 1 - Collecting User Information
def collect_user_data(id_counter):
    """
    Collects user information and generates a unique ID.

    Args:
        id_counter (int): Current ID counter value

    Returns:
        tuple: Updated ID counter, generated ID, user data
    """
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

# Lab 2 - Summing Up Prices
def calculate_total_amount():
    """
    Calculates the total amount by inputting item prices.

    Returns:
        float: Total amount
    """
    total_amount = 0
    while True:
        price = input("Enter the price of an item (or 'finish' to stop): ")
        if price.lower() == "finish":
            break
        total_amount += float(price)

    print(f"Total Amount: ${total_amount:.2f}")

    return total_amount

# Lab 3 - Decision Based on Total
def categorize_request(total_amount):
    """
    Categorizes and provides a recommendation based on the total amount.

    Args:
        total_amount (float): Total amount

    Returns:
        dict: Category and recommendation
    """
    if total_amount < 150:
        category = "Low"
        recommendation = "Proceed with standard processing."
    else:
        category = "High"
        recommendation = "Review for potential discounts."

    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")

    return {"category": category, "recommendation": recommendation}

# Lab 4 - Detailed Report
def create_detailed_report(user_data, total_amount, categorization):
    """
    Creates a detailed report based on user data and categorization.

    Args:
        user_data (dict): User data
        total_amount (float): Total amount
        categorization (dict): Category and recommendation

    Returns:
        None
    """
    print("Detailed Report:")
    print("----------------")
    print(f"User's Name: {user_data['name']}")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Category: {categorization['category']}")
    print(f"Recommendation: {categorization['recommendation']}")
    print("----------------")

def main():
    id_counter = 5000
    id_counter, user_id, user_data = collect_user_data(id_counter)
    total_amount = calculate_total_amount()
    categorization = categorize_request(total_amount)
    create_detailed_report(user_data, total_amount, categorization)

if __name__== "__main__":
    main()