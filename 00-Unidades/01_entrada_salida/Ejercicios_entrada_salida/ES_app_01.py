import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math
'''
nombre: Camila
apellido: Mori Principe
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        #alert("titulo","esto no anda, funciona")
        
        
        
        
        #Ingresar el valor del dólar oficial y el valor del dólar blue. 
        #Mostrar la diferencia expresada en porcentaje entre una cotización y otra.
        
        dolar_oficial = prompt("OFICIAL","ingrese el valor de dolar")
        dolar_blue = prompt("BLUE","Ingrese el valor de dolar blue")
        
        dolar_oficial_float = float(dolar_oficial)
        dolar_blue_float = float(dolar_blue)
        
        diferencia = dolar_blue_float - dolar_oficial_float
        porcentaje = diferencia / dolar_oficial_float
        calculo_final = porcentaje * 100
        
        mensaje = f"La diferencia porcentual es de {calculo_final}%"
    
        alert("RESULTADO", mensaje)
        




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
    
