#ctrl + k +c (comenta), ctrl + k +u (descomenta)
import turtle
#cadena = "(b)*aa|ba"
#cadena = "acb|(bac)*"
#cadena = "(bac)*ba|abcd"
#cadena = "(ab)*(a)*(ad)*"
#cadena = "(ab)*(a)*"
cadena = "aa(b)*|ba"
flechas = []
simbolosJerarquia = ["(", ")"]
simbolosOperaciones =["|", "*"]
for var in range (0, len(cadena)+2):#Agrego una flecha de mas talvez sirva
    var = turtle.Turtle()
    var.hideturtle()#Las escondo como no las estoy utilizando
    flechas.append(var)
    
flechas[0].showturtle()#si quisiera ir mostrandolas
ventana = turtle.Screen()#Instancia
ventana.title("Automata finito no determinista")#Titulo de la ventana
#-------------------------------------------------------------
def dibujarCirculo(nombre, final, flecha):
    circulo = turtle.Turtle()
    #Me ubicare en donde se había quedado antes el dibujo
    circulo.penup()
    circulo.setposition(flecha._position[0], flecha._position[1])
    circulo.pendown()
    circulo.width(2)#Grosor del contorno
    circulo.right(90)
    if(final == True):#Dibuja si es un estado final
         # Nos posicionaremos un poco adelante del primer circulo
        circulo.penup()
        circulo.right(-90)
        circulo.forward(5)
        circulo.right(90)
        circulo.pendown()
        circulo.circle(25)
        circulo.penup()
        circulo.right(-90)
        circulo.backward(5)
        circulo.right(90)
        circulo.pendown()
    circulo.circle(30)#30 es el radio del circulo
    circulo.left(90)
    circulo.penup()
    circulo.forward(25)
    circulo.pendown()
    style = ('Courier', 12, 'italic')
    circulo.write(nombre, font=style, align='center')
    circulo.hideturtle()
    return circulo
#------------------------------------------------------
def dibujarflechaR(letter,flecha,angulo):#De flecha recta
    arrow = turtle.Turtle()
    #Lo movemos mas adelante ya que se dibuja un circulo y las letras
    arrow.penup()
    
    arrow.right(angulo)

    arrow.setposition(flecha._position[0]+60, flecha._position[1]-10)
    arrow.pendown()
    if(len(letter) > 1):
        letter = ','.join(letter)#concateno si es a,b
    style = ('Courier', 12, 'italic')
    arrow.write(letter, font=style, align='center')
    arrow.backward(25)
    arrow.forward(60)
    return arrow
#----------------------------------------------------------
def dibujarflechaC(letter,flecha):#De flecha circular
    arrow = turtle.Turtle()
    #Lo movemos mas adelante ya que se dibuja un circulo y las letras
    arrow.penup()
    arrow.setposition(flecha._position[0]+30, flecha._position[1])
    arrow.right(25)
    arrow.forward(40)
    arrow.pendown()
    if(len(letter) > 1):
        letter = ','.join(letter)#concateno si es a,b
    style = ('Courier', 12, 'italic')
    ########    escribo palabra
    arrow.penup()
    arrow.right(90)
    arrow.forward(40)
    arrow.pendown()
    arrow.write(letter, font=style, align='center')
    arrow.penup()
    arrow.backward(30)
    arrow.right(-90)
    arrow.pendown()
    #########
    arrow.width(2)
    arrow.right(90)#Se posiciona para hacer bien el circulo
    arrow.circle(15)
    #colocando para que se mire bien que regresa a si mismo
    arrow.right(45)
    arrow.penup()
    arrow.forward(5)
    arrow.pendown()
    return arrow
