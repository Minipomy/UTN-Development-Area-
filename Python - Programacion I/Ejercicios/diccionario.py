'''
Crea un diccionario que represente los días de la semana, 
donde las claves son los nombres de los días y los valores 
son los números correspondientes (por ejemplo, {"lunes": 1, "martes": 2, ...}). 

Imprime el valor correspondiente al día "miércoles".
'''
semana = {"Lunes" : 1 ,"Martes" : 2 ,"Miercoles" : 3 ,"Jueves" : 4 ,"Viernes" : 5 ,"Sabado" : 6 ,"Domingo" : 7}
print(semana['Miercoles'])



'''
Crea un diccionario que represente los meses del año, 
donde las claves son los nombres de los meses y los valores 
son sus números correspondientes (por ejemplo, {"enero": 1, "febrero": 2, ...}). 

Imprime el número correspondiente al mes "julio".
'''

diccionario_mes = {"Enero": 1 ,"Febrero": 2 ,"Marzo": 3 ,"Abril": 4 , "Mayo": 5 ,"Junio": 6 ,"Julio": 7 ,"Agosto": 8 , "Septiembre": 9 ,"Octubre": 10 ,"Noviembre": 11 ,"Diciembre": 12}
print(diccionario_mes['Julio'])



'''
Crea un diccionario que contenga la información de una película, 
como título, 
director y 
año de estreno. 

Luego, imprime el título de la película.
'''

diccionario_pelicula = {
    'Titulo' : 'The Matrix',
    'Director' : 'The Wachowskis Brothers',
    'Año' : 1999
}

print(diccionario_pelicula["Titulo"])

'''
Crea un diccionario que contenga la información de una dirección: 
nombre de la calle, 
altura, 
localidad, 
código postal, 
partido y 
provincia. 

Luego, imprime el nombre de la calle, seguido de su altura.
'''

diccionario_direx = {
    'Calle' : 'Belgrano',
    'Altura' : 200,
    'Localidad' : 'Bernal',
    'Codigo_posta' : 1877,
    'Partido' : 'Quilmes',
    'Provincia' : 'Buenos Aires'
}

print(diccionario_direx['Calle'],diccionario_direx['Altura'])

'''
Crea un diccionario que represente los continentes, 
donde las claves son los nombres de los continentes y 
los valores son los números correspondientes 
(por ejemplo, {"América": 1, "Europa": 2, ...}). 

Imprime el valor correspondiente al continente "África".
'''

diccionario_continentes = {'America' : 1 , 'Europa' : 2 , 'Asia' : 3 , 'Africa' : 4 , 'Antartida' : 5 , 'Oceania' : 6}

print(diccionario_continentes['Africa'])

'''
Crea un diccionario que represente las estaciones del año, 
donde las claves son los nombres de las estaciones y 
los valores son los números correspondientes (por ejemplo, 
{"primavera": 1, "verano": 2, ...}). 

Imprime el valor correspondiente a la estación "invierno".
'''

diccionario_estaciones_anio = {'Primavera' : 1 , 'Verano' : 2 , 'Otoño' : 3 , 'Invierno' : 4}
print(diccionario_estaciones_anio['Invierno'])


'''
Crea un diccionario que contenga la información de una canción: 
título, 
artista y 
duración. 

Luego, imprime la duración de la canción.
'''

diccionario_cancion = {'Titulo' : 'Wallmonger' , 'Artista' : 'Virtual Riot', 'Duracion' : '4:09'}
print(diccionario_cancion['Duracion'])


'''
Crea un diccionario que represente las edades de varias personas, 
donde las claves son los nombres de las personas y 
los valores son sus edades. 

Imprime la edad de la persona más joven.
'''

diccionario_edades_personas = {'Maxi' : 26 , 'Brian' : 28 , 'Irina' : 22 , 'Juan' : 18}

for edad in diccionario_edades_personas.values():
    if(edad <= edad_menor):
        edad_menor = edad

print(edad_menor)


'''
Crea un diccionario que contenga las capitales de los países de América del Sur.
Luego, pide al usuario que ingrese el nombre de un país y 
muestra su capital correspondiente.
'''

diccionario_paises = {'Argentina' : 'Buenos Aires' , 'Bolivia' : 'Sucre' , 'Brasil' : 'Brasilia' ,
                'Chile' : 'Santiago de Chile' , 'Colombia' : 'Bogota' , 'Ecuador' : 'Quito', 
                'Paraguay' : 'Asuncion' , 'Peru' : 'Lima' , 'Surinam' : 'Parabarimo' , 
                'Trinidad y Tobago' : 'Puerto España' , 'Uruguay' : 'Montevideo' ,
                'Venezuela' : 'Caracas'}

