# Functions go here
def choices_checker(question):

    error = "Please choose rock / paper / scissors (or xxx to quit)"

    valid = False
    while not valid:
        response = input(question).lower()

        # If they say 'yes', output 'program continues'
        if response == "rock" or response == "r":
            return "rock"

        # If they say 'no', output 'display instructions'
        elif response == "paper" or response == "p":
            return "paper"

        elif response == "scissors" or response == "s":
            return "scissors"

        # exit code
        elif response == "xxx":
            return response

        else:
            print(error)

# Main routine goes here

# Looping for test


display_rps = ""
while display_rps != "xxx":

    display_rps = choices_checker("Choose rock (r), paper (p), or scissors (s): ")

    print("You have chosen '{}'".format(display_rps))

# Ask user for choice and check it's valid


# Prints out choice for comparison purposes
