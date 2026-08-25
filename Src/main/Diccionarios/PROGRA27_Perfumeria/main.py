import Funciones_Perfumeria

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE PERFUMERÍA ---")
    print("1. Consultar catálogo y stock")
    print("2. Agregar nuevo producto")
    print("3. Eliminar producto")
    print("4. Modificar precio")
    print("5. Actualizar stock (Compra/Venta)")
    print("6. Salir")
    opcion = ""
    while opcion != "6":
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Funcion de Catalogo:
            Funciones_Perfumeria.generar_catalogo()
            pass
        elif opcion == "2":
            # Funcion de nuevo producto
            Funciones_Perfumeria.generar_producto()
            pass
        elif opcion == "3":
            Funciones_Perfumeria.eliminar_producto()
            pass
        elif opcion == "4":
            Funciones_Perfumeria.modificar_precio_producto()
            pass
        elif opcion == "5":
            # Integra un trigger, que actualiza el stock una vez consumado la compra
            Funciones_Perfumeria.generar_compra()
            pass
        elif opcion == "6":
            print("Saliendo del sistema...")
        else:
            print("Opción inválida. Intente nuevamente.")
    exit()

def main():
    print("Progra1: Perfumeria")
    mostrar_menu()

main()