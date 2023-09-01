import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano
Apellido: Rivera Mendes
Division: J


Enunciado.
PUEDEN UTILIZAR EL EJERCICIO 2 DE LISTAS PARA REALIZARLO: EL BOTÓN CARGAR CONTENDRÁ LA CARGA Y VALIDACIÓN DE DATOS, Y EL BOTÓN MOSTRAR SE ENCARGARÁ DE LA PARTE LÓGICA, LOS CÁLCULOS Y MOSTRARÁ LOS RESULTADOS. TIENEN PERMITIDO HARDCODEAR LAS LISTAS CON DATOS PARA HACER LA PARTE LÓGICA PRIMERO. NECESITARÁN UN TOTAL DE 7 LISTAS, UNA PARA CADA DATO INGRESADO => 5 Y 2 LISTAS MÁS PARA EL PUNTO E).

------------------Listas de prueba---------------------------
En el parque de diversiones "Aventuras Extremas", un grupo de amigos ha decidido disfrutar del día probando las diferentes atracciones y luego se reúnen en un restaurante para compartir un delicioso almuerzo. Antes de que llegue la cuenta, deciden crear un programa para calcular y dividir los gastos de manera equitativa. Se pide ingresar los siguientes datos hasta que el usuario lo desee:

Para cada amigo:

Nombre del amigo,
Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").
Cantidad de platos principales pedidos (debe ser al menos 1).
Bebida elegida ("Refresco", "Agua", "Jugo").
Cantidad de bebidas pedidas (debe ser al menos 1).
Se conocen los siguientes precios base:

El precio unitario de cada plato principal es de $800.
El precio unitario de cada bebida es de $200.
Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente:

