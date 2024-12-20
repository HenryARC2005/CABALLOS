import datos_caballos as dc


class Usuario:
    def __init__(self, saldo):
        self.saldo = saldo

    def apostar(self, apuesta):
        self.saldo -= apuesta
        return apuesta

    def mostrar_saldo(self):
        print(f'\nSALDO DISPONIBLE ==> ${self.saldo:.2f}\n')


class Caballo:
    posicion = 0

    def __init__(self, nombre_genero, peso, edad, altura, cuotas_saltos_velocidad, etiqueta):
        self.nombre_genero = nombre_genero
        self.peso = peso
        self.edad = edad
        self.altura = altura
        self.cuotas_saltos_velocidad = cuotas_saltos_velocidad
        self.etiqueta = etiqueta

    def __str__(self):
        return f'CABALLO #{self.etiqueta}'

    def correr(self):
        suma = self.posicion + dc.choice(self.cuotas_saltos_velocidad[1])
        if suma > 49:
            self.posicion = 49
        else:
            self.posicion = suma


    def obtener_datos(self):
        print(f'* Nombre: {self.nombre_genero[0]}\n'
              f'* Género: {self.nombre_genero[1]}\n'
              f'* Peso: {self.peso} Kgs\n'
              f'* Edad: {self.edad} años\n'
              f'* Altura: {self.altura} mts\n'
              f'* Velocidad: {self.cuotas_saltos_velocidad[2]} Km/h\n'
              f'* Cuota: {self.cuotas_saltos_velocidad[0]}\n')
