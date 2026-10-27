class Paquete:
    def __init__(self,  info):
        self.codigo = info[0]
        self.denominacion = info[1]
        self.peso = info[2]
        self.estado = info[3]
        self.origen = info[4]
        self.destino = info[5]

    def actualizar_estado_paquete(self, nuevo_estado : str):
        if nuevo_estado != self.estado:
            self.estado = nuevo_estado
            print("Estado del paquete actualizado")
        else:
            print("Estado del paquete no fue actualizado")

    def mostrar_informacion(self):
        print(
            f"Código: {self.codigo} | "
            f"Denominación: {self.denominacion} | "
            f"Peso: {self.peso} | "
            f"Estado: {self.estado} | "
            f"Origen: {self.origen} | "
            f"Destino: {self.destino}"
        )

class Transporte:
    def __init__(self, informacion_flota : tuple):
        self.identificacion = informacion_flota[0]
        self.tipo = informacion_flota[1]
        self.capacidad_max = informacion_flota[2]
        self.paquetes = []

    def cargar_paquete(self, paquete):
        peso_actual = sum(p.peso for p in self.paquetes)
        if peso_actual + paquete.peso <= self.capacidad_max:
            self.paquetes.append(paquete)
            paquete.actualizar_estado_paquete("En tránsito")
            print(
                f"{paquete.codigo} asignado a "
                f"{self.identificacion}"
            )
            return True
        return False

    def mostrar_informacion(self):
        peso_actual = sum(p.peso for p in self.paquetes)
        print(f"\nTransporte: {self.identificacion}")
        print(f"Tipo: {self.tipo}")
        print(f"Capacidad: {self.capacidad_max}")
        print(f"Peso cargado: {peso_actual}")
        for paquete in self.paquetes:
            paquete.mostrar_informacion()

class TransporteTerrestre(Transporte):
    def calcular_costo(self, peso, distancia):
        return peso * distancia * 100

class TrasporteAereo(Transporte):
    def calcular_costo(self, peso, distancia):
        return peso * distancia * 300

class TrasporteMaritimo(Transporte):
    def calcular_costo(self, peso, distancia):
        return peso * distancia * 40

class Main:
    def main():
        #Incializar paquetes
        lista_paquetes = [("AA00", "Remeras", 500, "Creado", "Tierra del Fuego", "Pinamar"), 
                            ("AA01", "Juguetes", 6000, "Creado", "Tierra del Fuego", "Pinamar"), 
                            ("AA02", "Sabanas", 8000, "Creado", "Tierra del Fuego", "Pinamar"),
                            ("AA04", "Reloj", 2500, "Creado", "Tierra del Fuego", "Pinamar"),
                            ("AA05", "Pantalones", 500, "Creado", "Tierra del Fuego", "Pinamar"),
                            ("AA05", "Cubiertos", 4500, "Creado", "Tierra del Fuego", "Pinamar")]
        paquetes_embalados = []
        for i in lista_paquetes:
            paquete = Paquete(i)
            paquetes_embalados.append(paquete)

        for paquete in paquetes_embalados:
            paquete.mostrar_informacion()

        # Ahora cargarmos todos estos paquetes en un transporte
        lista_transporte = transportes = [
            ("AB123C", "Camion", 12000, 0),
            ("XZ89KL", "Camioneta", 1800, 0),
            ("QW45ER", "Furgoneta", 3200, 0),
            ("TY78UI", "Avion", 45000, 0),
            ("GH56JK", "Barco", 85000, 0),
            ("MN34OP", "Camion", 15000, 0),
            ("RS12TU", "Camioneta", 2200, 0),
            ("VW90XY", "Furgoneta", 2800, 0),
            ("ZA67BC", "Avion", 60000, 0),
            ("DE45FG", "Barco", 120000, 0),
            ("HI23LM", "Camion", 10000, 0),
            ("NP78QR", "Camioneta", 2500, 0),
            ("ST56VW", "Furgoneta", 3500, 0),
            ("XY34ZA", "Avion", 38000, 0),
            ("BC12DE", "Barco", 95000, 0)
        ]
        transportes = []
        for datos in lista_transporte:
            tipo = datos[1]
            if tipo in ("Camion", "Camioneta", "Furgoneta"):
                transporte = TransporteTerrestre(datos)
            elif tipo == "Avion":
                transporte = TrasporteAereo(datos)
            elif tipo == "Barco":
                transporte = TrasporteMaritimo(datos)
            else:
                continue
            transportes.append(transporte)

        for paquete in paquetes_embalados:
            asignado = False
            for transporte in transportes:
                if transporte.cargar_paquete(paquete):
                    asignado = True
                    break
            if not asignado:
                print(f"No se pudo asignar {paquete.codigo}")

        for transporte in transportes:
            transporte.mostrar_informacion()
Main.main()