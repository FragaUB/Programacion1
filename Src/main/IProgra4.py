'''
PROG_21: Un satélite en órbita necesita enviar fotos a la Tierra, pero
la velocidad de conexión es extremadamente lenta. Para solucionar esto,
el equipo de ingeniería diseñó un algoritmo de dos pasos para reducir
el peso de las imágenes antes de enviarlas:
1. Submuestreo: Reduce el tamaño de la imagen a la mitad recortando
píxeles.
2. Binarización: Simplifica los colores a solo dos tonos (Blanco y
Negro) usando un umbral de brillo. Las imágenes se representan
como matrices de enteros entre 0 (Negro) y 9 (Blanco).
Consignas:
1. La Imagen Original: Crear una matriz de 8 × 8 que represente una
foto en escala de grises. (Podemos usar IA para trabajar con una
imagen prefijada con una forma reconocible, como una carita o un
corazón, o generarla con random.randint(0, 9)).
2. Paso 1 - Reducción de Tamaño (Slicing): Crear una nueva matriz
imagen_reducida de 4 × 4 tomando solo 1 de cada 2 píxeles (las
filas y columnas pares).Requisito: Utilizar slicing con paso 2
(::2) dentro de una lista por comprensión.
3. Paso 2 - Simplificación de Color (Listas por Comprensión con
condición): Generar una matriz imagen_binaria a partir de la
reducida. Si el valor del píxel es mayor o igual a 5, se convierte
en 1 (Luz), de lo contrario en 0 (Sombra). Requisito: Utilizar
una lista por comprensión con expresión if-else.
4. Visualización en Pantalla (Bonus Visual): Muestra la imagen
original y la comprimida en la consola reemplazando los números 0
y 1 por caracteres visuales (por ejemplo, para 0 y para 1,
o " " y "██"). El siguiente código puede ayudar a la
representación:
'''

# Objectivo de una matriz, que represente la imagen, lograr comprimirlo a la mitad de la dimesion de la matriz original

from random import randint

def CrearMatriz(X, Y, Imagen_Original):
    Imagen_Original = [[randint(0, 9) for i in range(Y)] for j in range(X)]
    for i in Imagen_Original:
        print(i)
    return Imagen_Original

def ComprimirImagen(Imagen_Original):
    print("Comprension de imagen original")
    Imagen_Comprimida = []
    Imagen_Comprimida = [fila[::2] for fila in Imagen_Original[::2]]
    print("Imagen Comprimida")
    for fila in Imagen_Comprimida:
        print(fila)
    return Imagen_Comprimida

def ImagenBinaria(Imagen_Comprimida, X, Y):
    Imagen_Binaria = [[1 if pixel >= 5 else 0 for pixel in fila] for fila in Imagen_Comprimida]
    print("Imagen Binaria")
    for fila in Imagen_Binaria:
        print(fila)
    return Imagen_Binaria

def VisualizarImagen(Imagen, X, Y):
    for fila in Imagen:
        print(f"{"".join("██" if pixel == 1 else " " for pixel in fila)}\n")

def main():
    print("Welcome to photo satellite compression")
    X = 8
    Y = 8
    Imagen_Original = []
    Imagen_Original = CrearMatriz(X, Y, Imagen_Original)
    Imagen_Comprimida = ComprimirImagen(Imagen_Original)
    Imagen_Binaria = ImagenBinaria(Imagen_Comprimida, X, Y)
    print("##################################")
    VisualizarImagen(Imagen_Original, X, Y)
    print("##################################")
    VisualizarImagen(Imagen_Binaria, X//2, Y//2)
    print("##################################")
    VisualizarImagen(Imagen_Comprimida, X//2, Y//2)
    print("##################################")

main()
