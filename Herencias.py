class Vehiculo:
    velocidad=350
    cilindrada=200


class Coche(Vehiculo):
    color = 'verde'
    ruedas = 4
    puertas = 5


c = Coche()
print(c)