import random
from scipy.stats import norm

def runs_test(deck_size, set_size, sample_size, alpha=0.05):
    num_runs = sample_size - 1
    runs = [0] * (num_runs + 1)
    deck = list(range(deck_size))
    sample = random.sample(deck, set_size)
    last_card = sample[-1]
    for i in range(1, sample_size):
        current_sample = random.sample(deck, set_size)
        current_card = current_sample[-1]
        if current_card > last_card:
            runs[i - 1] = 1
        last_card = current_card

    run_count = sum(runs)
    expected_runs = (2 * set_size * (sample_size - set_size)) / set_size
    variance = (2 * set_size * (sample_size - set_size)) * (2 * set_size * (sample_size - set_size) - set_size) / (sample_size ** 2 * (sample_size - 1))
    z_scores = [(runs[i] - expected_runs) / variance ** 0.5 for i in range(num_runs)]
    p_value = 1 - norm.cdf(abs(max(z_scores)))

    return run_count, p_value
deck_size = 52
drawn_cards = int(input("Enter the number of cards you want to draw : "))
num_simulation = int(input("Enter the number of times you wish to simulate the game : "))
num_draws, p_value = runs_test(deck_size, drawn_cards, num_simulation)
print(f"Number of runs: {num_draws}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("The card game is statistically unfair.")
else:
    print("The card game is statistically fair.")
