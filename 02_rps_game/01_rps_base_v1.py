import random

# functions go here...


def check_rounds():

    while True:
        response = input("How many rounds (<enter> for continuous): ")

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

game_summary = []

# asks users if they have played, displays instructions if 'no'


# asks user for # rounds + looping

rounds_played = 0
rounds_lost = 0
rounds_draw = 0

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

    # end game with exit code if possible
    if choose == "xxx" and rounds_played > 0:
        break

    elif choose == "xxx":
        print("Play at least 1 round")
        continue

    print()
    print("You chose: {}".format(choose))

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])
    print("Computer chose: ", comp_choice)

    # compare choices
    # checks if user's choice is same as computer's
    # results in a tie
    if choose == comp_choice:
        result = "tied"
        rounds_draw += 1

    # checks if user's choice beats the computers
    # win for the user
    elif choose == "paper" and comp_choice == "rock":
        result = "win"
    elif choose == "scissors" and comp_choice == "paper":
        result = "win"
    elif choose == "rock" and comp_choice == "scissors":
        result = "win"

    # if user's choice isn't a win or tie, user loses
    else:
        result = "lose"
        rounds_lost += 1

    # prints the rounds result
    feedback = f'{choose} vs {comp_choice} - You {result}'
    print(feedback)
    rounds_played += 1

    outcome = f'Round: {rounds_played} - {feedback}'
    game_summary.append(outcome)

    if rounds_played == rounds:
        break

# asks user if they want to see game history


# calculates # of rounds won
rounds_won = rounds_played - rounds_lost - rounds_draw

# show game statistics...
# Calculate game stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_draw = rounds_draw / rounds_played * 100

# Displays the round's battles and results
print()
print("*** Game History ***")
for game in game_summary:
    print(game)

# displays game stats with %
# values to nearest who number

print()
print("#### Game Statistics ####")
print("Win: {}, ({:.0f}%) \nLose: {}, ({:.0f}%) \nTied: {}, ({:.0f}%)"
      .format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_draw, percent_draw))

print()
print("****** End Game Summary ******")
print(f'Won: {rounds_won} \t|\tLost: {rounds_lost} \t|\tTied: {rounds_draw}')
print()
print("!!! Thank you for playing !!!")
