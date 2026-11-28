class Transporte:
    def __init__(self, codigo, tipo, capacidad, ocupacion):
        self.codigo = codigo
        self.tipo = tipo
        self.capacidad = capacidad
        self.ocupacion = ocupacion

class TransporteTerrestre(Transporte):
    def calcular_costo(self, peso, distancia):
        return peso * distancia * 100

class TrasporteAereo(Transporte):
    def calcular_costo(self, peso, distancia):
        return peso * distancia * 300

class TrasporteMaritimo(Transporte):
    def calcular_costo(self, peso, distancia):
        return peso * distancia * 40

class main:
    def upgrade_file_transport() -> list:
        archivo = "transportes.txt"
        transportes = []
        try:
            with open(archivo, "r") as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(",")
                    transporte = Transporte(data[0], data[1], int(data[2]), int(data[3]))
                    transportes.append(transporte)
        except FileNotFoundError:
            print("El archivo de transportes no se encontró.")
        return transportes

