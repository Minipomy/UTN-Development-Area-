import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano
Apellido: Rivera Mendes

Enunciado:
Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        valor_ingresado = 0

        valor_ingresado = int(prompt("Ingresar numero", "Por favor, ingrese un numero:"))
        for valor in range(1,valor_ingresado):
            valor_ingresado = int(prompt("Ingresar numero", "Por favor, ingrese un numero:"))
            if(valor_ingresado == 9):
                break
        alert("Error", "Ingresaste un 9 y se termino la ejecucion")

        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()