from scipy.stats import t
sample_mean = 22
sample_std = 3
sample_size = 16
hypothesized_mean = 20
t_statistic = (sample_mean - hypothesized_mean) / (sample_std / (sample_size ** 0.5))
p_value = t.cdf(t_statistic, df=sample_size - 1)

alpha = 0.05
print("t test")
print("alpha = 0.05")
print("p_value = ",p_value)
if p_value < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")
