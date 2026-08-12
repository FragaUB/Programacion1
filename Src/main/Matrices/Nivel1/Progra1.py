'''
1. El Marco (matriz_marco)
Escribe la función matriz_marco(n) que retorne una matriz con 1 en las
celdas de los bordes exteriores y 0 en el interior.
'''

def generar_matriz_cuadrada(n):
    Matriz = []
    for i in range(n):
        Fila = []
        for j in range(n):
            Fila.append(1)
        Matriz.append(Fila)
    return Matriz

def matriz_marco(matriz, n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0
            
    return matriz

def main():
    matriz = generar_matriz_cuadrada(8)
    for i in range(len(matriz)):
        print(matriz[i])
    resultado = matriz_marco(matriz, 8)
    print("Matriz con marco:")
    for i in range(len(resultado)):
        print(resultado[i])

main()