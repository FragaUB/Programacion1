import manzanas

def main() -> None:
    print("Programa de simulacion de Manzaneros")

    # 1. Generar la cosecha
    CANTIDAD = 7
    print(f"Generando {CANTIDAD} registros de cosecha...")
    # Validacion de cantidad.
    try:
        cantidad_verificado = manzanas.verificar_cantidad(CANTIDAD)
        cosecha = manzanas.generar_cosecha(cantidad_verificado)

        # 2. Calcular y mostrar totales
        totales = manzanas.calcular_totales(cosecha)
    except ImportError:
        print("Error: No se pudo importar el módulo 'manzanas'. Asegúrate de que el archivo 'manzanas.py' esté en el mismo directorio.")
        return
    
    print(f"\nRegistros generados: {totales['total_registros']}")
    print(f"Peso total cosechado: {totales['peso_total_kg']:.2f} kg")

    premium = list(filter(lambda cosecha: cosecha["peso"] >=
    450, cosecha))
    print("premium: => ", premium)

    pesos_kg = list(map(lambda diccionario: round(diccionario["peso"] / 1000, 3), premium))
    print("Conversion: => ", pesos_kg)

    semestres = list(map(lambda diccionario: "Primer Semestre" if diccionario["mes"] <= 6 else "Segundo Semestre", cosecha))
    print("Semestres: => ", semestres)

if __name__ == "__main__":
    main()