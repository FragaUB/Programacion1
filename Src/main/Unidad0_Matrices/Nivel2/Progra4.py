'''4. La Serpiente (matriz_serpiente)
Escribe la función matriz_serpiente(n) que llene la matriz de 1 a N
2
fila por fila. Las filas pares (0,2, ...) se llenan de izquierda a derecha,
y las filas impares (1,3, ...) de derecha a izquierda.'''

def generar_matriz_serpiente(n):
    contador = 1
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(contador)
            contador += 1
        if i % 2 == 1: 
            fila.reverse()
        matriz.append(fila)
    return matriz

def main():
    matriz = generar_matriz_serpiente(3)
    for i in range(len(matriz)):
        print(matriz[i])

main()