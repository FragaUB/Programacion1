'''
PROG_50: Suma de los dígitos de un entero 
Consigna: Escribir una función suma_digitos(n) que reciba un número 
entero positivo y devuelva la suma de cada uno de sus dígitos. 
Pista: Para descomponer el número sin convertirlo a texto, utilizá 
operadores de división entera: 
o El operador resto (n % 10) te da el último dígito. 
o El operador división entera (n // 10) te da el número sin 
el último dígito. 
o Tu caso base es cuando el número es menor a 10 (ya tiene un 
solo dígito).'''


def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

print(suma_digitos(123))