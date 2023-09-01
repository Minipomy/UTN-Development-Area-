import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Maximiliano
Rivera: Mendes

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt) o el usuario ingrese cero. 
Calcular la suma acumulada de los positivos y multiplicar los negativos. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_producto

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_producto = customtkinter.CTkEntry(master=self, placeholder_text="Producto")
        self.txt_producto.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        positivos = 0
        negativos = 0
        valor_ingresado = 0
        flag = True

        while(flag != False):
            valor_ingresado = int(prompt("Ingresar numeros", "Por favor, ingresar un numero"))
            if(valor_ingresado > 0):
                positivos += valor_ingresado
            else:
                if(negativos == 0 and valor_ingresado <= 0):                
                    negativos = 1
                negativos *= valor_ingresado
            
            flag = question("Continuar?", "Desea continuar agregando numeros? S/N" )
        
        self.txt_producto.delete(0, 1000)
        self.txt_suma_acumulada.delete(0, 1000)
        self.txt_producto.insert(0, negativos)
        self.txt_suma_acumulada.insert(0, positivos)

        alert("Respuesta", f"El total de numeros positivos es de: {positivos}, y la multiplicacion de numeros negativos es de: -{negativos}")


            
if __name__ == "__main__":
    app = App()
    app.mainloop()
