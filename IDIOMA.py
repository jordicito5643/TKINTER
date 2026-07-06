import tkinter as tk
ventana = tk.Tk()
ventana.title("IDIOMAS")
ventana.geometry("1000x500")

def identificar_idioma():
    if var.get() == "ingles":
        etiqueta.config(text = "Hello!")
    elif var.get() == "español":
        etiqueta.config(text = "¡Hola!")
    elif var.get() == "frances":
        etiqueta.config(text = "Bonjour!")
    elif var.get() == "aleman":
        etiqueta.config(text = "Guten Tag")
    

etiqueta = tk.Label(ventana, text = "Elige un idioma")
etiqueta.pack(pady = 20)

var = tk.StringVar()
var.set("Ninguna")

p1 = tk.Radiobutton(ventana, text = "Ingles", variable = var, value = "ingles", command = identificar_idioma)
p2 = tk.Radiobutton(ventana, text = "Español", variable = var, value = "español", command = identificar_idioma)
p3 = tk.Radiobutton(ventana, text = "Francés", variable = var, value = "frances", command = identificar_idioma)
p4 = tk.Radiobutton(ventana, text = "Alemán", variable = var, value = "aleman", command = identificar_idioma)

p1.pack()
p2.pack()
p3.pack()
p4.pack()

ventana.mainloop()
