import sqlite3 as ora

def create_database():
    """Crea la base de datos del equipo Dream Team"""
    connection = ora.connect("data/Dream_Team.db")
    connection.commit()
    connection.close()

def createTable():
    """Crea la tabla jugadores del equipo dream team"""
    try:
        create_database()
    except FileExistsError as error:
        print(error)
    connection = ora.connect("data/Dream_Team.db")
    cursor = connection.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS jugadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT NULL,
        nombre TEXT,
        posicion TEXT,
        temporadas TEXT
        );'''
    )
    connection.commit()
    connection.close()

def insertRow(instruccion, parametro):
    """Inserta datos a la base de datos

    Args:
        instruccion (_type_): Debemos indicar una instruccion
        parametro (_type_): debemos indicar uno o varios parametros
    """
    connection = ora.connect("data/Dream_Team.db")
    cursor = connection.cursor()
    cursor.execute(instruccion, parametro.split(','))
    connection.commit()
    connection.close()

def readRows():
    """Imprime los datos de la base de datos"""
    connection = ora.connect("data/Dream_Team.db")
    cursor = connection.cursor()
    instruccion = "SELECT * FROM jugadores;"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    connection.commit()
    connection.close()
    print(datos)