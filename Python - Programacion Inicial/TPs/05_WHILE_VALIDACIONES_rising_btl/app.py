import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: 
Apellido: 

=== TP 5 (WHILE/Validaciones) Rising BTL ===
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"].
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Estado Civil")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_estado_civil = customtkinter.CTkEntry(master=self)
        self.txt_estado_civil.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)

        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=2, column=1)
                
        self.btn_validar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=3, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        edad = 0
        estado_civil = ""
        numero_legajo = 0

        edad = prompt("Ingrese edad", "Por favor, ingresar una edad entre 18 a 90 años")
        while(int(edad) < 18 or int(edad) > 90):
            edad = prompt("Ingrese edad", "Por favor, ingresar una edad entre 18 a 90 años")

        estado_civil = prompt("Ingrese estado civil", "Por favor, ingresar estado civil [Soltero/a, Casado/a, Divorciado/a, Viudo/a]")
        while(estado_civil != "Soltero" and estado_civil != "Casado" and estado_civil != "Divorciado" and estado_civil != "Viudo" and
              estado_civil != "Soltera" and estado_civil != "Casada" and estado_civil != "Divorciada" and estado_civil != "Viuda"):
            
            estado_civil = prompt("Ingrese estado civil", "Por favor, ingresar estado civil [Soltero/a, Casado/a, Divorciado/a, Viudo/a]")
        
        numero_legajo = prompt("Ingrese legajo", "Por favor, ingresar numero de legajo")
        while(numero_legajo == len(4)):
            numero_legajo = prompt("Ingrese legajo", "Por favor, ingresar numero de legajo")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()