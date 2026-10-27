from random import randint

class Trasporte:
    def __init__(self, conductor, tipo, peso_max, cant_maximo_paquete) -> None:
        self.conductor = conductor
        self.tipo = tipo
        self.peso = peso_max
        self.cant_paquete = cant_maximo_paquete

    def __str__(self):
        return (f"Tipo: {self.tipo} | Conductor: {self.conductor} | "
                f"Peso máximo: {self.peso} kg | "
                f"Cantidad máxima de paquetes: {self.cant_paquete}")

class Paquete(Trasporte):
    def __init__(self, denominacion, peso, estado, origen, destino, transporte):
        super.__init__(t_transporte)
        t_transporte = transporte 

    def actualizar_estado_paquete(self, estado):
        self.estado = estado
        if paquete_inicial.estado == 1:
            print(f"El paquete fue codificado al estado en camino ({estado})")

    def __str__(self):
        return (f"Paquete: {self.denominacion}\n"
                f"Peso: {self.peso_paquete} kg\n"
                f"Estado: {self.estado}\n"
                f"Origen: {self.origen}\n"
                f"Destino: {self.destino}\n"
                f"Transporte asignado: {self.transporte.tipo}")

class Main:
    paquete_inicial = Paquete("Licuadora Liliana", 500, 0, "Tierra del Fuego", "Olavarria", Trasporte[0])
    paquete_inicial.actualizar_estado_paquete(1)
    print(paquete_inicial)
    tipo_vehiculo = ("Camioneta", "Trailer")
    conductor = ("Agustin", "Pepe")
    transportes = []
    for i, c in enumerate(tipo_vehiculo):
        transporte = Trasporte(conductor[i], c, randint(5000, 100000), randint(0,100))
        transportes.append(transporte)

    print(paquete_inicial)
    def mostrar():
        for transporte in Main.transportes:
            print(transporte)

Main.mostrar()