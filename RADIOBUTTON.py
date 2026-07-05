import tkinter as tk

def al_click():
    if var.get() == "respuesta1":
        etiqueta.config(text="Eres buena persona")
    else:
        etiqueta.config(text="Eres mala persona")
        
ventana = tk.Tk()
ventana.title("RADIOBUTTON")
ventana.geometry("800x300")

etiqueta=tk.Label(
    ventana,
    text="Selecciona una opcion",
)
etiqueta.pack(pady=20)

boton=tk.Button(
    ventana,
    text="Ver resultados",
    command=al_click
)
boton.pack()
var=tk.StringVar()
var.set("ninguna")

opcion1=tk.Radiobutton(ventana, text="A un perro", variable=var, value="respuesta1")
opcion2=tk.Radiobutton(ventana, text="A un delincuente", variable=var, value="respuesta2")
opcion3=tk.Radiobutton(ventana, text="A un asesino", variable=var, value="respuesta3")

opcion1.pack()
opcion2.pack()
opcion3.pack()

ventana.mainloop()