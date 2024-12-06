from random import choice, uniform, randint

# FUNCIONES PARA EXTRAER LOS DATOS DE CADA CABALLO DE LA CARRERA
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
        cuota, saltos = round(uniform(6, 10), 2), range(1, 3)
    elif velocidad <= 55:
        cuota, saltos = round(uniform(3, 5), 2), range(1, 4)
    elif velocidad <= 65:
        cuota, saltos = round(uniform(2, 3), 2), range(1, 5)
    else:
        cuota, saltos = round(uniform(1, 1.50), 2), range(1, 6)

    return cuota, saltos, velocidad
