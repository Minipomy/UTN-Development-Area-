from data_stark import lista_heroes


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


#   ------------------------------------- 02 -------------------------------------
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


def obtener_nombre(list_hero:list):
    for hero in list_hero:
        for nombre in hero.items():
            print(hero(nombre))
    


print(obtener_nombre(stark_normalizar_datos(lista_heroes)))


for hero in lista_heroes:
    for nombre in hero:
        lista_heroes(nombre)