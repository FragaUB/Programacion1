'''
PROG_49: Contar las ocurrencias de un carácter 
Consigna: Escribir una función contar_caracter(texto, c) que devuelva 
cuántas veces aparece el carácter c dentro de texto. 
Pista: Evaluá únicamente el primer carácter de la cadena (texto[0]). Si 
coincide con c, suma 1; si no, suma 0. A ese resultado acumulale el 
llamado recursivo con el resto de la cadena (texto[1:]). '''

def contar_caracter(texto, c):
    contador = 0
    if len(texto) == 0:
        return contador
    else:
        if texto[0] == c:
            contador += 1
        return contador + contar_caracter(texto[1:], c)

print(contar_caracter("hola mundo", "o"))