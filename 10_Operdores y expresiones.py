# Lectura del valor
x = float(input("Introduce el valor de x: "))

# cálculo paso a paso
parte1 = 1 / x
parte2 = x + parte1
parte3 = 1 / parte2
parte4 = x + parte3
parte5 = 1 / parte4

y = 1 / (x + parte5)

print("y =", y)