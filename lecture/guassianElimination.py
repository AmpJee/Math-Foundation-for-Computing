def print_system(matrix, vector):
    for i in range(len(matrix)):
        row = " ".join(f"{x:6.2f}" for x in matrix[i])
        print(f"{row} | {vector[i]:6.2f}")
    print()

def gaussian_elimination(matrix, vector):
    N = len(matrix)

    # Forward elimination
    for i in range(N):
        # Make diagonal 1
        pivot = matrix[i][i]
        for k in range(N):
            matrix[i][k] /= pivot
        vector[i] /= pivot
        print_system(matrix, vector)

        # Eliminate column entries
        for j in range(N):
            if i != j:
                factor = matrix[j][i]
                for k in range(N):
                    matrix[j][k] -= factor * matrix[i][k]
                vector[j] -= factor * vector[i]
                print(f"k = {factor}")
                print_system(matrix, vector)

    # Result is now in vector since matrix is identity
    return vector

# Test with your original matrix
matrix = [[1, 1, 1],
         [3, 2, 1],
         [2, -1, 4]]

vector = [6, 10, 12]

print("Solution:", gaussian_elimination(matrix, vector))