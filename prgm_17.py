from scipy.stats import binom
n = 6  
p = 0.25 
k = 4 
prob_4_successes = binom.pmf(k, n, p)
print(f"Probability of exactly 4 successes: {prob_4_successes}")

prob_at_least_one_success = 1 - binom.pmf(0, n, p)
print(f"Probability of at least one success: {prob_at_least_one_success}")
