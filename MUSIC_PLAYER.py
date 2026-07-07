import tkinter as tk
import random 

texto1 = """Repetir: Sí
Aleatorio: Sí
Mostrar letras: Sí"""

texto2 = """Repetir: Sí
Aleatorio:Sí
Mostrar letras: No"""

texto3 = """Repetir: Sí
Aleatorio: No
Mostrar letras: Sí"""

texto4 = """Repetir: Sí
Aleatorio: No
Mostrar letras: No"""

texto5 = """Repetir: No
Aleatorio: Sí
Mostrar letras: Sí"""

texto6 = """Repetir: No
Aleatorio: Sí
Mostrar letras: No"""

texto7 = """Repetir: No
Aleatorio: No
Mostrar letras: Sí"""

texto8 = """Repetir: No
Aleatorio: No
Mostrar letras: No"""

def guardar():
    global datos_guardar
    global variable_guardar
    if var1.get() == True:
        if var2.get() == True:
            if var3.get() == True:    
                variable_guardar = texto1
            elif var3.get()==False:
                variable_guardar = texto2
        elif var2.get() == False:
            if var3.get() == True:
                variable_guardar = texto3
            elif var3.get() == False:
                variable_guardar = texto4
                
    elif var1.get() == False:
        if var2.get() == True:
            if var3.get() == True:
                variable_guardar = texto5
            elif var3.get() == False:
                variable_guardar = texto6
        elif var2.get() == False:
            if var3.get() == True:
                variable_guardar = texto7
            elif var3.get() == False:
                variable_guardar = texto8
                
    global variable_calidad
    if var.get() == "calidad_baja":
        variable_calidad = "Baja"
        
    elif var.get() == "calidad_media":
        variable_calidad = "Media"
    
    elif var.get() == "calidad_alta":
        variable_calidad = "Alta"
        
    datos_guardar = f"""Volumen: {numero_volumen}%
    Calidad: {variable_calidad}
    {variable_guardar}
    """
        
    etiqueta.config(text = datos_guardar)
    
    
        
    
def boton1_def():
    slider.set(50)
    var.set("calidad_media")
    var1.set(True)
    var2.set(False)
    var3.set(True)

def mover(valor):
    global numero_volumen
    numero_volumen = valor
    etiqueta.config(text = f"Volumen: {valor}%")
    
def mover_2(valor):
    slider.set(valor)
    etiqueta.config(text = "Volumen: {valor}%")
    
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
var.set("calidad_media")

p1 = tk.Radiobutton(ventana, text = "BAJA", variable = var, value = "calidad_baja")
p2 = tk.Radiobutton(ventana, text = "MEDIA", variable = var, value = "calidad_media")
p3 = tk.Radiobutton(ventana, text = "ALTA", variable = var, value = "calidad_alta")

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