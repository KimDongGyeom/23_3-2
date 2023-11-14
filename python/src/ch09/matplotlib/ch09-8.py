import matplotlib.pyplot as plt
import numpy as np

xData = np.arange(20, 50)
# 표준 정규 분포를 따르는 데이터를 만듬
# randn() -> 표준 정규 분포를 따름
# 원래 표준 편차는 0이나, 2를 곱해서, 2가 되고, 이 값에, xData
# ex) 대략적 [20 +-2, 21 +-2, 22 +-2, ...] // 랜덤이기 때문에, 무조건 +-2 는 아니나, 크게 벗어나지는 않음
yData = xData + 2*np.random.randn(30)

plt.scatter(xData, yData)
plt.title('Real Age vs Physical Age')
plt.xlabel('Real Age')
plt.ylabel('Physical Age')

plt.show()
