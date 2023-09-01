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

'''
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de valores.:

A) Para ello deberas programar el boton "Cargar operación" para poder cargar los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Cantidad de instrumentos
    * Tipo (CEDEAR, BONOS, MEP)   

En esta opción, se ingresaran operaciones hasta que el usuario lo desee.

B) Al presionar el boton mostrar se deberan listar todos los datos de los usuarios y su posición en la lista (por terminal) 

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.

    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, 
    si es impar, tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    En caso de que la suma sea 0, realizara el informe 7.

    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó.
    #! 1) - Tipo de instrumento que mas se operó.
    #! 2) - Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron mas de $50000.
    #! 3) - Cantidad de usuarios que no compraron BONOS y que hayan invertido entre $20000 y $100000 en la compra de 150 
            instrumentos o mas. 
    #! 4) - Nombre y cantidad de instrumentos del usuario que compro BONOS o MEP, que menos dinero invirtió. Puede ser mas de 
            uno.
    #! 5) - Nombre e instrumento de los usuarios que no invirtieron en BONOS que mas dinero invirtió. Puede ser mas de uno
            o mas instrumentos
    #! 6) - Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el monto promedio 
            (De cualquier tipo de instrumento). 
    #! 7) - Nombre de los usuarios que invirtieron en BONOS, cuya inversión supere el monto promedio 
            de ese tipo de instrumento.
    #! 8) - Porcentaje de usuarios que invirtieron en MEP, siempre y cuando el monto se encuentre entre $20000 y $50000.  
    #! 9) - Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto no supere los $50000.
'''
class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA - Rompe Cocos Capital")
        self.minsize(320, 200)

        self.label_title = customtkinter.CTkLabel(master=self, text="Rompe Cocos Capital", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)
        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Operaciones", command=self.btn_cargar_operacion_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")

        self.nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
                    "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]

        self.montos = [15000, 20000, 40000, 25000, 30000, 35000, 45000, 30000, 40000, 50000,
                    20000, 45000, 30000, 40000, 15000, 35000, 25000, 50000, 20000, 40000]

        self.cantidades_instrumentos = [120, 150, 200, 180, 250, 170, 300, 220, 190, 350,
                    110, 170, 240, 160, 210, 280, 300, 190, 230, 200]

        self.tipos_instrumento = ["CEDEAR", "BONOS", "MEP", "CEDEAR", "MEP", "BONOS", "MEP", "CEDEAR", "BONOS", "MEP",
                    "CEDEAR", "BONOS", "MEP", "CEDEAR", "BONOS", "MEP", "CEDEAR", "BONOS", "MEP", "CEDEAR"]   # 20 - 7MEP
        
        #PUEDE MODIFICAR LOS DATOS A SU ANTOJO, A EFECTOS DE REALIZAR PRUEBAS
        
    def btn_mostrar_todos_on_click(self):
        pass

    def btn_mostrar_informe_1(self):
        flag = True
        tipo_menos = ""
        cantidad_menos = 0

        for i in range(len(self.nombres)):
            cant_instrumentos = self.cantidades_instrumentos[i]
            tipo = self.tipos_instrumento[i]


            #! 0) - Tipo de instrumento que menos se operó.
            if(flag == True):
                tipo_menos = tipo
                cantidad_menos = cant_instrumentos
                flag = False
            elif(cantidad_menos > cant_instrumentos):
                tipo_menos = tipo
                cantidad_menos = cant_instrumentos

        print(tipo_menos, cantidad_menos)

    def btn_mostrar_informe_2(self):
        contador_otros = 0
        contador_general = 0
        porcentaje_no_mep = 0

        #! 9) - Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto no supere los $50000.
        for i in range(len(self.nombres)):
            pesos = self.montos[i]
            tipo = self.tipos_instrumento[i]

            if(tipo != "MEP" and pesos <= 50000):
                contador_otros += 1
            contador_general += 1
        
        porcentaje_no_mep = contador_otros * 100 / contador_general
        print(f"%{porcentaje_no_mep}")

    def btn_mostrar_informe_3(self):
        # contador_otros = 0
        # contador_mep = 0
        # porcentaje_mep = 0
        # #! 8) - Porcentaje de usuarios que invirtieron en MEP, siempre y cuando el monto se encuentre entre $20000 y $50000.

        # for i in range(len(self.nombres)):
        #     pesos = self.montos[i]
        #     tipo = self.tipos_instrumento[i]

        #     if(tipo == "MEP" and pesos >= 20000 and pesos <= 50000):
        #         contador_mep += 1
        #     contador_otros += 1

        # porcentaje_mep = float(contador_mep * 100 / contador_otros)
        # print(f"%{porcentaje_mep:.2f}")

        #! 7) - Nombre de los usuarios que invirtieron en BONOS, cuya inversión supere el monto promedio de ese tipo de instrumento.
        acumulador_bonos = 0
        contador_bonos = 0
        promedio_bonos = 0

        for i in range(len(self.nombres)):
            monto = self.montos[i]
            tipo_instrumento = self.tipos_instrumento[i]
            if(tipo_instrumento == "BONOS"):
                acumulador_bonos += monto
                contador_bonos += 1
            promedio_bonos = acumulador_bonos / contador_bonos
        for i in range(len(self.nombres)):
            monto = self.montos[i]
            tipo_instrumento = self.tipos_instrumento[i]

    def btn_cargar_operacion_on_click(self):
        nombre = ""
        pesos = 0
        cant_instrumentos = 0
        tipo = ""

        ''' 
        * Nombre
        * Monto en pesos de la operación (no menor a $10000)
        * Cantidad de instrumentos
        * Tipo (CEDEAR, BONOS, MEP)   
        '''

        nombre = prompt("Ingreso", "Por favor, ingresar un nombre")
        while(nombre == ""):
            nombre = prompt("Ingreso", "Por favor, ingresar un nombre")

        tipo = prompt("Ingreso", "Por favor, ingresar un tipo")
        while(tipo != "CEDEAR" and tipo != "MEP" and tipo != "BONOS"):
            tipo = prompt("Ingreso", "Por favor, ingresar un tipo")

        pesos = int(prompt("Ingreso", "Por favor, ingresar un monto en pesos"))
        while(pesos < 9999):
            pesos = int(prompt("Ingreso", "Por favor, ingresar un monto en pesos"))

        cant_instrumentos = int(prompt("Ingreso", "Por favor, ingresar un monto en pesos"))
        while(cant_instrumentos < 0):
            cant_instrumentos = int(prompt("Ingreso", "Por favor, ingresar un monto en pesos"))


if __name__ == "__main__":
    app = App()
    app.mainloop()

