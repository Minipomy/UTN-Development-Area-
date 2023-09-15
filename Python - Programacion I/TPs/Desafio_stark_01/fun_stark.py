from data_stark import lista_heroes


def print_only_male(list_hero:list) -> list:
    list_boys = []
    for hero in list_hero:
        if(hero.get('genero') == 'M'):
            list_boys.append(hero.get('nombre'))
    return(list_boys)

def print_only_female(list_hero:list) -> list:
    list_womens = []
    for hero in list_hero:
        if(hero.get('genero') == 'F'):
            list_womens.append(hero.get('nombre'))
    return(list_womens)


def get_tallest_male_hero(list_hero:list) -> str | None:
    hero_name = None
    hero_height = None
    flag = True
    for hero in list_hero:
        if(flag == True and print_only_male(list_hero)):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
            flag = False
        elif(print_only_male(list_hero) and hero_height <= float(hero.get('altura', 'ERROR'))):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
    return(hero_name, hero_height)

def get_tallest_female_hero(list_hero:list) -> str | None :
    hero_name = None
    hero_height = None
    flag = True
    for hero in list_hero:
        if(flag == True and print_only_female(list_hero)):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
            flag = False
        elif(print_only_female(list_hero) and hero_height <= float(hero.get('altura', 'ERROR'))):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
    return(hero_name, hero_height)

def get_lowest_male_hero(list_hero:list) -> str | None:
    hero_name = None
    hero_height = None
    flag = True
    for hero in list_hero:
        if(flag == True and print_only_male(list_hero)):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
            flag = False
        elif(print_only_male(list_hero) and hero_height >= float(hero.get('altura', 'ERROR'))):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
    return(hero_name, hero_height)

def get_lowest_female_hero(list_hero:list) -> str | None :
    hero_name = None
    hero_height = None
    flag = True
    for hero in list_hero:
        if(flag == True and print_only_female(list_hero)):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
            flag = False
        elif(print_only_female(list_hero) and hero_height >= float(hero.get('altura', 'ERROR'))):
            hero_name = hero.get('nombre', 'ERROR')
            hero_height = float(hero.get('altura', 'ERROR'))
    return(hero_name, hero_height)

def average_height_of_male_heroes(list_hero:list) -> int | None:
    counter = 0
    accumulator = 0
    average_male = None
    for hero in list_hero:
        if(print_only_male(list_hero)):
            accumulator += float(hero.get('altura', 'ERROR'))
            counter += 1
    if(counter != 0):
        average_male = float(accumulator / counter)
    return(average_male)

def average_height_of_female_heroes(list_hero:list) -> int | None :
    counter = 0
    accumulator = 0
    average_female = None
    for hero in list_hero:
        if(print_only_female(list_hero)):
            accumulator += float(hero.get('altura', 'ERROR'))
            counter += 1
            
    if(counter != 0):
        average_female = float(accumulator / counter)
    return(average_female)

def get_quantity_heroes_by_eye_color(list_heroes:list) -> dict:
    eyes_colors = {}
    for hero in list_heroes:
        color_actual = hero.get('color_ojos')

        if(color_actual in eyes_colors.keys()):
            eyes_colors[color_actual] += 1
        else:
            eyes_colors[color_actual] = 1 
    return(eyes_colors)

def get_quantity_heroes_by_hair_color(list_heroes:list) -> dict:
    hair_colors = {}
    for hero in list_heroes:
        color_actual = hero.get('color_pelo')

        if(color_actual in hair_colors.keys()):
            hair_colors[color_actual] += 1
        else:
            hair_colors[color_actual] = 1 
    return(hair_colors)

def get_quantity_heroes_by_intellect(list_heroes:list) -> dict:
    intellect_counts = {}
    for hero in list_heroes:
        actual_intel = hero.get('inteligencia')

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

def group_by_eye_color(list_heroes:list) -> str:
    colors_category = {}
    for hero in list_heroes:
        actual_color = hero.get('color_ojos')
        actual_name = hero.get('nombre')
        if(actual_color in colors_category.keys()):
            colors_category[actual_color] += [actual_name]
        else:
            colors_category[actual_color] = [actual_name]
    return(colors_category)

def group_by_hair_color(list_heroes:list) -> str:
    colors_category = {}
    for hero in list_heroes:
        actual_color = hero.get('color_pelo')
        actual_name = hero.get('nombre')
        if(actual_color in colors_category.keys()):
            colors_category[actual_color] += [actual_name]
        else:
            colors_category[actual_color] = [actual_name]
    return(colors_category)

def group_by_intellect(list_heroes:list) -> str:
    intel_category = {}
    for hero in list_heroes:
        actual_intel = hero.get('inteligencia')
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