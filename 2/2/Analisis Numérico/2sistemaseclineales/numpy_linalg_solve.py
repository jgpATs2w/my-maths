# Solve the system of equations x0 + 2 * x1 = 1 and 3 * x0 + 5 * x1 = 2
import numpy as np

A = np.array([[1,2], [3,5]])
B = np.array([1,2])

X = np.linalg.solve(A, B)

print(X)

print("Is solution close to exact? ", np.allclose(np.dot(A,X), B))