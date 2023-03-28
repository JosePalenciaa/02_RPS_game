def check_rounds():

    while True:
        response = input("How many rounds do you want to play: ")

        round_error = "Please type either < enter >, " \
                      "or an integer that is more than 0"

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


# main routine...

rounds_played = 0
choose_instruction = "Please choose rock (r), paper (p), or scissors (s)"

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

    choose = input("{} or 'xxx' to end: ".format(choose_instruction))

    if choose == "xxx":
        break

    print("You chose {}".format(choose))

    rounds_played += 1

    if rounds_played == rounds:
        break

print("Thank you for playing!")
