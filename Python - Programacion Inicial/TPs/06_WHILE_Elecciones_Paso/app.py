import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: 
Apellido: 

=== TP 6 (WHILE) Elecciones Paso ===
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
    A. Nombre del candidato con más votos.
    B. Nombre y edad del candidato con menos votos.
    C. El promedio de edades de los candidatos.
    D. Total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=1, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        pass
        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()