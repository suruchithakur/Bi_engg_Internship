import random
import numpy as np
from scipy.stats import chisquare

deck = list(range(1,53))  # create a deck of 52 cards numbered 1 to 52
outcomes = np.zeros((100, 25), dtype=int)  # initialize a 2D array to store outcomes

for i in range(100):
    random.shuffle(deck)  # shuffle the deck
    outcome = deck[:25]  # draw 25 cards randomly from the deck
    outcomes[i] = outcome  # store the outcome in the array

# Calculate observed frequencies for each card
obs_freq = np.zeros(52, dtype=int)
for card in range(1, 53):
    obs_freq[card-1] = np.count_nonzero(outcomes == card)

# Calculate expected frequencies assuming randomness
exp_freq = np.full(52, 25*100/52)

# Perform chi-square test
chi2, p_value = chisquare(obs_freq, exp_freq)

print("Chi-square test results:")
print("Chi-square statistic =", chi2)
print("P-value =", p_value)

if p_value <0.05:
    print("The draws were non random! ")
else:
    print("The draws were random!")