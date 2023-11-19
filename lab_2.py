import math

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
x = float(input("Введіть значення x: "))

y = a + b * x ** 2.518 + math.cos(3 * a * x)

print("Значення y = {:.3f}".format(y))