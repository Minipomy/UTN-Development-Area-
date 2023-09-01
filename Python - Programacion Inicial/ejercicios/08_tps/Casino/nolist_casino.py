import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''

Nombre: Maximiliano
Apellido: Rivera Mendes

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
        #   Variables TypeString
        nombre = ""
        juego = ""
        genero = ""
        nombre_mayor_dinero = ""
        genero_mayor_dinero = ""
        #   Variables TypeInt
        dinero_ingresado = 0
        total_dinero_poker = 0
        total_dinero_ruleta = 0
        total_dinero_tragamonedas = 0
        contador_poker = 0
        contador_ruleta = 0
        contador_tragamonedas = 0
        contador_persona= 0
        contador = 0
        maxima = 0
        minima = 0
        total_juegos = 0
        #   Variables TypeBool
        flag = True

        while(flag != False):
            
            juego = prompt("Ingresar juego", "Por favor, ingresar nombre del juego ganado")
            if(juego == None):
                break
            match(juego):
                case "Poker":
                    nombre = prompt("Ingresar nombre", "Por favor, ingrese un nombre:")
                    if(nombre == None):
                        break
                    genero = prompt("Ingresar Genero", "Por favor, ingrese el Genero:")
                    if(genero == None):
                        break
                    dinero_ingresado = prompt("Ingresar dinero", "Por favor, ingresar el dinero ganado")
                    if(dinero_ingresado == None):
                        break
                    total_dinero_poker += int(dinero_ingresado)
                    contador_poker += 1

                case "Ruleta":
                    nombre = prompt("Ingresar nombre", "Por favor, ingrese un nombre:")
                    if(nombre == None):
                        break
                    genero = prompt("Ingresar Genero", "Por favor, ingrese el Genero:")
                    if(genero == None):
                        break
                    dinero_ingresado = prompt("Ingresar dinero", "Por favor, ingresar el dinero ganado")
                    if(dinero_ingresado == None):
                        break
                    total_dinero_ruleta += int(dinero_ingresado)
                    contador_ruleta += 1
                    
                case "Tragamonedas":    
                    nombre = prompt("Ingresar nombre", "Por favor, ingrese un nombre:")
                    if(nombre == None):
                        break                    
                    genero = prompt("Ingresar Genero", "Por favor, ingrese el Genero:")
                    if(genero == None):
                        break
                    dinero_ingresado = prompt("Ingresar dinero", "Por favor, ingresar el dinero ganado")
                    if(dinero_ingresado == None):
                        break
                    total_dinero_tragamonedas += int(dinero_ingresado)
                    contador_tragamonedas += 1
                    #   d) La cantidad de ganadores del género masculino que ganaron más de $50000 en los Tragamonedas.
                    if(genero == "Masculino" and juego == "Tragamonedas" and int(dinero_ingresado) >= 50000):
                        contador += 1
                    

            #   Variables Globales
            total_juegos += 1
            contador_persona += 1
            
            # #   a) El nombre y el género de la persona que más dinero ganó.
            if(int(dinero_ingresado) > maxima):
                if(minima == 0 or minima > int(dinero_ingresado)):
                    minima = int(dinero_ingresado)
                maxima = int(dinero_ingresado)
                nombre_mayor_dinero = nombre
                genero_mayor_dinero = genero
            
            #   b) El promedio del dinero ganado en las mesas de Poker.
            if(contador_poker > 0):
                promedio_poker = float(total_dinero_poker/contador_poker)
            else:
                promedio_poker = 0

            #   c) El porcentaje de personas que ganaron en la Ruleta.
            porcentaje_ruleta = float(contador_ruleta / total_juegos * 100)

            #   e) Cuál de los tres juegos es el más popular entre las personas ganadoras.
            if(contador_poker >= contador_ruleta):
                popular = "Poker"
                if(contador_poker < contador_tragamonedas):
                    popular = "Tragamonedas"
            else:
                popular = "Ruleta"
                if(contador_ruleta < contador_tragamonedas):
                    popular = "Tragamonedas"

            flag = question("Continuar cargando?", "Desea ingresar mas ganadores?")
            
        alert("Respuesta final", f"A) la persona con mas dinero que gano es:{nombre_mayor_dinero} {genero_mayor_dinero} ${maxima}\nB)El promedio del dinero ganado en Poker es de: {promedio_poker:.2f}\nC)El porcentaje de personas que ganaron en la ruleta es de: %{porcentaje_ruleta:.0f}\nD)El numero de ganadores Masculinos en el tragamonedas mayores a $50.000 pesos es de: {contador}\nEl juego mas popular es {popular}")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()    