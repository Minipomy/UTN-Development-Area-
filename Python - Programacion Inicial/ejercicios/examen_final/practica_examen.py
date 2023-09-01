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
        self.lista_cantidad_de_platos = [2, 1, 3, 2, 2, 4, 3, 1, 1, 3]  #22 -- 17600
        self.lista_bebidas_elegidas = ["Refresco", "Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco"]
        self.lista_cantidad_de_bebidas = [2, 1, 5, 3, 2, 5, 1, 2, 1, 3] #25 -- 5000

    def btn_cargar_on_click(self):
        nombre = ""
        plato_principal = ""
        bebida_principal = ""
        cantidad_platos = 0
        cantidad_bebidas = 0
        flag = True

        while(flag != False):
            nombre = prompt("Ingreso", "Por favor, ingresar un nombre")
            while(nombre == ""):
                nombre = prompt("Ingreso", "Por favor, ingresar un nombre")
                
            plato_principal = prompt("Ingreso", "Por favor, ingresar un plato")
            while(plato_principal != "Pizza" and plato_principal != "Hamburguesa" and plato_principal != "Ensalada"):
                plato_principal = prompt("Ingreso", "Por favor, ingresar un plato")

            cantidad_platos = int(prompt("Ingreso", "Por favor, ingresar cantidad de platos"))
            while(cantidad_platos < 0):
                cantidad_platos = int(prompt("Ingreso", "Por favor, ingresar cantidad de platos"))

            bebida_principal = prompt("Ingreso", "Por favor, ingresar una bebida")
            while(bebida_principal != "Agua" and bebida_principal != "Jugo" and bebida_principal != "Refresco"):
                bebida_principal = prompt("Ingreso", "Por favor, ingresar una bebida")

            cantidad_bebidas = int(prompt("Ingreso", "Por favor, ingresar cantidad de bebidas"))
            while(cantidad_bebidas < 0):
                cantidad_bebidas = int(prompt("Ingreso", "Por favor, ingresar cantidad de bebidas"))

            self.lista_de_nombres.append(nombre)

            self.lista_plato_principal.append(plato_principal)
            self.lista_bebidas_elegidas.append(bebida_principal)

            self.lista_cantidad_de_platos.append(cantidad_platos)
            self.lista_cantidad_de_bebidas.append(cantidad_bebidas)

            flag = question("Continuar", "Desea continuar cargando datos?")

    def btn_mostrar_on_click(self):
        PRECIO_BEBIDA_UNITARIO = 200
        PRECIO_PLATO_UNITARIO = 800
        total_gastado = 0
        contador_agua = 0        
        contador_jugo = 0        
        contador_refresco = 0
        acumulador_cantidad_agua = 0
        acumulador_cantidad_jugo = 0
        acumulador_cantidad_refresco = 0
        promedio_jugo = 0
        total_platos = 0
        acumulador_cantidad_pizza = 0
        acumulador_cantidad_hamburguesa = 0
        acumulador_cantidad_ensalada = 0
        nombre_persona = ""
        cantidad_persona = 0
        flag = True
        lista_vacia_1 = []
        lista_vacia_2 = []

        for i in range(len(self.lista_de_nombres)):
            nombre = self.lista_de_nombres[i]
            plato_principal = self.lista_plato_principal[i]
            bebida_principal = self.lista_bebidas_elegidas[i]
            cantidad_platos = self.lista_cantidad_de_platos[i]
            cantidad_bebidas = self.lista_cantidad_de_bebidas[i]

            #   A)  El total gastado por el grupo (resultante del costo de los platos principales y las bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al 10% del total gastado).
            total_gastado += (cantidad_bebidas*PRECIO_BEBIDA_UNITARIO) + (cantidad_platos*PRECIO_PLATO_UNITARIO)
            propina = total_gastado * 10 / 100
            total_final = propina + total_gastado

            #   B)  Promedio del dinero gastado en “Jugo”,
            match(bebida_principal):
                case "Agua":
                    contador_agua += 1
                    acumulador_cantidad_agua += cantidad_bebidas
                case "Jugo":
                    contador_jugo += 1
                    acumulador_cantidad_jugo += cantidad_bebidas
                case "Refresco":
                    contador_refresco += 1
                    acumulador_cantidad_refresco += cantidad_bebidas

            #   C)  Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
            match(plato_principal):
                case "Pizza":
                    acumulador_cantidad_pizza += cantidad_platos
                case "Hamburguesa":
                    acumulador_cantidad_hamburguesa += cantidad_platos
                case "Ensalada":
                    acumulador_cantidad_ensalada += cantidad_platos
            total_platos += cantidad_platos

            #   D)  Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total (platos principales + bebidas) con una entrada gratuita para otra atracción del parque "Aventuras Extremas".
            if(flag == True):
                nombre_persona = nombre
                cantidad_persona = cantidad_bebidas + cantidad_platos
                flag = False
            elif(cantidad_persona < (cantidad_platos + cantidad_bebidas)):
                nombre_persona = nombre
                cantidad_persona = cantidad_bebidas + cantidad_platos

            #   E)  1.Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos principales del tipo "Pizza" y mostrar la lista completa por print.
            if(plato_principal == "Pizza"):
                lista_vacia_1.append(nombre)
            
            #   E)  2.Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por print.s
            if((cantidad_bebidas + cantidad_platos) <= 5):
                lista_vacia_2.append(nombre)
            
        porcentaje_pizza = acumulador_cantidad_pizza * 100 / total_platos
        porcentaje_hamburguesa = acumulador_cantidad_hamburguesa * 100 / total_platos
        porcentaje_ensalada = acumulador_cantidad_ensalada * 100 / total_platos
        
        promedio_jugo = float((acumulador_cantidad_jugo * PRECIO_BEBIDA_UNITARIO) / contador_jugo)

        #   A)  El total gastado por el grupo (resultante del costo de los platos principales y las bebidas), y la propina sugerida para el personal del restaurante (esta corresponde al 10% del total gastado).
        alert("Respuesta", f"El total gastado por el grupo es:Gasto general: {total_gastado}\nPropina: {propina}\nFinal: {total_final}")
    
        #   B)  Promedio del dinero gastado en “Jugo”,
        alert("Respuesta", f"El promedio de jugo gastado es: {promedio_jugo:.2f}")
    
        #   C)  Los porcentajes de cada tipo de platos pedidos (teniendo en cuenta su cantidad). Ejemplo: [30% pizza, 40% ensaladas, 30% hamburguesas]
        alert("Respuesta", f"El porcentaje de platos es:\nPizza %{porcentaje_pizza:.0f}\nHamburguesa %{porcentaje_hamburguesa:.0f}\nEnsalada %{porcentaje_ensalada:.0f}")

        #   D)  Además, desean premiar al amigo que realizó la mayor CANTIDAD de pedidos en total (platos principales + bebidas) con una entrada gratuita para otra atracción del parque "Aventuras Extremas".
        alert("Respuesta", f"La persona con mayor cantidad de pedidos es\nNombre: {nombre_persona}\nCantidad: {cantidad_persona}\nGano una entrada gratuita a 'Aventuras Extremas'")

        #   E)  1.Crear una lista nueva, agregar todos los nombres de los amigos que hayan elegido platos principales del tipo "Pizza" y mostrar la lista completa por print.
        alert("Respuesta", f"Las personas que pidieron pizza son: {lista_vacia_1}")

        #   E)  2.Crear una lista nueva, agregar todos los nombres de los amigos que hayan realizado menos de 5 pedidos en total (platos principales + bebidas) y mostrar la lista completa por prints.
        alert("Respuesta", f"Las personas que realizaron menos pedidos teniendo en cuenta platos y bedidas fueron: {lista_vacia_2}")


if __name__ == "__main__":
    app = App()
    app.mainloop()