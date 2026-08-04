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

'''PROG_11: Escribir una función que utilizando que reciba una pila de enteros y retorne dos pilas una con los números pares y otra con los impares.'''

def separar_pares_impares(pila):
    pila_pares = []
    pila_impares = []

    while (pila.size() > 0):
        numero = pila.pop()
        if numero % 2 == 0:
            pila_pares.append(numero)
        else:
            pila_impares.append(numero)

    return pila_pares, pila_impares

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
        while pila_ordenada and pila_ordenada[-1] > libro_actual:
            # Desapilar de la pila ordenada y apilarlo de nuevo en la pila original.
            pila_origen.append(pila_ordenada.pop())

        # Apilar el libro actual en la pila ordenada.
        pila_ordenada.append(libro_actual)

    return pila_ordenada

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


'''
PROG_14: Un centro de logística recibe productos desde la línea de
producción. Algunos productos están en óptimo estado y otros presentan
fallas ("roto"). El sistema cuenta con dos camiones de transporte (Pila
Camión Sano y Pila Camión Defectuoso). Funciones a desarrollar:
- clasificar_productos(pila_recepcion,camion_envio, defectuosos):
o Entrada: Una Pila de recepción con tuplas del tipo
(id_producto, estado).
o Proceso: Vacía la pila de recepción desapilando elemento
por elemento. Si el producto tiene estado "roto" o
"defectuoso", lo apila en defectuosos. En caso contrario,
lo apila en camion_envio.
o Retorno: Un resumen con la cantidad total de productos
clasificados.
'''

def clasificar_productos(pila_recepcion, camion_envio, defectuosos):
    while pila_recepcion:
        producto = pila_recepcion.pop()
        id_producto, estado = producto

        if estado.lower() in ["roto", "defectuoso"]:
            defectuosos.append(producto)
        else:
            camion_envio.append(producto)

    resumen = {
        "total_clasificados": len(camion_envio) + len(defectuosos),
        "total_sanos": len(camion_envio),
        "total_defectuosos": len(defectuosos)
    }
    return resumen


'''
PROG_15: Un tren de mercancías está compuesto por una lista de vagones.
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

####################################################################