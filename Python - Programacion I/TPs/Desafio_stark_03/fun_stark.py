#   ------------------------------------- 02 FORMATEO STRINGS -------------------------------------
def get_name(hero: dict) -> str:
    return f"Nombre: {hero['nombre']}"

def print_data(dato:str) -> str:
    print(dato)

def stark_data_normalized(list_hero:list):
    if(len(list_hero) > 0):
            for hero in list_hero:
                for clave, valor in hero.items():
                    if(clave == 'fuerza'):
                        hero[clave] = int(valor)
                        # print('Datos normalizados')
                    elif(clave == 'altura' or clave == 'peso'):
                        hero[clave] = float(valor)
                        # print('Datos normalizados')
                    elif(clave == 'color_ojos' or clave == 'color_pelo' or clave == 'inteligencia'):
                        hero[clave] = str(valor).capitalize()
                        # print('Datos normalizados')
    else:
        print('No hay nada para normalizar')
    return(list_hero)

#   ------------------------------------- 02 funciones -------------------------------------

def stark_print_hero_names(list_hero:list) -> dict:
    if(len(list_hero) < 0):
        return(-1)
    for hero in list_hero:
        print_data(get_name(hero))

def get_name_and_data(hero:list[dict], key:str) -> str:
    return(f'{get_name(hero)} | {key}: {hero.get(key)}')

def stark_print_names_heights(list_hero:list) -> str:
    if(len(list_hero) < 0):
            return(-1)
    for hero in list_hero:
        print_data(get_name_and_data(hero, 'altura'))

def max_calculate(list_hero:list, key:str) -> str:
    flag = True
    max_valor = 0
    max_hero = {}
    for hero in list_hero:
        for clave in hero:
            if(flag == True and clave == key):
                max_valor = hero.get(key)
                max_hero = hero
                flag = False
            elif(clave == key and max_valor <= hero.get(key)):
                max_valor = hero.get(key)
                max_hero = hero
    return(max_hero)

def min_calculate(list_hero:list, key:str) -> str:
    flag = True
    min_valor = 0
    min_hero = {}
    for hero in list_hero:
        for clave in hero:
            if(flag == True and clave == key):
                min_valor = hero.get(key)
                min_hero = hero
                flag = False
            elif(clave == key and min_valor >= hero.get(key)):
                min_valor = hero.get(key)
                min_hero = hero
    return(min_hero)

def min_max_data_calculate(list_hero:list, max_min:str, key:str):
    match(max_min.capitalize()):
        case 'Maximo':
            return(max_calculate(list_hero, key))
        case 'Minimo':
            return(min_calculate(list_hero, key))

def stark_print_calculate_hero(list_hero:list, max_min:str, key:str):
    if(len(list_hero) < 0):
        return(-1)
    hero = min_max_data_calculate(list_hero, max_min, key)
    print_data(f'{max_min.capitalize()} {key}: {get_name_and_data(hero, key)}')

def sum_data_hero(list_hero:list, key:str):
    if(len(list_hero) < 0):
        return(-1)
    sumar = 0
    for hero in list_hero:
        sumar += hero.get(key)
    return(sumar)

def divide(dividiendo:int, divisor:int) -> int:
    if (divisor == 0):
        return(0)
    return(dividiendo/divisor)

def average_calculate(list_hero:list, key:str) -> float:
    promedio = divide(sum_data_hero(list_hero, key), len(list_hero))
    return(promedio)

def stark_print_calculate_height_average(list_hero:list) -> str:
    if(len(list_hero) < 0):
        return(-1)
    promedio = average_calculate(list_hero, 'altura')
    print_data(f'the average height is: {promedio:.2f}')

def number_check(num_str:str):
    return(num_str.isdigit())

def imprimir_menu_2():
    print_data(
'''Menú:
    1. Imprimir nombres de héroes
    2. Imprimir nombres y alturas
    3. Calcular e imprimir el héroe con el máximo dato
    4. Calcular e imprimir el héroe con el mínimo dato
    5. Calcular e imprimir el promedio de alturas
    6. Salir\n''')

def stark_menu_principal_2():
    imprimir_menu_2()
    desire_option = input('Please, select your desire option:\n')
    while(number_check(desire_option) == False):
            imprimir_menu_2()
            desire_option = input('Wrong input, please try again:\n')
    return(int(desire_option))

def stark_marvel_app_2(list_hero:list):
    flag = True
    while(flag == True):
        desire_option = stark_menu_principal_2()
        match int(desire_option):
                case 1:
                    stark_print_hero_names(list_hero)
                    input('Press Enter to continue')
                case 2:
                    stark_print_names_heights(list_hero)
                    input('Press Enter to continue')
                case 3:
                    dato = input('select: fuerza, altura, peso, inteligencia')
                    stark_print_calculate_hero(list_hero, "maximo", dato)
                    input('Press Enter to continue')
                case 4:
                    dato = input('select: fuerza, altura, peso, inteligencia')
                    stark_print_calculate_hero(list_hero, "minimo", dato)
                    input('Press Enter to continue')
                case 5:
                    stark_print_calculate_height_average(list_hero)
                    input('Press Enter to continue')
                case 6:
                    flag = False

