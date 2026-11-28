'''
PROG_39: El módulo tambo.py genera el registro diario de ordeñe
(ordene.csv), dividiendo la producción en dos turnos: Mañana (primera
mitad de las vacas) y Tarde (segunda mitad de las vacas). Escribir un
programa interactivo en main.py que permita analizar:
1. Litros Totales por Turno: Calcular e informar la cantidad de
litros recolectados en la Mañana y en la Tarde.
2. Alertas de Cadena de Frío: Mostrar por pantalla todas las vacas y
registros cuya temperatura de tanque haya superado los 4.5 °C.
3. Control de Calidad y Producción Promedio por Vaca:
o Calcular el porcentaje de litros seguros (temperatura ≤
4.5 °C) sobre el total por cada turno.
o Calcular el promedio de litros producidos por vaca en cada
turno.
'''

def litros_totales_por_turno(ordeñes: list[dict]) -> dict:
    total_mañana = sum(float(ordeñe["litros"]) for ordeñe in ordeñes if ordeñe["turno"] == "Mañana")
    total_tarde = sum(float(ordeñe["litros"]) for ordeñe in ordeñes if ordeñe["turno"] == "Tarde")
    return {"Mañana": round(total_mañana, 2), "Tarde": round(total_tarde, 2)}

def alertas_cadena_frio(ordeñes: list[dict], temp_limite: float = 4.5) -> list[dict]:
    alertas = [ordeñe for ordeñe in ordeñes if float(ordeñe["temperatura_tanque"]) > temp_limite]
    return alertas

def control_calidad_y_promedio(ordeñes: list[dict], temp_limite: float = 4.5) -> dict:
    turnos = ["Mañana", "Tarde"]
    resultados = {}
    for turno in turnos:
        ordeñes_turno = [ordeñe for ordeñe in ordeñes if ordeñe["turno"] == turno]
        total_litros = sum(float(ordeñe["litros"]) for ordeñe in ordeñes_turno)
        litros_seguros = sum(float(ordeñe["litros"]) for ordeñe in ordeñes_turno if float(ordeñe["temperatura_tanque"]) <= temp_limite)
        porcentaje_seguros = (litros_seguros / total_litros * 100) if total_litros > 0 else 0.0
        promedio_por_vaca = (total_litros / len(ordeñes_turno)) if ordeñes_turno else 0.0
        resultados[turno] = {
            "porcentaje_seguros": round(porcentaje_seguros, 2),
            "promedio_por_vaca": round(promedio_por_vaca, 2)
        }
    return resultados