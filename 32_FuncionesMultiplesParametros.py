def velocidad(distancia, tiempo):
    return distancia / tiempo


def estado_velocidad(v):
    if v < 20:
        nivel = "muy lento"
    elif v < 60:
        nivel = "velocidad normal"
    else:
        nivel = "muy rápido"
    return v, nivel


distancia = float(input("Dime la distancia recorrida (km): "))
tiempo = float(input("Dime el tiempo empleado (horas): "))

v, nivel = estado_velocidad(velocidad(distancia, tiempo))

print("\nTu velocidad es:", round(v,2), "km/h")
print("Nivel:", nivel)