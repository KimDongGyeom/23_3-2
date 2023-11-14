import math
import matplotlib.pyplot as plt
import numpy as np

# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
years = [i for i in range(1965, 2016, 10)]
ko = [130, 650, 2450, 11600, 17790, 27250]
jp = [890, 5120, 11500, 42130, 40560, 38780]
ch = [100, 200, 290, 540, 1760, 7940]

x_range = np.arange(len(years))
# plt.bar(index, 눈금을 그릴 데이터)
plt.bar(x_range + 0.0, ko, width = 0.25)
plt.bar(x_range + 0.3, jp, width = 0.25)
plt.bar(x_range + 0.6, ch, width = 0.25)

plt.title('GDP per capita')
plt.ylabel('dollars')

# x축에 틱을 붙인다
plt.xticks(range(len(years)), years)

plt.show()
