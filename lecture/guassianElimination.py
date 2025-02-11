import random

def print_system(matrix, vector, step=None):
    if step is not None:
        print(f"Step {step}:")
    for i in range(len(matrix)):
        row = " ".join(f"{x:8.4f}" for x in matrix[i])
        print(f"{row} | {vector[i]:8.4f}")
    print()

def generate_linear_system(n):
    x_true = [i + 1 for i in range(n)]
    
    matrix = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
    
    vector = [sum(matrix[i][j] * x_true[j] for j in range(n)) for i in range(n)]
    
    return matrix, vector, x_true

def gaussian_elimination(matrix, vector):
    N = len(matrix)

    for i in range(N):
        if matrix[i][i] == 0:
            for j in range(i+1, N):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    vector[i], vector[j] = vector[j], vector[i]
                    break
        
        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("Singular matrix detected.")

        for k in range(i, N):
            matrix[i][k] /= pivot
        vector[i] /= pivot
        print_system(matrix, vector, step=f"Normalization of row {i}")

        for j in range(i + 1, N):
            factor = matrix[j][i]
            for k in range(i, N):
                matrix[j][k] -= factor * matrix[i][k]
            vector[j] -= factor * vector[i]
        print_system(matrix, vector, step=f"Eliminated column {i}")

    x = [0] * N
    for i in range(N - 1, -1, -1):
        x[i] = vector[i] - sum(matrix[i][j] * x[j] for j in range(i + 1, N))

    return x

def test_solution(matrix, vector, x_computed):
    residual = [sum(matrix[i][j] * x_computed[j] for j in range(len(matrix))) - vector[i] for i in range(len(vector))]
    return residual

def generate_hilbert_matrix(n):
    matrix = [[1 / (i + j + 1) for j in range(n)] for i in range(n)]
    
    x_true = [i + 1 for i in range(n)]
    
    vector = [sum(matrix[i][j] * x_true[j] for j in range(n)) for i in range(n)]
    
    return matrix, vector, x_true

def main():
    N = 3

    matrix, vector, x_true = generate_linear_system(N)
    print("Generated Normal System:")
    print_system(matrix, vector)

    solution = gaussian_elimination(matrix, vector)
    print("Computed Solution:", solution)
    error = test_solution(matrix, vector, solution)
    print("Residual Error:", error)


    matrix_hilbert, vector_hilbert, x_true_hilbert = generate_hilbert_matrix(N)
    print("\nGenerated Hilbert System:")
    print_system(matrix_hilbert, vector_hilbert)

    solution_hilbert = gaussian_elimination(matrix_hilbert, vector_hilbert)
    print("Computed Hilbert Solution:", solution_hilbert)
    error_hilbert = test_solution(matrix_hilbert, vector_hilbert, solution_hilbert)
    print("Hilbert Residual Error:", error_hilbert)

if __name__ == "__main__":
    main()