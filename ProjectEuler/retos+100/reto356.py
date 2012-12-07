'''
Created on 03/12/2012

@author: Carlitos
'''
from time import time

def cbrt(x):
    from math import pow
    if x >= 0: 
        return pow(x, 1.0/3.0)
    else:
        return -pow(abs(x), 1.0/3.0)

def polar(x, y, deg=0):        # radian if deg=0; degree if deg=1
    from math import hypot, atan2, pi
    if deg:
        return hypot(x, y), 180.0 * atan2(y, x) / pi
    else:
        return hypot(x, y), atan2(y, x)

def quadratic(a, b, c=None):
    import math, cmath
    if c:        # (ax^2 + bx + c = 0)
        a, b = b / float(a), c / float(a)
    t = a / 2.0
    r = t**2 - b
    if r >= 0:        # real roots
        y1 = math.sqrt(r)
    else:        # complex roots
        y1 = cmath.sqrt(r)
    y2 = -y1
    return y1 - t, y2 - t

def cubic(a, b, c, d=None):
    from math import cos
    if d:            # (ax^3 + bx^2 + cx + d = 0)
        a, b, c = b / float(a), c / float(a), d / float(a)
    t = a / 3.0
    p, q = b - 3 * t**2, c - b * t + 2 * t**3
    u, v = quadratic(q, -(p/3.0)**3)
    if type(u) == type(0j):    # complex cubic root
        r, w = polar(u.real, u.imag)
        y1 = 2 * cbrt(r) * cos(w / 3.0)
    else:            # real root
        y1 = cbrt(u) + cbrt(v)
    y2, y3 = quadratic(y1, p + y1**2)
    return y1 - t, y2 - t, y3 - t

def reto356():
    from math import floor
    print floor(max(cubic(1,-2**2,0,2)))**987654321%(10**8)

if __name__ == '__main__':
    ini = time()
    reto356()
    print "Tiempo =",time()-ini,"sg"