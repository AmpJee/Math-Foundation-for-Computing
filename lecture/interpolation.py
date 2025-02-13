import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return np.sin(x)

def f2(x):
    return np.sin(3*x)

def f3(x):
    return np.sin(5*x)


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

def polynomial_interpolation(x, y, x_values):
    V = np.vander(x, len(x))
    coeffs = np.linalg.solve(V, y)
    return np.polyval(coeffs, x_values)

a, b = 0, 4
m = 20

x_points = np.linspace(a, b, m)
y1_points = f1(x_points)
y2_points = f2(x_points)
y3_points = f3(x_points)

x_fine = np.linspace(a, b, 200)
f1_values = f1(x_fine)
f2_values = f2(x_fine)
f3_values = f3(x_fine)

y1_values = lagrange_interpolation(x_points, y1_points, x_fine)
y2_values = lagrange_interpolation(x_points, y2_points, x_fine)
y3_values = lagrange_interpolation(x_points, y3_points, x_fine)

y1_poly = polynomial_interpolation(x_points, y1_points, x_fine)
y2_poly = polynomial_interpolation(x_points, y2_points, x_fine)
y3_poly = polynomial_interpolation(x_points, y3_points, x_fine)

# plt.plot(x_fine, f1_values, 'black', label="F1(x)")
# plt.plot(x_fine, y1_values, 'r-', label="Lagrange F1(x)")
# plt.plot(x_fine, y1_poly, 'b--', label="Polynomial F1(x)")
# plt.scatter(x_points, y1_points, color='black', label="Interpolation points")
# plt.legend()
# plt.title("Polynomial Interpolation Example")
# plt.show()

# plt.plot(x_fine, f2_values, 'black', label="F2(x)")
# plt.plot(x_fine, y2_values, 'r-', label="Lagrange F2(x)")
# plt.plot(x_fine, y2_poly, 'b--', label="Polynomial F2(x)")
# plt.scatter(x_points, y2_points, color='black', label="Interpolation points")
# plt.legend()
# plt.title("Polynomial Interpolation Example")
# plt.show()

plt.plot(x_fine, f3_values, 'black', label="F3(x)")
plt.plot(x_fine, y3_values, 'r-', label="Lagrange F3(x)")
plt.plot(x_fine, y3_poly, 'b--', label="Polynomial F3(x)")
plt.scatter(x_points, y3_points, color='black', label="Interpolation points")
plt.legend()
plt.title("Polynomial Interpolation Example")
plt.show()