import random
import numpy as np
import matplotlib.pyplot as plt
# a = [[2, 1], [1, 3]]
# b = [3, 4]
# x0 = [0.8, 0.9]

# for i in range(10):
#     x2 = (b[0] - x0[1]) / a[0][0]
#     x1 = (b[1] - x0[0]) / a[1][1]
#     x0 = [x1, x2]
#     print(x0)

def jacobi_method(a, b, x0, tolerance=1e-6, max_iterations=1000):
    history = []
    for i in range(max_iterations):
        x = [(b[i] - sum(a[i][j] * x0[j] for j in range(len(x0)) if j != i)) / a[i][i] for i in range(len(b))]
        error = np.linalg.norm(np.array(x) - np.array(x0))
        history.append(error)
        
        if error < tolerance:
            break
        
        x0 = x
    
    return x0, history

def gauss_seidel_method(a, b, x0, tolerance=1e-6, max_iterations=1000):
    history = []
    N = len(a)
    for i in range(max_iterations):
        x_new = x0.copy()
        for j in range(N):
            s = sum(a[j][k] * x_new[k] for k in range(N) if k != j)
            x_new[j] = (b[j] - s) / a[j][j]

        error = np.linalg.norm(np.array(x_new) - np.array(x0))
        history.append(error)

        if error < tolerance:
            break

        x0 = x_new
    
    return x0, history

def generate_linear_system(n):
    x_true = [i + 1 for i in range(n)]
    matrix = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        row_sum = sum(abs(matrix[i][j]) for j in range(n)) - abs(matrix[i][i])
        matrix[i][i] = row_sum + random.randint(1, 10)
    
    vector = [sum(matrix[i][j] * x_true[j] for j in range(n)) for i in range(n)]
    
    return matrix, vector, x_true


def test_solution(matrix, vector, x_computed):
    residual = [sum(matrix[i][j] * x_computed[j] for j in range(len(matrix))) - vector[i] for i in range(len(vector))]
    return residual


N = 3
matrix, vector, x_true = generate_linear_system(N)
x0 = [random.uniform(x - 0.5, x + 0.5) for x in x_true]

jacobi_result, jacobi_history = jacobi_method(matrix, vector, x0)
gauss_seidel_result, gauss_seidel_history = gauss_seidel_method(matrix, vector, x0)

print(f"True solution: {x_true}")
print(f"Jacobi method: {jacobi_result}")
print(f"Gauss-Seidel method: {gauss_seidel_result}")

iterations = np.arange(len(jacobi_history))
plt.plot(iterations, jacobi_history, label="Jacobi")
plt.plot(iterations, gauss_seidel_history, label="Gauss-Seidel")
plt.xlabel("Iterations")
plt.ylabel("Error")
plt.legend()
plt.show()

print("="*50)
print(f"Jacobi residual: {test_solution(matrix, vector, jacobi_result)}")
print(f"Gauss-Seidel residual: {test_solution(matrix, vector, gauss_seidel_result)}")
# Test with Hilbert matrix
def generate_hilbert_matrix(n):
    matrix = [[1/(i + j + 1) for j in range(n)] for i in range(n)]
    x_true = [1] * n  # Using [1,1,...,1] as true solution
    vector = [sum(matrix[i][j] * x_true[j] for j in range(n)) for i in range(n)]
    return matrix, vector, x_true

print("\nTesting with Hilbert matrix:")
N = 4
matrix, vector, x_true = generate_hilbert_matrix(N)
x0 = [random.uniform(x - 0.5, x + 0.5) for x in x_true]

jacobi_result, jacobi_history = jacobi_method(matrix, vector, x0)
gauss_seidel_result, gauss_seidel_history = gauss_seidel_method(matrix, vector, x0)

print(f"True solution: {x_true}")
print(f"Jacobi method: {jacobi_result}")
print(f"Gauss-Seidel method: {gauss_seidel_result}")

plt.figure()
iterations = np.arange(len(jacobi_history))
plt.semilogy(iterations, jacobi_history, label="Jacobi")
plt.semilogy(iterations, gauss_seidel_history, label="Gauss-Seidel")
plt.xlabel("Iterations")
plt.ylabel("Error (log scale)")
plt.title("Convergence for Hilbert Matrix")
plt.legend()
plt.show()

print("="*50)
print(f"Hilbert matrix Jacobi residual: {test_solution(matrix, vector, jacobi_result)}")
print(f"Hilbert matrix Gauss-Seidel residual: {test_solution(matrix, vector, gauss_seidel_result)}")