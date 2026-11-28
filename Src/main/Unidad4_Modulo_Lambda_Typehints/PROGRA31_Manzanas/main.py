import manzanas

def main() -> None:
    print("Programa de simulacion de Manzaneros")

    # 1. Generar la cosecha
    CANTIDAD = 7
    print(f"Generando {CANTIDAD} registros de cosecha...")
    cosecha = manzanas.generar_cosecha(CANTIDAD)

    # 2. Calcular y mostrar totales
    totales = manzanas.calcular_totales(cosecha)
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