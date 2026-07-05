"CONTADOR"
import tkinter as tk
contador=0
def sumar():
    global contador
    if contador<10:
        contador=contador+1
        etiqueta.config(text=contador)
        if contador==10:
            etiqueta.config(fg="green")
        else:
            etiqueta.config(fg="black")
    
def restar():
    global contador
    if contador>-10:
        contador=contador-1
        etiqueta.config(text=contador)
        if contador==-10:
            etiqueta.config(fg="red")
        else:
            etiqueta.config(fg="black")

ventana=tk.Tk()
ventana.title("Si llegas a 10 cambia a color verde y a -10 cambia a rojo")
ventana.geometry("800x300")

etiqueta=tk.Label(ventana)
etiqueta.config(text=contador)
etiqueta.pack(pady=20)

boton_sumar=tk.Button(
    ventana,
    text="+",
    command=sumar
)
boton_sumar.pack(side="left")

boton_restar=tk.Button(
    ventana,
    text="-",
    command=restar
)
boton_restar.pack(side="right")
ventana.mainloop()