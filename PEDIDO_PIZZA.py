import tkinter as tk
ventana = tk.Tk()
ventana.title("PEDIDO_PIZZA")
ventana.geometry("2000x1500")

def entrar(e):
    boton.config(fg = "yellow", bg = "grey")

def salir(e):
    boton.config(fg = "black", bg = "SystemButtonFace")

def command():
    boton.config(state = "normal")
    boton.bind("<Enter>", entrar)
    boton.bind("<Leave>", salir)

def al_click():
    etiqueta.config(text = f"Tu pedido: {var.get()}")

etiqueta = tk.Label(
    ventana,
    text="¿Que tamaño de pizza desea usted?",
)
etiqueta.pack(pady=20)

boton = tk.Button(
    ventana,
    text = "Comprobar pedido",
    command = al_click
)
boton.pack()
boton.config(state = "disabled")


var = tk.StringVar()
var.set("Ninguna")

p1 = tk.Radiobutton(ventana, text="Pequeña 5€", variable=var, value="Pizza pequeña por 5 euros", command = command)
p2 = tk.Radiobutton(ventana, text="Mediana 8€", variable=var, value="Pizza mediana por 8 euros", command = command)
p3 = tk.Radiobutton(ventana, text="Grande 12€", variable=var, value="Pizza grande por 12 euros ", command = command)
p4 = tk.Radiobutton(ventana, text="Familiar 15€", variable=var, value="Pizza familiar por 15 euros", command = command)

p1.pack()
p2.pack()
p3.pack()
p4.pack()

ventana.mainloop()
