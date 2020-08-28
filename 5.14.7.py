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

def draw_bar(t, height, fill_color):

    """ Get turtle t to draw one bar, of height. """
    t.speed(0)
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.write(' ' + str(height))
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
xs = [48, 117, 200, 240, 160, 260, 220]


luke.color('Black',fill_color)

for v in xs:

    if height >= 200:
        fill_color = 'Red'
    elif height < 200 and >=100:
        fill_color = 'Yellow'
    elif height < 100:
        fill_color = 'Green'

    draw_bar(luke, v)


wn.mainloop()