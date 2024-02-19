from scipy.interpolate import BPoly

x = [0,1]
c = [[1], [2], [3]]
bp = BPoly(c,x)

print(str(bp))