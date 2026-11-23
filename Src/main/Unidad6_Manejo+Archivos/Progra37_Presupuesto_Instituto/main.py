def cargar_insumos() -> None:
    try:
        archivo = open(
            r"C:\Users\franc\OneDrive\Documentos\GitHub\Programacion1\Src\main\Archivos\Presupuesto_Instituto\insumos.txt",
            "a"
        )
        while True:
            insumo = input("Ingrese un insumo (o 'FIN' para terminar): ")
            if insumo.upper() == "FIN":
                break
            archivo.write(insumo + "\n")
        archivo.close()
    except Exception as e:
        print(f"Error al guardar los insumos: {e}")

def procesar_insumos() -> dict:
    dic_insumos = {}
    try:
        archivo = open(
            r"C:\Users\franc\OneDrive\Documentos\GitHub\Programacion1\Src\main\Archivos\Presupuesto_Instituto\insumos.txt",
            "r"
        )
        for linea in archivo:
            insumo = linea.strip()
            if insumo in dic_insumos:
                dic_insumos[insumo] += 1
            else:
                dic_insumos[insumo] = 1
        archivo.close()
        return dic_insumos
    except FileNotFoundError:
        print("Error: No se encontró el archivo insumos.txt.")
        return {}

def calcular_presupuesto(diccionario: dict) -> None:
    total = 0
    for insumo in diccionario:
        while True:
            try:
                precio = float(
                    input(f"Ingrese el precio unitario de '{insumo}': ")
                )
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Error: debe ingresar un número válido.")
        cantidad = diccionario[insumo]
        subtotal = precio * cantidad
        total += subtotal
        print(
            f"{insumo}: {cantidad} unidad/es x ${precio:.2f} = ${subtotal:.2f}"
        )
    print(f"\nPresupuesto total: ${total:.2f}")

def main():
    print("Inicio del programa\n")
    cargar_insumos()
    insumos = procesar_insumos()
    if len(insumos) > 0:
        print("\nInsumos procesados:")
        print(insumos)
        print("\n--- Cálculo del presupuesto ---")
        calcular_presupuesto(insumos)
    else:
        print("No hay insumos para procesar.")

if __name__ == "__main__":
    main()
