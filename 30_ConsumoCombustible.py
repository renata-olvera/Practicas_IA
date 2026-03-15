def litros_100km_a_mpg(litros):
    millas = 100000 / 1609.344
    galones = litros / 3.785411784
    return millas / galones


def mpg_a_litros_100km(mpg):
    km = 100
    millas = km / 1.609344
    galones = millas / mpg
    litros = galones * 3.785411784
    return litros


print(litros_100km_a_mpg(3.9))
print(litros_100km_a_mpg(7.5))
print(litros_100km_a_mpg(10.0))

print(mpg_a_litros_100km(60.3))
print(mpg_a_litros_100km(31.4))
print(mpg_a_litros_100km(23.5))