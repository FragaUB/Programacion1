import vivero
def agregar_producto_nuevo(ruta_archivo: str) -> None:
    print("\n--- AGREGAR NUEVA PLANTA ---")
    try:
        id_planta = input("Ingrese el ID de la planta: ").strip()
        nombre = input("Ingrese el nombre de la planta: ").strip()
        precio = input("Ingrese el precio de la planta: ").strip()
        dias_sin_regar = input("Ingrese los días sin regar la planta: ").strip()
        frecuencia_riego_dias = input("Ingrese la frecuencia de riego en días: ").strip()
        nueva_planta = f"{id_planta},{nombre},{precio},{dias_sin_regar},{frecuencia_riego_dias}\n"
        try:
            with open(ruta_archivo, "a", encoding="utf-8") as f:
                f.write(nueva_planta)
            print(f"Planta '{nombre}' agregada al catálogo.\n") 
        except FileNotFoundError:
            print(f"Error al agregar la planta: El archivo '{ruta_archivo}' no existe.")
    except ValueError:
        print("Error: Por favor, ingrese valores válidos.")


def reporte_riego_urgente(ruta_archivo: str) -> None:
    try:
        planta = open(ruta_archivo, "r", encoding="utf-8")
        for linea in planta:
            dato_planta = linea.strip().split(",")
            if dato_planta[3] < dato_planta[4]:
                print(f"Planta: {dato_planta[1]}, Días sin regar: {dato_planta[3]}, Frecuencia de riego: {dato_planta[4]}")
        planta.close()
    except FileNotFoundError:
        print(f"Error al agregar la planta: El archivo '{ruta_archivo}' no existe.")

def reporte_plantas_al_dia(ruta_archivo: str) -> None:
    try:
        planta = open(ruta_archivo, "r", encoding="utf-8")
        for linea in planta:
            dato_planta = linea.strip().split(",")
            if dato_planta[3] > dato_planta[4]:
                print(f"Planta: {dato_planta[1]}, Días sin regar: {dato_planta[3]}, Frecuencia de riego: {dato_planta[4]}")
        planta.close()
    except FileNotFoundError:
        print(f"Error al agregar la planta: El archivo '{ruta_archivo}' no existe.")

def main() -> None:
    ARCHIVO = "vivero.csv"
    vivero.guardar_catalogo_inicial_csv(ARCHIVO)
    opcion = ""
    while opcion != "4":
        print("\n=== SISTEMA DE GESTIÓN DE VIVERO ===")
        print("1. Agregar nueva planta al catálogo")
        print("2. Reporte de plantas que requieren riego URGENTE")
        print("3. Reporte de plantas que AÚN NO requieren riego")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            agregar_producto_nuevo(ARCHIVO)
        elif opcion == "2":
            reporte_riego_urgente(ARCHIVO)
        elif opcion == "3":
            reporte_plantas_al_dia(ARCHIVO)
        elif opcion == "4":
            print("Saliendo del programa...")
        else:
            print("Opción inválida.")
if __name__ == "__main__":
    main()