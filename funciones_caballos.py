import clases_juego as cj
import datos_caballos as dc
from os import system
from time import sleep


def mostrar_menu():
    system('cls')
    print('''
    *** SELECCIONA LA MODALIDAD ***

    A ... 2 Caballos.
    B ... 4 Caballos.
    C ... 8 Caballos.
    D ... Salir al MENÚ PRINCIPAL. 
    ''')


def mostrar_caballos(caballos):
    print()
    system('cls')
    for c in caballos.values():
        print(f'({c.etiqueta}) {c} --> {c.cuotas_saltos_velocidad[0]:.2f}')


def generar_caballos(cantidad):
    return {str(i + 1): cj.Caballo(dc.nombre_genero(), dc.peso(), dc.edad(), dc.altura(), dc.cuota_saltos_velocidad(),
                                   i + 1)
            for i in range(cantidad)}


def desarrollar_carrera(caballos, ha_terminado=False):
    system('cls')
    for c in caballos.values():
        print(f'CABALLO #{c.etiqueta}  ' + ' '.join('_' if i != c.posicion else '*' for i in range(30)) + '\n')
        c.correr() if not ha_terminado else None
    sleep(1)


# Función en donde se desarrolla toda la carrera y se determina al ganador
def carrera(cantidad_caballos):
    user = cj.Usuario(1000)
    caballos = generar_caballos(cantidad_caballos)
    comenzar_carrera = ha_apostado = False

    while not comenzar_carrera:
        mostrar_caballos(caballos)
        print(f'\n($) ... REALIZAR APUESTA\n(S) ... INICIAR CARRERA\n')

        user.mostrar_saldo()

        # Ingresar el número del caballo para visualizar todos sus datos
        opcion2 = input('\nSelecciona una opción para continuar ==> ').upper().strip()

        if opcion2 == '$':
            if ha_apostado:
                print('\nYA HAS REALIZADO UNA APUESTA EN LA CARRERA\n')
                system('pause')
                continue

            mostrar_caballos(caballos)
            caballo = input('\nNúmero del caballo sobre el que desea apostar ==> ')
            monto = input('Cantidad a apostar: $')
            monto = 0 if not monto.isnumeric() else float(monto)

            if any((monto > user.saldo, user.saldo <= 0, caballo not in caballos.keys(), monto == 0)):
                print('\nERROR... Datos de apuesta inválidos.\n')
                system('pause')

            elif monto < 100:
                print('\nMONTO MÍNIMO DE APUESTA: $100.00\n')
                system('pause')
            else:
                print('\nAPUESTA REALIZADA CON ÉXITO\n')
                apuesta = user.apostar(monto)
                ha_apostado = True
                system('pause')

        elif opcion2 == 'S':
            if not ha_apostado:
                print('\nNECESITAS REALIZAR UNA APUESTA PARA COMENZAR LA CARRERA\n')
                system('pause')
            else:
                comenzar_carrera = True
                system('pause')

        elif opcion2 in caballos.keys():
            print(f'\nDATOS DEL CABALLO #{opcion2}:\n')
            caballos[opcion2].obtener_datos()
            system('pause')

        else:
            print('\nOPCIÓN INVÁLIDA, POR FAVOR INTENTA OTRA VEZ.\n')
            system('pause')

    # Comenzando la carrera (Modalidad de 2 Caballos)
    while all([v.posicion < 29 for v in caballos.values()]):
        desarrollar_carrera(caballos)
    desarrollar_carrera(caballos, True)

    if max((c for c in caballos), key=lambda x: caballos[x].posicion) == caballo:
        user.saldo += apuesta * caballos[caballo].cuotas_saltos_velocidad[0]
        print(f'FELICIDADES, GANASTE LA APUESTA\n\n* SALDO DISPONIBLE: {user.saldo:.2f}\n')
        system('pause')
    else:
        print('HAS PERDIDO!!\n')
        system('pause')
