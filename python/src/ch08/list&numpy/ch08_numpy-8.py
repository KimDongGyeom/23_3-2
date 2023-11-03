import numpy as np

ages = np.array([18, 19, 25, 30, 28])

x = ages > 20
y = ages[ages > 20]

print(x)
print(y)

