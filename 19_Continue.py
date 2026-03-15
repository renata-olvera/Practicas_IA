#Feo deborador de vocales
palabra = input("Ingresa una palabra: ")
palabra = palabra.upper()

for letra in palabra:
    if letra in "AEIOU":
        continue
    print(letra)