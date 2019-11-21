#      Simple line drawing     #

import turtle

my_window = turtle.Screen()     # Create graphic window
my_window.bgcolor('blue')       # Set background colour to blue

my_pen = turtle.Turtle()        # Create turtle object
my_pen.shape('circle')
my_pen.speed(4)
my_pen.forward(150)
my_pen.left(90)
my_pen.forward(75)
my_pen.color('white')
my_pen.pensize(12)

turtle.done()