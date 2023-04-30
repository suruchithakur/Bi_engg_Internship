
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Set the parameters for the simulation
Name = 'Andar Bahar'
Number_of_cards_drawn = 21
draws_per_day = 960  # less draws
category_count = 52
game_with_replacement = False
Number_of_simulations = 1000
Number_of_games = 20000
game_step = 2000

# Set the significance level and effect size
alpha = 0.05
effect_size = 0.5


# Create a function to calculate the power for a given sample size
def calculate_power(sample_size):
    # Generate two sets of data with the specified effect size
    group1 = np.random.normal(loc=0, scale=1, size=sample_size)
    group2 = np.random.normal(loc=effect_size, scale=1, size=sample_size)

    # Perform a two-sample t-test
    t_stat, p_value = stats.ttest_ind(group1, group2)

    # Calculate the power of the test
    power = 1 - stats.norm.cdf(
        stats.norm.ppf(1 - alpha / 2) - np.sqrt(sample_size) * effect_size / 2 - t_stat / np.sqrt(
            2 * (sample_size - 1)))

    return power


# Create a range of sample sizes to test
sample_sizes = range(10, 500, 10)

# Calculate the power for each sample size
powers = [calculate_power(sample_size) for sample_size in sample_sizes]

# Plot the results
plt.plot(sample_sizes, powers)
plt.axhline(y=0.8, color='r', linestyle='--')
plt.xlabel('Sample size')
plt.ylabel('Power')
plt.title('Power Analysis')
plt.show()

# Find the minimum sample size required to achieve 80% power
min_sample_size = next((i for i, power in enumerate(powers) if power >= 0.8), None)
if min_sample_size is not None:
    print("The minimum sample size required to achieve 80% power is:", sample_sizes[min_sample_size])
else:
    print("A sample size of at least 300 is required to achieve 80% power.")

# Generate two sets of data with the specified effect size
group1 = np.random.normal(loc=0, scale=1, size=sample_sizes[min_sample_size])
group2 = np.random.normal(loc=effect_size, scale=1, size=sample_sizes[min_sample_size])

# Perform a two-sample t-test
t_stat, p_value = stats.ttest_ind(group1, group2)

# Print the results
print("T statistic:", t_stat)
print("P value:", p_value)

# Check if the result is statistically significant
if p_value < alpha:
    print("The difference between the means of the two samples is statistically significant.")
else:
    print("The difference between the means of the two samples is not statistically significant.")
