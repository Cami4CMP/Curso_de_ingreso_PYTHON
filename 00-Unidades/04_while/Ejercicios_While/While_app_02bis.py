import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Camila
apellido: Mori Principe
---
Ejercicio: while_02bis
---
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert la suma 
de los numeros pares comprendidos entre el 1 y el 10.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):

        #ENTRADAS: 
            #contador del 1 al 10
            #variables que acumule la suma de los numeros pares
        #PROCESO:
        #SALIDA:
            #Suma de numeros pares
        
        #contador = 1
        #suma = 0 #Aca estia pasando lo siguiente : 2+4+6+8+10 que seria 30

        #while contador <= 10:
         #   if contador % 2 == 0: #Si el numero ES PAR, SOLO si es par...
          #      suma += contador #...lo SUMO.

           # contador += 1 #Esto suma de a uno...y con el if de arriba se va verificando que los numeros sean pares y se sumen sino no suma nada y pasa al siguiente numero.
        
        #alert("ES", suma)


        suma = 0 
        contador = 2 #arranco desde mi primer numero par
        #NUMEROS PARES: 2 - 4 - 6 - 8 - 10

        while contador <= 10:
            suma += contador
            contador += 2 #sumarle 2 al contador para que ya directamente pase al 4 y asi sucesivamente
        
        alert("", suma)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()