class Vehiculo:
    def __init__(self, color, ruedas):
        self.color=  color
        self.ruedas= ruedas
    def __str__(self):
       return f'Vehiculo [Color: {self.color}, Ruedas: {self.ruedas}]'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self.velocidad=velocidad

    def __str__(self):
        return f'Coche[Velocidad: {self.velocidad} Km/hr] {super().__str__()} '

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Bicicleta[ Tipo: {self.tipo}] {super().__str__()} '


vehiculo=Vehiculo('rojo','grandes')
print(vehiculo)

coche=Coche('azul','pequeñas', '30')
print(coche)

bicicleta= Bicicleta('plateado','mediana','montaña')
print(bicicleta)
