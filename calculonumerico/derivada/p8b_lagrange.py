import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

pointsnum = 300

def datasample(poli, a, b, A, B):
    print("f(x)")
    print(poli)
    print("a = {}, b = {}".format(a,b))
    print("A = {}, B = {}".format(A,B))

fpoli = np.poly1d([6,1,0,5])
a = -1.1
b = 0.2
A = np.polyval(fpoli, a)
B = np.polyval(fpoli, b)

datasample(fpoli, a, b, A, B)
charasteristicx = [0]
charasteristicy = [0]
charasteristicx.append(a)
charasteristicx.append(b)

def writex(m, texto):
    plt.text(m, -0.5, texto, horizontalalignment='center', verticalalignment='top',
             fontsize=13, color='blue', weight='bold')

def writefx(m, M, texto):
    if(M>=0):
        posicion = 0.4 + M
        vertical = 'bottom'
    else:
        posicion = M - 0.4
        vertical = 'top'
    plt.text(m, posicion, texto, horizontalalignment='center', verticalalignment=vertical,
             fontsize=13, color='blue', weight='bold')
writefx(a, A, 'A')
writefx(b, B, 'B')
plt.plot(a, 0, 'yo')
plt.plot(b, 0, 'yo')
writex(a, 'a')
writex(b, 'b')
plt.plot(a, A, 'yo')
plt.plot(b, B, 'yo')
plt.plot([a, b], [A,B], 'k--', lw=1)
slope = (B-A)/(a-b)

d1 = np.polyder(fpoli)
d1[0] = d1[0] - slope
print(d1)

raices1 = np.roots(d1)
for i in range(0, len(raices1)):
    if np.iscomplex((raices1[i])):
        np.delete(raices1, i)
    else:
        if(raices1[i] < b) and (raices1[i] > a):
            c = raices1[i]
            C = np.polyval(fpoli, c)
            plt.plot(c, C, 'ko')
            plt.plot(c, 0, 'ko')
            writex(c, 'c')
            writefx(c, C, 'C')
            charasteristicx.append(c)
            i = len(raices1) + 2

xmax = 1.5 * np.max(charasteristicx)
xmin = 1.5 * np.min(charasteristicx)
if xmin == 0:
    xmin = -1
if xmax == 0:
    xmax = 1

ymax = 2 * max([0.5, A, B, C])
ymin = 2 * min([-0.5, A, B, C])
plt.plot([xmin, xmax], [C + slope * (xmin - c), C + slope * (xmax -c )], 'b--', lw=1)

x = np.linspace(xmin, xmax, pointsnum)
y = np.zeros(pointsnum, float)
for i in range(0, pointsnum):
    y[i] = np.polyval(fpoli, x[i])

plt.plot(x, y, 'r--', lw=2)
plt.axhline(color='black', lw=1)
plt.axvline(color='black', lw=1)
plt.ylim(ymin, ymax)
plt.ylabel('y')
plt.xlabel('x')
plt.show()
