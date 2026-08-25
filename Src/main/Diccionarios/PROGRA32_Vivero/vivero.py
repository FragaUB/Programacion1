'''
PROG_33: Un vivero necesita un sistema para administrar el catálogo de
sus plantas aromáticas y ornamentales, permitiendo actualizar precios
por inflación y detectar qué especies requieren riego inmediato.
1. obtener_catalogo_inicial() -> list[dict]: Devuelve una lista base
con al menos 5 plantas. Cada planta se representa como:
    o id: Entero identificador.
    o nombre: Cadena (ej. "Albahaca", "Menta", "Lavanda").
    o precio: Float.
    o dias_sin_regar: Entero.
    o frecuencia_riego_dias: Entero (cada cuántos días debe
    regarse).
    2. aplicar_aumento_precios(catalogo: list[dict], porcentaje: float)
-> list[dict]: Modifica o genera un catálogo actualizado donde el
precio de cada planta se incrementa según el porcentaje indicado.
3. obtener_plantas_para_regar(catalogo: list[dict]) -> list[dict]:
Filtra y retorna las plantas cuyo dias_sin_regar sea igual o mayor
a su frecuencia_riego_dias.
'''

def obtener_catalogo_inicial() -> list[dict]:
    """Retorna el catalogo por defecto de plantas en el vivero."""
    return [
        {
            "id": 1, 
            "nombre": "Albahaca", 
            "precio": 1200.0, 
            "dias_sin_regar": 3,
            "frecuencia_riego_dias": 2
        },
        {
            "id": 2, 
            "nombre": "Menta",
            "precio": 1500.0, 
            "dias_sin_regar": 1,
            "frecuencia_riego_dias": 2
        },
        {
            "id": 3, 
            "nombre": "Lavanda",
            "precio": 2800.0, 
            "dias_sin_regar": 5,
            "frecuencia_riego_dias": 4
        },
        {
            "id": 4, 
            "nombre": "Romero",
            "precio": 2100.0,
            "dias_sin_regar": 2,
            "frecuencia_riego_dias": 5
        },
        {
            "id": 5, 
            "nombre": "Manzanilla", 
            "precio": 1100.0, 
            "dias_sin_regar": 4,
            "frecuencia_riego_dias": 3
        },
    ]

def aplicar_aumento_precios(catalogo: list[dict], porcentaje: float) -> list[dict]:
    for i in catalogo:
        i["precio"] *= 1 + porcentaje / 100
    return catalogo

def obtener_plantas_para_regar(catalogo: list[dict]) -> list[dict]:
    resultados : list = [] 
    for i in catalogo:
        if i["dias_sin_regar"] >= i["frecuencia_riego_dias"]:
            resultados.append(
                {
                    "nombre" : i["nombre"],
                    "dias_sin_regar" : i["dias_sin_regar"],
                    "frecuencia_riego_dias" : i["dias_sin_regar"]
                }
            )
            return resultados  
