import scipy.stats as stats
import numpy as np
observed = np.array([[60, 54, 46, 41],
                     [40, 44, 53, 57]])

chi2, p_value, _, _ = stats.chi2_contingency(observed)
alpha = 0.05
print("chi2 test")
print("alpha = 0.05")
print("p_value = ",p_value)
if p_value < alpha:
    print("Gender and education level are dependent.")
else:
    print("Gender and education level are independent.")
