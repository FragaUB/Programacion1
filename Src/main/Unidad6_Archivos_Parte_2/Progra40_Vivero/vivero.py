def guardar_catalogo_inicial_csv(ruta_archivo: str = "vivero.csv") -> None:
    """Crea el archivo inicial del vivero con el encabezado y plantas base."""
    plantas_base = [
        "1,Albahaca,1200.0,3,2\n",
        "2,Menta,1500.0,1,2\n",
        "3,Lavanda,2800.0,5,4\n",
        "4,Romero,2100.0,2,5\n",
        "5,Manzanilla,1100.0,4,3\n"
        ]
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write("id,nombre,precio,dias_sin_regar,frecuencia_riego_dias\n")
        for p in plantas_base:
            f.write(p)
        print(f"[vivero.py] Catálogo inicial guardado en '{ruta_archivo}'.\n")
    except Exception as e:
        print(f"Error al generar el catálogo: {e}")