from random import choice
a = input('First Student:')
b = input('Second Student:')
c = input('Third Student:')
d = input('Fourth Student:')
name = choice([a, b, c, d])
print('The student who will erase the board today is {}.'.format(name))
