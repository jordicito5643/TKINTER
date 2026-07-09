import tkinter as tk
import os
import sys
import random

variable_temporal = True

paso = 1

def atras():
    preguntar_nombre.place(x = 771, y = 60, anchor = "center")
    boton_atras.pack_forget()
    etiqueta.config(text = "Introduce tu nombre")
    etiqueta.config(fg = "black")
    boton.pack()
    
def al_seleccionar2():  
    boton.pack()

def regresar():
    global variable_temporal
    global paso
    paso = 2
    slider.set(0)
    etiqueta.config(text = f"Hola {nombre}. ¿Que quieres hacer hoy?")
    opcion1.pack()
    opcion2.pack()
    opcion3.pack()
    boton_operacion_aleatoria.pack()
    boton_restablecer.pack()
    slider.pack_forget()
    escoger_opcion.set("ninguna")
    boton_regresar.pack_forget()
    variable_temporal = True

    

def comprobar_boxes():
        if dato_booleano == True and var1.get() == False and var2.get() == False and var3.get() == False:
            boton.config(text = "Saltar")
            ventana.after(100, comprobar_boxes)
        elif dato_booleano == True and (var1.get() == True or var2.get() == True or var3.get() == True): 
            boton.config(text = "Ok")
            ventana.after(100, comprobar_boxes)

def modificar_saldo():
    global numero
    global saldo
    global paso
    opcion1.pack_forget()
    opcion2.pack_forget()
    opcion3.pack_forget()
    boton_restablecer.pack_forget()
    boton_operacion_aleatoria.pack_forget()
    etiqueta.config(text = "¿Estas segur@ de esto?, esto cambiara tu saldo tanto para bien como para mal")
    si.pack()
    no.pack()
    si_o_no.set("ninguna")
    paso = 10

def restablecer():
    os.execl(sys.executable, sys.executable, *sys.argv)

def al_seleccionar():
    global variable_temporal
    boton.config(text = "Aceptar")
    global dato_booleano
    if variable_temporal == True:
        if escoger_opcion.get() == "retirar":
            boton.pack()
            variable_temporal = False
        elif escoger_opcion.get() == "ingresar":
            boton.pack()
            variable_temporal = False
        elif escoger_opcion.get() == "consultar":
            boton.pack()
            variable_temporal = False
        dato_booleano = True
        
    
def mover(valor):
    global dato_booleano
    if dato_booleano == True:
        boton.pack()
        boton.config(text = "Finalizar")
        dato_booleano = False
    elif dato_booleano == False:    
        slider.config(label = f"{valor} Euros")

