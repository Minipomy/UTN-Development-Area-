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

def calcula_descuento_en_producto(precio_original, descuento):
    descuento_aplicado = float(precio_original - (precio_original * (descuento/100)))
    return(descuento_aplicado)


'''
Crear una función que calcule el promedio de edad de un grupo de personas. 
Recibe una lista de edades y 
devuelve el promedio.
'''

lista_alumnos = [22,33,55,67,11]

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

#---------------------------EJ1------------------------------
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
#---------------------------EJ7------------------------------
print("El siguiente numero es: ", f'{es_par(11)}')

