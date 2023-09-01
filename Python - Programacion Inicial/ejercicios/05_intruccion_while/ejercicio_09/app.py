import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano
Rivera: Mendes

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_minimo = customtkinter.CTkEntry(master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        valor_ingresado = 0
        valor_maximo = 0
        valor_minimo = 0
        flag = True

        while(flag != False):
            valor_ingresado = int(prompt("Ingresar valor", "Por favor, ingresar un numero"))
            if(valor_ingresado > valor_maximo):
                valor_maximo = valor_ingresado
                if(valor_minimo == 0):
                    valor_minimo = valor_ingresado
            else:
                if(valor_ingresado > valor_minimo):
                    break
                valor_minimo = valor_ingresado
                
            flag = question("Continuar?", "Desea continuar ingresando numeros?")
        
        alert("Respuesta final", f"El numero mas alto es: {valor_maximo} y el numero minimo es: {valor_minimo}")

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
