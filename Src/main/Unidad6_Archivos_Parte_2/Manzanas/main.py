import manzanas
import PROGRA_38 

def main() -> None:
    ARCHIVO = "cosecha.csv"
    manzanas.generar_cosecha_csv(ARCHIVO, 1000)
    # En este punto, el archivo ya se genero y ya esta relleno
    opcion = ""
    while opcion != "4":
        print("\n=== MENÚ DE ANÁLISIS DE COSECHA ===")
        print("1. Buscar registros por Mes y Día")
        print("2. Ver Matriz de Cosecha (Árbol vs Mes)")
        print("3. Hallar la/s manzana/s más pesada/s")
        print("4. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            PROGRA_38.buscar_por_fecha(ARCHIVO) # Solo leer la archivo
        elif opcion == "2":
            PROGRA_38.mostrar_matriz_cosecha(ARCHIVO) # Solo leer la archivo
        elif opcion == "3":
            PROGRA_38.encontrar_manzana_mas_pesada(ARCHIVO) # Solo leer la archivo
        elif opcion == "4":
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()