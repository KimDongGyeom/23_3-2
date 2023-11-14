# 데이터 1,000개 Or 10,000개
# 투명도는 0.3
import matplotlib.pyplot as plt
import numpy as np
xData = np.random.randn(10000)
yData = np.random.randn(10000)

plt.title('Random Position')
plt.scatter(xData, yData, alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')

plt.show()
