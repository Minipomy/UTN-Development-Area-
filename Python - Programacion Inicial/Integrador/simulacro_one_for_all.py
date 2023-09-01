from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ejercicio: Simulacro examen
Alumno: Maximiliano, Rivera Mendes
Division: Div J

Enunciado:
Una vez ingresados los datos y realizadas las validaciones pertinentes se debe informar por alert:
La cantidad de aplicantes al puesto “Ssr” que sean mayores a 45 años.
El promedio de edad de los aplicantes para el puesto “Sr”.
Los porcentajes de aplicantes de cada género.
El nombre y género de la persona con más puntaje entrevistada para el puesto “Jr”.
DEBE REALIZAR DOS PUNTO EL PRIMERO CORRESPONDIENTE AL ÚLTIMO NÚMERO DE SU DNI PERSONAL (Ejemplo 4) Y EL SEGUNDO RESTANDO A 9 EL ÚLTIMO NÚMERO DE SU DNI (Ejemplo 9 - 4 = 5):

0) Crear una lista nueva, agregarle todos los Nombres de las personas del Género “M” y mostrar la lista completa por print.
1) Crear una lista nueva, agregarle todos los Nombres de las personas del Género “F” y mostrar la lista completa por print.
2) Crear una lista nueva, agregarle todos los Nombres de las personas del Género “NB” y mostrar la lista completa por print.
3) Crear una lista nueva, agregarle todos los Nombres de las personas con puesto “Jr” y mostrar la lista completa por print.
4) Crear una lista nueva, agregarle todos los Nombres de las personas con puesto “Sr” y mostrar la lista completa por print.
5) Crear una lista nueva, agregarle todos los Nombres de las personas con puntajes mayores a 250 y mostrar la lista completa por print.
6) Crear una lista nueva, agregarle todos los Nombres de las personas con puntajes mayores a 500 y mostrar la lista completa por print..
7) Crear una lista nueva, agregarle todos los Nombres de las personas con puntajes mayores a 750 y mostrar la lista completa por print.
8) Crear una lista nueva, agregarle todos los Nombres de las personas con puntajes menores a 500 y mostrar la lista completa por print.
9) Crear una lista nueva, agregarle todos los Nombres de las personas con puntajes menores a 250 y mostrar la lista completa por print.

