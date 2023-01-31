#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''a = float(input('Enter the value for the right straight of the triangle: '))
b = float(input('Enter some value for the left straight of the triangle: '))
c = float(input('Enter some value for the base of the triangle: '))
if a <= b <= c or a >= b >= c:
    x = a
if b <= a <= c or b >= a >= c:
    y = b
if c <= b <= a or c >= b >= a:
    z = c'''
#Bro, this is to hard to me, I really don't know how to do. Sorry for my self, I couldn't do!
# The Correct was:
a = float(input('First segment: '))
b = float(input('Second segment: '))
c = float(input('Third segment: '))
if a < b + c and b < a + c and c < a + b:
    print('The segments CAN form a Triangle.')
else:
    print('The segments CANNOT for a Triangle.')
#I can't believe, it was necessary to learn a math rule. Anyway, I'm learning and somethings like that happens.
# need to prepare and learn more to do the test.