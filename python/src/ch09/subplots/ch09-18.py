import matplotlib.pyplot as plt

# 갯수가 2*2개, 크기가 (5, 5) 인치
# fig, ax의 순서!!
fig, ax = plt.subplots(2, 2, figsize=(5, 5))

ax[0, 0].plot(range(10), 'r')
ax[1, 0].plot(range(10), 'b')
ax[0, 1].plot(range(10), 'g')
ax[1, 1].plot(range(10), 'k')

plt.show()
