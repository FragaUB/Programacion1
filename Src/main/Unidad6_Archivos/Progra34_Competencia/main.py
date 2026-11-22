def leer_datos_atletas():
    datos_atletas_salieron = []
    datos_atletas_llegaron = []
    datos_archivo_salieron = open("salieron.txt", "r")
    for linea in datos_archivo_salieron:
        datos_atleta = linea.strip().split(",")
        datos_atletas_salieron.append(datos_atleta)
    datos_archivo_salieron.close()

    datos_archivo_llegaron = open("llegaron.txt", "r")
    for linea in datos_archivo_llegaron:
        datos_atleta = linea.strip().split(",")
        datos_atletas_llegaron.append(datos_atleta)
    datos_archivo_llegaron.close()

    return datos_atletas_salieron, datos_atletas_llegaron

def analizar_abandonos(datos_salieron, datos_llegaron):
    atletas_fuera = []
    for atleta_salieron in datos_salieron:
        if atleta_salieron not in datos_llegaron:
            atletas_fuera.append(atleta_salieron)
    return atletas_fuera

def main():
    print("Procesaomiento de competencia de atletismo")
    # Leemos los datos de los atletas y cada uno los almacenamos en una lista.
    datos_salieron, datos_llegaron = leer_datos_atletas()
    # Vemos que atleta salieron pero no llegaron, osea que abandonaron como Boca.
    atletas_fuera = analizar_abandonos(datos_salieron, datos_llegaron)
    for i in atletas_fuera:
        print(f"El atleta {i[0]} con número de dorsal {i[1]} abandonó la competencia.")

if __name__ == "__main__":
    main()