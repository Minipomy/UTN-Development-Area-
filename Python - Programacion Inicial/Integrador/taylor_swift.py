from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ejercicio 1
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

        self.lista_nombres = ["Juan", "María", "Luis", "Ana", "Carlos", "Laura", "Pedro",
                              "Sofía", "Miguel", "Valentina",
                              "Andrés", "Lucía", "Fernando", "Gabriela", "Diego", "Martina",
                              "Jorge", "Camila", "Ricardo", "Isabella",
                              "José", "Paula", "Manuel", "Alejandra", "Santiago", "Daniela",
                              "Gustavo", "Carolina", "Emilio", "Antonella",
                              "Pablo", "Valeria", "Eduardo", "Florencia", "Alberto", "Agustina",
                              "Raul", "Rocio", "Javier", "Marina",
                              "Sebastian", "Catalina", "Rafael", "Carmen", "Rodrigo", "Elena",
                              "Oscar", "Pilar", "Hugo", "Juana", "Guillermo", "Natalia", "Francisco", "Constanza", "Hector",
                              "Adriana", "Victor", "Anita", "Lorenzo", "Estela",
                              "Enrique", "Diana", "Fabian", "Patricia", "Felipe", "Claudia",
                              "Camilo", "Teresa", "Samuel", "Rosa",
                              "Joaquin", "Monica", "Lucas", "Ines", "Omar", "Gloria", "Mariano",
                              "Silvia", "Nicolas", "Alicia",
                              "Federico", "Olga", "Arturo", "Amparo", "Julio", "Elsa", "Alfredo",
                              "Beatriz", "Elias", "Rita",
                              "Benjamin", "Margarita", "Agustin", "Dolores", "Dario", "Lourdes",
                              "Gerardo", "Manuela", "Feliciano", "Marta"]
        
        self.lista_edades = [25, 33, 20, 29, 16, 40, 22, 28, 35, 18,
                             26, 21, 30, 32, 19, 27, 24, 38, 31, 23,
                             29, 17, 28, 34, 20, 25, 22, 33, 40, 16,
                             19, 37, 24, 28, 31, 21, 33, 18, 29, 26,
                             35, 20, 23, 39, 30, 27, 22, 36, 28, 32,
                             31, 19, 24, 20, 25, 33, 40, 27, 21, 39,
                             29, 22, 36, 30, 19, 25, 21, 38, 34, 17,
                             32, 18, 23, 27, 22, 40, 36, 29, 20, 33,
                             31, 35, 24, 19, 28, 30, 26, 37, 33, 21,
                             25, 29, 16, 38, 40, 18, 27, 30, 32, 24]

        self.lista_generos = [
            "Masculino", "Femenino", "Masculino", "Femenino", "Otro",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
            "Femenino", "Masculino", "Femenino", "Masculino", "Femenino"
        ]
        # Lista de tipo de entrada (General, Campo delantero, Platea)
        self.lista_tipo_entrada = [
            "General", "Campo delantero", "Platea", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General",
            "Campo delantero", "Platea", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
            "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General",
            "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General",
            "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General",
            "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Campo delantero", "Platea", "General", "Platea", "Campo delantero", "General",
        ]

        # Lista de medio de pago (Credito, Debito, Efectivo)
        self.lista_medio_pago = [
            "Credito", "Debito", "Efectivo", "Credito", "Efectivo", "Debito",
            "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito"
        ]

        # Lista de precios correspondientes a cada tipo de entrada
        self.lista_precios = [16000, 30000, 25000, 16000, 25000, 30000, 16000, 25000,
                              30000, 16000,
                              25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
                              16000, 25000,
                              30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
                              25000, 30000,
                              16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
                              30000, 16000,
                              25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
                              16000, 25000,
                              30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
                              25000, 30000,
                              16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
                              30000, 16000,
                              25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
                              16000, 25000,
                              30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
                              25000, 30000,
                              16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
                              30000, 16000
                              ]

    def btn_agregar_on_click(self):
        
        nombre = ""
        genero = ""
        tipo_entrada = ""
        medio_de_pago = ""
        edad = 0
        precio = 0
        descuento = 0
        flag = True

        while(flag != False):
            nombre = prompt("Request", "Por favor, ingrese un nombre")
            while(nombre == ""):
                nombre = prompt("Request", "Por favor, ingrese un nombre")
                if(nombre == None):
                    break
            
            edad = prompt("Request", "Por favor, ingrese una edad")
            while(edad == ""):
                edad = prompt("Request", "Por favor, ingrese una edad")
                if(edad == None):
                    break

            genero = prompt("Request", "Por favor, ingrese un genero (Masculino, Femenino, Otros)")
            while(not (genero == "Masculino" or genero == "Femenino" or genero == "Otros")):
                genero = prompt("Request", "Por favor, ingrese un genero (Masculino, Femenino, Otros)")
                if(genero == None):
                    break
            
            tipo_entrada = prompt("Request", "Por favor, ingrese tipo de entrada (General, Campo Delantero, Platea)")
            while(not (tipo_entrada == "General" or tipo_entrada == "Campo Delantero" or tipo_entrada == "Platea")):
                tipo_entrada = prompt("Request", "Por favor, ingrese tipo de entrada (General, Campo Delantero, Platea)")
                if(tipo_entrada == None):
                    break
            
            medio_de_pago = prompt("Request", "Por favor, ingrese Medio de pago (Credito, Debito, Efectivo)")
            while(not (medio_de_pago == "Credito" or medio_de_pago == "Debito" or medio_de_pago == "Efectivo")):
                medio_de_pago = prompt("Request", "Por favor, ingrese Medio de pago (Credito, Debito, Efectivo)")
                if(medio_de_pago == None):
                    break

            if(nombre != None and edad != None and genero != None and tipo_entrada != None and medio_de_pago != None):
                
                match(tipo_entrada):
                    case "General":
                        precio = 16000
                    case "Campo Delantero":
                        precio = 25000
                    case "Platea":
                        precio = 30000

                match(medio_de_pago):
                    case "Credito":
                        descuento += 20
                    case "Debito":
                        descuento += 15
                    case "Efectivo":
                        descuento += 1
                precio_final = descuento * precio / 100

                self.lista_nombres.append(nombre)
                self.lista_edades.append(int(edad))
                self.lista_generos.append(genero)
                self.lista_tipo_entrada.append(tipo_entrada)
                self.lista_precios.append(int(precio_final))

                flag = question("Continuar", "Desea cargar mas personas?")
            else:
                flag = question("Continuar", "No se cargo la informacion correctamente, reintentar?")
            


    def btn_mostrar_on_click(self):
        total_recaudado = 0
        contador_general = 0
        contador_platea = 0
        contador_campo_delantero = 0
        total_edades = 0
        promedio_edad_platea = 0
        maximo_edad = 0
        indice = 0
        nombre_persona = ""
        lista_personas_mayores = []


        # A) Cantidad total de dinero recaudado por las ventas de entradas.
        for precio in self.lista_precios:
            total_recaudado += float(precio)
        alert("Taylor Swift Tour",f"Total recaudado ${total_recaudado:.2f}")

        #   B) Cantidad de entradas vendidas para cada tipo.
        for cantidad in self.lista_tipo_entrada:
            match(cantidad):
                case "General":
                    contador_general += 1
                case "Campo delantero":
                    contador_campo_delantero += 1
                case "Platea":
                    contador_platea += 1
        alert("Taylor Swift Tour", f"Cantidad de entrada por tipo,\n General: {contador_general}\nCampo Delantero: {contador_campo_delantero}\nPlatea: {contador_platea}")

        #   C) Promedio de edad de las personas que compraron ubicación en Platea.
        for edades in self.lista_edades:
            for ubicaciones in self.lista_tipo_entrada:
                if(ubicaciones == "Platea"):
                    total_edades += edades
                    promedio_edad_platea += 1
        promedio = total_edades / promedio_edad_platea
        alert("Taylor Swift Tour", f"Promedio edades: {promedio:.0f}")

        #   D)  Nombre de la persona de mayor edad que compró una entrada de platea.
        for ubicaciones in self.lista_tipo_entrada:
            if(ubicaciones == "Platea"):        
                if(self.lista_edades[indice] >= maximo_edad):
                    maximo_edad = self.lista_edades[indice]
                    nombre_persona = self.lista_nombres[indice]
            indice += 1
        alert("Taylor Swift Tour", f"El maximo de edad para Platea es: {nombre_persona} {maximo_edad} años")

        #   E)  Porcentaje de entradas vendidas de tipo General
        contador_cantidad_entradas = contador_platea + contador_general + contador_campo_delantero
        porcentaje_general = float(contador_general * contador_cantidad_entradas / 100)
        alert("",f"El porcentaje total de entradas generales es: %{porcentaje_general:.0f}")


        #   F)  Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
        indice -= len(self.lista_tipo_entrada)      #   Reset
        for ubicaciones in self.lista_tipo_entrada:
            if(ubicaciones == "General"):
                if(self.lista_generos[indice] == "Masculino"):
                    if(self.lista_edades[indice] >= 18 ):
                        lista_personas_mayores.append(self.lista_nombres[indice])
                        lista_personas_mayores.append(self.lista_edades[indice])
                        lista_personas_mayores.append(self.lista_generos[indice])
            indice += 1
        alert("Taylor Swift Tour", f"{lista_personas_mayores}")

        #   G)  Tipo de entradas más vendidas
        if(contador_general > contador_platea):
            tipo_mas_vendido = "General"
            if(contador_general < contador_campo_delantero):
                tipo_mas_vendido = "Campo Delantero"
        elif(contador_platea > contador_general):
            tipo_mas_vendido = "Platea"
            if(contador_platea < contador_campo_delantero):
                tipo_mas_vendido = "Campo Delantero"
        else:
            tipo_mas_vendido = "Campo Delantero"

        if(contador_general > contador_platea and contador_general > contador_campo_delantero):
            tipo_mas_vendido = "General"
        elif(contador_platea > contador_campo_delantero):
            tipo_mas_vendido = "Platea"
        else:
            tipo_mas_vendido = "Campo Delantero"

        alert("Taylor Swift Tour", f"Tipo mas vendido: {tipo_mas_vendido}")

print(__name__)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()