import matplotlib.pyplot as plt
import numpy as np

n_bins = 50

data1 = [1, 2, 3, 4, 5]
data2 = [2, 3, 4, 5, 6]

# 데이터를 행단위로 처리해, 2개가 나타남
# plt.boxplot([data1, data2]) # 행 위주로

# 데이터를 열 단위로 처리해서, 5개가 나타남
plt.boxplot(np.array([data1, data2]))

plt.show()
