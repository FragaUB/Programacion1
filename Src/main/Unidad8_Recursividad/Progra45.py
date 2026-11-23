'''
PROG_45: Factorial de n 
Consigna: Escribir una función factorial(n) que calcule el factorial de 
un número entero positivo 𝑛 (𝑛!=𝑛×(𝑛−1)×...×1). 
Pista: Mantené presente la definición matemática: 0!=1 y 1!=1 (tus 
casos base). Para el paso recursivo, recordá que 𝑛!=𝑛×(𝑛−1)!. '''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print(factorial(5))

main()