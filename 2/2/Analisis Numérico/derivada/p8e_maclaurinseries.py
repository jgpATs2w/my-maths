import sympy as sy

x, y, z = sy.symbols('x,y,z')
sy.init_printing(use_unicode=True)
j = complex(0, 1)

fx = sy.atan(x)
f0 = fx.subs(x, 0).evalf(3)
maclaurin = str(f0) + '+'
print("f(x) = ", str(fx))
for d in range(1, 11):
    derivative = sy.diff(fx, x, d)
    derivative0 = derivative.subs(x, 0).evalf(3)
    sd = str(derivative0)
    print('D', str(d), f"= {sd}; D{str(d)}(0= {sd}")
    if(sd != '0'):
        maclaurin += '[' + sd + ' * (x**' + str(d) + ') / '+str(d) + '!] + '

print(maclaurin + '...')
serie = fx.series(x, 0, 11)
print(serie)