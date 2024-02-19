

def gcd(a,b):
    r = a % b
    if r == 0:
        return b
    if r < b:
        return a
    return gcd(b,r)

_
