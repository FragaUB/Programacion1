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

def simular_ordeñe(cantidad_vacas: int, turno: str) -> list[dict]:
    import random
    ordeñes = []
    for vaca_id in range(1, cantidad_vacas + 1):
        litros = round(random.uniform(8.0, 25.0), 2)
        temperatura_tanque = round(random.uniform(3.0, 7.0), 2)
        ordeñe = {
            "vaca_id": vaca_id,
            "litros": litros,
            "temperatura_tanque": temperatura_tanque,
            "turno": turno
        }
        ordeñes.append(ordeñe)
    crear_archivo_ordeñe(ordeñe)
    return ordeñes

def crear_archivo_ordeñe(ordeñe: dict) -> None:
    import csv
    with open("ordene.csv", mode="a", newline="") as archivo:
        campos = ["vaca_id", "litros", "temperatura_tanque", "turno"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        if archivo.tell() == 0:
            escritor.writeheader()
        escritor.writerow(ordeñe)

def filtrar_alertas_cadena_frio(ordeñes: list[dict], temp_limite: float = 4.5) -> list[dict]:
    alertas = [ordeñe for ordeñe in ordeñes if ordeñe["temperatura_tanque"] > temp_limite]
    return alertas

def calcular_promedio_litros(ordeñes: list[dict]) -> float:
    if not ordeñes:
        return 0.0
    total_litros = sum(ordeñe["litros"] for ordeñe in ordeñes)
    promedio = total_litros / len(ordeñes)
    return round(promedio, 2)