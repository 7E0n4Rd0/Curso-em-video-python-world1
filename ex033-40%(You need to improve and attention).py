# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# I droped, althought this exercise can be easy for some one, but it's hard to me.
"""number_1 = int(input('Enter the first number:'))        """
'''number_2 = int(input('Enter the second number:'))       '''
'''number_3 = int(input('Enter the third number:'))        '''
'''if number_1 > number_2 > number_3:                      '''
'''  print('The first number is the higher.')              '''
'''if number_2 > number_3 > number_1:                      '''
'''  print('The second number is the higher.')             '''
'''if number_3 > number_2 > number_1:                      '''
'''  print('The third number is the higher.')              '''
# The way I did was kinda right, the problem was I didn't know what was going on to my commands doing wrong. Anyway,
#I tried my best, and it's normal sometimes you can't do something or doing wrong.
# The correct is:
number1 = int(input('Enter the 1º number: '))
number2 = int(input('Enter the 2º number: '))
number3 = int(input('Enter the 3º number: '))
higher = number1
if number2 > number1 and number3:
    higher = number2
if number3 > number2 and number1:
    higher = number3
lower = number1
if number2 < number1 and number3:
    lower = number2
if number3 < number2 and number1:
    lower = number3
print('The number {} is the highest.'.format(higher))
print('The number {} is the lowest.'.format(lower))
#probaly I did't get a good score because I'm tired, I'll try to do the last exercises tomorrow.