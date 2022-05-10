from numpy.polynomial.chebyshev import chebgauss
from sympy import *


def coefficients(nodes):
    A_i, x_i = chebgauss(nodes)
    return A_i, x_i


def Gauss_Chebyshev(funct, nodes):
    x = Symbol('x')
    A_i, x_i = coefficients(nodes)
    result = simplify(x-x)
    for i in range(nodes):
        result += x_i[i] * funct.subs(x, A_i[i])
    return result
