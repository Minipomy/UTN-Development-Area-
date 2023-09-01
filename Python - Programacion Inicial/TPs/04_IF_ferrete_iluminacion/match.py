import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano
Apellido: Rivera Mendes

=== TP 4 (IF) Ferrete Iluminacion ===
Todas las lámparas están al mismo precio de $800 pesos final.
		A.	Si compra 6 o más lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5 lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4 lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3 lamparitas bajo consumo marca "ArgentinaLuz" el descuento es del 15%, si es “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000 se obtien un descuento adicional de 5%.
    Informar mediante un alert el precio final con todos los descuentos aplicados cuando corresponda.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label_1.grid(row=0, column=0, padx=10, pady=10)

        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label_2.grid(row=1, column=0, padx=10, pady=10)
        
        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1","2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        #   Variables
        cantidad = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()
        PRECIO_UNITARIO = 800
        descuento = 0
        subtotal = 0
        importe_descuento = 0
        total = 0

        match cantidad:
            case 6 | 7 | 8 | 9 | 10 | 11 | 12:
                descuento = 50
            case 5:
                match marca:
                    case "ArgentinaLuz":
                        descuento = 40
                    case _:
                        descuento = 30
            case 4:
                match marca:
                    case "ArgentinaLuz" | "FelipeLamparas":
                        descuento = 25
                    case _:
                        descuento = 20
            case 3:
                match marca:
                    case "ArgentinaLuz":
                        descuento = 15
                    case "FelipeLamparas":
                        descuento = 10
                    case _:
                        descuento = 5
                        
        subtotal = PRECIO_UNITARIO * cantidad
        importe_descuento = subtotal * descuento/100
        total = subtotal - importe_descuento

        if(total >= 4000):
            descuento += 5
            subtotal = PRECIO_UNITARIO * cantidad
            importe_descuento = subtotal * descuento/100
            total = subtotal - importe_descuento
        
        alert("Resultado final", f"El precio es de: ${subtotal}\ncon %{descuento} de descuento,\nimporte descuento $-{importe_descuento} el precio final con descuento aplicado es de: ${total:.2f}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()