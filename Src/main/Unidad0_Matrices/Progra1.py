'''
PROG_01: Desarrollar un juego de mapa del tesoro. El jugador debe encontrar un
tesoro escondido en una matriz, con pistas limitadas Requisitos del
juego:
- Crear una matriz de tamaño n x n con números o símbolos (n es
ingresado por el usuario, se debe validar sea un entero).
- Colocar un “tesoro” al azar usando random.
- Dar al jugador una cantidad limitada de intentos para adivinar la
posición.
- En cada intento, el jugador ingresa coordenadas (fila, columna),
y se le dice si acertó o no. (validar enteros y que esté dentro
del rango de la matriz)
- Cuando el jugador acierte, debe mostrar por pantalla la matriz
con intentos y la cantidad de intentos realizados. El jugador debe
poder abandonar la partida.
'''

from random import randint

def generar_numero_randow():
    return randint(0, 12)

def generar_mapa_matriz(n):
    Matriz = [] 
    for i in range(n):
        Fila = []
        for j in range(n):
            Fila.append(0)
        Matriz.append(Fila)
    return Matriz

def ubicar_tesoro(matriz, n_randow_x, n_randow_y):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == n_randow_x and j == n_randow_y:
                matriz[i][j] = 1
    return matriz

def pedir_coordenadas(matriz, ubicacion_tesoro, vidas):
    while vidas > 0:
        try:
            fila = int(input("Ingrese la fila (0 a {}): ".format(len(matriz) - 1)))
            columna = int(input("Ingrese la columna (0 a {}): ".format(len(matriz) - 1)))

            if fila < 0 or fila >= len(matriz) or columna < 0 or columna >= len(matriz):
                print("Coordenadas fuera de rango. Intente nuevamente.")
                continue

            if ubicacion_tesoro[fila][columna] == 1:
                print("¡Felicidades! Has encontrado el tesoro.")
                break
            else:
                print("No has encontrado el tesoro. Te quedan {} vidas.".format(vidas - 1))
                vidas -= 1
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")

    if vidas == 0:
        print("Has perdido todas tus vidas. El juego ha terminado.")

def main():
    print("Juego del tesoro")
    n = generar_numero_randow()
    mapa = generar_mapa_matriz(n)
    EjeXTesoro = generar_numero_randow()
    EjeYTesoro = generar_numero_randow()
    ubicacion_tesoro = ubicar_tesoro(mapa, EjeXTesoro, EjeYTesoro)

    vidas = 4
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            print(mapa[i][j], end=" ")
        print()
    print("Eje X tesoro: ", EjeXTesoro)
    print("Eje Y tesoro: ", EjeYTesoro)
    pedir_coordenadas(mapa, ubicacion_tesoro, vidas)

main()