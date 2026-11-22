'''PROG_11: Escribir una función que utilizando que reciba una pila de enteros y retorne dos pilas una con los números pares y otra con los impares.'''

def separar_pares_impares(pila):
    pila_pares = []
    pila_impares = []

    while (pila.length() > 0):
        numero = pila.pop()
        if numero % 2 == 0:
            pila_pares.append(numero)
        else:
            pila_impares.append(numero)

    return pila_pares, pila_impares


