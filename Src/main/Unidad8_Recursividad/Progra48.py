'''
PROG_48: Invertir una cadena de texto 
Consigna: Escribir una función invertir_cadena(texto) que reciba un 
string y devuelva la cadena invertida. 
Pista: Al igual que con las listas, podés cortar strings con slicing. 
Si el string tiene 0 o 1 carácter, ya está invertido (caso base). Para 
invertirlo  recursivamente,  tomá  el  último  carácter  (texto[-1])  y 
concatenale la inversión del resto de la cadena (texto[:-1]). 
'''

def invertir_cadena(texto):
    if len(texto) <= 1:
        return texto
    else:
        return texto[-1] + invertir_cadena(texto[:-1])

print(invertir_cadena("hola"))