import Chebyshev_polynomials
from Chebyshev_polynomials import *
from sympy import *

def menu(funct):
    print("Podaj przedział aproksymacji, od: ")
    x_0 = input()
    print("do: ")
    x_n = input()
    print("Podaj stopień wielomianu aproksymującego: ")
    degree = input()
    print("Podaj liczbę węzłów: ")
    nodes = input()
    result = Chebyshev_polynomials.Approximation(funct, int(degree)+1, int(nodes))
    print("Wielomian aproksymujący: ")
    print(result)
    Chebyshev_polynomials.printing(float(x_0), float(x_n), funct, int(degree), int(nodes))


def main():
    check = True
    x = Symbol('x')
    while (check):
        print("Wybierz funkcje: ")
        print("0. Wyjście")
        print("1. Wykładowy: pi * (x + 1) * sqrt(1 - x ** 2)")
        print("2. |x|:  |x - 1| * sqrt(1 - x ** 2)")
        print("3. Wielomian: 3*x^(2)+2*x-2 * sqrt(1 - x ** 2)")
        print("4. Trygonometryczna: cos(x)+sin(x)")
        print("5. Złożenie: cos(x)-sin(x)+2*x")
        print("6. Liniowa: x + 2")
        choice = input()
        if choice == "0":
            check = False
        elif choice == "1":
            funct = pi * (x + 1) * sqrt(1 - x ** 2)
            menu(funct)
        elif choice == "2":
            funct = abs(x - 1) * sqrt(1 - x ** 2)
            menu(funct)
        elif choice == "3":
            funct = 3*x**2 + (2*x-2) * sqrt(1 - x ** 2)
            menu(funct)
        elif choice == "4":
            funct = sin(x)
            menu(funct)
        elif choice == "5":
            funct = cos(x)-sin(x)+2*x
            menu(funct)
        elif choice == "6":
            funct = x + 2
            menu(funct)

        else:
            print("Zły numer!")


if __name__ == '__main__':
    main()
