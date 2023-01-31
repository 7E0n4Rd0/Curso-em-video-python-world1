#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
question = float(input('How far will this trip be? (In Km): '))
#Simplify version: value = question * 0.50 if question <= 200 else question * 0.45
if question <= 200:
    print('The cost will be R${}.'.format(question*0.50))
if question > 200:
    print('The cost will be R${}.'.format(question*0.45))