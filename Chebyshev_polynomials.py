import math
import numpy.polynomial
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

import Newton_Cotes
from Newton_Cotes import *


def Chebyshev_polynominal(n):
    # p = numpy.polynomial.Chebyshev.basis(n)
    # poly = p.convert(kind=numpy.polynomial.Polynomial)
    x = Symbol('x')
    poly_list = [cos(i * acos(x)) for i in range(2)]
    for i in range(2, n):
        poly_list.append(simplify(2 * x * poly_list[i - 1] - poly_list[i - 2]))
    return poly_list


def Approximation(a, b, funct, n):
    x = Symbol('x')
    w_x = 1 / sqrt(1 - x**2)
    T_k = Chebyshev_polynominal(n)
    result = simplify(x-x)
    for i in range(n):
        count = simplify(w_x * funct * T_k[i]) #Ze wzoru wx * fx * Tx
        integral = Simpson_method(a, b, str(count))     #całkujemy na warunek ortogonalnosci
        if i == 0:
            result_integral = integral/pi
        else:
            result_integral = integral/(pi/2)
        result += simplify(result_integral * T_k[i])  #obliczamy wielomian aproksymacyjny zgodnie ze wzorem yx = c0g0(x) + ... + cmgm(x)
    return result


def printing(a, b, funct, n):
    x = Symbol('x')
    aprox = Approximation(a, b, funct, n)
    x_aprox = np.arange(a, b, 0.01)
    y_aprox = [aprox.subs(x, i) for i in x_aprox]
    y_real = [funct.subs(x, i) for i in x_aprox]
    plt.figure(figsize=(10, 7))
    plt.plot(x_aprox, y_aprox)
    plt.plot(x_aprox, y_real, "b")
    plt.xlabel("Oś OX")
    plt.ylabel("Oś OY")
    plt.show()
