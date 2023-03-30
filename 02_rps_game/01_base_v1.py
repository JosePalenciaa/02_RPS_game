import random

# functions go here...


def check_rounds():

    while True:
        response = input("How many rounds do you want to play: ")

        round_error = "Please type either < enter >, " \
                      "or an integer that is more than 0\n"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def choices_checker(question, valid_list, error):

    while True:
        response = input(question).lower()

        # Accepts items in a list and displays the full name
        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # Outputs error
        print(error)
        print()


# main routine goes here...

# list of valid responses...
yes_no = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# asks users if they have played, displays instructions if 'no'


# asks user for # rounds + looping

rounds_played = 0

# Ask user for # of rounds, < enter > for infinite
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose_instruction = "Choose rock (r), paper (p), scissors (s), or 'xxx' (x) to quit: "
    choose_error = "INVALID - please choose rock, paper, scissors, or 'xxx'"

    # Ask user for choice, checks if it is valid
    choose = choices_checker(choose_instruction, rps_list, choose_error)

    # end game with exit code
    if choose == "xxx":
        break

    print("You chose '{}'".format(choose))

    rounds_played += 1

    if rounds_played == rounds:
        break

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice, end='\t')

    # compare choices

# asks user if they want to see game history


# show game statistics...
