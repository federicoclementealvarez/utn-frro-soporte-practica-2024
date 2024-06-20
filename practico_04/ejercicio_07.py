"""Base de Datos SQL - Uso de múltiples tablas"""

import sqlite3
import datetime

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Check if the persona exists
    c.execute("SELECT IdPersona FROM Persona WHERE IdPersona = ?", (id_persona,))
    persona = c.fetchone()
    if not persona:
        conn.close()
        return False

    # Check if there is no registro posterior a la fecha ingresada
    c.execute("SELECT IdPersona FROM PersonaPeso WHERE IdPersona = ? AND Fecha > ?", (id_persona, fecha))
    registro = c.fetchone()
    if registro:
        conn.close()
        return False

    # Insert the peso record
    c.execute("INSERT INTO PersonaPeso (IdPersona, Fecha, Peso) VALUES (?, ?, ?)", (id_persona, fecha, peso))
    conn.commit()
    id_peso = c.lastrowid
    conn.close()
    return id_peso
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""

    pass # Completar


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
