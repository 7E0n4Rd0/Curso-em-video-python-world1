#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from calendar import isleap
from datetime import date
year = int(input('Enter some year here to analyze or Put 0 to analyze the actual year: '))
'''sleap = isleap(year)
if sleap:
    print('The year {} is sleap'.format(year))
else:
    print("The year {} isn't sleap.".format(year))'''
#the code on above is what I typed.
#another way to do this. My code was right!!
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('The year {} is sleap.'.format(year))
else:
    print('The year {} is not sleap'.format(year))
