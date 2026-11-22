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

def verificar_formacion(n: int) -> bool:
    try:
        if n <= 0:
            return False
        return True
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        return False
    except TypeError:
        print("Error: Ingrese un número entero válido.")
        return False
    finally:
        print("Verificación de formación completada.")

if verificar_formacion(8):
    crear_tren(8)
else:
    exit()