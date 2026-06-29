import numpy as np

print("Gauss-Seidel Method")


n = int(input("Enter the number of variables: "))


A = np.zeros((n, n))
print("Enter the coefficient matrix:")
for i in range(n):
    A[i] = list(map(float, input(f"Row {i+1}: ").split()))


B = np.zeros(n)
print("Enter the constant terms:")
for i in range(n):
    B[i] = float(input(f"B[{i+1}] = "))


x = np.zeros(n)


tol = float(input("Enter tolerance (e.g., 0.0001): "))
max_iter = int(input("Enter maximum iterations: "))

print("\nIterations:")

for k in range(max_iter):
    x_old = x.copy()

    for i in range(n):
        s1 = np.dot(A[i, :i], x[:i])
        s2 = np.dot(A[i, i+1:], x_old[i+1:])
        x[i] = (B[i] - s1 - s2) / A[i][i]

    print(f"Iteration {k+1}: {x}")


    error=abs(x-tol)
    T.append([itr]+ [x[i] for i in range(n)]+[error[i] for i in range(n)])
    if np.all(error<E):
        break
    itr+=1
if itr>N:
    print(f'solution is converged')
else:
    table=pd.dataFrame(T,columns=['iteration']+[f'x{i}' for  ])


    # Check convergence
    if np.linalg.norm(x - x_old, ord=np.inf) < tol:
        print("\nSolution Converged.")
        break

print("\nRequired Solution:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")

