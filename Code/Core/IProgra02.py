'''
1. Para la venta de boletos de un espectáculo con cupo limitado, se ingresa
el precio del boleto y la cantidad solicitada por el cliente. Mostrar el total
a pagar, pero si solicita 5 o más boletos mostrar un mensaje indicando
que no se puede realizar la venta.
2. Una persona abona un producto, si el importe es menor que el precio del
producto, avisarle que el dinero es insuficiente. Si el importe abonado es
mayor, calcular el vuelto.
3. Un banco necesita establecer los nuevos límites de crédito de sus
tarjetas. Las de tipo 1 aumentarán un 25%; las de tipo 2 aumentarán un
35%; las de tipo 3 aumentarán un 40%, y las de cualquier otro tipo
aumentarán un 50%. Desarrollar un algoritmo para calcular el nuevo
límite según el límite actual y tarjeta del cliente.
4. Se requiere determinar cuál de tres cantidades proporcionadas es la
mayor. Asumir que todas son siempre diferentes.
'''

###########################################

def VentaBoletos():
    print("Ingrese el precio del boleto:")
    Precio = float(input("=> "))

    print("Ingrese la cantidad de boletos:")
    Cantidad = int(input("=> "))

    if Cantidad >= 5:
        print("No se puede realizar la venta.")
    else:
        Total = Precio * Cantidad
        print("Total a pagar: $", Total)

VentaBoletos()

############################################

def PagoProducto():
    print("Ingrese el precio del producto:")
    Precio = float(input("=> "))

    print("Ingrese el importe abonado:")
    Importe = float(input("=> "))

    if Importe < Precio:
        print("El dinero es insuficiente.")
    else:
        Vuelto = Importe - Precio
        print("El vuelto es: $", Vuelto)

PagoProducto()

############################################

def LimiteCredito():
    print("Ingrese el límite actual:")
    Limite = float(input("=> "))

    print("Ingrese el tipo de tarjeta (1, 2, 3 u otro):")
    Tipo = int(input("=> "))

    if Tipo == 1:
        NuevoLimite = Limite * 1.25
    elif Tipo == 2:
        NuevoLimite = Limite * 1.35
    elif Tipo == 3:
        NuevoLimite = Limite * 1.40
    else:
        NuevoLimite = Limite * 1.50

    print("El nuevo límite de crédito es: $", NuevoLimite)

LimiteCredito()

############################################

def NumeroMayor():
    print("Ingrese el primer número:")
    Num1 = float(input("=> "))

    print("Ingrese el segundo número:")
    Num2 = float(input("=> "))

    print("Ingrese el tercer número:")
    Num3 = float(input("=> "))

    if Num1 > Num2 and Num1 > Num3:
        print("El número mayor es:", Num1)
    elif Num2 > Num1 and Num2 > Num3:
        print("El número mayor es:", Num2)
    else:
        print("El número mayor es:", Num3)

NumeroMayor()

############################################