import numpy as np
# bmi = weights / heights(m단위)**2

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73, 1.77]
weights = [86, 74, 59, 95, 80, 68, 78]

np_heights = np.array(heights)
np_weights = np.array(weights)

bmi = np_weights/(np_heights**2)
print('대상자들의 키: ', np_heights)
print('대상자들의 몸무게: ', np_weights)
print('대상자들의 BMI: ')
print(bmi)
print(bmi[bmi > 25])
