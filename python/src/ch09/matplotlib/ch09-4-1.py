import matplotlib.pyplot as plt

x = [x / 10 for x in range(21)]
y = [i**2 for i in x]
z = [i**3 for i in x]
p = [2**i for i in x]

plt.plot(x, x, label='linear')
plt.plot(x, y, label='quadratic')
plt.plot(x, z, label='qubic')
plt.plot(x, p, label='power')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('My Plot')
plt.legend()
plt.show()
