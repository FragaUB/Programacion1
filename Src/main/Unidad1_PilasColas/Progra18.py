'''
PROG_18: El sistema central de la autopista te ha encargado desarrollar
el módulo de control para una estación con 3 cabinas de peaje. Tu
objetivo es procesar la atención de los vehículos fila por fila, cobrando
las tarifas correspondientes y administrando el flujo de autos que van
llegando a la estación. Reglas de la Simulación.
- Estructura del Peaje: El peaje cuenta con 3 colas (cola_1, cola_2,
cola_3). Las 3 colas están agrupadas dentro de una lista principal
llamada peaje.
- Cobro y Tarifas: Cada vez que se atiende (desencolado) a un
vehículo de la cabina elegida, se cobra una tarifa según el tipo:
Moto: $1500, Auto: $2000, Camión: $5000
- Flujo de Arribo (El Turno): Cada vez que se atiende a un vehículo
con éxito, hay un 60% de probabilidad de que ingrese un nuevo
vehículo a la estación. Este nuevo vehículo (Moto, Auto o Camión)
se asignará automáticamente a una de las 3 colas de forma
aleatoria.
- Validación: No se puede atender una cola que esté vacía. Si el
usuario elige una cola vacía, el programa debe mostrar un mensaje
de advertencia y solicitar de nuevo la opción sin perder el turno.
- Se debe mostrar la recaudación total.
'''
from random import randint

def generar_random_vehiculo():
    tipo_vehiculo = randint(1, 3)
    return tipo_vehiculo

def cargar_colas_iniciales(peaje):
    for cola in peaje:
        cant_vehiculos = randint(1, 3)
        for i in range(cant_vehiculos):
            cola.append(generar_random_vehiculo())

def pedir_cabina(peaje):
    while True:
        try:
            opcion = int(input(f"Elegí una cabina para atender (1 a {len(peaje)}): "))
        except ValueError:
            print("Ingresá un número válido.")
            continue

        if opcion < 1 or opcion > len(peaje):
            print("Cabina inexistente. Intentá de nuevo.")
            continue

        return opcion - 1

def atender_cabina(peaje, indice_cola, tarifa_moto, tarifa_auto, tarifa_camion):
    if not peaje[indice_cola]:
        print("La cabina seleccionada está vacía. Elegí otra cabina.")
        return 0
    tarifa = 0.0
    vehiculo_atendido = peaje[indice_cola].pop(0)
    if vehiculo_atendido == 1:
        print(f"{clasificacion_vehiculo(vehiculo_atendido)}. Tarifa: $1500")
        tarifa = tarifa_moto
    elif vehiculo_atendido == 2:
        print(f"{clasificacion_vehiculo(vehiculo_atendido)}. Tarifa: $2000")
        tarifa = tarifa_auto
    elif vehiculo_atendido == 3:
        print(f"{clasificacion_vehiculo(vehiculo_atendido)}. Tarifa: $5000")
        tarifa = tarifa_camion

    return tarifa

def generar_arribo(peaje):
    probabilidad_arribo = randint(1, 100)
    if probabilidad_arribo <= 60:
        nuevo_vehiculo = generar_random_vehiculo()
        indice_cola = randint(0, len(peaje) - 1)
        peaje[indice_cola].append(nuevo_vehiculo)
        print(f"Nuevo vehículo {clasificacion_vehiculo(nuevo_vehiculo)} ha llegado a la cabina {indice_cola + 1}.")
    else:
        print("No hay nuevos vehículos llegando en este turno.")

def clasificacion_vehiculo(i):
    if i == 1:
        return "Moto"
    elif i == 2:
        return "Auto"
    elif i == 3:
        return "Camión"
    else:
        return "Desconocido"

def main():
    print("Sistema de Peaje")
    cola_1 = []
    cola_2 = []
    cola_3 = []
    tarifa_moto = 1500
    tarifa_auto = 2000
    tarifa_camion = 5000
    peaje = [cola_1, cola_2, cola_3]
    recaudacion_total = 0
    salir = True

    while salir:
        cargar_colas_iniciales(peaje)
        indice_cola = pedir_cabina(peaje)
        tarifa_cobrada = atender_cabina(peaje, indice_cola, tarifa_moto, tarifa_auto, tarifa_camion)
        recaudacion_total += tarifa_cobrada

        generar_arribo(peaje)

        continuar = input("¿Atender otro vehículo? (s/n): ").strip().lower()
        if continuar == "s":
            salir = False

    print(f"\nRecaudación total: ${recaudacion_total}")

main()