import random

def play_war_of_bets():
    # Simulate a single game of War of Bets
    player_card = random.randint(1, 13)
    dealer_card = random.randint(1, 13)
    if player_card > dealer_card:
        return 'player'
    elif player_card < dealer_card:
        return 'dealer'
    else:
        return 'war'

# Simulate 100 games of War of Bets
num_simulations = 1000
results = []
for i in range(num_simulations):
    result = play_war_of_bets()
    results.append(result)

# Calculate the number of runs for each player
player_runs = 1
dealer_runs = 1
war_runs = 1
prev_result = results[0]
for result in results[1:]:
    if result == prev_result:
        if result == 'player':
            player_runs += 1
        elif result == 'dealer':
            dealer_runs += 1
        elif result == 'war':
            war_runs += 1
    prev_result = result


print("Number of runs for player:", player_runs)
print("Number of runs for dealer:", dealer_runs)
print("Number of runs for war:", war_runs)
# Calculate the expected number of runs based on the formula
n = len(results)
p = 1/3  # Probability of a win, loss, or tie for each game
q = 1 - p
E_player = n * (p**2) / (q**2 + 2*p*q)
E_dealer = n * (p**2) / (q**2 + 2*p*q)
print("Expected number of runs for player:", E_player)
print("Expected number of runs for dealer:", E_dealer)
