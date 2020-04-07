import turtle
cadena = "abc"
flechas = []
simbolosJerarquia = ["(", ")"]
simbolosOperaciones =["|", "*"]
for var in range (0, len(cadena)+1):
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
#------------------------------------------------------
def dibujarflecha(letter,flecha):
    arrow = turtle.Turtle()
    #Lo movemos mas adelante ya que se dibuja un circulo y las letras
    arrow.penup()
    arrow.setposition(flecha._position[0]+85, flecha._position[1])
    arrow.pendown()
    if(len(letter) > 1):
        letter = ','.join(letter)#concateno si es a,b
    style = ('Courier', 12, 'italic')
    arrow.write(letter, font=style, align='center')
    arrow.backward(25)
    arrow.forward(60)


flechas[0].penup()
flechas[0].setposition(-450,280)#si no levantamos el lapiz dejara marca
flechas[0].pendown()
flechas[0].forward(60)
dibujarCirculo('q0', True, flechas[0])
dibujarflecha("ab", flechas[0])
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
for var in (arreglo1):
    if type(var) == list or type(var) == tuple:
        print("a is a list")
    else:

        print("procedimiento facil")
    
ventana.exitonclick()

