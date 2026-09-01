def crear_mapa():
    mapa = []
    for i in range(10):
        fila = []
        for j in range(10):
            fila.append("X")
        mapa.append(fila)
    return mapa

def leer_movimientos():
    movimientos = []
    archivo_movimientos = open("movimientos_robot.txt", "r")
    for mov in archivo_movimientos:
        movimiento = mov.strip().lower()
        movimientos.append(movimiento)
    archivo_movimientos.close()
    return movimientos

def actualizar_posicion_robotito(mapa, movimientos):
    x = 0 # Posicion actual del robotito en el mapa x
    y = 0 # Posicion actual del robotito en el mapa y
    mapa[x][y] = "R"
    for mov in movimientos:
        if mov == "arriba":
            mapa[x][y] = "X"
            try:
                if y + 1 < len(mapa):
                    mapa[x][y + 1] = "R"
            except IndexError:
                mapa[x][y] = "X"
            y += 1
        elif mov == "abajo":
            mapa[x][y] = "X"
            try:
                if y - 1 >= 0:
                    mapa[x][y - 1] = "R"
            except IndexError:
                mapa[x][y] = "X"
            y -= 1
        elif mov == "izquierda":
            mapa[x][y] = "X"
            try:
                if x - 1 >= 0:
                    mapa[x - 1][y] = "R"
            except IndexError:
                mapa[x][y] = "X"
            x -= 1
        elif mov == "derecha":
            mapa[x][y] = "X"
            try:
                if x + 1 < len(mapa):
                    mapa[x + 1][y] = "R"
            except IndexError:
                mapa[x][y] = "X"
            x += 1
    return mapa

def main():
    print("Los pasos de robotito")
    # Primero creamos el mapa de robotito
    mapa = crear_mapa()
    lectura_movimientos = leer_movimientos()
    mapa = actualizar_posicion_robotito(mapa, lectura_movimientos)
    for i in mapa:
        print(i)
if __name__ == "__main__":
    main()