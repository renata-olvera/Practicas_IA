def es_bisiesto(anio):

    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False


lista_anios = [1900, 2000, 2016, 1987]
resultados_correctos = [False, True, True, False]

for i in range(len(lista_anios)):
    anio = lista_anios[i]
    print(anio, "-> ", end="")

    if es_bisiesto(anio) == resultados_correctos[i]:
        print("OK")
    else:
        print("Fallido")