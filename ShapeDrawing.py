#       Shape drawing       #

import turtle

def drawSquare():
    window = turtle.Screen()

    pen = turtle.Turtle()
    pen.begin_fill()
    pen.color('lime')

    for x in range(4):
        pen.forward(90)
        pen.left(90)

    pen.end_fill()
    turtle.done()

def drawPolygon(sides, perim):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.width(5)
    
    colours = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'brown', 'magenta']

    for x in range(sides):
        pen.color(colours[x%8])
        pen.forward(perim / sides)
        pen.left(360 / sides)

    turtle.done()

def drawMandala():
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.width(4)
    pen.speed(7)

    colours = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'magenta']
    x = 1

    while True:
        pen.color(colours[x%7])
        x += 1
        pen.forward(150)
        pen.right(107)

drawPolygon(13, 900)