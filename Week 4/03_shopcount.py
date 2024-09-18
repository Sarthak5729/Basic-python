def show_output():
    number = 1
    count = 10
    value=4
    while count > 4:
        count = count- 2
        print(str(number) + ":", count, value) 
    value += count
    number += 1
    print()
    print(str(number) + "1", count, value)
def main():    
    show_output()
main()