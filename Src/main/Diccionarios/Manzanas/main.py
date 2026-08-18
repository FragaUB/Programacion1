import manzanas

def main() -> None:
    print("Programa de simulacion de Manzaneros")

    # 1. Generar la cosecha
    CANTIDAD = 10000
    print(f"Generando {CANTIDAD} registros de cosecha...")
    registros = manzanas.generar_cosecha(CANTIDAD)

    # 2. Calcular y mostrar totales
    totales = manzanas.calcular_totales(registros)
    print(f"\nRegistros generados: {totales['total_registros']}")
    print(f"Peso total cosechado: {totales['peso_total_kg']:.2f} kg")


if __name__ == "__main__":
    main()