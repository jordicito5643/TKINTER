"CORRECCION TRABAJO GERIATRIA"
"Tareas oriol"
import tkinter as tk
import sys
pregunta="incorrecta"
paso=1
pasito=1
estado=1

lista=[]


def buscar():
    global numero
    numero=len(lista)
    if numero>1:
        etiqueta_error.config(text="No puedes seleccionar más de una opcion")
        boton.config(state="disabled")
    elif len(lista)==0:
        etiqueta_error.config(text="Selecciona al menos una opcion")
        boton.config(state="disabled")
    else:
        etiqueta_error.config(text="")
        boton.config(state="normal")

def al_click():
    global pasito
    global paso
    global estado
    if paso==1:
        paso=2
        etiqueta.config(text=pregunta_geriatria)
        boton.config(text="Ir a las preguntas")
    elif paso==2:
        etiqueta.pack_forget()
        boton.pack()
        boton_anterior.pack(side="left")
        opcionA.pack()
        opcionB.pack()
        opcionC.pack()
        opcionD.pack()
        opcionE.pack()
        opcionF.pack()
        opcionG.pack()
        opcionH.pack()
        boton.config(text="Estoy segur@ de que es la correcta")
        paso=3
    elif paso==3:
        etiqueta.pack()
        paso=4
        opcionA.pack_forget()
        opcionB.pack_forget()
        opcionC.pack_forget()
        opcionD.pack_forget()
        opcionE.pack_forget()
        opcionF.pack_forget()
        opcionG.pack_forget()
        opcionH.pack_forget()
        boton_anterior.pack_forget()
        boton.config(text="Siguiente pregunta")
        if lista[0]=="respuesta3":
            etiqueta.config(text="Muy bien neyva, lo has logrado, SOLO UNA NEURONA TENIA ESA INFORMACIÓN")
        else:
            etiqueta.config(text=prueba_respuesta)
    elif paso==4:
        paso=5
        etiqueta.config(text=pregunta_ingles)
        boton.config(text="Avanzar a las preguntas")
    elif paso==5:
        var1.set(False)
        var2.set(False)
        var3.set(False)
        var4.set(False)
        var5.set(False)
        var6.set(False)
        var7.set(False)
        var8.set(False)
        paso=6
        etiqueta.pack_forget()
        boton_anterior.pack(side="left")
        boton.pack()
        boton.config(text="Estoy seguro de mi respuesta")
        pasito=1
        lista.clear()
        opcionA.config(text="LEFT")
        opcionB.config(text="HAS LEFT")
        opcionC.config(text="IS LEAVING")
        opcionD.config(text="WAS LEAVING")
        opcionE.config(text="HAS BEEN LEAVING")
        opcionF.config(text="WOULD HAVE")
        opcionG.config(text="LEAVES")
        opcionH.config(text="HAD LEFT")
        opcionA.pack()
        opcionB.pack()
        opcionC.pack()
        opcionD.pack()
        opcionE.pack()
        opcionF.pack()
        opcionG.pack()
        opcionH.pack()
        estado=2
    elif paso==6:
        paso=7
        etiqueta.pack()
        opcionA.pack_forget()
        opcionB.pack_forget()
        opcionC.pack_forget()
        opcionD.pack_forget()
        opcionE.pack_forget()
        opcionF.pack_forget()
        opcionG.pack_forget()
        opcionH.pack_forget()
        boton_anterior.pack_forget()
        if lista[0]=="respuesta8":
            etiqueta.config(text="MUY BIEN, (pero sabemos que ha sido suerte)")
        else:
            etiqueta.config(text=explicacion_pregunta_ingles)
        boton.config(text="FINALIZAR")
    elif paso==7:
        sys.exit()
            
    
        

def al_click2():
    global pasito
    if pasito==1 and estado==1:
        etiqueta.pack(pady=20)
        opcionA.pack_forget()
        opcionB.pack_forget()
        opcionC.pack_forget()
        opcionD.pack_forget()
        opcionE.pack_forget()
        opcionF.pack_forget()
        opcionG.pack_forget()
        opcionH.pack_forget()
        pasito=2
        etiqueta.config(text=pregunta_geriatria)
        boton.pack_forget()
        boton_anterior.config(text="Siguiente")
    elif pasito==2 and estado==1:
        boton.pack()
        etiqueta.pack_forget()
        opcionA.pack()
        opcionB.pack()
        opcionC.pack()
        opcionD.pack()
        opcionE.pack()
        opcionF.pack()
        opcionG.pack()
        opcionH.pack()
        boton.config(text="Estoy segur@ de que es la correcta")
        boton_anterior.pack(side="left")
        boton_anterior.config(text="Anterior")
        pasito=1
        
    elif pasito==1 and estado==2:
        etiqueta.pack(pady=20)
        opcionA.pack_forget()
        opcionB.pack_forget()
        opcionC.pack_forget()
        opcionD.pack_forget()
        opcionE.pack_forget()
        opcionF.pack_forget()
        opcionG.pack_forget()
        opcionH.pack_forget()
        pasito=2
        etiqueta.config(text=pregunta_ingles)
        boton_anterior.config(text="Siguiente")
        boton.pack_forget()
    
    elif pasito==2 and estado==2:
        boton.pack()
        etiqueta.pack_forget()
        opcionA.pack()
        opcionB.pack()
        opcionC.pack()
        opcionD.pack()
        opcionE.pack()
        opcionF.pack()
        opcionG.pack()
        opcionH.pack()
        pasito=1
        boton.config(text="Estoy segur@ de que es la correcta")
        boton_anterior.pack(side="left")
        boton_anterior.config(text="Anterior")
    
