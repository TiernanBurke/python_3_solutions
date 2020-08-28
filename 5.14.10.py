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

def find_hypot(adj,opp):
    '''Returns the hypotenuse of a right angled triangle'''
    adj_squared = adj**2
    opp_squared =  opp**2
    hyp = (adj_squared + opp_squared)**0.5
    print(hyp)

adjacent = float(input('Enter the adjacent length here: '))
opposite = float(input('Enter the opposite length here: '))

find_hypot(adjacent,opposite)
