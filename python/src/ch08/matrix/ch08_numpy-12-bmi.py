import numpy as np
# bmi = weights / heights(m단위)**2

x = np.array([
  [1.83, 1.76, 1.69, 1.86, 1.77, 1.73],
  [86.0, 74.0, 59.0, 95.0, 80.0, 68.0]
])

bmi = x[1]/(x[0]**2)

y = x[0:2, 1:3]
z = x[0:2][1:3]

print('x shape', x.shape)
print('y shape', y.shape)
print('z shape', z.shape)
print('z values', z)
print('bmi data', bmi)
