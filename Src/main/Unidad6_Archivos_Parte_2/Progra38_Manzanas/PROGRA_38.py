import manzanas

def buscar_por_fecha(ruta_archivo: str) -> None:
    try:
        mes = int(input("Ingrese el mes (1-12): "))
        dia = int(input("Ingrese el día (1-31): "))
        if not (1 <= mes <= 12) or not (1 <= dia <= 31):
            raise ValueError("Mes o día fuera de rango.")
        try:
            cosecha_archivo = open(ruta_archivo, "r", encoding="utf-8")
        except FileNotFoundError:
            print("Error al abrir el archivo.")
            return
        contador_registro: int = 0
        for cosecha in cosecha_archivo:
            peso, id_arbol, mes, dia = cosecha.strip().split(",")
            if int(mes) == mes and int(dia) == dia:
                print(f"Registro encontrado: Peso: {peso}g, ID Árbol: {id_arbol}, Mes: {mes}, Día: {dia}")
                contador_registro += 1
        if contador_registro == 0:
            print("No se encontraron registros para la fecha especificada.")
            return
    except ValueError, TypeError:
        print("Entrada inválida.")
        return

def mostrar_matriz_cosecha(ruta_archivo: str) -> None:
    matriz_cosecha = {}
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        for cosecha in archivo:
            peso, id_arbol, mes = cosecha.strip().split(",")
            if mes not in matriz_cosecha:
                matriz_cosecha[mes] = {}
            if id_arbol not in matriz_cosecha[mes]:
                matriz_cosecha[mes][id_arbol] = 0
            matriz_cosecha[mes][id_arbol] += int(peso)
    except FileNotFoundError:
        print("Error al abrir el archivo.")
        return

def encontrar_manzana_mas_pesada(ruta_archivo: str) -> None:
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
        manzana_mas_pesada : tuple = None
        peso_maximo : float = 0
        for cosecha in archivo:
            peso, id_arbol, mes, dia = cosecha.strip().split(",")
            if int(peso) > peso_maximo:
                peso_maximo = int(peso)
                manzana_mas_pesada = (peso, id_arbol, mes, dia)
        if manzana_mas_pesada is not None:
            print(f"La manzana más pesada es: Peso: {manzana_mas_pesada[0]}g, ID Árbol: {manzana_mas_pesada[1]}, Mes: {manzana_mas_pesada[2]}, Día: {manzana_mas_pesada[3]}")
    except FileNotFoundError:
        print("Error al abrir el archivo.")
    return