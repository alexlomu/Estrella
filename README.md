# Estrella
Mi dirección de GitHub para este repositorio es: [GitHub](https://github.com/alexlomu/Estrella)
https://github.com/alexlomu/Estrella
Para esta entrega hemos tenido que hacer un programa que dibujará usando turtle, una estrella del número de puntas que se introduzca.
El diagrama de flujo es el siguiente:![figma](https://user-images.githubusercontent.com/91721507/146833611-f7152f67-9a52-41ad-9033-c30b49816b9c.PNG)
El código es el siguiente:
´´´
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
´´´
