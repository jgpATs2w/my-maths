import numpy as np
import sympy as sy

x,y = sy.symbols('x,y')
p = x**2+y**2

print(p.subs([(x,1), (y,1)]))