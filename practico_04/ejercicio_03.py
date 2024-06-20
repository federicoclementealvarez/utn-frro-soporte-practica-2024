"""Base de Datos SQL - Baja"""

import sqlite3
import datetime

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM Persona WHERE IdPersona = ?", (id_persona,))
    rows_affected = c.rowcount
    conn.commit()
    conn.close()
    return rows_affected > 0
    
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
