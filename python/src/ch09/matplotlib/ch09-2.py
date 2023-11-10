import matplotlib.pyplot as plt
import numpy as np
import random

x = np.arange(1000)
y = np.random.randn(1000)

plt.plot(x, y, color='red', marker='o', linestyle='solid')

plt.title('rnadom num')
plt.show()
