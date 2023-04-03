while True:

    user_choice = input("User Choice: ")
    comp_choice = input("Comp Choice: ")

    print(f'User chose {user_choice}, Comp chose {comp_choice}')
    if user_choice == comp_choice:
        print("Its a draw / tie.")
