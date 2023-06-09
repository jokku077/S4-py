import numpy as np
hand = np.array([17, 15, 19, 17, 21])
height = np.array([150, 154, 169, 172, 175])
correlation_coefficient = np.corrcoef(hand, height)[0, 1]
print(f"Correlation coefficient: {correlation_coefficient}")
