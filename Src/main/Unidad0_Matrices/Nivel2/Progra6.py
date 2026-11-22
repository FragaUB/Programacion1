'''
6. Diagonales Crecientes (matriz_diagonales)
Escribe la función matriz_diagonales(n) que rellene la matriz con
números consecutivos del 1 al N
2 avanzando diagonal por diagonal,
desde la esquina superior izquierda hacia la inferior derecha.
'''

def generar_matriz_diagonales(n):
    matriz = [[0] * n for _ in range(n)]
    contador = 1
    for suma in range(2 * n - 1):
        for i in range(n):
            j = suma - i
            if 0 <= j < n:
                matriz[i][j] = contador
                contador += 1
    return matriz

def main():
    matriz = generar_matriz_diagonales(3)
    for fila in matriz:
        print(fila)

main()