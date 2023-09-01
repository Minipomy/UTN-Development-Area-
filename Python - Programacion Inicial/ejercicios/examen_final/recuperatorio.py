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
La empresa “Octavio Antigüedades” decide realizar una compra masiva de álbumes
musicales del siglo pasado, por lo que le pide elaborar un programa que pueda cargar una
serie de datos, hasta que el usuario quiera:
- Nombre del Artista,
- Precio del Álbum (entre 10 y 10000),
- Tipo de Álbum (“Vinilo”, “Cassette”, “CD”).

Además, una vez cargados los datos se pide informar:
A) Cantidad total de álbumes que sean del tipo Vinilo y tengan un precio superior a
$3000.
B) El nombre del artista con el álbum más barato.
C) REALIZAR DOS PUNTOS: EL PRIMERO CORRESPONDIENTE AL ÚLTIMO
NÚMERO DE SU DNI PERSONAL (Ejemplo 4)
D) EL SEGUNDO PUNTO SE CALCULA: RESTANDO A 9 EL ÚLTIMO NÚMERO DE
SU DNI (Ejemplo 9 - 4 = 5):
0) Informar el porcentaje de álbumes del tipo Vinilo. [Ejemplo: Vinilo 30%]
1) Informar el porcentaje de álbumes del tipo CD y Cassette [Ejemplo: CD 30%,
Cassette 40%]
2) Informar el porcentaje de álbumes del tipo CD. [Ejemplo: CD 30%]
3) Informar el porcentaje de álbumes del tipo Cassette. [Ejemplo: Cassette 30%]
4) Informar los porcentajes de cada uno de los tipos de álbumes. [Ejemplo: Vinilo 30%,
Cassette 40%, CD 30%]
5) Informar el precio promedio de los álbumes.
6) Informar el precio promedio de los álbumes del tipo CD.
7) Informar el precio promedio de los álbumes del tipo Cassette.
8) Informar el precio promedio de los álbumes del tipo Vinilo.
9) Informar el precio promedio de los álbumes que NO sean del tipo Vinilo.
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

        self.lista_de_nombres = ["Juan", "María", "Pedro", "Laura",
        "Carlos", "Ana", "Luis", "Elena", "Miguel", "Sofía"]

        self.lista_precios_albumes = [
        1500, 3000, 800, 3500, 2500, 3700, 4500, 200, 1000, 600]

        self.lista_tipos_albumes = ["Vinilo", "Cassette", "CD", "Vinilo",
        "CD", "Vinilo", "Cassette", "CD", "Vinilo", "CD"]

        # self.lista_de_nombres = []

        # self.lista_precios_albumes = []

        # self.lista_tipos_albumes = []


    def btn_cargar_on_click(self):
        '''
        Enunciado:
        - Nombre del Artista,
        - Precio del Álbum (entre 10 y 10000),
        - Tipo de Álbum (“Vinilo”, “Cassette”, “CD”).
        '''

        nombre = ""
        tipo_album = ""
        precio_album = 0
        flag = True

        while(flag != False):

            nombre = prompt("Ingreso", "Ingresar nombre:")
            while(nombre == ""):
                nombre = prompt("Ingreso", "Ingresar nombre:")
            
            precio_album = int(prompt("Ingreso", "Ingresar precio del album:"))
            while(precio_album < 10 or precio_album > 10000):
                precio_album = int(prompt("Ingreso", "Ingresar precio del album:"))
            
            tipo_album = prompt("Ingreso", "Ingresar tipo de album:")
            while(tipo_album != "CD" and tipo_album != "Cassette" and tipo_album != "Vinilo"):
                tipo_album = prompt("Ingreso", "Ingresar tipo de album:")
            
            self.lista_de_nombres.append(nombre)
            self.lista_precios_albumes.append(precio_album)
            self.lista_tipos_albumes.append(tipo_album)

            flag = question("Continuar", "Desea continuar cargando datos?")

    def btn_mostrar_on_click(self):
        contador_vinilo_mayor_3000 = 0
        nombre_artista_barato = 0
        album_barato = 0
        precio_barato = 0
        contador_vinilo = 0
        contador_cd = 0
        contador_cassette = 0
        promedio_no_vinilo = 0
        acumulador_precio_no_vinilo = 0
        porcentaje_vinilo = 0

        #acumulador_precio_cassette = 0
        #acumulador_precio_cd = 0
        #promedio_cd = 0
        #promedio_cassette = 0

        flag = True

        for i in range(len(self.lista_de_nombres)):
            nombre = self.lista_de_nombres[i]
            precio = self.lista_precios_albumes[i]
            album = self.lista_tipos_albumes[i]

            match(album):
                case "Vinilo":
                    contador_vinilo += 1
                    #   A) Cantidad total de álbumes que sean del tipo Vinilo y tengan un precio superior a $3000.
                    if(precio >= 3000):
                        contador_vinilo_mayor_3000 += 1
                case "CD":
                    contador_cd += 1
                    acumulador_precio_no_vinilo += precio
                    #acumulador_precio_cd += precio
                case "Cassette":
                    contador_cassette += 1
                    acumulador_precio_no_vinilo += precio
                    #acumulador_precio_cassette += precio

            #   B) El nombre del artista con el álbum más barato.
            if(flag == True):
                nombre_artista_barato = nombre
                album_barato = album
                precio_barato = precio
                flag = False
            elif(precio_barato > precio):
                nombre_artista_barato = nombre
                album_barato = album
                precio_barato = precio


        #   C)  0) Informar el porcentaje de álbumes del tipo Vinilo. [Ejemplo: Vinilo 30%]
        total_album = contador_cd + contador_cassette + contador_vinilo
        # if(total_album > 0):
        porcentaje_vinilo = float(contador_vinilo * 100 / total_album)

        #   9) Informar el precio promedio de los álbumes que NO sean del tipo Vinilo.
        # if(contador_cassette > 0 or contador_cd > 0):
        promedio_no_vinilo = float(acumulador_precio_no_vinilo / contador_cd + contador_cassette)

        #promedio_cd = float(acumulador_precio_cd / contador_cd + contador_cassette)
        #promedio_cassette = float(acumulador_precio_cassette / contador_cassette + contador_cd)

        #   A) Cantidad total de álbumes que sean del tipo Vinilo y tengan un precio superior a $3000.
        alert("Respuesta",f"A) Cantidad total de álbumes que sean del tipo Vinilo y tengan un precio superior a $3000.\n Cantidad: {contador_vinilo_mayor_3000}")

        #   B) El nombre del artista con el álbum más barato.
        alert("Respuesta",f"El nombre del artista con el álbum más barato. {nombre_artista_barato}, {album_barato}, {precio_barato}")

        #   C)  0) Informar el porcentaje de álbumes del tipo Vinilo. [Ejemplo: Vinilo 30%]
        alert("Respuesta",f"C)  0) Informar el porcentaje de álbumes del tipo Vinilo.\nVinilo: %{porcentaje_vinilo:.0f}")
        
        #   C)  9) Informar el precio promedio de los álbumes que NO sean del tipo Vinilo.
        alert("Respuesta",f"Informar el precio promedio de los álbumes que NO sean del tipo Vinilo.\nPromedio no vinilo {promedio_no_vinilo:.2f}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