entrada_pais = input("Por favor, ingresar un pais para conocer su capital\n")
print(diccionario_paises[entrada_pais])


'''
Crea un diccionario que represente las notas de un examen de varios estudiantes, 
donde las claves son los nombres de los estudiantes y 
los valores son sus notas. 

Imprime el promedio de las notas.
'''

diccionario_notas_estudiantes = {'Maxi' : 4 , 'Brian' : 7 , 'Irina' : 5 , 'Juan' : 10}
acumulador_notas = 0
contador_notas = 0

for nota in diccionario_notas_estudiantes.values():
    acumulador_notas += nota
    contador_notas += 1

promedio_notas = acumulador_notas / contador_notas
print(promedio_notas)


'''
Crea un diccionario que represente una lista de tareas por hacer. 
Cada clave del diccionario debe ser el nombre de una tarea y 
cada valor debe ser su estado 
(los estados son:  
pendiente, 
en proceso, 
completada). 

Imprimir todas las tareas seguido de su estado
'''


diccionario_tareas = {'Limpiar' : 'Pendiente' , 'Sacar la Basura' : 'Completada' , 'Cocina' : 'En proceso'}

for tarea in diccionario_tareas:
    print(tarea, diccionario_tareas[tarea])

'''
Crea un diccionario que represente una lista de las compras. 
Cada clave del diccionario debe ser el nombre de un producto y 
cada valor debe ser su cantidad. 

Pedir al usuario que ingrese el nombre del producto e imprimir la cantidad
'''

diccionario_compras = {'Ayudin' : 2 , 'Budin Carrefour' : 5 , 'Fernet' : 10}

producto_ingresado = input("Por favor, ingresar un producto\n")
print(diccionario_compras[producto_ingresado])


'''
Crea un diccionario que contenga el nombre y 
el nivel de dificultad de varios juegos de mesa. 
Luego, pedirle al usuario un nivel de dificultad, 
buscar los que coinciden e 

imprimir sus nombres
'''

diccionario_juegos = {'Monopoly' : 3 , 'Ajedrez' : 10 , 'LIFE' : 1}
dificultad_ingresada = int(input("Por favor, ingresar el nivel de dificultad deseada:\n"))

for juego in diccionario_juegos:
    if(diccionario_juegos[juego] == dificultad_ingresada):
        print(juego)


'''
Crea un diccionario que contenga el nombre como clave y 
el puntaje como valor de varios jugadores en un juego. 
Luego, pedirle al usuario el nombre del jugador y 
nuevo puntaje y 

actualizar el valor correspondiente en el diccionario.
'''

diccionario_puntaje = {'Maxi' : 110 , 'Brian' : 320 , 'Irina' : 0 , 'Juan' : 80}
nombre_ingresado = input("Por favor, ingresar el nombre del jugador:\n")
puntaje_ingresado = input("Por favor, ingresar el puntaje nuevo del jugador:\n")
diccionario_puntaje[nombre_ingresado] = puntaje_ingresado 
print(diccionario_puntaje)


'''
Crea un diccionario que contenga el nombre y 
el sueldo de varios empleados. 
Luego, permite al usuario aumentar el sueldo de un empleado y 
actualizar el valor correspondiente en el diccionario.
'''

diccionario_sueldos_empleados = {'Maxi' : 527000 , 'Brian' : 71000 , 'Irina' : 60000 , 'Juan' : 1999999}
nombre_ingresado = input("Por favor, ingresar el nombre del empleado:\n")
sueldo_ingresado = input("Por favor, ingresar el sueldo actualizado del empleado:\n")
diccionario_sueldos_empleados[nombre_ingresado] = sueldo_ingresado
print(diccionario_sueldos_empleados)


'''
Crea un diccionario que represente una lista de tareas pendientes, 
donde las claves son las tareas y 
los valores son "True" si están completadas y "False" si no lo están. 
Solicita al usuario el nombre de una tarea y 
modifica el valor para marcarla como completada. 

Imprimir el listado de tareas pendientes
'''

diccionario_pendientes = {'Limpiar' : True , 'Cocinar' : False , 'Ordenar' : False}
tarea_ingresada = input("Por favor, ingresar una tarea:\n")
diccionario_pendientes[tarea_ingresada] = not diccionario_pendientes[tarea_ingresada]
print(diccionario_pendientes)


