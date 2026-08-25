import Diccionario_Progra29

def main() ->  None:
    print("Tienda electronica:") 
    Ganancias = {}

    for producto in Diccionario_Progra29.precios:
        Ganancias[producto] = Diccionario_Progra29.precios[producto] * Diccionario_Progra29.ventas[producto]

    for producto in Ganancias:
        print(f"{producto}: ${Ganancias[producto]}")

    total_general = sum(Ganancias.values())
    print(f"\nTotal general recaudado: ${total_general}")

    producto_mas_vendido : float  = max(Diccionario_Progra29.ventas)
    producto_mayor_ingreso : float = max(Ganancias)

    print(f"\nProducto más vendido: {producto_mas_vendido}")
    print(f"Unidades vendidas: {Diccionario_Progra29.ventas[producto_mas_vendido]}")

    print(f"\nProducto que aportó más ingresos: {producto_mayor_ingreso}")
    print(f"Ingresos generados: ${Ganancias[producto_mayor_ingreso]}")
    
main()