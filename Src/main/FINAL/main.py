import pandas as pd
import transport as tr

class Main:
    def main():
        lista_paquetes = [("AA00", "Remeras", 500, "Creado", "Tierra del Fuego", "Pinamar"), 
                            ("AA01", "Juguetes", 6000, "Creado", "Tierra del Fuego", "Pinamar"), 
                            ("AA02", "Sabanas", 8000, "Creado", "Tierra del Fuego", "Pinamar"),
                            ("AA04", "Reloj", 2500, "Creado", "Tierra del Fuego", "Pinamar"),
                            ("AA05", "Pantalones", 500, "Creado", "Tierra del Fuego", "Pinamar"),
                            ("AA05", "Cubiertos", 4500, "Creado", "Tierra del Fuego", "Pinamar")]
        transportes : list = tr.main.upgrade_file_transport()
        plantilla = pd.DataFrame(transportes)
        print(plantilla)

Main.main()