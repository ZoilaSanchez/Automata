from tkinter import*
from tkinter import messagebox
from tkinter import messagebox as MessageBox
import ctypes
import re
import turtle
from main import dibujarAutomata

#configurar la pantalla del programa de acuerdo a la compu
#user32 = ctypes.windll.user32
#user32.SetProcessDPIAware()
#ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
ancho= 400
alto=700
resul=str(ancho)+"x"+str(alto)

#configurar root que seria la ventana en si
root=Tk()
root.config(bg="white")
root.geometry(resul+"+0+40")
#root.geometry("650x700+0+0")
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

lenguaje=Label(miframe,text="Lenguaje: ")
lenguaje.place(x=50,y=550)
lenguaje.config(fg="Green Yellow",bg="Black")#cambiar el color

##Generar cuadros de texto
automatatxt=Text(miframe,width=20 ,height=6)#poscion del dibujo # esto me ayuda a extraer el lengueja
automatatxt.place(x=70,y=120)
automatatxt.config(fg="blue",bg="white")

comcadena=Text(miframe,width=20,height=6)#poscion del dibujo# esto lo introducira andrea 
comcadena.place(x=70,y=350)
comcadena.config(fg="blue",bg="white")

#Estas con las variable a utilizar
lenguaje=[]
validacion_texto_vacio=""
cadenita=""
automata = dibujarAutomata("")
#validación de la cadena
def validarcadena(El_automata,La_cadena):
    cad=""
    the_string=""
    the_automat=""
    incorrecta="jaja"
  #  La_cadena = comcadena.get("1.0","end-1c")
  #  El_automata = automatatxt.get("1.0","end-1c")
    arrcadena=[]
    arrautomata=[]
    
    
    for caracter in La_cadena:
        arrcadena.append(caracter)


    for caracter in El_automata:
        arrautomata.append(caracter)
    
    for x in range(0,len(arrautomata)):
   
        signo=arrautomata[x]

        if signo=="(":
            signo=arrautomata[x+1]
            print("encontro un (")   
            cad=""          
        else:
            if signo=="*":
                cont=0
                tt=1                
                print("encontro un ", signo)
                cad_a_comparar=cad  
                cad=""  
                print("CADENA", arrcadena)
                for y in range(0,len(arrcadena)):
                    if cont<len(cad_a_comparar):
                        the_string=the_string+arrcadena[y]
                        print("the_string"," " ,the_string)
                        cont=cont+1
                    elif cont==len(cad_a_comparar):
                      
                        if the_string==cad_a_comparar:
                            print("si son inguales",the_string)
                            the_string=""
                            cont=0
                            the_string=the_string+arrcadena[y]
                            cont=cont+1
                            print("veamos acá")           
                        else: 
                            the_string=the_string+arrcadena[y]
                            cont=cont+1
                            print("acá no son iguales")

                    elif cont>len(cad_a_comparar):
                        the_string=the_string+arrcadena[y]
                        cont=cont+1
                        print("cadena sobrante", the_string)
                     
                print("cont",cont)
                print("tam",len(arrcadena))

                if the_string!=cad_a_comparar:
                    arrcadena=[]
                    for caracter in the_string:
                        arrcadena.append(caracter)
                    print("cad modificada",arrcadena)
                    incorrecta="true"
                    print("incorrecta",incorrecta)
               # else:
               #     arrcadena=[]
               #     print("CADENA CORRECTA")
                #print("signo", signo)
                #print("cadena", cad)
                #signo=arrautomata[x+1]
                #cad=cad+signo
                print("CAD ",cad)
                print("****incorrecta", incorrecta)
            elif signo=="|":
                cont=0
                cad_encontrada=""
                the_string=""
                cad_a_comparar=cad  
                print("veamos como inicia",cad_a_comparar)
                cad=""  
                print("encontro un ", signo)
                print("veamos si cambio el arrcad ", arrcadena)
                for y in range(0,len(arrcadena)):
                   # print("letra ", arrcadena[y])
                    print("entra",y,"veces")
                    if cont<len(cad_a_comparar):
                        the_string=the_string+arrcadena[y]
                        print("the_string"," " ,the_string)
                        cont=cont+1
                        cad_encontrada=cad_encontrada+arrcadena[y]
                    elif cont==len(cad_a_comparar):
                        #if the_string!=cad_a_comparar:
                        #    incorrecta="true"
                        #    the_string=""
                        #    the_string=the_string+arrcadena[y]
                        #    cont=cont+1
                        #    print("entra acá")
                            #cadena invalida                       
                        #else:
                            #cadena valida
                        print("aqui si entra")
                        if len(arrcadena)==len(cad_a_comparar):
                            incorrecta="false"
                            print("tienen el mismo tamaño")
                        else:
                            print("no tienen el mismo tamaño")
                            the_string=""
                            the_string=the_string+arrcadena[y]
                            cont=cont+1
                            incorrecta="true"

                    elif cont>len(cad_a_comparar):
                        print("se va para acá")
                        #cadena invalida     
                        print("AQUI AQUI")                   
                        the_string=the_string+arrcadena[y]
                        cont=cont+1

                print("veamos el tamaño de arrcadena",len(arrcadena))
                if cont==len(cad_a_comparar):
                    print("aqui si entra")
                    if len(arrcadena)==len(cad_a_comparar):
                        if cad_encontrada==cad_a_comparar:
                            incorrecta="false"
                            print("tienen el mismo tamaño y es igual")
                            the_string=""
                        else:
                            incorrecta="true"
                    elif len(arrcadena)>len(cad_a_comparar):
                        if cad_encontrada==cad_a_comparar:
                            arrcadena=[]
                            for caracter in the_string:
                                arrcadena.append(caracter)
                            print("cad modificada",arrcadena)
                            incorrecta="false"
                            print("incorrecta",incorrecta)
                            the_string=""
                        else:
                            incorrecta="true"
                    else:
                        arrcadena=[]
                        for caracter in the_string:
                            arrcadena.append(caracter)
                        print("cad modificada",arrcadena)
                        incorrecta="true"
                        print("incorrecta",incorrecta)
                        the_string=""

                print("incorrecta",incorrecta)        
               # if incorrecta=="true":
               #     arrcadena=[]
               # else:
               #     arrcadena=[]
               #     print("String despues de hallar la cadena",the_string)
               #     for caracter in the_string:
               #         arrcadena.append(caracter)

               #    print("cad modificada",arrcadena)
               #    print("CADENA CORRECTA")

            elif signo=="]":
                print("encontro un ", signo) 
                cont=0
                cad_encontrada=""
                the_string=""
                cad_a_comparar=cad  
                print("veamos como inicia",cad_a_comparar)
                cad=""  
                print("encontro un ", signo)
                print("veamos si cambio el arrcad ", arrcadena)
                for y in range(0,len(arrcadena)):
                   # print("letra ", arrcadena[y])
                    print("entra",y,"veces")
                    if cont<len(cad_a_comparar):
                        the_string=the_string+arrcadena[y]
                        print("the_string"," " ,the_string)
                        cont=cont+1
                        cad_encontrada=cad_encontrada+arrcadena[y]
                    elif cont==len(cad_a_comparar):
                        #if the_string!=cad_a_comparar:
                        #    incorrecta="true"
                        #    the_string=""
                        #    the_string=the_string+arrcadena[y]
                        #    cont=cont+1
                        #    print("entra acá")
                            #cadena invalida                       
                        #else:
                            #cadena valida
                        print("aqui si entra")
                        incorrecta="false"
                        print("no tienen el mismo tamaño")
                        the_string=""
                        the_string=the_string+arrcadena[y]
                        print("k pex en esta linea", the_string)
                        cont=cont+1

                    elif cont>len(cad_a_comparar):
                        print("se va para acá")
                        #cadena invalida     
                        print("AQUI AQUI")                   
                        the_string=the_string+arrcadena[y]
                        cont=cont+1

                print("veamos el tamaño de arrcadena",len(arrcadena))
                if len(arrcadena)>len(cad_a_comparar):
                    if cad_encontrada==cad_a_comparar:
                        arrcadena=[]
                        for caracter in the_string:
                            arrcadena.append(caracter)
                        print("cad modificada",arrcadena)
                        incorrecta="false"
                        print("incorrecta",incorrecta)
                        the_string=""
                    else:
                        incorrecta="true"
                else:
                    arrcadena=[]
                    for caracter in the_string:
                        arrcadena.append(caracter)
                    print("cad modificada",arrcadena)
                    incorrecta="true"
                    print("incorrecta",incorrecta)
                    the_string=""

                print("incorrecta",incorrecta)                      
            elif signo==")":
                signo=arrautomata[x+1]
            else:
                cad=cad+signo  
               # for y in range(0,len(arrcadena)):
               #     print("ARRCADENA",arrcadena[y])    
                print("imprime cad")     
                print (cad) 
    return incorrecta
