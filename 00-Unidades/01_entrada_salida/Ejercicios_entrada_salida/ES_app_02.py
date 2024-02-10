import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Camila
apellido: Mori Principe
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #valor = prompt("titulo","ingrese un valor")
        #alert("resultado", valor)
        
        #PERSONA 1
        nombre_primera_persona = prompt("PERSONA 1","Ingrese su nombre") #nombre, edad y peso
        edad_primera_persona = prompt("PERSONA 1","Ingrese su edad")
        int_edad_primera_persona = int(edad_primera_persona)
        peso_primera_persona = prompt("PERSONA 1","Ingrese el peso")
        float_peso_primera_persona = float(peso_primera_persona)


        #PERSONA 2
        nombre_segunda_persona = prompt("PERSONA 2","Ingrese su nombre") #nombre, edad y peso
        edad_segunda_persona = prompt("PERSONA 2","Ingrese su edad")
        int_edad_segunda_persona = int(edad_segunda_persona)
        peso_segunda_persona = prompt("PERSONA 3","Ingrese el peso")
        float_peso_segunda_persona = float(peso_segunda_persona)
    
        #CALCULO DE PESO, PROMEDIO Y PRECIO DE PASAJE DE AMBAS PERSONAS     
        suma_kilos = float_peso_primera_persona + float_peso_segunda_persona #CALCULO DEL PESO DE LAS DOS PERSONAS
        promedio_edad = (int_edad_primera_persona + int_edad_segunda_persona) / 2 #CALCULO PROMEDIO DE EDAD ENTRE LAS DOS PERSONAS
        precio_pasaje = suma_kilos * 1000
        
        mensaje = f"Hola {nombre_primera_persona} y {nombre_segunda_persona}. Sus pesos son de {peso_primera_persona} kilos y {peso_segunda_persona} kilos respectivamente, sumados da {suma_kilos} kilos. El promedio de edad es de {promedio_edad} y su viaje vale {precio_pasaje} pesos"
        alert("PASAJES",mensaje)
    
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()