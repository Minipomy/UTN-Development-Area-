
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Nombre: Maximiliano
Rivera: Mendes

Enunciado:
Al presionar el botón ‘Validar letra’, mediante prompt solicitar al usuario que ingrese una letra. 
Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas) 
En caso no coincidir con ninguna de las letras, volverla a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        letra = ""
        
        letra = prompt("Ingrese letra", "Por favor, ingresar letra")
        while(letra != "U" and letra != "T" and letra != "N"):      #   Maxi Nabo, logica proposicional de 1er grado no vuelvas a usar OR -Think Mark Think-
            letra = prompt("Ingrese letra", "Re ingresar letra")
    
if __name__ == "__main__":
    app = App()
    app.mainloop()