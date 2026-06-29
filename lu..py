import numpy as np

print("LU Decomposition using Doolittle Method")

# Input number of variables
n = int(input("Enter the number of variables: "))

# Input coefficient matrix
A = np.zeros((n, n))
print("Enter the coefficient matrix:")
for i in range(n):
    A[i] = list(map(float, input(f"Row {i+1}: ").split()))

# Input constant vector
B = np.zeros(n)
print("Enter the constant terms:")
for i in range(n):
    B[i] = float(input(f"B[{i+1}] = "))

# Initialize L and U
L = np.zeros((n, n))
U = np.zeros((n, n))

# Doolittle LU Decomposition
for i in range(n):

    # Upper triangular matrix
    for k in range(i, n):
        sum1 = 0
        for j in range(i):
            sum1 += L[i][j] * U[j][k]
        U[i][k] = A[i][k] - sum1

    # Lower triangular matrix
    L[i][i] = 1

    for k in range(i + 1, n):
        sum2 = 0
        for j in range(i):
            sum2 += L[k][j] * U[j][i]
        L[k][i] = (A[k][i] - sum2) / U[i][i]

# Forward Substitution (Ly = B)
Y = np.zeros(n)
for i in range(n):
    sum3 = 0
    for j in range(i):
        sum3 += L[i][j] * Y[j]
    Y[i] = B[i] - sum3

# Backward Substitution (Ux = Y)
X = np.zeros(n)
for i in range(n - 1, -1, -1):
    sum4 = 0
    for j in range(i + 1, n):
        sum4 += U[i][j] * X[j]
    X[i] = (Y[i] - sum4) / U[i][i]

print("\nLower Triangular Matrix (L):")
print(L)

print("\nUpper Triangular Matrix (U):")
print(U)

print("\nRequired Solution:")
for i in range(n):
    print(f"x{i+1} = {X[i]:.4f}")