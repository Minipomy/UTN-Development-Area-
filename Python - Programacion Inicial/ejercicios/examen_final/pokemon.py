
import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
#El profesor OAK de pueblo paleta quiere que construyas un modelo prototipico de pokedex con algunos pokemones de prueba.

A) Para ello deberas programar el boton "Cargar Pokedex" para poder cargar 10 pokemones.
Los datos que deberas pedir para los pokemones son:
    * El nombre del pokemon
    * El tipo de su elemento (Agua, Psiquico, Fuego)
    * Poder de ataque (validar que sea mayor a 50 y menor a 200)
B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) 
y mostrar los informe del punto C.

Del punto C solo debera realizar 3 informes. Para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    Informe 1- Tome el ultimo numero de su DNI Personal (Ej 4) y realice ese informe (Ej, Realizar informe 4)

    Informe 2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). En caso de que su DNI 
    finalice con el numero 0, debera realizar el informe 9.
    
    Informe 3- Tome la suma de los ultimos dos numeros de su DNI personal, en caso de ser un numero par, tomara el numero par 
    mas chico que su ultimo digito del DNI (en caso de que su ultimo digito sea 2, resolvera el ejercicio 8). En caso contrario, si es impar, 
    tomara el numero impar posterior (en caso de que su ultimo digito sea 9, resolvera el ejercicio 1)
    En caso de que el numero sea el mismo obtenido en el informe 2, realizara el siguiente informe en la lista.
    
    
    Realizar los informes correspondientes a los numeros obtenidos. EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
    #! 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.
    #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
    #! 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.
    #! 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
    #! 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).
    #! 6) - tipo de los pokemones del tipo que mas pokemones posea. 
    #! 7) - tipo de los pokemones del tipo que menos pokemones posea. 
    #! 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.
    #! 9) - el promedio de poder de todos los pokemones de tipo Psiquico.
   
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA - Pokedex")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text="Pokedex", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar Pokedex", command=self.btn_cargar_pokedex_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        self.btn_mostrar_todos = customtkinter.CTkButton(master=self, text="Mostrar todos", command=self.btn_mostrar_todos_on_click)
        self.btn_mostrar_todos.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_1 = customtkinter.CTkButton(master=self, text="Informe 1", command=self.btn_mostrar_informe_1)
        self.btn_informe_1.grid(row=4, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_2 = customtkinter.CTkButton(master=self, text="Informe 2", command=self.btn_mostrar_informe_2)
        self.btn_informe_2.grid(row=5, pady=10, columnspan=2, sticky="nsew")
        self.btn_informe_3 = customtkinter.CTkButton(master=self, text="Informe 3", command=self.btn_mostrar_informe_3)
        self.btn_informe_3.grid(row=6, pady=10, columnspan=2, sticky="nsew")
        # Cargar aca los pokemones
        self.lista_nombre_pokemones = ["Squirtle", "Psyduck", "Vaporeon", "Charizard", "Psyduck", "Vaporeon", "Squirtle", "Mewtwo", "Charizard", "Vaporeon"]
        self.lista_poder_pokemones = [90, 70, 150, 160, 70, 180, 100, 200, 170, 160]
        self.lista_tipo_pokemones = ["Agua", "Psiquico", "Agua", "Fuego", "Psiquico", "Agua", "Agua", "Psiquico", "Fuego", "Agua"]

    def btn_mostrar_todos_on_click(self):
        #   B) Al presionar el boton mostrar se deberan listar los pokemones y su posicion en la lista (por terminal) y mostrar los informe del punto C.
        mensaje = ""
        lista_for = []
        for i in range(len(self.lista_nombre_pokemones)):
            nombre_pokemon = self.lista_nombre_pokemones[i]
            poder_pokemon = self.lista_poder_pokemones[i]
            tipo_pokemon = self.lista_tipo_pokemones[i]
            contador = i+1
            
            alert("Respuesta", f"{nombre_pokemon} y su posicion: {contador}")
    
    def btn_mostrar_informe_1(self):        #! 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.
        AUMENTO_PODER = 10 / 100
        acumulador_pokemon = 0
        for i in range(len(self.lista_nombre_pokemones)):
            tipo_pokemon = self.lista_tipo_pokemones[i]
            poder_pokemon = self.lista_poder_pokemones[i]
            if(tipo_pokemon == "Fuego" and poder_pokemon + (poder_pokemon * AUMENTO_PODER) >= 100):
                acumulador_pokemon += 1

        alert("Respuesta", f"La cantidad de pokemones de tipo Fuego son: {acumulador_pokemon}")


    def btn_mostrar_informe_2(self):
        #       #! 9) - el promedio de poder de todos los pokemones de tipo Psiquico.
        contador_psiquico = 0
        acumulador_poder = 0
        promedio_psiquico = 0
        for i in range(len(self.lista_nombre_pokemones)):
            tipo_pokemon = self.lista_tipo_pokemones[i]
            poder_pokemon = self.lista_poder_pokemones[i]
            if(tipo_pokemon == "Psiquico"):
                contador_psiquico += 1

            acumulador_poder += poder_pokemon
            if(contador_psiquico > 0):
                promedio_psiquico = float(poder_pokemon / contador_psiquico ) 
        alert("Respuesta", f"{promedio_psiquico:.2f}")
    
    def btn_mostrar_informe_3(self):
        #       #! 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.
        for i in range(len(self.lista_nombre_pokemones)):
            nombre_pokemon = self.lista_nombre_pokemones[i]
            tipo_pokemon = self.lista_tipo_pokemones[i]
            poder_pokemon = self.lista_poder_pokemones[i]
            flag = True

            if(flag != False and tipo_pokemon == "Agua"):
                nombre_high = nombre_pokemon
                poder_high = poder_pokemon
                flag = True
            elif(poder_pokemon >= poder_high and tipo_pokemon == "Agua"):
                nombre_high = nombre_pokemon
                poder_high = poder_pokemon
        alert("Respuesta", f"El pokemon de agua con el poder mas alto es: {nombre_high} {poder_high}")
    
    def btn_cargar_pokedex_on_click(self):
        alert("carga","carga")

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
