'''
PROG_00: Un cuadrado mágico es una matriz cuadrada en la que la suma de
los números en todas las filas, todas las columnas y la diagonal
principal es siempre la misma. Por ejemplo, este cuadrado lo es:
Programar un sistema en Python que permita:
- Ingresar una matriz cuadrada con números definidos por el
usuario
- Verificar si los números ingresados forman un cuadrado mágico.
(Se incluye un template para desarrollar el programa completo)
'''
def validarFilas(cuadradoMagico):
    for i in range(len(cuadradoMagico)):
        sumaFila = sum(cuadradoMagico[i])
        if i == 0:
            sumaReferencia = sumaFila
        elif sumaFila != sumaReferencia:
            return False
    return True


def validarColumnas(cuadradoMagico):
    n = len(cuadradoMagico)
    for j in range(n):
        sumaColumna = sum(cuadradoMagico[i][j] for i in range(n))
        if j == 0:
            sumaReferencia = sumaColumna
        elif sumaColumna != sumaReferencia:
            return False
    return True

def validarDiagonales(cuadradoMagico, suma):
    sumaDiagonal = sum(cuadradoMagico[i][i] for i in range(len(cuadradoMagico)))
    if sumaDiagonal != suma:
        return False
    return True

def validarCuadrado(cuadradoMagico):
    resultadoFilas = validarFilas(cuadradoMagico)
    resultadoColumnas = validarColumnas(cuadradoMagico)
    resultadoDiagonales = validarDiagonales(cuadradoMagico, resultadoFilas)
    return resultadoFilas and resultadoColumnas and resultadoDiagonales

def pedir_valores(n, matriz):
    print(f"Ingrese los {n * n} valores de la matriz, fila por fila:")
    for i in range(n):
        for j in range(n):
            matriz[i][j] = pedirnumero(i, j)
    return matriz


def generar_matriz(n, matriz):
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        matriz.append(fila)
    return matriz


def pedirnumero(fila, columna):
    try:
        numero = int(input(f"Ingrese el valor para la posición ({fila}, {columna}): "))
        if numero > 0:
            return numero
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return pedirnumero(fila, columna)

def main():
    print("cuadrado magico")
    numero = pedirnumero(0, 0)
    matriz = []
    matriz = generar_matriz(numero, matriz)
    for i in range(numero):
        print(matriz[i])
    matriz = pedir_valores(numero, matriz)
    esMagico = validarCuadrado(matriz)
    if esMagico:
        print("La matriz es un cuadrado mágico.")
    else:
        print("La matriz no es un cuadrado mágico.")
main()