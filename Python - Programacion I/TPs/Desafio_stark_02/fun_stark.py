def print_only_male(list_hero:list) -> list:
    '''
    Uso: crea una lista vacia de heroes masculinos
    Variables: tipo lista, requiere una lista de heroes
    Retorna: tipo lista[Str] de heroes masculinos 
    '''
    list_boys = []
    for hero in list_hero:
        if(hero.get('genero') == 'M'):
            list_boys.append(hero.get('nombre'))
    return(list_boys)

def print_only_female(list_hero:list) -> list:
    '''
    Uso: crea una lista vacia de heroes femeninos
    Variables: tipo lista, requiere una lista de heroes
    Retorna: tipo lista[Str] de heroes femeninos
    '''
    list_womens = []
    for hero in list_hero:
        if(hero.get('genero') == 'F'):
            list_womens.append(hero.get('nombre'))
    return(list_womens)


def get_tallest_male_hero(list_hero:list) -> str | None:
    '''
    Uso: indica nombre del heroe masculino mas alto
    Variables: tipo lista, requiere una lista de heroes
    Retorna: nombre de heroe [Str] y Altura del hero [Float] Masculino mas bajo
    '''
    hero_name = None
    hero_height = None
    flag = True
    for hero in list_hero:
        gender = hero.get('genero')
        if(flag == True and gender == 'M'):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
            flag = False
        elif(gender == 'M' and hero_height <= float(hero.get('altura', 'ERROR'))):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
    return(hero_name, hero_height)

def get_tallest_female_hero(list_hero:list) -> str | None :
    '''
    Uso: indica nombre del heroe femenino mas alto
    Variables: tipo lista, requiere una lista de heroes
    Retorna: nombre de heroe [Str] y Altura del hero [Float] Femenino mas bajo
    '''
    hero_name = None
    hero_height = None
    flag = True
    for hero in list_hero:
        gender = hero.get('genero')
        if(flag == True and gender == 'F'):
            hero_name = hero.get('nombre', 'ERROR').capitalize()
            hero_height = float(hero.get('altura', 'ERROR'))
            flag = False
        elif(gender == 'F' and hero_height <= float(hero.get('altura', 'ERROR'))):
            hero_name = hero.get('nombre', 'ERROR').capitalize()
            hero_height = float(hero.get('altura', 'ERROR'))
    return(hero_name, hero_height)

def get_lowest_male_hero(list_hero:list) -> str | None:
    '''
    Uso: indica nombre del heroe masculino mas bajo
    Variables: tipo lista, requiere una lista de heroes
    Retorna: nombre de heroe [Str] y Altura del hero [Float] Masculino mas bajo
    '''
    hero_name = None
    hero_height = None
    flag = True
    for hero in list_hero:
        gender = hero.get('genero')
        if(flag == True and gender == 'M'):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
            flag = False
        elif(gender == 'M' and hero_height >= float(hero.get('altura', 'ERROR'))):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
    return(hero_name, hero_height)

def get_lowest_female_hero(list_hero:list) -> str | None :
    '''
    Uso: indica nombre del heroe femenino mas bajo
    Variables: tipo lista, requiere una lista de heroes
    Retorna: nombre de heroe [Str] y Altura del hero [Float] Femenino mas bajo
    '''
    hero_name = None
    hero_height = None
    flag = True
    for hero in list_hero:
        gender = hero.get('genero')
        if(flag == True and gender == 'F'):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
            flag = False
        elif(gender == 'F' and hero_height >= float(hero.get('altura', 'ERROR'))):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
    return(hero_name, hero_height)

def average_height_of_male_heroes(list_hero:list) -> float | None:
    '''
    Uso: indica el promedio de altura de heroes masculinos
    Variables: tipo lista, requiere una lista de heroes
    Retorna: average_male: valor de tipo [Float]
    '''
    counter = 0
    accumulator = 0
    average_male = None
    for hero in list_hero:
        gender = hero.get('genero')
        if(gender == 'M'):
            accumulator += float(hero.get('altura', 'ERROR'))
            counter += 1
    if(counter != 0):
        average_male = float(accumulator / counter)
    return(average_male)

def average_height_of_female_heroes(list_hero:list) -> int | None :
    '''
    Uso: indica el promedio de altura de heroes Femeninos
    Variables: tipo lista, requiere una lista de heroes
    Retorna: average_female: valor de tipo [Float]
    '''
    counter = 0
    accumulator = 0
    average_female = None
    for hero in list_hero:
        gender = hero.get('genero')
        if(gender == 'F'):
            accumulator += float(hero.get('altura', 'ERROR'))
            counter += 1
            
    if(counter != 0):
        average_female = float(accumulator / counter)
    return(average_female)

