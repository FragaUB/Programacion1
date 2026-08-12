'''
3. Triángulo Superior Izquierdo (matriz_triangulo_superior_izq)
Escribe la función matriz_triangulo_superior_izq(n) que rellene con 1
toda la región superior izquierda delimitada por la diagonal secundaria
(donde i + j < N) y con 0 el resto.
'''

def generar_matriz_cuadrada(n):
    Matriz = []
    for i in range(n):
        Fila = []
        for j in range(n):
            Fila.append(1)
        Matriz.append(Fila)
    return Matriz

def generar_matriz_triangulo(matriz, n):
    for i in range(n):
        for j in range(n):
            if i + j < n:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0 
    return matriz

def main():
    # Para ser matriz X, si o si tiene que ser numero impar (porque comienza desde 0)
    n = 5
    matriz = generar_matriz_cuadrada(n)
    for i in range(len(matriz)):
        print(matriz[i])
    print()
    matriz = generar_matriz_triangulo(matriz, n)
    for i in range(len(matriz)):
        print(matriz[i])
main()