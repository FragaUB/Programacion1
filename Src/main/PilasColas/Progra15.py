'''PROG_15: Un tren de mercancías está compuesto por una lista de vagones.
Cada vagón funciona como una pila con una capacidad máxima de peso (en
kg). A medida que llegan paquetes con pesos aleatorios, se deben apilar
en el vagón actual. Cuando el siguiente paquete supere la capacidad
restante del vagón, ese vagón se "sella" y se debe pasar al siguiente
vagón (siguiente pila). Funciones a desarrollar:
1. generar_paquete(peso_min, peso_max): Función que retorna
aleatoriamente el peso de un paquete a cargar. Recomendación: Los
paquetes pesan entre 10 y 40.
2. cargar_vagon(tren, vagón_numero, paquete): Función que retorna la
información del tren una vez terminada la carga del vagón. Recibe
como parámetro la “matriz” (dado que el tren representa la matriz
y cada fila los vagones del tren), la posición actual para la
carga (como recomendación, siempre se puede trabajar con la última
posición dependiendo de como se construya el programa principal)
y una tupla compuesta de información del paquete y el peso. El
vagón tiene un limite de 150.
3. Mostrar(tren): Mostrar informe de carga
'''

from random import randint

def generar_paquete():
    return randint(10, 40)


def crear_tren(n):
    tren  = []
    for i in range(n):
        paquete = generar_paquete()
        tren.append([]) # nuevo vagon
        peso = 0
        while peso < 150:
            paquete = generar_paquete()
            peso += paquete
            if peso < 150:  
                tren[i].append(paquete)
    print(tren)

crear_tren(8)