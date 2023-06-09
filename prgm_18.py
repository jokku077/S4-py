from scipy.stats import poisson

mean = 3.4
k = 6 
prob_X_equals_6 = poisson.pmf(k, mean)
print(f"Probability of X=6: {prob_X_equals_6}")
