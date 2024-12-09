import clases_juego as cj
import datos_caballos as dc
from os import system


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
    for c in caballos.values():
        print(f'({c.etiqueta}) {c} --> {c.cuotas_saltos_velocidad[0]}')


def generar_caballos(cantidad):
    return {str(i+1): cj.Caballo(dc.nombre_genero(), dc.peso(), dc.edad(), dc.altura(), dc.cuota_saltos_velocidad(), i+1)
            for i in range(cantidad)}


def desarrollar_carrera(caballos, ha_terminado=False):
    for c in caballos.values():
        print(f'CABALLO #{c.etiqueta}  ' + ' '.join('_' if i != c.posicion else '*' for i in range(30)) + '\n')
        c.correr() if not ha_terminado else None
