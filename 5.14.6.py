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

def grade(i):
    if i > 100:
        print('''That's impossible! Grade must be between 0 and 100''')
    elif i >= 75:
        print('First')
    elif i >= 70:
        print('Upper Second')
    elif i >= 60:
        print('Second')
    elif i >= 50:
        print('Third')
    elif i >= 45:
        print('F1 Supp')
    elif i >= 40:
        print('F2')
    else:
        print('F3')


xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for x in xs:
    grade(x)


