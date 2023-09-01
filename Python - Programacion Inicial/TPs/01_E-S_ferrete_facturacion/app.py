import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano
Apellido: Rivera Mendes

=== TP 1 (E/S) Ferrete Facturacion ===
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_sumar = customtkinter.CTkButton(master=self, text="SUMAR", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_precio_final = customtkinter.CTkButton(master=self, text="PRECIO FINAL", command=self.btn_precio_final_on_click)
        self.btn_precio_final.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_sumar_on_click(self):
        producto_a = int(self.txt_importe_1.get())
        producto_b = int(self.txt_importe_2.get())
        producto_c = int(self.txt_importe_3.get())
        suma = producto_a + producto_b + producto_c
        alert("Total valor de productos", f"la suma final es de: ${suma}")

    def btn_promedio_on_click(self):
        producto_a = int(self.txt_importe_1.get())
        producto_b = int(self.txt_importe_2.get())
        producto_c = int(self.txt_importe_3.get())
        promedio = float((producto_a + producto_b + producto_c) / 3)
        alert("Total promedio productos", f"El promedio de los productos es: {promedio:.2f}")

    def btn_precio_final_on_click(self):
        producto_a = int(self.txt_importe_1.get())
        producto_b = int(self.txt_importe_2.get())
        producto_c = int(self.txt_importe_3.get())
        suma = producto_a + producto_b + producto_c
        IVA = float(21/100)
        importe_iva = float(suma * IVA)
        final = float(suma + importe_iva)
        alert("Resultado general", f"El total de producto es de: ${suma}, tomando en cuenta el %{IVA:.2f} del IVA, que calcula un ${importe_iva:.2f}, el precio final es de ${final:.2f}")


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()