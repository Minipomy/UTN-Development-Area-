import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano
Rivera: Mendes

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos      # Totales_negativos
    La suma acumulada de los positivos      # Totales_positivos
    Cantidad de números positivos ingresados    # Contadores_Positivos
    Cantidad de números negativos ingresados    # Contadores_Negativos
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        valor_ingresado = 0
        suma_positivos = 0
        suma_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        flag = True

        while(flag != False):
            valor_ingresado = prompt("Ingresar Numero", "Por favor, ingresar un numero:")
            if(valor_ingresado == None):
                break
            if(int(valor_ingresado) > 0):
                contador_positivos += 1
                suma_positivos += int(valor_ingresado)
            elif(int(valor_ingresado) < 0):
                contador_negativos += 1
                suma_negativos -= int(valor_ingresado)
            else:
                contador_ceros += 1
            flag = question("Desea continuar?", "Desea seguir ingresando numeros?") 

        diferencia = contador_positivos - contador_negativos
        alert("Respuesta", f"la suma de los positivos es de:{suma_positivos}\nla suma de los negativos es de:{suma_negativos}\nla diferencia entre ambos es de:{diferencia}\nY se ingresaron esta cantidad de ceros:{contador_ceros}")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
