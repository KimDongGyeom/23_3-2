import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100) # 2행 100열

fig, axs = plt.subplots(2, 2, figsize=(5, 5))

# data[0]의미:
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1]) # hist2d는 hist를 2차원으로 그림을 의미

plt.show()
