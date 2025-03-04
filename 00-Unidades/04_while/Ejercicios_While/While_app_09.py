import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Camila
apellido: Mori Principe
---
Ejercicio: while_09
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        contador_iteracion = 0
        acumulador_numeros = 0 
        
        maximo = 1000
        minimo = 1000

        while contador_iteracion < 3 :
            numero = prompt("ingreso","Ingrese numeros")
            numero = int(numero)

            if contador_iteracion == 0:
                maximo = numero
                minimo = numero

            if numero > maximo:
                maximo = numero
                
            if numero <minimo:
                minimo = numero

            contador_iteracion += 1 #Incremento de la variable de control

       
        self.txt_suma_acumulada.insert(0, f"max: {maximo}")
        self.txt_promedio.insert(0, f"min: {minimo}")

        if numero > maximo:
            maximo = numero

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