'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_agregar = customtkinter.CTkButton(
            master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=0, column=0, pady=10, padx=10)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, column=0, pady=10, padx=10)

        self.lista_nombre = ["Ale", "Vale", "David", "Caro", "Javier"]
        self.lista_edad = [28, 47, 29, 45, 70]
        self.lista_genero = ["M", "M", "M", "F", "NB"]
        self.lista_puntaje = [550, 600, 250, 900, 200]
        self.lista_puesto = ["Ssr", "Ssr", "Sr", "Sr", "Jr"]


    def btn_agregar_on_click(self):
        #   Variables TypeString
        nombre = ""
        genero = ""
        puesto = ""
        edad = 0
        puntaje = 0
        #   Variable Flag
        flag = True

        while(flag != False):

            nombre = prompt("Ingrese nombre", "Por favor, ingresar un nombre: ")
            while(nombre == ""):
                nombre = prompt("Ingrese nombre", "Por favor, ingresar un nombre: ")

            edad = int(prompt("Ingrese edad", "Por favor, ingresar una edad: "))
            while(edad < 18 and edad > 90):
                edad = int(prompt("Ingrese edad", "Por favor, ingresar una edad: "))

            genero = prompt("Ingrese genero", "Por favor, ingresar el genero de la persona (M,F,NB): ")
            while(genero != "M" and genero != "F" and genero != "NB"):
                genero = prompt("Ingrese genero", "Por favor, ingresar el genero de la persona (M,F,NB): ")

            puntaje = int(prompt("Ingrese puntaje", "Por favor, ingresar el puntaje: "))
            while(puntaje < 0 and puntaje > 1000):
                puntaje = int(prompt("Ingrese puntaje", "Por favor, ingresar el puntaje: "))

            puesto = prompt("Ingrese puesto", "Por favor, ingresarel puesto (Ssr, Sr, Jr): ")
            while(puesto != "Ssr" and puesto != "Sr" and puesto != "Jr"):
                puesto = prompt("Ingrese puesto", "Por favor, ingresarel puesto (Ssr, Sr, Jr): ")
            
            self.lista_nombre.append(nombre)
            self.lista_edad.append(edad)
            self.lista_genero.append(genero)
            self.lista_puntaje.append(puntaje)
            self.lista_puesto.append(puesto)

            flag = question("Continuar", "Desea continuar cargando datos?")
            


    def btn_mostrar_on_click(self):
        acumulador_aplicantes_ssr_mayores = 0
        contador_jr = 0
        contador_sr = 0
        contador_ssr = 0
        contador_total_puestos = 0
        acumulador_edad_sr = 0
        promedio_edad = 0
        contador_m = 0
        contador_f = 0
        contador_nb = 0
        contador_total_generos = 0
        nombre_persona = ""
        genero_persona = ""
        highscore = 0
        mensaje = ""
        lista_vacia_1 = []
        lista_vacia_2 = []
        flag = True


        for i in range(len(self.lista_nombre)):
            nombre = self.lista_nombre[i]
            edad = self.lista_edad[i]
            genero = self.lista_genero[i]
            puntaje = self.lista_puntaje[i]
            puesto = self.lista_puesto[i]


            match(puesto):
                case "Jr":
                    contador_jr += 1
                case "Sr":
                    contador_sr += 1
                    acumulador_edad_sr += edad
                case "Ssr":
                    contador_ssr += 1
                    #   A)  La cantidad de aplicantes al puesto “Ssr” que sean mayores a 45 años.
                    if(edad >= 45):
                        acumulador_aplicantes_ssr_mayores += 1
            contador_total_puestos += 1
            
            #   Los porcentajes de aplicantes de cada género.
            match(genero):
                case "M":
                    contador_m += 1
                    #   E)  0) Crear una lista nueva, agregarle todos los Nombres de las personas del Género “M” y mostrar la lista completa por print.
                    lista_vacia_1.append(nombre)
                case "F":
                    contador_f += 1
                case "NB":
                    contador_nb += 1
            contador_total_generos += 1

            #   El nombre y género de la persona con más puntaje entrevistada para el puesto “Jr”.
            if(flag == True and puesto == "Jr"):
                nombre_persona = nombre
                genero_persona = genero
                highscore = puntaje
                mensaje = f"El nombre y genero de la persona con mayor puntaje es:\nNombre: {nombre_persona}\nGenero: {genero_persona}\nPuntaje: {highscore}"
                flag = False
            elif(highscore < puntaje and puesto == "Jr"):
                nombre_persona = nombre
                genero_persona = genero
                highscore = puntaje
                mensaje = f"El nombre y genero de la persona con mayor puntaje es:\nNombre: {nombre_persona}\nGenero: {genero_persona}\nPuntaje: {highscore}"
            else:
                mensaje = "No aplico ninguna persona"

            #   E)  9) Crear una lista nueva, agregarle todos los Nombres de las personas con puntajes menores a 250 y mostrar la lista completa por print.
            if(puntaje <= 250):
                lista_vacia_2.append(nombre)
                lista_vacia_2.append(puntaje)

        porcentaje_m = contador_m * 100 / contador_total_puestos
        porcentaje_f = contador_f * 100 / contador_total_puestos
        porcentaje_nb = contador_nb * 100 / contador_total_puestos

        promedio_edad = acumulador_edad_sr / contador_sr
        
        #   A)  La cantidad de aplicantes al puesto “Ssr” que sean mayores a 45 años.
        alert("Respuesta", f"La cantidad de aplicantes al puesto “Ssr” que sean mayores a 45 años. {acumulador_aplicantes_ssr_mayores}")
        
        #   B)  El promedio de edad de los aplicantes para el puesto “Sr”.
        alert("Respuesta", f"El promedio de edad de los aplicantes para el puesto Sr {promedio_edad}")
        
        #   C)  Los porcentajes de aplicantes de cada género.
        alert("Respuesta", f"El porcentaje de generos que aplicaron:\nMasculinos %{porcentaje_m:.0f}\nFemeninos: %{porcentaje_f:.0f}\nNoBinarios: %{porcentaje_nb:.0f}")
        
        #   D)  El nombre y género de la persona con más puntaje entrevistada para el puesto “Jr”.
        alert("Respuesta", mensaje)
        
        #   E)  0) Crear una lista nueva, agregarle todos los Nombres de las personas del Género “M” y mostrar la lista completa por print.
        alert("Respuesta", f"Aplicantes de tipo masculino: {lista_vacia_1}")
        
        #   E)  9) Crear una lista nueva, agregarle todos los Nombres de las personas con puntajes menores a 250 y mostrar la lista completa por print.
        alert("Respuesta", f"Aplicantes con puntajes menor a 250: {lista_vacia_2}")

print(__name__)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
