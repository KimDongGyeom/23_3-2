import math
import matplotlib.pyplot as plt

# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
years = [i for i in range(1950, 2011, 10)]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505.0, 11865.3, 22105.3]

# plt.bar(index, 눈금을 그릴 데이터)
plt.bar(range(len(years)), gdp)

plt.title('GDP per capita')
plt.ylabel('dollars')

# x축에 틱을 붙인다
plt.xticks(range(len(years)), years)

plt.show()
