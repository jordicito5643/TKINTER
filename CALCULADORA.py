"CALCULADORA"
import tkinter as tk
import sys
def salir():
    sys.exit()
def sumar():
    a=float(caja1.get())
    b=float(caja2.get())
    resultado=a+b
    resultado=str(resultado)
    etiqueta.config(text=f"El resultado de la suma de {a} + {b} es : {resultado}")

def restar():
    a=float(caja1.get())
    b=float(caja2.get())
    resultado=a-b
    etiqueta.config(text=f"El resultado de la resta de {a} - {b} es : {resultado}")
    resultado=str(resultado)

def multiplicar():
    a=float(caja1.get())
    b=float(caja2.get())
    resultado=a*b
    resultado=str(resultado)
    etiqueta.config(text=f"El resultado de la multiplicación de {a} * {b} es : {resultado}")

def dividir():
    a=float(caja1.get())
    b=float(caja2.get())
    if b==0:
        etiqueta.config(text="No puedes dividir entre 0")
    else:
        resultado=a/b
        resultado=str(resultado)
        etiqueta.config(text=f"El resultado de la division de {a} / {b} es : {resultado}")

ventana=tk.Tk()
ventana.title("OPERACIONES")
ventana.geometry("2000x1500")

etiqueta=tk.Label(ventana, text="Dime dos numeros")
etiqueta.pack(pady=20)

caja1=tk.Entry(ventana)
caja1.pack()
caja2=tk.Entry(ventana)
caja2.pack()
boton_sumar=tk.Button(
    ventana,
    text="Sumar",
    command=sumar
)
boton_sumar.pack()

boton_restar=tk.Button(
    ventana,
    text="Restar",
    command=restar
)
boton_restar.pack()

boton_multiplicar=tk.Button(
    ventana,
    text="Multiplicar",
    command=multiplicar
)
boton_multiplicar.pack()

boton_dividir=tk.Button(
    ventana,
    text="Dividir",
    command=dividir
)
boton_dividir.pack()

boton_salir=tk.Button(
    ventana,
    text="SALIR",
    command=salir
)
boton_salir.pack(pady=310)

ventana.mainloop()