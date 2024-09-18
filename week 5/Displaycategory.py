

def  calculate_total_amount():
    total_amount = 0
    while True:
        price = input("Enter the price of an item (or 'finish' to stop): ")
        if price.lower() == "finish":
            break
        total_amount = total_amount + float(price)
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
def  main_answer():
    total_amount = calculate_total_amount()
    categorization = categorize_request(total_amount)
main_answer()
    



    
