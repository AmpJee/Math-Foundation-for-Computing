import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def f(x):
    return x**2 - 4

def bisection(a, b, tol=1e-6, max_itr=1000):
    x_vals = []
    for i in range(max_itr):
        m = (a + b) / 2
        x_vals.append(m)
        if abs(f(m)) < tol:
            return x_vals
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return x_vals

def plot(a, b):
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.linspace(a, b, 100)
    y = f(x)
    x_vals = bisection(a, b)

    def animate(i):
        ax.clear()
        ax.plot(x, y, label='f(x)')
        ax.plot(x_vals[:i], f(np.array(x_vals[:i])), 'ro', label='x')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.set_title(f"Iteration {i} : x = {x_vals[i]}")
        ax.legend()

        return ax

    anim = FuncAnimation(fig, animate, frames=len(x_vals), interval=500, repeat=False)
    plt.show()
    return anim

a = -5
b =5
anim = plot(a, b)
anim.save('bisection_animation.gif', writer='pillow')


