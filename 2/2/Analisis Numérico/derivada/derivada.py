import numpy as np

p = np.poly1d([1,0,1])

print(p)
print(p.deriv())
print(p(2))