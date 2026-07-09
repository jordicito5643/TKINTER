import tkinter as tk
import random 

def guardar():
    texto_correcto = f"""CONFIGURACION GUARDADA
    Volumen: {slider.get()}%
    Calidad: {var.get()}
    Repetir: {"Sí" if var1.get() == True else "No"}
    Aleatorio: {"Sí" if var2.get() == True else "No"}
    Mostrar Letras: {"Sí" if var3.get() == True else "No"}"""
    etiqueta.config(text = texto_correcto)
    
    
        
    
def boton1_def():
    slider.set(50)
    var.set("Media")
    var1.set(True)
    var2.set(False)
    var3.set(True)

def mover(valor):
    global numero_volumen
    etiqueta.config(text = f"Volumen: {valor}%")
    
def mover_2(valor):
    slider.set(valor)
    etiqueta.config(text = f"Volumen: {valor}%")
    
ventana = tk.Tk()
ventana.title("MUSIC PLAYER")
ventana.geometry("2000x1500")

etiqueta = tk.Label(ventana, text = "CONFIGURACIÓN DEL REPRODUCTOR")
etiqueta.pack(pady = 20)

slider = tk.Scale(
    ventana,
    from_ = 0,
    to = 100,
    orient = "horizontal",
    command = mover
)
slider.set(50)
slider.pack()

var = tk.StringVar()
var.set("Media")

p1 = tk.Radiobutton(ventana, text = "BAJA", variable = var, value = "Baja")
p2 = tk.Radiobutton(ventana, text = "MEDIA", variable = var, value = "Media")
p3 = tk.Radiobutton(ventana, text = "ALTA", variable = var, value = "Alta")

p1.pack()
p2.pack()
p3.pack()

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

opcion1 = tk.Checkbutton(ventana, text = "REPETIR CANCIÓN", variable = var1)
opcion2 = tk.Checkbutton(ventana, text = "MODO ALEATORIO", variable = var2)
opcion3 = tk.Checkbutton(ventana, text = "MOSTRAR LETRAS", variable = var3)

opcion1.pack()
opcion2.pack()
opcion3.pack()

boton1 = tk.Button(
    ventana,
    text = "RESTABLECER",
    command = boton1_def
)
boton1.pack()

boton2 = tk.Button(
    ventana,
    text = "VOLUMEN MÁXIMO",
    command = lambda: mover_2(100)
)
boton2.pack()

boton3 = tk.Button(
    ventana,
    text = "VOLUMEN MÍNIMO",
    command = lambda : mover_2(0)
)
boton3.pack()

boton4 = tk.Button(
    ventana,
    text = "VOLUMEN ALEATORIO",
    command = lambda: mover_2(random.randint(0,100))
)
boton4.pack()

boton5 = tk.Button(
    ventana,
    text = "GUARDAR CONFIGURACION",
    command = guardar
)

boton5.pack()
ventana.mainloop()