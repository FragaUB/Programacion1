'''
PROG_23: Un crear un programa que utilizando que, utilizando dos
conjuntos, uno para números impares y otro para números pares, permita
al usuario:
- Ingresar un número a uno de estos conjuntos (se deberá validar
mediante función si el número ingresado debe ir al conjunto par o
al conjunto impar; dado que solo se permiten números enteros
naturales utilizar la función de validar número del template)
- Crear una función que pueda ser llamada por la opción dos del menú
y que verifique si un número se encuentra en el conjunto par. El
número será ingresado por el usuario utilizando como validación
la función de validar número
- Ingresando un valor numérico al igual que en el caso anterior, se
informará al usuario si el número se encuentra en el conjunto
impar.
'''

def verificar_par(n, cp, ci):
    if n in cp: 
        return True 
    return False

def verificar_impar(n, cp, ci):
    if n in ci: 
        return True 
    return False
    

def agregar_conjunto(n, Conjunto_Par, Conjunto_Impar):
    if n % 2 == 0:
        Conjunto_Par.add(n)
    else:
        Conjunto_Impar.add(n)

def validar_numero(numero):
    if type(numero) == int and numero >= 0: 
        return True 
    return False

def main():
    Conjunto_Par = {2, 4, 6, 8, 10, 12}
    Conjunto_Impar = {1, 3, 5, 7, 11}
    s = True
    while s:
        numero = int(input("Ingrese un numero: (s para salir)"))
        validar_numero = validar_numero(numero)
        if validar_numero == True:
            # Chekeamos que no este ese numero:
            if(verificar_par(numero, Conjunto_Par, Conjunto_Impar)):
                agregar_conjunto(numero, Conjunto_Par, Conjunto_Impar)
            elif (verificar_impar(numero, Conjunto_Par, Conjunto_Impar)):
                agregar_conjunto(numero, Conjunto_Par, Conjunto_Impar)
        else:
            print("Ingrese un numero!")
            continue

main()