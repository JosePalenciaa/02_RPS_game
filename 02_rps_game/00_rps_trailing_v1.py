import random

# main routine goes here...

rps = ["scissors", "rock", "paper", 'xxx']

# testing loop to generate 20 tokens
# accounts for all values in the list,
# except for the last one (-1)
comp_choice = random.choice(rps[:-1])
print(comp_choice, end='\t')
