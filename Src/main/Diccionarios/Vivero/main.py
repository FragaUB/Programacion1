import vivero

def main() -> None:
    print("=== SISTEMA DE GESTION DE VIVERO ===")
    catalogo = vivero.obtener_catalogo_inicial()
    # 1. Revisar plantas con necesidad de riego
    a_regar = vivero.obtener_plantas_para_regar(catalogo)
    print("\n Plantas que requieren riego urgente:")
    for p in a_regar:
        print(f" - {p['nombre']}: Lleva {p['dias_sin_regar']} dias sin agua (Max: {p['frecuencia_riego_dias']})")
    # 2. Actualizar precios
    AUMENTO = 15.0 # 15%
    print(f"\nAplicando aumento del {AUMENTO}% por inflacion...")
    vivero.aplicar_aumento_precios(catalogo, AUMENTO)
    print("\nPrecios actualizados:")
    for p in catalogo:
        print(f" - {p['nombre']}: ${p['precio']:.2f}")

if __name__ == "__main__":
    main()