import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=5)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        if self.txt_nombre.get() != "":
            nombre_ingresado = prompt("Nombre Requerido", "Por favor, ingrese su nombre")
        else:
            alert("Saludos", "Hola " + self.txt_nombre.get())
        alert("Saludos", "Hola " + nombre_ingresado)         
    
if __name__ == "__main__":
    app = App()
    app.mainloop()