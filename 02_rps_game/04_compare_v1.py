rps_list = ["rock", "paper", "scissors"]

comp_index = 0

for item in rps_list:
    user_index = 0

    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # compare options...
        print()
        print(f'You chose:  {user_choice}. Comp chose: {comp_choice}')

        if user_choice == comp_choice:
            result = "tie"
            print("Its a draw / tie.")
        elif user_choice == "paper" and comp_choice == "rock":
            result = "win"
        elif user_choice == "scissors" and comp_choice == "paper":
            result = "win"
        elif user_choice == "rock" and comp_choice == "scissors":
            result = "win"
        else:
            result = "lose"
            print("😢You lose😢")

        if result == "win":
            print("✔you win✔")

    comp_index += 1
