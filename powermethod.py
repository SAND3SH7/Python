# import numpy as np
# import pandas as pd


# print("GAUSS-SEIDEL METHOD OF SOLVING SYSTEM OF LINEAR EQUATIONS")

# n = int(input("Enter the order of matrix in the system: "))
# A = []
# T=[]
# print("Enter the augmented matrix row by row:")
# for i in range(n):
#     row = list(
#         map(float, input(f"Enter row {i + 1} ({n + 1} values): ").split()))
#     if len(row) != n + 1:
#         raise ValueError(f"Row {i + 1} must contain exactly {n + 1} values")
#     A.append(row)

# A = np.array(A, dtype=float)
# print("The square matrix is:")
# print(A)

# N = int(input("Enter the maximum number of iterations: "))
# E = float(input("Enter the tolerable error threshold: "))
# x = np.array(list(map(float, input(
#     f"Enter the initial guess vector with {n} values: ").split())), dtype=float)

# itr = 0
# old_ev=0
# while itr<=N:
#     y=np.dot(A,x)
#     max_ev=np.max(abs(y))
#     x=y/max_ev
#     error=abs(max_ev-old_ev)
#     T.append([itr,max_ev]+[x[i] for i in range(n)])
#     if error<E:
#         break
#     old_ev=max_ev
#     itr+=1

# if itr > N:
#     print(f"Solution does not reached in {N} iterations!")
# else:
#     columns = ["Itr"] + \
#         [f"x{i}" for i in range(n)] + [f"error{i}" for i in range(n)]
#     table = pd.DataFrame(T, columns=columns)
#     print("Iteration Table:")
#     print(table.to_string(index=False))
#     print(f"Approximate solution in {itr} iterations is:")
#     for i in range(n):
#         print(f"x{i}: {x[i]}")



import numpy as np
import pandas as pd

print("POWER METHOD")

n = int(input("Enter the order of matrix: "))

A = []
T = []

print("Enter the matrix row by row:")
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

A = np.array(A, dtype=float)

N = int(input("Enter the maximum number of iterations: "))
E = float(input("Enter the tolerable error: "))

x = np.array(list(map(float, input(f"Enter the initial guess ({n} values): ").split())), dtype=float)

itr = 0
old_ev = 0

while itr <= N:
    y = np.dot(A, x)

    max_ev = np.max(np.abs(y))

    x = y / max_ev

    error = abs(max_ev - old_ev)

    T.append([itr, max_ev] + list(x) + [error])

    if error < E:
        break

    old_ev = max_ev
    itr += 1

if itr > N:
    print("Solution did not converge.")
else:
    columns = ["Itr", "Eigenvalue"] + [f"x{i+1}" for i in range(n)] + ["Error"]

    table = pd.DataFrame(T, columns=columns)

    print("\nIteration Table:")
    print(table.to_string(index=False))

    print("\nDominant Eigenvalue =", max_ev)
    print("Corresponding Eigenvector:")

    for i in range(n):
        print(f"x{i+1} = {x[i]:.6f}")