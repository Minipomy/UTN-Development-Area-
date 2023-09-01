import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Maximiliano
apellido: Rivera Mendes
---
Ejercicio: instrucion_if_04
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, 
transformarlo en número y calcular si es mayor, menor o adolescente (edad entre 13 y 17 años) 
de edad, se deberá informar utilizando el Dialog aler.
'''

    # 0 a 13 > 13 a 17 > 17 a 99
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
            if(valor_edad < 13):
                alert("Valor muy bajo", "usted es menor")
            
            elif(valor_edad >= 13 and not valor_edad >=18):
                alert("Valor muy bajo", "usted es adolecente")
            
            else:
                alert("Usted es mayor", "Usted es mayor a 18 años")
        else:
            alert("Error", "La edad tiene que ser un numero")        


if __name__ == "__main__":
    app = App()
    app.mainloop()