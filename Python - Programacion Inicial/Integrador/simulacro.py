from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ejercicio: Simulacro examen
Alumno: Maximiliano, Rivera Mendes
Division: Div J

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
        self.lista_puntaje = [550, 600, 700, 900, 200]
        self.lista_puesto = ["Ssr", "Jr", "Jr", "Sr", "Jr"]


    def btn_agregar_on_click(self):
        #   Variables TypeString
        nombre = ""
        genero = ""
        puesto = ""
        #   Variables TypeInt
        edad = ""
        puntaje = 0
        #   Variable Flag
        flag = True

        while(flag != False):

            nombre = prompt("Ingrese nombre", "Por favor, ingresar un nombre: ")
            while(nombre == "" or nombre == None):
                nombre = prompt("Ingrese nombre", "Por favor, ingresar un nombre: ")
                if(nombre == None):
                    break
            edad = prompt("Ingrese edad", "Por favor, ingresar una edad: ")
            while(edad == "" or edad == None):
                edad = prompt("Ingrese edad", "Por favor, ingresar una edad: ")
                if(edad == None):
                    break
            genero = prompt("Ingrese genero", "Por favor, ingresar el genero de la persona (M,F,NB): ")
            while(not (genero == "M" or genero == "F" or genero == "NB")):
                genero = prompt("Ingrese genero", "Por favor, ingresar el genero de la persona (M,F,NB): ")
                if(genero == None):
                    break
            puntaje = prompt("Ingrese puntaje", "Por favor, ingresar el puntaje: ")
            while(puntaje == ""):
                puntaje = prompt("Ingrese puntaje", "Por favor, ingresar el puntaje: ")
                if(puntaje == None):
                    break
            puesto = prompt("Ingrese puesto", "Por favor, ingresarel puesto (Ssr, Sr, Jr): ")
            while(not (puesto == "Ssr" or puesto == "Sr" or puesto == "Jr")):
                puesto = prompt("Ingrese puesto", "Por favor, ingresarel puesto (Ssr, Sr, Jr): ")
                if(puesto == None):
                    break
            
            if(nombre != None and edad != None and genero != None and puntaje != None and puesto != None):
                self.lista_nombre.append(nombre)
                self.lista_edad.append(int(edad))
                self.lista_genero.append(genero)
                self.lista_puntaje.append(int(puntaje))
                self.lista_puesto.append(puesto)
                print(self.lista_nombre, self.lista_edad, self.lista_genero, self.lista_puntaje, self.lista_puesto)
                flag = question("Continuar", "Desea continuar cargando datos?")
            else:
                flag = question("Error", "No se cargo la informacion correctamente, reintentar?")


    def btn_mostrar_on_click(self):

        #    A) La cantidad de aplicantes al puesto “Ssr” que sean mayores a 45 años.
        contador_aplicantes = 0

        for i in range(len(self.lista_nombre)):
            puesto = self.lista_puesto[i]
            edad = self.lista_edad[i]
            print(puesto, edad)
            if(puesto == "Ssr" and edad >= 45):
                contador_aplicantes += 1
        alert("Respuesta", f"La cantidad de aplicantes mayores a 45 años y en un puesto de Ssr es de:{contador_aplicantes}")

        #   B)  El promedio de edad de los aplicantes para el puesto “Sr”.
        acumulador_edades = 0
        for i in range(len(self.lista_nombre)):
            puesto = self.lista_puesto[i]
            edad = self.lista_edad[i]
            if(puesto == "Sr"):
                acumulador_edades += edad
        promedio_edades = acumulador_edades / (i+1)
        if(promedio_edades > 0):
            alert("Respuesta", f"El promedio de edades es de {promedio_edades:.0f} años")
        else:
            alert("Respuesta", f"No aplico nadie para el puesto de Sr")
        
        #   C)  Los porcentajes de aplicantes de cada género.
        contador_masculinos = 0
        contador_femeninos = 0
        contador_no_binarios = 0
        for i in range(len(self.lista_nombre)):
            genero = self.lista_genero[i]

            match(genero):
                case "M":
                    contador_masculinos += 1
                case "F":
                    contador_femeninos += 1
                case "NB":
                    contador_no_binarios += 1
        
        porcentaje_masculinos = contador_masculinos * 100 / (i+1)
        porcentaje_femeninos = contador_femeninos * 100 / (i+1)
        porcentaje_no_binarios = contador_no_binarios * 100 / (i+1)
        alert("Respuesta", f"El porcentaje de aplicantes por genero es:\nMasculinos: %{porcentaje_masculinos}\nFemeninos: %{porcentaje_femeninos}\nNo Binarios: %{porcentaje_no_binarios}")

        #   D)  El nombre y género de la persona con más puntaje entrevistada para el puesto “Jr”.
        maximo_puntaje = 0
        minimo_puntaje = 0
        for i in range(len(self.lista_nombre)):
            nombre = self.lista_nombre[i]
            genero = self.lista_genero[i]
            puesto = self.lista_puesto[i]
            puntaje = self.lista_puntaje[i]
            if(puesto == "Jr" and puntaje >= maximo_puntaje):
                nombre_persona = nombre
                genero_persona = genero
                maximo_puntaje = puntaje
                if(minimo_puntaje == 0 and puntaje <= minimo_puntaje):
                    minimo_puntaje = puntaje
        alert("Respuesta", f"La persona con mas puntaje es: {nombre_persona} {genero_persona} y su puntaje es de {maximo_puntaje}")

        #   E)  DEBE REALIZAR DOS PUNTO EL PRIMERO CORRESPONDIENTE AL ÚLTIMO NÚMERO DE SU DNI PERSONAL (Ejemplo 4) Y EL SEGUNDO RESTANDO A 9 EL ÚLTIMO NÚMERO DE SU DNI (Ejemplo 9 - 4 = 5):

print(__name__)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
