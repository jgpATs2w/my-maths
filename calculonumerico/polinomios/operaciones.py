import sympy as sy

x,y = sy.symbols('x,y')
P = 3 * x**3 + 2 * x**2 - 1
Q = -4 * x**3 - x + 2
R = x - 2

print("a: ", sy.poly((P-Q)*R))

print("q factors: ", sy.gcd_terms(Q))

print("b", sy.poly(Q / R))

print("P(-2): ", P.subs(x, -2))
print("Q(2): ", Q.subs(x, 2))
