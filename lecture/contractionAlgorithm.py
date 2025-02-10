import math
def g(x):
    return x*x - 2*x

x = 1
xnew = 1
alpha = -1/4
for i in range(1000):
    xnew = alpha * g(x) + x
    if abs(xnew - x) < 0.05:
        break
    x = xnew
    print(f"Iterations: {i + 1}\t\tValue = {x}")