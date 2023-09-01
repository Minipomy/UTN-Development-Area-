import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre: Maximiliano
Rivera: Mendes

Enunciado:
Al presionar el botón ‘Validar número’, mediante prompt solicitar al usuario que ingrese un número. 
Se deberá validar que se encuentre entre 0 y 9 inclusive. En caso no coincidir con el rango, 
volverlo a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_numero = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_numero_on_click)
        self.btn_validar_numero.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_numero_on_click(self):
        numero_ingresado = -1
        
        numero_ingresado = int(prompt("Ingrese numero", "Por favor, ingrese un numero entre 0 y 9"))
        while(numero_ingresado >= 10 or numero_ingresado < 0):
            numero_ingresado = int(prompt("Error", "Re ingrese un numero entre 0 y 9"))
    
if __name__ == "__main__":
    app = App()
    app.mainloop()