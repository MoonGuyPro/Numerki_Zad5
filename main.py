def menu(funct):
    print("Podaj przedział aproksymacji, od: ")
    x_0 = input()
    print("do: ")
    x_n = input()
    print("Podaj stopień wielomianu aproksymującego: ")
    degree = input()
    print("Podaj ilość węzłów: ")
    nodes = input()


def main():
    check = True
    while (check):
        print("Wybierz funkcje: ")
        print("0. Wyjście")
        print("1. Liniowa: (−1/3)x − 2")
        print("2. |x|:  |x - 1| + 1")
        print("3. Wielomian: 3*x^(2)+2*x-2")
        print("4. Trygonometryczna: cos(x)+sin(x)")
        print("5. Złożenie: cos(x)-sin(x)+2*x")
        choice = input()
        if choice == "0":
            check = False
        elif choice == "1":
            funct = "(-1/3)*x - 2"

        elif choice == "2":
            funct = "abs(x - 1) + 1"

        elif choice == "3":
            funct = "3*x**2 + 2*x-2"

        elif choice == "4":
            funct = "np.cos(x)+np.sin(x)"

        elif choice == "5":
            funct = "np.cos(x)-np.sin(x)+2*x"

        else:
            print("Zły numer!")


if __name__ == '__main__':
    main()