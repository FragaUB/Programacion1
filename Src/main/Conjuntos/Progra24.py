'''
PROG_24: Tomando como referencia el programa anterior construir un
programa similar que tenga las siguientes características:
- Ingresar números enteros naturales a un primer conjunto llamado
conjunto ‘A’
- Ingresar números en un conjunto ‘B’
- Ver la Unión de los conjuntos A - B
- Ver la intersección de los conjuntos A - B
- Ver la diferencia simétrica y
- Eliminar un elemento del conjunto ‘A’
- Eliminar un elemento del conjunto ‘B’ se debe validar (en 6 y 7)
para la eliminación previamente que el conjunto no esté vacío para
proceder con la eliminación caso contrario se avisará por pantalla
hoy.
'''

def Join(set1, set2):
    return set1.union(set2)

def Intersection(set1, set2):
    return set1.intersection(set2)

def symeticDifference(set1, set2):
    return set1 ^ set2

a = set(input("Ingrese un set de datos (ej:123) sin espacios: "))
b = set(input("Ingrese otro set de datos(ej:345) sin espacios: "))

print(f"Union: {Join(a,b)}")
print(f"Interseccion: {Intersection(a,b)}")
print(f"Diferencia simetrica: {symeticDifference(a,b)}")