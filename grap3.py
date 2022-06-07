import turtle
turtle.shapesize(2)
turtle.color("black")
turtle.speed(7)
counter = 0
while counter < 36:
    for i in range(5):
        for colours in["red","blue","orange","green"]:
            turtle.color(colours)
            turtle.forward(100)
            turtle.right(90)
        turtle.right(10)
        counter += 1
a = input()              
turtle.exitonclick()        
        
