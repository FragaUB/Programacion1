'''
PROG_44: Conteo regresivo 
Consigna: Escribir una función recursiva cuenta_regresiva(n) que imprima 
los números desde n hasta 1 y al final muestre en pantalla "¡Despegue!". 
Pista: Pensá cuál es la condición que hace que el conteo se detenga 
(caso base). En este ejercicio la función no necesita devolver ningún 
valor con return al final, solo debe imprimir y llamar a la función con 
el número anterior. 
Casos de prueba:
'''

def cuenta_regresiva(n):
    if n == 1:
        print(n)
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n - 1)

def main():
    cuenta_regresiva(5)

main()