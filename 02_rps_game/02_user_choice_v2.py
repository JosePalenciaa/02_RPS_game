# Functions go here
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

# Main routine goes here

# Accepted values


rps_list = ["rock", "paper", "scissors", "xxx"]

# Looping for test
display_rps = ""
while display_rps != "xxx":

    display_rps = choices_checker("Choose rock (r), paper (p), "
                                  " scissors (s), or 'xxx' to quit: ", rps_list,
                                  "Please choose rock / paper / scissors "
                                  "(or xxx to quit)")

    print("You have chosen '{}'".format(display_rps))
