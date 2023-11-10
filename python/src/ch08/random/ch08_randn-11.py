import numpy as np
import random

m = 175 # 평균
sigma = 10
heights = m + sigma * np.random.randn(10000)
print(heights)

print('평균: ', np.mean(heights))
print('중앙 값: ', np.median(heights))
