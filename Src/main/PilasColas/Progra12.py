'''
PROG_12: Un bibliotecario necesita apilar una serie de libros que van
llegando a su escritorio. Por cuestiones de estabilidad física, nunca
se puede colocar un libro de mayor tamaño encima de uno más pequeño.
Escribe un algoritmo que reciba una pila de libros desordenados y,
utilizando únicamente una pila auxiliar, devuelva la pila original
ordenada de tal manera que el libro más grande quede en la base y el
más pequeño en el tope (los libros se pueden representar con un número
que indica su tamaño). Funciones a desarrollar:
- ordenar_pila_libros(pila_origen):
o Entrada: Un lista con los tamaños de los libros (enteros).
o Retorno: Una nueva Pila ordenada donde los tamaños van de
mayor (base) a menor (tope).
o Restricción: Solo se permite utilizar métodos de las pilas
(apilar, desapilar, ver tope)
'''

def ordenar_pila_libros(pila_origen): # Ejemplo: pila_origen = [5, 1, 3, 2, 4]
    # Pila auxiliar.
    pila_ordenada = []
    while pila_origen:
        # Desapilar el libro de la pila original.
        # Sale primero el libro 4
        libro_actual = pila_origen.pop()

        # Mientras la pila ordenada no esté vacía y el libro en la cima sea más grande que el libro actual.
        while len(pila_ordenada) > 0 and pila_ordenada[-1] > libro_actual:
            # Desapilar de la pila ordenada y apilarlo de nuevo en la pila original.
            pila_origen.append(pila_ordenada.pop())

        # Apilar el libro actual en la pila ordenada.
        pila_ordenada.append(libro_actual)

    return pila_ordenada

