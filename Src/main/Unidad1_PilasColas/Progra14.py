'''
PROG_14: Un centro de logística recibe productos desde la línea de
producción. Algunos productos están en óptimo estado y otros presentan
fallas ("roto"). El sistema cuenta con dos camiones de transporte (Pila
Camión Sano y Pila Camión Defectuoso). Funciones a desarrollar:
- clasificar_productos(pila_recepcion,camion_envio, defectuosos):
o Entrada: Una Pila de recepción con tuplas del tipo
(id_producto, estado).
o Proceso: Vacía la pila de recepción desapilando elemento
por elemento. Si el producto tiene estado "roto" o
"defectuoso", lo apila en defectuosos. En caso contrario,
lo apila en camion_envio.
o Retorno: Un resumen con la cantidad total de productos
clasificados.
'''

def clasificar_productos(pila_recepcion, camion_envio, defectuosos):
    while pila_recepcion:
        producto = pila_recepcion.pop()
        id_producto, estado = producto

        if estado.lower() in ["roto", "defectuoso"]:
            defectuosos.append(producto)
        else:
            camion_envio.append(producto)

    resumen = {
        "total_clasificados": len(camion_envio) + len(defectuosos),
        "total_sanos": len(camion_envio),
        "total_defectuosos": len(defectuosos)
    }
    return resumen
