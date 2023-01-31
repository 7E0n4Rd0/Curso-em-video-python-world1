# "Hello World" in Red color.
"""print('\033[31mHello, World!')"""
# "Hello World" with text in Red and the back is yellow.
'''print('\033[31;43mHello, World!')'''
# "Hello Wolrd" with text in Bold,Red and the back is yellow.
'''print('\033[1;31;43mHello, World!')'''
# Removing the excess of the yellow back.
'''print('\033[1;31;43m Hello, World!\033[m')'''
# "Hello World" with text in Underline, White and the back is violet.
'''print('\033[4;45m Hello, World!\033[m')'''
# "Hello World" in inversion colors.
'''print('\033[7;33;44m Hello, World!\033[m')'''
# Puting colors in variables:
'''a = 3
b = 4
print('The values are \033[32;44m{}\033[m and \033[31;44m{}\033[m'.format(a, b))'''
# Using with .format:
'''name = 'Leonardo'
print('Hello World, nice to meet you {}{}{}'.format('\033[4;34m', name, '\033[m'))'''
# Another way using Dictionary:
name = 'Leonardo'
colors = {'clean': '\033[m',
          'blue': '\033[34m',
          'yellow': '\033[33m',
          'blackandwhite': '\033[7;40m'}
print('Hello World!! Nice to meet you {}{}{}'.format(colors['blackandwhite'], name, colors['clean']))
