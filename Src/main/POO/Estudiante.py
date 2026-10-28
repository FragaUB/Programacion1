class Estudiante:
    def __init__(self, _dni, _nombre, _apellido, _edad, _ficho) -> None:
        self.dni = _dni
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad
        self.ficho = _ficho

    def __str__(self):
        return f"{self.dni} + {self.nombre} + {self.apellido} + {self.edad} + {self.ficho}"

    def fichar(self, _estado_nuevo):
        if self.ficho != _estado_nuevo:
            self.ficho = _estado_nuevo
            print("Asistencia registrada!")
        else:
            print("El estado de asistencia no cambió.")


class Curso:
    def __init__(self, _list_estudiante, _identificacion, _carrera, _capacidad) -> None:
        self.list_estudiante = _list_estudiante
        self.identificacion = _identificacion
        self.carrera = _carrera
        self.capacidad = _capacidad

    def __str__(self):
        return f"{self.list_estudiante} + {self.identificacion} + {self.carrera} + {self.capacidad}"

    def agregar_estudiante(self, _estudiante_nuevo):
        if self.capacidad < len(self.list_estudiante):
            self.list_estudiante.append(_estudiante_nuevo)
            print(
                f"Estudiante agregado al curso {self.identificacion}, "
                f"carrera {self.carrera}"
            )
        else:
            print("El curso alcanzó su capacidad máxima.")

class Main:
    def main():
        print("Ejercicio Estudiante")
        list_estudiantes = []
        estudiante = Estudiante("48039813", "Pepe", "Argento", "20", 0)
        list_estudiantes.append(estudiante)
        print(f"Informacion del estudiante: {estudiante}")
        curso = Curso(list_estudiantes, "TM01", "Arquitectura", 150)
        print(f"Informacion del curso: {curso}")
        estudiante_nuevo = Estudiante(
            "40111222", "Moni", "Argento", 19, 0
        )
        curso.agregar_estudiante(estudiante_nuevo)
        print(f"Información del curso: {curso}")

Main.main()
