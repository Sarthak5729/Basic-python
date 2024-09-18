def what_to_do_now():
    message = "Time to "
    prompt = "Enter selection (1,2, or 3): "
    user_choice = int(input(prompt))
    if user_choice == 1:
        print(message, "eat")
    elif user_choice == 2:
        print (message, "play")
    elif user_choice == 3: 
        print(message, "sleep")
    else:
        print("incorrect selection!")
   
what_to_do_now()