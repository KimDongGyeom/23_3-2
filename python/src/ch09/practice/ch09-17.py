import matplotlib.pyplot as plt
import numpy as np

data1 = 100
data2 = 10

# 데이터를 열 단위로 처리해서, 5개가 나타남
plt.boxplot(np.random.randn(data1, data2))

plt.show()
