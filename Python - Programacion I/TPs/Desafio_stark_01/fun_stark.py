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
 

def obtain_tallest_male_hero(list_hero:list) -> str | None:
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

def obtain_tallest_female_hero(list_hero:list) -> str | None :
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

def obtain_lowest_male_hero(list_hero:list) -> str | None:
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

def obtain_lowest_female_hero(list_hero:list) -> str | None :
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
