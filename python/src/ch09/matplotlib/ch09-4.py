import matplotlib.pyplot as plt

x = [x for x in range(20)]
y = [i**2 for i in x]
z = [i**3 for i in x]

plt.plot(x, x, label='linear')
plt.plot(x, y, label='quadratic')
plt.plot(x, z, label='qubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('My Plot')
plt.legend()
plt.show()
