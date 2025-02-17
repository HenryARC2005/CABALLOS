from random import choice, uniform, randint

def nombre_genero():
    with open('NOMBRES_gen.txt', encoding='UTF8') as archivo:
        nombre_y_gen = choice(archivo.readlines()).rstrip()
    return nombre_y_gen.split()


def peso():
    return round(uniform(400, 570), 2)


def edad():
    return randint(6, 12)


def altura():
    return round(uniform(1.45, 1.80), 2)


def cuota_saltos_velocidad():
    velocidad = randint(30, 71)

    if velocidad <= 40:
        cuota, saltos = round(uniform(2, 3), 2), range(2, 4)
    elif velocidad <= 55:
        cuota, saltos = round(uniform(1, 3), 2), range(1, 5)
    elif velocidad <= 66:
        cuota, saltos = round(uniform(1.20, 1.90), 2), range(1, 5)
    else:
        cuota, saltos = round(uniform(1.05, 1.40), 2), range(1, 6)

    return cuota, saltos, velocidad
