# Functions go here
def choices_checker(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # If they say 'yes', output 'program continues'
        if response == "rock" or response == "r":
            response = "rock"
            return response

        # If they say 'no', output 'display instructions'
        elif response == "paper" or response == "p":
            response = "paper"
            return response

        elif response == "scissor" or response == "s":
            response = "scissors"
            return response

        else:
            print("Please choose 'rock', 'paper', or 'scissors'")

# Main routine goes here


display_rps = choices_checker("Choose rock (r), paper (p), or scissors (s): ")

print("You have chose {}".format(display_rps))

# Ask user for choice and check it's valid


# Prints out choice for comparison purposes
