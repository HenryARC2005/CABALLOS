import clases_juego as cj
import datos_caballos as dc
from os import  system


def mostrar_menu():
    system('cls')
    print('''
    *** SELECCIONA LA MODALIDAD ***

    A... 2 Caballos.
    B... 4 Caballos.
    C... Salir al MENÚ PRINCIPAL. 
    ''')


def mostrar_caballos(caballos):
    print()
    system('cls')
    for k, v in caballos.items():
        print(f'({v.etiqueta}) {v} --> {v.cuotas_saltos_velocidad[0]}')


def generar_caballos(cantidad):
    return {f'{i+1}': cj.Caballo(dc.nombre_genero(), dc.peso(), dc.edad(), dc.altura(), dc.cuota_saltos_velocidad(), i+1)
            for i in range(cantidad)}