def command1():
    global pregunta
    
    #VAR 1
    if var1.get()==True:
        pregunta="incorrecta"
        lista.append("respuesta1")
        buscar()
    elif var1.get()==False:
        if "respuesta1" in lista:
            lista.remove("respuesta1")
            buscar()
            
def command2():
    #VAR 2        
    if var2.get()==True:
        pregunta="incorrecta"
        lista.append("respuesta2")
        buscar()
    elif var2.get()==False:
        if "respuesta2" in lista:
            lista.remove("respuesta2")
            buscar()
            
def command3():    
    #VAR 3
    if var3.get()==True:
        pregunta="correcta"
        lista.append("respuesta3")
        buscar()
    elif var3.get()==False:
        if "respuesta3" in lista:
            lista.remove("respuesta3")
            buscar()
            
def command4():
    #VAR 4        
    if var4.get()==True:
        pregunta="incorrecta"
        lista.append("respuesta4")
        buscar()
    elif var4.get()==False:
        if "respuesta4" in lista:
            lista.remove("respuesta4")
            buscar()
            
def command5():            
    #VAR 5        
    if var5.get()==True:
        pregunta="incorrecta"
        lista.append("respuesta5")
        buscar()
    elif var5.get()==False:
        if "respuesta5" in lista:
            lista.remove("respuesta5")
            buscar()

def command6():    
    #VAR 6        
    if var6.get()==True:
        pregunta="incorrecta"
        lista.append("respuesta6")
        buscar()
    elif var6.get()==False:
        if "respuesta6" in lista:
            lista.remove("respuesta6")
            buscar()

def command7():         
    #VAR 7
    if var7.get()==True:
        pregunta="incorrecta"
        lista.append("respuesta7")
        buscar()
    elif var7.get()==False:
        if "respuesta7" in lista:
            lista.remove("respuesta7")  
            buscar()    

def command8():    
    #VAR 8
    if var8.get()==True:
        pregunta="incorrecta"
        lista.append("respuesta8")
        buscar()
    elif var8.get()==False:
        if "respuesta8" in lista:
            lista.remove("respuesta8")  
            buscar()
    
        

ventana=tk.Tk()
ventana.title("Pregunta geriatria")
ventana.geometry("2000x1800")

etiqueta_error = tk.Label(
    ventana, 
    text="",
    fg="red",
    wraplength=1800
)
etiqueta_error.pack()

prueba_respuesta="""MAL, la opcion correcta era la 3, porque la evidencia muestra que, en pacientes geriátricos con fragilidad,
multimorbilidad y polifarmacia, la Valoración Geriátrica Integral (VGI) junto con una intervención multicomponentee individualizada 
es la estrategia que más mejora la funcionalidad, reduce delirium, caídas e institucionalización y optimiza la calidad de vida.
Además, respeta las preferencias de la paciente, priorizando objetivos clínicos centrados en la persona en lugar de tratar enfermedades de forma aislada."""

pregunta_geriatria=f"""Una mujer de 92 años vive sola y era independiente hasta hace 4 meses (Índice de Barthel 95/100). 
Presenta pérdida ponderal del 11% en 5 meses, dos caídas recientes, enlentecimiento de la marcha (0,58 m/s),
fuerza de prensión disminuida, fatiga intensa y disminución de la actividad física. Tiene:

Insuficiencia cardiaca con FE preservada.
Enfermedad renal crónica estadio G4 (TFGe 24 ml/min/1,73 m²).
Diabetes mellitus tipo 2.
Fibrilación auricular permanente.
Osteoporosis con fractura vertebral previa.
Deterioro cognitivo leve confirmado por biomarcadores compatibles con enfermedad de Alzheimer.
Anemia normocítica (Hb 9,8 g/dL).
Hipotensión ortostática sintomática.
Polineuropatía diabética.
Incontinencia urinaria de urgencia.
Depresión parcialmente tratada.

Tratamiento actual:
Apixabán
Empagliflozina
Furosemida
Espironolactona
Sacubitrilo/valsartán
Metformina
Insulina basal
Donepezilo
Sertralina
Pregabalina
Oxibutinina
Omeprazol
Atorvastatina

Analítica:
Albúmina 2,9 g/dL
PCR 31 mg/L
Vitamina D 11 ng/mL
Ferritina 420 ng/mL
Saturación de transferrina 15%
NT-proBNP elevado
HbA1c 6,2%

Durante el ingreso desarrolla un delirium hipoactivo sin causa infecciosa demostrable. La familia solicita "hacer todo lo posible", mientras que la paciente, 
en momentos de lucidez, afirma repetidamente que su mayor prioridad es "seguir viviendo en casa aunque viva menos tiempo".

Según la mejor evidencia disponible en geriatría moderna, considerando simultáneamente fisiopatología del envejecimiento, deprescripción, medicina basada en 
la evidencia, ética clínica, pronóstico, prevención cuaternaria, valoración geriátrica integral y preferencias del paciente, ¿cuál es la intervención inicial 
que maximiza la probabilidad de mejorar supervivencia libre de discapacidad y calidad de vida a 12 meses?"""

