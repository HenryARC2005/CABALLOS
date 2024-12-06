import funciones_caballos as fc
import clases_juego as cj
from os import system
from time import sleep

# Limpiando la consola después de cada ejecución
system('cls')

# Usuario de prueba para testear la carrera y su funcionamiento
user = cj.Usuario(1000)

salir = False
while not salir:
    fc.mostrar_menu()
    opcion = input('Elige una opción ==> ').upper().strip()

    if opcion == 'A':
        caballos = fc.generar_caballos(2)

        comenzar_carrera = ha_apostado = False
        while not comenzar_carrera:
            fc.mostrar_caballos(caballos)

            print(f'\n($) ... REALIZAR APUESTA\n(S) ... INICIAR CARRERA\n')
            user.mostrar_saldo()

            # Ingresar el número del caballo para visualizar todos sus datos
            opcion2 = input('\nSelecciona una opción para continuar ==> ').upper().strip()

            if opcion2 == '$':
                if ha_apostado:
                    print('\nYA HAS REALIZADO UNA APUESTA EN LA CARRERA\n')
                    system('pause')
                    continue

                fc.mostrar_caballos(caballos)
                caballo = input('\nNúmero del caballo sobre el que desea apostar ==> ')
                monto = float(input('Cantidad a apostar: $'))

                if any((monto > user.saldo, user.saldo <= 0, caballo not in caballos.keys())):
                    print('\nERROR... Datos de apuesta inválidos.\n')
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
                    print()
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
            system('cls')
            for c in caballos.values():
                print(f'CABALLO #{c.etiqueta}  ' + ' '.join('_' if i != c.posicion else '*' for i in range(30)) + '\n')
                c.correr()
            sleep(1)
        system('cls')
        for c in caballos.values():
            print(f'CABALLO #{c.etiqueta}  ' + ' '.join('_' if i != c.posicion else '*' for i in range(30)) + '\n')
        sleep(1)

        if max((c for c in caballos), key=lambda x: caballos[x].posicion) == caballo:
            user.saldo += apuesta * caballos[caballo].cuotas_saltos_velocidad[0]
            print(f'FELICIDADES, GANASTE LA APUESTA\n\n* SALDO DISPONIBLE: {user.saldo:.2f}')
            system('pause')
        else:
            print('\nHAS PERDIDO!!\n')
            system('pause')



    elif opcion == 'C':
        system('cls')
        print('\nVolviendo...\n')
        system('pause')
        salir = True

    else:
        print('\nOPCIÓN INVÁLIDA, POR FAVOR INTENTA OTRA VEZ.\n')
        system('pause')
