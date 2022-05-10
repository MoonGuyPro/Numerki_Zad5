import numpy as np
from sympy import *


def f_x(x, function):
    f = eval(function)
    return f


def Simpson_method(a, b, funct):
    result = 0.0
    diff = 10
    iteration = 1
    n = 3

    while diff > 0.1:
        old_result = result
        h = (b - a) / (n - 1)
        x = np.linspace(a, b, n)
        f = f_x(x, funct)

        result = (h / 3) * (f[0] + 2 * sum(f[:n - 2:2]) + 4 * sum(f[1:n - 1:2]) + f[n - 1])
        n += 1
        iteration += 1
        diff = abs(result - old_result)
    # print("Liczba iteracji: " + str(iteration))
    return round(result, 2)