import sqlite3 as sql3

with sql3.connect('/DB_dream_team.db') as conexion:
    try:
        command = '''create table EQUIPO 
        (id integer primary key autoincrement,
        nombre_equipo text,
        jugadores integer)'''
        conexion.execute(command)
        print('Se creo la tabla EQUIPO')
    except sql3.OperationalError:
        print('La tabla EQUIPO ya existe')