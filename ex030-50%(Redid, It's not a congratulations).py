#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
number = int(input('Enter some number here: '))
value = number%2
if value == 0:
    print('This number is pair.')
else:
    print('This number is unpair.')