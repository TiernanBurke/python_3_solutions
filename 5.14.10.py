
def find_hypot(adj,opp):
    '''Returns the hypotenuse of a right angled triangle'''
    adj_squared = adj**2
    opp_squared =  opp**2
    hyp = (adj_squared + opp_squared)**0.5
    print(hyp)

adjacent = float(input('Enter the adjacent length here: '))
opposite = float(input('Enter the opposite length here: '))

find_hypot(adjacent,opposite)
