import funciones_caballos as fc
from clases_juego import Usuario
from os import system

# Limpiando la consola después de cada ejecución
system('cls')

user = Usuario(1000)
salir = False

while not salir:
    fc.mostrar_menu()
    opcion = input('Elige una opción ==> ').upper().strip()

    if opcion == 'A':
        fc.carrera(cantidad_caballos=2, usuario=user)

    elif opcion == 'B':
        fc.carrera(cantidad_caballos=4, usuario=user)

    elif opcion == 'C':
        fc.carrera(cantidad_caballos=8, usuario=user)

    elif opcion == 'D':
        system('cls')
        print('\nVolviendo...\n')
        system('pause')
        salir = True

    else:
        print('\nOPCIÓN INVÁLIDA, POR FAVOR INTENTA OTRA VEZ.\n')
        system('pause')
