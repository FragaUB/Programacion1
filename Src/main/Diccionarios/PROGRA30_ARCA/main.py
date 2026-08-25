import __main__

mapa_satelital = [
['TE', 'TE', 'AV', 'LO', 'LO'],
['LO', 'TE', 'AV', 'TE', 'CH'],
['AV', 'AV', 'AV', 'AV', 'AV'],
['TE', 'LO', 'AV', 'LO', 'TE'],
['TE', 'LO', 'AV', 'TE', 'LO']
]

tarifas_abl = {
'CH': 2000,
'TE': 2500,
'LO': 3500
}

conteo_hogares = {
'CH': 0,
'TE': 0,
'LO': 0,
'AV': 0
}

# TODO 1: Recorrer la matriz mapa_satelital (bucle anidado para filas y celdas)
# e ir incrementando los contadores en conteo_hogares.

def contar_parcelas(mapa_satelite: list[list] ,dic_conteo : dict) -> list[dict]:
    for i in mapa_satelite:
        for j in i:
            if j == 'CH':
                dic_conteo['CH'] += 1
            elif j == 'TE':
                dic_conteo['TE'] += 1
            elif j == 'LO':
                dic_conteo['LO'] += 1
            elif j == 'AV':
                dic_conteo['AV'] += 1
    return dic_conteo 

# TODO 2: Crear el diccionario recaudacion_subtotal calculando (conteo * tarifa)
# para las categorías imponibles ('CH', 'TE', 'LO').

def calcular_recaudacion_x_tarifa(dic_conteo : dict, tarifas_abl : dict) -> dict:
    recaudacion_subtotal = {
        'CH': dic_conteo['CH'] * tarifas_abl['CH'],
        'TE': dic_conteo['TE'] * tarifas_abl['TE'],
        'LO': dic_conteo['LO'] * tarifas_abl['LO'],
    }
    return recaudacion_subtotal

# TODO 3: Mostrar el reporte final:
# - Cantidad de construcciones por tipo
# - Subtotal a cobrar por cada tipo
# - Suma total general recaudada por la zona

def mostrar_datos(mapa_satelital : list[list], dic_conteo : dict, tarifas_abl : dict) -> None:
    cant_parcelas : list[dict] = contar_parcelas(mapa_satelital, dic_conteo)
    cant_recaudado : dict = calcular_recaudacion_x_tarifa(dic_conteo, tarifas_abl)
    for i in cant_parcelas:
        print(f"Cantidad de parcela: {i}, es de {cant_parcelas[i]} ")
    for j in cant_recaudado:
        print(f"Cantidad recaudado por {j}, es de {cant_recaudado[j]}")
    return None

def main ():
    print("Sistema de Impuestos: ExAfip")
    mostrar_datos(mapa_satelital,conteo_hogares,tarifas_abl)
    exit()

if __name__ == '__main__':
    main()