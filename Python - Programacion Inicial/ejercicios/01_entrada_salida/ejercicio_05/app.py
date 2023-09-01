import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Maximiliano
apellido: Rivera Mendes
---
Ejercicio: entrada_salida_05
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener tanto el nombre como la edad contenida en 
las cajas de texto correspondientes y luego mostrarlo concatenados utilizando el Dialog Alert. 
Ej: "Usted se llama José y su edad es 66 años"
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=5)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label2.grid(row=1, column=0, padx=20, pady=5)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        nombre_ingresado = prompt("Nombre requerido", "Por favor, ingrese su nombre") # Section nombre
        # <Detalles esteticos, no funcionales>
        self.txt_nombre.delete(0, 1000)             
        self.txt_nombre.insert(0, nombre_ingresado) 
        # </Detalles esteticos, no funcionales>

        edad_ingresado = prompt("Edad requerida", "Por favor, ingrese su edad") # Section Edad
        # <Detalles esteticos, no funcionales>
        self.txt_edad.delete(0, 1000)
        self.txt_edad.insert(0, edad_ingresado) 
        # </Detalles esteticos, no funcionales>

        alert("Resultado", "Usted se llama: " + nombre_ingresado + " y su edad es: " + edad_ingresado) # Notificacion

if __name__ == "__main__":
    app = App()
    app.mainloop()