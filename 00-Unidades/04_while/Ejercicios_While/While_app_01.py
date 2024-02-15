import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Camila
apellido: Mori Principe
---
Ejercicio: while_01
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):


        contador_iteracion = 0

        while contador_iteracion < 10:
            print(contador_iteracion + 1)
            contador_iteracion = contador_iteracion + 1 # Si el contador vale 0. Acá se tiene que igualar a 0 + 1, de esta forma ya se cuenta el resultado de esa suma y pasa a contar desde 1, y en el bucle ya se va sumando de forma ascendente hasta llegar a mas de 10 y ahi logar que la condición sea falsa.

        

    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()