'''
PROG_32: Un tambo automatizado requiere un módulo para registrar las
sesiones de ordeñe diarias y monitorear la cadena de frío de la leche
en los tanques de recolección.
1. simular_ordeñe(cantidad_vacas: int, turno: str) -> list[dict]:
Genera una lista de eventos de ordeñe. Cada registro contiene:
o vaca_id: Identificador único (1 a cantidad_vacas).
o litros: Número aleatorio entre 8.0 y 25.0 litros.
o temperatura_tanque: Float aleatorio entre 3.0 °C y 7 °C.
o turno: Cadena indicando 'Mañana' o 'Tarde'.
2. filtrar_alertas_cadena_frio(ordeñes: list[dict], temp_limite:
float = 4.5) -> list[dict]: Retorna una lista con únicamente los
eventos de ordeñe donde la temperatura del tanque superó el límite
de seguridad de conservación.
3. calcular_promedio_litros(ordeñes: list[dict]) -> float: Calcula
la producción promedio de leche por vaca en el ordeñe.
'''

import tambo as tambo_module
import random as rd
import csv
import tambo_file as tambo_file_module

def encontrar_mas_productiva(ordeñes: list[dict]) -> dict:
    top_5_vacas = sorted(ordeñes, key=lambda o: o["litros"], reverse=True)[:5]
    return top_5_vacas

def main() -> None:
    print("Programa de Tambo Automatizado")
    print("Simular Ordeñe")
    turno : tuple = ("Mañana", "Tarde")
    cantidad_vacas : int = 10
    resutlado_ordeñe = tambo_module.simular_ordeñe(cantidad_vacas, turno[rd.randint(0, 1)])
    for i in resutlado_ordeñe:
        print(i)

    alertas = tambo_module.filtrar_alertas_cadena_frio(resutlado_ordeñe)
    for alerta in alertas:
        print(f"Alerta: Vaca ID {alerta['vaca_id']} - Temperatura Tanque: {alerta['temperatura_tanque']} °C")

    promedio = tambo_module.calcular_promedio_litros(resutlado_ordeñe)
    print(f"Promedio de litros por vaca: {promedio}")

    print("PROGRA 39:")
    try:
        with open("ordene.csv", mode="r", newline="") as archivo:
            import csv
            lector = csv.DictReader(archivo)
            ordeñes : list[dict] = [row for row in lector]
            resultados_litros = tambo_file_module.litros_totales_por_turno(ordeñes)
            alertas_frio = tambo_file_module.alertas_cadena_frio(ordeñes)
            control_calidad = tambo_file_module.control_calidad_y_promedio(ordeñes)
            for turno, litros in resultados_litros.items():
                print(f"Litros Totales en {turno}: {litros} litros")
            for alerta in alertas_frio:
                print(f"Alerta de Cadena de Frío: Vaca ID {alerta['vaca_id']} - Temperatura Tanque: {alerta['temperatura_tanque']} °C")
            for turno, datos in control_calidad.items():
                print(f"Turno: {turno} - Porcentaje de Litros Seguros: {datos['porcentaje_seguros']}% - Promedio por Vaca: {datos['promedio_por_vaca']} litros")
    except FileNotFoundError:
        print("El archivo 'ordene.csv' no existe. Por favor, genere los registros de ordeñe primero.")
main()