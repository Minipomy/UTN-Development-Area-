import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Para un casino ubicado en Mar del Plata, cargar a las
personas ganadoras, hasta que el usuario quiera e informar:
- Nombre,
- Dinero Ganado,
- Género ("Masculino", "Femenino", "Otro"),
- Juego ("Poker", "Ruleta", "Tragamonedas")
a) El nombre y el género de la persona que más dinero ganó.
b) El promedio del dinero ganado en las mesas de Poker.
c) El porcentaje de personas que ganaron en la Ruleta.
d) La cantidad de ganadores del género masculino que
ganaron más de $50000 en los Tragamonedas.
e) Cuál de los tres juegos es el más popular entre las
personas ganadoras.

DEBE REALIZAR DOS PUNTO EL PRIMERO CORRESPONDIENTE AL ÚLTIMO NÚMERO DE SU DNI PERSONAL (Ejemplo 4) Y EL SEGUNDO RESTANDO A 9 EL ÚLTIMO NÚMERO DE SU DNI (Ejemplo 9 - 4 = 5):

0) Crear una lista nueva, agregarle todos los Nombres de las personas del Género “M” y mostrar la lista completa por print.
1) Crear una lista nueva, agregarle todos los Nombres de las personas del Género “F” y mostrar la lista completa por print.
2) Crear una lista nueva, agregarle todos los Nombres de las personas del Género “NB” y mostrar la lista completa por print.
3) Crear una lista nueva, agregarle todos los Nombres de las personas que ganaron en “Poker” y mostrar la lista completa por print.
4) Crear una lista nueva, agregarle todos los Nombres de las personas que ganaron en “Tragamonedas” y mostrar la lista completa por print.
5) Crear una lista nueva, agregarle todos los Nombres de las personas con monto mayores a 25000 y mostrar la lista completa por print.
6) Crear una lista nueva, agregarle todos los Nombres de las personas con monto mayores a 50000 y mostrar la lista completa por print..
7) Crear una lista nueva, agregarle todos los Nombres de las personas con monto mayores a 75000 y mostrar la lista completa por print.
8) Crear una lista nueva, agregarle todos los Nombres de las personas con monto menores a 50000 y mostrar la lista completa por print.
9) Crear una lista nueva, agregarle todos los Nombres de las personas con monto menores a 25000 y mostrar la lista completa por print.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=0, column=0, pady=10, padx=10)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, column=0, pady=10, padx=10)

        self.nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
                    "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]

        self.montos = [15000, 20000, 40000, 25000, 30000, 35000, 45000, 30000, 40000, 50000,
                    20000, 45000, 30000, 40000, 15000, 35000, 25000, 50000, 20000, 40000]
        
        self.generos = ["M", "F", "NB","M", "F", "NB","M", "F", "NB","M", "F", "NB","M", "F", "NB","M", "F", "NB","M", "F"]

        self.juegos = ["Poker", "Ruleta", "Tragamonedas","Poker", "Ruleta", "Tragamonedas","Poker", "Ruleta", "Tragamonedas",
                       "Poker", "Ruleta", "Tragamonedas","Poker", "Ruleta", "Tragamonedas","Poker", "Ruleta", "Tragamonedas",
                       "Poker", "Ruleta"]

    def btn_agregar_on_click(self):
        flag = True
        nombre = "" 
        genero = ""
        juego = ""
        monto = 0

        while(flag != False):

            nombre = prompt("Ingreso", "Ingresar nombre:")
            while(nombre == ""):
                nombre = prompt("Ingreso", "Ingresar nombre:")

            genero = prompt("Ingreso", "Ingresar genero:")
            while(genero != "M" and genero != "F" and genero != "NB"):
                genero = prompt("Ingreso", "Ingresar genero:")

            juego = prompt("Ingreso", "Ingresar juego:")
            while(juego != "Poker" and juego != "Ruleta" and juego != "Tragamonedas"):
                juego = prompt("Ingreso", "Ingresar juego:")

            monto = int(prompt("Ingreso", "Ingresar monto:"))
            while(monto >= 10000):
                monto = int(prompt("Ingreso", "Ingresar monto:"))

            self.nombres.append(nombre)
            self.generos.append(genero)
            self.juegos.append(juego)
            self.montos.append(monto)
            
            flag = question("Continuar", "Desea seguir cargando datos?")


    def btn_mostrar_on_click(self):
        flag = True
        persona_highscore = ""
        genero_highscore = ""
        popular = ""
        monto_highscore = 0
        contador_general = 0
        contador_poker = 0
        contador_ruleta = 0
        contador_tragamonedas = 0
        porcentaje_ruleta = 0
        acumulador_monto_poker = 0
        promedio_dinero_poker = 0
        contador_masculinos = 0
        lista_masculinos_tragamonedas = []
        lista_1 = []
        lista_2 = []

        for i in range(len(self.nombres)):
            nombre = self.nombres[i]
            genero = self.generos[i]
            monto = self.montos[i]
            juego = self.juegos[i]

            #   A) El nombre y el género de la persona que más dinero ganó.
            if(flag != False):
                persona_highscore = nombre
                genero_highscore = genero
                monto_highscore = monto
                flag = False
            elif(monto > monto_highscore):
                persona_highscore = nombre
                genero_highscore = genero
                monto_highscore = monto
            
            
            #   B) El promedio del dinero ganado en las mesas de Poker.
            match(juego):
                case "Poker":
                    contador_poker += 1
                    acumulador_monto_poker += monto
                case "Ruleta":
                    contador_ruleta += 1
                case "Tragamonedas":
                    contador_tragamonedas += 1
                    if(genero == "M" and monto >= 50000):
                        contador_masculinos += 1
                        lista_masculinos_tragamonedas.append(nombre)
            contador_general += 1

            #   0) Crear una lista nueva, agregarle todos los Nombres de las personas del Género “M” y mostrar la lista completa por print.
            if(genero == "M"):
                lista_1.append(nombre)
            
            #   9) Crear una lista nueva, agregarle todos los Nombres de las personas con monto menores a 25000 y mostrar la lista completa por print.
            if(monto <= 25000):
                lista_2.append(nombre)
                lista_2.append(monto)

        promedio_dinero_poker = acumulador_monto_poker / contador_poker
        #   C)  El porcentaje de personas que ganaron en la Ruleta.
        porcentaje_ruleta = contador_ruleta * 100 / contador_general

        print("Acumulador_poker",acumulador_monto_poker)
        #   E) Cuál de los tres juegos es el más popular entre las personas ganadoras.
        if(contador_poker >= contador_ruleta and contador_poker >= contador_tragamonedas):
            popular = "Poker"
        elif(contador_ruleta >= contador_tragamonedas):
            popular = "Ruleta"
        else:
            popular = "Tragamonedas"

        #   A) El nombre y el género de la persona que más dinero ganó.
        print("Respuesta", "El nombre y el género de la persona que más dinero ganó.", persona_highscore, genero_highscore, monto_highscore) 
        
        #   B) El promedio del dinero ganado en las mesas de Poker.
        print("Respuesta", "El promedio del dinero ganado en las mesas de Poker.", promedio_dinero_poker) 
        
        #   C)  El porcentaje de personas que ganaron en la Ruleta.
        print("Respuesta", "El porcentaje de personas que ganaron en la Ruleta", porcentaje_ruleta) 
        
        #   D) La cantidad de ganadores del género masculino que ganaron más de $50000 en los Tragamonedas.
        print("Respuesta", "La cantidad de ganadores del género masculino que ganaron más de $50000 en los Tragamonedas", contador_masculinos, lista_masculinos_tragamonedas)

        #   E) Cuál de los tres juegos es el más popular entre las personas ganadoras.
        print("Respuesta", "el más popular entre las personas ganadoras es:", popular)

        #   0) Crear una lista nueva, agregarle todos los Nombres de las personas del Género “M” y mostrar la lista completa por print.
        print("Respuesta", "Las personas masculinas son:", lista_1) 
        #   9) Crear una lista nueva, agregarle todos los Nombres de las personas con monto menores a 25000 y mostrar la lista completa por print.
        print("Respuesta", "Las personas con montos menores a 25000 son:", lista_2)

if __name__ == "__main__":
    app = App()
    app.mainloop()    