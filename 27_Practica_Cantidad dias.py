def es_bisiesto(anio):
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True


def dias_en_mes(anio, mes):

    if anio < 1582 or mes < 1 or mes > 12:
        return None

    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 2 and es_bisiesto(anio):
        return 29

    return dias[mes - 1]


# pruebas
datos_prueba = [(1900,2),(2000,2),(2016,1),(1987,11)]
resultados = [28,29,31,30]

for i in range(len(datos_prueba)):
    anio, mes = datos_prueba[i]
    print(anio, mes, "->", dias_en_mes(anio, mes))