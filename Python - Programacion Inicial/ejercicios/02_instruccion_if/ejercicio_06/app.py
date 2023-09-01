import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Maximiliano 
apellido: Rivera Mendes
---
Ejercicio: instrucion_if_06
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, transformarlo en número 
y calcular si es mayor, niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años) o adolescente (edad entre 13 y 17 años) de edad, 
se deberá informar utilizando el Dialog alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        valor_edad = self.txt_edad.get()
        if(int(valor_edad.isnumeric())):
            valor_edad = int(valor_edad)
            if(valor_edad <= 10):
                alert("Niño", "Es un niño")
            
            elif(valor_edad <= 13):
                alert("Pre-adolecente", "Es un pre-adolecente")
            
            else:
                alert("Adolecente", "Es un Adolecente")
        else:
            alert("Error", "La edad tiene que ser un numero")

        
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()