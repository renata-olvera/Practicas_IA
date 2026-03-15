numero = int(input("Ingresa un número: "))

contador = 0

while True:

    if numero == 1:
        break

    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = numero * 3 + 1

    print(numero)
    contador = contador + 1

print("pasos =", contador)