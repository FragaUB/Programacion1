from random import randint

# Jugadores y sus números apostados (cada jugador eligió 6 números)
jugadores = {
"Carlos": {4, 8, 15, 16, 23, 42},
"Ana": {1, 5, 12, 20, 25, 30},
"Beatriz": {4, 12, 18, 23, 33, 40},
"Diego": {7, 14, 21, 28, 35, 39}
}
# 1. Generar los 6 números ganadores del sorteo (sin repetidos)
# TODO: Usar random o un conjunto con un bucle while para obtener 6 números entre 1 y 40.
numeros_sorteados = set()
while len(numeros_sorteados) != 6:
    numeros_sorteados.add(randint(1, 40))
print(f"Números sorteados hoy: {numeros_sorteados}")

cantidadAciertos = 0
aciertos = {}
for i in jugadores:
    cantidadAciertos = len(jugadores[i].intersection(numeros_sorteados))
    print(cantidadAciertos)
    if i not in aciertos:
        aciertos[i] = set()
    aciertos[i].add(cantidadAciertos)
print(aciertos)

curr = next(iter(aciertos))
empates = []
for i in aciertos:
        if(sum(aciertos[curr]) < sum(aciertos[i])):
            curr = i
        elif(sum(aciertos[curr]) == sum(aciertos[i])) and (curr != i):
            empates.append(i)
            empates.append(curr)

if len(empates) > 0:
    if (sum(aciertos(empates[0]))) >= (sum(aciertos[curr])):
        print(f"empate: {empate}")
    else:
        print(f"ganador: curr")
else:
    print(f"Ganador: {curr}")