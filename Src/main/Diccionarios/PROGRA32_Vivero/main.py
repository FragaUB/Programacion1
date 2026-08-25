import vivero

def main() -> None:
    print("=== SISTEMA DE GESTION DE VIVERO ===")
    catalogo = vivero.obtener_catalogo_inicial()
    # Catalogo => Tipo Diccionarios
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

    ##############################
    # PROGRA_V2_MANZANAS:
    ranking_regado = sorted(catalogo, key=lambda planta: planta["dias_sin_regar"] - planta["frecuencia_riego_dias"])
    print(ranking_regado)
    
    precio_descuento = list[lambda catalogo: round(catalogo["precio"] * 0.8, 2) if catalogo["precio"] > 2000 else catalogo["precio"]]
    print(precio_descuento)

    plantas_seleccionadas = list(filter( lambda catalogo: (catalogo["nombre"].startswith("M") or catalogo["nombre"].startswith("L")) and catalogo["precio"] < 2000, catalogo))
    print(plantas_seleccionadas)

if __name__ == "__main__":
    main()