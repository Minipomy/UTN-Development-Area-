from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ejercicio 1
Alumno: Maximiliano, Rivera Mendes
Division: Div J

Enunciado:

Lista de precios:
General: $16000
Campo: $25000
Platea: $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de
descuento sobre el precio de la entrada, mientras que las adquiridas con
tarjeta de débito un 15%.

Al finalizar la venta de entradas, los organizadores quieren obtener la
siguiente información:
A. Cantidad total de dinero recaudado por las ventas de entradas.
B. Cantidad de entradas vendidas para cada tipo.
C. Promedio de edad de las personas que compraron ubicación en
Platea.
D. Nombre de la persona de mayor edad que compró una entrada de
platea.
E. Porcentaje de entradas vendidas de tipo general
F. Nombre de la/s persona/s de mayor edad, de género Masculino
que compro una entrada general.
G. Tipo de entradas más vendidas
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
        '''
        ● Nombre del comprador
        ● Edad (no menor a 16)
        ● Género (Masculino, Femenino, Otro)
        ● Tipo de entrada (General, Campo delantero, Platea)
        ● Medio de pago (Crédito, Efectivo, Débito)
        ● Precio de la entrada (Se debe calcular)
        '''

    def btn_mostrar_on_click(self):
        total_recaudado = 0
        contador_general = 0
        contador_platea = 0
        contador_campo_delantero = 0
        acumulador_edades_platea = 0
        promedio_platea = 0
        nombre_persona = ""
        edad_mas_alta = 0
        lista_vacia_1 = []
        mensaje = "No existen personas Masculinas que compraran una entrada de tipo General"
        mensaje_mas_vendido = ""
        flag = True

        for i in range(len(self.lista_nombres)):
            nombre = self.lista_nombres[i]
            edad = self.lista_edades[i]
            genero = self.lista_generos[i]
            tipo_entrada = self.lista_tipo_entrada[i]
            precio = self.lista_precios[i]

            #   A. Cantidad total de dinero recaudado por las ventas de entradas.
            total_recaudado += precio

            #   B. Cantidad de entradas vendidas para cada tipo.
            match(tipo_entrada):
                case "General":
                    contador_general += 1
                    
                    #   F. Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
                    if(genero == "Masculino"):
                        lista_vacia_1.append(nombre)
                        mensaje = f"La/s perona/s que compraron una entrada de tipo general son: {lista_vacia_1}"

                case "Platea":
                    contador_platea += 1
                    acumulador_edades_platea += edad

                    #   D. Nombre de la persona de mayor edad que compró una entrada de platea.
                    if(flag != False):
                        nombre_persona = nombre
                        edad_mas_alta = edad
                        flag = False
                    elif(edad_mas_alta < edad):
                        nombre_persona = nombre
                        edad_mas_alta = edad

                case "Campo delantero":
                    contador_campo_delantero += 1    

        
        promedio_platea = acumulador_edades_platea / contador_platea
        
        #E. Porcentaje de entradas vendidas de tipo general        
        total_entradas = float(contador_general + contador_campo_delantero + contador_platea)
        porcentaje_general = float(contador_general * 100 / total_entradas)
        porcentaje_platea = float(contador_platea * 100 / total_entradas)
        porcentaje_campo_abierto = float(contador_campo_delantero * 100 / total_entradas)
        
        #   G. Tipo de entradas más vendidas        -- La razon es sencilla, 3 tipos de entradas y en porcentaje seria del 0% al 100% entonces al dividir por 3, sabemos el minimo que es 33%
        print(porcentaje_campo_abierto, porcentaje_general, porcentaje_platea)
        if(porcentaje_general > 100/3):
            mensaje_mas_vendido = "General"
        elif(porcentaje_platea > 100/3):
            mensaje_mas_vendido = "Platea"
        elif(porcentaje_campo_abierto > 100/3):
            mensaje_mas_vendido = "Campo Delantero"
        else:
            mensaje_mas_vendido = "Es un empate"

        # if(contador_general > contador_platea and contador_general > contador_campo_delantero):
        #     tipo_mas_vendido = "General"
        # elif(contador_platea > contador_campo_delantero):
        #     tipo_mas_vendido = "Platea"
        # else:
        #     tipo_mas_vendido = "Campo Delantero"


        #   A. Cantidad total de dinero recaudado por las ventas de entradas.
        alert("Respuesta", f"El total recaudado corresponde a: {total_recaudado:.2f}")

        #   B. Cantidad de entradas vendidas para cada tipo.
        alert("Respuesta", f"Cantidad de entradas vendidas de cada tipo:\nGeneral: {contador_general}\nPlatea: {contador_platea}\nCampo Delantero: {contador_campo_delantero}")

        #   C. Promedio de edad de las personas que compraron ubicación en Platea.
        alert("Respuesta", f"El promedio de edades que compraron en platea es de: {promedio_platea:.2f}")

        #   D. Nombre de la persona de mayor edad que compró una entrada de platea.
        alert("Respuesta", f"La persona con mayor edad que compro en platea es\nNombre: {nombre_persona}\nEdad: {edad_mas_alta}")

        #   E. Porcentaje de entradas vendidas de tipo general
        alert("Respuesta", f"El porcentaje de entradas vendidas de tipo general es: %{porcentaje_general:.0f}")
    
        #   F. Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
        alert("Respuesta", mensaje)

        #   G. Tipo de entradas más vendidas
        alert("Respuesta", f"La entrada mas vendida es: {mensaje_mas_vendido}")

print(__name__)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()