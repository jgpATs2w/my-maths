import numpy as np
from numpy.polynomial import chebyshev as C
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0,1,2000)
y = x**3 - x**2 + np.random.randn(len(x))

p = np.polynomial.Chebyshev.fit(x, y, 90)

plt.plot(x, y, 'r.')
plt.plot(x, p(x), 'k--')
plt.show()