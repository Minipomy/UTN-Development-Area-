import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano
Apellido: Rivera Mendes

=== TP 7 (FOR) UTN Factory ===
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F - M - NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
A. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
B. Nombre del postulante Jr con menor edad.
C. Promedio de edades por género.
D. Tecnologia con mas postulantes (solo hay una).
E. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=1, pady=20, columnspan=2, sticky="nsew")

        self.lista_nombres = ["Maxi","Lucas","Cata","Javier","La Abuela"]
        self.lista_edades = [25, 30, 40, 29, 65]
        self.lista_generos = ["M","M","NB","NB","F"]
        self.lista_tecnologias = ["PYTHON", "PYTHON", "ASP.NET", "JS", "JS"]
        self.lista_puestos = ["Ssr", "Ssr", "Ssr", "Sr", "Ssr"]

    def btn_validar_on_click(self):
        acumulador_mayores_nb_python_net = 0
        contador_ssr = 0
        contador_sr = 0
        contador_jr = 0
        contador_net = 0
        contador_js = 0
        contador_m = 0
        contador_f = 0
        contador_nb = 0
        contador_python = 0
        acumulador_edades_m = 0
        acumulador_edades_f = 0
        acumulador_edades_nb = 0
        promedio_edades_m = 0
        promedio_edades_f = 0
        promedio_edades_nb = 0
        porcentaje_postulantes_m = 0
        porcentaje_postulantes_f = 0
        porcentaje_postulantes_nb = 0
        mayor_postulantes = ""
        nombre_persona = ""
        edad_persona = 0
        flag = True


        for i in range(len(self.lista_nombres)):
            nombre = self.lista_nombres[i]
            edad = self.lista_edades[i]
            genero = self.lista_generos[i]
            tecnologia = self.lista_tecnologias[i]
            puesto = self.lista_puestos[i]
            contador = i+1

            match(puesto):
                case "Ssr":
                    contador_ssr += 1
                    if(genero == "NB" and (tecnologia == "JS" or tecnologia == "ASP.NET") and edad >= 25 and edad <= 40):
                        acumulador_mayores_nb_python_net += 1
                case "Sr":
                    contador_sr += 1
                case "Jr":
                    contador_jr += 1
                    if(flag == True):
                        nombre_persona = nombre
                        edad_persona = edad
                        flag = False
                    elif(edad <= edad_persona):
                        nombre_persona = nombre
                        edad_persona = edad
            
            match(genero):
                case "M":
                    acumulador_edades_m += edad
                    contador_m += 1
                case "F":
                    acumulador_edades_f += edad
                    contador_f += 1
                case "NB":
                    acumulador_edades_nb += edad
                    contador_nb += 1

                
            match(tecnologia):
                case "PYTHON":
                    contador_python += 1
                case "JS":
                    contador_js += 1
                case "ASP.NET":
                    contador_net += 1
        
        if(contador_python > contador_js):
            mayor_postulantes = "PYTHON"
            if(contador_python < contador_net):
                mayor_postulantes = "ASP.NET"
        elif(contador_js > contador_net):
            mayor_postulantes = "JS"
            if(contador_python > contador_net):
                mayor_postulantes = "PYTHON"
        else:
            mayor_postulantes = "ASP.NET"

        promedio_edades_m += acumulador_edades_m / contador_m
        promedio_edades_f = acumulador_edades_f / contador_f
        promedio_edades_nb = acumulador_edades_nb / contador_nb

        porcentaje_postulantes_m += contador_m * 100 // contador
        porcentaje_postulantes_f = contador_f * 100 // contador
        porcentaje_postulantes_nb = contador_nb * 100 // contador

        #   A) Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
        alert("Respuesta", f"La Cantidad de postulantes de genero no binario (NB)\nque programan en ASP.NET o JS\n cuya edad este entre 25 y 40\nY que se hayan postulado para un puesto Ssr es de: {acumulador_mayores_nb_python_net}")
        #   B) Nombre del postulante Jr con menor edad.
        alert("Respuesta", f"El nombre de la persona Jr con menor edad es: {nombre_persona} y su edad es: {edad_persona} años")
        #   C) Promedio de edades por género.
        alert("Respuesta", f"El promedio de edades por genero es:\nMasculinos {promedio_edades_m:.0f} años\nFemeninos: {promedio_edades_f:.0f} años\nNoBinarios: {promedio_edades_nb:.0f} años")
        #   D) Tecnologia con mas postulantes (solo hay una).
        alert("Respuesta", f"La tecnologia con mayor postulantes es: {mayor_postulantes}")
        #   E) Porcentaje de postulantes de cada genero.
        alert("Respuesta", f"Los porcentajes de postulantes de cada genero es:\nMasculinos: %{porcentaje_postulantes_m:.0f}\nFemeninos: %{porcentaje_postulantes_f:.0f}\nNoBinarios: %{porcentaje_postulantes_nb:.0f}")
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()