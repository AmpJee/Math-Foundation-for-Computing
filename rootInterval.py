import math
a = 1
b = 4
m = (a + b) / 2
eps = 1e-30
itr = 0
max_itr = 10000000000
estimate_iter = math.ceil(math.log2((b - a) / eps))
def f(x):
    return x**2 - 4

print("Number of iterations:", estimate_iter)

while b - a > eps and 0 < estimate_iter:
    if f(a) * f(m) < 0:
        b = m
    else:
        a = m
    m = (a + b) / 2
    estimate_iter -= 1
print(f"Root: {m}")

a = 1
b = 4
m = (a + b) / 2
while b - a > eps and itr < max_itr:
    if f(m) == 0:
        break
    elif f(a) * f(m) < 0:
        b = m
    else:
        a = m
    m = (a + b) / 2
    itr += 1
print(f"Real number of iterations: {itr}\nRoot: {m}")

