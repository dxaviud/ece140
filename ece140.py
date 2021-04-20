from cmath import polar, rect

# returns equivalent impedance of 2 parallel impedances
def p(c1, c2):
    return ((c1 * c2) / (c1 + c2))

# returns equivalent impedance of 2 series impedances
def s(c1, c2):
    return c1 + c2

# returns equivalent impedance of many parallel impedances (at least 2 required)
def mp(c1, c2, *others):
    res = p(c1, c2)
    for c in others:
        res = p(res, c)
    return res	

# returns equivalent impedance of many series impedances (at least 2 requried)
def ms(c1, c2, *others):
    res = s(c1, c2)
    for c in others:
        res = s(res, c)
    return res

# python's cmath library includes the cmath.polar(x) and cmath.rect(r, phi) functions
# cmath.polar(x) returns the representation of x in polar coordinates, a tuple (r, phi)
# cmath.rect(r, phi) returns the rectangular representation, a complex number
# to unpack a tuple (r, phi) and use it as the argument of cmath.rect, do cmath.rect(*tuple)
# returns equivalent impedance of 2 parallel impedances
