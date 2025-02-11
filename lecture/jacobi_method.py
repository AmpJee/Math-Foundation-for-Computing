import random
a = [[2, 1], [1, 3]]
b = [3, 4]
x0 = [0.8, 0.9]

# for i in range(10):
#     x2 = (b[0] - x0[1]) / a[0][0]
#     x1 = (b[1] - x0[0]) / a[1][1]
#     x0 = [x1, x2]
#     print(x0)

def jacobi_method(a, b, x0, max_iterations=10):
    for i in range(max_iterations):
        x = [(b[i] - sum(a[i][j] * x0[j] for j in range(len(x0)) if j != i)) / a[i][i] for i in range(len(b))]
        x0 = x
        print(x0)

def new_jacobi_method(a, b, x0):
    N = len(a)
    x_new = [0 for _ in range(N)]
    for i in range(N):
        x_new[i] = b[i]
        for j in range(N):
            if i != j:
                x_new[i] -= a[i][j] * x0[j]
        x_new[i] /= a[i][i]
    return x_new

for i in range(10):
    x0 = new_jacobi_method(a, b, x0)
    print(x0)
print("="*50)
# jacobi_method(a, b, x0)