def inicio_de_validacion():
    #La_cadena_i="abc"#llamar a los valores que ingresa el usuario 
    #El_automata_i="aa(b)*|abc|"#llamar a los valores que ingresa el usuario 
    La_cadena_i = comcadena.get("1.0","end-1c")
    El_automata_i = automatatxt.get("1.0","end-1c")
    arrautomata=[]
    cont_arraut=""
    autaux=""
    sobra=""
    incorrect="true"

    for caracter in El_automata_i:
        arrautomata.append(caracter)


    for x in range(0,len(arrautomata)):
        signo=arrautomata[x]

        if signo=="(" and x==0:
            if x<len(arrautomata):
                cont_arraut=cont_arraut+signo
                singo=arrautomata[x+1]
        elif arrautomata[x-1]!="*" and signo=="(":
            if arrautomata[x-1]!="|":
                if x<len(arrautomata):
                    cont_arraut=cont_arraut+("]")
                    cont_arraut=cont_arraut+singo
                    singo=arrautomata[x+1]

        elif signo=="|":
            if incorrect=="true":
                if arrautomata[x-1]=="*":
                    print("cadena", cont_arraut)
                    #llamar  a la función que
                    incorrect=validarcadena(cont_arraut,La_cadena_i)
                    if incorrect=="true":
                        cont_arraut=""
                else:
                    cont_arraut=cont_arraut+signo
                    print ("la cadena", cont_arraut)
                    incorrect=validarcadena(cont_arraut,La_cadena_i)
                    if incorrect=="true":
                        cont_arraut=""
            else:
                if x<len(arrautomata)-1:
                    signo=arrautomata[x+1]
                #llamar a validación
            
        else:
      
            if x<len(arrautomata)-1:
                cont_arraut=cont_arraut+signo
                singo=arrautomata[x+1]  
            elif x==len(arrautomata)-1:
                cont_arraut=cont_arraut+signo

    if incorrect=="false":
        MessageBox.showinfo("", "¡ La cadena ingresada es valida !")
    elif incorrect=="true":
        MessageBox.showinfo("", "¡ La cadena ingresada NO es valida !")
    print(cont_arraut)
    print("AQUI AQUI AQUI",incorrect)
    print(cont_arraut)
   
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
            print("comosdsf ")     
            print(mostrarlen)   
            lengu = " ".join(mostrarlen)
            print(lengu)
            for z in mostrarlen:
                copia.remove(z)
            #print(copia)
            for item in copia:
                sim.append(item)
            #print(sim)
            if(not sim):
                print("no hay simbolos")
                
                lenguaje=Label(miframe,text=lengu.upper())
                lenguaje.place(x=100,y=600)
                lenguaje.config(fg="Green Yellow",bg="Black",font=("comic",24))#cambiar el color
                #messagebox.showwarning(message="No hay simbolosdfjskf", title="Aviso")
                #tamcine se puede hacer qeu sea correcto
                automata.cambiarLetra(auto)
                automata.crear()
                
                
            else:    
                for item in sim:
                    x=simbolosaceptados.count(item)
                    if(x==0):
                        erroes.append("no")
                    else:
                         print('',end="")
                if(not erroes):
                #aqui la cadena es correcta
                    lenguaje=Label(miframe,text=lengu.upper())
                    lenguaje.place(x=100,y=600)
                    lenguaje.config(fg="Green Yellow",bg="Black",font=("comic",24))#cambiar el color
                    automata.cambiarLetra(auto)
                    automata.crear()
                   
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
botonverificar.place(x=250,y=145)


botonverificar=Button(miframe,text="VERIFICAR CADENA",command=inicio_de_validacion,image=img2)
botonverificar.place(x=250,y=375)

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