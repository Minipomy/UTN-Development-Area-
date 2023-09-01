import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Maximiliano 
apellido: Rivera Mendes
---
Ejercicio: entrada_salida_04
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un nombre utilizando el Dialog Prompt y luego mostrarlo en la caja de texto txt_nombre (.delete / .insert )
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")    # Etiqueta "nombre" 
        self.label1.grid(row=0, column=0, padx=20, pady=10)     # Posicion de la Etiqueta "nombre"
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)   # Box del entrada de datos"
        self.txt_nombre.grid(row=0, column=1)   # Posicion del Box del "entrada de datos"
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click) # Boton "Mostrar"
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")  # Posicion del boton "Mostrar"


    def btn_mostrar_on_click(self):
        nombre_ingresado = prompt("Nombre requerido", "Por favor, ingresar un nombre")
        self.txt_nombre.delete(0, 1000)
        self.txt_nombre.insert(0, nombre_ingresado)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()