import numpy as np
import matplotlib.pyplot as plt
import sympy
import sympy as sy

x,y,z = sy.symbols('x,y,z')

a = 60
aradians = np.deg2rad(a)
fx = 3 * sy.sin(2*x)
fa = fx.subs(x, aradians).evalf(6)

derivative = [0,0,0,0,0]
p = np.zeros(5)
derivative[0] = fx
p[0] = "%6.2f" % a
strp = p[0]
for d in range(1,5):
    derivative[d] = sy.diff(fx, x, d)
    p[d] = str(derivative[d].subs(x,aradians).evalf(2))
    strp = strp + ' + (' + p[d] + '/' + str(sy.factorial(d)) + ')(x-a)^'+str(d)
