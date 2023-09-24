from fun_stark import *

def impimir_menu() -> str:
    print_data(
'''Menú:
    1. Imprimir nombres de héroes
    2. Imprimir nombres y alturas
    3. Calcular e imprimir el héroe con el máximo dato
    4. Calcular e imprimir el héroe con el mínimo dato
    5. Calcular e imprimir el promedio de alturas
    6. Salir\n''')

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
                    stark_print_hero_names(list_hero)
                    input('Press Enter to continue')
                case 2:
                    stark_print_names_heights(list_hero)
                    input('Press Enter to continue')
                case 3:
                    stark_print_calculate_hero(list_hero, "maximo", "fuerza")
                    input('Press Enter to continue')
                case 4:
                    stark_print_calculate_hero(list_hero, "minimo", "fuerza")
                    input('Press Enter to continue')
                case 5:
                    stark_print_calculate_height_average(list_hero)
                    input('Press Enter to continue')
                case 6:
                    flag = False