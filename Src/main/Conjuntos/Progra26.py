'''
PROG_26:: Utilizando listas, tuplas y conjuntos, crear un programa que
genere todas las fichas de un dominó. Cada ficha individual será una
tupla contenida dentro de un conjunto que es el total de las fichas.
Crear un método que seleccione aleatoriamente dos fichas, las imprima y
mediante una validación imprima por pantalla si esas dos fichas
“encajan.” Ejemplo: La ficha (1,2) encaja con (3,2) pero no con (3,3).
'''

import random

def generar_fichas(fichas):
    for i in range(7):
        for j in range(i, 7):
            fichas.add((i, j))
    return fichas

def validar_encaje(ficha1, ficha2):
    if ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]:
        return True
    else:
        return False

def main():
    print("Programa de Dominó")
    Jugadas = set()
    generar_fichas(Jugadas)
    print(f"Total de fichas generadas: {len(Jugadas)}")

    ficha1, ficha2 = random.sample(list(Jugadas), 2)
    print(f"Ficha 1: {ficha1}")
    print(f"Ficha 2: {ficha2}")

    if validar_encaje(ficha1, ficha2):
        print("¡Las fichas ENCAJAN!")
    else:
        print("Las fichas NO encajan.")

main()