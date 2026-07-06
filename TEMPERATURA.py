import tkinter as tk
def comando():
    boton.config(state = "normal")
    boton.bind("<Enter>", entrar)
    boton.bind("<Leave>", salir)
    
def entrar(e):
    boton.config(fg = "yellow", bg = "blue")
    
def salir(e):
    boton.config(fg = "black", bg = "SystemButtonFace")

def al_click():
    global resultado
    global grados_reales
    global grados
    global temperatura
    if var.get() == "primera conversion":
        temperatura = float(grados.get())
        grados_reales = (temperatura * 9/5) +32
        grados_reales = str(grados_reales)
        etiqueta.config(text = f"{grados}°C = {grados_reales}°F")
    
    elif var.get() == "segunda conversion":
        temperatura = float(grados.get())
        grados_reales = (temperatura - 32) * 5/9
        grados_reales = str(grados_reales)
        etiqueta.config(text = f"{temperatura}°F = {grados_reales}°C")
        
    elif var.get() == "tercera conversion":
        temperatura = float(grados.get())
        grados_reales = temperatura + 273.15
        grados_reales = str(grados_reales)
        etiqueta.config(text = f"{temperatura}°C = {grados_reales}K")
         
ventana = tk.Tk()
ventana.title("TEMPERATURA")
ventana.geometry("1000x500")

etiqueta = tk.Label(ventana, text = "Selecciona una opcion")
etiqueta.pack(pady = 20)

grados = tk.Entry(ventana, text = "Selecciona temperatura")
grados.pack(pady = 23)

boton = tk.Button(
    ventana,
    text = "Convertir",
    command = al_click
)
boton.pack()
boton.config(state = "disabled")

var = tk.StringVar()
var.set("ninguna")

p1 = tk.Radiobutton(ventana, text = "Celsius a Fahrenheit", variable = var, value = "primera conversion", command = comando)
p2 = tk.Radiobutton(ventana, text = "Fahrenheit a Celsius", variable = var, value = "segunda conversion", command = comando)
p3 = tk.Radiobutton(ventana, text = "Celsius a Kelvin", variable = var, value = "tercera conversion", command = comando)

p1.pack()
p2.pack()
p3.pack()

ventana.mainloop()