def al_click():
    global nombre
    global preguntar_nombre
    global saldo
    global saldo_nuevo
    global paso
    global dato_booleano2
    global si_o_no
    global dato_booleano
    global estado
    global variable_temporal
    
    if paso == 10:
        if si_o_no.get() == "si":
            numero = random.randint(0,100)
            signo = random.randint(1,2)
            if signo == 1:
                saldo = saldo + numero
            elif signo == 2:
                saldo = saldo - numero
            etiqueta.config(text = f"Nuevo saldo: {saldo} Euros")
            slider.config(to = saldo)
            boton_regresar.pack()
            boton.pack_forget()
            si.pack_forget()
            no.pack_forget()
            paso = 2
        elif si_o_no.get() == "no":
            si.pack_forget()
            no.pack_forget()
            regresar()
            boton.pack_forget()
            paso = 2
    elif paso == 1:
        escoger_opcion.set("ninguna")
        nombre = preguntar_nombre.get()
        numero_caracteres = len(nombre)
        if numero_caracteres < 5:
            preguntar_nombre.place_forget()
            boton.pack_forget()
            etiqueta.config(fg = "red")
            etiqueta.config(text = "Debes introducir al menos 5 caracteres")
            boton_atras.pack()
        else:
            etiqueta.config(fg = "black")
            preguntar_nombre.place_forget()
            etiqueta.config(text = f"Hola {nombre.capitalize()}. ¿Qué deseas hacer hoy?")
            preguntar_nombre.pack_forget()
            opcion1.pack()
            opcion2.pack()
            opcion3.pack()
            boton_operacion_aleatoria.pack()
            boton_restablecer.pack()
            paso = 2
            boton.pack_forget()
        
    elif paso == 2:
        if escoger_opcion.get() == "retirar" or escoger_opcion.get() == "ingresar":
            opcion1.pack_forget()
            opcion2.pack_forget()
            opcion3.pack_forget()
            boton_operacion_aleatoria.pack_forget()
            boton_restablecer.pack_forget()
            slider.pack()
            slider.set(0)
            slider.config(label = slider.get())
            boton.pack_forget()
            etiqueta.config(text = f"¿Cuando dinero desea usted {escoger_opcion.get()}?")
            paso = 3
            
        elif escoger_opcion.get() == "consultar":
            etiqueta.config(text = f"Saldo: {saldo}")
            opcion1.pack_forget()
            opcion2.pack_forget()
            opcion3.pack_forget()
            boton_regresar.pack()
            boton.pack_forget()
            boton_operacion_aleatoria.pack_forget()
            boton_restablecer.pack_forget()
            paso = 1
        
    elif paso == 3:
        p1.pack()
        p2.pack()
        p3.pack()
        slider.pack_forget()
        var1.set(False)
        var2.set(False)
        var3.set(False)
        variable_temporal = True
        dato_booleano = True
        etiqueta.config(text = "Seleccione las que desee, puede saltar si quiere")
        comprobar_boxes()
        paso = 4
        
    elif paso == 4:
        dato_booleano = False
        slider.pack_forget()
        p1.pack_forget()
        p2.pack_forget()
        p3.pack_forget()
        boton.config(text = "De acuerdo")
        etiqueta.config(text = "¿Estas seguro de esto? Esta operacion es irreversible")
        boton.pack_forget()
        si.pack()
        no.pack()
        si_o_no.set("ninguna")
        paso = 5
        
    elif paso == 5:
        if si_o_no.get() == "si":
            si.pack_forget()
            no.pack_forget()
            operador = int(slider.get())
            slider.pack_forget()
            if escoger_opcion.get() == "ingresar":
                saldo = int(saldo) + int(operador)#-------------------------------DEFINIMOS SALDO NUEVO
            elif escoger_opcion.get() == "retirar":
                saldo = saldo - operador#-------------------------------DEFINIMOS SALDO NUEVO
            if escoger_opcion.get() == "retirar":
                estado = "retirado"
            elif escoger_opcion.get() == "ingresar":
                estado = "ingresado"
            
            texto = f"""Ha {estado} {operador} euros. Nuevo saldo: {saldo}
            Opciones extras elegidas:
              Imprimir recibo: {"SI" if var1.get() else "NO"}
              Enviar SMS: {"SI" if var2.get() else "NO"}
              Guardar operacion en el historial: {"SI" if var3.get() else "NO"}"""
            slider.config(to = saldo)
            etiqueta.config(text = texto)
            boton.config(text = "Volver al menú")
            dato_booleano = True
            slider.set(0)
            paso = 1
        else:
            opcion1.pack_forget()
            opcion2.pack_forget()
            boton.pack_forget()
            si.pack_forget()
            no.pack_forget()
            slider.pack()
            etiqueta.config(text = f"¿Cuando dinero deseas {escoger_opcion.get()}")
            dato_booleano = True
            paso = 3
            

ventana = tk.Tk()
ventana.title("GESTION DE DINERO")
ventana.geometry("2000x1500")

etiqueta = tk.Label(ventana, text = "Introduce tu nombre")
etiqueta.pack()

saldo = 1000

preguntar_nombre = tk.Entry(ventana)
preguntar_nombre.place(x = 771, y = 60, anchor = "center")

boton = tk.Button(
    ventana,
    text = "Aceptar",
    command = al_click
)
boton.pack()

escoger_opcion = tk.StringVar()
escoger_opcion.set("ninguna")

opcion1 = tk.Radiobutton(ventana, text = "Ingresar dinero", variable = escoger_opcion, value = "ingresar", command = al_seleccionar)
opcion2= tk.Radiobutton(ventana, text = "Retirar dinero", variable = escoger_opcion, value = "retirar", command = al_seleccionar)
opcion3 = tk.Radiobutton(ventana, text = "Consultar mi saldo", variable = escoger_opcion, value = "consultar", command = al_seleccionar)

si_o_no = tk.StringVar()

si = tk.Radiobutton(ventana, text = "Sí", variable = si_o_no, value = "si", command = al_seleccionar2)
no = tk.Radiobutton(ventana, text = "No", variable = si_o_no, value = "no", command = al_seleccionar2)

slider = tk.Scale(
    ventana,
    from_ = 0,
    to = saldo,
    orient = "horizontal",
    command = mover
)

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

p1 = tk.Checkbutton(
    ventana,
    text = "Imprimir recibo",
    variable = var1
)

p2 = tk.Checkbutton(
    ventana,
    text = "Enviar SMS",
    variable = var2
)

p3 = tk.Checkbutton(
    ventana,
    text = "Guardar operacion en el historial",
    variable = var3
)

boton_operacion_aleatoria = tk.Button(
    ventana,
    text = "Operacion aleatoria",
    command = modificar_saldo
)

boton_restablecer = tk.Button(
    ventana,
    text = "Restablecer",
    command = restablecer
)

boton_regresar = tk.Button(
    ventana,
    text = "Regresar al menú",
    command = regresar
)

boton_atras = tk.Button(
    ventana,
    text = "Volver atrás",
    command = atras
)

ventana.mainloop()