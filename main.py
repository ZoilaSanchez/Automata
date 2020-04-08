#ctrl + k +c (comenta), ctrl + k +u (descomenta)
import turtle
cadena = "ab|abcc"
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
for var in cadena:
    if(var == simbolosJerarquia[0]):
        inicio = True
        arreglo2 = []
    elif(var == simbolosJerarquia[1]):
        inicio = False
        arreglo1.append(arreglo2)
    if(inicio == True and var != "("):
        #print("inserto ", var)
        arreglo2.append(var)
    elif(var != "*" and var != "(" and var != ")"):
        #print("inserto en el otro ",var)
        arreglo1.append(var)
flechas[0].penup()
flechas[0].setposition(-450,270)#si no levantamos el lapiz dejara marca
flechas[0].pendown()
flechas[0].forward(60)
#dibujarCirculo('q0', False, flechas[0])
flechas[0] = dibujarCirculo('q0', False, flechas[0])


#dibujarflechaC("ab", flechas[0])
#algo =dibujarflechaR("ab", flechas[0])
#dibujarCirculo('q1', False, algo)
#dibujarflechaC('c', algo)  
valor = 1
inclinacion = 0
nombre = 1
for var in (arreglo1):
    print(var)
    momentaneo = flechas[valor-1]
    momentaneo2 = flechas[valor-1]
    if type(var) == list or type(var) == tuple:
        print("a is a list")
    else:
        if(arreglo1[valor-1] != "|"):
            momentaneo2 = dibujarflechaR(var,momentaneo,inclinacion)
            cadena = "q" + str(nombre).strip()#concateno sin espacio
            if(valor != len(arreglo1)): #Sirve para cuando es a|b     
                if(valor != len(arreglo1)):
                    if(arreglo1[valor] == "|"):
                        flechas[valor]=dibujarCirculo(cadena, True, momentaneo2)
                    else:
                        flechas[valor]=dibujarCirculo(cadena, False, momentaneo2)
            else:#Aqui detecta si es estado final
                flechas[valor]=dibujarCirculo(cadena, True, momentaneo2)      
            nombre += 1#para el nombre de q y asi
        else:#Me voy al inicio
            inclinacion += 35 #inclino mas la flecha 
            flechas[valor].penup()
            #flechas[valor].setposition(-290,0)
            flechas[valor].setposition(flechas[0]._position[0] - inclinacion/2
            ,flechas[0]._position[1]-inclinacion*9/10)
            flechas[valor].pendown()
            print(flechas[valor - 1]._position[0])
            print("Componer angulo")
    valor += 1
ventana.exitonclick()

