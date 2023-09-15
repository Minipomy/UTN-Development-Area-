from fun_stark import *

def __ui_app__(input:input) -> str | dict | list | int :
    flag = True
    while(flag == True):
        desire_option = input('''Please, select you desire option: (HAS TO BE A NUMERIC VALUE)\n
                                1.- Imprimir por consola el nombre de cada superhéroe de género M
                                2.- Imprimir por consola el nombre de cada superhéroe de género F
                                3.- Determina cuál es el superhéroe más alto de género M 
                                4.- Determina cuál es el superhéroe más alto de género F 
                                5.- Determina cuál es el superhéroe más bajo  de género M 
                                6.- Determina cuál es el superhéroe más bajo  de género F 
                                7.- Determina la altura promedio de los  superhéroes de género M
                                8.- Determina la altura promedio de los  superhéroes de género F
                                9.- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
                                10.-Determinar cuántos superhéroes tienen cada tipo de color de pelo.
                                11.-Determinar cuántos superhéroes tienen cada tipo de inteligencia
                                12.-Listar todos los superhéroes agrupados por color de ojos.
                                13.-Listar todos los superhéroes agrupados por color de pelo.
                                14.-Listar todos los superhéroes agrupados por tipo de inteligencia
                                15.-Finalizar\n''')
        while(not desire_option.isdigit()):
            desire_option = input('''Please, select you desire option: (HAS TO BE A NUMERIC VALUE)\n
                                1.- Imprimir por consola el nombre de cada superhéroe de género M
                                2.- Imprimir por consola el nombre de cada superhéroe de género F
                                3.- Determina cuál es el superhéroe más alto de género M 
                                4.- Determina cuál es el superhéroe más alto de género F 
                                5.- Determina cuál es el superhéroe más bajo  de género M 
                                6.- Determina cuál es el superhéroe más bajo  de género F 
                                7.- Determina la altura promedio de los  superhéroes de género M
                                8.- Determina la altura promedio de los  superhéroes de género F
                                9.- Determinar cuántos superhéroes tienen cada tipo de color de ojos.
                                10.-Determinar cuántos superhéroes tienen cada tipo de color de pelo.
                                11.-Determinar cuántos superhéroes tienen cada tipo de inteligencia
                                12.-Listar todos los superhéroes agrupados por color de ojos.
                                13.-Listar todos los superhéroes agrupados por color de pelo.
                                14.-Listar todos los superhéroes agrupados por tipo de inteligencia
                                15.-Finalizar\n''')
        match int(desire_option):
            case 1:
                print(f'The male characters are: {print_only_male(lista_heroes)}')
            case 2:
                print(f'The female characters are: {print_only_female(lista_heroes)}')
            case 3:
                print(f'The tallest male height hero is: {get_tallest_male_hero(lista_heroes)}')
            case 4:
                print(f'The tallest female height hero is: {get_tallest_female_hero(lista_heroes)}')
            case 5:
                print(f'The lowest male height hero is: {get_lowest_male_hero(lista_heroes)}')
            case 6:
                print(f'The lowest female height hero is: {get_lowest_female_hero(lista_heroes)}')
            case 7:
                print(f'The average height of male heroes is: {average_height_of_male_heroes(lista_heroes)}')
            case 8:
                print(f'The average height of female heroes is: {average_height_of_female_heroes(lista_heroes)}')
            case 9:
                print(f'Color eyes count is: {get_quantity_heroes_by_eye_color(lista_heroes)}')
            case 10:
                print(f'Color hair count is: {get_quantity_heroes_by_hair_color(lista_heroes)}')
            case 11:
                print(f'Intellect count is: {get_quantity_heroes_by_intellect(lista_heroes)}')
            case 12:
                print(f'{order_by_key(group_by_eye_color(lista_heroes))}')
            case 13:
                print(f'{order_by_key(group_by_hair_color(lista_heroes))}')
            case 14:
                print(f'{order_by_key(group_by_intellect(lista_heroes))}')
            case 15:
                flag = False