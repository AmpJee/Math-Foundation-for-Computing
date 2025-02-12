x = [0, 1, 2]
y = [1, 2, 3]
x_values = np.linspace(0, 2, 100)
y_values = lagrange_interpolation(x, y, x_values)
print(y_values)