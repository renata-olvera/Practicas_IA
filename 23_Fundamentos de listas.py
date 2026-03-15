lista = [1, 2, 3, 4, 5]

nuevo = int(input("Escribe un número: "))
lista[2] = nuevo

lista.pop()

print(len(lista))

print(lista)