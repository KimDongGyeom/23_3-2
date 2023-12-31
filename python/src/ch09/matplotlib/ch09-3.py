import matplotlib.pyplot as plt

x = [x for x in range(-20, 20)]
# y = 2x
y1 = [2*t for t in x]
# y = 2x +5
y2 = [t**2 + 5 for t in x]
# y = -2x -5
y3 = [-t**2 - 5 for t in x]

plt.plot(x, y1, 'r--', x, y2, 'g^-', x, y3, 'b*:')
plt.axis([-30, 30, -30, 30])
plt.show()
