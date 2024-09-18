def get_earthquake_magnitude(magnitude):
    if 2.0 >= magnitude :
        return "Micro"
    elif 2.0 <= magnitude < 3.0:
        return "Very minor"
    elif 3.0 <= magnitude < 4.0:
        return "Minor"
    elif 4.0 <= magnitude < 5.0:
        return "Light"
    elif 5.0 <= magnitude < 6.0:
        return "Moderate"
    elif 6.0 <= magnitude <= 7.0:
        return "Strong"
    elif 7.0 <= magnitude <= 8.0:
        return "Major"
    elif 8.0 <= magnitude <= 10.0:
        return "Great"
    elif 10.0 <= magnitude  :
        return "Meteroic"
    else :
        return "Too much magnitude Descriptor"

def main():
        
        magnitude = float(input("Enter the magnitude: "))
        magnitude_Descriptor = get_earthquake_magnitude(magnitude)
        
        if magnitude_Descriptor:
            print(f"your entered magnitude is {magnitude_Descriptor} .")
        else:
            print("Error: Please enter a valid number.")
    
   
main()