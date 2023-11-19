x0 = float(input("Введіть значення x0: "))
x1 = float(input("Введіть значення x1: "))

for i in range(2, 100):

    xn = x1 * (x0 + 1)

    print("Значення xn = ", xn)

    x0 = x1
    x1 = xn