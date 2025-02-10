import random

N = 2
A = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randint(1, 5))
    A.append(row)
print(A)

b = []
for i in range(N):
    b.append(random.randint(1, 5))
print(b)

real_solution = [random.randint(1, 5) for i in range(N)]

b = [0, 0]
b[0] = A[0][0] * real_solution[0] * A[0][1] * real_solution[1]
b[1] = A[1][0] * real_solution[0] * A[1][1] * real_solution[1]

print(f"Matrix is {A}\nRight hand is {b}")

solve = False
while not solve:
    x = []
    for i in range(N):
        x.append(float(input(f"Enter x[{i}]: ")))
    print(f"Your guess is {x}")

    test