import turtle 
turtle.fillcolor("green") 
turtle.begin_fill()             
puntas = int(input("Cuantos lados quiere que tenga la estrella? "))                   
if puntas%2 != 0:
    n = 1 
    giro =  180 - (360/(puntas*2)) 
    while n <= puntas:
        turtle.forward(150) 
        turtle.right(giro) 
        n += 1                  
    turtle.end_fill()  
if puntas%2 == 0:
    n = 1
    while n <= puntas:
        turtle.forward(60)
        turtle.left(360/puntas)
        turtle.forward(60)
        turtle.right((360*2/puntas))
        n += 1  
    turtle.end_fill()  