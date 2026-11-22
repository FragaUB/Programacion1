import random

# =====================================================================
# CÓDIGO PREARMADO PARA EL ALUMNO (NO MODIFICAR)
# =====================================================================

def generar_sonar_6x6():
    """Genera una matriz de 6x6 con un perfil marino aleatorio."""
    matriz = []

    for i in range(6):
        fila = []
        for j in range(6):
            fila.append(0)
        matriz.append(fila)

    for col in range(6):
        inicio_fondo = random.randint(1, 5)

        for f in range(inicio_fondo, 6):
            matriz[f][col] = random.choice([1, 1, 2, 9])

    return matriz


def obtener_simbolo(valor):
    """Convierte el código numérico en su representación visual mediante condicionales simples."""
    if valor == 0:
        return " ~ "
    elif valor == 1:
        return " . "
    elif valor == 2:
        return " # "
    elif valor == 9:
        return " X "
    else:
        return " ? "


def mostrar_sonar(matriz):
    """Muestra el barrido del sonar formateado en consola."""
    print("\n================ BARRIDO DEL SONAR (6x6) ================")
    print("Columnas (Camino) ->   0   1   2   3   4   5")
    print("---------------------------------------------------------")

    for i in range(6):
        linea = ""

        for j in range(6):
            val = matriz[i][j]
            simbolo = obtener_simbolo(val)
            linea = linea + simbolo

        print("Fila " + str(i) + " (Prof) | " + linea)

    print("---------------------------------------------------------")
    print("Simbología: [ ~ Agua ]  [ . Arena ]  [ # Roca ]  [ X Estructura ]\n")


# =====================================================================
# FUNCIÓN A COMPLETAR
# =====================================================================

def evaluar_recorrido_seguro(matriz, columna_destino):
    """
    Evalúa si el barco puede navegar de manera segura desde la columna 0
    hasta la columna_destino.

    Todas las columnas del trayecto deben tener al menos
    2 celdas de agua (0) desde la superficie.
    """

    camino_seguro = True

    for columna in range(columna_destino + 1):

        profundidad = 0

        for fila in range(6):

            if matriz[fila][columna] == 0:
                profundidad += 1
            else:
                break

        if profundidad < 2:
            camino_seguro = False

    return camino_seguro


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================

if __name__ == "__main__":
    navegando = True

    print("⚓ SISTEMA DE NAVEGACIÓN Y CONTROL DE SONAR INICIADO ⚓")

    while navegando:
        mapa_sonar = generar_sonar_6x6()
        mostrar_sonar(mapa_sonar)
        input()

        columna_destino = int(input("Ingrese la columna destino (0-5): "))

        if evaluar_recorrido_seguro(mapa_sonar, columna_destino):
            print("El recorrido es seguro.")
            navegando = False
        else:
            print("El recorrido es peligroso. Virando...")