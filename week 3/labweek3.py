def get_color_from_wavelength(wavelength):
    if 380 <= wavelength < 450:
        return "Violet"
    elif 450 <= wavelength < 495:
        return "Blue"
    elif 495 <= wavelength < 570:
        return "Green"
    elif 570 <= wavelength < 590:
        return "Yellow"
    elif 590 <= wavelength < 620:
        return "Orange"
    elif 620 <= wavelength <= 750:
        return "Red"
    else:
        return None

def main():
   
        wavelength = float(input("Enter the wavelength (in nm): "))
        color = get_color_from_wavelength(wavelength)
        
        if color:
            print(f"The color corresponding to {wavelength} nm is {color}.")
        else:
            print("Error: The wavelength is outside the visible spectrum (380 nm to 750 nm).")
    
main()