import numpy as np
import matplotlib.pyplot as plt


x_data = np.genfromtxt('data.csv', delimiter=',', usecols=0)
y_data = np.genfromtxt('data.csv', delimiter=',', usecols=1)

A = np.column_stack([
    np.ones_like(x_data),         # 1
    np.cos(x_data),               # cos(x)
    np.sin(x_data),               # sin(x)
    x_data,                       # x
    x_data**2,                    # x^2
    np.log(x_data)                # ln(x)
])

b = y_data

c = np.linalg.solve(A.T @ A, A.T @ b)

def f(c, x):
    return (c[0] + c[1]*np.cos(x) + c[2]*np.sin(x) + c[3]*x + c[4]*x**2 + c[5]*np.log(x))

x_fit = np.linspace(min(x_data), max(x_data), 200)
y_fit = f(c, x_fit)

plt.figure(figsize=(8,5))
plt.scatter(x_data, y_data, color='red', label='Data')
plt.plot(x_fit, y_fit, 'b-', label='Fitted model')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fit: c0 + c1 cos(x) + c2 sin(x) + c3 x + c4 x^2 + c5 ln(x)')
plt.legend()
plt.show()

print("Fitted coefficients [c0, c1, c2, c3, c4, c5]:")
print(c)
