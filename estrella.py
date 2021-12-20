import turtle #Importamos turtle
turtle.fillcolor("green") #Definimos el color con el que se dibujará la estrella
turtle.begin_fill()  #Empieza el dibujo          
puntas = int(input("Cuantos lados quiere que tenga la estrella? "))  #Preguntamos cuantas puntas quiere que tenga la estrella            
if puntas%2 != 0: #Si el número de puntas es impar
    n = 1 
    giro =  180 - (360/(puntas*2)) 
    while n <= puntas:
        turtle.forward(150) 
        turtle.right(giro) 
        n += 1                  
    turtle.end_fill()  #Se rellena el dibujo trazado
elif puntas%2 == 0: #Si el número de puntas es par
    n = 1
    while n <= puntas:
        turtle.forward(60)
        turtle.left(360/puntas)
        turtle.forward(60)
        turtle.right(720/puntas)
        n += 1  
    turtle.end_fill()  #Se rellena el dibujo trazado