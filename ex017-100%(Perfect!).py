import math
Co = float(input('Enter the value of the opposite side(Co):'))
Ca = float(input('Enter the value of the adjacent side(Ca):'))
'''b = Co**2
c = Ca**2
x = b+c
H = sqrt(x)'''
H = math.hypot(Co, Ca)
print('The Hypotenuse value is {:.2f}'.format(H))
