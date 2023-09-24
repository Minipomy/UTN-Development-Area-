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
    imprimir_dato(f'{max_min.capitalize()} {key}: {obtener_nombre_y_dato(hero, key)}')

def sumar_dato_heroe(list_hero:list, key:str):
    if(len(list_hero) < 0):
        return(-1)
    sumar = 0
    for hero in list_hero:
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
    promedio = calcular_promedio(list_hero, 'altura')
    imprimir_dato(f'the average height is: {promedio:.2f}')
