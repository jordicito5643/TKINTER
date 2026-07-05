import tkinter as tk
lista=[]

def radio ():
    boton.config(state = "normal")

def al_clic ():
    boton.config(state = "normal")
    if var.get() == "respuesta1":
        etiqueta.config(text="Haay que bandolero")
    elif var.get() == "respuesta2":
        etiqueta.config(text="Que buena persona estas hecha")
    elif var.get() == "respuesta3":
        etiqueta.config(text="Al menos le das 5 euros, osea lo que vale la cartera")
    elif var.get() == "respuesta4":
        etiqueta.config(text="Entonces vendrá otro como tu y ya sabes lo que hará")

ventana = tk.Tk()
ventana.title("Personalidad")
ventana.geometry("2000x1500")

etiqueta = tk.Label(ventana, text="¿Qué harías si encontraras una cartera con dinero?")
etiqueta.pack(pady=20)
boton = tk.Button(
    ventana,
    text = "Veamos tu personalidad",
    command = al_clic,
)
boton.pack()
boton.config(state = "disabled")

var = tk.StringVar()
var.set("NADA")

opcion1 = tk.Radiobutton(ventana, text="Me la quedo toda", variable=var, value="respuesta1", command=radio)
opcion2 = tk.Radiobutton(ventana, text="La entrego a la policía", variable=var, value="respuesta2", command=radio)
opcion3 = tk.Radiobutton(ventana, text="Me quedo el dinero y entrego la cartera", variable=var, value="respuesta3", command=radio)
opcion4 = tk.Radiobutton(ventana, text="La dejo donde está", variable=var, value="respuesta4", command=radio)

opcion1.pack()
opcion2.pack()
opcion3.pack()
opcion4.pack()

ventana.mainloop()