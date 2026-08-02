'''
1. Tomando el ejercicio de estructuras selectivas cuyo enunciado dice:
“Una persona abona un producto, si el importe es menor que el precio
del producto, avisarle que el dinero es insuficiente. Si el importe abonado
es mayor, calcular el vuelto”, realizar un nuevo algoritmo que ejecute la
operación anterior de manera repetitiva y sólo termine cuando se
ingresa un valor de producto de cero pesos. Utilizar el ciclo apropiado.
2. Realizar un algoritmo que pida uno por uno los precios de los
productos comprados por el cliente en un mercado, y que al ingresar
un precio igual a cero muestre el total de la compra y la cantidad de
productos. El cliente siempre compra al menos un producto. Utilizar el
ciclo apropiado.
3. Realizar un algoritmo que calcule la nota promedio de un curso. Se
dispone de la nota de cada examen y la cantidad de alumnos que lo
rindieron. Utilizar el ciclo apropiado.
'''

def CalculoProducto():
    Precio = float(input("Ingrese el precio del producto (0 para salir): => "))

    while Precio != 0:
        Importe = float(input("Ingrese el importe abonado: => "))
        if Importe < Precio:
            print("El dinero es insuficiente.")
        else:
            Vuelto = Importe - Precio
            print("El vuelto es: $", Vuelto)
        Precio = float(input("Ingrese el precio del producto (0 para salir): => "))

    print("Programa finalizado")
    exit()

#######################################################

def CalculoPrecio():
    TotalCompra = 0.0
    CantidadProductos = 0

    print("Ingrese el precio del producto (0 para finalizar):")
    Precio = float(input("=> "))

    while Precio != 0:
        TotalCompra += Precio
        CantidadProductos += 1
        print("Ingrese el precio del siguiente producto (0 para finalizar):")
        Precio = float(input("=> "))

    print(f"Total de la compra: ${TotalCompra}")
    print(f"Cantidad de productos: {CantidadProductos}")

########################################################

def CalculoNota():
    TotalNotas = 0.0
    CantidadAlumnos = 0

    print("Ingrese la nota del examen (0 para finalizar):")
    Nota = float(input("=> "))

    while Nota != 0:
        if 0 <= Nota <= 10:
            TotalNotas += Nota
            CantidadAlumnos += 1
        else:
            print("Nota inválida.")

        print("Ingrese la siguiente nota (0 para finalizar):")
        Nota = float(input("=> "))

    if CantidadAlumnos > 0:
        Promedio = TotalNotas / CantidadAlumnos
        print(f"Promedio de notas: {Promedio}")
    else:
        print("No se ingresaron notas.")

#########################################

def main():
    print("Entrando a la funcion main")
    print("Seleccione alguna opcion a continuacion:")
    Option = int(input("0. Salir / 1. P1 / 2. P2 / 3. P3: => "))
    while Option != 0:
        if Option == 1:
            CalculoProducto()
        elif Option == 2:
            CalculoPrecio()
        elif Option == 3:
            CalculoNota()
        else:
            print("Opción inválida.")

    print("\nSeleccione otra opción:")
    Option = int(input("0. Salir / 1. P1 / 2. P2 / 3. P3: => "))

main()