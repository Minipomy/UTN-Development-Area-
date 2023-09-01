import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano
Apellido: Rivera Mendes

=== TP 8 (LIST) Conteo ===
Enunciado:
Al presionar el botón "Comenzar ingreso", solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. El minimo de los negativos
    G. El maximo de los positivos
    H. El promedio de los negativos

Informar los resultados mediante alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_cargar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        numero = 0
        flag = True

        while(flag == True):
            numero = prompt("Ingresar numero", "Por favor, ingrese un numero:")
            while(numero.isalpha()):
                numero = prompt("Ingresar numero", "Por favor, ingrese un numero:")
                if(numero == None):
                    break
            
            if(numero != None):
                self.lista.append(numero)
            flag = question("Continuar", "Desea seguir cargando datos?")

    def btn_mostrar_estadisticas_on_click(self):
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        minimo = 0
        maximo = 0
        promedio_negativos = 0
        flag = True

        for i in range(len(self.lista)):
            numero = int(self.lista[i])

            if(numero > 0):
                acumulador_positivos += numero
                contador_positivos += 1
            elif(numero < 0):
                acumulador_negativos += numero
                contador_negativos += 1
            else:
                contador_ceros += 1
    
            if(flag == True):
                maximo = numero
                minimo = numero
                flag = False
            elif(maximo < numero):
                maximo = numero
            elif(minimo > numero):
                minimo = numero
            
        if(contador_negativos > 0):
            promedio_negativos = acumulador_negativos / contador_negativos

        #   A)B) la suma de positivos y negativos
        alert("Respuesta",f"La suma total de positivos y negativos es de: {acumulador_positivos} {acumulador_negativos}")
        #   C)D)E) Cantidad de números positivos ingresados D. Cantidad de números negativos ingresados E. Cantidad de ceros
        alert("Respuesta",f"La cantidad de numeros ingresados son:\nPositivos: {contador_positivos}\nNegativos: {contador_negativos}\nCeros: {contador_ceros}")
        #   F. El minimo de los negativos G. El maximo de los positivos
        alert("Respuesta",f"El maximo y el minimo es: {maximo} {minimo}")
        #   H. El promedio de los negativos
        alert("Respuesta",f"el promedio de negativos es de {promedio_negativos:.2f}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
