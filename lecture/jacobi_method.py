import random
import matplotlib.pyplot as plt
# a = [[2, 1], [1, 3]]
# b = [3, 4]
# x0 = [0.8, 0.9]

# for i in range(10):
#     x2 = (b[0] - x0[1]) / a[0][0]
#     x1 = (b[1] - x0[0]) / a[1][1]
#     x0 = [x1, x2]
#     print(x0)

def jacobi_method(a, b, x0, tolerence=1e-6, max_iterations=1000):
    history = []
    for i in range(max_iterations):
        x = [(b[i] - sum(a[i][j] * x0[j] for j in range(len(x0)) if j != i)) / a[i][i] for i in range(len(b))]
        error = np.linalg.norm(np.array(x_new) - np.array(x0))
        history.append(error)

        if error < tolerance:
            break

        x0 = x
        print(x0)
    return x0, history

def gauss_seidel_method(a, b, x0):
    tolerance = 1e-6
    max_iterations = 1000
    history = []
    N = len(a)
    x_new = [0 for _ in range(N)]
    for i in range(N):
        x_new[i] = b[i]
        for j in range(N):
            if i != j:
                x_new[i] -= a[i][j] * x0[j]
        x_new[i] /= a[i][i]
        
        error = np.linalg.norm(np.array(x_new) - np.array(x0))
        history.append(error)

        if error < tolerance:
            break

        x0 = x_new
    return x_new, history

def generate_linear_system(n):
    x_true = [i + 1 for i in range(n)]
    
    matrix = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
    
    vector = [sum(matrix[i][j] * x_true[j] for j in range(n)) for i in range(n)]
    
    return matrix, vector, x_true

def generate_x0(x_true):
    return [random.uniform(x - 0.5, x + 0.5) for x in x_true]

for i in range(10):
    x0 = new_jacobi_method(matrix, vector, generate_x0(x_true)) 
    print(x0)
    

    
print(f"Jacobi method for matrix {matrix} and vector {vector}")
print(f"True solution: {x_true}")
# x0 = jacobi_method(matrix, vector, generate_x0(x_true))

def test_solution(matrix, vector, x_computed):
    residual = [sum(matrix[i][j] * x_computed[j] for j in range(len(matrix))) - vector[i] for i in range(len(vector))]
    return residual

print("="*50)
print(test_solution(matrix, vector, x0))

N = 3
matrix, vector, x_true = generate_linear_system(N)
x0 = generate_x0(x_true)

jacobi_result, jacobi_history = jacobi_method(matrix, vector, x0)
se

# print("="*50)
# jacobi_method(a, b, x0)