pregunta_ingles="""English A1 QUESTION
Choose the correct option to complete the sentence:
By the time we arrived at the station, the train ________."""

explicacion_pregunta_ingles="""MUY MAL, PERO SI ES A1, COMO HAS PODIDO FALLAR. Se usa el past perfect (had left) 
para indicar que una acción ocurrió antes de otra acción pasada (we arrived). 
La estructura "By the time..." suele requerir este tiempo verbal cuando un hecho ya había finalizado antes del otro."""

opcion_numero_c_geriatria="""C) Realizar una Valoración Geriátrica Integral multidimensional inmediata, establecer objetivos terapéuticos centrados en la paciente, 
iniciar un programa multifactorial de reversión de fragilidad (ejercicio multicomponente, soporte nutricional, revisión/deprescripción sistemática de fármacos 
con carga anticolinérgica y riesgo de hipotensión, prevención del delirium, corrección de déficits reversibles y planificación anticipada de decisiones), aceptando objetivos menos 
estrictos para factores de riesgo tradicionales cuando exista beneficio neto."""

etiqueta=tk.Label(
    ventana,
    text="Hola Neyva, hoy vas a resolver un problema facil de geriatria, cuando estes lista le das al boton.",
    wraplength=1800,
    justify="left"
)
etiqueta.pack(pady=20)


boton=tk.Button(
    ventana,
    text="I am ready, ¡Lets go!",
    command=al_click
)
boton.pack()
var1=tk.BooleanVar()
var2=tk.BooleanVar()
var3=tk.BooleanVar()
var4=tk.BooleanVar()
var5=tk.BooleanVar()
var6=tk.BooleanVar()
var7=tk.BooleanVar()
var8=tk.BooleanVar()

boton_anterior=tk.Button(
    ventana,
    text="Ventana anterior",
    command=al_click2
)

opcionA=tk.Checkbutton(
    ventana,
    text="A) Optimizar el tratamiento cardiovascular intensificando la terapia de insuficiencia cardiaca hasta dosis objetivo, mantener todos los tratamientos preventivos y añadir hierro intravenoso.",
    command=command1,
    variable=var1
)
var=tk.BooleanVar()
opcionB=tk.Checkbutton(
    ventana,
    text="B) Priorizar el control glucémico estricto (HbA1c <6%), mantener la prevención cardiovascular completa e iniciar rehabilitación tras el alta.",
    command=command2,
    variable=var2
)
var=tk.BooleanVar()
opcionC=tk.Checkbutton(
    ventana,
    text=opcion_numero_c_geriatria,
    command=command3,
    variable=var3
)
var=tk.BooleanVar()
opcionD=tk.Checkbutton(
    ventana,
    text="D) Suspender toda medicación preventiva por la edad avanzada, limitar el tratamiento exclusivamente al control sintomático e iniciar cuidados paliativos exclusivos.",
    command=command4,
    variable=var4
)
var=tk.BooleanVar()
opcionE=tk.Checkbutton(
    ventana,
    text="E) Priorizar el tratamiento específico del deterioro cognitivo añadiendo un anticuerpo antiamiloide y mantener sin cambios el resto del tratamiento hasta estabilizar la función cognitiva.",
    command=command5,
    variable=var5
)
var=tk.BooleanVar()
opcionF=tk.Checkbutton(
    ventana,
    text="F) Mantener el tratamiento actual, ya que modificar simultáneamente múltiples variables aumenta el riesgo de eventos adversos y dificulta identificar la causa de futuras complicaciones.",
    command=command6,
    variable=var6
)
var=tk.BooleanVar()
opcionG=tk.Checkbutton(
    ventana,
    text="G) Ingresar de forma permanente en una residencia geriátrica para reducir el riesgo de caídas y asegurar la adherencia terapéutica.",
    command=command7,
    variable=var7
)
var=tk.BooleanVar()
opcionH=tk.Checkbutton(
    ventana,
    text="H) Suspender únicamente los medicamentos potencialmente inapropiados según criterios STOPP/START y no realizar otras intervenciones, dado que la evidencia sobre programas multicomponente en nonagenarios es insuficiente.",
    command=command8,
    variable=var8
)
ventana.mainloop()