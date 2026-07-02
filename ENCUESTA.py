"ENCUESTA"
"ENCUESTA"
import tkinter as tk 
lista_hobbies=[]
paso=1

def command():
    lista_hobbies.clear()
    if var1.get()==True:
        lista_hobbies.append("Fútbol")
    if var2.get()==True:
        lista_hobbies.append("Jugar Videojuegos")
    if var3.get()==True:
        lista_hobbies.append("Leer")
    boton.pack()
    
    
def al_click():
    global paso
    global nombre
    if paso==1:
        nombre=str(preguntar_nombre.get())
        if nombre=="":
            etiqueta.config(text="Introduce un nombre válido")
        else:
            etiqueta.config(text=f"Hola {nombre}, ahora escoge al menos una opcion de las siguientes:")
            preguntar_nombre.pack_forget()
            opcion1.pack()
            opcion2.pack()
            opcion3.pack()
            paso=2
        
    
    elif paso==2:
         global numero_opciones
         global texto
         if not lista_hobbies:
            etiqueta.config(text="Debes marcar al menos una opcion")
         else:
            numero_opciones=len(lista_hobbies)
            if numero_opciones==1:
                texto=lista_hobbies[0]
            elif numero_opciones==2:
                texto=f"{lista_hobbies[0]} y {lista_hobbies[1]}"
            else:
                texto=f"{', '.join(lista_hobbies[:-1])} y {lista_hobbies[-1]}"
            etiqueta.config(text=f"Tu nombre es {nombre} y te gusta {texto}")


       
def decir_nombre():
    global nombre
    if nombre=="":
        etiqueta.config(text="Introduce un nombre válido")
    else:
        etiqueta.config(text=f"Hola {nombre}, ahora escoge al menos una opcion de las siguientes:")

ventana=tk.Tk()
ventana.title("Hobbies")
ventana.geometry("2000x1500")

etiqueta=tk.Label(ventana, text="Introduce nombre y luego selecciona al menos 1 hobbie")
etiqueta.pack(pady=20)

preguntar_nombre=tk.Entry(ventana)
preguntar_nombre.pack()

var1=tk.BooleanVar()
var2=tk.BooleanVar()
var3=tk.BooleanVar()

boton=tk.Button(
    ventana,
    text="Registrar",
    command=al_click,
)
boton.pack()


opcion1=tk.Checkbutton(
    ventana,
    text="Programar",
    command=command,
    variable=var1
)


opcion2=tk.Checkbutton(
    ventana,
    text="Jugar Videojuegos",
    command=command,
    variable=var2
)


opcion3=tk.Checkbutton(
    ventana,
    text="Leer",
    command=command,
    variable=var3
)

ventana.mainloop()