import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Camila
apellido: Mori Principe
---
Ejercicio: while_06
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        
        contador_iteracion = 0 #Variable de control del while. Esto se suelen nombrar con una sola letra pero en este caso es contador_iteracion
        acumulador_numeros = 0 
        #Lo que ocurre antes del while
        while contador_iteracion < 5 :
            #Lo que ocurre dentro del while
            numero = prompt("ingreso","Ingresar 5 numeros")
            numero = int(numero)

            acumulador_numeros = acumulador_numeros + numero #Con esto ya podemos sumar y "RECORDAR" de alguna manera cumulando los numeros.


            contador_iteracion += 1 #Incremento de la variable de control

        #Lo que ocurre después del while
        
        promedio = acumulador_numeros / contador_iteracion #Se coloca por fuera del while para que suceda SOLO UNA VEZ y no 5 veces si estuviera dentro del while.
        
        self.txt_suma_acumulada.insert(0, acumulador_numeros)
        self.txt_promedio.insert(0, promedio)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
