import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano
Apellido: Rivera Mendes

Enunciado:
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
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
        lista_numerica = []

        valor_ingresado = int(prompt("Ingrese numero", "Por favor, ingresar un numero"))
        for i in range(1, valor_ingresado):
            if(i % 2 == 0):
                lista_numerica.append(i)    
        
        alert(lista_numerica)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()