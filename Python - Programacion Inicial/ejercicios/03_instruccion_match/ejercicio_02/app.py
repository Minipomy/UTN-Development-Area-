import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Maximiliano
apellido: Rivera Mendes
---
Enunciado:
Al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si estamos en invierno: ‘¡Abrígate que hace frío!’
    Si aún no llegó el invierno: ‘¡Ya pasamos frío, ahora calor!’
    Si ya pasó el invierno: ‘¡Ya pasamos frío, ahora calor!’
	
Aclaracion: tomamos a Julio y Agosto como los meses de invierno

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        mes = self.combobox_mes.get()
        mensaje = ""

        match mes:
            case "Junio" | "Julio" | "Agosto" | "Semptiembre":
                mensaje = "¡Abrígate que hace frío!"
            case _:
                mensaje = "¡Ya pasamos frío, ahora calor!"

        alert("Respuesta", mensaje)
if __name__ == "__main__":
    app = App()
    app.mainloop()