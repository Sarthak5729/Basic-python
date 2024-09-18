def what_to_wear(temperature):
    if temperature > 25:
        print("Wear shorts.")
    else:
        print("Not hot today!")
        print("Enjoy yourself.")
    print("Wear long pants.")
def main():
    what_to_wear(20)
    print()
    what_to_wear(30)
main()