El total gastado por el grupo (resultante del costo de los platos principales y las bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al 10% del total gastado).
Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general.
Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total (platos principales + bebidas) con una entrada gratuita para otra atracción del parque "Aventuras Extremas".
REALIZAR DOS PUNTO; EL PRIMERO CORRESPONDIENTE AL ÚLTIMO NÚMERO DE SU DNI PERSONAL (Ejemplo 4) Y EL SEGUNDO RESTANDO A 9 EL ÚLTIMO NÚMERO DE SU DNI (Ejemplo 9 - 4 = 5):
Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos principales del tipo "Pizza" y mostrar la lista completa por print.
Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos principales del tipo "Hamburguesa" y mostrar la lista completa por print.
Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos principales del tipo "Ensalada" y mostrar la lista completa por print.
Crear una lista nueva, agregar todos los nombres de los amigos que hayan pedido bebidas del tipo "Refresco" y mostrar la lista completa por print.
Crear una lista nueva, agregar todos los nombres de los amigos que hayan pedido bebidas del tipo "Agua" y mostrar la lista completa por print.
Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado más de 7 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos de 3 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_de_nombres = ["Juan", "María", "Pedro", "Laura", "Carlos", "Ana", "Luis", "Elena", "Miguel", "Sofía"]
        self.lista_plato_principal = ["Pizza", "Hamburguesa", "Ensalada", "Pizza", "Hamburguesa", "Ensalada", "Pizza", "Hamburguesa", "Ensalada", "Pizza"]
        self.lista_cantidad_de_platos = [2, 1, 3, 2, 2, 4, 3, 1, 1, 3]
        self.lista_bebidas_elegidas = ["Refresco", "Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco"]
        self.lista_cantidad_de_bebidas = [2, 1, 5, 3, 2, 5, 1, 2, 1, 3]

    def btn_mostrar_on_click(self):
        flag = True
        nombre = ""
        plato_principal = ""
        cantidad_platos = 0
        bebida = ""
        cantidad_bebida = 0

        while(flag != False):

            nombre = prompt("Ingrese", "Ingrese nombre:")
            while(nombre == ""):
                nombre = prompt("Ingrese", "Ingrese nombre:")

            plato_principal = prompt("Ingrese", "Ingrese plato:")
            while(plato_principal != "Pizza" and plato_principal != "Hamburguesa" and plato_principal != "Ensalada"):
                plato_principal = prompt("Ingrese", "Ingrese plato:")

            cantidad_platos = int(prompt("Ingrese", "Ingrese cantidad de platos:"))
            while(cantidad_platos < 1):
                cantidad_platos = int(prompt("Ingrese", "Ingrese cantidad de platos:"))

            bebida = prompt("Ingrese", "Ingrese bebida:")
            while(bebida != "Refresco" and bebida != "Agua" and bebida != "Jugo"):
                bebida = prompt("Ingrese", "Ingrese bebida:")

            cantidad_bebida = int(prompt("Ingrese", "Ingrese cantidad de bebidas:"))
            while(cantidad_bebida < 1):
                cantidad_bebida = int(prompt("Ingrese", "Ingrese cantidad de bebidas:"))

            self.lista_de_nombres.append(nombre)
            self.lista_plato_principal.append(plato_principal)
            self.lista_cantidad_de_platos.append(cantidad_platos)
            self.lista_bebidas_elegidas.append(bebida)
            self.lista_cantidad_de_bebidas.append(cantidad_bebida)

            flag = question("continuar", "Desea cargar mas datos")


    def btn_cargar_on_click(self):
        PRECIO_PLATO_UNITARIO = 800
        PRECIO_BEBIDA_UNITARIO = 200
        NUMERO_FINAL_DNI = 0        #40.621.380
        acumulador_gasto_total = 0
        contador_pizza = 0
        contador_hamburguesa = 0
        contador_ensalada = 0
        contador_refresco = 0
        contador_agua = 0
        contador_jugo = 0
        total_platos = 0
        nombre_persona = ""
        mensaje1 = ""
        mensaje2 = ""
        lista_case_1 = []
        lista_case_2 = []

        for i in range(len(self.lista_de_nombres)):
            nombre = self.lista_de_nombres[i]
            plato_principal = self.lista_plato_principal[i]
            cantidad_platos = self.lista_cantidad_de_platos[i]
            bebida = self.lista_bebidas_elegidas[i]
            cantidad_bebidas = self.lista_cantidad_de_bebidas[i]
            total_platos += cantidad_platos
            contador = i+1
            flag = True
            
            #   El precio unitario de cada plato principal es de $800.
            #   El precio unitario de cada bebida es de $200.

            #   El total gastado por el grupo (resultante del costo de los platos principales y las bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al 10% del total gastado).
            match(plato_principal):
                case "Pizza":
                    contador_pizza += cantidad_platos
                    acumulador_gasto_total += PRECIO_PLATO_UNITARIO * contador_pizza
                case "Hamburguesa":
                    contador_hamburguesa += cantidad_platos
                    acumulador_gasto_total += PRECIO_PLATO_UNITARIO * contador_hamburguesa
                case "Ensalada":
                    contador_ensalada += cantidad_platos
                    acumulador_gasto_total += PRECIO_PLATO_UNITARIO * contador_ensalada

            match(bebida):
                case "Refresco":
                    contador_refresco += cantidad_bebidas
                    acumulador_gasto_total += PRECIO_BEBIDA_UNITARIO * cantidad_bebidas
                case "Agua":
                    contador_agua += cantidad_bebidas
                    acumulador_gasto_total += PRECIO_BEBIDA_UNITARIO * cantidad_bebidas
                case "Jugo":
                    contador_jugo += cantidad_bebidas
                    acumulador_gasto_total += PRECIO_BEBIDA_UNITARIO * cantidad_bebidas

            if(flag == True):
                nombre_persona = nombre
                maximo_cantidad = cantidad_platos + cantidad_bebidas
                flag == False
            elif((cantidad_platos + cantidad_bebidas) >= maximo_cantidad):
                nombre_persona = nombre
                maximo_cantidad = cantidad_platos + cantidad_bebidas

                
            match(NUMERO_FINAL_DNI):
                case 0:
                    if(plato_principal == "Pizza"):
                        lista_case_1.append(nombre)
                case 1:
                    if(plato_principal == "Hamburguesa"):
                        lista_case_1.append(nombre)
                case 2:
                    if(plato_principal == "Ensalada"):
                        lista_case_1.append(nombre)
                case 3:
                    if(bebida == "Refresco"):
                        lista_case_1.append(nombre)
                case 4:
                    if(bebida == "Agua"):
                        lista_case_2.append(nombre)
                case 5: 
                    if((cantidad_bebidas + cantidad_platos) >= 3):
                        lista_case_2.append(nombre)
                case 6:
                    if((cantidad_bebidas + cantidad_platos) >= 5):
                        lista_case_2.append(nombre)
                case 7:
                    if((cantidad_bebidas + cantidad_platos) >= 7):
                        lista_case_1.append(nombre)
                case 8:
                    if((cantidad_bebidas + cantidad_platos) <= 3):
                        lista_case_1.append(nombre)
                case 9:
                    if((cantidad_bebidas + cantidad_platos) <= 5):
                        lista_case_1.append(nombre)
            mensaje1 = lista_case_1

            match(NUMERO_FINAL_DNI - 9):
                case 0:
                    if(plato_principal == "Pizza"):
                        lista_case_2.append(nombre)
                case -1:
                    if(plato_principal == "Hamburguesa"):
                        lista_case_2.append(nombre)
                case -2:
                    if(plato_principal == "Ensalada"):
                        lista_case_2.append(nombre)
                case -3:
                    if(bebida == "Refresco"):
                        lista_case_2.append(nombre)
                case -4:
                    if(bebida == "Agua"):
                        lista_case_2.append(nombre)
                case -5: 
                    if((cantidad_bebidas + cantidad_platos) >= 3):
                        lista_case_2.append(nombre)
                case -6:
                    if((cantidad_bebidas + cantidad_platos) >= 5):
                        lista_case_2.append(nombre)
                case -7:
                    if((cantidad_bebidas + cantidad_platos) >= 7):
                        lista_case_2.append(nombre)
                case -8:
                    if((cantidad_bebidas + cantidad_platos) <= 3):
                        lista_case_2.append(nombre)
                case -9:
                    if((cantidad_bebidas + cantidad_platos) <= 5):
                        lista_case_2.append(nombre)
            mensaje2 = lista_case_2

            #   Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
            
        porcentaje_pizza = contador_pizza * 100 // cantidad_platos
        porcentaje_hamburguesa = contador_hamburguesa * 100 // cantidad_platos
        porcentaje_ensalada = contador_ensalada * 100 // cantidad_platos
        propina = float((10 * acumulador_gasto_total) / 100)

        #   B)  Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general.
        if(contador_jugo > 0):
            promedio_gasto_jugo =  float((PRECIO_BEBIDA_UNITARIO * contador_jugo) / contador)

        #   A)   El total gastado por el grupo (resultante del costo de los platos principales y las bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al 10% del total gastado).
        alert("Respuesta", f"El total gastado en grupo es de {acumulador_gasto_total:.2f} y dejaron de propina: {propina:.2f}")
        #   B)  Promedio del dinero gastado en “Jugo”, sobre el grupo de amigos en general.
        alert("Respuesta", f"El promedio gastado en Jugo es de {promedio_gasto_jugo:.2f}")
        #   C)  Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
        alert("Respuesta", f"los porcentajes de cada tipo son Pizza %{porcentaje_pizza}\n Hamburguesa %{porcentaje_hamburguesa}\nEnsalada %{porcentaje_ensalada}")
        #   D) Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total (platos principales + bebidas) con una entrada gratuita para otra atracción del parque "Aventuras Extremas".
        alert("Respuesta", f"El premio se lo lleva {nombre_persona} con un total de: {maximo_cantidad}")
        #   E) REALIZAR DOS PUNTO; EL PRIMERO CORRESPONDIENTE AL ÚLTIMO NÚMERO DE SU DNI PERSONAL (Ejemplo 4) Y EL SEGUNDO RESTANDO A 9 EL ÚLTIMO NÚMERO DE SU DNI (Ejemplo 9 - 4 = 5):
        alert("Respuesta", f"Para el caso del ultimo digito de mi dni:{mensaje1}\n para el caso de -9 {mensaje2}")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()