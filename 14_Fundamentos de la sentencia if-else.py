ingreso = float(input("Escribe tu ingreso anual: "))

if ingreso <= 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = (ingreso - 85528) * 0.32 + 14839.02

# evitar impuestos negativos
if impuesto < 0:
    impuesto = 0

# redondear resultado
impuesto = round(impuesto, 0)

print("El impuesto es:", impuesto, "pesos")