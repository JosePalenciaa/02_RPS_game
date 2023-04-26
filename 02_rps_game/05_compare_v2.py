while True:

    user_choice = input("User Choice: ")
    comp_choice = input("Comp Choice: ")

    print(f'User chose {user_choice}, Comp chose {comp_choice}')
    if user_choice == comp_choice:
        print("Its a draw / tie.")

    elif user_choice == "rock" and comp_choice == "paper":
        print("You lose")
