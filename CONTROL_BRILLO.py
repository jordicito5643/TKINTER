import tkinter as tk
import random

def cambiar(valor):
    slider.set(valor)

def al_mover(e):
    etiqueta.config(text = f"Brillo = {e}%")

ventana = tk.Tk()
ventana.title("BRILLO")
ventana.geometry("2000x1500")

etiqueta = tk.Label(
    ventana,
    text = "Brillo = 50%",
)
etiqueta.pack()

slider = tk.Scale(
    ventana,
    from_ = 0,
    to = 100,
    orient = "horizontal",
    command = al_mover
)
slider.pack()
slider.set(50)

boton1 = tk.Button(
    ventana,
    text = "Brillo máximo",
    command = lambda: cambiar(100)
)
boton1.pack()
boton2 = tk.Button(
    ventana,
    text = "Brillo mínimo",
    command = lambda: cambiar(0)
)
boton2.pack()
boton3 = tk.Button(
    ventana,
    text = "Brillo aleatorio",
    command = lambda: cambiar(random.randint(1,100))
)
boton3.pack()

ventana.mainloop()