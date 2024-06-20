"""Base de Datos - ORM"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio

from typing import List, Optional

class DatosSocio():
    def __init__(self, engine):
        self.session_factory = sessionmaker(bind=engine)

    def session(self):
        return self.session_factory()
    
    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        session = self.session()
        try:
            socio = session.query(Socio).filter_by(id_socio=id_socio).one_or_none()
            session.close()
            return socio
        except:
            session.close()
            return None

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        session = self.session()
        try:
            socio = session.query(Socio).filter_by(dni=dni_socio).one_or_none()
            session.close()
            return socio
        except:
            session.close()
            return None

    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        session = self.session()
        try:
            socios = session.query(Socio).all()
            session.close()
            return socios
        except:
            session.close()
            return []

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        session = self.session()
        try:
            session.query(Socio).delete()
            session.commit()
            session.close()
            return True
        except:
            session.close()
            return False

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        session = self.session()
        try:
            session.add(socio)
            session.commit()
            session.close()
            print(socio)    
            return socio
        except:
            session.close()
            raise

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        session = self.session()
        try:
            socio = session.query(Socio).filter_by(id_socio=id_socio).one_or_none()
            if socio:
                session.delete(socio)
                session.commit()
                session.close()
                return True
            else:
                session.close()
                return False
        except:
            session.close()
            return False

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        session = self.session()
        try:
            session.add(socio)
            session.commit()
            session.close()
            return socio
        except:
            session.close()
            raise

    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        session = self.session()
        try:
            total_socios = session.query(Socio).count()
            session.close()
            return total_socios
        except:
            session.close()
            return 0

# NO MODIFICAR - INICIO

# Test Creación
os.remove("test.db")
engine = create_engine("sqlite:///test.db", echo=True)
datos = DatosSocio(engine)

Base.metadata.create_all(engine)

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
session = datos.session()  # Open the session
assert socio.id_socio > 0
session.close()  # Close the session

# Test Baja
session = datos.session()  # Open the session
assert datos.baja(socio.id_socio) == True
session.close()  # Close the session

# Test Consulta
session = datos.session()  # Open the session
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id_socio) == socio_2
session.close()  # Close the session

# Test Buscar DNI
session = datos.session()  # Open the session
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2
session.close()  # Close the session

# Test Modificación
session = datos.session()  # Open the session
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id_socio)
assert socio_3_modificado.id_socio == socio_3.id_socio
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587
session.close()  # Close the session

# Test Conteo
session = datos.session()  # Open the session
assert len(datos.todos()) == 3
session.close()  # Close the session

# Test Delete
session = datos.session()  # Open the session
datos.borrar_todos()
assert len(datos.todos()) == 0
session.close()  # Close the session

