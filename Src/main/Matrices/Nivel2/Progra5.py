'''
5. Tablero de Ajedrez Secuencial (matriz_tablero)
Escribe la función matriz_tablero(n) que coloque una secuencia numérica
creciente solo en las posiciones donde (i + j) sea par. Las celdas impares
deben quedar en 0.
'''

def generar_matriz_tablero(n):
    Matriz = []
    Count = 1
    for i in range(n):
        fila = []
        for j in range(n):
            if (i + j) % 2 != 0:
                fila.append(0)
            else:
                fila.append(Count)
                Count += 1
        Matriz.append(fila)
    return Matriz

def main():
    matriz = generar_matriz_tablero(3)
    for i in range(len(matriz)):
        print(matriz[i])
main()