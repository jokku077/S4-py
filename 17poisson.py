import math

def poisson_probability(mean, k):
    # Calculate the probability
    probability = (math.exp(-mean) * mean**k) / math.factorial(k)
    
    return probability

# Calculate the probability of x = 6
mean = 3.4
k = 6
prob_x_6 = poisson_probability(mean, k)
print(f"The probability of x = 6 is: {prob_x_6}")
