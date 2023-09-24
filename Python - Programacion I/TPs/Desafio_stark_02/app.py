from fun_stark import *

def impimir_menu() -> str:
    imprimir_dato('''
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

def validar_entero(num_str:str):
    return(num_str.isdigit())

def stark_menu_principal():
    impimir_menu()
    desire_option = input('Please, select your desire option:\n')
    while(validar_entero(desire_option) == False):
            impimir_menu()
            desire_option = input('Wrong input, please try again:\n')
    return(int(desire_option))

def stark_marvel_app(list_hero:list):
    flag = True
    while(flag == True):
        desire_option = stark_menu_principal()
        match int(desire_option):
                case 1:
                    imprimir_dato(f'The male characters are: {print_only_male(list_hero)}')
                    input('Press Enter to continue')
                case 2:
                    imprimir_dato(f'The female characters are: {print_only_female(list_hero)}')
                    input('Press Enter to continue')
                case 3:
                    imprimir_dato(f'The tallest male height hero is: {get_tallest_male_hero(list_hero)}')
                    input('Press Enter to continue')
                case 4:
                    imprimir_dato(f'The tallest female height hero is: {get_tallest_female_hero(list_hero)}')
                    input('Press Enter to continue')
                case 5:
                    imprimir_dato(f'The lowest male height hero is: {get_lowest_male_hero(list_hero)}')
                    input('Press Enter to continue')
                case 6:
                    imprimir_dato(f'The lowest female height hero is: {get_lowest_female_hero(list_hero)}')
                    input('Press Enter to continue')
                case 7:
                    imprimir_dato(f'The average height of male heroes is: {average_height_of_male_heroes(list_hero)}')
                    input('Press Enter to continue')
                case 8:
                    imprimir_dato(f'The average height of female heroes is: {average_height_of_female_heroes(list_hero)}')
                    input('Press Enter to continue')
                case 9:
                    imprimir_dato(f'Color eyes count is: {get_quantity_heroes_by_eye_color(list_hero)}')
                    input('Press Enter to continue')
                case 10:
                    imprimir_dato(f'Color hair count is: {get_quantity_heroes_by_hair_color(list_hero)}')
                    input('Press Enter to continue')
                case 11:
                    imprimir_dato(f'Intellect count is: {get_quantity_heroes_by_intellect(list_hero)}')
                    input('Press Enter to continue')
                case 12:
                    imprimir_dato(f'{order_by_key(group_by_eye_color(list_hero))}')
                    input('Press Enter to continue')
                case 13:
                    imprimir_dato(f'{order_by_key(group_by_hair_color(list_hero))}')
                    input('Press Enter to continue')
                case 14:
                    imprimir_dato(f'{order_by_key(group_by_intellect(list_hero))}')
                    input('Press Enter to continue')
                case 15:
                    flag = False