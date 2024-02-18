import numpy as np
import matplotlib.pyplot as plt

def subplot(ax, i, j, x, y, title):
    ax[i,j].plot(x, y)
    ax[i,j].set_title(title)
    ax[i,j].set_ylim(-10, 10)

x = np.linspace(-10, 10, 1000)

fig, ax = plt.subplots(2, 6, sharex=True, sharey=True)

subplot(ax, 0, 0, x, np.sin(x), "sin")
subplot(ax, 0, 1, x, np.cos(x), "cos")
subplot(ax, 0, 2, x, np.tan(x), "tan")
subplot(ax, 0, 3, x, np.arctan(x), "arctan")
subplot(ax, 0, 4, x, np.sqrt(x), "sqrt")
subplot(ax, 0, 5, x, np.sqrt(-x), "sqrt(-x)")
subplot(ax, 1, 0, x, np.abs(x), "abs")
subplot(ax, 1, 1, x, x, "x")
subplot(ax, 1, 2, x, x**2, "x^2")
subplot(ax, 1, 3, x, np.emath.sqrt(-x**2), "x^2+y^2")
subplot(ax, 1, 4, x, 1/x, "1/x")
subplot(ax, 1, 5, x, np.exp(x), "exp")

plt.show()