import turtle
cadena = "ab"
flechas = []
for var in range (0, len(cadena)+1):
    var = turtle.Turtle()
    var.hideturtle()#Las escondo como no las estoy utilizando
    flechas.append(var)
    
flechas[0].showturtle()#si quisiera ir mostrandolas
ventana = turtle.Screen()#Instancia
ventana.title("Automata finito no determinista")#Titulo de la ventana
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

flechas[0].penup()
flechas[0].setposition(-450,280)#si no levantamos el lapiz dejara marca
flechas[0].pendown()
flechas[0].forward(30)
dibujarCirculo('q0', True, flechas[0])
flechas[0].forward(60)
dibujarCirculo('q1', True, flechas[0])
ventana.exitonclick()

