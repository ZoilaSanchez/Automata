from tkinter import*
from tkinter import messagebox
import ctypes
import re


#configurar la pantalla del programa de acuerdo a la compu
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
resul=str(ancho)+"x"+str(alto)

#configurar root que seria la ventana en si
root=Tk()
root.config(bg="white")
root.geometry(resul)
root.resizable(width=0, height=0)

#configurar el frame donde se insertaran los demas botones
miframe=Frame(root,width=ancho,height=alto)
miframe.config(bg="Black")
miframe.pack()

#generar los nombres para cada texto
cadenalable=Label(miframe,text="Automata: ")
cadenalable.place(x=50,y=75)
cadenalable.config(fg="Green Yellow",bg="Black")#cambiar el color

comprobacionlable=Label(miframe,text="Ingrese la Cadena: ")
comprobacionlable.place(x=50,y=300)
comprobacionlable.config(fg="Green Yellow",bg="Black")#cambiar el color

dibujolabel=Label(miframe,text="Dibujar")
dibujolabel.place(x=1250,y=50)
dibujolabel.config(fg="Green Yellow",bg="Black")#cambiar el color

##Generar cuadros de texto
automatatxt=Text(miframe,width=40 ,height=6)#poscion del dibujo # esto me ayuda a extraer el lengueja
automatatxt.place(x=70,y=120)
automatatxt.config(fg="blue",bg="white")

comcadena=Text(miframe,width=40,height=6)#poscion del dibujo# esto lo introducira andrea 
comcadena.place(x=70,y=350)
comcadena.config(fg="blue",bg="white")

dibujotxt=Text(miframe,width=128,height=45)#poscion del dibujo # esto es para dibujar
dibujotxt.place(x=600,y=100)
dibujotxt.config(fg="blue",bg="white")

#Estas con las variable a utilizar
lenguaje=[]
validacion_texto_vacio=""
cadenita=""
#generar botones eventos
def extraerautomata():
    autos = automatatxt.get("1.0","end-1c")
    autoss = autos.lower()
    autosss =autoss.strip()
    aut=autosss.replace(" ", "")
    auto= re.sub(r"\s+", "", aut)
    if(not auto): #1
        messagebox.showwarning(message="cadena vacia", title="Aviso")
    else:  #ceramos el if 1
        lenguaje=[]  
        ver=[]
        numeros=["0","1","2","3","4","5","6","7","8","9"]
        for item in numeros:
            if(auto.find(item)>=0):#2
                ver.append("true")
            else:#cerramos if 2
                print('',end="")
        if(len(ver)>0): #3
            messagebox.showerror(message="Cadena contiene numeros", title="Aviso")
        else:    #cerramos if 3
            comparacioncadena=auto
            resultado=comparacioncadena
            v=frecuencia(resultado)  
            for i in v:
                lenguaje.append(i)

            alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","x","z"]
            simbolosaceptados=["*","|","(",")"]
            mostrarlen=[]
            sim=[]
            erroes=[]
            for i in lenguaje:
                for x in alfabeto:
                    if(i==x):
                        mostrarlen.append(i)
            
            copia=lenguaje
            print(copia)     
            print(mostrarlen)     
            for z in mostrarlen:
                copia.remove(z)
            print(copia)
            for item in copia:
                sim.append(item)
            print(sim)
            if(not sim):
                print("no hay simbolos")
                #tamcine se puede hacer qeu sea correcto
            else:    
                for item in sim:
                    x=simbolosaceptados.count(item)
                    if(x==0):
                        erroes.append("no")
                    else:
                         print('',end="")
                if(not erroes):
                    print("correcto")
                #aqui la cadena es correcta
                else:
                     messagebox.showerror(message="simbolos incorrecto", title="Aviso")   


def extraercadena():
    autos = comcadena.get("1.0","end-1c")
    autoss = autos.lower()
    autosss =autoss.strip()
    aut=autosss.replace(" ", "")
    auto= re.sub(r"\s+", "", aut)
    if(not auto): #1
        messagebox.showwarning(message="cadena vacia", title="Aviso")
    else:  #ceramos el if 1
        lenguaje=[]  
        ver=[]
        numeros=["0","1","2","3","4","5","6","7","8","9"]
        for item in numeros:
            if(auto.find(item)>=0):#2
                ver.append("true")
            else:#cerramos if 2
                print('',end="")
        if(len(ver)>0): #3
            messagebox.showerror(message="Cadena contiene numeros", title="Aviso")
        else:    #cerramos if 3
            comparacioncadena=auto
            resultado=comparacioncadena
            v=frecuencia(resultado)  
            for i in v:
                lenguaje.append(i)

            alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","x","z"]
            simbolosaceptados=["*","|","(",")"]
            mostrarlen=[]
            sim=[]
            erroes=[]
            for i in lenguaje:
                for x in alfabeto:
                    if(i==x):
                        mostrarlen.append(i)
            
            copia=lenguaje
            print(copia)     
            print(mostrarlen)     
            for z in mostrarlen:
                copia.remove(z)
            print(copia)
            for item in copia:
                sim.append(item)
            print(sim)
            if(not sim):
                print("no hay simbolos")
                #tamcine se puede hacer qeu sea correcto
            else:    
                for item in sim:
                    x=simbolosaceptados.count(item)
                    if(x==0):
                        erroes.append("no")
                    else:
                         print('',end="")
                if(not erroes):
                    print("correcto")
                #aqui la cadena es correcta
                else:
                     messagebox.showerror(message="simbolos incorrecto", title="Aviso")  
        


   
#colocar imagenes a los botones
img = PhotoImage(file='b.png')
img2=PhotoImage(file='c.png')


botonverificar=Button(miframe,text="VERIFICAR",command=extraerautomata,image=img)
botonverificar.place(x=505,y=145)


botonverificar=Button(miframe,text="VERIFICAR CADENA",command=extraercadena,image=img2)
botonverificar.place(x=505,y=375)

#empieza las validaciones del programa
def frecuencia(v):
    res = dict()
    for caracter in v:
        if caracter in res.keys():
            res[caracter] = res[caracter] + 1
        else:
            res[caracter] = 1
    return res












root.mainloop()# siempre va alfinal por la ventana