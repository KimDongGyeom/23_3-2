# 데이터 1,000개 Or 10,000개
# 투명도는 0.3
import matplotlib.pyplot as plt

n_bins = 3
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.hist(x, n_bins)
plt.show()
