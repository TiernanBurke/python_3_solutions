#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tiernan
#
# Created:     28/08/2020
# Copyright:   (c) Tiernan 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.speed(0)
    t.begin_fill()
    t.left(90)
    t.forward(height)

    if height > 0:
        t.write(' ' + str(height))
    else:
        t.penup()
        t.forward(-15)
        t.pendown()
        t.write(' ' + str(height))
        t.penup()
        t.forward(15)
        t.pendown()

    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

wn=turtle.Screen()
luke=turtle.Turtle()
xs = [48, 117, -200, 240, 160, 260, 220,-100]

for v in xs:
    if v >= 200:
        fill_color = 'Red'
    elif v < 200 and v >=100:
        fill_color = 'Yellow'
    elif v < 100:
        fill_color = 'Green'

    luke.color('Black',fill_color)
    draw_bar(luke, v)


wn.mainloop()