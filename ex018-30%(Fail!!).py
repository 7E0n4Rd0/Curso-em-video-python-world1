'''from math import sin,cos,tan
an = float(input('Enter some value(Angle):'))
print('The angle in Sine is {:.2f}.\nThe angle in Cosine is {:.2f}.\nThe angle in Tangent is {:.2f}'.format(sin(an),cos(an),tan(an)))'''
from math import sin, cos, tan, radians
an = float(input('Enter some value of angle:'))
sin = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('The angle of {} in Sine is {:.2f}\n in Cosine is {:.2f}\n in Tangent is {:.2f}'.format(an, sin, cos, tan))
