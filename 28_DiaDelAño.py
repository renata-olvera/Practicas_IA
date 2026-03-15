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

    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 2 and es_bisiesto(anio):
        return 29

    return dias_mes[mes - 1]


def dia_del_anio(anio, mes, dia):
    total = 0

    for i in range(1, mes):
        dias = dias_en_mes(anio, i)
        if dias is None:
            return None
        total += dias

    dias_mes_actual = dias_en_mes(anio, mes)

    if dias_mes_actual is None or dia < 1 or dia > dias_mes_actual:
        return None

    return total + dia


print(dia_del_anio(2000, 12, 31))