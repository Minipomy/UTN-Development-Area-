import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Maximiliano
apellido: Rivera Mendes
---
Ejercicio: instrucion_if_07
---
Enunciado:
Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde los dieciocho (18) años están habilitados a votar. 
Al presionar el botón  'Calcular', se deberá informar (utilizando el Dialog Alert) si es o no posible que la persona concurra a votar en base a la información 
suministrada.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Tipo")
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.combobox_tipo = customtkinter.CTkComboBox(master=self, values=["NATIVO", "NATURALIZADO"])
        self.combobox_tipo.grid(row=1, column=1, padx=20, pady=10)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        valor_edad = self.txt_edad.get()
        if(int(valor_edad.isnumeric())):
            valor_edad = int(valor_edad)
            if(valor_edad >= 16 and self.combobox_tipo.get() == "NATIVO"):
                alert("Nativo", "Puede votar NATIVO")
            
            elif(valor_edad >= 18 and self.combobox_tipo.get() == "NATURALIZADO"):
                alert("Nativo", "Puede votar NATURALIZADO")

            else:
                origen = self.combobox_tipo.get()
                alert("Error", f"Demasiado menor para votar {origen}")
        else:
            alert("Error", "La edad debe de ser un numero")
        
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()