import matplotlib.pyplot as plt
import numpy as np

n_bins = 50

random_data = np.random.randn(100)

plt.boxplot(random_data)
plt.show()
