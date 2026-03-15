numero_secreto = 777

print("""
*********************************
*  Juego: Adivina el número     *
*********************************
""")

while True:
    intento = int(input("Escribe tu número: "))

    if intento == numero_secreto:
        print("¡Bien hecho, muggle! Eres libre ahora.")
        break
    else:
        print("¡Ja ja! Estás atrapado en mi bucle!")