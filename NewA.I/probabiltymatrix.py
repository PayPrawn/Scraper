import matplotlib.pyplot as plt
import numpy as np

x = []
start = -100
for i in range(200):
    x.append(start)
    start = start + 1
y = []
for i in range(len(x)):
    y.append(x[i] ** 2)

print(x)
plt.plot(x, y)
plt.axis([-50, 50, -50, 50])
plt.show()