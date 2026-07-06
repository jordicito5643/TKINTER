import tkinter as tk

def entrar (e):
    boton.config(fg = "yellow", bg = "blue")
    etiqueta.config(text = e)
    
def salir(e):
    boton.config(fg = "black", bg = "SystemButtonFace")
    etiqueta.config(text = e)

def botonazo():
     boton.pack()
     boton.bind("<Enter>", entrar)
     boton.bind("<Leave>", salir)
     
def al_click():
    global precio
    global propina
    global precio_total
    if total.get() == "":
        etiqueta.config(text = "Tienes que escribir un precio")
    
    else:
        precio = float(total.get())
        if var.get() == "primer descuento":
            propina = (10 * precio)/100
            precio_total = precio + propina
        elif var.get() == "segundo descuento":
            propina = (15 * precio)/100
            precio_total = precio + propina
        elif (var.get()) == "tercer descuento":
            propina = (20 * precio)/100
            precio_total = precio + propina
        etiqueta.config(text = f"Propina : {propina} -- Precio total: {precio_total}")
        


ventana = tk.Tk()
ventana.title("DESCUENTO")
ventana.geometry("1000x500")

etiqueta = tk.Label(ventana, text = "Introduce precio total y selecciona una de las propinas")
etiqueta.pack(pady = 20)

total = tk.Entry(ventana, text = "Introduce el precio total de la compra: ")
total.pack()

boton = tk.Button(
    ventana,
    text = "CALCULAR",
    command = al_click
)


var = tk.StringVar()
var.set("ninguna")

p1 = tk.Radiobutton(ventana, text = "10%", variable = var, value = "primer descuento", command = botonazo)
p2 = tk.Radiobutton(ventana, text = "15%", variable = var, value = "segundo descuento", command = botonazo)
p3 = tk.Radiobutton(ventana, text = "20%", variable = var, value = "tercer descuento", command = botonazo)

p1.pack()
p2.pack()
p3.pack()

ventana.mainloop()