#----------------------------------------------------------------------
def flechaCurveada(letter,flecha1, flecha2, inclinacion):#De flecha circular para kleen
    arrow = turtle.Turtle()
    #Lo movemos mas adelante ya que se dibuja un circulo y las letras
    arrow.penup()
    arrow.setposition(flecha1._position[0]-10, flecha1._position[1]+15)
    arrow.pendown()
    #recorrido = int(flecha1._position[0]-25) - int(flecha2._position[0]
    recorrido = flecha1._position[0]-25 - flecha2._position[0]
    recorrido = recorrido * 12/11 #Para que alcanze la linea
    recorrido = int(recorrido)

    #Escribo el nombre
    arrow.penup()
    arrow.left(90)
    arrow.forward(20)
    arrow.left(270)

    arrow.backward(recorrido/(inclinacion*1.6))
    arrow.pendown
    style = ('Courier', 12, 'italic')
    arrow.write(letter, font=style, align='center')
    arrow.penup()

    arrow.left(90)
    arrow.forward(-20)
    arrow.left(270)

    arrow.forward(recorrido/(inclinacion*1.6))
    arrow.pendown()

    inclinacion = inclinacion * 3/4
    arrow.left(-30*inclinacion)
    #arrow.left(-30)
    for i in range(0, recorrido):
        arrow.forward(-1)  
        arrow.left(0.4)
    arrow.right(180)
    # for i in range(0, int(recorrido/2)):
    #     arrow.forward(-1)  
    #     arrow.left(1)
    #print(flecha1._position[0])
    #print(flecha1._position[1])
    #print(flecha2._position[0])
#---------------------------------

arreglo1 = []
final = False
inicio = False
#Con esto se cuantas concatenaciones debo hacer en total
aux = 1 #Sirve para saber una posicion adelante
for var in cadena:
    if(var == simbolosJerarquia[0]):
        inicio = True
        arreglo2 = []
    elif(var == simbolosJerarquia[1]):
        inicio = False
        arreglo1.append(arreglo2)
    if(inicio == True and var != "("):
        #print("inserto ", var, aux+1)
        arreglo2.append(var)
        #"a|b(a)*" inserto * en los arreglos
        if(aux != len(cadena)):
            if(cadena[aux+1] == "*"):
                arreglo2.append(cadena[aux+1])#me muevo para saltar parentesis
                #print("hasta esta posicion llego", cadena[aux+1]) 
    elif(var != "*" and var != "(" and var != ")"):
        #print("inserto en el otro ",var)
        arreglo1.append(var)
    aux += 1
flechas[0].penup()
flechas[0].setposition(-450,280)#si no levantamos el lapiz dejara marca
flechas[0].pendown()
flechas[0].forward(60)
#dibujarCirculo('q0', False, flechas[0])

#Aqui comparamos si el siguiente tiene estrella de kleene
#debemos de hacerlo con todos los valores hijos
bandera = False
extra = 0
print("cantidad ", arreglo1)
for i in (arreglo1):
    #print("valores ", i[0])
    if type(i) == list or type(i) == tuple:
        if(len(arreglo1) == 1): #Si solo es uno con kleene
            if(i[len(i)-1] == "*"):
                bandera = True
        elif(i == arreglo1[0] and arreglo1[extra+1] == "|"):# para evitar problemas con eso cadena = "(b)*aa|ba"
            if(i[len(i)-1] == "*"):
                #print("Es con kleene")
                bandera = True#esto ayudara para ver si es final o no
                #y con uno de los caminos que de si bastara para que sea final
        elif(arreglo1[extra - 1] == "|" or arreglo1[extra] == "|"):#para evitar"a|b(b)*"
            if(i[len(i)-1] == "*"):#Ya que nos posicionamos una posicion antes
                #print("Es con kleene")#y con eso miramos si hubo |
                bandera = True
        else:
            ban = False
            for i in range (0, len(arreglo1)):
                if(i + 1 != len(arreglo1)):
                    if(arreglo1[i+1][len(arreglo1[i+1])-1] != "*"):
                        ban = True
                if(ban == True):
                    break
            if(ban == True):
                bandera = False
            else:
                bandera = True        
    extra += 1
flechas[0] = dibujarCirculo('q0', bandera, flechas[0])

