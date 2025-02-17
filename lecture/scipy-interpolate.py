import numpy as np
from scipy.interpolate import CubicSpline, lagrange
import matplotlib.pyplot as plt

def F(x):
    return 1.0/(1.0 + 25 * x**2)

n = 10
x_interp = np.linspace(-1, 1, n)
y_interp = F(x_interp)

lagraage_poly = lagrange(x_interp, y_interp)
cubic_spline = CubicSpline(x_interp, y_interp)

x_fine = np.linspace(-1, 1, 500)
y_fine = F(x_fine)

x_lagrange = lagraage_poly(x_fine)
y_cubic_spline = cubic_spline(x_fine)

plt.plot(x_interp, y_interp, 'o', label="Interpolation Points")
plt.plot(x_fine, y_fine, label="True Function")
plt.plot(x_fine, x_lagrange, label="Lagrange Interpolation")
plt.plot(x_fine, y_cubic_spline, label="Cubic Spline Interpolation")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()