import numpy as np
import scipy
import matplotlib.pyplot as plt

x = np.array([0,1,2])
y = x ** 3
poly = scipy.interpolate.lagrange(x, y)
x_new = np.arange(0, 2.1, 0.1)

plt.plot(x_new, np.polynomial.polynomial.Polynomial(poly.coef[::-1])(x_new), label='Polynomial')
plt.plot(x_new, 3*x_new**2 - 2*x_new + 0 * x_new, label = r"$3 x^2 - 2x$", linestyle='-.')
plt.scatter(x,y,label='data')
plt.legend()
plt.show()