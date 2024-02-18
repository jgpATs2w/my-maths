import numpy as np

A = np.array([[1,2],[3,4]])
C = np.array([[5,6],[7,8]])
E = np.array([[1,0],[0,1]])

print('A='+str(A))
print('A.E=' + str(np.dot(A,E)))