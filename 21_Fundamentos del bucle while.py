bloques = int(input("Introduce la cantidad de bloques: "))

altura = 0
necesarios = 1

while bloques >= necesarios:
    bloques -= necesarios
    altura += 1
    necesarios += 1

print("La altura de la pirámide es:", altura)