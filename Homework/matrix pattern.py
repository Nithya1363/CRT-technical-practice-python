def generate_pattern_matrix(N):
    # Initialize the matrix
    matrix = [[0] * N for _ in range(N)]
    
    # Fill the matrix with the desired pattern
    for i in range(N):
        for j in range(N):
            # Calculate the element value
            if i == 0 and j == 0:
                matrix[i][j] = 1
            elif i == 0:
                matrix[i][j] = matrix[i][j-1] + (j + 1)
            elif j == 0:
                matrix[i][j] = matrix[i-1][j] + (i + 1)
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1] + (i + j + 1)
                
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

# Input for the size of the matrix
N = 3  # You can change this to generate a larger or smaller matrix

matrix = generate_pattern_matrix(N)
print_matrix(matrix)
