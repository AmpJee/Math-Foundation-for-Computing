import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x**4) + (3 * x**3) + (x**2) - (2*x) - 0.5

def bisection(a, b, tol=1e-6, max_itr=1000):
    if f(a) * f(b) >= 0:
        return None
    for i in range(max_itr):
        m = (a + b) / 2
        if abs(f(m)) < tol:
            return m
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

def find_all_roots(a, b, tol=1e-6, roots=[]):
    m = (a + b) / 2
    ans_roots = roots
    if f(a) * f(b) >= 0:
        find_all_roots(a, m, tol, ans_roots)
        find_all_roots(m, b, tol, ans_roots)
    else:
        mnew = bisection(a, b, tol, 1000)
        ans_roots.append(mnew)
    return ans_roots

print(f"Roots: {find_all_roots(-3, 1, 1e-6, [])}")
