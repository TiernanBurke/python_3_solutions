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

def number_to_day(i):
  if i>6 or i<0:
    print('That number is out of the range!')

  else:
      if i == 0:
        print('''That's Sunday!''')

      elif i == 1:
        print('''That's Monday!''')

      elif i == 2:
        print('''That's Tuesday!''')

      elif i == 3:
        print('''That's Wednesday!''')

      elif i == 4:
        print('''That's Thursday!''')

      elif i == 5:
        print('''That's Friday!''')

      elif i == 6:
        print('''That's Saturday!''')


starting_day_number = int(input('Enter the starting day number: '))
length_stay = int(input('Enter the length of your stay: '))

length_stay = length_stay%7
resultant = (length_stay + starting_day_number)%7

number_to_day(resultant)

