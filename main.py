#ctrl + k +c (comenta), ctrl + k +u (descomenta)
import turtle
#cadena = "abc(b)*|ba"
cadena = "(c)*|b"
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

    arrow.setposition(flecha._position[0]+60, flecha._position[1])
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
    arrow.left(90)
    arrow.forward(30)
    arrow.pendown()
    if(len(letter) > 1):
        letter = ','.join(letter)#concateno si es a,b
    style = ('Courier', 12, 'italic')
    ########    escribo palabra
    arrow.penup()
    arrow.right(90)
    arrow.forward(35)
    arrow.pendown()
    arrow.write(letter, font=style, align='center')
    arrow.penup()
    arrow.backward(35)
    arrow.right(-90)
    arrow.pendown()
    #########
    arrow.width(2)
    arrow.right(90)#Se posiciona para hacer bien el circulo
    arrow.circle(20)
    #colocando para que se mire bien que regresa a si mismo
    arrow.right(90)
    arrow.penup()
    arrow.forward(5)
    arrow.pendown()
    return arrow
#----------------------------------------------------------------------
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
flechas[0].setposition(-450,270)#si no levantamos el lapiz dejara marca
flechas[0].pendown()
flechas[0].forward(60)
#dibujarCirculo('q0', False, flechas[0])

#Aqui comparamos si el siguiente tiene estrella de kleene
#debemos de hacerlo con todos los valores hijos
bandera = False
extra = 0
for i in (arreglo1):
    #print("valores ", i[0])
    if type(i) == list or type(i) == tuple:
        if(i == arreglo1[0]):
            if(i[len(i)-1] == "*"):
                #print("Es con kleene")
                bandera = True#esto ayudara para ver si es final o no
                #y con uno de los caminos que de si bastara para que sea final
        elif(arreglo1[extra - 1] == "|"):#para evitar"a|b(b)*"
            if(i[len(i)-1] == "*"):#Ya que nos posicionamos una posicion antes
                #print("Es con kleene")#y con eso miramos si hubo |
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
    print(var)
    momentaneo = flechas[valor-1]#tomo de referencia la ultima flecha creada
    momentaneo2 = flechas[valor-1]
    if type(var) == list or type(var) == tuple:
        print("a is a list")
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
    valor += 1
print(arreglo1)
ventana.exitonclick()