def get_quantity_heroes_by_eye_color(list_heroes:list) -> dict:
    '''
    Uso: indica un diccionario, donde sus keys son colores de ojos y sus claves la cantidad de heroes con ese color de ojos
    Variables: tipo lista, requiere una lista de heroes
    Retorna: eyes_colors: retorna diccionario[List]
    '''
    eyes_colors = {}
    for hero in list_heroes:
        color_actual = hero.get('color_ojos').capitalize()

        if(color_actual in eyes_colors.keys()):
            eyes_colors[color_actual] += 1
        else:
            eyes_colors[color_actual] = 1 
    return(eyes_colors)

def get_quantity_heroes_by_hair_color(list_heroes:list) -> dict:
    '''
    Uso: indica un diccionario, donde sus keys son color de pelo y sus claves la cantidad de heroes con ese color de pelo
    Variables: tipo lista, requiere una lista de heroes
    Retorna: hair_colors: retorna diccionario[List]
    '''
    hair_colors = {}
    for hero in list_heroes:
        color_actual = hero.get('color_pelo').capitalize()

        if(color_actual in hair_colors.keys()):
            hair_colors[color_actual] += 1
        else:
            hair_colors[color_actual] = 1 
    return(hair_colors)

def get_quantity_heroes_by_intellect(list_heroes:list) -> dict:
    '''
    Uso: indica un diccionario, donde sus keys son el intelecto y sus claves la cantidad de heroes con ese intelecto
    Variables: tipo lista, requiere una lista de heroes
    Retorna: intellect_counts: retorna diccionario[List]
    '''
    intellect_counts = {}
    for hero in list_heroes:
        actual_intel = hero.get('inteligencia').capitalize()

        if(actual_intel in intellect_counts.keys()):
            match(actual_intel):
                case "":
                    intellect_counts['No tiene'] += 1
                case _:
                    intellect_counts[actual_intel] += 1 
        else:
            match(actual_intel):
                case "":
                    intellect_counts['No tiene'] = 1
                case _:
                    intellect_counts[actual_intel] = 1 
    return(intellect_counts)

def group_by_eye_color(list_heroes:list) -> dict:
    '''
    Uso: indica un diccionario, donde sus keys son el color de ojos y sus claves listas de heroes que corresponden al mismo
    Variables: tipo lista, requiere una lista de heroes
    Retorna: colors_category: retorna diccionario[List]
    '''
    colors_category = {}
    for hero in list_heroes:
        actual_color = hero.get('color_ojos').capitalize()
        actual_name = hero.get('nombre')
        if(actual_color in colors_category.keys()):
            colors_category[actual_color] += [actual_name]
        else:
            colors_category[actual_color] = [actual_name]
    return(colors_category)

def group_by_hair_color(list_heroes:list) -> dict:
    '''
    Uso: indica un diccionario, donde sus keys son el color de pelo y sus claves listas de heroes que corresponden al mismo
    Variables: tipo lista, requiere una lista de heroes
    Retorna: colors_category: retorna diccionario[List]
    '''
    colors_category = {}
    for hero in list_heroes:
        actual_color = hero.get('color_pelo').capitalize()
        actual_name = hero.get('nombre')
        if(actual_color in colors_category.keys()):
            match(actual_color):
                case "":
                    colors_category['No tiene'] += [actual_name] 
                case _:
                    colors_category[actual_color] += [actual_name] 
        else:
            match(actual_color):
                case "":
                    colors_category['No tiene'] = [actual_name]
                case _:
                    colors_category[actual_color] = [actual_name] 
    return(colors_category)

def group_by_intellect(list_heroes:list) -> dict[list]:
    '''
    Uso: indica un diccionario, donde sus keys son el intelecto y sus claves listas de heroes que corresponden al mismo
    Variables: tipo lista, requiere una lista de heroes
    Retorna: intel_category: retorna diccionario[List]
    '''
    intel_category = {}
    for hero in list_heroes:
        actual_intel = hero.get('inteligencia').capitalize()
        actual_name = hero.get('nombre')
        if(actual_intel in intel_category.keys()):
            match(actual_intel):
                case "":
                    intel_category['No tiene'] += [actual_name] 
                case _:
                    intel_category[actual_intel] += [actual_name] 
        else:
            match(actual_intel):
                case "":
                    intel_category['No tiene'] = [actual_name] 
                case _:
                    intel_category[actual_intel] = [actual_name] 
    return(intel_category)

