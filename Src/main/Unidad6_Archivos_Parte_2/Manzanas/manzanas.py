from random import randint

def obtener_dias_mes(mes: int) -> int:
    if mes == 2:
        return 28
    elif mes in (4, 6, 9, 11):
        return 30
    else:
        return 31

def generar_cosecha(cantidad_registros: int) -> list[dict]:
    cosecha = []
    for i in range(cantidad_registros):
        mes = randint(1, 12)
        registro = {
            "peso": randint(100, 600),
            "id_arbol": randint(1, 100),
            "mes": mes,
            "dia": randint(1, obtener_dias_mes(mes))
        }
        cosecha.append(registro)
    return cosecha

def generar_cosecha_csv(path: str, cant_registros: int) -> None:
    cosecha_generada : list[dict] = generar_cosecha(cant_registros)
    try:
        archivo = open(path, "a", encoding="utf-8")
        for registro in cosecha_generada:
            archivo.write(f"{registro['peso']},{registro['id_arbol']},{registro['mes']},{registro['dia']}\n")
        archivo.close()
    except:
        print(f"Error al generar el archivo CSV")

def calcular_totales(cosecha: list[dict]) -> dict:
    peso_total_gramos : float = 0
    for registro in cosecha:
        peso_total_gramos += registro["peso"]

    return {
            'peso_total_kg' : peso_total_gramos / 1000,
            'total_registros' : len(cosecha)
            }