'''
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