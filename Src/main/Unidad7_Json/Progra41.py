'''
PROG_41: Implementar  un  sistema  CRUD  para  gestionar  el  archivo 
cosecha.json. 
1.  Crear  (Agregar):  Solicitar  la  clave  única  del  registro  (ej. 
REG_011). Validar que la clave NO exista antes de agregar. Pedir 
datos numéricos validando con try-except (ValueError) y guardar 
en el archivo JSON. 
2.  Leer  (Ver  todos):  Cargar  el  archivo  con  try-except 
(FileNotFoundError) y mostrar los registros en pantalla.
3.  Editar (Actualizar peso): Pedir la clave del registro. Validar 
que la clave SÍ exista. Si existe, solicitar el nuevo peso y 
actualizar el archivo. 
4.  Eliminar: Pedir la clave del registro. Validar que la clave SÍ 
exista, eliminarla del diccionario y guardar los cambios.'''