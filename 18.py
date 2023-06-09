import math

# define the data
data = {'Class': ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80'],
        'Frequency': [5, 10, 20, 40, 30, 20, 10, 5]}

# calculate the mean
sum_freq = sum(data['Frequency'])
sum_cf = 0
for i in range(len(data['Frequency'])):
    sum_cf += (i+0.5)*data['Frequency'][i]
mean = sum_cf/sum_freq

# calculate the variance
sum_sq_cf_diff = 0
for i in range(len(data['Frequency'])):
    sum_sq_cf_diff += ((i+0.5)-mean)**2 * data['Frequency'][i]
variance = sum_sq_cf_diff/sum_freq

# calculate the standard deviation
sd = math.sqrt(variance)

# calculate the coefficient of variation
cv = (sd/mean)*100

# print the results
print('Mean:', mean)
print('Variance:', variance)
print('Standard deviation:', sd)
print('Coefficient of variation:', cv)
