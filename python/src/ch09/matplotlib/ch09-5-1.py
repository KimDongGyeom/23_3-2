import math
import matplotlib.pyplot as plt

x = []
y = []
z = []

for angle in range(360):
  x.append(angle)
  y.append(math.sin(math.radians(angle)))
  z.append(math.cos(math.radians(angle)))


plt.plot(x, y, label='sin')
plt.plot(x, z, 'r', label='cos')
plt.title('SINE COSINE WAVE')
plt.legend()
plt.show()
