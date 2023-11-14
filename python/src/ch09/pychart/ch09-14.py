import matplotlib.pyplot as plt
import numpy as np
import random

n_bins = 50

Data = np.random.randn(10000)
Data_plus = 10 + 2*np.random.randn(10000)
Data_minus = -6 + 3*np.random.randn(10000)

plt.figure(figsize=(10, 6)) # 단위는 인치로 -> 10인치, 6인치

plt.hist(Data, n_bins,  alpha=0.4)
plt.hist(Data_plus, n_bins,  alpha=0.4)
plt.hist(Data_minus, n_bins,  alpha=0.4)
plt.show()
