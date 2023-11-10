import numpy as np
import random

a = np.random.randn(5)
print(a)
print('----')

b = np.random.randn(5, 4)
print(b)
print('----')

mu = 10 # 평균
sigma = 2
randoms = mu + sigma * np.random.randn(5, 4)
print(randoms)
print('----')
