
PROG_16: Un centro de salud necesita un sistema en consola para gestionar
el turno de atención de los pacientes a medida que van arribando a la
sala de espera. Deberemos implementar una estructura de datos de tipo
Cola (Queue) simulado con listas para gestionar la recepción y atención
de pacientes siguiendo un orden estrictamente secuencial (Primero en
Llegar, Primero en Ser Atendido). Trabajaremos con tres listas
sincronizadas, cada posición es un paciente único. La primer lista
almacena el dni, la segunda el primer nombre y la tercera el apellido.
En el programa debemos generar tres funciones: mostrar_lista_espera (la
cual nos muestra los pacientes en sala de espera pendientes en el orden
en que serán atendidos), cargar_paciente (cargamos un paciente al final
de la cola) y atender_paciente (se anuncia el paciente que será atendido
y se lo elimina de la lista).Importante: si no hay pacientes, no podemos
eliminar de la lista, por lo que debemos validar que haya pacientes para
que no interrumpa el programa.

PROG_17: El centro de salud ha decidido implementar un protocolo de
atención rápida para pacientes prioritarios (embarazadas, personas con
movilidad reducida o adultos mayores). Al programa anterior, le haremos la
siguiente mejora: Al registrar un paciente, el sistema preguntará si se
trata de un caso Prioritario. Comportamiento en la cola:
(dificultad intermedia)
- Si la cola está vacía, el paciente prioritario ingresa
normalmente.
- Si ya hay personas esperando, el paciente prioritario se ubica
inmediatamente en el segundo puesto de la cola (es decir, justo
detrás de la persona que está a punto de ser llamada, respetando
la atención de quien ya estaba esperando al frente).
(dificultad avanzada: opcional)
- Si ingresa un nuevo paciente prioritario y ya hay otro en el
segundo puesto, el nuevo se ubica detrás de los prioritarios
existentes, pero delante de la lista general.
'''

'''
PROG_18: El sistema central de la autopista te ha encargado desarrollar
el módulo de control para una estación con 3 cabinas de peaje. Tu
objetivo es procesar la atención de los vehículos fila por fila, cobrando
las tarifas correspondientes y administrando el flujo de autos que van
llegando a la estación. Reglas de la Simulación.
- Estructura del Peaje: El peaje cuenta con 3 colas (cola_1, cola_2,
cola_3). Las 3 colas están agrupadas dentro de una lista principal
llamada peaje.
Cobro y Tarifas: Cada vez que se atiende (desencolado) a un
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
Se te facilita un código base para comenzar a trabajar
'''

'''
PROG_19: Un minimarket necesita un sistema para administrar la heladera
de lacteos. Para evitar pérdidas por vencimiento, los productos que
ingresan deben gestionarse con lógica de cola. El cajero/repositor puede
vender el producto al frente, comprar stock nuevo o rotar los productos
de la góndola para exponer los que vencen antes. Reglas:
- Listas Sincronizadas: Manejaremos 3 listas donde el mismo índice
representa al mismo producto:
o nombres: Nombre del producto (ej: "Leche", "Yogur").
o dias_vencimiento: Días restantes antes de que venza (un
número entero).
o precios: Precio de venta del producto.
- Acciones del Menú:
1. Vender producto: Se atiende al cliente vendiendo el producto
que está al frente de la cola (índice 0). Se desencola de
las 3 listas, se cobra el precio y transcurre 1 día en el
local (se resta 1 día a la fecha de vencimiento de todos
los demás productos en stock).
2. Comprar / Reponer stock: El usuario ingresa el nombre y
precio de un nuevo producto. El sistema le asigna
automáticamente días de vencimiento aleatorios (entre 15 y
30 días) y lo encola al final.
3. Rotar góndola (Reordenar): Quita el producto del frente
(índice 0) y lo vuelve a encolar al final de las 3 listas.
Esto permite mover un producto que todavía tiene muchos días
por delante para dar paso a otros más urgentes.
4. Salir: Muestra el resumen de ventas.
- Cada vez que transcurre un día (al vender), si el producto del
frente tiene dias_vencimiento <= 0, el sistema no permite
venderlo: debe descartarse automáticamente (desencolarse sin
sumar dinero) avisando al usuario.
