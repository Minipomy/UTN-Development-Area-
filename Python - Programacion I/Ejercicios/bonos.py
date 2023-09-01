# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "Maximiliano" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

B) Al presionar el botón mostrar 
    
    Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal) 

# IMPORTANTE:
Del punto C solo deberá realizar SOLAMENTE 2 informes. 
(PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
no es necesario validar que no haya nombres repetidos)

Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4)

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)


        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=1, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_0 = customtkinter.CTkButton(master=self, text="Informe 0", command=self.btn_mostrar_informe_0)
        self.btn_informe_0.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_4 = customtkinter.CTkButton(master=self, text="Informe 4", command=self.btn_mostrar_informe_4)
        self.btn_informe_4.grid(row=7, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_5 = customtkinter.CTkButton(master=self, text="Informe 5", command=self.btn_mostrar_informe_5)
        self.btn_informe_5.grid(row=8, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_6 = customtkinter.CTkButton(master=self, text="Informe 6", command=self.btn_mostrar_informe_6)
        self.btn_informe_6.grid(row=9, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_7 = customtkinter.CTkButton(master=self, text="Informe 7", command=self.btn_mostrar_informe_7)
        self.btn_informe_7.grid(row=10, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_8 = customtkinter.CTkButton(master=self, text="Informe 8", command=self.btn_mostrar_informe_8)
        self.btn_informe_8.grid(row=11, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_9 = customtkinter.CTkButton(master=self, text="Informe 9", command=self.btn_mostrar_informe_9)
        self.btn_informe_9.grid(row=12, pady=10, columnspan=2, sticky="nsew")
    
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS

        self.nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
                    "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]

        self.montos = [15000, 20000, 40000, 25000, 30000, 35000, 45000, 30000, 40000, 50000,
                    20000, 45000, 30000, 40000, 15000, 35000, 25000, 50000, 20000, 40000]

        self.cantidades_instrumentos = [120, 150, 200, 180, 250, 170, 300, 220, 190, 350,
                    110, 170, 240, 160, 210, 280, 300, 190, 230, 200]

        self.tipos_instrumento = ["CEDEAR", "BONOS", "MEP", "CEDEAR", "MEP", "BONOS", "MEP", "CEDEAR", "BONOS", "MEP",
                    "CEDEAR", "BONOS", "MEP", "CEDEAR", "BONOS", "MEP", "CEDEAR", "BONOS", "MEP", "CEDEAR"]   # 20 - 7MEP
        
    def btn_mostrar_todos_on_click(self):
        pass
    
    def btn_mostrar_informe_0(self):
        #!   0) - Tipo de instrumento que menos se operó en total.
        ULTIMO_NUMERO_DNI = 0
        cantidad_menor = 0 
        tipo = 0
        flag = True

        for i in range(len(self.nombres)):
            cantidad = self.cantidades_instrumentos[i]
            tipo = self.tipos_instrumento[i]
            if(flag == True):
                cantidad_menor = cantidad
                tipo_menor = tipo
                flag = False
            elif(cantidad_menor >= cantidad):
                cantidad_menor = cantidad
                tipo_menor = tipo
        print(f"El instrumento menos operado es\nTIPO: {tipo_menor}\nCANTIDAD: {cantidad_menor}")

    def btn_mostrar_informe_1(self):
        #   Informe 1 - Se deberán listar todos los datos de los usuarios y su posición en la lista (por terminal)

        for i in range(len(self.nombres)):
            print(f"NOMBRE: {self.nombres[i]}", f"MONTO: {self.montos[i]}", f"CANTIDAD: {self.cantidades_instrumentos[i]}", f"TIPO: {self.tipos_instrumento[i]}\n")

    def btn_mostrar_informe_2(self):
        pass
    def btn_mostrar_informe_3(self):
        pass
    def btn_mostrar_informe_4(self):
        pass

    def btn_mostrar_informe_5(self):
        #! 5) - Nombre y posicion de la persona que menos BONOS compro
        flag = True

        for i in range(len(self.nombres)):
            if(flag == True):
                posicion = i
                flag = False
            elif(self.cantidades_instrumentos[posicion] >= self.cantidades_instrumentos[i]):
                posicion = i
        print(f"POSICION: {posicion}", 
              f"NOMBRE: {self.nombres[posicion]}", 
              f"TIPO: {self.tipos_instrumento[posicion]}", 
              f"CANT: {self.cantidades_instrumentos[posicion]}") 

    def btn_mostrar_informe_6(self):
        #! 6) - Nombre y posicion del usuario que invirtio menos dinero
        flag = True

        for i in range(len(self.nombres)):
            if(flag == True):
                posicion = i
                flag = False
            elif(self.montos[posicion] >= self.montos[i]):
                posicion = i
        print(f"POSICION: {posicion}", 
              f"NOMBRE: {self.nombres[posicion]}", 
              f"TIPO: {self.tipos_instrumento[posicion]}", 
              f"MONTO: {self.montos[posicion]}")

    def btn_mostrar_informe_7(self):
        #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
        flag = True

        for i in range(len(self.nombres)):
            if(flag == True):
                posicion = i
                flag = False
            elif(self.cantidades_instrumentos[posicion] <= self.cantidades_instrumentos[i]):
                posicion = i
        print(f"POSICION: {posicion}", 
              f"NOMBRE: {self.nombres[posicion]}", 
              f"TIPO: {self.tipos_instrumento[posicion]}", 
              f"CANT: {self.cantidades_instrumentos[posicion]}")
    
    def btn_mostrar_informe_8(self):
        #! 8) - Promedio de dinero en CEDEAR  ingresado en total.
        promedio_cedear = 0
        contador_cedear = 0
        acumulador_cantidad_instrumentos = 0
        for i in range(len(self.nombres)):
            cantidad = self.cantidades_instrumentos[i]
            tipo = self.tipos_instrumento[i]
            if(tipo == "CEDEAR"):
                acumulador_cantidad_instrumentos += cantidad
                contador_cedear += 1
                print(f"CANT: {cantidad}",f"ACU: {acumulador_cantidad_instrumentos}", f"CONTADOR ACTUAL: {contador_cedear}")
        
        promedio_cedear = acumulador_cantidad_instrumentos / contador_cedear
        print(f"El promedio es: {promedio_cedear:.2f}")


    def btn_mostrar_informe_9(self):
        #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total

        promedio_mep = 0
        contador_mep = 0
        acumulador_cantidad_instrumentos = 0
        for i in range(len(self.nombres)):
            cantidad = self.cantidades_instrumentos[i]
            tipo = self.tipos_instrumento[i]
            if(tipo == "MEP"):
                acumulador_cantidad_instrumentos += cantidad
                contador_mep += 1
                print(f"CANT: {cantidad}",f"ACU: {acumulador_cantidad_instrumentos}", f"CONTADOR ACTUAL: {contador_mep}")
        
        promedio_mep = acumulador_cantidad_instrumentos / contador_mep
        print(f"El promedio es: {promedio_mep:.2f}")

    def btn_cargar_datos_on_click(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
