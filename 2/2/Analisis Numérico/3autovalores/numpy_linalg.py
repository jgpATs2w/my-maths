import numpy as np

A = np.array([[1,0],[0,2]])

evalues, evectors = np.linalg.eig(A)

print("autovalores:")
print(evalues)
print("autovectores:")
print(evectors)