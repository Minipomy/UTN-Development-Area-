import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Maximiliano
apellido: Rivera Mendes
---
Ejercicio: instrucion_if_02
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, transformarlo en número 
y calcular si es mayor de edad, si es mayor de 18 se mostrará el mensaje “MAYOR” utilizando el Dialog Alert.
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
        if(valor_edad.isnumeric()):
            if(int(valor_edad) >= 18):
                alert("Respuesta", "MAYOR")
            else:
                alert("Respuesta", "MENOR")
        else:
            alert("Error", "La edad tiene que ser un numero")

        
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()