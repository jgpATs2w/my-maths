# https://acme.byu.edu/00000181-49cc-d0f9-a7bd-ffee67060000/intro-to-sympy
import sympy as sy

x0 = sy.symbols('x0')
# Define multiple symbolic variables simultaneously.
x2, x3 = sy.symbols('x2, x3') # Separate symbols by commas,
m, a = sy.symbols('mass acceleration') # by spaces,
x, y, z = sy.symbols('x:z') # or by colons.
x4, x5, x6 = sy.symbols('x4:7')
# Combine symbolic variables to form expressions.
expr = x**2 + x*y + 3*x*y + 4*y**3
force = m * a
print(expr, force, sep='\n')