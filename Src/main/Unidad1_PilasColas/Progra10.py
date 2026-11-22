# Unidad Pilas y Colas
'''PROG_10: Leer una palabra y verificar si es un palíndromo (se lee igual al derecho que al revés) usando una pila.'''

def es_palindromo(palabra):
    #Ejemplo: Entra 'radar'

    palabra_invertida = ""
    pila = []
    palabra = palabra.lower().replace(" ", "")

    # Por cada caracter en la palabra, apilarlo en la pila
    for char in palabra:
        pila.append(char)
        # pila = ['r', 'a', 'd', 'a', 'r']

    # Mientras pila no sea nulo o este vacio dentra dentro del bucle
    while pila:
        # El primero en salir sera pila[4] = r, luego pila[3] = a, luego pila[2] = d, luego pila[1] = a, y por ultimo pila[0] = r
        # Cuando Pila este vacio sale del bucle.
        palabra_invertida += pila.pop()

    # Retorna True si la palabra es igual a la palabra invertida, de lo contrario retorna False
    return palabra == palabra_invertida

