lista_alumnos = [22,33,55,67,11]
lista_edades = [22,33,56,78,11]
lista_nombres_1 = ["Nico", "Maxi", "Brian", "Juan"]
lista_nombres_2 = ["Brian", "Nico", "Maxi", "Pedro"]
lista_peliculas = [{'titulo' : 'The Matrix' , 'genero' : 'Accion' , 'director' : 'The Wachowskis Brothers'},
                   {'titulo' : 'Pacific Rim' , 'genero' : 'Accion' , 'director' : 'Guillermo del Toro'},
                   {'titulo' : 'Oppenheimer' , 'genero' : 'Drama' , 'director' : 'Nolan'}]


'''
Crear una función que convierta grados Celsius a grados Fahrenheit. 
Recibe un parámetro (grados Celsius) y 

devuelve el resultado en grados Fahrenheit.
'''

def convertir_celsius_a_fahrenheit(grados_cenlsius:float) -> float:
    grados_fahrenheit = (grados_cenlsius * 9/5) + 32
    return(grados_fahrenheit)


'''
Crear una función que calcule el área de un círculo. 
Recibe un parámetro (radio) y 

devuelve el área del círculo.
'''

def area_circulo(radio:int) -> int:
    area = float(3.14*radio**2)
    return(area)


'''
Crear una función que calcule el descuento aplicado a un producto. 
Recibe dos parámetros (precio original y precio con descuento) y 

devuelve el porcentaje de descuento aplicado.
'''

def calcula_descuento_en_producto(precio_original:float, descuento:float) -> float:
    descuento_aplicado = precio_original - (precio_original * (descuento/100))
    return(descuento_aplicado)


'''
Crear una función que calcule el promedio de edad de un grupo de personas. 
Recibe una lista de edades y 
devuelve el promedio.
'''

def promedio_edades_personas(lista:list) -> int:
    acumulador_edades = 0
    contador_edades = 0
    for edad in lista:
        acumulador_edades += edad
        contador_edades += 1
    return(acumulador_edades / contador_edades)


'''
Crear una función que determine si un número es primo o no. 
Recibe un parámetro (número) y 
devuelve True si es primo y False si no lo es.
'''

def numero_primo(numero:int) -> bool:
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

'''
Crear una función que calcule el área de un triángulo. 
Recibe dos parámetros (base y altura) y }
devuelve el área.
'''

def area_triangulo(base:float, altura:float) -> float:
    area = float((base * altura) / 2)
    return(area) 


'''
Crear una función que calcule el máximo común divisor de dos números. 
Recibe dos parámetros (números) y 
devuelve el máximo común divisor.
'''

def mcd(numero_a:int, numero_b:int) -> max:
    numero_t = 0
    while numero_b != 0:
        numero_t = numero_b
        numero_b = numero_a % numero_b
        numero_a = numero_t
    return numero_a


'''
Crear una función que verifique si un número es par o impar. 
Recibe un número como parámetro y 
devuelve True si es par o False si es impar.
'''

def es_par(numero:int) -> bool:
    return(numero % 2 == 0)

'''
Crear una función que cuente la cantidad de veces que aparece un elemento en una lista. 
Recibe una lista y un elemento como parámetros y 
devuelve la cantidad de veces que aparece en la lista.
'''

def cantidad_repetidos(lista:list, elemento:any) -> int:
    contador = 0
    for item in lista:
        if(item == elemento):
            contador += 1
    return(contador)


'''
Crea una función que reciba como parámetros una lista de palabras y 
devuelva la palabra más larga.
'''
lista_palabras = ['superapretujembajem', 'alkazam', 'espectropatronuz']

def palabra_grande(lista:list) -> str:
    palabra_temporal = ""
    flag = True
    for palabra in lista:
        if(flag == True):
            palabra_temporal = palabra
            flag = False
        elif(len(palabra_temporal) <= len(palabra)):
            palabra_temporal = palabra
    return(palabra_temporal)


'''
Crea una función que reciba como parámetro una cadena de texto y 
devuelva la cantidad de vocales que tiene.
'''

def cantidad_vocales(texto:str) -> int:
    contador_vocal = 0
    for letra in texto:
        if letra.lower() in 'aeiou':
            contador_vocal += 1
    return(contador_vocal)

