import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano 
Apellido: Rivera Mendes

=== TP 3 (E/S) Ferrete Construccion ===
Enunciado:
El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado perimetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar el perimetro y el area del terreno.
    B. Informar la cantidad de postes de quebracho Grueso (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino (van cada 12 mts lineales).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de metros de alambre necesarios para rodear el perimetro con 7 hilos de alambre.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso
    (F)Poste Quebracho Fino
    (V)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)
       
        self.btn_calcular = customtkinter.CTkButton(master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")
        

    def btn_calcular_on_click(self):
        valor_ancho = int(self.txt_ancho.get())
        valor_largo = int(self.txt_largo.get())
        perimetro = int((2 * valor_ancho) + (2 * valor_largo))
        area = int(valor_ancho * valor_largo)
        quebracho_bold = int((perimetro * 1/250) + 4) # HOTFIX: Falto calcular esquinas
        quebracho_slim = int(perimetro * 1/12)
        varillas = int(perimetro * 1/2)
        alambre_total = int(perimetro * 7)
        alert("Respuesta", f"Las medidas de {valor_ancho} Mts X {valor_largo} Mts,\ntiene un perimetro de: {perimetro},\n un area de: {area}\n y se deberan obtener un total de:\n {quebracho_bold} Quebracho Grueso,\n {quebracho_slim} Quebracho Fino,\n {varillas} Varillas,\n y finalmente {alambre_total} Mts de Alambre")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
