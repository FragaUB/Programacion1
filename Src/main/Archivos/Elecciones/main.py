def procesar_elecciones() -> dict:
    # Diccionario inicializado en 0 para cada candidato
    candidatos = {
        "BELGRANO": 0,
        "PUEYRREDON": 0,
        "URQUIZA": 0,
        "ROSAS": 0,
        "SAAVEDRA": 0
    }

    datos_votos = leer_votos()
    for voto in datos_votos:
        if voto in candidatos:
            candidatos[voto] += 1
    return candidatos

def leer_votos() -> list:
    datos_archivo = open("C:\\Users\\franc\\OneDrive\\Documentos\\GitHub\\Programacion1\\Src\\main\\Archivos\\Elecciones\\votos.txt", "r")
    datos_votos = []
    for linea in datos_archivo:
        datos_votos.append(linea.strip())
    datos_archivo.close()
    return datos_votos

def main() -> None:
    print("Bienvenido al sistema de elecciones")
    conteo = procesar_elecciones()
    for candidato, votos in conteo.items():
        print(f"{candidato}: {votos} votos")

if __name__ == "__main__":
    main()