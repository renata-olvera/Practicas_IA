# Leer datos de entrada
hora_inicio = int(input("Hora de inicio: "))
min_inicio = int(input("Minutos de inicio: "))
duracion = int(input("Duración del evento (minutos): "))

# Convertir todo a minutos
total_min = hora_inicio * 60 + min_inicio + duracion

# Obtener hora y minutos finales
hora_final = (total_min // 60) % 24
min_final = total_min % 60

# Mostrar resultado
print(hora_final, ":", min_final, sep="")