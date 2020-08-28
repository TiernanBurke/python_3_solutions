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

def right_angle_tri(x,y,z):
    '''Returns boolean value if a triangle is at a right angle or not'''
    longest_len=max(x,y,z)

    x_squared = x**2
    y_squared = y**2
    z_squared = z**2

    if (x and y) < z:
        hyp = (x_squared + y_squared)**0.5
    elif (z and y) < x:
        hyp = (z_squared + y_squared)**0.5
    elif ( x and z) < y:
        hyp = (x_squared + z_squared)**0.5

    if abs(longest_len - hyp) < 0.000001:
        print(True)
    else:
        print(False)

len_1 = float(input('Enter the first length: '))
len_2 = float(input('Enter the second length: '))
len_3 = float(input('Enter the third length: '))

right_angle_tri(len_1,len_2,len_3)

