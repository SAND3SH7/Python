import numpy as np
import pandas as pd


print("GAUSS-SEIDEL METHOD OF SOLVING SYSTEM OF LINEAR EQUATIONS")

n = int(input("Enter the number of variables in the system: "))
A = []

print("Enter the augmented matrix row by row:")
for i in range(n):
    row = list(
        map(float, input(f"Enter row {i + 1} ({n + 1} values): ").split()))
    if len(row) != n + 1:
        raise ValueError(f"Row {i + 1} must contain exactly {n + 1} values")
    A.append(row)

A = np.array(A, dtype=float)
print("The augmented matrix is:")
print(A)

history = []

for i in range(n):
    diagonal = abs(A[i][i])
    non_diagonal = np.sum(np.abs(A[i][:n])) - diagonal
    if diagonal < non_diagonal:
        print("The system is not diagonally dominant, may not converge!")

N = int(input("Enter the maximum number of iterations: "))
epsilon = float(input("Enter the tolerable error threshold: "))
x = np.array(list(map(float, input(
    f"Enter the initial guess vector with {n} values: ").split())), dtype=float)

if len(x) != n:
    raise ValueError(f"Initial guess vector must contain exactly {n} values")

itr = 0
while itr <= N:
    xold = x.copy()

    for i in range(n):
        s = 0.0
        for j in range(n):
            if j != i:
                s += A[i][j] * x[j]

        if A[i][i] == 0:
            raise ZeroDivisionError(
                f"Zero diagonal element found at row {i + 1}")

        x[i] = (A[i][-1] - s) / A[i][i]

    error = np.abs(x - xold)
    history.append([itr, *x.tolist(), *error.tolist()])

    if np.all(error < epsilon):
        break

    itr += 1

if itr > N:
    print(f"Solution does not reached in {N} iterations!")
else:
    columns = ["Itr"] + \
        [f"x{i}" for i in range(n)] + [f"error{i}" for i in range(n)]
    table = pd.DataFrame(history, columns=columns)
    print("Iteration Table:")
    print(table.to_string(index=False))
    print(f"Approximate solution in {itr} iterations is:")
    for i in range(n):
        print(f"x{i}: {x[i]}")