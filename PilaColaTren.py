import random

def generar_paquete():
    return random.randint(10, 40)

def cargar_vagon(tren, paquete):
    print("cargando trencito")


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

crear_tren(n = 8)