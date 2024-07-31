def matrix_chain_multiplication(dimensions):
    n = len(dimensions)
    dp = [[0] * n for _ in range(n)]
    
    for length in range(2, n):
        for i in range(1, n - length + 1):
            j = i + length - 1
            dp[i][j] = min(dp[i][k] + dp[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j] for k in range(i, j))
    
    return dp[1][n - 1]

# Get user input for matrix dimensions
matrix_dimensions = [int(input(f"Enter the dimension of matrix {i + 1}: ")) for i in range(int(input("Enter the number of matrices: ")))]

# Calculate the minimum number of scalar multiplications
result = matrix_chain_multiplication(matrix_dimensions)
print("Minimum number of scalar multiplications:", result)
