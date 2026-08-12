'''
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
'''


def cargar_paciente(id, name, surname, priority, nuevo_id, nuevo_name, nuevo_surname, nueva_priority):
    print("Cargando pacientes...")
    # Se crea un nuevo paciente y se le agrega a la ultima posicion de la lista
    id.append(nuevo_id)
    name.append(nuevo_name)
    surname.append(nuevo_surname)
    priority.append(nueva_priority)

    print(f"Paciente {nuevo_name} {nuevo_surname} cargado con éxito.")
    # Llamada a la función para ordenar pacientes por prioridad
    ordenar_pacientes(id, name, surname, priority)

def ordenar_pacientes(id, name, surname, priority):
    id_aux = []
    name_aux = []
    surname_aux = []
    priority_aux = []
    for i in range(len(priority)):
        if priority[i] == 1:
            id_aux.append(id[i])
            name_aux.append(name[i])
            surname_aux.append(surname[i])
            priority_aux.append(priority[i])

    for j in range(len(priority)):
        if priority[j] == 0:
            id_aux.append(id[j])
            name_aux.append(name[j])
            surname_aux.append(surname[j])
            priority_aux.append(priority[j])

    id.clear()
    name.clear()
    surname.clear()
    priority.clear()

    # En este momemnto, la lista original tiene un paciente con prioridad en la posicion i, y las listas auxiliares tienen los pacientes sin prioridad.
    id.extend(id_aux) 
    name.extend(name_aux) 
    surname.extend(surname_aux) 
    priority.extend(priority_aux) 
    return True

def mostrar_lista_pacientes(id, name, surname, priority):
    print("Lista de pacientes:")
    for i in range(len(id)):
        print(f"Posicion {i}: ID: {id[i]}, Nombre: {name[i]}, Apellido: {surname[i]}, Prioridad: {priority[i]}")

# Antes de antender a un paciente, siempre se verifica que no haya algun paciente con prioridad en la cola.
def atender_paciente(id, name, surname, priority):
    print("Llamado al paciente:")
    if id:
        paciente_atendido = (id.pop(0), name.pop(0), surname.pop(0), priority.pop(0))
        print(f"Paciente atendido: ID: {paciente_atendido[0]}, Nombre: {paciente_atendido[1]}, Apellido: {paciente_atendido[2]}, Prioridad: {paciente_atendido[3]}")
    else:
        print("No hay pacientes en la lista.")

def main():
    id = [15, 24, 33, 42, 51]
    name = ["Juan", "María", "Pedro", "Ana", "Luis"]
    surname = ["Gómez", "López", "Rodríguez", "Martínez", "Hernández"]
    priority = [0, 1, 1, 0, 1]  # 0 = prioridad baja, 1 = prioridad alta
    cargar_paciente(id, name, surname, priority, 5, "Pepe", "Austral", 1)  # llamada a la función para cargar pacientes
    mostrar_lista_pacientes(id, name, surname, priority)   #llamada a la función para mostrar la lista de pacientes
    atender_paciente(id, name, surname, priority)  # llamada a la función para atender pacientes

main()