'''
PROG_25: Se nos ha solicitado crear un programa que mediante el uso de
un conjunto de tuplas podamos identificar la posición unas oficinas en
un mapa. El usuario podrá ingresar una nueva oficina cuyos valores son
ingresados por teclado como coordenada X e Y. Se almacenarán como una
tupla dentro del conjunto. Se deberá validar que no está dentro del
conjunto y de ser así se avisará al usuario que ese local ya fue
ingresado. Luego, mediante una función se avisará al usuario cuántas
oficinas se encuentran en la región norte, cuántas en la región este
cuántas en la región oeste, y cuántas en la región sur; para ello, tener
en cuenta que las coordenadas, cuando son ingresadas, son números
enteros naturales que van del 0 al 100. La coordenada X=50, y = 50 es
el punto que divide norte de sur y este de oeste.
'''

# 1. Crear una matrix, de conjuntos, de 10 x 10, que representará el mapa de oficinas. (todas estan libres)
# 2. Simulamos algunas, coordenadas de oficinas ya existentes, para que el usuario pueda ver que hay oficinas en el mapa.
# 3. Se muestra el mapa actual.
# 4. Se le pide al user ingresar coordenadas, x e y, que sera una tupla.
# 5. Se comprueba que esa coordenada no este en el conjunto. 
# 6. Si es valida, avisar la orientancion cartografica de la oficina. Norte, sur, este y oeste. 
# 7. Se le devuelve al usuario el mapa actualizado más un conteo por region de cuantas oficinas hay en cada una de las cuatro regiones.

def generar_mapa():
    matriz = []
    for i in range(10):
        fila = [] 
        for j in range(10):
            fila.append(set())
        matriz.append(fila)
    return matriz

def imprimir_mapa(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j]:
                print(f"[{i},{j}]", end="")
            else:
                print("[   ]", end="")

def agregar_oficinas(mapa, oficinas):
    for i in range(10): # Este recorrera las filas
        for j in range(10): # Este recorrera las "columnas"
            for oficina in oficinas:
                if oficina[0] == i and oficina[1] == j:
                    mapa[i][j].add(oficina)

def pedir_coordenadas():
    salir = False
    while salir == False:
        x = int(input("Ingrese la coordenada X: (-1 para salir) "))
        if x == -1:
            salir = True
        else:
            y = int(input("Ingrese la coordenada Y: "))
        return (verificar_coordenadas(x, y))

def verificar_coordenadas(x, y):
    try:
        if x < 0 or x > 9 or y < 0 or y > 9:
            return False
        return True
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        return False
    except TypeError:
        print("Error: Ingrese un número entero válido.")
        return False
    finally:
        print("Verificación de coordenadas completada.")

    '''if x < 0 or x > 9 or y < 0 or y > 9:
        print("Coordenadas fuera de rango. Deben estar entre 0 y 9.")
        return False
    return True'''

def vef_exists_oficina(mapa, coordenadas):
    x, y = coordenadas
    if (x, y) in mapa[x][y]:
        return True
    return False

def contar_oficinas_por_region(mapa):
    # Usaremos el punto (5, 5) como referencia para dividir las regiones
    # Lo que podriamos hacer es tomar, los valores x e y de cada uno de los conjunto, y ver el siguiente patron:
    # Norte = y < 4 (comienza en 0 => 4 = 5)
    # Sur   = y > 4 (comienza en 5 => 9)
    # Este  = x > 4 
    # Oeste = x < 4 
    norte = 0
    sur = 0
    este = 0
    oeste = 0
    for filas in range(len(mapa)):
        for columnas in range(len(mapa[filas])):
            for oficina in mapa[filas][columnas]:
                if oficina == 0:
                    continue
                x, y = oficina
                if y < 5:
                    norte += 1
                else:
                    sur += 1
                if x < 5:
                    oeste += 1
                else:
                    este += 1

    print(f"Oficinas en la región Norte: {norte}")
    print(f"Oficinas en la región Sur: {sur}")
    print(f"Oficinas en la región Este: {este}")
    print(f"Oficinas en la región Oeste: {oeste}")

def main():
    print("Mapeando oficinas")
    # Primero: generamos el mapa, osea un matrix de conjuntos de 100 x 100
    mapa = generar_mapa()
    imprimir_mapa(mapa) # Se imprime correcto :)
    print("Simulacion de oficinas precargadas:")
    # Creada, la matriz, simulamos algunas coordenadas como oficinas ya creadas.
    simulacion_oficinas = [(4,4)] # Esto es Norte - Oeste
    agregar_oficinas(mapa, simulacion_oficinas)
    imprimir_mapa(mapa)

    # Pedimos las coordenadas al usuario
    coordenadas = pedir_coordenadas()
    # Verificamos que las coordenadas ingresadas no esten en el conjunto de oficinas
    verif_existe_oficinas = vef_exists_oficina(mapa, coordenadas)
    if verif_existe_oficinas == True:
        print("La oficina ya existe en el mapa.")
        pedir_coordenadas()
    else:
        # Agregamos la oficina al mapa
        agregar_oficinas(mapa, [coordenadas])
        imprimir_mapa(mapa)
        # Contamos cuantas oficinas hay en cada region
        contar_oficinas_por_region(mapa)

    pedir_coordenadas()
    exit()

main()