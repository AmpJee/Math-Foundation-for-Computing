import matplotlib.pyplot as plt
import numpy as np

h = 1
k = 2

r = 4

def x(t):
    return h + r * np.cos(t)
    # return 16 * np.sin(t)**3

def y(t):
    return k + r * np.sin(t)
    # return 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

a, b = 0, 2 * np.pi
n = 100

t_fine = []
for i in range(n):
    t = ((b - a) * i / n )+ a
    t_fine.append(t)

# t_fine = np.linspace(0, 2*np.pi, 100)
x_fine = x(t_fine)
y_fine = y(t_fine)

plt.figure(figsize=(10, 6))
plt.plot(x_fine, y_fine)
plt.axis('equal')
plt.show()