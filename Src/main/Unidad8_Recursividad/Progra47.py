'''
PROG_47: Sumar elementos de una lista de enteros  
Consigna: Escribir una función suma_lista(lista) que devuelva la suma 
de  todos  los  números  contenidos  en  una  lista  sin  utilizar  bucles 
for/while ni la función sum(). 
Pista: Podés aplicar slicing (rebanado) para achicar la lista. El caso 
base ocurre cuando la lista no tiene elementos (su suma es 0). En el 
paso recursivo, sumá el primer elemento (lista[0]) a la suma del resto 
de la lista (lista[1:]).'''

def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])