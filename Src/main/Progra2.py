# Ejercicios de Colas
# Ejercicio Sistema de salud:

def cargar_paciente(id, name, surname, priority):
    print("Cargando pacientes...")
    # Se crea un nuevo objecto "paciente" y se le agrega a la ultima posicion de la lista
    id_new = 5
    name_new = "Pepe"
    surname_new = "Austral"
    priority_new = 1  # 0 = prioridad baja, 1 = prioridad alta

    id.append(id_new) 
    name.append(name_new) 
    surname.append(surname_new) 
    priority.append(priority_new)

    print(f"Paciente {name_new} {surname_new} cargado con éxito.")
    # Llamada a la función para ordenar pacientes por prioridad
    ordernar_pacientes(id, name, surname, priority)
    mostrar_lista_pacientes(id, name, surname)

def ordernar_pacientes(id, name, surname, priority):
    id_aux = []
    name_aux = []
    surname_aux = []
    priority_aux = []
    # Agarramos sincronicamente las cuatros listas, dentro de un bucle for, y vamos preguntando, si alguno tiene prioridad, si hay uno con prioridad, al crear una lista auxiliar, vamos a almacenar momentanemanete los pacientes sin prioridad, y intercambiamos la posicion del paciente con prioridad, y luego volvemos a agregar los pacientes sin prioridad a la lista original.
    for i in range(len(priority)):
        if priority[i] == 1:
            id_aux.append(id[i]) 
            name_aux.append(name[i]) 
            surname_aux.append(surname[i]) 
            priority_aux.append(priority[i])

    # Almacenamos los pacientes sin prioridad en las listas auxiliares
    for j in range(len(priority)):
        if j != i: # para todos aquellos pacientes cuya prioridad sea 0:
            id_aux.append(id[j])
            name_aux.append(name[j])
            surname_aux.append(surname[j])
            priority_aux.append(priority[j])

    # En este momemnto, la lista original tiene un paciente con prioridad en la posicion i, y las listas auxiliares tienen los pacientes sin prioridad.
    id.extend(id_aux) 
    name.extend(name_aux) 
    surname.extend(surname_aux) 
    priority.extend(priority_aux) 
    return True

def mostrar_lista_pacientes(id, name, surname):
    print("Lista de pacientes:")
    for i in range(len(id)):
        print(f"Posicion {i}: ID: {id[i]}, Nombre: {name[i]}, Apellido: {surname[i]}")

# Antes de antender a un paciente, siempre se verifica que no haya algun paciente con prioridad en la cola.
def atender_paciente(id, name, surname, priority):
    print ("Llamado al paciente:")
    if id and name and surname:
        paciente_atendido = (id.pop(0), name.pop(0), surname.pop(0), priority.pop(0))
        print(f"Paciente atendido: ID: {paciente_atendido[0]}, Nombre: {paciente_atendido[1]}, Apellido: {paciente_atendido[2]}, Prioridad: {paciente_atendido[3]}")
    else:
        print("No hay pacientes en la lista.")

def main():
    id = [15, 24, 33, 42, 51]
    name = ["Juan", "María", "Pedro", "Ana", "Luis"]
    surname = ["Gómez", "López", "Rodríguez", "Martínez", "Hernández"]
    priority = [0, 1, 1, 0, 1]  # 0 = prioridad baja, 1 = prioridad alta
    cargar_paciente(id, name, surname, priority) # llamada a la función para cargar pacientes
    mostrar_lista_pacientes(id, name, surname) # llamada a la función para mostrar la lista de pacientes
    atender_paciente(id, name, surname, priority) # llamada a la función para atender pacientes

main()






