game_summary = []

rounds_lost = 0
rounds_draw = 0
rounds_played = 5

for item in range(0, 5):
    result = input("Choose result: ")

    outcome = f"Round {item}: {result}"

    if result == "lose":
        rounds_lost += 1

    elif result == "tie":
        rounds_draw += 1

    game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost - rounds_draw

# Calculate game stats
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_draw = rounds_draw / rounds_played * 100

print()
print("*** Game History ***")
for game in game_summary:
    print(game)

print()

# displays game stats with %
# values to nearest who number
print("*** Game Statistics ***")
print("Win: {}, ({:.0f}%) \nLose: {}, ({:.0f}%) \nTie: {}, ({:.0f}%)"
      .format(rounds_won, percent_win, rounds_lost, percent_lose, rounds_draw, percent_draw))
