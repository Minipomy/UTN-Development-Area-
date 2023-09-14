from fun_stark import *

'''
Agregar al código elaborado para cumplir el desafío #01 los siguientes puntos, utilizando un menú que permita acceder a cada uno de los puntos por separado.
Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
Determinar cuántos superhéroes tienen cada tipo de color de ojos.
Determinar cuántos superhéroes tienen cada tipo de color de pelo.
Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
Listar todos los superhéroes agrupados por color de ojos.
Listar todos los superhéroes agrupados por color de pelo.
Listar todos los superhéroes agrupados por tipo de inteligencia

'''



#   A.-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M

print(f'The male characters are: {print_only_male(lista_heroes)}')

#   B.-Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F

print(f'The female characters are: {print_only_female(lista_heroes)}')

#   C.-Recorrer la lista y determinar cuál es el superhéroe más alto de género M

print(f'The tallest male height hero is: {obtain_tallest_male_hero(lista_heroes)}')

#   D.-Recorrer la lista y determinar cuál es el superhéroe más alto de género F 

print(f'The tallest female height hero is: {obtain_tallest_female_hero(lista_heroes)}')

#   E.-Recorrer la lista y determinar cuál es el superhéroe más bajo de género M 

print(f'The lowest male height hero is: {obtain_lowest_male_hero(lista_heroes)}')

#   F.-Recorrer la lista y determinar cuál es el superhéroe más bajo de género F 

print(f'The lowest female height hero is: {obtain_lowest_female_hero(lista_heroes)}')

#   G.-Recorrer la lista y determinar la altura promedio de los  superhéroes de género M

print(f'The average height of male heroes is: {average_height_of_male_heroes(lista_heroes)}')

#   H.-Recorrer la lista y determinar la altura promedio de los  superhéroes de género F

print(f'The average height of male heroes is: {average_height_of_female_heroes(lista_heroes)}')

#   I.-Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
