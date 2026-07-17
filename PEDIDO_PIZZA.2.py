import tkinter as tk
paso = 1

def proseguir():
    if len(preguntar_nombre.get()) == 0 :
        boton.config(state = "disabled")
        ventana.after(1000, proseguir)
    elif len(preguntar_nombre.get()) != 0 :
        boton.config(state = "normal")
        ventana.after(1000, proseguir)

def al_click_menos_1():
    global paso
    global preguntar_nombre
    while paso == 20:
        preguntar_nombre.pack()
        preguntar_nombre.set("")
        boton.config(text = "Aceptar")
        paso = 1

def al_click1():
    global paso
    if paso == 1:
        preguntar_nombre.place_forget
        if len(preguntar_nombre.get()) < 3:
            preguntar_nombre.place_forget()
            etiqueta.config(text = "Tu nombre debe tener minimo 3 caracteres")
            etiqueta.config(fg = "red")
            paso = 20
            boton.config(text = "Volver")
        else:
            print("HOLA MUNDO")
    elif paso == 20:
        preguntar_nombre.pack()
        boton.config(text = "Aceptar")
        paso = 1

            
        

ventana = tk.Tk()
ventana.title("PEDIDO DE PIZZA")
ventana.geometry("2000x1500")

etiqueta = tk.Label(
    ventana,
    text = "Introduce tu nombre",
)
etiqueta.pack()

preguntar_nombre = tk.Entry(ventana)
preguntar_nombre.place(x = "771", y = "40", anchor = "center")

boton = tk.Button(
    ventana,
    text = "OK",
    command = al_click1
)
boton.place(x = "771", y = "110 ", anchor = "center")
boton.config(state = "disabled")
proseguir()
ventana.mainloop()