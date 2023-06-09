import numpy as np
import pandas as pd

data = {'State': ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware'],
        'Population': [4779736, 710231, 6392017, 2915918, 37253956, 5029196, 3574097, 897934],
        'Murder': [5.7, 5.6, 4.7, 5.6, 4.4, 2.8, 2.4, 5.8]}

df = pd.DataFrame(data)
def mean():
 mean_pop = np.mean(df['Population'])
 mean_murder = np.mean(df['Murder'])
 print('Mean population:', mean_pop)
 print('Mean murder rate:', mean_murder)
def median():
 median_pop = np.median(df['Population'])
 median_murder = np.median(df['Murder'])
 print('Median population:', median_pop)
 print('Median murder rate:', median_murder)
def variance():
 var_pop = np.var(df['Population'])
 var_murder = np.var(df['Murder'])
 print('Variance of population:', var_pop)
 print('Variance of murder rate:', var_murder)
mean()
median()
variance()
