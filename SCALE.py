import tkinter as tk

ventana = tk.Tk()
ventana.title("SCALE")
ventana.geometry("3000x1500")

def definir_valor():
    slider.set(99)

def al_mover(valor):
    etiqueta.config(text = valor)

etiqueta = tk.Label(ventana, text = "")
etiqueta.pack(pady = 20)

slider = tk.Scale(
    ventana,
    from_ = 0,
    to = 100,
    orient = "horizontal",
    command = al_mover
)

boton = tk.Button(
    ventana,
    text = "Ir directo a 99",
    command = definir_valor
)
boton.pack()
slider.pack()

ventana.mainloop()