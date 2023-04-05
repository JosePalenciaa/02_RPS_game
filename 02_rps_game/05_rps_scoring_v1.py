rounds_played = 0
rounds_lost = 0
rounds_draw = 0


test_results = ["won", "won", "loss", "loss", "tie"]

for item in test_results:
    rounds_played += 1

    result = item

    if result == "tie":
        result = "It's a tie"
        rounds_draw += 1

    elif result == "loss":
        result = "It's a loss"
        rounds_lost += 1

rounds_won = rounds_played - rounds_lost - rounds_draw

print()
print("End Game Summary")
print(f'Won: {rounds_won} \t\t\tLost: {rounds_lost} \t\tTie: {rounds_draw}')
print()
print("Thank you for playing")
