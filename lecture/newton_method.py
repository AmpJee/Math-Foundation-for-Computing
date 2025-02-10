import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*x - 5*x + 4

def df(x):
    return 2*x - 5

x = 5
xnew = 0
errors = []
x_vals = []
for i in range(10):
    xnew = x - (f(x) / df(x))
    if f(x) == 0:
        break
    error = abs(x - xnew)
    errors.append(error)
    x = xnew
    x_vals.append(x)
    print(f"Iteration {i +1}: {x}\nError={error}")


plt.plot(errors)
plt.show()