import random

# main routine goes here...

rps = ["scissors", "rock", "paper", 'xxx']

# testing loop to generate 20 tokens
# accounts for all values in the list,
# except for the last one (-1)
comp_choice = random.choice(rps[:-1])
print("Computer chose: ", comp_choice)

fruit_list = []

for item in range(0, 4):
    fruit = input("Fruit: ")
    fruit_list.append(fruit)

print()
print("*** The Fruit List***")

for item in fruit_list:
    print(item)
