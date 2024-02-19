import numpy as np

f = np.poly1d([3,-5,1])

x0 = -2.0

deltax = abs(x0/2) if abs(x0) > 0 else 0.1
print("  delta x         /      delta y / delta x")

while deltax >= 1e-6:
    deltay = np.polyval(f, (x0 + deltax)) - np.polyval(f, x0)
    c = deltay / deltax
    print("{:.6f}        {:.6f}".format(deltax, c))
    deltax = 0.1 * deltax

print("x0 =  ", x0)
print("f(x)= ")
print(f)

df = np.polyder(f,1)
print("df(x): ", df)
print(f"df({x0}) = ", np.polyval(df, x0))