def order_by_key(dictionary:dict[list]):
    '''
    Uso: formatea el contenido de un diccionario de tipo lista en strings
    Variable: de tipo diccionario[Lista]
    '''
    for category in dictionary:
        print(
            f'''----Category {category}----\n
            {dictionary[category]}\n''')


#   ------------------------------------- 02 FORMATEO STRINGS -------------------------------------

def obtener_nombre(heroe: dict) -> str:
    return f"Nombre: {heroe['nombre']}"

def imprimir_dato(dato:str) -> str:
    print(dato)

def stark_normalizar_datos(list_hero:list):
    if(len(list_hero) > 0):
            for hero in list_hero:
                for clave, valor in hero.items():
                    if(clave == 'fuerza'):
                        hero[clave] = int(valor)
                        print('Datos normalizados')
                    elif(clave == 'altura' or clave == 'peso'):
                        hero[clave] = float(valor)
                        print('Datos normalizados')
                    elif(clave == 'color_ojos' or clave == 'color_pelo' or clave == 'inteligencia'):
                        hero[clave] = str(valor).capitalize()
                        print('Datos normalizados')
    else:
        print('No hay nada para normalizar')
    return(list_hero)

#   ------------------------------------- 02 funciones -------------------------------------

def stark_imprimir_nombres_heroes(list_hero:list) -> dict:
    if(len(list_hero) < 0):
        return(-1)
    for hero in list_hero:
        imprimir_dato(obtener_nombre(hero))

def obtener_nombre_y_dato(hero:list[dict], key:str) -> str:
    return(f'Nombre: {hero["nombre"]} | {key}: {hero.get(key)}')


def stark_imprimir_nombres_alturas(list_hero:list) -> str:
    if(len(list_hero) < 0):
            return(-1)
    for hero in list_hero:
        imprimir_dato(obtener_nombre_y_dato(hero, 'altura'))

def calcular_max(list_hero:list, key:str) -> str:
    flag = True
    max_valor = 0
    max_hero = 0
    for hero in list_hero:
        for clave in hero:
            if(flag == True and clave == key):
                max_valor = hero.get(key)
                max_hero = hero.get('nombre')
                flag = False
            elif(clave == key and max_valor <= hero.get(key)):
                max_valor = hero.get(key)
                max_hero = hero.get('nombre')
    return(max_hero)

def calcular_min(list_hero:list, key:str) -> str:
    flag = True
    min_valor = 0
    min_hero = 0
    for hero in list_hero:
        for clave in hero:
            if(flag == True and clave == key):
                min_valor = hero.get(key)
                min_hero = hero.get('nombre')
                flag = False
            elif(clave == key and min_valor >= hero.get(key)):
                min_valor = hero.get(key)
                min_hero = hero.get('nombre')
    return(min_hero)

def calcular_max_min_dato(list_hero:list, max_min:str, key:str):
    match(max_min.capitalize()):
        case 'Maximo':
            return(calcular_max(list_hero, key))
        case 'Minimo':
            return(calcular_min(list_hero, key))
    
def stark_calcular_imprimir_heroe(list_hero:list, max_min:str, key:str):
    if(len(list_hero) < 0):
        return(-1)
    hero = calcular_max_min_dato(list_hero, max_min, key)
    match(max_min.capitalize()):
        case 'Maximo':
            imprimir_dato(f'Mayor {key}: {obtener_nombre_y_dato(hero, key)}')
        case 'Minimo':
            imprimir_dato(f'Menor {key}: {obtener_nombre_y_dato(hero, key)}')
    
def sumar_dato_heroe(list_hero:list, key:str):
    if(len(list_hero) < 0):
        return(-1)
    sumar = 0
    list_refactor = stark_normalizar_datos(list_hero)
    for hero in list_refactor:
        sumar += hero.get(key)
    return(sumar)

def dividir(dividiendo:int, divisor:int) -> int:
    if (divisor == 0):
        return(0)
    return(dividiendo/divisor)

def calcular_promedio(list_hero:list, key:str) -> float:
    promedio = dividir(sumar_dato_heroe(list_hero, key), len(list_hero))
    return(promedio)


def stark_calcular_imprimir_promedio_altura(list_hero:list) -> str:
    if(len(list_hero) < 0):
        return(-1)
    suma = sumar_dato_heroe(list_hero, 'altura')
    promedio = calcular_promedio(list_hero, 'altura')
    imprimir_dato(suma)
    imprimir_dato(promedio)