#dibujarflechaC("ab", flechas[0])
#algo =dibujarflechaR("ab", flechas[0])
#dibujarCirculo('q1', False, algo)
#dibujarflechaC('c', algo)  
valor = 1
inclinacion = 0
nombre = 1
for var in (arreglo1):
    #print(var)
    momentaneo = flechas[valor-1]#tomo de referencia la ultima flecha creada
    momentaneo2 = flechas[valor-1]
    if type(var) == list or type(var) == tuple:
        flechasExtras = []
        for f in range (0, len(var)+2):#Agrego una flecha de mas talvez sirva
            f = turtle.Turtle()
            f.hideturtle()#Las escondo como no las estoy utilizando
            flechasExtras.append(f)
        valor2 = 1
        flechasExtras[valor2 - 1] = flechas[valor-1]#Inicio mi primera flecha en la ultima creada
        if(var[len(var) - 1] == "*"):
            for i in (var):#Aqui recorremos cada sub arreglo
                momentaneo = flechasExtras[valor2-1]#tomo de referencia la ultima flecha creada
                momentaneo2 = flechasExtras[valor2-1]
                if(i != "*"):
                    momentaneo2 = dibujarflechaR(i,momentaneo,inclinacion)
                    cadena = "q" + str(nombre).strip()#concateno sin espacio
                    print("valor ", i, valor2,"a comparar", len(var)-1)
                    if(valor2 != len(var) - 1):#le restamos el asterisco
                        flechasExtras[valor2]=dibujarCirculo(cadena, False, momentaneo2)
                    else:
                        flechasExtras[valor2]=dibujarCirculo(cadena, True, momentaneo2)
                    if(len(var) == 2):#Dibujamos si regresa a si mismo
                        dibujarflechaC(var[0],momentaneo2)
                    elif(valor2 + 1 == len(var)):#por el asterisco sumo 1
                        #print("debo llamar a curvear")
                        print("esta letro debo enviar ", var[0])
                        flechaCurveada(var[0],flechasExtras[valor2], flechasExtras[1], valor2-1)
                        #Mando la flecha ultima y a la primera
                    nombre += 1
                    valor2 += 1
            flechas[valor] = flechasExtras[valor2-1]#sincronizo flechas
        else:
            print("Procedimiento diferente")
    else:
        if(arreglo1[valor-1] != "|"):
            momentaneo2 = dibujarflechaR(var,momentaneo,inclinacion)
            cadena = "q" + str(nombre).strip()#concateno sin espacio
            if(valor != len(arreglo1)): #Sirve para cuando es a|b  
                if(arreglo1[valor] == "|"):
                    flechas[valor]=dibujarCirculo(cadena, True, momentaneo2)
                elif(type(arreglo1[valor]) == list or type(arreglo1[valor]) == tuple):#Aqui abajo añadimos la condicion kleene
                    print("Existe una lista", arreglo1[valor])
                    if(arreglo1[valor][len(arreglo1[valor])-1] == "*"):
                        print("el siguiente es kleene")
                        flechas[valor]=dibujarCirculo(cadena, True, momentaneo2)
                    #flechas[valor]=dibujarCirculo(cadena, True, momentaneo2)
                else:
                    flechas[valor]=dibujarCirculo(cadena, False, momentaneo2)
            else:#Aqui detecta si es estado final
                flechas[valor]=dibujarCirculo(cadena, True, momentaneo2)      
            nombre += 1#para el nombre de q y asi
        else:#Me voy al inicio aqui surgen otros caminos
            inclinacion += 35 #inclino mas la flecha 
            flechas[valor].penup()
            flechas[valor].setposition(flechas[0]._position[0] - inclinacion/2
            ,flechas[0]._position[1]-inclinacion*9/10)
            flechas[valor].pendown()
            #print("Componer angulo")
    valor += 1 #Sumo las flechas normales
print(arreglo1)
ventana.exitonclick()

