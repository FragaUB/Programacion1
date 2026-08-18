from Dic_Perfumeria import nombres, precios, stock 

def generar_catalogo():
    print("Cargando catalogo...")
    for clave, valor in nombres.items():
        print(f"{clave}: {valor}")
    print()
    for clave, valor in precios.items():
        print(f"{clave}: {valor}")
    print()
    for clave, valor in stock.items():
            print(f"{clave}: {valor}")
    print()

def generar_producto():
    print("Añade una nuevo producto")
    salir = 1
    while salir:
        print("Para finalizar intrese 0")
        cod = input(f"Ingrese el codigo; Max 6 caracteres: ")
        if len(cod) <= 6 and len(cod) > 1:
            new_name = input("Ingrese el nomre del nuevo producto: ")
            new_price = float(input("Ingrese el precio: "))
            new_stock = int(input("Ingrese al cantidad de stock: "))
            # Faltan las verificaciones, se dejan para despues. :)
            # Agregar al diccionario
            nombres[cod] = new_name
            precios[cod] = new_price
            stock[cod] = new_stock
            print("Producto agregado!")
            return True
        else:
            print("Error al cargar el producto:")
            return False
    return True

def eliminar_producto():
    print("Eliminar un producto determinado")
    cod = input("Escriba el codigo:")
    for i in nombres.items():
        print(f"Codigos dispobibles: {i}")
    if cod in nombres.keys():
        del nombres[cod]
        del precios[cod]
        del stock[cod]
        return True
    else:
        return False

def modificar_precio_producto():
    print("Modificar el precio de un producto")
    cod = input("Escriba el codigo:")
    if cod in precios.keys():
        new_price = float(int("Ingrese el nuevo precio: "))
        precios[cod] = new_price
        print(f"Precio del codigo {cod} actualizado!")
        return True
    else:
        return False

def generar_compra():
    print("Añade al carrito un nuevo producto")
    print("Cargando catalogo...")
    for clave, valor in nombres.items():
        print(f"{clave}: {valor}")
    print()
    for clave, valor in stock.items():
        print(f"{clave}: {valor}")
    print()
    print("Ingrese una opcion:")
    print("1: Sumar Stock:")
    print("2: Vender:")
    op = int(input("Opcion: <"))
    if op == 1:
        Sumar_Stock()
        return True
    elif op == 2:
        Vender()
        return True
    else:
        print("Opcion invalida")
    return False

def Sumar_Stock():
    cod = input("Escriba el codigo:")
    if cod in stock.keys():
        new_stock = float(int("Ingrese el nuevo stock: "))
        stock[cod] += new_stock
        print(f"Stock del codigo {cod} actualizado!")
        generar_catalogo()
        return True
    else:
        return False

def Vender() -> tuple[str, float]:
    generar_catalogo()
    carrito : str = ""
    precio : float
    cod = input("Escriba el codigo:")
    if cod in nombres.keys():
        carrito = nombres[cod]
        precio = precios[cod]
        if stock[cod] > 0:
            stock[cod] -= 1
        else:
            print("No hay stock disponible")        
        return carrito, precio
    else:
        print("Error al generar la venta")
        return None
