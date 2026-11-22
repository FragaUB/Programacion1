'''
PROG_13: En la bodega de un avión, las valijas se apilan en dos filas
paralelas (Pila A y Pila B). Cada valija tiene un código de etiqueta
único. Cuando un pasajero reclama una valija por su código, el operario
debe retirarla. Sin embargo, como están apiladas, para sacar una valija
que está abajo, primero se deben desapilar temporalmente las que están
arriba. Función a desarrollar
- buscar_y_extraer_maleta(pila_a, pila_b, etiqueta_buscada):
o Entrada: Dos listas (pila_a y pila_b) y la etiqueta
(string/int) de la maleta buscada.
o Proceso: Busca la maleta en la pila_a. Si no está, busca en
la pila_b. Utiliza una pila auxiliar para guardar
temporalmente las maletas que están encima de la buscada.
Una vez extraída la maleta solicitada, se devuelven las
demás a su pila original en el orden correcto.
o Retorno: True si la maleta fue encontrada y extraída, False
si no existía en ninguna de las dos filas.
'''

def buscar_y_extraer_maleta(pila_a, pila_b, etiqueta_buscada):
    pila_auxiliar = []

    # Buscar en la pila A
    while pila_a:
        maleta = pila_a.pop()
        if maleta == etiqueta_buscada:
            while pila_auxiliar:
                pila_a.append(pila_auxiliar.pop())
            return True
        else:
            pila_auxiliar.append(maleta)

    while pila_b:
        maleta = pila_b.pop()
        if maleta == etiqueta_buscada:
            while pila_auxiliar:
                pila_b.append(pila_auxiliar.pop())
            return True
        else:
            pila_auxiliar.append(maleta)

    while pila_auxiliar:
        if len(pila_a) < len(pila_b):
            pila_a.append(pila_auxiliar.pop())
        else:
            pila_b.append(pila_auxiliar.pop())

    return False

