import random
def user_number_guess(computer_num):
    prompt = "Enter your Guss(1-99): "
    guess = 0
    number = 0
    while number != computer_num:
          number = int(input(prompt))
          guess  +=1 
    if number < computer_num:
       print("Too low ")
    elif  number > computer_num :
       print("Too High ")
    else:
       print(f"Correct ! number of guess : {guess}")
def main():
   user_number_guess(random.randrange(1,100))
main()
        