'''
Crea una función que reciba dos listas de nombres, y 
devuelva una lista con los nombres que aparecen en ambas listas
'''


def nombres_repetidos(lista_a:list, lista_b:list) -> list:
    lista_vacia = []
    for palabra in lista_a:
        if palabra in lista_b:
            lista_vacia.append(palabra)
    return(lista_vacia)


'''
Crear una función que recibe una lista de palabras y 
devuelve un diccionario con las palabras como llaves y su longitud como valores.
'''

def lista_palabras_a_dict(lista:list) -> dict:
    diccionario = {}
    for indice in range(len(lista)):
        diccionario[lista[indice]] = indice
    return(diccionario)


'''
Crear una función que recibe una lista de números y 
devuelve un diccionario con el valor mínimo, 
el valor máximo y el promedio de los números en la lista.
'''

def lista_numeros_a_dict(lista:list) -> dict:
    diccionario = {}
    acumulador_numeros = 0
    numero_mayor = 0
    numero_menor = 0
    contador_numeros = 0
    for indice in range(len(lista)):
        acumulador_numeros += lista[indice]
        contador_numeros += 1
        if(lista[indice] >= numero_mayor):
            numero_mayor = lista[indice]
        elif(numero_menor <= lista[indice]):
            numero_menor = lista[indice]
    promedio = acumulador_numeros / contador_numeros
    diccionario['Valor Minimo'] = numero_menor 
    diccionario['Valor Maximo'] = numero_mayor
    diccionario['Valor Promedio'] = promedio 
    return(diccionario)



'''
Crear una función que recibe una lista de diccionarios con información de películas 
(título, género, director) y 
devuelve un diccionario con la cantidad de películas por género.
'''

def cantidad_peliculas_por_genero(lista:list[dict]) -> dict:
    diccionario_vacio = {}
    for peliculas in lista:
        genero = peliculas.get("genero", "ERROR")
        if not genero in diccionario_vacio.keys():
            diccionario_vacio[genero] = 1
        else:
            diccionario_vacio[genero] += 1
    return diccionario_vacio

# ---------------------------EJ1------------------------------
print("La conversion final es: "f'{convertir_celsius_a_fahrenheit(35.3):.2f}')
#---------------------------EJ2------------------------------
print("El area del circulo es: ", f'{area_circulo(2):.2f}')
#---------------------------EJ3------------------------------
print("El precio final con descuento aplicado es: ", f'{calcula_descuento_en_producto(500, 10):.2f}')
#---------------------------EJ4------------------------------
print("El promedio de edades es: ", promedio_edades_personas(lista_alumnos))
#---------------------------EJ5------------------------------
print("el siguiente numero es: ", numero_primo(11))
#---------------------------EJ6------------------------------
print("El area del triangulo es: ", f'{area_triangulo(4, 8):.2f}')
#---------------------------EJ7------------------------------
print("El MCD es: ", f'{mcd(4, 8)}')
#---------------------------EJ8------------------------------
print("El siguiente numero es: ", f'{es_par(11)}')
#---------------------------EJ9------------------------------
print("El elemento se repite: ", f'{cantidad_repetidos(lista_alumnos, 22)}')
#---------------------------EJ10------------------------------
print("La palabra mas grande es: ", f'{palabra_grande(lista_palabras)}')
#---------------------------EJ11------------------------------
print("La cantidad de vocales es: ", f'{cantidad_vocales("aaeeioubasd")}')
#---------------------------EJ12------------------------------
print("Los nombres repetidos son: ", f'{nombres_repetidos(lista_nombres_1, lista_nombres_2)}')
#---------------------------EJ13------------------------------
print("La transformacion de la lista de palabras a dict: ", f'{lista_palabras_a_dict(lista_nombres_1)}')
#---------------------------EJ14------------------------------
print("La transformacion de la lista de numeros a dict: ", f'{lista_numeros_a_dict(lista_edades)}')
# #---------------------------EJ15------------------------------
print("La cantidad de peliculas por genero es: ", f'{cantidad_peliculas_por_genero(lista_peliculas)}')



