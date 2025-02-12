import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# function_input = input("Enter the function: ")
# function = sp.sympify(function_input)
# x = sp.symbols('x')

# a = float(input("Enter the lower bound: "))
# b = float(input("Enter the upper bound: "))
# m = int(input("Enter the number of interpolation points: "))

a, b = 0, 2 * np.pi
m = 20  

def F(x):
    return np.sin(3*x)  # Example function; you can change it to whatever you like

x_points = np.linspace(a, b, m)
y_points = F(x_points)

# 3) Construct the Vandermonde matrix and solve for the polynomial coefficients
V = np.vander(x_points, m)

# Solve the linear system V * coeffs = y_points
coeffs = np.linalg.solve(V, y_points)

# 4) Define a helper function to evaluate our interpolating polynomial
def P(x):
    return np.polyval(coeffs, x)  # np.polyval expects highest power first

# Create a fine grid for plotting
x_fine = np.linspace(a, b, 200)
f_values = F(x_fine)
p_values = P(x_fine)

# Plot the results
plt.plot(x_fine, f_values, 'b-', label="F(x)")
plt.plot(x_fine, p_values, 'r--', label="P_m(x)") 
plt.scatter(x_points, y_points, color='black', label="Interpolation points")
plt.legend()
plt.title("Polynomial Interpolation Example")
plt.show()
