'''
PROG_46: Potencia de un número (𝑎𝑏) 
Consigna: Escribir una función potencia(base, exponente) que calcule 
𝑏𝑎𝑠𝑒𝑒𝑥𝑝𝑜𝑛𝑒𝑛𝑡𝑒 para exponentes enteros mayores o iguales a 0. No podés 
usar el operador ** ni la función math.pow(). 
Pista: Fijate que la base nunca cambia entre llamadas; lo único que 
se reduce es el exponente. ¿A qué equivale cualquier número elevado 
a la 0? Ese es tu caso base. 
'''

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1) 

print(potencia(2, 3))