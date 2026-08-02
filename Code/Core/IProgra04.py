'''
• Realizar un programa para ingresar desde el teclado un conjunto de números
(validando que sean enteros positivos.) Si se ingresa -1 se finaliza el bucle y se muestra
pantalla el menor y el mayor de ellos.
• Crear un programa que cree la tabla de multiplicar de un número entero hasta el 12. El
múltiplo es ingresado por el usuario. Al terminar el bucle, se muestra la suma de los 12
números mostrados.
• Se desea analizar cuántos autos circulan con patente con numeración par y cuántos
con numeración impar en un día. Escribir un programa que permita ingresar la
terminación de la patente (entre 0 y 9) hasta ingresar -1 e informe cuántos vehículos
pasaron con numeración par y cuántos con numeración impar.
• El factorial de un número entero N mayor que cero se define como el producto de
todos los enteros X tales que 0 < X <= N. Desarrollar un programa para calcular el
factorial de un número dado. Deberán rechazarse las entradas inválidas (menores que
0).
• Leer números que representan edades de un grupo de personas, finalizando la lectura
cuando se ingrese el número -1. Imprimir cuántos son menores de 18 años, cuántos
tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que
no representan una edad válida. (Se considera válida una edad entre 0 y 100).
'''

def CalcularMayorMenor():
    #Varibles globales
    a = 0
    b = 0 
    print("Calcular el mayor y menor: (-1 para finalizar)")
    while True:
        numero = int(input("Ingrese un número entero positivo: => "))
        if numero == -1:
            break
        elif numero < 0:
            print("Número inválido. Ingrese un número entero positivo.")
            continue


#########################################

def main():
    print("Entrando a la funcion main")
    print("Seleccione alguna opcion a continuacion:")
    Option = int(input("0. Salir / 1. P1 / 2. P2 / 3. P3: => "))
    while Option != 0:
        if Option == 1:
            CalcularMayorMenor()
        elif Option == 2:
            CalcularTablaMultiplicar()
        elif Option == 3:
            CalcularPatentes()
        elif Option == 4:
            CalcularFactorial()
        elif Option == 5:
            CalcularEdades()
        else:
            print("Opción inválida.")

    print("\nSeleccione otra opción:")
    Option = int(input("0. Salir / 1. P1 / 2. P2 / 3. P3: => "))

main()