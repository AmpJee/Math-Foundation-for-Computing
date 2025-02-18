import matplotlib.pyplot as plt
import numpy as np

def g(c, x):
    return c[0] + c[1] * np.sin(x) + c[2] * x**2

A = np.array([[1, np.sin(0), 0], 
            [1, np.sin(1), 1], 
            [1, np.sin(2), 4],
            [1, np.sin(3), 9]])

b = np.array([1, 2, 3, 2])

c = np.linalg.solve(A.T @ A, A.T @ b)

x = np.linspace(0, 3, 100)
y = g(c, x)

plt.plot(x, y)
plt.scatter(A[:, 1], b)
plt.show()

