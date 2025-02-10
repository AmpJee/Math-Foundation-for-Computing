import math

def g(x):
    return math.sqrt(x)

x = 2
while True:
    if x == g(x):
        break
    else:
        x = g(x)
    print(x)