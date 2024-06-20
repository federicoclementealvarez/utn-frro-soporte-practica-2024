"""Base de Datos SQL - Crear y Borrar Tablas"""
import sqlite3

def crear_tabla():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Persona
                (IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
                Nombre CHAR(30),
                FechaNacimiento DATE,
                DNI INTEGER,
                Altura INTEGER)''')
    conn.commit()
    conn.close()

    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """


def borrar_tabla():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS Persona')
    conn.commit()
    conn.close()
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN

crear_tabla()
borrar_tabla()
