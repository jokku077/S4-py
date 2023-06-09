import scipy.stats as stats
import numpy as np
pop_mean = 3.8
pop_stddev = 1.0  
sample_size = 15
sample_mean = 4.1
t_statistic, p_value = stats.ttest_1samp(np.random.normal(pop_mean, pop_stddev, size=sample_size), pop_mean)
alpha = 0.05
print("Null Hypothesis: The average productivity in the department is equal to or lower than the company's mean productivity.")
print("Alternative Hypothesis : The average productivity in the department is higher than the company's mean productivity.")
print("Sample mean:", sample_mean)
print("t-statistic:", t_statistic)
print("p-value:", p_value)
if p_value < alpha:
    print("Reject the null hypothesis.")
    print("The mean productivity rating in the Human Resource Management department is significantly higher than in the company as a whole.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is not enough evidence to conclude that the mean productivity rating in the Human Resource Management department is significantly higher than in the company as a whole.")
