import numpy as np

def lagrange_interpolation(x, y, x_values):
    m = len(x)
    y_values = np.zeros(len(x_values))
    for i in range(m):
        l = 1
        for j in range(m):
            if i != j:
                l *= (x_values - x[j]) / (x[i] - x[j])
        y_values += y[i] * l
    return y_values

x = [0, 1, 2]
y = [1, 2, 3]
x_values = np.linspace(0, 2, 100)
y_values = lagrange_interpolation(x, y, x_values)
print(y_values)

