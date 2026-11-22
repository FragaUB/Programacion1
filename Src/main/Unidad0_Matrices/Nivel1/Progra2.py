'''2. La Equis (matriz_equis)
Escribe la función matriz_equis(n) que coloque 1 en las celdas que
pertenecen a la diagonal principal (i = j) o a la diagonal secundaria
(i + j = N − 1), y 0 en el resto.'''

def generar_matriz_cuadrada(n):
    Matriz = []
    for i in range(n):
        Fila = []
        for j in range(n):
            Fila.append(1)
        Matriz.append(Fila)
    return Matriz

def generar_matriz_x(matriz, n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
            
    return matriz

def main():
    # Para ser matriz X, si o si tiene que ser numero impar (porque comienza desde 0)
    matriz = generar_matriz_cuadrada(5)
    for i in range(len(matriz)):
        print(matriz[i])

    resultado = generar_matriz_x(matriz, 5)
    print("Matriz con X:")
    for i in range(len(resultado)):
        print(resultado[i])

main()