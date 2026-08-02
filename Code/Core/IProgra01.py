'''1. Se requiere determinar el sueldo semanal de un trabajador con base en las
horas que trabaja y el pago por hora que recibe. Realice el diagrama de
flujo y el pseudocódigo que representen el algoritmo de solución
correspondiente.
2. Se requiere armar un algoritmo que, ingresando el valor de dólares que se
tiene y cuánto es su cotización al día de la fecha, haga la conversión a
pesos.
3. Se requiere armar un algoritmo que, ingresando un valor en kilos, devuelva
el valor en onzas.
4. Realice un diagrama de flujo y pseudocódigo que representen el algoritmo
para determinar cuánto pagará finalmente una persona por un artículo
equis, considerando que tiene un descuento de 20%, y debe pagar 21% de
IVA (debe mostrar el precio con descuento y el precio final).
5. Realice un ejercicio que pida al usuario su salario mensual, su porcentaje de
ahorro y el precio del producto que quiere comprar. Luego que imprima
cuántos meses hacen falta para poder comprar dicho producto.'''

##########################################

def CalcularSueldo():
    #Variable globales
    ValorXHoras = 150.0
    SueldoCalculado = 0.0
    print("Ingrese las horas operadas:")
    HorasOperadas = float(input("=> "))
    SueldoCalculado = float(ValorXHoras) * HorasOperadas

    #Muestra de resultados:
    print(f"Sueldo presupuestado: {SueldoCalculado}")

##########################################

def ConversorDivisas():
    ValorNominalPesos = 1549.50 # Ponele ".-."
    ConversionParcial = 0.0
    print("Ingrese la cantidad de dolares para la conversion")
    print(f"Cotizacion actual del dolar {ValorNominalPesos}")
    CantidadDolares = float(input("=> "))

    #Conversion:
    ConversionParcial = float(ValorNominalPesos * CantidadDolares)
    print(f"Cantidad de convertida: {ConversionParcial}")

##########################################

def ConversorKilogramos():
    ConstOnzas = 0.02834952

    print("Ingrese el valor en kilogramos:")
    ValorKilogramo = float(input("=> "))

    ValorConversion = ValorKilogramo / ConstOnzas

    print("El valor en onzas es:", ValorConversion)

##########################################

def CalcularPrecio():
    print("Ingrese el precio del artículo:")
    Precio = float(input("=> "))

    Descuento = Precio * 0.20
    PrecioDescuento = Precio - Descuento

    IVA = PrecioDescuento * 0.21
    PrecioFinal = PrecioDescuento + IVA

    print("Precio con descuento: $", PrecioDescuento)
    print("Precio final con IVA: $", PrecioFinal)

##########################################

def CalcularCuotas():
    print("Ingrese su salario mensual:")
    Salario = float(input("=> "))

    print("Ingrese el porcentaje de ahorro:")
    PorcentajeAhorro = float(input("=> "))

    print("Ingrese el precio del producto:")
    PrecioProducto = float(input("=> "))

    AhorroMensual = Salario * (PorcentajeAhorro / 100)
    Meses = PrecioProducto / AhorroMensual

    print("Necesita", Meses, "meses para comprar el producto.")

##########################################

def main():
    print("Entrando a la funcion main")
    print("Seleccione alguna opcion a continuacion:")
    Option = int(input("0. Salir / 1. P1 / 2. P2 / 3. P3 / 4. P4 / 5. P5:"))
    while Option != 0:
        if Option == 1:
            CalcularSueldo()
        elif Option == 2:
            ConversorDivisas()
        elif Option == 3:
            ConversorKilogramos()
        elif Option== 4:
            CalcularPrecio()
        elif Option == 5:
            CalcularCuotas()
    print("Programa finalizado")

main()