'''
Crea un diccionario que represente las películas de un cine, 
donde las claves son los nombres de las películas y 
los valores son los horarios correspondientes. 

Modifica el horario de la película "Avengers: Endgame" a las 19:30.
'''

diccionario_peliculas = {'The Matrix' : '22:30' , 'John Wick' : '19:30' , 'Pacific Rim' : '17:00', 'Avengers: Endgame' : '13:00'}
pelicula_ingresada = input("Por favor, ingresar nombre de la pelicula:\n")
horario_ingresada = input("Por favor, ingresar horario de la pelicula:\n")
diccionario_peliculas[pelicula_ingresada] = horario_ingresada
print(diccionario_peliculas)


'''
Crea un diccionario que represente los juegos de una consola, 
donde las claves son los nombres de los juegos y 
los valores son las puntuaciones correspondientes. 
Solicita al usuario el nombre de un juego y luego su puntuación, 
si el juego no existe agregarlo y si existe actualizar su puntuación
'''

diccionario_juegos_consola = {'Uncharted 3' : 8.9 , 'Call of Duty: Black Ops 2' : 10.0 , 'Destiny 2' : 7.8}
juego_ingresado = input("Por favor, ingresar nombre del juego:\n")
puntaje_ingresado = float(input("Por favor, ingresar puntaje del juego:\n"))
diccionario_juegos_consola[juego_ingresado] = puntaje_ingresado
print(diccionario_juegos_consola)


'''
Crea un diccionario que represente las temperaturas de una ciudad durante una semana, 
donde las claves son los días de la semana y 
los valores son las temperaturas correspondientes. 

Calcula la temperatura promedio de la semana.
'''

diccionario_temp_quilmes = {'Lunes' : 28.3 , 'Martes' : 30.6 , 'Miercoles' : 14.7 ,
                            'Jueves' : 24.1 , 'Viernes' : 32.8 , 'Sabado' : 8.3 ,
                            'Domingo' : 35.7 }
acumulador_temperatura = 0
contador_temperatura = 0 

for temperatura in diccionario_temp_quilmes.values():
    acumulador_temperatura += float(temperatura)
    contador_temperatura += 1

promedio_temperatura = float(acumulador_temperatura / contador_temperatura)
print(f'{promedio_temperatura:.1f} Centigrados')


'''
Crea un diccionario que represente los asientos de un avión, 
donde las claves son los números de asientos y 
los valores son "True" si están ocupados y "False" si no lo están. 
Solicita al usuario un número de asiento y 
modifica su valor para marcarlo como ocupado. 

Luego imprimí la lista de asientos libres
'''

diccionario_asientos_avion = {100 : True , 204 : False , 228 : False , 175 : True}
asiento_ingresado = int(input("Por favor, ingresar una tarea:\n"))
diccionario_asientos_avion[asiento_ingresado] = not diccionario_asientos_avion[asiento_ingresado]

for asientos in diccionario_asientos_avion:
    if(diccionario_asientos_avion[asientos] == True):
        print(asientos, diccionario_asientos_avion[asientos])



'''
Crea un diccionario que represente los gastos de una persona en diferentes categorías, 
donde las claves son los nombres de las categorías y 
los valores son los gastos correspondientes. 

Calcula el total de gastos de la persona.
'''
acumulador_gastos = 0
diccionario_gastos = {'Luz' : 33000 , 'Gas' : 8000 , 'Agua' : 15000}
for gasto in diccionario_gastos.values():
    acumulador_gastos += gasto
print(acumulador_gastos)


'''
Crea un diccionario que represente los contactos de un teléfono, 
donde las claves son los nombres de las personas y 
los valores son los números de teléfono correspondientes. 
Solicitar al usuario el nombre de un contacto: 
agregarlo al diccionario en caso de que no exista. 
En caso de que exista modificar el número de teléfono del contacto.
'''

diccionario_contactos_telefono = {'Maxi' : 24343534 , 'Brian' : 42256336 , 'Irina' : 42657886 , 'Juan' : 11235467}
contacto_ingresado = input("Por favor, ingresar nombre de un contacto:\n")
telefono_ingresado = input("Por favor, ingresar el numero de telefono:\n")
if(diccionario_contactos_telefono.get(contacto_ingresado, 'NOT FOUND') == 'NOT FOUND'):
    telefono_ingresado = int(input("Por favor, es un contacto nuevo, ingresar el telefono:\n"))
diccionario_contactos_telefono[contacto_ingresado] = telefono_ingresado