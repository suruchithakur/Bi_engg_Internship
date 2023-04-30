import statsmodels.stats.power as smp

#parameters
alpha = 0.05 # significance level
power = 0.80 # desired power
effect_size = 0.5 # Cohen's d effect size

#game
n_cards = int(input("Enter the number of cards you want to draw : "))# number of cards drawn
n_decks = 1

# Calculate the required sample size
power_analysis = smp.NormalIndPower()
sample_size = power_analysis.solve_power(effect_size, power=power, alpha=alpha, nobs1=None, ratio=n_cards/n_decks)

# Round up the sample size to the nearest integer
sample_size = int(sample_size) + 1

# Print the required sample size
print(f"The required sample size to detect non-randomness in the card game is {sample_size} rounds of drawing {n_cards} cards from {n_decks} deck(s) of cards.")
