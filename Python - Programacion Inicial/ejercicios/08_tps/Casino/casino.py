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
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar= customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        


    def btn_cargar_on_click(self):
        # ganadores = []
        # nombre = ""
        # genero = ""
        # dinero_ganado = 0
        # juego = ""
        # flag = True

        maximo = 0
        minimo = 0
        contador_poker = 0
        contador_ruleta = 0
        contador_tragamonedas = 0
        nombre_mayor_dinero = 0
        genero_mayor_dinero = 0
        #   porcentaje_ruleta = 0
        total_juegos = 0
        ganadores = [["Maxi", "Masculino", 19000, "Poker"],["Cata", "Femenino", 14000, "Ruleta"],["Maxi", "Masculino", 50000, "Tragamonedas"],["Cata", "Femenino", 80000, "Poker"], ["Lucas", "Masculino", 19000, "Poker"],["Lucas", "Masculino", 75000, "Tragamonedas"]]
        flag = True

        while(flag != False):
            #  <Cargo NOMBRE, GENERO, DINERO_GANADO Y JUEGO en una lista>
            nombre = prompt("Ingresar nombre", "Por favor, ingrese un nombre:")
            if(nombre == None):
                break
            genero = prompt("Ingresar Genero", "Por favor, ingrese NUMERO del Genero:")
            if(genero == None):
                break
            dinero_ganado = prompt("Ingresar dinero", "Por favor, ingresar el dinero ganado")
            if(dinero_ganado == None):
                break
            juego = prompt("Ingresar juego", "Por favor, ingresar el NUMERO del juego ganado")
            if(juego == None):
                break            
            ganadores.append([nombre, genero, dinero_ganado, juego])
            #   fin </Cargo NOMBRE, GENERO, DINERO_GANADO Y JUEGO en una lista>

            flag = question("Continuar cargando?", "Desea ingresar mas ganadores?")
        


        #   Contadores Globales que definen total de juegos y sus cantidades separas
        for popular in ganadores:
            if(popular[3] == "Poker"): 
                contador_poker += 1
                total_juegos += 1
            elif(popular[3] == "Ruleta"): 
                contador_ruleta += 1
                total_juegos += 1
            elif(popular[3] == "Tragamonedas"): 
                contador_tragamonedas += 1
                total_juegos += 1


        #   A) El nombre y el género de la persona que más dinero ganó.

        for nombre, genero, dinero in ganadores:
            if(dinero[2] >= maximo):
                if(minimo == 0 or minimo > dinero[2]):
                    minimo = dinero[2]
                maximo = dinero[2]
                nombre_mayor_dinero = nombre[0]
                genero_mayor_dinero = genero[1]
            if(minimo > dinero[2]):
                    minimo = dinero[2]
        print(nombre_mayor_dinero, genero_mayor_dinero)

        #   b) El promedio del dinero ganado en las mesas de Poker.
        if(contador_poker > 0):
            promedio_poker = float(total_dinero_poker/contador_poker)
        else:
            promedio_poker = 0
        
        #   c) El porcentaje de personas que ganaron en la Ruleta.
        #   porcentaje_ruleta = contador_ruleta/total_juegos * 100

        #   e) Cuál de los tres juegos es el más popular entre las personas ganadoras.
        if(contador_poker >= contador_ruleta):
            popular = "Poker"
            if(contador_poker < contador_tragamonedas):
                popular = "Tragamonedas"
        else:
            popular = "Ruleta"
            if(contador_ruleta < contador_tragamonedas):
                popular = "Tragamonedas"
                

        alert("Respuesta", f"{ganadores} {maximo}")

if __name__ == "__main__":
    app = App()
    app.mainloop()    